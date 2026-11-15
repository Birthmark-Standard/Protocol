"""The link-level tracer (C4 item 5) and the Registry Node vantage (item 6).

The tracer is a global passive observer. It sees every link event: send and arrival times, endpoints, and a
size that tells only the padding class. It knows the protocol and every hold distribution.

Association at a relay. At node X the relay-class arrivals (from an external host, or from another node) are
matched to X's relay-class departures to other nodes. Legs to and from the validator are known by their
endpoint and left out. An arrival from an external host is at its first relay and must leave again; an arrival
from a node is either at its second relay (and leaves) or at its destination (and stays). A departure releases
on X's 10-second tick grid, whose phase the tracer reads from X's own departures. Pairing arrival i with
departure d is possible when d lies on the grid at or after the first tick after i, within the cap; its weight
is the geometric hold probability of the k ticks it waited, with the mean of i's position (60 s at a first relay,
300 s at a second). Under one release probability every complete pairing of a node's packets has the same
likelihood, because the sum of the ticks waited is fixed by the times; the weights differ only between the two
positions and through the cap.

The tracer does not pick one pairing. It wants each packet's probability of leaving on each departure: the
share, by weight, of the complete pairings that use that pair. Counting complete pairings exactly is a
permanent, so it uses the standard approximation of matrix scaling (Sinkhorn): the weight matrix, with a
"stays here" column for arrivals from nodes, is scaled until every departure is used once and every arrival
once. The probability that an arrival from a node stays here is set from its own upstream: an arrival whose
upstream departure carried a first-relay packet is at its second relay, and one whose upstream departure
carried a second-relay packet is at its destination. The two are refined in turn over all nodes. On small
cases the result is checked against exact enumeration (brute_force).

Tracing a device packet: its first relay's departures, then the second relay's departures, give a mixture over
arrivals at destination nodes (Z_m at time a_m, weight w_km). The packet is a credential packet with probability
1/3 and a content packet with probability 2/3, which the tracer cannot tell apart. As a credential packet its
record follows its arrival at C by the density p_C. As a content packet, its destination submits it to the
registry in one of the submission frames the tracer sees leave that node (the origin floods every peer at once,
so the origin is on the wire), after the density q; and the record follows that frame by the density p_R:
  score(r, k) = log sum_m w_km [ 1/3 p_C(u_r - a_m) + 2/3 sum_f q(t_f - a_m) p_R(u_r - t_f) ],
over the frames f that left Z_m. Devices are named as the observer names them.

Registry Node. A Registry Node reads each registry submission, so it knows which nodes submitted each record as
F and I, and when. For record r it scores packet k by its traced arrivals at those two nodes: log sum over m
with Z_m in {F_r, I_r} of w_km q(s_Z - a_m), with q the density of a submission after its content arrival.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy import sparse

from . import attacks as AT
from . import lottery as LT
from . import params as P
from . import sim as S

M_MAX = 200         # traced destination arrivals kept per device packet
W_MIN = 1e-6        # smaller path weights are dropped
ITER = 60           # Sinkhorn iterations per pass
PASSES = 3          # passes over every node, refining the stay-here probabilities


def _hold_table(mean):
    """Probability of releasing at the k-th tick (k = 1 .. K) for a hold of this mean."""
    p, K = LT.stage_lottery(mean)
    k = np.arange(1, K + 1)
    pk = p * (1 - p) ** (k - 1)
    pk[-1] = (1 - p) ** (K - 1)
    return pk


def relay_events(run):
    """Relay-class legs between pool nodes and from external hosts, with the validator's legs left out."""
    ev = run.events
    lo, hi = P.PAD_MIN + P.TLS13_OVERHEAD, P.PAD_MAX + P.TLS13_OVERHEAD
    rel = (ev["rtype"] == P.RT_APPDATA) & (ev["size"] >= lo) & (ev["size"] <= hi)
    rel &= (ev["dst"] < P.N_NODES) & ((ev["src"] < P.N_NODES) | (ev["src"] == S.EXT))
    return np.nonzero(rel)[0]


def node_phase(ts):
    """A node's tick phase from its departures: each sits 0.5 to 3 ms after a tick."""
    x = np.mod(ts - 0.00175, P.TICK_S)
    c = np.angle(np.mean(np.exp(2j * np.pi * x / P.TICK_S))) * P.TICK_S / (2 * np.pi)
    return np.mod(c, P.TICK_S)


def _ragged(a, b):
    """Row index and position for every j in [a_i, b_i)."""
    n = np.maximum(b - a, 0)
    rows = np.repeat(np.arange(a.size), n)
    pos = np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n) + np.repeat(a, n)
    return rows, pos


class Node:
    """One node's association problem: rows are its relay-class arrivals, columns its departures to nodes."""

    def __init__(self, X, arr_idx, dep_idx, ev, cfg):
        self.X, self.ai, self.di = X, arr_idx, dep_idx
        ta, ts = ev["t_arr"][arr_idx], ev["t_send"][dep_idx]
        first = ev["src"][arr_idx] == S.EXT
        self.first = first
        nr, nc = arr_idx.size, dep_idx.size
        R_, C_, V_ = [np.zeros(0, np.int64)], [np.zeros(0, np.int64)], [np.zeros(0)]
        ph = node_phase(ts) if nc else 0.0
        for pos_, mean in ((True, cfg.relay1_mean), (False, cfg.relay2_mean)):
            sel = np.nonzero(first == pos_)[0]
            if sel.size == 0 or nc == 0:
                continue
            if mean <= 0:
                a = np.searchsorted(ts, ta[sel] + 0.0004)
                b = np.searchsorted(ts, ta[sel] + 0.0031, "right")
                r, c = _ragged(a, b)
                R_.append(sel[r]); C_.append(c); V_.append(np.ones(c.size))
                continue
            pk = _hold_table(mean)
            K = pk.size
            t1 = LT.next_tick(ta[sel], ph)
            a = np.searchsorted(ts, t1 - 0.001)
            b = np.searchsorted(ts, t1 + P.TICK_S * (K - 1) + 0.0045, "right")
            r, c = _ragged(a, b)
            d = ts[c] - t1[r]
            k = np.rint((d - 0.00175) / P.TICK_S).astype(int) + 1
            on = (np.abs(d - P.TICK_S * (k - 1) - 0.00175) < 0.0025) & (k >= 1) & (k <= K)
            R_.append(sel[r[on]]); C_.append(c[on]); V_.append(pk[k[on] - 1])
        self.W = sparse.csr_matrix((np.concatenate(V_), (np.concatenate(R_), np.concatenate(C_))), shape=(nr, nc))
        self.stay_prior = np.where(first, 0.0, 0.5)

    def solve(self):
        """Sinkhorn scaling with a stay-here column; returns (pairing marginals, stay marginals)."""
        W = self.W
        nr, nc = W.shape
        rowmax = W.max(axis=1).toarray().ravel() if nc else np.zeros(nr)
        stay = np.where(self.first, 0.0, self.stay_prior / np.maximum(1 - self.stay_prior, 1e-12))
        stay = stay * np.where(rowmax > 0, rowmax, 1.0)          # a stay weight on the scale of a pairing weight
        r = np.ones(nr)
        c = np.ones(nc)
        Wt = W.T.tocsr()
        for _ in range(ITER):
            colsum = Wt @ r
            c = np.where(colsum > 0, 1.0 / np.maximum(colsum, 1e-300), 0.0)
            rowsum = W @ c + stay
            r = np.where(rowsum > 0, 1.0 / np.maximum(rowsum, 1e-300), 0.0)
        X = sparse.diags(r) @ W @ sparse.diags(c)
        return X.tocsr(), r * stay


def build(run):
    """Every node's association, with stay-here probabilities refined over PASSES passes. Returns the nodes,
    their solutions, and the global indexing: every relay event's row at its receiving node and column at its
    sending node."""
    ev, cfg = run.events, run.cfg
    idx = relay_events(run)
    nodes = {}
    for X in range(P.N_NODES):
        arr = idx[ev["dst"][idx] == X]
        dep = idx[(ev["src"][idx] == X)]
        arr = arr[np.argsort(ev["t_arr"][arr], kind="stable")]
        dep = dep[np.argsort(ev["t_send"][dep], kind="stable")]
        nodes[X] = Node(X, arr, dep, ev, cfg)
    n_ev = ev["t_send"].shape[0]
    row_node, row_i = np.full(n_ev, -1), np.full(n_ev, -1)
    col_node, col_j = np.full(n_ev, -1), np.full(n_ev, -1)
    for X, nd in nodes.items():
        row_node[nd.ai], row_i[nd.ai] = X, np.arange(nd.ai.size)
        col_node[nd.di], col_j[nd.di] = X, np.arange(nd.di.size)
    sol = {}
    for _ in range(PASSES):
        for X, nd in nodes.items():
            sol[X] = nd.solve()
        # an arrival from a node stays (is at its destination) when its upstream departure carried a packet that
        # was itself at its second relay there
        share = np.full(n_ev, np.nan)
        for Y, nd in nodes.items():
            Xs, _ = sol[Y]
            tot = np.asarray(Xs.sum(axis=0)).ravel()
            sec = np.asarray(Xs.T @ (~nd.first).astype(float)).ravel()
            share[nd.di] = np.where(tot > 0, sec / np.maximum(tot, 1e-300), np.nan)
        for X, nd in nodes.items():
            v = share[nd.ai]
            pri = np.where(nd.first, 0.0, np.where(np.isfinite(v), np.clip(v, 1e-3, 1 - 1e-3), 0.5))
            nd.stay_prior = pri
    return nodes, sol, (row_node, row_i, col_node, col_j)


def trace(run, nodes, sol, index, first_events, chunk=4000):
    """For each device first-hop event: its traced paths as (destination node, arrival time, weight), heaviest
    first. The two hops compose as a sparse product: first relay row -> its departures -> the second relay's row
    for that departure (normalised over leaving, since the packet is at its second relay) -> its departures."""
    ev = run.events
    row_node, row_i, col_node, col_j = index
    # global departure index g for every node departure; G2[g, g'] = P(departure g' | packet carried by g, leaving)
    offs, o = {}, 0
    for X, nd in nodes.items():
        offs[X] = o
        o += nd.di.size
    n_dep = o
    gev = np.concatenate([nodes[X].di for X in nodes])
    rows2, cols2, vals2 = [], [], []
    for X, nd in nodes.items():                       # X as second relay
        Xs, _ = sol[X]
        tot = np.asarray(Xs.sum(axis=1)).ravel()
        coo = Xs.tocoo()
        up = nd.ai[coo.row]                           # the upstream event (a departure of another node)
        gu = np.where(col_node[up] >= 0, np.array([offs.get(int(n), 0) for n in col_node[up]]) + col_j[up], -1)
        ok = (gu >= 0) & (tot[coo.row] > 0)
        rows2.append(gu[ok]); cols2.append(offs[X] + coo.col[ok]); vals2.append(coo.data[ok] / tot[coo.row][ok])
    G2 = sparse.csr_matrix((np.concatenate(vals2), (np.concatenate(rows2), np.concatenate(cols2))), shape=(n_dep, n_dep))
    out = [[] for _ in first_events]
    fe = np.asarray(first_events)
    for c0 in range(0, fe.size, chunk):
        part = fe[c0:c0 + chunk]
        r1, c1, v1 = [], [], []
        for k, e in enumerate(part):
            X, i = row_node[e], row_i[e]
            if X < 0:
                continue
            row = sol[X][0].getrow(i)
            r1.append(np.full(row.nnz, k)); c1.append(offs[X] + row.indices); v1.append(row.data)
        if not r1:
            continue
        G1 = sparse.csr_matrix((np.concatenate(v1), (np.concatenate(r1), np.concatenate(c1))), shape=(part.size, n_dep))
        T = (G1 @ G2).tocsr()
        for k in range(part.size):
            a, b = T.indptr[k], T.indptr[k + 1]
            if b <= a:
                continue
            w, g = T.data[a:b], T.indices[a:b]
            keep = w >= W_MIN
            w, g = w[keep], g[keep]
            if w.size > M_MAX:
                top = np.argpartition(-w, M_MAX)[:M_MAX]
                w, g = w[top], g[top]
            d = gev[g]
            out[c0 + k] = list(zip(ev["dst"][d], ev["t_arr"][d], w))
    return out


def arrays(paths):
    n = len(paths)
    Z = np.full((n, M_MAX), -1, np.int64)
    A = np.full((n, M_MAX), np.nan)
    Wt = np.zeros((n, M_MAX))
    for k, ps in enumerate(paths):
        for m, (z, a, w) in enumerate(ps):
            Z[k, m], A[k, m], Wt[k, m] = z, a, w
    return Z, A, Wt


def densities(cfg, seed0, runs=20):
    """On the model seeds: the record time after the credential packet's arrival at C (C); a registry submission
    after its content arrival (sub, pooled over F and I); the record time after a submission (rec, pooled); and,
    for the Registry Node, the same submission density."""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate, 0.2))
    c, q, rr = [], [], []
    for k in range(runs):
        s = S.simulate(mc, seed0 + k).subs
        ok = np.isfinite(s["posted"])
        u = s["posted"][ok]
        c.append(u - s["arr_c"][ok])
        q.append(np.r_[s["reg_f"][ok] - s["arr_f"][ok], s["reg_i"][ok] - s["arr_i"][ok]])
        rr.append(np.r_[u - s["reg_f"][ok], u - s["reg_i"][ok]])
    out = {}
    for name, x in (("C", c), ("sub", q), ("rec", rr)):
        x = np.concatenate(x)
        bw = AT.BW_Y if np.ptp(x) > 50 else 0.001
        out[name] = LT.EmpiricalLogPDF(x, bw)
    return out


F_PATHS = 24        # traced paths per packet followed to their destination's submission frames
F_MAX = 64          # frames kept per packet


def frames(run):
    """Every registry submission frame as the tracer sees it: its origin node and send time, by origin."""
    s, ev = run.subs, run.events
    e = np.r_[s["ev_reg_f"], s["ev_reg_i"]]
    e = e[e >= 0]
    org, t = ev["src"][e], ev["t_send"][e]
    return {X: np.sort(t[org == X]) for X in range(P.N_NODES)}


def frame_mixture(Z, A, Wt, fr, q):
    """Per packet: the submission frames its content would leave in, with weights sum_m w_km q(t_f - a_m), over its
    F_PATHS heaviest paths; the F_MAX heaviest frames kept. Returns (times, weights), n x F_MAX."""
    n = Z.shape[0]
    TF = np.full((n, F_MAX), np.nan)
    WF = np.zeros((n, F_MAX))
    zz, aa, ww = Z[:, :F_PATHS], A[:, :F_PATHS], Wt[:, :F_PATHS]
    kk = np.broadcast_to(np.arange(n)[:, None], zz.shape)
    ok = (zz >= 0) & (ww > 0)
    zz, aa, ww, kk = zz[ok], aa[ok], ww[ok], kk[ok]
    lo, hi = q.support
    K_, T_, V_ = [], [], []
    for X in range(P.N_NODES):
        sel = zz == X
        if not sel.any() or fr[X].size == 0:
            continue
        a0 = np.searchsorted(fr[X], aa[sel] + lo)
        a1 = np.searchsorted(fr[X], aa[sel] + hi, "right")
        r, pos = _ragged(a0, a1)
        tf = fr[X][pos]
        v = ww[sel][r] * np.exp(q(tf - aa[sel][r]))
        K_.append(kk[sel][r]); T_.append(tf); V_.append(v)
    if not K_:
        return TF, WF
    k, t, v = np.concatenate(K_), np.concatenate(T_), np.concatenate(V_)
    o = np.lexsort((t, k))
    k, t, v = k[o], t[o], v[o]
    new = np.r_[True, (k[1:] != k[:-1]) | (t[1:] != t[:-1])]
    gid = np.cumsum(new) - 1
    vs = np.bincount(gid, weights=v)
    k, t = k[new], t[new]
    for kk_ in np.unique(k):
        sel = np.nonzero(k == kk_)[0]
        if sel.size > F_MAX:
            sel = sel[np.argpartition(-vs[sel], F_MAX)[:F_MAX]]
        TF[kk_, :sel.size], WF[kk_, :sel.size] = t[sel], vs[sel]
    return TF, WF


def score(run, m, dens, out, registry=False):
    """The tracer's (or the Registry Node's) table, on the observer's candidates and records."""
    from . import devscore as DS
    cand, rec, base, shuf = out["_cand"], out["_rec"], out["_base"], out["_shuf"]
    nodes, sol, index = build(run)
    tie_dev = cand["dev"]
    paths = trace(run, nodes, sol, index, cand["ev"])
    Z, A, Wt = arrays(paths)
    logW = np.log(np.maximum(Wt, 1e-300))
    pC, pq, pR = dens["C"], dens["sub"], dens["rec"]
    if not registry:
        TF, WF = frame_mixture(Z, A, Wt, frames(run), pq)
        logWF = np.log(np.maximum(WF, 1e-300))
    u, n = rec["u"], rec["sub"].size
    s = run.subs
    g = m.pdf["g"]
    lo, hi = AT._band(u, g)
    col = DS.Collector(n, tie_dev)
    if not np.isfinite(lo).all():
        raise ValueError("band")
    if registry:
        Fr, Ir = s["F"][rec["sub"]], s["I"][rec["sub"]]
        rf, ri = s["reg_f"][rec["sub"]], s["reg_i"][rec["sub"]]

    def lse(v):
        mx = np.max(v, axis=2, keepdims=True)
        mxf = np.where(np.isfinite(mx), mx, 0.0)
        with np.errstate(divide="ignore"):
            out_ = np.log(np.sum(np.exp(v - mxf), axis=2)) + mxf[:, :, 0]
        return np.where(np.isfinite(mx[:, :, 0]), out_, -np.inf)

    def fn(rows, k0, k1):
        Ak, Wk, Zk = A[k0:k1], logW[k0:k1], Z[k0:k1]
        if not registry:
            y = u[rows][:, None, None] - Ak[None, :, :]
            vc = lse(pC(np.where(np.isfinite(y), y, -1e9)) + Wk[None, :, :]) + np.log(1 / 3)
            yf = u[rows][:, None, None] - TF[None, k0:k1, :]
            vf = lse(pR(np.where(np.isfinite(yf), yf, -1e9)) + logWF[None, k0:k1, :]) + np.log(2 / 3)
            return dict(tr=np.logaddexp(vc, vf))
        else:
            tF = np.where(Zk[None, :, :] == Fr[rows][:, None, None], rf[rows][:, None, None], np.nan)
            tI = np.where(Zk[None, :, :] == Ir[rows][:, None, None], ri[rows][:, None, None], np.nan)
            tt = np.where(np.isfinite(tF), tF, tI)
            y = tt - Ak[None, :, :]
            return dict(tr=lse(pq(np.where(np.isfinite(y), y, -1e9)) + Wk[None, :, :]))
    AT.score_blocks(lo, hi, cand, fn, dict(sub=rec["sub"], dev=rec["dev"]), ("tr",),
                    extra=lambda nm, rows, a, b, W, is_t: col(rows, a, b, W))
    labs, scs = [], []
    for i in range(n):
        lab, sc = col.get(i)
        labs.append(lab)
        scs.append(sc)
    t = DS.table(labs, scs, rec, np.arange(n), np.zeros(n), base, rec["dev"], shuf)
    return t, dict(paths_mean=float(np.mean([len(p) for p in paths])) if paths else 0.0,
                   traced_share=float(np.mean([len(p) > 0 for p in paths])) if paths else 0.0)


# --------------------------------------------------------------------------- the brute-force check
def brute_force(W, first, stay_prior):
    """Exact pairing marginals of a small node problem by enumeration: every assignment of arrivals to departures
    (each departure used exactly once; an arrival from a node may stay), weighted by the product of its pairing
    weights and its stay weights."""
    W = np.asarray(W, float)
    nr, nc = W.shape
    stay = np.where(first, 0.0, stay_prior / np.maximum(1 - stay_prior, 1e-12)) * np.where(W.max(1) > 0, W.max(1), 1.0)
    M = np.zeros((nr, nc))
    S_ = np.zeros(nr)
    Z = 0.0
    for perm in itertools.permutations(range(nr), nc):          # departure j is used by arrival perm[j]
        w = 1.0
        for j, i in enumerate(perm):
            w *= W[i, j]
            if w == 0:
                break
        if w == 0:
            continue
        used = set(perm)
        for i in range(nr):
            if i not in used:
                w *= stay[i]
        if w == 0:
            continue
        Z += w
        for j, i in enumerate(perm):
            M[i, j] += w
        for i in range(nr):
            if i not in used:
                S_[i] += w
    return M / Z, S_ / Z

"""The link-level tracer (C4 item 5) and the Registry Node vantage (item 6).

The tracer is a global passive observer. It sees every link event: send and arrival times, endpoints, and a size
that tells only the padding class. It knows the protocol and every hold distribution. It follows each device
packet across every leg the protocol puts on the wire:

  relays        At each node, its relay-class arrivals (from an external host or another node) are paired with its
                relay-class departures to other nodes. An arrival from an external host is at its first relay and
                leaves again; an arrival from a node is at its second relay (it leaves) or at its destination (it
                stays).
  destination   At each node, the arrivals that stay are paired with what a destination sends next: C's CV-1 to the
                validator (the credential packet) or one of the node's registry submissions (a content packet). The
                origin of a submission is on the wire, because the origin floods it to every peer at once.
  validator     At the validator, each CV-1 is paired with a CV-2 reply.
  quorum        Each reply reaching C is paired with the two submissions it leads to (F's and I's). From the reply,
                C's legs to the three gatekeepers, the gatekeepers' postings and the boards' pushes, a node Z learns
                of quorum at about the reply's arrival plus the second smallest, over the gatekeepers g, of the
                latencies C to g and g to Z. The tracer measures every link's latency on the wire (the fastest
                transit seen on it), and pairs the reply with each submission from Z by the density of the
                submission's time after that estimate.

A departure that follows a hold leaves on the holding clock's 10-second grid, whose phase the tracer reads from
that clock's own departures. Pairing an arrival with such a departure has the weight of the hold's geometric
release at the tick it waited, with the hold's mean (60 s at a first relay, 300 s at a second, C's and the
validator's holds before CV-1 and CV-2). A submission follows its content packet by the density of that delay on
the model seeds. Under one release probability every complete pairing of a node's packets has the same
likelihood, because the ticks waited sum to a total the times fix; the weights differ between positions, through
the cap, and between a CV-1 and a submission.

The tracer wants each packet's probability of leaving on each departure: the share, by weight, of the complete
pairings that use it. That share is a ratio of permanents. A node's problem splits into independent pieces (the
connected components of its possible pairings). For a piece with at most EXACT_ROWS arrivals the tracer counts
every complete pairing exactly, by a forward and backward sum over the sets of arrivals used. A larger piece is
approximated by matrix scaling (Sinkhorn): the weight matrix, with a "not here" column for arrivals that may not
be paired at this step, is scaled until every departure is used once and every arrival once. brute_force
enumerates the pairings of a small case, for checking both. At the relays, the probability that an arrival from a node stays is refined from its
upstream: an arrival whose upstream departure carried a first-relay packet is at its second relay.

A device packet k then has a mixture of end points, each a submission whose flood has reached every node at time
tau, with weight w: through C, the validator and quorum (the packet as a credential packet) or through its
destination (as a content packet). A record comes from one transaction: one credential packet and two content packets from one source address,
sent apart by the device's own holds. For packet k and record r let
  E_c(r, k) = sum over k's credential end points m of w_km p_F(u_r - tau_m),   E_t(r, k) the same over content
end points, with p_F the record time after a submission has reached every node (model seeds). The tracer scores a
device by its triples of packets, any of the three being the credential packet:
  score(r, d) = log sum over triples {a, b, c} of d's packets, and over the choice of c,
                 p_o(s_a - s_c) p_o(s_b - s_c) E_c(r, c) E_t(r, a) E_t(r, b),
with s the packets' send times and p_o the density of a content packet's send time after its credential packet's
(model seeds). A device with fewer than three packets near the record is scored by
log (sum_k E_c + e) + log (sum_k E_t + e) - 20, e = 10^-6, so it ranks below any device with a triple.

Registry Node. A Registry Node reads each submission, so it knows the two submissions of each record. It scores
packet k by the weight of its end points at exactly those submissions.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy import sparse

from . import attacks as AT
from . import lottery as LT
from . import params as P
from . import sim as S

M_MAX = 200         # end points kept per device packet
EXACT_ROWS = 10     # pieces with at most this many arrivals are counted exactly
W_MIN = 1e-6        # smaller path weights are dropped
ITER = 60           # Sinkhorn iterations
PASSES = 3          # passes over the relays, refining the stay probabilities
PROC = (0.0005, 0.003)                     # a node's processing before a send
V_PROC = P.VALIDATOR_PROC_MS[0] / 1000, P.VALIDATOR_PROC_MS[1] / 1000


# --------------------------------------------------------------------------- weights
def _ragged(a, b):
    """Row index and position for every j in [a_i, b_i)."""
    n = np.maximum(b - a, 0)
    rows = np.repeat(np.arange(a.size), n)
    pos = np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n) + np.repeat(a, n)
    return rows, pos


def _hold_table(mean):
    """Probability of releasing at the k-th tick (k = 1 .. K) for a hold of this mean."""
    p, K = LT.stage_lottery(mean)
    k = np.arange(1, K + 1)
    pk = p * (1 - p) ** (k - 1)
    pk[-1] = (1 - p) ** (K - 1)
    return pk


def clock_phase(ts, offset):
    """A clock's phase from departures that leave `offset` after one of its ticks (circular mean)."""
    if ts.size == 0:
        return 0.0
    x = np.mod(ts - offset, P.TICK_S)
    c = np.angle(np.mean(np.exp(2j * np.pi * x / P.TICK_S))) * P.TICK_S / (2 * np.pi)
    return float(np.mod(c, P.TICK_S))


def hold_pairs(ta, ts, mean, pre, post, density=False):
    """Every possible (arrival i, departure j) of a hold: the arrival waits `pre` (an interval of processing), holds on
    a 10-second clock with the given mean, and the departure leaves `post` (an interval) after its tick. ts sorted.
    Returns rows, cols and weights: the release probability (density=True: per second, so a hold can be compared
    with a density)."""
    if ta.size == 0 or ts.size == 0:
        return np.zeros(0, np.int64), np.zeros(0, np.int64), np.zeros(0)
    if mean <= 0:
        lo, hi = ta + pre[0] + post[0], ta + pre[1] + post[1]
        a, b = np.searchsorted(ts, lo - 1e-6), np.searchsorted(ts, hi + 1e-6, "right")
        r, c = _ragged(a, b)
        w = np.full(c.size, 1.0 / (hi[0] - lo[0]) if density else 1.0)
        return r, c, w
    ph = clock_phase(ts, 0.5 * (post[0] + post[1]))
    pk = _hold_table(mean)
    K = pk.size
    t1 = LT.next_tick(ta + 0.5 * (pre[0] + pre[1]), ph)
    a = np.searchsorted(ts, t1 + post[0] - 0.001)
    b = np.searchsorted(ts, t1 + P.TICK_S * (K - 1) + post[1] + 0.001, "right")
    r, c = _ragged(a, b)
    d = ts[c] - t1[r]
    k = np.rint((d - 0.5 * (post[0] + post[1])) / P.TICK_S).astype(int) + 1
    off = d - P.TICK_S * (k - 1)
    on = (off >= post[0] - 0.001) & (off <= post[1] + 0.001) & (k >= 1) & (k <= K)
    w = pk[np.clip(k, 1, K) - 1] / (P.TICK_S if density else 1.0)
    return r[on], c[on], w[on]


class Assoc:
    """One pairing problem: rows are arrivals, columns departures; every column is used once, every row `need` times
    (default once) or, with probability skip, not here."""

    def __init__(self, W, skip, need=1.0):
        self.W = W.tocsr()
        self.skip = np.asarray(skip, float)
        self.need = need

    def solve(self):
        W = self.W
        nr, nc = W.shape
        rowmax = W.max(axis=1).toarray().ravel() if nc else np.zeros(nr)
        stay = self.skip / np.maximum(1 - self.skip, 1e-12) * np.where(rowmax > 0, rowmax, 1.0)
        r, c = np.ones(nr), np.ones(nc)
        Wt = W.T.tocsr()
        for _ in range(ITER):
            colsum = Wt @ r
            c = np.where(colsum > 0, 1.0 / np.maximum(colsum, 1e-300), 0.0)
            rowsum = W @ c + stay
            r = np.where(rowsum > 0, self.need / np.maximum(rowsum, 1e-300), 0.0)
        X = (sparse.diags(r) @ W @ sparse.diags(c)).tocsr()
        S_ = r * stay
        if self.need == 1.0:
            X, S_ = _exact_pieces(W, stay, X, S_)
        return X, S_


def _exact_pieces(W, stay, X, S_):
    """Replace the Sinkhorn shares of every small piece of the problem by the exact shares."""
    from scipy.sparse import csgraph
    nr, nc = W.shape
    if nr == 0 or nc == 0:
        return X, S_
    A = sparse.bmat([[None, W], [W.T, None]]).tocsr()
    ncomp, lab = csgraph.connected_components(A, directed=False)
    rl, cl = lab[:nr], lab[nr:]
    nrow, ncol = np.bincount(rl, minlength=ncomp), np.bincount(cl, minlength=ncomp)
    small = (ncol > 0) & (nrow <= EXACT_ROWS) & (ncol <= nrow)
    rows_of = np.split(np.argsort(rl, kind="stable"), np.cumsum(nrow)[:-1])
    cols_of = np.split(np.argsort(cl, kind="stable"), np.cumsum(ncol)[:-1])
    Wd = W.tocsr()
    R_, C_, V_, done = [], [], [], np.zeros(nr, bool)
    S_ = S_.copy()
    for comp in np.nonzero(small)[0]:
        ri, ci = rows_of[comp], cols_of[comp]
        if ri.size == 1:                                 # one arrival, one departure: it leaves there
            R_.append(ri); C_.append(ci); V_.append(np.ones(1)); S_[ri] = 0.0; done[ri] = True
            continue
        sub = Wd[ri][:, ci].toarray()
        res = exact(sub, stay[ri])
        if res is None:
            continue
        M, St = res
        a, b = np.nonzero(sub > 0)
        R_.append(ri[a]); C_.append(ci[b]); V_.append(M[a, b])
        S_[ri] = St
        done[ri] = True
    if not R_:
        return X, S_
    keep = sparse.diags((~done).astype(float)) @ X
    ex = sparse.csr_matrix((np.concatenate(V_), (np.concatenate(R_), np.concatenate(C_))), shape=(nr, nc))
    return (keep + ex).tocsr(), S_


def exact(W, stay):
    """Exact pairing shares of one small piece: every column used by one distinct row, each unused row weighted by
    its stay weight. Forward f[j][mask] and backward b[j][mask] sums over the set of rows used. None if no complete
    pairing exists."""
    n, m = W.shape
    full = 1 << n
    masks = np.arange(full)
    bits = ((masks[:, None] >> np.arange(n)[None, :]) & 1).astype(bool)          # (full, n)
    f = np.zeros((m + 1, full))
    f[0, 0] = 1.0
    for j in range(m):
        for i in range(n):
            if W[i, j] == 0:
                continue
            src = ~bits[:, i]
            f[j + 1, masks[src] | (1 << i)] += f[j, src] * W[i, j]
    endw = np.prod(np.where(bits, 1.0, stay[None, :]), axis=1)                      # unused rows stay
    b = np.zeros((m + 1, full))
    b[m] = endw
    for j in range(m - 1, -1, -1):
        for i in range(n):
            if W[i, j] == 0:
                continue
            src = ~bits[:, i]
            b[j, src] += W[i, j] * b[j + 1, masks[src] | (1 << i)]
    Z = b[0, 0]
    if not np.isfinite(Z) or Z <= 0:
        return None
    M = np.zeros((n, m))
    for j in range(m):
        for i in range(n):
            if W[i, j] == 0:
                continue
            src = ~bits[:, i]
            M[i, j] = (f[j, src] * W[i, j] * b[j + 1, masks[src] | (1 << i)]).sum() / Z
    St = np.array([(f[m, ~bits[:, i]] * endw[~bits[:, i]]).sum() / Z for i in range(n)])
    return M, St


def link_latency(ev):
    """Every directed link's latency between pool nodes as the wire shows it: the fastest transit seen on it."""
    n = P.N_NODES + P.N_VALIDATORS
    m = (ev["src"] < n) & (ev["dst"] < n)
    lat = np.full((n, n), np.nan)
    tr = ev["t_arr"][m] - ev["t_send"][m]
    key = ev["src"][m].astype(np.int64) * n + ev["dst"][m]
    o = np.argsort(key, kind="stable")
    k, t = key[o], tr[o]
    u, start = np.unique(k, return_index=True)
    mn = np.minimum.reduceat(t, start)
    lat.flat[u] = mn
    return lat


def known_estimate(t2, C, lat, gk_set):
    """When each node learns of quorum, estimated from the reply's arrival at C (t2): rows t2, columns nodes Z."""
    via = lat[C, gk_set][:, None] + lat[gk_set][:, :P.N_NODES]          # (3, Z)
    return t2[:, None] + np.sort(via, axis=0)[1][None, :]


def brute_force(W, skip):
    """Exact pairing shares of a small problem by enumeration, with the same weights as Assoc: every assignment of
    each column to a distinct row, the unused rows not here, weighted by the product of the pairing weights and the
    not-here weights."""
    W = np.asarray(W, float)
    nr, nc = W.shape
    skip = np.asarray(skip, float)
    stay = skip / np.maximum(1 - skip, 1e-12) * np.where(W.max(1) > 0, W.max(1), 1.0)
    M, S_, Z = np.zeros((nr, nc)), np.zeros(nr), 0.0
    for perm in itertools.permutations(range(nr), nc):
        w = np.prod([W[i, j] for j, i in enumerate(perm)])
        if w == 0:
            continue
        unused = [i for i in range(nr) if i not in perm]
        w *= np.prod([stay[i] for i in unused]) if unused else 1.0
        if w == 0:
            continue
        Z += w
        for j, i in enumerate(perm):
            M[i, j] += w
        for i in unused:
            S_[i] += w
    return M / Z, S_ / Z


# --------------------------------------------------------------------------- the three steps
def _relay_index(run):
    ev = run.events
    lo, hi = P.PAD_MIN + P.TLS13_OVERHEAD, P.PAD_MAX + P.TLS13_OVERHEAD
    rel = (ev["rtype"] == P.RT_APPDATA) & (ev["size"] >= lo) & (ev["size"] <= hi)
    to_node = rel & (ev["dst"] < P.N_NODES) & ((ev["src"] < P.N_NODES) | (ev["src"] == S.EXT))
    to_val = rel & (ev["src"] < P.N_NODES) & (ev["dst"] >= P.N_NODES) & (ev["dst"] != S.EXT)
    from_val = rel & (ev["src"] >= P.N_NODES) & (ev["src"] != S.EXT) & (ev["dst"] < P.N_NODES)
    return np.nonzero(to_node)[0], np.nonzero(to_val)[0], np.nonzero(from_val)[0]


def _sorted(idx, t):
    return idx[np.argsort(t[idx], kind="stable")]


class Tracer:
    """Every pairing step of one run, and each device packet's end points."""

    def __init__(self, run, dens):
        self.run, self.dens = run, dens
        ev, cfg, s = run.events, run.cfg, run.subs
        self.ev = ev
        n_ev = ev["t_send"].shape[0]
        rel, cv1, cv2 = _relay_index(run)
        # relays
        self.rows, self.cols, self.relay = {}, {}, {}
        first = {}
        for X in range(P.N_NODES):
            arr = _sorted(rel[ev["dst"][rel] == X], ev["t_arr"])
            dep = _sorted(rel[ev["src"][rel] == X], ev["t_send"])
            f = ev["src"][arr] == S.EXT
            R_, C_, V_ = [], [], []
            for pos, mean in ((True, cfg.relay1_mean), (False, cfg.relay2_mean)):
                sel = np.nonzero(f == pos)[0]
                r, c, w = hold_pairs(ev["t_arr"][arr[sel]], ev["t_send"][dep], mean, (0.0, 0.0), PROC)
                R_.append(sel[r]); C_.append(c); V_.append(w)
            W = sparse.csr_matrix((np.concatenate(V_), (np.concatenate(R_), np.concatenate(C_))), shape=(arr.size, dep.size))
            self.relay[X] = Assoc(W, np.where(f, 0.0, 0.5))
            self.rows[X], self.cols[X], first[X] = arr, dep, f
        col_of = np.full(n_ev, -1)
        node_of = np.full(n_ev, -1)
        for X in range(P.N_NODES):
            col_of[self.cols[X]], node_of[self.cols[X]] = np.arange(self.cols[X].size), X
        self.sol = {}
        for _ in range(PASSES):
            for X, a in self.relay.items():
                self.sol[X] = a.solve()
            share = np.full(n_ev, np.nan)
            for Y, a in self.relay.items():
                Xs, _ = self.sol[Y]
                tot = np.asarray(Xs.sum(axis=0)).ravel()
                sec = np.asarray(Xs.T @ (~first[Y]).astype(float)).ravel()
                share[self.cols[Y]] = np.where(tot > 0, sec / np.maximum(tot, 1e-300), np.nan)
            for X, a in self.relay.items():
                v = share[self.rows[X]]
                a.skip = np.where(first[X], 0.0, np.where(np.isfinite(v), np.clip(v, 1e-3, 1 - 1e-3), 0.5))
        # destinations: arrivals that stay, paired with C's CV-1 or with one of the node's submissions
        org_e = np.r_[s["ev_reg_f"], s["ev_reg_i"]]
        reach = np.r_[s["reach_f"], s["reach_i"]]
        ok = org_e >= 0
        org_e, reach = org_e[ok], reach[ok]
        self.dest, self.dcols = {}, {}
        q = dens["sub"]
        for X in range(P.N_NODES):
            arr, f = self.rows[X], first[X]
            stay = self.sol[X][1]
            node_rows = np.nonzero(~f)[0]
            c1 = _sorted(cv1[ev["src"][cv1] == X], ev["t_send"])
            fr = org_e[ev["src"][org_e] == X]
            fr = fr[np.argsort(ev["t_send"][fr], kind="stable")]
            ta = ev["t_arr"][arr[node_rows]]
            r1, k1, w1 = hold_pairs(ta, ev["t_send"][c1], cfg.c_hold_mean, (0.0, 0.0), PROC, density=True)
            tf = ev["t_send"][fr]
            a0, a1 = np.searchsorted(tf, ta + q.support[0]), np.searchsorted(tf, ta + q.support[1], "right")
            r2, k2 = _ragged(a0, a1)
            w2 = np.exp(q(tf[k2] - ta[r2]))
            W = sparse.csr_matrix((np.r_[w1 / 3, 2 * w2 / 3], (np.r_[r1, r2], np.r_[k1, c1.size + k2])),
                                  shape=(node_rows.size, c1.size + fr.size))
            self.dest[X] = (node_rows, Assoc(W, 1.0 - np.clip(stay[node_rows], 1e-6, 1.0)))
            self.dcols[X] = (c1, fr)
        self.dsol = {X: a.solve() for X, (_, a) in self.dest.items()}
        # validators: CV-1 paired with CV-2
        self.val = {}
        for v in np.unique(ev["dst"][cv1]):
            arr = _sorted(cv1[ev["dst"][cv1] == v], ev["t_arr"])
            dep = _sorted(cv2[ev["src"][cv2] == v], ev["t_send"])
            r, c, w = hold_pairs(ev["t_arr"][arr], ev["t_send"][dep], cfg.v_hold_mean, V_PROC, (0.0, 0.0))
            W = sparse.csr_matrix((w, (r, c)), shape=(arr.size, dep.size))
            self.val[int(v)] = (arr, dep, Assoc(W, np.zeros(arr.size)).solve()[0])
        self.reach_of = dict(zip(org_e.tolist(), reach.tolist()))
        # quorum: each reply's arrival at C paired with its two submissions
        lat = link_latency(ev)
        self.via = np.full((P.N_NODES, P.N_NODES), np.nan)
        for X in range(P.N_NODES):
            self.via[X] = known_estimate(np.zeros(1), X, lat, run.gk_set)[0]
        c2a = _sorted(cv2, ev["t_arr"])
        t2, Cn = ev["t_arr"][c2a], ev["dst"][c2a]
        org_sorted = org_e[np.argsort(ev["t_send"][org_e], kind="stable")]
        f_org, f_t = ev["src"][org_sorted], ev["t_send"][org_sorted]
        qd = dens["Q"]
        R_, C_, V_ = [], [], []
        for X in range(P.N_NODES):
            rows = np.nonzero(Cn == X)[0]
            if rows.size == 0:
                continue
            ke = known_estimate(t2[rows], X, lat, run.gk_set)               # (rows, Z)
            for Z in range(P.N_NODES):
                if Z == X:
                    continue
                cols = np.nonzero(f_org == Z)[0]
                if cols.size == 0:
                    continue
                tz = f_t[cols]
                a0 = np.searchsorted(tz, ke[:, Z] + qd.support[0])
                a1 = np.searchsorted(tz, ke[:, Z] + qd.support[1], "right")
                r, c = _ragged(a0, a1)
                w = np.exp(qd(tz[c] - ke[r, Z]))
                R_.append(rows[r]); C_.append(cols[c]); V_.append(w)
        Wq = sparse.csr_matrix((np.concatenate(V_) if V_ else [], (np.concatenate(R_) if R_ else [], np.concatenate(C_) if C_ else [])),
                               shape=(c2a.size, org_sorted.size))
        self.quorum = (c2a, org_sorted, Assoc(Wq, np.zeros(c2a.size), need=2.0).solve()[0])

    def end_points(self, first_events):
        """For each device first-hop event: (end-point event ids, types (0 reply at C, 1 submission), times, weights),
        the M_MAX heaviest. Built as sparse products: first relay -> second relay -> destination -> end point."""
        ev = self.ev
        nodes = list(range(P.N_NODES))
        # global index of every relay departure
        off, o = {}, 0
        for X in nodes:
            off[X] = o
            o += self.cols[X].size
        n_dep = o
        gdep = np.concatenate([self.cols[X] for X in nodes])
        where = {}
        for X in nodes:
            for i, e in enumerate(self.rows[X]):
                where[int(e)] = (X, i)
        # G2: a relay departure -> the second relay's departures, given that the packet leaves there
        R2, C2, V2 = [], [], []
        for X in nodes:
            Xs, _ = self.sol[X]
            tot = np.asarray(Xs.sum(axis=1)).ravel()
            coo = Xs.tocoo()
            up = self.rows[X][coo.row]
            gu = np.array([off[int(ev["src"][e])] + int(np.searchsorted(self.cols[int(ev["src"][e])], e))
                           if ev["src"][e] < P.N_NODES else -1 for e in up], np.int64) if up.size else np.zeros(0, np.int64)
            okk = (gu >= 0) & (tot[coo.row] > 0)
            R2.append(gu[okk]); C2.append(off[X] + coo.col[okk]); V2.append(coo.data[okk] / tot[coo.row][okk])
        G2 = sparse.csr_matrix((np.concatenate(V2), (np.concatenate(R2), np.concatenate(C2))), shape=(n_dep, n_dep))
        # GD: a relay departure that arrives at its destination -> end points
        ends_e, ends_type, ends_t, ends_z, ends_s = [], [], [], [], []
        idx_of = {}

        def end(e, typ, t, z, ts):
            if e not in idx_of:
                idx_of[e] = len(ends_e)
                ends_e.append(e); ends_type.append(typ); ends_t.append(t); ends_z.append(z); ends_s.append(ts)
            return idx_of[e]
        RD, CD, VD = [], [], []
        q_rows, q_cols, Qs = self.quorum
        qrow = {int(e): i for i, e in enumerate(q_rows)}
        vmap = {}
        for v, (arr, dep, Vs) in self.val.items():
            for i, e in enumerate(arr):
                vmap[int(e)] = (v, i)
        for X in nodes:
            node_rows, _ = self.dest[X]
            Ds, skip = self.dsol[X]
            c1, fr = self.dcols[X]
            matched = np.asarray(Ds.sum(axis=1)).ravel()
            coo = Ds.tocoo()
            for r, c, w in zip(coo.row, coo.col, coo.data):
                if matched[r] <= 0:
                    continue
                arr_e = int(self.rows[X][node_rows[r]])
                src = int(ev["src"][arr_e])
                if src >= P.N_NODES:
                    continue
                g = off[src] + int(np.searchsorted(self.cols[src], arr_e))
                w = w / matched[r]
                if c < c1.size:                              # a CV-1: on to the validator's reply, then to quorum
                    v, i = vmap.get(int(c1[c]), (None, None))
                    if v is None:
                        continue
                    arr_v, dep_v, Vs = self.val[v]
                    row = Vs.getrow(i)
                    tot = row.data.sum()
                    for j, x in zip(row.indices, row.data):
                        e2 = int(dep_v[j])
                        wx = w * x / max(tot, 1e-300)
                        # the reply reaching C, kept for the joint score of a transaction
                        RD.append(g); CD.append(end((e2, 2), 2, float(ev["t_arr"][e2]), int(ev["dst"][e2]), float(ev["t_arr"][e2])))
                        VD.append(wx)
                        qi = qrow.get(e2)
                        if qi is None:
                            continue
                        qr = Qs.getrow(qi)
                        for jj, y in zip(qr.indices, qr.data):
                            e3 = int(q_cols[jj])
                            RD.append(g); CD.append(end((e3, 0), 0, self.reach_of[e3], int(ev["src"][e3]), float(ev["t_send"][e3])))
                            VD.append(wx * y / 2.0)
                else:                                        # a submission
                    e2 = int(fr[c - c1.size])
                    RD.append(g); CD.append(end((e2, 1), 1, self.reach_of[e2], int(ev["src"][e2]), float(ev["t_send"][e2]))); VD.append(w)
        GD = sparse.csr_matrix((VD, (RD, CD)), shape=(n_dep, max(len(ends_e), 1)))
        ends_e = np.array([e for e, _ in ends_e], np.int64)
        ends_type, ends_t = np.array(ends_type, np.int8), np.array(ends_t)
        ends_z, ends_s = np.array(ends_z, np.int64), np.array(ends_s)
        # G1: device packet -> its first relay's departures
        fe = np.asarray(first_events)
        R1, C1, V1 = [], [], []
        for k, e in enumerate(fe):
            X, i = where.get(int(e), (None, None))
            if X is None:
                continue
            row = self.sol[X][0].getrow(i)
            R1.append(np.full(row.nnz, k)); C1.append(off[X] + row.indices); V1.append(row.data)
        G1 = sparse.csr_matrix((np.concatenate(V1) if V1 else [], (np.concatenate(R1) if R1 else [], np.concatenate(C1) if C1 else [])),
                               shape=(fe.size, n_dep))
        T = (G1 @ (G2 @ GD)).tocsr()
        n = fe.size
        E = np.full((n, M_MAX), -1, np.int64)
        TY = np.zeros((n, M_MAX), np.int8)
        TT = np.full((n, M_MAX), np.nan)
        WW = np.zeros((n, M_MAX))
        ZZ = np.full((n, M_MAX), -1, np.int64)
        TS = np.full((n, M_MAX), np.nan)
        for k in range(n):
            a, b = T.indptr[k], T.indptr[k + 1]
            w, j = T.data[a:b], T.indices[a:b]
            keep = w >= W_MIN
            w, j = w[keep], j[keep]
            if w.size > M_MAX:
                top = np.argpartition(-w, M_MAX)[:M_MAX]
                w, j = w[top], j[top]
            E[k, :w.size], TY[k, :w.size], TT[k, :w.size], WW[k, :w.size] = ends_e[j], ends_type[j], ends_t[j], w
            ZZ[k, :w.size], TS[k, :w.size] = ends_z[j], ends_s[j]
        self.ZZ, self.TS = ZZ, TS
        return E, TY, TT, WW


# --------------------------------------------------------------------------- densities and scoring
def densities(cfg, seed0, runs=20):
    """On the model seeds: a submission after its content packet's arrival (sub); a submission after the estimate
    of when its node learned of quorum (Q); the record time after a submission has reached every node (F)."""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate, 0.2))
    sub, qq, f, so, pw = [], [], [], [], []
    for k in range(runs):
        run = S.simulate(mc, seed0 + k)
        s = run.subs
        ok = np.isfinite(s["posted"])
        u = s["posted"][ok]
        sub.append(np.r_[s["reg_f"][ok] - s["arr_f"][ok], s["reg_i"][ok] - s["arr_i"][ok]])
        f.append(np.r_[u - s["reach_f"][ok], u - s["reach_i"][ok]])
        pw.append(u - np.fmax(s["reach_f"][ok], s["reach_i"][ok]))
        lat = link_latency(run.events)
        idx = np.nonzero(ok)[0]
        for Cx in range(P.N_NODES):
            j = idx[s["C"][idx] == Cx]
            if j.size == 0:
                continue
            ke = known_estimate(s["cv2_a"][j], Cx, lat, run.gk_set)
            qq.append(np.r_[s["reg_f"][j] - ke[np.arange(j.size), s["F"][j]], s["reg_i"][j] - ke[np.arange(j.size), s["I"][j]]])
        cs = run.events["t_send"]
        so.append(np.r_[cs[s["ev_ca"][:, 0]] - cs[s["ev_cred"][:, 0]], cs[s["ev_cb"][:, 0]] - cs[s["ev_cred"][:, 0]]])
    out = {}
    for name, x in (("sub", sub), ("Q", qq), ("F", f), ("o", so), ("post", pw)):
        x = np.concatenate(x)
        x = x[np.isfinite(x)]
        out[name] = LT.EmpiricalLogPDF(x, AT.BW_Y if np.ptp(x) > 50 else 0.001)
    return out


def score(run, m, dens, out, registry=False, tracer=None):
    """The tracer's (or the Registry Node's) table, on the observer's candidates and records."""
    from . import devscore as DS
    cand, rec, base, shuf = out["_cand"], out["_rec"], out["_base"], out["_shuf"]
    tr = tracer or Tracer(run, dens)
    E, TY, TT, WW = tr.end_points(cand["ev"])
    tr._E, tr._TY, tr._TT, tr._WW = E, TY, TT, WW
    logW = np.log(np.maximum(WW, 1e-300))
    u, n = rec["u"], rec["sub"].size
    s = run.subs
    lo, hi = AT._band(u, m.pdf["g"])
    col_c, col_t = DS.Collector(n, cand["dev"]), DS.Collector(n, cand["dev"])
    pF = dens["F"]
    if registry:
        mine_f, mine_i = s["ev_reg_f"][rec["sub"]], s["ev_reg_i"][rec["sub"]]

    def lse(v):
        mx = np.max(v, axis=2, keepdims=True)
        mxf = np.where(np.isfinite(mx), mx, 0.0)
        with np.errstate(divide="ignore"):
            out_ = np.log(np.sum(np.exp(v - mxf), axis=2)) + mxf[:, :, 0]
        return np.where(np.isfinite(mx[:, :, 0]), out_, -np.inf)

    def fn(rows, k0, k1):
        if registry:
            hit = (E[None, k0:k1, :] == mine_f[rows][:, None, None]) | (E[None, k0:k1, :] == mine_i[rows][:, None, None])
            v = np.where(hit, logW[None, k0:k1, :], -np.inf)
        else:
            y = u[rows][:, None, None] - TT[None, k0:k1, :]
            v = pF(np.where(np.isfinite(y), y, -1e9)) + logW[None, k0:k1, :]
        ty = TY[None, k0:k1, :]
        return dict(trc=lse(np.where(ty == 0, v, -np.inf)), trt=lse(np.where(ty == 1, v, -np.inf)))     # replies (2) only in _joint

    per = [dict() for _ in range(n)]

    def extra(nm, rows, a, b, W, is_t):
        (col_c if nm == "trc" else col_t)(rows, a, b, W)
        for i, r in enumerate(rows):
            ok = np.isfinite(W[i])
            per[r][nm] = (a + np.nonzero(ok)[0], W[i, ok])
    AT.score_blocks(lo, hi, cand, fn, dict(sub=rec["sub"], dev=rec["dev"]), ("trc", "trt"), extra=extra)
    floor = np.log(1e-6)
    po = dens["o"]
    labs, scs = [], []
    for i in range(n):
        lc, sc = col_c.get(i)
        lt, st = col_t.get(i)
        lab = np.union1d(lc, lt)
        a = np.full(lab.size, floor)
        b = np.full(lab.size, floor)
        a[np.searchsorted(lab, lc)] = np.logaddexp(sc, floor)
        b[np.searchsorted(lab, lt)] = np.logaddexp(st, floor)
        score_ = a + b - 20.0
        # triples of each device's packets
        kc, vc = per[i].get("trc", (np.zeros(0, int), np.zeros(0)))
        kt, vt = per[i].get("trt", (np.zeros(0, int), np.zeros(0)))
        ks = np.union1d(kc, kt)
        if ks.size >= 3:
            Ec = np.full(ks.size, -np.inf)
            Et = np.full(ks.size, -np.inf)
            Ec[np.searchsorted(ks, kc)] = vc
            Et[np.searchsorted(ks, kt)] = vt
            dv = cand["dev"][ks]
            for d in np.unique(dv):
                j = np.nonzero(dv == d)[0]
                if j.size < 3:
                    continue
                t = cand["t"][ks[j]]
                best = []
                for c in range(j.size):
                    off = po(t - t[c])                          # every other packet as content after this credential
                    x = Ec[j[c]] + off + Et[j]
                    x[c] = -np.inf
                    if np.isfinite(Ec[j[c]]) and np.isfinite(x).sum() >= 2:
                        xs = np.sort(x[np.isfinite(x)])
                        # sum over pairs {a, b} of exp(x_a + x_b - Ec): log of ((sum e^x)^2 - sum e^2x) / 2, minus Ec
                        m_ = xs.max()
                        e1 = np.exp(xs - m_).sum()
                        e2 = np.exp(2 * (xs - m_)).sum()
                        if e1 * e1 - e2 > 0:
                            best.append(np.log((e1 * e1 - e2) / 2) + 2 * m_ - Ec[j[c]])
                if best:
                    pos = np.searchsorted(lab, d)
                    score_[pos] = np.logaddexp.reduce(best)
        if not registry:
            band = np.arange(np.searchsorted(cand["t"], lo[i]), np.searchsorted(cand["t"], hi[i]))
            score_ = _joint(score_, lab, band, cand, tr, dens, u[i])
        labs.append(lab)
        scs.append(score_)
    t = DS.table(labs, scs, rec, np.arange(n), np.zeros(n), base, rec["dev"], shuf)
    return t, tr


SHORT = 60          # devices per record given the joint score of a transaction
J_REPLY, J_FRAME = 8, 12   # end points per packet kept in the joint score
J_FLOOR = -np.inf     # outside the range of a density seen on the model seeds


def _joint(score_, lab, ks, cand, tr, dens, u):
    """The joint likelihood of the record under each of the SHORT best devices: over the device's triples of packets
    near the record (any of the three as the credential packet), the reply its credential packet leads to, the
    submissions its content packets lead to (at two different nodes), the quorum timing of those submissions after
    the reply, and the record's posting after the later submission. A value outside the range of a density seen on the
    model seeds is floored at e^-30. Other devices rank below these."""
    if ks.size < 3:
        return score_
    E, TY, ZZ, TS, TT, WW = tr._E, tr._TY, tr.ZZ, tr.TS, tr._TT, tr._WW
    fl = J_FLOOR
    pQ, po, pp = ((lambda x, f=dens[k]: np.maximum(f(x), fl)) for k in ("Q", "o", "post"))
    order = np.argsort(-score_)
    top = lab[order[:SHORT]]
    dv = cand["dev"][ks]
    out = score_.copy()
    got = []
    for d in top:
        j = ks[dv == d]
        if j.size < 3:
            continue
        t = cand["t"][j]
        reps, frs = [], []
        for k in j:
            sel = TY[k] == 2
            o2 = np.argsort(-WW[k][sel])[:J_REPLY]
            reps.append((ZZ[k][sel][o2], TS[k][sel][o2], WW[k][sel][o2]))
            sel = TY[k] == 1
            o1 = np.argsort(-WW[k][sel])[:J_FRAME]
            frs.append((ZZ[k][sel][o1], TS[k][sel][o1], TT[k][sel][o1], WW[k][sel][o1]))
        tot = []
        for c in range(j.size):
            cz, ct, cw = reps[c]
            if cw.size == 0:
                continue
            for a in range(j.size):
                for b in range(a + 1, j.size):
                    if c in (a, b):
                        continue
                    lo_ = po(np.array([t[a] - t[c], t[b] - t[c]]))
                    if not np.isfinite(lo_).all():
                        continue
                    za, ta_, ra, wa = frs[a]
                    zb, tb_, rb, wb = frs[b]
                    if wa.size == 0 or wb.size == 0:
                        continue
                    # (reply, frame a, frame b)
                    kea = ct[:, None] + tr.via[cz][:, za]                    # (R, Fa)
                    keb = ct[:, None] + tr.via[cz][:, zb]
                    qa = pQ(ta_[None, :] - kea) + np.log(wa)[None, :]
                    qb = pQ(tb_[None, :] - keb) + np.log(wb)[None, :]
                    pr = pp(u - np.maximum(ra[:, None], rb[None, :]))        # (Fa, Fb)
                    diff = za[:, None] != zb[None, :]
                    x = np.log(cw)[:, None, None] + qa[:, :, None] + qb[:, None, :] + np.where(diff, pr, -np.inf)[None, :, :]
                    m_ = np.max(x)
                    if np.isfinite(m_):
                        tot.append(lo_.sum() + m_ + np.log(np.exp(x - m_).sum()))
        if tot:
            got.append((d, np.logaddexp.reduce(tot)))
    if got:
        base = min(v for _, v in got) - 50.0
        out = np.minimum(out, base) if np.isfinite(base) else out
        for d, v in got:
            out[np.searchsorted(lab, d)] = v
    return out

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
  quorum        For each reply reaching C, when each node learns of quorum (known_estimate): the protocol followed
                from the reply with every hold at its first possible release, through C's fan-out tick, the
                gatekeepers' hold ticks and 30-second departure grids, and the boards' 10-second pushes. The joint
                score pairs a reply with submissions by the time of each submission after that estimate.

A departure that follows a hold leaves on the holding clock's 10-second grid, whose phase the tracer reads from
that clock's own departures; the gatekeepers' grids and the boards' push schedules have phases the tracer is given
(a global observer reads them from the times departures and submissions leave). Pairing an arrival with such a
departure has the weight of the hold's geometric release at the tick it waited. Under one release probability every
complete pairing of a node's packets has the same likelihood, because the ticks waited sum to a total the times fix;
the weights differ between positions, through the cap, and between a CV-1 and a submission.

The tracer wants each packet's probability of leaving on each departure: the share, by weight, of the complete
pairings that use it. That share is a ratio of permanents. A node's problem splits into independent pieces (the
connected components of its possible pairings). For a piece with at most EXACT_ROWS arrivals the tracer counts
every complete pairing exactly, by a forward and backward sum over the sets of arrivals used. A larger piece is
approximated by matrix scaling (Sinkhorn). brute_force enumerates the pairings of a small case, for checking both.
At the relays, the probability that an arrival from a node stays is refined from its upstream: an arrival whose
upstream departure carried a first-relay packet is at its second relay.

A device packet k then has a mixture of end points with weights w: the replies it leads to as a credential packet
and the submissions it leads to as a content packet (end_points). The tracer scores every device with at least
three packets near the record by its triples of packets, any of the three as the credential packet (_joint):

  score(r, d) = log sum over d's credential packets c, their replies rho, and pairs {a, b} of d's other packets of
                P(a, b | c) w(c, rho) sum over submissions f_a of a and f_b of b at different nodes of
                w(a, f_a) w(b, f_b) p_Q(f_a | rho) p_Q(f_b | rho) p_post(u_r - the later flood of f_a, f_b),

with P(a, b | c) the content packets' send times after c's (density o), normalized over the pairs of d's packets,
p_Q the submission after the reply's quorum estimate, and p_post the record time after the later submission has
reached every node. The densities come from model seeds at the cell's load; under registry-level bundling p_Q is the
probability of the bundle interval, and under the posting schedule p_post is flat over one period. A device with no
such triple is scored by its content packets' end points alone and ranks below.

Registry Node. A Registry Node reads each submission, so it knows the two submissions of each record. It scores
devices by the same joint score with the two submissions fixed and no record-time term.
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
CHUNK = 2000        # device packets per block of the end-point product
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


def known_estimate(t2, C, lat, run):
    """When each node learns of quorum, estimated from the reply's arrival at C (t2): rows t2, columns nodes Z.

    It follows the protocol with every hold at its first possible release: C's fan-out leg leaves at the next tick
    of C's clock (at once with no fan-out hold); the gatekeeper releases at the next tick of its hold clock (at once
    with no hold) and posts at the next boundary of its 30-second departure grid (no grid when the schedules are
    off); the board pushes at its next 10-second push; the push reaches Z after the link's latency. Quorum is the
    second of the three. The tracer is given each clock's, grid's and push schedule's phase: a global observer
    reads them from the times departures and submissions leave, so this is an upper bound on what it learns."""
    cfg = run.cfg
    t2 = np.asarray(t2, float)
    out = np.empty((3, t2.size, P.N_NODES))
    gproc = 0.5 * (P.GATEKEEPER_PROC_MS[0] + P.GATEKEEPER_PROC_MS[1]) / 1000
    proc = 0.5 * (PROC[0] + PROC[1])
    leg = t2 if cfg.fanout_mean <= 0 else LT.next_tick(t2, run.phase[C])
    for j, g in enumerate(run.gk_set):
        g = int(g)
        chk = leg + proc + lat[C, g] + gproc
        rel = chk if cfg.gk_mean <= 0 else LT.next_tick(chk, run.gk_phase[g])
        if not cfg.grid_off:
            ph = run.bundle_phase[g]
            rel = ph + P.BUNDLE_S * np.ceil((rel - ph) / P.BUNDLE_S)
        post = rel + proc
        if not cfg.grid_off:
            ph = run.push_phase[g]
            post = ph + P.BOARD_PUSH_S * np.ceil((post - ph) / P.BOARD_PUSH_S)
        out[j] = post[:, None] + lat[g, :P.N_NODES][None, :]
    return np.sort(out, axis=0)[1]


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
        # quorum: each reply's estimate of when each node learns of quorum; the joint score pairs a reply with
        # submissions by it
        lat = link_latency(ev)
        c2a = _sorted(cv2, ev["t_arr"])
        t2, Cn = ev["t_arr"][c2a], ev["dst"][c2a]
        self.ke = np.full((c2a.size, P.N_NODES), np.nan)
        self.ke_row = {int(e): i for i, e in enumerate(c2a)}
        for X in range(P.N_NODES):
            rows = np.nonzero(Cn == X)[0]
            if rows.size:
                self.ke[rows] = known_estimate(t2[rows], X, lat, run)

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
                if c < c1.size:                              # a CV-1: on to the validator's reply
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
        n = fe.size
        E = np.full((n, M_MAX), -1, np.int64)
        TY = np.zeros((n, M_MAX), np.int8)
        TT = np.full((n, M_MAX), np.nan)
        WW = np.zeros((n, M_MAX))
        ZZ = np.full((n, M_MAX), -1, np.int64)
        TS = np.full((n, M_MAX), np.nan)
        for c0 in range(0, n, CHUNK):                    # device packets in chunks, multiplied from their side
            T = ((G1[c0:c0 + CHUNK] @ G2) @ GD).tocsr()
            for kk in range(T.shape[0]):
                k = c0 + kk
                a, b = T.indptr[kk], T.indptr[kk + 1]
                w, j = T.data[a:b], T.indices[a:b]
                keep = w >= W_MIN
                w, j = w[keep], j[keep]
                if w.size > M_MAX:
                    top = np.argpartition(-w, M_MAX)[:M_MAX]
                    w, j = w[top], j[top]
                E[k, :w.size], TY[k, :w.size], TT[k, :w.size], WW[k, :w.size] = ends_e[j], ends_type[j], ends_t[j], w
                ZZ[k, :w.size], TS[k, :w.size] = ends_z[j], ends_s[j]
            del T
        self.ZZ, self.TS = ZZ, TS
        return E, TY, TT, WW


# --------------------------------------------------------------------------- densities and scoring
class Tailed:
    """A density fitted on the model seeds, mixed with a uniform tail of weight 1 / (n + 1) over a range MARGIN of its
    span wider on each side, so a value just past the samples is unlikely rather than impossible."""
    MARGIN = 0.05

    def __init__(self, pdf, n):
        self.pdf = pdf
        lo, hi = pdf.support
        w = max(self.MARGIN * (hi - lo), 1e-3)
        self.support = (lo - w, hi + w)
        self.eps = 1.0 / (n + 1)
        self.tail = np.log(self.eps) - np.log(self.support[1] - self.support[0])

    def __call__(self, x):
        x = np.asarray(x, float)
        with np.errstate(divide="ignore"):
            f = self.pdf(x) + np.log1p(-self.eps)
        inside = (x >= self.support[0]) & (x <= self.support[1])
        return np.where(inside, np.logaddexp(f, self.tail), -np.inf)


class Atom:
    """A density with a point mass at 0 (a delay that is exactly zero in some cases, such as a record posted the
    moment its later submission has reached every node), as a box of width 2 POINT around 0, plus the density
    of the other samples."""
    POINT = 1e-6

    def __init__(self, x):
        z = np.abs(x) <= 1e-9
        self.p0 = float(z.mean())
        rest = x[~z]
        self.rest = LT.EmpiricalLogPDF(rest, AT.BW_Y if np.ptp(rest) > 50 else 0.001) if rest.size > 1 else None
        lo, hi = (-self.POINT, self.POINT)
        if self.rest is not None:
            lo, hi = min(lo, self.rest.support[0]), max(hi, self.rest.support[1])
        self.support = (lo, hi)

    def __call__(self, x):
        x = np.asarray(x, float)
        with np.errstate(divide="ignore"):
            a = np.where(np.abs(x) <= self.POINT, np.log(self.p0) - np.log(2 * self.POINT), -np.inf)
            b = np.log1p(-self.p0) + self.rest(x) if self.rest is not None else np.full(x.shape, -np.inf)
        return np.logaddexp(a, b)


def _fit(x):
    """A tracer density from model-seed samples: a point mass at 0 when at least 1% of samples are exactly 0."""
    if np.mean(np.abs(x) <= 1e-9) >= 0.01:
        return Atom(x)
    return LT.EmpiricalLogPDF(x, AT.BW_Y if np.ptp(x) > 50 else 0.001)


class Interval:
    """The probability that a time bundled onto a schedule of period B fell in the interval that ends at its departure:
    x is the departure after an anchor, r the model-seed samples of the time before bundling after the same anchor,
    and the value is log P(x - B < r <= x) by the samples' distribution, mixed with a uniform tail of weight
    1 / (n + 1)."""

    def __init__(self, r, B):
        self.r = np.sort(r)
        self.B = B
        lo, hi = self.r[0], self.r[-1]
        w = max(Tailed.MARGIN * (hi - lo), 1e-3)
        self.support = (lo - w, hi + B + w)
        self.eps = 1.0 / (self.r.size + 1)
        self.tail = self.eps * B / (self.support[1] - self.support[0])

    def __call__(self, x):
        x = np.asarray(x, float)
        n = self.r.size
        p = (np.searchsorted(self.r, x, "right") - np.searchsorted(self.r, x - self.B, "right")) / n
        inside = (x >= self.support[0]) & (x <= self.support[1])
        with np.errstate(divide="ignore"):
            return np.where(inside, np.log((1 - self.eps) * p + self.tail), -np.inf)


class Window:
    """The record time after the later submission has reached every node, under a posting schedule of period B: the
    record posts at the next boundary, so any value in [0, B] has the same likelihood."""

    def __init__(self, B):
        self.B = B
        self.support = (-1e-6, B + 1e-6)

    def __call__(self, x):
        x = np.asarray(x, float)
        return np.where((x >= self.support[0]) & (x <= self.support[1]), 0.0, -np.inf)


def densities(cfg, seed0, runs=20):
    """On the model seeds: a submission after its content packet's arrival (sub); a submission after the estimate
    of when its node learned of quorum (Q); the record time after a submission has reached every node (F); a content
    packet's send time after its credential packet's (o); the record time after the later submission has reached
    every node (post). The model runs carry the cell's whole load (real and decoy together) as real traffic.

    Under registry-level bundling a submission leaves at the next boundary of a schedule shared by every content
    server, so its time tells only the bundle interval its ready time fell in: sub and Q are then Interval
    likelihoods of the ready time. Under the posting schedule the record posts at the next boundary after the later
    submission has reached every node, so post is a Window over one period, and F is fitted with BW_X-wide bins so it
    does not follow one run's schedule phases."""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate + cfg.decoy_rate, 0.2), measure_s=min(cfg.measure_s, 4 * 3600.0))
    bundle, posting = cfg.reg_bundle_s > 0, cfg.reg_post_s > 0
    sub, qq, f, so, pw = [], [], [], [], []
    for k in range(runs):
        run = S.simulate(mc, seed0 + k)
        s = run.subs
        ok = np.isfinite(s["posted"])
        u = s["posted"][ok]
        tf, ti = (s["ready_f"], s["ready_i"]) if bundle else (s["reg_f"], s["reg_i"])
        sub.append(np.r_[tf[ok] - s["arr_f"][ok], ti[ok] - s["arr_i"][ok]])
        f.append(np.r_[u - s["reach_f"][ok], u - s["reach_i"][ok]])
        pw.append(u - np.fmax(s["reach_f"][ok], s["reach_i"][ok]))
        lat = link_latency(run.events)
        idx = np.nonzero(ok)[0]
        for Cx in range(P.N_NODES):
            j = idx[s["C"][idx] == Cx]
            if j.size == 0:
                continue
            ke = known_estimate(s["cv2_a"][j], Cx, lat, run)
            qq.append(np.r_[tf[j] - ke[np.arange(j.size), s["F"][j]], ti[j] - ke[np.arange(j.size), s["I"][j]]])
        cs = run.events["t_send"]
        so.append(np.r_[cs[s["ev_ca"][:, 0]] - cs[s["ev_cred"][:, 0]], cs[s["ev_cb"][:, 0]] - cs[s["ev_cred"][:, 0]]])
    out = {}
    for name, x in (("sub", sub), ("Q", qq), ("F", f), ("o", so), ("post", pw)):
        x = np.concatenate(x)
        x = x[np.isfinite(x)]
        if bundle and name in ("sub", "Q"):
            out[name] = Interval(x, cfg.reg_bundle_s)
        elif posting and name == "post":
            out[name] = Window(cfg.reg_post_s)
        elif posting and name == "F":
            out[name] = Tailed(LT.EmpiricalLogPDF(x, AT.BW_X), x.size)
        else:
            out[name] = Tailed(_fit(x), x.size)
    return out


def score(run, m, dens, out, registry=False, tracer=None):
    """The tracer's (or the Registry Node's) table, on the observer's candidates and records. Every device with a
    triple of packets near the record is scored by the joint likelihood (_joint); the Registry Node fixes the two
    submissions to the record's own. A device without one is scored by its content packets' end points alone and
    ranks below."""
    from . import devscore as DS
    cand, rec, base, shuf = out["_cand"], out["_rec"], out["_base"], out["_shuf"]
    tr = tracer or Tracer(run, dens)
    E, TY, TT, WW = tr.end_points(cand["ev"])
    tr._E, tr._TY, tr._TT, tr._WW = E, TY, TT, WW
    logW = np.log(np.maximum(WW, 1e-300))
    u, n = rec["u"], rec["sub"].size
    s = run.subs
    lo, hi = AT._band(u, m.pdf["g"])
    col = DS.Collector(n, cand["dev"])
    pF = dens["F"]
    if registry:
        mine = np.c_[s["ev_reg_f"][rec["sub"]], s["ev_reg_i"][rec["sub"]]]

    def fn(rows, k0, k1):
        if registry:
            hit = (E[None, k0:k1, :] == mine[rows, 0][:, None, None]) | (E[None, k0:k1, :] == mine[rows, 1][:, None, None])
            v = np.where(hit, logW[None, k0:k1, :], -np.inf)
        else:
            y = u[rows][:, None, None] - TT[None, k0:k1, :]
            v = pF(np.where(np.isfinite(y), y, -1e9)) + logW[None, k0:k1, :]
        v = np.where(TY[None, k0:k1, :] == 1, v, -np.inf)
        mx = np.max(v, axis=2, keepdims=True)
        mxf = np.where(np.isfinite(mx), mx, 0.0)
        with np.errstate(divide="ignore"):
            o_ = np.log(np.sum(np.exp(v - mxf), axis=2)) + mxf[:, :, 0]
        return dict(trt=np.where(np.isfinite(mx[:, :, 0]), o_, -np.inf))

    AT.score_blocks(lo, hi, cand, fn, dict(sub=rec["sub"], dev=rec["dev"]), ("trt",),
                    extra=lambda nm, rows, a, b, W, is_t: col(rows, a, b, W))
    floor = np.log(1e-6)
    labs, scs = [], []
    for i in range(n):
        lab0, st = col.get(i)
        band = np.arange(np.searchsorted(cand["t"], lo[i]), np.searchsorted(cand["t"], hi[i]))
        dv, cnt = np.unique(cand["dev"][band], return_counts=True)
        lab = np.union1d(lab0, dv[cnt >= 3])                    # every device with a triple near the record
        score_ = np.full(lab.size, floor - 20.0)
        score_[np.searchsorted(lab, lab0)] = np.logaddexp(st, floor) - 20.0
        if lab.size:
            score_ = _joint(score_, lab, band, cand, tr, dens, u[i], fixed=mine[i] if registry else None)
        labs.append(lab)
        scs.append(score_)
    t = DS.table(labs, scs, rec, np.arange(n), np.zeros(n), base, rec["dev"], shuf)
    return t, tr


def _group_prefix(A, key):
    """For each column f (in the given order), the sum of A over earlier columns with the same key. A: (R, F)."""
    o = np.argsort(key, kind="stable")
    cs = np.cumsum(A[:, o], axis=1)
    k = key[o]
    start = np.r_[0, np.nonzero(k[1:] != k[:-1])[0] + 1]
    base = np.zeros_like(cs)
    first = np.zeros(k.size, np.int64)
    first[start] = start
    first = np.maximum.accumulate(first)
    prev = np.where(first[None, :] > 0, cs[:, np.maximum(first - 1, 0)], 0.0)
    out = np.empty_like(cs)
    out[:, o] = cs - A[:, o] - prev
    return out


def _joint(score_, lab, ks, cand, tr, dens, u, fixed=None):
    """The joint likelihood of the record under every device with at least three packets near it: over the device's
    triples of packets (any of the three as the credential packet), the reply its credential packet leads to, the
    submissions its content packets lead to (at two different nodes), the quorum timing of those submissions after
    the reply, and the record's time after the later submission. Every end point a packet keeps is used. For one
    credential packet and reply, the sum over pairs of submissions is taken in order of flood time with prefix sums,
    so its cost is linear in the submissions. fixed: the record's two submissions, when they are known (the Registry
    Node); the record-time term is then dropped. A device with no triple, or none the densities allow, ranks below
    every device with one."""
    if ks.size < 3:
        return score_
    E, TY, ZZ, TS, TT, WW = tr._E, tr._TY, tr.ZZ, tr.TS, tr._TT, tr._WW
    pQ, po, pp = dens["Q"], dens["o"], dens["post"]
    post_lo = pp.support[0]
    dv = cand["dev"][ks]
    devs, cnt = np.unique(dv, return_counts=True)
    reps, frs = {}, {}

    def packet(k):
        if k not in reps:
            sel = (TY[k] == 2) & (E[k] >= 0)
            kr = np.array([tr.ke_row.get(int(e), -1) for e in E[k][sel]], np.int64)
            ok = kr >= 0
            reps[k] = (kr[ok], np.log(WW[k][sel][ok]))
            if fixed is None:
                sel = (TY[k] == 1) & (u - TT[k] >= post_lo)        # a submission that reached every node before the record
            else:
                sel = (TY[k] == 1) & np.isin(E[k], fixed)
            frs[k] = (ZZ[k][sel], TS[k][sel], TT[k][sel], np.log(WW[k][sel]))
        return reps[k], frs[k]
    out = score_.copy()
    got = []
    for d in devs[cnt >= 3]:
        j = ks[dv == d]
        t = cand["t"][j]
        F = [packet(k)[1] for k in j]
        nf = np.array([f[0].size for f in F])
        if (nf > 0).sum() < 2:
            continue
        z_all = np.concatenate([f[0] for f in F]).astype(np.int64)
        ts_all = np.concatenate([f[1] for f in F])
        r_all = np.concatenate([f[2] for f in F])
        lw_all = np.concatenate([f[3] for f in F])
        pk_all = np.repeat(np.arange(j.size), nf)
        o = np.argsort(r_all, kind="stable")                      # in order of flood time
        z_all, ts_all, r_all, lw_all, pk_all = z_all[o], ts_all[o], r_all[o], lw_all[o], pk_all[o]
        lpp = pp(u - r_all) if fixed is None else np.zeros(r_all.size)
        tot = []
        for c in range(j.size):
            kr, lcw = packet(j[c])[0]
            if kr.size == 0:
                continue
            lo_ = po(t - t[c])                                     # (packets,)
            # each credential packet spreads one unit of probability over the pairs that could be its content
            # packets, so a device with more packets near the record gains only by having more transactions
            e_ = np.exp(np.delete(lo_, c))
            zc = 0.5 * (e_.sum() ** 2 - (e_ ** 2).sum())
            if not zc > 0:
                continue
            lo_ = lo_ - 0.5 * np.log(zc)
            keep = (pk_all != c) & np.isfinite(lo_[pk_all])
            if keep.sum() < 2:
                continue
            z, pk = z_all[keep], pk_all[keep]
            la = lo_[pk] + lw_all[keep] + pQ(ts_all[keep][None, :] - tr.ke[kr][:, z])     # (R, F)
            m_ = np.max(la)
            if not np.isfinite(m_):
                continue
            A = np.exp(la - m_)
            earlier = np.cumsum(A, axis=1) - A
            S_ = (earlier - _group_prefix(A, z) - _group_prefix(A, pk) + _group_prefix(A, z * (j.size + 1) + pk))
            S_ = np.maximum(S_, 0.0)
            lp = lpp[keep]
            with np.errstate(divide="ignore"):
                v = np.log(A) + np.log(S_) + lp[None, :] + 2 * m_     # (R, F): f the later submission
            v = v + lcw[:, None]
            mv = np.max(v)
            if np.isfinite(mv):
                tot.append(mv + np.log(np.exp(v - mv).sum()))
        if tot:
            got.append((d, np.logaddexp.reduce(tot)))
    if got:
        base = min(v for _, v in got) - 50.0
        out = np.minimum(out, base)
        for d, v in got:
            out[np.searchsorted(lab, d)] = v
    return out

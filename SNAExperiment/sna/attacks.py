"""Record-to-device linking: vantages, wire extraction, likelihood models, and the scoring of one run.

The harm Semantic Non-Assembly guards against is naming the device behind a public registry record.
Every vantage therefore starts from a registry record and names a device submission. A record's
two submissions (F's and I's) are paired, because the public record names both servers. The
record is timed at their midpoint. Candidates are the device-originated first-hop packets on the
wire, three per capture, decoy sources' packets included.

Each vantage's own exact knowledge enters the likelihood of "record r came from candidate k":

  baseline              g(u_r - s_k): record time against the packet's departure s_k
  first hop (A or D/G)  its own forward time replaces the departure for packets it relayed
  content server        adds its exact content arrival a_r for records it submitted: the joint
                        density of the record time and a_r - s_k
  validator             names device identities directly: its candidates are its own replies
  gatekeeper            sums over its own postings j: sum_j P(k -> j) p(r | j)
  credential processor  sums over its own transactions, mixed with the baseline for traffic
                        that did not pass through it

Success is scored at two levels: the device (primary; the posterior summed over each source's
packets, since a source address is visible on the wire) and the submission (the chosen packet
belongs to the record's own capture). Each vantage is paired with the baseline on the same
records. ANALYSIS_PLAN.md, amendment A.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from . import lottery as LT
from . import params as P
from . import sim as S

VANTAGES = ("baseline", "first_hop_cred", "first_hop_content", "cred_processor", "content_server",
            "validator", "gatekeeper")
CAN_TELL = ("cred_processor", "validator", "gatekeeper")
CANNOT_TELL = ("baseline", "first_hop_cred", "first_hop_content", "content_server")
LABEL = {"baseline": "Baseline", "first_hop_cred": "First hop, credential",
         "first_hop_content": "First hop, content", "cred_processor": "Credential processor",
         "content_server": "Content server", "validator": "Validator", "gatekeeper": "Gatekeeper"}
LEVELS = ("dev", "sub")
BW = 0.5                  # histogram bin width (s) of every delay model
BW_FINE = 0.05            # bin width when every hold is off (sensitivity control)
MAX_CELLS = 3_000_000     # rows x candidates per dense block
T_GRID = np.exp(np.linspace(np.log(0.1), np.log(10.0), 11))   # temperatures for calibrated confidence
_INT_MAX = np.iinfo(np.int32).max


# =========================================================================== wire extraction
def registry_answers(run, pools):
    """Registry submissions as a passive observer finds them: gossip frames (Noise record type,
    the gossip frame size) that one node sends to nearly every other node within 2 ms are a
    flood-publish burst. Submissions leaving one node on the same clock tick share a burst; the
    burst then carries one frame per submission to every peer, so the number of submissions is
    the smallest per-peer frame count. Returns answer times (sorted), the transaction each belongs
    to (truth, -1 if none) and each transaction's answers."""
    ev, N = run.events, P.N_NODES
    idx = np.nonzero((ev["rtype"] == P.RT_NOISE) & (ev["size"] == pools.gossip_wire))[0]
    t, src = ev["t_send"][idx], ev["src"][idx]
    o = np.lexsort((t, src))
    idx, t, src = idx[o], t[o], src[o]
    new = np.ones(idx.size, bool)
    new[1:] = (src[1:] != src[:-1]) | (np.diff(t) > 2e-3)
    cid = np.cumsum(new) - 1
    starts = np.nonzero(new)[0]
    nc = starts.size
    per_dst = np.bincount(cid * N + ev["dst"][idx].astype(np.int64), minlength=nc * N).reshape(nc, N)
    per_dst[np.arange(nc), src[starts]] = np.iinfo(per_dst.dtype).max
    k = per_dst.min(1)
    k = np.where(np.bincount(cid, minlength=nc) >= N - 4, k, 0)
    leg = ev["leg"][idx]
    is_org = (leg == S.REG_F) | (leg == S.REG_I)
    pairs = np.unique(np.c_[cid[is_org], ev["sub"][idx][is_org]], axis=0)
    t_c = t[starts]
    col_t, col_sub = [], []
    rank = np.zeros(nc, np.int64)
    for c_, sb in pairs:
        if rank[c_] < k[c_]:
            col_t.append(t_c[c_])
            col_sub.append(sb)
        rank[c_] += 1
    extra = np.maximum(k - rank, 0)
    col_t = np.r_[np.array(col_t, float), np.repeat(t_c, extra)]
    col_sub = np.r_[np.array(col_sub, np.int64), np.full(int(extra.sum()), -1, np.int64)]
    o = np.argsort(col_t, kind="stable")
    col_t, col_sub = col_t[o], col_sub[o]
    return col_t, col_sub, answers_of(col_sub, run.subs["t0"].shape[0])


def answers_of(col_sub, n_sub):
    """(n_sub, k) answer indices belonging to each transaction, -1 padded."""
    idx = np.nonzero(col_sub >= 0)[0]
    idx = idx[np.argsort(col_sub[idx], kind="stable")]
    subs = col_sub[idx]
    cnt = np.bincount(subs, minlength=n_sub)
    k = max(int(cnt.max()) if cnt.size else 1, 1)
    out = np.full((n_sub, k), -1, np.int64)
    first = np.concatenate([[0], np.cumsum(cnt)[:-1]])
    out[subs, np.arange(idx.size) - first[subs]] = idx
    return out


def records(run, pools):
    """Registry records: a transaction whose two submissions were both found. The public record
    names both submitting servers, so the observer pairs them; u is their midpoint."""
    col_t, _, tc = registry_answers(run, pools)
    ok = (tc >= 0).sum(1) >= 2
    sub = np.nonzero(ok)[0]
    u = 0.5 * (col_t[tc[sub, 0]] + col_t[tc[sub, 1]])
    return dict(sub=sub, u=u, dev=run.subs["src"][sub])


def candidates(run, pools):
    """Device submissions on the wire, grouped by source. Packets are relay-class application
    records from an external host to a pool node; an external source that ever sends anything else
    (a handshake, a DNS lookup, a record outside the class) is not a device and is dropped. Each
    source's packets are grouped greedily in time order: a group holds up to three packets within
    one device hold (310 s) of its first. A group is timed at its members' mean send time.
    Returns groups sorted by that time, with truth labels (sub = -1 for a mixed group) and, per
    member, the first hop, the arrival and the first hop's forward time."""
    ev, s = run.events, run.subs
    lo, hi = P.PAD_MIN + pools.tls13_overhead, P.PAD_MAX + pools.tls13_overhead
    ext = ev["src"] == S.EXT
    relay = ext & (ev["dst"] < P.N_NODES) & (ev["rtype"] == P.RT_APPDATA) & (ev["size"] >= lo) & (ev["size"] <= hi)
    bad_src = np.unique(ev["ext_src"][ext & ~relay])
    pk = np.nonzero(relay & ~np.isin(ev["ext_src"], bad_src))[0]
    src = ev["ext_src"][pk].astype(np.int64)
    t = ev["t_send"][pk]
    o = np.lexsort((t, src))
    pk, src, t = pk[o], src[o], t[o]
    gid = np.empty(pk.size, np.int64)
    g, first, size = -1, 0.0, 3
    span = P.TICK_S * (P.MAX_TICKS + 1)
    for i in range(pk.size):                         # greedy grouping per source
        if i == 0 or src[i] != src[i - 1] or size >= 3 or t[i] - first > span:
            g += 1
            first, size = t[i], 0
        gid[i] = g
        size += 1
    n_g = g + 1
    fwd_of = np.full(ev["t_send"].shape[0], -1, np.int64)
    for key in ("ev_cred", "ev_ca", "ev_cb"):
        fwd_of[s[key][:, 0]] = s[key][:, 1]
    cnt = np.bincount(gid, minlength=n_g)
    slot = np.arange(pk.size) - np.r_[0, np.cumsum(cnt)[:-1]][gid]
    mem = np.full((n_g, 3), -1, np.int64)
    mem[gid, slot] = pk
    ok = mem >= 0
    m0 = np.maximum(mem, 0)
    tm = np.where(ok, ev["t_send"][m0], np.nan)
    gt = np.nanmean(tm, 1)
    psub = np.where(ok & (ev["kind"][m0] == S.K_BIRTHMARK), ev["sub"][m0], -1)
    pure = (psub[:, 0] >= 0) & np.all((psub == psub[:, :1]) | ~ok, 1)
    f = fwd_of[m0]
    out = dict(t=gt, sub=np.where(pure, psub[:, 0], -1).astype(np.int64), msub=psub.astype(np.int64),
               dev=src[np.r_[0, np.cumsum(cnt)[:-1]]],
               n=cnt, node=np.where(ok, ev["dst"][m0], -1).astype(np.int64),
               hold=np.where(ok & (f >= 0), ev["t_send"][np.maximum(f, 0)] - ev["t_arr"][m0], np.nan))
    o = np.argsort(out["t"], kind="stable")
    return {k: x[o] for k, x in out.items()}


# =========================================================================== models
class CondPDF:
    """log p(y | x) from a 2D histogram of true pairs, shrunk towards the marginal density of y
    (K_SHRINK pseudo-samples per x bin), so a sparse or unseen x bin falls back to the marginal.
    y outside the marginal's support is -inf."""
    K_SHRINK = 20.0

    def __init__(self, x, y, marg: "LT.EmpiricalLogPDF", bw_x):
        x, y = np.asarray(x, float), np.asarray(y, float)
        ok = np.isfinite(x) & np.isfinite(y)
        x, y = x[ok], y[ok]
        self.marg, self.bx = marg, bw_x
        self.xlo = x.min()
        nx = int(np.ceil((x.max() - self.xlo) / bw_x)) + 1
        ny = marg.logd.shape[0]
        xi = np.clip(((x - self.xlo) / bw_x).astype(np.int64), 0, nx - 1)
        yi = np.clip(np.floor((y - marg.lo) / marg.bw).astype(np.int64), 0, ny - 1)
        c = np.bincount(xi * ny + yi, minlength=nx * ny).reshape(nx, ny).astype(float)
        cx = c.sum(1, keepdims=True)
        prior = np.exp(marg.logd)[None, :] * marg.bw
        self.logT = np.log((c + self.K_SHRINK * prior) / (cx + self.K_SHRINK) / marg.bw)
        self.nx = nx
        self.support = marg.support
        self.x_support = (self.xlo, self.xlo + nx * bw_x)

    def __call__(self, x, y):
        x, y = np.asarray(x, float), np.asarray(y, float)
        x, y = np.broadcast_arrays(x, y)
        yi = np.floor((y - self.marg.lo) / self.marg.bw).astype(np.int64)
        oky = (y >= self.support[0]) & (y <= self.support[1]) & (yi >= 0) & (yi < self.marg.logd.shape[0])
        xi = np.floor((x - self.xlo) / self.bx).astype(np.int64)
        okx = np.isfinite(x) & (xi >= 0) & (xi < self.nx)
        out = np.full(y.shape, -np.inf)
        both = oky & okx
        out[both] = self.logT[xi[both], yi[both]]
        m = oky & ~okx
        out[m] = self.marg.logd[yi[m]]
        return out


@dataclass
class Models:
    pdf: dict = field(default_factory=dict)
    mc_runs: int = 0
    samples: dict = field(default_factory=dict)


BW_Y = 1.0                # bin width (s) of the record-time density y = u - s
BW_X = 10.0               # bin width (s) of a vantage's extra observation x


def _true_samples(run, pools, acc):
    """Every true (record, own submission group) pair: y = u - s (s: the group's mean departure)
    and each vantage's extra observation x. Groups come from the same extraction as scoring."""
    s = run.subs
    rec = records(run, pools)
    cand = candidates(run, pools)
    pure = cand["sub"] >= 0
    gi = np.full(s["t0"].shape[0], -1, np.int64)
    gi[cand["sub"][pure]] = np.nonzero(pure)[0]
    k = gi[rec["sub"]]
    ok = k >= 0
    sub, u, k = rec["sub"][ok], rec["u"][ok], k[ok]
    sg = cand["t"][k]
    y = u - sg
    add = lambda name, x: acc.setdefault(name, []).append(np.asarray(x, float).ravel())  # noqa: E731
    add("y", y)
    # first hop: own hold of each member (a first hop holds exactly one of the three)
    add("fh_x", cand["hold"][k].ravel())
    add("fh_y", np.repeat(y, 3))
    # content server: content arrival at F and at I, relative to the group time
    add("cs_x", np.r_[s["arr_f"][sub] - sg, s["arr_i"][sub] - sg])
    add("cs_y", np.r_[y, y])
    # gatekeeper: each of the three postings relative to the group time
    add("gk_x", (s["posts"][sub] - sg[:, None]).ravel())
    add("gk_y", np.repeat(y, 3))
    # credential processor: its fan-out median relative to the group time
    add("c_x", np.sort(s["gk_send"][sub], 1)[:, 1] - sg)
    add("c_y", y)
    # validator: record time against its own reply send
    add("gV", u - run.events["t_send"][s["ev_cv2"][sub]])


def build_models(cfg: P.Config, pools, seed0=1_000_000_000, min_samples=300_000, max_runs=200) -> Models:
    """Monte Carlo of the protocol under the configuration attacked (background off, which enters
    none of these delays), on seeds disjoint from every evaluation seed. Delays do not depend on
    volume (no queueing), so one set of models serves every volume."""
    mc = cfg.with_(background_enabled=False, nonblending_enabled=False, decoy_rate=0.0,
                   real_rate=max(cfg.real_rate, 0.2))
    fine = not cfg.lottery_enabled
    bw_y, bw_x = (0.05, 0.5) if fine else (BW_Y, BW_X)
    acc = {}
    k = 0
    while True:
        _true_samples(S.simulate(mc, seed0 + k, pools), pools, acc)
        k += 1
        if (sum(x.size for x in acc["y"]) >= min_samples and k >= 3) or k >= max_runs:
            break
    cat = {n: np.concatenate(v) for n, v in acc.items()}
    m = Models(mc_runs=k, samples={n: int(np.isfinite(v).sum()) for n, v in cat.items()})
    g = LT.EmpiricalLogPDF(cat["y"], bw_y)
    m.pdf["g"] = g
    for name in ("fh", "cs", "gk", "c"):
        m.pdf[name] = CondPDF(cat[f"{name}_x"], cat[f"{name}_y"], g, bw_x)
        xs = cat[f"{name}_x"]
        m.pdf[name + "_q"] = LT.EmpiricalLogPDF(xs[np.isfinite(xs)], bw_x)     # marginal of x
    m.pdf["gV"] = LT.EmpiricalLogPDF(cat["gV"], bw_y)
    return m


# =========================================================================== block scoring engine
def _lse(x, axis=1):
    m = np.max(x, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0.0)
    with np.errstate(divide="ignore"):
        return (np.log(np.sum(np.exp(x - m), axis=axis, keepdims=True)) + m).squeeze(axis)


def _stats(W, lab, is_t, out, rows, lvl, want_lse):
    """Per-row decision statistics of a dense score block W (rows x m): column labels lab, and
    is_t (rows x m) marking the columns that are right for each row."""
    o = out[lvl]
    fin = np.isfinite(W)
    o["n_feas"][rows] = fin.sum(1)
    if W.shape[1] == 0:
        return
    ar = np.arange(W.shape[0])
    am = np.argmax(W, 1)
    top1 = W[ar, am]
    o["top1"][rows] = top1
    o["pick"][rows] = np.where(np.isfinite(top1), lab[am], -1)
    o["correct"][rows] = np.isfinite(top1) & is_t[ar, am]
    if W.shape[1] >= 2:
        o["top2"][rows] = -np.partition(-W, 1, axis=1)[:, 1]
    st = np.max(np.where(is_t, W, -np.inf), 1)
    o["s_true"][rows] = st
    o["n_true"][rows] = (is_t & fin).sum(1)
    o["rank"][rows] = np.where(np.isfinite(st), 1 + (W > st[:, None]).sum(1), _INT_MAX)
    if want_lse:
        top = np.where(np.isfinite(top1), top1, 0.0)
        for i, T in enumerate(T_GRID):
            o["lse"][rows, i] = _lse(W / T) - top / T


def _aggregate(W, lab):
    """Log of the summed posterior per label (columns grouped by label)."""
    u, inv = np.unique(lab, return_inverse=True)
    order = np.argsort(inv, kind="stable")
    starts = np.r_[0, np.nonzero(np.diff(inv[order]))[0] + 1]
    M = np.max(W, 1)
    Mf = np.where(np.isfinite(M), M, 0.0)
    E = np.exp(W - Mf[:, None])
    with np.errstate(divide="ignore"):
        agg = np.log(np.add.reduceat(E[:, order], starts, axis=1)) + Mf[:, None]
    agg[~np.isfinite(M)] = -np.inf
    return agg, u


def score_blocks(t_lo, t_hi, cand, block_fn, truth, max_cells=MAX_CELLS):
    """Score every row against the candidates whose time lies in [t_lo, t_hi) of that row.

    cand: dict with sorted "t", "sub" (the group's capture, -1 if mixed), "msub" (each member's
    capture: a pick is right at the submission level if any member belongs to the record's
    capture) and "dev" labels. block_fn(rows, k0, k1) returns the
    dense log-likelihood block (len(rows), k1 - k0). truth: dict level -> (n,) true label.
    Returns per-level arrays: pick, top1, top2, s_true, rank, n_feas, n_true, lse."""
    n = t_lo.shape[0]
    out = {lvl: dict(pick=np.full(n, -1, np.int64), correct=np.zeros(n, bool), top1=np.full(n, -np.inf), top2=np.full(n, -np.inf),
                     s_true=np.full(n, -np.inf), rank=np.full(n, _INT_MAX, np.int32),
                     n_feas=np.zeros(n, np.int32), n_true=np.zeros(n, np.int32),
                     lse=np.full((n, T_GRID.size), np.nan)) for lvl in LEVELS}
    if n == 0:
        return _finish(out)
    ct = cand["t"]
    k0s = np.searchsorted(ct, t_lo, "left")
    k1s = np.maximum(np.searchsorted(ct, t_hi, "left"), k0s)
    order = np.argsort(t_lo, kind="stable")
    i = 0
    while i < n:
        lo, hi = k0s[order[i]], k1s[order[i]]
        maxw = hi - lo
        j = i + 1
        while j < n:                       # grow the block while it stays dense
            nlo, nhi = min(lo, k0s[order[j]]), max(hi, k1s[order[j]])
            mw = max(maxw, k1s[order[j]] - k0s[order[j]])
            if (nhi - nlo) * (j - i + 1) > max_cells or (nhi - nlo) > 2 * max(mw, 1):
                break
            lo, hi, maxw = nlo, nhi, mw
            j += 1
        rows = order[i:j]
        i = j
        if hi <= lo:
            continue
        with np.errstate(divide="ignore", invalid="ignore"):
            W = block_fn(rows, lo, hi)
        cols = np.arange(lo, hi)
        inb = (cols[None, :] >= k0s[rows][:, None]) & (cols[None, :] < k1s[rows][:, None])
        W = np.where(inb & np.isfinite(W), W, -np.inf)
        ms = cand["msub"][lo:hi]
        is_t = (ms[None, :, :] == truth["sub"][rows][:, None, None]).any(2) if ms.ndim == 2 else \
            ms[None, :] == truth["sub"][rows][:, None]
        _stats(W, cand["sub"][lo:hi], is_t, out, rows, "sub", False)
        Wd, labd = _aggregate(W, cand["dev"][lo:hi])
        _stats(Wd, labd, labd[None, :] == truth["dev"][rows][:, None], out, rows, "dev", True)
    return _finish(out)


def _finish(out):
    for o in out.values():
        o["lse"] = np.where(np.isfinite(o["lse"]), o["lse"], np.nan).astype(np.float16)
    return out


def _random_rate(o, lvl):
    """Chance of a uniformly random pick among the feasible candidates being right: true packets
    over feasible packets (submission level), one over feasible devices when the true device is
    feasible (device level)."""
    nf = np.maximum(o["n_feas"], 1)
    if lvl == "sub":
        return np.where(o["n_feas"] > 0, o["n_true"] / nf, 0.0)
    return np.where((o["n_feas"] > 0) & (o["n_true"] > 0), 1.0 / nf, 0.0)


# =========================================================================== vantage block functions
def _band(u, pdf):
    return u - pdf.support[1], u - pdf.support[0] + 1e-9


class _MixtureV:
    """Per-candidate mixture of conditional record-time densities over one server's own events j:

        V_k(y) = pi * sum_j w_kj real_j p(y | x_kj) + (1 - pi [Z_k > 0]) g(y),
        x_kj = e_j - s_k,  w_kj = q(x_kj) / Z_k,  Z_k = sum_j q(x_kj)

    e_j: the server's event times (sorted); real_j: 1 for a real transaction (a decoy never
    produces a record). With pi = 1 the baseline term vanishes. The (candidate, event) pairs are
    computed per chunk of candidates and cached while scoring moves forward in time. A block is
    evaluated directly on its (row, candidate) pairs when that is cheaper than tabulating V_k over
    every y bin, and through the tabulated V_k otherwise; both give the same values."""
    CH = 1024

    def __init__(self, cand_t, e, real, cond: CondPDF, q, g, pi=1.0):
        self.ct, self.e, self.real, self.cond, self.q, self.g, self.pi = cand_t, e, real, cond, q, g, pi
        self.Tp = np.exp(cond.logT)                       # (nx, ny) conditional densities
        self.gp = np.exp(g.logd)                          # (ny,) marginal density
        self.pairs, self.V = {}, {}

    def _evict(self, c):
        for d in (self.pairs, self.V):
            for k in [k for k in d if k < c - 2]:
                del d[k]

    def _pair(self, c):
        """(xi, w, outx, Z) for chunk c: event x bin, normalised real weight (0 where the x bin is
        outside the table), weight whose x falls outside the table, and Z_k."""
        if c in self.pairs:
            return self.pairs[c]
        self._evict(c)
        s = self.ct[c * self.CH:(c + 1) * self.CH]
        K = s.size
        xi = np.zeros((K, 1), np.int64)
        w = np.zeros((K, 1))
        outx, Z = np.zeros(K), np.zeros(K)
        if self.e.size and K:
            a = np.searchsorted(self.e, s + self.q.support[0], "left")
            b = np.searchsorted(self.e, s + self.q.support[1], "right")
            n = b - a
            B = int(n.max())
            if B > 0:
                j = np.minimum(a[:, None] + np.arange(B)[None, :], self.e.size - 1)
                valid = np.arange(B)[None, :] < n[:, None]
                x = self.e[j] - s[:, None]
                qw = np.where(valid, np.exp(self.q(x)), 0.0)
                Z = qw.sum(1)
                wr = qw * self.real[j] / np.where(Z > 0, Z, 1.0)[:, None]
                xi = np.floor((x - self.cond.xlo) / self.cond.bx).astype(np.int64)
                inx = valid & (xi >= 0) & (xi < self.cond.nx)
                outx = np.where(valid & ~inx, wr, 0.0).sum(1)
                w = np.where(inx, wr, 0.0)
                xi = np.clip(xi, 0, self.cond.nx - 1)
        self.pairs[c] = (xi, w, outx, Z)
        return self.pairs[c]

    def _vtab(self, c):
        if c in self.V:
            return self.V[c]
        xi, w, outx, Z = self._pair(c)
        K = Z.size
        kk = np.broadcast_to(np.arange(K)[:, None], xi.shape)
        M = np.bincount((kk * self.cond.nx + xi).ravel(), weights=w.ravel(),
                        minlength=K * self.cond.nx).reshape(K, self.cond.nx)
        V = self.pi * (M @ self.Tp + outx[:, None] * self.gp[None, :])
        V += (1.0 - self.pi * (Z > 0))[:, None] * self.gp[None, :]
        self.V[c] = V
        return V

    def block(self, u, k0, k1):
        """log V_k(u_r - s_k) for rows u (r) and candidates k0..k1-1."""
        g = self.g
        ny = self.gp.size
        y = u[:, None] - self.ct[None, k0:k1]
        yi = np.floor((y - g.lo) / g.bw).astype(np.int64)
        ok = (y >= g.support[0]) & (y <= g.support[1]) & (yi >= 0) & (yi < ny)
        yi = np.clip(yi, 0, ny - 1)
        vals = np.empty(y.shape)
        for c in range(k0 // self.CH, (k1 - 1) // self.CH + 1):
            c0, c1 = max(k0, c * self.CH), min(k1, (c + 1) * self.CH)
            loc = slice(c0 - c * self.CH, c1 - c * self.CH)
            cols = slice(c0 - k0, c1 - k0)
            xi, w, outx, Z = self._pair(c)
            B = xi.shape[1]
            yb = yi[:, cols]
            if u.size * B < self.Tp.size or c in self.V:
                if c in self.V:
                    V = self.V[c][loc]
                    vals[:, cols] = V[np.arange(c1 - c0)[None, :], yb]
                    continue
                xs, ws = xi[loc], w[loc]                              # (k, B)
                mix = np.zeros(yb.shape)
                for r0 in range(0, u.size, max(1, 2_000_000 // max(1, (c1 - c0) * B))):
                    rs = slice(r0, r0 + max(1, 2_000_000 // max(1, (c1 - c0) * B)))
                    mix[rs] = (ws[None, :, :] * self.Tp[xs[None, :, :], yb[rs][:, :, None]]).sum(2)
                gy = self.gp[yb]
                vals[:, cols] = self.pi * (mix + outx[loc][None, :] * gy) + (1.0 - self.pi * (Z[loc] > 0))[None, :] * gy
            else:
                V = self._vtab(c)[loc]
                vals[:, cols] = V[np.arange(c1 - c0)[None, :], yb]
        with np.errstate(divide="ignore"):
            return np.where(ok, np.log(vals), -np.inf)


def _vantage_rows(v, run, rec):
    """(record index, group, extra) for every scored record the vantage took part in."""
    s = run.subs
    sub = rec["sub"]
    n = sub.size
    idx = np.arange(n)
    if v in ("baseline", "validator"):
        return idx, np.zeros(n, int), {}
    if v == "first_hop_cred":
        return idx, s["A"][sub], {}
    if v == "first_hop_content":
        return np.r_[idx, idx], np.r_[s["D"][sub], s["G"][sub]], {}
    if v == "cred_processor":
        return idx, s["C"][sub], {}
    if v == "content_server":
        return np.r_[idx, idx], np.r_[s["F"][sub], s["I"][sub]], dict(a=np.r_[s["arr_f"][sub], s["arr_i"][sub]])
    if v == "gatekeeper":
        return np.tile(idx, 3), np.repeat(run.gk_set, n), dict(j=np.repeat(np.arange(3), n))
    raise KeyError(v)


def score_vantage(v, run, rec, cand, m: Models, base):
    """Score one vantage on its rows. Returns (row record index, group, per-level output)."""
    pdf, s, ev = m.pdf, run.subs, run.events
    ri, grp, extra = _vantage_rows(v, run, rec)
    u = rec["u"][ri]
    truth = dict(sub=rec["sub"][ri], dev=rec["dev"][ri])
    g = pdf["g"]
    lo, hi = _band(u, g)
    if v == "baseline":
        return ri, grp, base
    if v in ("first_hop_cred", "first_hop_content"):
        fh = pdf["fh"]

        def fn(rows, k0, k1):
            y = u[rows][:, None] - cand["t"][None, k0:k1]
            match = cand["node"][None, k0:k1, :] == grp[rows][:, None, None]      # (r, k, member)
            own = match.any(2)
            hold = np.nansum(np.where(match, cand["hold"][None, k0:k1, :], 0.0), 2)
            return np.where(own, fh(np.where(own, hold, np.nan), y), g(y))
        return ri, grp, score_blocks(lo, hi, cand, fn, truth, max_cells=MAX_CELLS // 3)
    if v == "content_server":
        cs, csq = pdf["cs"], pdf["cs_q"]
        a = extra["a"]

        def fn(rows, k0, k1):
            # joint density p(y, x) = p(y | x) q(x): the content arrival's offset x depends on
            # which candidate is the source, so it carries evidence of its own
            sk = cand["t"][None, k0:k1]
            x = a[rows][:, None] - sk
            return cs(x, u[rows][:, None] - sk) + csq(x)
        return ri, grp, score_blocks(lo, hi, cand, fn, truth)
    if v == "validator":
        real = ~s["decoy"]
        t = ev["t_send"][s["ev_cv2"]][real]
        o = np.argsort(t, kind="stable")
        vsub = np.nonzero(real)[0][o].astype(np.int64)
        vc = dict(t=t[o], sub=vsub, msub=vsub, dev=s["src"][real][o].astype(np.int64))
        gV = pdf["gV"]

        def fn(rows, k0, k1):
            return gV(u[rows][:, None] - vc["t"][None, k0:k1])
        vlo, vhi = _band(u, gV)
        return ri, grp, score_blocks(vlo, vhi, vc, fn, truth)
    if v == "gatekeeper":
        outs = []
        for j in range(3):
            sel = np.nonzero(extra["j"] == j)[0]
            post = s["posts"][:, j]
            o = np.argsort(post, kind="stable")
            mix = _MixtureV(cand["t"], post[o], (~s["decoy"][o]).astype(float), pdf["gk"], pdf["gk_q"], g)
            us = u[sel]
            outs.append((sel, score_blocks(lo[sel], hi[sel], cand, lambda rows, k0, k1, us=us, mix=mix: mix.block(us[rows], k0, k1),
                                           dict(sub=truth["sub"][sel], dev=truth["dev"][sel]))))
        return ri, grp, _merge(outs, ri.size)
    if v == "cred_processor":
        pi = 1.0 / (P.N_NODES - P.N_GATEKEEPERS)
        m_all = np.sort(s["gk_send"], 1)[:, 1]
        outs = []
        for X in np.unique(grp):
            sel = np.nonzero(grp == X)[0]
            mine = np.nonzero(s["C"] == X)[0]
            mine = mine[np.argsort(m_all[mine], kind="stable")]
            mix = _MixtureV(cand["t"], m_all[mine], (~s["decoy"][mine]).astype(float), pdf["c"], pdf["c_q"], g, pi=pi)
            us = u[sel]
            outs.append((sel, score_blocks(lo[sel], hi[sel], cand, lambda rows, k0, k1, us=us, mix=mix: mix.block(us[rows], k0, k1),
                                           dict(sub=truth["sub"][sel], dev=truth["dev"][sel]))))
        return ri, grp, _merge(outs, ri.size)
    raise KeyError(v)


def _merge(parts, n):
    out = {}
    for lvl in LEVELS:
        tmpl = parts[0][1][lvl]
        o = {k: np.empty((n,) + x.shape[1:], x.dtype) for k, x in tmpl.items()}
        for sel, res in parts:
            for k in o:
                o[k][sel] = res[lvl][k]
        out[lvl] = o
    return out


def scored_mask(run, sub):
    t0 = run.subs["t0"][sub]
    return (t0 >= P.WARMUP_S) & (t0 < P.WARMUP_S + run.cfg.measure_s) & ~run.subs["decoy"][sub]


def compute(run, pools, m: Models, vantages=VANTAGES):
    """Score every vantage and the baseline on one run. Each vantage's record carries its rows
    (scored records it took part in) with the vantage's and the paired baseline's decisions."""
    rec = records(run, pools)
    keep = scored_mask(run, rec["sub"])
    rec = {k: x[keep] for k, x in rec.items()}
    cand = candidates(run, pools)
    g = m.pdf["g"]
    lo, hi = _band(rec["u"], g)
    truth = dict(sub=rec["sub"], dev=rec["dev"])

    def gfn(rows, k0, k1):
        return g(rec["u"][rows][:, None] - cand["t"][None, k0:k1])
    base = score_blocks(lo, hi, cand, gfn, truth)
    out = {}
    for v in vantages:
        ri, grp, res = score_vantage(v, run, rec, cand, m, base)
        r = dict(sub=rec["sub"][ri].astype(np.int32), group=np.asarray(grp).astype(np.int16))
        for lvl in LEVELS:
            o = res[lvl]
            b = base[lvl]
            r[f"{lvl}_v_correct"] = o["correct"].astype(np.int8)
            r[f"{lvl}_b_correct"] = b["correct"][ri].astype(np.int8)
            r[f"{lvl}_v_rand"] = _random_rate(o, lvl).astype(np.float32)
            r[f"{lvl}_b_rand"] = _random_rate({k: x[ri] for k, x in b.items()}, lvl).astype(np.float32)
            r[f"{lvl}_n_feas"] = o["n_feas"]
            r[f"{lvl}_rank"] = o["rank"]
            r[f"{lvl}_top1"] = o["top1"].astype(np.float32)
            r[f"{lvl}_top2"] = o["top2"].astype(np.float32)
            r[f"{lvl}_s_true"] = o["s_true"].astype(np.float32)
            if lvl == "dev":
                r["dev_lse"] = o["lse"]
        out[v] = r
    return out

"""Record-to-device linking: vantages, wire extraction, likelihood models, and the scoring of one run.

The harm Semantic Non-Assembly guards against is naming the device behind a public registry record.
Every vantage therefore starts from a registry record and names a device. The registry merges F's
and I's submissions into one record at intake and posts it on its own schedule; the posted time is
the record time. A passive observer sees the submissions' gossip frames but cannot tell which
record they belong to, so the frames carry no evidence. The candidates are the device-originated
first-hop packets on the wire, three per capture, decoy sources' packets included. Each packet is a
candidate on its own, and every likelihood is learned per packet from the Monte Carlo, pooled over
a capture's three packets.

Each vantage's own exact knowledge enters the likelihood of "record r came from candidate k":

  observer              g(u_r - s_k): record time against the packet's departure s_k
  first hop             its own hold, on the packets it relayed
  content server        its content arrival a_r, on the records that name it: the joint density
                        of the record time and a_r - s_k
  validator             its own reply times, which name the device; its candidates are its replies
  gatekeeper            the mixture over its own postings j: sum_j P(k -> j) p(r | j)
  credential processor  the mixture over its own transactions' fan-out sends, with a prior of 1/17
                        that it was the record's C
  combined              one node's every role, as likelihood ratios against the observer

Success is scored at two levels: the device (primary; the posterior summed over each source's
packets, since a source address is visible on the wire; ties go to a random device) and the
submission (the chosen packet belongs to the record's own capture). Every node is compromised in
turn: one pass over the records per node yields each vantage that node holds.

Every pass also scores two variants on the same likelihoods: the label shuffle (every candidate's
device label permuted within the run) and, for the observer, a flat timing likelihood.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from . import lottery as LT
from . import params as P
from . import sim as S

LEVELS = ("dev", "sub")
MAX_CELLS = 3_000_000     # rows x candidates per dense block
T_GRID = np.exp(np.linspace(np.log(0.1), np.log(10.0), 11))   # temperatures for calibrated confidence
_INT_MAX = np.iinfo(np.int32).max
PTYPES = ("credential", "F content", "I content")
_PTYPE = {S.CRED1: 0, S.CA1: 1, S.CB1: 2}


# =========================================================================== wire extraction
def records(run, mid=False):
    """Registry records: every transaction the registry posted. u is the posted time, the boundary
    of the registry's posting schedule at which the merged record appeared; with mid, the midpoint
    of F's and I's registry submissions instead (a scoring diagnostic)."""
    s = run.subs
    sub = np.nonzero(np.isfinite(s["posted"]))[0]
    return dict(sub=sub, u=(s["mid"] if mid else s["posted"])[sub], dev=s["src"][sub])


def candidates(run):
    """Device submissions on the wire, one candidate per packet. Packets are relay-class application
    records from an external host to a pool node; an external source that ever sends anything else
    (a handshake, a DNS lookup, a record outside the class) is not a device and is dropped. Returns
    packets sorted by send time, with truth labels (sub: the packet's capture; ptype: credential, F
    content or I content) and, per packet, its first hop and that hop's hold (node and hold have one
    column, the packet itself)."""
    ev, s = run.events, run.subs
    lo, hi = P.PAD_MIN + P.TLS13_OVERHEAD, P.PAD_MAX + P.TLS13_OVERHEAD
    ext = ev["src"] == S.EXT
    relay = ext & (ev["dst"] < P.N_NODES) & (ev["rtype"] == P.RT_APPDATA) & (ev["size"] >= lo) & (ev["size"] <= hi)
    bad_src = np.unique(ev["ext_src"][ext & ~relay])
    pk = np.nonzero(relay & ~np.isin(ev["ext_src"], bad_src))[0]
    pk = pk[np.argsort(ev["t_send"][pk], kind="stable")]
    fwd_of = np.full(ev["t_send"].shape[0], -1, np.int64)
    for key in ("ev_cred", "ev_ca", "ev_cb"):
        fwd_of[s[key][:, 0]] = s[key][:, 1]
    f = fwd_of[pk]
    sub = np.where(ev["kind"][pk] == S.K_BIRTHMARK, ev["sub"][pk], -1).astype(np.int64)
    leg = ev["leg"][pk]
    ptype = np.full(pk.size, -1, np.int8)
    for lg, k in _PTYPE.items():
        ptype[leg == lg] = k
    return dict(t=ev["t_send"][pk], sub=sub, msub=sub, dev=ev["ext_src"][pk].astype(np.int64), ptype=ptype,
                node=ev["dst"][pk].astype(np.int64)[:, None],
                hold=np.where(f >= 0, ev["t_send"][np.maximum(f, 0)] - ev["t_arr"][pk], np.nan)[:, None])


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
REF_DELAY_S = P.Config().max_delay_s   # bins widen with a configuration's delay bound beyond the main one's


def _true_samples(run, acc):
    """Every true (record, own packet) pair: y = u - s (s: the packet's departure) and each
    vantage's extra observation x. A record has three true packets (credential, F content, I
    content), which no vantage can tell apart on the wire, so every density is pooled over the three.
    y_mid is the same with the record time at the midpoint of F's and I's submissions."""
    s = run.subs
    rec, mid = records(run), records(run, mid=True)
    cand = candidates(run)
    u_of, m_of = np.full(s["t0"].shape[0], np.nan), np.full(s["t0"].shape[0], np.nan)
    u_of[rec["sub"]], m_of[mid["sub"]] = rec["u"], mid["u"]
    k = np.nonzero((cand["sub"] >= 0) & np.isfinite(u_of[np.maximum(cand["sub"], 0)]))[0]
    sub = cand["sub"][k]
    sk = cand["t"][k]
    y, ym = u_of[sub] - sk, m_of[sub] - sk
    add = lambda name, x: acc.setdefault(name, []).append(np.asarray(x, float).ravel())  # noqa: E731
    add("y", y)
    add("y_mid", ym)
    # first hop: the own hold of the packet it relayed
    add("fh_x", cand["hold"][k, 0])
    add("fh_y", y)
    # content server: content arrival at F and at I, relative to the packet's departure
    add("cs_x", np.r_[s["arr_f"][sub] - sk, s["arr_i"][sub] - sk])
    add("cs_y", np.r_[y, y])
    add("cs_y_mid", np.r_[ym, ym])
    # gatekeeper: each of the three postings relative to the packet's departure
    add("gk_x", (s["posts"][sub] - sk[:, None]).ravel())
    add("gk_y", np.repeat(y, 3))
    # credential processor: its fan-out median relative to the packet's departure
    add("c_x", np.sort(s["gk_send"][sub], 1)[:, 1] - sk)
    add("c_y", y)
    # validator: record time against its own reply send, once per record
    add("gV", rec["u"] - run.events["t_send"][s["ev_cv2"][rec["sub"]]])


def build_models(cfg: P.Config, seed0=1_000_000_000, min_samples=300_000, max_runs=200) -> Models:
    """Monte Carlo of the protocol under the configuration attacked, on seeds disjoint from every
    evaluation seed. Delays do not depend on volume (no queueing), so one set of models serves
    every volume. min_samples counts records."""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate, 0.2))
    scale = max(1.0, cfg.max_delay_s / REF_DELAY_S)
    bw_y, bw_x = BW_Y * scale, BW_X * scale
    acc = {}
    k = 0
    while True:
        _true_samples(S.simulate(mc, seed0 + k), acc)
        k += 1
        if (sum(x.size for x in acc["gV"]) >= min_samples and k >= 3) or k >= max_runs:
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
    g_mid = LT.EmpiricalLogPDF(cat["y_mid"][np.isfinite(cat["y_mid"])], bw_y)
    m.pdf["g_mid"] = g_mid
    m.pdf["cs_mid"] = CondPDF(cat["cs_x"], cat["cs_y_mid"], g_mid, bw_x)
    return m


# =========================================================================== block scoring engine
def _lse(x, axis=1):
    m = np.max(x, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0.0)
    with np.errstate(divide="ignore"):
        return (np.log(np.sum(np.exp(x - m), axis=axis, keepdims=True)) + m).squeeze(axis)


def _empty(n, want_lse):
    o = dict(pick=np.full(n, -1, np.int64), pidx=np.full(n, -1, np.int64), correct=np.zeros(n, bool),
             top1=np.full(n, -np.inf), top2=np.full(n, -np.inf), s_true=np.full(n, -np.inf),
             n_feas=np.zeros(n, np.int32), n_true=np.zeros(n, np.int32))
    if want_lse:
        o["lse"] = np.full((n, T_GRID.size), np.nan)
    return o


def _stats(W, lab, is_t, o, rows, want_lse):
    """Per-row decision statistics of a dense score block W (rows x m): column labels lab, and
    is_t (rows x m) marking the columns that are right for each row. The pick is the first maximum."""
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
    if want_lse:
        top = np.where(np.isfinite(top1), top1, 0.0)
        for i, T in enumerate(T_GRID):
            o["lse"][rows, i] = _lse(W / T) - top / T


def _groups(lab):
    """Column grouping by label: (labels, column order, group starts)."""
    u, inv = np.unique(lab, return_inverse=True)
    order = np.argsort(inv, kind="stable")
    return u, order, np.r_[0, np.nonzero(np.diff(inv[order]))[0] + 1]


def _aggregate(W, grp):
    """Log of the summed posterior per label (columns grouped by label)."""
    u, order, starts = grp
    M = np.max(W, 1)
    Mf = np.where(np.isfinite(M), M, 0.0)
    E = np.exp(W - Mf[:, None])
    with np.errstate(divide="ignore"):
        agg = np.log(np.add.reduceat(E[:, order], starts, axis=1)) + Mf[:, None]
    agg[~np.isfinite(M)] = -np.inf
    return agg, u


def score_blocks(t_lo, t_hi, cand, block_fn, truth, names, lse=(), max_cells=MAX_CELLS, extra=None):
    """Score every row against the candidates whose time lies in [t_lo, t_hi) of that row.

    cand: dict with sorted "t", "sub" and "msub" (the candidate's capture: a pick is right at the
    submission level if it belongs to the record's capture), "dev" labels and "dev_shuf" (the same
    labels permuted within the run). block_fn(rows, k0, k1) returns {name: dense log-likelihood
    block (len(rows), k1 - k0)}; every name is scored on the same rows. truth: dict level -> (n,)
    true label. extra(name, rows, lo, hi, W, is_t), if given, sees every scored block.
    Returns {name: {"dev", "sub", "shuf": per-row arrays}}, "shuf" being the device level under the
    permuted labels."""
    n = t_lo.shape[0]
    out = {nm: dict(dev=_empty(n, nm in lse), sub=_empty(n, False), shuf=_empty(n, False)) for nm in names}
    if n == 0:
        return out
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
            Ws = block_fn(rows, lo, hi)
        cols = np.arange(lo, hi)
        inb = (cols[None, :] >= k0s[rows][:, None]) & (cols[None, :] < k1s[rows][:, None])
        is_t = cand["msub"][lo:hi][None, :] == truth["sub"][rows][:, None]
        gd, gs = _groups(cand["dev"][lo:hi]), _groups(cand["dev_shuf"][lo:hi])
        ar = np.arange(rows.size)
        for nm, W in Ws.items():
            W = np.where(inb & np.isfinite(W), W, -np.inf)
            o = out[nm]
            _stats(W, cand["sub"][lo:hi], is_t, o["sub"], rows, False)
            am = np.argmax(W, 1)
            o["sub"]["pidx"][rows] = np.where(np.isfinite(W[ar, am]), lo + am, -1)
            Wd, labd = _aggregate(W, gd)
            _stats(Wd, labd, labd[None, :] == truth["dev"][rows][:, None], o["dev"], rows, nm in lse)
            Ws_, labs = _aggregate(W, gs)
            _stats(Ws_, labs, labs[None, :] == truth["dev"][rows][:, None], o["shuf"], rows, False)
            if extra is not None:
                extra(nm, rows, lo, hi, W, is_t)
    return out


def _random_rate(o, lvl):
    """Chance of a uniformly random pick among the feasible candidates being right: true packets
    over feasible packets (submission level), one over feasible devices when the true device is
    feasible (device level)."""
    nf = np.maximum(o["n_feas"], 1)
    if lvl == "sub":
        return np.where(o["n_feas"] > 0, o["n_true"] / nf, 0.0)
    return np.where((o["n_feas"] > 0) & (o["n_true"] > 0), 1.0 / nf, 0.0)


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

    def own_share(self, u, kidx):
        """Share of V_k(u - s_k) that comes from the server's own events, at one candidate per row."""
        out = np.zeros(u.size)
        ok = kidx >= 0
        g = self.g
        ny = self.gp.size
        for c in np.unique(kidx[ok] // self.CH):
            m = ok & (kidx // self.CH == c)
            loc = kidx[m] - c * self.CH
            V = self._vtab(c)
            Z = self._pair(c)[3]
            y = u[m] - self.ct[kidx[m]]
            yi = np.clip(np.floor((y - g.lo) / g.bw).astype(np.int64), 0, ny - 1)
            tot = V[loc, yi]
            rest = (1.0 - self.pi * (Z[loc] > 0)) * self.gp[yi]
            with np.errstate(invalid="ignore", divide="ignore"):
                out[m] = np.where(tot > 0, 1.0 - rest / tot, 0.0)
        return out

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



# --------------------------------------------------------------------------- combined view of one node
# The role pair a compromised node held in the record's own transaction (truth; used only to
# classify its decisions, never to score them).
PAIR_CLASSES = ("no role", "one relay or gatekeeper role", "destination only",
                "credential first relay + content destination", "content first relay + content destination",
                "content first relay + credential destination", "second relay + destination",
                "three or more roles, with a destination",
                "second relay + first relay", "second relay + second relay", "gatekeeper + first relay",
                "gatekeeper + second relay", "three or more roles, no destination")
# A class is identifiable when the node held a destination role (C, F or I) in the record's transaction:
# it reads the plaintext hash there, so it can select those records. Every other class is defined by
# information the node does not have (oracle-conditioned).
IDENTIFIABLE = tuple(c for c in PAIR_CLASSES if "destination" in c and "no destination" not in c)
PAIR_CODE = {c: i for i, c in enumerate(PAIR_CLASSES)}


def role_pair_class(s, sub, X, gk_set):
    """Class code of the roles node X held in each transaction sub (arrays of equal length)."""
    held = {k: s[k][sub] == X for k in "ABCDEFGHI"}
    gk = np.isin(X, gk_set)
    first, second = held["A"] | held["D"] | held["G"], held["B"] | held["E"] | held["H"]
    dest = held["C"] | held["F"] | held["I"]
    n_roles = sum(h.astype(int) for h in held.values()) + gk.astype(int)
    code = np.full(sub.shape, PAIR_CODE["no role"], np.int8)
    one = n_roles == 1
    code[one & dest] = PAIR_CODE["destination only"]
    code[one & ~dest] = PAIR_CODE["one relay or gatekeeper role"]
    two = n_roles == 2
    rules = (
        ("credential first relay + content destination", held["A"] & (held["F"] | held["I"])),
        ("content first relay + content destination", (held["D"] & held["I"]) | (held["G"] & held["F"])),
        ("content first relay + credential destination", (held["D"] | held["G"]) & held["C"]),
        ("second relay + destination", second & dest),
        ("second relay + first relay", second & first),
        ("second relay + second relay", (held["B"].astype(int) + held["E"] + held["H"]) == 2),
        ("gatekeeper + first relay", gk & first),
        ("gatekeeper + second relay", gk & second),
    )
    for name, m in rules:
        code[two & m] = PAIR_CODE[name]
    code[(n_roles >= 3) & dest] = PAIR_CODE["three or more roles, with a destination"]
    code[(n_roles >= 3) & ~dest] = PAIR_CODE["three or more roles, no destination"]
    return code



def scored_mask(run, sub):
    t0 = run.subs["t0"][sub]
    return (t0 >= run.cfg.warmup_s) & (t0 < run.cfg.warmup_s + run.cfg.measure_s) & ~run.subs["decoy"][sub]


def n_roles(s, sub, X, gk_set):
    """How many roles node X held in each transaction sub, counting an active gatekeeper role."""
    return sum((s[k][sub] == X).astype(np.int8) for k in "ABCDEFGHI") + np.int8(X in gk_set)


def _relabel(labels, rng):
    """A random bijection of the device labels: (labels, mapping function)."""
    perm = labels[rng.permutation(labels.size)]
    return lambda x: perm[np.searchsorted(labels, x)]


def _table(o, rec, ri, grp, base, **extra):
    """Per-row record of one vantage: its device- and submission-level outcomes, its chance rates, its
    shuffled-label outcome, and the observer's outcome on the same record."""
    t = dict(sub=rec["sub"][ri].astype(np.int32), group=np.asarray(grp).astype(np.int16))
    for lvl in LEVELS:
        t[f"{lvl}_v_correct"] = o[lvl]["correct"].astype(np.int8)
        t[f"{lvl}_v_rand"] = _random_rate(o[lvl], lvl).astype(np.float32)
        t[f"{lvl}_n_feas"] = o[lvl]["n_feas"].astype(np.int32)
        t[f"{lvl}_b_correct"] = base[lvl]["correct"][ri].astype(np.int8)
        t[f"{lvl}_b_rand"] = _random_rate(base[lvl], lvl)[ri].astype(np.float32)
    t["dev_top1"] = o["dev"]["top1"].astype(np.float32)
    t["dev_s_true"] = o["dev"]["s_true"].astype(np.float32)
    if "lse" in o["dev"]:
        t["dev_lse"] = np.where(np.isfinite(o["dev"]["lse"]), o["dev"]["lse"], np.nan).astype(np.float16)
    t["dev_s_correct"] = o["shuf"]["correct"].astype(np.int8)
    t["dev_s_rand"] = _random_rate(o["shuf"], "dev").astype(np.float32)
    for k, x in extra.items():
        t[k] = np.asarray(x)
    return t


def _cat(parts):
    return {k: np.concatenate([p[k] for p in parts]) for k in parts[0]}


def compute(run, m: Models, rng):
    """Score every vantage of one run, each node compromised in turn. rng draws the random order in
    which ties break and the label permutation of the shuffle. Returns {vantage: per-row table}:

      observer, observer_flat (flat timing likelihood), observer_mid (record time at the midpoint)
      first_hop          every node, every record; took_part_A, took_part_DG, claim
      cred_processor     every node outside the gatekeeper set, every record; took_part, claim
      gatekeeper         each active gatekeeper, every record
      combined           every node, every record; pair (the roles it held in the record's transaction)
      content_server, content_server_mid   the records naming the node as F or I
      validator          every record

    Every node-scored table carries nroles, the roles the node held in the record's transaction."""
    pdf, s = m.pdf, run.subs
    rec = records(run)
    keep = scored_mask(run, rec["sub"])
    rec = {k: x[keep] for k, x in rec.items()}
    mid = records(run, mid=True)
    mid = {k: x[keep] for k, x in mid.items()}
    cand = candidates(run)
    labels = np.unique(np.r_[cand["dev"], s["src"]])
    tie = _relabel(labels, rng)                   # ties break in a random order of the devices
    cand["dev"], rec["dev"], mid["dev"] = tie(cand["dev"]), tie(rec["dev"]), tie(mid["dev"])
    shuf = _relabel(np.unique(tie(labels)), rng)
    cand["dev_shuf"] = shuf(cand["dev"])
    srow, u, n = rec["sub"], rec["u"], rec["sub"].size
    idx = np.arange(n)
    truth = dict(sub=srow, dev=rec["dev"])
    g, gm = pdf["g"], pdf["g_mid"]
    out = {}

    # the observer, its flat-timing variant, and its hits by packet type
    tfeas = np.zeros((3, n), bool)

    def obs_extra(nm, rows, lo, hi, W, is_t):
        if nm == "observer":
            ok = is_t & np.isfinite(W)
            for k in range(3):
                tfeas[k, rows] = (ok & (cand["ptype"][lo:hi] == k)[None, :]).any(1)

    def obs(rows, k0, k1):
        lg = g(u[rows][:, None] - cand["t"][None, k0:k1])
        return dict(observer=lg, observer_flat=np.where(np.isfinite(lg), 0.0, -np.inf))
    lo, hi = _band(u, g)
    res = score_blocks(lo, hi, cand, obs, truth, ("observer", "observer_flat"), lse=("observer",), extra=obs_extra)
    base = res["observer"]
    pidx = base["sub"]["pidx"]
    hit_type = np.where(base["sub"]["correct"], cand["ptype"][np.maximum(pidx, 0)], -1).astype(np.int8)
    half = (s["t0"][srow] >= run.cfg.warmup_s + run.cfg.measure_s / 2).astype(np.int8)   # second half of the window
    out["observer"] = _table(base, rec, idx, np.zeros(n), base, hit_type=hit_type,
                             tfeas=tfeas.T.astype(np.int8), half=half)
    out["observer_flat"] = _table(res["observer_flat"], rec, idx, np.zeros(n), base)
    um = mid["u"]
    mlo, mhi = _band(um, gm)
    resm = score_blocks(mlo, mhi, cand, lambda rows, k0, k1: dict(observer_mid=gm(um[rows][:, None] - cand["t"][None, k0:k1])),
                        truth, ("observer_mid",))
    out["observer_mid"] = _table(resm["observer_mid"], rec, idx, np.zeros(n), base)

    # one pass per compromised node: its first-hop evidence, its credential-processor or gatekeeper
    # mixture, its content arrival on the records naming it, and their combination
    fh, cs, csq = pdf["fh"], pdf["cs"], pdf["cs_q"]
    pi = 1.0 / (P.N_NODES - P.N_GATEKEEPERS)
    m_all = np.sort(s["gk_send"], 1)[:, 1]
    parts = {k: [] for k in ("first_hop", "cred_processor", "gatekeeper", "combined")}
    for X in range(P.N_NODES):
        isgk = bool(np.isin(X, run.gk_set))
        a = np.where(s["F"][srow] == X, s["arr_f"][srow], np.where(s["I"][srow] == X, s["arr_i"][srow], np.nan))
        if isgk:
            post = s["posts"][:, int(np.nonzero(run.gk_set == X)[0][0])]
            o = np.argsort(post, kind="stable")
            mix, role = _MixtureV(cand["t"], post[o], np.ones(o.size), pdf["gk"], pdf["gk_q"], g), "gatekeeper"
        else:
            mine = np.nonzero(s["C"] == X)[0]
            mine = mine[np.argsort(m_all[mine], kind="stable")]
            mix, role = _MixtureV(cand["t"], m_all[mine], np.ones(mine.size), pdf["c"], pdf["c_q"], g, pi=pi), "cred_processor"
        mine_pk = cand["node"][:, 0] == X
        hold = np.where(mine_pk, cand["hold"][:, 0], np.nan)

        def fn(rows, k0, k1, a=a, mix=mix, role=role, mine_pk=mine_pk, hold=hold):
            sk = cand["t"][None, k0:k1]
            y = u[rows][:, None] - sk
            lg = g(y)
            ok = np.isfinite(lg)
            lg0 = np.where(ok, lg, 0.0)
            own = mine_pk[None, k0:k1] & ok
            t_fh = np.where(own, fh(hold[None, k0:k1], y) - lg0, 0.0) if own.any() else 0.0
            ar = a[rows]
            t_cs = 0.0
            if np.isfinite(ar).any():
                x = ar[:, None] - sk
                named = np.isfinite(ar)[:, None] & ok
                t_cs = np.where(named, cs(x, y) + csq(x) - lg0, 0.0)
            t_mix = np.where(ok, mix.block(u[rows], k0, k1) - lg0, 0.0)
            neg = -np.inf
            return {"first_hop": np.where(ok, lg + t_fh, neg), role: np.where(ok, lg + t_mix, neg),
                    "combined": np.where(ok, lg + t_fh + t_cs + t_mix, neg)}
        names = ("first_hop", role, "combined")
        r = score_blocks(lo, hi, cand, fn, truth, names, lse=names, max_cells=MAX_CELLS // 3)
        grp = np.full(n, X)
        nr = n_roles(s, srow, X, run.gk_set)
        pair = role_pair_class(s, srow, X, run.gk_set)
        pk = r["first_hop"]["sub"]["pidx"]
        claim = (pk >= 0) & (cand["node"][np.maximum(pk, 0), 0] == X)
        parts["first_hop"].append(_table(r["first_hop"], rec, idx, grp, base, took_part_A=(s["A"][srow] == X).astype(np.int8),
                                         took_part_DG=((s["D"][srow] == X) | (s["G"][srow] == X)).astype(np.int8),
                                         claim=claim.astype(np.int8), nroles=nr, pair=pair))
        if isgk:
            parts["gatekeeper"].append(_table(r[role], rec, idx, grp, base, nroles=nr, pair=pair))
        else:
            claim = mix.own_share(u, r[role]["sub"]["pidx"]) > pi       # evidence favours its own transactions
            parts["cred_processor"].append(_table(r[role], rec, idx, grp, base, took_part=(s["C"][srow] == X).astype(np.int8),
                                                  claim=claim.astype(np.int8), nroles=nr, pair=pair))
        parts["combined"].append(_table(r["combined"], rec, idx, grp, base, took_part=(pair != PAIR_CODE["no role"]).astype(np.int8),
                                        nroles=nr, pair=pair))
    for k, v in parts.items():
        out[k] = _cat(v)

    # content server: the records naming it as F or I, which it identifies by the content hash it submitted
    ri = np.r_[idx, idx]
    grp = np.r_[s["F"][srow], s["I"][srow]]
    a = np.r_[s["arr_f"][srow], s["arr_i"][srow]]
    tr = dict(sub=srow[ri], dev=rec["dev"][ri])
    nr = (sum((s[k][srow[ri]] == grp).astype(np.int8) for k in "ABCDEFGHI") + np.isin(grp, run.gk_set)).astype(np.int8)
    for name, uu, gg, cond in (("content_server", u, g, cs), ("content_server_mid", um, gm, pdf["cs_mid"])):
        ur = uu[ri]

        def fn(rows, k0, k1, ur=ur, cond=cond):
            sk = cand["t"][None, k0:k1]
            x = a[rows][:, None] - sk
            return {name: cond(x, ur[rows][:, None] - sk) + csq(x)}
        clo, chi = _band(ur, gg)
        r = score_blocks(clo, chi, cand, fn, tr, (name,), lse=(name,) if name == "content_server" else ())
        out[name] = _table(r[name], rec, ri, grp, base, nroles=nr)

    # validator: names device identities directly; its candidates are its own replies, real and decoy
    t = run.events["t_send"][s["ev_cv2"]]
    o = np.argsort(t, kind="stable")
    vdev = tie(s["src"][o].astype(np.int64))
    vc = dict(t=t[o], sub=o.astype(np.int64), msub=o.astype(np.int64), dev=vdev, dev_shuf=shuf(vdev))
    gV = pdf["gV"]
    vlo, vhi = _band(u, gV)
    r = score_blocks(vlo, vhi, vc, lambda rows, k0, k1: dict(validator=gV(u[rows][:, None] - vc["t"][None, k0:k1])),
                     truth, ("validator",), lse=("validator",))
    out["validator"] = _table(r["validator"], rec, idx, np.zeros(n), base)
    return out


def shuffle_test(run, m: Models, rng, K=200):
    """The label-shuffle control, taken apart for the observer on one run. One permutation is scored
    as in compute(); from the same scores, the outcome under K further permutations follows exactly,
    because permuting labels only renames the groups the posterior is summed over.

    Returns per-run totals: records n; labels L; for the scored permutation, records whose shuffled
    pick is not the permuted unshuffled pick (the shuffle itself), records whose feasible-device count
    changes (the feasible set), and its correct and chance sums; the exact expectation over every
    permutation of the correct and chance sums; and the correct and chance sums under each of K
    permutations (the estimator's spread)."""
    s = run.subs
    rec = records(run)
    keep = scored_mask(run, rec["sub"])
    rec = {k: x[keep] for k, x in rec.items()}
    cand = candidates(run)
    labels = np.unique(np.r_[cand["dev"], s["src"]])
    L, n = labels.size, rec["sub"].size
    li = np.searchsorted(labels, cand["dev"])
    p0 = rng.permutation(L)                                   # label index i -> label index p0[i]
    cand["dev_shuf"] = labels[p0[li]]
    feas = np.zeros((n, L), bool)

    def extra(nm, rows, lo, hi, W, is_t):
        rr, cc = np.nonzero(np.isfinite(W))
        feas[rows[rr], li[lo:hi][cc]] = True
    g = m.pdf["g"]
    u = rec["u"]
    lo, hi = _band(u, g)
    res = score_blocks(lo, hi, cand, lambda rows, k0, k1: dict(observer=g(u[rows][:, None] - cand["t"][None, k0:k1])),
                       dict(sub=rec["sub"], dev=rec["dev"]), ("observer",), extra=extra)["observer"]
    pick, spick = res["dev"]["pick"], res["shuf"]["pick"]
    has = pick >= 0
    pi_ = np.where(has, np.searchsorted(labels, np.where(has, pick, labels[0])), -1)
    ti = np.searchsorted(labels, rec["dev"])
    nf = feas.sum(1)
    mismatch = int((has & (spick != labels[p0[np.maximum(pi_, 0)]])).sum())
    nfeas_mismatch = int((nf != res["dev"]["n_feas"]).sum())
    inv0 = np.argsort(p0)
    real_correct = int((has & (p0[np.maximum(pi_, 0)] == ti)).sum())
    real_chance = float(np.where(nf > 0, feas[np.arange(n), inv0[ti]] / np.maximum(nf, 1), 0.0).sum())
    perms = np.argsort(rng.random((K, L)), 1)
    inv = np.argsort(perms, 1)
    ck = (has[None, :] & (perms[:, np.maximum(pi_, 0)] == ti[None, :])).sum(1)
    chk = np.where(nf[None, :] > 0, feas[np.arange(n)[None, :], inv[:, ti]] / np.maximum(nf, 1)[None, :], 0.0).sum(1)
    return dict(n=n, L=L, shuffle_mismatch=mismatch, nfeas_mismatch=nfeas_mismatch, correct=real_correct, chance=real_chance,
                scored_correct=int(res["shuf"]["correct"].sum()), scored_chance=float(_random_rate(res["shuf"], "dev").sum()),
                exact_correct=float(has.sum() / L), exact_chance=float((nf > 0).sum() / L),
                correct_k=ck.astype(np.int32), chance_k=chk.astype(np.float64))

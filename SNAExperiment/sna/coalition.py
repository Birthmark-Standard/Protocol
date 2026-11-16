"""Cross-role coalition vantages (C3 item 2).

Validator with a node. The validator names the device of every reply it sends. A node adds what it holds:
  as C of a transaction       the transaction's fan-out times, linked to the reply by tx_id;
  as a gatekeeper             its own posting of every transaction, linked by Enc_FullPacketHash;
  as F or I of the record      its content packet's arrival, against each reply's time;
  as a first relay             its own holds, as a likelihood ratio against the observer, per device.
For each record the coalition scores every device:
  log sum over the device's replies j of p(the coalition's observations | j)  +  the first-hop log ratio,
where the observations are the record time after the fan-out median when the node was C of j, after the
node's own posting when it is a gatekeeper, and after the reply otherwise, together with the content
arrival after the reply when the node is the record's F or I. Each record is classed by the node's role in
its transaction.

A first relay with the destination on its path. A relay decrypts its transit layer and forwards the rest, so the
inner packet (CredP, ContP_F or ContP_I, an encryption to the destination's Channel Key under a fresh ephemeral
key) is byte-identical at the first relay and at the destination. The pair matches it exactly, with no timing:
the first relay holds the source address it came from. Scored on the records whose transaction used the path:
  content path (D with F, G with I): F holds the record's ContentHash, so the pair names the device of the record
      exactly.
  credential path (A with C): the pair names the device of each of C's transactions that came through A. C holds
      FullPacketHash, which the record does not carry, so it links a transaction to a record by timing: as a
      Registry Node it reads the match boards, and finds its transaction's postings by FullPacketHash. The pair
      scores each such transaction by the density of the record time after the transaction's quorum (the second
      posting) and names the device of the best.
"""
from __future__ import annotations

import pickle
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from . import attacks as AT
from . import devscore as DS
from . import lottery as LT
from . import params as P
from . import sim as S


@dataclass
class Extra:
    pdf: dict = field(default_factory=dict)
    mc_runs: int = 0


def build_extra(cfg: P.Config, gV, seed0=1_000_000_000, runs=93) -> Extra:
    """Densities the coalitions need, on the model seeds (disjoint from every evaluation seed). With y the
    record time minus the transaction's CV-2 send:
    gV2  the density of y: the validator's own model, so a coalition that adds nothing scores as the validator
    gC   log p(y | x), x the fan-out median minus the CV-2 send (C's own sends)
    gG   log p(y | x), x one gatekeeper's posting minus the CV-2 send (pooled over the three)
    gFA  log p(y | x), x the content arrival at F or I minus the CV-2 send (pooled), and qFA the density of x
Each conditional is held as the density of the residual y - x (the record time after the node's own event)
given x in 30-second bins, which is far less sparse than a density over (x, y) cells.
    p2   arrival at the destination minus the first relay's departure (second hop, pooled over the paths)
    gCm  the record time minus the fan-out median
    gQ   the record time minus the transaction's quorum (its second posting), for the credential-path coalition"""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate, 0.2))
    acc = {k: [] for k in ("y", "xc", "yg", "xg", "yfa", "xfa", "p2", "cm", "uq")}
    for k in range(runs):
        run = S.simulate(mc, seed0 + k)
        s, ts = run.subs, run.events["t_send"]
        ok = np.isfinite(s["posted"])
        u, cv = s["posted"][ok], s["cv2_s"][ok]
        y = u - cv
        med = np.sort(s["gk_send"][ok], 1)[:, 1]
        acc["y"].append(y)
        acc["xc"].append(med - cv)
        acc["cm"].append(u - med)
        acc["uq"].append(u - s["quorum"][ok])
        acc["yg"].append(np.repeat(y, 3))
        acc["xg"].append((s["posts"][ok] - cv[:, None]).ravel())
        acc["yfa"].append(np.r_[y, y])
        acc["xfa"].append(np.r_[s["arr_f"][ok] - cv, s["arr_i"][ok] - cv])
        for key, arr in (("ev_cred", "arr_c"), ("ev_ca", "arr_f"), ("ev_cb", "arr_i")):
            acc["p2"].append(s[arr] - ts[s[key][:, 1]])
    c = {k: np.concatenate(v) for k, v in acc.items()}
    e = Extra(mc_runs=runs)
    gV2 = gV
    e.pdf["gV2"] = gV2
    e.pdf["gC"] = Residual(c["xc"], c["y"])
    e.pdf["gG"] = Residual(c["xg"], c["yg"])
    e.pdf["gFA"] = Residual(c["xfa"], c["yfa"])
    e.pdf["qFA"] = LT.EmpiricalLogPDF(c["xfa"][np.isfinite(c["xfa"])], AT.BW_X)
    for k, src in (("p2", "p2"), ("gCm", "cm"), ("gQ", "uq")):
        x = c[src]
        e.pdf[k] = LT.EmpiricalLogPDF(x[np.isfinite(x)], AT.BW_Y)
    return e


class Residual:
    """log p(y | x) held as the density of r = y - x given x: one histogram of r per 30-second bin of x,
    shrunk towards the pooled histogram of r, as attacks.CondPDF shrinks towards a marginal."""

    def __init__(self, x, y, bw_x=30.0):
        x, y = np.asarray(x, float), np.asarray(y, float)
        ok = np.isfinite(x) & np.isfinite(y)
        x, r = x[ok], (y - x)[ok]
        self.marg = LT.EmpiricalLogPDF(r, AT.BW_Y)
        self.cond = AT.CondPDF(x, r, self.marg, bw_x)

    def __call__(self, x, y):
        x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float))
        return self.cond(x, y - x)


def load_extra(path, cfg, seed0, gV):
    p = Path(path)
    if p.exists():
        with open(p, "rb") as f:
            return pickle.load(f)
    e = build_extra(cfg, gV, seed0)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(e, f)
    tmp.replace(p)
    return e


# role classes of the node in the record's transaction, for the validator-with-a-node coalition
ROLE_CLASSES = ("C", "gatekeeper", "F or I", "relay only", "no role")


def role_class(s, sub, X, gk_set):
    held = {k: s[k][sub] == X for k in "ABCDEFGHI"}
    code = np.full(sub.shape, 4, np.int8)
    code[held["A"] | held["B"] | held["D"] | held["E"] | held["G"] | held["H"]] = 3
    code[held["F"] | held["I"]] = 2
    if np.isin(X, gk_set):
        code[:] = 1
    code[held["C"]] = 0
    return code


class NodeLR:
    """Per node and record: each device's log ratio of the node's own evidence (first hop and content
    arrival) to the observer's, from the compute hook."""

    def __init__(self, n, cand, u, g):
        self.n, self.cand, self.u, self.g = n, cand, u, g
        self.data = {}

    def __call__(self, X, rows, lo, hi, W):
        y = self.u[rows][:, None] - self.cand["t"][None, lo:hi]
        lg = np.where(np.isfinite(W), self.g(y), -np.inf)
        grp = AT._groups(self.cand["dev"][lo:hi])
        a, lab = AT._aggregate(W, grp)
        b, _ = AT._aggregate(lg, grp)
        d = self.data.setdefault(X, [None] * self.n)
        with np.errstate(invalid="ignore"):
            lr = a - b
        for i, r in enumerate(rows):
            m = np.isfinite(lr[i])
            d[r] = (lab[m], lr[i, m])


def validator_with_node(run, m, ex, out, nodelr):
    """Tables of the validator with each node, every record, classed by the node's role."""
    s, rec, tie, shuf = run.subs, out["_rec"], out["_tie"], out["_shuf"]
    base = out["_base"]
    u, srow, n = rec["u"], rec["sub"], rec["sub"].size
    t = run.events["t_send"][s["ev_cv2"]]
    o = np.argsort(t, kind="stable")
    vdev = tie(s["src"][o].astype(np.int64))
    vc = dict(t=t[o], sub=o.astype(np.int64), msub=o.astype(np.int64), dev=vdev, dev_shuf=shuf(vdev))
    gV2, gC, gG, gFA, qFA = (ex.pdf[k] for k in ("gV2", "gC", "gG", "gFA", "qFA"))
    x_c = np.sort(s["gk_send"], 1)[:, 1][o] - vc["t"]
    lo, hi = AT._band(u, gV2)
    truth = dict(sub=srow, dev=rec["dev"])
    parts = []
    for X in range(P.N_NODES):
        isgk = bool(np.isin(X, run.gk_set))
        if isgk:
            x_own, cond, own = s["posts"][o][:, int(np.nonzero(run.gk_set == X)[0][0])] - vc["t"], gG, np.ones(o.size, bool)
        else:
            x_own, cond, own = x_c, gC, s["C"][o] == X
        col = DS.Collector(n, vc["dev"])
        # the content arrival of the records naming the node as F or I
        a = np.where(s["F"][srow] == X, s["arr_f"][srow], np.where(s["I"][srow] == X, s["arr_i"][srow], np.nan))

        def fn(rows, k0, k1, x_own=x_own, cond=cond, own=own, a=a):
            y = u[rows][:, None] - vc["t"][None, k0:k1]
            sc = gV2(y)
            ow = own[None, k0:k1] & np.isfinite(sc)
            if ow.any():
                sc = np.where(ow, cond(np.broadcast_to(x_own[None, k0:k1], y.shape), y), sc)
            ar = a[rows]
            if np.isfinite(ar).any():
                # F or I of the record: p(y, x) = p(y | x) q(x) with x its content arrival after the reply; the node's
                # own C or gatekeeper knowledge is not combined with it here
                x = ar[:, None] - vc["t"][None, k0:k1]
                fa = gFA(x, y) + qFA(x)
                sc = np.where(np.isfinite(ar)[:, None], fa, sc)
            return dict(vx=sc)
        AT.score_blocks(lo, hi, vc, fn, truth, ("vx",), extra=lambda nm, rows, a_, b_, W, is_t: col(rows, a_, b_, W))
        lr = nodelr.data.get(X, [None] * n)
        labs, scs = [], []
        for i in range(n):
            lab, sc = col.get(i)
            if lr[i] is not None and lab.size and lr[i][0].size:
                ll, lv = lr[i]
                pos = np.clip(np.searchsorted(ll, lab), 0, ll.size - 1)
                sc = sc + np.where(ll[pos] == lab, lv[pos], 0.0)
            labs.append(lab)
            scs.append(sc)
        cls = role_class(s, srow, X, run.gk_set)
        parts.append(DS.table(labs, scs, rec, np.arange(n), np.full(n, X), base, rec["dev"], shuf, role=cls))
    return AT._cat(parts)


def path_coalitions(run, ex, out):
    """Tables of a first relay with the destination on its path, on the records whose transaction used the path:
    kind 0 credential (A with C), 1 F content (D with F), 2 I content (G with I)."""
    s, rec, tie, shuf, base = run.subs, out["_rec"], out["_tie"], out["_shuf"], out["_base"]
    gQ = ex.pdf["gQ"]
    u, srow, n = rec["u"], rec["sub"], rec["sub"].size
    dev_all = tie(s["src"].astype(np.int64))           # the source address each packet came from, as A, D or G see it
    q = s["quorum"]
    labs, scs, ri, kind, grp = [], [], [], [], []
    for i in range(n):
        j = srow[i]
        # content paths: the inner packet matched exactly; F (or I) holds the record
        for k, (fr, dn) in ((1, ("D", "F")), (2, ("G", "I"))):
            labs.append(np.array([dev_all[j]]))
            scs.append(np.zeros(1))
            ri.append(i); kind.append(k); grp.append(int(s[fr][j]) * 32 + int(s[dn][j]))
        # credential path: C's transactions that came through A, each with its device; the record by timing
        mine = np.nonzero((s["C"] == s["C"][j]) & (s["A"] == s["A"][j]) & np.isfinite(q))[0]
        sc = gQ(u[i] - q[mine])
        ok = np.isfinite(sc)
        lab, sc = dev_all[mine[ok]], sc[ok]
        if lab.size:
            uu, inv = np.unique(lab, return_inverse=True)
            mx = sc.max()
            lab, sc = uu, np.log(np.bincount(inv, weights=np.exp(sc - mx))) + mx
        labs.append(lab)
        scs.append(sc)
        ri.append(i); kind.append(0); grp.append(int(s["A"][j]) * 32 + int(s["C"][j]))
    ri = np.array(ri, np.int64)
    return DS.table(labs, scs, rec, ri, np.array(grp), base, rec["dev"][ri], shuf, path=np.array(kind, np.int8))


# --------------------------------------------------------------------------- same-role coalitions (item 7) and k nodes (item 8)
COALITION_SEED = 18_000_000
RELAY_SIZES = (2, 3, 6)                     # first relays and second relays per coalition
NODE_COUNTS = (1, 2, 3, 4, 5, 6)            # compromised nodes, each in every role it holds
PATHS = (("ev_cred", "A", "B", "C"), ("ev_ca", "D", "E", "F"), ("ev_cb", "G", "H", "I"))
NODE_CLASSES = ("content path held at both ends", "credential path held at both ends", "destination and second relay",
                "destination only", "timing roles only", "no role")


def build_roles(cfg: P.Config, g, seed0=1_000_000_000 + 80_000, runs=30) -> Extra:
    """Densities the same-role coalitions need, on the model seeds (pooled over the three packets of a transaction):
    q1      a packet's arrival at its second relay after its send (the first relay's hold and two links)
    r2      p(y | z), z the packet's arrival at its destination after its send; y the record time after the send
    gk2     p(y | x), x the later of two gatekeepers' postings after the send (every pair of the three); gk2_q its x
    gk3     p(y | x), x the quorum (the second posting) after the send; gk3_q its x"""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate, 0.2))
    acc = {k: [] for k in ("q1", "z", "y", "x2", "y2", "x3")}
    for k in range(runs):
        run = S.simulate(mc, seed0 + k)
        s, ev = run.subs, run.events
        ok = np.isfinite(s["posted"])
        u, po = s["posted"][ok], s["posts"][ok]
        for key, *_ in PATHS:
            e = s[key][ok]
            sk = ev["t_send"][e[:, 0]]
            acc["q1"].append(ev["t_arr"][e[:, 1]] - sk)
            acc["z"].append(ev["t_arr"][e[:, 2]] - sk)
            acc["y"].append(u - sk)
            acc["x3"].append(np.sort(po, 1)[:, 1] - sk)
            for a, b in ((0, 1), (0, 2), (1, 2)):
                acc["x2"].append(np.maximum(po[:, a], po[:, b]) - sk)
                acc["y2"].append(u - sk)
    c = {k: np.concatenate(v) for k, v in acc.items()}
    e = Extra(mc_runs=runs)
    e.pdf["q1"] = LT.EmpiricalLogPDF(c["q1"], AT.BW_Y)
    e.pdf["r2"] = AT.CondPDF(c["z"], c["y"], g, AT.BW_X)
    e.pdf["r2_q"] = LT.EmpiricalLogPDF(c["z"], AT.BW_X)
    for nm, x, y in (("gk2", c["x2"], c["y2"]), ("gk3", c["x3"], c["y"])):
        e.pdf[nm] = AT.CondPDF(x, y, g, AT.BW_X)
        e.pdf[nm + "_q"] = LT.EmpiricalLogPDF(x, AT.BW_X)
    return e


def load_roles(path, cfg, g, seed0=1_000_000_000 + 80_000):
    p = Path(path)
    if p.exists():
        with open(p, "rb") as f:
            return pickle.load(f)
    e = build_roles(cfg, g, seed0)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(e, f)
    tmp.replace(p)
    return e


class _SecondRelayMix(AT._MixtureV):
    """The second relays' mixture: for device packet k, its weight on each packet j a coalition node relayed second
    is the first relay's hold density at j's arrival after k's send, among the packets that came from k's own first
    relay; its conditional density of the record time uses j's arrival at the destination."""

    def __init__(self, cand_t, cand_node, e, e_dest, e_from, cond, q, g, pi):
        super().__init__(cand_t, e, np.ones(e.size), cond, q, g, pi=pi)
        self.cn, self.e_dest, self.e_from = cand_node, e_dest, e_from

    def _pair(self, c):
        if c in self.pairs:
            return self.pairs[c]
        self._evict(c)
        sl = slice(c * self.CH, (c + 1) * self.CH)
        s, nd = self.ct[sl], self.cn[sl]
        K = s.size
        xi, w = np.zeros((K, 1), np.int64), np.zeros((K, 1))
        outx, Z = np.zeros(K), np.zeros(K)
        if self.e.size and K:
            a = np.searchsorted(self.e, s + self.q.support[0], "left")
            b = np.searchsorted(self.e, s + self.q.support[1], "right")
            n = b - a
            B = int(n.max())
            if B > 0:
                j = np.minimum(a[:, None] + np.arange(B)[None, :], self.e.size - 1)
                valid = (np.arange(B)[None, :] < n[:, None]) & (self.e_from[j] == nd[:, None])
                qw = np.where(valid, np.exp(self.q(self.e[j] - s[:, None])), 0.0)
                Z = qw.sum(1)
                wr = qw / np.where(Z > 0, Z, 1.0)[:, None]
                x = self.e_dest[j] - s[:, None]
                xi = np.floor((x - self.cond.xlo) / self.cond.bx).astype(np.int64)
                inx = valid & (xi >= 0) & (xi < self.cond.nx)
                outx = np.where(valid & ~inx, wr, 0.0).sum(1)
                w = np.where(inx, wr, 0.0)
                xi = np.clip(xi, 0, self.cond.nx - 1)
        self.pairs[c] = (xi, w, outx, Z)
        return self.pairs[c]


def _pick(R, run_id, code, k, pool):
    """One coalition: k nodes drawn uniformly from pool, from a seed set by the cell, the run id and the vantage."""
    rng = np.random.default_rng([COALITION_SEED, int(R), int(run_id), code, k])
    return np.sort(rng.choice(np.asarray(pool), size=k, replace=False))


def _packet_level(run, m, rx, out, nodes, roles):
    """Every record's device scores from the observer's view plus the pooled evidence of the coalition's nodes in the
    given roles ("first", "second", "C", "gatekeeper"), each as a log ratio against the observer per packet, summed
    over roles, then summed over each device's packets. Returns (labels, scores) per record."""
    s, ev, cand, rec = run.subs, run.events, out["_cand"], out["_rec"]
    u, n = rec["u"], rec["sub"].size
    g, fh = m.pdf["g"], m.pdf["fh"]
    lo, hi = AT._band(u, g)
    nodes = [int(x) for x in nodes]
    mixes = []                                   # (column mask or None, mixture)
    if "first" in roles:
        mine = np.isin(cand["node"][:, 0], nodes)
        hold = np.where(mine, cand["hold"][:, 0], np.nan)
    if "second" in roles:
        ea, ed, ef = [], [], []
        for key, fr, sr, _ in PATHS:
            sel = np.isin(s[sr], nodes)
            e = s[key][sel]
            ea.append(ev["t_arr"][e[:, 1]]); ed.append(ev["t_arr"][e[:, 2]]); ef.append(s[fr][sel])
        ea, ed, ef = np.concatenate(ea), np.concatenate(ed), np.concatenate(ef)
        o = np.argsort(ea, kind="stable")
        mixes.append((None, _SecondRelayMix(cand["t"], cand["node"][:, 0], ea[o], ed[o], ef[o], rx.pdf["r2"], rx.pdf["q1"],
                                            g, pi=len(nodes) / P.N_NODES)))
    if "C" in roles:
        cs = [X for X in nodes if X not in set(run.gk_set.tolist())]
        if cs:
            mine_c = np.isin(s["C"], cs)
            med = np.sort(np.sort(s["gk_send"][mine_c], 1)[:, 1])
            mixes.append((None, AT._MixtureV(cand["t"], med, np.ones(med.size), m.pdf["c"], m.pdf["c_q"], g,
                                             pi=len(cs) / (P.N_NODES - P.N_GATEKEEPERS))))
    if "gatekeeper" in roles:
        js = [int(np.nonzero(run.gk_set == X)[0][0]) for X in nodes if X in set(run.gk_set.tolist())]
        if js:
            po = s["posts"][:, js]
            if len(js) == 1:
                x, cond, q = po[:, 0], m.pdf["gk"], m.pdf["gk_q"]
            elif len(js) == 2:
                x, cond, q = po.max(1), rx.pdf["gk2"], rx.pdf["gk2_q"]
            else:
                x, cond, q = np.sort(po, 1)[:, 1], rx.pdf["gk3"], rx.pdf["gk3_q"]
            x = np.sort(x[np.isfinite(x)])
            mixes.append((None, AT._MixtureV(cand["t"], x, np.ones(x.size), cond, q, g)))
    col = DS.Collector(n, cand["dev"])

    def fn(rows, k0, k1):
        y = u[rows][:, None] - cand["t"][None, k0:k1]
        lg = g(y)
        ok = np.isfinite(lg)
        lg0 = np.where(ok, lg, 0.0)
        tot = lg0.copy()
        if "first" in roles:
            own = mine[None, k0:k1] & ok
            if own.any():
                tot = tot + np.where(own, fh(hold[None, k0:k1], y) - lg0, 0.0)
        for _, mix in mixes:
            tot = tot + np.where(ok, mix.block(u[rows], k0, k1) - lg0, 0.0)
        return dict(v=np.where(ok, tot, -np.inf))
    AT.score_blocks(lo, hi, cand, fn, dict(sub=rec["sub"], dev=rec["dev"]), ("v",),
                    extra=lambda nm, rows, a, b, W, is_t: col(rows, a, b, W))
    return [col.get(i) for i in range(n)]


def _device_lse(dev, v):
    ok = np.isfinite(v)
    if not ok.any():
        return np.zeros(0, np.int64), np.zeros(0)
    dev, v = dev[ok], v[ok]
    lab, inv = np.unique(dev, return_inverse=True)
    mx = np.full(lab.size, -np.inf)
    np.maximum.at(mx, inv, v)
    return lab, np.log(np.bincount(inv, weights=np.exp(v - mx[inv]))) + mx


def _arrival(cand, a, q, first=None):
    """Each device's log sum over its packets of q(a - s_k): the density of a known arrival after the packet's send.
    first: only packets whose first relay is that node."""
    k0, k1 = np.searchsorted(cand["t"], a - q.support[1]), np.searchsorted(cand["t"], a - q.support[0], "right")
    v = q(a - cand["t"][k0:k1])
    if first is not None:
        v = np.where(cand["node"][k0:k1, 0] == first, v, -np.inf)
    return _device_lse(cand["dev"][k0:k1], v)


def _add(parts):
    """Sum of device scores over channels; a device must appear in every channel."""
    lab, sc = parts[0]
    for l2, s2 in parts[1:]:
        common, i1, i2 = np.intersect1d(lab, l2, return_indices=True)
        lab, sc = common, sc[i1] + s2[i2]
    return lab, sc


def _destination(run, m, out, rx, i, held, first_held, second_held):
    """A record whose F or I (or both) the coalition holds: each held destination's arrival, through its path's first
    relay (exact), its second relay (the first relay's arrivals weighed by its hold), or its own arrival density."""
    s, ev, cand, tie = run.subs, run.events, out["_cand"], out["_tie"]
    j = out["_rec"]["sub"][i]
    parts = []
    for (key, fr, sr, dn) in PATHS[1:]:
        if not held[dn]:
            continue
        if first_held[fr]:
            return np.array([tie(s["src"][j:j + 1].astype(np.int64))[0]]), np.zeros(1)
        e = s[key][j]
        if second_held[sr]:
            parts.append(_arrival(cand, ev["t_arr"][e[1]], rx.pdf["q1"], first=int(s[fr][j])))
        else:
            parts.append(_arrival(cand, ev["t_arr"][e[2]], m.pdf["cs_q"]))
    return _add(parts)


def _credential_exact(run, out, ex, i):
    """A and C both held: the device of each of C's transactions through A, by the record time after its quorum."""
    s, tie, rec = run.subs, out["_tie"], out["_rec"]
    j = rec["sub"][i]
    mine = np.nonzero((s["C"] == s["C"][j]) & (s["A"] == s["A"][j]) & np.isfinite(s["quorum"]))[0]
    return _device_lse(tie(s["src"][mine].astype(np.int64)), ex.pdf["gQ"](rec["u"][i] - s["quorum"][mine]))


def same_role(run, m, ex, rx, out, R, run_id):
    """Item 7: first relays and second relays (RELAY_SIZES nodes), two and three gatekeepers, and the record's own F
    with I. One table per coalition; relay tables carry `held`, the number of the record's packets whose relay in
    that position the coalition holds."""
    s, rec, base, shuf = run.subs, out["_rec"], out["_base"], out["_shuf"]
    srow, n = rec["sub"], rec["sub"].size
    ri = np.arange(n)
    res = {}
    for code, (role, pos) in enumerate((("first", "ADG"), ("second", "BEH"))):
        for k in RELAY_SIZES:
            S_ = _pick(R, run_id, code, k, np.arange(P.N_NODES))
            sc = _packet_level(run, m, rx, out, S_, (role,))
            held = sum(np.isin(s[x][srow], S_).astype(np.int8) for x in pos)
            res[f"{role}_relays_{k}"] = DS.table([a for a, _ in sc], [b for _, b in sc], rec, ri, np.zeros(n), base,
                                                 rec["dev"], shuf, held=held)
    for k in (2, 3):
        S_ = _pick(R, run_id, 2, k, run.gk_set)
        sc = _packet_level(run, m, rx, out, S_, ("gatekeeper",))
        res[f"gatekeepers_{k}"] = DS.table([a for a, _ in sc], [b for _, b in sc], rec, ri, np.zeros(n), base, rec["dev"], shuf)
    labs, scs = [], []
    cand = out["_cand"]
    for i in range(n):
        j = srow[i]
        lab, sc = _add([_arrival(cand, s["arr_f"][j], m.pdf["cs_q"]), _arrival(cand, s["arr_i"][j], m.pdf["cs_q"])])
        labs.append(lab)
        scs.append(sc)
    res["f_with_i"] = DS.table(labs, scs, rec, ri, np.zeros(n), base, rec["dev"], shuf)
    return res


def node_class(s, sub, S_):
    """Each record's class (NODE_CLASSES) for a coalition of nodes S_."""
    h = {x: np.isin(s[x][sub], S_) for x in "ABCDEFGHI"}
    gk = np.zeros(sub.shape, bool)              # filled by the caller when a node is an active gatekeeper
    exact_c = (h["F"] & h["D"]) | (h["I"] & h["G"])
    exact_cr = ~exact_c & h["A"] & h["C"]
    dest2 = ~exact_c & ~exact_cr & ((h["F"] & h["E"]) | (h["I"] & h["H"]))
    dest = ~exact_c & ~exact_cr & ~dest2 & (h["F"] | h["I"])
    timing = ~(exact_c | exact_cr | dest2 | dest) & (h["A"] | h["B"] | h["C"] | h["D"] | h["E"] | h["G"] | h["H"] | gk)
    code = np.full(sub.shape, 5, np.int8)
    for c, msk in enumerate((exact_c, exact_cr, dest2, dest, timing)):
        code[msk & (code == 5)] = c
    return code, h


def compromised(run, m, ex, rx, out, R, run_id):
    """Item 8: k nodes (NODE_COUNTS), each in every role it holds. A record is scored by its class: a held content
    path is exact; a held credential path links C's transactions through A by the time after quorum; a held
    destination uses its arrival (through its path's second relay when held); otherwise the observer with every
    relay, C and gatekeeper role the coalition holds, pooled."""
    s, rec, base, shuf = run.subs, out["_rec"], out["_base"], out["_shuf"]
    srow, n = rec["sub"], rec["sub"].size
    ri = np.arange(n)
    res = {}
    for k in NODE_COUNTS:
        S_ = _pick(R, run_id, 3, k, np.arange(P.N_NODES))
        cls, h = node_class(s, srow, S_)
        if np.isin(run.gk_set, S_).any():
            cls[cls == 5] = 4                       # an active gatekeeper holds every transaction
        sc = _packet_level(run, m, rx, out, S_, ("first", "second", "C", "gatekeeper"))
        labs, scs = [], []
        for i in range(n):
            if cls[i] == 0 or cls[i] == 2 or cls[i] == 3:
                held = {x: bool(h[x][i]) for x in "ABCDEFGHI"}
                lab, sc_i = _destination(run, m, out, rx, i, held, held, held)
            elif cls[i] == 1:
                lab, sc_i = _credential_exact(run, out, ex, i)
            else:
                lab, sc_i = sc[i]
            labs.append(lab)
            scs.append(sc_i)
        res[f"nodes_{k}"] = DS.table(labs, scs, rec, ri, np.zeros(n), base, rec["dev"], shuf, cls=cls)
    return res

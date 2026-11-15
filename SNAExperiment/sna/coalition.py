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

A first relay with the destination on its path. Scored on the records whose transaction used that path:
  content path (D with F, G with I): F holds the record and the content packet's arrival from E. Its
      candidates are the packets D sent to that E; each is weighed by the density of the second hop.
  credential path (A with C): C holds its transactions' arrivals from B and their fan-out times. Its
      candidates are pairs (C's transaction, a packet A sent to that transaction's B), weighed by the density
      of the second hop and the density of the record time after the fan-out.
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
    gCm  the record time minus the fan-out median, for the credential-path coalition"""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate, 0.2))
    acc = {k: [] for k in ("y", "xc", "yg", "xg", "yfa", "xfa", "p2", "cm")}
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
    for k, src in (("p2", "p2"), ("gCm", "cm")):
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
    """Tables of a first relay with the destination on its path, on the records whose transaction used the
    path: kind 0 credential (A with C), 1 F content (D with F), 2 I content (G with I)."""
    s, ev, rec, tie, shuf = run.subs, run.events, out["_rec"], out["_tie"], out["_shuf"]
    cand, base = out["_cand"], out["_base"]
    p2, gC = ex.pdf["p2"], ex.pdf["gCm"]
    u, srow, n = rec["u"], rec["sub"], rec["sub"].size
    # every first-hop packet: its first relay, its departure from it and the next hop it was sent to
    ts, ta, dst = ev["t_send"], ev["t_arr"], ev["dst"]
    fwd = np.full(ts.shape[0], -1, np.int64)
    for key in ("ev_cred", "ev_ca", "ev_cb"):
        fwd[s[key][:, 0]] = s[key][:, 1]
    first = ev["src"] == S.EXT
    first &= np.isin(np.arange(ts.size), np.r_[s["ev_cred"][:, 0], s["ev_ca"][:, 0], s["ev_cb"][:, 0]])
    pk = np.nonzero(first & (fwd >= 0))[0]
    relay, dep, nxt = dst[pk], ts[fwd[pk]], dst[fwd[pk]]
    dev = tie(ev["ext_src"][pk].astype(np.int64))
    key = relay.astype(np.int64) * 64 + nxt
    order = np.lexsort((dep, key))
    key, dep, dev = key[order], dep[order], dev[order]
    lo_p2, hi_p2 = p2.support
    m_all = np.sort(s["gk_send"], 1)[:, 1]
    labs, scs, ri, kind, grp = [], [], [], [], []
    for i in range(n):
        j = srow[i]
        for k, (fr, sr, dn, arr) in enumerate((("A", "B", "C", "arr_c"), ("D", "E", "F", "arr_f"), ("G", "H", "I", "arr_i"))):
            kk = int(s[fr][j]) * 64 + int(s[sr][j])
            if k > 0:
                a = s[arr][j]
                b0, b1 = np.searchsorted(key, kk, "left"), np.searchsorted(key, kk, "right")
                d = dep[b0:b1]
                c0, c1 = np.searchsorted(d, a - hi_p2), np.searchsorted(d, a - lo_p2, "right")
                sc = p2(a - d[c0:c1])
                lab = dev[b0:b1][c0:c1]
            else:
                # C's transactions whose record time fits, each paired with A's packets to that transaction's B
                Cn = int(s["C"][j])
                mine = np.nonzero((s["C"] == Cn) & np.isfinite(m_all))[0]
                y = u[i] - m_all[mine]
                lc = gC(y)
                mine, lc = mine[np.isfinite(lc)], lc[np.isfinite(lc)]
                lab_l, sc_l = [], []
                for jj, l1 in zip(mine, lc):
                    kj = int(s["A"][j]) * 64 + int(s["B"][jj])
                    b0, b1 = np.searchsorted(key, kj, "left"), np.searchsorted(key, kj, "right")
                    d = dep[b0:b1]
                    a = s["arr_c"][jj]
                    c0, c1 = np.searchsorted(d, a - hi_p2), np.searchsorted(d, a - lo_p2, "right")
                    lab_l.append(dev[b0:b1][c0:c1])
                    sc_l.append(l1 + p2(a - d[c0:c1]))
                lab = np.concatenate(lab_l) if lab_l else np.zeros(0, np.int64)
                sc = np.concatenate(sc_l) if sc_l else np.zeros(0)
            ok = np.isfinite(sc)
            lab, sc = lab[ok], sc[ok]
            if lab.size:
                u_, inv = np.unique(lab, return_inverse=True)
                mx = sc.max()
                agg = np.log(np.bincount(inv, weights=np.exp(sc - mx))) + mx
                lab, sc = u_, agg
            labs.append(lab)
            scs.append(sc)
            ri.append(i)
            kind.append(k)
            grp.append(int(s[fr][j]) * 32 + int(s[dn][j]))
    ri = np.array(ri, np.int64)
    return DS.table(labs, scs, rec, ri, np.array(grp), base, rec["dev"][ri], shuf, path=np.array(kind, np.int8))

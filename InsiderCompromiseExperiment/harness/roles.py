"""Rounds, per-role anchors and likelihood models, and the scoring of every scenario.

Every scenario scores ALL transactions of a run: each transaction has exactly one A, C, D, F and
V, and the three active gatekeepers each see every transaction. A row's group is the server that
held the role for it, and the joint assignment is solved per group (one compromised server at a
time). See ANALYSIS_PLAN.md section 3 for the attacks.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from . import ROOT  # noqa: F401  (puts birthmark_l3 and insider on the path)
from birthmark_l3 import attack as A
from birthmark_l3 import fastsim as FS
from birthmark_l3 import lottery as LT
from birthmark_l3 import params as P
from insider import core as K

from . import engine as E

INTERVAL_MIN = 20
ROUNDS = {
    1: dict(role_rules="catalog", ring_sig=False),
    2: dict(role_rules="insider_v2", ring_sig=True),
    3: dict(role_rules="insider_v2", ring_sig=True, gk_hold="gatekeeper"),
}
# Variants of a round (cells). "positive": the positive control (lottery and gatekeeper hold off).
VARIANTS = {
    "": {},
    "positive": dict(lottery_enabled=False, gk_hold=""),
}
TOL = 0.006


def devices_for(L: float) -> int:
    """Workbook Little's law at a 20-minute interval: L = devices / 20 x 2 min."""
    return int(round(L * INTERVAL_MIN / 2))


def round_config(rnd: int, L: float, variant: str = "", measure_min: float = 180.0, **kw) -> P.Config:
    base = dict(ROUNDS[rnd])
    base.update(VARIANTS[variant])
    base.update(kw)
    return P.Config(devices=devices_for(L), interval_min=INTERVAL_MIN, measure_s=measure_min * 60.0, **base)


# =========================================================================== wire helpers
def gk_leg_mask(run, pools):
    """Legs the observer can take for GK fan-out legs: the ring-signed GK class under Rounds 2/3,
    every relay-class message under Round 1 (its GK legs share the relay class)."""
    ev, cfg = run.events, run.cfg
    if not cfg.ring_sig:
        return A.signature_mask(ev, cfg.attacker_reads_record_type, pools.tls13_overhead)
    lo, hi = P.gk_class(True)
    m = (ev["size"] >= lo + pools.tls13_overhead) & (ev["size"] <= hi + pools.tls13_overhead)
    if cfg.attacker_reads_record_type:
        m &= ev["rtype"] == P.RT_APPDATA
    return m


def best_legs(ev, mask, c, tv, g, hop, hop_max):
    """For each item i: among the legs c[i] -> g sent in (tv[i], tv[i] + hop_max), the one with the
    highest hop likelihood (first one on ties, as the original per-candidate loop). Returns the
    hop log-likelihood (-inf if none), the leg's arrival time, and its event index."""
    n = c.shape[0]
    w = np.full(n, -np.inf)
    arr = np.full(n, np.nan)
    eid = np.full(n, -1, np.int64)
    sel = np.nonzero(mask & (ev["dst"] == g))[0]
    if sel.size == 0 or n == 0:
        return w, arr, eid
    src = ev["src"][sel]
    for cc in np.unique(c):
        items = np.nonzero(c == cc)[0]
        e = sel[src == cc]
        if e.size == 0:
            continue
        ts = ev["t_send"][e]
        a = np.searchsorted(ts, tv[items], side="right")
        b = np.searchsorted(ts, tv[items] + hop_max, side="left")
        width = b - a
        B = int(width.max()) if width.size else 0
        if B <= 0:
            continue
        for s0 in range(0, items.size, max(1, 2_000_000 // B)):
            it = items[s0:s0 + max(1, 2_000_000 // B)]
            aa, ww = a[s0:s0 + it.size], width[s0:s0 + it.size]
            j = np.arange(B)[None, :]
            valid = j < ww[:, None]
            idx = np.minimum(aa[:, None] + j, e.size - 1)
            dd = ts[idx] - tv[it][:, None]
            W = np.where(valid & (dd > 0) & (dd < hop_max), hop(np.clip(dd, 0, hop_max)), -np.inf)
            k = np.argmax(W, axis=1)
            best = W[np.arange(it.size), k]
            ok = np.isfinite(best)
            w[it[ok]] = best[ok]
            eid[it[ok]] = e[idx[np.arange(it.size), k][ok]]
            arr[it[ok]] = ev["t_arr"][eid[it[ok]]]
    return w, arr, eid


def best_prior(ev, mask_rows, c, t_ref, hop, hop_max):
    """For each item i: among the events in mask_rows arriving at node c[i] in (t_ref - hop_max,
    t_ref), the one that maximises hop(t_ref - arrival). Used by a gatekeeper to find the CV-2 that
    most likely triggered its own GK leg. Returns the arrival time (nan if none)."""
    n = c.shape[0]
    out = np.full(n, np.nan)
    sel = np.nonzero(mask_rows)[0]
    order = np.argsort(ev["t_arr"][sel], kind="stable")
    sel = sel[order]
    dst, ta = ev["dst"][sel], ev["t_arr"][sel]
    for cc in np.unique(c):
        items = np.nonzero(c == cc)[0]
        m = dst == cc
        t = ta[m]
        if t.size == 0:
            continue
        a = np.searchsorted(t, t_ref[items] - hop_max, side="right")
        b = np.searchsorted(t, t_ref[items], side="left")
        width = b - a
        B = int(width.max()) if width.size else 0
        if B <= 0:
            continue
        j = np.arange(B)[None, :]
        valid = j < width[:, None]
        idx = np.minimum(a[:, None] + j, t.size - 1)
        dd = t_ref[items][:, None] - t[idx]
        W = np.where(valid & (dd > 0) & (dd < hop_max), hop(np.clip(dd, 0, hop_max)), -np.inf)
        k = np.argmax(W, axis=1)
        ok = np.isfinite(W[np.arange(items.size), k])
        out[items[ok]] = t[idx[np.arange(items.size), k]][ok]
    return out


def cv2_mask(run, pools):
    ev, cfg = run.events, run.cfg
    sig = A.signature_mask(ev, cfg.attacker_reads_record_type, pools.tls13_overhead)
    src, dst = ev["src"].astype(int), ev["dst"].astype(int)
    return sig & (src >= P.N_NODES) & (src < P.N_NODES + P.N_VALIDATORS) & (dst < P.N_NODES)


def hold_mean(cfg) -> float:
    """Expected gatekeeper hold plus processing (the part of another gatekeeper's post time an
    insider cannot see)."""
    if cfg.gk_hold:
        return float(K._hold_samples(cfg, np.random.default_rng(7), m=20_000).mean())
    return K.GK_PROC_MEAN_S


# =========================================================================== anchors
def anchors(run, pools, lik):
    """Every role's anchor time per transaction (the latest event it knows exactly on the path to
    the registry, or an estimate built from its own knowledge plus the wire).
    Returns {name: (S,) or (S, 3)}; NaN = the role could not form an anchor."""
    ev, s, cfg = run.events, run.subs, run.cfg
    S = s["t0"].shape[0]
    out = {
        "A": ev["t_send"][s["ev_cred"][:, 1]],
        "D": ev["t_send"][s["ev_ca"][:, 1]],
        "N": ev["t_arr"][s["ev_cv2"]],                   # the GPA's own anchor (sequencing attack)
        "V.timing": ev["t_send"][s["ev_cv2"]],
        "C": K.quorum_from_legs(run),
    }
    if cfg.role_rules != "insider_v2":
        return out
    gks = [int(g) for g in s["gk"][0]]
    gm = gk_leg_mask(run, pools)
    mu = hold_mean(cfg)
    C = s["C"].astype(int)
    tv = ev["t_arr"][s["ev_cv2"]]
    a = np.stack([best_legs(ev, gm, C, tv, g, lik.hop, lik.hop_max)[1] for g in gks], 1)
    out["V.full"] = np.sort(np.where(np.isfinite(a), a + mu, np.inf), 1)[:, 1]
    # a compromised gatekeeper j: its own post exactly, and the other two posts estimated
    own_post = s["posts"]
    own_send = ev["t_send"][s["ev_gk"]]
    cvm = cv2_mask(run, pools)
    gk_t = np.empty((S, 3))
    gk_f = np.empty((S, 3))
    for j in range(3):
        gk_t[:, j] = own_post[:, j]
        tstar = best_prior(ev, cvm, C, own_send[:, j], lik.hop, lik.hop_max)
        est = [own_post[:, j]]
        for jj, g in enumerate(gks):
            if jj == j:
                continue
            ok = np.isfinite(tstar)
            aj = np.full(S, np.inf)
            if ok.any():
                aj[ok] = best_legs(ev, gm, C[ok], tstar[ok], g, lik.hop, lik.hop_max)[1] + mu
            est.append(np.where(np.isfinite(aj), aj, np.inf))
        gk_f[:, j] = np.sort(np.stack(est, 1), 1)[:, 1]
    out["GK.timing"], out["GK.full"] = gk_t, gk_f
    return out


def registry_answers(run, pools):
    """The registry postings on the wire (gossip origination), sorted by time, the transaction
    each belongs to, and each transaction's two right answers (F's and I's posting)."""
    ev, s = run.events, run.subs
    cols = A.gossip_origins(ev, run.cfg.attacker_reads_record_type, pools.gossip_wire)
    cols = cols[np.argsort(ev["t_send"][cols], kind="stable")]
    col_t = ev["t_send"][cols]
    col_sub = np.where(np.isin(ev["leg"][cols], [FS.REG_F_ORIGIN, FS.REG_I_ORIGIN]), ev["sub"][cols], -1)
    return col_t, col_sub, answers_of(col_sub, s["t0"].shape[0])


def answers_of(col_sub, S):
    """Each transaction's right answers: every detected posting that belongs to it (any message
    the burst detector picked from F's or I's flood counts, as in the published scoring)."""
    idx = np.nonzero(col_sub >= 0)[0]
    order = np.argsort(col_sub[idx], kind="stable")
    idx = idx[order]
    subs = col_sub[idx]
    cnt = np.bincount(subs, minlength=S)
    k = max(int(cnt.max()) if cnt.size else 1, 1)
    out = np.full((S, k), -1, np.int64)
    first = np.concatenate([[0], np.cumsum(cnt)[:-1]])
    slot = np.arange(idx.size) - first[subs]
    out[subs, slot] = idx
    return out


def reg_delays(run, pools, lik, anc=None):
    """Monte Carlo samples: registry posting time minus each role's anchor (both postings)."""
    ev, s = run.events, run.subs
    anc = anc if anc is not None else anchors(run, pools, lik)
    post = np.stack([ev["t_send"][s["ev_reg_f"]], ev["t_send"][s["ev_reg_i"]]], 1)
    out = {}
    for k, a in anc.items():
        a2 = a if a.ndim == 2 else a[:, None]
        d = (post[:, :, None] - a2[:, None, :]).ravel()
        out[k] = d[np.isfinite(d)]
    return out


# =========================================================================== models
@dataclass
class Models:
    reg: dict = field(default_factory=dict)       # role anchor -> EmpiricalLogPDF of posting - anchor
    f: object = None                              # F model (insider.core.InsiderModel fields)
    f_d2_all: object = None                       # N(a) for F: content arrival - CV-2, all items
    fine: bool = False


def build_models(cfg: P.Config, pools, lik, n_runs=None, seed0=900_000, min_samples=60_000) -> Models:
    """Monte Carlo of the protocol under the configuration being attacked, background off (it does
    not enter these delays), on seeds disjoint from the evaluation seeds."""
    mc_cfg = cfg.with_(bg_clients_per_node=0, nonblending_enabled=False)
    fine = not cfg.lottery_enabled
    reg, d1u, d2u, d2c, nc, nt = {}, [], [], [], 0, 0
    k = 0
    while True:
        run = FS.simulate(mc_cfg, seed0 + k, pools)
        for name, d in reg_delays(run, pools, lik).items():
            reg.setdefault(name, []).append(d)
        d1, d2, cens = K._content_features(run, "F")
        d1u.append(d1[~cens]); d2u.append(d2[~cens]); d2c.append(d2[cens])
        nc += int(cens.sum()); nt += cens.size
        k += 1
        have = min(sum(x.size for x in v) for v in reg.values())
        if (n_runs and k >= n_runs) or (not n_runs and have >= min_samples and k >= 3):
            break
    bw = 0.05 if fine else 0.5
    m = Models(fine=fine)
    for name, parts in reg.items():
        x = np.concatenate(parts)
        m.reg[name] = LT.EmpiricalLogPDF(x, bw)
    cat = np.concatenate
    d1u, d2u, d2c = cat(d1u), cat(d2u), cat(d2c)
    bw2 = 0.05 if fine else 2.0
    m.f = K.InsiderModel(
        p_cens=nc / nt, d1_unc=LT.EmpiricalLogPDF(d1u, 0.05 if fine else 0.5),
        d2_unc=LT.EmpiricalLogPDF(d2u, bw2), d2_cens=LT.EmpiricalLogPDF(d2c, bw2),
        seq_c=m.reg["C"], d_max=float(max(np.abs(d2u).max(), np.abs(d2c).max(), d1u.max())) + 5.0,
        seq_max=float(m.reg["C"].support[1]))
    m.f_d2_all = LT.EmpiricalLogPDF(cat([d2u, d2c]), bw2)
    m.mc_runs = k
    return m


# =========================================================================== scoring
def _scored(run):
    t0 = run.subs["t0"]
    return (t0 >= P.WARMUP_S) & (t0 < P.WARMUP_S + run.cfg.measure_s)


def _record(res, dec, groups, row_sub, keep):
    """Per-decision record for the scored rows."""
    r = dict(sub=row_sub[keep].astype(np.int32), group=groups[keep].astype(np.int16),
             correct=dec["correct"][keep].astype(np.int8),
             correct_argmax=dec["correct_argmax"][keep].astype(np.int8),
             pred=dec["pred_joint"][keep].astype(np.int32), pred_argmax=dec["pred_argmax"][keep].astype(np.int32),
             top1=res["top1"][keep].astype(np.float32), top2=res["top2"][keep].astype(np.float32),
             s_true=res["s_true"][keep].astype(np.float32), s_joint=dec["s_joint"][keep].astype(np.float32),
             rank=res["rank"][keep], n_feas=res["n_feas"][keep], n_true=res["n_true"][keep],
             rand=E.random_baseline(res)[keep].astype(np.float32), lse=res["lse"][keep])
    return r


def score_registry(anchor, pdf, col_t, fn_extra=None):
    lo, hi = pdf.support
    return (anchor + lo, anchor + hi)


def run_registry_role(anchor, pdf, col_t, col_sub, true_cols, row_sub, groups, keep):
    ok = np.isfinite(anchor)
    a = np.where(ok, anchor, -1e12)

    def fn(r, c):
        return pdf(col_t[c] - a[r])
    t_lo = np.where(ok, a + pdf.support[0], np.inf)
    t_hi = np.where(ok, a + pdf.support[1], np.inf)
    res = E.score_rows(t_lo, t_hi, col_t, fn, true_cols)
    dec = E.decide(res, groups, col_sub, row_sub, true_cols)
    return _record(res, dec, groups, row_sub, keep), res


def n_registry(run, lik, col_t, col_sub, true_cols, keep):
    """N(a) on the registry answer list: the published GPA sequencing likelihood, anchored at each
    transaction's CV-2 arrival at C. Scored once; the joint assignment is then grouped per role."""
    ev, s = run.events, run.subs
    a = ev["t_arr"][s["ev_cv2"]]

    def fn(r, c):
        d = col_t[c] - a[r]
        return np.where((d > 0) & (d < lik.seq_max), lik.seq(np.clip(d, 0, lik.seq_max)), -np.inf)
    return E.score_rows(a, a + lik.seq_max, col_t, fn, true_cols)


def credential_answers(run, pools):
    """Validator replies (CV-2) seen arriving at C servers, sorted by arrival time."""
    ev, s = run.events, run.subs
    cols = np.nonzero(cv2_mask(run, pools))[0]
    cols = cols[np.argsort(ev["t_arr"][cols], kind="stable")]
    pos = np.full(ev["t_send"].shape[0], -1, np.int64)
    pos[cols] = np.arange(cols.size)
    return cols, ev["t_arr"][cols], ev["dst"][cols].astype(int), ev["sub"][cols], pos[s["ev_cv2"]][:, None]


def f_scores(run, pools, lik, m: Models, rng):
    """F (Rounds 2/3 and Round 1) plus N(a) for F. The credential answer list, as in Rounds 1-3."""
    ev, s, cfg = run.events, run.subs, run.cfg
    fm = m.f
    cols, t_v, c_node, col_sub, true_cols = credential_answers(run, pools)
    S = s["t0"].shape[0]
    F = s["F"].astype(int)
    arr, det = s["arr_f"], s["det_f"]
    cens = np.abs(det - LT.next_tick(arr, run.phase[F])) < 1e-6
    lp, lq = np.log(fm.p_cens), np.log(1 - fm.p_cens)
    out = {}

    def timing(r, c):
        d1, d2 = det[r] - t_v[c], arr[r] - t_v[c]
        w = np.where(cens[r], lp + fm.d2_cens(d2), lq + fm.d1_unc(d1) + fm.d2_unc(d2))
        return np.where(d1 > 0, w, -np.inf)
    d2hi = max(fm.d2_unc.support[1], fm.d2_cens.support[1])
    t_lo = np.minimum(det - fm.d1_unc.support[1], arr - d2hi)
    out["F.timing"] = E.score_rows(t_lo, det, t_v, timing, true_cols)

    def nf(r, c):                           # N(a) for F: content arrival only
        return m.f_d2_all(arr[r] - t_v[c])
    lo2, hi2 = m.f_d2_all.support
    out["N.F"] = E.score_rows(arr - hi2, arr - lo2 + 1e-9, t_v, nf, true_cols)

    if cfg.role_rules == "insider_v2":
        gks = [int(g) for g in s["gk"][0]]
        gm = gk_leg_mask(run, pools)
        legs = [best_legs(ev, gm, c_node, t_v, g, lik.hop, lik.hop_max) for g in gks]
        total = sum(L[0] for L in legs)                                    # -inf if any leg missing
        arrs = np.stack([L[1] for L in legs], 1)
        if cfg.gk_hold:
            held = K._hold_samples(cfg, rng).ravel()
            Gs = np.sort(held)
            mfloor = 1.0 / (held.size // 3)

            def Fq(x, c):
                p = np.searchsorted(Gs, x[:, None] - arrs[c], side="right") / Gs.size
                return p[:, 0] * p[:, 1] + p[:, 0] * p[:, 2] + p[:, 1] * p[:, 2] - 2 * p.prod(1)

            def agree(r, c):
                up = Fq(det[r] + TOL, c)
                pr = np.where(cens[r], up, up - Fq(det[r] - P.TICK_S - TOL, c))
                return np.log(np.maximum(pr, mfloor))
        else:
            q = np.sort(arrs, 1)[:, 1] + K.GK_PROC_MEAN_S

            def agree(r, c):
                ok = (q[c] <= det[r] + TOL) & (cens[r] | (q[c] > det[r] - P.TICK_S - TOL))
                return np.where(ok, 0.0, K.INCONSISTENT)

        def base(r, c):
            d1 = det[r] - t_v[c]
            return (d1 > 0) & (d1 < fm.d_max) & np.isfinite(total[c])

        def full(r, c):
            d2 = arr[r] - t_v[c]
            term = np.where(cens[r], fm.d2_cens(d2), fm.d2_unc(d2))
            term = np.where(np.isfinite(term), term, -10.0)
            return np.where(base(r, c), total[c] + agree(r, c) + term, -np.inf)

        def legs_only(r, c):
            return np.where(base(r, c), total[c] + agree(r, c), -np.inf)
        out["F.full"] = E.score_rows(det - fm.d_max, det, t_v, full, true_cols)
        out["F.legs"] = E.score_rows(det - fm.d_max, det, t_v, legs_only, true_cols)
    else:
        out["F.full"] = _f_round1_full(run, pools, lik, fm, t_v, c_node, true_cols, arr, det, cens)
    return out, (t_v, col_sub, true_cols)


def _f_round1_full(run, pools, lik, fm, t_v, c_node, true_cols, arr, det, cens):
    """Round 1 full variant (harness/round1.py), vectorised: candidates are C's own validator replies
    (the board record names C), the transaction's gatekeepers are known, and when F is also one of
    them its own received GK leg replaces the search for that gatekeeper."""
    ev, s = run.events, run.subs
    S, N = s["t0"].shape[0], P.N_NODES
    sig = A.signature_mask(ev, run.cfg.attacker_reads_record_type, pools.tls13_overhead)
    bw = np.full((t_v.size, N), -np.inf)
    ba = np.full((t_v.size, N), np.nan)
    for g in range(N):
        w, a, _ = best_legs(ev, sig, c_node, t_v, g, lik.hop, lik.hop_max)
        bw[:, g], ba[:, g] = w, a
    gk = s["gk"].astype(int)
    valid = s["gk_valid"]
    X = s["F"].astype(int)
    own = (gk == X[:, None]) & valid
    own_eid = np.where(own, s["ev_gk"], -1)
    own_send = np.where(own_eid >= 0, ev["t_send"][np.maximum(own_eid, 0)], np.nan)
    own_arr = np.where(own_eid >= 0, ev["t_arr"][np.maximum(own_eid, 0)], np.nan)
    C = s["C"].astype(int)

    def full(r, c):
        g = gk[r]
        w = bw[c[:, None], g]
        a = ba[c[:, None], g]
        dd = own_send[r] - t_v[c][:, None]
        w_own = np.where((dd > 0) & (dd < lik.hop_max), lik.hop(np.clip(np.nan_to_num(dd), 0, lik.hop_max)), -np.inf)
        w = np.where(own[r], w_own, w)
        a = np.where(own[r], own_arr[r], a)
        v = valid[r]
        total = np.where(v, w, 0.0).sum(1)
        missing = (v & ~np.isfinite(w)).any(1)
        arrivals = np.where(v, a + K.GK_PROC_MEAN_S, np.inf)
        q = np.sort(arrivals, 1)[:, 1]
        ok = (q <= det[r] + TOL) & (cens[r] | (q > det[r] - P.TICK_S - TOL))
        d2 = arr[r] - t_v[c]
        term = np.where(cens[r], fm.d2_cens(d2), fm.d2_unc(d2))
        term = np.where(np.isfinite(term), term, -10.0)
        wf = total + np.where(ok, 0.0, K.INCONSISTENT) + term
        return np.where((c_node[c] == C[r]) & (det[r] - t_v[c] > 0) & ~missing, wf, -np.inf)
    # candidates are C's own replies only: score per C so each row's band holds only its C's replies
    res_parts = []
    order = np.argsort(t_v, kind="stable")
    n = S
    merged = None
    for cc in np.unique(C):
        rows = np.nonzero(C == cc)[0]
        cidx = np.nonzero(c_node == cc)[0]            # sorted by time (t_v is sorted)
        sub_t = t_v[cidx]
        tc = np.where(np.isin(true_cols[rows], cidx), np.searchsorted(cidx, true_cols[rows]), -1)
        res = E.score_rows(np.full(rows.size, -np.inf), det[rows], sub_t,
                           lambda r, c: full(rows[r], cidx[c]), tc)
        res_parts.append((rows, cidx, res))
    return _merge_parts(res_parts, n)


def _merge_parts(parts, n):
    """Combine per-group score_rows outputs (local row/answer indices) into one global output."""
    tmpl = parts[0][2]
    out = {k: np.empty((n,) + v.shape[1:], v.dtype) for k, v in tmpl.items() if k != "edges"}
    er, ec, ew = [], [], []
    for rows, cidx, res in parts:
        for k in out:
            out[k][rows] = res[k]
        am = res["argmax"]
        out["argmax"][rows] = np.where(am >= 0, cidx[np.maximum(am, 0)], -1)
        r, c, w = res["edges"]
        er.append(rows[r]); ec.append(cidx[c]); ew.append(w)
    out["edges"] = (np.concatenate(er), np.concatenate(ec), np.concatenate(ew))
    return out

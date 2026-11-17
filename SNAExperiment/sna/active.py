"""Active attacks (C5): delay marking and drop with resubmission, scored by record-finding accuracy.

The actor recognises its target's transaction when it acts, and later picks, among the records posted after
its act, the one most likely to be the marked transaction's. Its anchor is a time it knows:
  first relay        when it released the packet it held (delay), or when the packet reached it (drop)
  access network     the latest of the times it released the target's packets (delay), or when the first
                     packet left the device (drop)
  validator          when it sent the reply (also when it withholds the other credentials' replies)
It scores every record by the density of (record time minus anchor) under the marked system, built on the model
seeds with every real device marked (a histogram with 15-second bins), and picks the highest; records of one posting tie, and a tie breaks at
random. Record-finding accuracy is the share of marked transactions whose record (for a drop, the
resubmission's record) it picks. A marked transaction with no record counts as missed. Chance is one over the
records the density does not rule out.
"""
from __future__ import annotations

import numpy as np

from . import attacks as AT
from . import lottery as LT
from . import sim as S

LEG1 = {0: "ev_cred", 1: "ev_ca", 2: "ev_cb"}


def anchors(run):
    """Per marked transaction: (sub, anchor time, the transaction whose record is sought)."""
    cfg, s, ev = run.cfg, run.subs, run.events
    m = np.nonzero(s["marked"])[0]
    path = s["mark_path"][m]
    ts, ta = ev["t_send"], ev["t_arr"]
    a = np.full(m.size, np.nan)
    drop = cfg.mark_mode == "drop"
    for k in range(3):
        e = s[LEG1[k]][m]
        if cfg.mark_actor in ("first_relay", "access_one"):
            sel = path == k
            if cfg.mark_actor == "first_relay":
                a[sel] = (ta[e[sel, 0]] if drop else ts[e[sel, 1]])
            else:
                a[sel] = (ts[e[sel, 0]] if drop else ta[e[sel, 0]])
        elif cfg.mark_actor == "access":
            t = ts[e[:, 0]] if drop else ta[e[:, 0]]
            a = np.fmin(a, t) if drop else np.fmax(a, t)
    if cfg.mark_actor.startswith("validator"):          # marking its target's reply, or withholding the others
        a = s["cv2_s"][m]
    target = m.copy()
    if drop:
        child = np.full(s["t0"].size, -1, np.int64)
        kids = np.nonzero(s["parent"] >= 0)[0]
        child[s["parent"][kids]] = kids
        target = child[m]
    return m, a, target


def model_samples(run):
    """Record time minus anchor for every marked transaction with a record (the attacker's model)."""
    m, a, target = anchors(run)
    ok = target >= 0
    u = np.full(m.size, np.nan)
    u[ok] = run.subs["posted"][target[ok]]
    return (u - a)[np.isfinite(u - a)]


def build_model(cfg, seeds, bw=15.0):
    """The density of the record time after the anchor; None when no marked transaction ever posts a record (a
    mark longer than the quorum timeout drops every one), and the attacker then finds nothing."""
    x = np.concatenate([model_samples(S.simulate(cfg, sd)) for sd in seeds])
    return (LT.EmpiricalLogPDF(x, bw) if x.size else None), int(x.size)


def score(run, pdf, rng, window):
    """Record-finding outcomes for the marked transactions captured in the window."""
    s = run.subs
    m, a, target = anchors(run)
    inwin = (s["t0"][m] >= window[0]) & (s["t0"][m] < window[1])
    m, a, target = m[inwin], a[inwin], target[inwin]
    fin = np.nonzero(np.isfinite(s["posted"]))[0]
    o = np.argsort(s["posted"][fin], kind="stable")
    rs, ru = fin[o], s["posted"][fin][o]
    lo, hi = pdf.support if pdf is not None else (0.0, 0.0)
    correct = np.zeros(m.size, np.int8)
    found = ((target >= 0) & np.isfinite(s["posted"][np.maximum(target, 0)])).astype(np.int8)
    nfeas = np.zeros(m.size, np.int32)
    nT = AT.T_GRID.size
    top1, s_true = np.full(m.size, -np.inf), np.full(m.size, -np.inf)
    lse, ent = np.full((m.size, nT), np.nan), np.full((m.size, nT), np.nan)
    rank = np.full(m.size, -1, np.int32)
    for i in range(m.size if pdf is not None else 0):
        if not np.isfinite(a[i]):
            continue
        b0, b1 = np.searchsorted(ru, a[i] + lo, "left"), np.searchsorted(ru, a[i] + hi, "right")
        if b1 <= b0:
            continue
        sc = pdf(ru[b0:b1] - a[i])
        ok = np.isfinite(sc)
        nfeas[i] = int(ok.sum())
        if not ok.any():
            continue
        best = np.nonzero(sc == sc[ok].max())[0]
        pick = rs[b0:b1][best[rng.integers(0, best.size)]]
        correct[i] = int(target[i] >= 0 and pick == target[i])
        # the posterior over the candidate records, for the spread metrics (the decision above is unchanged)
        top1[i] = sc[ok].max()
        is_t = (rs[b0:b1] == target[i]) & ok
        if is_t.any():
            s_true[i] = sc[is_t].max()
        rank[i] = int((sc[ok] > s_true[i]).sum()) if is_t.any() else nfeas[i]
        for k, T in enumerate(AT.T_GRID):
            x = sc[ok] / T
            lse[i, k] = np.log(np.exp(x - x.max()).sum()) + x.max() - top1[i] / T
            ent[i, k] = AT._entropy(sc[ok][None, :], T)[0]
    rand = np.where(np.isfinite(s_true) & (nfeas > 0), 1.0 / np.maximum(nfeas, 1), 0.0)
    return dict(sub=m.astype(np.int32), correct=correct, has_record=found, n_feas=nfeas,
                path=s["mark_path"][m].astype(np.int8), dev_v_correct=correct, dev_v_rand=rand.astype(np.float32),
                dev_n_feas=nfeas, dev_top1=top1.astype(np.float32), dev_s_true=s_true.astype(np.float32),
                dev_lse=lse.astype(np.float16), dev_ent=ent.astype(np.float16), dev_rank=rank)

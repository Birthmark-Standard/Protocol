"""One run -> every requested decision record.

Scenarios: N, A, C, D, F, V, GK. Records written per run:
  F.timing, F.full, F.legs (Rounds 2/3)   F.timing, F.full (Round 1)   N.F      (N(a) paired with F)
  C, A, D, V.timing, V.full, GK.timing, GK.full                         N@<role> (N(a) paired)
  Nb.seq  the published sequencing attack (all transactions, one joint assignment)
  Nb.main the published main attack, per transaction (L <= 40: its dense assignment)
"""
from __future__ import annotations

import hashlib

import numpy as np

from . import ROOT  # noqa: F401
from birthmark_l3 import fastsim as FS
from birthmark_l3 import params as P

from . import engine as E
from . import roles as R

SCENARIOS = ("N", "A", "C", "D", "F", "V", "GK")
NB_MAIN_MAX_DEVICES = 400      # L <= 40


def traffic_seed(base: int, L: float, run: int, n_nodes: int = 20) -> int:
    """Common random numbers: the traffic depends on (base seed, L, run id, pool size) only, so
    every scenario and every round reads the same traffic."""
    return int.from_bytes(hashlib.sha256(f"insider-x:{base}:{L:g}:{run}:{n_nodes}".encode()).digest()[:4], "big")


def attack_seed(base: int, rnd: int, L: float, run: int, scenario: str) -> int:
    return int.from_bytes(hashlib.sha256(f"insider-x-attack:{base}:{rnd}:{L:g}:{run}:{scenario}".encode()).digest()[:4], "big")


def compute(run, pools, lik, models, scenarios, rnd, L, base, run_id):
    ev, s, cfg = run.events, run.subs, run.cfg
    S = s["t0"].shape[0]
    keep = R._scored(run)
    sub = np.arange(S)
    recs = {}
    v2 = cfg.role_rules == "insider_v2"
    need_reg = any(x in scenarios for x in ("N", "A", "C", "D", "V", "GK"))
    if need_reg:
        col_t, col_sub, true_cols = R.registry_answers(run, pools)
        anc = R.anchors(run, pools, lik)
        nres = R.n_registry(run, lik, col_t, col_sub, true_cols, keep)

        def n_paired(groups, name):
            dec = E.decide(nres, groups, col_sub, sub, true_cols)
            recs[name] = R._record(nres, dec, groups, sub, keep)

        role_groups = {"A": s["A"], "C": s["C"], "D": s["D"], "V": s["val"] - FS.VAL0}
        for role in ("A", "C", "D"):
            if role in scenarios:
                recs[role], _ = R.run_registry_role(anc[role], models.reg[role], col_t, col_sub, true_cols,
                                                    sub, role_groups[role], keep)
                n_paired(role_groups[role], f"N@{role}")
        if "V" in scenarios and v2:
            for var in ("V.timing", "V.full"):
                recs[var], _ = R.run_registry_role(anc[var], models.reg[var], col_t, col_sub, true_cols,
                                                   sub, role_groups["V"], keep)
            n_paired(role_groups["V"], "N@V")
        if "GK" in scenarios and v2:
            rows3 = np.tile(sub, 3)
            g3 = np.repeat(np.arange(3), S)
            k3 = np.tile(keep, 3)
            t3 = np.tile(true_cols, (3, 1))
            for var in ("GK.timing", "GK.full"):
                a3 = anc[var].T.ravel()
                recs[var], _ = R.run_registry_role(a3, models.reg[var], col_t, col_sub, t3, rows3, g3, k3)
        if "GK" in scenarios or "N" in scenarios:
            n_paired(np.zeros(S, np.int16), "Nb.seq")          # one joint assignment over everything
    if "F" in scenarios:
        rng = np.random.default_rng(attack_seed(base, rnd, L, run_id, "F"))
        fres, (t_v, ccol_sub, ctrue) = R.f_scores(run, pools, lik, models, rng)
        groups = s["F"]
        for name, res in fres.items():
            dec = E.decide(res, groups, ccol_sub, sub, ctrue)
            recs[name] = R._record(res, dec, groups, sub, keep)
    if "N" in scenarios and cfg.devices <= NB_MAIN_MAX_DEVICES:
        recs["Nb.main"] = nb_main(run, lik, pools, keep)
    return recs


def nb_main(run, lik, pools, keep):
    """The published main attack (attack.attack_run): Stage 1 chain reconstruction unchanged, then
    Stage 2 (origin-time pairing of credential and content chains) scored banded, because the
    origin likelihood is -inf beyond origin_max, and solved with the sparse optimal assignment. Same
    scores and objective as the dense published version; its dense matrix does not fit in memory
    over a 3-hour window at L = 40."""
    from birthmark_l3 import attack as A
    ev, subs, cfg = run.events, run.subs, run.cfg
    sig = A.signature_mask(ev, cfg.attacker_reads_record_type, pools.tls13_overhead)
    s1 = A.stage1(ev, sig, lik)
    cred, cont, _ = A.build_chains(ev, sig, s1)
    S = subs["t0"].shape[0]
    leg, sub_of = ev["leg"], ev["sub"]
    oc = np.where(cred["ok"], ev["t_arr"][np.maximum(cred["origin_ev"], 0)], np.nan)
    ox = ev["t_arr"][cont["origin_ev"]]
    order = np.argsort(ox, kind="stable")
    ox_s = ox[order]
    cont_term_sub = np.where(np.isin(leg[cont["term"]], [FS.CA3, FS.CB3]), sub_of[cont["term"]], -1)[order]
    om = lik.origin_max

    def fn(r, c):
        d = oc[r] - ox_s[c]
        return np.where(np.abs(d) < om, lik.origin(np.clip(d, -om, om)), -np.inf)
    ok = np.isfinite(oc)
    t_lo = np.where(ok, oc - om, np.inf)
    t_hi = np.where(ok, oc + om, np.inf)
    row_is_cred3 = leg[cred["term"]] == FS.CRED3
    row_sub = np.where(row_is_cred3, sub_of[cred["term"]], -1)
    from .roles import answers_of
    res = E.score_rows(t_lo, t_hi, ox_s, fn, answers_of(cont_term_sub, S)[np.maximum(row_sub, 0)] *
                       (row_sub >= 0)[:, None] - (row_sub < 0)[:, None])
    pick = E.joint_assign(oc.shape[0], res["edges"], np.zeros(oc.shape[0], int))
    pred = np.where(pick >= 0, cont_term_sub[np.maximum(pick, 0)], -1)
    sc = np.nonzero(keep)[0]
    row_of_sub = np.full(S, -1, np.int64)
    row_of_sub[row_sub[row_is_cred3]] = np.nonzero(row_is_cred3)[0]
    r = row_of_sub[sc]
    has = r >= 0
    correct = has & (np.where(has, pred[np.maximum(r, 0)], -2) == sc)
    top1 = np.where(has, res["top1"][np.maximum(r, 0)], -np.inf)
    top2 = np.where(has, res["top2"][np.maximum(r, 0)], -np.inf)
    with np.errstate(invalid="ignore"):
        gap = np.where(np.isfinite(top1), top1 - top2, np.nan)
    return dict(sub=sc.astype(np.int32), correct=correct.astype(np.int8), gap=gap.astype(np.float32),
                detected=has.astype(np.int8))

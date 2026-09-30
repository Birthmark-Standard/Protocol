"""Equivalence of the tool's F attack with the original (insider/core.py), on the original runs.

The tool scores F with a vectorised implementation (banded answer list, sparse top-K joint
assignment, and for the gatekeeper hold the exact probability that the held quorum lands in F's
detection window, where the original averaged 2,000 Monte Carlo draws). This check runs it in the
original setting (one compromised node per run, 40-minute window, the original attacker models,
the original seeds) and compares it decision by decision with the stored Round 2 and Round 3 runs.

    python -m harness equivalence
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from . import ROOT
from . import engine as E
from . import runner as RN

CASES = {  # name -> (round, devices, stored raw file under results/raw)
    "r2_F_L8": (2, 80, "ring_F_80"), "r2_F_L40": (2, 400, "ring_F_400"),
    "r3_F_L8": (3, 80, "gkhold_F_80"), "r3_F_L40": (3, 400, "gkhold_F_400"),
}
RUNS = 200
_W = {}


def _worker(name, k):
    from birthmark_l3 import attack as A
    from birthmark_l3 import fastsim as FS
    from birthmark_l3 import params as P
    from birthmark_l3.wire_pools import Pools
    from insider import core as K
    from insider.run import seed_for
    from . import roles as R
    rnd, d, _ = CASES[name]
    if "pools" not in _W:
        _W["pools"] = Pools()
    pools = _W["pools"]
    kw = dict(ring_sig=True, gk_hold="gatekeeper" if rnd == 3 else "")
    cfg = K.adopted_config(d, 20, **kw)
    if rnd not in _W:
        fm = K.build_model(pools, gk_hold=kw["gk_hold"])
        _W[rnd] = (R.Models(f=fm, f_d2_all=fm.d2_unc), A.build_likelihoods(cfg))
    models, lik = _W[rnd]
    seed = seed_for("F", d, k)
    run = FS.simulate(cfg, seed, pools)
    X = int(np.random.default_rng(seed ^ 0x5EED).integers(0, P.N_NODES))
    fres, (t_v, col_sub, true_cols) = R.f_scores(run, pools, lik, models, np.random.default_rng(seed))
    s = run.subs
    items = np.nonzero(s["F"] == X)[0]
    scored = K._scored_mask(run, items)
    out = dict(run=k, X=X)
    for var in ("timing", "full", "legs"):
        res = fres[f"F.{var}"]
        # the original solves one assignment over X's items only: restrict the group to X
        groups = np.where(s["F"] == X, 0, 1 + np.arange(s["F"].size))
        dec = E.decide(res, groups, col_sub, np.arange(s["F"].size), true_cols)
        out[var] = dec["correct"][items][scored].astype(np.int8)
    return [(name, out)]


def run(out: Path, workers="auto"):
    tasks = []
    for name in CASES:
        done = RN.done_runs(out, name)
        tasks += [(name, k) for k in range(RUNS) if k not in done]
    tasks.sort(key=lambda t: (t[1], t[0]))
    RN.execute(tasks, _worker, out, workers, label="equivalence")
    return report(out)


def report(out: Path):
    from .regress import _load_file
    rng = np.random.default_rng(0)
    rows, ok_all = [], True
    for name, (rnd, d, stored) in CASES.items():
        new = {r["run"]: r for r in RN.load(out, name)}
        old = _load_file(ROOT / "results" / "raw" / f"{stored}.pkl.gz")
        for var in ("timing", "full", "legs"):
            a = np.concatenate([old[k][var]["correct"] for k in sorted(new)])
            b = np.concatenate([new[k][var] for k in sorted(new)])
            per = np.array([[old[k][var]["correct"].sum(), new[k][var].sum(), new[k][var].size] for k in sorted(new)], float)
            idx = rng.integers(0, per.shape[0], (2000, per.shape[0]))
            diff = (per[idx, 1].sum(1) - per[idx, 0].sum(1)) / per[idx, 2].sum(1)
            lo, hi = np.percentile(diff, [2.5, 97.5])
            same = bool(lo <= 0 <= hi)
            ok_all &= same
            rows.append(dict(case=name, variant=var, n=int(a.size), original=round(float(a.mean()), 4),
                             tool=round(float(b.mean()), 4), agreement=round(float((a == b).mean()), 4),
                             diff_ci95=[round(float(lo), 4), round(float(hi), 4)],
                             status="PASS" if same else "FAIL"))
    res = dict(passed=bool(ok_all), checks=rows)
    Path(out).mkdir(parents=True, exist_ok=True)
    (Path(out) / "equivalence.json").write_text(json.dumps(res, indent=1))
    for r in rows:
        print(r)
    print("EQUIVALENCE", "PASSED" if ok_all else "FAILED")
    return res

"""Regression check: reproduce the published Round 1 and Round 3 results through the tool.

Runs the ORIGINAL attack code (harness/round1.py for Round 1, insider/core.py for Round 3) on the
ORIGINAL seeds and settings (one compromised node per run, 40-minute scored window), through this
tool's runner. Where the stored raw results of those rounds are on disk, every run's per-item
outcomes must match bit for bit. Everywhere, the accuracy must fall inside the published 95% CI.

    python -m harness regress --out results/regression
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from . import ROOT
from . import runner as RN

# name -> (round, devices, interval, published accuracy, published 95% CI, stored raw file)
CHECKS = {
    "r1_F_L4": (1, 40, 20, 0.8564, None, "results/raw_first_run/t1_F.pkl.gz"),
    "r1_F_L40": (1, 200, 10, 0.3261, None, "results/raw_first_run/t2_F_200_10.pkl.gz"),
    "r3_F_L8": (3, 80, 20, None, None, "results/raw/gkhold_F_80.pkl.gz"),
    "r3_F_L24": (3, 240, 20, None, None, "results/raw/gkhold_F_240.pkl.gz"),
    "r3_F_L40": (3, 400, 20, None, None, "results/raw/gkhold_F_400.pkl.gz"),
}
RUNS = 200


def _published():
    """Published accuracy and CI of the full variant, from the committed summaries."""
    first = json.loads((ROOT / "results/first_run/summary.json").read_text())
    cur = json.loads((ROOT / "results/summary.json").read_text())["runs"]
    pub = {"r1_F_L4": first["tier1"]["F"]["full"], "r1_F_L40": first["tier2"]["F_200_10"]["full"]}
    for d, L in ((80, 8), (240, 24), (400, 40)):
        pub[f"r3_F_L{L}"] = cur[f"gkhold_F_{d}"]["full"]
    return {k: (v["accuracy"], v["ci95"]) for k, v in pub.items()}


def seed_for(name, k):
    rnd, d, i = CHECKS[name][:3]
    if rnd == 1:     # Round 1 runner (commit 49cab2b): job names t1_F and t2_F_<devices>_<interval>
        job = "t1_F" if (d, i) == (40, 20) else f"t2_F_{d}_{i}"
        return int.from_bytes(hashlib.sha256(f"insider:{job}:{k}".encode()).digest()[:4], "big")
    from insider.run import seed_for as r3_seed    # Rounds 2 and 3 runner
    return r3_seed("F", d, k)


_W = {}


def _worker(name, k):
    import time
    from birthmark_l3 import attack as A
    from birthmark_l3.wire_pools import Pools
    rnd, d, i = CHECKS[name][:3]
    if "pools" not in _W:
        _W["pools"] = Pools()
    pools = _W["pools"]
    if rnd == 1:
        from . import round1 as K
        cfg = K.adopted_config(d, i)
        if "r1" not in _W:
            _W["r1"] = (K.build_model(pools), A.build_likelihoods(cfg))
        model, lik = _W["r1"]
    else:
        from insider import core as K
        cfg = K.adopted_config(d, i, ring_sig=True, gk_hold="gatekeeper")
        if "r3" not in _W:
            _W["r3"] = (K.build_model(pools, gk_hold="gatekeeper"), A.build_likelihoods(cfg))
        model, lik = _W["r3"]
    t = time.time()
    out = K.run_scenario("F", cfg, seed_for(name, k), pools, lik, model)
    out["run"], out["seconds"] = k, time.time() - t
    return [(name, out)]


def run(out: Path, workers="auto", names=None):
    names = names or list(CHECKS)
    tasks = []
    for name in names:
        done = RN.done_runs(out, name)
        tasks += [(name, k) for k in range(RUNS) if k not in done]
    tasks.sort(key=lambda t: (t[1], t[0]))
    RN.execute(tasks, _worker, out, workers, label="regress")
    return report(out, names)


def _acc_ci(runs, rng):
    c = np.concatenate([r["full"]["correct"] for r in runs]).astype(float)
    per = [(r["full"]["correct"].sum(), r["full"]["correct"].size) for r in runs]
    k = np.array(per, float)
    boots = []
    for _ in range(2000):
        s = k[rng.integers(0, len(k), len(k))]
        boots.append(s[:, 0].sum() / max(s[:, 1].sum(), 1))
    return c.mean(), np.percentile(boots, [2.5, 97.5]), c.size


def report(out: Path, names=None):
    pub = _published()
    rng = np.random.default_rng(0)
    rows, ok_all = [], True
    for name in names or list(CHECKS):
        runs = sorted(RN.load(out, name), key=lambda r: r["run"])
        if len(runs) < RUNS:
            rows.append(dict(check=name, status=f"incomplete ({len(runs)}/{RUNS} runs)"))
            ok_all = False
            continue
        acc, ci, n = _acc_ci(runs, rng)
        p_acc, p_ci = pub[name]
        within = p_ci[0] <= acc <= p_ci[1]
        stored = ROOT / CHECKS[name][5]
        bitwise = None
        if stored.exists():
            old = _load_file(stored)
            same = [np.array_equal(old[r["run"]]["full"]["correct"], r["full"]["correct"])
                    and np.array_equal(old[r["run"]]["timing"]["correct"], r["timing"]["correct"])
                    for r in runs if r["run"] in old]
            bitwise = f"{sum(same)}/{len(same)} runs identical"
            within = within and all(same) and len(same) == RUNS
        ok_all &= within
        rows.append(dict(check=name, accuracy=round(acc, 4), ci95=[round(x, 4) for x in ci], n=n,
                         published=round(p_acc, 4), published_ci95=[round(x, 4) for x in p_ci],
                         stored_raw=bitwise, status="PASS" if within else "FAIL"))
    res = dict(passed=bool(ok_all), checks=rows)
    (Path(out) / "regression.json").write_text(json.dumps(res, indent=1))
    for r in rows:
        print(r)
    print("REGRESSION", "PASSED" if ok_all else "FAILED")
    return res


def _load_file(p: Path):
    import gzip
    import pickle
    res = {}
    with gzip.open(p, "rb") as f:
        while True:
            try:
                r = pickle.load(f)
                res[r["run"]] = r
            except (EOFError, OSError, pickle.UnpicklingError):
                break
    return res

"""Shuffle control check (prediction in results/v2/checks/shuffle_check_prediction.md).

Run from SNAExperiment/:  python audit/shuffle_check.py <work_dir>
work_dir holds the models; calibration is copied from results/v2. Writes
results/v2/checks/shuffle_check.json.
"""
import json
import shutil
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sna import analyze as AN, attacks as AT, experiment as EX  # noqa: E402
from sna import sim as S  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
WORK = Path(sys.argv[1])
BUILD, R = "permitted_overlap", 20
VANT = ("baseline", "cred_processor")


def one(args):
    seed0, k, D = args
    with open(EX.model_path(WORK, BUILD), "rb") as f:
        m = pickle.load(f)
    cfg = EX.config_of(dict(R=float(R), decoys=float(EX.DECOYS), build=BUILD), D)
    run = S.simulate(cfg, EX.traffic_seed(R, k))
    seed = [seed0, R, k]
    # the permutation compute() draws, replayed to find the real devices it leaves on their own label
    cand = AT.candidates(run)
    devs = np.unique(np.r_[cand["dev"], run.subs["src"]])
    perm = devs[np.random.default_rng(seed).permutation(devs.size)]
    fixed_real = int(((perm == devs) & (devs < 100_000)).sum())
    recs = AT.compute(run, m, VANT, k, label_rng=np.random.default_rng(seed))
    return k, fixed_real, {v: (int(x["dev_v_correct"].sum()), int(x["dev_v_correct"].size), float(x["dev_v_rand"].sum()))
                           for v, x in recs.items()}


import pickle  # noqa: E402

if __name__ == "__main__":
    WORK.mkdir(parents=True, exist_ok=True)
    shutil.copy(HERE / "results" / "v2" / "calibration.json", WORK / "calibration.json")
    D = EX.calibrate(WORK)["D"]
    EX.ensure_models(WORK, BUILD)
    out, rng = {}, np.random.default_rng(1)
    for name, seed0, runs in (("committed seeds, runs 0-19", EX.SHUFFLE_SEED, 20),
                              ("fresh seeds, runs 0-99", EX.SHUFFLE_SEED + 1, 100)):
        with Pool() as p:
            res = p.map(one, [(seed0, k, D) for k in range(runs)])
        fx = np.array([r[1] for r in res])
        cell = dict(runs=runs, runs_fixing_a_real_device=int((fx > 0).sum()))
        for v in VANT:
            a = np.array([r[2][v] for r in res], float)
            acc, lo, hi = AN.cluster_boot(a[:, 0], a[:, 1], rng)
            row = dict(accuracy=acc, lo=lo, hi=hi, chance=a[:, 2].sum() / a[:, 1].sum(), n=int(a[:, 1].sum()))
            for lab, sel in (("no_real_fixed", fx == 0), ("real_fixed", fx > 0)):
                row[f"accuracy_{lab}"] = float(a[sel, 0].sum() / a[sel, 1].sum()) if sel.any() else None
            cell[v] = row
            print(name, v, {k: (round(100 * x, 3) if isinstance(x, float) else x) for k, x in row.items()}, flush=True)
        out[name] = cell
    p = HERE / "results" / "v2" / "checks" / "shuffle_check.json"
    p.write_text(json.dumps(out, indent=1))

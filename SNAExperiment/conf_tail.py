"""Read-only. Lists the most confident guesses of one vantage in one cell, and how often the
confident ones were right. Writes nothing. Run from the SNAExperiment folder:

    py conf_tail.py results\\C2 --cell main__R100_D100 --vantage content_server
    py conf_tail.py results\\C2 --cell main__R100_D100 --vantage combined
"""
import argparse
import sys
from pathlib import Path

import numpy as np

from sna import analyze as A
from sna import attacks as AT
from sna import runner as RU


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out", help="results folder that holds raw\\, for example results\\C2")
    ap.add_argument("--cell", default="main__R100_D100")
    ap.add_argument("--vantage", default="content_server")
    ap.add_argument("--top", type=int, default=25)
    a = ap.parse_args()

    recs = RU.load(Path(a.out), a.cell)
    if not recs:
        raw = Path(a.out) / "raw"
        names = sorted(p.name for p in raw.glob("*.pkl.gz")) if raw.exists() else []
        sys.exit(f"no records for {a.cell}. Files in {raw}: {names}")
    avail = list(recs[0]["vantages"])
    if a.vantage not in avail:
        sys.exit(f"no vantage {a.vantage}. Available: {avail}")

    t = A.stack(recs, a.vantage)
    conf, temps = A.calibrated_confidence(t)
    right = t["dev_v_correct"].astype(bool)
    n = conf.size
    print(f"{a.cell} / {a.vantage}: {len(recs)} runs, {n} guesses, temperatures {temps}")
    print(f"confidence percentiles: p50 {np.percentile(conf, 50):.4f}  p90 {np.percentile(conf, 90):.4f}  "
          f"p99 {np.percentile(conf, 99):.4f}  max {conf.max():.4f}")
    print()
    print("Guesses at or above each confidence level")
    print(f"{'level':>7} {'guesses':>9} {'share':>9} {'right':>7} {'hit rate':>9} {'mean conf':>10}")
    for lv in (0.9, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05):
        m = conf >= lv
        k = int(m.sum())
        if k:
            print(f"{lv:>7.2f} {k:>9d} {100 * k / n:>8.4f}% {int(right[m].sum()):>7d} "
                  f"{right[m].mean():>9.3f} {conf[m].mean():>10.3f}")
        else:
            print(f"{lv:>7.2f} {0:>9d}")
    print()
    # Does the confidence depend on which half of the runs a guess falls in? The temperature is
    # fitted on the other half, so each half can use a different one.
    half = (t["run"] % 2).astype(int)
    print("Confidence by half of the runs (temperature fitted on the other half)")
    for f in (0, 1):
        m = half == f
        print(f"  runs with parity {f}: temperature {temps[f]:.4f}, {int(m.sum())} guesses, max {conf[m].max():.4f}, "
              f"at least 0.5: {int((conf[m] >= 0.5).sum())}, at least 0.2: {int((conf[m] >= 0.2).sum())}")
    ti_all = A._fit_temperature(t, np.ones(n, dtype=bool))
    c1 = A._posterior(t, ti_all)
    print(f"  one temperature fitted on all guesses: {AT.T_GRID[ti_all]:.4f}, max {c1.max():.4f}, "
          f"at least 0.5: {int((c1 >= 0.5).sum())}, at least 0.2: {int((c1 >= 0.2).sum())}")
    print()
    # Belief in the truth: the posterior the attacker's model gives the TRUE device of each record,
    # whether or not it was the top pick. This is what an attacker holding one record of interest has.
    p_true = np.zeros(n)
    for fold in (0, 1):
        this = (t["run"] % 2) == fold
        ti = A._fit_temperature(t, ~this)
        T = AT.T_GRID[ti]
        off = t["dev_lse"][:, ti].astype(float)
        with np.errstate(over="ignore", invalid="ignore"):
            pt = np.exp((t["dev_s_true"].astype(float) - t["dev_top1"].astype(float)) / T - off)
        pt = np.where(np.isfinite(pt), np.clip(pt, 0, 1), 0.0)
        p_true[this] = pt[this]
    def belief_at(ti):
        T = AT.T_GRID[ti]
        off = t["dev_lse"][:, ti].astype(float)
        with np.errstate(over="ignore", invalid="ignore"):
            pt = np.exp((t["dev_s_true"].astype(float) - t["dev_top1"].astype(float)) / T - off)
        return np.where(np.isfinite(pt), np.clip(pt, 0, 1), 0.0)
    print("Belief in the true device under a fixed temperature (max; records at 0.2 or more; at 0.1 or more)")
    for label, ti in (("temperature 1.0", int(np.argmin(np.abs(AT.T_GRID - 1.0)))),
                      (f"temperature {AT.T_GRID[ti_all]:.3f} (fitted on all guesses)", ti_all)):
        b = belief_at(ti)
        print(f"  {label}: max {b.max():.4f}, at least 0.2: {int((b >= 0.2).sum())}, at least 0.1: {int((b >= 0.1).sum())}")
    print()
    print("Belief in the true device (one record of interest)")
    print(f"  mean {p_true.mean():.4f}  p50 {np.percentile(p_true, 50):.4f}  p90 {np.percentile(p_true, 90):.4f}  "
          f"p99 {np.percentile(p_true, 99):.4f}  p99.9 {np.percentile(p_true, 99.9):.4f}  max {p_true.max():.4f}")
    for lv in (0.5, 0.3, 0.2, 0.1):
        k = int((p_true >= lv).sum())
        print(f"  records where the true device got at least {lv:.1f}: {k} of {n} ({100 * k / n:.4f}%)")
    print()
    hit_idx = np.nonzero(right)[0]
    miss_idx = np.nonzero(~right)[0]
    rank = np.empty(n, dtype=np.int64)
    rank[np.argsort(-conf, kind="stable")] = np.arange(1, n + 1)
    if hit_idx.size:
        h = hit_idx[np.argmax(conf[hit_idx])]
        print(f"Most confident HIT : confidence {conf[h]:.4f}, rank {rank[h]} of {n}, "
              f"{int(t['dev_n_feas'][h])} candidates, run {int(t['run'][h])}, record {int(t['sub'][h])}")
    else:
        print("Most confident HIT : none")
    if miss_idx.size:
        m = miss_idx[np.argmax(conf[miss_idx])]
        print(f"Most confident MISS: confidence {conf[m]:.4f}, rank {rank[m]} of {n}, "
              f"{int(t['dev_n_feas'][m])} candidates, run {int(t['run'][m])}, record {int(t['sub'][m])}")
    print(f"Hits {hit_idx.size} of {n} ({100 * hit_idx.size / n:.2f}%). "
          f"Mean confidence of hits {conf[hit_idx].mean():.4f}, of misses {conf[miss_idx].mean():.4f}")
    print()
    print(f"The {a.top} most confident guesses")
    print(f"{'rank':>4} {'conf':>7} {'right':>6} {'candidates':>11} {'run':>5} {'record':>8} {'group':>6} {'half':>5}")
    order = np.argsort(-conf, kind="stable")[: a.top]
    for i, j in enumerate(order, 1):
        print(f"{i:>4d} {conf[j]:>7.4f} {str(bool(right[j])):>6} {int(t['dev_n_feas'][j]):>11d} "
              f"{int(t['run'][j]):>5d} {int(t['sub'][j]):>8d} {int(t['group'][j]):>6d} {int(half[j]):>5d}")


if __name__ == "__main__":
    main()

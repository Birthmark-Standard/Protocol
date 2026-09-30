"""Command line: python -m sna <command> [options]

  quick      smoke test of the whole pipeline in under a minute (results/quick; never reported)
  checks     pre-run checks, written to results/checks.json
  estimate   probe one run of every cell, then print seconds per run, successes per run, runs
             needed for a stable finding, and total time for a given run count
  run        run the sweep (resumable; rerun the same command to continue)
  analyze    metrics, tables and figures from the records on disk
  volume     table of L to devices and captures per day at the measured end-to-end delay

Every command is deterministic: results depend on the cell and run id only, never on the worker
count or the order runs finish in.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np

from . import attacks as AT
from . import cells as CE
from . import runner as RN


def _specs(which):
    return CE.grid(which)


def cmd_quick(a):
    t = time.time()
    out = Path(a.out or CE.RESULTS / "quick")
    D = CE.calibrate(out, runs=2)["D"]
    from . import params as P
    from .pools import Pools
    import pickle
    p = CE.model_path(out, False)
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        m = AT.build_models(P.Config(), Pools(), seed0=CE.MODEL_SEED0, min_samples=20_000)
        with open(p, "wb") as f:
            pickle.dump(m, f)
    specs = [s for s in CE.grid("all") if s["key"] in ("R24", "R24_T100")]
    for s in specs:
        s["key"] = s["key"] + "_quick"
    import dataclasses  # noqa: F401
    CE.write_cells(out, specs, D)
    tasks = [(str(out), dict(s, quick=True), k, D) for s in specs for k in range(2)
             if k not in RN.done_runs(out, s["key"])]
    RN.execute(tasks, _quick_worker, out, a.workers, label="quick")
    from . import analyze as AN
    cells = {s["key"]: s for s in specs}
    rows, _ = AN.analyze(out, cells, lambda k: RN.load(out, k))
    for r in rows:
        print(f"  {r['cell']:<16} {r['vantage']:<18} n={r['n']:5d} accuracy {r.get('accuracy', math.nan):.3f} "
              f"baseline {r.get('baseline', math.nan):.3f} 1/L {r['inv_L']:.3f}")
    print(f"quick: D = {D:.0f} s, {time.time() - t:.0f} s total")


def _quick_worker(out, spec, run_id, D):
    from . import params as P
    spec = dict(spec)
    import dataclasses
    cfg = CE.config_of(spec, D)
    cfg = dataclasses.replace(cfg, measure_s=1800.0)
    from . import sim as S
    from .pools import Pools
    import pickle
    with open(CE.model_path(out, False), "rb") as f:
        m = pickle.load(f)
    t = time.time()
    run = S.simulate(cfg, CE.traffic_seed(spec["R"], run_id), Pools())
    recs = AT.compute(run, Pools(), m)
    return [(spec["key"], dict(run=run_id, seconds=time.time() - t, sim_seconds=0.0, vantages=recs,
                               n_real=int((~run.subs["decoy"]).sum()), n_decoy=int(run.subs["decoy"].sum())))]


def cmd_checks(a):
    from . import checks
    checks.run_checks(Path(a.out or CE.RESULTS), runs=a.check_runs)


def cmd_estimate(a):
    out = Path(a.out or CE.RESULTS)
    specs = _specs(a.cells)
    costs = CE.probe_costs(out, specs, probe_runs=a.probe_runs, workers=a.workers)
    nw = RN.resolve_workers(a.workers)
    total = 0.0
    print(f"\n{'cell':<14}{'s/run':>8}{'real':>7}{'decoy':>8}  runs needed for {AN_MIN()} successes and failures per vantage")
    for spec in specs:
        c = costs.get(spec["key"])
        if not c:
            continue
        need = {}
        for v in AT.VANTAGES:
            s, f = c["successes_per_run"][v], c["failures_per_run"][v]
            need[v] = max(CE.runs_needed(s, AN_MIN()), CE.runs_needed(f, AN_MIN()))
        total += c["sec_per_run"] * a.runs
        nd = " ".join(f"{_short(v)}={('inf' if math.isinf(n) else n)}" for v, n in need.items())
        print(f"{spec['key']:<14}{c['sec_per_run']:8.1f}{c['n_real']:7.0f}{c['n_decoy']:8.0f}  {nd}")
    print(f"\n{a.runs} runs per cell: {total / 3600:.1f} core-hours, about {total / 3600 / nw:.1f} hours on {nw} workers")


def AN_MIN():
    from . import analyze as AN
    return AN.MIN_EACH


def _short(v):
    return dict(baseline="Base", first_hop_cred="A", first_hop_content="D", cred_processor="C",
                content_server="F", validator="V", gatekeeper="GK")[v]


def cmd_run(a):
    CE.run_cells(Path(a.out or CE.RESULTS), _specs(a.cells), a.runs, a.workers)


def cmd_analyze(a):
    from . import report
    report.build(Path(a.out or CE.RESULTS))


def cmd_volume(a):
    from . import report
    print(report.volume_table(CE.calibrate(Path(a.out or CE.RESULTS))["D"]))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m sna", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["quick", "checks", "estimate", "run", "analyze", "volume"])
    ap.add_argument("--out", help="results directory (default: results/)")
    ap.add_argument("--workers", default="auto", help="worker processes (default: all cores)")
    ap.add_argument("--runs", type=int, default=100, help="runs per cell (run, estimate)")
    ap.add_argument("--cells", default="all", choices=["all", "nodecoy", "decoy", "control"])
    ap.add_argument("--probe-runs", type=int, default=1)
    ap.add_argument("--check-runs", type=int, default=12)
    a = ap.parse_args(argv)
    dict(quick=cmd_quick, checks=cmd_checks, estimate=cmd_estimate, run=cmd_run, analyze=cmd_analyze,
         volume=cmd_volume)[a.command](a)

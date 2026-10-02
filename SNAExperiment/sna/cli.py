"""Command line: python -m sna <command> [options]

  quick      smoke test of the whole pipeline in under a minute (results/quick; never reported)
  checks     pre-run checks, written to results/checks.json
  estimate   probe one run of every cell, then print seconds per run, successes per run, runs
             needed for a stable finding, and total time for a given run count
  run        run the sweep (resumable; rerun the same command to continue)
  analyze    metrics, tables and figures from the records on disk
  volume     table of L to devices and captures per day at the measured end-to-end delay
  latency    capture-to-finalisation time under each build, by stage (results/latency.json)
  bundles    registry-level bundle sizes over the sweep's runs (results/registry_bundles_<build>.json)
  gatekeeper each gatekeeper's own load and bundle sizes by decoy target and window
             (results/gatekeeper_occupancy.json)
  diag-cs    exploratory: the content server's evidence split into record time and content arrival
             (results/diag_content_server.json)
  sequence   every run, analysis and latency step of one plan section, in order (e.g. sequence 6h)

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


def _specs(which, build=None):
    return CE.grid(which, build or CE.DEFAULT_BUILD)


def cmd_quick(a):
    t = time.time()
    out = Path(a.out or CE.RESULTS / "quick")
    D = CE.calibrate(out, runs=2)["D"]
    from . import params as P
    from .pools import Pools
    import pickle
    for bundle in (False, True):
        p = CE.model_path(out, False, bundle)
        if not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            m = AT.build_models(P.Config(bundle_s=P.BUNDLE_S if bundle else 0.0, **CE.build_kw(CE.DEFAULT_BUILD)),
                                Pools(), seed0=CE.MODEL_SEED0, min_samples=40_000)
            with open(p, "wb") as f:
                pickle.dump(m, f)
    specs = [s for s in CE.grid("all") if s["key"] in ("R15_D40", "R15_D40_B")]
    for s in specs:
        s["key"] = s["key"] + "_quick"
    names = {s["key"]: CE.rec_name(s) for s in specs}
    import dataclasses  # noqa: F401
    CE.write_cells(out, specs, D)
    tasks = [(str(out), dict(s, quick=True), k, D) for s in specs for k in range(2)
             if k not in RN.done_runs(out, names[s["key"]])]
    RN.execute(tasks, _quick_worker, out, a.workers, label="quick")
    from . import analyze as AN
    cells = {s["key"]: s for s in specs}
    rows, _, _ = AN.analyze(out, cells, lambda k: RN.load(out, names[k]))
    for r in rows:
        print(f"  {r['cell']:<16} {r['vantage']:<18} n={r['n']:5d} device {r.get('dev_accuracy', math.nan):.3f} "
              f"(baseline {r.get('dev_baseline', math.nan):.3f}, random {r.get('dev_random', math.nan):.3f})  "
              f"submission {r.get('sub_accuracy', math.nan):.3f} (1/L {r['inv_L']:.3f})")
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
    with open(CE.model_path(out, False, spec.get("bundle", False)), "rb") as f:
        m = pickle.load(f)
    t = time.time()
    run = S.simulate(cfg, CE.traffic_seed(spec["R"], run_id), Pools())
    recs = AT.compute(run, Pools(), m, run_id=run_id)
    return [(CE.rec_name(spec), dict(run=run_id, seconds=time.time() - t, sim_seconds=0.0, vantages=recs,
                               n_real=int((~run.subs["decoy"]).sum()), n_decoy=int(run.subs["decoy"].sum())))]


def cmd_checks(a):
    from . import checks
    checks.run_checks(Path(a.out or CE.RESULTS), runs=a.check_runs)


def cmd_estimate(a):
    out = Path(a.out or CE.RESULTS)
    specs = _specs(a.cells, a.build)
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
    specs = _specs(a.cells, a.build)
    if a.allrecords:
        specs = CE.allrecords_specs(specs)
    CE.run_cells(Path(a.out or CE.RESULTS), specs, a.runs, a.workers)


def cmd_analyze(a):
    from . import report
    report.build(Path(a.out or CE.RESULTS), a.build)


def cmd_latency(a):
    CE.latency(Path(a.out or CE.RESULTS))


def cmd_bundles(a):
    CE.registry_bundles(Path(a.out or CE.RESULTS), runs=a.runs, build=a.build, workers=a.workers,
                        which="extra" if a.cells == "extra" else "bundle")


def cmd_gatekeeper(a):
    CE.gatekeeper_occupancy(Path(a.out or CE.RESULTS), workers=a.workers)


def cmd_diag_cs(a):
    from . import diagnostics
    diagnostics.content_server_sources(Path(a.out or CE.RESULTS), workers=a.workers)


def cmd_sequence(a):
    """Every step of one plan section, in order: each build's runs, then each build's analysis, then
    the latency of every build. Resumable: rerunning the same command skips finished runs."""
    from . import report
    seq = CE.SEQUENCES[a.name]
    out = Path(a.out or CE.ROOT / seq["out"])
    out.mkdir(parents=True, exist_ok=True)
    cal = out / "calibration.json"
    if not cal.exists() and (CE.RESULTS / "calibration.json").exists():
        cal.write_text((CE.RESULTS / "calibration.json").read_text())
    t0 = time.time()
    steps = [(f"run {b}", lambda b=b: CE.run_cells(out, CE.grid(seq["cells"], b), seq["runs"], a.workers))
             for b in seq["builds"]]
    steps += [(f"analyze {b}", lambda b=b: report.build(out, b)) for b in seq["builds"]]
    steps += [("latency", lambda: CE.latency(out, runs=seq.get("latency_runs", 20), builds=seq["builds"]))]
    for i, (name, fn) in enumerate(steps, 1):
        print(f"\n=== step {i} of {len(steps)}: {name} ({(time.time() - t0) / 60:.1f} min elapsed) ===", flush=True)
        fn()
    print(f"\nsequence {a.name} done in {(time.time() - t0) / 60:.1f} min; results in {out}", flush=True)


def cmd_volume(a):
    from . import report
    print(report.volume_table(CE.calibrate(Path(a.out or CE.RESULTS))["D"]))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m sna", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["quick", "checks", "estimate", "run", "analyze", "volume", "latency", "bundles", "gatekeeper", "diag-cs", "sequence"])
    ap.add_argument("--out", help="results directory (default: results/)")
    ap.add_argument("--workers", default="auto", help="worker processes (default: all cores)")
    ap.add_argument("--runs", type=int, default=100, help="runs per cell (run, estimate)")
    ap.add_argument("--cells", default="all", choices=["all", "bundle", "nobundle", "control", "extra", "settled"])
    ap.add_argument("--probe-runs", type=int, default=1)
    ap.add_argument("--check-runs", type=int, default=12)
    ap.add_argument("name", nargs="?", default="6h", help="sequence name (sequence command only)")
    ap.add_argument("--build", default=CE.DEFAULT_BUILD, choices=list(CE.BUILDS),
                    help="protocol build (default: %(default)s): push; twopoint adds the two-point gatekeeper hold; "
                         "regbundle adds registry-level pooled bundling")
    ap.add_argument("--allrecords", action="store_true",
                    help="re-score the first hops and credential processor on every record (plan section 6a)")
    a = ap.parse_args(argv)
    dict(quick=cmd_quick, checks=cmd_checks, estimate=cmd_estimate, run=cmd_run, analyze=cmd_analyze, latency=cmd_latency, bundles=cmd_bundles, gatekeeper=cmd_gatekeeper, **{"diag-cs": cmd_diag_cs}, sequence=cmd_sequence,
         volume=cmd_volume)[a.command](a)

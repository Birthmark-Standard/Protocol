"""Command line: python -m sna <command> [options]

  reproduce  the whole experiment in order: calibration, hold timing, every build's runs and
             analysis, latency, F/I pair timing, then TABLES.md and the figures. Resumable:
             rerunning the same command skips finished runs.
  run        one build's runs (--build), resumable
  analyze    one build's summary and tables from the records on disk (--build)
  tables     every build's CSV and tables, TABLES.md and the figures, from the summaries on disk
  latency    capture-to-finalization time under every build (results/latency.json)
  pairs      how often a record's two registry submissions leave together (results/pair_gaps.json)
  timing     every stage's simulated hold, and departure bundle sizes (results/timing_check.json)

Every command is deterministic: results depend on the cell and run id only, never on the worker
count or the order runs finish in.
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path

from . import experiment as EX
from . import report


def cmd_reproduce(a):
    out = Path(a.out or EX.RESULTS)
    out.mkdir(parents=True, exist_ok=True)
    side = min(a.runs, 20)                         # latency and pair timing: 20 runs per cell
    print(f"calibration under {EX.EXPERIMENT}: D = {EX.calibrate(out)['D']:.1f} s", flush=True)
    steps = [("hold timing", lambda: EX.timing_check(out, runs=min(a.runs, 10), workers=a.workers))]
    steps += [(f"run {b}", lambda b=b: EX.run_cells(out, EX.grid(b), a.runs, a.workers)) for b in EX.BUILDS]
    steps += [(f"analyze {b}", lambda b=b: report.summarize(out, b)) for b in EX.BUILDS]
    steps += [("latency", lambda: EX.latency(out, runs=side)),
              ("F/I pair timing", lambda: EX.pair_gaps(out, runs=side, workers=a.workers)),
              ("tables and figures", lambda: report.write_tables(out))]
    t0 = time.time()
    for i, (name, fn) in enumerate(steps, 1):
        print(f"\n=== step {i} of {len(steps)}: {name} ({(time.time() - t0) / 60:.1f} min elapsed) ===", flush=True)
        fn()
    print(f"\n{EX.EXPERIMENT} done in {(time.time() - t0) / 60:.1f} min; results in {out}", flush=True)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m sna", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["reproduce", "run", "analyze", "tables", "latency", "pairs", "timing"])
    ap.add_argument("--out", help="results directory (default: results/)")
    ap.add_argument("--workers", default="auto", help="worker processes (default: all cores)")
    ap.add_argument("--runs", type=int, default=EX.RUNS, help="runs per cell (default: %(default)s)")
    ap.add_argument("--build", default=EX.BASELINE, choices=list(EX.BUILDS), help="build (default: %(default)s)")
    a = ap.parse_args(argv)
    out = Path(a.out or EX.RESULTS)
    dict(reproduce=lambda: cmd_reproduce(a),
         run=lambda: EX.run_cells(out, EX.grid(a.build), a.runs, a.workers),
         analyze=lambda: report.summarize(out, a.build),
         tables=lambda: report.tables_from_summaries(out),
         latency=lambda: EX.latency(out, runs=min(a.runs, 20)),
         pairs=lambda: EX.pair_gaps(out, runs=min(a.runs, 20), workers=a.workers),
         timing=lambda: EX.timing_check(out, runs=min(a.runs, 10), workers=a.workers))[a.command]()

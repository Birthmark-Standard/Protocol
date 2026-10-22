"""Command line: python -m sna <command> [options]

  run        one build's runs (--build), resumable
  analyze    one build's summary and tables from the records on disk (--build)
  tables     every build's CSV and tables, TABLES.md and the figures, from the summaries on disk

Every command is deterministic: results depend on the cell and run id only, never on the worker
count or the order runs finish in.
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path

from . import experiment as EX
from . import report


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m sna", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["run", "analyze"])
    ap.add_argument("--out", help="results directory (default: results/)")
    ap.add_argument("--workers", default="auto", help="worker processes (default: all cores)")
    ap.add_argument("--runs", type=int, default=None, help=f"runs per cell (default: {EX.RUNS})")
    ap.add_argument("--build", default=EX.BASELINE, choices=list(EX.ALL_BUILDS), help="build (default: %(default)s)")
    a = ap.parse_args(argv)
    paths_runs = a.runs or 300
    a.runs = a.runs or EX.RUNS
    out = Path(a.out or EX.RESULTS)
    dict(run=lambda: EX.run_cells(out, EX.grid(a.build), a.runs, a.workers),
         analyze=lambda: report.summarize(out, a.build))[a.command]()

"""Command-line interface.

    python -m harness regress  [--out DIR] [--workers auto]
"""
from __future__ import annotations

import argparse
from pathlib import Path

from . import ROOT


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m harness")
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("regress", help="reproduce the published Round 1 and Round 3 results")
    g.add_argument("--out", default=str(ROOT / "results" / "regression"))
    g.add_argument("--workers", default="auto")
    g.add_argument("--only", nargs="*", help="subset of checks")
    a = ap.parse_args(argv)
    if a.cmd == "regress":
        from . import regress
        res = regress.run(Path(a.out), a.workers, a.only)
        raise SystemExit(0 if res["passed"] else 1)

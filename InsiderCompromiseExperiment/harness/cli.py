"""Command-line interface. Windows PowerShell, macOS and Linux:

    python -m harness quick                                   # smoke test, under 2 minutes
    python -m harness run --scenario N A C D F V GK --round 3 --L 4 8 --runs 20 --out results/x
    python -m harness analyze --in results/x
    python -m harness estimate --scenario N A C D F V GK --round 3 --L 4 40 200 1000 --runs 20
    python -m harness regress                                 # reproduce the published rounds
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path

from . import ROOT

SCEN = ("N", "A", "C", "D", "F", "V", "GK")


def _specs(a):
    from .tool import cell_spec
    specs = []
    for rnd in a.round:
        for L in a.L:
            for share in (a.share or [0.0]):
                specs.append(cell_spec(rnd, L, a.scenario, a.variant, share, a.nodes, a.window, a.seed))
    return specs


def _plan_args(p, runs_default=20):
    p.add_argument("--scenario", nargs="+", default=list(SCEN), choices=SCEN)
    p.add_argument("--round", nargs="+", type=int, default=[3], choices=[1, 2, 3])
    p.add_argument("--L", nargs="+", type=float, default=[4])
    p.add_argument("--runs", type=int, default=runs_default)
    p.add_argument("--workers", default="auto")
    p.add_argument("--seed", type=int, default=1, help="base seed")
    p.add_argument("--variant", default="", choices=["", "positive"], help="positive = lottery and gatekeeper hold off")
    p.add_argument("--share", nargs="*", type=float, help="validator 0's share of devices (V scenario)")
    p.add_argument("--nodes", type=int, default=20, help="pool size")
    p.add_argument("--window", type=float, default=180.0, help="scored window, minutes")
    p.add_argument("--no-crypto", action="store_true", help="use the measured size tables; no crypto packages needed")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m harness")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="simulate and score; resumable")
    _plan_args(r)
    r.add_argument("--out", default=str(ROOT / "results" / "extension"))
    e = sub.add_parser("estimate", help="expected runtime for a plan, from measured per-run costs")
    _plan_args(e)
    e.add_argument("--costs", help="costs.json from an earlier run (default: bundled measurements)")
    z = sub.add_parser("analyze", help="metrics from persisted decisions (never re-simulates)")
    z.add_argument("--in", dest="inp", default=str(ROOT / "results" / "extension"))
    z.add_argument("--publish", action="store_true", help="also write results/ tables and figures")
    q = sub.add_parser("quick", help="smoke test, under 2 minutes")
    q.add_argument("--out", default=None)
    q.add_argument("--workers", default="auto")
    g = sub.add_parser("regress", help="reproduce the published Round 1 and Round 3 results")
    g.add_argument("--out", default=str(ROOT / "results" / "regression"))
    g.add_argument("--workers", default="auto")
    g.add_argument("--only", nargs="*", help="subset of checks")
    v = sub.add_parser("equivalence", help="the tool's F attack vs the original, on the original runs")
    v.add_argument("--out", default=str(ROOT / "results" / "equivalence"))
    v.add_argument("--workers", default="auto")
    a = ap.parse_args(argv)
    if getattr(a, "no_crypto", False):
        import os
        os.environ["BIRTHMARK_NO_CRYPTO"] = "1"      # inherited by worker processes

    if a.cmd == "run":
        from .tool import run_cells
        run_cells(Path(a.out), _specs(a), a.runs, a.workers)
    elif a.cmd == "estimate":
        from .tool import estimate
        estimate(_specs(a), a.runs, a.workers, a.costs)
    elif a.cmd == "analyze":
        from .report import analyze_dir
        analyze_dir(Path(a.inp), publish=a.publish)
    elif a.cmd == "quick":
        import tempfile
        from .report import analyze_dir
        from .tool import cell_spec, run_cells
        t = time.time()
        out = Path(a.out) if a.out else Path(tempfile.mkdtemp(prefix="harness_quick_"))
        spec = cell_spec(3, 4, SCEN, window=40.0)
        run_cells(out, [spec], 4, a.workers)
        analyze_dir(out, publish=False)
        print(f"quick: done in {time.time() - t:.0f} s; output in {out}")
    elif a.cmd == "equivalence":
        from . import equivalence
        res = equivalence.run(Path(a.out), a.workers)
        raise SystemExit(0 if res["passed"] else 1)
    elif a.cmd == "regress":
        from . import regress
        res = regress.run(Path(a.out), a.workers, a.only)
        raise SystemExit(0 if res["passed"] else 1)

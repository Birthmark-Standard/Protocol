"""Insider experiment, extended: null case, roles A, C, D, F, V and a gatekeeper, adversary-confidence
analysis, and scale. Command-line tool: python -m harness --help

Builds on GPAExperiment/birthmark_l3 (imported, not copied) and on insider/ (Rounds 2 and 3)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GPA = ROOT.parent / "GPAExperiment"
for p in (GPA, ROOT):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

"""Compare the R = 1 cell of a new run with the R = 1 cell of an earlier run, decision by decision.

    python compare_r1.py results/C1 --new results/C2

OLD_RESULTS and --new are results directories (each holding raw/ and run_info.json) or their raw/ folders.
Every configuration's R = 1 file is read from both sides, run by run, for every vantage the earlier run
scored. A vantage only the new run has (such as observer_typed) is listed and not compared.

A decision is one row of a vantage's table: one record, scored by one vantage (and, for a node vantage,
one compromised node). The tables do not store which device was named. They store the decision's outcome
at the device and the submission level, its top score, the true device's score, its feasible counts, its
calibrated-confidence terms, the outcome under the shuffled labels, and the observer's outcome on the same
record. A decision counts as differing when any of these differs. The count of decisions whose
device-level outcome differs is printed beside it.

Prints the decisions compared, the decisions that differ, and the Python, numpy, scipy and platform of
both sides where run_info.json records them. Exits 0 when every run is on both sides and nothing differs,
and 1 otherwise. Needs numpy and this repository's own modules only.
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path

import numpy as np

from sna import experiment as EX
from sna import runner as RN

R = 1


def results_dir(p):
    """A results directory, given it or its raw/ folder."""
    p = Path(p)
    return p.parent if p.name == "raw" else p


def versions(d):
    """The versions run_info.json records, or None for a run that did not record them."""
    p = Path(d) / "run_info.json"
    if not p.exists():
        return None
    info = json.loads(p.read_text())
    return dict(versions=info.get("versions"), resumed_under=info.get("versions_on_resume", []))


def _same(x, y):
    """Element-wise equality of two columns, rows on the first axis, NaN equal to NaN."""
    if x.dtype.kind == "f" or y.dtype.kind == "f":
        eq = (x == y) | (np.isnan(x.astype(float)) & np.isnan(y.astype(float)))
    else:
        eq = x == y
    return eq.reshape(eq.shape[0], -1).all(1)


def compare(old, new):
    """Every R = 1 decision of every configuration and every vantage the old run scored. Returns the counts
    and a list of what differs."""
    old, new = results_dir(old), results_dir(new)
    out = dict(compared=0, differ=0, dev_outcome_differ=0, incomplete=False, notes=[], tables={})
    for name in EX.CONFIGS:
        f = EX.rec_name(name, R)
        a = {r["run"]: r for r in RN.load(old, f)}
        b = {r["run"]: r for r in RN.load(new, f)}
        if not a and not b:
            continue
        runs = sorted(set(a) & set(b))
        if set(a) ^ set(b):
            out["incomplete"] = True
        if set(a) - set(b):
            out["notes"].append(f"{name}: {len(set(a) - set(b))} runs only in the earlier run, not compared")
        if set(b) - set(a):
            out["notes"].append(f"{name}: {len(set(b) - set(a))} runs only in the new run, not compared")
        for k in runs:
            va, vb = a[k]["vantages"], b[k]["vantages"]
            if k == runs[0]:
                for v in sorted(set(vb) - set(va)):
                    out["notes"].append(f"{name}: vantage {v} only in the new run, not compared")
            for v in sorted(va):
                ta = va[v]
                n = int(ta["sub"].shape[0])
                key = (name, v)
                t = out["tables"].setdefault(key, dict(compared=0, differ=0, dev_outcome_differ=0, columns={}))
                t["compared"] += n
                out["compared"] += n
                tb = vb.get(v)
                if tb is None or int(tb["sub"].shape[0]) != n or any(c not in tb for c in ta):
                    t["differ"] += n
                    t["dev_outcome_differ"] += n
                    out["differ"] += n
                    out["dev_outcome_differ"] += n
                    out["notes"].append(f"{name} run {k}: vantage {v} has a different shape or set of columns in the new run")
                    continue
                bad = np.zeros(n, bool)
                for c in ta:
                    m = ~_same(np.asarray(ta[c]), np.asarray(tb[c]))
                    if m.any():
                        t["columns"][c] = t["columns"].get(c, 0) + int(m.sum())
                    bad |= m
                dev = ~_same(np.asarray(ta["dev_v_correct"]), np.asarray(tb["dev_v_correct"]))
                t["differ"] += int(bad.sum())
                t["dev_outcome_differ"] += int(dev.sum())
                out["differ"] += int(bad.sum())
                out["dev_outcome_differ"] += int(dev.sum())
            for part in ("stats", "shuffle_test"):
                if part in a[k] and repr(a[k][part]) != repr(b[k].get(part)):
                    out["incomplete"] = True
                    out["notes"].append(f"{name} run {k}: {part} differs")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 epilog="Example: " + __doc__.split("\n\n")[1].strip())
    ap.add_argument("old", help="the earlier run's results directory, or its raw/ folder")
    ap.add_argument("--new", default="results/C2", help="the new run's results directory (default: %(default)s)")
    a = ap.parse_args(argv)
    for side, d in (("earlier run", a.old), ("new run", a.new)):
        if not (results_dir(d) / "raw").is_dir():
            raise SystemExit(f"{side}: no raw/ folder under {results_dir(d)}")
    res = compare(a.old, a.new)
    print(f"R = {R}: decisions compared {res['compared']:,}; decisions that differ {res['differ']:,} "
          f"(device-level outcome differs: {res['dev_outcome_differ']:,})")
    for (name, v), t in sorted(res["tables"].items()):
        cols = ", ".join(f"{c} {n:,}" for c, n in sorted(t["columns"].items()))
        print(f"  {name:20s} {v:20s} compared {t['compared']:>10,}  differ {t['differ']:>8,}" + (f"  ({cols})" if cols else ""))
    for note in res["notes"]:
        print("  note:", note)
    for side, d in (("earlier run", a.old), ("new run", a.new)):
        v = versions(results_dir(d))
        if v is None:
            print(f"{side}: no run_info.json")
        else:
            print(f"{side}: versions {v['versions'] or 'not recorded'}" + (f"; resumed under {v['resumed_under']}" if v["resumed_under"] else ""))
    try:
        import scipy
        sv = scipy.__version__
    except ImportError:
        sv = "not installed"
    print(f"this comparison ran on: python {platform.python_version()}, numpy {np.__version__}, scipy {sv}, {platform.platform()}")
    if res["incomplete"]:
        print("the comparison is incomplete or a run's statistics differ: see the notes above")
    return 0 if res["differ"] == 0 and not res["incomplete"] else 1


if __name__ == "__main__":
    sys.exit(main())

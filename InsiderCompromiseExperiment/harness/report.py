"""analyze: tables (and, with --publish, figures) from a run directory. Never re-simulates."""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

from . import ROOT
from . import analyze as AN
from . import runner as RN

# record -> (scenario, variant, what the adversary's label means, paired N(a) record)
RECORDS = {
    "N@A": ("N", "paired with A", "none (wire only)", None),
    "N@C": ("N", "paired with C", "none (wire only)", None),
    "N@D": ("N", "paired with D", "none (wire only)", None),
    "N@V": ("N", "paired with V", "none (wire only)", None),
    "N.F": ("N", "paired with F", "none (wire only)", None),
    "Nb.seq": ("N", "published sequencing", "none (wire only)", None),
    "A": ("A", "", "network address (device id)", "N@A"),
    "D": ("D", "", "network address (device id)", "N@D"),
    "C": ("C", "", "transaction (manufacturer via key_ref)", "N@C"),
    "V.timing": ("V", "timing", "device identity", "N@V"),
    "V.full": ("V", "full", "device identity", "N@V"),
    "GK.timing": ("GK", "timing", "transaction (manufacturer known)", "Nb.seq"),
    "GK.full": ("GK", "full", "transaction (manufacturer known)", "Nb.seq"),
    "F.timing": ("F", "timing", "content (ContentHash)", "N.F"),
    "F.full": ("F", "full", "content (ContentHash)", "N.F"),
    "F.legs": ("F", "legs", "content (ContentHash)", "N.F"),
}
PRIMARY = {"N": "Nb.seq", "A": "A", "C": "C", "D": "D", "F": "F.full", "V": "V.full", "GK": "GK.full"}

SUMMARY_COLS = ["cell", "round", "L", "variant", "share", "nodes", "window_min", "record", "scenario", "scenario_variant",
                "label", "primary", "runs", "n", "n_correct", "inv_L", "accuracy", "ci_lo", "ci_hi", "ci_adj_lo",
                "ci_adj_hi", "lift", "lift_lo", "lift_hi", "top3", "top3_lo", "top3_hi", "accuracy_per_decision",
                "random_assignment", "signal_accuracy", "auc_posterior", "auc_posterior_lo", "auc_posterior_hi",
                "auc_gap", "auc_gap_lo", "auc_gap_hi", "auc_stable", "runs_needed_for_auc", "signal_auc", "signal",
                "ece", "posterior_yield_coverage_at_p50", "posterior_best_precision_cov1",
                "minus_N_a", "minus_N_a_lo", "minus_N_a_hi", "minus_Nb_seq", "minus_Nb_seq_lo", "minus_Nb_seq_hi",
                "minus_Nb_main", "minus_Nb_main_lo", "minus_Nb_main_hi",
                "shuffled_accuracy", "shuffled_lo", "shuffled_hi", "shuffled_auc", "shuffled_auc_lo", "shuffled_auc_hi"]


def _records_in(out, key):
    names = {}
    for p in (Path(out) / "raw").glob(f"{key}__*.pkl.gz"):
        name = p.name[len(key) + 2:-7]
        if name != "done":
            names[name] = p
    return names


def analyze_dir(out: Path, publish=False):
    out = Path(out)
    cells = json.loads((out / "cells.json").read_text())
    rng = np.random.default_rng(0)
    rows, conf_rows, pc_rows, rel_rows, curves_all = [], [], [], [], {}
    for key, spec in cells.items():
        done = {r["run"] for r in RN.load(out, f"{key}__done")}
        if not done:
            continue
        recs = {n: [r for r in RN.load(out, f"{key}__{n}") if r["run"] in done] for n in _records_in(out, key)}
        for name, rr in sorted(recs.items()):
            if not rr or name == "Nb.main":
                continue
            m, curves = AN.metrics(rr, spec["L"], rng, with_curves=True)
            scen, var, label, npair = RECORDS[name]
            row = dict(cell=key, round=spec["round"], L=spec["L"], variant=spec["variant"], share=spec["share"],
                       nodes=spec["nodes"], window_min=spec["window"], record=name, scenario=scen,
                       scenario_variant=var, label=label, primary=PRIMARY.get(scen) == name)
            row.update(m)
            if npair and recs.get(npair):
                d = AN.paired_difference(rr, recs[npair], rng)
                row.update(minus_N_a=d["diff"], minus_N_a_lo=d["lo"], minus_N_a_hi=d["hi"])
            if scen != "N" and recs.get("Nb.seq"):
                d = AN.paired_difference(rr, recs["Nb.seq"], rng)
                row.update(minus_Nb_seq=d["diff"], minus_Nb_seq_lo=d["lo"], minus_Nb_seq_hi=d["hi"])
            if scen != "N" and recs.get("Nb.main"):
                d = AN.paired_difference(rr, recs["Nb.main"], rng)
                row.update(minus_Nb_main=d["diff"], minus_Nb_main_lo=d["lo"], minus_Nb_main_hi=d["hi"])
            rows.append(row)
            curves_all[(key, name)] = curves
            for cname in ("posterior", "gap"):
                for pc in curves[cname]["precision_coverage"]:
                    pc_rows.append(dict(cell=key, record=name, confidence=cname, **pc))
            for rel in curves["reliability"]:
                rel_rows.append(dict(cell=key, record=name, **rel))
        if recs.get("Nb.main"):
            t = AN.stack(recs["Nb.main"])
            num, den = AN.per_run(t["correct"].astype(bool), t["run"])
            acc, lo, hi = AN.cluster_boot(num, den, rng)
            rows.append(dict(cell=key, round=spec["round"], L=spec["L"], variant=spec["variant"], share=spec["share"],
                             nodes=spec["nodes"], window_min=spec["window"], record="Nb.main", scenario="N",
                             scenario_variant="published main attack", label="none (wire only)", primary=False,
                             runs=len(recs["Nb.main"]), n=int(den.sum()), n_correct=int(num.sum()), inv_L=1 / spec["L"],
                             accuracy=acc, ci_lo=lo, ci_hi=hi, lift=acc * spec["L"]))
        if recs.get("V.full") and recs.get("C"):
            d = AN.paired_difference(recs["V.full"], recs["C"], rng)
            for r in rows:
                if r["cell"] == key and r["record"] == "V.full":
                    r.update(V_minus_C=d["diff"], V_minus_C_lo=d["lo"], V_minus_C_hi=d["hi"])
    _write(out, rows, pc_rows, rel_rows)
    _print(rows)
    if publish:
        from . import figures
        figures.make_all(out, rows, curves_all)
    return rows


def _clean(v):
    if isinstance(v, (np.floating, float)):
        return None if not math.isfinite(float(v)) else round(float(v), 6)
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, dict):
        return json.dumps(v)
    return v


def _write(out, rows, pc_rows, rel_rows):
    cols = SUMMARY_COLS + [c for c in ("V_minus_C", "V_minus_C_lo", "V_minus_C_hi", "temperature")]
    with open(out / "summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: _clean(r.get(k)) for k in cols})
    conf_cols = ["cell", "record", "n", "n_correct", "auc_posterior", "auc_posterior_lo", "auc_posterior_hi",
                 "auc_gap", "auc_gap_lo", "auc_gap_hi", "auc_stable", "runs_needed_for_auc", "ece", "temperature"]
    conf_cols += [k for k in rows[0] if k.startswith(("posterior_", "gap_"))] if rows else []
    with open(out / "confidence_metrics.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=conf_cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            if "auc_posterior" in r:
                w.writerow({k: _clean(r.get(k)) for k in conf_cols})
    for name, data in (("confidence_precision_coverage.csv", pc_rows), ("confidence_reliability.csv", rel_rows)):
        if data:
            with open(out / name, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(data[0].keys()))
                w.writeheader()
                for r in data:
                    w.writerow({k: _clean(v) for k, v in r.items()})
    (out / "summary.json").write_text(json.dumps([{k: _clean(v) for k, v in r.items()} for r in rows], indent=1))


def _print(rows):
    print(f"{'cell':<18}{'record':<11}{'n':>8}{'acc':>8}{'95% CI':>17}{'1/L':>7}{'lift':>6}{'AUC':>7}{'-N(a)':>8}  signal")
    for r in rows:
        ci = f"[{r['ci_lo']:.4f},{r['ci_hi']:.4f}]" if "ci_lo" in r else ""
        auc = f"{r['auc_posterior']:.3f}" if r.get("auc_stable") else "  -  "
        dn = f"{r['minus_N_a']:+.4f}" if "minus_N_a" in r else ""
        print(f"{r['cell']:<18}{r['record']:<11}{r['n']:>8}{r['accuracy']:>8.4f}{ci:>17}{1 / r['L']:>7.4f}"
              f"{r['lift']:>6.2f}{auc:>7}{dn:>8}  {'SIGNAL' if r.get('signal') else ''}")

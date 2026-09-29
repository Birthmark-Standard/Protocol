"""Publish the extension's results into results/: the extended summary.csv, confidence tables,
figures, the paper table and the volume table. Reads results/extension/summary.json (written by
`python -m harness analyze`).

    python -m harness analyze --in results/extension --publish
    python -m harness publish
"""
from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

from . import ROOT

EXT = ROOT / "results" / "extension"
RES = ROOT / "results"
L_GRID = (4, 8, 24, 40, 200, 1000)
ROLE_ROWS = [  # role, record, what it knows exactly, label
    ("N", "Nb.seq", "sizes and timing on every link; no keys", "none"),
    ("A", "A", "credential packet's source address and arrival; its own hold and forward times", "network address"),
    ("D", "D", "one content copy's source address and arrival; its own hold and forward times", "network address"),
    ("C", "C", "PacketHash, key_ref, its own GK-leg sends and CV-2 arrival", "transaction (manufacturer)"),
    ("F", "F.full", "ContentHash, content arrival, its quorum-detection tick, board postings", "content"),
    ("V", "V.full", "device identity, CV-1 arrival, CV-2 send, C's address", "device identity"),
    ("GK", "GK.full", "PacketHash, vk_id, C's address, its GK-leg arrival, own hold and post", "transaction (manufacturer)"),
]
CAPTURE_TO_REGISTRY_S = 723.0   # measured mean, Round 3 (RESULTS.md, volume table)


def _rows():
    return json.loads((EXT / "summary.json").read_text())


def _main_cell(r):
    return not r["variant"] and not r["share"] and r["nodes"] == 20


def _window_ok(r):
    return r["window_min"] == (40.0 if r["L"] >= 1000 else 180.0)


def pct(x, d=2):
    return "n/a" if x is None else f"{100 * x:.{d}f}%"


def extend_summary_csv(rows):
    path = RES / "summary.csv"
    with open(path) as f:
        old = list(csv.DictReader(f))
    old = [r for r in old if r.get("study", "rounds_2_3") == "rounds_2_3"]
    base = [k for k in old[0].keys() if k != "study"] if old else []
    extra = ["study", "round", "record", "label", "window_min", "nodes", "validator0_share", "lift", "lift_lo", "lift_hi",
             "top3", "accuracy_per_decision", "auc_posterior", "auc_posterior_lo", "auc_posterior_hi", "auc_gap",
             "auc_stable", "runs_needed_for_auc", "ece", "posterior_yield_coverage_at_p50",
             "posterior_best_precision_cov1", "signal", "minus_N_a", "minus_N_a_lo", "minus_N_a_hi",
             "minus_Nb_main", "minus_Nb_main_lo", "minus_Nb_main_hi"]
    cols = base + extra
    out = []
    for r in old:
        r = dict(r)
        r["study"] = "rounds_2_3"
        out.append(r)
    for r in rows:
        variant = f"round{r['round']}" + (f"_{r['variant']}" if r["variant"] else "")
        out.append(dict(config=variant, scenario=r["scenario"], variant=r["scenario_variant"],
                        devices=int(round(r["L"] * 10)), interval_min=20, L=r["L"], inv_L=round(1 / r["L"], 6),
                        runs=r["runs"], n_scored=r["n"], accuracy=r["accuracy"], ci_lo=r.get("ci_lo"), ci_hi=r.get("ci_hi"),
                        above_inv_L=r.get("signal_accuracy"), random_assignment=r.get("random_assignment"),
                        study="extension", round=r["round"], record=r["record"], label=r.get("label"),
                        window_min=r["window_min"], nodes=r["nodes"], validator0_share=r["share"],
                        **{k: r.get(k) for k in extra if k not in ("study", "round", "record", "label", "window_min",
                                                                   "nodes", "validator0_share")}))
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)


def copy_tables():
    for name in ("confidence_metrics.csv", "confidence_precision_coverage.csv", "confidence_reliability.csv"):
        if (EXT / name).exists():
            shutil.copy(EXT / name, RES / name)
    fig_src = EXT / "figures"
    if fig_src.exists():
        dst = RES / "figures"
        dst.mkdir(exist_ok=True)
        for p in fig_src.glob("*.png"):
            shutil.copy(p, dst / p.name)


def paper_table(rows):
    """One row per role, Round 3: accuracy [95% CI] at each L, and AUC [95% CI] at L = 4."""
    by = {(r["record"], r["L"]): r for r in rows if r["round"] == 3 and _main_cell(r) and _window_ok(r)}
    csv_rows, md = [], []
    head = "| Role | Knows exactly | Label | " + " | ".join(f"L = {L} (1/L = {pct(1 / L, 1)})" for L in L_GRID) + " | AUC, L = 4 |"
    md.append(head)
    md.append("|" + "---|" * (4 + len(L_GRID)))
    for role, rec, knows, label in ROLE_ROWS:
        cells, row = [], dict(role=role, record=rec, knows=knows, label=label)
        for L in L_GRID:
            r = by.get((rec, float(L)))
            if r:
                cells.append(f"{pct(r['accuracy'])} [{pct(r['ci_lo'])}, {pct(r['ci_hi'])}]")
                row.update({f"acc_L{L}": r["accuracy"], f"lo_L{L}": r["ci_lo"], f"hi_L{L}": r["ci_hi"],
                            f"lift_L{L}": r["lift"]})
            else:
                cells.append("not run")
        a = by.get((rec, 4.0))
        auc = (f"{a['auc_posterior']:.2f} [{a['auc_posterior_lo']:.2f}, {a['auc_posterior_hi']:.2f}]"
               if a and a.get("auc_stable") else "too few successes")
        if a:
            row.update(auc_L4=a.get("auc_posterior"), auc_L4_lo=a.get("auc_posterior_lo"), auc_L4_hi=a.get("auc_posterior_hi"))
        md.append(f"| {role} | {knows} | {label} | " + " | ".join(cells) + f" | {auc} |")
        csv_rows.append(row)
    with open(ROOT / "paper_table.csv", "w", newline="") as f:
        keys = sorted({k for r in csv_rows for k in r}, key=lambda k: (k not in ("role", "record", "knows", "label"), k))
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(csv_rows)
    return "\n".join(md)


def volume_table():
    lines = ["| L (workbook) | Devices | Captures per day | In flight at once (measured delay) |", "|---|---|---|---|"]
    for L in L_GRID:
        dev = int(L * 10)
        per_day = dev * 24 * 60 / 20
        inflight = dev / (20 * 60) * CAPTURE_TO_REGISTRY_S
        lines.append(f"| {L} | {dev:,} | {per_day:,.0f} | {inflight:,.0f} |")
    return "\n".join(lines)


def main():
    rows = _rows()
    extend_summary_csv(rows)
    copy_tables()
    table = paper_table(rows)
    (ROOT / "results" / "paper_table.md").write_text(table + "\n")
    (ROOT / "results" / "volume_table.md").write_text(volume_table() + "\n")
    print(table)
    print()
    print(volume_table())

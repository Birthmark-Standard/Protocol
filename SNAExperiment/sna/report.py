"""Tables and figures from the analysed records: results/summary.json, results/summary.csv,
results/tables.md, results/figures/*.png. RESULTS.md and PAPER_TABLE.md quote these files."""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

from . import analyze as AN
from . import attacks as AT
from . import cells as CE
from . import params as P
from . import runner as RN

ORDER = AT.VANTAGES


def pct(x, d=2):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{100 * x:.{d}f}%"


def ci(r, k, lo, hi, d=2):
    return f"{pct(r.get(k), d)} [{pct(r.get(lo), d)}, {pct(r.get(hi), d)}]"


def volume_table(D):
    lines = ["| L (in flight) | Captures per second | Captures per day | Devices (20-minute interval) |",
             "|---|---|---|---|"]
    for L in sorted(set(CE.DECOY_R) | set(CE.NODECOY_R) | {int(P.DECOYS_IN_FLIGHT)}):
        rate = L / D
        lines.append(f"| {L} | {rate:.4f} | {rate * 86400:,.0f} | {rate * P.INTERVAL_MIN * 60:,.1f} |")
    return "\n".join(lines)


def _load(out, key):
    """A cell's run records. Where re-scored records of the vantages scored on every record exist,
    they replace those vantages' rows run by run."""
    recs = RN.load(out, f"{key}__{CE.TARGET}")
    extra = {r["run"]: r for r in RN.load(out, f"{key}__{CE.TARGET}__allrecords")}
    if extra:
        recs = [r for r in recs if r["run"] in extra]
        for r in recs:
            for v in CE.ALL_RECORDS:
                if v != "baseline":
                    r["vantages"][v] = extra[r["run"]]["vantages"][v]
    return recs


def _clean(r):
    return {k: v for k, v in r.items() if not k.startswith("_")}


def build(out: Path):
    out = Path(out)
    cells = json.loads((out / "cells.json").read_text())
    rows, effects = AN.analyze(out, cells, lambda k: _load(out, k))
    clean = [_clean(r) for r in rows]
    (out / "summary.json").write_text(json.dumps(dict(rows=clean, decoy_effects=effects), indent=1, default=float))
    keys = sorted({k for r in clean for k in r if not isinstance(r[k], dict)},
                  key=lambda k: (k not in ("cell", "vantage", "R", "T"), k))
    with open(out / "summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(clean)
    D = CE.calibrate(out)["D"]
    md = tables(clean, effects, D, out)
    (out / "tables.md").write_text(md)
    figures(clean, out / "figures")
    print(f"wrote {out / 'summary.json'}, summary.csv, tables.md and figures/")


def _get(rows, v, R, T, control=False):
    for r in rows:
        if r["vantage"] == v and r["R"] == R and r["T"] == T and r["control"] == control:
            return r
    return None


def _acc(r, lvl):
    s = ci(r, f"{lvl}_accuracy", f"{lvl}_ci_lo", f"{lvl}_ci_hi")
    if lvl == "dev" and not r["stable"]:
        s += f" (unstable; {r['runs_needed']} runs needed)"
    return s


def _cell_label(r):
    return f"R = {r['R']:g}" + (f" + {P.DECOYS_IN_FLIGHT:g} decoys (T = {r['T']:g})" if r.get("T", r["R"]) > r["R"] else ", no decoys")


def tables(rows, effects, D, out):
    md = [f"# Tables\n\nRecord-to-device linking with genuine decoys. Measured end-to-end delay D = {D:.1f} s. "
          "Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the "
          "record's. Submission level: the named submission group contains a packet of the record's capture. "
          "Rows are real records only.\n"]
    md.append("## Volume\n\n" + volume_table(D) + "\n")
    cells_ = sorted({(r["R"], r["T"], r["control"]) for r in rows if not r["control"]}, key=lambda x: (x[1] > x[0], x[0]))
    md.append("## Every cell\n")
    for v in ORDER:
        md.append(f"### {AT.LABEL[v]}\n")
        md.append("| Cell | Device accuracy [95% CI] | Random device | Lift vs random | Baseline | Contribution [95% CI] | "
                  "Submission accuracy [95% CI] | 1/T | Lift (x T) | Baseline | Contribution [95% CI] | "
                  "AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |")
        md.append("|" + "---|" * 17)
        for R, T, _ in cells_:
            r = _get(rows, v, R, T)
            if not r or "dev_accuracy" not in r:
                continue
            md.append(f"| {_cell_label(r)} | {_acc(r, 'dev')} | {pct(r['dev_random'])} | {r['dev_lift_random']:.2f} | "
                      f"{pct(r['dev_baseline'])} | {ci(r, 'dev_contribution', 'dev_contribution_lo', 'dev_contribution_hi')} | "
                      f"{_acc(r, 'sub')} | {pct(1 / T)} | {r['sub_accuracy'] * T:.2f} | {pct(r['sub_baseline'])} | "
                      f"{ci(r, 'sub_contribution', 'sub_contribution_lo', 'sub_contribution_hi')} | "
                      f"{r['auc']:.3f} [{r['auc_lo']:.3f}, {r['auc_hi']:.3f}] | {pct(r['p_at_1'], 1)} | "
                      f"{pct(r['p_at_5'], 1)} | {pct(r['coverage_p50'], 3)} | {r['runs']} | {r['n']} |")
        md.append("")
    md.append("## Effect of the decoy stream on the same real records\n")
    md.append("Accuracy with decoys minus accuracy without, matched record by record on identical real traffic.\n")
    md.append("| Vantage | R | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |")
    md.append("|---|---|---|---|---|")
    for v in ORDER:
        for R in CE.NODECOY_R:
            e = effects.get(f"{v}.R{R:g}")
            if e:
                md.append(f"| {AT.LABEL[v]} | {R} | {100 * e['dev']['effect']:+.2f} [{100 * e['dev']['lo']:+.2f}, {100 * e['dev']['hi']:+.2f}] | "
                          f"{100 * e['sub']['effect']:+.2f} [{100 * e['sub']['lo']:+.2f}, {100 * e['sub']['hi']:+.2f}] | {e['dev']['n']} |")
    md.append("")
    md.append("## Sensitivity control (R = 40, every hold off)\n")
    md.append("| Vantage | Device accuracy [95% CI] | Random device | Submission accuracy | 1/L |")
    md.append("|---|---|---|---|---|")
    for v in ORDER:
        r = _get(rows, v, CE.CONTROL_R, CE.CONTROL_R, True)
        if r and "dev_accuracy" in r:
            md.append(f"| {AT.LABEL[v]} | {_acc(r, 'dev')} | {pct(r['dev_random'])} | {pct(r['sub_accuracy'])} | {pct(1 / CE.CONTROL_R)} |")
    md.append("")
    md.append("## Outcome-shuffle control (stable cells)\n")
    st = [r for r in rows if r.get("stable")]
    bad = [r for r in st if not (r["shuffle_auc_lo"] <= 0.5 <= r["shuffle_auc_hi"])]
    md.append(f"{len(st)} stable cells; {len(bad)} with a shuffled-outcome AUC interval excluding 0.5"
              + ("" if not bad else ": " + ", ".join(f"{r['cell']} {r['vantage']} ({r['shuffle_auc']:.3f})" for r in bad))
              + ".\n")
    return "\n".join(md)


# --------------------------------------------------------------------------- figures
SURFACE, INK, INK2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e5a", "#e6e5e0"
SLOT = {"baseline": "#2a78d6", "first_hop_cred": "#eb6834", "first_hop_content": "#eda100",
        "cred_processor": "#1baf7a", "content_server": "#e87ba4", "validator": "#008300", "gatekeeper": "#4a3aa7"}
MARK = {"baseline": "o", "first_hop_cred": "s", "first_hop_content": "^", "cred_processor": "D",
        "content_server": "v", "validator": "P", "gatekeeper": "X"}


def _style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=7)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def figures(rows, fig_dir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig_dir = Path(fig_dir)
    fig_dir.mkdir(parents=True, exist_ok=True)
    f = plt.figure(figsize=(10, 4.4), dpi=300, facecolor=SURFACE)
    for i, (key, lo, hi, ylab) in enumerate((("dev_accuracy", "dev_ci_lo", "dev_ci_hi", "device accuracy"),
                                             ("sub_accuracy", "sub_ci_lo", "sub_ci_hi", "submission accuracy"))):
        ax = f.add_subplot(1, 2, i + 1)
        _style(ax)
        for v in ORDER:
            pts = sorted((r for r in rows if r["vantage"] == v and r["T"] > r["R"] and not r["control"] and key in r),
                         key=lambda r: r["R"])
            if not pts:
                continue
            x = np.array([r["R"] for r in pts])
            ax.fill_between(x, [r[lo] for r in pts], [r[hi] for r in pts], color=SLOT[v], alpha=0.12, linewidth=0)
            ax.plot(x, [r[key] for r in pts], "-", color=SLOT[v], linewidth=2, marker=MARK[v], markersize=4,
                    markeredgecolor=SURFACE, label=AT.LABEL[v])
            nd = sorted((r for r in rows if r["vantage"] == v and r["T"] == r["R"] and not r["control"] and key in r),
                        key=lambda r: r["R"])
            ax.plot([r["R"] for r in nd], [r[key] for r in nd], linestyle="none", color=SLOT[v], marker=MARK[v],
                    markersize=5, markerfacecolor="none")
        if i == 0:
            pts = sorted((r for r in rows if r["vantage"] == "baseline" and r["T"] > r["R"] and not r["control"]),
                         key=lambda r: r["R"])
            ax.plot([r["R"] for r in pts], [r["dev_random"] for r in pts], ":", color=INK2, linewidth=1,
                    label="random device")
            ax.legend(fontsize=6.5, frameon=False, labelcolor=INK)
        else:
            Rs = np.array(sorted({r["R"] for r in rows if r["T"] > r["R"] and not r["control"]}))
            ax.plot(Rs, 1 / (Rs + P.DECOYS_IN_FLIGHT), ":", color=INK2, linewidth=1)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("R (real transactions in flight), with 40 decoys in flight", color=INK, fontsize=8)
        ax.set_ylabel(ylab + " (hollow: no decoys)", color=INK, fontsize=8)
    f.tight_layout()
    f.savefig(fig_dir / "accuracy_vs_R.png", facecolor=SURFACE)
    plt.close(f)

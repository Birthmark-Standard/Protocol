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
    for L in sorted(set(CE.LOW_R) | set(CE.WIDE_L)):
        rate = L / D
        lines.append(f"| {L} | {rate:.4f} | {rate * 86400:,.0f} | {rate * P.INTERVAL_MIN * 60:,.1f} |")
    return "\n".join(lines)


def _clean(r):
    return {k: v for k, v in r.items() if not k.startswith("_")}


def build(out: Path):
    out = Path(out)
    cells = json.loads((out / "cells.json").read_text())
    rows, trends = AN.analyze(out, cells, lambda k: RN.load(out, f"{k}__{CE.TARGET}"))
    clean = [_clean(r) for r in rows]
    (out / "summary.json").write_text(json.dumps(dict(rows=clean, trends=trends), indent=1, default=float))
    keys = sorted({k for r in clean for k in r if not isinstance(r[k], dict)},
                  key=lambda k: (k not in ("cell", "vantage", "R", "T"), k))
    with open(out / "summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(clean)
    D = CE.calibrate(out)["D"]
    md = tables(clean, trends, D, out)
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


def tables(rows, trends, D, out):
    md = [f"# Tables\n\nRecord-to-device linking. Measured end-to-end delay D = {D:.1f} s. Per-decision "
          "attack; intervals resample whole runs. Device level (primary): the named device is the record's. "
          "Submission level: the named submission group contains a packet of the record's capture.\n"]
    md.append("## Volume\n\n" + volume_table(D) + "\n")
    Ls = sorted({int(r["R"]) for r in rows if r["R"] == r["T"] and not r["control"]})
    md.append("## No-decoy sweep (T = R)\n")
    for v in ORDER:
        md.append(f"### {AT.LABEL[v]}\n")
        md.append("| L | Device accuracy [95% CI] | Random device | Lift vs random | Baseline | Contribution [95% CI] | "
                  "Submission accuracy [95% CI] | 1/L | Lift (x L) | Baseline | Contribution [95% CI] | "
                  "AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |")
        md.append("|" + "---|" * 17)
        for L in Ls:
            r = _get(rows, v, L, L)
            if not r or "dev_accuracy" not in r:
                continue
            ub = " (upper bound)" if v in AT.CAN_TELL and L > 40 else ""
            md.append(f"| {L}{ub} | {_acc(r, 'dev')} | {pct(r['dev_random'])} | {r['dev_lift_random']:.2f} | "
                      f"{pct(r['dev_baseline'])} | {ci(r, 'dev_contribution', 'dev_contribution_lo', 'dev_contribution_hi')} | "
                      f"{_acc(r, 'sub')} | {pct(1 / L)} | {r['sub_lift']:.2f} | {pct(r['sub_baseline'])} | "
                      f"{ci(r, 'sub_contribution', 'sub_contribution_lo', 'sub_contribution_hi')} | "
                      f"{r['auc']:.3f} [{r['auc_lo']:.3f}, {r['auc_hi']:.3f}] | {pct(r['p_at_1'], 1)} | "
                      f"{pct(r['p_at_5'], 1)} | {pct(r['coverage_p50'], 3)} | {r['runs']} | {r['n']} |")
        md.append("")
    md.append("## Lift trend, L = 40 to 500 (no-decoy sweep)\n")
    md.append("| Vantage | Level | Lift at 40 | Lift at 500 | Slope of log lift on log L [95% CI] | Direction |")
    md.append("|---|---|---|---|---|---|")
    for v in ORDER:
        for level, name in (("dev", "device (vs random)"), ("sub", "submission (x L)")):
            t = trends.get(f"{v}.{level}")
            if t:
                md.append(f"| {AT.LABEL[v]} | {name} | {t['lift_40']:.2f} | {t['lift_500']:.2f} | "
                          f"{t['slope']:.3f} [{t['lo']:.3f}, {t['hi']:.3f}] | {t['direction']} |")
    md.append("")
    Ts = sorted({int(r["T"]) for r in rows})
    for lvl, title in (("dev", "Device accuracy"), ("sub", "Submission accuracy")):
        md.append(f"## Decoy sweep: {title.lower()} (rows R, columns T)\n")
        for v in ORDER:
            md.append(f"### {AT.LABEL[v]}" + (" (can tell decoys: every T > R entry is an upper bound on L)"
                                              if v in AT.CAN_TELL else "") + "\n")
            md.append("| R \\ T | " + " | ".join(str(T) for T in Ts) + " |")
            md.append("|" + "---|" * (len(Ts) + 1))
            for R in CE.LOW_R:
                cells_ = []
                for T in Ts:
                    r = _get(rows, v, R, T)
                    cells_.append("" if r is None or f"{lvl}_accuracy" not in r else
                                  f"{pct(r[f'{lvl}_accuracy'])} ({r[f'{lvl}_contribution'] * 100:+.2f})"
                                  + ("" if r["stable"] else " u"))
                md.append(f"| {R} | " + " | ".join(cells_) + " |")
            md.append("\n(Accuracy, then the contribution over the paired baseline in points. u: fewer than 50 "
                      "device-level successes or failures; runs needed in summary.csv.)\n")
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
    for i, (lvl, key, lo, hi, ylab) in enumerate((
            ("dev", "dev_lift_random", "dev_lift_random_lo", "dev_lift_random_hi", "device accuracy / random device rate"),
            ("sub", "sub_lift", "sub_lift_lo", "sub_lift_hi", "submission accuracy x L"))):
        ax = f.add_subplot(1, 2, i + 1)
        _style(ax)
        for v in ORDER:
            pts = sorted((r for r in rows if r["vantage"] == v and r["R"] == r["T"] and not r["control"] and key in r),
                         key=lambda r: r["R"])
            if not pts:
                continue
            x = np.array([r["R"] for r in pts])
            ax.fill_between(x, np.maximum([r[lo] for r in pts], 1e-3), np.maximum([r[hi] for r in pts], 1e-3),
                            color=SLOT[v], alpha=0.12, linewidth=0)
            ax.plot(x, np.maximum([r[key] for r in pts], 1e-3), "-", color=SLOT[v], linewidth=2, marker=MARK[v],
                    markersize=4, markeredgecolor=SURFACE, label=AT.LABEL[v])
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.axhline(1.0, color=INK2, linewidth=1, linestyle=":")
        ax.set_xlabel("L (real transactions in flight, no decoys)", color=INK, fontsize=8)
        ax.set_ylabel(ylab + " (1 = chance)", color=INK, fontsize=8)
        ax.set_title("Device level" if lvl == "dev" else "Submission level", fontsize=9, color=INK, loc="left")
        if i == 0:
            ax.legend(fontsize=6.5, frameon=False, labelcolor=INK)
    f.tight_layout()
    f.savefig(fig_dir / "lift_vs_L_nodecoy.png", facecolor=SURFACE)
    plt.close(f)
    f = plt.figure(figsize=(10, 5.2), dpi=300, facecolor=SURFACE)
    cmap = plt.get_cmap("viridis")
    for i, v in enumerate(ORDER):
        ax = f.add_subplot(2, 4, i + 1)
        _style(ax)
        for j, R in enumerate(CE.LOW_R):
            pts = sorted((r for r in rows if r["vantage"] == v and r["R"] == R and not r["control"] and "dev_accuracy" in r),
                         key=lambda r: r["T"])
            if not pts:
                continue
            ax.plot([r["T"] for r in pts], np.maximum([r["dev_accuracy"] for r in pts], 1e-4), "-o", markersize=2.5,
                    linewidth=1.3, color=cmap(j / (len(CE.LOW_R) - 1)), label=f"R = {R}")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_ylim(1e-4, 1.2)
        ax.set_title(AT.LABEL[v], fontsize=8, color=INK, loc="left")
        ax.set_xlabel("T (total in flight)", fontsize=7, color=INK)
        if i % 4 == 0:
            ax.set_ylabel("device accuracy", fontsize=7, color=INK)
    ax = f.add_subplot(2, 4, 8)
    ax.axis("off")
    h, lab = f.axes[0].get_legend_handles_labels()
    if h:
        ax.legend(h, lab, fontsize=7, frameon=False, loc="center", labelcolor=INK)
    f.tight_layout()
    f.savefig(fig_dir / "device_accuracy_vs_T_decoy.png", facecolor=SURFACE)
    plt.close(f)

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
    for L in sorted({R + d for R in CE.REAL_R for d in CE.DECOY_LEVELS} | set(CE.REAL_R)):
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
    (out / "summary.json").write_text(json.dumps(dict(rows=clean, bundling_effects=effects), indent=1, default=float))
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


def _get(rows, v, R, d, bundle, control=False):
    for r in rows:
        if (r["vantage"] == v and r["R"] == R and r.get("decoys", 0) == d and r.get("bundle", False) == bundle
                and r["control"] == control):
            return r
    return None


def _acc(r, lvl):
    s = ci(r, f"{lvl}_accuracy", f"{lvl}_ci_lo", f"{lvl}_ci_hi")
    if lvl == "dev" and not r["stable"]:
        s += f" (unstable; {r['runs_needed']} runs needed)"
    return s


def _cell_label(r):
    if r["control"]:
        return f"R = {r['R']:g}, every hold off"
    return f"R = {r['R']:g}, {r['decoys']:g} decoys, bundling {'on' if r['bundle'] else 'off'}"


def tables(rows, effects, D, out):
    md = [f"# Tables\n\nRecord-to-device linking with genuine decoys, gatekeeper departure bundling on and off. "
          f"Measured end-to-end delay D = {D:.1f} s. Per-decision attack; intervals resample whole runs. Device level "
          "(primary): the named device is the record's. Submission level: the named submission group contains a "
          "packet of the record's capture. Rows are real records only. The first hops and the credential processor "
          "are scored on every record.\n"]
    md.append("## Volume\n\n" + volume_table(D) + "\n")
    md.append("## Departure bundle sizes\n")
    md.append("Postings per 30-second bundle at one gatekeeper, on its own grid, over every run of the cell. Off cells "
              "report the bundles the same selections would have formed.\n")
    md.append("| R | Decoys | Mean per bundle | Empty | Exactly 1 | Fewer than 2 | 1, of non-empty | Postings departing alone | Bundles |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    for R in CE.REAL_R:
        for d in CE.DECOY_LEVELS:
            r = _get(rows, "baseline", R, d, True)
            if r and "bundle_mean" in r:
                md.append(f"| {R} | {d} | {r['bundle_mean']:.2f} | {pct(r['bundle_p0'], 1)} | {pct(r['bundle_p1'], 1)} | "
                          f"{pct(r['bundle_p_lt2'], 1)} | {pct(r['bundle_p1_nonempty'], 1)} | {pct(r['bundle_alone_share'], 1)} | "
                          f"{r['bundle_bundles']:,} |")
    md.append("")
    md.append("## Effect of bundling on the same records\n")
    md.append("Accuracy with bundling minus accuracy without, matched record by record on identical traffic "
              "(percentage points).\n")
    md.append("| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |")
    md.append("|---|---|---|---|---|---|")
    for v in ORDER:
        for R in CE.REAL_R:
            for d in CE.DECOY_LEVELS:
                e = effects.get(f"{v}.R{R:g}.D{d:g}")
                if e:
                    md.append(f"| {AT.LABEL[v]} | {R} | {d} | {100 * e['dev']['effect']:+.2f} [{100 * e['dev']['lo']:+.2f}, "
                              f"{100 * e['dev']['hi']:+.2f}] | {100 * e['sub']['effect']:+.2f} [{100 * e['sub']['lo']:+.2f}, "
                              f"{100 * e['sub']['hi']:+.2f}] | {e['dev']['n']} |")
    md.append("")
    md.append("## Every cell\n")
    for v in ORDER:
        md.append(f"### {AT.LABEL[v]}\n")
        md.append("| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | "
                  "Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | "
                  "AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |")
        md.append("|" + "---|" * 15)
        for r in sorted((x for x in rows if x["vantage"] == v),
                        key=lambda x: (x["control"], x["R"], x.get("decoys", 0), x.get("bundle", False))):
            if "dev_accuracy" not in r:
                continue
            md.append(f"| {_cell_label(r)} | {_acc(r, 'dev')} | {pct(r['dev_random'])} | {pct(r['dev_baseline'])} | "
                      f"{ci(r, 'dev_contribution', 'dev_contribution_lo', 'dev_contribution_hi')} | {_acc(r, 'sub')} | "
                      f"{pct(1 / r['T'])} | {pct(r['sub_baseline'])} | "
                      f"{ci(r, 'sub_contribution', 'sub_contribution_lo', 'sub_contribution_hi')} | "
                      f"{r['auc']:.3f} [{r['auc_lo']:.3f}, {r['auc_hi']:.3f}] | {pct(r['p_at_1'], 1)} | "
                      f"{pct(r['p_at_5'], 1)} | {pct(r['coverage_p50'], 3)} | {r['runs']} | {r['n']} |")
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
    cmap = plt.get_cmap("viridis")
    for i, (key, ylab) in enumerate((("dev_accuracy", "passive observer: device accuracy"),
                                     ("sub_accuracy", "passive observer: submission accuracy"))):
        ax = f.add_subplot(1, 2, i + 1)
        _style(ax)
        for j, R in enumerate(CE.REAL_R):
            col = cmap(j / max(len(CE.REAL_R) - 1, 1) * 0.85)
            for bundle, ls in ((False, "--"), (True, "-")):
                pts = sorted((r for r in rows if r["vantage"] == "baseline" and r["R"] == R and not r["control"]
                              and r.get("bundle") == bundle and key in r), key=lambda r: r["decoys"])
                if pts:
                    ax.plot([r["decoys"] for r in pts], [r[key] for r in pts], ls, color=col, linewidth=2, marker="o",
                            markersize=3.5, label=f"R = {R}, bundling {'on' if bundle else 'off'}")
        ax.set_yscale("log")
        ax.set_xlabel("decoys in flight", color=INK, fontsize=8)
        ax.set_ylabel(ylab, color=INK, fontsize=8)
        if i == 0:
            ax.legend(fontsize=6.5, frameon=False, labelcolor=INK)
    f.tight_layout()
    f.savefig(fig_dir / "bundling_gpa.png", facecolor=SURFACE)
    plt.close(f)

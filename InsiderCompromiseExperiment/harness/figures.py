"""Figures (PNG, 300 dpi): lift against L, confidence ECDFs, reliability, precision against coverage.

Colours: the dataviz reference categorical palette in fixed order, one slot per scenario, validated
(scripts/validate_palette.js, light surface): all checks pass; three light hues are below 3:1
against the surface, so every series also carries a direct label and its own marker shape, and the
numbers are in RESULTS.md tables.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

SURFACE, INK, INK2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e5a", "#e6e5e0"
SLOT = {"N": "#2a78d6", "A": "#eb6834", "C": "#1baf7a", "D": "#eda100", "F": "#e87ba4",
        "V": "#008300", "GK": "#4a3aa7", "F (Round 1)": "#e34948"}
MARK = {"N": "o", "A": "s", "C": "D", "D": "^", "F": "v", "V": "P", "GK": "X", "F (Round 1)": "o"}
ORDER = ("N", "A", "C", "D", "F", "V", "GK")
PRIMARY = {"N": "Nb.seq", "A": "A", "C": "C", "D": "D", "F": "F.full", "V": "V.full", "GK": "GK.full"}
TWO = ("#2a78d6", "#eb6834")        # correct, incorrect


def _style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=7)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def _fig(w, h):
    f = plt.figure(figsize=(w, h), dpi=300, facecolor=SURFACE)
    return f


def _main_series(rows, rec, rnd):
    """Main cells of one record: 20 nodes, no variant or share, the 3-hour window (40 minutes at
    L = 1000, where compute sets the window)."""
    return sorted((r for r in rows if r["record"] == rec and r["round"] == rnd and not r["variant"]
                   and not r["share"] and r["nodes"] == 20
                   and r["window_min"] == (40.0 if r["L"] >= 1000 else 180.0)), key=lambda r: r["L"])


def _spread(ys, min_gap):
    """End-label positions (log10 units) pushed apart by at least min_gap, order kept."""
    order = np.argsort(ys)
    out = np.array(ys, float)
    for i in range(1, len(order)):
        a, b = order[i - 1], order[i]
        if out[b] - out[a] < min_gap:
            out[b] = out[a] + min_gap
    return out


def lift_vs_L(rows, path, rnd=3):
    """Lift (accuracy x L) against L for each scenario's primary attack, Round 3, with F under
    Round 1 dashed. Left: joint assignment (pre-registered). Right: per-decision attack."""
    f = _fig(10.0, 4.4)
    for k, (mode, title) in enumerate((("joint", "Joint assignment (pre-registered primary)"),
                                       ("per_decision", "Per-decision attack"))):
        ax = f.add_subplot(1, 2, k + 1)
        _style(ax)
        series = [(sc, _main_series(rows, PRIMARY[sc], rnd), "-") for sc in ORDER]
        series.append(("F (Round 1)", _main_series(rows, "F.full", 1), "--"))
        ends = []
        for name, pts, ls in series:
            if not pts:
                continue
            x = np.array([r["L"] for r in pts])
            if mode == "joint":
                y = np.array([r["lift"] for r in pts])
                ax.fill_between(x, [r["lift_lo"] for r in pts], [r["lift_hi"] for r in pts],
                                color=SLOT[name], alpha=0.12, linewidth=0)
            else:
                y = np.array([r["accuracy_per_decision"] * r["L"] for r in pts])
            y = np.maximum(y, 1e-3)
            ax.plot(x, y, ls, color=SLOT[name], linewidth=2, marker=MARK[name], markersize=4,
                    markeredgecolor=SURFACE, markeredgewidth=0.8)
            ends.append((name, x[-1], y[-1]))
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_ylim(0.01, 30)
        ax.axhline(1.0, color=INK2, linewidth=1, linestyle=":")
        ax.annotate("chance (lift = 1)", (4, 1.0), xytext=(0, 4), textcoords="offset points", fontsize=7, color=INK2)
        ly = _spread([np.log10(e[2]) for e in ends], 0.09)
        for (name, xe, ye), yl in zip(ends, ly):
            ax.annotate(name, (xe, ye), xytext=(xe * 1.25, 10 ** yl), textcoords="data", va="center",
                        fontsize=7, color=INK, arrowprops=dict(arrowstyle="-", color=GRID, linewidth=0.6))
        ax.set_xlim(3, 4000)
        ax.set_xlabel("L (workbook Little's-law anonymity set)", color=INK, fontsize=8)
        if k == 0:
            ax.set_ylabel("lift = accuracy x L", color=INK, fontsize=8)
        ax.set_title(title, color=INK, fontsize=9, loc="left")
    f.suptitle(f"Lift against L, Round {rnd} (F under Round 1 dashed). L = 1000 uses the 40-minute window.",
               fontsize=8, color=INK2, x=0.01, ha="left")
    f.tight_layout()
    f.savefig(path, facecolor=SURFACE)
    plt.close(f)


def _panels(n):
    cols = min(4, n)
    rows = int(np.ceil(n / cols))
    return rows, cols


def per_cell(cell, rows, curves, outdir):
    """ECDF, reliability and precision-coverage small multiples for one cell (primary attacks)."""
    recs = [(sc, PRIMARY[sc]) for sc in ORDER if (cell, PRIMARY[sc]) in curves]
    if not recs:
        return
    L = next(r["L"] for r in rows if r["cell"] == cell)
    nr, nc = _panels(len(recs))
    for kind in ("ecdf", "reliability", "precision_coverage"):
        f = _fig(2.1 * nc, 1.9 * nr + 0.4)
        for i, (sc, rec) in enumerate(recs):
            ax = f.add_subplot(nr, nc, i + 1)
            _style(ax)
            cv = curves[(cell, rec)]
            corr = cv["correct"]
            conf = cv["posterior"]["conf"]
            if kind == "ecdf":
                for lab, m, col in (("correct", corr, TWO[0]), ("incorrect", ~corr, TWO[1])):
                    x = np.sort(conf[m])
                    if x.size:
                        ax.step(x, np.arange(1, x.size + 1) / x.size, where="post", color=col, linewidth=1.5,
                                label=f"{lab} (n={x.size})")
                ax.set_xlim(0, 1)
                ax.legend(fontsize=5.5, frameon=False, loc="lower right", labelcolor=INK)
                ax.set_xlabel("calibrated posterior", fontsize=6.5, color=INK)
            elif kind == "reliability":
                rel = cv["reliability"]
                x = [r["confidence"] for r in rel]
                y = [r["accuracy"] for r in rel]
                ax.plot([0, 1], [0, 1], color=INK2, linewidth=0.8, linestyle=":")
                ax.plot(x, y, color=SLOT[sc], linewidth=2, marker=MARK[sc], markersize=4,
                        markeredgecolor=SURFACE, markeredgewidth=0.8)
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.set_xlabel("confidence", fontsize=6.5, color=INK)
            else:
                order = np.argsort(-conf, kind="stable")
                c = corr[order].astype(float)
                k = np.arange(1, c.size + 1)
                ax.plot(k / c.size, np.cumsum(c) / k, color=SLOT[sc], linewidth=2)
                ax.axhline(1 / L, color=INK2, linewidth=0.8, linestyle=":")
                ax.set_xscale("log")
                ax.set_ylim(0, 1)
                ax.set_xlabel("coverage", fontsize=6.5, color=INK)
            ax.set_title(f"{sc} ({rec})", fontsize=7, color=INK, loc="left")
        title = {"ecdf": "Confidence given correct vs incorrect", "reliability": "Reliability (calibrated posterior)",
                 "precision_coverage": "Precision against coverage (dotted: 1/L)"}[kind]
        f.suptitle(f"{title}: {cell}", fontsize=8, color=INK, x=0.01, ha="left")
        f.tight_layout()
        f.savefig(Path(outdir) / f"{kind}_{cell}.png", facecolor=SURFACE)
        plt.close(f)


def make_all(out, rows, curves):
    fig = Path(out) / "figures"
    fig.mkdir(parents=True, exist_ok=True)
    lift_vs_L(rows, fig / "lift_vs_L_round3.png", 3)
    for cell in sorted({c for c, _ in curves}):
        per_cell(cell, rows, curves, fig)

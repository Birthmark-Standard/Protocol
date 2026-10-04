"""Run10: the tables and figures a reader of the paper needs, written from the sequence's own outputs
into <out>/RUN10_TABLES.md and <out>/figures/.

Every number here is read from the summaries, latency, timing and pair-gap files of the same run; the
report computes nothing new except the zero-access baseline (one over every registered device)."""
from __future__ import annotations

import json
import math
from pathlib import Path

from . import attacks as AT
from . import cells as CE

ORDER = ("baseline", "first_hop_cred", "first_hop_content", "cred_processor", "validator", "gatekeeper",
         "content_server")
NAME = {"baseline": "Passive observer", "first_hop_cred": "First hop, credential", "first_hop_content": "First hop, content",
        "cred_processor": "Credential processor", "validator": "Validator", "gatekeeper": "Gatekeeper",
        "content_server": "Content server"}
EXCLUSIONS = (("run10_no_vc", "without V's and C's holds"), ("run10_no_incl", "without the inclusion lottery (next-boundary bundling)"),
              ("run10_no_pm", "without the post-match lottery"), ("run10_no_reg", "without registry bundling"),
              ("run10_no_role", "without role-aware holds (device content and F/I at 120 s)"),
              ("run10_none", "without all five"))
VARIATIONS = (("run10_relay180", "relay hops at 180 s"), ("run10_role360", "device content and F/I at 360 s"),
              ("run10_gk120", "gatekeeper hold at 120 s"))


def _pct(x, d=2):
    return f"{100 * x:.{d}f}%"


def _rows(out, build):
    p = Path(out) / f"summary_{build}.json"
    if not p.exists():
        return None, None
    d = json.loads(p.read_text())
    return {(r["cell"], r["vantage"]): r for r in d["rows"]}, d.get("build_effects", {})


def _cell(R):
    return CE.cell_key(R, CE.RUN10_DECOYS, True)


def _strongest(rows, c):
    return max(ORDER, key=lambda v: rows[(c, v)]["dev_accuracy"])


def write(out):
    out = Path(out)
    D = CE.calibrate(out)["D"]
    lat = json.loads((out / "latency.json").read_text())["cells"] if (out / "latency.json").exists() else {}
    timing = json.loads((out / "timing_check.json").read_text())["builds"] if (out / "timing_check.json").exists() else {}
    pairs = json.loads((out / "pair_gaps.json").read_text())["cells"] if (out / "pair_gaps.json").exists() else {}
    base, _ = _rows(out, "run10")
    md = ["# Run10 tables", "",
          f"Generated from `{out.name}/`. End-to-end delay under Run10: D = {D:.1f} s; rates are R / D and "
          f"{CE.RUN10_DECOYS} / D, so R real and {CE.RUN10_DECOYS} decoy transactions are in flight. Device level: the "
          "vantage names the device behind a registry record. Intervals are 95%, resampling whole runs.", ""]

    if "run10" in timing:
        md += ["## Timing as simulated (R = 20)", "", "| Stage | Mean | Std dev | Maximum |", "|---|---|---|---|"]
        for name, v in timing["run10"]["stages"].items():
            md.append(f"| {name} | {v['mean']:.1f} s | {v['sd']:.1f} s | {v['max']:.1f} s |")
        bd = timing["run10"]["bundle"]
        md += ["", f"Postings per departure bundle at one gatekeeper: mean {bd['mean']:.2f}; "
               f"{_pct(bd['p_lt2'], 1)} of bundles hold fewer than two; {_pct(bd['p_empty'], 1)} are empty.", ""]

    if base:
        md += ["## The adversary against Run10", "",
               "For each single compromised component: how often it names the right device, against two chance "
               "rates (a guess among the devices that could have produced the record, and a guess among every "
               "registered device), its lead over a passive observer, and its own confidence that a match is right.", ""]
        for R in CE.RUN10_R:
            c = _cell(R)
            cfg = CE.config_of(dict(R=float(R), decoys=float(CE.RUN10_DECOYS), bundle=True, control=False, build="run10"), D)
            N = cfg.real_devices + cfg.decoy_sources
            md += [f"### R = {R}, {CE.RUN10_DECOYS} decoys ({N} registered devices; one in {N} is {_pct(1 / N)})", "",
                   "| Component | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Multiple of one in N "
                   "| Lead over observer [95% CI] | Mean confidence in its match | Confidence, 99th percentile | Top 1% right [95% CI] "
                   "| Decisions in a most-confident set right more than half the time |",
                   "|---|---|---|---|---|---|---|---|---|---|"]
            for v in ORDER:
                r = base[(c, v)]
                lead = "" if v == "baseline" else (f"{100 * r['dev_contribution']:+.2f} [{100 * r['dev_contribution_lo']:+.2f}, "
                                                   f"{100 * r['dev_contribution_hi']:+.2f}]")
                md.append(f"| {NAME[v]} | {_pct(r['dev_accuracy'])} [{_pct(r['dev_ci_lo'])}, {_pct(r['dev_ci_hi'])}] | "
                          f"{_pct(r['dev_random'])} | ×{r['dev_lift_random']:.2f} [{r['dev_lift_random_lo']:.2f}, {r['dev_lift_random_hi']:.2f}] | "
                          f"×{r['dev_accuracy'] * N:.1f} | {lead or 'reference'} | {_pct(r['conf_mean'])} | {_pct(r['conf_p99'])} | "
                          f"{_pct(r['p_at_1'], 1)} [{_pct(r['p_at_1_lo'], 1)}, {_pct(r['p_at_1_hi'], 1)}] | "
                          f"{r['count_p50']} of {r['decisions']:,} |")
            ok = all(base[(c, v)]["p_at_1_hi"] < 0.5 and base[(c, v)]["coverage_p50"] < 0.001 for v in ORDER)
            L = lat.get(f"run10.R{R}.D{CE.RUN10_DECOYS}", {}).get("total", {})
            md += ["", f"Claim criterion (section 6i): **{'pass' if ok else 'fail'}**. Mean capture to finalisation: "
                   f"{L.get('mean', float('nan')):.0f} s (median {L.get('median', float('nan')):.0f} s, 95th percentile "
                   f"{L.get('p95', float('nan')):.0f} s).", ""]

        md += ["## Reliability of the adversary's confidence (R = 20)", "",
               "Matches sorted into ten equal groups by the component's own calibrated confidence; each row compares "
               "the group's mean confidence with how often its matches were right.", "",
               "| Component | Lowest decile: confidence / right | Median decile | Highest decile | Mean absolute gap |",
               "|---|---|---|---|---|"]
        c = _cell(20)
        for v in ORDER:
            rel = base[(c, v)]["reliability"]
            f = lambda x: f"{_pct(x['conf'], 1)} / {_pct(x['hit'], 1)}"
            md.append(f"| {NAME[v]} | {f(rel[0])} | {f(rel[len(rel) // 2])} | {f(rel[-1])} | {base[(c, v)]['calibration_error'] * 100:.2f} points |")
        md.append("")

    for title, group in (("What each mechanism contributes: Run10 with one mechanism removed", EXCLUSIONS),
                         ("Variations on Run10", VARIATIONS)):
        md += [f"## {title}", "",
               "Paired against Run10 on the same records (the effect is the variant minus Run10, in points).", "",
               "| Variant | R | Strongest component | Device named | Multiple of chance [95% CI] | Largest lead over observer "
               "| Observer: effect vs Run10 [95% CI] | Strongest Run10 component: effect vs Run10 [95% CI] | Top 1% right, best component "
               "| Mean latency |", "|---|---|---|---|---|---|---|---|---|---|"]
        for R in CE.RUN10_R:
            c = _cell(R)
            sb = _strongest(base, c) if base else None
            r0 = base[(c, sb)]
            L0 = lat.get(f"run10.R{R}.D{CE.RUN10_DECOYS}", {}).get("total", {}).get("mean", float("nan"))
            lead0 = max(base[(c, v)]["dev_contribution"] for v in ORDER if v != "baseline")
            bp0 = max(ORDER, key=lambda v: base[(c, v)]["p_at_1"])
            md.append(f"| Run10 | {R} | {NAME[sb]} | {_pct(r0['dev_accuracy'])} | ×{r0['dev_lift_random']:.2f} "
                      f"[{r0['dev_lift_random_lo']:.2f}, {r0['dev_lift_random_hi']:.2f}] | {100 * lead0:+.2f} | reference | reference | "
                      f"{_pct(base[(c, bp0)]['p_at_1'], 1)} | {L0:.0f} s |")
            for b, label in group:
                rows, eff = _rows(out, b)
                if rows is None:
                    continue
                s = _strongest(rows, c)
                r = rows[(c, s)]
                lead = max(rows[(c, v)]["dev_contribution"] for v in ORDER if v != "baseline")
                e = eff.get("run10", {})
                eo = e.get(f"baseline.R{R:g}.D{CE.RUN10_DECOYS}", {}).get("dev")
                es = e.get(f"{sb}.R{R:g}.D{CE.RUN10_DECOYS}", {}).get("dev")
                fe = lambda x: "" if x is None else f"{100 * x['effect']:+.2f} [{100 * x['lo']:+.2f}, {100 * x['hi']:+.2f}]"
                bp = max(ORDER, key=lambda v: rows[(c, v)]["p_at_1"])
                L = lat.get(f"{b}.R{R}.D{CE.RUN10_DECOYS}", {}).get("total", {}).get("mean", float("nan"))
                md.append(f"| {label} | {R} | {NAME[s]} | {_pct(r['dev_accuracy'])} | ×{r['dev_lift_random']:.2f} "
                          f"[{r['dev_lift_random_lo']:.2f}, {r['dev_lift_random_hi']:.2f}] | {100 * lead:+.2f} | {fe(eo)} | {fe(es)} | "
                          f"{_pct(rows[(c, bp)]['p_at_1'], 1)} | {L:.0f} s |")
        md.append("")

    if pairs:
        md += ["## F and I submitting together", "", "| Build | R | Within 5 s at submission | Within 5 s as they leave |", "|---|---|---|---|"]
        for k, v in pairs.items():
            md.append(f"| {v['build']} | {v['R']} | {_pct(v['within5_at_submission'], 1)} | {_pct(v['within5_at_departure'], 1)} |")
        md.append("")
    (out / "RUN10_TABLES.md").write_text("\n".join(md), encoding="utf-8")
    if base:
        _figures(out, base)
    print(f"wrote {out / 'RUN10_TABLES.md'}", flush=True)


def _figures(out, base):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    (out / "figures").mkdir(parents=True, exist_ok=True)
    # 1. how often each component names the device, against chance, at each R
    f, axes = plt.subplots(1, len(CE.RUN10_R), figsize=(11, 3.8), dpi=200, sharey=False)
    for ax, R in zip(axes, CE.RUN10_R):
        c = _cell(R)
        acc = [100 * base[(c, v)]["dev_accuracy"] for v in ORDER]
        lo = [100 * (base[(c, v)]["dev_accuracy"] - base[(c, v)]["dev_ci_lo"]) for v in ORDER]
        hi = [100 * (base[(c, v)]["dev_ci_hi"] - base[(c, v)]["dev_accuracy"]) for v in ORDER]
        ax.barh(range(len(ORDER)), acc, xerr=[lo, hi], color="#2a78d6", alpha=0.85)
        ax.axvline(100 * base[(c, "baseline")]["dev_random"], color="#5f5e5a", linestyle=":", linewidth=1.2, label="chance (feasible set)")
        ax.set_yticks(range(len(ORDER)))
        ax.set_yticklabels([NAME[v] for v in ORDER] if R == CE.RUN10_R[0] else [], fontsize=7)
        ax.set_title(f"R = {R}, {CE.RUN10_DECOYS} decoys", fontsize=9)
        ax.set_xlabel("device named (%)", fontsize=8)
        ax.invert_yaxis()
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
    axes[0].legend(fontsize=7, frameon=False, loc="lower right")
    f.tight_layout()
    f.savefig(out / "figures" / "run10_device_named.png")
    plt.close(f)
    # 2. reliability of the adversary's confidence at R = 20
    c = _cell(20)
    f, ax = plt.subplots(figsize=(5, 4.2), dpi=200)
    for v in ORDER:
        rel = base[(c, v)]["reliability"]
        ax.plot([100 * x["conf"] for x in rel], [100 * x["hit"] for x in rel], marker="o", markersize=3, linewidth=1.2, label=NAME[v])
    top = max(100 * x["conf"] for v in ORDER for x in base[(c, v)]["reliability"]) * 1.1
    ax.plot([0, top], [0, top], color="#5f5e5a", linestyle=":", linewidth=1)
    ax.set_xlabel("component's confidence in its match (%)", fontsize=8)
    ax.set_ylabel("matches actually right (%)", fontsize=8)
    ax.set_title("R = 20: confidence against outcome, by decile", fontsize=9)
    ax.legend(fontsize=6, frameon=False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    f.tight_layout()
    f.savefig(out / "figures" / "run10_confidence_reliability.png")
    plt.close(f)

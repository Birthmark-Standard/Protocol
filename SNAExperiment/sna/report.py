"""Summaries, tables and figures from the per-decision records.

Per build: <out>/summary_<build>.json, summary_<build>.csv and tables_<build>.md. For the whole
experiment: <out>/TABLES.md and <out>/figures/*.png, read from the per-build summaries and the
latency, pair-timing and hold-timing files of the same output directory."""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

from . import analyze as AN
from . import attacks as AT
from . import experiment as EX
from . import runner as RN

ORDER = ("baseline", "first_hop_cred", "first_hop_content", "cred_processor", "validator", "gatekeeper",
         "content_server")
NAME = {"baseline": "Passive observer", "first_hop_cred": "First hop, credential", "first_hop_content": "First hop, content",
        "cred_processor": "Credential processor", "validator": "Validator", "gatekeeper": "Gatekeeper",
        "content_server": "Content server"}


def _pct(x, d=2):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{100 * x:.{d}f}%"


def _ci(r, k, lo, hi, d=2):
    return f"{_pct(r.get(k), d)} [{_pct(r.get(lo), d)}, {_pct(r.get(hi), d)}]"


# --------------------------------------------------------------------------- one build
def summarize(out: Path, build=EX.BASELINE):
    """Analyse one build's records and write its summary and tables."""
    out = Path(out)
    cells = {k: dict(v, build=build) for k, v in json.loads((out / "cells.json").read_text()).items()}
    refs = {} if build == EX.BASELINE else {EX.BASELINE: lambda k: RN.load(out, f"{k}__{EX.BASELINE}")}
    rows, changes = AN.analyze(cells, lambda k: RN.load(out, f"{k}__{build}"), references=refs)
    clean = [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]
    (out / f"summary_{build}.json").write_text(json.dumps(dict(build=build, rows=clean, paired_effects=changes),
                                                          indent=1, default=float))
    write_csv(out, build, clean)
    write_build_tables(out, build, clean, changes)
    print(f"wrote {out / f'summary_{build}.json'}, summary_{build}.csv and tables_{build}.md", flush=True)


def write_csv(out, build, rows):
    keys = sorted({k for r in rows for k in r if not isinstance(r[k], (dict, list))},
                  key=lambda k: (k not in ("cell", "vantage", "R", "T"), k))
    with open(Path(out) / f"summary_{build}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def _acc(r, lvl):
    s = _ci(r, f"{lvl}_accuracy", f"{lvl}_ci_lo", f"{lvl}_ci_hi")
    if lvl == "dev" and not r["stable"]:
        s += f" (unstable; {r['runs_needed']} runs needed)"
    return s


def write_build_tables(out, build, rows, changes):
    D = EX.calibrate(out)["D"]
    md = [f"# {EX.LABEL[build]}", "",
          f"Build `{build}`. Record-to-device linking with {EX.DECOYS} decoy transactions in flight; end-to-end delay "
          f"D = {D:.1f} s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the "
          "named device is the record's. Submission level: the named submission group contains a packet of the "
          "record's capture. Rows are real records only. The first hops and the credential processor are scored on "
          "every record.", ""]
    for name, ch in changes.items():
        if not ch:
            continue
        md += [f"## Paired against {EX.EXPERIMENT}", "",
               f"Accuracy under this build minus accuracy under {EX.EXPERIMENT}, matched record by record on identical "
               "traffic (percentage points).", "",
               "| Vantage | R | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |", "|---|---|---|---|---|"]
        for v in ORDER:
            for R in EX.REAL_R:
                e = ch.get(f"{v}.R{R:g}.D{EX.DECOYS:g}")
                if e:
                    md.append(f"| {NAME[v]} | {R} | {100 * e['dev']['effect']:+.2f} [{100 * e['dev']['lo']:+.2f}, "
                              f"{100 * e['dev']['hi']:+.2f}] | {100 * e['sub']['effect']:+.2f} [{100 * e['sub']['lo']:+.2f}, "
                              f"{100 * e['sub']['hi']:+.2f}] | {e['dev']['n']} |")
        md.append("")
    md += ["## Every cell", ""]
    for v in ORDER:
        md += [f"### {NAME[v]}", "",
               "| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | "
               "Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | "
               "AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |",
               "|" + "---|" * 15]
        for r in sorted((x for x in rows if x["vantage"] == v), key=lambda x: x["R"]):
            if "dev_accuracy" not in r:
                continue
            md.append(f"| {r['R']:g} | {_acc(r, 'dev')} | {_pct(r['dev_random'])} | {_pct(r['dev_baseline'])} | "
                      f"{_ci(r, 'dev_contribution', 'dev_contribution_lo', 'dev_contribution_hi')} | {_acc(r, 'sub')} | "
                      f"{_pct(1 / r['T'])} | {_pct(r['sub_baseline'])} | "
                      f"{_ci(r, 'sub_contribution', 'sub_contribution_lo', 'sub_contribution_hi')} | "
                      f"{r['auc']:.3f} [{r['auc_lo']:.3f}, {r['auc_hi']:.3f}] | {_pct(r['p_at_1'], 1)} | "
                      f"{_pct(r['p_at_5'], 1)} | {_pct(r['coverage_p50'], 3)} | {r['runs']} | {r['n']} |")
        md.append("")
    st = [r for r in rows if r.get("stable")]
    bad = [r for r in st if not (r["shuffle_auc_lo"] <= 0.5 <= r["shuffle_auc_hi"])]
    md += ["## Outcome-shuffle control", "",
           f"{len(st)} stable rows; {len(bad)} with a shuffled-outcome AUC interval excluding 0.5"
           + ("" if not bad else ": " + ", ".join(f"R = {r['R']:g} {NAME[r['vantage']]} ({r['shuffle_auc']:.3f})" for r in bad))
           + ".", ""]
    (Path(out) / f"tables_{build}.md").write_text("\n".join(md), encoding="utf-8")


def tables_from_summaries(out):
    """Rewrite every build's CSV and tables from its summary JSON, then TABLES.md and the figures."""
    out = Path(out)
    for b in EX.BUILDS:
        p = out / f"summary_{b}.json"
        if p.exists():
            d = json.loads(p.read_text())
            write_csv(out, b, d["rows"])
            write_build_tables(out, b, d["rows"], d.get("paired_effects", {}))
    write_tables(out)


# --------------------------------------------------------------------------- the whole experiment
def _rows(out, build):
    p = Path(out) / f"summary_{build}.json"
    if not p.exists():
        return None, None
    d = json.loads(p.read_text())
    return {(r["cell"], r["vantage"]): r for r in d["rows"]}, d.get("paired_effects", {})


def _strongest(rows, c):
    return max(ORDER, key=lambda v: rows[(c, v)]["dev_accuracy"])


def claim_holds(rows, c):
    """The claim criterion in one cell: for every component, the upper bound of the 95% interval on
    the precision of its most confident 1% of matches is below 50%, and fewer than 0.1% of its
    matches fall in a most-confident set that is right more than half the time."""
    return all(rows[(c, v)]["p_at_1_hi"] < 0.5 and rows[(c, v)]["coverage_p50"] < 0.001 for v in ORDER)


def write_tables(out):
    out = Path(out)
    D = EX.calibrate(out)["D"]
    lat = json.loads((out / "latency.json").read_text())["cells"] if (out / "latency.json").exists() else {}
    timing = json.loads((out / "timing_check.json").read_text())["builds"] if (out / "timing_check.json").exists() else {}
    pairs = json.loads((out / "pair_gaps.json").read_text())["cells"] if (out / "pair_gaps.json").exists() else {}
    base, _ = _rows(out, EX.BASELINE)
    B = EX.BASELINE
    md = [f"# {EX.EXPERIMENT} tables", "",
          f"End-to-end delay under {EX.EXPERIMENT}: D = {D:.1f} s; rates are R / D and {EX.DECOYS} / D, so R real and "
          f"{EX.DECOYS} decoy transactions are in flight. Device level: the vantage names the device behind a registry "
          "record. Intervals are 95%, resampling whole runs.", ""]

    if B in timing:
        md += ["## Timing as simulated (R = 20)", "", "| Stage | Mean | Std dev | Maximum |", "|---|---|---|---|"]
        for name, v in timing[B]["stages"].items():
            md.append(f"| {name} | {v['mean']:.1f} s | {v['sd']:.1f} s | {v['max']:.1f} s |")
        bd = timing[B]["bundle"]
        md += ["", f"Postings per departure bundle at one gatekeeper: mean {bd['mean']:.2f}; "
               f"{_pct(bd['p_lt2'], 1)} of bundles hold fewer than two; {_pct(bd['p_empty'], 1)} are empty.", ""]

    if base:
        md += [f"## The adversary against {EX.EXPERIMENT}", "",
               "For each single compromised component: how often it names the right device, against two chance "
               "rates (a guess among the devices that could have produced the record, and a guess among every "
               "registered device), its lead over a passive observer, and its own confidence that a match is right.", ""]
        for R in EX.REAL_R:
            c = EX.cell_key(R)
            cfg = EX.config_of(dict(R=float(R), decoys=float(EX.DECOYS)), D)
            N = cfg.real_devices + cfg.decoy_sources
            md += [f"### R = {R}, {EX.DECOYS} decoys ({N} registered devices; one in {N} is {_pct(1 / N)})", "",
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
            L = lat.get(f"{B}.R{R}.D{EX.DECOYS}", {}).get("total", {})
            md += ["", f"Claim criterion: **{'pass' if claim_holds(base, c) else 'fail'}**. Mean capture to finalization: "
                   f"{L.get('mean', float('nan')):.0f} s (median {L.get('median', float('nan')):.0f} s, 95th percentile "
                   f"{L.get('p95', float('nan')):.0f} s).", ""]

        md += ["## Reliability of the adversary's confidence (R = 20)", "",
               "Matches sorted into ten equal groups by the component's own calibrated confidence; each row compares "
               "the group's mean confidence with how often its matches were right.", "",
               "| Component | Lowest decile: confidence / right | Median decile | Highest decile | Mean absolute gap |",
               "|---|---|---|---|---|"]
        c = EX.cell_key(20)
        for v in ORDER:
            rel = base[(c, v)]["reliability"]
            f = lambda x: f"{_pct(x['conf'], 1)} / {_pct(x['hit'], 1)}"  # noqa: E731
            md.append(f"| {NAME[v]} | {f(rel[0])} | {f(rel[len(rel) // 2])} | {f(rel[-1])} | "
                      f"{base[(c, v)]['calibration_error'] * 100:.2f} points |")
        md.append("")

        for title, group in ((f"What each mechanism contributes: {EX.EXPERIMENT} with one mechanism removed", EX.REMOVALS),
                             (f"Alternative settings", EX.ALTERNATIVES)):
            md += [f"## {title}", "",
                   f"Paired against {EX.EXPERIMENT} on the same records (the effect is the build minus {EX.EXPERIMENT}, "
                   "in points).", "",
                   "| Build | R | Strongest component | Device named | Multiple of chance [95% CI] | Largest lead over observer "
                   f"| Observer: effect [95% CI] | Strongest {EX.EXPERIMENT} component: effect [95% CI] | Top 1% right, best component "
                   "| Mean latency |", "|---|---|---|---|---|---|---|---|---|---|"]
            for R in EX.REAL_R:
                c = EX.cell_key(R)
                sb = _strongest(base, c)
                r0 = base[(c, sb)]
                L0 = lat.get(f"{B}.R{R}.D{EX.DECOYS}", {}).get("total", {}).get("mean", float("nan"))
                lead0 = max(base[(c, v)]["dev_contribution"] for v in ORDER if v != "baseline")
                bp0 = max(ORDER, key=lambda v: base[(c, v)]["p_at_1"])
                md.append(f"| {EX.EXPERIMENT} | {R} | {NAME[sb]} | {_pct(r0['dev_accuracy'])} | ×{r0['dev_lift_random']:.2f} "
                          f"[{r0['dev_lift_random_lo']:.2f}, {r0['dev_lift_random_hi']:.2f}] | {100 * lead0:+.2f} | reference | reference | "
                          f"{_pct(base[(c, bp0)]['p_at_1'], 1)} | {L0:.0f} s |")
                for b in group:
                    rows, eff = _rows(out, b)
                    if rows is None:
                        continue
                    s = _strongest(rows, c)
                    r = rows[(c, s)]
                    lead = max(rows[(c, v)]["dev_contribution"] for v in ORDER if v != "baseline")
                    e = eff.get(B, {})
                    eo = e.get(f"baseline.R{R:g}.D{EX.DECOYS}", {}).get("dev")
                    es = e.get(f"{sb}.R{R:g}.D{EX.DECOYS}", {}).get("dev")
                    fe = lambda x: "" if x is None else f"{100 * x['effect']:+.2f} [{100 * x['lo']:+.2f}, {100 * x['hi']:+.2f}]"  # noqa: E731
                    bp = max(ORDER, key=lambda v: rows[(c, v)]["p_at_1"])
                    L = lat.get(f"{b}.R{R}.D{EX.DECOYS}", {}).get("total", {}).get("mean", float("nan"))
                    md.append(f"| {EX.LABEL[b]} | {R} | {NAME[s]} | {_pct(r['dev_accuracy'])} | ×{r['dev_lift_random']:.2f} "
                              f"[{r['dev_lift_random_lo']:.2f}, {r['dev_lift_random_hi']:.2f}] | {100 * lead:+.2f} | {fe(eo)} | {fe(es)} | "
                              f"{_pct(rows[(c, bp)]['p_at_1'], 1)} | {L:.0f} s |")
            md.append("")

    if pairs:
        md += ["## F and I submitting together", "", "| Build | R | Within 5 s at submission | Within 5 s as they leave |",
               "|---|---|---|---|"]
        for v in pairs.values():
            md.append(f"| {EX.LABEL[v['build']]} | {v['R']} | {_pct(v['within5_at_submission'], 1)} | "
                      f"{_pct(v['within5_at_departure'], 1)} |")
        md.append("")
    (out / "TABLES.md").write_text("\n".join(md), encoding="utf-8")
    if base:
        figures(out, base, lat)
    print(f"wrote {out / 'TABLES.md'} and figures/", flush=True)


def figures(out, base, lat):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    out = Path(out)
    (out / "figures").mkdir(parents=True, exist_ok=True)
    # 1. how often each component names the device, against chance, at each R
    f, axes = plt.subplots(1, len(EX.REAL_R), figsize=(11, 3.8), dpi=200, sharey=False)
    for ax, R in zip(axes, EX.REAL_R):
        c = EX.cell_key(R)
        acc = [100 * base[(c, v)]["dev_accuracy"] for v in ORDER]
        lo = [100 * (base[(c, v)]["dev_accuracy"] - base[(c, v)]["dev_ci_lo"]) for v in ORDER]
        hi = [100 * (base[(c, v)]["dev_ci_hi"] - base[(c, v)]["dev_accuracy"]) for v in ORDER]
        ax.barh(range(len(ORDER)), acc, xerr=[lo, hi], color="#2a78d6", alpha=0.85)
        ax.axvline(100 * base[(c, "baseline")]["dev_random"], color="#5f5e5a", linestyle=":", linewidth=1.2,
                   label="chance (feasible set)")
        ax.set_yticks(range(len(ORDER)))
        ax.set_yticklabels([NAME[v] for v in ORDER] if R == EX.REAL_R[0] else [], fontsize=7)
        ax.set_title(f"R = {R}, {EX.DECOYS} decoys", fontsize=9)
        ax.set_xlabel("device named (%)", fontsize=8)
        ax.invert_yaxis()
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
    axes[0].legend(fontsize=7, frameon=False, loc="lower right")
    f.tight_layout()
    f.savefig(out / "figures" / "device_named.png")
    plt.close(f)
    # 2. reliability of the adversary's confidence at R = 20
    c = EX.cell_key(20)
    f, ax = plt.subplots(figsize=(5, 4.2), dpi=200)
    for v in ORDER:
        rel = base[(c, v)]["reliability"]
        ax.plot([100 * x["conf"] for x in rel], [100 * x["hit"] for x in rel], marker="o", markersize=3, linewidth=1.2,
                label=NAME[v])
    top = max(100 * x["conf"] for v in ORDER for x in base[(c, v)]["reliability"]) * 1.1
    ax.plot([0, top], [0, top], color="#5f5e5a", linestyle=":", linewidth=1)
    ax.set_xlabel("component's confidence in its match (%)", fontsize=8)
    ax.set_ylabel("matches actually right (%)", fontsize=8)
    ax.set_title("R = 20: confidence against outcome, by decile", fontsize=9)
    ax.legend(fontsize=6, frameon=False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    f.tight_layout()
    f.savefig(out / "figures" / "confidence_reliability.png")
    plt.close(f)
    # 3. capture-to-finalization time under each build, R = 1
    if lat:
        f, ax = plt.subplots(figsize=(7, 3.6), dpi=300, facecolor="#fcfcfb")
        ax.set_facecolor("#fcfcfb")
        cmap = plt.get_cmap("viridis")
        builds = [b for b in EX.BUILDS if f"{b}.R1.D{EX.DECOYS}" in lat]
        for j, b in enumerate(builds):
            h = np.array(lat[f"{b}.R1.D{EX.DECOYS}"]["hist10"], float)
            x = np.arange(h.size) * 10 + 5
            ax.plot(x, 100 * h / h.sum(), color=cmap(j / max(len(builds) - 1, 1) * 0.85), linewidth=1.4,
                    label=EX.LABEL[b])
        ax.set_xlim(0, 2400)
        ax.set_xlabel("capture to registry finalization (s)", fontsize=8)
        ax.set_ylabel("share of real transactions per 10 s (%)", fontsize=8)
        ax.set_title(f"R = 1, {EX.DECOYS} decoys in flight", fontsize=9)
        ax.legend(fontsize=5.5, frameon=False)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        f.tight_layout()
        f.savefig(out / "figures" / "latency_by_build.png", facecolor="#fcfcfb")
        plt.close(f)

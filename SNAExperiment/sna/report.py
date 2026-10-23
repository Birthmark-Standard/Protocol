"""Analysis of the run's per-decision records, and every file in results/.

results/summary.json, summary.csv   every row of the main configuration
results/controls/                   each control's rows, the shuffle test, the intended-path shares
results/timing.json                 every stage's delay, capture to finalization, packet-type delays
results/run_info.json               seeds, runs per cell, D, the calibration and the in-flight counts
results/TABLES.md, PAPER_TABLE.md   the tables
results/figures/                    the figures
"""
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

# (row name, table, took_part column) for the vantages scored on every record or on their own records
VANTAGES = (("Passive observer", "observer", None), ("First hop, credential", "first_hop", "took_part_A"),
            ("First hop, content", "first_hop", "took_part_DG"), ("Credential processor", "cred_processor", "took_part"),
            ("Validator", "validator", None), ("Gatekeeper", "gatekeeper", None),
            ("Content server", "content_server", None), ("Combined", "combined", "took_part"))
NODE_TABLES = ("first_hop", "cred_processor", "gatekeeper", "content_server", "combined")
SHUFFLED = ("observer", "first_hop", "cred_processor", "validator", "gatekeeper", "content_server", "combined")


def _spec(R):
    return dict(key=EX.cell_key(R), R=float(R), T=float(R + EX.DECOYS))


def _table(recs, v, took=None, sel=None):
    t = AN.stack(recs, v)
    if took is not None:
        t["took_part"] = t[took]
    elif "took_part" in t and v != "cred_processor" and v != "combined":
        del t["took_part"]
    if sel is not None:
        m = sel(t)
        t = {k: x[m] for k, x in t.items()}
    return t


def _acc(c, run, rng):
    num, den = AN.per_run(np.asarray(c, float), run)
    return AN.cluster_boot(num, den, rng)


def _clean(r):
    return {k: v for k, v in r.items() if not k.startswith("_")}


# --------------------------------------------------------------------------- analysis of one configuration
def analyze_config(out, name, seed=12345):
    """Every row of one configuration: each vantage on all its records; each node vantage on the records in
    which the node held no coincident role; the combined view by the roles the node held; the label
    shuffle of every vantage; and the diagnostics."""
    rng = np.random.default_rng(seed)
    rows, shuffle, diag, stats = [], [], [], {}
    for R in EX.REAL_R:
        recs = sorted(RN.load(out, EX.rec_name(name, R)), key=lambda r: r["run"])
        if not recs:
            continue
        spec = _spec(R)
        base = dict(config=name, cell=spec["key"], R=R)
        for label, v, took in VANTAGES:
            t = _table(recs, v, took)
            r = AN.metrics(recs, v, spec, rng, t=t, name=label)
            rows.append(dict(base, **_clean(r), subset="all records"))
            if v in NODE_TABLES and v != "combined":
                tn = _table(recs, v, took, sel=lambda t: t["nroles"] <= 1)
                r = AN.metrics(recs, v, spec, rng, t=tn, name=label)
                rows.append(dict(base, **_clean(r), subset="no coincident role", prevalence=float(tn["sub"].size / max(t["sub"].size, 1))))
        tc = _table(recs, "combined", "took_part")
        ident = [AT.PAIR_CODE[c] for c in AT.IDENTIFIABLE]
        first = [AT.PAIR_CODE[c] for c in AT.PAIR_CLASSES if "first relay" in c]
        subsets = [(c, c in AT.IDENTIFIABLE, tc["pair"] == AT.PAIR_CODE[c]) for c in AT.PAIR_CLASSES]
        subsets += [("every record the node can select", None, np.isin(tc["pair"], ident)),
                    ("first relay held", None, np.isin(tc["pair"], first)),
                    ("no first relay held", None, ~np.isin(tc["pair"], first))]
        for cls, identifiable, sel in subsets:
            if not sel.any():
                continue
            r = AN.metrics(recs, "combined", spec, rng, t={k: x[sel] for k, x in tc.items()}, name="Combined")
            rows.append(dict(base, **_clean(r), subset=cls, identifiable=identifiable, prevalence=float(sel.mean())))
        # first relays by path: the first-hop vantage on the records whose transaction it relayed as A, D or G
        tf = AN.stack(recs, "first_hop")
        for path, col in (("A", "took_part_A"), ("D or G", "took_part_DG")):
            m = tf[col].astype(bool)
            lead, lo, hi = _acc(tf["dev_v_correct"][m].astype(float) - tf["dev_b_correct"][m], tf["run"][m], rng)
            diag.append(dict(base, kind="first relay by path", path=path, lead=lead, lo=lo, hi=hi, n=int(m.sum()),
                             accuracy=float(tf["dev_v_correct"][m].mean()) if m.any() else math.nan,
                             observer=float(tf["dev_b_correct"][m].mean()) if m.any() else math.nan))
        # the label shuffle
        for label, v, _ in VANTAGES:
            if label == "First hop, content":
                continue
            t = AN.stack(recs, v)
            a, lo, hi = _acc(t["dev_s_correct"], t["run"], rng)
            chance = float(t["dev_s_rand"].sum() / t["dev_s_rand"].size)
            shuffle.append(dict(base, vantage=label.replace("First hop, credential", "First hop"), accuracy=a, lo=lo, hi=hi,
                                chance=chance, n=int(t["sub"].size), passed=bool(lo <= chance <= hi)))
        # diagnostics on the same traffic
        to = AN.stack(recs, "observer")
        for v, label in (("observer_flat", "observer, timing evidence off"), ("observer_mid", "observer, record time at the midpoint"),
                         ("content_server_mid", "content server, record time at the midpoint")):
            t = AN.stack(recs, v)
            a, lo, hi = _acc(t["dev_v_correct"], t["run"], rng)
            ch = float(t["dev_v_rand"].mean())
            ref = "observer" if v != "content_server_mid" else "content_server"
            tr = AN.stack(recs, ref)
            ar, rlo, rhi = _acc(tr["dev_v_correct"], tr["run"], rng)
            d, dlo, dhi = _acc(t["dev_v_correct"].astype(float) - tr["dev_v_correct"], t["run"], rng) if v != "observer_flat" else (math.nan,) * 3
            diag.append(dict(base, kind=label, accuracy=a, lo=lo, hi=hi, chance=ch, multiple=a / ch if ch else math.nan,
                             posted=ar, posted_lo=rlo, posted_hi=rhi, change=d, change_lo=dlo, change_hi=dhi, n=int(t["sub"].size)))
        # the observer in the first and the second half of the window
        h = to["half"].astype(bool)
        parts = {}
        for part, sel in (("first half", ~h), ("second half", h)):
            parts[part] = _acc(to["dev_v_correct"][sel], to["run"][sel], rng)
        num1, den1 = AN.per_run(to["dev_v_correct"][~h].astype(float), to["run"][~h])
        num2, den2 = AN.per_run(to["dev_v_correct"][h].astype(float), to["run"][h])
        idx = rng.integers(0, num1.size, (AN.BOOT, num1.size))
        dif = num2[idx].sum(1) / den2[idx].sum(1) - num1[idx].sum(1) / den1[idx].sum(1)
        d0 = num2.sum() / den2.sum() - num1.sum() / den1.sum()
        dlo, dhi = np.percentile(dif, (2.5, 97.5))
        diag.append(dict(base, kind="observer by half of the window", first=parts["first half"], second=parts["second half"],
                         change=float(d0), change_lo=float(dlo), change_hi=float(dhi), agree=bool(dlo <= 0 <= dhi),
                         n_first=int((~h).sum()), n_second=int(h.sum())))
        for k, pt in enumerate(AT.PTYPES):
            a, lo, hi = _acc(to["hit_type"] == k, to["run"], rng)
            rnd = float(np.where(to["sub_n_feas"] > 0, to["tfeas"][:, k] / np.maximum(to["sub_n_feas"], 1), 0.0).mean())
            diag.append(dict(base, kind="observer submission hit by packet type", packet=pt, accuracy=a, lo=lo, hi=hi,
                             random=rnd, n=int(to["sub"].size)))
        stats[spec["key"]] = _run_stats(recs, rng)
        if name == EX.MAIN:
            stats[spec["key"]]["shuffle_test"] = _shuffle_test(recs, rng)
    return rows, shuffle, diag, stats


def _run_stats(recs, rng):
    st = [r["stats"] for r in recs]
    out = dict(runs=len(recs), real_in_flight=float(np.mean([s["real_in_flight"] for s in st])),
               decoys_in_flight=float(np.mean([s["decoys_in_flight"] for s in st])),
               board_share=float(sum(s["board"] for s in st) / max(sum(s["confirmations"] for s in st), 1)),
               f_path_share=float(sum(s["f_path"] for s in st) / max(sum(s["records"] for s in st), 1)),
               sim_seconds=float(np.mean([r["sim_seconds"] for r in recs])),
               score_seconds=float(np.mean([r["score_seconds"] for r in recs])),
               test_seconds=float(np.mean([r.get("test_seconds", 0.0) for r in recs])),
               unfinalized=int(sum(s["unfinalized"] for s in st)), introduced=int(sum(s["introduced"] for s in st)))
    out["content_share"] = 1.0 - out["board_share"]
    for key in ("stages", "packet_delay", "path_delay"):
        acc = {}
        for s in st:
            for k, (n, sm, sq, mx) in s[key].items():
                a = acc.setdefault(k, [0, 0.0, 0.0, 0.0])
                a[0] += n
                a[1] += sm
                a[2] += sq
                a[3] = max(a[3], mx)
        out[key] = {k: dict(mean=a[1] / a[0], sd=math.sqrt(max(a[2] / a[0] - (a[1] / a[0]) ** 2, 0.0)), max=a[3], n=a[0])
                    for k, a in acc.items() if a[0]}
    # capture to finalization: run-resampled interval on the mean
    lat = [s["stages"]["capture to finalization"] for s in st]
    m, lo, hi = AN.cluster_boot(np.array([x[1] for x in lat]), np.array([x[0] for x in lat], float), rng)
    out["latency"] = dict(mean=m, lo=lo, hi=hi)
    h = np.sum([s["latency_hist"] for s in st], axis=0)
    out["latency_hist10"] = h.tolist()
    return out


def _shuffle_test(recs, rng, reps=500):
    """Where a shortfall of the shuffled observer below chance would come from: the shuffle itself
    (shuffled picks that are not the permuted unshuffled picks), the feasible set (changed feasible
    counts, or a chance rate that does not average to its exact expectation), or the estimator (the
    spread of the run-resampled estimate across permutations, and how often its interval covers the
    exact expectation)."""
    x = [r["shuffle_test"] for r in recs]
    n = np.array([a["n"] for a in x], float)
    N = n.sum()
    ck = np.stack([a["correct_k"] for a in x]).astype(float)       # runs x K
    chk = np.stack([a["chance_k"] for a in x])
    exact_c, exact_ch = sum(a["exact_correct"] for a in x) / N, sum(a["exact_chance"] for a in x) / N
    est = ck.sum(0) / N
    cover = 0
    idx = rng.integers(0, n.size, (reps, n.size))
    for k in range(ck.shape[1]):
        b = ck[idx, k].sum(1) / n[idx].sum(1)
        lo, hi = np.percentile(b, (2.5, 97.5))
        cover += int(lo <= exact_c <= hi)
    real = sum(a["correct"] for a in x) / N
    return dict(records=int(N), runs=len(x), labels_mean=float(np.mean([a["L"] for a in x])),
                shuffle_mismatches=int(sum(a["shuffle_mismatch"] for a in x)),
                scored_equals_derived=bool(all(a["scored_correct"] == a["correct"] for a in x)),
                feasible_count_mismatches=int(sum(a["nfeas_mismatch"] for a in x)),
                exact_accuracy=exact_c, exact_chance=exact_ch,
                mean_accuracy_over_permutations=float(est.mean()), mean_chance_over_permutations=float(chk.sum(0).mean() / N),
                sd_accuracy_over_permutations=float(est.std()), permutations=int(ck.shape[1]),
                interval_coverage=cover / ck.shape[1], scored_accuracy=real,
                scored_chance=float(sum(a["chance"] for a in x) / N),
                scored_percentile=float((est < real).mean()))


# --------------------------------------------------------------------------- formatting
def _pct(x, d=2):
    return "n/a" if x is None or (isinstance(x, float) and not math.isfinite(x)) else f"{100 * x:.{d}f}%"


def _pts(x, lo, hi):
    return "n/a" if not math.isfinite(x) else f"{100 * x:+.2f} [{100 * lo:+.2f}, {100 * hi:+.2f}]"


def _claim(r):
    if not r.get("stable"):
        return f"unstable ({r.get('runs_needed')} runs needed)"
    return "pass" if r["claim"] else "fail"


def _vantage_table(rows, cell, subset="all records", names=None):
    md = ["| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] "
          "| Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["cell"] != cell or r["subset"] != subset or (names and r["vantage"] not in names):
            continue
        if r["vantage"] == "Combined" and subset == "all records" and names is None:
            pass
        lead = "reference" if r["vantage"] == "Passive observer" else _pts(r["dev_contribution"], r["dev_contribution_lo"], r["dev_contribution_hi"])
        if not r.get("stable"):
            md.append(f"| {r['vantage']} | unstable | {_pct(r['dev_random'])} | | | {r['n']:,} | | | {_claim(r)} |")
            continue
        md.append(f"| {r['vantage']} | {_pct(r['dev_accuracy'])} [{_pct(r['dev_ci_lo'])}, {_pct(r['dev_ci_hi'])}] | "
                  f"{_pct(r['dev_random'])} | ×{r['dev_lift_random']:.2f} [{r['dev_lift_random_lo']:.2f}, {r['dev_lift_random_hi']:.2f}] | "
                  f"{lead} | {r['n']:,} | {_pct(r['p_at_1_hi'], 1)} | {_pct(r['coverage_p50'], 3)} | {_claim(r)} |")
    return md


def _class_table(rows, cell):
    md = ["| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | "
          "Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["cell"] != cell or r["vantage"] != "Combined" or r["subset"] == "all records":
            continue
        idf = {True: "yes", False: "no", None: ""}[r.get("identifiable")]
        if not r.get("stable"):
            md.append(f"| {r['subset']} | {idf} | {_pct(r.get('prevalence'))} | unstable | {_pct(r['dev_random'])} | | | "
                      f"{r['n']:,} | | | {_claim(r)} |")
            continue
        md.append(f"| {r['subset']} | {idf} | {_pct(r.get('prevalence'))} | {_pct(r['dev_accuracy'])} [{_pct(r['dev_ci_lo'])}, "
                  f"{_pct(r['dev_ci_hi'])}] | {_pct(r['dev_random'])} | ×{r['dev_lift_random']:.2f} | "
                  f"{_pts(r['dev_contribution'], r['dev_contribution_lo'], r['dev_contribution_hi'])} | {r['n']:,} | "
                  f"{_pct(r['p_at_1_hi'], 1)} | {_pct(r['coverage_p50'], 3)} | {_claim(r)} |")
    return md


def write_csv(path, rows):
    keys = sorted({k for r in rows for k in r if not isinstance(r[k], (dict, list))},
                  key=lambda k: (k not in ("config", "cell", "R", "vantage", "subset"), k))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def _dump(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=1, default=float))


# --------------------------------------------------------------------------- every file in results/
def write_all(out, run_info):
    out = Path(out)
    res = {name: analyze_config(out, name) for name in EX.CONFIGS}
    rows, shuffle, diag, stats = res[EX.MAIN]
    _dump(out / "summary.json", dict(rows=rows, shuffle=shuffle, diagnostics=diag))
    write_csv(out / "summary.csv", rows)
    for c in EX.CONTROLS:
        cr, cs, cd, cst = res[c]
        _dump(out / "controls" / f"{c}.json", dict(rows=cr, shuffle=cs, diagnostics=cd, stats=cst))
        write_csv(out / "controls" / f"{c}.csv", cr)
    _dump(out / "controls" / "shuffle_test.json", {k: v["shuffle_test"] for k, v in stats.items()})
    timing = {name: {cell: {k: v for k, v in s.items() if k not in ("shuffle_test",)} for cell, s in res[name][3].items()}
              for name in EX.CONFIGS}
    _dump(out / "timing.json", timing)
    run_info["in_flight"] = {name: {cell: dict(real=s["real_in_flight"], target_real=float(cell.split("_")[0][1:]),
                                               decoys=s["decoys_in_flight"], target_decoys=EX.DECOYS, runs=s["runs"])
                                    for cell, s in res[name][3].items()} for name in EX.CONFIGS}
    run_info["cost"] = {name: {cell: dict(sim_seconds=s["sim_seconds"], score_seconds=s["score_seconds"],
                                          test_seconds=s["test_seconds"]) for cell, s in res[name][3].items()}
                        for name in EX.CONFIGS}
    _dump(out / "run_info.json", run_info)
    write_tables(out, res, run_info)
    figures(out, rows, stats)
    print(f"wrote {out}/summary.json, summary.csv, TABLES.md, PAPER_TABLE.md, controls/, figures/, timing.json, run_info.json",
          flush=True)


def write_tables(out, res, info):
    rows, shuffle, diag, stats = res[EX.MAIN]
    cells = [EX.cell_key(R) for R in EX.REAL_R if EX.cell_key(R) in stats]
    D = info["D"][EX.MAIN]
    md = ["# Tables", "",
          f"Main run: D = {D:.1f} s; rates are R / D and {EX.DECOYS} / D. Intervals are 95% and resample whole runs. "
          "Device named: the vantage names the device behind a registry record. Chance, feasible set: a uniform guess "
          "among the devices whose packets could have produced the record. A row with fewer than 50 right or 50 wrong "
          "device-level decisions is unstable and shows no estimate.", "",
          "## In flight", "", "| Configuration | Cell | Real in flight (target) | Decoys in flight (target) | Runs |", "|---|---|---|---|---|"]
    for name, x in info["in_flight"].items():
        for cell, v in x.items():
            md.append(f"| {EX.LABEL[name]} | {cell} | {v['real']:.2f} ({v['target_real']:g}) | {v['decoys']:.2f} ({v['target_decoys']}) | {v['runs']} |")
    md += ["", "## Timing (main run, R = 100)", "", "| Stage | Mean | Std dev | Maximum |", "|---|---|---|---|"]
    st = stats.get(EX.cell_key(100), {})
    for k, v in st.get("stages", {}).items():
        md.append(f"| {k} | {v['mean']:.1f} s | {v['sd']:.1f} s | {v['max']:.1f} s |")
    md += ["", "| Cell | Mean capture to finalization [95% CI] |", "|---|---|"]
    for c in cells:
        L = stats[c]["latency"]
        md.append(f"| {c} | {L['mean']:.1f} s [{L['lo']:.1f}, {L['hi']:.1f}] |")
    md.append("")
    for c in cells:
        md += [f"## {c}: every vantage on all its records", ""] + _vantage_table(rows, c) + [""]
        md += [f"### {c}: each node vantage on the records in which the node held no coincident role", ""]
        md += _vantage_table(rows, c, subset="no coincident role") + [""]
        md += [f"### {c}: the combined view by the roles the node held", ""] + _class_table(rows, c) + [""]
    md += ["## Diagnostics", "", "| Cell | Variant | Device named [95% CI] | Chance | Multiple of chance | Posted-time number [95% CI] "
           "| Change [95% CI] |", "|---|---|---|---|---|---|---|"]
    for d in diag:
        if d["kind"].startswith(("observer, ", "content server, ")):
            md.append(f"| {d['cell']} | {d['kind']} | {_pct(d['accuracy'])} [{_pct(d['lo'])}, {_pct(d['hi'])}] | {_pct(d['chance'])} | "
                      f"×{d['multiple']:.2f} | {_pct(d['posted'])} [{_pct(d['posted_lo'])}, {_pct(d['posted_hi'])}] | "
                      f"{_pts(d['change'], d['change_lo'], d['change_hi'])} |")
    md += ["", "| Cell | Packet type | Observer submission hit [95% CI] | Random rate | Delay to record time, mean | Std dev |",
           "|---|---|---|---|---|---|"]
    for d in diag:
        if d["kind"] == "observer submission hit by packet type":
            pd = stats[d["cell"]]["packet_delay"][d["packet"]]
            md.append(f"| {d['cell']} | {d['packet']} | {_pct(d['accuracy'])} [{_pct(d['lo'])}, {_pct(d['hi'])}] | "
                      f"{_pct(d['random'])} | {pd['mean']:.1f} s | {pd['sd']:.1f} s |")
    md += ["", "| Cell | Packet | Departure to arrival at its destination, mean | Std dev |", "|---|---|---|---|"]
    for c in cells:
        for pt, v in stats[c]["path_delay"].items():
            dest = {"credential": "C", "F content": "F", "I content": "I"}[pt]
            md.append(f"| {c} | {pt} (at {dest}) | {v['mean']:.1f} s | {v['sd']:.1f} s |")
    md += ["", "| Cell | Observer, first half of the window [95% CI] | Second half [95% CI] | Second minus first [95% CI] | Agree |",
           "|---|---|---|---|---|"]
    for d in diag:
        if d["kind"] == "observer by half of the window":
            f, g = d["first"], d["second"]
            md.append(f"| {d['cell']} | {_pct(f[0])} [{_pct(f[1])}, {_pct(f[2])}] | {_pct(g[0])} [{_pct(g[1])}, {_pct(g[2])}] | "
                      f"{_pts(d['change'], d['change_lo'], d['change_hi'])} | {'yes' if d['agree'] else 'no'} |")
    md += ["", "| Configuration | Cell | Real transactions introduced in the window | Never finalized (quorum timeout) |", "|---|---|---|---|"]
    for name in EX.CONFIGS:
        for c, v in res[name][3].items():
            md.append(f"| {EX.LABEL[name]} | {c} | {v['introduced']:,} | {v['unfinalized']:,} |")
    md += ["", "| Cell | F and I confirmations set by the match board |", "|---|---|"]
    for c in cells:
        md.append(f"| {c} | {_pct(stats[c]['board_share'], 1)} |")
    md += ["", "## Label shuffle", "", "| Configuration | Cell | Vantage | Shuffled accuracy [95% CI] | Chance | Pass |",
           "|---|---|---|---|---|---|"]
    for name in EX.CONFIGS:
        for s in res[name][1]:
            md.append(f"| {EX.LABEL[name]} | {s['cell']} | {s['vantage']} | {_pct(s['accuracy'])} [{_pct(s['lo'])}, {_pct(s['hi'])}] | "
                      f"{_pct(s['chance'])} | {'pass' if s['passed'] else 'fail'} |")
    md += ["", "### Shuffle test (observer)", "",
           "| Cell | Shuffle mismatches | Feasible-count mismatches | Exact expected accuracy | Exact expected chance | "
           "Mean accuracy over permutations (sd) | Mean chance over permutations | Interval coverage | Scored accuracy | Scored percentile |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for c in cells:
        t = stats[c]["shuffle_test"]
        md.append(f"| {c} | {t['shuffle_mismatches']} | {t['feasible_count_mismatches']} | {_pct(t['exact_accuracy'], 3)} | "
                  f"{_pct(t['exact_chance'], 3)} | {_pct(t['mean_accuracy_over_permutations'], 3)} ({_pct(t['sd_accuracy_over_permutations'], 3)}) | "
                  f"{_pct(t['mean_chance_over_permutations'], 3)} | {_pct(t['interval_coverage'], 1)} | {_pct(t['scored_accuracy'], 3)} | "
                  f"{_pct(t['scored_percentile'], 1)} |")
    md += ["", "## Controls", ""]
    for name in EX.CONTROLS:
        cr, cs, cd, cst = res[name]
        md += [f"### {EX.LABEL[name]}", ""]
        if name in EX.INTENDED:
            key = dict(board="board_share", content="content_share", f_path="f_path_share")[EX.INTENDED[name]]
            md += ["| Cell | Intended path's share |", "|---|---|"] + [f"| {c} | {_pct(v[key], 1)} |" for c, v in cst.items()] + [""]
        for c in [k for k in cells if k in cst]:
            md += [f"#### {c}", ""] + _vantage_table(cr, c, names=("Passive observer", "First hop, credential", "Combined")) + [""]
            md += _class_table(cr, c) + [""]
            md += ["| First relay as | Lead over observer [95% CI] | Decisions |", "|---|---|---|"]
            for d in cd:
                if d["kind"] == "first relay by path" and d["cell"] == c:
                    md.append(f"| {d['path']} | {_pts(d['lead'], d['lo'], d['hi'])} | {d['n']:,} |")
            md.append("")
    md += ["## Cost per run", "", "| Configuration | Cell | Simulation | Scoring | Shuffle test |", "|---|---|---|---|---|"]
    for name, x in info["cost"].items():
        for c, v in x.items():
            md.append(f"| {EX.LABEL[name]} | {c} | {v['sim_seconds']:.1f} s | {v['score_seconds']:.1f} s | {v['test_seconds']:.1f} s |")
    (Path(out) / "TABLES.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    pt = ["# Paper table", "",
          f"How often each single compromised component names the device behind a registry record, with {EX.DECOYS} decoy "
          "transactions in flight and every node compromised in turn. Intervals are 95% and resample whole runs.", ""]
    for c in cells:
        pt += [f"## {c}", ""] + _vantage_table(rows, c) + [""]
    (Path(out) / "PAPER_TABLE.md").write_text("\n".join(pt) + "\n", encoding="utf-8")


def figures(out, rows, stats):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    out = Path(out)
    (out / "figures").mkdir(parents=True, exist_ok=True)
    names = [v[0] for v in VANTAGES]
    cells = [EX.cell_key(R) for R in EX.REAL_R if EX.cell_key(R) in stats]
    by = {(r["cell"], r["vantage"]): r for r in rows if r["subset"] == "all records"}
    f, axes = plt.subplots(1, len(cells), figsize=(11, 3.8), dpi=200)
    for ax, c in zip(np.atleast_1d(axes), cells):
        rs = [by.get((c, v)) for v in names]
        acc = [100 * r["dev_accuracy"] if r else 0 for r in rs]
        lo = [100 * (r["dev_accuracy"] - r["dev_ci_lo"]) if r else 0 for r in rs]
        hi = [100 * (r["dev_ci_hi"] - r["dev_accuracy"]) if r else 0 for r in rs]
        ax.barh(range(len(names)), acc, xerr=[lo, hi], color="#2a78d6", alpha=0.85)
        ax.axvline(100 * by[(c, "Passive observer")]["dev_random"], color="#5f5e5a", linestyle=":", linewidth=1.2,
                   label="chance (feasible set)")
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels(names if c == cells[0] else [], fontsize=7)
        ax.set_title(c, fontsize=9)
        ax.set_xlabel("device named (%)", fontsize=8)
        ax.invert_yaxis()
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
    np.atleast_1d(axes)[0].legend(fontsize=7, frameon=False, loc="lower right")
    f.tight_layout()
    f.savefig(out / "figures" / "device_named.png")
    plt.close(f)
    c = EX.cell_key(100) if EX.cell_key(100) in stats else cells[0]
    f, ax = plt.subplots(figsize=(5, 4.2), dpi=200)
    top = 0.0
    for v in names:
        r = by.get((c, v))
        if not r:
            continue
        rel = r["reliability"]
        ax.plot([100 * x["conf"] for x in rel], [100 * x["hit"] for x in rel], marker="o", markersize=3, linewidth=1.2, label=v)
        top = max(top, max(100 * x["conf"] for x in rel))
    ax.plot([0, top * 1.1], [0, top * 1.1], color="#5f5e5a", linestyle=":", linewidth=1)
    ax.set_xlabel("vantage's confidence in its match (%)", fontsize=8)
    ax.set_ylabel("matches actually right (%)", fontsize=8)
    ax.set_title(f"{c}: confidence against outcome, by decile", fontsize=9)
    ax.legend(fontsize=6, frameon=False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    f.tight_layout()
    f.savefig(out / "figures" / "confidence_reliability.png")
    plt.close(f)
    f, ax = plt.subplots(figsize=(7, 3.6), dpi=200)
    for c in cells:
        h = np.array(stats[c]["latency_hist10"], float)
        ax.plot(np.arange(h.size) * 10 + 5, 100 * h / max(h.sum(), 1), linewidth=1.4, label=c)
    ax.set_xlim(0, 3600)
    ax.set_xlabel("capture to registry posting (s)", fontsize=8)
    ax.set_ylabel("share of real transactions per 10 s (%)", fontsize=8)
    ax.legend(fontsize=7, frameon=False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    f.tight_layout()
    f.savefig(out / "figures" / "latency.png")
    plt.close(f)

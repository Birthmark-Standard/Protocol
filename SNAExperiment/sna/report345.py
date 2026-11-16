"""Tables of C3, C4 and C5 from their raw files (never re-simulates).

Main table, every row: the vantage (and class), its device-named accuracy with the 95% interval over runs, chance,
the multiple of chance, the lead over the passive observer on the same records, count_p50, coverage_p50, the
confidence AUC, whether the row meets the stability rule, and the bound from the posting schedule where it applies:
over every record of a vantage that names a device from the record time. A class chosen by the truth (the roles a
node held) can exceed it, so class rows show none.

Spread table, every row with a posterior: Shannon entropy and min-entropy in bits and the effective anonymity-set
size at the calibrated temperature, top-1, top-5 and top-10 accuracy, the naming rate over true devices (median,
90th percentile and the worst-off device, with its records), the calibration error and the flag for a badly
miscalibrated attacker. The reliability tables follow.

Chance is the same everywhere: the expected accuracy of naming, for each decision, one candidate drawn uniformly
from those the vantage finds feasible; zero when the truth is not feasible.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from . import analyze as AN
from . import runner as RN

D_MAIN = 1168.2274123090758
POST_S = 120.0
_BOUND = {}


def posting_bound(R, decoys, per_device=None, draws=400_000):
    """E[k / n] for a record's posting: n records in it, k of them from the record's device. Records post at
    (R + decoys) / D per second; a device makes 120 / (20 minutes) records per posting."""
    key = (R, decoys, per_device)
    if key not in _BOUND:
        lam = POST_S * (R + decoys) / D_MAIN
        x = POST_S / (20 * 60) if per_device is None else per_device
        rng = np.random.default_rng(7)
        X = rng.poisson(x, draws)
        Y = rng.poisson(max(lam - x, 0.0), draws)
        _BOUND[key] = float(np.mean((1 + X) / (1 + X + Y)))
    return _BOUND[key]


def record_bound(R, decoys):
    """Finding one record from its time: E[1 / (1 + Poisson(lambda))] = (1 - e^-lambda) / lambda."""
    lam = POST_S * (R + decoys) / D_MAIN
    return float((1 - math.exp(-lam)) / lam)


def summarize(out, files, classes=None, decoys_of=None, bound_na=(), seed=12345):
    """Rows for every vantage of the given raw files. classes: {vantage: (column, {code: label})} to split a
    vantage's rows; decoys_of(job, variant) -> decoys in flight; bound_na: vantages the bound does not apply to."""
    rng = np.random.default_rng(seed)
    rows = []
    for name in files:
        recs = sorted(RN.load(out, name), key=lambda r: r["run"])
        if not recs or "vantages" not in recs[0]:
            continue
        job, variant, cell = name.split("__")
        R = float(cell[1:])
        dec = decoys_of(job, variant) if decoys_of else 100.0
        spec = dict(R=R, T=R + dec, key=name)
        stats = [r.get("stats", {}) for r in recs]
        for v in recs[0]["vantages"]:
            if "dev_lse" not in recs[0]["vantages"][v]:          # diagnostics without confidence terms
                continue
            t_all = AN.stack(recs, v)
            splits = [(v, None)]
            if classes and v in classes:
                col, labels = classes[v]
                splits = [(f"{v} [{lab}]", (t_all[col] == code) if code is not None else np.ones(t_all[col].shape, bool))
                          for code, lab in labels.items()]
            for label, mask in splits:
                t = t_all if mask is None else {k: (a[mask] if isinstance(a, np.ndarray) and a.shape[:1] == mask.shape else a)
                                               for k, a in t_all.items()}
                if t["sub"].size == 0:
                    continue
                if "claim" in t and "took_part" not in t:     # the first hop's claims are read per hop position in C2
                    t = {k: a for k, a in t.items() if k != "claim"}
                mt = AN.metrics(recs, v, spec, rng, t=t, name=label)
                mt.pop("_per_run", None)
                mt.update(job=job, variant=variant, file=name, decoys=dec,
                          bound=None if (v in bound_na or label in bound_na or (mask is not None and not label.endswith("[all records]")))
                          else posting_bound(R, dec),
                          real_in_flight=float(np.mean([s.get("real_in_flight", np.nan) for s in stats])),
                          decoys_in_flight=float(np.mean([s.get("decoys_in_flight", np.nan) for s in stats])),
                          score_seconds=float(np.mean([r.get("score_seconds", 0.0) for r in recs])),
                          sim_seconds=float(np.mean([r.get("sim_seconds", 0.0) for r in recs])))
                rows.append(mt)
    return rows


def _rate_row(name, vantage, run, correct, chance, rng, bound=None, **extra):
    """A row from per-decision outcomes: accuracy with the 95% interval over runs, chance and the multiple."""
    num, den = AN.per_run(np.asarray(correct, float), np.asarray(run))
    acc, lo, hi = AN.cluster_boot(num, den, rng)
    ch = float(np.mean(chance)) if len(chance) else math.nan
    nc = int(np.sum(correct))
    n = int(np.size(correct))
    return dict(file=name, vantage=vantage, runs=int(np.unique(run).size), n=n, dev_accuracy=acc, dev_ci_lo=lo, dev_ci_hi=hi,
                dev_random=ch, dev_lift_random=acc / ch if ch and ch > 0 else math.nan, dev_contribution=math.nan,
                stable=bool(nc >= AN.MIN_EACH and n - nc >= AN.MIN_EACH), bound=bound, **extra)


def _spread_rows(row, run, correct, dev, rank, H, Hmin, conf, feas):
    """Spread metrics and calibration for decisions whose posterior is summarized by rank, entropy and min-entropy
    (bits) and whose confidence is conf."""
    H, Hmin = np.asarray(H, float), np.asarray(Hmin, float)
    ok = np.isfinite(H)
    row.update(entropy_bits=float(np.mean(H[ok])) if ok.any() else math.nan,
               anonymity_set=float(np.mean(2.0 ** H[ok])) if ok.any() else math.nan,
               min_entropy_bits=float(np.nanmean(Hmin)) if np.isfinite(Hmin).any() else math.nan)
    for k in AN.TOP_K:
        row[f"top{k}"] = float(np.mean(np.asarray(feas) & (np.asarray(rank) < k)))
    c = np.asarray(correct, bool)
    row["reliability"], row["calibration_error"] = AN.reliability(np.asarray(conf, float), c)
    row["conf_mean"] = float(np.mean(conf))
    row["calibration_null"] = AN.calibration_null(np.asarray(conf, float))
    row["miscalibrated"] = AN.miscalibrated(row["calibration_error"], row["dev_accuracy"], row["conf_mean"], row["calibration_null"])
    if len(c) >= 10 and 0 < c.sum() < len(c):
        row["auc"] = AN.auc_clustered(np.asarray(conf, float), c.astype(int), np.asarray(run))["auc"]
    d = np.asarray(dev, np.int64)
    u, inv, cnt = np.unique(d, return_inverse=True, return_counts=True)
    rate = np.bincount(inv, weights=c.astype(float)) / cnt
    big = cnt >= AN.MIN_DEVICE_RECORDS
    row["devices"] = int(big.sum())
    if big.any():
        w = int(np.argmax(rate[big]))
        row.update(device_rate_p50=float(np.median(rate[big])), device_rate_p90=float(np.percentile(rate[big], 90)),
                   device_rate_max=float(rate[big][w]), device_worst_records=int(cnt[big][w]))
    return row


def summarize_c4(out, files, seed=12345):
    """C4: every vantage of the observer files (as summarize), then per file the ceiling attacker, the K-record
    attacker on the observer's posteriors per K, and the edit-chain attacker per chain length."""
    from . import krecord as KR
    rng = np.random.default_rng(seed)
    rows = summarize(out, files, bound_na=(), seed=seed)
    for name in files:
        recs = sorted(RN.load(out, name), key=lambda r: r["run"])
        if not recs or "ceiling" not in recs[0]:
            continue
        _, variant, cell = name.split("__")
        R = float(cell[1:])
        run = np.concatenate([np.full(r["ceiling"]["correct"].size, r["run"]) for r in recs])
        c = np.concatenate([r["ceiling"]["correct"] for r in recs])
        ch = np.concatenate([1.0 / np.maximum(r["ceiling"]["size"].astype(float), 1) for r in recs])
        rows.append(_rate_row(name, "ceiling", run, c, ch, rng, bound=posting_bound(R, 100.0)))
        Ks = (1, 2, 3, 5, 10, 20) if (R == 1 or variant in ("W1", "W2")) else (1, 2, 3, 5)
        _, per = KR.k_record(recs, Ks, full=True)
        for K in Ks:
            if not per[K]:
                continue
            a = np.array(per[K], float)              # run, correct, device, rank, H, Hmin, chance
            row = _rate_row(name, f"K records, K = {K}", a[:, 0], a[:, 1], a[:, 6], rng, bound=None)
            rows.append(_spread_rows(row, a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5], 2.0 ** -a[:, 5],
                                     a[:, 3] >= 0))
        if "vec_lb" in recs[0]:
            res = KR.chains(recs)
            for L in sorted({L for per_run in res for L in per_run}):
                num = np.array([per_run.get(L, (0, 0, 0.0))[0] for per_run in res], float)
                den = np.array([per_run.get(L, (0, 0, 0.0))[1] for per_run in res], float)
                chs = np.array([per_run.get(L, (0, 0, 0.0))[2] for per_run in res], float)
                acc, lo, hi = AN.cluster_boot(num, den, rng)
                ch = chs.sum() / max(den.sum(), 1)
                rows.append(dict(file=name, vantage=f"edit chain, {L} records", runs=len(res), n=int(den.sum()), dev_accuracy=acc,
                                 dev_ci_lo=lo, dev_ci_hi=hi, dev_random=ch, dev_lift_random=acc / ch if ch > 0 else math.nan,
                                 dev_contribution=math.nan, stable=bool(num.sum() >= AN.MIN_EACH and den.sum() - num.sum() >= AN.MIN_EACH),
                                 bound=None))
    return rows


def summarize_c5(out, files, seed=12345):
    """C5: per setting and cell, finding the target's records: accuracy with its interval over runs, chance, the
    bound from the posting schedule for record finding (not for a withholding validator, which changes how many
    records share a posting), and the spread and calibration of the attacker's posterior over candidate records."""
    rng = np.random.default_rng(seed)
    rows = []
    for name in files:
        recs = sorted(RN.load(out, name), key=lambda r: r["run"])
        if not recs or "marks" not in recs[0]:
            continue
        _, setting, cell = name.split("__")
        R = float(cell[1:])
        if "dev_lse" not in recs[0]["marks"]:
            continue
        groups = [(setting, recs)]
        if setting.startswith("vwh3_"):                # by the share of the target's own validator
            groups = [(f"{setting}, target's validator {lab}", [r for r in recs if r.get("target_key", -1) in ks])
                      for lab, ks in (("50%", (0,)), ("30% or 20%", (1, 2)))]
        for label, grp in groups:
            if grp:
                rows += _c5_rows(name, label, grp, R, setting, rng)
    return rows


def _c5_rows(name, label, recs, R, setting, rng):
    """One C5 row from a group of runs."""
    mk = [r["marks"] for r in recs]
    t = {k: np.concatenate([m_[k] for m_ in mk]) for k in ("sub", "dev_v_correct", "dev_v_rand", "dev_top1", "dev_s_true",
                                                         "dev_lse", "dev_ent", "dev_rank")}
    t["run"] = np.concatenate([np.full(m_["sub"].size, r["run"], np.int32) for m_, r in zip(mk, recs)])
    if t["sub"].size == 0:
        return []
    conf, temps = AN.calibrated_confidence(t)
    bound = None if setting.startswith("vwh") else record_bound(R, 100.0)
    row = _rate_row(name, label, t["run"], t["dev_v_correct"], t["dev_v_rand"], rng, bound=bound,
                    target_transactions=float(np.mean([r["target_transactions"] for r in recs])))
    ti = np.array([int(np.argmin(np.abs(AN.T_GRID - temps[f]))) for f in (0, 1)])[t["run"] % 2]
    r_ = np.arange(t["sub"].size)
    H = t["dev_ent"][r_, ti].astype(float) / math.log(2)
    Hmin = t["dev_lse"][r_, ti].astype(float) / math.log(2)
    runs = [r["run"] for r in recs]
    dev = np.array([r["target"] for r in recs])[np.searchsorted(runs, t["run"])] + t["run"].astype(np.int64) * 10 ** 6
    return [_spread_rows(row, t["run"], t["dev_v_correct"], dev, t["dev_rank"], H, Hmin, conf, np.isfinite(t["dev_s_true"]))]


def pct(x):
    return "—" if x is None or (isinstance(x, float) and not math.isfinite(x)) else f"{100 * x:.2f}%"


def num(x, f="{:.2f}"):
    return "—" if x is None or (isinstance(x, float) and not math.isfinite(x)) else f.format(x)


def markdown(rows, title, dry=False):
    lines = []
    if dry:
        lines.append("DRY RUN: fewer runs than the full count. These numbers are not results.\n")
    lines.append(f"# {title}\n")
    lines.append("Chance is the expected accuracy of naming, for each decision, one candidate drawn uniformly from those "
                 "the vantage finds feasible; zero when the truth is not feasible.\n")
    lines.append("| File | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | "
                 "count_p50 | coverage_p50 | AUC | Stable | Bound | Real, decoys in flight |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        if "dev_accuracy" not in r:
            continue
        lead = r.get("dev_contribution", math.nan)
        lines.append(
            f"| {r['file']} | {r['vantage']} | {r['runs']} | {r['n']:,} | {pct(r['dev_accuracy'])} [{pct(r['dev_ci_lo'])}, {pct(r['dev_ci_hi'])}] | "
            f"{pct(r['dev_random'])} | ×{num(r['dev_lift_random'])} | {num(100 * lead if math.isfinite(lead) else math.nan, '{:+.2f}')} | "
            f"{r.get('count_p50', '—')} | {num(r.get('coverage_p50', math.nan), '{:.4f}')} | {num(r.get('auc', math.nan), '{:.3f}')} | "
            f"{'yes' if r['stable'] else 'no'} | {'not applicable' if r['bound'] is None else pct(r['bound'])} | "
            f"{num(r.get('real_in_flight', math.nan))}, {num(r.get('decoys_in_flight', math.nan))} |")
    lines.append("\n## Spread of the posterior and calibration\n")
    lines.append("Entropy and min-entropy in bits at the calibrated temperature; the effective anonymity set is 2 to the "
                 "entropy. Devices: the naming rate over true devices with at least "
                 f"{AN.MIN_DEVICE_RECORDS} records (median, 90th percentile, and the worst-off device with its records). "
                 "Sampling: the calibration error a perfectly calibrated attacker would reach at the 99th percentile "
                 "by sampling alone, at the same confidences. Flag: the calibration error is above that and exceeds both "
                 "2 points and a quarter of the larger of the accuracy and the mean confidence.\n")
    lines.append("| File | Vantage | Entropy | Effective set | Min-entropy | Top-1 | Top-5 | Top-10 | Devices: median, p90, worst (records) | "
                 "Calibration error | Sampling | Flag |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        if "top1" not in r and "calibration_error" not in r:
            continue
        dv = (f"{pct(r['device_rate_p50'])}, {pct(r['device_rate_p90'])}, {pct(r['device_rate_max'])} ({r['device_worst_records']})"
              if "device_rate_max" in r else "—")
        lines.append(f"| {r['file']} | {r['vantage']} | {num(r.get('entropy_bits', math.nan))} | {num(r.get('anonymity_set', math.nan), '{:.1f}')} | "
                     f"{num(r.get('min_entropy_bits', math.nan))} | {pct(r.get('top1', r['dev_accuracy']))} | {pct(r.get('top5'))} | "
                     f"{pct(r.get('top10'))} | {dv} | {pct(r.get('calibration_error'))} | {pct(r.get('calibration_null'))} | "
                     f"{'badly miscalibrated' if r.get('miscalibrated') else ''} |")
    lines.append("\n## Reliability\n")
    lines.append("Per row, the confidence deciles: mean confidence → hit rate.\n")
    for r in rows:
        if r.get("reliability"):
            cells = "; ".join(f"{100 * x['conf']:.1f} → {100 * x['hit']:.1f}" for x in r["reliability"])
            lines.append(f"- {r['file']}, {r['vantage']}: {cells}")
    return "\n".join(lines) + "\n"


def write(out, rows, stem, title, dry=False):
    out = Path(out)
    clean = [{k: v for k, v in r.items() if k != "temperature"} for r in rows]
    stem = stem + ("_dry_run" if dry else "")
    (out / f"{stem}.json").write_text(json.dumps(clean, indent=1, default=float))
    (out / f"{stem}.md").write_text(markdown(rows, title, dry))

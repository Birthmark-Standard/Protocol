"""Metrics from the persisted per-decision records (never re-simulates). ANALYSIS_PLAN.md section 5.

Intervals resample whole runs (cluster bootstrap on per-run totals). AUC uses the clustered-data
variance of Obuchowski (1997). Precision at a coverage uses the Wilson interval.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm

from . import attacks as AT
from .attacks import T_GRID

Z95 = 1.959963984540054
FAMILY = 14                                   # 7 vantages x 2 tests per cell
Z_ADJ = float(norm.ppf(1 - 0.05 / FAMILY / 2))
BOOT = 2000
MIN_EACH = 50                                 # successes (and failures) needed for a stable finding
AUC_MARGIN = 0.03                             # confidence AUCs within this of 0.5 are not read as signal


def cluster_boot(num, den, rng, z=None, reps=BOOT):
    num, den = np.asarray(num, float), np.asarray(den, float)
    est = num.sum() / max(den.sum(), 1e-12)
    if num.size < 2:
        return est, math.nan, math.nan
    idx = rng.integers(0, num.size, (reps, num.size))
    b = num[idx].sum(1) / np.maximum(den[idx].sum(1), 1e-12)
    lo, hi = (2.5, 97.5) if z is None else (100 * norm.sf(z), 100 * norm.cdf(z))
    return float(est), float(np.percentile(b, lo)), float(np.percentile(b, hi))


def wilson(k, n, z=Z95):
    if n == 0:
        return (math.nan, math.nan, math.nan)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, c - h, c + h


def auc_clustered(score, label, cluster):
    score = np.asarray(score, float)
    pos, neg = score[label == 1], score[label == 0]
    if pos.size == 0 or neg.size == 0:
        return dict(auc=math.nan, se=math.nan)
    sn, sp = np.sort(neg), np.sort(pos)
    v10 = (np.searchsorted(sn, pos, "left") + np.searchsorted(sn, pos, "right")) / (2.0 * neg.size)
    v01 = 1.0 - (np.searchsorted(sp, neg, "left") + np.searchsorted(sp, neg, "right")) / (2.0 * pos.size)
    A = v10.mean()
    ks = np.unique(cluster)
    I = ks.size
    if I < 2:
        return dict(auc=float(A), se=math.nan)
    M, N = pos.size, neg.size
    ip, in_ = np.searchsorted(ks, cluster[label == 1]), np.searchsorted(ks, cluster[label == 0])
    S10 = np.bincount(ip, weights=v10, minlength=I)
    S01 = np.bincount(in_, weights=v01, minlength=I)
    m = np.bincount(ip, minlength=I).astype(float)
    n = np.bincount(in_, minlength=I).astype(float)
    a, b = S10 - m * A, S01 - n * A
    var = I / (I - 1) * ((a * a).sum() / M ** 2 + (b * b).sum() / N ** 2 + 2 * (a * b).sum() / (M * N))
    return dict(auc=float(A), se=float(math.sqrt(max(var, 0.0))))


# --------------------------------------------------------------------------- confidence
def stack(records, v):
    parts = [r["vantages"][v] for r in records]
    keys = [k for k, x in parts[0].items() if isinstance(x, np.ndarray)]
    out = {k: np.concatenate([p[k] for p in parts]) for k in keys}
    out["run"] = np.concatenate([np.full(p["sub"].shape[0], r["run"], np.int32) for p, r in zip(parts, records)])
    return out


def _posterior(t, ti):
    """Calibrated posterior of the device pick at grid temperature T_GRID[ti]: softmax of the top
    score, exp(top1 / T - LSE_T), stored as the offset LSE_T - top1 / T."""
    p = np.exp(-t["dev_lse"][:, ti].astype(float))
    return np.where(np.isfinite(p), np.clip(p, 0, 1), 0.0)


def _fit_temperature(t, rows):
    ok = rows & np.isfinite(t["dev_s_true"]) & np.isfinite(t["dev_top1"])
    if ok.sum() < 10:
        return int(np.argmin(np.abs(T_GRID - 1.0)))
    nll = [np.mean(t["dev_lse"][ok, i].astype(float) + t["dev_top1"][ok] / T - t["dev_s_true"][ok] / T)
           for i, T in enumerate(T_GRID)]
    return int(np.nanargmin(nll))


def calibrated_confidence(t):
    """Cross-fitted by run parity: each half uses the temperature fitted on the other half."""
    conf = np.zeros(t["sub"].shape[0])
    temps = {}
    for fold in (0, 1):
        this = (t["run"] % 2) == fold
        ti = _fit_temperature(t, ~this)
        conf[this] = _posterior(t, ti)[this]
        temps[fold] = float(T_GRID[ti])
    return conf, temps


def precision_at(conf, correct, q):
    order = np.argsort(-conf, kind="stable")
    k = max(1, int(round(q * conf.size)))
    return wilson(int(correct[order][:k].sum()), k)


def max_coverage_p50(conf, correct):
    """Largest coverage (share of decisions, most confident first) whose precision exceeds 50%."""
    if conf.size == 0:
        return math.nan
    order = np.argsort(-conf, kind="stable")
    prec = np.cumsum(correct[order]) / np.arange(1, conf.size + 1)
    good = np.nonzero(prec > 0.5)[0]
    return float((good.max() + 1) / conf.size) if good.size else 0.0


# --------------------------------------------------------------------------- one cell, one vantage
def per_run(values, run):
    runs, inv = np.unique(run, return_inverse=True)
    return np.bincount(inv, weights=values.astype(float)), np.bincount(inv).astype(float)


def _level(t, lvl, T, rng, out):
    """Accuracy, paired contribution and chance references at one success level."""
    c = t[f"{lvl}_v_correct"].astype(bool)
    b = t[f"{lvl}_b_correct"].astype(bool)
    num, den = per_run(c, t["run"])
    p = f"{lvl}_"
    out[p + "n_correct"] = int(c.sum())
    out[p + "accuracy"], out[p + "ci_lo"], out[p + "ci_hi"] = cluster_boot(num, den, rng)
    _, out[p + "ci_adj_lo"], out[p + "ci_adj_hi"] = cluster_boot(num, den, rng, z=Z_ADJ)
    nb, _ = per_run(b, t["run"])
    out[p + "baseline"], out[p + "baseline_lo"], out[p + "baseline_hi"] = cluster_boot(nb, den, rng)
    nd, _ = per_run(c.astype(float) - b, t["run"])
    out[p + "contribution"], out[p + "contribution_lo"], out[p + "contribution_hi"] = cluster_boot(nd, den, rng)
    nr, _ = per_run(t[f"{lvl}_v_rand"].astype(float), t["run"])
    out[p + "random"] = float(nr.sum() / den.sum())
    out[p + "baseline_random"] = float(t[f"{lvl}_b_rand"].mean())
    # lift against the random-assignment rate (the chance of a uniform pick among the feasible
    # candidates), with the interval from the same run resampling
    rnd = out[p + "random"]
    out[p + "lift_random"] = out[p + "accuracy"] / rnd if rnd > 0 else math.nan
    out[p + "lift_random_lo"] = out[p + "ci_lo"] / rnd if rnd > 0 else math.nan
    out[p + "lift_random_hi"] = out[p + "ci_hi"] / rnd if rnd > 0 else math.nan
    out[p + "signal_random"] = bool(out[p + "ci_adj_lo"] > rnd) if math.isfinite(out[p + "ci_adj_lo"]) else False
    out[p + "candidates_median"] = float(np.median(t[f"{lvl}_n_feas"]))
    return num, den


def metrics(records, v, spec, rng):
    t = stack(records, v)
    R, T = spec["R"], spec["T"]
    n = int(t["sub"].size)
    out = dict(cell=spec["key"], vantage=v, R=R, T=T, L=T, control=spec["control"], runs=len(records), n=n,
               inv_L=1.0 / T, inv_R=1.0 / R)
    if n == 0:
        return out
    num, den = _level(t, "dev", T, rng, out)
    nums, dens = _level(t, "sub", T, rng, out)
    out["sub_lift"], out["sub_lift_lo"], out["sub_lift_hi"] = out["sub_accuracy"] * T, out["sub_ci_lo"] * T, out["sub_ci_hi"] * T
    out["sub_signal_L"] = bool(out["sub_ci_adj_lo"] > 1.0 / T) if math.isfinite(out["sub_ci_adj_lo"]) else False
    # stability and confidence at the primary (device) level
    c = t["dev_v_correct"].astype(bool)
    enough = out["dev_n_correct"] >= MIN_EACH and (n - out["dev_n_correct"]) >= MIN_EACH
    out["stable"] = bool(enough)
    per = out["dev_n_correct"] / len(records)
    fails = (n - out["dev_n_correct"]) / len(records)
    need = max(MIN_EACH / per if per > 0 else math.inf, MIN_EACH / fails if fails > 0 else math.inf)
    out["runs_needed"] = 0 if enough else (math.inf if not math.isfinite(need) else int(math.ceil(need)))
    conf, temps = calibrated_confidence(t)
    out["temperature"] = temps
    a = auc_clustered(conf, c.astype(int), t["run"])
    out["auc"], out["auc_lo"], out["auc_hi"] = a["auc"], a["auc"] - Z95 * a["se"], a["auc"] + Z95 * a["se"]
    out["auc_adj_lo"] = a["auc"] - Z_ADJ * a["se"]
    out["signal_auc"] = bool(enough and out["auc_adj_lo"] > 0.5 + AUC_MARGIN)
    out["signal"] = out["dev_signal_random"] or out["signal_auc"]
    for q, name in ((0.01, "p_at_1"), (0.05, "p_at_5"), (0.10, "p_at_10"), (0.25, "p_at_25")):
        p, lo, hi = precision_at(conf, c, q)
        out[name], out[name + "_lo"], out[name + "_hi"] = p, lo, hi
    out["coverage_p50"] = max_coverage_p50(conf, c)
    out["count_p50"] = int(round(out["coverage_p50"] * conf.size))
    out["decisions"] = int(conf.size)
    # the attacker's own confidence that its match is right (calibrated, cross-fitted by run parity):
    # its distribution, and how well it tracks the actual hit rate (reliability by confidence decile)
    out["conf_mean"] = float(conf.mean())
    for q in (50, 90, 99):
        out[f"conf_p{q}"] = float(np.percentile(conf, q))
    out["conf_max"] = float(conf.max())
    order = np.argsort(conf, kind="stable")
    bins = np.array_split(order, 10)
    out["reliability"] = [dict(conf=float(conf[b].mean()), hit=float(c[b].mean()), n=int(b.size)) for b in bins if b.size]
    out["calibration_error"] = float(sum(abs(x["conf"] - x["hit"]) * x["n"] for x in out["reliability"]) / conf.size)
    perm = c.copy()
    for rid in np.unique(t["run"]):
        m = np.nonzero(t["run"] == rid)[0]
        perm[m] = c[m][rng.permutation(m.size)]
    a = auc_clustered(conf, perm.astype(int), t["run"])
    out["shuffle_auc"], out["shuffle_auc_lo"], out["shuffle_auc_hi"] = a["auc"], a["auc"] - Z95 * a["se"], a["auc"] + Z95 * a["se"]
    if "claim" in t:
        _claims(t, rng, out)
    out["_per_run"] = dict(dev=(num, den), sub=(nums, dens))
    return out


def _claims(t, rng, out):
    """For a vantage scored on every record: how many records it claims, how often a claim is
    right, the baseline's accuracy on the same claimed records, and its accuracy on the records it
    actually took part in (which it cannot identify)."""
    cl = t["claim"].astype(bool)
    part = t["took_part"].astype(bool)
    n_runs = np.unique(t["run"]).size
    nc, nd = per_run(cl, t["run"])
    out["claim_rate"] = float(nc.sum() / nd.sum())
    out["took_part_rate"] = float(part.mean())
    out["claims_on_own_records"] = float((cl & part).sum() / max(cl.sum(), 1))
    for lvl in ("dev", "sub"):
        c = t[f"{lvl}_v_correct"].astype(bool)
        b = t[f"{lvl}_b_correct"].astype(bool)
        for name, m in (("claimed", cl), ("took_part", part)):
            if m.sum() == 0:
                continue
            num, den = per_run(c[m], t["run"][m])
            k = f"{lvl}_{name}"
            out[k], out[k + "_lo"], out[k + "_hi"] = cluster_boot(num, den, rng)
            nb, _ = per_run(b[m], t["run"][m])
            out[k + "_baseline"] = float(nb.sum() / den.sum())
            out[k + "_n"] = int(m.sum())
    return out


def decoy_effect(with_recs, without_recs, v, rng):
    """Paired effect on the same real records: accuracy in one cell minus accuracy in its paired
    cell (bundling on minus off), matched row by row on (run, transaction, group), with an
    interval from resampling runs. Both cells carry identical traffic."""
    base = {}
    for r in without_recs:
        x = r["vantages"][v]
        base[r["run"]] = x
    out = {}
    for lvl in ("dev", "sub"):
        num, den, n_unmatched = [], [], 0
        for r in with_recs:
            y = r["vantages"][v]
            x = base.get(r["run"])
            if x is None:
                continue
            kx = {(int(a), int(b)): i for i, (a, b) in enumerate(zip(x["sub"], x["group"]))}
            idx = [kx.get((int(a), int(b)), -1) for a, b in zip(y["sub"], y["group"])]
            idx = np.array(idx, np.int64)
            ok = idx >= 0
            n_unmatched += int((~ok).sum())
            d = y[f"{lvl}_v_correct"][ok].astype(float) - x[f"{lvl}_v_correct"][idx[ok]].astype(float)
            num.append(d.sum())
            den.append(ok.sum())
        e, lo, hi = cluster_boot(np.array(num), np.array(den), rng)
        out[lvl] = dict(effect=e, lo=lo, hi=hi, n=int(sum(den)), unmatched=n_unmatched)
    return out


def analyze(out, cells, loader, seed=12345, priors=None):
    """Metrics for every cell with records. loader(key) -> list of run records. priors maps a name
    to a loader of the same cells under an earlier build; each vantage's effect of the change from
    that build is then paired against it, record by record."""
    rng = np.random.default_rng(seed)
    rows = []
    for key, spec in cells.items():
        recs = loader(key)
        if not recs:
            continue
        recs = sorted(recs, key=lambda r: r["run"])
        bs = bundle_stats(recs)
        for v in AT.VANTAGES:
            r = metrics(recs, v, spec, rng)
            r["decoys"], r["bundle"] = float(spec.get("decoys", 0.0)), bool(spec.get("bundle", False))
            if bs:
                r.update({f"bundle_{k}": x for k, x in bs.items() if k != "hist"})
            rows.append(r)
    effects = {}
    by_key = {spec["key"]: spec for spec in cells.values()}
    for key, spec in by_key.items():
        if not spec.get("bundle"):
            continue
        ref = next((k for k, sp in by_key.items() if sp["R"] == spec["R"] and sp.get("decoys") == spec.get("decoys")
                    and not sp.get("bundle") and not sp["control"]), None)
        if ref is None:
            continue
        w, wo = loader(key), loader(ref)
        if not w or not wo:
            continue
        for v in AT.VANTAGES:
            effects[f"{v}.R{spec['R']:g}.D{spec['decoys']:g}"] = decoy_effect(w, wo, v, rng)
    changes = {}
    for name, prior_loader in (priors or {}).items():
        ch = {}
        for key, spec in by_key.items():
            w, pr = loader(key), prior_loader(key)
            if spec["control"] or not w or not pr:
                continue
            for v in AT.VANTAGES:
                ch[f"{v}.R{spec['R']:g}.D{spec['decoys']:g}"] = decoy_effect(w, pr, v, rng)
        changes[name] = ch
    return rows, effects, changes


def bundle_stats(records):
    """Departure-bundle size distribution summed over a cell's runs (per gatekeeper bundle)."""
    h = np.sum([r["bundles"] for r in records if "bundles" in r], axis=0)
    if np.ndim(h) == 0 or h.sum() == 0:
        return None
    k = np.arange(h.size)
    n, pk = h.sum(), (h * k).sum()
    return dict(bundles=int(n), mean=float(pk / n), p0=float(h[0] / n), p1=float(h[1] / n),
                p_lt2=float((h[0] + h[1]) / n), p1_nonempty=float(h[1] / max(n - h[0], 1)),
                alone_share=float(h[1] / max(pk, 1)), hist=h.tolist())

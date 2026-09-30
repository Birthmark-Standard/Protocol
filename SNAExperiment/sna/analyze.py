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
TREND_L = (40, 50, 100, 200, 500)


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
    out["signal_auc"] = bool(enough and out["auc_adj_lo"] > 0.5)
    out["signal"] = out["dev_signal_random"] or out["signal_auc"]
    for q, name in ((0.01, "p_at_1"), (0.05, "p_at_5")):
        p, lo, hi = precision_at(conf, c, q)
        out[name], out[name + "_lo"], out[name + "_hi"] = p, lo, hi
    out["coverage_p50"] = max_coverage_p50(conf, c)
    perm = c.copy()
    for rid in np.unique(t["run"]):
        m = np.nonzero(t["run"] == rid)[0]
        perm[m] = c[m][rng.permutation(m.size)]
    a = auc_clustered(conf, perm.astype(int), t["run"])
    out["shuffle_auc"], out["shuffle_auc_lo"], out["shuffle_auc_hi"] = a["auc"], a["auc"] - Z95 * a["se"], a["auc"] + Z95 * a["se"]
    out["_per_run"] = dict(dev=(num, den), sub=(nums, dens))
    return out


def lift_trend(rows_by_L, rng, level="dev", reps=BOOT):
    """Slope of log lift against log L across TREND_L, with a percentile interval from resampling
    runs within each cell. Device level: lift against the random-assignment rate. Submission
    level: accuracy x L. Direction: rises / falls if the interval excludes 0, else holds flat."""
    Ls = [L for L in TREND_L if L in rows_by_L and "_per_run" in rows_by_L[L]]
    if len(Ls) < 2:
        return None
    x = np.log(np.array(Ls, float))
    ref = np.array([1.0 / rows_by_L[L][f"{level}_random"] if level == "dev" else L for L in Ls], float)

    def slope(acc):
        return float(np.polyfit(x, np.log(np.maximum(np.array(acc) * ref, 1e-6)), 1)[0])
    est = slope([rows_by_L[L][f"{level}_accuracy"] for L in Ls])
    boots = []
    for _ in range(reps):
        acc = []
        for L in Ls:
            num, den = rows_by_L[L]["_per_run"][level]
            i = rng.integers(0, num.size, num.size)
            acc.append(num[i].sum() / max(den[i].sum(), 1e-12))
        boots.append(slope(acc))
    lo, hi = np.percentile(boots, [2.5, 97.5])
    direction = "rises" if lo > 0 else ("falls" if hi < 0 else "holds flat")
    return dict(slope=est, lo=float(lo), hi=float(hi), direction=direction, L=Ls,
                lift_40=float(rows_by_L[Ls[0]][f"{level}_accuracy"] * ref[0]),
                lift_500=float(rows_by_L[Ls[-1]][f"{level}_accuracy"] * ref[-1]))


def analyze(out, cells, loader, seed=12345):
    """Metrics for every cell with records. loader(key) -> list of run records."""
    rng = np.random.default_rng(seed)
    rows = []
    for key, spec in cells.items():
        recs = loader(key)
        if not recs:
            continue
        recs = sorted(recs, key=lambda r: r["run"])
        for v in AT.VANTAGES:
            rows.append(metrics(recs, v, spec, rng))
    trends = {}
    for v in AT.VANTAGES:
        by_L = {int(r["T"]): r for r in rows if r["vantage"] == v and r["R"] == r["T"] and not r["control"]}
        for level in ("dev", "sub"):
            tr = lift_trend(by_L, rng, level)
            if tr:
                trends[f"{v}.{level}"] = tr
    return rows, trends

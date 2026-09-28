"""Metrics from persisted per-decision records (never re-simulates). ANALYSIS_PLAN.md section 4.

Confidence intervals: accuracy and paired differences resample whole runs (cluster bootstrap on
per-run totals). AUC uses the clustered-data variance of Obuchowski (1997), which accounts for
decisions sharing a run the same way run resampling does and stays fast at a million decisions.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm

from .engine import T_GRID

Z95 = 1.959963984540054
FAMILY = 14                                   # 7 scenarios x 2 tests per (round, L)
Z_ADJ = float(norm.ppf(1 - 0.05 / FAMILY / 2))
BOOT = 2000
COVERAGES = (0.01, 0.05, 0.10, 0.25, 0.50, 1.00)
MIN_EACH = 50                                  # correct and incorrect decisions needed for an AUC finding


def stack(records):
    """Concatenate run records into one table with a run index per decision."""
    keys = [k for k, v in records[0].items() if isinstance(v, np.ndarray)]
    out = {k: np.concatenate([r[k] for r in records]) for k in keys}
    out["run"] = np.concatenate([np.full(r["correct"].shape[0], r["run"], np.int32) for r in records])
    return out


# --------------------------------------------------------------------------- intervals
def cluster_boot(num, den, rng, z=None, reps=BOOT):
    """Ratio sum(num)/sum(den) over runs, with a percentile interval from resampled runs."""
    num, den = np.asarray(num, float), np.asarray(den, float)
    est = num.sum() / max(den.sum(), 1e-12)
    idx = rng.integers(0, num.size, (reps, num.size))
    b = num[idx].sum(1) / np.maximum(den[idx].sum(1), 1e-12)
    lo, hi = (2.5, 97.5) if z is None else (100 * norm.sf(z), 100 * norm.cdf(z))
    return est, float(np.percentile(b, lo)), float(np.percentile(b, hi))


def per_run(values, run):
    runs, inv = np.unique(run, return_inverse=True)
    return np.bincount(inv, weights=values.astype(float)), np.bincount(inv).astype(float)


def wilson(k, n, z=Z95):
    if n == 0:
        return (math.nan, math.nan, math.nan)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, c - h, c + h


def auc_clustered(score, label, cluster):
    """AUC of score for label=1 vs 0, with Obuchowski's clustered variance. Ties count 1/2."""
    score = np.asarray(score, float)
    pos, neg = score[label == 1], score[label == 0]
    if pos.size == 0 or neg.size == 0:
        return dict(auc=math.nan, se=math.nan)
    sn = np.sort(neg)
    sp = np.sort(pos)
    # V10(x) = P(neg < x) + P(neg == x)/2 ; V01(y) = P(pos > y) + P(pos == y)/2
    v10 = (np.searchsorted(sn, pos, "left") + np.searchsorted(sn, pos, "right")) / (2.0 * neg.size)
    v01 = 1.0 - (np.searchsorted(sp, neg, "left") + np.searchsorted(sp, neg, "right")) / (2.0 * pos.size)
    A = v10.mean()
    cp, cn = cluster[label == 1], cluster[label == 0]
    ks = np.unique(cluster)
    I = ks.size
    if I < 2:
        return dict(auc=float(A), se=math.nan)
    M, N = pos.size, neg.size
    ip, in_ = np.searchsorted(ks, cp), np.searchsorted(ks, cn)
    S10 = np.bincount(ip, weights=v10, minlength=I)
    S01 = np.bincount(in_, weights=v01, minlength=I)
    m = np.bincount(ip, minlength=I).astype(float)
    n = np.bincount(in_, minlength=I).astype(float)
    a, b = S10 - m * A, S01 - n * A
    f = I / (I - 1)
    var = f * ((a * a).sum() / M ** 2 + (b * b).sum() / N ** 2 + 2 * (a * b).sum() / (M * N))
    return dict(auc=float(A), se=float(math.sqrt(max(var, 0.0))))


# --------------------------------------------------------------------------- confidence
def softmax_conf(t, T_idx):
    """Calibrated posterior of the chosen answer at grid temperature T_GRID[T_idx]."""
    T = T_GRID[T_idx]
    lse = t["lse"][:, T_idx].astype(float) + t["top1"] / T
    with np.errstate(over="ignore", invalid="ignore"):
        p = np.exp(t["s_joint"] / T - lse)
    return np.where(np.isfinite(p), np.clip(p, 0, 1), 0.0)


def fit_temperature(t, rows):
    """Grid temperature minimising the negative log-likelihood of the true answer."""
    ok = rows & np.isfinite(t["s_true"]) & np.isfinite(t["top1"])
    if ok.sum() < 10:
        return int(np.argmin(np.abs(T_GRID - 1.0)))
    nll = []
    for i, T in enumerate(T_GRID):
        lse = t["lse"][ok, i].astype(float) + t["top1"][ok] / T
        nll.append(np.mean(lse - t["s_true"][ok] / T))
    return int(np.argmin(nll))


def calibrated_confidence(t):
    """Cross-fitted: runs split by run-id parity; each half uses the temperature fitted on the
    other half, so no decision's own outcome enters its confidence."""
    conf = np.zeros(t["correct"].shape[0])
    temps = {}
    for fold in (0, 1):
        this = (t["run"] % 2) == fold
        ti = fit_temperature(t, ~this)
        conf[this] = softmax_conf(t, ti)[this]
        temps[fold] = float(T_GRID[ti])
    return conf, temps


def gap_confidence(t):
    g = t["top1"].astype(float) - t["top2"].astype(float)
    g = np.where(np.isfinite(t["top1"]) & ~np.isfinite(t["top2"]), np.inf, g)   # a single feasible answer
    g = np.where(np.isfinite(t["top1"]), g, -np.inf)                            # no feasible answer
    fin = g[np.isfinite(g)]
    hi = fin.max() + 1 if fin.size else 1.0
    return np.clip(np.nan_to_num(g, posinf=hi, neginf=-1.0), -1.0, hi)


def precision_coverage(conf, correct):
    order = np.argsort(-conf, kind="stable")
    c = correct[order].astype(float)
    n = c.size
    cum = np.cumsum(c)
    rows = []
    for q in COVERAGES:
        k = max(1, int(round(q * n)))
        p, lo, hi = wilson(cum[k - 1], k)
        rows.append(dict(coverage=q, n=k, precision=p, ci_lo=lo, ci_hi=hi))
    prec = cum / np.arange(1, n + 1)
    good = np.nonzero(prec >= 0.5)[0]
    yield_cov = float((good.max() + 1) / n) if good.size else 0.0
    k1 = max(1, int(math.ceil(0.01 * n)))
    best = float(prec[k1 - 1:].max()) if n else math.nan
    return rows, yield_cov, best


def reliability(conf, correct, bins=15):
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(conf, edges) - 1, 0, bins - 1)
    rows, ece = [], 0.0
    for b in range(bins):
        m = idx == b
        if m.any():
            acc, cf = correct[m].mean(), conf[m].mean()
            ece += m.mean() * abs(acc - cf)
            rows.append(dict(bin_lo=edges[b], bin_hi=edges[b + 1], n=int(m.sum()), confidence=float(cf), accuracy=float(acc)))
    return rows, float(ece)


def quantiles(x):
    if x.size == 0:
        return dict(median=math.nan, q25=math.nan, q75=math.nan)
    q = np.percentile(x, [25, 50, 75])
    return dict(q25=float(q[0]), median=float(q[1]), q75=float(q[2]))


def shuffled(t, rng):
    """Negative control: each decision's true transaction permuted among the same server's decisions
    in the same run."""
    key = t["run"].astype(np.int64) * 100_000 + t["group"].astype(np.int64)
    order = np.lexsort((rng.random(key.size), key))
    perm_sub = t["sub"].copy()
    ks = key[order]
    bounds = np.flatnonzero(np.diff(ks)) + 1
    for sl in np.split(np.arange(ks.size), bounds):
        src = order[sl]
        perm_sub[src] = t["sub"][src[rng.permutation(src.size)]]
    return (t["pred"] == perm_sub) & (t["pred"] >= 0)


# --------------------------------------------------------------------------- one cell
def metrics(records, L, rng, with_curves=False):
    t = stack(records)
    n_runs = len(records)
    correct = t["correct"].astype(bool)
    out = dict(L=L, runs=n_runs, n=int(correct.size), n_correct=int(correct.sum()), inv_L=1.0 / L)
    num, den = per_run(correct, t["run"])
    out["accuracy"], out["ci_lo"], out["ci_hi"] = cluster_boot(num, den, rng)
    _, out["ci_adj_lo"], out["ci_adj_hi"] = cluster_boot(num, den, rng, z=Z_ADJ)
    out["lift"], out["lift_lo"], out["lift_hi"] = out["accuracy"] * L, out["ci_lo"] * L, out["ci_hi"] * L
    num3, _ = per_run(t["rank"] <= 3, t["run"])
    out["top3"], out["top3_lo"], out["top3_hi"] = cluster_boot(num3, den, rng)
    numa, _ = per_run(t["correct_argmax"].astype(bool), t["run"])
    out["accuracy_per_decision"] = float(numa.sum() / den.sum())
    out["random_assignment"] = float(t["rand"].mean())
    out["signal_accuracy"] = bool(out["ci_adj_lo"] > 1.0 / L)
    conf_post, temps = calibrated_confidence(t)
    conf_gap = gap_confidence(t)
    out["temperature"] = temps
    curves = {}
    for name, conf in (("posterior", conf_post), ("gap", conf_gap)):
        a = auc_clustered(conf, correct.astype(int), t["run"])
        out[f"auc_{name}"] = a["auc"]
        out[f"auc_{name}_lo"] = a["auc"] - Z95 * a["se"]
        out[f"auc_{name}_hi"] = a["auc"] + Z95 * a["se"]
        out[f"auc_{name}_adj_lo"] = a["auc"] - Z_ADJ * a["se"]
        cq, iq = quantiles(conf[correct]), quantiles(conf[~correct])
        for k, v in cq.items():
            out[f"{name}_correct_{k}"] = v
        for k, v in iq.items():
            out[f"{name}_incorrect_{k}"] = v
        pc, ycov, best = precision_coverage(conf, correct)
        out[f"{name}_yield_coverage_at_p50"] = ycov
        out[f"{name}_best_precision_cov1"] = best
        for row in pc:
            out[f"{name}_prec_at_{int(row['coverage'] * 100)}"] = row["precision"]
            out[f"{name}_prec_at_{int(row['coverage'] * 100)}_lo"] = row["ci_lo"]
            out[f"{name}_prec_at_{int(row['coverage'] * 100)}_hi"] = row["ci_hi"]
        curves[name] = dict(conf=conf, precision_coverage=pc)
    rel, ece = reliability(conf_post, correct)
    out["ece"] = ece
    enough = out["n_correct"] >= MIN_EACH and (out["n"] - out["n_correct"]) >= MIN_EACH
    out["auc_stable"] = bool(enough)
    per_run_success = out["n_correct"] / max(n_runs, 1)
    out["runs_needed_for_auc"] = (0 if enough else
                                  (math.inf if per_run_success == 0 else int(math.ceil(MIN_EACH / per_run_success))))
    out["signal_auc"] = bool(enough and out["auc_posterior_adj_lo"] > 0.5)
    out["signal"] = out["signal_accuracy"] or out["signal_auc"]
    sh = shuffled(t, rng)
    ns, _ = per_run(sh, t["run"])
    out["shuffled_accuracy"], out["shuffled_lo"], out["shuffled_hi"] = cluster_boot(ns, den, rng)
    a = auc_clustered(conf_post, sh.astype(int), t["run"])
    out["shuffled_auc"], out["shuffled_auc_lo"], out["shuffled_auc_hi"] = a["auc"], a["auc"] - Z95 * a["se"], a["auc"] + Z95 * a["se"]
    # post-hoc negative control (analysis code): outcome labels permuted within each run, so
    # confidence cannot carry information about them; AUC must be ~0.5 and precision at every
    # coverage ~ the overall accuracy
    perm = correct.copy()
    for rid in np.unique(t["run"]):
        m = np.nonzero(t["run"] == rid)[0]
        perm[m] = correct[m][rng.permutation(m.size)]
    a = auc_clustered(conf_post, perm.astype(int), t["run"])
    out["outcome_shuffle_auc"], out["outcome_shuffle_auc_lo"], out["outcome_shuffle_auc_hi"] = \
        a["auc"], a["auc"] - Z95 * a["se"], a["auc"] + Z95 * a["se"]
    _, _, best_perm = precision_coverage(conf_post, perm)
    out["outcome_shuffle_best_precision_cov1"] = best_perm
    if with_curves:
        curves["correct"] = correct
        curves["reliability"] = rel
        return out, curves
    return out


def paired_difference(role_recs, n_recs, rng):
    """Role minus N(a) (or any other scenario) on the same transactions of the same runs:
    mean difference in correctness, cluster-bootstrap CI. A role with several rows per transaction
    (the gatekeepers) is compared row by row with the transaction's single N row."""
    nmap = {}
    for r in n_recs:
        nmap[r["run"]] = dict(zip(r["sub"].tolist(), r["correct"].tolist()))
    diffs, den = [], []
    for r in role_recs:
        m = nmap.get(r["run"])
        if m is None:
            continue
        nc = np.array([m.get(s, np.nan) for s in r["sub"].tolist()], float)
        ok = np.isfinite(nc)
        diffs.append((r["correct"][ok] - nc[ok]).sum())
        den.append(ok.sum())
    if not den:
        return dict(diff=math.nan, lo=math.nan, hi=math.nan, n=0)
    d, lo, hi = cluster_boot(np.array(diffs), np.array(den), rng)
    return dict(diff=d, lo=lo, hi=hi, n=int(sum(den)))

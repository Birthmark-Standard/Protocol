"""The hold lottery and the empirical likelihoods built from it.

Every node holds packets on a node-wide clock of 10-second ticks with a random phase, so a release
lands on the node's own grid and carries no trace of the packet's arrival phase. Each hold has its
own mean: at every tick the packet is released with a fixed probability, and it is released
unconditionally at three times the mean. A device's hold uses an independent random phase per
channel.

The attacks' likelihoods are built by Monte Carlo simulation of the whole process (the multi-hop
total has no closed form), then histogramming.
"""
from __future__ import annotations

import numpy as np

from . import params as P


def next_tick(t, phase):
    """First tick of a clock with the given phase strictly after time t."""
    return phase + P.TICK_S * (np.floor((t - phase) / P.TICK_S) + 1.0)


_P_CACHE = {}


def stage_lottery(mean_s):
    """Per-tick release probability and cap (in ticks) for a hold of the given mean, with the cap at
    three times the mean. The first tick follows a uniform wait (mean 5 s), so the probability
    solves 5 + 10 (E[min(G, K)] - 1) = mean, where E[min(G, K)] = sum_{j<K} (1-p)^j."""
    if mean_s in _P_CACHE:
        return _P_CACHE[mean_s]
    K = max(1, int(round(P.CAP_FACTOR * mean_s / P.TICK_S)))
    target = (mean_s + P.TICK_S / 2) / P.TICK_S
    lo, hi = 1e-6, 1.0
    for _ in range(100):
        p = 0.5 * (lo + hi)
        s = (1 - (1 - p) ** K) / p
        lo, hi = (p, hi) if s > target else (lo, p)
    _P_CACHE[mean_s] = (0.5 * (lo + hi), K)
    return _P_CACHE[mean_s]


def hold(rng, t_arrive, phase, mean_s):
    """Release time of a hold: 10-second ticks on a clock with the given phase (None: a fresh random
    phase per packet), geometric release, forced release at three times the mean. The draws are
    always taken, so a hold switched off (mean 0) leaves every later draw unchanged."""
    t = np.asarray(t_arrive, dtype=float)
    n = t.shape[0]
    ph = rng.uniform(0.0, P.TICK_S, size=n) if phase is None else phase
    p, K = stage_lottery(mean_s if mean_s > 0 else 30.0)
    k = np.minimum(rng.geometric(p, size=n), K)
    if mean_s <= 0:
        return t.copy()
    return next_tick(t, ph) + P.TICK_S * (k - 1)


def inclusion_departure(rng, ready, phase, window_s, p_board, max_boundaries):
    """Departure bundling with an inclusion lottery: from the first boundary of the window grid after
    the packet is ready, it draws p_board at each boundary for a place in that boundary's bundle;
    after max_boundaries - 1 misses it boards unconditionally."""
    ready = np.asarray(ready, dtype=float)
    k = np.minimum(rng.geometric(p_board, size=ready.shape[0]), max_boundaries)
    first = phase + window_s * np.ceil((ready - phase) / window_s)
    return first + window_s * (k - 1)


class EmpiricalLogPDF:
    """Histogram density of Monte-Carlo samples, evaluated as a log-likelihood.

    Out-of-support values get -inf; empty in-support bins get a small floor so a single
    unlucky bin can't veto an otherwise plausible match."""

    def __init__(self, samples, bin_width, lo=None, hi=None, floor_frac=1e-3):
        samples = np.asarray(samples, dtype=float)
        lo = samples.min() if lo is None else lo
        hi = samples.max() if hi is None else hi
        self.lo, self.bw = lo, bin_width
        nb = int(np.ceil((hi - lo) / bin_width)) + 1
        counts = np.bincount(np.clip(((samples - lo) / bin_width).astype(np.int64), 0, nb - 1),
                             minlength=nb).astype(float)
        dens = counts / (counts.sum() * bin_width)
        floor = floor_frac * dens[dens > 0].min()
        self.logd = np.log(np.maximum(dens, floor))
        self.support = (samples.min() - bin_width, samples.max() + bin_width)

    def __call__(self, x):
        x = np.asarray(x, dtype=float)
        idx = np.floor((x - self.lo) / self.bw).astype(np.int64)
        ok = (x >= self.support[0]) & (x <= self.support[1]) & (idx >= 0) & (idx < self.logd.shape[0])
        out = np.full(x.shape, -np.inf)
        out[ok] = self.logd[idx[ok]]
        return out

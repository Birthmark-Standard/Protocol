"""The relay timing lottery and the empirical likelihoods built from it.

Every node holds packets on one node-wide clock of 10-second ticks with a random phase, so a
release lands on the node's own grid and carries no trace of the packet's arrival phase. A
device's hold before each first hop uses an independent random phase per channel. Gatekeepers
hold on a dedicated hold clock with its own phase.

The attacks' likelihoods are built by Monte Carlo simulation of the whole process (the multi-hop
total has no closed form), then histogramming.
"""
from __future__ import annotations

import numpy as np

from . import params as P


def draw_ticks(rng, n, scale=1.0):
    """Number of ticks until release: roll p each tick, forced release at tick 30. A scale k
    stretches the lottery: release probability p / k and forced release at tick 30 k, so the mean
    and the cap grow by k and the share released by the cap stays the same."""
    if scale == 1.0:
        return np.minimum(rng.geometric(P.RELEASE_P, size=n), P.MAX_TICKS)
    return np.minimum(rng.geometric(P.RELEASE_P / scale, size=n), int(round(P.MAX_TICKS * scale)))


def next_tick(t, phase):
    """First tick of a clock with the given phase strictly after time t."""
    return phase + P.TICK_S * (np.floor((t - phase) / P.TICK_S) + 1.0)


def release_time(rng, t_arrive, phase, enabled: bool = True, scale=1.0):
    """Release time of a packet that entered a holding pool at t_arrive, on a clock with the
    given phase."""
    t_arrive = np.asarray(t_arrive, dtype=float)
    if not enabled:
        return t_arrive.copy()
    k = draw_ticks(rng, t_arrive.shape[0], scale)
    return next_tick(t_arrive, phase) + P.TICK_S * (k - 1)


def device_release(rng, t0, enabled: bool = True, scale=1.0):
    """Release of one channel's first hop from the device, on a fresh random phase per channel."""
    t0 = np.asarray(t0, dtype=float)
    if not enabled:
        return t0.copy()
    phase = rng.uniform(0.0, P.TICK_S, size=t0.shape[0])
    return next_tick(t0, phase) + P.TICK_S * (draw_ticks(rng, t0.shape[0], scale) - 1)


def lottery_mean_s() -> float:
    q = 1.0 - P.RELEASE_P
    return P.TICK_S * sum(q ** k for k in range(P.MAX_TICKS))


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


# --------------------------------------------------------------------------- Run10 stage holds
_P_CACHE = {}


def stage_lottery(mean_s):
    """Per-tick release probability and cap (in ticks) for a hold of the given mean on 10-second
    ticks, with the cap at three times the mean. The first tick follows a uniform wait (mean 5 s), so
    the probability solves 5 + 10 (E[min(G, K)] - 1) = mean, where E[min(G, K)] = sum_{j<K} (1-p)^j."""
    if mean_s in _P_CACHE:
        return _P_CACHE[mean_s]
    K = max(1, int(round(3.0 * mean_s / P.TICK_S)))
    target = (mean_s + P.TICK_S / 2) / P.TICK_S
    lo, hi = 1e-6, 1.0
    for _ in range(100):
        p = 0.5 * (lo + hi)
        s = (1 - (1 - p) ** K) / p
        lo, hi = (p, hi) if s > target else (lo, p)
    _P_CACHE[mean_s] = (0.5 * (lo + hi), K)
    return _P_CACHE[mean_s]


def hold(rng, t_arrive, phase, enabled, mean_s):
    """Release time of a Run10 stage hold: 10-second ticks on a clock with the given phase (None: a
    fresh random phase per packet), geometric release, forced release at three times the mean. The
    draws are always taken, so a stage switched off (mean 0) leaves every later draw unchanged."""
    t = np.asarray(t_arrive, dtype=float)
    n = t.shape[0]
    ph = rng.uniform(0.0, P.TICK_S, size=n) if phase is None else phase
    p, K = stage_lottery(mean_s if mean_s > 0 else 30.0)
    k = np.minimum(rng.geometric(p, size=n), K)
    if not enabled or mean_s <= 0:
        return t.copy()
    return next_tick(t, ph) + P.TICK_S * (k - 1)


def inclusion_departure(rng, ready, phase, window_s, p_board, max_boundaries):
    """Departure bundling with an inclusion lottery: from the first boundary of the window grid after
    the packet is ready, it draws p_board at each boundary for a place in that boundary's bundle;
    after max_boundaries misses it boards unconditionally."""
    ready = np.asarray(ready, dtype=float)
    k = np.minimum(rng.geometric(p_board, size=ready.shape[0]), max_boundaries)
    first = phase + window_s * np.ceil((ready - phase) / window_s)
    return first + window_s * (k - 1)

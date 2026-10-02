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

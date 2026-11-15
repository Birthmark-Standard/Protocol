"""Device-level scores per record, for vantages built on top of the scoring engine.

A vantage here ends with, for each record, a log score per device. The scores are turned into the same
per-decision table the other vantages write (attacks._table), so the analysis treats every vantage alike.
These vantages decide at the device level only: their submission-level columns repeat the device level.
"""
from __future__ import annotations

import numpy as np

from . import attacks as AT

T_GRID = AT.T_GRID


class Collector:
    """Collects, per record row, the device labels and the log of the summed posterior per device from the
    score blocks of attacks.score_blocks (as an extra hook or a compute hook)."""

    def __init__(self, n, cand_dev):
        self.lab = [None] * n
        self.sc = [None] * n
        self.cand_dev = cand_dev

    def __call__(self, rows, lo, hi, W):
        grp = AT._groups(self.cand_dev[lo:hi])
        Wd, u = AT._aggregate(W, grp)
        fin = np.isfinite(Wd)
        for i, r in enumerate(rows):
            m = fin[i]
            self.lab[r] = u[m]
            self.sc[r] = Wd[i, m]

    def get(self, r):
        if self.lab[r] is None:
            return np.zeros(0, np.int64), np.zeros(0)
        return self.lab[r], self.sc[r]


def outcome(labels, scores, truth_dev, shuf):
    """The decision arrays of one vantage from per-row (labels, scores): pick (the first maximum, labels in
    ascending order, as the engine breaks ties), correctness, top scores, feasible counts, the calibrated-
    confidence terms, and the same decision under the shuffled labels. Returns the dict layout of
    attacks.score_blocks for one name ({"dev", "sub", "shuf"})."""
    n = len(labels)
    o = {lvl: AT._empty(n, lvl == "dev") for lvl in ("dev", "sub", "shuf")}
    for i in range(n):
        lab, sc = np.asarray(labels[i]), np.asarray(scores[i], float)
        fin = np.isfinite(sc)
        lab, sc = lab[fin], sc[fin]
        d = o["dev"]
        d["n_feas"][i] = lab.size
        if lab.size == 0:
            continue
        order = np.argsort(lab, kind="stable")
        lab, sc = lab[order], sc[order]
        am = int(np.argmax(sc))
        top = sc[am]
        d["pick"][i], d["top1"][i] = lab[am], top
        d["correct"][i] = lab[am] == truth_dev[i]
        if sc.size >= 2:
            d["top2"][i] = np.partition(-sc, 1)[1] * -1
        t = lab == truth_dev[i]
        d["n_true"][i] = int(t.any())
        d["s_true"][i] = sc[t].max() if t.any() else -np.inf
        for k, T in enumerate(T_GRID):
            x = sc / T
            mx = x.max()
            d["lse"][i, k] = np.log(np.exp(x - mx).sum()) + mx - top / T
        sl = shuf(lab)
        o2 = np.argsort(sl, kind="stable")
        sl2, sc2 = sl[o2], sc[o2]
        k2 = int(np.argmax(sc2))
        s_ = o["shuf"]
        s_["n_feas"][i], s_["n_true"][i] = lab.size, int(t.any())
        s_["pick"][i], s_["top1"][i], s_["correct"][i] = sl2[k2], sc2[k2], sl2[k2] == truth_dev[i]
    for key in ("pick", "correct", "top1", "top2", "s_true", "n_feas", "n_true"):
        o["sub"][key] = o["dev"][key].copy()
    return o


def table(labels, scores, rec, ri, grp, base, truth_dev, shuf, **extra):
    """A per-decision table (attacks._table layout) from per-row device scores. ri: the record row of each
    decision; base: the observer's outcome over the records."""
    o = outcome(labels, scores, truth_dev, shuf)
    return AT._table(o, rec, np.asarray(ri), grp, base, **extra)

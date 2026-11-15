"""Decoy knowledge and decoy concentration (C3 items 1 and 3).

Decoy knowledge. Each decoy identity belongs to one of two decoy operators, drawn with probability one half
from a seed set by the cell and the run. A party that knows an operator's decoys removes their packets from
its candidates. Variants: none known (C2), one operator's decoys known, both known, and the validator of a
manufacturer that keeps records of its credentials (its candidates are real credentials only).

Decoy concentration. Under a concentration factor the decoy identities are fewer and each captures at that
multiple of a device's rate. The discounting attacker counts each source address's captures over the
observed span and weighs each device by the probability that an address with that count is a real device,
from Poisson rates measured on the model seeds.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import poisson

from . import attacks as AT
from . import devscore as DS
from . import sim as S

OPS_SEED = 15_000_000


def operators(run, R, run_id):
    """The two operators' decoy source addresses."""
    ids = np.unique(run.subs["src"][run.subs["decoy"]])
    rng = np.random.default_rng([OPS_SEED, int(R), int(run_id)])
    a = rng.random(ids.size) < 0.5
    return ids[a], ids[~a]


def captures_per_source(run):
    """Captures each external source address made over the run's span, counted from its first-hop packets."""
    ev = run.events
    m = (ev["src"] == S.EXT) & np.isin(ev["leg"], (S.CRED1, S.CA1, S.CB1))
    src, cnt = np.unique(ev["ext_src"][m], return_counts=True)
    return src.astype(np.int64), cnt / 3.0


def rate_model(cfg, seeds):
    """Mean captures over the run's span of a real device and of a decoy identity, and the share of
    identities that are real, from simulations of the same cell on the model seeds."""
    real, dec, n_r, n_d = [], [], 0, 0
    for sd in seeds:
        run = S.simulate(cfg, sd)
        src, c = captures_per_source(run)
        isdec = src >= 100_000
        real.append(c[~isdec])
        dec.append(c[isdec])
        n_r += cfg.real_devices
        n_d += cfg.decoy_sources
    return dict(lam_real=float(np.concatenate(real).mean()), lam_decoy=float(np.concatenate(dec).mean()),
                pi_real=n_r / (n_r + n_d))


def discounted(run, out, col, rm):
    """The observer's device scores plus the log probability that each address is a real device."""
    rec, tie, shuf, base = out["_rec"], out["_tie"], out["_shuf"], out["_base"]
    src, cnt = captures_per_source(run)
    k = np.round(cnt).astype(int)
    lr = rm["pi_real"] * poisson.pmf(k, rm["lam_real"])
    ld = (1 - rm["pi_real"]) * poisson.pmf(k, rm["lam_decoy"])
    with np.errstate(divide="ignore"):
        logp = np.log(lr) - np.log(lr + ld)
    lab_t = tie(src)
    o = np.argsort(lab_t)
    lab_t, logp = lab_t[o], logp[o]
    n = rec["sub"].size
    labs, scs = [], []
    for i in range(n):
        lab, sc = col.get(i)
        pos = np.clip(np.searchsorted(lab_t, lab), 0, lab_t.size - 1)
        add = np.where(lab_t[pos] == lab, logp[pos], -np.inf)
        labs.append(lab)
        scs.append(sc + add)
    return DS.table(labs, scs, rec, np.arange(n), np.zeros(n), base, rec["dev"], shuf)

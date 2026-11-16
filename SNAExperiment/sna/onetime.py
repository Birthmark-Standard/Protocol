"""The blind-issued one-time certificates candidate, on the same relay layer as the credential path.

Per capture the device takes a fresh one-time key whose certificate an issuer signed blind in advance, and signs the
content fields with it. One packet per capture carries ContentHash, the claim and other fields, the one-time public
key, the issuer's signature on it, and the device's signature. It goes through a first relay and a second relay, with
the credential path's relay holds and padding and the same device routing table and wrapping as a content packet, to
one destination Registry Node (uniform over the 20 nodes; the two relays distinct from it and from each other). The
destination submits it on the registry's 120-second shared submission schedule; the submission floods to every node;
every Registry Node verifies the certificate and the device signature, then drops them; the registry posts the record
on its 120-second posting schedule. The posted record carries neither. There is no C, validator, gatekeeper or match
board.

Certificates. Each identity (real device or decoy identity, in its own name) holds a stock. Under the threshold rule,
when a capture leaves the stock at otc_refill_at, the device fetches otc_batch more, directly from its issuer (not
through the relays): the issuer sees the identity, the time and the count. An unused certificate expires after
cert_expiry_s. A capture with no certificate waits on the device until a refill arrives. Each identity's stock starts
at the window from its long-run state: under the threshold rule, uniform over the stocks just before a capture. The
issuers are as many as the validators, with the same split for real devices and for decoys (n_validators,
real_val_split, decoy_val_split), one issuing key each; an identity's issuer is drawn once.

Natural variant: no device hold. Lengthened-hold variant: the device holds the packet (otc_hold_mean, the holds'
10-second lottery) so the end-to-end latency matches the credential path's.

Edits: the editing software takes the device role, with certificates from the developer's issuer, which the issuer
vantages do not score; the record carries the parent ContentHash. Edits come from the capture's own address
(edit_same_source) or from the user's machine, as in the credential path.

Capture times and source addresses are drawn from the same streams, in the same order, as the credential path's, so
one seed gives both candidates the same captures from the same devices.
"""
from __future__ import annotations

import numpy as np

from . import lottery as LT
from . import params as P
from . import sim as S

PK1, PK2, PK3, REG_PK = 20, 21, 22, 23          # the packet's three legs and its registry submission (truth only)
S.LEG_NAMES.update({PK1: "Pkt-1", PK2: "Pkt-2", PK3: "Pkt-3", REG_PK: "Reg"})
NAME = P.CANDIDATES[1]


def is_onetime(cfg) -> bool:
    return cfg.candidate == NAME


def _captures(w, r, rate, n_src, src0, decoy):
    """Capture times and sources, drawn exactly as the credential path draws them, and the first-hop latencies."""
    cfg, H = w.cfg, w.cfg.horizon_s
    kind = "W0" if (cfg.workload == "Wmis" and decoy) else ("W2" if cfg.workload == "Wmis" else cfg.workload)
    if kind == "W0":
        n = int(r.poisson(rate * H)) if rate > 0 else 0
        t0 = np.sort(r.uniform(0, H, n))
        src = src0 + r.integers(0, max(n_src, 1), n)
    else:
        t0, src = S._workload(w, rate, n_src, decoy, kind)
        src = src0 + src
    lat_src = r.uniform(*P.LAT_EXT_MS, size=(max(n_src, 1), P.N_NODES)) / 1000
    w.lat_tab[src0] = lat_src
    return t0, src, lat_src[src - src0]


def _route(r, n):
    """Destination uniform over the nodes; first and second relay distinct from it and from each other."""
    dest = r.integers(0, P.N_NODES, n)
    x = r.random((n, P.N_NODES))
    x[np.arange(n), dest] = 2.0
    rel = np.argsort(x, axis=1)[:, :2]
    return rel[:, 0], rel[:, 1], dest


class Stock:
    """Each identity's certificates under the threshold rule: the issuance time of every certificate held (used oldest
    first), and every refill (identity, time, count)."""

    def __init__(self, cfg, rng):
        self.cfg, self.rng = cfg, rng
        self.held = {}
        self.refills = []

    def _start(self, ident, t):
        b, k = self.cfg.otc_batch, self.cfg.otc_refill_at
        n = int(self.rng.integers(k + 1, k + b + 1))          # long-run state: uniform over the stocks before a capture
        self.held[ident] = list(np.full(n, t - 1.0))

    def take(self, ident, t):
        """A capture at t: the time a certificate is available (t, or the next refill), after which the stock is
        refilled when it falls to the threshold."""
        cfg = self.cfg
        if ident not in self.held:
            self._start(ident, t)
        h = self.held[ident]
        while h and h[0] <= t - cfg.cert_expiry_s:             # expired certificates
            h.pop(0)
        ready = t
        if not h:                                              # none left: the capture waits for a refill
            h.extend([t] * cfg.otc_batch)
            self.refills.append((ident, t, cfg.otc_batch))
        h.pop(0)
        if len(h) <= cfg.otc_refill_at:
            self.refills.append((ident, ready, cfg.otc_batch))
            h.extend([ready] * cfg.otc_batch)
        return ready


def _transactions(w, r, t0, src, lat, sub0, decoy, stock, gen=0, ident=None):
    """The packets of one stream of captures: certificates, the device's hold, the relays, the destination."""
    cfg = w.cfg
    n = t0.size
    sub = sub0 + np.arange(n)
    ready = t0.copy()
    if stock is not None:
        o = np.argsort(t0, kind="stable")
        for i in o:
            ready[i] = stock.take(int(ident[i]), float(t0[i]))
    first, second, dest = _route(r, n)
    (_, _, arr), ev = S._chain(w, r, ready, src, lat, first, second, dest, (PK1, PK2, PK3), sub, cfg.otc_hold_mean)
    reg = arr + S._proc(r, n)
    if cfg.reg_bundle_s > 0:                                   # the registry's shared submission schedule
        ph = w.reg_phase
        reg = ph + cfg.reg_bundle_s * np.ceil((reg - ph) / cfg.reg_bundle_s)
    reg = reg + S._proc(r, n)
    return dict(t0=t0, ready=ready, src=src, decoy=np.full(n, decoy), A=first, B=second, D=dest, arr=arr, reg=reg,
                ev_pk=ev, gen=np.full(n, gen, np.int8))


def _register(w, subs, lo, hi, split, gen):
    """Every submission floods from its destination; the record posts at the next boundary of the posting schedule
    after the flood has reached every node."""
    cfg = w.cfg
    sub = np.arange(lo, hi)
    ev_r, reach = np.full(hi - lo, -1, np.int64), np.full(hi - lo, np.nan)
    for stream, part in enumerate((sub < split, sub >= split)):
        if not part.any():
            continue
        oids, rch = S._gossip(w, subs["D"][lo:hi][part], subs["reg"][lo:hi][part], sub[part],
                              np.full(part.sum(), REG_PK), 2 * gen + stream)
        ev_r[part], reach[part] = oids, rch
    posted = reach if cfg.reg_post_s <= 0 else w.post_phase + cfg.reg_post_s * np.ceil((reach - w.post_phase) / cfg.reg_post_s)
    for k, v in (("ev_reg", ev_r), ("reach", reach), ("intake", reach), ("posted", posted), ("final", posted)):
        if k not in subs or subs[k].shape[0] < hi:
            old = subs.get(k, np.zeros(0, v.dtype))
            subs[k] = np.r_[old, np.full(hi - old.shape[0], -1 if k.startswith("ev_") else np.nan, v.dtype)]
        subs[k][lo:hi] = v


def _cat(a, b):
    return {k: np.concatenate([a[k], b[k]]) for k in a}


def _edits(w, subs, lo, hi):
    """The next generation of edits: each edit of a posted record, from the capture's own address or the user's
    machine, as the credential path draws them (rng_edit)."""
    cfg, e, H = w.cfg, w.rng_edit, w.cfg.horizon_s
    idx = np.arange(lo, hi)
    par = idx[(subs["edits_left"][idx] > 0) & np.isfinite(subs["posted"][idx])]
    if par.size == 0:
        return None
    t0 = subs["posted"][par] + P.EDIT_DELAY_MIN_S + e.exponential(P.EDIT_DELAY_MEAN_S, par.size)
    keep = t0 < H
    par, t0 = par[keep], t0[keep]
    same = e.random(par.size) < cfg.edit_same_source
    dev = subs["src"][par] % P.MACHINE_OFFSET
    src = np.where(same, subs["src"][par], dev + P.MACHINE_OFFSET)
    lat = np.empty((par.size, P.N_NODES))
    for i, (d, s_) in enumerate(zip(dev, src)):
        key = ("lat", int(s_))
        if key not in w.lat_tab:
            w.lat_tab[key] = e.uniform(*P.LAT_EXT_MS, size=P.N_NODES) / 1000
        lat[i] = w.lat_tab[key]
    o = np.argsort(t0, kind="stable")
    return par[o], t0[o], src[o], lat[o]


def simulate(cfg: P.Config, seed: int) -> S.Run:
    """One run of the blind-issued one-time certificates candidate."""
    assert is_onetime(cfg)
    w = S.World(cfg, seed)
    grow = 1.0 + cfg.edits_per_capture
    stock = Stock(cfg, np.random.default_rng([int(seed), 7]))          # the stocks' long-run start
    tr, sr, lr = _captures(w, w.rng_real, cfg.real_rate / grow, cfg.real_devices, 0, False)
    td, sd, ld = _captures(w, w.rng_decoy, cfg.decoy_rate / grow, cfg.decoy_sources, 100_000, True)
    issuer = {}
    for src0, n_src, srcs, dec in ((0, cfg.real_devices, sr, False), (100_000, cfg.decoy_sources, sd, True)):
        issuer[src0] = S._validator_of(w, srcs, src0, n_src, dec)
    real = _transactions(w, w.rng_real, tr, sr, lr, 0, False, stock, ident=sr)
    dec = _transactions(w, w.rng_decoy, td, sd, ld, tr.size, True, stock, ident=sd)
    subs = _cat(real, dec)
    subs["issuer"] = np.r_[issuer[0], issuer[100_000]].astype(np.int8)
    n = subs["t0"].size
    subs["parent"], subs["root"] = np.full(n, -1, np.int64), np.arange(n)
    edited = w.rng_edit.random(n) < cfg.edit_share
    subs["edits_left"] = np.where(edited, 1 + np.minimum(w.rng_edit.poisson(P.EDIT_EXTRA_MEAN, n), P.EDIT_MAX - 1), 0)
    _register(w, subs, 0, n, tr.size, 0)
    lo, hi, gen = 0, n, 0
    while cfg.edit_share > 0:
        nxt = _edits(w, subs, lo, hi)
        if nxt is None:
            break
        gen += 1
        par, t0, src, lat = nxt
        x = _transactions(w, w.rng_edit, t0, src, lat, hi, False, None, gen=gen)
        x["decoy"] = subs["decoy"][par]
        x["issuer"] = np.full(par.size, -1, np.int8)            # the developer's issuer
        x["parent"], x["root"] = par, subs["root"][par]
        x["edits_left"] = subs["edits_left"][par] - 1
        for k in subs:
            if k in x:
                subs[k] = np.r_[subs[k], x[k]]
        lo, hi = hi, hi + par.size
        split = hi                                               # one gossip stream per generation
        _register(w, subs, lo, hi, split, gen)
    events, rank = w.ev.finalize()
    for k, v in subs.items():
        if k.startswith("ev_"):
            subs[k] = np.where(v >= 0, rank[np.maximum(v, 0)], -1)
    run = S.Run(cfg=cfg, events=events, subs=subs, phase=w.phase, gk_phase=w.gk_phase, gk_set=np.zeros(0, np.int64),
                bundle_phase=w.bundle_phase, push_phase=w.push_phase, reg_phase=w.reg_phase, post_phase=w.post_phase,
                horizon=cfg.horizon_s)
    rf = np.array(stock.refills, float).reshape(-1, 3)
    ident = rf[:, 0].astype(np.int64)
    key = {int(s_): int(k) for s_, k in zip(subs["src"], subs["issuer"]) if k >= 0}
    run.refills = dict(src=ident, t=rf[:, 1], n=rf[:, 2].astype(np.int32),
                       issuer=np.array([key.get(int(i), 0) for i in ident], np.int8))
    return run

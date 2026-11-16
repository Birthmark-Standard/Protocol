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
LAST_LAM = {}                                   # the last run's long-run rate of each identity (for checks)


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
        lam = np.full(max(n_src, 1), rate / max(n_src, 1))
    else:
        lam = _long_run_rates(w, rate, n_src, decoy, kind)
        t0, src = S._workload(w, rate, n_src, decoy, kind)
        src = src0 + src
    lat_src = r.uniform(*P.LAT_EXT_MS, size=(max(n_src, 1), P.N_NODES)) / 1000
    w.lat_tab[src0] = lat_src
    w.lam = getattr(w, "lam", {})
    w.lam.update({src0 + i: float(x) for i, x in enumerate(lam)})
    return t0, src, lat_src[src - src0]


def _long_run_rates(w, rate, n_src, decoy, kind):
    """Each identity's long-run capture rate under W1 or W2: the rate factors and sessions sim._workload draws, read
    from a copy of its stream, so the run itself is unchanged."""
    import copy
    rg, n = copy.deepcopy(w.rng_work), max(n_src, 1)
    if rate <= 0:
        return np.zeros(n)
    m = np.exp(rg.normal(-P.W_SIGMA ** 2 / 2, P.W_SIGMA, n))
    m = np.ones(n) if n == 1 else m / m.mean()
    sess = np.zeros(n, bool)
    if kind == "W2":
        sess = np.ones(n, bool) if (n == 1 and not decoy) else rg.random(n) < P.SESSION_SHARE
    boost = 1.0 + (P.SESSION_MULT - 1) * np.mean(P.SESSION_MIN) * 60 * P.SESSION_PER_S
    base = rate * m / np.sum(m * np.where(sess, boost, 1.0))
    return base * np.where(sess, boost, 1.0)


def _route(r, n):
    """Destination uniform over the nodes; first and second relay distinct from it and from each other."""
    dest = r.integers(0, P.N_NODES, n)
    x = r.random((n, P.N_NODES))
    x[np.arange(n), dest] = 2.0
    rel = np.argsort(x, axis=1)[:, :2]
    return rel[:, 0], rel[:, 1], dest


class Stock:
    """Each identity's certificates under the threshold rule: the issuance time of every certificate held (used oldest
    first), and every refill (identity, time, count).

    Issuer withholding (mark_actor "issuer_withhold"): inside each window (withhold_len, one every withhold_len +
    WITHHOLD_GAP_S from the warm-up's end) the target's issuer serves the target and refuses (withhold) or holds to
    the window's end (delay) every other refill of its identities. A refused device asks again at each later
    capture; a device with no certificate left gets its refill when the window ends."""

    def __init__(self, cfg, rng, issuer_of=None, lam=None):
        self.cfg, self.rng = cfg, rng
        self.held = {}
        self.refills = []
        self.lam = lam or {}
        self.sched = {}                                           # random schedule: identity -> (refill times, next index)
        self.stock_seen = []                                      # the stock before each capture inside the window
        self.pending = {}                                         # identity -> the time its held refill is served
        self.issuer_of = issuer_of or {}
        self.attack = cfg.mark_actor == "issuer_withhold"

    def _window_end(self, t):
        """The end of the withholding window containing t, or None."""
        cfg = self.cfg
        if not self.attack or cfg.withhold_len <= 0:
            return None
        period = cfg.withhold_len + P.WITHHOLD_GAP_S
        x = t - cfg.warmup_s
        if x < 0 or np.mod(x, period) >= cfg.withhold_len:
            return None
        return cfg.warmup_s + period * np.floor(x / period) + cfg.withhold_len

    def _blocked(self, ident, t):
        cfg = self.cfg
        if not self.attack or ident == cfg.mark_target or cfg.withhold_mode == "none":
            return None
        tgt = self.issuer_of.get(cfg.mark_target, -1)
        if self.issuer_of.get(ident, -2) != tgt:
            return None
        return self._window_end(t)

    def _start(self, ident, t):
        cfg = self.cfg
        b, k = cfg.otc_batch, cfg.otc_refill_at
        if cfg.otc_refill_rule != "random":
            n = int(self.rng.integers(k + 1, k + b + 1))      # long-run state: uniform over the stocks before a capture
            self.held[ident] = list(np.full(n, t - 1.0))
            return
        # random schedule, long-run state: with more issued than used, the queue of certificates (used oldest
        # first) grows until its oldest reach the expiry age, after which every certificate issued in the last two
        # weeks is still held. So the stock starts as the refills of the two weeks before the window.
        lam = self.lam.get(ident, 0.0)
        t_lo, H = -cfg.cert_expiry_s, cfg.horizon_s
        rho = cfg.otc_random_factor * lam / b
        rt = np.sort(self.rng.uniform(t_lo, H, int(self.rng.poisson(rho * (H - t_lo)))))
        j = int(np.searchsorted(rt, 0.0))
        h = [x for x in rt[:j] for _ in range(b)]
        self.held[ident] = h
        self.sched[ident] = [rt, j]
        self.refills.extend((ident, float(x), b) for x in rt[(rt >= 0.0)])     # the issuer sees every request

    def _scheduled(self, ident, t):
        """Random schedule: every refill due by t arrives; with none held, the capture waits for the next one."""
        rt, j = self.sched[ident]
        h = self.held[ident]
        while j < rt.size and rt[j] <= t:
            h.extend([rt[j]] * self.cfg.otc_batch)
            j += 1
        ready = t
        while not (h and h[-1] > t - self.cfg.cert_expiry_s) and j < rt.size:    # held in order of issuance
            ready = rt[j]
            h.extend([rt[j]] * self.cfg.otc_batch)
            j += 1
        self.sched[ident][1] = j
        return ready

    def finish(self, idents):
        """Random schedule: start the identities that made no capture in the run, so their requests are seen too."""
        if self.cfg.otc_refill_rule == "random":
            for i in idents:
                if i not in self.held:
                    self._start(i, 0.0)

    def take(self, ident, t):
        """A capture at t: the time a certificate is available (t, or the next refill), after which the stock is
        refilled when it falls to the threshold."""
        cfg = self.cfg
        if ident not in self.held:
            self._start(ident, t)
        h = self.held[ident]
        if cfg.otc_refill_rule == "random":
            ready = self._scheduled(ident, t)
            while h and h[0] <= ready - cfg.cert_expiry_s:
                h.pop(0)
            if cfg.warmup_s <= t < cfg.warmup_s + cfg.measure_s:
                self.stock_seen.append(len(h))
            if h:
                h.pop(0)
            return ready
        while h and h[0] <= t - cfg.cert_expiry_s:             # expired certificates
            h.pop(0)
        if cfg.warmup_s <= t < cfg.warmup_s + cfg.measure_s:
            self.stock_seen.append(len(h))
        ready = t
        tp = self.pending.get(ident)
        if tp is not None and (tp <= t or not h):               # a held refill arrives
            ready = max(t, tp)
            h.extend([tp] * cfg.otc_batch)
            self.refills.append((ident, tp, cfg.otc_batch))
            del self.pending[ident]
        if not h:                                              # none left: the capture waits for a refill
            end = self._blocked(ident, t)
            ready = t if end is None else end
            h.extend([ready] * cfg.otc_batch)
            self.refills.append((ident, ready, cfg.otc_batch))
        h.pop(0)
        if len(h) <= cfg.otc_refill_at and ident not in self.pending:
            end = self._blocked(ident, ready)
            if end is None:
                self.refills.append((ident, ready, cfg.otc_batch))
                h.extend([ready] * cfg.otc_batch)
            elif cfg.withhold_mode == "delay":
                self.pending[ident] = end
            # withhold: refused; the device asks again at its next capture
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
    tr, sr, lr = _captures(w, w.rng_real, cfg.real_rate / grow, cfg.real_devices, 0, False)
    td, sd, ld = _captures(w, w.rng_decoy, cfg.decoy_rate / grow, cfg.decoy_sources, 100_000, True)
    issuer = {}
    for src0, n_src, srcs, dec in ((0, cfg.real_devices, sr, False), (100_000, cfg.decoy_sources, sd, True)):
        issuer[src0] = S._validator_of(w, srcs, src0, n_src, dec)
    issuer_of = {int(a): int(b) for src0, srcs in ((0, sr), (100_000, sd)) for a, b in zip(srcs, issuer[src0])}
    if cfg.mark_target >= 0 and cfg.mark_target not in issuer_of and cfg.n_validators > 1:
        issuer_of[cfg.mark_target] = int(w.vkey[0][cfg.mark_target])
    stock = Stock(cfg, np.random.default_rng([int(seed), 7]), issuer_of, getattr(w, "lam", {}))   # the stocks' long-run start
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
    stock.finish(list(getattr(w, "lam", {})))
    LAST_LAM.clear()
    LAST_LAM.update(getattr(w, "lam", {}))
    run.stock_seen = np.array(stock.stock_seen, np.int32)
    rf = np.array(stock.refills, float).reshape(-1, 3)
    rf = rf[np.argsort(rf[:, 1], kind="stable")] if rf.size else rf
    ident = rf[:, 0].astype(np.int64)
    key = {int(s_): int(k) for s_, k in zip(subs["src"], subs["issuer"]) if k >= 0}
    run.refills = dict(src=ident, t=rf[:, 1], n=rf[:, 2].astype(np.int32),
                       issuer=np.array([key.get(int(i), 0) for i in ident], np.int8))
    return run


# =========================================================================== attackers
from . import attacks as AT                                      # noqa: E402
from . import devscore as DS                                     # noqa: E402

TRIGGER = 1.0                                                    # one capture per refill is the refill's own


def _samples(run, acc):
    """True (record, packet) pairs of one model run: y the record time after the packet's send, the first relay's
    hold, the arrival at the destination after the send, and the record time and arrival after the capture."""
    s, ev = run.subs, run.events
    ok = np.nonzero(np.isfinite(s["posted"]))[0]
    e = s["ev_pk"][ok]
    sk = ev["t_send"][e[:, 0]]
    u = s["posted"][ok]
    for k, v in (("y", u - sk), ("fh_x", ev["t_send"][e[:, 1]] - ev["t_arr"][e[:, 0]]), ("cs_x", ev["t_arr"][e[:, 2]] - sk),
                 ("ut", u - s["ready"][ok]), ("at", ev["t_arr"][e[:, 2]] - s["ready"][ok])):
        acc.setdefault(k, []).append(v)


def build_models(cfg, seed0=1_000_000_000, min_samples=300_000, max_runs=200) -> AT.Models:
    """The attackers' densities for this candidate, on the model seeds: g (record after send), fh and cs (the record
    after send given the first relay's hold, and given the arrival at the destination) with their marginals, and
    gT and gA (the record and the arrival after the capture, for the issuer)."""
    mc = cfg.with_(decoy_rate=0.0, real_rate=max(cfg.real_rate, 0.2), mark_actor="")
    scale = max(1.0, cfg.max_delay_s / AT.REF_DELAY_S)
    bw_y, bw_x = AT.BW_Y * scale, AT.BW_X * scale
    acc, k = {}, 0
    while True:
        _samples(simulate(mc, seed0 + k), acc)
        k += 1
        if (sum(x.size for x in acc["y"]) >= min_samples and k >= 3) or k >= max_runs:
            break
    c = {n: np.concatenate(v) for n, v in acc.items()}
    m = AT.Models(mc_runs=k, samples={n: int(v.size) for n, v in c.items()})
    g = LT.EmpiricalLogPDF(c["y"], bw_y)
    m.pdf["g"] = g
    for name in ("fh", "cs"):
        m.pdf[name] = AT.CondPDF(c[name + "_x"], c["y"], g, bw_x)
        m.pdf[name + "_q"] = LT.EmpiricalLogPDF(c[name + "_x"], bw_x)
    m.pdf["gT"] = LT.EmpiricalLogPDF(c["ut"], bw_y)
    m.pdf["gA"] = LT.EmpiricalLogPDF(c["at"], bw_y)
    return m


def _issuer_terms(run, rec, cand, k, dens, at):
    """Issuer k's evidence per record: for each of its identities, log(its rate times the share of captures that do
    not trigger a refill + the sum over its refills of the density of `at` (the record time or the arrival) after the
    refill). Returns (identities, per record (labels, that against the rate alone, that itself))."""
    cfg, rf, s = run.cfg, run.refills, run.subs
    mine = rf["issuer"] == k
    ids = np.unique(rf["src"][mine])
    H = max(cfg.horizon_s, 1.0)
    out = []
    t_by = {int(i): np.sort(rf["t"][mine & (rf["src"] == i)]) for i in ids}
    lam = {i: max(t.size, 1) * cfg.otc_batch / H for i, t in t_by.items()}   # the long-run rate, from its refills
    if cfg.otc_refill_rule == "random":
        lam = {i: v / cfg.otc_random_factor for i, v in lam.items()}
    lo, hi = dens.support
    for x in at:
        labs, lr = [], []
        for i, t in t_by.items():
            j0, j1 = np.searchsorted(t, x - hi), np.searchsorted(t, x - lo, "right")
            hit = np.exp(dens(x - t[j0:j1])).sum() * TRIGGER if j1 > j0 else 0.0
            if cfg.otc_refill_rule == "random":                # refills say nothing about captures
                labs.append(i)
                lr.append((np.log(lam[i]), np.log(lam[i])))
                continue
            labs.append(i)
            lr.append((np.log(lam[i] * (1 - 1 / cfg.otc_batch) + hit), np.log(lam[i])))
        a = np.array(lr).reshape(-1, 2)
        out.append((np.array(labs, np.int64), a[:, 0] - a[:, 1], a[:, 0]))
    return ids, out


def compute(run, m, rng, hooks=None, pick=None):
    """Every vantage of this candidate on one run, in the tables of attacks._table:
      observer                  the passive observer
      first_hop                 each node as first relay: its own holds (group: the node)
      destination               each node, on the records it was the destination of: its packet's arrival and the
                                record (group: the node)
      destination_keyed         the same, told each source address's issuer (an upper bound), so it competes only among
                                the identities of the packet's issuer, which it learns from the certificate
      first_relay_with_destination  the record's own first relay and destination: the inner packet matched exactly
      issuer_k                  issuer k alone: its identities' refill times and rates (column own: the record's device
                                is one of its identities)
      issuer_k_with_observer    issuer k's evidence on its identities, added to the observer's
      issuer_k_with_first_relay issuer k with one first relay (drawn per run by pick)
      issuer_k_with_destination issuer k with the record's destination Registry Node, on the records whose packet it
                                issued: the destination's evidence among issuer k's identities, with the refill times
                                against the arrival."""
    hooks = hooks or {}
    pdf, s, ev = m.pdf, run.subs, run.events
    g = pdf["g"]
    rec = AT.records(run)
    keep = AT.scored_mask(run, rec["sub"])
    rec = {k: x[keep] for k, x in rec.items()}
    cand = AT.candidates(run)
    labels = np.unique(np.r_[cand["dev"], s["src"]])
    tie = AT._relabel(labels, rng)
    raw_dev = cand["dev"].copy()
    cand["dev"], rec["dev"] = tie(cand["dev"]), tie(rec["dev"])
    shuf = AT._relabel(np.unique(tie(labels)), rng)
    cand["dev_shuf"] = shuf(cand["dev"])
    srow, u, n = rec["sub"], rec["u"], rec["sub"].size
    idx = np.arange(n)
    truth = dict(sub=srow, dev=rec["dev"])
    out = {}
    col = DS.Collector(n, cand["dev"])
    if "init" in hooks:
        hooks["init"](cand, rec, g)

    def obs_extra(nm, rows, lo_, hi_, W, is_t):
        col(rows, lo_, hi_, W)
        if "observer" in hooks:
            hooks["observer"](rows, lo_, hi_, W)
    lo, hi = AT._band(u, g)
    res = AT.score_blocks(lo, hi, cand, lambda rows, k0, k1: dict(observer=g(u[rows][:, None] - cand["t"][None, k0:k1])),
                          truth, ("observer",), lse=("observer",), extra=obs_extra)
    base = res["observer"]
    out["observer"] = AT._table(base, rec, idx, np.zeros(n), base)
    obs_scores = [col.get(i) for i in range(n)]
    # first relays
    fh = pdf["fh"]
    parts = []
    for X in range(P.N_NODES):
        mine = cand["node"][:, 0] == X
        hold = np.where(mine, cand["hold"][:, 0], np.nan)

        def fn(rows, k0, k1, mine=mine, hold=hold):
            y = u[rows][:, None] - cand["t"][None, k0:k1]
            lg = g(y)
            own = mine[None, k0:k1] & np.isfinite(lg)
            return dict(v=np.where(own, fh(hold[None, k0:k1], y), lg))
        r = AT.score_blocks(lo, hi, cand, fn, truth, ("v",), lse=("v",))
        parts.append(AT._table(r["v"], rec, idx, np.full(n, X), base, took_part=(s["A"][srow] == X).astype(np.int8)))
    out["first_hop"] = AT._cat(parts)
    # destination: each record scored by its own destination
    cs, csq = pdf["cs"], pdf["cs_q"]
    arr = s["arr"][srow]
    clo, chi = arr - csq.support[1], arr - csq.support[0]
    key_of = {int(a): int(b) for a, b in zip(s["src"], s["issuer"])}
    ckey = np.array([key_of.get(int(d), -1) for d in raw_dev], np.int64)
    rkey = s["issuer"][srow].astype(np.int64)
    colk = DS.Collector(n, cand["dev"])
    coli = DS.Collector(n, cand["dev"])

    def dfn(rows, k0, k1):
        x = arr[rows][:, None] - cand["t"][None, k0:k1]
        v = cs(x, u[rows][:, None] - cand["t"][None, k0:k1]) + csq(x)
        same = ckey[None, k0:k1] == rkey[rows][:, None]
        return dict(destination=v, destination_keyed=np.where(same, v, -np.inf))

    def dextra(nm, rows, a, b, W, is_t):
        if nm == "destination_keyed":
            colk(rows, a, b, W)
    r = AT.score_blocks(clo, chi, cand, dfn, truth, ("destination", "destination_keyed"), lse=("destination", "destination_keyed"),
                        extra=dextra)
    grp = s["D"][srow]
    out["destination"] = AT._table(r["destination"], rec, idx, grp, base, issuer=rkey.astype(np.int8))
    out["destination_keyed"] = AT._table(r["destination_keyed"], rec, idx, grp, base, issuer=rkey.astype(np.int8))
    keyed_scores = [colk.get(i) for i in range(n)]
    # first relay with the destination on its path: the source address of the matched packet
    out["first_relay_with_destination"] = DS.table([np.array([d]) for d in rec["dev"]], [np.zeros(1)] * n, rec, idx,
                                                   s["A"][srow] * 32 + s["D"][srow], base, rec["dev"], shuf)
    # issuers
    gT, gA = pdf["gT"], pdf["gA"]
    nk = max(1, run.cfg.n_validators)
    X1 = pick if pick is not None else int(rng.integers(0, P.N_NODES))
    fh_scores = None
    for k in range(nk):
        ids, terms = _issuer_terms(run, rec, cand, k, gT, u)
        tids = tie(ids) if ids.size else ids
        own = (rkey == k).astype(np.int8)
        labs, scs, lo_, so_ = [], [], [], []
        for i, (lab, lr, ab) in enumerate(terms):
            tl = tie(lab) if lab.size else lab
            o = np.argsort(tl)
            labs.append(tl[o]); scs.append(ab[o])
            ol, os_ = obs_scores[i]
            add = np.zeros(ol.size)
            pos = np.searchsorted(tl[o], ol)
            hit = (pos < tl.size) & (tl[o][np.minimum(pos, max(tl.size - 1, 0))] == ol) if tl.size else np.zeros(ol.size, bool)
            add[hit] = lr[o][pos[hit]]
            lo_.append(ol); so_.append(os_ + add)
        out[f"issuer_{k}"] = DS.table(labs, scs, rec, idx, np.full(n, k), base, rec["dev"], shuf, own=own)
        out[f"issuer_{k}_with_observer"] = DS.table(lo_, so_, rec, idx, np.full(n, k), base, rec["dev"], shuf, own=own)
        # with one first relay: its own holds on the observer's scores, plus the issuer's evidence
        if fh_scores is None:
            colf = DS.Collector(n, cand["dev"])
            minef = cand["node"][:, 0] == X1
            holdf = np.where(minef, cand["hold"][:, 0], np.nan)

            def ffn(rows, k0, k1):
                y = u[rows][:, None] - cand["t"][None, k0:k1]
                lg = g(y)
                own_ = minef[None, k0:k1] & np.isfinite(lg)
                return dict(v=np.where(own_, fh(holdf[None, k0:k1], y), lg))
            AT.score_blocks(lo, hi, cand, ffn, truth, ("v",), extra=lambda nm, rows, a, b, W, is_t: colf(rows, a, b, W))
            fh_scores = [colf.get(i) for i in range(n)]
        lf, sf = [], []
        for i, (lab, lr, _) in enumerate(terms):
            fl, fs = fh_scores[i]
            tl = tie(lab) if lab.size else lab
            o = np.argsort(tl)
            add = np.zeros(fl.size)
            if tl.size:
                pos = np.searchsorted(tl[o], fl)
                hit = (pos < tl.size) & (tl[o][np.minimum(pos, tl.size - 1)] == fl)
                add[hit] = lr[o][pos[hit]]
            lf.append(fl); sf.append(fs + add)
        out[f"issuer_{k}_with_first_relay"] = DS.table(lf, sf, rec, idx, np.full(n, X1), base, rec["dev"], shuf, own=own)
        # with the destination: on records whose packet this issuer signed, the keyed destination plus the refills
        # against the arrival
        _, tA = _issuer_terms(run, rec, cand, k, gA, arr)
        ld, sd = [], []
        for i, (lab, lr, _) in enumerate(tA):
            kl, ks = keyed_scores[i]
            if rkey[i] != k or kl.size == 0:
                ld.append(np.zeros(0, np.int64)); sd.append(np.zeros(0))
                continue
            tl = tie(lab) if lab.size else lab
            o = np.argsort(tl)
            add = np.zeros(kl.size)
            if tl.size:
                pos = np.searchsorted(tl[o], kl)
                hit = (pos < tl.size) & (tl[o][np.minimum(pos, tl.size - 1)] == kl)
                add[hit] = lr[o][pos[hit]]
            ld.append(kl); sd.append(ks + add)
        sel = np.nonzero(rkey == k)[0]
        out[f"issuer_{k}_with_destination"] = DS.table([ld[i] for i in sel], [sd[i] for i in sel], rec, sel, np.full(sel.size, k),
                                                       base, rec["dev"][sel], shuf)
    out["_cand"], out["_rec"], out["_tie"], out["_shuf"], out["_base"] = cand, rec, tie, shuf, base
    return out


def issuer_find(run, pdf, rng, window):
    """Record-finding by the target's issuer: for each refill of the target inside a withholding window (the capture
    that triggered it is known to the issuer), the record whose time best fits the density of the record after the
    capture; right when it is that capture's record. The same fields as active.score."""
    cfg, s, rf = run.cfg, run.subs, run.refills
    st = Stock(cfg, None)
    a = rf["t"][(rf["src"] == cfg.mark_target)]
    a = a[(a >= window[0]) & (a < window[1])]
    a = np.array([x for x in a if st._window_end(x) is not None])        # only the target's refills inside a window
    tgt = np.array([np.nonzero((s["src"] == cfg.mark_target) & ~s["decoy"] & (np.abs(s["ready"] - x) < 1e-9))[0][:1] for x in a],
                   dtype=object)
    target = np.array([int(t[0]) if len(t) else -1 for t in tgt], np.int64)
    fin = np.nonzero(np.isfinite(s["posted"]))[0]
    o = np.argsort(s["posted"][fin], kind="stable")
    rs, ru = fin[o], s["posted"][fin][o]
    lo, hi = pdf.support
    n = a.size
    nT = AT.T_GRID.size
    correct, nfeas, rank = np.zeros(n, np.int8), np.zeros(n, np.int32), np.full(n, -1, np.int32)
    top1, s_true = np.full(n, -np.inf), np.full(n, -np.inf)
    lse, ent = np.full((n, nT), np.nan), np.full((n, nT), np.nan)
    for i in range(n):
        b0, b1 = np.searchsorted(ru, a[i] + lo, "left"), np.searchsorted(ru, a[i] + hi, "right")
        if b1 <= b0:
            continue
        sc = pdf(ru[b0:b1] - a[i])
        ok = np.isfinite(sc)
        nfeas[i] = int(ok.sum())
        if not ok.any():
            continue
        best = np.nonzero(sc == sc[ok].max())[0]
        correct[i] = int(target[i] >= 0 and rs[b0:b1][best[rng.integers(0, best.size)]] == target[i])
        top1[i] = sc[ok].max()
        is_t = (rs[b0:b1] == target[i]) & ok
        if is_t.any():
            s_true[i] = sc[is_t].max()
        rank[i] = int((sc[ok] > s_true[i]).sum()) if is_t.any() else nfeas[i]
        for k, T in enumerate(AT.T_GRID):
            x = sc[ok] / T
            lse[i, k] = np.log(np.exp(x - x.max()).sum()) + x.max() - top1[i] / T
            ent[i, k] = AT._entropy(sc[ok][None, :], T)[0]
    rand = np.where(np.isfinite(s_true) & (nfeas > 0), 1.0 / np.maximum(nfeas, 1), 0.0)
    return dict(sub=np.maximum(target, 0).astype(np.int32), correct=correct, has_record=(target >= 0).astype(np.int8), n_feas=nfeas,
                path=np.full(n, 5, np.int8), dev_v_correct=correct, dev_v_rand=rand.astype(np.float32), dev_n_feas=nfeas,
                dev_top1=top1.astype(np.float32), dev_s_true=s_true.astype(np.float32), dev_lse=lse.astype(np.float16),
                dev_ent=ent.astype(np.float16), dev_rank=rank)

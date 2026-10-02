"""Vectorised generator of one run's complete wire trace, real and decoy traffic together.

Output: an event table (one row per message on a link, as a passive observer of every link sees
it: send and arrival times, endpoints, wire size, record type) plus hidden truth columns (leg,
transaction) and a per-transaction truth table used only for scoring.

Random streams. One run seed is split into independent streams for the world (latencies, clock
phases, gatekeeper set, gossip mesh), the real transactions, the decoy transactions, background
traffic and non-blending traffic. Real traffic is therefore identical, event for event, whatever
the decoy volume and whether background traffic is on, which makes every comparison across decoy
volume paired on the same real transactions.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from . import lottery as LT
from . import params as P
from .pools import Pools

EXT = 99                  # every external host (device, decoy source, background client)
VAL = P.N_NODES           # the validator's node id

# leg codes (truth only)
CRED1, CRED2, CRED3, CA1, CA2, CA3, CB1, CB2, CB3 = range(1, 10)
CV1, CV2, GK1, GK2, GK3, REG_F, REG_I, REG_RELAY = range(10, 18)
LEG_NAMES = {CRED1: "Cred-1", CRED2: "Cred-2", CRED3: "Cred-3", CA1: "ContA-1", CA2: "ContA-2", CA3: "ContA-3",
             CB1: "ContB-1", CB2: "ContB-2", CB3: "ContB-3", CV1: "CV-1", CV2: "CV-2", GK1: "GK-1", GK2: "GK-2",
             GK3: "GK-3", REG_F: "Reg-F", REG_I: "Reg-I", REG_RELAY: "Reg relay"}
K_BIRTHMARK, K_BLEND, K_BULK, K_KEEPALIVE = 0, 1, 2, 3


class _Events:
    """Column buffers, finalised into one table sorted by send time."""
    COLS = ("t_send", "t_arr", "src", "dst", "size", "rtype", "kind", "leg", "sub", "ext_src", "ext_dst")
    DT = dict(t_send=np.float64, t_arr=np.float64, src=np.int16, dst=np.int16, size=np.int32,
              rtype=np.int16, kind=np.int8, leg=np.int8, sub=np.int32, ext_src=np.int32, ext_dst=np.int32)

    def __init__(self):
        self.parts = {c: [] for c in self.COLS}
        self.n = 0

    def add(self, t_send, t_arr, src, dst, size, rtype, kind, leg=0, sub=-1, ext_src=-1, ext_dst=-1):
        t_send = np.asarray(t_send, dtype=float)
        n = t_send.shape[0]
        if n == 0:
            return np.zeros(0, dtype=np.int64)
        vals = dict(t_send=t_send, t_arr=t_arr, src=src, dst=dst, size=size, rtype=rtype, kind=kind,
                    leg=leg, sub=sub, ext_src=ext_src, ext_dst=ext_dst)
        for c in self.COLS:
            self.parts[c].append(np.broadcast_to(np.asarray(vals[c]), (n,)).astype(self.DT[c]))
        ids = np.arange(self.n, self.n + n)
        self.n += n
        return ids

    def finalize(self):
        cols = {c: np.concatenate(self.parts[c]) for c in self.COLS}
        order = np.argsort(cols["t_send"], kind="stable")
        rank = np.empty_like(order)
        rank[order] = np.arange(order.shape[0])
        return {c: v[order] for c, v in cols.items()}, rank


@dataclass
class Run:
    cfg: P.Config
    events: dict
    subs: dict              # per-transaction truth; ev_* are row indices into events
    phase: np.ndarray       # node clock phases
    gk_phase: np.ndarray    # gatekeeper hold-clock phases (per node; used for the active three)
    gk_set: np.ndarray
    horizon: float
    bundle_phase: np.ndarray = None
    push_phase: np.ndarray = None
    reg_phase: float = 0.0


class World:
    def __init__(self, cfg: P.Config, seed: int, pools: Pools):
        self.cfg, self.pools = cfg, pools
        ss = np.random.SeedSequence(seed)
        streams = ss.spawn(9)
        (self.rng_world, self.rng_real, self.rng_decoy, self.rng_bg, self.rng_nb, rng_bundle, rng_push,
         self.rng_gkhold, rng_reg) = (np.random.default_rng(s) for s in streams)
        # each gatekeeper's departure-bundle grid phase, on its own stream, so bundling on or off
        # leaves every other draw unchanged
        self.bundle_phase = rng_bundle.uniform(0, P.BUNDLE_S, P.N_NODES)
        # each match board's push schedule phase, on its own stream
        self.push_phase = rng_push.uniform(0, P.BOARD_PUSH_S, P.N_NODES)
        # the registry-level bundle schedule: one phase shared by every content server
        self.reg_phase = float(rng_reg.uniform(0, max(cfg.reg_bundle_s, 1.0)))
        r = self.rng_world
        n_int = P.N_NODES + P.N_VALIDATORS
        base = r.uniform(*P.LAT_INT_MS, size=(n_int, n_int)) / 1000
        self.lat_int = (base + base.T) / 2
        self.phase = r.uniform(0, P.TICK_S, P.N_NODES)
        self.gk_phase = r.uniform(0, P.TICK_S, P.N_NODES)
        self.gk_set = np.sort(r.permutation(P.N_NODES)[:P.N_GATEKEEPERS])
        self.mesh = _mesh(r)
        self.gossip_seed = int(r.integers(0, 2 ** 62))
        self.ev = _Events()

    def size(self, rng, cls, n):
        """Wire size of a transit leg: a target drawn uniformly from its padding class, plus the
        measured TLS 1.3 record overhead."""
        lo, hi = P.PAD_GK if cls == "GK" else (P.PAD_MIN, P.PAD_MAX)
        return rng.integers(lo, hi + 1, n) + self.pools.tls13_overhead


def _mesh(rng):
    """6-regular gossip mesh: circulant i +- 1, 2, 3 over a random node ordering."""
    order = rng.permutation(P.N_NODES)
    pos = np.empty_like(order)
    pos[order] = np.arange(P.N_NODES)
    half = P.GOSSIP_MESH_D // 2
    return {v: [int(order[(pos[v] + k) % P.N_NODES]) for k in list(range(1, half + 1)) + list(range(-half, 0))]
            for v in range(P.N_NODES)}


# --------------------------------------------------------------------------- transactions
def _roles(r, S, gk_set):
    """Nine distinct nodes per transaction. C, F and I never belong to the active gatekeeper set;
    the first hops (A, D, G) and random hops (B, E, H) are drawn from the other 17 nodes, so the
    three paths share no node, a first hop is never C, F or I, and a gatekeeper may relay."""
    N = P.N_NODES
    pool = np.setdiff1d(np.arange(N), gk_set)
    cfi = pool[np.argsort(r.random((S, pool.size)), axis=1)[:, :3]]
    x = r.random((S, N))
    idx = np.arange(S)[:, None]
    x[idx, cfi] = 2.0
    rest = np.argsort(x, axis=1)[:, :6]
    C, F, I = cfi.T
    A, B, D, E, G, H = rest.T
    return C, F, I, A, B, D, E, G, H


def _chain(w, r, t0, src_id, lat_src, first, second, dest, legs, sub, scale=1.0):
    """Device (or decoy source) -> addressed hop -> random hop -> destination. scale stretches the
    device's hold and both relay hops' holds on this path."""
    cfg, n = w.cfg, t0.shape[0]
    on = cfg.lottery_enabled
    dep = LT.device_release(r, t0, on, scale) + _proc(r, n)
    arr = dep + lat_src[np.arange(n), first] + _jit(r, n)
    ids = [w.ev.add(dep, arr, EXT, first, w.size(r, "relay", n), P.RT_APPDATA, K_BIRTHMARK, legs[0], sub,
                    ext_src=src_id)]
    arrs = [arr]
    cur = first
    for nxt, leg in ((second, legs[1]), (dest, legs[2])):
        rel = LT.release_time(r, arr, w.phase[cur], on, scale) + _proc(r, n)
        arr = rel + w.lat_int[cur, nxt] + _jit(r, n)
        ids.append(w.ev.add(rel, arr, cur, nxt, w.size(r, "relay", n), P.RT_APPDATA, K_BIRTHMARK, leg, sub))
        arrs.append(arr)
        cur = nxt
    return arrs, np.stack(ids, 1)


def _jit(r, n):
    return r.exponential(P.JITTER_MS / 1000, n)


def _proc(r, n):
    return r.uniform(*P.PROC_MS, n) / 1000


def _content_server(w, r, arr, node):
    """Hold on the node clock. Returns the hold release time."""
    return LT.release_time(r, arr, w.phase[node], w.cfg.lottery_enabled)


def _pushed(w, posts, node):
    """When a content server learns of quorum. Each board pushes every match posted since its
    last push to every content server on its own schedule; the server learns of quorum when the
    second of the three boards' pushes carrying the match reaches it. The server never queries a
    board itself. Pushes go to every server on a fixed schedule whatever they carry, and are
    internal to the board layer, so they are not on the observed wire."""
    known = np.empty_like(posts)
    for j in range(posts.shape[1]):
        g = int(w.gk_set[j])
        ph = w.push_phase[g]
        push = ph + P.BOARD_PUSH_S * np.ceil((posts[:, j] - ph) / P.BOARD_PUSH_S)
        known[:, j] = push + w.lat_int[g, node]
    return np.sort(known, axis=1)[:, 1]


def gen_transactions(w: World, r, rate, n_src, src0, sub0, decoy: bool):
    """One stream of transactions (real devices, or the decoy infrastructure's identities) up to
    the horizon. Both streams run the same code; the decoy flag is truth only."""
    cfg, H = w.cfg, w.cfg.horizon_s
    S = int(r.poisson(rate * H)) if rate > 0 else 0
    t0 = np.sort(r.uniform(0, H, S))
    src = src0 + r.integers(0, max(n_src, 1), S)
    lat_src = r.uniform(*P.LAT_EXT_MS, size=(max(n_src, 1), P.N_NODES)) / 1000
    lat = lat_src[src - src0]
    sub = sub0 + np.arange(S)
    C, F, I, A, B, D, E, G, Hh = _roles(r, S, w.gk_set)
    on = cfg.lottery_enabled

    (_, _, arr_c), ev_cred = _chain(w, r, t0, src, lat, A, B, C, (CRED1, CRED2, CRED3), sub, cfg.cred_hold_scale)
    (_, _, arr_f), ev_ca = _chain(w, r, t0, src, lat, D, E, F, (CA1, CA2, CA3), sub, cfg.content_hold_scale)
    (_, _, arr_i), ev_cb = _chain(w, r, t0, src, lat, G, Hh, I, (CB1, CB2, CB3), sub, cfg.content_hold_scale)

    # C -> V -> C: CV-1 on receipt, V's reply after processing (APPROVED with sigma_V and the
    # plaintext real/dummy indicator; the reply is padded in the relay class either way)
    cv1_s = arr_c + _proc(r, S)
    cv1_a = cv1_s + w.lat_int[C, VAL] + _jit(r, S)
    ev_cv1 = w.ev.add(cv1_s, cv1_a, C, VAL, w.size(r, "relay", S), P.RT_APPDATA, K_BIRTHMARK, CV1, sub)
    cv2_s = cv1_a + r.uniform(*P.VALIDATOR_PROC_MS, S) / 1000
    cv2_a = cv2_s + w.lat_int[VAL, C] + _jit(r, S)
    ev_cv2 = w.ev.add(cv2_s, cv2_a, VAL, C, w.size(r, "relay", S), P.RT_APPDATA, K_BIRTHMARK, CV2, sub)

    # fan-out: each leg its own lottery draw on C's node clock; a dummy carries a same-size
    # placeholder in place of sigma_C, so the leg is drawn from the same class either way
    gk = np.broadcast_to(w.gk_set, (S, 3))
    gk_send, gk_arr, posts, gk_rel = np.empty((S, 3)), np.empty((S, 3)), np.empty((S, 3)), np.empty((S, 3))
    ev_gk = np.empty((S, 3), np.int64)
    for j in range(3):
        g = int(w.gk_set[j])
        rel = LT.release_time(r, cv2_a, w.phase[C], on) + _proc(r, S)
        arr = rel + w.lat_int[C, g] + _jit(r, S)
        ev_gk[:, j] = w.ev.add(rel, arr, C, g, w.size(r, "GK", S), P.RT_APPDATA, K_BIRTHMARK, GK1 + j, sub)
        gk_send[:, j], gk_arr[:, j] = rel, arr
        # verify sigma_V and sigma_C, hold on the gatekeeper's own hold clock, post
        chk = arr + r.uniform(*P.GATEKEEPER_PROC_MS, S) / 1000
        rel_gk = LT.release_time(r, chk, w.gk_phase[g], on)
        if cfg.gk_twopoint and on:
            # two-point hold: release at once, or hold the full cap. Drawn on its own stream (the
            # lottery draw above is still consumed), so every other draw is unchanged
            cap = w.rng_gkhold.random(S) >= P.GK_IMMEDIATE_P
            rel_gk = chk + np.where(cap, P.GK_CAP_S, 0.0)
        gk_rel[:, j] = rel_gk
        if cfg.bundle_s > 0:
            # departure bundling: a selected posting waits for the next boundary of this
            # gatekeeper's own grid and departs with every posting selected since the last one
            ph = w.bundle_phase[g]
            rel_gk = ph + cfg.bundle_s * np.ceil((rel_gk - ph) / cfg.bundle_s)
        posts[:, j] = rel_gk + _proc(r, S)
    quorum = np.sort(posts, axis=1)[:, 1]          # second of three boards

    # content servers: hold on the node clock; submit once the hold has released and the board
    # pushes have shown quorum, whichever is later; drop after 30 minutes without quorum
    out = {}
    for name, arr, node in (("f", arr_f, F), ("i", arr_i, I)):
        hold = _content_server(w, r, arr, node)
        det = np.maximum(hold, _pushed(w, posts, node))
        ok = np.isfinite(quorum) & (det - arr <= P.QUORUM_TIMEOUT_S)
        det = np.where(ok, det, np.nan)
        dep = det
        if cfg.reg_bundle_s > 0:
            # registry-level pooled bundling: a confirmed submission waits for the next boundary of
            # one schedule shared by every content server, and departs with every other
            # submission confirmed since the previous boundary, from every server
            ph = w.reg_phase
            dep = ph + cfg.reg_bundle_s * np.ceil((det - ph) / cfg.reg_bundle_s)
        post = dep + _proc(r, S)
        out[name] = (hold, det, post, ok)

    return dict(t0=t0, src=src, decoy=np.full(S, decoy), C=C, F=F, I=I, A=A, B=B, D=D, E=E, G=G, H=Hh,
                arr_c=arr_c, arr_f=arr_f, arr_i=arr_i, cv2_s=cv2_s, cv2_a=cv2_a,
                gk_send=gk_send, gk_arr=gk_arr, posts=posts, gk_release=gk_rel, quorum=quorum,
                hold_f=out["f"][0], det_f=out["f"][1], reg_f=out["f"][2], ok_f=out["f"][3],
                hold_i=out["i"][0], det_i=out["i"][1], reg_i=out["i"][2], ok_i=out["i"][3],
                ev_cred=ev_cred, ev_ca=ev_ca, ev_cb=ev_cb, ev_cv1=ev_cv1, ev_cv2=ev_cv2, ev_gk=ev_gk)


def _gossip(w: World, origin, t_origin, sub, origin_leg, stream=0):
    """Registry submissions: gossipsub flood-publishes to every peer; each peer then forwards on
    first receipt to its mesh peers (not back to the origin). stream 0 carries the real
    transactions' submissions and stream 1 the decoys', so decoys leave the real frames unchanged."""
    r, N = np.random.default_rng([w.gossip_seed, stream]), P.N_NODES
    size = w.pools.gossip_wire
    origin_ids = np.full(origin.shape[0], -1, dtype=np.int64)
    for o in range(N):
        sel = np.nonzero(origin == o)[0]
        if sel.size == 0:
            continue
        others = np.array([v for v in range(N) if v != o])
        ts = t_origin[sel][:, None] + r.uniform(0, 1e-3, (sel.size, others.size))
        ta = ts + w.lat_int[o, others][None, :] + _jit(r, ts.size).reshape(ts.shape)
        ids = w.ev.add(ts.ravel(), ta.ravel(), o, np.tile(others, sel.size), size, P.RT_NOISE, K_BIRTHMARK,
                       np.repeat(origin_leg[sel], others.size), np.repeat(sub[sel], others.size))
        origin_ids[sel] = ids.reshape(sel.size, others.size)[:, 0]
        for j, v in enumerate(others):
            fwd = np.array([u for u in w.mesh[v] if u != o])
            if fwd.size == 0:
                continue
            tf = ta[:, j][:, None] + r.uniform(*P.GOSSIP_VALIDATE_MS, (sel.size, 1)) / 1000 \
                + r.uniform(0, 1e-3, (sel.size, fwd.size))
            tfa = tf + w.lat_int[v, fwd][None, :] + _jit(r, tf.size).reshape(tf.shape)
            w.ev.add(tf.ravel(), tfa.ravel(), v, np.tile(fwd, sel.size), size, P.RT_NOISE, K_BIRTHMARK,
                     REG_RELAY, np.repeat(sub[sel], fwd.size))
    return origin_ids


def gen_birthmark(w: World):
    cfg = w.cfg
    real = gen_transactions(w, w.rng_real, cfg.real_rate, cfg.real_devices, 0, 0, decoy=False)
    S_r = real["t0"].shape[0]
    dec = gen_transactions(w, w.rng_decoy, cfg.decoy_rate, cfg.decoy_sources, 100_000, S_r, decoy=True)
    subs = {k: np.concatenate([real[k], dec[k]]) for k in real}
    S = subs["t0"].shape[0]
    sub = np.arange(S)
    # registry submissions: every transaction. A decoy is a genuine transaction from a registered
    # credential held by the decoy infrastructure; it is approved, fanned out, posted and
    # finalised exactly as a real one. The decoy flag is truth only, for scoring real records.
    okf, oki = subs["ok_f"], subs["ok_i"]
    ev_rf, ev_ri = np.full(S, -1, np.int64), np.full(S, -1, np.int64)
    for stream, part in enumerate((sub < S_r, sub >= S_r)):
        f_, i_ = okf & part, oki & part
        origin = np.concatenate([subs["F"][f_], subs["I"][i_]])
        t_org = np.concatenate([subs["reg_f"][f_], subs["reg_i"][i_]])
        osub = np.concatenate([sub[f_], sub[i_]])
        legs = np.concatenate([np.full(f_.sum(), REG_F), np.full(i_.sum(), REG_I)])
        oids = _gossip(w, origin, t_org, osub, legs, stream)
        ev_rf[f_] = oids[:f_.sum()]
        ev_ri[i_] = oids[f_.sum():]
    subs["ev_reg_f"], subs["ev_reg_i"] = ev_rf, ev_ri
    subs["final"] = np.where(okf & oki, np.fmax(subs["reg_f"], subs["reg_i"]), np.nan)
    return subs


# --------------------------------------------------------------------------- background
def _pool_arrays(pools: Pools):
    sess = pools.tls_sessions
    off = np.cumsum([0] + [s.shape[0] for s in sess])
    flat = np.concatenate(sess)
    pairs = []
    for s in sess:
        app = s[s[:, 4] == 1]
        for f in np.unique(app[:, 1]):
            fl = app[app[:, 1] == f]
            if fl[0, 0] == 0:
                nxt = app[(app[:, 1] == f + 1) & (app[:, 0] == 1)]
                pairs.append(np.concatenate([fl, nxt]) if nxt.size else fl)
    poff = np.cumsum([0] + [p.shape[0] for p in pairs])
    pflat = np.concatenate(pairs).copy()
    pflat[:, 1] = pflat[:, 0]
    nfl = np.array([s[:, 1].max() + 1 for s in sess])
    return off, flat, nfl, poff, pflat


def _expand(tx_start, tx_rec_off, tx_rec_cnt, flat, lat, think):
    n_rec = tx_rec_cnt.sum()
    tx_of = np.repeat(np.arange(tx_start.shape[0]), tx_rec_cnt)
    within = np.arange(n_rec) - np.repeat(np.cumsum(tx_rec_cnt) - tx_rec_cnt, tx_rec_cnt)
    rec = flat[np.repeat(tx_rec_off, tx_rec_cnt) + within]
    direction, flight, rtype, size, app = rec.T
    step = lat[tx_of] + 0.001
    t_send = tx_start[tx_of] + flight * step + np.where((direction == 1) & (app == 1), think[tx_of], 0.0) \
        + within * 1e-5
    return tx_of, direction, rtype, size, t_send


def gen_background(w: World, arrays):
    """Clients transacting with pool nodes (HTTPS sessions drawn from the measured pool, and DNS
    lookups): 90% casual, 10% back-to-back on persistent connections; 20% of clients are other
    pool nodes."""
    cfg, r, H, pools = w.cfg, w.rng_bg, w.cfg.horizon_s, w.pools
    n_cl = cfg.bg_clients_per_node * P.N_NODES
    if n_cl == 0 or not cfg.background_enabled:
        return
    off, flat, nfl, poff, pflat = arrays
    n_int = int(round(n_cl * P.BG_INTERNAL_FRACTION))
    internal_host = np.full(n_cl, -1)
    internal_host[:n_int] = r.integers(0, P.N_NODES, n_int)
    hifreq = np.zeros(n_cl, bool)
    hifreq[r.permutation(n_cl)[: int(round(n_cl * (1 - P.BG_CASUAL_FRACTION)))]] = True
    lat_cl = r.uniform(*P.LAT_EXT_MS, size=(n_cl, P.N_NODES)) / 1000
    for c in range(n_cl):
        host = internal_host[c]
        if hifreq[c]:
            n = int(H / 0.25) + 50
            pause = r.uniform(*P.BG_HIFREQ_PAUSE_S, n)
        else:
            n = int(H / 25.0) + 20
            pause = r.uniform(*P.BG_CASUAL_PAUSE_S, n)
        server = r.integers(0, P.N_NODES, n)
        if host >= 0:
            server = np.where(server == host, (server + 1) % P.N_NODES, server)
            lat = w.lat_int[host, server]
        else:
            lat = lat_cl[c, server]
        is_dns = r.random(n) < P.BG_DNS_FRACTION
        think = r.uniform(0.001, 0.050, n)
        if hifreq[c]:
            pidx = r.integers(0, poff.shape[0] - 1, n)
            rec_off, rec_cnt, nflight = poff[pidx], np.diff(poff)[pidx], np.full(n, 2)
            src_flat = pflat
        else:
            sidx = r.integers(0, off.shape[0] - 1, n)
            rec_off, rec_cnt, nflight = off[sidx], np.diff(off)[sidx], nfl[sidx]
            src_flat = flat
        dur = np.where(is_dns, 2 * lat + 0.015, nflight * (lat + 0.001) + think)
        start = np.cumsum(dur + pause) - (dur + pause)[0] + r.uniform(0, 60)
        keep = start < H
        start, server, lat, think, is_dns = start[keep], server[keep], lat[keep], think[keep], is_dns[keep]
        rec_off, rec_cnt = rec_off[keep], rec_cnt[keep]
        h = ~is_dns
        tx_of, d, rt, sz, ts = _expand(start[h], rec_off[h], rec_cnt[h], src_flat, lat[h], think[h])
        srv = server[h][tx_of]
        ta = ts + lat[h][tx_of] + _jit(r, ts.shape[0])
        if host >= 0:
            w.ev.add(ts, ta, np.where(d == 0, host, srv), np.where(d == 0, srv, host), sz, rt, K_BLEND)
        else:
            cid = 1_000_000 + c
            w.ev.add(ts, ta, np.where(d == 0, EXT, srv), np.where(d == 0, srv, EXT), sz, rt, K_BLEND,
                     ext_src=np.where(d == 0, cid, -1), ext_dst=np.where(d == 0, -1, cid))
        dn = np.nonzero(is_dns)[0]
        if dn.size:
            k = r.integers(0, pools.dns_query.shape[0], dn.size)
            rl = r.uniform(*P.LAT_EXT_MS, dn.size) / 1000
            qs = start[dn]
            w.ev.add(qs, qs + rl, server[dn], EXT, pools.dns_query[k], P.RT_DNS, K_BLEND, ext_dst=2_000_000)
            rs = qs + 2 * rl + r.uniform(0.001, 0.030, dn.size)
            w.ev.add(rs, rs + rl, EXT, server[dn], pools.dns_resp[k], P.RT_DNS, K_BLEND, ext_src=2_000_000)


def gen_nonblending(w: World):
    """Bulk transfers (full-size records, far outside every padding class) and keepalives."""
    if not w.cfg.nonblending_enabled:
        return
    r, H, N, pools = w.rng_nb, w.cfg.horizon_s, P.N_NODES, w.pools
    rec_sz = pools.bulk_record_wire
    payload = rec_sz - pools.tls13_overhead

    def transfers(n, src_of, dst_of, ext_src, ext_dst, lat):
        sizes = np.exp(np.log(P.BULK_MEDIAN_BYTES) + r.normal(0, 1, n)).astype(np.int64)
        nrec = sizes // payload + 1
        start = r.uniform(0, H, n)
        tx = np.repeat(np.arange(n), nrec)
        within = np.arange(nrec.sum()) - np.repeat(np.cumsum(nrec) - nrec, nrec)
        last = within == nrec[tx] - 1
        size = np.where(last, sizes[tx] % payload + pools.tls13_overhead, rec_sz)
        ts = start[tx] + within * 0.0013
        w.ev.add(ts, ts + lat[tx], src_of[tx], dst_of[tx], size, P.RT_APPDATA, K_BULK,
                 ext_src=ext_src[tx] if ext_src is not None else -1,
                 ext_dst=ext_dst[tx] if ext_dst is not None else -1)

    n = r.poisson(P.BULK_EXT_RATE_PER_NODE * H * N)
    node = r.integers(0, N, n)
    up = r.random(n) < 0.3
    cid = 3_000_000 + np.arange(n)
    transfers(n, np.where(up, EXT, node), np.where(up, node, EXT), np.where(up, cid, -1), np.where(up, -1, cid),
              r.uniform(*P.LAT_EXT_MS, n) / 1000)
    n = r.poisson(P.BULK_INT_RATE_PER_NODE * H * N)
    a = r.integers(0, N, n)
    b = (a + r.integers(1, N, n)) % N
    transfers(n, a, b, None, None, w.lat_int[a, b])
    ends = [(i, j) for i in range(N) for j in range(N + P.N_VALIDATORS) if i != j]
    ends += [(j, i) for i in range(N) for j in range(N, N + P.N_VALIDATORS)]
    ends = np.array(ends)
    k = int(H / P.KEEPALIVE_PERIOD_S) + 1
    ph = r.uniform(0, P.KEEPALIVE_PERIOD_S, len(ends))
    ts = (ph[:, None] + P.KEEPALIVE_PERIOD_S * np.arange(k)[None, :] + r.uniform(-1, 1, (len(ends), k))).ravel()
    s, d = np.repeat(ends[:, 0], k), np.repeat(ends[:, 1], k)
    ok = (ts > 0) & (ts < H)
    w.ev.add(ts[ok], ts[ok] + w.lat_int[s[ok], d[ok]], s[ok], d[ok], pools.keepalive_wire, P.RT_APPDATA, K_KEEPALIVE)


# --------------------------------------------------------------------------- run
_ARRAYS = {}


def simulate(cfg: P.Config, seed: int, pools: Pools) -> Run:
    key = id(pools)
    if key not in _ARRAYS:
        _ARRAYS[key] = _pool_arrays(pools)
    w = World(cfg, seed, pools)
    subs = gen_birthmark(w)
    gen_background(w, _ARRAYS[key])
    gen_nonblending(w)
    events, rank = w.ev.finalize()
    for k, v in subs.items():
        if k.startswith("ev_"):
            subs[k] = np.where(v >= 0, rank[np.maximum(v, 0)], -1)
    return Run(cfg=cfg, events=events, subs=subs, phase=w.phase, gk_phase=w.gk_phase, gk_set=w.gk_set,
               bundle_phase=w.bundle_phase, push_phase=w.push_phase, reg_phase=w.reg_phase,
               horizon=cfg.horizon_s)

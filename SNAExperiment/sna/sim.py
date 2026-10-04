"""Vectorised generator of one run's complete wire trace, real and decoy traffic together.

Output: an event table (one row per message on a link, as a passive observer of every link sees
it: send and arrival times, endpoints, wire size, record type) plus hidden truth columns (leg,
transaction) and a per-transaction truth table used only for scoring.

Random streams. One run seed is split into independent streams: the world (latencies, clock phases,
gatekeeper set, gossip mesh), the real transactions, the decoy transactions, and one stream for
each mechanism that can be removed (departure-bundle grids, board pushes, the registry schedule,
the post-match lottery, the inclusion lottery, the validator's clock). Real traffic is therefore
identical, event for event, whatever the decoy volume, and removing a mechanism changes only what
that mechanism does.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from . import lottery as LT
from . import params as P

EXT = 99                  # every external host (device or decoy source)
VAL = P.N_NODES           # the validator's node id

# leg codes (truth only)
CRED1, CRED2, CRED3, CA1, CA2, CA3, CB1, CB2, CB3 = range(1, 10)
CV1, CV2, GK1, GK2, GK3, REG_F, REG_I, REG_RELAY = range(10, 18)
LEG_NAMES = {CRED1: "Cred-1", CRED2: "Cred-2", CRED3: "Cred-3", CA1: "ContA-1", CA2: "ContA-2", CA3: "ContA-3",
             CB1: "ContB-1", CB2: "ContB-2", CB3: "ContB-3", CV1: "CV-1", CV2: "CV-2", GK1: "GK-1", GK2: "GK-2",
             GK3: "GK-3", REG_F: "Reg-F", REG_I: "Reg-I", REG_RELAY: "Reg relay"}
K_BIRTHMARK = 0


class _Events:
    """Column buffers, finalized into one table sorted by send time."""
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
    def __init__(self, cfg: P.Config, seed: int):
        self.cfg = cfg
        ss = np.random.SeedSequence(seed)
        streams = ss.spawn(13)
        # streams 4, 5, 8 and 11 are reserved and unused here
        (self.rng_world, self.rng_real, self.rng_decoy, _, _, rng_bundle, rng_push,
         _, rng_reg, self.rng_post, _, self.rng_incl, rng_v) = (np.random.default_rng(s) for s in streams)
        # the validator's hold-clock phase
        self.v_phase = float(rng_v.uniform(0, P.TICK_S))
        # each gatekeeper's departure-bundle grid phase
        self.bundle_phase = rng_bundle.uniform(0, P.BUNDLE_S, P.N_NODES)
        # each match board's push schedule phase
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
        TLS 1.3 record overhead."""
        lo, hi = P.PAD_GK if cls == "GK" else (P.PAD_MIN, P.PAD_MAX)
        return rng.integers(lo, hi + 1, n) + P.TLS13_OVERHEAD


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


def _chain(w, r, t0, src_id, lat_src, first, second, dest, legs, sub, device_mean):
    """Device (or decoy source) -> addressed hop -> random hop -> destination. The device holds on a
    fresh clock phase for this channel with its own mean; each relay hop holds on its node clock."""
    n = t0.shape[0]
    dep = LT.hold(r, t0, None, device_mean) + _proc(r, n)
    arr = dep + lat_src[np.arange(n), first] + _jit(r, n)
    ids = [w.ev.add(dep, arr, EXT, first, w.size(r, "relay", n), P.RT_APPDATA, K_BIRTHMARK, legs[0], sub,
                    ext_src=src_id)]
    arrs = [arr]
    cur = first
    for nxt, leg in ((second, legs[1]), (dest, legs[2])):
        rel = LT.hold(r, arr, w.phase[cur], w.cfg.relay_mean) + _proc(r, n)
        arr = rel + w.lat_int[cur, nxt] + _jit(r, n)
        ids.append(w.ev.add(rel, arr, cur, nxt, w.size(r, "relay", n), P.RT_APPDATA, K_BIRTHMARK, leg, sub))
        arrs.append(arr)
        cur = nxt
    return arrs, np.stack(ids, 1)


def _jit(r, n):
    return r.exponential(P.JITTER_MS / 1000, n)


def _proc(r, n):
    return r.uniform(*P.PROC_MS, n) / 1000


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

    (_, _, arr_c), ev_cred = _chain(w, r, t0, src, lat, A, B, C, (CRED1, CRED2, CRED3), sub, cfg.dev_cred_mean)
    (_, _, arr_f), ev_ca = _chain(w, r, t0, src, lat, D, E, F, (CA1, CA2, CA3), sub, cfg.dev_content_mean)
    (_, _, arr_i), ev_cb = _chain(w, r, t0, src, lat, G, Hh, I, (CB1, CB2, CB3), sub, cfg.dev_content_mean)

    # C -> V -> C: C holds on its node clock, then sends CV-1; V processes, holds on its own clock,
    # and replies (APPROVED with sigma_V; the reply is padded in the relay class either way)
    cv1_s = LT.hold(r, arr_c, w.phase[C], cfg.c_hold_mean) + _proc(r, S)
    cv1_a = cv1_s + w.lat_int[C, VAL] + _jit(r, S)
    ev_cv1 = w.ev.add(cv1_s, cv1_a, C, VAL, w.size(r, "relay", S), P.RT_APPDATA, K_BIRTHMARK, CV1, sub)
    cv2_s = cv1_a + r.uniform(*P.VALIDATOR_PROC_MS, S) / 1000
    cv2_s = LT.hold(r, cv2_s, w.v_phase, cfg.v_hold_mean)
    cv2_a = cv2_s + w.lat_int[VAL, C] + _jit(r, S)
    ev_cv2 = w.ev.add(cv2_s, cv2_a, VAL, C, w.size(r, "relay", S), P.RT_APPDATA, K_BIRTHMARK, CV2, sub)

    # fan-out: each leg its own hold on C's node clock, timed from C's receipt of CV-2
    gk_send, gk_arr, posts, gk_rel = np.empty((S, 3)), np.empty((S, 3)), np.empty((S, 3)), np.empty((S, 3))
    ev_gk = np.empty((S, 3), np.int64)
    for j in range(3):
        g = int(w.gk_set[j])
        rel = LT.hold(r, cv2_a, w.phase[C], cfg.fanout_mean) + _proc(r, S)
        arr = rel + w.lat_int[C, g] + _jit(r, S)
        ev_gk[:, j] = w.ev.add(rel, arr, C, g, w.size(r, "GK", S), P.RT_APPDATA, K_BIRTHMARK, GK1 + j, sub)
        gk_send[:, j], gk_arr[:, j] = rel, arr
        # verify sigma_V and sigma_C, hold on the gatekeeper's own hold clock
        chk = arr + r.uniform(*P.GATEKEEPER_PROC_MS, S) / 1000
        rel_gk = LT.hold(r, chk, w.gk_phase[g], cfg.gk_mean)
        gk_rel[:, j] = rel_gk
        ph = w.bundle_phase[g]
        if cfg.gk_inclusion:
            # inclusion lottery: at each boundary of this gatekeeper's grid the ready posting draws
            # for a place in that boundary's bundle; boarding is forced at the 12th boundary
            rel_gk = LT.inclusion_departure(w.rng_incl, rel_gk, ph, P.BUNDLE_S, P.INCLUSION_P, P.INCLUSION_MAX)
        else:
            # every ready posting departs at the next boundary
            rel_gk = ph + P.BUNDLE_S * np.ceil((rel_gk - ph) / P.BUNDLE_S)
        posts[:, j] = rel_gk + _proc(r, S)
    quorum = np.sort(posts, axis=1)[:, 1]          # second of three boards

    # content servers: hold on the node clock; confirm once the hold has released and the board
    # pushes have shown quorum, whichever is later; drop after 30 minutes without quorum
    out = {}
    for name, arr, node in (("f", arr_f, F), ("i", arr_i, I)):
        hold = LT.hold(r, arr, w.phase[node], cfg.cs_mean)
        known = _pushed(w, posts, node)
        det = np.maximum(hold, known)
        ok = np.isfinite(quorum) & (det - arr <= P.QUORUM_TIMEOUT_S)
        det = np.where(ok, det, np.nan)
        ready = det
        if cfg.post_match:
            # post-match lottery: a hold on a fresh random phase, timed from the moment this server
            # confirms quorum
            ready = LT.hold(w.rng_post, np.where(ok, det, 0.0), None, cfg.pm_mean)
            ready = np.where(ok, ready, np.nan)
        dep = ready
        if cfg.reg_bundle_s > 0:
            # registry-level bundling: a confirmed submission waits for the next boundary of one
            # schedule shared by every content server, and departs with every other submission
            # confirmed since the previous boundary, from every server
            ph = w.reg_phase
            dep = ph + cfg.reg_bundle_s * np.ceil((ready - ph) / cfg.reg_bundle_s)
        post = dep + _proc(r, S)
        out[name] = (hold, det, post, ok, ready, known)

    return dict(t0=t0, src=src, decoy=np.full(S, decoy), C=C, F=F, I=I, A=A, B=B, D=D, E=E, G=G, H=Hh,
                arr_c=arr_c, arr_f=arr_f, arr_i=arr_i, cv1_s=cv1_s, cv2_s=cv2_s, cv2_a=cv2_a,
                gk_send=gk_send, gk_arr=gk_arr, posts=posts, gk_release=gk_rel, quorum=quorum,
                hold_f=out["f"][0], det_f=out["f"][1], reg_f=out["f"][2], ok_f=out["f"][3],
                hold_i=out["i"][0], det_i=out["i"][1], reg_i=out["i"][2], ok_i=out["i"][3],
                ready_f=out["f"][4], ready_i=out["i"][4], known_f=out["f"][5], known_i=out["i"][5],
                ev_cred=ev_cred, ev_ca=ev_ca, ev_cb=ev_cb, ev_cv1=ev_cv1, ev_cv2=ev_cv2, ev_gk=ev_gk)


def _gossip(w: World, origin, t_origin, sub, origin_leg, stream=0):
    """Registry submissions: gossipsub flood-publishes to every peer; each peer then forwards on
    first receipt to its mesh peers (not back to the origin). stream 0 carries the real
    transactions' submissions and stream 1 the decoys', so decoys leave the real frames unchanged."""
    r, N = np.random.default_rng([w.gossip_seed, stream]), P.N_NODES
    size = P.GOSSIP_WIRE
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
    # finalized exactly as a real one. The decoy flag is truth only, for scoring real records.
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


# --------------------------------------------------------------------------- run
def simulate(cfg: P.Config, seed: int) -> Run:
    w = World(cfg, seed)
    subs = gen_birthmark(w)
    events, rank = w.ev.finalize()
    for k, v in subs.items():
        if k.startswith("ev_"):
            subs[k] = np.where(v >= 0, rank[np.maximum(v, 0)], -1)
    return Run(cfg=cfg, events=events, subs=subs, phase=w.phase, gk_phase=w.gk_phase, gk_set=w.gk_set,
               bundle_phase=w.bundle_phase, push_phase=w.push_phase, reg_phase=w.reg_phase,
               horizon=cfg.horizon_s)

"""Vectorised generator of one run's complete wire trace, real and decoy traffic together.

Output: an event table (one row per message on a link, as a passive observer of every link sees
it: send and arrival times, endpoints, wire size, record type) plus hidden truth columns (leg,
transaction) and a per-transaction truth table used only for scoring.

Random streams. One run seed is split into independent streams: the world (latencies, clock phases,
gatekeeper set, gossip mesh), the real transactions, the decoy transactions, and one stream for
each mechanism that can be removed (departure-bundle grids, board pushes, the registry schedule,
the post-match lottery, the inclusion lottery, the validator's clock, the registry's posting
schedule). Real traffic is therefore
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
    post_phase: float = 0.0


class World:
    def __init__(self, cfg: P.Config, seed: int):
        self.cfg = cfg
        ss = np.random.SeedSequence(seed)
        streams = ss.spawn(15)
        # streams 4, 5, 8 and 11 are reserved and unused here; stream 13 draws the relays when
        # overlap is on, so every other draw is the same with overlap on or off; stream 14 draws the
        # registry's posting-schedule phase
        (self.rng_world, self.rng_real, self.rng_decoy, _, _, rng_bundle, rng_push,
         _, rng_reg, self.rng_post, _, self.rng_incl, rng_v, self.rng_relays,
         rng_regpost) = (np.random.default_rng(s) for s in streams)
        # the validator's hold-clock phase
        self.v_phase = float(rng_v.uniform(0, P.TICK_S))
        # each gatekeeper's departure-bundle grid phase
        self.bundle_phase = rng_bundle.uniform(0, P.BUNDLE_S, P.N_NODES)
        # each match board's push schedule phase
        self.push_phase = rng_push.uniform(0, P.BOARD_PUSH_S, P.N_NODES)
        # the registry-level bundle schedule: one phase shared by every content server
        self.reg_phase = float(rng_reg.uniform(0, max(cfg.reg_bundle_s, 1.0)))
        # the registry's own posting schedule, on an independent phase
        self.post_phase = float(rng_regpost.uniform(0, max(cfg.reg_post_s, 1.0)))
        # streams for the C3 to C5 options, spawned after the fifteen above so those are unchanged: the
        # workloads, the edit chains, and the active attacks with their resubmissions
        self.rng_work, self.rng_edit, self.rng_mark, _ = (np.random.default_rng(s) for s in ss.spawn(4))
        self.lat_tab = {}
        self.served = {}
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
def _roles(r, S, gk_set, n_nodes=P.N_NODES, rng_relays=None):
    """The nodes of each transaction's three paths: credential A -> B -> C, content D -> E -> F and
    G -> H -> I. C, F and I are three distinct nodes, never in the active gatekeeper set.

    By default every role is a distinct node: the relays are six distinct nodes drawn from the
    nodes other than C, F and I, so the three paths share no node, a first hop is never C, F or I,
    and a gatekeeper may relay.

    With rng_relays (permitted overlap) the relays are drawn under the routing design's guarantees
    only, in order, each uniform over the nodes its constraints allow: A, D and G pairwise distinct
    and each different from its own path's destination; then B, E and H, each different from its
    own path's first relay and destination. Every other coincidence is allowed. C, F and I are the
    same as by default, and the default draws are still taken, so every later draw is unchanged."""
    N = n_nodes
    pool = np.setdiff1d(np.arange(N), gk_set)
    cfi = pool[np.argsort(r.random((S, pool.size)), axis=1)[:, :3]]
    x = r.random((S, N))
    idx = np.arange(S)[:, None]
    x[idx, cfi] = 2.0
    rest = np.argsort(x, axis=1)[:, :6]
    C, F, I = cfi.T
    if rng_relays is None:
        A, B, D, E, G, H = rest.T
        return C, F, I, A, B, D, E, G, H
    rows = np.arange(S)

    def pick(*excluded):
        u = rng_relays.random((S, N))
        for e in excluded:
            u[rows, e] = 2.0
        return np.argmin(u, axis=1)
    A = pick(C)
    D = pick(F, A)
    G = pick(I, A, D)
    B = pick(A, C)
    E = pick(D, F)
    H = pick(G, I)
    return C, F, I, A, B, D, E, G, H


PATHS = (("A", "B", "C"), ("D", "E", "F"), ("G", "H", "I"))
CROSS_PAIRS = tuple((a, b) for i, p in enumerate(PATHS) for q in PATHS[i + 1:] for a in p for b in q)


def cross_path_overlap(roles):
    """True where some node holds roles on two different paths of the same transaction."""
    out = np.zeros(np.asarray(roles["A"]).shape, bool)
    for a, b in CROSS_PAIRS:
        out |= roles[a] == roles[b]
    return out


def _chain(w, r, t0, src_id, lat_src, first, second, dest, legs, sub, device_mean, d_access=None, d_first=None):
    """Device (or decoy source) -> addressed hop -> random hop -> destination. The device holds on a
    fresh clock phase for this channel with its own mean; each relay hop holds on its node clock, with
    the mean of its hop position (first or second). Nothing here depends on the path: a relay cannot
    tell a credential packet from a content packet."""
    n = t0.shape[0]
    dep = LT.hold(r, t0, None, device_mean) + _proc(r, n)
    arr = dep + lat_src[np.arange(n), first] + _jit(r, n)
    if d_access is not None:                     # an access-network mark: the packet reaches the first relay late
        arr = arr + d_access
    ids = [w.ev.add(dep, arr, EXT, first, w.size(r, "relay", n), P.RT_APPDATA, K_BIRTHMARK, legs[0], sub,
                    ext_src=src_id)]
    arrs = [arr]
    cur = first
    for hop, (nxt, leg, mean) in enumerate(((second, legs[1], w.cfg.relay1_mean), (dest, legs[2], w.cfg.relay2_mean))):
        rel = LT.hold(r, arr, w.phase[cur], mean) + _proc(r, n)
        if hop == 0 and d_first is not None:     # a first-relay mark: the relay holds the packet longer
            rel = rel + d_first
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
        push = posts[:, j] if w.cfg.grid_off else ph + P.BOARD_PUSH_S * np.ceil((posts[:, j] - ph) / P.BOARD_PUSH_S)
        known[:, j] = push + w.lat_int[g, node]
    return np.sort(known, axis=1)[:, 1]


def _workload(w, rate, n_src, decoy, kind):
    """Capture times and sources under W1 or W2 (rng_work): each identity a Poisson process at its own
    rate, a lognormal factor of the device rate scaled to mean 1 over the population; under W2 a share of
    identities also has sessions at SESSION_MULT times its rate. The population's total rate is kept. A
    single real device (R = 1) keeps the cell's rate under W1, and has sessions under W2."""
    rg, H, n = w.rng_work, w.cfg.horizon_s, max(n_src, 1)
    if rate <= 0:
        return np.zeros(0), np.zeros(0, np.int64)
    m = np.exp(rg.normal(-P.W_SIGMA ** 2 / 2, P.W_SIGMA, n))
    m = np.ones(n) if n == 1 else m / m.mean()
    sess = np.zeros(n, bool)
    if kind == "W2":
        sess = np.ones(n, bool) if (n == 1 and not decoy) else rg.random(n) < P.SESSION_SHARE
    mean_len = np.mean(P.SESSION_MIN) * 60
    boost = 1.0 + (P.SESSION_MULT - 1) * mean_len * P.SESSION_PER_S      # mean rate multiple of a session identity
    base = rate * m / np.sum(m * np.where(sess, boost, 1.0))              # each identity's rate between sessions
    ts, ss = [], []
    for i in range(n):
        k = rg.poisson(base[i] * H)
        ts.append(rg.uniform(0, H, k))
        ss.append(np.full(k, i))
        if sess[i]:
            lead = 2 * P.SESSION_MIN[1] * 60
            for st in rg.uniform(-lead, H, rg.poisson(P.SESSION_PER_S * (H + lead))):
                ln = rg.uniform(*P.SESSION_MIN) * 60
                a, b = max(st, 0.0), min(st + ln, H)
                if b > a:
                    k = rg.poisson(base[i] * (P.SESSION_MULT - 1) * (b - a))
                    ts.append(rg.uniform(a, b, k))
                    ss.append(np.full(k, i))
    t0, src = np.concatenate(ts), np.concatenate(ss).astype(np.int64)
    o = np.argsort(t0, kind="stable")
    return t0[o], src[o]


def gen_transactions(w: World, r, rate, n_src, src0, sub0, decoy: bool, t0=None, src=None, lat=None, gen=0):
    """One stream of transactions (real devices, or the decoy infrastructure's identities) up to
    the horizon. Both streams run the same code; the decoy flag is truth only. t0, src and lat (one row
    of first-hop latencies per transaction) are given for edits and resubmissions."""
    cfg, H = w.cfg, w.cfg.horizon_s
    if t0 is None:
        kind = "W0" if (cfg.workload == "Wmis" and decoy) else ("W2" if cfg.workload == "Wmis" else cfg.workload)
        if kind == "W0":
            S = int(r.poisson(rate * H)) if rate > 0 else 0
            t0 = np.sort(r.uniform(0, H, S))
            src = src0 + r.integers(0, max(n_src, 1), S)
        else:
            t0, src = _workload(w, rate, n_src, decoy, kind)
            src = src0 + src
            S = t0.shape[0]
        lat_src = r.uniform(*P.LAT_EXT_MS, size=(max(n_src, 1), P.N_NODES)) / 1000
        w.lat_tab[src0] = lat_src
        lat = lat_src[src - src0]
    else:
        S = t0.shape[0]
    sub = sub0 + np.arange(S)
    C, F, I, A, B, D, E, G, Hh = _roles(r, S, w.gk_set, rng_relays=w.rng_relays if cfg.overlap else None)

    mk = _marks(w, S, src, decoy, gen)
    (_, _, arr_c), ev_cred = _chain(w, r, t0, src, lat, A, B, C, (CRED1, CRED2, CRED3), sub, cfg.dev_cred_mean, *mk["d"][0])
    (_, _, arr_f), ev_ca = _chain(w, r, t0, src, lat, D, E, F, (CA1, CA2, CA3), sub, cfg.dev_content_mean, *mk["d"][1])
    dev_i = cfg.dev_content_mean if cfg.dev_content_i_mean < 0 else cfg.dev_content_i_mean
    (_, _, arr_i), ev_cb = _chain(w, r, t0, src, lat, G, Hh, I, (CB1, CB2, CB3), sub, dev_i, *mk["d"][2])

    # C -> V -> C: C holds on its node clock, then sends CV-1; V processes, holds on its own clock,
    # and replies (APPROVED with sigma_V; the reply is padded in the relay class either way)
    cv1_s = LT.hold(r, arr_c, w.phase[C], cfg.c_hold_mean) + _proc(r, S)
    cv1_a = cv1_s + w.lat_int[C, VAL] + _jit(r, S)
    ev_cv1 = w.ev.add(cv1_s, cv1_a, C, VAL, w.size(r, "relay", S), P.RT_APPDATA, K_BIRTHMARK, CV1, sub)
    cv2_s = cv1_a + r.uniform(*P.VALIDATOR_PROC_MS, S) / 1000
    cv2_s = LT.hold(r, cv2_s, w.v_phase, cfg.v_hold_mean)
    if mk["d_v"] is not None:                    # a validator mark: the reply leaves late
        cv2_s = cv2_s + mk["d_v"]
    if cfg.mark_actor == "validator_withhold":
        cv2_s = _withhold(w, mk, cv2_s, src, src0, n_src, decoy)
    cv2_a = cv2_s + w.lat_int[VAL, C] + _jit(r, S)
    ev_cv2 = w.ev.add(cv2_s, cv2_a, VAL, C, w.size(r, "relay", S), P.RT_APPDATA, K_BIRTHMARK, CV2, sub)

    # fan-out, serialized: from C's receipt of CV-2, the transaction's three legs share one draw per
    # tick of C's node clock; each successful draw sends the next leg in a random order, and the
    # next draw starts at the following tick, so no two legs leave on the same tick
    gk_send, gk_arr, posts, gk_rel = np.empty((S, 3)), np.empty((S, 3)), np.empty((S, 3)), np.empty((S, 3))
    ev_gk = np.empty((S, 3), np.int64)
    order = r.permuted(np.tile(np.arange(3), (S, 1)), axis=1)      # order[:, i]: the i-th leg to leave
    tick = np.empty((S, 3))
    t_draw = cv2_a
    for i in range(3):
        # a draw that succeeded sits exactly on a tick; the offset keeps the next draw off that tick
        t_draw = LT.hold(r, t_draw + (1e-6 if i else 0.0), w.phase[C], cfg.fanout_mean)
        tick[np.arange(S), order[:, i]] = t_draw
    for j in range(3):
        g = int(w.gk_set[j])
        rel = tick[:, j] + _proc(r, S)
        arr = rel + w.lat_int[C, g] + _jit(r, S)
        ev_gk[:, j] = w.ev.add(rel, arr, C, g, w.size(r, "GK", S), P.RT_APPDATA, K_BIRTHMARK, GK1 + j, sub)
        gk_send[:, j], gk_arr[:, j] = rel, arr
        # verify sigma_V and sigma_C, hold on the gatekeeper's own hold clock
        chk = arr + r.uniform(*P.GATEKEEPER_PROC_MS, S) / 1000
        rel_gk = LT.hold(r, chk, w.gk_phase[g], cfg.gk_mean)
        gk_rel[:, j] = rel_gk
        ph = w.bundle_phase[g]
        if cfg.grid_off:
            pass                                 # no departure grid: the posting leaves when ready
        elif cfg.gk_inclusion:
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
        ok = np.isfinite(quorum) & (det - arr <= cfg.quorum_timeout_s)
        if cfg.board_window_s > 0:               # the boards no longer hold the postings when F or I checks
            ok &= det - quorum <= cfg.board_window_s
        if mk["drop"] is not None:               # a dropped packet never confirms
            ok &= ~mk["drop"]
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

    extra = {}
    if cfg.overlap:
        extra["overlap"] = cross_path_overlap(dict(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=Hh, I=I))
    return dict(t0=t0, src=src, decoy=np.full(S, decoy), C=C, F=F, I=I, A=A, B=B, D=D, E=E, G=G, H=Hh, **extra,
                arr_c=arr_c, arr_f=arr_f, arr_i=arr_i, cv1_s=cv1_s, cv2_s=cv2_s, cv2_a=cv2_a,
                gk_send=gk_send, gk_arr=gk_arr, posts=posts, gk_release=gk_rel, quorum=quorum,
                hold_f=out["f"][0], det_f=out["f"][1], reg_f=out["f"][2], ok_f=out["f"][3],
                hold_i=out["i"][0], det_i=out["i"][1], reg_i=out["i"][2], ok_i=out["i"][3],
                ready_f=out["f"][4], ready_i=out["i"][4], known_f=out["f"][5], known_i=out["i"][5],
                ev_cred=ev_cred, ev_ca=ev_ca, ev_cb=ev_cb, ev_cv1=ev_cv1, ev_cv2=ev_cv2, ev_gk=ev_gk,
                marked=mk["marked"], mark_path=mk["path"], dropped=mk["drop"] if mk["drop"] is not None else np.zeros(S, bool),
                withheld=mk.get("withheld", np.zeros(S, bool)))


def _withhold(w, mk, cv2_s, src, src0, n_src, decoy):
    """Validator withholding: inside each window the validator replies to its target and withholds, or delays to the
    window's end, its reply to every other credential it serves (a share of identities, drawn once per run). A
    withheld transaction fails. The target's replies inside a window are the marked transactions."""
    cfg = w.cfg
    if src0 not in w.served:
        w.served[src0] = w.rng_mark.random(max(n_src, 1)) < cfg.withhold_share
    served = w.served[src0][np.clip(src - src0, 0, max(n_src, 1) - 1)]
    period = cfg.withhold_len + P.WITHHOLD_GAP_S
    x = cv2_s - cfg.warmup_s
    inwin = (x >= 0) & (np.mod(x, period) < cfg.withhold_len)
    tgt = (src == cfg.mark_target) & (not decoy)
    hold = served & inwin & ~tgt
    mk["withheld"] = hold
    mk["marked"] = tgt & inwin
    mk["path"] = np.where(mk["marked"], 4, -1).astype(np.int8)
    if cfg.withhold_mode == "delay":
        end = cfg.warmup_s + period * np.floor(np.maximum(x, 0) / period) + cfg.withhold_len
        return np.where(hold, end, cv2_s)
    mk["drop"] = hold                            # no reply: the transaction never reaches quorum
    return cv2_s


def _marks(w, S, src, decoy, gen):
    """The active attack on one generation of transactions: which are the target's and marked, on which path
    (0 credential, 1 F content, 2 I content, 3 all three, 4 the validator's reply), and the delays or the drop.
    Only the target's own first transactions are marked; resubmissions and edits are not."""
    cfg = w.cfg
    none = dict(marked=np.zeros(S, bool), path=np.full(S, -1, np.int8), d=[(None, None)] * 3, d_v=None, drop=None)
    if cfg.mark_actor == "validator_withhold":
        return dict(none, withheld=np.zeros(S, bool))
    if not cfg.mark_actor or decoy or gen > 0 or cfg.mark_target == -1:
        return none
    marked = (src == cfg.mark_target) if cfg.mark_target >= 0 else np.ones(S, bool)   # -2: every real device (models)
    one = w.rng_mark.integers(0, 3, S)           # the first relay that holds it, or the one packet marked
    path = np.full(S, -1, np.int8)
    if cfg.mark_actor in ("first_relay", "access_one"):
        path = np.where(marked, one, -1).astype(np.int8)
    elif cfg.mark_actor == "access":
        path = np.where(marked, 3, -1).astype(np.int8)
    elif cfg.mark_actor == "validator":
        path = np.where(marked, 4, -1).astype(np.int8)
    else:
        raise ValueError(cfg.mark_actor)
    out = dict(marked=marked, path=path, d=[(None, None)] * 3, d_v=None, drop=None)
    if cfg.mark_mode == "drop":
        if cfg.mark_actor == "validator":
            raise ValueError("the validator does not drop")
        out["drop"] = path >= 0
        return out
    dl = []
    for k in range(3):
        hit = (path == k) | (path == 3)
        d = np.where(hit, cfg.mark_delta, 0.0)
        dl.append((d, None) if cfg.mark_actor.startswith("access") else (None, d))
    out["d"] = dl
    if cfg.mark_actor == "validator":
        out["d_v"] = np.where(path == 4, cfg.mark_delta, 0.0)
    return out


def _gossip(w: World, origin, t_origin, sub, origin_leg, stream=0):
    """Registry submissions: gossipsub flood-publishes to every peer; each peer then forwards on
    first receipt to its mesh peers (not back to the origin). stream 0 carries the real
    transactions' submissions and stream 1 the decoys', so decoys leave the real frames unchanged."""
    r, N = np.random.default_rng([w.gossip_seed, stream]), P.N_NODES
    size = P.GOSSIP_WIRE
    origin_ids = np.full(origin.shape[0], -1, dtype=np.int64)
    reach = np.full(origin.shape[0], np.nan)
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
        reach[sel] = ta.max(1)                       # the flood-publish has reached every peer
        for j, v in enumerate(others):
            fwd = np.array([u for u in w.mesh[v] if u != o])
            if fwd.size == 0:
                continue
            tf = ta[:, j][:, None] + r.uniform(*P.GOSSIP_VALIDATE_MS, (sel.size, 1)) / 1000 \
                + r.uniform(0, 1e-3, (sel.size, fwd.size))
            tfa = tf + w.lat_int[v, fwd][None, :] + _jit(r, tf.size).reshape(tf.shape)
            w.ev.add(tf.ravel(), tfa.ravel(), v, np.tile(fwd, sel.size), size, P.RT_NOISE, K_BIRTHMARK,
                     REG_RELAY, np.repeat(sub[sel], fwd.size))
    return origin_ids, reach


def gen_birthmark(w: World):
    cfg = w.cfg
    grow = 1.0 + cfg.edits_per_capture           # edits are transactions too: captures slow so the volume holds
    real = gen_transactions(w, w.rng_real, cfg.real_rate / grow, cfg.real_devices, 0, 0, decoy=False)
    S_r = real["t0"].shape[0]
    dec = gen_transactions(w, w.rng_decoy, cfg.decoy_rate / grow, cfg.decoy_sources, 100_000, S_r, decoy=True)
    subs = {k: np.concatenate([real[k], dec[k]]) for k in real}
    S = subs["t0"].shape[0]
    subs["parent"] = np.full(S, -1, np.int64)
    subs["root"] = np.arange(S)
    subs["gen"] = np.zeros(S, np.int8)
    _register(w, subs, 0, S, S_r, 0)
    if cfg.edit_share > 0:
        e = w.rng_edit
        edited = e.random(S) < cfg.edit_share
        subs["edits_left"] = np.where(edited, 1 + np.minimum(e.poisson(P.EDIT_EXTRA_MEAN, S), P.EDIT_MAX - 1), 0)
    gen, lo = 0, 0
    while True:
        kids = _children(w, subs, lo, S)
        if kids is None or gen >= 6:
            break
        gen += 1
        parts, sub0 = [], S
        for decoy, (par, t0, src, src0, lat, r) in kids:
            if par.size == 0:
                continue
            x = gen_transactions(w, r, 0.0, 0, src0, sub0, decoy=decoy, t0=t0, src=src, lat=lat, gen=gen)
            x["parent"], x["root"], x["gen"] = par, subs["root"][par], np.full(par.size, gen, np.int8)
            if "edits_left" in subs:
                x["edits_left"] = subs["edits_left"][par] - 1
            parts.append(x)
            sub0 += par.size
        if not parts:
            break
        n_real = parts[0]["t0"].size if not parts[0]["decoy"][0] else 0
        for k in parts[0]:
            subs[k] = np.concatenate([subs[k]] + [x[k] for x in parts])
        lo, S = S, subs["t0"].shape[0]
        _register(w, subs, lo, S, lo + n_real, gen)
    return subs


def _children(w, subs, lo, hi):
    """The next generation: edits of the transactions in [lo, hi) that posted and have edits left, or the
    resubmissions of dropped transactions. Returns [(decoy, (parents, t0, src, src0, latency rows, rng))]
    for the real and the decoy children, or None."""
    cfg, H = w.cfg, w.cfg.horizon_s
    idx = np.arange(lo, hi)
    out = []
    if cfg.edit_share > 0:
        e = w.rng_edit
        par = idx[(subs["edits_left"][idx] > 0) & np.isfinite(subs["posted"][idx])]
        t0 = subs["posted"][par] + P.EDIT_DELAY_MIN_S + e.exponential(P.EDIT_DELAY_MEAN_S, par.size)
        same = e.random(par.size) < cfg.edit_same_source
        keep = t0 < H
        par, t0, same = par[keep], t0[keep], same[keep]
        for decoy, src0 in ((False, 0), (True, 100_000)):
            m = subs["decoy"][par] == decoy
            p_, t_, sm = par[m], t0[m], same[m]
            dev = subs["src"][p_] % P.MACHINE_OFFSET            # the capture device's own address
            src = np.where(sm, dev, dev + P.MACHINE_OFFSET)
            lat = _latency(w, src, src0)
            o = np.argsort(t_, kind="stable")
            out.append((decoy, (p_[o], t_[o], src[o], src0, lat[o], e)))
        return out if any(x[1][0].size for x in out) else None
    if cfg.mark_actor and cfg.mark_mode == "drop":
        par = idx[subs["dropped"][idx] & (subs["gen"][idx] == 0)]
        if par.size == 0:
            return None
        t0 = subs["t0"][par] + P.RESUB_WAIT_S + w.rng_mark.exponential(cfg.resub_mean_s, par.size)
        keep = t0 < H
        par, t0 = par[keep], t0[keep]
        src = subs["src"][par]
        o = np.argsort(t0, kind="stable")
        return [(False, (par[o], t0[o], src[o], 0, _latency(w, src, 0)[o], w.rng_mark))] if par.size else None
    return None


def _latency(w, src, src0):
    """First-hop latency rows for these sources: a device's own row, or for a user's machine a row of its
    own, drawn once per run from the edit stream."""
    out = np.empty((src.size, P.N_NODES))
    own = src < src0 + P.MACHINE_OFFSET
    out[own] = w.lat_tab[src0][src[own] - src0]
    if (~own).any():
        key = src0 + P.MACHINE_OFFSET
        if key not in w.lat_tab:
            w.lat_tab[key] = w.rng_edit.uniform(*P.LAT_EXT_MS, size=(w.lat_tab[src0].shape[0], P.N_NODES)) / 1000
        out[~own] = w.lat_tab[key][src[~own] - key]
    return out


def _register(w, subs, lo, hi, split, gen):
    """Registry submissions and records of the transactions in [lo, hi): real ones below split, decoys from
    it. Gossip streams 2 gen and 2 gen + 1, so generation 0 draws exactly as before."""
    cfg = w.cfg
    S = hi - lo
    sub = np.arange(lo, hi)
    # registry submissions: every transaction. A decoy is a genuine transaction from a registered
    # credential held by the decoy infrastructure; it is approved, fanned out, posted and
    # finalized exactly as a real one. The decoy flag is truth only, for scoring real records.
    okf, oki = subs["ok_f"][lo:hi], subs["ok_i"][lo:hi]
    ev_rf, ev_ri = np.full(S, -1, np.int64), np.full(S, -1, np.int64)
    reach = np.full((2, S), np.nan)
    F, I, rf, ri = subs["F"][lo:hi], subs["I"][lo:hi], subs["reg_f"][lo:hi], subs["reg_i"][lo:hi]
    for stream, part in enumerate((sub < split, sub >= split)):
        f_, i_ = okf & part, oki & part
        origin = np.concatenate([F[f_], I[i_]])
        t_org = np.concatenate([rf[f_], ri[i_]])
        osub = np.concatenate([sub[f_], sub[i_]])
        legs = np.concatenate([np.full(f_.sum(), REG_F), np.full(i_.sum(), REG_I)])
        oids, rch = _gossip(w, origin, t_org, osub, legs, 2 * gen + stream)
        ev_rf[f_] = oids[:f_.sum()]
        ev_ri[i_] = oids[f_.sum():]
        reach[0, f_] = rch[:f_.sum()]
        reach[1, i_] = rch[f_.sum():]
    # the registry merges F's and I's submissions into one record at intake, once both have
    # reached every node, and posts it at the next boundary of its own posting schedule; the
    # posted time is the public record time
    intake = np.where(okf & oki, np.fmax(reach[0], reach[1]), np.nan)
    if cfg.reg_post_s > 0:
        ph = w.post_phase
        posted = ph + cfg.reg_post_s * np.ceil((intake - ph) / cfg.reg_post_s)
    else:
        posted = intake
    # the midpoint of F's and I's registry submissions (used only by a scoring diagnostic)
    mid = np.where(okf & oki, 0.5 * (rf + ri), np.nan)
    # when each submission's flood has reached every node: on the wire, the latest arrival of its flood frames
    for k, v in (("ev_reg_f", ev_rf), ("ev_reg_i", ev_ri), ("intake", intake), ("posted", posted), ("final", posted),
                 ("mid", mid), ("reach_f", reach[0]), ("reach_i", reach[1])):
        if k not in subs:
            subs[k] = np.full(subs["t0"].shape[0], -1 if k.startswith("ev_") else np.nan, v.dtype)
        elif subs[k].shape[0] < hi:
            subs[k] = np.r_[subs[k], np.full(hi - subs[k].shape[0], -1 if k.startswith("ev_") else np.nan, v.dtype)]
        subs[k][lo:hi] = v


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
               post_phase=w.post_phase, horizon=cfg.horizon_s)

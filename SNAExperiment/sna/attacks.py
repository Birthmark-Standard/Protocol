"""Vantages, answer lists, likelihood models, and the scoring of one run.

Every vantage links an item it holds to an answer on the wire. Registry vantages pick the registry
submission (a gossip flood origin) that belongs to their item's transaction; the content server
picks the validator reply (CV-2) that belongs to its content. Each vantage is scored twice on the
same traffic: with its own knowledge (the vantage attack) and with only what a passive observer of
every link has at the same anchoring event (its paired baseline). ANALYSIS_PLAN.md section 3.

Every server that can hold a role is compromised in turn: a row's group is the server that held
the item, and the joint assignment is solved per group.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from . import engine as E
from . import lottery as LT
from . import params as P
from . import sim as S

VANTAGES = ("baseline", "first_hop_cred", "first_hop_content", "cred_processor", "content_server",
            "validator", "gatekeeper")
CAN_TELL = ("cred_processor", "validator", "gatekeeper")        # separate decoys by construction
CANNOT_TELL = ("baseline", "first_hop_cred", "first_hop_content", "content_server")
LABEL = {"baseline": "Baseline", "first_hop_cred": "First hop, credential",
         "first_hop_content": "First hop, content", "cred_processor": "Credential processor",
         "content_server": "Content server", "validator": "Validator", "gatekeeper": "Gatekeeper"}
BW = 0.5                  # histogram bin width (s) of every delay model
BW_FINE = 0.05            # bin width when every hold is off (sensitivity control)


# =========================================================================== answer lists
def registry_answers(run, pools):
    """Registry submissions as a passive observer finds them: gossip frames (Noise record type,
    the gossip frame size) that one node sends to nearly every other node within 2 ms are a
    flood-publish burst. Submissions leaving one node on the same clock tick share a burst; the
    burst then carries one frame per submission to every peer, so the number of submissions is
    the smallest per-peer frame count. Returns answer times (sorted), the transaction each belongs
    to (truth, -1 if none) and each transaction's right answers."""
    ev, N = run.events, P.N_NODES
    idx = np.nonzero((ev["rtype"] == P.RT_NOISE) & (ev["size"] == pools.gossip_wire))[0]
    t, src = ev["t_send"][idx], ev["src"][idx]
    o = np.lexsort((t, src))
    idx, t, src = idx[o], t[o], src[o]
    new = np.ones(idx.size, bool)
    new[1:] = (src[1:] != src[:-1]) | (np.diff(t) > 2e-3)
    cid = np.cumsum(new) - 1
    starts = np.nonzero(new)[0]
    nc = starts.size
    per_dst = np.bincount(cid * N + ev["dst"][idx].astype(np.int64), minlength=nc * N).reshape(nc, N)
    per_dst[np.arange(nc), src[starts]] = np.iinfo(per_dst.dtype).max
    k = per_dst.min(1)                                 # submissions in each burst
    k = np.where(np.bincount(cid, minlength=nc) >= N - 4, k, 0)
    leg = ev["leg"][idx]
    is_org = (leg == S.REG_F) | (leg == S.REG_I)
    # truth: the distinct transactions whose origin frames are in each burst
    pairs = np.unique(np.c_[cid[is_org], ev["sub"][idx][is_org]], axis=0)
    t_c = t[starts]
    col_t, col_sub = [], []
    rank = np.zeros(nc, np.int64)
    for c_, sb in pairs:
        if rank[c_] < k[c_]:
            col_t.append(t_c[c_]); col_sub.append(sb)
        rank[c_] += 1
    extra = np.maximum(k - rank, 0)                    # bursts the truth cannot label
    col_t = np.r_[np.array(col_t, float), np.repeat(t_c, extra)]
    col_sub = np.r_[np.array(col_sub, np.int64), np.full(int(extra.sum()), -1, np.int64)]
    o = np.argsort(col_t, kind="stable")
    col_t, col_sub = col_t[o], col_sub[o]
    return col_t, col_sub, answers_of(col_sub, run.subs["t0"].shape[0])


def credential_answers(run, pools):
    """Validator replies on the wire: relay-class messages from the validator to a pool node,
    ordered by arrival at the credential processor."""
    ev = run.events
    lo, hi = P.PAD_MIN + pools.tls13_overhead, P.PAD_MAX + pools.tls13_overhead
    m = (ev["src"] == S.VAL) & (ev["dst"] < P.N_NODES) & (ev["rtype"] == P.RT_APPDATA) \
        & (ev["size"] >= lo) & (ev["size"] <= hi)
    cols = np.nonzero(m)[0]
    cols = cols[np.argsort(ev["t_arr"][cols], kind="stable")]
    csub = np.where(ev["leg"][cols] == S.CV2, ev["sub"][cols], -1).astype(np.int64)
    return ev["t_arr"][cols], csub, answers_of(csub, run.subs["t0"].shape[0])


def answers_of(col_sub, n_sub):
    """(n_sub, k) answer indices belonging to each transaction, -1 padded."""
    idx = np.nonzero(col_sub >= 0)[0]
    idx = idx[np.argsort(col_sub[idx], kind="stable")]
    subs = col_sub[idx]
    cnt = np.bincount(subs, minlength=n_sub)
    k = max(int(cnt.max()) if cnt.size else 1, 1)
    out = np.full((n_sub, k), -1, np.int64)
    first = np.concatenate([[0], np.cumsum(cnt)[:-1]])
    out[subs, np.arange(idx.size) - first[subs]] = idx
    return out


# =========================================================================== rows and anchors
def rows(run, v):
    """Every item a vantage holds in the run. Returns sub (transaction), group (the server holding
    the item), anchor_v (the vantage's anchor), anchor_b (its paired baseline's anchor), decoy,
    and, for the content server, its extra fields."""
    ev, s = run.events, run.subs
    n = s["t0"].shape[0]
    sub = np.arange(n)
    dec = s["decoy"]
    if v == "baseline":
        a = s["cv2_a"]
        return dict(sub=sub, group=np.zeros(n, int), anchor_v=a, anchor_b=a, decoy=dec)
    if v == "first_hop_cred":
        return dict(sub=sub, group=s["A"], anchor_v=ev["t_send"][s["ev_cred"][:, 1]],
                    anchor_b=ev["t_arr"][s["ev_cred"][:, 0]], decoy=dec)
    if v == "first_hop_content":
        return dict(sub=np.r_[sub, sub], group=np.r_[s["D"], s["G"]],
                    anchor_v=np.r_[ev["t_send"][s["ev_ca"][:, 1]], ev["t_send"][s["ev_cb"][:, 1]]],
                    anchor_b=np.r_[ev["t_arr"][s["ev_ca"][:, 0]], ev["t_arr"][s["ev_cb"][:, 0]]], decoy=np.r_[dec, dec])
    if v == "cred_processor":
        return dict(sub=sub, group=s["C"], anchor_v=np.sort(s["gk_send"], 1)[:, 1], anchor_b=s["cv2_a"], decoy=dec)
    if v == "validator":
        a = ev["t_send"][s["ev_cv2"]]
        return dict(sub=sub, group=np.zeros(n, int), anchor_v=a, anchor_b=a, decoy=dec)
    if v == "gatekeeper":
        return dict(sub=np.tile(sub, 3), group=np.repeat(run.gk_set, n),
                    anchor_v=s["posts"].T.ravel(), anchor_b=s["gk_arr"].T.ravel(), decoy=np.tile(dec, 3))
    if v == "content_server":
        arr = np.r_[s["arr_f"], s["arr_i"]]
        det = np.r_[s["det_f"], s["det_i"]]
        hold = np.r_[s["hold_f"], s["hold_i"]]
        return dict(sub=np.r_[sub, sub], group=np.r_[s["F"], s["I"]], anchor_v=det, anchor_b=arr,
                    arr=arr, det=det, cens=np.isfinite(det) & (np.abs(det - hold) < 1e-9), decoy=np.r_[dec, dec])
    raise KeyError(v)


def answers_for(v, run, pools, cache):
    key = "cred" if v == "content_server" else "reg"
    if key not in cache:
        cache[key] = credential_answers(run, pools) if key == "cred" else registry_answers(run, pools)
    return cache[key]


# =========================================================================== models
@dataclass
class Models:
    reg: dict = field(default_factory=dict)       # anchor name -> EmpiricalLogPDF of answer - anchor
    cs: dict = field(default_factory=dict)        # content server: d1/d2 per censoring class, d2 overall
    mc_runs: int = 0
    samples: dict = field(default_factory=dict)


def _true_deltas(anchor, sub, col_t, true_cols):
    tc = true_cols[sub]
    ok = tc >= 0
    d = np.where(ok, col_t[np.maximum(tc, 0)] - anchor[:, None], np.nan)
    return d[np.isfinite(d)]


def build_models(cfg: P.Config, pools, seed0=1_000_000_000, min_samples=150_000, max_runs=200) -> Models:
    """Monte Carlo of the protocol under the configuration attacked (background off, which enters
    none of these delays), on seeds disjoint from every evaluation seed. Delays do not depend on
    volume (no queueing), so one set of models serves every volume."""
    mc = cfg.with_(background_enabled=False, nonblending_enabled=False, decoy_rate=0.0,
                   real_rate=max(cfg.real_rate, 0.2))
    bw = BW if cfg.lottery_enabled else BW_FINE
    acc = {}
    k = 0
    while True:
        run = S.simulate(mc, seed0 + k, pools)
        cache = {}
        for v in VANTAGES:
            R = rows(run, v)
            real = ~R["decoy"]
            col_t, _, tc = answers_for(v, run, pools, cache)
            if v == "content_server":
                has = real & np.isfinite(R["det"])
                t_true = np.where(tc[R["sub"], 0] >= 0, col_t[np.maximum(tc[R["sub"], 0], 0)], np.nan)
                d1, d2 = R["det"] - t_true, R["arr"] - t_true
                for cls, m in (("c", has & R["cens"]), ("u", has & ~R["cens"])):
                    acc.setdefault(f"cs_{cls}_d1", []).append(d1[m])
                    acc.setdefault(f"cs_{cls}_d2", []).append(d2[m])
                acc.setdefault("cs_all_d2", []).append(d2[real & np.isfinite(d2)])
                continue
            for side in ("v", "b"):
                a = R[f"anchor_{side}"][real]
                acc.setdefault(f"{v}.{side}", []).append(_true_deltas(a, R["sub"][real], col_t, tc))
        k += 1
        have = min(sum(x.size for x in parts) for parts in acc.values())
        if (have >= min_samples and k >= 3) or k >= max_runs:
            break
    m = Models(mc_runs=k)
    for name, parts in acc.items():
        x = np.concatenate(parts)
        x = x[np.isfinite(x)]
        m.samples[name] = int(x.size)
        pdf = LT.EmpiricalLogPDF(x, bw)
        (m.cs if name.startswith("cs_") else m.reg)[name] = pdf
    return m


# =========================================================================== scoring
def _score_delay(anchor, pdf, col_t, true_cols, detail=None):
    ok = np.isfinite(anchor)
    a = np.where(ok, anchor, -1e12)

    def fn(r, c):
        return pdf(col_t[c] - a[r])
    t_lo = np.where(ok, a + pdf.support[0], np.inf)
    t_hi = np.where(ok, a + pdf.support[1], np.inf)
    return E.score_rows(t_lo, t_hi, col_t, fn, true_cols, detail=detail)


def _score_content_server(R, m: Models, col_t, true_cols, detail=None):
    cs = m.cs
    det, arr, cens = R["det"], R["arr"], R["cens"]
    has = np.isfinite(det)
    dd = np.where(has, det, 0.0)

    def fn(r, c):
        d1, d2 = dd[r] - col_t[c], arr[r] - col_t[c]
        w = np.where(cens[r], cs["cs_c_d1"](d1) + cs["cs_c_d2"](d2), cs["cs_u_d1"](d1) + cs["cs_u_d2"](d2))
        return np.where(has[r], w, cs["cs_all_d2"](d2))
    d1lo = min(cs["cs_c_d1"].support[0], cs["cs_u_d1"].support[0])
    d1hi = max(cs["cs_c_d1"].support[1], cs["cs_u_d1"].support[1])
    lo2, hi2 = cs["cs_all_d2"].support
    t_lo = np.where(has, dd - d1hi, arr - hi2)
    t_hi = np.where(has, dd - d1lo, arr - lo2) + 1e-9
    return E.score_rows(t_lo, t_hi, col_t, fn, true_cols, detail=detail)


def _score_baseline_cs(R, m, col_t, true_cols, detail=None):
    return _score_delay(R["arr"], _Shift(m.cs["cs_all_d2"]), col_t, true_cols, detail)


class _Shift:
    """answer - anchor model from an anchor - answer model (content arrival follows the reply)."""
    def __init__(self, pdf):
        self.pdf = pdf
        self.support = (-pdf.support[1], -pdf.support[0])

    def __call__(self, x):
        return self.pdf(-np.asarray(x))


def scored_mask(run, sub):
    t0 = run.subs["t0"][sub]
    return (t0 >= P.WARMUP_S) & (t0 < P.WARMUP_S + run.cfg.measure_s) & ~run.subs["decoy"][sub]


def score_vantage(run, pools, m: Models, v, cache):
    """Score one vantage and its paired baseline on one run. Returns the per-decision record for
    the scored rows (real items in the scored window), paired row by row."""
    R = rows(run, v)
    col_t, col_sub, tc = answers_for(v, run, pools, cache)
    real = ~R["decoy"]
    keep = scored_mask(run, R["sub"])
    if v == "content_server":
        keep &= np.isfinite(R["det"])              # a real item dropped at the timeout has no decision
    out = dict(sub=R["sub"][keep].astype(np.int32), group=R["group"][keep].astype(np.int16))
    for side in ("v", "b"):
        # the rows this side guesses for: every item held, decoys included unless it can tell.
        # The content server decides on quorum, which a decoy never reaches, so its own attack
        # guesses for the items that reached quorum; its baseline guesses for every item.
        if side == "v" and v in CAN_TELL:
            guess = real
        elif side == "v" and v == "content_server":
            guess = np.isfinite(R["det"])
        else:
            guess = np.ones_like(real)
        gi = np.nonzero(guess)[0]
        Rs = {k: x[gi] for k, x in R.items()}
        true_cols = tc[Rs["sub"]]
        detail = keep[gi] if side == "v" else np.zeros(gi.size, bool)     # confidence: vantage only
        if v == "content_server":
            res = _score_content_server(Rs, m, col_t, true_cols, detail) if side == "v" else \
                _score_baseline_cs(Rs, m, col_t, true_cols, detail)
        else:
            res = _score_delay(Rs[f"anchor_{side}"], m.reg[f"{v}.{side}"], col_t, true_cols, detail)
        dec = E.decide(res, Rs["group"], col_sub, Rs["sub"], true_cols)
        pos = np.full(R["sub"].shape[0], -1)
        pos[gi] = np.arange(gi.size)
        k = pos[keep]
        assert (k >= 0).all()
        out[f"{side}_correct"] = dec["correct_argmax"][k].astype(np.int8)
        out[f"{side}_correct_joint"] = dec["correct"][k].astype(np.int8)
        out[f"{side}_rand"] = E.random_baseline(res)[k].astype(np.float32)
        out[f"{side}_n_feas"] = res["n_feas"][k]
        out[f"{side}_rank"] = res["rank"][k]
        if side == "v":
            out["top1"] = res["top1"][k].astype(np.float32)
            out["top2"] = res["top2"][k].astype(np.float32)
            out["s_true"] = res["s_true"][k].astype(np.float32)
            out["n_true"] = res["n_true"][k]
            out["lse"] = res["lse"][k]
        out[f"{side}_rows"] = int(gi.size)
    return out


def compute(run, pools, m: Models, vantages=VANTAGES):
    cache = {}
    return {v: score_vantage(run, pools, m, v, cache) for v in vantages}

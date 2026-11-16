"""Experiments C3, C4 and C5: their jobs, cells, variants and the per-run worker.

Every job uses C2's main configuration, its calibrated D and its windows (results/C2/run_info.json), its
traffic seeds and its models, and changes only what its item changes. A job's runs are written as C2's are:
one raw file per (job, variant, cell), one pickle record per run, appended as runs finish, so a job can be
stopped and resumed. Results depend on the cell, the variant and the run id only.
"""
from __future__ import annotations

import hashlib
import math
import json
import pickle
import time
from pathlib import Path

import numpy as np

from . import attacks as AT
from . import coalition as CO
from . import decoys as DC
from . import devscore as DS
from . import experiment as EX
from . import params as P
from . import sim as S

ROOT = Path(__file__).resolve().parent.parent
C2_INFO = ROOT / "results" / "C2" / "run_info.json"
RATE_SEED0 = EX.MODEL_SEED0 + 50_000            # model seeds for the discounting attacker's rate model
EVAL_TAG = "sna-c3-c5-fresh"                   # the evaluation seed set of C3 to C5 (not C2's)
DRY_SEED0 = EX.MODEL_SEED0 + 300_000             # model seeds of dry runs: DRY_SEED0 + 1000 R + run id
SEED_SETS = ("evaluation", "model (dry run)")


def eval_seed(R, run_id):
    """The traffic seed of one full run of C3 to C5: SHA-256 of the tag, the cell and the run id."""
    h = hashlib.sha256(f"{EVAL_TAG}|R={R:g}|run={run_id}".encode()).digest()
    return int.from_bytes(h[:8], "little") >> 1


def dry_seed(R, run_id):
    """The traffic seed of one dry run: a model seed, disjoint from every model's own seeds."""
    return DRY_SEED0 + 1000 * int(R) + int(run_id)


def traffic(out, R, run_id):
    """The traffic seed for a run written to out: the seed set its run_info.json names."""
    key = ("seed_set", str(out))
    if key not in _C:
        p = Path(out) / "run_info.json"
        _C[key] = json.loads(p.read_text()).get("seed_set", SEED_SETS[0]) if p.exists() else SEED_SETS[0]
    return eval_seed(R, run_id) if _C[key] == SEED_SETS[0] else dry_seed(R, run_id)


def c2_info():
    return json.loads(C2_INFO.read_text())


def cell_config(R, decoys=EX.DECOYS, window=None, **kw):
    """The main configuration of one cell, with C2's D and windows, and the given options."""
    info = c2_info()
    D, win = info["D"][EX.MAIN], info["windows"][EX.MAIN]
    measure = EX.window_s(R, D, win["window"]) if window is None else window
    return P.Config(real_rate=R / D, decoy_rate=decoys / D, measure_s=measure, warmup_len=win["warmup"],
                    cooldown_len=win["cooldown"], **kw)


def rec_name(job, variant, R):
    return f"{job}__{variant}__R{R:g}"


# --------------------------------------------------------------------------- per-process caches
_C = {}


def models(out, name=EX.MAIN):
    key = ("models", name)
    if key not in _C:
        EX.ensure_models(out, name)
        with open(EX.model_path(out, name), "rb") as f:
            _C[key] = pickle.load(f)
    return _C[key]


def extra(out):
    if "extra" not in _C:
        _C["extra"] = CO.load_extra(Path(out) / "models" / "extra_main.pkl", P.Config(**EX.CONFIGS[EX.MAIN]), EX.MODEL_SEED0,
                                    models(out).pdf["gV"])
    return _C["extra"]


def roles(out):
    if "roles" not in _C:
        _C["roles"] = CO.load_roles(Path(out) / "models" / "roles_main.pkl", P.Config(**EX.CONFIGS[EX.MAIN]), models(out).pdf["g"])
    return _C["roles"]


def rate_model(cfg, key):
    if ("rate", key) not in _C:
        _C[("rate", key)] = DC.rate_model(cfg, [RATE_SEED0 + k for k in range(3)])
    return _C[("rate", key)]


def _rng(R, run_id):
    """C2's per-run scoring stream of the main configuration, so ties break and labels shuffle as in C2."""
    return np.random.default_rng([EX.SHUFFLE_SEED, list(EX.CONFIGS).index(EX.MAIN), int(R), run_id])


def _record(run_id, run, tables, t_sim, t_score, **kw):
    real, dec = EX.in_flight(run)
    return dict(run=run_id, sim_seconds=t_sim, score_seconds=t_score, vantages=tables,
                stats=dict(real_in_flight=real, decoys_in_flight=dec, transactions=int(run.subs["t0"].size)), **kw)


class _Hooks:
    """Collects the observer's device scores and each node's own-evidence ratios during compute."""

    def __init__(self, nodes=False):
        self.col = self.nodelr = None
        self.nodes = nodes

    def init(self, cand, rec, g):
        self.col = DS.Collector(rec["sub"].size, cand["dev"])
        if self.nodes:
            self.nodelr = CO.NodeLR(rec["sub"].size, cand, rec["u"], g)

    def dict(self):
        d = {"init": self.init, "observer": lambda rows, lo, hi, W: self.col(rows, lo, hi, W)}
        if self.nodes:
            d["node"] = lambda X, rows, lo, hi, W: self.nodelr(X, rows, lo, hi, W)
        return d


def _public(tables):
    return {k: v for k, v in tables.items() if not k.startswith("_")}


# --------------------------------------------------------------------------- C3
def work_c3_kc(out, R, variant, run_id):
    """Items 1 and 2 on C2's main traffic: decoy knowledge (none, one operator, both, validator of a
    manufacturer that keeps records) and the coalition vantages."""
    cfg = cell_config(R)
    t = time.time()
    run = S.simulate(cfg, traffic(out, R, run_id))
    t_sim = time.time() - t
    m, ex = models(out), extra(out)
    res = []
    t = time.time()
    hk = _Hooks(nodes=True)
    tab = AT.compute(run, m, _rng(R, run_id), hooks=hk.dict())
    vx = CO.validator_with_node(run, m, ex, tab, hk.nodelr)
    pc = CO.path_coalitions(run, ex, tab)
    rx = roles(out)
    same = CO.same_role(run, m, ex, rx, tab, R, run_id)            # item 7
    nodes = CO.compromised(run, m, ex, rx, tab, R, run_id)          # item 8
    t1 = time.time() - t
    res.append((rec_name("c3_knowledge", "none", R), _record(run_id, run, _public(tab), t_sim, t1)))
    res.append((rec_name("c3_coalition", "all", R), _record(run_id, run, {"validator_with_node": vx, "first_relay_with_destination": pc,
                                                                          **same, **nodes}, t_sim, 0.0)))
    op_a, op_b = DC.operators(run, R, run_id)
    decoy_ids = np.r_[op_a, op_b]
    for v, kw in (("one", dict(drop_dev=op_a, drop_dev_validator=op_a)), ("both", dict(drop_dev=decoy_ids, drop_dev_validator=decoy_ids)),
                  ("manufacturer", dict(vantages=("validator",), drop_dev_validator=decoy_ids))):
        t = time.time()
        tab = AT.compute(run, m, _rng(R, run_id), **kw)
        res.append((rec_name("c3_knowledge", v, R), _record(run_id, run, tab, 0.0, time.time() - t,
                                                           known=int(len(kw.get("drop_dev", kw.get("drop_dev_validator", [])))))))
    return res


def work_c3_conc(out, R, variant, run_id):
    """Item 3: fewer, faster decoy identities; the observer with and without the discount."""
    f = float(variant[1:])
    cfg = cell_config(R, decoy_factor=f)
    t = time.time()
    run = S.simulate(cfg, traffic(out, R, run_id))
    t_sim = time.time() - t
    t = time.time()
    hk = _Hooks()
    tab = AT.compute(run, models(out), _rng(R, run_id), vantages=("observer",), hooks=hk.dict())
    rm = rate_model(cfg, (R, f))
    tab["observer_discount"] = DC.discounted(run, tab, hk.col, rm)
    return [(rec_name("c3_concentration", variant, R), _record(run_id, run, _public(tab), t_sim, time.time() - t, rate_model=rm))]


VALIDATORS = dict(n_validators=3, real_val_split=(0.5, 0.3, 0.2), decoy_val_split=(0.5, 0.3, 0.2))


def work_c3_val(out, R, variant, run_id):
    """Item 9: three validators; the observer, the validators (all, and each alone), and C with and without key_ref."""
    cfg = cell_config(R, **VALIDATORS)
    t = time.time()
    run = S.simulate(cfg, traffic(out, R, run_id))
    t_sim = time.time() - t
    t = time.time()
    tab = AT.compute(run, models(out), _rng(R, run_id), vantages=("observer", "validator", "cred_processor"))
    return [(rec_name("c3_validators", variant, R), _record(run_id, run, tab, t_sim, time.time() - t))]


def work_c3_vol(out, R, variant, run_id):
    """Item 4: decoy volume; every vantage."""
    v = float(variant[1:])
    cfg = cell_config(R, decoys=v)
    t = time.time()
    run = S.simulate(cfg, traffic(out, R, run_id))
    t_sim = time.time() - t
    t = time.time()
    tab = AT.compute(run, models(out), _rng(R, run_id))
    return [(rec_name("c3_volume", variant, R), _record(run_id, run, tab, t_sim, time.time() - t))]


# --------------------------------------------------------------------------- C4: ceiling, K records, chains, workloads
C4_WINDOW_R100 = 2 * 3600.0                    # the R = 100 cell's window, so a device has records enough for K up to 5
CHAIN_WARMUP_EXTRA = 3 * 3600.0                # chains reach a steady state only after several generations
C4_VARIANTS = {"W0": {}, "W1": dict(workload="W1"), "W2": dict(workload="W2"), "Wmis": dict(workload="Wmis"),
               "chain100": dict(edit_share=0.3, edit_same_source=1.0), "chain50": dict(edit_share=0.3, edit_same_source=0.5)}


def c4_config(R, variant):
    kw = C4_VARIANTS[variant]
    cfg = cell_config(R, window=C4_WINDOW_R100 if R == 100 else None, **kw)
    if kw.get("edit_share", 0) > 0:
        cfg = cfg.with_(warmup_len=cfg.warmup_s + CHAIN_WARMUP_EXTRA)
    return cfg


def work_c4_obs(out, R, variant, run_id):
    """Items 5a, 7, 8 and the chain variant: the observer, its device scores for K records and chains, and the
    ceiling attacker, under one workload or chain setting."""
    from . import krecord as KR
    cfg = c4_config(R, variant)
    t = time.time()
    run = S.simulate(cfg, traffic(out, R, run_id))
    t_sim = time.time() - t
    m = models(out)
    t = time.time()
    hk = _Hooks()
    tab = AT.compute(run, m, _rng(R, run_id), vantages=("observer",), hooks=hk.dict())
    rec, tie = tab["_rec"], tab["_tie"]
    n = rec["sub"].size
    s = run.subs
    root = s["root"][rec["sub"]]
    meta = dict(sub=rec["sub"].astype(np.int32), dev=rec["dev"], u=rec["u"], root=root,
                root_dev=tie(s["src"][root].astype(np.int64) % P.MACHINE_OFFSET), gen=s["gen"][rec["sub"]])
    r = dict(vec=KR.vectors(hk.col, n), meta=meta,
             ceiling=KR.ceiling(run, rec, np.random.default_rng([CEIL_SEED, int(R), run_id])))
    if "edit_share" in C4_VARIANTS[variant]:
        par = s["parent"][rec["sub"]]
        lb = np.where(par >= 0, s["posted"][np.maximum(par, 0)], -np.inf)
        r["vec_lb"] = KR.lower_bound_pass(run, m, tab, lb)
    rec_ = _record(run_id, run, _public(tab), t_sim, time.time() - t, **r)
    return [(rec_name("c4_obs", variant, R), rec_)]


CEIL_SEED = 16_000_000


# --------------------------------------------------------------------------- C6: the two candidates
OTC_HOLD_S = 693.0                               # the lengthened-hold variant's device hold: the credential path's latency
C6_CANDIDATES = {"cp": {}, "otc": dict(candidate=P.CANDIDATES[1]),
                 "otcL": dict(candidate=P.CANDIDATES[1], otc_hold_mean=OTC_HOLD_S)}
C6_VARIANTS = tuple(f"{c}_{w}" for c in C6_CANDIDATES for w in C4_VARIANTS)
OTC_MODEL_SEED0 = EX.MODEL_SEED0 + 400_000


def c6_config(R, variant):
    c, w = variant.split("_", 1)
    cfg = c4_config(R, w).with_(**VALIDATORS, **C6_CANDIDATES[c])
    return cfg


def otc_models(out, lengthened):
    from . import onetime as OT
    key = ("otc", lengthened)
    if key not in _C:
        p = Path(out) / "models" / f"otc_{'lengthened' if lengthened else 'natural'}.pkl"
        if p.exists():
            _C[key] = pickle.loads(p.read_bytes())
        else:
            cfg = P.Config(candidate=P.CANDIDATES[1], otc_hold_mean=OTC_HOLD_S if lengthened else 0.0, **VALIDATORS)
            _C[key] = OT.build_models(cfg, seed0=OTC_MODEL_SEED0 + (10_000 if lengthened else 0))
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(pickle.dumps(_C[key]))
    return _C[key]


C6_ISSUER = {f"iwh_{mode}_L{int(L // 60)}": dict(withhold_mode=mode, withhold_len=float(L))
             for mode in ("none", "withhold", "delay") for L in (600, 1800, 3600, 7200)}


def work_c6_issuer(out, R, setting, run_id):
    """C6 item 8: the target's issuer withholds or delays every other refill of its identities inside each window
    (mode none: nothing withheld), then finds the record of each target capture whose refill fell in a window."""
    from . import onetime as OT
    target = 0 if R == 1 else int(np.random.default_rng([TARGET_SEED, int(R), run_id]).integers(0, cell_config(R).real_devices))
    base = cell_config(R, window=C5_WINDOW, candidate=P.CANDIDATES[1], mark_actor="issuer_withhold", mark_target=target,
                       **VALIDATORS, **C6_ISSUER[setting])
    t = time.time()
    run = OT.simulate(base, traffic(out, R, run_id))
    t_sim = time.time() - t
    t = time.time()
    res = OT.issuer_find(run, otc_models(out, False).pdf["gT"], np.random.default_rng([CEIL_SEED + 2, int(R), run_id]),
                         (base.warmup_s, base.warmup_s + base.measure_s))
    s = run.subs
    mine = (s["src"] == target) & ~s["decoy"]
    rec = dict(run=run_id, sim_seconds=t_sim, score_seconds=time.time() - t, target=target, marks=res,
               target_transactions=int(res["sub"].size), target_key=int(s["issuer"][mine][0]) if mine.any() else -1,
               waited=int((s["ready"] > s["t0"] + 1e-9).sum()))
    return [(rec_name("c6_issuer", setting, R), rec)]


def _latency(run, rec_sub):
    s = run.subs
    return float(np.mean(s["posted"][rec_sub] - s["t0"][rec_sub])) if rec_sub.size else float("nan")


def work_c6(out, R, variant, run_id):
    """C6: one candidate under one workload or chain setting: every vantage both candidates have, the second
    candidate's issuers and coalitions, the observer's device scores for K records and chains, and the latency."""
    from . import krecord as KR
    from . import onetime as OT
    cfg = c6_config(R, variant)
    otc = OT.is_onetime(cfg)
    t = time.time()
    run = (OT.simulate if otc else S.simulate)(cfg, traffic(out, R, run_id))
    t_sim = time.time() - t
    t = time.time()
    hk = _Hooks()
    if otc:
        m = otc_models(out, cfg.otc_hold_mean > 0)
        pick = int(CO._pick(R, run_id, 4, 1, np.arange(P.N_NODES))[0])
        tab = OT.compute(run, m, _rng(R, run_id), hooks=hk.dict(), pick=pick)
    else:
        m = models(out)
        tab = AT.compute(run, m, _rng(R, run_id), vantages=("observer", "first_hop", "content_server"), hooks=hk.dict())
        pc = CO.path_coalitions(run, extra(out), tab)
        content = pc["path"] > 0
        tab["first_relay_with_destination"] = {k: (v[content] if isinstance(v, np.ndarray) and v.shape[:1] == content.shape else v)
                                               for k, v in pc.items()}
    rec, tie = tab["_rec"], tab["_tie"]
    s = run.subs
    root = s["root"][rec["sub"]]
    meta = dict(sub=rec["sub"].astype(np.int32), dev=rec["dev"], u=rec["u"], root=root,
                root_dev=tie(s["src"][root].astype(np.int64) % P.MACHINE_OFFSET), gen=s["gen"][rec["sub"]])
    r = dict(vec=KR.vectors(hk.col, rec["sub"].size), meta=meta,
             ceiling=KR.ceiling(run, rec, np.random.default_rng([CEIL_SEED, int(R), run_id])),
             latency=_latency(run, rec["sub"]), candidate=cfg.candidate, otc_hold_mean=cfg.otc_hold_mean)
    if cfg.edit_share > 0:
        par = s["parent"][rec["sub"]]
        lb = np.where(par >= 0, s["posted"][np.maximum(par, 0)], -np.inf)
        r["vec_lb"] = KR.lower_bound_pass(run, m, tab, lb)
    if otc:
        r["refills_in_window"] = int(((run.refills["t"] >= cfg.warmup_s) & (run.refills["t"] < cfg.warmup_s + cfg.measure_s)).sum())
    return [(rec_name("c6", variant, R), _record(run_id, run, _public(tab), t_sim, time.time() - t, **r))]


# --------------------------------------------------------------------------- C5: active attacks
C5_WINDOW = 67 * 3600.0                        # about 200 of the target's transactions per run
C5_DELTAS = (0, 60, 300, 600, 900, 1200, 1500, 1800, 2400, 3600)
C5_RESUB = (1800, 3600, 7200, 21600)
C5_WITHHOLD_SHARE = (0.1, 0.25, 0.5, 1.0)
C5_WITHHOLD_LEN = (600, 1800, 3600, 7200)
TARGET_SEED, C5_MODEL_SEED0 = 17_000_000, EX.MODEL_SEED0 + 60_000


def c5_settings():
    """Every setting: delay marks by each actor at the specification's timeout, the validator and the first relay
    at the two shorter timeouts, content-side marks with the match board window, and drops with resubmission."""
    out = {}
    for actor in ("first_relay", "access", "access_one", "validator"):
        for d in C5_DELTAS:
            out[f"{actor}_d{d}_t1800"] = dict(mark_actor=actor, mark_delta=float(d))
    for actor in ("first_relay", "validator"):
        for T in (1500, 1200):
            for d in C5_DELTAS:
                out[f"{actor}_d{d}_t{T}"] = dict(mark_actor=actor, mark_delta=float(d), quorum_timeout_s=float(T))
    for actor in ("first_relay", "access", "access_one"):
        for d in (600, 900, 1200, 1500, 1800, 2400):
            out[f"{actor}_d{d}_bw"] = dict(mark_actor=actor, mark_delta=float(d), board_window_s=1800.0)
    for actor in ("first_relay", "access"):
        for mres in C5_RESUB:
            out[f"{actor}_drop_m{mres}"] = dict(mark_actor=actor, mark_mode="drop", resub_mean_s=float(mres))
    for mode in ("withhold", "delay"):
        for L in C5_WITHHOLD_LEN:
            out[f"vwh3_{mode}_L{int(L // 60)}"] = dict(mark_actor="validator_withhold", withhold_mode=mode,
                                                       withhold_len=float(L), **VALIDATORS)
    for mode in ("withhold", "delay"):
        for share in C5_WITHHOLD_SHARE:
            for L in C5_WITHHOLD_LEN:
                out[f"vwh_{mode}_s{int(share * 100)}_L{int(L // 60)}"] = dict(
                    mark_actor="validator_withhold", withhold_mode=mode, withhold_share=share, withhold_len=float(L))
    return out


C5_SETTINGS = c5_settings()


def c5_config(R, setting, target):
    base = cell_config(R, window=C5_WINDOW, mark_target=target, **C5_SETTINGS[setting])
    return base.with_(cooldown_len=base.cooldown_len + max(C5_DELTAS))


def c5_model(out, setting):
    """The attacker's model of the marked system: record time minus anchor, every real device marked, on the
    model seeds (R = 100, a 6-hour window). Withholding leaves the target's own transactions unchanged, so the
    withholding validator uses the unmarked validator's model."""
    if setting.startswith("vwh"):
        setting = "validator_d0_t1800"
    key = ("c5", setting)
    if key in _C:
        return _C[key]
    p = Path(out) / "models" / f"c5_{setting}.pkl"
    if p.exists():
        with open(p, "rb") as f:
            _C[key] = pickle.load(f)
        return _C[key]
    from . import active as AC
    cfg = cell_config(100, window=6 * 3600.0, mark_target=-2, **C5_SETTINGS[setting])
    cfg = cfg.with_(cooldown_len=cfg.cooldown_len + max(C5_DELTAS))
    pdf, n = AC.build_model(cfg, [C5_MODEL_SEED0 + k for k in range(6)])
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(f".{np.random.default_rng().integers(1 << 30)}.tmp")
    with open(tmp, "wb") as f:
        pickle.dump((pdf, n), f)
    tmp.replace(p)
    _C[key] = (pdf, n)
    return _C[key]


def _build_c5_model(out, setting):
    c5_model(out, setting)
    return []


def work_c5(out, R, setting, run_id):
    from . import active as AC
    target = 0 if R == 1 else int(np.random.default_rng([TARGET_SEED, int(R), run_id]).integers(0, cell_config(R).real_devices))
    cfg = c5_config(R, setting, target)
    t = time.time()
    run = S.simulate(cfg, traffic(out, R, run_id))
    t_sim = time.time() - t
    t = time.time()
    pdf, n_model = c5_model(out, setting)
    window = (cfg.warmup_s, cfg.warmup_s + cfg.measure_s)
    res = AC.score(run, pdf, np.random.default_rng([CEIL_SEED + 1, int(R), run_id]), window)
    s = run.subs
    mine = (s["src"] == target) & ~s["decoy"] & (s["gen"] == 0) & (s["t0"] >= window[0]) & (s["t0"] < window[1])
    fixed = ((s["A"] == 0) | (s["D"] == 0) | (s["G"] == 0))[mine]
    held = s["withheld"]
    rec = dict(run=run_id, sim_seconds=t_sim, score_seconds=time.time() - t, target=target, marks=res,
               withheld=int(held.sum()), withheld_dropped=int((held & ~np.isfinite(s["posted"])).sum()),
               target_transactions=int(mine.sum()), fixed_node_share=float(fixed.mean()) if fixed.size else float("nan"),
               target_key=int(s["val"][(s["src"] == target) & ~s["decoy"]][0]) if ((s["src"] == target) & ~s["decoy"]).any() else -1,
               model_samples=n_model)
    return [(rec_name("c5", setting, R), rec)]


# --------------------------------------------------------------------------- the jobs
JOBS = {
    "c3_kc": dict(fn=work_c3_kc, cells=(1, 100), variants=("all",), files=("c3_knowledge", "c3_coalition")),
    "c3_kc_r300": dict(fn=work_c3_kc, cells=(300,), variants=("all",), files=("c3_knowledge", "c3_coalition")),
    "c3_conc": dict(fn=work_c3_conc, cells=(1, 100), variants=("f5", "f25"), files=("c3_concentration",)),
    "c3_vol": dict(fn=work_c3_vol, cells=(1, 100), variants=("v50", "v10", "v0"), files=("c3_volume",)),
    "c4_obs": dict(fn=work_c4_obs, cells=(1, 100), variants=tuple(C4_VARIANTS), files=("c4_obs",)),
    "c5_marks": dict(fn=work_c5, cells=(1, 100), variants=tuple(k for k in C5_SETTINGS if "_drop_" not in k and not k.startswith("vwh")),
                     files=("c5",)),
    "c5_drops": dict(fn=work_c5, cells=(1, 100), variants=tuple(k for k in C5_SETTINGS if "_drop_" in k), files=("c5",)),
    "c5_withhold": dict(fn=work_c5, cells=(1, 100), variants=tuple(k for k in C5_SETTINGS if k.startswith("vwh_")), files=("c5",)),
    "c3_val": dict(fn=work_c3_val, cells=(1, 100), variants=("v3",), files=("c3_validators",)),
    "c6": dict(fn=work_c6, cells=(1, 100), variants=C6_VARIANTS, files=("c6",)),
    "c6_issuer": dict(fn=work_c6_issuer, cells=(1, 100), variants=tuple(C6_ISSUER), files=("c6_issuer",)),
    "c5_withhold3": dict(fn=work_c5, cells=(1, 100), variants=tuple(k for k in C5_SETTINGS if k.startswith("vwh3_")), files=("c5",)),
}


def worker(out, job, R, variant, run_id):
    return JOBS[job]["fn"](out, R, variant, run_id)


def first_file(job, variant, R):
    """The file whose runs mark a task as done: the job's first output file for the cell."""
    j = JOBS[job]
    v = variant if j["files"][0] != "c3_knowledge" else "none"
    return rec_name(j["files"][0], v, R)


def tasks(out, job, runs, done):
    j = JOBS[job]
    return [(str(out), job, R, v, k) for k in range(runs) for R in j["cells"] for v in j["variants"]
            if k not in done(first_file(job, v, R))]


def job_hash(job):
    """Fingerprint of a job's settings: its cells, variants and the base configuration."""
    j = JOBS[job]
    blob = json.dumps(dict(job=job, cells=j["cells"], variants=j["variants"], base=P.Config().hash_dict(),
                           c2=c2_info()["config_hash"]), sort_keys=True, default=str)
    return hashlib.sha256(blob.encode()).hexdigest()[:16]


# --------------------------------------------------------------------------- running and summarizing
EXPERIMENT_OF = {"c3": "C3", "c4": "C4", "c5": "C5", "c6": "C6"}


def git_commit(path=None):
    import subprocess
    try:
        args = ["git", "log", "-1", "--format=%H"] + (["--", str(path)] if path else [])
        return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def run(out, jobs, runs, workers="auto", label=None, dry=False):
    """Run the given jobs' runs not yet on disk, then write the summary of each experiment present. A dry run uses
    model seeds (dry_seed) and is labelled as one; a full run uses the evaluation seed set (eval_seed)."""
    from . import runner as RN
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    p = out / "run_info.json"
    info = json.loads(p.read_text()) if p.exists() else {}
    for job in jobs:
        h = job_hash(job)
        old = info.setdefault("jobs", {}).get(job)
        if old and old["hash"] != h:
            raise SystemExit(f"{out} holds {job} runs made under other settings. Use a new folder.")
        info["jobs"][job] = dict(hash=h, cells=list(JOBS[job]["cells"]), variants=list(JOBS[job]["variants"]),
                                 runs=max(runs, (old or {}).get("runs", 0)))
    exp = {EXPERIMENT_OF[j[:2]] for j in jobs}
    seed_set = SEED_SETS[1] if dry else SEED_SETS[0]
    if info.get("seed_set", seed_set) != seed_set:
        raise SystemExit(f"{out} holds runs on the {info['seed_set']} seeds. Use a new folder.")
    info["seed_set"] = seed_set
    if dry:
        label = label if (label or "").startswith("dry") else "dry run" + (f": {label}" if label else "")
    info.setdefault("code_commit", git_commit())
    info.setdefault("predictions_commit", {e: git_commit(ROOT / f"PREDICTIONS_{e}.md") for e in ("C3", "C4", "C5", "C6")})
    info.setdefault("c2_config_hash", c2_info()["config_hash"])
    info.setdefault("seeds", dict(traffic=(f"sha256 of '{EVAL_TAG}', the volume and the run id" if not dry else
                                           f"{DRY_SEED0} + 1000 R + run id (model seeds)"), models=EX.MODEL_SEED0, rates=RATE_SEED0,
                                  operators=DC.OPS_SEED, coalitions=CO.COALITION_SEED))
    v = EX.versions()
    if "versions" not in info:
        info["versions"] = v
    elif info["versions"] != v:
        info.setdefault("versions_on_resume", []).append(v)
    if label:
        info["label"] = label
    p.write_text(json.dumps(info, indent=1))
    models(out)
    if any(j.startswith("c3_kc") for j in jobs):
        extra(out)
    c5 = sorted({("validator_d0_t1800" if v.startswith("vwh") else v) for j in jobs if j.startswith("c5") for v in JOBS[j]["variants"]})
    if c5:
        RN.execute([(str(out), v) for v in c5 if not (out / "models" / f"c5_{v}.pkl").exists()], _build_c5_model, out,
                   workers, label="c5 models")
    done = lambda name: RN.done_runs(out, name)  # noqa: E731
    todo = []
    for job in jobs:
        todo += tasks(out, job, runs, done)
    t0 = time.time()
    RN.execute(todo, worker, out, workers, label=",".join(jobs))
    info = json.loads(p.read_text())
    info.setdefault("elapsed_min", {})[",".join(jobs)] = (time.time() - t0) / 60
    p.write_text(json.dumps(info, indent=1))
    summarize(out, info.get("label", "").startswith("dry"))


def summarize(out, dry=False):
    from . import report345 as RP
    out = Path(out)
    names = sorted(p.name[:-len(".pkl.gz")] for p in (out / "raw").glob("*.pkl.gz"))
    fs6 = [n for n in names if n.startswith("c6__")]
    fsi = [n for n in names if n.startswith("c6_issuer__")]
    if fs6 or fsi:
        rows = RP.summarize_c6(out, fs6) if fs6 else []
        for r in RP.summarize_c5(out, fsi):
            r.update(candidate=RP.C6_LABEL["otc"], workload="W0", cell=r["file"].split("__")[2], latency=math.nan,
                     family="issuer withholding or delaying refills")
            rows.append(r)
        RP.write_c6(out, rows, dry)
    for exp in ("c3", "c4", "c5"):
        fs = [n for n in names if n.startswith(exp + "_")]
        if not fs:
            continue
        if exp == "c3":
            rows = RP.summarize(out, fs, **_c3_summary())
        elif exp == "c4":
            rows = RP.summarize_c4(out, fs)
        else:
            rows = RP.summarize_c5(out, fs)
        RP.write(out, rows, f"TABLES_{exp.upper()}", f"Experiment {exp.upper()}", dry)


def costs(out):
    """Mean worker seconds of one task (one run of one job variant in one cell), from the raw files: the sum over
    the files the task writes of their simulation and scoring seconds."""
    from . import runner as RN
    out = Path(out)
    rows = {}
    for p in sorted((out / "raw").glob("*.pkl.gz")):
        name = p.name[:-len(".pkl.gz")]
        prefix, variant, cell = name.split("__")
        job = next((j for j, d in JOBS.items() if prefix in d["files"] and (variant in d["variants"] or d["files"][0] == "c3_knowledge")
                    and float(cell[1:]) in d["cells"]), prefix)
        key = (job, variant if job not in ("c3_kc", "c3_kc_r300") else "all", cell)
        for r in RN.load(out, name):
            a = rows.setdefault(key, {})
            a[r["run"]] = a.get(r["run"], 0.0) + r.get("sim_seconds", 0.0) + r.get("score_seconds", 0.0)
    return {k: float(np.mean(list(v.values()))) for k, v in rows.items()}


def _c3_summary():
    from . import coalition as CO_
    roles = {None: "all records", **{i: c for i, c in enumerate(CO_.ROLE_CLASSES)}}
    paths = {0: "credential path, A with C", 1: "F content path, D with F", 2: "I content path, G with I"}

    def decoys_of(job, variant):
        return float(variant[1:]) if job == "c3_volume" else 100.0
    held = {None: "all records", 0: "none held", 1: "one held", 2: "two held", 3: "three held"}
    ncls = {None: "all records", **{i: c for i, c in enumerate(CO_.NODE_CLASSES)}}
    classes = {"validator_with_node": ("role", roles), "first_relay_with_destination": ("path", paths)}
    classes.update({f"{r}_relays_{k}": ("held", held) for r in ("first", "second") for k in CO_.RELAY_SIZES})
    classes.update({f"nodes_{k}": ("cls", ncls) for k in CO_.NODE_COUNTS})
    shares = VALIDATORS["real_val_split"]
    classes.update({f"validator_{k}": ("own", {None: f"share {100 * shares[k]:g}%, all records",
                                              1: f"share {100 * shares[k]:g}%, its own devices", 0: "other keys' devices"})
                    for k in range(VALIDATORS["n_validators"])})
    took = {None: "all records", 1: "C's own transactions"}
    classes.update({"cred_processor": ("took_part", took), "cred_processor_keyed": ("took_part", took)})
    return dict(classes=classes, decoys_of=decoys_of,
                bound_na={"content_server", "content_server_mid", "validator_with_node [F or I]",
                          "first_relay_with_destination [F content path, D with F]",
                          "first_relay_with_destination [I content path, G with I]", "f_with_i",
                          *(f"nodes_{k} [all records]" for k in CO_.NODE_COUNTS)})



def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(prog="python -m sna.stronger")
    ap.add_argument("jobs", nargs="+", choices=sorted(JOBS))
    ap.add_argument("--runs", type=int, default=100)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", default="auto")
    ap.add_argument("--label", default=None)
    ap.add_argument("--dry", action="store_true", help="a dry run on model seeds, labelled as one")
    a = ap.parse_args(argv)
    run(a.out, a.jobs, a.runs, a.workers, a.label, a.dry)


if __name__ == "__main__":
    main()

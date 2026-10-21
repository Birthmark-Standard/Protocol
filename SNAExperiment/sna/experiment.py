"""InternalCompromiseRun: its builds and cells, seeds, the end-to-end delay calibration, the
attacker's models, and the per-run worker, with the latency, pair-timing and hold-timing
measurements.

A cell is a real volume R (real transactions in flight) with 60 decoy transactions in flight.
Rates follow from the measured end-to-end delay D (capture to registry finalization): real rate
R / D, decoy rate 60 / D. A decoy is a genuine transaction from one of the decoy infrastructure's
registered identities, each capturing at a device's rate.

A build is the protocol as attacked. internal_compromise is the protocol with every hold at the
specification's timing; each other build removes one mechanism or changes one setting, and is
paired against internal_compromise record by record.
"""
from __future__ import annotations

import hashlib
import json
import pickle
import time
from pathlib import Path

import numpy as np

from . import attacks as AT
from . import params as P
from . import runner as RN
from . import sim as S

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
EXPERIMENT = "InternalCompromiseRun"

REAL_R = (1, 20, 100)                            # real transactions in flight
DECOYS = 60                                      # decoy transactions in flight
RUNS = 200                                       # runs per cell

BASELINE = "internal_compromise"
_NONE = dict(c_hold_mean=0.0, v_hold_mean=0.0, gk_inclusion=False, post_match=False, reg_bundle_s=0.0,
             dev_content_mean=120.0, cs_mean=120.0)
BUILDS = {
    BASELINE: {},
    # each mechanism removed in turn
    "no_vc_holds": dict(c_hold_mean=0.0, v_hold_mean=0.0),
    "no_inclusion_lottery": dict(gk_inclusion=False),
    "no_post_match_lottery": dict(post_match=False),
    "no_registry_bundling": dict(reg_bundle_s=0.0),
    "no_role_aware_holds": dict(dev_content_mean=120.0, cs_mean=120.0),
    "no_mechanisms": _NONE,
    # alternative settings
    "relay_180s": dict(relay_mean=180.0),
    "role_aware_360s": dict(dev_content_mean=360.0, cs_mean=360.0),
    "gatekeeper_120s": dict(gk_mean=120.0),
    # the routing design's permitted coincidences between roles on different paths
    "permitted_overlap": dict(overlap=True),
}
# controls, run on request and never part of reproduce: every hold and lottery off
CONTROLS = {
    "overlap_no_holds": dict(overlap=True, relay_mean=0.0, dev_cred_mean=0.0, dev_content_mean=0.0, c_hold_mean=0.0,
                             v_hold_mean=0.0, fanout_mean=0.0, gk_mean=0.0, gk_inclusion=False, cs_mean=0.0,
                             post_match=False, reg_bundle_s=0.0),
    # first-relay signal: only the relay holds (120 s) and one device channel's hold (240 s) are on, so the
    # record time follows one path's relay holds and a first relay on that path knows its own share of them
    "first_relay_signal_cred": dict(overlap=True, relay_mean=120.0, dev_cred_mean=240.0, dev_content_mean=0.0,
                                    c_hold_mean=0.0, v_hold_mean=0.0, fanout_mean=0.0, gk_mean=0.0, gk_inclusion=False,
                                    cs_mean=0.0, post_match=False, reg_bundle_s=0.0),
    "first_relay_signal_content": dict(overlap=True, relay_mean=120.0, dev_cred_mean=0.0, dev_content_mean=240.0,
                                       c_hold_mean=0.0, v_hold_mean=0.0, fanout_mean=0.0, gk_mean=0.0, gk_inclusion=False,
                                       cs_mean=0.0, post_match=False, reg_bundle_s=0.0),
    # one content path carries the signal: the device holds only its F channel (240 s)
    "first_relay_signal_one_content": dict(overlap=True, relay_mean=120.0, dev_cred_mean=0.0, dev_content_mean=240.0,
                                           dev_content_i_mean=0.0, c_hold_mean=0.0, v_hold_mean=0.0, fanout_mean=0.0,
                                           gk_mean=0.0, gk_inclusion=False, cs_mean=0.0, post_match=False, reg_bundle_s=0.0),
}
ALL_BUILDS = {**BUILDS, **CONTROLS}
LABEL = {
    BASELINE: EXPERIMENT,
    "no_vc_holds": "without V's and C's holds",
    "no_inclusion_lottery": "without the inclusion lottery (next-boundary bundling)",
    "no_post_match_lottery": "without the post-match lottery",
    "no_registry_bundling": "without registry bundling",
    "no_role_aware_holds": "without role-aware holds (device content and F/I at 120 s)",
    "no_mechanisms": "without all five",
    "relay_180s": "relay hops at 180 s",
    "role_aware_360s": "device content and F/I at 360 s",
    "gatekeeper_120s": "gatekeeper hold at 120 s",
    "permitted_overlap": "permitted overlap",
    "overlap_no_holds": "permitted overlap, every hold off",
    "first_relay_signal_cred": "permitted overlap, credential path dominates the record time",
    "first_relay_signal_content": "permitted overlap, content paths dominate the record time",
    "first_relay_signal_one_content": "permitted overlap, the F content path dominates the record time",
}
REMOVALS = ("no_vc_holds", "no_inclusion_lottery", "no_post_match_lottery", "no_registry_bundling",
            "no_role_aware_holds", "no_mechanisms")
ALTERNATIVES = ("relay_180s", "role_aware_360s", "gatekeeper_120s")

CAL_SEED0, MODEL_SEED0 = 2_000_000_000, 1_000_000_000
LATENCY_SEED0, PAIRS_SEED0, TIMING_SEED0 = 3_000_000, 8_000_000, 11_000_000


def cell_key(R, decoys=DECOYS):
    return f"R{R:g}_D{decoys:g}"


def grid(build=BASELINE):
    return [dict(key=cell_key(R), R=float(R), T=float(R + DECOYS), decoys=float(DECOYS), build=build) for R in REAL_R]


def window_s(R, D):
    """Scored window: 3 hours, extended at small real volume until it holds MIN_REAL_PER_RUN real
    transactions on average (the run count stays the same)."""
    return max(P.MEASURE_S, P.MIN_REAL_PER_RUN * D / R)


def config_of(spec, D):
    R = spec["R"]
    return P.Config(real_rate=R / D, decoy_rate=float(spec.get("decoys", DECOYS)) / D, measure_s=window_s(R, D),
                    **ALL_BUILDS[spec.get("build", BASELINE)])


def traffic_seed(R, run_id):
    """Seed of one run's traffic. It depends on the real volume and the run only, so every build
    carries the same real traffic in the same cell and run, and every vantage reads the same run."""
    h = hashlib.sha256(f"sna|R={R:g}|run={run_id}|control=0".encode()).digest()
    return int.from_bytes(h[:8], "little") >> 1


# --------------------------------------------------------------------------- calibration
def calibrate(out=RESULTS, runs=10, force=False):
    """Mean end-to-end delay D (capture to the registry posting the merged record) over real
    transactions in the scored window, from seeded runs of the baseline build, so rates R / D and
    decoys / D give R and decoys transactions in flight under it. Every result directory is stamped
    with the simulator version; a directory written by another version is refused, so its runs are
    never resumed under this one."""
    p = Path(out) / "calibration.json"
    if p.exists() and not force:
        cal = json.loads(p.read_text())
        if cal.get("sim_version", 1) != P.SIM_VERSION:
            raise SystemExit(f"{out} holds results of simulator version {cal.get('sim_version', 1)}; this code is "
                             f"version {P.SIM_VERSION}. Use a new --out directory, or remove that one's results.")
        return cal
    cfg = P.Config(real_rate=0.2)
    d = []
    for k in range(runs):
        run = S.simulate(cfg, CAL_SEED0 + k)
        s = run.subs
        m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s) & ~s["decoy"]
        d.append(s["final"][m] - s["t0"][m])
    d = np.concatenate(d)
    fin = d[np.isfinite(d)]
    cal = dict(D=float(fin.mean()), D_median=float(np.median(fin)), D_p95=float(np.percentile(fin, 95)),
               n=int(fin.size), dropped=int((~np.isfinite(d)).sum()), runs=runs, build=BASELINE,
               sim_version=P.SIM_VERSION)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cal, indent=1))
    return cal


# --------------------------------------------------------------------------- models
def model_path(out, build):
    """The attacker's likelihood models under one build. An attacker knows the protocol, so each
    build is attacked with models built under it."""
    return Path(out) / "models" / f"{build}.pkl"


def ensure_models(out, build):
    p = model_path(out, build)
    if p.exists():
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    t = time.time()
    m = AT.build_models(P.Config(**ALL_BUILDS[build]), seed0=MODEL_SEED0)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(m, f)
    tmp.replace(p)
    print(f"models ({build}): {m.mc_runs} Monte Carlo runs, {time.time() - t:.0f} s", flush=True)


def rec_name(spec):
    return f"{spec['key']}__{spec.get('build', BASELINE)}"


# --------------------------------------------------------------------------- worker
_W = {}


def worker(out, spec, run_id, D):
    """One run of one cell: simulate once, score every vantage and its paired baseline."""
    mp = model_path(out, spec.get("build", BASELINE))
    if _W.get("model_key") != str(mp):
        with open(mp, "rb") as f:
            _W["models"] = pickle.load(f)
        _W["model_key"] = str(mp)
    cfg = config_of(spec, D)
    t = time.time()
    run = S.simulate(cfg, traffic_seed(spec["R"], run_id))
    t_sim = time.time() - t
    vantages = AT.VANTAGES + (("combined",) if cfg.overlap else ())
    recs = AT.compute(run, _W["models"], vantages, run_id)
    rec = dict(run=run_id, seconds=time.time() - t, sim_seconds=t_sim, vantages=recs,
               n_real=int((~run.subs["decoy"]).sum()), n_decoy=int(run.subs["decoy"].sum()),
               bundles=bundle_sizes(run))
    return [(rec_name(spec), rec)]


def bundle_sizes(run, window=P.BUNDLE_S):
    """Histogram (sizes 0..63) of hold releases per 30-second window at each active gatekeeper, over
    the scored window, on each gatekeeper's own departure grid."""
    s = run.subs
    lo_t, hi_t = run.cfg.warmup_s, run.cfg.warmup_s + run.cfg.measure_s
    hist = np.zeros(64, np.int64)
    for j, g in enumerate(run.gk_set):
        ph = run.bundle_phase[g]
        b = np.ceil((s["gk_release"][:, j] - ph) / window).astype(np.int64)
        k0, k1 = int(np.ceil((lo_t - ph) / window)), int(np.floor((hi_t - ph) / window))
        b = b[(b >= k0) & (b < k1)]
        cnt = np.bincount(b - k0, minlength=k1 - k0)
        hist += np.bincount(np.minimum(cnt, 63), minlength=64)
    return hist


def write_cells(out, specs, D):
    p = Path(out) / "cells.json"
    cells = json.loads(p.read_text()) if p.exists() else {}
    for s in specs:
        cells[s["key"]] = dict({k: v for k, v in s.items() if k != "build"}, window_s=window_s(s["R"], D), D=D)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cells, indent=1))


def run_cells(out, specs, runs=RUNS, workers="auto"):
    """Run every cell for run ids 0..runs-1, resuming what is already on disk. Cells advance
    together (run 0 of every cell first), so an interrupted sweep is balanced across cells."""
    out = Path(out)
    D = calibrate(out)["D"]
    write_cells(out, specs, D)
    tasks = []
    for spec in specs:
        done = RN.done_runs(out, rec_name(spec))
        todo = [k for k in range(runs) if k not in done]
        if todo:
            ensure_models(out, spec.get("build", BASELINE))
        tasks += [(str(out), spec, k, D) for k in todo]
    tasks.sort(key=lambda t: (t[2], t[1]["T"], t[1]["key"]))
    RN.execute(tasks, worker, out, workers, label="run")


def _scored(s, cfg):
    return (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s)


# --------------------------------------------------------------------------- latency
def latency(out, runs=20, builds=None):
    """Capture-to-finalization time of real transactions under each build, with the stages that
    make it up. Run ids from 3,000,000 up, never used by the main runs. Written to
    <out>/latency.json."""
    out = Path(out)
    D = calibrate(out)["D"]
    res = {}
    builds = tuple(builds or BUILDS)
    for build in builds:
        for R in REAL_R:
            spec = dict(R=float(R), decoys=float(DECOYS), build=build)
            cfg = config_of(spec, D)
            acc = {k: [] for k in ("total", "to_gatekeeper", "gk_hold", "gk_bundle_wait", "quorum",
                                  "quorum_to_confirmed", "registry_bundle_wait", "registry_posting_wait",
                                  "confirmed_to_final")}
            for k in range(runs):
                s = S.simulate(cfg, traffic_seed(R, LATENCY_SEED0 + k)).subs
                m = _scored(s, cfg) & ~s["decoy"] & s["ok_f"] & s["ok_i"]
                t0 = s["t0"][m]
                acc["total"].append(s["final"][m] - t0)
                acc["to_gatekeeper"].append(s["gk_arr"][m].mean(1) - t0)
                acc["gk_hold"].append((s["gk_release"][m] - s["gk_arr"][m]).mean(1))
                acc["gk_bundle_wait"].append((s["posts"][m] - s["gk_release"][m]).mean(1))
                acc["quorum"].append(s["quorum"][m] - t0)
                last = np.where(s["reg_f"][m] >= s["reg_i"][m], 0, 1)
                det = np.where(last == 0, s["det_f"][m], s["det_i"][m])
                reg = np.where(last == 0, s["reg_f"][m], s["reg_i"][m])
                acc["quorum_to_confirmed"].append(det - s["quorum"][m])
                acc["registry_bundle_wait"].append(reg - det)
                acc["registry_posting_wait"].append(s["posted"][m] - s["intake"][m])
                acc["confirmed_to_final"].append(s["final"][m] - det)
            row = {}
            for k, v in acc.items():
                v = np.concatenate(v)
                row[k] = dict(mean=float(v.mean()), median=float(np.median(v)), p95=float(np.percentile(v, 95)))
            tot = np.concatenate(acc["total"])
            row["n"] = int(tot.size)
            h, _ = np.histogram(tot, bins=np.arange(0, 2400 + 10, 10))
            row["hist10"] = h.tolist()
            row["largest_bin_share"] = float(h.max() / h.sum())
            row["occupied_bins"] = int((h > 0).sum())
            res[f"{build}.R{R}.D{DECOYS}"] = row
            t = row["total"]
            print(f"{build:22s} R={R:3d}: capture to finalization mean {t['mean']:.1f} s, "
                  f"median {t['median']:.1f} s, p95 {t['p95']:.1f} s (n = {row['n']})", flush=True)
    (out / "latency.json").write_text(json.dumps(dict(runs=runs, rates_from_D=D, cells=res), indent=1))
    return res


# --------------------------------------------------------------------------- F and I submitting together
def _pairs_one(args):
    build, R, d, run_id, D = args
    cfg = config_of(dict(R=float(R), decoys=float(d), build=build), D)
    run = S.simulate(cfg, traffic_seed(R, PAIRS_SEED0 + run_id))
    s = run.subs
    m = _scored(s, cfg) & ~s["decoy"] & s["ok_f"] & s["ok_i"]
    sub_gap = np.abs(s["reg_f"][m] - s["reg_i"][m])            # as the two submissions leave
    ready_gap = np.abs(s["ready_f"][m] - s["ready_i"][m])      # at the point of submission, before any registry wait
    waited = (s["det_f"][m] > s["hold_f"][m] + 1e-9) & (s["det_i"][m] > s["hold_i"][m] + 1e-9)
    either = (s["det_f"][m] > s["hold_f"][m] + 1e-9) | (s["det_i"][m] > s["hold_i"][m] + 1e-9)
    per_server = np.r_[s["det_f"][m] > s["hold_f"][m] + 1e-9, s["det_i"][m] > s["hold_i"][m] + 1e-9]
    W = cfg.reg_bundle_s
    if W > 0:
        bf = np.ceil((s["ready_f"][m] - run.reg_phase) / W)
        bi = np.ceil((s["ready_i"][m] - run.reg_phase) / W)
        same = bf == bi
    else:
        same = np.zeros(m.sum(), bool)
    return build, R, d, sub_gap, ready_gap, waited, same, either, per_server


def pair_gaps(out, builds=None, runs=20, workers="auto"):
    """How often a record's two registry submissions leave together. For every build and cell: the
    share of real records whose submissions leave within 5 s of each other; the same at the point
    of submission, before any registry wait; and, of the pairs separated by more than 5 s at that
    point, the share that the registry schedule puts back in one bundle. Run ids from 8,000,000
    up, never used by the main runs. Written to <out>/pair_gaps.json."""
    import multiprocessing as mp
    out = Path(out)
    D = calibrate(out)["D"]
    builds = tuple(builds or BUILDS)
    tasks = [(b, R, DECOYS, k, D) for b in builds for R in REAL_R for k in range(runs)]
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_pairs_one, tasks, chunksize=1)
    rows = {}
    for b in builds:
        for R in REAL_R:
            x = [r for r in res if r[0] == b and r[1] == R]
            sg, rg, wt, sm, ei, ps = (np.concatenate([r[i] for r in x]) for i in (3, 4, 5, 6, 7, 8))
            sep = rg > 5.0
            reg = P.Config(**ALL_BUILDS[b]).reg_bundle_s > 0
            row = dict(build=b, R=R, decoys=DECOYS, records=int(sg.size), runs=runs,
                       within5_at_departure=float((sg <= 5.0).mean()),
                       within5_at_submission=float((rg <= 5.0).mean()),
                       quorum_outlasted_both_holds=float(wt.mean()),
                       quorum_outlasted_either_hold=float(ei.mean()),
                       quorum_outlasted_hold_per_server=float(ps.mean()),
                       within5_at_submission_when_outlasted=float((rg[wt] <= 5.0).mean()) if wt.any() else float("nan"),
                       separated=int(sep.sum()),
                       separated_same_bundle=float(sm[sep].mean()) if sep.any() and reg else float("nan"),
                       median_gap_at_submission=float(np.median(rg)))
            rows[f"{b}.R{R}.D{DECOYS}"] = row
            sb = row["separated_same_bundle"]
            print(f"{b:22s} R={R:3d}: within 5 s at submission {100 * row['within5_at_submission']:5.1f}%, "
                  f"as they leave {100 * row['within5_at_departure']:5.1f}%; separated pairs put back in one bundle "
                  f"{'n/a' if np.isnan(sb) else f'{100 * sb:.1f}%'} (n = {row['records']})", flush=True)
    (out / "pair_gaps.json").write_text(json.dumps(dict(runs=runs, cells=rows), indent=1))
    return rows


# --------------------------------------------------------------------------- hold timing as simulated
def _timing_one(args):
    build, R, d, run_id, D = args
    cfg = config_of(dict(R=float(R), decoys=float(d), build=build), D)
    run = S.simulate(cfg, traffic_seed(R, TIMING_SEED0 + run_id))
    s, ev = run.subs, run.events
    a, b = cfg.warmup_s, cfg.warmup_s + cfg.measure_s
    m = _scored(s, cfg) & s["ok_f"] & s["ok_i"]
    ts, ta = ev["t_send"], ev["t_arr"]
    cr, ca, cb = s["ev_cred"][m], s["ev_ca"][m], s["ev_cb"][m]
    st = {
        "device, credential channel": ts[cr[:, 0]] - s["t0"][m],
        "device, content channels": np.r_[ts[ca[:, 0]], ts[cb[:, 0]]] - np.r_[s["t0"][m], s["t0"][m]],
        "relay hops": np.r_[ts[cr[:, 1]] - ta[cr[:, 0]], ts[cr[:, 2]] - ta[cr[:, 1]], ts[ca[:, 1]] - ta[ca[:, 0]],
                            ts[ca[:, 2]] - ta[ca[:, 1]], ts[cb[:, 1]] - ta[cb[:, 0]], ts[cb[:, 2]] - ta[cb[:, 1]]],
        "C before CV-1": s["cv1_s"][m] - s["arr_c"][m],
        "V before CV-2": ts[s["ev_cv2"][m]] - ta[s["ev_cv1"][m]],
        "C fan-out, per leg": (s["gk_send"][m] - s["cv2_a"][m][:, None]).ravel(),
        "gatekeeper hold": (s["gk_release"][m] - s["gk_arr"][m]).ravel(),
        "departure bundling wait": (s["posts"][m] - s["gk_release"][m]).ravel(),
        "F/I pre-match hold": np.r_[s["hold_f"][m] - s["arr_f"][m], s["hold_i"][m] - s["arr_i"][m]],
        "post-match lottery": np.r_[s["ready_f"][m] - s["det_f"][m], s["ready_i"][m] - s["det_i"][m]],
        "registry bundle wait": np.r_[s["reg_f"][m] - s["ready_f"][m], s["reg_i"][m] - s["ready_i"][m]],
        "registry posting wait": s["posted"][m] - s["intake"][m],
        "capture to finalization": s["final"][m] - s["t0"][m],
    }
    # postings per departure bundle at each gatekeeper (every transaction, real and decoy)
    counts = []
    for j, g in enumerate(run.gk_set):
        dep = s["posts"][:, j]
        W, ph = P.BUNDLE_S, run.bundle_phase[g]
        k = np.round((dep - ph) / W).astype(np.int64)      # posts sit just after a boundary (processing)
        k0, k1 = int(np.ceil((a - ph) / W)), int(np.floor((b - ph) / W))
        k = k[(k >= k0) & (k < k1)] - k0
        counts.append(np.bincount(k, minlength=k1 - k0))
    return build, st, np.concatenate(counts)


def timing_check(out, builds=(BASELINE, "no_inclusion_lottery"), R=20, runs=10, workers="auto"):
    """Every stage's simulated hold (mean, standard deviation, maximum), and postings per departure
    bundle. Run ids from 11,000,000 up, never used by the main runs. Written to
    <out>/timing_check.json."""
    import multiprocessing as mp
    out = Path(out)
    D = calibrate(out)["D"]
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_timing_one, [(b, R, DECOYS, k, D) for b in builds for k in range(runs)], chunksize=1)
    rows = {}
    for b in builds:
        x = [r for r in res if r[0] == b]
        stages = {}
        for name in x[0][1]:
            v = np.concatenate([r[1][name] for r in x])
            v = v[np.isfinite(v)]
            stages[name] = dict(mean=float(v.mean()), sd=float(v.std()), max=float(v.max()), n=int(v.size))
        c = np.concatenate([r[2] for r in x])
        rows[b] = dict(stages=stages, bundle=dict(mean=float(c.mean()), p_lt2=float((c < 2).mean()),
                                                   p_empty=float((c == 0).mean()), bundles=int(c.size)))
        print(f"== {b}")
        for name, v in stages.items():
            print(f"   {name:28s} mean {v['mean']:7.1f} s  sd {v['sd']:6.1f}  max {v['max']:7.1f}")
        print(f"   postings per departure bundle: mean {c.mean():.2f}, fewer than 2 {100 * (c < 2).mean():.1f}%, "
              f"empty {100 * (c == 0).mean():.1f}%", flush=True)
    (out / "timing_check.json").write_text(json.dumps(dict(R=R, decoys=DECOYS, runs=runs, builds=rows), indent=1))
    return rows


# --------------------------------------------------------------------------- permitted overlap: how often roles coincide
OVERLAP_SEED = 13_000_000


def overlap_counts(out, n_transactions=100_000, pools=(20, 50, 100)):
    """How often the permitted-overlap role draw puts one node in roles on two different paths of a
    transaction (count only, no attack). Three active gatekeepers in every pool. Written to
    <out>/overlap_counts.json."""
    rows = {}
    for N in pools:
        rng = np.random.default_rng([OVERLAP_SEED, N])
        gk = np.sort(rng.permutation(N)[:P.N_GATEKEEPERS])
        C, F, I, A, B, D, E, G, H = S._roles(rng, n_transactions, gk, n_nodes=N, rng_relays=rng)
        r = dict(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I)
        assert all(((r[p[0]] != r[p[1]]) & (r[p[1]] != r[p[2]]) & (r[p[0]] != r[p[2]])).all() for p in S.PATHS)
        assert ((A != D) & (A != G) & (D != G) & (C != F) & (C != I) & (F != I)).all()
        assert not np.isin(np.r_[C, F, I], gk).any()
        fd = {f"{a}={b}": float((r[a] == r[b]).mean()) for a, b in
              (("A", "F"), ("A", "I"), ("D", "C"), ("D", "I"), ("G", "C"), ("G", "F"))}
        fd_any = np.zeros(n_transactions, bool)
        for k in fd:
            a, b = k.split("=")
            fd_any |= r[a] == r[b]
        sr = np.zeros(n_transactions, bool)
        for a, b in S.CROSS_PAIRS:
            if a in "BEH" or b in "BEH":
                sr |= r[a] == r[b]
        gk_relay = np.zeros(n_transactions, bool)
        for a in "ABDEGH":
            gk_relay |= np.isin(r[a], gk)
        node = int(np.setdiff1d(np.arange(N), gk)[0])           # one fixed node outside the gatekeeper set
        paths_held = sum(((r[p[0]] == node) | (r[p[1]] == node) | (r[p[2]] == node)).astype(int) for p in S.PATHS)
        fd_node = np.zeros(n_transactions, bool)
        for k in fd:
            a, b = k.split("=")
            fd_node |= (r[a] == node) & (r[b] == node)
        rows[str(N)] = dict(nodes=N, transactions=n_transactions, gatekeepers=gk.tolist(),
                            any_cross_path=float(S.cross_path_overlap(r).mean()),
                            first_relay_is_other_destination=float(fd_any.mean()), first_relay_by_pair=fd,
                            second_relay_with_other_path_role=float(sr.mean()),
                            gatekeeper_relays=float(gk_relay.mean()),
                            fixed_node=node, fixed_node_two_paths=float((paths_held >= 2).mean()),
                            fixed_node_first_relay_and_destination=float(fd_node.mean()))
        x = rows[str(N)]
        print(f"{N:3d} nodes: any cross-path coincidence {100 * x['any_cross_path']:.2f}%, first relay = other path's "
              f"destination {100 * x['first_relay_is_other_destination']:.2f}%, second relay with another path's role "
              f"{100 * x['second_relay_with_other_path_role']:.2f}%, gatekeeper relays {100 * x['gatekeeper_relays']:.2f}%; "
              f"node {node}: two paths {100 * x['fixed_node_two_paths']:.2f}%, first relay and destination "
              f"{100 * x['fixed_node_first_relay_and_destination']:.2f}%", flush=True)
    Path(out).mkdir(parents=True, exist_ok=True)
    (Path(out) / "overlap_counts.json").write_text(json.dumps(dict(transactions=n_transactions, cells=rows), indent=1))
    return rows


# --------------------------------------------------------------------------- permitted overlap: shuffled-label control
SHUFFLE_SEED = 14_000_000


def _shuffle_one(args):
    out, build, R, run_id, D = args
    with open(model_path(out, build), "rb") as f:
        m = pickle.load(f)
    cfg = config_of(dict(R=float(R), decoys=float(DECOYS), build=build), D)
    run = S.simulate(cfg, traffic_seed(R, run_id))
    vantages = AT.VANTAGES + (("combined",) if cfg.overlap else ())
    recs = AT.compute(run, m, vantages, run_id, label_rng=np.random.default_rng([SHUFFLE_SEED, int(R), run_id]))
    return R, run_id, {v: (int(x["dev_v_correct"].sum()), int(x["dev_v_correct"].size), float(x["dev_v_rand"].sum()),
                           int(x["dev_b_correct"].sum()), float(x["dev_b_rand"].sum())) for v, x in recs.items()}


def shuffle_control(out, build="permitted_overlap", runs=20, workers="auto"):
    """Negative control: within each run the device labels of every candidate (and of every validator
    reply) are permuted at random, so no candidate carries its own device's label; every vantage is then
    scored as usual. Accuracy should fall to the feasible chance rate. Scored run ids 0..runs-1. Written to
    <out>/shuffle_control.json."""
    import multiprocessing as mp
    from . import analyze as AN
    out = Path(out)
    D = calibrate(out)["D"]
    ensure_models(out, build)
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_shuffle_one, [(str(out), build, R, k, D) for R in REAL_R for k in range(runs)], chunksize=1)
    rng = np.random.default_rng(SHUFFLE_SEED)
    rows = {}
    for R in REAL_R:
        x = [r[2] for r in res if r[0] == R]
        for v in x[0]:
            a = np.array([y[v] for y in x], float)              # per run: correct, n, chance sum, observer correct, observer chance
            acc, lo, hi = AN.cluster_boot(a[:, 0], a[:, 1], rng)
            row = dict(R=R, vantage=v, runs=runs, decisions=int(a[:, 1].sum()), accuracy=acc, accuracy_lo=lo,
                       accuracy_hi=hi, feasible_chance=a[:, 2].sum() / a[:, 1].sum(),
                       observer_accuracy=a[:, 3].sum() / a[:, 1].sum(), observer_feasible_chance=a[:, 4].sum() / a[:, 1].sum())
            row["passes"] = bool(lo <= row["feasible_chance"] <= hi)
            rows[f"{v}.R{R}"] = row
            print(f"R={R:3d} {v:18s} shuffled: {100 * acc:5.2f}% [{100 * lo:5.2f}, {100 * hi:5.2f}], feasible chance "
                  f"{100 * row['feasible_chance']:5.2f}%, observer {100 * row['observer_accuracy']:5.2f}% "
                  f"(chance {100 * row['observer_feasible_chance']:5.2f}%), n = {row['decisions']}: "
                  f"{'pass' if row['passes'] else 'FAIL'}", flush=True)
    (out / "shuffle_control.json").write_text(json.dumps(dict(build=build, runs=runs, cells=rows), indent=1))
    return rows


# --------------------------------------------------------------------------- first relays by path
PATH_VARIANTS = {"credential path only": "first_relay_signal_cred", "both content paths": "first_relay_signal_content",
                 "F content path only": "first_relay_signal_one_content"}


def _paths_one(args):
    out, b, run_id, D = args
    with open(model_path(out, b), "rb") as f:
        m = pickle.load(f)
    run = S.simulate(config_of(dict(R=1.0, decoys=float(DECOYS), build=b), D), traffic_seed(1.0, run_id))
    s = run.subs
    rec = AT.records(run)
    keep = AT.scored_mask(run, rec["sub"])
    rec = {k: x[keep] for k, x in rec.items()}
    cand = AT.candidates(run)
    g = m.pdf["g"]
    lo, hi = AT._band(rec["u"], g)
    base = AT.score_blocks(lo, hi, cand, lambda r, k0, k1: g(rec["u"][r][:, None] - cand["t"][None, k0:k1]),
                           dict(sub=rec["sub"], dev=rec["dev"]))
    ri, grp, res, _ = AT.score_vantage("first_hop_cred", run, rec, cand, m, base, run_id)
    v, bb, sub = res["dev"]["correct"].astype(float), base["dev"]["correct"][ri].astype(float), rec["sub"][ri]
    return b, {p: (v[grp == s[p][sub]].sum(), bb[grp == s[p][sub]].sum(), int((grp == s[p][sub]).sum())) for p in "ADG"}


def first_relay_paths(out, runs=300, run0=2000, workers="auto"):
    """Each first relay's lead over the observer on the records whose transaction it relayed as A, D or G, at
    R = 1, under three controls that put the timing signal on the credential path, on both content paths, or
    on the F content path only. Run ids from run0 up. Written to <out>/first_relay_paths.json."""
    import multiprocessing as mp
    from . import analyze as AN
    out = Path(out)
    D = calibrate(out)["D"]
    for b in PATH_VARIANTS.values():
        ensure_models(out, b)
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_paths_one, [(str(out), b, k, D) for b in PATH_VARIANTS.values() for k in range(run0, run0 + runs)],
                       chunksize=2)
    rng = np.random.default_rng(99)
    rows = {}
    for label, b in PATH_VARIANTS.items():
        for p in "ADG":
            a = np.array([r[1][p] for r in res if r[0] == b], float)
            lead, lo, hi = AN.cluster_boot(a[:, 0] - a[:, 1], a[:, 2], rng)
            rows[f"{label}.{p}"] = dict(lead=lead, lo=lo, hi=hi, accuracy=a[:, 0].sum() / a[:, 2].sum(),
                                        observer=a[:, 1].sum() / a[:, 2].sum(), n=int(a[:, 2].sum()), runs=len(a))
            print(f"{label:22s} {p}: lead {100 * lead:+.2f} [{100 * lo:+.2f}, {100 * hi:+.2f}], n {int(a[:, 2].sum())}", flush=True)
    (out / "first_relay_paths.json").write_text(json.dumps(dict(runs=runs, run0=run0, cells=rows), indent=1))
    return rows

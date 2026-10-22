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
BUILDS = {BASELINE: dict(overlap=True)}
ALL_BUILDS = dict(BUILDS)
LABEL = {BASELINE: EXPERIMENT}

CAL_SEED0, MODEL_SEED0 = 2_000_000_000, 1_000_000_000


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








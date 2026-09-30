"""The experiment grid, per-cell configuration, seeds, the end-to-end delay calibration, model
caching, and the per-run worker.

A cell is one (real volume R, total volume T) pair, both in transactions in flight. R = T is a
no-decoy cell; T > R is a decoy cell carrying T - R decoy transactions in flight on top of the
same real traffic. Rates follow from the measured end-to-end delay D (capture to registry
finalisation): real rate R / D, decoy credential rate (T - R) / D, two decoy content packets per
decoy credential transaction.
"""
from __future__ import annotations

import hashlib
import json
import math
import pickle
import time
from pathlib import Path

import numpy as np

from . import attacks as AT
from . import params as P
from . import runner as RN
from . import sim as S
from .pools import Pools

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"

WIDE_L = (4, 8, 24, 40, 50, 100, 200, 500)       # no-decoy sweep, and the decoy targets
LOW_R = (1, 2, 3, 4, 8, 24, 40)                  # low range, and the real floors of the decoy grid
CONTROL_R = 40                                   # sensitivity control volume (every hold off)
CAL_SEED0, MODEL_SEED0 = 2_000_000_000, 1_000_000_000


def cell_key(R, T=None, control=False):
    T = R if T is None else T
    k = f"R{R:g}" if T == R else f"R{R:g}_T{T:g}"
    return k + ("_control" if control else "")


def grid(which="all"):
    """Cell specs. which: all | nodecoy | decoy | control."""
    specs = []
    if which in ("all", "nodecoy"):
        for R in sorted(set(WIDE_L) | set(LOW_R)):
            specs.append(dict(key=cell_key(R), R=float(R), T=float(R), control=False))
    if which in ("all", "decoy"):
        for R in LOW_R:
            for T in WIDE_L:
                if T > R:
                    specs.append(dict(key=cell_key(R, T), R=float(R), T=float(T), control=False))
    if which in ("all", "control"):
        specs.append(dict(key=cell_key(CONTROL_R, control=True), R=float(CONTROL_R), T=float(CONTROL_R),
                          control=True))
    return specs


def window_s(R, D):
    """Scored window: 3 hours, extended at small real volume until it holds MIN_REAL_PER_RUN real
    transactions on average (the run count stays the same)."""
    return max(P.MEASURE_S, P.MIN_REAL_PER_RUN * D / R)


def config_of(spec, D):
    R, T = spec["R"], spec["T"]
    return P.Config(real_rate=R / D, decoy_rate=max(0.0, T - R) / D, measure_s=window_s(R, D),
                    lottery_enabled=not spec["control"], background_enabled=False, nonblending_enabled=False)


def traffic_seed(R, run_id, control=False):
    """Seed of one run's traffic. It depends on the real volume and the run only, so every decoy
    cell at the same R carries the same real traffic as the no-decoy cell (and every vantage reads
    the same run)."""
    h = hashlib.sha256(f"sna|R={R:g}|run={run_id}|control={int(control)}".encode()).digest()
    return int.from_bytes(h[:8], "little") >> 1


# --------------------------------------------------------------------------- calibration
def calibrate(out=RESULTS, runs=10, force=False):
    """Mean end-to-end delay D (capture to registry finalisation, the later of the two
    submissions) over real transactions in the scored window, from seeded runs."""
    p = Path(out) / "calibration.json"
    if p.exists() and not force:
        return json.loads(p.read_text())
    pools = Pools()
    cfg = P.Config(real_rate=0.2, background_enabled=False, nonblending_enabled=False)
    d = []
    for k in range(runs):
        run = S.simulate(cfg, CAL_SEED0 + k, pools)
        s = run.subs
        m = (s["t0"] >= P.WARMUP_S) & (s["t0"] < P.WARMUP_S + cfg.measure_s) & ~s["decoy"]
        d.append(s["final"][m] - s["t0"][m])
    d = np.concatenate(d)
    fin = d[np.isfinite(d)]
    cal = dict(D=float(fin.mean()), D_median=float(np.median(fin)), D_p95=float(np.percentile(fin, 95)),
               n=int(fin.size), dropped=int((~np.isfinite(d)).sum()), runs=runs)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cal, indent=1))
    return cal


# --------------------------------------------------------------------------- models
TARGET = "link"             # record-to-device linking; names every model and record file


def model_path(out, control):
    return Path(out) / "models" / (f"{TARGET}_control.pkl" if control else f"{TARGET}_main.pkl")


def rec_name(spec):
    return f"{spec['key']}__{TARGET}"


def ensure_models(out, control, pools=None):
    p = model_path(out, control)
    if p.exists():
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    t = time.time()
    m = AT.build_models(P.Config(lottery_enabled=not control), pools or Pools(), seed0=MODEL_SEED0)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(m, f)
    tmp.replace(p)
    print(f"models ({'control' if control else 'main'}): {m.mc_runs} Monte Carlo runs, {time.time() - t:.0f} s",
          flush=True)


# --------------------------------------------------------------------------- worker
_W = {}


def worker(out, spec, run_id, D):
    """One run of one cell: simulate once, score every vantage and its paired baseline."""
    if "pools" not in _W:
        _W["pools"] = Pools()
    mp = model_path(out, spec["control"])
    if _W.get("model_key") != str(mp):
        with open(mp, "rb") as f:
            _W["models"] = pickle.load(f)
        _W["model_key"] = str(mp)
    cfg = config_of(spec, D)
    t = time.time()
    run = S.simulate(cfg, traffic_seed(spec["R"], run_id, spec["control"]), _W["pools"])
    t_sim = time.time() - t
    recs = AT.compute(run, _W["pools"], _W["models"])
    rec = dict(run=run_id, seconds=time.time() - t, sim_seconds=t_sim, vantages=recs,
               n_real=int((~run.subs["decoy"]).sum()), n_decoy=int(run.subs["decoy"].sum()))
    return [(rec_name(spec), rec)]


def write_cells(out, specs, D):
    p = Path(out) / "cells.json"
    cells = json.loads(p.read_text()) if p.exists() else {}
    for s in specs:
        cells[s["key"]] = dict(s, window_s=window_s(s["R"], D), D=D)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cells, indent=1))


def run_cells(out, specs, runs, workers="auto"):
    """Run every cell for run ids 0..runs-1, resuming what is already on disk. Cells advance
    together (run 0 of every cell first), so an interrupted sweep is balanced across cells."""
    out = Path(out)
    D = calibrate(out)["D"]
    write_cells(out, specs, D)
    pools = Pools()
    tasks = []
    for spec in specs:
        done = RN.done_runs(out, rec_name(spec))
        todo = [k for k in range(runs) if k not in done]
        if todo:
            ensure_models(out, spec["control"], pools)
        tasks += [(str(out), spec, k, D) for k in todo]
    tasks.sort(key=lambda t: (t[2], t[1]["T"], t[1]["key"]))
    RN.execute(tasks, worker, out, workers, label="run")


# --------------------------------------------------------------------------- estimate
def probe_costs(out, specs, probe_runs=1, workers="auto"):
    """Measure seconds per run and successes per run for each cell from probe runs (run ids from
    1,000,000 up, never used by a sweep). Written to <out>/costs.json."""
    out = Path(out)
    D = calibrate(out)["D"]
    ensure_models(out, False)
    if any(s["control"] for s in specs):
        ensure_models(out, True)
    probe = out / "probe"
    tasks = []
    for spec in specs:
        done = RN.done_runs(probe, rec_name(spec))
        tasks += [(str(out), spec, 1_000_000 + k, D) for k in range(probe_runs) if 1_000_000 + k not in done]
    RN.execute(tasks, _probe_worker, probe, workers, label="probe")
    costs = {}
    for spec in specs:
        recs = RN.load(probe, rec_name(spec))
        if not recs:
            continue
        succ = {v: float(np.mean([r["vantages"][v]["dev_v_correct"].sum() for r in recs])) for v in AT.VANTAGES}
        fail = {v: float(np.mean([(1 - r["vantages"][v]["dev_v_correct"]).sum() for r in recs])) for v in AT.VANTAGES}
        bsucc = {v: float(np.mean([r["vantages"][v]["dev_b_correct"].sum() for r in recs])) for v in AT.VANTAGES}
        costs[spec["key"]] = dict(R=spec["R"], T=spec["T"], control=spec["control"],
                                  sec_per_run=float(np.mean([r["seconds"] for r in recs])),
                                  sim_sec_per_run=float(np.mean([r["sim_seconds"] for r in recs])),
                                  successes_per_run=succ, failures_per_run=fail, baseline_successes_per_run=bsucc,
                                  n_real=float(np.mean([r["n_real"] for r in recs])),
                                  n_decoy=float(np.mean([r["n_decoy"] for r in recs])), probe_runs=len(recs))
    (out / "costs.json").write_text(json.dumps(costs, indent=1))
    return costs


def _probe_worker(out, spec, run_id, D):
    return worker(out, spec, run_id, D)


def runs_needed(successes_per_run, min_successes):
    if successes_per_run <= 0:
        return math.inf
    return int(math.ceil(min_successes / successes_per_run))

"""The run / estimate / quick commands: cells, model caching, and the per-run worker.

A cell is one (round, L, variant, validator share, pool size, window) combination. Its records go
to <out>/raw/<cell>__<record>.pkl.gz; <cell>__done lists the runs whose records are all written,
which is what resume reads. Attacker models are built once per cell in the parent process and
cached in <out>/models/, so workers never race to build them.
"""
from __future__ import annotations

import json
import math
import pickle
import time
from pathlib import Path

import numpy as np

from . import ROOT
from . import runner as RN

DEFAULT_COSTS = Path(__file__).with_name("costs_default.json")


def cell_key(rnd, L, variant="", share=0.0, nodes=20, window=180.0):
    k = f"r{rnd}_L{L:g}"
    if variant:
        k += f"_{variant}"
    if share:
        k += f"_s{share:g}"
    if nodes != 20:
        k += f"_n{nodes}"
    if window != 180.0:
        k += f"_w{window:g}"
    return k


def cell_spec(rnd, L, scenarios, variant="", share=0.0, nodes=20, window=180.0, base=1):
    return dict(key=cell_key(rnd, L, variant, share, nodes, window), round=int(rnd), L=float(L),
                variant=variant, share=float(share), nodes=int(nodes), window=float(window),
                scenarios=list(scenarios), base=int(base))


def config_of(spec):
    from . import roles as R
    kw = {}
    if spec["share"]:
        kw.update(validator0_share=spec["share"], n_validators=1 if spec["share"] >= 1.0 else 4)
    if spec["nodes"] != 20:
        kw["n_nodes"] = spec["nodes"]
    return R.round_config(spec["round"], spec["L"], spec["variant"], measure_min=spec["window"], **kw)


def model_path(out, spec):
    k = cell_key(spec["round"], spec["L"], spec["variant"], spec["share"], spec["nodes"])
    return Path(out) / "models" / f"{k}.pkl"


def ensure_models(out, spec, pools):
    """Build (or load) the attacker's likelihood models for a cell."""
    from birthmark_l3 import attack as A
    from . import roles as R
    p = model_path(out, spec)
    if p.exists():
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    cfg = config_of(spec)
    t = time.time()
    lik = A.build_likelihoods(cfg)
    models = R.build_models(cfg, pools, lik)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump((lik, models), f)
    tmp.replace(p)
    print(f"models for {spec['key']}: {models.mc_runs} Monte Carlo runs, {time.time() - t:.0f} s", flush=True)


_W = {}


def worker(out, spec, run_id):
    """One run of one cell: simulate once, compute every requested scenario, return the records."""
    from birthmark_l3 import fastsim as FS
    from birthmark_l3.wire_pools import Pools
    from . import scenarios as SC
    if "pools" not in _W:
        _W["pools"] = Pools()
    mp = model_path(out, spec)
    if _W.get("model_key") != str(mp):
        with open(mp, "rb") as f:
            _W["models"] = pickle.load(f)
        _W["model_key"] = str(mp)
    lik, models = _W["models"]
    cfg = config_of(spec)
    t = time.time()
    run = FS.simulate(cfg, SC.traffic_seed(spec["base"], spec["L"], run_id, spec["nodes"]), _W["pools"])
    t_sim = time.time() - t
    recs = SC.compute(run, _W["pools"], lik, models, spec["scenarios"], spec["round"], spec["L"], spec["base"], run_id)
    secs = time.time() - t
    out_pairs = []
    for name, r in recs.items():
        r["run"] = run_id
        out_pairs.append((f"{spec['key']}__{name}", r))
    out_pairs.append((f"{spec['key']}__done", dict(run=run_id, seconds=secs, sim_seconds=t_sim,
                                                  records=sorted(recs), n_subs=int(run.subs["t0"].shape[0]))))
    return out_pairs


def write_cells(out, specs):
    p = Path(out) / "cells.json"
    cells = json.loads(p.read_text()) if p.exists() else {}
    for s in specs:
        cells[s["key"]] = s
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cells, indent=1))


def run_cells(out, specs, runs, workers="auto"):
    """Run every cell for run ids 0..runs-1, resuming what is already on disk."""
    from birthmark_l3.wire_pools import Pools
    out = Path(out)
    write_cells(out, specs)
    pools = Pools()
    tasks = []
    for spec in specs:
        done = RN.done_runs(out, f"{spec['key']}__done")
        todo = [k for k in range(runs) if k not in done]
        if todo:
            ensure_models(out, spec, pools)
        tasks += [(str(out), spec, k) for k in todo]
    tasks.sort(key=lambda t: (t[2], t[1]["L"], t[1]["key"]))      # every cell advances together
    RN.execute(tasks, worker, out, workers, label="run")
    record_costs(out, specs)


def record_costs(out, specs):
    p = Path(out) / "costs.json"
    costs = json.loads(p.read_text()) if p.exists() else {}
    for spec in specs:
        recs = RN.load(out, f"{spec['key']}__done")
        if recs:
            costs[spec["key"]] = dict(L=spec["L"], scenarios=spec["scenarios"], round=spec["round"],
                                      nodes=spec["nodes"], window=spec["window"],
                                      sec_per_run=float(np.median([r["seconds"] for r in recs])), runs=len(recs))
    p.write_text(json.dumps(costs, indent=1))


# --------------------------------------------------------------------------- estimate
def estimate(specs, runs, workers, costs_file=None):
    """Expected wall-clock time for a plan, from measured per-run costs. Each cell uses the measured
    cost of the most similar measured cell, scaled by L with the power law fitted across measured
    L values (costs grow with the answers each row is scored against)."""
    src = [Path(costs_file)] if costs_file else []
    src.append(DEFAULT_COSTS)
    costs = {}
    for p in src[::-1]:
        if p.exists():
            costs.update(json.loads(p.read_text()))
    if not costs:
        raise SystemExit("no measured costs: run `python -m harness quick` first")
    nw = RN.resolve_workers(workers)
    total = 0.0
    lines = []
    for spec in specs:
        cand = [c for c in costs.values() if set(spec["scenarios"]) <= set(c["scenarios"])] or list(costs.values())
        Ls = np.array([c["L"] for c in cand])
        sec = np.array([c["sec_per_run"] * 180.0 / max(c.get("window", 180.0), 1) for c in cand])
        near = int(np.argmin(np.abs(np.log(Ls) - math.log(spec["L"]))))
        if len(set(Ls)) >= 2:
            alpha = float(np.polyfit(np.log(Ls), np.log(sec), 1)[0])
        else:
            alpha = 1.3
        per = sec[near] * (spec["L"] / Ls[near]) ** alpha * spec["window"] / 180.0
        t = per * runs
        total += t
        lines.append(f"  {spec['key']:<28} {per:9.1f} s/run x {runs} runs = {t / 3600:7.2f} core-hours")
    print("\n".join(lines))
    print(f"total {total / 3600:.2f} core-hours; on {nw} workers about {total / 3600 / nw:.2f} hours wall-clock")
    return total / nw

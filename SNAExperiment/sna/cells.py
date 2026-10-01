"""The experiment grid, per-cell configuration, seeds, the end-to-end delay calibration, model
caching, and the per-run worker.

A cell is a real volume R (real transactions in flight), a decoy target (decoy transactions in
flight, a steady stream independent of real traffic), and gatekeeper departure bundling on or
off. Rates follow from the measured end-to-end delay D (capture to registry finalisation): real
rate R / D, decoy rate decoys / D. A decoy is a genuine transaction from one of the decoy
infrastructure's registered identities, each capturing at a device's rate.
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

REAL_R = (1, 15, 50)                             # real volumes
DECOY_LEVELS = (20, 40, 60)                      # decoy targets, transactions in flight
CONTROL_R = 40                                   # sensitivity control volume (every hold off)
CAL_SEED0, MODEL_SEED0 = 2_000_000_000, 1_000_000_000


# builds: the protocol as attacked. Each later build adds one mechanism to the one before it.
BUILDS = {
    "push": dict(target="link_push"),
    "twopoint": dict(target="link_twopoint", gk_twopoint=True),
    "regbundle": dict(target="link_regbundle", gk_twopoint=True, reg_bundle_s=P.REG_BUNDLE_S),
}
DEFAULT_BUILD = "regbundle"
PRIOR_BUILDS = {"twopoint": ("push",), "regbundle": ("twopoint", "push")}


def build_kw(build):
    return {k: v for k, v in BUILDS[build].items() if k != "target"}


def target(build):
    return BUILDS[build]["target"]



def cell_key(R, decoys=0, bundle=False, control=False):
    return f"R{R:g}" + (f"_D{decoys:g}" if decoys else "") + ("_B" if bundle else "") + ("_control" if control else "")


def grid(which="all", build=DEFAULT_BUILD):
    """Cell specs. which: all | bundle | nobundle | control."""
    specs = [dict(s, build=build) for s in _grid(which)]
    return specs


def _grid(which):
    specs = []
    for bundle in (False, True):
        if which not in ("all", "bundle" if bundle else "nobundle"):
            continue
        for R in REAL_R:
            for d in DECOY_LEVELS:
                specs.append(dict(key=cell_key(R, d, bundle), R=float(R), T=float(R + d), decoys=float(d),
                                  bundle=bundle, control=False))
    if which in ("all", "control"):
        specs.append(dict(key=cell_key(CONTROL_R, control=True), R=float(CONTROL_R), T=float(CONTROL_R),
                          decoys=0.0, bundle=False, control=True))
    return specs


def window_s(R, D):
    """Scored window: 3 hours, extended at small real volume until it holds MIN_REAL_PER_RUN real
    transactions on average (the run count stays the same)."""
    return max(P.MEASURE_S, P.MIN_REAL_PER_RUN * D / R)


def config_of(spec, D):
    R = spec["R"]
    return P.Config(real_rate=R / D, decoy_rate=float(spec.get("decoys", 0.0)) / D,
                    bundle_s=P.BUNDLE_S if spec.get("bundle") else 0.0, measure_s=window_s(R, D),
                    lottery_enabled=not spec["control"], background_enabled=False, nonblending_enabled=False,
                    **build_kw(spec.get("build", DEFAULT_BUILD)))


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
TARGET = target(DEFAULT_BUILD)
PRIOR_TARGET = "link_bundling"  # the push build's cells with content servers checking the boards on their own clock


def model_path(out, control, bundle=False, build=DEFAULT_BUILD):
    """The attacker's likelihood models for a configuration: every hold off (control), or the
    protocol with gatekeeper departure bundling on or off, under one build. An attacker knows the
    protocol, so each configuration is attacked with models built under it."""
    name = "control" if control else ("main_bundle" if bundle else "main")
    return Path(out) / "models" / f"{target(build)}_{name}.pkl"


ALL_RECORDS = ("baseline", "first_hop_cred", "first_hop_content", "cred_processor")


def rec_name(spec):
    return f"{spec['key']}__{target(spec.get('build', DEFAULT_BUILD))}" + ("__allrecords" if spec.get("allrecords") else "")


def allrecords_specs(specs):
    """The same cells, re-scored for the vantages that are scored on every record."""
    return [dict(s, allrecords=True, vantages=ALL_RECORDS) for s in specs]


def ensure_models(out, control, pools=None, bundle=False, build=DEFAULT_BUILD):
    p = model_path(out, control, bundle, build)
    if p.exists():
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    t = time.time()
    m = AT.build_models(P.Config(lottery_enabled=not control, bundle_s=P.BUNDLE_S if bundle else 0.0,
                                 **build_kw(build)),
                        pools or Pools(), seed0=MODEL_SEED0)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(m, f)
    tmp.replace(p)
    print(f"models ({p.stem}): {m.mc_runs} Monte Carlo runs, {time.time() - t:.0f} s",
          flush=True)


# --------------------------------------------------------------------------- worker
_W = {}


def worker(out, spec, run_id, D):
    """One run of one cell: simulate once, score every vantage and its paired baseline."""
    if "pools" not in _W:
        _W["pools"] = Pools()
    mp = model_path(out, spec["control"], spec.get("bundle", False), spec.get("build", DEFAULT_BUILD))
    if _W.get("model_key") != str(mp):
        with open(mp, "rb") as f:
            _W["models"] = pickle.load(f)
        _W["model_key"] = str(mp)
    cfg = config_of(spec, D)
    t = time.time()
    run = S.simulate(cfg, traffic_seed(spec["R"], run_id, spec["control"]), _W["pools"])
    t_sim = time.time() - t
    recs = AT.compute(run, _W["pools"], _W["models"], spec.get("vantages", AT.VANTAGES), run_id)
    rec = dict(run=run_id, seconds=time.time() - t, sim_seconds=t_sim, vantages=recs,
               n_real=int((~run.subs["decoy"]).sum()), n_decoy=int(run.subs["decoy"].sum()),
               bundles=bundle_sizes(run))
    return [(rec_name(spec), rec)]


def bundle_sizes(run, window=P.BUNDLE_S):
    """Histogram (sizes 0..63) of postings per departure bundle at each active gatekeeper, over the
    scored window, on each gatekeeper's own grid. Computed whether or not bundling is on, so the
    off cells report how large the bundles would have been."""
    s = run.subs
    lo_t, hi_t = P.WARMUP_S, P.WARMUP_S + run.cfg.measure_s
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
        cells[s["key"]] = dict(s, window_s=window_s(s["R"], D), D=D)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cells, indent=1))


def run_cells(out, specs, runs, workers="auto"):
    """Run every cell for run ids 0..runs-1, resuming what is already on disk. Cells advance
    together (run 0 of every cell first), so an interrupted sweep is balanced across cells."""
    out = Path(out)
    D = calibrate(out)["D"]
    write_cells(out, [s for s in specs if not s.get("allrecords")], D)
    pools = Pools()
    tasks = []
    for spec in specs:
        done = RN.done_runs(out, rec_name(spec))
        todo = [k for k in range(runs) if k not in done]
        if todo:
            ensure_models(out, spec["control"], pools, spec.get("bundle", False), spec.get("build", DEFAULT_BUILD))
        tasks += [(str(out), spec, k, D) for k in todo]
    tasks.sort(key=lambda t: (t[2], t[1]["T"], t[1]["key"]))
    RN.execute(tasks, worker, out, workers, label="run")


# --------------------------------------------------------------------------- estimate
def probe_costs(out, specs, probe_runs=1, workers="auto"):
    """Measure seconds per run and successes per run for each cell from probe runs (run ids from
    1,000,000 up, never used by a sweep). Written to <out>/costs.json."""
    out = Path(out)
    D = calibrate(out)["D"]
    for b, bl in sorted({(bool(s.get("bundle")), s.get("build", DEFAULT_BUILD)) for s in specs if not s["control"]}):
        ensure_models(out, False, bundle=b, build=bl)
    for bl in sorted({s.get("build", DEFAULT_BUILD) for s in specs if s["control"]}):
        ensure_models(out, True, build=bl)
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


# --------------------------------------------------------------------------- latency
LATENCY_SEED0 = 3_000_000


def latency(out, runs=20, cells=((1, 40), (15, 40), (50, 40))):
    """Capture-to-finalisation time of real transactions under each build, with the stages that
    make it up. Run ids from 3,000,000 up, never used by a sweep. Written to <out>/latency.json."""
    out = Path(out)
    D = calibrate(out)["D"]
    pools = Pools()
    res = {}
    for build in BUILDS:
        for R, d in cells:
            spec = dict(R=float(R), decoys=float(d), bundle=True, control=False, build=build)
            cfg = config_of(spec, D)
            acc = {k: [] for k in ("total", "to_gatekeeper", "gk_hold", "gk_bundle_wait", "quorum",
                                  "quorum_to_confirmed", "registry_bundle_wait", "confirmed_to_final")}
            for k in range(runs):
                s = S.simulate(cfg, traffic_seed(R, LATENCY_SEED0 + k), pools).subs
                m = (s["t0"] >= P.WARMUP_S) & (s["t0"] < P.WARMUP_S + cfg.measure_s) & ~s["decoy"] \
                    & s["ok_f"] & s["ok_i"]
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
                acc["confirmed_to_final"].append(s["final"][m] - det)
            row = {}
            for k, v in acc.items():
                v = np.concatenate(v)
                row[k] = dict(mean=float(v.mean()), median=float(np.median(v)), p95=float(np.percentile(v, 95)))
            tot = np.concatenate(acc["total"])
            row["n"] = int(tot.size)
            # shape of the total: 10-second histogram, to show whether it collapses onto a few values
            h, _ = np.histogram(tot, bins=np.arange(0, 2400 + 10, 10))
            row["hist10"] = h.tolist()
            row["largest_bin_share"] = float(h.max() / h.sum())
            row["occupied_bins"] = int((h > 0).sum())
            res[f"{build}.R{R}.D{d}"] = row
            t = row["total"]
            print(f"{build:9s} R={R:2d} decoys={d}: capture to finalisation mean {t['mean']:.1f} s, "
                  f"median {t['median']:.1f} s, p95 {t['p95']:.1f} s (n = {row['n']})", flush=True)
    (out / "latency.json").write_text(json.dumps(dict(runs=runs, rates_from_D=D, cells=res), indent=1))
    _latency_figure(out, res, cells)
    return res


def _latency_figure(out, res, cells):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    R, d = cells[0]
    f, ax = plt.subplots(figsize=(7, 3.6), dpi=300, facecolor="#fcfcfb")
    ax.set_facecolor("#fcfcfb")
    cmap = plt.get_cmap("viridis")
    for j, build in enumerate(BUILDS):
        h = np.array(res[f"{build}.R{R}.D{d}"]["hist10"], float)
        x = np.arange(h.size) * 10 + 5
        ax.plot(x, 100 * h / h.sum(), color=cmap(j / max(len(BUILDS) - 1, 1) * 0.85), linewidth=1.6, label=build)
    ax.set_xlim(0, 1600)
    ax.set_xlabel("capture to registry finalisation (s)", fontsize=8)
    ax.set_ylabel("share of real transactions per 10 s (%)", fontsize=8)
    ax.set_title(f"R = {R}, {d} decoys in flight", fontsize=9)
    ax.legend(fontsize=7, frameon=False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    f.tight_layout()
    (out / "figures").mkdir(parents=True, exist_ok=True)
    f.savefig(out / "figures" / "latency_by_build.png", facecolor="#fcfcfb")
    plt.close(f)

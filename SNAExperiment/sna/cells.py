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
DECOY_LEVELS = (20, 30, 40, 60, 100, 150)        # decoy targets, transactions in flight
DECOY_CORE = (20, 40, 60)                        # the levels of sections 6b to 6e
DECOY_EXTRA = (30, 100, 150)                     # the levels added in section 6f
CONTROL_R = 40                                   # sensitivity control volume (every hold off)
CAL_SEED0, MODEL_SEED0 = 2_000_000_000, 1_000_000_000


REG_WINDOWS = (60, 120, 240, 480)                # registry bundling windows swept (section 6e)

# builds: the protocol as attacked. Each later build adds one mechanism to the one before it.
BUILDS = {
    "push": dict(target="link_push"),
    "twopoint": dict(target="link_twopoint", gk_twopoint=True),
    "regbundle": dict(target="link_regbundle", gk_twopoint=True, reg_bundle_s=P.REG_BUNDLE_S),
    # registry-level bundling on the push build, without the two-point hold, at four windows
    **{f"reg{w}": dict(target=f"link_reg{w}", reg_bundle_s=float(w)) for w in REG_WINDOWS},
}
HOLD_SCALES = (1.5, 2.0, 3.0)                    # device and relay hold stretch factors (section 6g)
BUILDS.update({f"hold{int(k * 100)}": dict(target=f"link_hold{int(k * 100)}", reg_bundle_s=P.REG_BUNDLE_S,
                                          cred_hold_scale=k, content_hold_scale=k) for k in HOLD_SCALES})
BUILDS.update({f"content{int(k * 100)}": dict(target=f"link_content{int(k * 100)}", reg_bundle_s=P.REG_BUNDLE_S,
                                             content_hold_scale=k) for k in (2.0, 3.0)})
CRED_SHORT = (0.75, 0.5, 0.25)                   # credential-path hold factors with content x2 (section 6h)
BUILDS.update({f"c200_cr{int(k * 100)}": dict(target=f"link_c200_cr{int(k * 100)}", reg_bundle_s=P.REG_BUNDLE_S,
                                             content_hold_scale=2.0, cred_hold_scale=k) for k in CRED_SHORT})
# section 6j: content-side stretching at stages that know their role (the device's content channels
# and the content servers' own hold), and the post-match lottery
BUILDS.update({f"dev{int(k * 100)}": dict(target=f"link_dev{int(k * 100)}", reg_bundle_s=P.REG_BUNDLE_S,
                                         content_device_scale=k, cs_hold_scale=k) for k in (2.0, 3.0)})
BUILDS["pm120"] = dict(target="link_pm120", reg_bundle_s=P.REG_BUNDLE_S, post_match=True)
BUILDS["pm_push"] = dict(target="link_pm_push", post_match=True)
BUILDS.update({f"pm{w}": dict(target=f"link_pm{w}", reg_bundle_s=float(w), post_match=True) for w in (60, 240, 480)})
# section 6k: every relay hop's hold widened alike on every path, then a static content-server hold
BUILDS.update({"r150": dict(target="link_r150", reg_bundle_s=P.REG_BUNDLE_S, relay_scale=1.5),
               "r200": dict(target="link_r200", reg_bundle_s=P.REG_BUNDLE_S, relay_scale=2.0),
               "rmix": dict(target="link_rmix", reg_bundle_s=P.REG_BUNDLE_S, relay_mix=True)})
# static hold: the 95th percentile of quorum after content arrival under each relay variant, rounded up
# to 10 s (measured with quorum_timing before section 6k was written)
STATIC_S = {"r150": 740.0, "r200": 870.0, "rmix": 970.0}
for _v, _sv in STATIC_S.items():
    _base = {k: x for k, x in BUILDS[_v].items() if k != "target"}
    BUILDS[f"{_v}_s"] = dict(target=f"link_{_v}_s", cs_static_s=_sv, **_base)
    BUILDS[f"{_v}_sp"] = dict(target=f"link_{_v}_sp", cs_static_s=_sv, post_match_residual=True, **_base)
# section 6l: role-aware x2 (device content channels and content servers' own lottery hold) together
# with every relay hop widened x1.5 as in r150, without the static hold
BUILDS["dev200_r150"] = dict(target="link_dev200_r150", reg_bundle_s=P.REG_BUNDLE_S, content_device_scale=2.0,
                             cs_hold_scale=2.0, relay_scale=1.5)
DEFAULT_BUILD = f"reg{int(P.REG_BUNDLE_S)}"
PRIOR_BUILDS = {"twopoint": ("push",), "regbundle": ("twopoint", "push"),
                **{f"reg{w}": ("push",) for w in REG_WINDOWS}, "reg480": ("push", "reg120"),
                **{b: ("reg120",) for b in ("hold150", "hold200", "hold300", "content200", "content300")},
                **{f"c200_cr{int(k * 100)}": ("reg120", "content200") for k in CRED_SHORT},
                "dev200": ("reg120", "content200"), "dev300": ("reg120", "content300"), "pm120": ("reg120",),
                **{v: ("reg120",) for v in ("r150", "r200", "rmix")},
                **{f"{v}_s": ("reg120", v) for v in ("r150", "r200", "rmix")},
                **{f"{v}_sp": ("reg120", f"{v}_s") for v in ("r150", "r200", "rmix")},
                "dev200_r150": ("dev200", "dev300")}

# Sequences: every step of one plan section, run one after another by `python -m sna sequence <name>`.
SEQUENCES = {
    "6h": dict(out="results/6h", runs=200,
               steps=[(b, "settled") for b in ("reg120", "content200", "c200_cr75", "c200_cr50", "c200_cr25")]),
    "6j": dict(out="results/6j", runs=200,
               steps=[("reg120", "bundle"), ("pm120", "bundle"), ("content200", "settled"), ("content300", "settled"),
                      ("dev200", "settled"), ("dev300", "settled")],
               pairs=dict(builds=("push", "pm_push", "reg60", "pm60", "reg120", "pm120", "reg240", "pm240",
                                  "reg480", "pm480"))),
    "6k": dict(out="results/6k", runs=200,
               quorum=dict(builds=("reg120", "r150", "r200", "rmix")),
               steps=[(b, "settled") for b in ("reg120", "r150", "r150_s", "r150_sp", "r200", "r200_s", "r200_sp",
                                               "rmix", "rmix_s", "rmix_sp")],
               pairs=dict(builds=("reg120", "r150", "r150_s", "r150_sp", "r200", "r200_s", "r200_sp",
                                  "rmix", "rmix_s", "rmix_sp"))),
    "6l": dict(out="results/6l", runs=200,
               steps=[(b, "settled") for b in ("dev200", "dev300", "dev200_r150")],
               pairs=dict(builds=("dev200", "dev300", "dev200_r150"))),
    "smoke": dict(out="results/quick/sequence", runs=2, latency_runs=2,     # checks the sequence itself; never reported
                  steps=[("reg120", "settled"), ("r150_sp", "settled")], quorum=dict(builds=("r150",)),
                  pairs=dict(builds=("reg120", "r150_sp"), runs=2)),
}


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
    """which: all | bundle | nobundle | control use the core decoy levels; extra is the section 6f
    levels with bundling on."""
    specs = []
    if which == "settled":
        return [dict(key=cell_key(R, 40, True), R=float(R), T=float(R + 40), decoys=40.0, bundle=True,
                     control=False) for R in REAL_R]
    if which == "extra":
        return [dict(key=cell_key(R, d, True), R=float(R), T=float(R + d), decoys=float(d), bundle=True,
                     control=False) for R in REAL_R for d in DECOY_EXTRA]
    for bundle in (False, True):
        if which not in ("all", "bundle" if bundle else "nobundle"):
            continue
        for R in REAL_R:
            for d in DECOY_CORE:
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
        m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s) & ~s["decoy"]
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


def latency(out, runs=20, cells=((1, 40), (15, 40), (50, 40)), builds=None):
    """Capture-to-finalisation time of real transactions under each build, with the stages that
    make it up. Run ids from 3,000,000 up, never used by a sweep. Written to <out>/latency.json."""
    out = Path(out)
    D = calibrate(out)["D"]
    pools = Pools()
    res = {}
    builds = tuple(builds or BUILDS)
    for build in builds:
        for R, d in cells:
            spec = dict(R=float(R), decoys=float(d), bundle=True, control=False, build=build)
            cfg = config_of(spec, D)
            acc = {k: [] for k in ("total", "to_gatekeeper", "gk_hold", "gk_bundle_wait", "quorum",
                                  "quorum_to_confirmed", "registry_bundle_wait", "confirmed_to_final")}
            for k in range(runs):
                s = S.simulate(cfg, traffic_seed(R, LATENCY_SEED0 + k), pools).subs
                m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s) & ~s["decoy"] \
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
    _latency_figure(out, res, cells, builds)
    return res


def _latency_figure(out, res, cells, builds):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    R, d = cells[0]
    f, ax = plt.subplots(figsize=(7, 3.6), dpi=300, facecolor="#fcfcfb")
    ax.set_facecolor("#fcfcfb")
    cmap = plt.get_cmap("viridis")
    for j, build in enumerate(builds):
        h = np.array(res[f"{build}.R{R}.D{d}"]["hist10"], float)
        x = np.arange(h.size) * 10 + 5
        ax.plot(x, 100 * h / h.sum(), color=cmap(j / max(len(builds) - 1, 1) * 0.85), linewidth=1.6, label=build)
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


# --------------------------------------------------------------------------- registry bundles
def _reg_bundle_one(args):
    spec, run_id, D = args
    cfg = config_of(spec, D)
    run = S.simulate(cfg, traffic_seed(spec["R"], run_id, spec["control"]), Pools())
    s, W, ph = run.subs, cfg.reg_bundle_s, run.reg_phase
    det = np.concatenate([s["det_f"][s["ok_f"]], s["det_i"][s["ok_i"]]])
    sub = np.concatenate([np.nonzero(s["ok_f"])[0], np.nonzero(s["ok_i"])[0]])
    b = np.ceil((det - ph) / W).astype(np.int64)
    k0, k1 = int(np.ceil((cfg.warmup_s - ph) / W)), int(np.floor((cfg.warmup_s + cfg.measure_s - ph) / W))
    m = (b >= k0) & (b < k1)
    ns = np.bincount(b[m] - k0, minlength=k1 - k0)
    pairs = np.unique(np.c_[b[m] - k0, sub[m]], axis=0)
    nt = np.bincount(pairs[:, 0], minlength=k1 - k0)
    return spec["key"], np.bincount(np.minimum(ns, 127), minlength=128), np.bincount(np.minimum(nt, 127), minlength=128)


def registry_bundles(out, runs=200, build=DEFAULT_BUILD, workers="auto", which="bundle"):
    """Submissions and distinct transactions per registry-level bundle, over the sweep's own runs
    (simulation only). Written to <out>/registry_bundles_<build>.json."""
    import multiprocessing as mp
    out = Path(out)
    D = calibrate(out)["D"]
    specs = [s for s in grid(which, build)]
    tasks = [(s, k, D) for s in specs for k in range(runs)]
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_reg_bundle_one, tasks, chunksize=4)
    acc = {}
    for key, hs, ht in res:
        a = acc.setdefault(key, [np.zeros(128, np.int64), np.zeros(128, np.int64)])
        a[0] += hs
        a[1] += ht
    rows = {}
    for s in specs:
        hs, ht = acc[s["key"]]
        k = np.arange(128)
        n = hs.sum()
        rows[s["key"]] = dict(R=s["R"], decoys=s["decoys"], window_s=P.REG_BUNDLE_S, bundles=int(n),
                              mean_submissions=float((hs * k).sum() / n), mean_transactions=float((ht * k).sum() / n),
                              p_lt2_submissions=float(hs[:2].sum() / n), p_lt2_transactions=float(ht[:2].sum() / n),
                              p_empty=float(hs[0] / n))
        r = rows[s["key"]]
        print(f"{s['key']:10s} bundles {r['bundles']:6d} submissions {r['mean_submissions']:.1f} transactions "
              f"{r['mean_transactions']:.1f} fewer than 2 transactions {100 * r['p_lt2_transactions']:.3f}%", flush=True)
    (out / f"registry_bundles_{build}.json").write_text(json.dumps(dict(runs=runs, build=build, cells=rows), indent=1))
    return rows


# --------------------------------------------------------------------------- gatekeeper occupancy
GK_SEED0 = 4_000_000


def _gk_one(args):
    R, d, run_id, D, windows = args
    spec = dict(R=float(R), decoys=float(d), bundle=True, control=False, build="push")
    cfg = config_of(spec, D).with_(measure_s=P.MEASURE_S)
    run = S.simulate(cfg, traffic_seed(R, GK_SEED0 + run_id), Pools())
    s = run.subs
    a, b = cfg.warmup_s, cfg.warmup_s + cfg.measure_s
    out = dict(arrivals=0, hold_sum=0.0, occ_samples=[], tick_counts=[], win={w: [] for w in windows})
    probes = np.linspace(a, b, 2000, endpoint=False)
    for j, g in enumerate(run.gk_set):
        arr, rel = s["gk_arr"][:, j], s["gk_release"][:, j]
        m = (arr >= a) & (arr < b)
        out["arrivals"] += int(m.sum())
        out["hold_sum"] += float((rel[m] - arr[m]).sum())
        # occupancy: packets held (arrived, not yet selected) at evenly spaced instants
        sa, sr = np.sort(arr), np.sort(rel)
        out["occ_samples"].append(np.searchsorted(sa, probes, "right") - np.searchsorted(sr, probes, "right"))
        # selections per tick of the gatekeeper's hold clock, and per bundle window on its own grid
        sel = rel[(rel >= a) & (rel < b)]
        ph = run.gk_phase[g]
        k = np.floor((sel - ph) / P.TICK_S).astype(np.int64)
        k0, k1 = int(np.ceil((a - ph) / P.TICK_S)), int(np.floor((b - ph) / P.TICK_S))
        kk = k[(k >= k0) & (k < k1)] - k0
        out["tick_counts"].append(np.bincount(kk, minlength=k1 - k0))
        for w in windows:
            phw = run.bundle_phase[g] * w / P.BUNDLE_S
            kb = np.ceil((sel - phw) / w).astype(np.int64)
            b0, b1 = int(np.ceil((a - phw) / w)) + 1, int(np.floor((b - phw) / w))
            kb = kb[(kb >= b0) & (kb < b1)] - b0
            out["win"][w].append(np.bincount(kb, minlength=b1 - b0))
    return R, d, out, cfg.measure_s * len(run.gk_set)


def gatekeeper_occupancy(out, runs=50, R=1, decoys=(20, 30, 40, 50, 60, 100, 150, 175, 200, 250, 300),
                         windows=(30, 60, 90, 120, 135, 150, 180, 240, 300), workers="auto"):
    """Each active gatekeeper's own load under the push build (relay-lottery gatekeeper hold,
    departure bundling on), measured directly: arrival rate, mean hold, packets held at once,
    selections per tick, and postings per bundle at several windows and decoy targets. Run ids
    from 4,000,000 up, never used by a sweep. Written to <out>/gatekeeper_occupancy.json."""
    import multiprocessing as mp
    out = Path(out)
    D = calibrate(out)["D"]
    tasks = [(R, d, k, D, windows) for d in decoys for k in range(runs)]
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_gk_one, tasks, chunksize=1)
    rows = {}
    for d in decoys:
        parts = [(o, t) for (r_, d_, o, t) in res if d_ == d]
        arrivals = sum(o["arrivals"] for o, _ in parts)
        span = sum(t for _, t in parts)
        hold = sum(o["hold_sum"] for o, _ in parts) / arrivals
        occ = np.concatenate([x for o, _ in parts for x in o["occ_samples"]])
        ticks = np.concatenate([x for o, _ in parts for x in o["tick_counts"]])
        row = dict(R=R, decoys=d, arrivals_per_s=arrivals / span, mean_hold_s=hold,
                   held_mean=float(occ.mean()), held_p5=float(np.percentile(occ, 5)),
                   held_p95=float(np.percentile(occ, 95)),
                   selections_per_tick=float(ticks.mean()), ticks_with_none=float((ticks == 0).mean()),
                   windows={})
        for w in windows:
            c = np.concatenate([x for o, _ in parts for x in o["win"][w]])
            n = c.sum()
            row["windows"][str(w)] = dict(mean=float(c.mean()), p_lt2=float((c < 2).mean()),
                                          p_empty=float((c == 0).mean()),
                                          alone_share=float((c == 1).sum() / max(n, 1)),
                                          added_wait_mean_s=w / 2)
        rows[str(d)] = row
        w30 = row["windows"]["30"]
        print(f"decoys {d:3d}: {row['arrivals_per_s']:.4f} arrivals/s per gatekeeper, mean hold {hold:.1f} s, "
              f"held at once {row['held_mean']:.2f} (5-95%: {row['held_p5']:.0f}-{row['held_p95']:.0f}), "
              f"selections per tick {row['selections_per_tick']:.3f}; 30 s bundle mean {w30['mean']:.2f}, "
              f"fewer than 2 {100 * w30['p_lt2']:.2f}%", flush=True)
        print("    " + "  ".join(f"W={w}: {row['windows'][str(w)]['mean']:.1f}/{100 * row['windows'][str(w)]['p_lt2']:.2f}%"
                                 for w in windows), flush=True)
    (out / "gatekeeper_occupancy.json").write_text(json.dumps(dict(runs=runs, rates_from_D=D, cells=rows), indent=1))
    return rows



# --------------------------------------------------------------------------- F and I submitting together
PAIRS_SEED0 = 8_000_000


def _pairs_one(args):
    build, R, d, run_id, D = args
    spec = dict(R=float(R), decoys=float(d), bundle=True, control=False, build=build)
    cfg = config_of(spec, D)
    run = S.simulate(cfg, traffic_seed(R, PAIRS_SEED0 + run_id), Pools())
    s = run.subs
    m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s) & ~s["decoy"] & s["ok_f"] & s["ok_i"]
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


def pair_gaps(out, builds, runs=20, cells=None, workers="auto"):
    """How often a record's two registry submissions leave together. For every build and cell: the
    share of real records whose submissions leave within 5 s of each other; the same at the point
    of submission, before any registry wait; and, of the pairs separated by more than 5 s at that
    point, the share that a registry window puts back in one bundle. Run ids from 8,000,000 up,
    never used by a sweep. Written to <out>/pair_gaps.json."""
    import multiprocessing as mp
    out = Path(out)
    D = calibrate(out)["D"]
    # real records' timing does not depend on the decoy stream, so one decoy level suffices
    cells = cells or [(R, 40) for R in REAL_R]
    tasks = [(b, R, d, k, D) for b in builds for R, d in cells for k in range(runs)]
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_pairs_one, tasks, chunksize=1)
    rows = {}
    for b in builds:
        for R, d in cells:
            x = [r for r in res if r[0] == b and r[1] == R and r[2] == d]
            sg, rg, wt, sm, ei, ps = (np.concatenate([r[i] for r in x]) for i in (3, 4, 5, 6, 7, 8))
            sep = rg > 5.0
            row = dict(build=b, R=R, decoys=d, records=int(sg.size), runs=runs,
                       within5_at_departure=float((sg <= 5.0).mean()),
                       within5_at_submission=float((rg <= 5.0).mean()),
                       quorum_outlasted_both_holds=float(wt.mean()),
                       quorum_outlasted_either_hold=float(ei.mean()),
                       quorum_outlasted_hold_per_server=float(ps.mean()),
                       within5_at_submission_when_outlasted=float((rg[wt] <= 5.0).mean()) if wt.any() else float("nan"),
                       separated=int(sep.sum()),
                       separated_same_bundle=float(sm[sep].mean()) if sep.any() and BUILDS[b].get("reg_bundle_s") else float("nan"),
                       median_gap_at_submission=float(np.median(rg)))
            rows[f"{b}.R{R}.D{d}"] = row
            sb = row["separated_same_bundle"]
            print(f"{b:8s} R={R:2d} decoys={d:2d}: within 5 s at submission {100 * row['within5_at_submission']:5.1f}%, "
                  f"as they leave {100 * row['within5_at_departure']:5.1f}%; separated pairs put back in one bundle "
                  f"{'n/a' if np.isnan(sb) else f'{100 * sb:.1f}%'} (n = {row['records']})", flush=True)
    (out / "pair_gaps.json").write_text(json.dumps(dict(runs=runs, cells=rows), indent=1))
    return rows



# --------------------------------------------------------------------------- quorum timing at the content servers
QUORUM_SEED0 = 9_000_000


def _quorum_one(args):
    build, R, d, run_id, D = args
    cfg = config_of(dict(R=float(R), decoys=float(d), bundle=True, control=False, build=build), D)
    s = S.simulate(cfg, traffic_seed(R, QUORUM_SEED0 + run_id), Pools()).subs
    m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s)
    out = []
    for nm, arr in (("f", "arr_f"), ("i", "arr_i")):
        ok = m & np.isfinite(s[f"known_{nm}"])
        out.append(s[f"known_{nm}"][ok] - s[arr][ok])
    return build, np.concatenate(out)


def quorum_timing(out, builds, runs=20, R=15, d=40, workers="auto"):
    """When quorum reaches a content server, measured from its content's arrival there (negative:
    quorum was already known). Every transaction, real and decoy. Run ids from 9,000,000 up, never
    used by a sweep. Written to <out>/quorum_timing.json."""
    import multiprocessing as mp
    out = Path(out)
    D = calibrate(out)["D"]
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_quorum_one, [(b, R, d, k, D) for b in builds for k in range(runs)], chunksize=1)
    rows = {}
    for b in builds:
        x = np.concatenate([r[1] for r in res if r[0] == b])
        q = {f"p{p}": float(np.percentile(x, p)) for p in (50, 75, 90, 95, 99)}
        rows[b] = dict(n=int(x.size), mean=float(x.mean()), already_known=float((x <= 0).mean()), **q)
        print(f"{b:8s} quorum after content arrival: mean {x.mean():6.1f} s, median {q['p50']:6.1f}, p90 {q['p90']:6.1f}, "
              f"p95 {q['p95']:6.1f}, p99 {q['p99']:6.1f}; already known at arrival {100 * rows[b]['already_known']:.1f}% "
              f"(n = {x.size})", flush=True)
    (out / "quorum_timing.json").write_text(json.dumps(dict(runs=runs, R=R, decoys=d, builds=rows), indent=1))
    return rows

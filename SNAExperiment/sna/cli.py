"""Command line: python -m sna run [--runs N] [--workers N] [--out DIR]

  run   calibrates D under every configuration's own holds, builds the attacker's models, simulates
        and scores every run of the main configuration and the controls, and writes every file in
        results/. Resumable: rerunning the same command skips the runs already on disk.

Results depend on the cell and run id only, never on the worker count or the order runs finish in.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from . import experiment as EX
from . import report
from . import runner as RN


def run(out, runs, workers):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    p = out / "run_info.json"
    info = json.loads(p.read_text()) if p.exists() else {}
    if info and info.get("config_hash") != EX.config_hash():
        raise SystemExit(f"{out} holds runs made under other settings. Use a new --out directory, or empty that one.")
    t0 = time.time()
    if "D" not in info:
        info["calibration"] = {}
        longest = {name: EX.calibrate_longest(name) for name in EX.CONFIGS}
        info["windows"] = {name: EX.windows(longest, name) for name in EX.CONFIGS}
        for name, w in info["windows"].items():
            print(f"windows ({name}): longest capture to finalization {w['longest']:.1f} s; warm-up {w['warmup']:.1f} s, "
                  f"window {w['window']:.1f} s, cool-down {w['cooldown']:.1f} s", flush=True)
        for name in EX.CONFIGS:
            cal = EX.calibrate(name, info["windows"][name])
            info["calibration"][name] = cal
            last = cal["history"][-1]
            print(f"calibration ({name}): D = {cal['D']:.1f} s; in flight at R = {EX.CAL_R}: real {last['real_in_flight']:.2f}, "
                  f"decoys {last['decoys_in_flight']:.2f}{'' if cal['converged'] else ' (NOT within 3%)'}", flush=True)
            if not cal["converged"]:
                raise SystemExit(f"calibration of {name} did not bring the in-flight counts within 3% of their targets")
        info["D"] = {k: v["D"] for k, v in info["calibration"].items()}
        info.update(config_hash=EX.config_hash(), seeds=dict(calibration=EX.CAL_SEED0, models=EX.MODEL_SEED0,
                    shuffle=EX.SHUFFLE_SEED, traffic="sha256 of the volume and run id"), decoys=EX.DECOYS, R=list(EX.REAL_R))
    info["runs_per_cell"] = {EX.MAIN: runs, **{c: min(EX.CONTROL_RUNS[c], runs) for c in EX.CONTROLS}}
    p.write_text(json.dumps(info, indent=1))
    for name in EX.CONFIGS:
        EX.ensure_models(out, name)
    done = lambda name, R: RN.done_runs(out, EX.rec_name(name, R))  # noqa: E731
    todo = []
    for name, n in info["runs_per_cell"].items():
        todo += EX.tasks(out, name, n, info["D"][name], info["windows"][name], done)
    RN.execute(todo, EX.worker, out, workers, label="run")
    report.write_all(out, info)
    print(f"done in {(time.time() - t0) / 60:.1f} min; results in {out}", flush=True)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m sna", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["run"])
    ap.add_argument("--out", help="results directory (default: results/)")
    ap.add_argument("--workers", default="auto", help="worker processes (default: half the cores)")
    ap.add_argument("--runs", type=int, default=EX.RUNS, help="runs per cell of the main configuration (default: %(default)s); "
                    "each control runs its own count or this, whichever is smaller")
    a = ap.parse_args(argv)
    run(Path(a.out or EX.RESULTS), a.runs, a.workers)

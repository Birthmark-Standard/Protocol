"""Parallel, resumable execution of independent runs.

Each finished run is appended to <out>/raw/<file>.pkl.gz as one pickle record, so an interrupted
job loses at most the runs in flight (one per worker). On restart, run ids already on disk are
skipped. Works with the spawn start method (Windows, macOS): workers are top-level functions and
all per-process state lives in module-level caches.
"""
from __future__ import annotations

import gzip
import os
import pickle
import time
from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from pathlib import Path


def raw_path(out: Path, name: str) -> Path:
    return Path(out) / "raw" / f"{name}.pkl.gz"


def load(out: Path, name: str) -> list[dict]:
    """Every complete record in one raw file. A record cut off by an interruption is dropped."""
    p = raw_path(out, name)
    res = []
    if p.exists():
        with gzip.open(p, "rb") as f:
            while True:
                try:
                    res.append(pickle.load(f))
                except (EOFError, OSError, pickle.UnpicklingError):
                    break
    return res


def done_runs(out: Path, name: str) -> set[int]:
    return {r["run"] for r in load(out, name)}


def resolve_workers(workers) -> int:
    if workers in (None, "auto"):
        return max(1, os.cpu_count() or 1)
    return max(1, int(workers))


def execute(tasks, worker, out: Path, workers="auto", label=""):
    """Run worker(*task) for every task. A worker returns a list of (file name, record) pairs,
    each record carrying its "run" id; the parent appends them as they arrive.

    tasks: list of tuples, in the order they should start."""
    out = Path(out)
    (out / "raw").mkdir(parents=True, exist_ok=True)
    n, nw = len(tasks), resolve_workers(workers)
    if not n:
        print(f"{label}: nothing to do", flush=True)
        return
    print(f"{label}: {n} runs on {nw} workers", flush=True)
    handles, t0, finished = {}, time.time(), 0
    pending, it = set(), iter(tasks)
    try:
        with ProcessPoolExecutor(nw) as ex:
            for _ in range(nw * 2):                   # bounded queue: at most 2 runs per worker in flight
                t = next(it, None)
                if t is None:
                    break
                pending.add(ex.submit(worker, *t))
            while pending:
                done, pending = wait(pending, return_when=FIRST_COMPLETED)
                for f in done:
                    for name, rec in f.result():
                        if name not in handles:
                            p = raw_path(out, name)
                            handles[name] = gzip.open(p, "ab")
                        pickle.dump(rec, handles[name])
                        handles[name].flush()
                    finished += 1
                    t = next(it, None)
                    if t is not None:
                        pending.add(ex.submit(worker, *t))
                el = time.time() - t0
                eta = el / finished * (n - finished)
                if finished == n or finished % max(1, min(50, n // 20)) == 0:
                    print(f"{label}: {finished}/{n} runs, {el / 60:.1f} min elapsed, ETA {eta / 60:.1f} min", flush=True)
    finally:
        for h in handles.values():
            h.close()

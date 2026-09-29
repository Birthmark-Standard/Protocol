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
    """Every complete record in one raw file. Each writing session appends its own gzip member;
    a member cut off by an interruption is skipped, and every intact member after it is still
    read. A record cut off mid-pickle is dropped."""
    p = raw_path(out, name)
    if not p.exists():
        return []
    by_run = {}
    for r in read_records(p):                  # a run recomputed after an interruption is identical
        by_run[r.get("run")] = r
    return list(by_run.values())


def read_records(p: Path) -> list[dict]:
    import io
    import zlib
    data = Path(p).read_bytes()
    res, pos, magic = [], 0, b"\x1f\x8b\x08"
    while pos < len(data):
        d = zlib.decompressobj(wbits=31)
        try:
            raw = d.decompress(data[pos:])
            complete = d.eof
        except zlib.error:
            raw, complete = b"", False
        buf = io.BytesIO(raw)
        while True:
            try:
                res.append(pickle.load(buf))
            except (EOFError, pickle.UnpicklingError, ValueError, TypeError, AttributeError, IndexError):
                break
        if complete:
            pos = len(data) - len(d.unused_data)
        else:                                  # damaged member: resume at the next member header
            nxt = data.find(magic, pos + 1)
            if nxt < 0:
                break
            pos = nxt
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

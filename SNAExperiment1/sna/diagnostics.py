"""Diagnostics outside the pre-registered analysis. Each is reported as exploratory.

content_server_sources: splits the content server's evidence into its two sources. The content
server scores a candidate with the joint density of the record time's offset y = u - s and its own
content arrival's offset x = a - s. This diagnostic also scores the same rows with each source
alone: the record time alone (the passive observer's likelihood g(y), restricted to the content
server's rows) and the content arrival alone (the marginal density q(x), over the candidates
whose x lies in q's support). It runs on the sweep's own run ids, under each build's own models.
"""
from __future__ import annotations

import json
import pickle
from pathlib import Path

import numpy as np

from . import attacks as AT
from . import cells as CE
from . import sim as S
from .pools import Pools


def _cs_one(args):
    out, build, R, d, run_id, D = args
    spec = dict(R=float(R), decoys=float(d), bundle=True, control=False, build=build)
    with open(CE.model_path(out, False, True, build), "rb") as f:
        m = pickle.load(f)
    pools = Pools()
    run = S.simulate(CE.config_of(spec, D), CE.traffic_seed(R, run_id), pools)
    rec, cand = AT.records(run, pools), AT.candidates(run, pools)
    ri, grp, extra = AT._vantage_rows("content_server", run, rec, run_id)
    u, a = rec["u"][ri], extra["a"]
    truth = dict(sub=rec["sub"][ri], dev=rec["dev"][ri])
    g, cs, csq = m.pdf["g"], m.pdf["cs"], m.pdf["cs_q"]
    lo, hi = AT._band(u, g)
    joint = AT.score_blocks(lo, hi, cand, lambda r, k0, k1: cs(a[r][:, None] - cand["t"][None, k0:k1],
                                                               u[r][:, None] - cand["t"][None, k0:k1])
                            + csq(a[r][:, None] - cand["t"][None, k0:k1]), truth)
    rec_only = AT.score_blocks(lo, hi, cand, lambda r, k0, k1: g(u[r][:, None] - cand["t"][None, k0:k1]), truth)
    alo, ahi = a - csq.support[1], a - csq.support[0] + 1e-9
    arr_only = AT.score_blocks(alo, ahi, cand, lambda r, k0, k1: csq(a[r][:, None] - cand["t"][None, k0:k1]), truth)
    real = ~run.subs["decoy"][rec["sub"][ri]]
    return (build, R, d, int(real.sum()),
            *(int(x["dev"]["correct"][real].sum()) for x in (joint, rec_only, arr_only)),
            float(np.mean(1.0 / np.maximum(arr_only["dev"]["n_feas"][real], 1))),
            float(np.mean(1.0 / np.maximum(rec_only["dev"]["n_feas"][real], 1))))


def content_server_sources(out, builds=("push", "reg120", "reg240", "reg480"), cells=((1, 40), (15, 40)),
                           runs=40, workers="auto"):
    import multiprocessing as mp
    from . import runner as RN
    out = Path(out)
    D = CE.calibrate(out)["D"]
    tasks = [(str(out), b, R, d, k, D) for b in builds for R, d in cells for k in range(runs)]
    with mp.Pool(RN.resolve_workers(workers)) as pool:
        res = pool.map(_cs_one, tasks, chunksize=1)
    rows = {}
    for b in builds:
        for R, d in cells:
            x = [r for r in res if r[0] == b and r[1] == R and r[2] == d]
            n = sum(r[3] for r in x)
            row = dict(build=b, R=R, decoys=d, runs=runs, n=n,
                       joint=sum(r[4] for r in x) / n, record_time_only=sum(r[5] for r in x) / n,
                       arrival_only=sum(r[6] for r in x) / n,
                       random_arrival_band=float(np.mean([r[7] for r in x])),
                       random_record_band=float(np.mean([r[8] for r in x])))
            rows[f"{b}.R{R}.D{d}"] = row
            print(f"{b:7s} R={R:2d} decoys={d}: content server {100 * row['joint']:.2f}%, record time alone "
                  f"{100 * row['record_time_only']:.2f}%, content arrival alone {100 * row['arrival_only']:.2f}% "
                  f"(random {100 * row['random_record_band']:.2f}% / {100 * row['random_arrival_band']:.2f}%), "
                  f"n = {n}", flush=True)
    (out / "diag_content_server.json").write_text(json.dumps(dict(runs=runs, cells=rows), indent=1))
    return rows

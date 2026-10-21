"""Scoring, pairing, loader and control-configuration checks for AUDIT.md. Changes nothing.

Run from SNAExperiment/:  python audit/scoring_audit.py [out_dir]
Builds the internal_compromise models in <out_dir> (seed 1e9, as the experiment does), scores 3 runs at
R = 20 on run ids 60,000 and up, and writes <out_dir>/scoring_results.json.
"""
import dataclasses
import gzip
import json
import pickle
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sna import attacks as AT, experiment as EX, params as P, runner as RN, sim as S  # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "out"
OUT.mkdir(parents=True, exist_ok=True)
D = json.loads((Path(__file__).resolve().parent.parent / "results" / "calibration.json").read_text())["D"]
res = {}

EX.ensure_models(OUT, "internal_compromise")
m = pickle.load(open(EX.model_path(OUT, "internal_compromise"), "rb"))
res["G3_models"] = dict(pdf_keys=sorted(m.pdf), mc_runs=m.mc_runs, samples=m.samples,
                        one_first_hop_model_for_all_paths="fh" in m.pdf and not any(k.startswith("fh_") and k != "fh_q" for k in m.pdf))

ties, feas, vfeas, rows = {}, {}, [], {}
for k in range(3):
    cfg = EX.config_of(dict(R=20.0, decoys=60.0, build="internal_compromise"), D)
    run = S.simulate(cfg, EX.traffic_seed(20, 60_000 + k))
    rec = AT.records(run)
    keep = AT.scored_mask(run, rec["sub"])
    rec = {x: y[keep] for x, y in rec.items()}
    cand = AT.candidates(run)
    g = m.pdf["g"]
    lo, hi = AT._band(rec["u"], g)
    base = AT.score_blocks(lo, hi, cand, lambda r, a, b: g(rec["u"][r][:, None] - cand["t"][None, a:b]),
                           dict(sub=rec["sub"], dev=rec["dev"]))
    for v in AT.VANTAGES:
        ri, grp, out, _ = AT.score_vantage(v, run, rec, cand, m, base, k)
        o = out["dev"]
        t = (o["top1"] == o["top2"]) & np.isfinite(o["top1"])
        ties.setdefault(v, []).append(float(t.mean()))
        feas.setdefault(v, []).append(float(np.median(o["n_feas"])))
        rows.setdefault(v, []).append(int(ri.size))
        if v == "validator":
            vfeas.append(int(np.median(o["n_feas"])))
    res.setdefault("F4_rows_per_run", rows)
res["G4_share_device_decisions_with_tied_top_score"] = {v: float(np.mean(x)) for v, x in ties.items()}
res["G6_median_feasible_devices"] = {v: float(np.mean(x)) for v, x in feas.items()}
res["F4_rows_per_run"] = {v: x for v, x in rows.items()}

# H3. pairing across builds: same seed, same real traffic
a = S.simulate(EX.config_of(dict(R=20.0, decoys=60.0, build="internal_compromise"), D), EX.traffic_seed(20, 60_000)).subs
b = S.simulate(EX.config_of(dict(R=20.0, decoys=60.0, build="no_mechanisms"), D), EX.traffic_seed(20, 60_000)).subs
c = S.simulate(EX.config_of(dict(R=20.0, decoys=60.0, build="permitted_overlap"), D), EX.traffic_seed(20, 60_000)).subs
res["H3_pairing_across_builds"] = dict(
    same_t0_src_no_mechanisms=bool(np.array_equal(a["t0"], b["t0"]) and np.array_equal(a["src"], b["src"])),
    same_t0_src_CFI_permitted_overlap=bool(all(np.array_equal(a[x], c[x]) for x in ("t0", "src", "C", "F", "I"))),
    same_relays_permitted_overlap=bool(all(np.array_equal(a[x], c[x]) for x in "ABDEGH")))

# I4. loader: an interrupted member, then two resumed sessions
with tempfile.TemporaryDirectory() as tmp:
    p = RN.raw_path(tmp, "x")
    p.parent.mkdir(parents=True)
    blob = gzip.compress(b"".join(pickle.dumps(dict(run=i, pad=bytes(3000))) for i in range(5)))
    p.write_bytes(blob[: len(blob) * 2 // 3])
    done_before = sorted(RN.done_runs(tmp, "x"))
    with gzip.open(p, "ab") as f:
        for i in range(5, 8):
            pickle.dump(dict(run=i), f)
    with gzip.open(p, "ab") as f:
        pickle.dump(dict(run=8), f)
    res["I4_loader"] = dict(runs_read_while_cut_member_is_last=done_before, runs_read_after_two_resumed_members=sorted(RN.done_runs(tmp, "x")))

# I2. control and build configurations against the defaults
base = dataclasses.asdict(P.Config())
res["I2_configurations"] = {b: {k: v for k, v in dataclasses.asdict(P.Config(**kw)).items() if v != base[k]}
                            for b, kw in EX.ALL_BUILDS.items()}
res["defaults"] = base
(OUT / "scoring_results.json").write_text(json.dumps(res, indent=1, default=float))
print(json.dumps(res, indent=1, default=float))

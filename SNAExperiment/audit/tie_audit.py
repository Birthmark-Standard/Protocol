"""Ties at the top device score: how often, which device wins, and how often the winner is right.
Run from SNAExperiment/ after scoring_audit.py (it reuses the models in <out_dir>).
Scores 3 runs per cell at R = 1 and R = 20 on run ids 60,000 and up. Writes <out_dir>/tie_results.json."""
import json
import pickle
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sna import attacks as AT, experiment as EX, sim as S  # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "out"
D = json.loads((Path(__file__).resolve().parent.parent / "results" / "calibration.json").read_text())["D"]
m = pickle.load(open(EX.model_path(OUT, "internal_compromise"), "rb"))
res = {}
for R in (1, 20):
    acc = {}
    for k in range(3):
        cfg = EX.config_of(dict(R=float(R), decoys=60.0, build="internal_compromise"), D)
        run = S.simulate(cfg, EX.traffic_seed(R, 60_000 + k))
        rec = AT.records(run)
        keep = AT.scored_mask(run, rec["sub"])
        rec = {x: y[keep] for x, y in rec.items()}
        cand = AT.candidates(run)
        g = m.pdf["g"]
        lo, hi = AT._band(rec["u"], g)
        base = AT.score_blocks(lo, hi, cand, lambda r, a, b: g(rec["u"][r][:, None] - cand["t"][None, a:b]),
                               dict(sub=rec["sub"], dev=rec["dev"]))
        for v in ("baseline", "first_hop_cred", "content_server"):
            ri, grp, out, _ = AT.score_vantage(v, run, rec, cand, m, base, k)
            o = out["dev"]
            tie = (o["top1"] == o["top2"]) & np.isfinite(o["top1"])
            a = acc.setdefault(v, dict(decisions=0, ties=0, tie_pick_real_device=0, tie_correct=0, correct=0))
            a["decisions"] += int(tie.size); a["ties"] += int(tie.sum())
            a["tie_pick_real_device"] += int((o["pick"][tie] < 100_000).sum())
            a["tie_correct"] += int(o["correct"][tie].sum()); a["correct"] += int(o["correct"].sum())
    res[f"R{R}"] = acc
(OUT / "tie_results.json").write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=1))

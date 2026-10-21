"""Trace of the controls' configurations for AUDIT.md item I2. Reads the experiment code; changes nothing.

Run from SNAExperiment/:  python audit/control_trace.py [out_dir]
Writes <out_dir>/control_trace.json (default audit/out). Run ids 70,000 and up are used by no result.
For each control: every per-stage wait that remains, and the share of F and I confirmations set by the
board (the credential path) rather than by the server's own content arrival and hold, on 5 runs at R = 20.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sna import experiment as EX, sim as S  # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "out"
OUT.mkdir(parents=True, exist_ok=True)
D = json.loads((Path(__file__).resolve().parent.parent / "results" / "calibration.json").read_text())["D"]
RUN0, RUNS, R = 70_000, 5, 20


def mean(x):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    return float(x.mean()) if x.size else None


res = {}
for b in ["internal_compromise", *EX.CONTROLS]:
    acc = {}
    for k in range(RUNS):
        cfg = EX.config_of(dict(R=float(R), decoys=60.0, build=b), D)
        run = S.simulate(cfg, EX.traffic_seed(R, RUN0 + k))
        s, ev = run.subs, run.events
        m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s) & s["ok_f"] & s["ok_i"]
        ts, ta = ev["t_send"], ev["t_arr"]
        row = dict(
            device_cred=ts[s["ev_cred"][m, 0]] - s["t0"][m],
            device_F=ts[s["ev_ca"][m, 0]] - s["t0"][m],
            device_I=ts[s["ev_cb"][m, 0]] - s["t0"][m],
            relay_A=ts[s["ev_cred"][m, 1]] - ta[s["ev_cred"][m, 0]],
            relay_D=ts[s["ev_ca"][m, 1]] - ta[s["ev_ca"][m, 0]],
            relay_G=ts[s["ev_cb"][m, 1]] - ta[s["ev_cb"][m, 0]],
            C_hold=s["cv1_s"][m] - s["arr_c"][m],
            fanout=(s["gk_send"][m] - s["cv2_a"][m][:, None]).ravel(),
            gk_hold=(s["gk_release"][m] - s["gk_arr"][m]).ravel(),
            gk_departure_wait=(s["posts"][m] - s["gk_release"][m]).ravel(),
            board_push_wait=s["known_f"][m] - s["quorum"][m],
            F_prematch=s["hold_f"][m] - s["arr_f"][m],
            F_postmatch=s["ready_f"][m] - s["det_f"][m],
            registry_wait=s["reg_f"][m] - s["ready_f"][m],
            F_set_by_board=(s["known_f"][m] >= s["hold_f"][m]).astype(float),
            I_set_by_board=(s["known_i"][m] >= s["hold_i"][m]).astype(float),
            capture_to_final=np.maximum(s["reg_f"][m], s["reg_i"][m]) - s["t0"][m],
        )
        for key, v in row.items():
            acc.setdefault(key, []).append(v)
    res[b] = {key: mean(np.concatenate(v)) for key, v in acc.items()}
    print(b, {k: round(v, 2) for k, v in res[b].items()}, flush=True)
(OUT / "control_trace.json").write_text(json.dumps(res, indent=1))

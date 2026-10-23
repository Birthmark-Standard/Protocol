"""The run: its configurations, cells, seeds, the in-flight calibration, the attacker's models, the
per-run worker and the run-level measurements.

A cell is a real volume R (real transactions in flight) with 100 decoy transactions in flight. Rates
follow from the mean end-to-end delay D (capture to the registry posting the record): real rate
R / D, decoy rate 100 / D. D is calibrated under each configuration's own holds, and the counts in
flight are measured in every run. A decoy is a genuine transaction from one of the decoy
infrastructure's registered identities, each capturing at a device's rate.

The main configuration is the protocol as specified, with the role draw that allows every
coincidence the routing design permits. The controls change its holds only.
"""
from __future__ import annotations

import hashlib
import json
import pickle
import time
from pathlib import Path

import numpy as np

from . import attacks as AT
from . import params as P
from . import sim as S

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"

REAL_R = (1, 100, 500)                           # real transactions in flight
DECOYS = 100                                     # decoy transactions in flight
RUNS = 200                                       # runs per cell, main configuration
TOLERANCE = 0.03                                 # measured in-flight counts within 3% of their targets

MAIN = "main"
_OFF = dict(relay1_mean=60.0, relay2_mean=300.0, dev_cred_mean=0.0, dev_content_mean=0.0, c_hold_mean=0.0, v_hold_mean=0.0,
            fanout_mean=0.0, gk_mean=0.0, gk_inclusion=False, cs_mean=0.0, post_match=False, reg_bundle_s=0.0,
            reg_post_s=0.0)
CONFIGS = {
    MAIN: {},
    # every hold, lottery and schedule off
    "no_holds": dict(_OFF, relay1_mean=0.0, relay2_mean=0.0),
    # the credential path sets the record time: every credential-side stage holds (150 s), the content
    # paths carry only their relays
    "first_relay_cred": dict(_OFF, dev_cred_mean=150.0, c_hold_mean=150.0, v_hold_mean=150.0, fanout_mean=50.0,
                             gk_mean=150.0, gk_inclusion=True),
    # the content paths set the record time: the device holds both content channels (7,200 s)
    "first_relay_content": dict(_OFF, dev_content_mean=7200.0),
    # the F content path sets the record time: the device holds its F channel only (7,200 s)
    "first_relay_f": dict(_OFF, dev_content_mean=7200.0, dev_content_i_mean=0.0),
}
CONTROLS = tuple(k for k in CONFIGS if k != MAIN)
CONTROL_RUNS = {"no_holds": 50, "first_relay_cred": 100, "first_relay_content": 100, "first_relay_f": 100}
LABEL = {MAIN: "Main run", "no_holds": "Every hold off", "first_relay_cred": "Credential path sets the record time",
         "first_relay_content": "Content paths set the record time", "first_relay_f": "F content path sets the record time"}
# what sets a confirmation under each first-relay control, and so what its intended-path share counts
INTENDED = {"first_relay_cred": "board", "first_relay_content": "content", "first_relay_f": "f_path"}

CAL_SEED0, MODEL_SEED0, SHUFFLE_SEED = 2_000_000_000, 1_000_000_000, 14_000_000
CAL_RUNS, CAL_R = 40, 100
SHUFFLE_K = 200


def cell_key(R, decoys=DECOYS):
    return f"R{R:g}_D{decoys:g}"


WINDOW_D = 10.0                                  # the scored window lasts at most 10 D ...
MAX_REAL_PER_RUN = 220                           # ... and holds at most 220 real transactions per run on average


def window_s(R, D):
    """Scored window: WINDOW_D times D, shortened at large real volume to hold MAX_REAL_PER_RUN real
    transactions on average and extended at small real volume to hold MIN_REAL_PER_RUN. Measured in units
    of D, it holds the same number of records per run under every configuration."""
    return D * max(P.MIN_REAL_PER_RUN / R, min(WINDOW_D, MAX_REAL_PER_RUN / R))


def config(name, R, D):
    return P.Config(real_rate=R / D, decoy_rate=DECOYS / D, measure_s=window_s(R, D), **CONFIGS[name])


def traffic_seed(R, run_id):
    """Seed of one run's traffic. It depends on the real volume and the run only."""
    h = hashlib.sha256(f"sna|R={R:g}|run={run_id}|control=0".encode()).digest()
    return int.from_bytes(h[:8], "little") >> 1


def config_hash():
    """Fingerprint of every configuration and the cells, written to run_info.json; a results
    directory written under other settings is never resumed."""
    blob = json.dumps(dict(configs={k: P.Config(**v).__dict__ for k, v in CONFIGS.items()}, R=REAL_R, decoys=DECOYS),
                      sort_keys=True, default=str)
    return hashlib.sha256(blob.encode()).hexdigest()[:16]


# --------------------------------------------------------------------------- in flight
def leaves(s):
    """When each transaction leaves the system: the registry posting its record, or, for one that never
    reaches quorum, the content server dropping it 30 minutes after its content arrived."""
    drop = np.fmax(s["arr_f"], s["arr_i"]) + P.QUORUM_TIMEOUT_S
    return np.where(np.isfinite(s["final"]), s["final"], drop)


def in_flight(run):
    """Mean number of real and of decoy transactions in flight over the scored window: from capture to
    leaving the system."""
    s, cfg = run.subs, run.cfg
    a, b = cfg.warmup_s, cfg.warmup_s + cfg.measure_s
    overlap = np.clip(np.minimum(leaves(s), b) - np.maximum(s["t0"], a), 0.0, None)
    return float(overlap[~s["decoy"]].sum() / (b - a)), float(overlap[s["decoy"]].sum() / (b - a))


def calibrate(name, D0=1000.0, runs=CAL_RUNS, R=CAL_R, max_iter=6):
    """D under one configuration's own holds. Each iteration runs the cell at rates from the current D,
    measures the counts in flight and the mean time a transaction stays in the system, and sets D to
    that time (Little's law); it stops once both counts are within TOLERANCE of their targets."""
    D, history, ok = D0, [], False
    for it in range(max_iter):
        cfg = config(name, R, D)
        real, dec, dur = [], [], []
        for k in range(runs):
            run = S.simulate(cfg, CAL_SEED0 + k)
            s = run.subs
            m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s)
            dur.append(leaves(s)[m] - s["t0"][m])
            r, d = in_flight(run)
            real.append(r)
            dec.append(d)
        dur = np.concatenate(dur)
        h = dict(D=D, real_in_flight=float(np.mean(real)), decoys_in_flight=float(np.mean(dec)),
                 mean_residence=float(np.mean(dur)), runs=runs, R=R)
        history.append(h)
        ok = abs(h["real_in_flight"] / R - 1) <= TOLERANCE and abs(h["decoys_in_flight"] / DECOYS - 1) <= TOLERANCE
        if ok and it > 0:
            break
        D = h["mean_residence"]
    return dict(D=history[-1]["D"], history=history, converged=ok)


# --------------------------------------------------------------------------- models
def model_path(out, name):
    """The attacker's likelihood models under one configuration. An attacker knows the protocol, so each
    configuration is attacked with models built under it."""
    return Path(out) / "models" / f"{name}.pkl"


def ensure_models(out, name):
    p = model_path(out, name)
    if p.exists():
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    t = time.time()
    m = AT.build_models(P.Config(**CONFIGS[name]), seed0=MODEL_SEED0)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(m, f)
    tmp.replace(p)
    print(f"models ({name}): {m.mc_runs} Monte Carlo runs, {time.time() - t:.0f} s", flush=True)


def rec_name(name, R):
    return f"{name}__{cell_key(R)}"


# --------------------------------------------------------------------------- run-level measurements
def _stage(acc, name, v):
    v = np.asarray(v, float)
    v = v[np.isfinite(v)]
    a = acc.setdefault(name, [0, 0.0, 0.0, 0.0])
    a[0] += v.size
    a[1] += v.sum()
    a[2] += (v * v).sum()
    a[3] = max(a[3], float(v.max())) if v.size else a[3]


def run_stats(run):
    """In-flight counts, what sets each confirmation, every stage's delay, and the delay from each
    packet type's departure to the record time, over the run's scored real transactions."""
    s, ev = run.subs, run.events
    real, dec = in_flight(run)
    window = AT.scored_mask(run, np.arange(s["t0"].size))
    # a real transaction introduced in the window that never reaches a posted record (a quorum timeout)
    unfinalized = int((window & ~np.isfinite(s["posted"])).sum())
    m = window & s["ok_f"] & s["ok_i"]
    board = np.r_[s["known_f"][m] >= s["hold_f"][m], s["known_i"][m] >= s["hold_i"][m]]
    f_path = (s["hold_f"][m] > s["known_f"][m]) & (s["reg_f"][m] >= s["reg_i"][m])
    ts, ta = ev["t_send"], ev["t_arr"]
    cr, ca, cb = s["ev_cred"][m], s["ev_ca"][m], s["ev_cb"][m]
    st = {}
    for name, v in (
            ("device, credential channel", ts[cr[:, 0]] - s["t0"][m]),
            ("device, content channels", np.r_[ts[ca[:, 0]], ts[cb[:, 0]]] - np.r_[s["t0"][m], s["t0"][m]]),
            ("first relay hops (A, D, G)", np.r_[ts[cr[:, 1]] - ta[cr[:, 0]], ts[ca[:, 1]] - ta[ca[:, 0]], ts[cb[:, 1]] - ta[cb[:, 0]]]),
            ("second relay hops (B, E, H)", np.r_[ts[cr[:, 2]] - ta[cr[:, 1]], ts[ca[:, 2]] - ta[ca[:, 1]], ts[cb[:, 2]] - ta[cb[:, 1]]]),
            ("C before CV-1", s["cv1_s"][m] - s["arr_c"][m]),
            ("V before CV-2", ts[s["ev_cv2"][m]] - ta[s["ev_cv1"][m]]),
            ("C fan-out, per leg", (s["gk_send"][m] - s["cv2_a"][m][:, None]).ravel()),
            ("gatekeeper hold", (s["gk_release"][m] - s["gk_arr"][m]).ravel()),
            ("departure bundling wait", (s["posts"][m] - s["gk_release"][m]).ravel()),
            ("F/I pre-match hold", np.r_[s["hold_f"][m] - s["arr_f"][m], s["hold_i"][m] - s["arr_i"][m]]),
            ("post-match lottery", np.r_[s["ready_f"][m] - s["det_f"][m], s["ready_i"][m] - s["det_i"][m]]),
            ("registry bundle wait", np.r_[s["reg_f"][m] - s["ready_f"][m], s["reg_i"][m] - s["ready_i"][m]]),
            ("registry posting wait", s["posted"][m] - s["intake"][m]),
            ("capture to finalization", s["final"][m] - s["t0"][m])):
        _stage(st, name, v)
    delay, path = {}, {}
    for k, e in enumerate((cr, ca, cb)):
        _stage(delay, AT.PTYPES[k], s["posted"][m] - ts[e[:, 0]])
    # from the packet's departure to its arrival at its destination (C, F or I), network time included
    for k, arr in enumerate((s["arr_c"][m], s["arr_f"][m], s["arr_i"][m])):
        _stage(path, AT.PTYPES[k], arr - ts[(cr, ca, cb)[k][:, 0]])
    fin = s["final"][m] - s["t0"][m]
    return dict(real_in_flight=real, decoys_in_flight=dec, unfinalized=unfinalized, introduced=int(window.sum()),
                board=int(board.sum()), confirmations=int(board.size),
                f_path=int(f_path.sum()), records=int(m.sum()), stages=st, packet_delay=delay, path_delay=path,
                latency_hist=np.histogram(fin, bins=np.arange(0, 3 * 3600 + 10, 10))[0])


# --------------------------------------------------------------------------- worker
_W = {}


def worker(out, name, R, run_id, D):
    """One run of one cell: simulate once, score every vantage, the shuffle and the diagnostics."""
    mp = model_path(out, name)
    if _W.get("model_key") != str(mp):
        with open(mp, "rb") as f:
            _W["models"] = pickle.load(f)
        _W["model_key"] = str(mp)
    cfg = config(name, R, D)
    t = time.time()
    run = S.simulate(cfg, traffic_seed(R, run_id))
    t_sim = time.time() - t
    rng = np.random.default_rng([SHUFFLE_SEED, list(CONFIGS).index(name), int(R), run_id])
    t = time.time()
    tables = AT.compute(run, _W["models"], rng)
    t_score = time.time() - t
    rec = dict(run=run_id, sim_seconds=t_sim, score_seconds=t_score, vantages=tables, stats=run_stats(run))
    if name == MAIN:
        t = time.time()
        rec["shuffle_test"] = AT.shuffle_test(run, _W["models"], rng, SHUFFLE_K)
        rec["test_seconds"] = time.time() - t
    return [(rec_name(name, R), rec)]


def tasks(out, name, runs, D, done=lambda name, R: set()):
    """Every run of one configuration not yet on disk, cells advancing together."""
    return [(str(out), name, R, k, D) for k in range(runs) for R in REAL_R if k not in done(name, R)]

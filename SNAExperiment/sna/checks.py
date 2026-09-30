"""Pre-run checks (ANALYSIS_PLAN.md section 4). Every check's outcome is written to
results/checks.json and reported, pass or fail.

1. Padding classes: every leg's wire size lies in its class; every raw payload fits its class; the
   Ring V signature measured with real keys has the size the leg table assumes.
2. Answer extraction: with background traffic on, the registry submissions a passive observer
   extracts are exactly the true ones, and its device candidates hold every device and decoy
   first-hop packet and no background packet. The share of submission groups that hold one
   capture only is reported.
3. Background independence: every vantage's and baseline's decisions are identical with background
   traffic on and off (so sweeps may run without it).
4. Decoys, cannot tell: for every vantage, every feature it observes has an AUC for real against
   decoy whose adjusted interval covers 0.5. Decoys run the same code path as real transactions,
   so this is expected to pass by construction; the check confirms nothing in the simulator
   separates them.
5. Decoys reach the registry: every decoy transaction reaches quorum and produces a registry
   record, as every real one does.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.stats import norm

from . import analyze as AN
from . import attacks as AT
from . import cells as CE
from . import params as P
from . import ring_sig
from . import sim as S
from .pools import Pools

CHECK_SEED0 = 3_000_000_000
LEG_CLASS = {S.GK1: "GK", S.GK2: "GK", S.GK3: "GK"}


def _auc_features(feats, decoy, run_id, n_tests):
    z = float(norm.ppf(1 - 0.05 / max(n_tests, 1) / 2))
    out = {}
    for name, x in feats.items():
        ok = np.isfinite(x)
        a = AN.auc_clustered(x[ok], (~decoy[ok]).astype(int), run_id[ok])
        lo, hi = a["auc"] - z * a["se"], a["auc"] + z * a["se"]
        out[name] = dict(auc=a["auc"], lo=lo, hi=hi, covers_half=bool(lo <= 0.5 <= hi),
                         n_real=int((ok & ~decoy).sum()), n_decoy=int((ok & decoy).sum()))
    return out


def _prev_gap(src, t):
    """Time since the same source's previous capture, per transaction."""
    o = np.lexsort((t, src))
    gap = np.full(t.size, np.nan)
    same = src[o][1:] == src[o][:-1]
    g = np.diff(t[o])
    gap[o[1:][same]] = g[same]
    return gap


def features(run):
    ev, s = run.events, run.subs
    ts, ta, sz = ev["t_send"], ev["t_arr"], ev["size"].astype(float)
    cr, ca, cb = s["ev_cred"], s["ev_ca"], s["ev_cb"]
    first_dep = np.stack([ts[cr[:, 0]], ts[ca[:, 0]], ts[cb[:, 0]]], 1)
    src_gap = _prev_gap(s["src"], first_dep.min(1))
    wire = {
        "Cred-1 size": sz[cr[:, 0]], "Cred-2 size": sz[cr[:, 1]], "Cred-3 size": sz[cr[:, 2]],
        "ContA-1 size": sz[ca[:, 0]], "ContA-3 size": sz[ca[:, 2]], "ContB-1 size": sz[cb[:, 0]],
        "CV-1 size": sz[s["ev_cv1"]], "CV-2 size": sz[s["ev_cv2"]], "GK leg size (mean of 3)": sz[s["ev_gk"]].mean(1),
        "C: Cred-3 arrival to CV-1 send": ts[s["ev_cv1"]] - ta[cr[:, 2]],
        "V: CV-1 arrival to CV-2 send": ts[s["ev_cv2"]] - ta[s["ev_cv1"]],
        "C: CV-2 arrival to first GK send": ts[s["ev_gk"]].min(1) - ta[s["ev_cv2"]],
        "C: GK send spread": ts[s["ev_gk"]].max(1) - ts[s["ev_gk"]].min(1),
        "source: spread of its three first-hop sends": first_dep.max(1) - first_dep.min(1),
        "source: time since its previous capture": src_gap,
        "A: hold": ts[cr[:, 1]] - ta[cr[:, 0]], "B: hold": ts[cr[:, 2]] - ta[cr[:, 1]],
        "D: hold": ts[ca[:, 1]] - ta[ca[:, 0]], "E: hold": ts[ca[:, 2]] - ta[ca[:, 1]],
    }
    first_cred = {k: wire[k] for k in ("Cred-1 size", "A: hold", "source: time since its previous capture")}
    first_cont = {"Content first-hop size": np.r_[sz[ca[:, 0]], sz[cb[:, 0]]],
                  "hold at the first hop": np.r_[ts[ca[:, 1]] - ta[ca[:, 0]], ts[cb[:, 1]] - ta[cb[:, 0]]],
                  "source: time since its previous capture": np.r_[src_gap, src_gap]}
    arr = np.r_[s["arr_f"], s["arr_i"]]
    content = {"Content last-leg size": np.r_[sz[ca[:, 2]], sz[cb[:, 2]]],
               "arrival to first board check": np.r_[s["hold_f"], s["hold_i"]] - arr}
    gk = {"GK arrival to board posting": (s["posts"] - s["gk_arr"]).ravel()}
    vgap = _prev_gap(s["src"], ta[s["ev_cv1"]])
    validator = {"CV-1 arrival to CV-2 send": ts[s["ev_cv2"]] - ta[s["ev_cv1"]],
                 "time since the same credential's previous request": vgap,
                 "CV-1 size": sz[s["ev_cv1"]]}
    cred = {"Cred-3 arrival to CV-1 send": ts[s["ev_cv1"]] - ta[cr[:, 2]],
            "CV-2 arrival to first GK send": ts[s["ev_gk"]].min(1) - ta[s["ev_cv2"]],
            "GK send spread": ts[s["ev_gk"]].max(1) - ts[s["ev_gk"]].min(1),
            "CV-2 size": sz[s["ev_cv2"]], "Cred-3 size": sz[cr[:, 2]]}
    return dict(baseline=(wire, 1), first_hop_cred=(first_cred, 1), first_hop_content=(first_cont, 2),
                cred_processor=(cred, 1), content_server=(content, 2), validator=(validator, 1), gatekeeper=(gk, 3))


def run_checks(out=CE.RESULTS, runs=4, verbose=True):
    out = Path(out)
    pools = Pools()
    D = CE.calibrate(out)["D"]
    res = {}
    spec = dict(key="check", R=15.0, T=15.0 + P.DECOYS_IN_FLIGHT, decoys=True, control=False)
    cfg = CE.config_of(spec, D).with_(background_enabled=True, nonblending_enabled=True, measure_s=P.MEASURE_S)

    # 1. padding classes -------------------------------------------------------------------
    ov = pools.tls13_overhead
    run = S.simulate(cfg, CHECK_SEED0, pools)
    ev = run.events
    bm = (ev["kind"] == S.K_BIRTHMARK) & (ev["leg"] >= S.CRED1) & (ev["leg"] <= S.GK3)
    is_gk = np.isin(ev["leg"], [S.GK1, S.GK2, S.GK3])
    lo = np.where(is_gk, P.PAD_GK[0], P.PAD_MIN) + ov
    hi = np.where(is_gk, P.PAD_GK[1], P.PAD_MAX) + ov
    inside = (ev["size"] >= lo) & (ev["size"] <= hi)
    keys = [ring_sig.RingKey()]
    sig = ring_sig.sign(b"APPROVED", [k.pk for k in keys], 0, keys[0])
    ring_ok = ring_sig.verify(b"APPROVED", [k.pk for k in keys], sig)
    raw_fit = {k: dict(raw=v + (P.INDICATOR_BYTES if k == "CV-2" else 0),
                       class_min=P.PAD_GK[0] if k == "GK" else P.PAD_MIN)
               for k, v in P.RAW.items() if k != "Reg"}
    for v in raw_fit.values():
        v["fits"] = v["raw"] <= v["class_min"]
    scaling = [dict(ring_v_members=n, gk_raw=689 + ring_sig.size(n), fits_class=689 + ring_sig.size(n) <= P.PAD_GK[0],
                    within_class_max=689 + ring_sig.size(n) <= P.PAD_GK[1]) for n in range(1, 9)]
    res["padding"] = dict(
        legs_checked=int(bm.sum()), legs_outside_class=int((bm & ~inside).sum()),
        ring_v_signature_bytes=len(sig), ring_v_verifies=bool(ring_ok), ring_v_expected=P.RING_V_BYTES,
        raw_fits=raw_fit, ring_v_scaling_note=scaling,
        passed=bool((bm & ~inside).sum() == 0 and len(sig) == P.RING_V_BYTES and ring_ok
                    and all(v["fits"] for v in raw_fit.values())))

    # 2. answer extraction with background on ---------------------------------------------
    s = run.subs
    real = ~s["decoy"]
    col_t, col_sub, tc = AT.registry_answers(run, pools)
    expected = int(s["ok_f"].sum() + s["ok_i"].sum())            # decoys reach the registry too
    cand = AT.candidates(run, pools)
    mem = cand["msub"]
    first_hops = int(3 * s["t0"].size)                          # every capture's three first-hop packets
    found = int((mem >= 0).sum())
    bg_members = int(((cand["n"][:, None] > np.arange(3)[None, :]) & (mem < 0)).sum())
    res["answer_extraction"] = dict(
        registry_found=int(col_t.size), registry_expected=expected, registry_unlabelled=int((col_sub < 0).sum()),
        device_packets_found=found, device_packets_expected=first_hops, background_packets_in_candidates=bg_members,
        submission_groups=int(cand["t"].size), pure_group_share=float((cand["sub"] >= 0).mean()),
        passed=bool(col_t.size == expected and (col_sub < 0).sum() == 0 and ((tc >= 0).sum(1) == 2).all()
                    and found == first_hops and bg_members == 0))

    # 3. background independence --------------------------------------------------------
    CE.ensure_models(out, False, pools)
    import pickle
    with open(CE.model_path(out, False), "rb") as f:
        models = pickle.load(f)
    small = cfg.with_(measure_s=3600.0)
    on = AT.compute(S.simulate(small, CHECK_SEED0 + 1, pools), pools, models)
    off = AT.compute(S.simulate(small.with_(background_enabled=False, nonblending_enabled=False),
                                CHECK_SEED0 + 1, pools), pools, models)
    same = {}
    for v in AT.VANTAGES:
        same[v] = all(np.array_equal(on[v][k], off[v][k]) for k in
                      ("sub", "dev_v_correct", "dev_b_correct", "sub_v_correct", "sub_b_correct", "dev_top1"))
    res["background_independence"] = dict(identical=same, passed=bool(all(same.values())))

    # 4 and 5. decoys --------------------------------------------------------------------
    feats, decs, rids = {}, {}, {}
    for k in range(runs):
        rk = run if k == 0 else S.simulate(cfg, CHECK_SEED0 + 10 + k, pools)
        sk = rk.subs
        for name, (fd, rep) in features(rk).items():
            d = np.tile(sk["decoy"], rep)
            for fn, x in fd.items():
                feats.setdefault(name, {}).setdefault(fn, []).append(x)
            decs.setdefault(name, []).append(d)
            rids.setdefault(name, []).append(np.full(d.size, k))
    n_tests = sum(len(v) for v in feats.values())
    decoy_res = {}
    for name in feats:
        fd = {fn: np.concatenate(x) for fn, x in feats[name].items()}
        decoy_res[name] = _auc_features(fd, np.concatenate(decs[name]), np.concatenate(rids[name]), n_tests)
    cannot = {}
    for v in AT.VANTAGES:
        ok = all(f["covers_half"] for f in decoy_res[v].values())
        cannot[v] = dict(features=decoy_res[v], passed=bool(ok))
    res["decoys_cannot_tell"] = cannot
    s = run.subs
    res["decoys_reach_registry"] = dict(
        decoy_records=int((s["ok_f"] & s["ok_i"] & s["decoy"]).sum()), decoys=int(s["decoy"].sum()),
        real_records=int((s["ok_f"] & s["ok_i"] & ~s["decoy"]).sum()), real=int((~s["decoy"]).sum()),
        passed=bool((s["ok_f"] & s["ok_i"]).all()))
    res["n_feature_tests"] = n_tests
    res["runs"] = runs
    res["cell"] = dict(R=15, decoys_in_flight=P.DECOYS_IN_FLIGHT, background=True)
    (out / "checks.json").write_text(json.dumps(res, indent=1, default=_json))
    if verbose:
        print_checks(res)
    return res


def _json(x):
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, np.bool_):
        return bool(x)
    raise TypeError(type(x))


def print_checks(res):
    def mark(b):
        return "PASS" if b else "FAIL"
    p = res["padding"]
    print(f"[{mark(p['passed'])}] padding classes: {p['legs_checked']} legs, {p['legs_outside_class']} outside class; "
          f"Ring V signature {p['ring_v_signature_bytes']} B (verifies: {p['ring_v_verifies']})")
    a = res["answer_extraction"]
    print(f"[{mark(a['passed'])}] answer extraction: registry {a['registry_found']}/{a['registry_expected']}, "
          f"device packets {a['device_packets_found']}/{a['device_packets_expected']}, "
          f"background packets among candidates {a['background_packets_in_candidates']}; "
          f"{a['pure_group_share']:.1%} of submission groups hold one capture")
    b = res["background_independence"]
    print(f"[{mark(b['passed'])}] background independence: " + ", ".join(f"{k} {v}" for k, v in b["identical"].items()))
    for v, r in res["decoys_cannot_tell"].items():
        worst = max(r["features"].items(), key=lambda kv: abs(kv[1]["auc"] - 0.5))
        print(f"[{mark(r['passed'])}] cannot tell decoys, {v}: {len(r['features'])} features, "
              f"largest |AUC - 0.5| {worst[0]} AUC {worst[1]['auc']:.3f} [{worst[1]['lo']:.3f}, {worst[1]['hi']:.3f}]")
    d = res["decoys_reach_registry"]
    print(f"[{mark(d['passed'])}] decoys reach the registry: {d['decoy_records']}/{d['decoys']} decoy and "
          f"{d['real_records']}/{d['real']} real transactions finalised")

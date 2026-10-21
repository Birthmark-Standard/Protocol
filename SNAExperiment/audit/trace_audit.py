"""Trace measurements for AUDIT.md. Reads the experiment code; changes nothing.

Run from SNAExperiment/:  python audit/trace_audit.py [out_dir]
Writes <out_dir>/trace_results.json (default audit/out). Run ids 50,000 and up are used by no result.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sna import attacks as AT, experiment as EX, lottery as LT, params as P, sim as S  # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "out"
OUT.mkdir(parents=True, exist_ok=True)
D = json.loads((Path(__file__).resolve().parent.parent / "results" / "calibration.json").read_text())["D"]
RUN0, RUNS, R = 50_000, 10, 20
res = {}


def stats(x):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    return dict(n=int(x.size), mean=float(x.mean()), sd=float(x.std()), min=float(x.min()), max=float(x.max()))


def corr(a, b):
    ok = np.isfinite(a) & np.isfinite(b)
    return float(np.corrcoef(a[ok], b[ok])[0, 1])


def tick_count(dur_from_first_tick, tick=P.TICK_S):
    return np.round(dur_from_first_tick / tick).astype(int) + 1


runs = []
for k in range(RUNS):
    cfg = EX.config_of(dict(R=float(R), decoys=60.0, build="internal_compromise"), D)
    runs.append((cfg, S.simulate(cfg, EX.traffic_seed(R, RUN0 + k)), S.World(cfg, EX.traffic_seed(R, RUN0 + k))))


def collect(fn):
    return np.concatenate([fn(cfg, run, w) for cfg, run, w in runs])


def scored(cfg, s):
    return (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s)


# ---------------------------------------------------------------- A. roles
def roles_check(overlap):
    out = dict(transactions=0, all_nine_distinct=0, cfi_in_gk=0, relay_is_gk=0, cross_path_coincidence=0,
               path_repeat=0, first_relays_repeat=0, dests_repeat=0)
    for k in range(RUNS):
        cfg = EX.config_of(dict(R=float(R), decoys=60.0, build="permitted_overlap" if overlap else "internal_compromise"), D)
        s = S.simulate(cfg, EX.traffic_seed(R, RUN0 + k)).subs
        gk = S.World(cfg, EX.traffic_seed(R, RUN0 + k)).gk_set
        rr = np.stack([s[x] for x in "ABCDEFGHI"], 1)
        out["transactions"] += len(rr)
        out["all_nine_distinct"] += int(sum(len(set(t)) == 9 for t in rr.tolist()))
        out["cfi_in_gk"] += int(np.isin(np.r_[s["C"], s["F"], s["I"]], gk).sum())
        out["relay_is_gk"] += int(np.isin(np.c_[s["A"], s["B"], s["D"], s["E"], s["G"], s["H"]], gk).any(1).sum())
        out["cross_path_coincidence"] += int(S.cross_path_overlap(s).sum())
        out["path_repeat"] += int(sum(((s[p[0]] == s[p[1]]) | (s[p[1]] == s[p[2]]) | (s[p[0]] == s[p[2]])).sum() for p in S.PATHS))
        out["first_relays_repeat"] += int(((s["A"] == s["D"]) | (s["A"] == s["G"]) | (s["D"] == s["G"])).sum())
        out["dests_repeat"] += int(((s["C"] == s["F"]) | (s["C"] == s["I"]) | (s["F"] == s["I"])).sum())
        out["gatekeepers"] = int(len(gk)); out["nodes"] = P.N_NODES
    return out


res["A_roles_overlap_false"] = roles_check(False)
res["A_roles_overlap_true"] = roles_check(True)


# ---------------------------------------------------------------- B. holds
def dev_holds(cfg, run, w):
    s, ev = run.subs, run.events
    m = scored(cfg, s)
    ts = ev["t_send"]
    return np.c_[ts[s["ev_cred"][m, 0]] - s["t0"][m], ts[s["ev_ca"][m, 0]] - s["t0"][m], ts[s["ev_cb"][m, 0]] - s["t0"][m],
                 ts[s["ev_ca"][m, 0]], ts[s["ev_cb"][m, 0]]]


d = collect(dev_holds)
res["B2_device"] = dict(credential=stats(d[:, 0]), content_F=stats(d[:, 1]), content_I=stats(d[:, 2]),
                        corr_F_I_hold=corr(d[:, 1], d[:, 2]), corr_cred_F_hold=corr(d[:, 0], d[:, 1]),
                        corr_F_I_release_time=corr(d[:, 3], d[:, 4]),
                        share_F_I_same_release_within_1s=float((np.abs(d[:, 3] - d[:, 4]) < 1.0).mean()),
                        i_channel_default=P.Config().dev_content_i_mean)


def relay_holds(cfg, run, w):
    s, ev = run.subs, run.events
    m = scored(cfg, s)
    ts, ta, dst = ev["t_send"], ev["t_arr"], ev["dst"]
    rows = []
    for key in ("ev_cred", "ev_ca", "ev_cb"):
        e = s[key][m]
        for hop in (0, 1):
            node = dst[e[:, hop]]
            arr, rel = ta[e[:, hop]], ts[e[:, hop + 1]]
            ph = w.phase[node]
            first = LT.next_tick(arr, ph)
            k = tick_count(np.round(rel - first, 1))              # processing (<= 3 ms) is below the rounding
            off = np.mod(rel - ph, P.TICK_S)                       # release minus the node clock, mod 10 s
            rows.append(np.c_[np.full(len(arr), 2 * ["ev_cred", "ev_ca", "ev_cb"].index(key) + hop), rel - arr, k, off])
    return np.concatenate(rows)


r = collect(relay_holds)
hops = {0: "A", 1: "B", 2: "D", 3: "E", 4: "G", 5: "H"}
p120, K120 = LT.stage_lottery(120.0)
res["B3_relay"] = {hops[h]: stats(r[r[:, 0] == h, 1]) for h in hops}
res["B3_relay_node_clock"] = dict(share_release_within_3ms_after_node_tick=float((r[:, 3] < 0.0031).mean()))
res["B1_lottery_relay"] = dict(p=p120, K=K120, share_k1=float((r[:, 2] == 1).mean()), max_k=int(r[:, 2].max()),
                               share_at_cap=float((r[:, 2] == K120).mean()),
                               expected_share_at_cap=float((1 - p120) ** (K120 - 1)))


def ab_pairs(cfg, run, w):
    s, ev = run.subs, run.events
    m = scored(cfg, s)
    ts, ta = ev["t_send"], ev["t_arr"]
    e = s["ev_cred"][m]
    return np.c_[ts[e[:, 1]] - ta[e[:, 0]], ts[e[:, 2]] - ta[e[:, 1]]]


ab = collect(ab_pairs)
res["B3_relay_independence"] = dict(corr_A_hold_B_hold_same_packet=corr(ab[:, 0], ab[:, 1]))


def c_v_fanout(cfg, run, w):
    s, ev = run.subs, run.events
    m = scored(cfg, s)
    ts, ta = ev["t_send"], ev["t_arr"]
    fan = s["gk_send"][m] - s["cv2_a"][m][:, None]
    same_tick = (np.abs(np.diff(np.sort(s["gk_send"][m], 1), axis=1)) < 0.01).any(1)
    return np.c_[s["cv1_s"][m] - s["arr_c"][m], ts[s["ev_cv2"][m]] - ta[s["ev_cv1"][m]], fan, same_tick]


c = collect(c_v_fanout)
res["B4"] = dict(C_before_CV1=stats(c[:, 0]), V_before_CV2_incl_validator_processing=stats(c[:, 1]),
                 fanout_leg1=stats(c[:, 2]), fanout_leg2=stats(c[:, 3]), fanout_leg3=stats(c[:, 4]),
                 corr_leg1_leg2=corr(c[:, 2], c[:, 3]), corr_leg1_leg3=corr(c[:, 2], c[:, 4]),
                 share_two_or_more_legs_within_10ms=float(c[:, 5].mean()))


def fi(cfg, run, w):
    s = run.subs
    m = scored(cfg, s) & s["ok_f"] & s["ok_i"]
    return np.c_[s["hold_f"][m] - s["arr_f"][m], s["hold_i"][m] - s["arr_i"][m], s["ready_f"][m] - s["det_f"][m],
                 s["ready_i"][m] - s["det_i"][m], s["reg_f"][m] - s["ready_f"][m], s["reg_i"][m] - s["ready_i"][m],
                 np.abs(s["ready_f"][m] - s["ready_i"][m]) <= 5.0, np.abs(s["reg_f"][m] - s["reg_i"][m]) <= 5.0,
                 s["det_f"][m] - np.maximum(s["hold_f"][m], s["known_f"][m]), s["known_f"][m] - s["quorum"][m],
                 np.mod(s["reg_f"][m] - w.reg_phase, P.REG_BUNDLE_S)]


f = collect(fi)
res["B5"] = dict(F_prematch=stats(f[:, 0]), I_prematch=stats(f[:, 1]), corr_F_I_prematch=corr(f[:, 0], f[:, 1]),
                 F_postmatch=stats(f[:, 2]), I_postmatch=stats(f[:, 3]), corr_F_I_postmatch=corr(f[:, 2], f[:, 3]),
                 share_F_I_within_5s_before_registry_bundle=float(f[:, 6].mean()),
                 share_F_I_within_5s_as_they_leave=float(f[:, 7].mean()))
res["B6_registry"] = dict(wait=stats(f[:, 4]), wait_I=stats(f[:, 5]),
                          share_departures_within_3ms_after_shared_boundary=float((f[:, 10] < 0.0031).mean()))
res["D2"] = dict(max_abs_det_minus_max_hold_known=float(np.nanmax(np.abs(f[:, 8]))), board_push_wait=stats(f[:, 9]))


def gk(cfg, run, w):
    s = run.subs
    m = scored(cfg, s)
    out = []
    for j, g in enumerate(run.gk_set):
        hold = s["gk_release"][m, j] - s["gk_arr"][m, j]
        ph = run.bundle_phase[g]
        first = ph + P.BUNDLE_S * np.ceil((s["gk_release"][m, j] - ph) / P.BUNDLE_S)
        dep = s["posts"][m, j]
        kb = np.round((dep - first) / P.BUNDLE_S).astype(int) + 1
        off = np.mod(dep - ph, P.BUNDLE_S)
        out.append(np.c_[hold, dep - s["gk_release"][m, j], kb, off])
    return np.concatenate(out)


g = collect(gk)
res["B6_gatekeeper"] = dict(hold=stats(g[:, 0]), bundling_wait=stats(g[:, 1]),
                            share_board_at_first_boundary=float((g[:, 2] == 1).mean()),
                            boarding_rate_per_boundary_given_reached=[float((g[:, 2] == b).sum() / (g[:, 2] >= b).sum())
                                                                     for b in range(1, 13)],
                            max_boundary=int(g[:, 2].max()),
                            share_departures_within_3ms_after_own_boundary=float((g[:, 3] < 0.0031).mean()))


# ---------------------------------------------------------------- B7. delays outside the hold table
def extra(cfg, run, w):
    s, ev = run.subs, run.events
    m = scored(cfg, s)
    leg = ev["leg"]
    lat = ev["t_arr"] - ev["t_send"]
    return lat[(leg >= 1) & (leg <= 15)]


res["B7_link_latency_per_leg"] = stats(collect(extra))
res["B7_parameters"] = dict(processing_ms=P.PROC_MS, validator_processing_ms=P.VALIDATOR_PROC_MS,
                            gatekeeper_processing_ms=P.GATEKEEPER_PROC_MS, gossip_validate_ms=P.GOSSIP_VALIDATE_MS,
                            latency_external_ms=P.LAT_EXT_MS, latency_internal_ms=P.LAT_INT_MS, jitter_ms=P.JITTER_MS,
                            board_push_s=P.BOARD_PUSH_S, quorum_timeout_s=P.QUORUM_TIMEOUT_S)
res["B7_quorum_timeouts"] = int(sum((~run.subs["ok_f"] | ~run.subs["ok_i"]).sum() for _, run, _ in runs))


# ---------------------------------------------------------------- C. padding
def sizes(cfg, run, w):
    ev = run.events
    return np.c_[ev["leg"], ev["size"], ev["rtype"]]


z = collect(sizes)
legs = {}
for code, name in S.LEG_NAMES.items():
    x = z[z[:, 0] == code]
    if len(x):
        pl = x[:, 1] - P.TLS13_OVERHEAD
        cls = (820, 860) if name.startswith("GK") else (420, 460)
        counts = np.bincount((pl - cls[0]).clip(0), minlength=cls[1] - cls[0] + 1) if name not in ("Reg-F", "Reg-I", "Reg relay") else None
        legs[name] = dict(n=int(len(x)), wire_min=int(x[:, 1].min()), wire_max=int(x[:, 1].max()),
                          payload_min=int(pl.min()), payload_max=int(pl.max()),
                          chi2_uniform=(float(((counts - counts.mean()) ** 2 / counts.mean()).sum()) if counts is not None else None),
                          bins=(cls[1] - cls[0] + 1))
res["C_padding_by_leg"] = legs


# ---------------------------------------------------------------- D. record time
def rec_time(cfg, run, w):
    rec = AT.records(run)
    s = run.subs
    return rec["u"] - 0.5 * (s["reg_f"][rec["sub"]] + s["reg_i"][rec["sub"]])


res["D1_record_time_minus_true_midpoint"] = stats(collect(rec_time))


# ---------------------------------------------------------------- E. traffic
def inflight(cfg, run, w):
    s = run.subs
    t = np.linspace(cfg.warmup_s, cfg.warmup_s + cfg.measure_s, 200)
    fin = np.where(np.isfinite(s["final"]), s["final"], np.inf)
    real = [(((s["t0"] <= x) & (fin > x)) & ~s["decoy"]).sum() for x in t]
    dec = [(((s["t0"] <= x) & (fin > x)) & s["decoy"]).sum() for x in t]
    lat = (s["final"] - s["t0"])[scored(cfg, s) & ~s["decoy"]]
    return np.array([[np.mean(real), np.mean(dec), np.nanmean(lat), s["decoy"].sum(), (s["ok_f"] & s["ok_i"])[s["decoy"]].mean()]])


e = collect(inflight)
res["E"] = dict(real_in_flight=float(e[:, 0].mean()), decoys_in_flight=float(e[:, 1].mean()),
                capture_to_finalization_mean=float(e[:, 2].mean()), decoy_share_finalized=float(e[:, 4].mean()),
                R=R, runs=RUNS)

# ---------------------------------------------------------------- G. candidates
def cands(cfg, run, w):
    cand = AT.candidates(run)
    s = run.subs
    pure = cand["sub"] >= 0
    full = pure & (cand["n"] == 3)
    real_subs = np.nonzero(scored(cfg, s))[0]
    got = np.isin(real_subs, cand["sub"][full])
    return np.array([[pure.mean(), full.mean(), got.mean(), np.unique(cand["dev"]).size,
                      len(np.unique(s["src"]))]])


g2 = collect(cands)
res["G1_candidates"] = dict(share_groups_one_capture=float(g2[:, 0].mean()),
                            share_groups_one_capture_all_three_packets=float(g2[:, 1].mean()),
                            share_scored_captures_with_a_whole_group=float(g2[:, 2].mean()),
                            sources_in_candidates=float(g2[:, 3].mean()), sources_in_truth=float(g2[:, 4].mean()))

# ---------------------------------------------------------------- which clock each hold releases on
def clocks(cfg, run, w):
    s = run.subs
    m = scored(cfg, s) & s["ok_f"] & s["ok_i"]
    off = lambda t, ph: np.mod(t - ph, P.TICK_S)  # noqa: E731
    pre = off(s["hold_f"][m], w.phase[s["F"][m]])                       # F pre-match hold, F's node clock
    post = off(s["ready_f"][m], w.phase[s["F"][m]])                     # F post-match lottery, F's node clock
    gk_node = off(s["gk_release"][m, 0], w.phase[run.gk_set[0]])        # gatekeeper hold against its node clock
    gk_own = off(s["gk_release"][m, 0], w.gk_phase[run.gk_set[0]])      # against its separate hold clock
    v_own = off(s["cv2_s"][m], w.v_phase)
    return np.c_[pre < 1e-6, post < 1e-6, gk_node < 1e-6, gk_own < 1e-6, v_own < 1e-6]


ck = collect(clocks)
res["B_clocks_share_on_tick"] = dict(F_prematch_on_F_node_clock=float(ck[:, 0].mean()),
                                     F_postmatch_on_F_node_clock=float(ck[:, 1].mean()),
                                     gatekeeper_hold_on_its_node_clock=float(ck[:, 2].mean()),
                                     gatekeeper_hold_on_its_own_hold_clock=float(ck[:, 3].mean()),
                                     validator_hold_on_its_clock=float(ck[:, 4].mean()))

(OUT / "trace_results.json").write_text(json.dumps(res, indent=1, default=float))
print(json.dumps(res, indent=1, default=float))

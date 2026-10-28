"""Fast tests: python -m pytest tests -q"""
import gzip
import pickle

import numpy as np

from sna import attacks as AT
from sna import experiment as EX
from sna import lottery as LT
from sna import params as P
from sna import runner as RN
from sna import sim as S

SMALL = P.Config(real_rate=0.04, decoy_rate=0.1, measure_s=1800.0)


def test_same_seed_same_trace():
    a, b = S.simulate(SMALL, 11), S.simulate(SMALL, 11)
    for k in a.events:
        assert np.array_equal(a.events[k], b.events[k])


def test_real_traffic_unchanged_by_decoys():
    base = S.simulate(SMALL.with_(decoy_rate=0.0), 12).subs
    s = S.simulate(SMALL, 12).subs
    real = ~s["decoy"]
    for k in ("t0", "C", "F", "I", "posts", "reg_f", "reg_i", "det_f", "src"):
        assert np.array_equal(base[k], s[k][real], equal_nan=True), k


def test_decoys_reach_the_registry():
    """A decoy is a genuine transaction: it reaches quorum and produces a record like a real one."""
    run = S.simulate(SMALL, 13)
    s = run.subs
    assert s["ok_f"][s["decoy"]].all() and s["ok_i"][s["decoy"]].all()
    assert np.isfinite(s["posted"][s["decoy"]]).all()


def test_fanout_is_serialized():
    """The three fan-out legs leave on distinct ticks of C's node clock, at least one tick apart."""
    run = S.simulate(SMALL, 19)
    s = run.subs
    send = np.sort(s["gk_send"], 1)
    assert (np.diff(send, axis=1) >= P.TICK_S - 0.01).all()
    off = np.mod(send - run.phase[s["C"]][:, None], P.TICK_S)
    assert ((off < 0.01) | (off > P.TICK_S - 0.01)).all()


def test_registry_posts_merged_record_on_its_schedule():
    """One record per transaction, posted at the first boundary of the registry's schedule after both
    submissions have reached every node; the record time is the posted time."""
    run = S.simulate(SMALL, 20)
    s = run.subs
    ok = np.isfinite(s["posted"])
    assert (ok == (s["ok_f"] & s["ok_i"])).all()
    assert (s["intake"][ok] >= np.fmax(s["reg_f"], s["reg_i"])[ok]).all()
    w = s["posted"][ok] - s["intake"][ok]
    assert (w >= 0).all() and (w < P.REG_POST_S).all()
    k = (s["posted"][ok] - run.post_phase) / P.REG_POST_S
    assert np.allclose(k, np.round(k))
    rec = AT.records(run)
    assert np.array_equal(rec["u"], s["posted"][rec["sub"]])


def test_every_device_packet_is_a_candidate():
    """No grouping: each of a capture's three first-hop packets is its own candidate."""
    run = S.simulate(SMALL, 21)
    cand = AT.candidates(run)
    cnt = np.bincount(cand["sub"][cand["sub"] >= 0])
    assert set(np.unique(cnt[cnt > 0])) == {3}
    assert (np.diff(cand["t"]) >= 0).all()


def test_role_rules():
    """With overlap off, the nine roles are distinct; C, F and I are never active gatekeepers."""
    s = S.simulate(SMALL.with_(overlap=False), 14).subs
    roles = np.stack([s[k] for k in "ABCDEFGHI"], 1)
    assert all(len(set(r)) == 9 for r in roles.tolist())
    gk = set(S.World(SMALL, 14).gk_set.tolist())
    assert not (set(s["C"]) | set(s["F"]) | set(s["I"])) & gk


def test_loader_skips_damaged_member(tmp_path):
    p = RN.raw_path(tmp_path, "x")
    p.parent.mkdir(parents=True)
    with gzip.open(p, "ab") as f:
        pickle.dump(dict(run=0), f)
    with open(p, "ab") as f:
        f.write(gzip.compress(pickle.dumps(dict(run=1)))[:-12])      # cut off mid-member
    with gzip.open(p, "ab") as f:
        pickle.dump(dict(run=2), f)
    assert sorted(r["run"] for r in RN.load(tmp_path, "x")) == [0, 2]


def test_seed_depends_on_volume_and_run_only():
    assert EX.traffic_seed(4, 7) == EX.traffic_seed(4.0, 7)
    assert EX.traffic_seed(4, 7) != EX.traffic_seed(8, 7)


def _small_scored(seed=15):
    m = AT.build_models(P.Config(), min_samples=3000, max_runs=3)
    run = S.simulate(SMALL.with_(measure_s=900.0), seed)
    return m, run, AT.compute(run, m, np.random.default_rng(seed))


VANT = {"observer", "observer_flat", "observer_mid", "observer_typed", "first_hop", "cred_processor", "gatekeeper", "combined",
        "content_server", "content_server_mid", "validator"}


def test_every_vantage_scores():
    """Every vantage runs end to end on a small run, with small models; every node is compromised in turn."""
    m, run, out = _small_scored()
    assert set(out) == VANT
    n = out["observer"]["sub"].size
    for v, r in out.items():
        assert r["sub"].size > 0 and r["dev_v_correct"].size == r["sub"].size, v
    assert out["first_hop"]["sub"].size == P.N_NODES * n and out["combined"]["sub"].size == P.N_NODES * n
    assert out["cred_processor"]["sub"].size == (P.N_NODES - P.N_GATEKEEPERS) * n
    assert out["gatekeeper"]["sub"].size == P.N_GATEKEEPERS * n and out["content_server"]["sub"].size == 2 * n


def test_flat_timing_keeps_the_feasible_set():
    """The observer with its timing evidence off scores the same candidates as the observer."""
    m, run, out = _small_scored()
    assert np.array_equal(out["observer_flat"]["dev_n_feas"], out["observer"]["dev_n_feas"])
    assert np.array_equal(out["observer_flat"]["dev_v_rand"], out["observer"]["dev_v_rand"])


def test_midpoint_record_time():
    """The midpoint diagnostic times each record at the midpoint of F's and I's registry submissions."""
    run = S.simulate(SMALL, 23)
    s = run.subs
    mid = AT.records(run, mid=True)
    assert np.allclose(mid["u"], 0.5 * (s["reg_f"] + s["reg_i"])[mid["sub"]])
    assert np.array_equal(mid["sub"], AT.records(run)["sub"])


def test_hits_by_packet_type_add_up():
    """The observer's submission-level hits by packet type sum to its submission-level hits."""
    m, run, out = _small_scored()
    o = out["observer"]
    assert set(np.unique(o["hit_type"])) <= {-1, 0, 1, 2}
    assert np.array_equal(o["hit_type"] >= 0, o["sub_v_correct"].astype(bool))
    assert (o["tfeas"].sum(1) <= o["sub_n_feas"]).all()


def test_board_share():
    """The share of F and I confirmations set by the match board, counted from the run's own fields."""
    run = S.simulate(SMALL, 25)
    st = EX.run_stats(run)
    s = run.subs
    m = AT.scored_mask(run, np.arange(s["t0"].size)) & s["ok_f"] & s["ok_i"]
    assert st["confirmations"] == 2 * m.sum()
    assert st["board"] == int((s["known_f"][m] >= s["hold_f"][m]).sum() + (s["known_i"][m] >= s["hold_i"][m]).sum())


def test_path_delay():
    """Departure to arrival at C, F or I: the two relay holds plus network time, for every packet type."""
    run = S.simulate(P.Config(real_rate=0.2, decoy_rate=0.0, measure_s=7200.0), 29)
    st = EX.run_stats(run)["path_delay"]
    for k in AT.PTYPES:
        n, sm, sq, mx = st[k]
        assert n > 100 and abs(sm / n - 360.0) < 25.0 and mx <= 180.0 + 900.0 + 1.0, k


def test_window_halves_and_candidates_outside_the_window():
    """The half-window flag splits the scored records at the window's midpoint, and the observer's candidates
    include packets from the warm-up and the cool-down."""
    m, run, out = _small_scored()
    s, cfg = run.subs, run.cfg
    o = out["observer"]
    t0 = s["t0"][o["sub"]]
    mid = cfg.warmup_s + cfg.measure_s / 2
    assert np.array_equal(o["half"].astype(bool), t0 >= mid)
    assert (t0 >= cfg.warmup_s).all() and (t0 < cfg.warmup_s + cfg.measure_s).all()
    cand = AT.candidates(run)
    assert cand["t"].min() < cfg.warmup_s and cand["t"].max() > cfg.warmup_s + cfg.measure_s


def test_decoy_identities_capture_at_the_real_device_rate():
    """In every cell of every configuration, a decoy identity captures at the rate of a real device, within 5%."""
    for name, D in (("main", 1170.0), ("no_holds", 20.5), ("first_relay_content", 10900.0), ("first_relay_f", 7550.0)):
        for R in EX.REAL_R:
            c = EX.config(name, R, D)
            real, dec = c.real_rate / c.real_devices, c.decoy_rate / c.decoy_sources
            assert abs(real / dec - 1) < 0.05, (name, R, real / dec)


def test_shuffle_test_is_exact():
    """The shuffle test's derived outcome for the scored permutation equals the scored outcome, and the
    shuffle changes neither the picks (beyond renaming) nor the feasible counts."""
    m = AT.build_models(P.Config(), min_samples=3000, max_runs=3)
    run = S.simulate(SMALL.with_(measure_s=900.0), 26)
    t = AT.shuffle_test(run, m, np.random.default_rng(3), K=20)
    assert t["shuffle_mismatch"] == 0 and t["nfeas_mismatch"] == 0 and t["scored_correct"] == t["correct"]
    assert abs(t["scored_chance"] - t["chance"]) < 1e-9


def test_in_flight_calibration():
    """Calibrated D gives R real and 100 decoy transactions in flight, each within 3%."""
    lg = EX.calibrate_longest(EX.MAIN, runs=10)
    win = EX.windows({EX.MAIN: lg}, EX.MAIN)
    assert win["warmup"] == lg + EX.MARGIN_S and win["window"] == EX.WINDOW_MAIN_S
    cal = EX.calibrate(EX.MAIN, win, runs=10)
    h = cal["history"][-1]
    assert cal["converged"]
    assert abs(h["real_in_flight"] / EX.CAL_R - 1) <= EX.TOLERANCE
    assert abs(h["decoys_in_flight"] / EX.DECOYS - 1) <= EX.TOLERANCE


def test_in_flight_counts_little():
    """Measured in flight equals arrivals per second times the mean delay (Little's law) on a long run."""
    D = 1100.0
    cfg = EX.config(EX.MAIN, 20, D)
    run = S.simulate(cfg, 27)
    real, dec = EX.in_flight(run)
    s = run.subs
    m = (s["t0"] >= cfg.warmup_s) & (s["t0"] < cfg.warmup_s + cfg.measure_s)
    dur = np.mean(EX.leaves(s)[m] - s["t0"][m])
    assert abs(real / (cfg.real_rate * dur) - 1) < 0.10 and abs(dec / (cfg.decoy_rate * dur) - 1) < 0.10


def test_content_server_waits_for_board_push():
    """A content server acts at the later of its hold release and the second board push carrying
    the match; it never acts on a board posting before the push reaches it."""
    s = S.simulate(SMALL, 17).subs
    for nm in ("f", "i"):
        ok = s[f"ok_{nm}"]
        assert (s[f"det_{nm}"][ok] >= s[f"hold_{nm}"][ok]).all()
        assert (s[f"det_{nm}"][ok] >= s["quorum"][ok]).all()


def test_relay_holds_follow_hop_position():
    """First relays hold for 60 s and second relays for 300 s on every path alike."""
    run = S.simulate(P.Config(real_rate=0.2, decoy_rate=0.0, measure_s=7200.0), 28)
    s, ev = run.subs, run.events
    ts, ta = ev["t_send"], ev["t_arr"]
    for key in ("ev_cred", "ev_ca", "ev_cb"):
        e = s[key]
        first, second = ts[e[:, 1]] - ta[e[:, 0]], ts[e[:, 2]] - ta[e[:, 1]]
        assert abs(first.mean() - 60.0) < 4.0 and first.max() <= 180.0 + 0.01, key
        assert abs(second.mean() - 300.0) < 15.0 and second.max() <= 900.0 + 0.01, key


def test_post_match_lottery_starts_at_confirmation():
    s = S.simulate(SMALL, 22).subs
    ok = s["ok_f"]
    wait = s["ready_f"][ok] - s["det_f"][ok]
    assert (wait >= 0).all() and (wait <= P.CAP_FACTOR * 30.0 + 1e-6).all()


def test_holds_meet_their_means_and_caps():
    """Every hold has its target mean and a cap at three times it; the inclusion lottery departs on
    a boundary of the gatekeeper's grid, at most 12 boundaries after the posting is ready."""
    rng = np.random.default_rng(7)
    t = rng.uniform(0, 1e6, 300_000)
    for m in (20.0, 30.0, 60.0, 120.0, 180.0, 240.0):
        h = LT.hold(rng, t, 3.0, m) - t
        assert abs(h.mean() - m) < 0.02 * m and h.max() <= 3 * m + 1e-6
    d = LT.inclusion_departure(rng, t, 7.0, 30.0, P.INCLUSION_P, P.INCLUSION_MAX)
    assert np.allclose((d - 7.0) / 30.0, np.round((d - 7.0) / 30.0))
    assert (d >= t).all() and (d - t <= 30.0 * P.INCLUSION_MAX + 1e-6).all()


def test_permitted_overlap_role_constraints():
    """Under permitted overlap: first relays pairwise distinct, destinations pairwise distinct and
    never gatekeepers, the three nodes of each path distinct; destinations and every other draw are
    the same as with overlap off; and some roles on different paths coincide."""
    on = S.simulate(SMALL.with_(overlap=True), 24).subs
    off = S.simulate(SMALL.with_(overlap=False), 24).subs
    gk = S.World(SMALL, 24).gk_set
    for p in S.PATHS:
        a, b, c = (on[k] for k in p)
        assert ((a != b) & (b != c) & (a != c)).all(), p
    assert ((on["A"] != on["D"]) & (on["A"] != on["G"]) & (on["D"] != on["G"])).all()
    assert ((on["C"] != on["F"]) & (on["C"] != on["I"]) & (on["F"] != on["I"])).all()
    assert not np.isin(np.r_[on["C"], on["F"], on["I"]], gk).any()
    for k in ("t0", "src", "C", "F", "I", "decoy"):
        assert np.array_equal(on[k], off[k]), k
    assert on["overlap"].any() and "overlap" not in off
    assert np.array_equal(on["overlap"], S.cross_path_overlap(on))
    C, F, I, A, B, D, E, G, H = S._roles(np.random.default_rng(3), 50_000, np.array([17, 18, 19]),
                                         rng_relays=np.random.default_rng(4))
    assert (A == F).any() and (D == C).any() and (B == E).any() and (E == I).any() and np.isin(B, [17, 18, 19]).any()


def test_loader_reads_resumed_file(tmp_path):
    """A member cut off mid-write (no trailer), then a resumed session's member, then another: every
    complete record in all three is read, and the cut member reads the same before and after the
    later members are appended."""
    import os
    p = RN.raw_path(tmp_path, "y")
    p.parent.mkdir(parents=True)
    blob = gzip.compress(b"".join(pickle.dumps(dict(run=k, pad=os.urandom(3000))) for k in range(5)))
    with open(p, "wb") as f:
        f.write(blob[: len(blob) * 2 // 3])                                   # interrupted session
    before = sorted(r["run"] for r in RN.load(tmp_path, "y"))
    with gzip.open(p, "ab") as f:
        for k in range(5, 8):
            pickle.dump(dict(run=k), f)
    with gzip.open(p, "ab") as f:
        pickle.dump(dict(run=8), f)
    after = sorted(r["run"] for r in RN.load(tmp_path, "y"))
    assert before and set(before) <= set(after)
    assert after == before + [5, 6, 7, 8]


# --------------------------------------------------------------------------- the observer told the packet type
def test_every_candidate_has_a_packet_type():
    """Every device packet on the wire, real or decoy, is a credential, F content or I content packet."""
    cand = AT.candidates(S.simulate(SMALL, 31))
    assert cand["ptype"].size > 0 and set(np.unique(cand["ptype"])) == {0, 1, 2}


def test_typed_densities_split_the_pooled_samples():
    """The three typed densities come from the pooled density's own samples, one third each, at its bin width."""
    m = AT.build_models(P.Config(), min_samples=3000, max_runs=3)
    g, gt = m.pdf["g"], m.pdf["g_type"]
    assert len(gt) == 3 and all(d.bw == g.bw for d in gt)
    assert all(g.support[0] <= d.support[0] and d.support[1] <= g.support[1] for d in gt)


def test_typed_with_the_pooled_density_is_the_observer():
    """With each typed density replaced by the pooled one, the typed observer is the observer, decision for decision."""
    import copy
    m = AT.build_models(P.Config(), min_samples=3000, max_runs=3)
    m2 = copy.deepcopy(m)
    m2.pdf["g_type"] = (m.pdf["g"],) * 3
    run = S.simulate(SMALL.with_(measure_s=900.0), 15)
    out = AT.compute(run, m2, np.random.default_rng(15))
    o, t = out["observer"], out["observer_typed"]
    for k in t:
        assert np.array_equal(o[k], t[k], equal_nan=o[k].dtype.kind == "f"), k


def test_typed_hits_by_packet_type_add_up():
    """The typed observer's submission-level hits by packet type sum to its submission-level hits."""
    m, run, out = _small_scored()
    t = out["observer_typed"]
    assert set(np.unique(t["hit_type"])) <= {-1, 0, 1, 2}
    assert np.array_equal(t["hit_type"] >= 0, t["sub_v_correct"].astype(bool))
    assert (t["tfeas"].sum(1) <= t["sub_n_feas"]).all()
    assert np.array_equal(t["dev_b_correct"], out["observer"]["dev_v_correct"])     # paired with the pooled observer


def test_typed_agrees_with_pooled_when_packets_leave_together():
    """With every hold off, a capture's three packets leave together, so the three types share one delay to the record
    and telling the observer the type changes almost no decision."""
    name = "no_holds"
    m = AT.build_models(P.Config(**EX.CONFIGS[name]), min_samples=20000, max_runs=20)
    run = S.simulate(EX.config(name, 20, 20.5).with_(measure_s=600.0), 100)
    out = AT.compute(run, m, np.random.default_rng(0))
    o, t = out["observer"]["dev_v_correct"], out["observer_typed"]["dev_v_correct"]
    assert o.size > 300 and (o != t).mean() <= 0.01


def test_typed_densities_inform_when_the_credential_path_sets_the_record():
    """When the credential path sets the record time, the credential packet leaves after its device hold and the
    content packets at capture, so each type's own density fits held-out true packets better than the pooled one."""
    name = "first_relay_cred"
    cfg = P.Config(**EX.CONFIGS[name])
    m = AT.build_models(cfg, min_samples=100000, max_runs=200)     # smaller models' 1 s bins are too noisy for the gap
    acc = {}
    for seed in (7, 8, 9):                                          # seeds outside the models' own
        AT._true_samples(S.simulate(cfg.with_(decoy_rate=0.0, real_rate=0.2), seed), acc)
    y, pt = np.concatenate(acc["y"]), np.concatenate(acc["ptype"])
    for k in range(3):
        lt, lg = m.pdf["g_type"][k](y[pt == k]), m.pdf["g"](y[pt == k])
        ok = np.isfinite(lt) & np.isfinite(lg)
        assert ok.mean() > 0.99 and (lt[ok] - lg[ok]).mean() > 0.0, AT.PTYPES[k]


def test_typed_beats_pooled_when_one_content_path_sets_the_record():
    """When the F content path sets the record time, the F packet carries the timing and the other two do not, so the
    observer told the type names the device more often than the pooled observer on the same records."""
    import json
    name = "first_relay_f"
    m = AT.build_models(P.Config(**EX.CONFIGS[name]), min_samples=20000, max_runs=20)
    info = json.loads((EX.RESULTS / "run_info.json").read_text())
    cfg = EX.config(name, 20, info["D"][name], info["windows"][name]).with_(measure_s=8000.0)
    o = t = 0
    for k in range(2):
        out = AT.compute(S.simulate(cfg, 300 + k), m, np.random.default_rng(k))
        o += int(out["observer"]["dev_v_correct"].sum())
        t += int(out["observer_typed"]["dev_v_correct"].sum())
    assert t > o + 3


def test_typed_diagnostic_moves_no_other_interval(tmp_path):
    """The typed observer's diagnostic draws from its own random generator: every other row, interval and statistic of
    the analysis is the same with and without the typed observer in the records."""
    import json
    from sna import report as RP
    m = AT.build_models(P.Config(), min_samples=3000, max_runs=3)
    name = "no_holds"
    for d in ("with", "without"):
        p = RN.raw_path(tmp_path / d, EX.rec_name(name, EX.REAL_R[0]))
        p.parent.mkdir(parents=True)
    for k in range(4):
        run = S.simulate(SMALL.with_(measure_s=900.0), 40 + k)
        rec = dict(run=k, sim_seconds=0.0, score_seconds=0.0, vantages=AT.compute(run, m, np.random.default_rng(k)),
                   stats=EX.run_stats(run))
        for d in ("with", "without"):
            r = dict(rec, vantages={v: x for v, x in rec["vantages"].items() if d == "with" or v != "observer_typed"})
            with gzip.open(RN.raw_path(tmp_path / d, EX.rec_name(name, EX.REAL_R[0])), "ab") as f:
                pickle.dump(r, f)
    a, b = RP.analyze_config(tmp_path / "with", name), RP.analyze_config(tmp_path / "without", name)
    typed = ("packet type revealed", "typed observer submission hit by packet type")
    assert any(d["kind"] in typed for d in a[2]) and not any(d["kind"] in typed for d in b[2])
    a = (a[0], a[1], [d for d in a[2] if d["kind"] not in typed], a[3])
    js = lambda x: json.dumps(x, sort_keys=True, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))  # noqa: E731
    assert js(a) == js(b)


def test_compare_r1_counts_differing_decisions(tmp_path):
    """compare_r1 compares every R = 1 decision of the vantages the earlier run scored, counts a row as
    differing when any of its columns differs, skips vantages only the new run has, and flags runs on one side only."""
    import compare_r1
    m, run, out = _small_scored()
    f = EX.rec_name("main", 1)

    def write(d, recs):
        p = RN.raw_path(tmp_path / d, f)
        p.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(p, "ab") as h:
            for r in recs:
                pickle.dump(r, h)
    old = {v: x for v, x in out.items() if v != "observer_typed"}
    write("old", [dict(run=0, vantages=old), dict(run=1, vantages=old)])
    write("same", [dict(run=0, vantages=out), dict(run=1, vantages=out)])
    res = compare_r1.compare(tmp_path / "old", tmp_path / "same")
    n = sum(int(x["sub"].size) for x in old.values()) * 2
    assert res["compared"] == n and res["differ"] == 0 and not res["incomplete"]
    bad = {v: {c: a.copy() for c, a in x.items()} for v, x in out.items()}
    bad["observer"]["dev_v_correct"][0] ^= 1
    bad["first_hop"]["dev_top1"][3] += 1.0
    write("bad", [dict(run=0, vantages=bad)])
    res = compare_r1.compare(tmp_path / "old", tmp_path / "bad")
    assert res["differ"] == 2 and res["dev_outcome_differ"] == 1 and res["incomplete"]

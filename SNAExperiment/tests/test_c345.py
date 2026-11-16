"""Fast checks of the C3 to C5 options and attackers. The C2 reproduction check is test_c2_r1_reproduction."""
import json
from pathlib import Path

import numpy as np
import pytest

from sna import attacks as AT
from sna import devscore as DS
from sna import experiment as EX
from sna import krecord as KR
from sna import params as P
from sna import sim as S
from sna import stronger as ST

D = 1168.2274123090758
ROOT = Path(__file__).resolve().parent.parent


def _cfg(R=1, hours=2.0, **kw):
    return P.Config(real_rate=R / D, decoy_rate=100 / D, measure_s=hours * 3600, warmup_len=2616.75, cooldown_len=2616.75, **kw)


def _same_run(a, b, skip=()):
    for k in a.events:
        assert np.array_equal(a.events[k], b.events[k], equal_nan=a.events[k].dtype.kind == "f"), k
    for k in a.subs:
        if k in skip:
            continue
        x, y = a.subs[k], b.subs[k]
        assert np.array_equal(x, y, equal_nan=x.dtype.kind == "f"), k


def test_c2_config_hash_unchanged():
    assert EX.config_hash() == "c54e444f07f27a7a"


def test_default_options_are_c2():
    """Every new option at its default, written out, gives the same run."""
    a = S.simulate(_cfg(), 3)
    b = S.simulate(_cfg(decoy_factor=1.0, workload="W0", edit_share=0.0, quorum_timeout_s=1800.0, board_window_s=0.0,
                        grid_off=False, mark_actor="", mark_target=-1, withhold_share=0.0, n_validators=1,
                        real_val_split=(), decoy_val_split=()), 3)
    _same_run(a, b)


def test_mark_of_zero_is_the_unmarked_run():
    a = S.simulate(_cfg(), 4)
    for actor in ("first_relay", "access", "access_one", "validator"):
        b = S.simulate(_cfg(mark_actor=actor, mark_delta=0.0, mark_target=0), 4)
        _same_run(a, b, skip=("marked", "mark_path"))
        assert b.subs["marked"].sum() > 0


def test_mark_delays_the_marked_path():
    a = S.simulate(_cfg(), 4)
    b = S.simulate(_cfg(mark_actor="validator", mark_delta=600.0, mark_target=0), 4)
    m = b.subs["marked"]
    assert np.allclose(b.subs["cv2_s"][m] - a.subs["cv2_s"][m], 600.0)
    assert np.allclose(b.subs["cv2_s"][~m], a.subs["cv2_s"][~m])


def test_drop_resubmits_on_a_fresh_transaction():
    run = S.simulate(_cfg(hours=6, mark_actor="access", mark_mode="drop", mark_target=0, resub_mean_s=1800.0), 5)
    s = run.subs
    d = np.nonzero(s["dropped"])[0]
    assert d.size and not np.isfinite(s["posted"][d]).any()
    kids = np.nonzero(s["parent"] >= 0)[0]
    assert set(s["parent"][kids]) <= set(d)
    assert np.all(s["t0"][kids] >= s["t0"][s["parent"][kids]] + P.RESUB_WAIT_S)
    assert np.all(s["src"][kids] == s["src"][s["parent"][kids]])


def test_concentration_identities():
    for f, n in ((1, 100), (5, 20), (25, 4)):
        assert _cfg(decoy_factor=f).decoy_sources == n


def test_edits_follow_their_parents():
    run = S.simulate(_cfg(hours=6, edit_share=0.3, edit_same_source=0.5), 6)
    s = run.subs
    e = np.nonzero(s["parent"] >= 0)[0]
    assert e.size
    assert np.all(s["t0"][e] >= s["posted"][s["parent"][e]] + P.EDIT_DELAY_MIN_S)
    other = s["src"][e] != s["src"][s["parent"][e]] % P.MACHINE_OFFSET
    assert 0.2 < other.mean() < 0.8


def test_first_relay_share_is_three_in_twenty():
    run = S.simulate(_cfg(R=100, hours=3), 7)
    s = run.subs
    share = np.mean([((s["A"] == x) | (s["D"] == x) | (s["G"] == x)).mean() for x in range(P.N_NODES)])
    assert abs(share - 3 / 20) < 0.005


def test_knowledge_of_nothing_is_c2(tmp_path):
    """Dropping no device gives the C2 tables."""
    run = S.simulate(_cfg(), 8)
    m = ST.models(tmp_path)
    a = AT.compute(run, m, np.random.default_rng(1))
    b = AT.compute(run, m, np.random.default_rng(1), drop_dev=[], drop_dev_validator=[])
    for v in a:
        for k in a[v]:
            assert np.array_equal(a[v][k], b[v][k], equal_nan=a[v][k].dtype.kind == "f"), (v, k)


def test_device_scores_reproduce_the_engine(tmp_path):
    """The device-score tables give the observer's own decisions, and K = 1 gives them too."""
    run = S.simulate(_cfg(), 9)
    m = ST.models(tmp_path)
    hk = ST._Hooks()
    tab = AT.compute(run, m, np.random.default_rng(2), vantages=("observer",), hooks=hk.dict())
    rec, n = tab["_rec"], tab["_rec"]["sub"].size
    labs, scs = KR.vectors(hk.col, n)
    t = DS.table(labs, scs, rec, np.arange(n), np.zeros(n), tab["_base"], rec["dev"], tab["_shuf"])
    assert np.array_equal(t["dev_v_correct"], tab["observer"]["dev_v_correct"])
    assert np.array_equal(t["dev_n_feas"], tab["observer"]["dev_n_feas"])
    for i in range(n):
        ok, _, _ = KR.decide([(labs[i], scs[i])], 1.0, rec["dev"][i])
        assert ok == bool(tab["observer"]["dev_v_correct"][i])


def test_ceiling_expectation():
    run = S.simulate(_cfg(R=100, hours=1), 10)
    rec = AT.records(run)
    keep = AT.scored_mask(run, rec["sub"])
    rec = {k: v[keep] for k, v in rec.items()}
    c = KR.ceiling(run, rec, np.random.default_rng(0))
    assert 0.03 < c["expected"].mean() < 0.08


def test_c2_r1_reproduction(tmp_path):
    """Two R = 1 runs of C2's main configuration, made now with default options, against C2's own raw files,
    decision by decision. Runs only where C2's raw files are and the versions are C2's."""
    info = json.loads((ROOT / "results" / "C2" / "run_info.json").read_text())
    raw = ROOT / "results" / "C2" / "raw"
    if not raw.exists():
        pytest.skip("results/C2/raw is not on this machine; run this test where C2 was made")
    if info.get("versions") != EX.versions():
        pytest.skip(f"versions differ from C2's ({info.get('versions')} against {EX.versions()}); decisions are compared "
                    "only on the same versions")
    import compare_r1
    from sna import runner as RN
    EX.ensure_models(tmp_path, EX.MAIN)
    RN.execute([(str(tmp_path), EX.MAIN, 1, k, info["D"][EX.MAIN], info["windows"][EX.MAIN]) for k in range(2)],
               EX.worker, tmp_path, 1, label="reproduction")
    res = compare_r1.compare(ROOT / "results" / "C2", tmp_path)
    assert res["compared"] > 0 and res["differ"] == 0


# --------------------------------------------------------------------------- tracer
def _small_problem(rng):
    from sna import lottery as LT
    from sna import tracer as TR
    nr = int(rng.integers(1, 8))
    first = rng.random(nr) < 0.4
    ta = np.sort(rng.uniform(0, 600, nr))
    leaves = first | (rng.random(nr) < 0.5)
    ts = np.sort(np.array([LT.hold(rng, np.array([ta[i]]), 3.0, 60.0 if first[i] else 300.0)[0] + 0.0017
                           for i in np.nonzero(leaves)[0]]))
    W = np.zeros((nr, ts.size))
    for pos, mean in ((True, 60.0), (False, 300.0)):
        sel = np.nonzero(first == pos)[0]
        r, c, w = TR.hold_pairs(ta[sel], ts, mean, (0, 0), TR.PROC)
        W[sel[r], c] = w
    return W, np.where(first, 0.0, 0.5)


def test_tracer_counts_small_pieces_exactly():
    from scipy import sparse
    from sna import tracer as TR
    rng = np.random.default_rng(11)
    n = 0
    while n < 60:
        W, skip = _small_problem(rng)
        if W.shape[1] == 0 or (W.sum(0) == 0).any():
            continue
        try:
            M, St = TR.brute_force(W, skip)
        except ZeroDivisionError:
            continue
        X, Sk = TR.Assoc(sparse.csr_matrix(W), skip).solve()
        assert np.abs(X.toarray() - M).max() < 1e-9 and np.abs(Sk - St).max() < 1e-9
        n += 1


def _gate(R, measure_s, seed, grid_off=True):
    """The tracer on a model seed, every hold off: with grid_off, every schedule off too (the gate)."""
    from sna import tracer as TR
    info = json.loads((ROOT / "results" / "C2" / "run_info.json").read_text())
    Dn, wn = info["D"]["no_holds"], info["windows"]["no_holds"]
    base = P.Config(**EX.CONFIGS["no_holds"]).with_(grid_off=grid_off)
    m = AT.build_models(base, seed0=EX.MODEL_SEED0, min_samples=60_000)
    cfg = base.with_(real_rate=R / Dn, decoy_rate=100 / Dn, measure_s=measure_s, warmup_len=wn["warmup"],
                     cooldown_len=wn["cooldown"])
    dens = TR.densities(cfg, EX.MODEL_SEED0, runs=4)
    run = S.simulate(cfg, EX.MODEL_SEED0 + 70_100 + seed)
    hk = ST._Hooks()
    tab = AT.compute(run, m, np.random.default_rng(seed), vantages=("observer",), hooks=hk.dict())
    t, _ = TR.score(run, m, dens, tab)
    return float(t["dev_v_correct"].mean()), int(t["sub"].size)


def test_tracer_gate_r1():
    acc, n = _gate(1, 9600.0, 0)
    assert n >= 300 and acc >= 0.990


def test_tracer_gate_r100():
    acc, n = _gate(100, 240.0, 0)
    assert n > 200 and acc >= 0.981


def test_joint_pair_sum_is_exact():
    """The prefix-sum sum over pairs of submissions equals the double loop."""
    from sna import tracer as TR
    rng = np.random.default_rng(0)
    for _ in range(100):
        F, R = int(rng.integers(2, 25)), int(rng.integers(1, 4))
        z, pk, lp = rng.integers(0, 4, F), rng.integers(0, 4, F), rng.normal(size=F)
        A = rng.random((R, F))
        S_ = np.cumsum(A, 1) - A - TR._group_prefix(A, z) - TR._group_prefix(A, pk) + TR._group_prefix(A, z * 5 + pk)
        fast = (A * S_ * np.exp(lp)[None, :]).sum(1)
        slow = np.zeros(R)
        for a in range(F):
            for b in range(a + 1, F):
                if z[a] != z[b] and pk[a] != pk[b]:
                    slow += A[:, a] * A[:, b] * np.exp(lp[b])
        assert np.allclose(fast, slow)


def test_tracer_schedule_likelihoods():
    """A bundled time's likelihood is the share of samples in the interval it closes; the posting window is flat."""
    from sna import tracer as TR
    r = np.random.default_rng(1).uniform(0, 300, 100_000)
    iv = TR.Interval(r, 120.0)
    assert abs(np.exp(iv(np.array([200.0])))[0] - 0.4) < 0.01
    w = TR.Window(120.0)
    assert w(np.array([0.0, 60.0, 120.0])).tolist() == [0.0, 0.0, 0.0] and np.isneginf(w(np.array([121.0])))[0]
    a = TR.Atom(np.r_[np.zeros(50), np.random.default_rng(2).uniform(0, 1, 50)])
    assert a(np.array([0.0]))[0] > a(np.array([0.002]))[0] + 5


# --------------------------------------------------------------------------- coalitions and withholding
def test_first_relay_with_its_content_destination_is_exact(tmp_path):
    from sna import coalition as CO
    run = S.simulate(_cfg(), 12)
    m = ST.models(tmp_path)
    ex = CO.build_extra(P.Config(), m.pdf["gV"], runs=3)
    tab = AT.compute(run, m, np.random.default_rng(3), vantages=("observer",), hooks=ST._Hooks().dict())
    pc = CO.path_coalitions(run, ex, tab)
    assert pc["dev_v_correct"][pc["path"] > 0].all()


def test_validator_withholding():
    kw = dict(mark_actor="validator_withhold", mark_target=0, withhold_share=1.0, withhold_len=1800.0)
    a = S.simulate(_cfg(hours=6), 13)
    d = S.simulate(_cfg(hours=6, withhold_mode="delay", **kw), 13)
    h = S.simulate(_cfg(hours=6, withhold_mode="withhold", **kw), 13)
    held = d.subs["withheld"]
    assert held.any() and not (held & (d.subs["src"] == 0) & ~d.subs["decoy"]).any()
    assert np.all(d.subs["cv2_s"][held] > a.subs["cv2_s"][held])
    assert np.allclose(d.subs["cv2_s"][~held], a.subs["cv2_s"][~held])
    assert not np.isfinite(h.subs["posted"][h.subs["withheld"]]).any()
    assert d.subs["marked"].sum() > 0


def test_several_validators():
    cfg = _cfg(R=100, hours=1, n_validators=3, real_val_split=(0.5, 0.3, 0.2), decoy_val_split=(0.4, 0.4, 0.2))
    run = S.simulate(cfg, 14)
    s, ev = run.subs, run.events
    # each identity keeps one key, and its legs go to that key's validator
    for src in np.unique(s["src"])[:50]:
        assert np.unique(s["val"][s["src"] == src]).size == 1
    assert np.array_equal(ev["dst"][s["ev_cv1"]], S.VAL + s["val"])
    assert np.array_equal(ev["src"][s["ev_cv2"]], S.VAL + s["val"])
    assert np.bincount(s["val"][~s["decoy"]], minlength=3).min() > 0


def test_each_validator_scores_only_its_own_replies(tmp_path):
    cfg = _cfg(R=100, hours=1, n_validators=2, real_val_split=(0.5, 0.5), decoy_val_split=(0.5, 0.5))
    run = S.simulate(cfg, 15)
    tab = AT.compute(run, ST.models(tmp_path), np.random.default_rng(4), vantages=("validator",))
    for k in (0, 1):
        t = tab[f"validator_{k}"]
        assert not t["dev_v_correct"][t["own"] == 0].any()       # a record of another key's device is never named



# --------------------------------------------------------------------------- same-role coalitions and compromised nodes
def _small(tmp_path):
    from sna import coalition as CO
    run = S.simulate(_cfg(R=100, hours=1.0), 21)
    m = ST.models(tmp_path)
    ex = CO.build_extra(P.Config(), m.pdf["gV"], runs=3)
    rx = CO.build_roles(P.Config(), m.pdf["g"], runs=3)
    tab = AT.compute(run, m, np.random.default_rng(3), vantages=("observer",), hooks=ST._Hooks().dict())
    return run, m, ex, rx, tab


def test_same_role_and_compromised_nodes(tmp_path):
    from sna import coalition as CO
    run, m, ex, rx, tab = _small(tmp_path)
    sr = CO.same_role(run, m, ex, rx, tab, 100, 0)
    n = tab["observer"]["sub"].size
    for k in CO.RELAY_SIZES:
        for r in ("first", "second"):
            t = sr[f"{r}_relays_{k}"]
            assert t["sub"].size == n and t["held"].min() >= 0 and t["held"].max() <= 3
    assert {"gatekeepers_2", "gatekeepers_3", "f_with_i"} <= set(sr)
    nodes = CO.compromised(run, m, ex, rx, tab, 100, 0)
    t = nodes["nodes_6"]
    exact = t["cls"] == 0
    assert exact.any() and t["dev_v_correct"][exact].all()       # a content path held at both ends names the device
    # a coalition of k nodes is drawn from the cell, the run and k, and is the same every time
    assert np.array_equal(CO._pick(100, 0, 3, 6, np.arange(20)), CO._pick(100, 0, 3, 6, np.arange(20)))


def test_node_classes_follow_the_roles():
    from sna import coalition as CO
    s = {x: np.array([v]) for x, v in zip("ABCDEFGHI", range(9))}
    cls, _ = CO.node_class(s, np.array([0]), np.array([3, 5]))       # D and F: the content path at both ends
    assert cls[0] == 0
    cls, _ = CO.node_class(s, np.array([0]), np.array([0, 2]))       # A and C
    assert cls[0] == 1
    cls, _ = CO.node_class(s, np.array([0]), np.array([4, 5]))       # E and F
    assert cls[0] == 2
    cls, _ = CO.node_class(s, np.array([0]), np.array([8]))          # I only
    assert cls[0] == 3
    cls, _ = CO.node_class(s, np.array([0]), np.array([1]))          # B only
    assert cls[0] == 4
    cls, _ = CO.node_class(s, np.array([0]), np.array([19]))
    assert cls[0] == 5


# --------------------------------------------------------------------------- spread of the posterior
def test_spread_terms_do_not_change_decisions(tmp_path):
    from sna import analyze as AN
    run = S.simulate(_cfg(R=100, hours=1.0), 22)
    m = ST.models(tmp_path)
    t = AT.compute(run, m, np.random.default_rng(4), vantages=("observer",))["observer"]
    c = t["dev_v_correct"].astype(bool)
    feas = np.isfinite(t["dev_s_true"])
    assert np.array_equal(c, feas & (t["dev_rank"] == 0) & (t["dev_top1"] == t["dev_s_true"]))
    H = t["dev_ent"].astype(float)
    assert np.nanmin(H) >= -1e-2 and np.all(H[t["dev_n_feas"] == 1] < 1e-2)
    assert np.all(H <= np.log(np.maximum(t["dev_n_feas"], 1))[:, None] + 1e-2)
    out = AN.metrics([dict(run=0, vantages=dict(observer=t)), dict(run=1, vantages=dict(observer=t))], "observer",
                     dict(R=100, T=200, key="x"), np.random.default_rng(0))
    assert out["top1"] == pytest.approx(out["dev_accuracy"]) and out["top1"] <= out["top5"] <= out["top10"]
    assert out["min_entropy_bits"] <= out["entropy_bits"] + 1e-6 and out["anonymity_set"] >= 1.0
    assert "miscalibrated" in out and "device_rate_max" in out


def test_entropy_of_a_posterior():
    W = np.array([[np.log(0.5), np.log(0.25), np.log(0.25), -np.inf]])
    assert AT._entropy(W, 1.0)[0] == pytest.approx(1.5 * np.log(2))


def test_k_record_full_decision_is_the_same():
    labs = [np.array([1, 2, 3]), np.array([1, 2])]
    scs = [np.array([0.0, -1.0, -2.0]), np.array([-0.5, 0.0])]
    base = KR.decide(list(zip(labs, scs)), 1.0, 1)
    full = KR.decide(list(zip(labs, scs)), 1.0, 1, full=True)
    assert full[:3] == base and full[3] >= 0 and full[5] <= full[4] + 1e-9


def test_c5_posterior_terms_and_tables(tmp_path):
    from sna import active as AC
    from sna import lottery as LT
    from sna import report345 as RP
    from sna import runner as RN
    import gzip, pickle
    cfg = _cfg(R=1, hours=3.0, mark_actor="validator", mark_delta=600.0, mark_target=0)
    recs = []
    for k in range(2):
        run = S.simulate(cfg, 40 + k)
        pdf = LT.EmpiricalLogPDF(AC.model_samples(run), 15.0)
        res = AC.score(run, pdf, np.random.default_rng(k), (cfg.warmup_s, cfg.warmup_s + cfg.measure_s))
        ok = res["correct"].astype(bool)
        assert np.all(res["dev_rank"][ok] == 0)
        recs.append(dict(run=k, marks=res, target=0, target_transactions=int(res["sub"].size)))
    (tmp_path / "raw").mkdir()
    with gzip.open(RN.raw_path(tmp_path, "c5__validator_d600_t1800__R1"), "wb") as f:
        for r in recs:
            pickle.dump(r, f)
    rows = RP.summarize_c5(tmp_path, ["c5__validator_d600_t1800__R1"])
    assert rows and "entropy_bits" in rows[0] and "calibration_error" in rows[0] and rows[0]["bound"] is not None
    md = RP.markdown(rows, "x")
    assert "Spread of the posterior" in md and "Reliability" in md


def test_calibration_flag_ignores_sampling_noise():
    from sna import analyze as AN
    rng = np.random.default_rng(5)
    conf = rng.uniform(0.02, 0.06, 600)
    hits = rng.random(600) < conf                                # calibrated: only sampling noise
    err = AN.reliability(conf, hits)[1]
    assert not AN.miscalibrated(err, hits.mean(), conf.mean(), AN.calibration_null(conf))
    bad = np.zeros(600, bool)                                    # confident and never right
    conf2 = np.full(600, 0.5)
    err2 = AN.reliability(conf2, bad)[1]
    assert AN.miscalibrated(err2, 0.0, 0.5, AN.calibration_null(conf2))



# --------------------------------------------------------------------------- seed sets
def test_evaluation_seeds_are_fresh_and_dry_runs_use_model_seeds(tmp_path):
    ev = {ST.eval_seed(R, k) for R in (1, 100, 300) for k in range(100)}
    c2 = {EX.traffic_seed(R, k) for R in (1, 100, 300) for k in range(100)}
    assert len(ev) == 300 and not ev & c2
    dry = {ST.dry_seed(R, k) for R in (1, 100, 300) for k in range(100)}
    assert len(dry) == 300 and min(dry) >= EX.MODEL_SEED0 + 300_000 and max(dry) < EX.MODEL_SEED0 + 1_000_000
    assert not dry & ev
    # a folder's run_info.json names its seed set, and every worker reads it
    (tmp_path / "run_info.json").write_text(json.dumps(dict(seed_set="model (dry run)")))
    assert ST.traffic(tmp_path, 100, 3) == ST.dry_seed(100, 3)
    other = tmp_path / "full"
    other.mkdir()
    assert ST.traffic(other, 100, 3) == ST.eval_seed(100, 3)


# --------------------------------------------------------------------------- several validators: withholding
def test_withholding_under_several_validators_is_the_targets_validator():
    cfg = _cfg(R=100, hours=2.0, mark_actor="validator_withhold", mark_target=0, withhold_mode="withhold",
               withhold_len=1800.0, **ST.VALIDATORS)
    run = S.simulate(cfg, 31)
    s = run.subs
    tv = s["val"][(s["src"] == 0) & ~s["decoy"]][0]
    held = s["withheld"]
    assert held.any() and np.all(s["val"][held] == tv)           # only its own identities' credentials are withheld
    assert not held[(s["src"] == 0) & ~s["decoy"]].any()           # never the target's own


def test_several_validators_job_tables(tmp_path):
    run = S.simulate(_cfg(R=100, hours=1.0, **ST.VALIDATORS), 32)
    tab = AT.compute(run, ST.models(tmp_path), np.random.default_rng(1), vantages=("observer", "validator", "cred_processor"))
    assert {"validator_0", "validator_1", "validator_2", "cred_processor_keyed"} <= set(tab)
    for k in range(3):
        assert not tab[f"validator_{k}"]["dev_v_correct"][tab[f"validator_{k}"]["own"] == 0].any()


# --------------------------------------------------------------------------- C6: blind-issued one-time certificates
def _otc(R=100, hours=2.0, **kw):
    from sna import onetime as OT
    return _cfg(R=R, hours=hours, candidate=OT.NAME, **ST.VALIDATORS, **kw)


def test_onetime_shares_captures_with_the_credential_path():
    from sna import onetime as OT
    a = S.simulate(_cfg(R=100, hours=2.0, **ST.VALIDATORS), 51)
    b = OT.simulate(_otc(), 51)
    for k in ("t0", "src", "decoy"):
        assert np.array_equal(a.subs[k][a.subs["gen"] == 0], b.subs[k][b.subs["gen"] == 0]), k
    # the issuer is the identity's validator draw
    assert np.array_equal(a.subs["val"][a.subs["gen"] == 0], b.subs["issuer"][b.subs["gen"] == 0])


def test_onetime_packet_route_and_record():
    from sna import onetime as OT
    run = OT.simulate(_otc(), 52)
    s, ev = run.subs, run.events
    assert np.all((s["A"] != s["B"]) & (s["A"] != s["D"]) & (s["B"] != s["D"]))
    e = s["ev_pk"]
    assert np.all(ev["src"][e[:, 0]] == S.EXT) and np.array_equal(ev["dst"][e[:, 2]], s["D"])
    ok = np.isfinite(s["posted"])
    assert ok.mean() > 0.9
    # a submission leaves on the shared 120 s schedule; the record posts on the 120 s schedule after its flood
    ph = run.reg_phase
    x = np.mod(s["reg"][ok] - ph, 120.0)
    assert np.all((x < 0.01) | (x > 119.99))
    assert np.all(s["posted"][ok] >= s["reach"][ok]) and np.all(s["posted"][ok] - s["reach"][ok] <= 120.0 + 1e-6)
    assert not any(k in s for k in ("ev_cred", "ev_cv1", "posts"))     # no C, validator or gatekeepers


def test_onetime_threshold_refills():
    from sna import onetime as OT
    run = OT.simulate(_otc(R=1, hours=24.0), 53)
    rf, s = run.refills, run.subs
    assert np.all(rf["n"] == 20)
    real = rf["src"] == 0
    caps = int(((s["src"] == 0) & (s["gen"] == 0)).sum())
    assert abs(real.sum() - caps / 20) <= 1.5                       # one refill per 20 captures
    assert np.array_equal(s["ready"], s["t0"])                       # nobody runs dry under the threshold rule
    # a refill fires at the time of a capture of the same identity
    for i, t in zip(rf["src"][:50], rf["t"][:50]):
        assert np.any((s["src"] == i) & (np.abs(s["t0"] - t) < 1e-9))


def test_random_refills_leave_every_other_vantage_unchanged():
    from sna import onetime as OT
    cfg = _otc(R=100, hours=2.0)
    a = OT.simulate(cfg, 57)
    b = OT.simulate(cfg.with_(otc_refill_rule="random"), 57)
    for k in ("t0", "src", "ready", "posted", "A", "B", "D"):
        assert np.array_equal(a.subs[k], b.subs[k], equal_nan=True), k
    rf = b.run_refills if hasattr(b, "run_refills") else b.refills
    caps = set(np.round(b.subs["t0"], 9))
    assert np.mean([round(t, 9) in caps for t in rf["t"]]) < 0.01     # refills are not at captures
    assert 1100 < b.stock_seen.mean() < 1400                          # about 1.25 x 3 per hour x 336 hours
    assert 6 <= a.stock_seen.min() and a.stock_seen.max() <= 25         # the threshold rule: 6 to 25 before a capture
    m = OT.build_models(cfg, seed0=EX.MODEL_SEED0 + 400_000, min_samples=20_000)
    out = OT.compute(b, m, np.random.default_rng(0))
    for k in range(3):                                                # the issuer adds nothing to the observer
        assert np.array_equal(out[f"issuer_{k}_with_observer"]["dev_v_correct"], out["observer"]["dev_v_correct"])


def test_long_run_rates_follow_the_workload():
    from sna import onetime as OT
    run = OT.simulate(_otc(R=100, hours=48.0, workload="W1"), 58)
    s = run.subs
    lam = []
    for i in np.unique(s["src"][~s["decoy"]])[:40]:
        lam.append(((s["src"] == i).sum() / run.cfg.horizon_s, run_lam(run, i)))
    a = np.array(lam)
    assert np.corrcoef(a[:, 0], a[:, 1])[0, 1] > 0.8


def run_lam(run, i):
    from sna import onetime as OT
    return OT.LAST_LAM.get(int(i), np.nan)


def test_c5_mark_longer_than_the_timeout_finds_nothing():
    from sna import active as AC
    cfg = _cfg(R=100, hours=1.0, mark_actor="validator", mark_delta=3600.0, mark_target=-2, quorum_timeout_s=1200.0)
    pdf, n = AC.build_model(cfg, [61])
    assert pdf is None and n == 0
    run = S.simulate(cfg.with_(mark_target=0), 62)
    res = AC.score(run, None, np.random.default_rng(0), (cfg.warmup_s, cfg.warmup_s + cfg.measure_s))
    assert not res["correct"].any()

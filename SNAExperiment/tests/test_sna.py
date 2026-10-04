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
    col_t, col_sub, tc = AT.registry_answers(run)
    assert ((tc >= 0).sum(1) == 2).all()


def test_role_rules():
    s = S.simulate(SMALL, 14).subs
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


def test_every_vantage_scores():
    """Every vantage runs end to end on a small run, with small models."""
    m = AT.build_models(P.Config(), min_samples=3000, max_runs=3)
    run = S.simulate(SMALL.with_(measure_s=900.0), 15)
    out = AT.compute(run, m, run_id=1)
    assert set(out) == set(AT.VANTAGES)
    for v, r in out.items():
        assert r["sub"].size > 0 and r["dev_v_correct"].size == r["sub"].size, v


def test_content_server_waits_for_board_push():
    """A content server acts at the later of its hold release and the second board push carrying
    the match; it never acts on a board posting before the push reaches it."""
    s = S.simulate(SMALL, 17).subs
    for nm in ("f", "i"):
        ok = s[f"ok_{nm}"]
        assert (s[f"det_{nm}"][ok] >= s[f"hold_{nm}"][ok]).all()
        assert (s[f"det_{nm}"][ok] >= s["quorum"][ok]).all()


def test_removing_a_mechanism_moves_only_its_stage():
    """Each mechanism draws on its own stream: removing it leaves everything before it unchanged."""
    a = S.simulate(SMALL, 18).subs
    b = S.simulate(SMALL.with_(post_match=False), 18).subs
    for k in ("t0", "posts", "det_f", "det_i", "hold_f"):
        assert np.array_equal(a[k], b[k], equal_nan=True), k
    c = S.simulate(SMALL.with_(reg_bundle_s=0.0), 18).subs
    for k in ("posts", "det_f", "ready_f"):
        assert np.array_equal(a[k], c[k], equal_nan=True), k
    ok = a["ok_f"]
    w = a["reg_f"][ok] - c["reg_f"][ok]
    assert (w > -0.01).all() and (w < P.REG_BUNDLE_S + 0.01).all()
    d = S.simulate(SMALL.with_(gk_inclusion=False), 18).subs
    for k in ("t0", "gk_release", "gk_arr", "C", "F", "I"):
        assert np.array_equal(a[k], d[k]), k


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
    for m in (30.0, 60.0, 120.0, 240.0):
        h = LT.hold(rng, t, 3.0, m) - t
        assert abs(h.mean() - m) < 0.02 * m and h.max() <= 3 * m + 1e-6
    d = LT.inclusion_departure(rng, t, 7.0, 30.0, P.INCLUSION_P, P.INCLUSION_MAX)
    assert np.allclose((d - 7.0) / 30.0, np.round((d - 7.0) / 30.0))
    assert (d >= t).all() and (d - t <= 30.0 * P.INCLUSION_MAX + 1e-6).all()

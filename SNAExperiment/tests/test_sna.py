"""Fast tests: python -m pytest tests -q"""
import gzip
import pickle

import numpy as np

from sna import attacks as AT
from sna import cells as CE
from sna import params as P
from sna import runner as RN
from sna import sim as S
from sna.pools import Pools

POOLS = Pools()
SMALL = P.Config(real_rate=0.04, decoy_rate=0.1, measure_s=1800.0, background_enabled=False,
                 nonblending_enabled=False)


def test_same_seed_same_trace():
    a, b = S.simulate(SMALL, 11, POOLS), S.simulate(SMALL, 11, POOLS)
    for k in a.events:
        assert np.array_equal(a.events[k], b.events[k])


def test_real_traffic_unchanged_by_decoys_and_background():
    base = S.simulate(SMALL.with_(decoy_rate=0.0), 12, POOLS).subs
    for cfg in (SMALL, SMALL.with_(background_enabled=True)):
        s = S.simulate(cfg, 12, POOLS).subs
        real = ~s["decoy"]
        for k in ("t0", "C", "F", "I", "posts", "reg_f", "reg_i", "det_f", "src"):
            assert np.array_equal(base[k], s[k][real], equal_nan=True), k


def test_decoys_reach_the_registry():
    """A decoy is a genuine transaction: it reaches quorum and produces a record like a real one."""
    run = S.simulate(SMALL, 13, POOLS)
    s = run.subs
    assert s["ok_f"][s["decoy"]].all() and s["ok_i"][s["decoy"]].all()
    col_t, col_sub, tc = AT.registry_answers(run, POOLS)
    assert ((tc >= 0).sum(1) == 2).all()


def test_role_rules():
    s = S.simulate(SMALL, 14, POOLS).subs
    roles = np.stack([s[k] for k in "ABCDEFGHI"], 1)
    assert all(len(set(r)) == 9 for r in roles.tolist())
    gk = set(S.World(SMALL, 14, POOLS).gk_set.tolist())
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


def test_seed_excludes_decoy_volume():
    assert CE.traffic_seed(4, 7) == CE.traffic_seed(4.0, 7)
    assert CE.traffic_seed(4, 7) != CE.traffic_seed(8, 7)


def test_every_vantage_scores():
    """Every vantage runs end to end on a small run, with small models."""
    m = AT.build_models(P.Config(), POOLS, min_samples=3000, max_runs=3)
    run = S.simulate(SMALL.with_(measure_s=900.0), 15, POOLS)
    out = AT.compute(run, POOLS, m, run_id=1)
    assert set(out) == set(AT.VANTAGES)
    for v, r in out.items():
        assert r["sub"].size > 0 and r["dev_v_correct"].size == r["sub"].size, v


def test_bundling_moves_only_postings():
    """Bundling on and off share every random draw: only postings and what follows them move."""
    a = S.simulate(SMALL, 16, POOLS).subs
    b = S.simulate(SMALL.with_(bundle_s=P.BUNDLE_S), 16, POOLS).subs
    for k in ("t0", "gk_release", "gk_arr", "C", "F", "I"):
        assert np.array_equal(a[k], b[k]), k
    shift = b["posts"] - a["posts"]
    assert (shift >= 0).all() and (shift < P.BUNDLE_S).all()


def test_content_server_waits_for_board_push():
    """A content server acts at the later of its hold release and the second board push carrying
    the match; it never acts on a board posting before the push reaches it."""
    run = S.simulate(SMALL, 17, POOLS)
    s = run.subs
    for nm in ("f", "i"):
        ok = s[f"ok_{nm}"]
        assert (s[f"det_{nm}"][ok] >= s[f"hold_{nm}"][ok]).all()
        assert (s[f"det_{nm}"][ok] >= s["quorum"][ok]).all()


def test_new_mechanisms_move_only_their_stage():
    """The two-point hold and registry bundling draw on their own streams: captures, relay legs and
    fan-out departures are unchanged; registry bundling moves only the submissions."""
    a = S.simulate(SMALL.with_(bundle_s=P.BUNDLE_S), 18, POOLS).subs
    b = S.simulate(SMALL.with_(bundle_s=P.BUNDLE_S, gk_twopoint=True), 18, POOLS).subs
    c = S.simulate(SMALL.with_(bundle_s=P.BUNDLE_S, gk_twopoint=True, reg_bundle_s=P.REG_BUNDLE_S), 18, POOLS).subs
    for k in ("t0", "gk_arr", "arr_f", "hold_f", "C", "F", "I"):
        assert np.array_equal(a[k], b[k]), k
    h = (b["gk_release"] - b["gk_arr"]).ravel()
    assert ((h < 0.02) | ((h > P.GK_CAP_S) & (h < P.GK_CAP_S + 0.02))).all()
    for k in ("posts", "det_f", "det_i", "gk_release"):
        assert np.array_equal(b[k], c[k], equal_nan=True), k
    ok = b["ok_f"]
    w = c["reg_f"][ok] - b["reg_f"][ok]
    assert (w > -0.01).all() and (w < P.REG_BUNDLE_S + 0.01).all()


def test_hold_scale_stretches_only_device_and_relay_holds():
    """A hold scale k stretches the lottery's mean and cap by k on its path only; the gatekeeper,
    credential processor and content server holds are unchanged in distribution."""
    from sna import lottery as LT
    rng = np.random.default_rng(5)
    t = rng.uniform(0, 1e6, 400_000)
    h1 = LT.release_time(rng, t, 3.0) - t
    h2 = LT.release_time(rng, t, 3.0, True, 2.0) - t
    assert abs(h2.mean() / h1.mean() - 2.0) < 0.05
    assert h2.max() <= P.TICK_S * P.MAX_TICKS * 2 + 1e-6
    assert abs((h2 > P.TICK_S * (P.MAX_TICKS * 2 - 1)).mean() - (h1 > P.TICK_S * (P.MAX_TICKS - 1)).mean()) < 0.01
    cfg = SMALL.with_(bundle_s=P.BUNDLE_S, content_hold_scale=2.0)
    s = S.simulate(cfg, 21, POOLS).subs
    assert cfg.warmup_s == 2 * P.WARMUP_S
    assert np.isfinite(s["reg_f"][s["ok_f"]]).all()


def test_post_match_lottery_starts_at_confirmation():
    """The post-match lottery starts when the server confirms quorum, never before, and draws on its
    own stream: everything up to confirmation is unchanged."""
    a = S.simulate(SMALL.with_(bundle_s=P.BUNDLE_S), 22, POOLS).subs
    b = S.simulate(SMALL.with_(bundle_s=P.BUNDLE_S, post_match=True), 22, POOLS).subs
    for k in ("t0", "posts", "det_f", "det_i", "hold_f"):
        assert np.array_equal(a[k], b[k], equal_nan=True), k
    ok = b["ok_f"]
    wait = b["ready_f"][ok] - b["det_f"][ok]
    assert (wait >= 0).all() and (wait <= P.TICK_S * (P.MAX_TICKS + 1)).all()

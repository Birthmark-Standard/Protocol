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
                        grid_off=False, mark_actor="", mark_target=-1), 3)
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

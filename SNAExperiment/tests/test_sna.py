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
        for k in ("t0", "C", "F", "I", "posts", "reg_f", "reg_i", "det_f"):
            assert np.array_equal(base[k], s[k][real], equal_nan=True), k


def test_decoys_never_reach_the_registry():
    run = S.simulate(SMALL, 13, POOLS)
    s = run.subs
    assert not s["ok_f"][s["decoy"]].any() and not s["ok_i"][s["decoy"]].any()
    col_t, col_sub, tc = AT.registry_answers(run, POOLS)
    assert not np.isin(col_sub, np.nonzero(s["decoy"])[0]).any()
    assert ((tc[~s["decoy"]] >= 0).sum(1) == 2).all()


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

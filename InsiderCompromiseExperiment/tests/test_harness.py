"""Checks on the extension tool (harness/): engine exactness, determinism, and the analysis code.

    python -m pytest -q tests/test_harness.py
"""
import math
import pickle

import numpy as np
import pytest
from scipy.optimize import linear_sum_assignment

import harness  # noqa: F401  (paths)
from harness import analyze as AN
from harness import engine as E
from harness import runner as RN
from harness import tool as TL


def _problem(seed, n=80, m=160):
    rng = np.random.default_rng(seed)
    anchor = np.sort(rng.uniform(0, 1000, n))
    col_t = np.sort(rng.uniform(0, 1100, m))
    vals = np.round(rng.normal(-5, 2, (n, m)), 1)          # ties, like binned densities
    width = 60.0

    def fn(r, c):
        d = col_t[c] - anchor[r]
        return np.where((d >= 0) & (d < width), vals[r, c], -np.inf)
    true_cols = rng.integers(0, m, (n, 1))
    return anchor, col_t, fn, width, true_cols, vals


def test_banded_scoring_equals_dense():
    anchor, col_t, fn, width, true_cols, _ = _problem(0)
    n, m = anchor.size, col_t.size
    res = E.score_rows(anchor, anchor + width, col_t, fn, true_cols)
    W = fn(np.repeat(np.arange(n), m), np.tile(np.arange(m), n)).reshape(n, m)
    srt = -np.sort(-W, axis=1)
    assert np.array_equal(res["top1"], srt[:, 0]) and np.array_equal(res["top2"], srt[:, 1])
    assert np.array_equal(res["n_feas"], np.isfinite(W).sum(1))
    st = W[np.arange(n), true_cols[:, 0]]
    rank = np.where(np.isfinite(st), 1 + (W > st[:, None]).sum(1), np.iinfo(np.int32).max)
    assert np.array_equal(res["rank"], rank)
    for i, T in enumerate(E.T_GRID):                      # stored as float16 offsets from top1 / T
        with np.errstate(divide="ignore"):
            lse = np.log(np.exp(W / T).sum(1))
        got = res["lse"][:, i].astype(float) + res["top1"] / T
        ok = np.isfinite(lse)
        assert np.allclose(got[ok], lse[ok], atol=2e-2)


def test_sparse_assignment_matches_dense_optimum():
    for seed in range(4):
        anchor, col_t, fn, width, true_cols, _ = _problem(seed)
        n, m = anchor.size, col_t.size
        res = E.score_rows(anchor, anchor + width, col_t, fn, true_cols, keep=10 ** 6)
        pick = E.joint_assign(n, res["edges"], np.zeros(n, int))
        W = fn(np.repeat(np.arange(n), m), np.tile(np.arange(m), n)).reshape(n, m)
        cost = np.where(np.isfinite(W), -W, 1e9)
        ri, ci = linear_sum_assignment(cost)
        ok = cost[ri, ci] < 1e9
        dense = (int(ok.sum()), round(float(W[ri[ok], ci[ok]].sum()), 6))
        got = pick >= 0
        sparse = (int(got.sum()), round(float(W[np.nonzero(got)[0], pick[got]].sum()), 6))
        assert dense == sparse


def test_clustered_auc_matches_brute_force():
    rng = np.random.default_rng(1)
    s = np.round(rng.normal(size=400), 1)
    y = (rng.random(400) < 0.3).astype(int)
    a = AN.auc_clustered(s, y, rng.integers(0, 20, 400))["auc"]
    pos, neg = s[y == 1], s[y == 0]
    brute = ((pos[:, None] > neg[None, :]).sum() + 0.5 * (pos[:, None] == neg[None, :]).sum()) / (pos.size * neg.size)
    assert math.isclose(a, brute, rel_tol=1e-12)


def test_wilson_interval():
    p, lo, hi = AN.wilson(10, 100)
    assert p == 0.1 and math.isclose(lo, 0.0552, abs_tol=1e-3) and math.isclose(hi, 0.1744, abs_tol=1e-3)


def test_results_do_not_depend_on_worker_count(tmp_path):
    """Same seed, one worker vs two: identical records (each run's seed depends only on its key)."""
    spec = TL.cell_spec(3, 4, ("N", "C", "F"), window=20.0)
    outs = {}
    for w in (1, 2):
        out = tmp_path / f"w{w}"
        TL.run_cells(out, [spec], 2, workers=w)
        outs[w] = {r["run"]: r for r in RN.load(out, f"{spec['key']}__F.full")}
    for k in (0, 1):
        a, b = outs[1][k], outs[2][k]
        for key in ("correct", "pred", "top1", "rank"):
            assert np.array_equal(a[key], b[key])


def test_loader_skips_a_damaged_member(tmp_path):
    """An interrupted session leaves a truncated gzip member; records before and after it survive."""
    import gzip
    p = tmp_path / "raw" / "x.pkl.gz"
    p.parent.mkdir()
    for runs in ((0, 1), (2,), (3, 4)):
        with gzip.open(p, "ab") as f:
            for k in runs:
                pickle.dump(dict(run=k, v=np.arange(50)), f)
    data = p.read_bytes()
    starts = [i for i in range(len(data)) if data.startswith(b"\x1f\x8b\x08", i)]
    cut = data[:starts[1]] + data[starts[1]:starts[2]][:20] + data[starts[2]:]   # truncate member 2
    p.write_bytes(cut)
    assert sorted(r["run"] for r in RN.load(tmp_path, "x")) == [0, 1, 3, 4]

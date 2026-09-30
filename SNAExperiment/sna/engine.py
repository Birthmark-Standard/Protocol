"""Banded scoring, per-decision statistics and joint assignment, shared by every vantage.

A vantage supplies, for every row (one item as one compromised server holds it):
  * a time window [t_lo, t_hi) on the answer times, outside which its likelihood is -inf
    (EmpiricalLogPDF returns -inf outside the Monte Carlo support, so the band loses nothing);
  * a score function w(rows, cols) -> log-likelihood, vectorised over flattened pairs;
  * the answer list's times (sorted) and the transaction each answer belongs to;
  * the server each row belongs to (joint assignment is solved per server).

The engine returns one record per scored row: the joint-assignment pick, the per-decision
(highest-score) pick, the top two scores, the true candidate's score and rank, the number of
feasible candidates, and log-sum-exp of the row's scores at a grid of temperatures, which is all
the confidence analysis needs (softmax at a grid temperature T is exp(s / T - LSE_T)). LSE_T is
stored as float16 offsets from top1 / T (always >= 0 and small, so float16 keeps 3 decimals).
"""
from __future__ import annotations

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import min_weight_full_bipartite_matching

T_GRID = np.exp(np.linspace(np.log(0.1), np.log(10.0), 21)).astype(np.float64)
K_ASSIGN = 64            # candidates per row kept for the joint assignment (checked against all)
CHUNK_CELLS = 4_000_000  # rows x band cells evaluated per chunk
_UNMATCHED = 1e6


def _lse(x, axis):
    m = np.max(x, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0.0)
    with np.errstate(divide="ignore"):
        return (np.log(np.sum(np.exp(x - m), axis=axis, keepdims=True)) + m).squeeze(axis)


def score_rows(t_lo, t_hi, col_t, fn, true_cols, keep=K_ASSIGN, detail=None):
    """Evaluate every row against the answers inside its band.

    t_lo, t_hi: (n,) band per row: col_t in [t_lo, t_hi).
    col_t: (m,) answer times, sorted ascending.
    fn(r, c): scores for flattened row/answer index arrays (may return -inf).
    true_cols: (n, k) answer indices that are right for each row (-1 = none).
    detail: (n,) bool, rows that need the temperature-grid log-sum-exp (the scored rows); None =
      every row. Other rows get NaN there; their picks, ranks and edges are still computed.
    Returns a dict of per-row arrays plus the kept edges (row, col, score) for assignment."""
    n = t_lo.shape[0]
    start = np.searchsorted(col_t, t_lo, side="left")
    stop = np.maximum(np.searchsorted(col_t, t_hi, side="left"), start)
    width = stop - start
    out = dict(top1=np.full(n, -np.inf), top2=np.full(n, -np.inf), argmax=np.full(n, -1, np.int64),
               n_feas=np.zeros(n, np.int32), s_true=np.full(n, -np.inf),
               rank=np.full(n, np.iinfo(np.int32).max, np.int32), lse=np.full((n, T_GRID.size), -np.inf))
    er, ec, ew = [], [], []
    # the true answers' scores, evaluated directly (they may lie outside the band: then -inf)
    tr = np.repeat(np.arange(n), true_cols.shape[1])
    tc = true_cols.ravel()
    ts = np.full(tc.shape, -np.inf)
    ok = tc >= 0
    if ok.any():
        inb = ok.copy()
        inb[ok] = (tc[ok] >= start[tr[ok]]) & (tc[ok] < stop[tr[ok]])
        if inb.any():
            ts[inb] = fn(tr[inb], tc[inb])
    out["s_true"] = ts.reshape(n, -1).max(axis=1)
    out["n_true"] = np.isfinite(ts).reshape(n, -1).sum(1).astype(np.int8)

    order = np.argsort(-width, kind="stable")            # chunks of similar width
    i = 0
    while i < n:
        B = max(int(width[order[i]]), 1)
        take = max(1, CHUNK_CELLS // B)
        rows = order[i:i + take]
        i += take
        B = max(int(width[rows].max()), 1)
        j = np.arange(B)[None, :]
        valid = j < width[rows][:, None]
        cols = start[rows][:, None] + j
        W = np.full(valid.shape, -np.inf)
        rr = np.broadcast_to(rows[:, None], valid.shape)[valid]
        cc = cols[valid]
        if rr.size:
            W[valid] = fn(rr, cc)
        fin = np.isfinite(W)
        out["n_feas"][rows] = fin.sum(1)
        if B >= 2:
            part = -np.partition(-W, 1, axis=1)[:, :2]
            out["top1"][rows], out["top2"][rows] = part[:, 0], part[:, 1]
        else:
            out["top1"][rows] = W[:, 0]
        am = np.argmax(W, axis=1)
        out["argmax"][rows] = np.where(np.isfinite(out["top1"][rows]), start[rows] + am, -1)
        st = out["s_true"][rows]
        out["rank"][rows] = np.where(np.isfinite(st), 1 + (W > st[:, None]).sum(1), out["rank"][rows])
        dr = np.ones(rows.size, bool) if detail is None else detail[rows]
        if dr.any():
            Wd = W[dr]
            for t_i, T in enumerate(T_GRID):
                out["lse"][rows[dr], t_i] = _lse(Wd / T, axis=1)
        k = min(keep, B)
        if k < B:
            idx = np.argpartition(-W, k - 1, axis=1)[:, :k]
        else:
            idx = np.broadcast_to(np.arange(B)[None, :], W.shape)
        kw = np.take_along_axis(W, idx, axis=1)
        m = np.isfinite(kw)
        er.append(np.broadcast_to(rows[:, None], kw.shape)[m])
        ec.append((start[rows][:, None] + idx)[m])
        ew.append(kw[m])
    cat = (lambda x, dt: np.concatenate(x).astype(dt) if x else np.zeros(0, dt))
    out["edges"] = (cat(er, np.int64), cat(ec, np.int64), cat(ew, np.float64))
    top = np.where(np.isfinite(out["top1"]), out["top1"], 0.0)[:, None] / T_GRID[None, :]
    out["lse"] = np.where(np.isfinite(out["lse"]), out["lse"] - top, np.nan).astype(np.float16)
    return out


def joint_assign(n_rows, edges, groups):
    """Optimal one-to-one assignment per group, maximising summed score over the kept edges
    (the same objective as linear_sum_assignment with an infeasibility penalty: first as many
    rows as possible assigned, then the largest total score). Returns the picked answer per row."""
    er, ec, ew = edges
    pick = np.full(n_rows, -1, np.int64)
    if er.size == 0:
        return pick
    g_of_edge = groups[er]
    order = np.argsort(g_of_edge, kind="stable")
    er, ec, ew, g_of_edge = er[order], ec[order], ew[order], g_of_edge[order]
    bounds = np.flatnonzero(np.diff(g_of_edge)) + 1
    for sl in np.split(np.arange(er.size), bounds):
        if sl.size == 0:
            continue
        r_u, r_inv = np.unique(er[sl], return_inverse=True)
        c_u, c_inv = np.unique(ec[sl], return_inverse=True)
        nr, nc = r_u.size, c_u.size
        shift = ew[sl].max() + 1.0                       # strictly positive costs
        rows = np.concatenate([r_inv, np.arange(nr)])
        cols = np.concatenate([c_inv, nc + np.arange(nr)])  # one private "unassigned" column per row
        cost = np.concatenate([shift - ew[sl], np.full(nr, _UNMATCHED)])
        G = csr_matrix((cost, (rows, cols)), shape=(nr, nc + nr))
        ri, ci = min_weight_full_bipartite_matching(G)
        hit = ci < nc
        pick[r_u[ri[hit]]] = c_u[ci[hit]]
    return pick


def random_baseline(res):
    """Per-decision random assignment over the same feasible answers: the expected share right is
    (true answers inside the row's feasible set) / (feasible answers). Exact, no sampling."""
    return np.where(res["n_feas"] > 0, res["n_true"] / np.maximum(res["n_feas"], 1), 0.0)


def decide(res, groups, col_sub, row_sub, true_cols):
    """Joint and per-decision picks, and the per-row decision record."""
    n = row_sub.shape[0]
    pick = joint_assign(n, res["edges"], groups)
    s_joint = np.full(n, -np.inf)
    er, ec, ew = res["edges"]
    if er.size:
        key = er * (col_sub.shape[0] + 1) + ec
        want = np.nonzero(pick >= 0)[0]
        q = want * (col_sub.shape[0] + 1) + pick[want]
        o = np.argsort(key)
        pos = np.searchsorted(key[o], q)
        s_joint[want] = ew[o][pos]
    pj = np.where(pick >= 0, col_sub[np.maximum(pick, 0)], -1)
    pa = np.where(res["argmax"] >= 0, col_sub[np.maximum(res["argmax"], 0)], -1)
    return dict(pred_joint=pj, pred_argmax=pa, correct=(pj == row_sub) & (pj >= 0),
                correct_argmax=(pa == row_sub) & (pa >= 0), s_joint=s_joint)

"""The ceiling attacker, the K-record attacker and the edit-chain attacker (C4 items 5a, 7 and the chain variant).

Ceiling attacker. It is told each transaction's true posting. For a record it picks one of that posting's
records at random and names its device. It is right with probability k / n, n the records in the posting and
k those of the record's device.

K-record attacker. It is told that K records share one device. For every device it sums, over the K records,
the calibrated log posterior a single-record attacker gives it, and names the device with the highest sum.
The posteriors are calibrated as C2 calibrates confidence: a temperature fitted on the runs of one parity is
applied to the runs of the other. A device with no feasible packet for a record gets a posterior of 10^-6
there. Each device's records in the window are taken in time order in disjoint groups of K.

Edit-chain attacker. It is told the chain (the records are public). It sums the log posteriors over the
chain's records, as the K-record attacker does, and names the device of the chain's capture. For an edit
record it uses only packets sent after the parent record's posting, since an edit is submitted after its
parent has posted.
"""
from __future__ import annotations

import numpy as np

from . import analyze as AN
from . import attacks as AT

FLOOR = np.log(1e-6)


def ceiling(run, rec, rng):
    """Per scored record: the ceiling attacker's outcome (a random pick in its posting) and its expectation."""
    s = run.subs
    post = s["posted"]
    fin = np.isfinite(post)
    key = np.round(post[fin], 6)
    order = np.argsort(key, kind="stable")
    keys, starts = np.unique(key[order], return_index=True)
    ends = np.r_[starts[1:], key.size]
    subs_sorted = np.nonzero(fin)[0][order]
    src = s["src"]
    correct, expect, size = [], [], []
    for sub in rec["sub"]:
        b = np.searchsorted(keys, np.round(post[sub], 6))
        members = subs_sorted[starts[b]:ends[b]]
        same = src[members] == src[sub]
        pick = members[rng.integers(0, members.size)]
        correct.append(src[pick] == src[sub])
        expect.append(same.mean())
        size.append(members.size)
    return dict(sub=rec["sub"].astype(np.int32), correct=np.array(correct, np.int8), expected=np.array(expect, np.float32),
                size=np.array(size, np.int16))


def vectors(col, n):
    """The collected device scores of every record, as compact arrays."""
    labs, scs = [], []
    for i in range(n):
        lab, sc = col.get(i)
        labs.append(lab.astype(np.int64))
        scs.append(sc.astype(np.float32))
    return labs, scs


def lower_bound_pass(run, m, out, lb):
    """The observer's device scores with each record's packets limited to those sent at or after lb (its parent's
    posting; -inf where the record is not an edit)."""
    from . import devscore as DS
    cand, rec = out["_cand"], out["_rec"]
    g = m.pdf["g"]
    u, n = rec["u"], rec["sub"].size
    lo, hi = AT._band(u, g)
    lo = np.maximum(lo, lb)
    hi = np.maximum(hi, lo)
    col = DS.Collector(n, cand["dev"])

    def fn(rows, k0, k1):
        return dict(obs=g(u[rows][:, None] - cand["t"][None, k0:k1]))
    AT.score_blocks(lo, hi, cand, fn, dict(sub=rec["sub"], dev=rec["dev"]), ("obs",),
                    extra=lambda nm, rows, a, b, W, is_t: col(rows, a, b, W))
    return vectors(col, n)


def _posterior(lab, sc, T):
    x = sc.astype(float) / T
    mx = x.max()
    return x - (np.log(np.exp(x - mx).sum()) + mx)


def decide(recs, T, dev, full=False):
    """One decision on a group of records [(labels, scores)] known to share a device: the summed calibrated log
    posteriors, floored at 10^-6 per record. Returns (correct, devices feasible in every record, truth among them);
    with full, also the true device's rank under the summed score and the entropy and min-entropy (bits) of the
    group's posterior, the softmax of the sum."""
    recs = [(lab, sc) for lab, sc in recs if lab.size]
    if not recs:
        return (False, 0, False, -1, np.nan, np.nan) if full else (False, 0, False)
    U = np.unique(np.concatenate([lab for lab, _ in recs]))
    M = np.full((len(recs), U.size), FLOOR)
    present = np.zeros((len(recs), U.size), bool)
    for i, (lab, sc) in enumerate(recs):
        pos = np.searchsorted(U, lab)
        M[i, pos] = np.maximum(_posterior(lab, sc, T), FLOOR)
        present[i, pos] = True
    tot = M.sum(0)
    pick = U[int(np.argmax(tot))]
    allp = present.all(0)
    res = (bool(pick == dev), int(allp.sum()), bool(allp[U == dev].any()) if (U == dev).any() else False)
    if not full:
        return res
    t = U == dev
    rank = int((tot > tot[t].max()).sum()) if t.any() else U.size
    H = AT._entropy(tot[None, :], 1.0)[0] / np.log(2.0)
    Hmin = (np.log(np.exp(tot - tot.max()).sum())) / np.log(2.0)
    return res + (rank, float(H), float(Hmin))


def temperatures(recs):
    """Per run parity, the temperature fitted on the observer's decisions of the other parity (as C2)."""
    t = AN.stack(recs, "observer")
    _, temps = AN.calibrated_confidence(t)
    return temps


def k_groups(recs_meta, K, key="dev"):
    """Disjoint groups of K records sharing a device, in time order: [(row indices, device)]."""
    dev, u = recs_meta[key], recs_meta["u"]
    out = []
    for d in np.unique(dev):
        rows = np.nonzero(dev == d)[0]
        rows = rows[np.argsort(u[rows], kind="stable")]
        for j in range(rows.size // K):
            out.append((rows[j * K:(j + 1) * K], d))
    return out


def k_record(recs, Ks, vec="vec", full=False):
    """Accuracy of the K-record attacker per K over a cell's runs: per run, (correct, decisions, chance sum). With
    full, also per K the decisions' rows: run, correct, device, rank, entropy and min-entropy (bits)."""
    temps = temperatures(recs)
    res = {K: [] for K in Ks}
    rows_ = {K: [] for K in Ks}
    for r in recs:
        T = temps[r["run"] % 2]
        labs, scs = r[vec]
        meta = r["meta"]
        for K in Ks:
            c = n = ch = 0
            for rows, d in k_groups(meta, K):
                ok, nall, tin, rank, H, Hmin = decide([(labs[i], scs[i]) for i in rows], T, d, full=True)
                c += ok
                n += 1
                ch += (1.0 / nall) if (tin and nall) else 0.0
                rows_[K].append((r["run"], int(ok), int(d), rank, H, Hmin, (1.0 / nall) if (tin and nall) else 0.0))
            res[K].append((c, n, ch))
    return (res, rows_) if full else res


def chains(recs, vec="vec_lb"):
    """Accuracy of the edit-chain attacker by chain length (records of the chain in the window): per run,
    {L: (correct, decisions, chance sum)}."""
    temps = temperatures(recs)
    res = []
    for r in recs:
        T = temps[r["run"] % 2]
        labs, scs = r[vec]
        meta = r["meta"]
        per = {}
        for root in np.unique(meta["root"]):
            rows = np.nonzero(meta["root"] == root)[0]
            d = meta["root_dev"][rows[0]]
            ok, nall, tin = decide([(labs[i], scs[i]) for i in rows], T, d)
            a = per.setdefault(int(rows.size), [0, 0, 0.0])
            a[0] += ok
            a[1] += 1
            a[2] += (1.0 / nall) if (tin and nall) else 0.0
        res.append(per)
    return res

"""Tables of C3, C4 and C5 from their raw files (never re-simulates).

Every row: the vantage (and class), its device-named accuracy with the 95% interval over runs, chance, the
multiple of chance, the lead over the passive observer on the same records, count_p50, coverage_p50, the
confidence AUC, whether the row meets the stability rule, and the bound from the posting schedule where it
applies: over every record of a vantage that names a device from the record time. A class chosen by the truth
(the roles a node held) can exceed it, so class rows show none.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from . import analyze as AN
from . import runner as RN

D_MAIN = 1168.2274123090758
POST_S = 120.0
_BOUND = {}


def posting_bound(R, decoys, per_device=None, draws=400_000):
    """E[k / n] for a record's posting: n records in it, k of them from the record's device. Records post at
    (R + decoys) / D per second; a device makes 120 / (20 minutes) records per posting."""
    key = (R, decoys, per_device)
    if key not in _BOUND:
        lam = POST_S * (R + decoys) / D_MAIN
        x = POST_S / (20 * 60) if per_device is None else per_device
        rng = np.random.default_rng(7)
        X = rng.poisson(x, draws)
        Y = rng.poisson(max(lam - x, 0.0), draws)
        _BOUND[key] = float(np.mean((1 + X) / (1 + X + Y)))
    return _BOUND[key]


def _cells(names):
    out = {}
    for n in names:
        job, variant, cell = n.split("__")
        out.setdefault((job, variant), []).append(float(cell[1:]))
    return out


def summarize(out, files, classes=None, decoys_of=None, bound_na=(), seed=12345):
    """Rows for every vantage of the given raw files. classes: {vantage: (column, {code: label})} to split a
    vantage's rows; decoys_of(job, variant) -> decoys in flight; bound_na: vantages the bound does not apply to."""
    rng = np.random.default_rng(seed)
    rows = []
    for name in files:
        recs = sorted(RN.load(out, name), key=lambda r: r["run"])
        if not recs:
            continue
        job, variant, cell = name.split("__")
        R = float(cell[1:])
        dec = decoys_of(job, variant) if decoys_of else 100.0
        spec = dict(R=R, T=R + dec, key=name)
        stats = [r.get("stats", {}) for r in recs]
        for v in recs[0]["vantages"]:
            if "dev_lse" not in recs[0]["vantages"][v]:          # diagnostics without confidence terms
                continue
            t_all = AN.stack(recs, v)
            splits = [(v, None)]
            if classes and v in classes:
                col, labels = classes[v]
                splits = [(f"{v} [{lab}]", (t_all[col] == code) if code is not None else np.ones(t_all[col].shape, bool))
                          for code, lab in labels.items()]
            for label, mask in splits:
                t = t_all if mask is None else {k: (a[mask] if isinstance(a, np.ndarray) and a.shape[:1] == mask.shape else a)
                                               for k, a in t_all.items()}
                if t["sub"].size == 0:
                    continue
                if "claim" in t and "took_part" not in t:     # the first hop's claims are read per hop position in C2
                    t = {k: a for k, a in t.items() if k != "claim"}
                mt = AN.metrics(recs, v, spec, rng, t=t, name=label)
                mt.pop("_per_run", None)
                mt.update(job=job, variant=variant, file=name, decoys=dec,
                          bound=None if (v in bound_na or label in bound_na or (mask is not None and not label.endswith("[all records]")))
                          else posting_bound(R, dec),
                          real_in_flight=float(np.mean([s.get("real_in_flight", np.nan) for s in stats])),
                          decoys_in_flight=float(np.mean([s.get("decoys_in_flight", np.nan) for s in stats])),
                          score_seconds=float(np.mean([r.get("score_seconds", 0.0) for r in recs])),
                          sim_seconds=float(np.mean([r.get("sim_seconds", 0.0) for r in recs])))
                rows.append(mt)
    return rows


def pct(x):
    return "—" if x is None or (isinstance(x, float) and not math.isfinite(x)) else f"{100 * x:.2f}%"


def markdown(rows, title, dry=False):
    lines = []
    if dry:
        lines.append("DRY RUN: fewer runs than the full count. These numbers are not results.\n")
    lines.append(f"# {title}\n")
    lines.append("| File | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | "
                 "count_p50 | coverage_p50 | AUC | Stable | Bound | Real, decoys in flight |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        if "dev_accuracy" not in r:
            continue
        lines.append(
            f"| {r['file']} | {r['vantage']} | {r['runs']} | {r['n']:,} | {pct(r['dev_accuracy'])} [{pct(r['dev_ci_lo'])}, {pct(r['dev_ci_hi'])}] | "
            f"{pct(r['dev_random'])} | ×{r['dev_lift_random']:.2f} | {100 * r['dev_contribution']:+.2f} | {r['count_p50']} | "
            f"{r['coverage_p50']:.4f} | {r['auc']:.3f} | {'yes' if r['stable'] else 'no'} | "
            f"{'not applicable' if r['bound'] is None else pct(r['bound'])} | {r['real_in_flight']:.2f}, {r['decoys_in_flight']:.2f} |")
    return "\n".join(lines) + "\n"


def write(out, rows, stem, title, dry=False):
    out = Path(out)
    clean = [{k: v for k, v in r.items() if k not in ("reliability", "temperature")} for r in rows]
    stem = stem + ("_dry_run" if dry else "")
    (out / f"{stem}.json").write_text(json.dumps(clean, indent=1, default=float))
    (out / f"{stem}.md").write_text(markdown(rows, title, dry))

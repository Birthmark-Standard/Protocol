# Copyright (C) 2024-2026 The Birthmark Standard Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

"""Build the Part B JSON, summary and comparison from the raw logs of one run.

Every number is computed from results/raw/partB_<run_id>_*. Extrapolated
values are labelled EXTRAPOLATED wherever they appear.

Usage: python3 summarize_partB.py RUN_ID [--field gf2_128|fp64_2]

--field picks the field for comparison.md and the extrapolation. Without it,
the field with the most measured sizes is used; on a tie, the one with the
lower median prove time at the largest size both measured.
"""

import argparse
import datetime
import json
import math
import os
import re
import statistics

import summarize_partA

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
RAW = os.path.join(RESULTS, "raw")

TARGET_BYTES = 30000000
TARGET_COMPRESSIONS = 468750
VENDOR_POINT = 130944
EIGHT_GB = 8 * 1024 ** 3
SWAP_LABEL = "setup with swap, not comparable"
EXTRAP = "EXTRAPOLATED"


def compressions(n):
    return (n + 8) // 64 + 1


def stats_s(xs):
    xs = sorted(xs)
    n = len(xs)
    return {
        "n": n,
        "min_s": xs[0],
        "median_s": statistics.median(xs),
        "mean_s": statistics.fmean(xs),
        "p95_s": xs[max(0, math.ceil(0.95 * n) - 1)],
        "std_s": statistics.stdev(xs) if n > 1 else 0.0,
    }


def read_jsonl(path):
    header, after, lines = None, None, []
    with open(path) as f:
        for raw in f:
            raw = raw.strip()
            if not raw.startswith("{"):
                continue
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if o.get("type") == "header" and header is None:
                header = o
            elif o.get("type") == "driver_after":
                after = o
            else:
                lines.append(o)
    return header, after or {}, lines


def fit_power_law(points):
    """Least squares of log(y) on log(c). Returns b, a, r2 for y = exp(a) * c^b."""
    pts = [(math.log(c), math.log(y)) for c, y in points if c > 0 and y > 0]
    if len(pts) < 2:
        return None
    xs, ys = zip(*pts)
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx == 0:
        return None
    b = sum((x - mx) * (y - my) for x, y in pts) / sxx
    a = my - b * mx
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - (a + b * x)) ** 2 for x, y in pts)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else None
    return {"exponent": b, "log_coefficient": a, "r2": r2, "points": len(pts)}


def at(fit, c):
    return math.exp(fit["log_coefficient"]) * c ** fit["exponent"]


def size_label(n):
    if n == VENDOR_POINT:
        return "130,944 B (127.9 KiB)"
    if n >= 1 << 20 and n % (1 << 20) == 0:
        return f"{n >> 20} MiB"
    if n >= 1024 and n % 1024 == 0:
        return f"{n >> 10} KiB"
    return f"{n:,} B"


def fmt_s(x):
    if x is None:
        return "n/a"
    if x >= 100:
        return f"{x:,.0f}"
    if x >= 1:
        return f"{x:.2f}"
    return f"{x:.4g}"


def fmt_ms(x):
    return summarize_partA.fmt(x)


def fmt_mib(kb):
    if kb is None:
        return "n/a"
    if kb >= 10 * 1024 * 1024:
        return f"{kb / 1024 / 1024:,.0f} GiB"
    return f"{kb / 1024:,.0f} MiB"


def load(run_id):
    names = sorted(f for f in os.listdir(RAW) if f.startswith(f"partB_{run_id}_"))
    if not names:
        raise SystemExit(f"no raw logs for run {run_id} in {RAW}")
    machine, label = None, None
    setups, proves, hashes, stops, raw_files = [], [], [], [], []
    for name in names:
        path = os.path.join(RAW, name)
        rel = os.path.relpath(path, HERE)
        raw_files.append(rel)
        if name.endswith("_stopped.json"):
            with open(path) as f:
                stops.append(dict(json.load(f), raw_file=rel))
            continue
        header, after, lines = read_jsonl(path)
        if not header:
            continue
        machine = machine or header.get("machine")
        label = label or header.get("label")
        tv = after.get("time_v", {})
        common = {
            "raw_file": rel,
            "exit_code": after.get("exit_code"),
            "timed_out": after.get("timed_out"),
            "terminated_by_signal": tv.get("terminated_by_signal"),
            "peak_rss_kb": tv.get("max_rss_kb"),
            "throttle": summarize_partA.throttle_flag(header.get("before"), after.get("after")),
            "stderr_tail": (after.get("stderr") or "")[-600:],
            "swap_activity": after.get("swap_activity"),
            "peak_rss_method": header.get("peak_rss_method", "GNU time -v"),
        }
        sa = after.get("swap_activity")
        swapped = bool(sa and sa.get("pages_swapped"))
        if header["phase"] == "setup":
            st = next((x for x in lines if x.get("type") == "setup"), {})
            saved = next((x for x in lines if x.get("type") == "circuit_saved"), {})
            cf = next((x for x in lines if x.get("type") == "circuit_file"), {})
            swap_on = bool((header.get("swap") or {}).get("active") or (after.get("swap_after") or {}).get("active"))
            # Logs without swap_activity predate its recording; treat active swap as used.
            if swap_on and (swapped or sa is None):
                setup_label = SWAP_LABEL
            elif swap_on:
                setup_label = "swap on, no pages swapped"
            else:
                setup_label = "on this machine, no swap"
            setups.append(dict(common, field=header["field"], message_bytes=header["message_bytes"],
                               compressions=header["compressions"],
                               setup_label=setup_label,
                               swap_active=swap_on, setup_s=st.get("setup_s"), circuit=st.get("circuit"),
                               circuit_id=st.get("circuit_id"), circuit_file_bytes=saved.get("bytes"),
                               circuit_sha256=cf.get("sha256"),
                               ok=common["exit_code"] == 0 and saved.get("status") == "ok",
                               build=header.get("build")))
        elif header["phase"] == "prove":
            st = next((x for x in lines if x.get("type") == "setup"), {})
            runs = [x for x in lines if x.get("type") == "run"]
            done = next((x for x in lines if x.get("type") == "done"), {})
            ok = common["exit_code"] == 0 and done.get("all_checks_passed") is True \
                and len(runs) == header.get("repeats") and not swapped
            rec = dict(common, phase_kind="prove", field=header["field"], message_bytes=header["message_bytes"],
                       compressions=header["compressions"], repeats=header.get("repeats"),
                       threads=header.get("threads"), ok=ok, load_s=st.get("setup_s"),
                       circuit=st.get("circuit"), circuit_id=st.get("circuit_id"),
                       zero_knowledge=st.get("zero_knowledge"), ligero_rate=st.get("ligero_rate"),
                       ligero_queries=st.get("ligero_queries"), build=header.get("build"),
                       swap_active=bool((header.get("swap") or {}).get("active")),
                       checks_first_repeat=runs[0]["checks"] if runs else None)
            if runs:
                rec["prove"] = stats_s([x["time_s"]["prove"] for x in runs])
                rec["verify"] = stats_s([x["time_s"]["verify"] for x in runs])
                rec["witness_median_s"] = statistics.median(
                    x["time_s"]["host_witness"] + x["time_s"]["fill_inputs"] for x in runs)
                rec["proof_bytes_median"] = statistics.median(x["proof_bytes"] for x in runs)
            proves.append(rec)
        elif header["phase"] == "hash":
            for r in lines:
                if r.get("type") != "row" or r.get("status") != "ok":
                    continue
                s = summarize_partA.stats_ms(r["samples_ns"])
                hashes.append(dict(s, variant=header["variant"], name=r["name"], bytes=r["bytes"],
                                   path=summarize_partA.path_label(machine, header["variant"], r["name"]),
                                   throttle=common["throttle"], raw_file=rel))
    return machine, label, setups, proves, hashes, stops, raw_files


def choose_field(proves, wanted):
    ok = [p for p in proves if p["ok"]]
    if wanted:
        return wanted, f"chosen with --field {wanted}"
    by_field = {}
    for p in ok:
        by_field.setdefault(p["field"], {})[p["message_bytes"]] = p
    if not by_field:
        return None, "no field has a measured size"
    counts = {f: len(v) for f, v in by_field.items()}
    best = max(counts.values())
    tied = [f for f, n in counts.items() if n == best]
    if len(tied) == 1:
        return tied[0], f"the field with the most measured sizes ({best})"
    common = set.intersection(*(set(by_field[f]) for f in tied))
    if not common:
        return sorted(tied)[0], "tie on measured sizes with no common size; first by name"
    n = max(common)
    f = min(tied, key=lambda x: by_field[x][n]["prove"]["median_s"])
    return f, f"tie on measured sizes; lower median prove time at {size_label(n)}"


def hash_row(hashes, name, variant, nbytes):
    for h in hashes:
        if h["name"] == name and h["variant"] == variant and h["bytes"] == nbytes:
            return h
    return None


def summarize(run_id, wanted_field=None):
    machine, label, setups, proves, hashes, stops, raw_files = load(run_id)
    dry = label == summarize_partA.DRY_LABEL
    sha_ext = machine["sha_extensions"]
    field, field_rule = choose_field(proves, wanted_field)

    # Hash columns: "with SHA extensions" exists only on a CPU that has them.
    def hash_with(n):
        return hash_row(hashes, "sha256_bytes_openssl", "default", n) if sha_ext else None

    def hash_without(n):
        if sha_ext:
            return hash_row(hashes, "sha256_bytes_openssl", "caps_off", n)
        return hash_row(hashes, "sha256_bytes_openssl", "default", n)

    # Pilot: both fields measured at the same size.
    pilot = []
    sizes_by_field = {}
    for p in proves:
        if p["ok"]:
            sizes_by_field.setdefault(p["field"], {})[p["message_bytes"]] = p
    if len(sizes_by_field) >= 2:
        common = set.intersection(*(set(v) for v in sizes_by_field.values()))
        for n in sorted(common):
            rows = {f: v[n]["prove"]["median_s"] for f, v in sizes_by_field.items()}
            pilot.append({"message_bytes": n, "median_prove_s": rows, "faster": min(rows, key=rows.get)})

    # Ratios at each measured size of every field.
    ratios = []
    for p in proves:
        if not p["ok"]:
            continue
        n = p["message_bytes"]
        row = {"field": p["field"], "message_bytes": n, "prove_median_s": p["prove"]["median_s"]}
        for key, h in (("openssl_default", hash_row(hashes, "sha256_bytes_openssl", "default", n)),
                       ("openssl_caps_off", hash_row(hashes, "sha256_bytes_openssl", "caps_off", n)),
                       ("libsodium", hash_row(hashes, "sha256_bytes_libsodium", "default", n))):
            if h:
                row[key] = {"hash_median_ms": h["median_ms"], "path": h["path"],
                            "ratio": p["prove"]["median_s"] / (h["median_ms"] / 1e3)}
        ratios.append(row)

    # Extrapolation to 30,000,000 B for the chosen field.
    extrap = None
    if field:
        ok = sorted((p for p in proves if p["ok"] and p["field"] == field), key=lambda p: p["compressions"])
        su = sorted((s for s in setups if s["ok"] and s["field"] == field), key=lambda s: s["compressions"])
        if ok:
            largest = ok[-1]
            pts_t = [(p["compressions"], p["prove"]["median_s"]) for p in ok]
            pts_m = [(p["compressions"], p["peak_rss_kb"]) for p in ok if p["peak_rss_kb"]]
            pts_s = [(s["compressions"], s["peak_rss_kb"]) for s in su if s["peak_rss_kb"]]
            ft, fm, fs = fit_power_law(pts_t), fit_power_law(pts_m), fit_power_law(pts_s)
            scale = TARGET_COMPRESSIONS / largest["compressions"]
            extrap = {
                "label": EXTRAP, "field": field, "target_bytes": TARGET_BYTES,
                "target_compressions": TARGET_COMPRESSIONS,
                "largest_measured": {"message_bytes": largest["message_bytes"],
                                     "compressions": largest["compressions"]},
                "prove_s": {"power_law_fit": ft, "power_law": at(ft, TARGET_COMPRESSIONS) if ft else None,
                            "linear_from_largest": largest["prove"]["median_s"] * scale},
                "prove_peak_rss_kb": {"power_law_fit": fm,
                                      "power_law": at(fm, TARGET_COMPRESSIONS) if fm else None,
                                      "linear_from_largest": (largest["peak_rss_kb"] or 0) * scale},
                "setup_peak_rss_kb": None,
            }
            if su:
                big = su[-1]
                extrap["setup_peak_rss_kb"] = {
                    "power_law_fit": fs, "power_law": at(fs, TARGET_COMPRESSIONS) if fs else None,
                    "linear_from_largest": (big["peak_rss_kb"] or 0) * TARGET_COMPRESSIONS / big["compressions"],
                    "largest_measured": {"message_bytes": big["message_bytes"], "compressions": big["compressions"]},
                }

    build = next((p["build"] for p in proves if p.get("build")), None) or \
        next((s["build"] for s in setups if s.get("build")), None) or {}
    now = datetime.datetime.now(datetime.timezone.utc)
    result = {
        "label": label, "run_id": run_id, "generated_utc": now.isoformat(timespec="seconds"),
        "machine": machine, "core": summarize_partA.core_name(machine["model"]),
        "prover": "longfellow-zk", "build": build, "statement":
            "knowledge of M with SHA-256(M) = H; H public; length of M fixed by the circuit",
        "vendor_point_note": "130,944 B (2,047 compressions) approximates the vendor's unpublished "
                             "byte count for the \"127.9 KiB\" message",
        "comparison_field": field, "comparison_field_rule": field_rule,
        "setup": setups, "prove": proves, "stops": stops, "hash": hashes, "pilot": pilot,
        "ratios": ratios, "extrapolation": extrap, "raw_files": raw_files,
    }

    host = re.sub(r"[^A-Za-z0-9_.-]", "_", machine["hostname"])
    date = run_id.split("T")[0]
    date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
    tag = f"_{summarize_partA.DRY_TAG}" if dry else ""
    json_path = summarize_partA.unique_path(os.path.join(RESULTS, f"partB{tag}_{date}_{host}.json"))
    text = json.dumps(result, indent=2).replace('{\n  "label"', '{"label"', 1)
    with open(json_path, "x") as f:
        f.write(text + "\n")
    md_path = os.path.join(RESULTS, f"partB_summary{tag}.md")
    with open(md_path, "w") as f:
        f.write(render_summary(result, os.path.relpath(json_path, HERE), dry))
    cmp_path = os.path.join(RESULTS, f"comparison{tag}.md")
    with open(cmp_path, "w") as f:
        f.write(render_comparison(result, hash_with, hash_without, dry))
    return json_path, md_path, cmp_path


def build_lines(res):
    b = res["build"] or {}
    info = b.get("info") or {}
    out = [f"- Prover: Longfellow-zk, commit `{info.get('commit')}`, {info.get('compiler')}, "
           f"build type {info.get('build_type')}."]
    changes = []
    if info.get("no_pmull_build_changes"):
        changes.append("no-PMULL changes (compile flags without +crypto; GF(2^128) on Longfellow's NEON code)")
    if info.get("wide_label_build_change"):
        changes.append("4-byte wire labels in the circuit file format")
    out.append("- Build changes to Longfellow: " + ("; ".join(changes) if changes else "none") +
               ". The diff is in each raw log's header.")
    if info.get("crypto_extension_instructions_in_binary") is not None:
        out.append(f"- Crypto-extension instructions in the prover binary: "
                   f"{info.get('crypto_extension_instructions_in_binary')}.")
    return out


def render_summary(res, json_rel, dry):
    m = res["machine"]
    L = []
    if dry:
        L += [summarize_partA.DRY_LABEL, "", "# Part B summary (dry run)", "",
              f"This run is not from a Raspberry Pi. The machine reports `{m['model'] or m['cpu_model']}`. "
              "These numbers test the code path only and must not be cited as Pi results.", ""]
    else:
        L += [f"# Part B summary: {m['model']}", "", f"Measured on a {m['model']}, {res['core']}.", ""]
    L.append(f"- Run: `{res['run_id']}`. Full data: `{json_rel}`.")
    L.append(f"- Statement: {res['statement']}. Zero-knowledge on. One thread, pinned to core {m['pinned_cpu']}.")
    L += build_lines(res)
    L.append(f"- RAM: {m['mem_total_kb'] / 1048576:.2f} GiB. CPU features: {m['cpu_features']}")
    L.append(f"- {res['vendor_point_note']}.")
    L.append("")

    L += ["## Setup: circuit construction", "",
          "Setup is not part of the prover time. A setup row marked \"setup with swap, not comparable\" "
          "ran while swap was active, and its time must not be compared with anything.", "",
          "| Field | Size | Compressions | Setup time (s) | Setup label | Peak memory | Circuit file | Status |",
          "|---|---|---:|---:|---|---:|---:|---|"]
    for s in sorted(res["setup"], key=lambda s: (s["field"], s["message_bytes"])):
        status = "ok" if s["ok"] else failure_text(s)
        L.append(f"| {s['field']} | {size_label(s['message_bytes'])} | {s['compressions']:,} | "
                 f"{fmt_s(s['setup_s'])} | {s['setup_label']} | {fmt_mib(s['peak_rss_kb'])} | "
                 f"{(s['circuit_file_bytes'] or 0) / 1e6:,.1f} MB | {status} |")
    L.append("")

    L += ["## Prove: measured", "",
          "Times in seconds. Prove covers Longfellow's commit and prove calls. Peak memory is the whole "
          "prove process (circuit load and all repeats), from `/usr/bin/time -v`.", "",
          "| Field | Size | Compressions | n | Prove min | Prove median | Prove mean | Prove p95 | Prove std | "
          "Verify median | Circuit load | Proof size | Peak memory | Checks | Flag |",
          "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|"]
    for p in sorted(res["prove"], key=lambda p: (p["field"], p["message_bytes"])):
        if not p.get("prove"):
            L.append(f"| {p['field']} | {size_label(p['message_bytes'])} | {p['compressions']:,} | 0 | "
                     f"| | | | | | | | {fmt_mib(p['peak_rss_kb'])} | {failure_text(p)} | |")
            continue
        pr, ve, c = p["prove"], p["verify"], p["checks_first_repeat"] or {}
        checks = (f"honest {c.get('verify_honest_child')}, tampered proof {c.get('verify_tampered_proof')}, "
                  f"wrong H {c.get('verify_wrong_h')}") if p["ok"] else failure_text(p)
        flag = "THROTTLED" if p["throttle"] == "THROTTLED" else ""
        L.append(f"| {p['field']} | {size_label(p['message_bytes'])} | {p['compressions']:,} | {pr['n']} | "
                 f"{fmt_s(pr['min_s'])} | {fmt_s(pr['median_s'])} | {fmt_s(pr['mean_s'])} | {fmt_s(pr['p95_s'])} | "
                 f"{fmt_s(pr['std_s'])} | {fmt_s(ve['median_s'])} | {fmt_s(p['load_s'])} | "
                 f"{p['proof_bytes_median'] / 1e3:,.0f} kB | {fmt_mib(p['peak_rss_kb'])} | {checks} | {flag} |")
    L.append("")

    if res["pilot"]:
        L += ["## Field pilot", ""]
        for pl in res["pilot"]:
            parts = ", ".join(f"{f} {fmt_s(t)} s" for f, t in sorted(pl["median_prove_s"].items()))
            L.append(f"- {size_label(pl['message_bytes'])}: median prove {parts}. Faster: {pl['faster']}.")
        L.append("")
    L.append(f"Field used for the comparison and the extrapolation: {res['comparison_field']} "
             f"({res['comparison_field_rule']}).")
    L.append("")

    if res["stops"]:
        L += ["## Where the sweep stopped", ""]
        for s in res["stops"]:
            L.append(f"- {s['field']}, {size_label(s['message_bytes'])}: {s['reason']}.")
        L.append("")

    L += ["## Plain SHA-256 of M on the same machine", "",
          "Times in milliseconds, M in RAM, same code as Part A row A1.", "",
          "| Size | Path | n | min | median | p95 | std | Flag |", "|---|---|---:|---:|---:|---:|---:|---|"]
    order = {"default": 0, "caps_off": 1}
    for h in sorted(res["hash"], key=lambda h: (h["bytes"], order.get(h["variant"], 9), "libsodium" in h["name"])):
        flag = "THROTTLED" if h["throttle"] == "THROTTLED" else ""
        L.append(f"| {size_label(h['bytes'])} | {h['path']} | {h['n']} | {fmt_ms(h['min_ms'])} | "
                 f"{fmt_ms(h['median_ms'])} | {fmt_ms(h['p95_ms'])} | {fmt_ms(h['std_ms'])} | {flag} |")
    L.append("")

    L += ["## Prover time ÷ hash time", "",
          "Median prove time divided by the median plain-hash time of the same M.", "",
          "| Field | Size | Prove median (s) | ÷ OpenSSL default | ÷ OpenSSL capabilities off | ÷ libsodium |",
          "|---|---|---:|---:|---:|---:|"]
    for r in sorted(res["ratios"], key=lambda r: (r["field"], r["message_bytes"])):
        def cell(key):
            return f"{r[key]['ratio']:,.0f}" if key in r else "n/a"
        L.append(f"| {r['field']} | {size_label(r['message_bytes'])} | {fmt_s(r['prove_median_s'])} | "
                 f"{cell('openssl_default')} | {cell('openssl_caps_off')} | {cell('libsodium')} |")
    L.append("")

    L += extrapolation_lines(res)
    if dry:
        L += [f"{summarize_partA.DRY_LABEL}. None of the numbers above is a Raspberry Pi measurement.", ""]
    return "\n".join(L)


def failure_text(r):
    sa = r.get("swap_activity") or {}
    if r.get("phase_kind") == "prove" and sa.get("pages_swapped"):
        return "FAILED: pages were swapped during proving"
    if r.get("timed_out"):
        return "FAILED: timed out"
    if r.get("terminated_by_signal"):
        sig = r["terminated_by_signal"]
        name = {4: "SIGILL, illegal instruction", 6: "SIGABRT", 9: "SIGKILL, likely out of memory",
                11: "SIGSEGV"}.get(sig, f"signal {sig}")
        return f"FAILED: {name}"
    return f"FAILED: exit {r.get('exit_code')}"


def extrapolation_lines(res):
    e = res["extrapolation"]
    L = [f"## Extrapolation to 30,000,000 B ({EXTRAP})", ""]
    if not e:
        return L + ["No field has a measured size, so nothing is extrapolated.", ""]
    lm = e["largest_measured"]
    L.append(f"Field {e['field']}. Target: {TARGET_BYTES:,} B, {TARGET_COMPRESSIONS:,} compressions. "
             f"Largest measured size: {size_label(lm['message_bytes'])} ({lm['compressions']:,} compressions).")
    L.append("")
    L += [f"| Quantity | Power-law fit | Points | R² | {EXTRAP}: power law | {EXTRAP}: linear from largest point |",
          "|---|---|---:|---:|---:|---:|"]

    def row(name, d, unit):
        f = d["power_law_fit"] if d else None
        conv = (lambda v: f"{v:,.0f} s") if unit == "s" else (lambda v: fmt_mib(v))
        if not d:
            return f"| {name} | no data | | | | |"
        fit = f"value ∝ compressions^{f['exponent']:.3f}" if f else "fewer than 2 points"
        r2 = "n/a" if not f or f["r2"] is None else f"{f['r2']:.4f}"
        pts = f["points"] if f else 0
        pl = conv(d["power_law"]) + f" ({EXTRAP})" if d.get("power_law") else "n/a"
        return f"| {name} | {fit} | {pts} | {r2} | {pl} | {conv(d['linear_from_largest'])} ({EXTRAP}) |"
    L.append(row("Prove time", e["prove_s"], "s"))
    L.append(row("Prove-process peak memory", e["prove_peak_rss_kb"], "kb"))
    L.append(row("Setup peak memory", e["setup_peak_rss_kb"], "kb"))
    L.append("")
    for d in (e["prove_s"], e["prove_peak_rss_kb"], e["setup_peak_rss_kb"]):
        if d and d["power_law_fit"] and d["power_law_fit"]["points"] == 2:
            L.append("With two points the power law passes through both, so R² is 1 by construction and "
                     "says nothing about the fit.")
            break
    L.append("")
    mem_total = res["machine"]["mem_total_kb"] * 1024
    for name, d in (("prove process", e["prove_peak_rss_kb"]), ("setup", e["setup_peak_rss_kb"])):
        if not d:
            continue
        vals = [v for v in (d.get("power_law"), d.get("linear_from_largest")) if v]
        if not vals:
            continue
        lo = min(vals) * 1024
        verdicts = []
        for cap_name, cap in (("this machine's RAM", mem_total), ("8 GB", EIGHT_GB)):
            verdicts.append(f"{'does not fit' if lo > cap else 'may fit'} in {cap_name}")
        L.append(f"- Memory, {name} ({EXTRAP}): the lower of the two estimates is {lo / 2**30:,.1f} GiB, which "
                 f"{' and '.join(verdicts)}. Basis: the measured growth in the rows above.")
    L.append("")
    return L


def render_comparison(res, hash_with, hash_without, dry):
    m = res["machine"]
    e = res["extrapolation"]
    field = res["comparison_field"]
    L = []
    if dry:
        L += [summarize_partA.DRY_LABEL, ""]
    L += ["# Part B comparison", ""]
    L.append(f"Machine: {m['model'] or m['cpu_model']}" + (f", {res['core']}" if res["core"] else "") +
             f". Prover: Longfellow-zk, field {field}, zero-knowledge on, one thread. Run `{res['run_id']}`.")
    L.append("")
    flag = "sha2" if m["arch"] == "aarch64" else "sha_ni"
    with_note = None if m["sha_extensions"] else f"not available: the CPU feature list has no {flag}"
    any_h = hash_without(TARGET_BYTES) or hash_without(1024)
    without_path = any_h["path"] if any_h else "n/a"
    L += [f"Hash times in milliseconds. \"Without\" is {without_path}.", "",
          "| Input size | Hash time with SHA extensions | Hash time without | Prover time | Prover peak memory | "
          "Ratio (prover ÷ hash without) |",
          "|---|---:|---:|---:|---:|---:|"]
    proves = sorted((p for p in res["prove"] if p["ok"] and p["field"] == field), key=lambda p: p["message_bytes"])
    for p in proves:
        n = p["message_bytes"]
        hw, ho = hash_with(n), hash_without(n)
        ratio = f"{p['prove']['median_s'] / (ho['median_ms'] / 1e3):,.0f}" if ho else "n/a"
        L.append(f"| {size_label(n)} | {with_note or (fmt_ms(hw['median_ms']) if hw else 'n/a')} | "
                 f"{fmt_ms(ho['median_ms']) if ho else 'n/a'} | {fmt_s(p['prove']['median_s'])} s | "
                 f"{fmt_mib(p['peak_rss_kb'])} | {ratio} |")
    hw, ho = hash_with(TARGET_BYTES), hash_without(TARGET_BYTES)
    if e:
        for kind, key in (("power law", "power_law"), ("linear from largest point", "linear_from_largest")):
            t = e["prove_s"].get(key)
            mem = e["prove_peak_rss_kb"].get(key)
            ratio = f"{t / (ho['median_ms'] / 1e3):,.0f} ({EXTRAP})" if t and ho else "n/a"
            L.append(f"| 30,000,000 B | {with_note or (fmt_ms(hw['median_ms']) if hw else 'n/a')} | "
                     f"{fmt_ms(ho['median_ms']) if ho else 'n/a'} | "
                     f"{(fmt_s(t) + ' s') if t else 'n/a'} ({EXTRAP}, {kind}) | "
                     f"{fmt_mib(mem) if mem else 'n/a'} ({EXTRAP}, {kind}) | {ratio} |")
    L.append("")
    L.append("Hash times at 30,000,000 B are measured. Every prover cell at 30,000,000 B is EXTRAPOLATED.")
    L.append(f"{res['vendor_point_note']}.")
    L.append("")
    L += limitations(res)
    if dry:
        L += [f"{summarize_partA.DRY_LABEL}. None of the numbers above is a Raspberry Pi measurement.", ""]
    return "\n".join(L)


def limitations(res):
    m = res["machine"]
    info = (res["build"] or {}).get("info") or {}
    core = res["core"] or m["cpu_model"]
    L = ["## Limitations", ""]
    L.append(f"- One machine: {m['model'] or m['cpu_model']}" + (" (a dry run, not a Pi)." if res["label"] ==
                                                                  summarize_partA.DRY_LABEL else "."))
    L.append(f"- Core class: the {core} is an out-of-order core. The papers' figures are for their slowest "
             "class, an in-order Cortex-A8 at 800 MHz. These results do not show what a Cortex-A8 would measure.")
    L.append("- Prover: Longfellow-zk. It is open source (Apache-2.0), zero-knowledge, needs no trusted setup, "
             "proves the full chained SHA-256 of one message, and builds from a pinned commit. Hekate, the "
             "system the papers cite, has a closed prover binary; it is not part of this run.")
    L.append(f"- Zero-knowledge: on in every proof (Ligero rate 7, 132 queries; Longfellow's source states "
             f"about 109 bits of statistical security).")
    L.append("- Setup: circuit construction is not included in the prover time. It is reported separately in "
             "partB_summary.md. Setup rows that ran with swap are labelled \"setup with swap, not comparable\".")
    if info.get("no_pmull_build_changes"):
        L.append("- PMULL fallback: this CPU has no PMULL. In GF(2^128), Longfellow multiplies with its NEON "
                 "fallback (8-bit polynomial multiplies) in place of 64-bit PMULL. GF(2^128) proving is "
                 "therefore slower here than on a core of the same class with PMULL. The size of that "
                 "slowdown is not measured: this board cannot run the PMULL path. The Fp64_2 field does not "
                 "use PMULL.")
    if info.get("wide_label_build_change"):
        L.append("- Circuit file format: built with 4-byte wire labels (Longfellow's format uses 3), so that "
                 "larger circuits can be saved. This changes the file format only, not the proof.")
    L.append("- Statement: H is public and the length of M is fixed by the circuit, as in Hekate's statement. "
             "Longfellow's own SHA-256 benchmark marks no input public, so its published figures prove a "
             "different statement; this run uses its own circuit.")
    L.append("- Threads: one, pinned, to match the single-core hash in Part A.")
    if any(p.get("swap_active") for p in res["prove"]):
        L.append("- Swap: some prove runs started with swap active (--allow-active-swap, for a machine "
                 "without sudo). Any run during which a page was swapped in or out is counted as failed.")
    methods = sorted({r.get("peak_rss_method") for r in res["prove"] + res["setup"] if r.get("peak_rss_method")})
    if methods:
        L.append("- Peak memory method: " + "; ".join(methods) + ".")
    L.append("- Root of unity: for Fp64_2 the driver uses the root 2752994695033296049 with order 2^29. "
             "Longfellow's BM_ShaZK_Fp64_2 benchmark passes order 2^32, with which an honest proof is rejected.")
    L.append("- Plain hash: M is in RAM; no disk reads.")
    failed = [p for p in res["prove"] if not p["ok"]] + [s for s in res["setup"] if not s["ok"]]
    if failed or res["stops"]:
        L.append("- Failures and stops:")
        for r in failed:
            L.append(f"  - {r['field']}, {size_label(r['message_bytes'])}: {failure_text(r)} "
                     f"(raw log `{r['raw_file']}`).")
        for s in res["stops"]:
            L.append(f"  - {s['field']}, {size_label(s['message_bytes'])}: stopped, {s['reason']}.")
    else:
        L.append("- Failures: none in this run.")
    L.append("")
    return L


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_id")
    ap.add_argument("--field", choices=("gf2_128", "fp64_2"))
    a = ap.parse_args()
    for p in summarize(a.run_id, a.field):
        print(os.path.relpath(p, HERE))

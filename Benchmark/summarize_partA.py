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

"""Build the Part A JSON and Markdown results from the raw logs of one run.

Every number written here is computed from the raw samples in
results/raw/partA_<run_id>_<variant>.jsonl. Nothing else is read.

Usage: python3 summarize_partA.py RUN_ID
"""

import datetime
import json
import math
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
RAW = os.path.join(RESULTS, "raw")

DRY_LABEL = "DRY RUN, NOT PI"
DRY_TAG = "DRY_RUN_NOT_PI"

# Claims from the papers, in milliseconds.
CLAIM_ENCRYPTION = (2.0, 10.0)        # Protocol paper; Integration section 8.1
CLAIM_HASH_SOFTWARE = (430.0, 600.0)  # Integration section 8.2, Cortex-A8 at 800 MHz
CLAIM_HASH_ARMV8 = (120.0, 170.0)     # Integration section 8.2
CLAIM_CPB_SOFTWARE = 13.7             # eBACS figure the 430-600 ms range is built on


def stats_ms(samples_ns):
    xs = sorted(s / 1e6 for s in samples_ns)
    n = len(xs)
    p95 = xs[max(0, math.ceil(0.95 * n) - 1)]
    return {
        "n": n,
        "min_ms": xs[0],
        "median_ms": statistics.median(xs),
        "mean_ms": statistics.fmean(xs),
        "p95_ms": p95,
        "std_ms": statistics.stdev(xs) if n > 1 else 0.0,
    }


def read_raw(path):
    header, meta, after, selftests, rows, other = None, None, None, [], [], []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                other.append(line)
                continue
            t = obj.get("type")
            if t == "header":
                header = obj
            elif t == "meta":
                meta = obj
            elif t == "driver_after":
                after = obj
            elif t in ("selftest", "selftest_summary"):
                selftests.append(obj)
            elif t == "row":
                rows.append(obj)
            else:
                other.append(obj)
    return header, meta, after, selftests, rows, other


def parse_throttled(s):
    if not s:
        return None
    m = re.search(r"0x([0-9a-fA-F]+)", s)
    return int(m.group(1), 16) if m else None


def throttle_flag(before, after):
    """THROTTLED if a current throttle bit is set after the run, or a sticky bit appeared during it."""
    b = parse_throttled((before or {}).get("vcgencmd_get_throttled"))
    a = parse_throttled((after or {}).get("vcgencmd_get_throttled"))
    if a is None:
        return "unknown (vcgencmd not available)"
    if (a & 0xF) or ((a & ~(b or 0)) & 0xF0000):
        return "THROTTLED"
    return "not throttled"


def freq_hz(state):
    """Frequency of the pinned core from a before/after snapshot, in Hz, and its source."""
    if not state:
        return None, None
    khz = state.get("scaling_cur_freq_khz")
    if khz:
        return khz * 1000.0, "scaling_cur_freq"
    arm = state.get("vcgencmd_measure_clock_arm")
    if arm:
        m = re.search(r"=(\d+)", arm)
        if m:
            return float(m.group(1)), "vcgencmd measure_clock arm"
    mhz = state.get("proc_cpuinfo_mhz")
    if mhz:
        return mhz * 1e6, "/proc/cpuinfo cpu MHz"
    return None, None


def range_label(rel):
    return {
        "inside": "within range",
        "below": "below range (faster than calculated)",
        "above": "above range (slower than calculated)",
    }[rel]


def path_label(machine, variant, name):
    """Code path for a row's SHA-256 work.

    OpenSSL 3.0 dispatch, crypto/sha/asm/sha512-armv8.pl (aarch64): SHA extensions if present,
    else NEON if present, else scalar. sha256-x86_64.pl (x86-64): SHA-NI, else AVX2, AVX or SSSE3,
    else scalar. OPENSSL_armcap=0 and OPENSSL_ia32cap=0x0:0x0 clear every capability bit.
    """
    if "libsodium" in name:
        return "libsodium crypto_hash_sha256 (portable C)"
    features = set((machine.get("cpu_features") or "").split())
    arch = machine["arch"]
    if variant == "caps_off":
        env = "OPENSSL_armcap=0" if arch == "aarch64" else "OPENSSL_ia32cap=0x0:0x0"
        return f"OpenSSL capabilities off (scalar, {env})"
    if arch == "aarch64":
        if "sha2" in features:
            return "OpenSSL default (ARMv8 SHA extensions)"
        if "asimd" in features:
            return "OpenSSL default (NEON, no SHA extensions)"
        return "OpenSSL default (scalar, no NEON)"
    if arch == "x86_64":
        if "sha_ni" in features:
            return "OpenSSL default (SHA-NI)"
        return "OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI)"
    return "OpenSSL default"


def relation(value, lo, hi):
    if value < lo:
        return "below"
    if value > hi:
        return "above"
    return "inside"


def fmt(x, nd=3):
    if x is None:
        return "n/a"
    if abs(x) >= 100:
        return f"{x:.1f}"
    if abs(x) >= 1:
        return f"{x:.3f}"
    return f"{x:.{nd + 1}g}"


def core_name(model):
    if model.startswith("Raspberry Pi 4 Model B"):
        return "Cortex-A72 at 1.5 GHz"
    if model.startswith("Raspberry Pi 5"):
        return "Cortex-A76 at 2.4 GHz"
    return None


def unique_path(path):
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 2
    while os.path.exists(f"{base}_{i}{ext}"):
        i += 1
    return f"{base}_{i}{ext}"


def summarize(run_id):
    files = sorted(
        os.path.join(RAW, f) for f in os.listdir(RAW)
        if f.startswith(f"partA_{run_id}_") and f.endswith(".jsonl")
    )
    if not files:
        raise SystemExit(f"no raw logs for run {run_id} in {RAW}")

    variants = []
    machine = None
    for path in files:
        header, meta, after, selftests, rows, other = read_raw(path)
        if header is None:
            raise SystemExit(f"{path}: no header line")
        machine = machine or header["machine"]
        summary = next((s for s in selftests if s["type"] == "selftest_summary"), None)
        passed = bool(summary and summary.get("pass"))
        variants.append({
            "raw_file": os.path.relpath(path, HERE),
            "variant": header["variant"],
            "variant_description": header["variant_description"],
            "env": header["env"],
            "command": header["command"],
            "before": header["before"],
            "after": (after or {}).get("after"),
            "exit_code": (after or {}).get("exit_code"),
            "stderr": (after or {}).get("stderr", ""),
            "meta": meta,
            "selftests": selftests,
            "selftest_pass": passed,
            "throttle": throttle_flag(header["before"], (after or {}).get("after")),
            "rows": rows if passed else [],
            "rows_discarded_failed_selftest": 0 if passed else len(rows),
            "failed_rows": [r for r in rows if r.get("status") != "ok"],
        })

    order = {"default": 0, "caps_off": 1}
    variants.sort(key=lambda v: order.get(v["variant"], 9))

    dry = not machine["is_pi"]
    label = DRY_LABEL if dry else machine["model"]
    sha_ext = machine["sha_extensions"]
    arch = machine["arch"]
    sha_flag_name = "sha2" if arch == "aarch64" else "sha_ni"

    # Statistics for every ok row.
    out_rows = []
    for v in variants:
        f_hz = [x for x in (freq_hz(v["before"])[0], freq_hz(v["after"] or {})[0]) if x]
        f_src = freq_hz(v["before"])[1]
        for r in v["rows"]:
            if r.get("status") != "ok":
                continue
            s = stats_ms(r["samples_ns"])
            row = {
                "variant": v["variant"],
                "part": r["part"],
                "name": r["name"],
                "description": r["description"],
                "impl": r["impl"],
                "bytes": r["bytes"],
                "warmup": r["warmup"],
                **s,
                "throttle": v["throttle"],
                "raw_file": v["raw_file"],
            }
            if r["part"] == "A1" and r["bytes"]:
                if r.get("cycles"):
                    row["cycles_per_byte"] = statistics.median(r["cycles"]) / r["bytes"]
                    row["cycles_per_byte_method"] = "perf_event_open cycle counter, user space, median sample"
                elif f_hz:
                    hz = statistics.fmean(f_hz)
                    row["cycles_per_byte"] = s["median_ms"] / 1e3 * hz / r["bytes"]
                    row["cycles_per_byte_method"] = (
                        f"median time x clock frequency ({f_src}, mean of before and after: {hz / 1e6:.0f} MHz)")
                else:
                    row["cycles_per_byte"] = None
                    row["cycles_per_byte_method"] = "not available: no cycle counter and no frequency reading"
            out_rows.append(row)

    def find(variant, name, nbytes=None):
        for r in out_rows:
            if r["variant"] == variant and r["name"] == name and (nbytes is None or r["bytes"] == nbytes):
                return r
        return None

    # Path for each A1 row, and whether the capability switch changed the timing.
    path_check = None
    d30 = find("default", "sha256_file_openssl", 30000000)
    o30 = find("caps_off", "sha256_file_openssl", 30000000)
    if d30 and o30:
        ratio = o30["median_ms"] / d30["median_ms"]
        path_check = {
            "median_default_ms": d30["median_ms"],
            "median_caps_off_ms": o30["median_ms"],
            "ratio_caps_off_over_default": ratio,
            "time_changed": abs(ratio - 1.0) > 0.05,
        }
    for r in out_rows:
        r["path"] = path_label(machine, r["variant"], r["name"])

    # Sanity check: the whole capture contains the 30,000,000 B hash, so its median should not be lower.
    sanity = []
    for variant, whole_name, hash_name in (
            ("default", "whole_capture_openssl", "sha256_file_openssl"),
            ("caps_off", "whole_capture_openssl", "sha256_file_openssl"),
            ("default", "whole_capture_libsodium", "sha256_file_libsodium")):
        w = find(variant, whole_name)
        h = find(variant, hash_name, 30000000)
        if not (w and h):
            continue
        flagged = w["median_ms"] < h["median_ms"]
        if flagged:
            w["sanity_flag"] = True
        sanity.append({
            "variant": variant,
            "whole_capture_row": whole_name,
            "hash_row": f"{hash_name} 30000000 B",
            "whole_capture_median_ms": w["median_ms"],
            "hash_median_ms": h["median_ms"],
            "flag": "SANITY FLAG" if flagged else "ok",
        })

    # Claims. Each comparison names the row it uses.
    def compare(r, rng):
        return {
            "row": r["name"],
            "variant": r["variant"],
            "bytes": r["bytes"],
            "path": r["path"] if r["part"] in ("A1", "A5") else r["impl"],
            "median_ms": r["median_ms"],
            "cycles_per_byte": r.get("cycles_per_byte"),
            "label": range_label(relation(r["median_ms"], *rng)),
            "throttled": r["throttle"] == "THROTTLED",
        }

    claims = []
    seven = find("default", "ecies_seven_layers")
    claims.append({
        "claim": "2 to 10 ms for encryption",
        "source": "Protocol paper; Integration section 8.1",
        "comparisons": [compare(seven, CLAIM_ENCRYPTION)] if seven else [],
        "not_tested": None if seven else "the ecies_seven_layers row is missing",
    })

    sw_rows = [r for r in (
        d30 if not sha_ext else None,
        o30,
        find("default", "sha256_file_libsodium", 30000000),
    ) if r]
    claims.append({
        "claim": "430 to 600 ms for hashing a 30 MB file without hardware extensions",
        "source": "Integration section 8.2",
        "comparisons": [compare(r, CLAIM_HASH_SOFTWARE) for r in sw_rows],
        "not_tested": None if sw_rows else "no 30,000,000 B row without SHA extensions",
        "note": (f"The calculation assumes {CLAIM_CPB_SOFTWARE} cycles/byte on a Cortex-A8 at 800 MHz. "
                 "Cycles per byte do not depend on the clock and are the closer comparison."),
    })
    if sha_ext and d30:
        c = compare(d30, CLAIM_HASH_ARMV8)
        if not (path_check and path_check["time_changed"]):
            c["label"] += "; path change NOT VERIFIED"
        claims.append({
            "claim": "120 to 170 ms with ARMv8 crypto extensions",
            "source": "Integration section 8.2",
            "comparisons": [c],
            "not_tested": None,
        })
    else:
        claims.append({
            "claim": "120 to 170 ms with ARMv8 crypto extensions",
            "source": "Integration section 8.2",
            "comparisons": [],
            "not_tested": f"the CPU feature list has no {sha_flag_name}, so no run used SHA extensions",
        })

    now = datetime.datetime.now(datetime.timezone.utc)
    result = {
        "label": label,
        "run_id": run_id,
        "generated_utc": now.isoformat(timespec="seconds"),
        "machine": machine,
        "core": core_name(machine["model"]),
        "sha_extensions_present": sha_ext,
        "sha_path_check": path_check,
        "sanity_checks": sanity,
        "variants": [{k: val for k, val in v.items() if k not in ("rows",)} for v in variants],
        "rows": out_rows,
        "claims": claims,
    }

    host = re.sub(r"[^A-Za-z0-9_.-]", "_", machine["hostname"])
    date = run_id.split("T")[0]
    date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
    stem = f"partA_{DRY_TAG}_{date}_{host}" if dry else f"partA_{date}_{host}"
    json_path = unique_path(os.path.join(RESULTS, stem + ".json"))
    text = json.dumps(result, indent=2)
    text = text.replace('{\n  "label"', '{"label"', 1)  # label on the first line
    with open(json_path, "x") as f:
        f.write(text + "\n")

    md_path = os.path.join(RESULTS, f"partA_summary_{DRY_TAG}.md" if dry else "partA_summary.md")
    with open(md_path, "w") as f:
        f.write(render_md(result, os.path.relpath(json_path, HERE)))
    return json_path, md_path


def render_md(res, json_rel):
    m = res["machine"]
    dry = res["label"] == DRY_LABEL
    L = []
    if dry:
        L.append(DRY_LABEL)
        L.append("")
        L.append("# Part A summary (dry run)")
        L.append("")
        L.append(f"This run is not from a Raspberry Pi. The machine reports `{m['model'] or m['cpu_model']}`. "
                 "These numbers test the code path only and must not be cited as Pi results.")
    else:
        L.append(f"# Part A summary: {m['model']}")
        L.append("")
        L.append(f"Measured on a {m['model']}, {res['core']}.")
    L.append("")
    L.append(f"- Run: `{res['run_id']}`. Generated {res['generated_utc']} from the raw logs below. "
             f"Full data: `{json_rel}`.")
    L.append(f"- CPU: {m['cpu_model']}, {m['arch']}, {m['cpu_count']} cores. "
             f"Measured max frequency of the pinned core: {fmt_khz(m.get('cpuinfo_max_freq_khz'))}.")
    if res["core"] and m.get("cpuinfo_max_freq_khz") and abs(m["cpuinfo_max_freq_khz"] - 1500000) > 1000 \
            and m["model"].startswith("Raspberry Pi 4"):
        L.append(f"- Note: the core is named here as {res['core']}, but this board reports a maximum of "
                 f"{fmt_khz(m['cpuinfo_max_freq_khz'])}.")
    L.append(f"- CPU features: {m['cpu_features']}")
    L.append(f"- RAM: {m['mem_total_kb'] / 1048576:.2f} GiB. OS: {m['os']}. Kernel: {m['uname']}.")
    L.append(f"- Pinned to core {m['pinned_cpu']} with taskset. Governor before the run: {m['governor_before']}. "
             f"Governor during the run: {m['governor_during']}.")
    v0 = res["variants"][0]
    meta = v0.get("meta") or {}
    L.append(f"- Compiler: gcc {meta.get('compiler')}, flags `{meta.get('cflags')}`. "
             f"OpenSSL {meta.get('openssl_runtime')}. libsodium {meta.get('libsodium')}.")
    L.append(f"- Clock: {meta.get('clock')}. Cycle counter: {meta.get('cycle_counter')}.")
    L.append("")

    L.append("## Runs")
    L.append("")
    L.append("| Variant | Environment | Self-tests | Throttle | Temp before | Temp after | Exit | Raw log |")
    L.append("|---|---|---|---|---|---|---|---|")
    for v in res["variants"]:
        env = ", ".join(f"{k}={val}" for k, val in v["env"].items()) or "unchanged"
        L.append(f"| {v['variant']} | {env} | {'pass' if v['selftest_pass'] else 'FAIL'} | {v['throttle']} | "
                 f"{(v['before'] or {}).get('vcgencmd_measure_temp') or 'n/a'} | "
                 f"{(v['after'] or {}).get('vcgencmd_measure_temp') or 'n/a'} | {v['exit_code']} | "
                 f"`{v['raw_file']}` |")
    L.append("")
    failures = [v for v in res["variants"] if not v["selftest_pass"] or v["exit_code"] != 0 or v["failed_rows"]]
    throttled = [v for v in res["variants"] if v["throttle"] == "THROTTLED"]
    if failures:
        L.append("Failures:")
        for v in failures:
            if not v["selftest_pass"]:
                L.append(f"- {v['variant']}: self-tests failed. No timing from this run is reported.")
            if v["exit_code"] != 0:
                L.append(f"- {v['variant']}: exit code {v['exit_code']}. stderr: `{v['stderr'].strip()[:300]}`")
            for r in v["failed_rows"]:
                L.append(f"- {v['variant']}: row {r.get('name')} failed: {r.get('error')}")
        L.append("")
    if throttled:
        L.append("THROTTLED: " + ", ".join(v["variant"] for v in throttled)
                 + ". Rows from these runs carry the THROTTLED flag.")
        L.append("")

    L.append("## Results")
    L.append("")
    L.append("Times in milliseconds. n is the number of timed repeats after warm-up.")
    L.append("")
    if not res["sha_extensions_present"]:
        flag = "sha2" if m["arch"] == "aarch64" else "sha_ni"
        L.append(f"The CPU feature list has no `{flag}`. No row used SHA extensions, so the rows "
                 "\"with SHA extensions\" are not reported.")
        L.append("")
    pc = res["sha_path_check"]
    if pc:
        L.append(f"Capability switch check, 30,000,000 B: OpenSSL default median {fmt(pc['median_default_ms'])} ms, "
                 f"capabilities off {fmt(pc['median_caps_off_ms'])} ms, ratio {pc['ratio_caps_off_over_default']:.3f}. "
                 f"The time {'changed' if pc['time_changed'] else 'did not change'} by more than 5%.")
        L.append("")
    L.append("| Part | Row | Path or implementation | Bytes | n | min | median | mean | p95 | std | cycles/byte | Flag |")
    L.append("|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for r in res["rows"]:
        path = r.get("path") if r["part"] in ("A1", "A5") else (
            r["impl"] + ("" if r["variant"] == "default" else "; OpenSSL capabilities off"))
        cpb = f"{r['cycles_per_byte']:.2f}" if r.get("cycles_per_byte") else ""
        flag = " ".join(f for f, on in (("THROTTLED", r["throttle"] == "THROTTLED"),
                                        ("SANITY FLAG", r.get("sanity_flag"))) if on)
        L.append(f"| {r['part']} | {r['name']} | {path} | {r['bytes'] or ''} | {r['n']} | {fmt(r['min_ms'])} | "
                 f"{fmt(r['median_ms'])} | {fmt(r['mean_ms'])} | {fmt(r['p95_ms'])} | {fmt(r['std_ms'])} | {cpb} | "
                 f"{flag} |")
    L.append("")
    methods = sorted({r["cycles_per_byte_method"] for r in res["rows"] if r.get("cycles_per_byte_method")})
    if methods:
        L.append("Cycles per byte method: " + "; ".join(methods) + ".")
        L.append("")

    L.append("## Sanity checks")
    L.append("")
    L.append("The whole capture contains the 30,000,000 B hash plus the other work, so its median should not be "
             "lower than the hash-only median from the same run.")
    L.append("")
    for s in res["sanity_checks"]:
        line = (f"- {s['flag']}: {s['variant']}, {s['whole_capture_row']} median "
                f"{fmt(s['whole_capture_median_ms'])} ms; {s['hash_row']} median {fmt(s['hash_median_ms'])} ms.")
        if s["flag"] != "ok":
            line += (" The whole capture is lower. This points to variation between the two rows, such as a "
                     "clock change or other load. Treat both rows with caution.")
        L.append(line)
    if not res["sanity_checks"]:
        L.append("- No pair of rows was available.")
    L.append("")

    L.append("## The papers' claims")
    L.append("")
    L.append("Each comparison uses the median of the named row. The labels are \"within range\", "
             "\"below range (faster than calculated)\" and \"above range (slower than calculated)\".")
    L.append("")
    for c in res["claims"]:
        L.append(f"- \"{c['claim']}\" ({c['source']}):")
        if c["not_tested"]:
            L.append(f"  - Not tested: {c['not_tested']}.")
        for x in c["comparisons"]:
            size = f", {x['bytes']:,} B" if x["bytes"] else ""
            cpb = f", {x['cycles_per_byte']:.2f} cycles/byte" if x.get("cycles_per_byte") else ""
            throttled = " From a THROTTLED run." if x["throttled"] else ""
            L.append(f"  - Row `{x['row']}`{size}, variant `{x['variant']}`, {x['path']}: median "
                     f"{fmt(x['median_ms'])} ms{cpb}. {x['label'][0].upper() + x['label'][1:]}.{throttled}")
        if c.get("note"):
            L.append(f"  - {c['note']}")
    L.append("")
    core = res["core"] or m["cpu_model"]
    L.append(f"The papers' calculated figures are for their slowest hardware class, a Cortex-A8 at 800 MHz. "
             f"This core ({core}) is faster than that class, so these results do not confirm the "
             "slowest-class figures.")
    L.append("")
    if dry:
        L.append(f"{DRY_LABEL}. None of the numbers above is a Raspberry Pi measurement.")
        L.append("")
    return "\n".join(L)


def fmt_khz(khz):
    return f"{khz / 1000:.0f} MHz" if khz else "not available"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    j, m = summarize(sys.argv[1])
    print(j)
    print(m)

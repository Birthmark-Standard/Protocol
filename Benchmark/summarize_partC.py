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

"""Build the Part C JSON and Markdown results from the raw log of one run.

Every timing written here is computed from the raw samples in
results/raw/partC_<run_id>_default.jsonl. The comparison file also reads
one Part A results JSON, named with --partA-json, and takes Part A's rows
from it as they are.

Usage: python3 summarize_partC.py RUN_ID [--partA-json PATH]
"""

import argparse
import datetime
import json
import os
import re

import summarize_partA as A

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
RAW = os.path.join(RESULTS, "raw")

DRY_LABEL = A.DRY_LABEL
DRY_TAG = A.DRY_TAG

# Repeat minimums by the row's measured median.
CLASSES = (("under 5 ms", 5.0, 2000), ("5 to 100 ms", 100.0, 200), ("over 100 ms", float("inf"), 50))
DESIGN_TOKENS = "blind-signed tokens"
DESIGN_DAA = "DAA or EPID signature"
PRIMARY_VARIANT = "RSABSSA-SHA384-PSS-Deterministic"
FILE_BYTES = 30000000
BATCH = 20


def repeat_class(median_ms):
    for name, upper, minimum in CLASSES:
        if median_ms < upper:
            return name, minimum
    return CLASSES[-1][0], CLASSES[-1][2]


def read_raw(path):
    out = {"header": None, "meta": None, "after": None, "selftests": [], "rows": [], "sizes": [], "other": []}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                out["other"].append(line)
                continue
            t = obj.get("type")
            if t == "header":
                out["header"] = obj
            elif t == "meta":
                out["meta"] = obj
            elif t == "driver_after":
                out["after"] = obj
            elif t in ("selftest", "selftest_summary"):
                out["selftests"].append(obj)
            elif t == "row":
                out["rows"].append(obj)
            elif t == "size":
                out["sizes"].append(obj)
            else:
                out["other"].append(obj)
    return out


def summarize(run_id, partA_json=None):
    path = os.path.join(RAW, f"partC_{run_id}_default.jsonl")
    if not os.path.exists(path):
        raise SystemExit(f"no raw log {path}")
    raw = read_raw(path)
    header = raw["header"]
    if header is None:
        raise SystemExit(f"{path}: no header line")
    machine = header["machine"]
    dry = not machine["is_pi"]

    # Check the Part A file before writing anything.
    partA = None
    if partA_json:
        with open(partA_json) as f:
            partA = json.load(f)
        partA_dry = partA.get("label") == DRY_LABEL
        if partA_dry != dry:
            raise SystemExit(
                f"refusing to combine: this Part C run is {'a dry run' if dry else 'from a Raspberry Pi'}, "
                f"and {partA_json} is {'a dry run' if partA_dry else 'from a Raspberry Pi'}")

    summary = next((s for s in raw["selftests"] if s["type"] == "selftest_summary"), None)
    passed = bool(summary and summary.get("pass"))
    after = (raw["after"] or {}).get("after")
    throttle = A.throttle_flag(header["before"], after)

    rows, rejected = [], []
    for r in (raw["rows"] if passed else []):
        if r.get("status") != "ok":
            rejected.append({"name": r.get("name"), "scheme": r.get("scheme"), "reason": r.get("error", "failed")})
            continue
        s = A.stats_ms(r["samples_ns"])
        cls, minimum = repeat_class(s["median_ms"])
        row = {k: r.get(k) for k in ("design", "scheme", "name", "variant", "params", "security", "description",
                                     "impl", "bytes", "warmup", "repeat_class")}
        row.update(s)
        row["measured_class"] = cls
        row["repeat_minimum"] = minimum
        row["throttle"] = throttle
        row["raw_file"] = os.path.relpath(path, HERE)
        if s["n"] < minimum:
            rejected.append({"name": row["name"], "scheme": row["scheme"],
                             "reason": f"n = {s['n']} is below the minimum of {minimum} for a row {cls}"})
            continue
        rows.append(row)

    now = datetime.datetime.now(datetime.timezone.utc)
    result = {
        "label": DRY_LABEL if dry else machine["model"],
        "run_id": run_id,
        "generated_utc": now.isoformat(timespec="seconds"),
        "machine": machine,
        "core": A.core_name(machine["model"]),
        "raw_file": os.path.relpath(path, HERE),
        "command": header["command"],
        "build_info": header.get("build_info"),
        "before": header["before"],
        "after": after,
        "exit_code": (raw["after"] or {}).get("exit_code"),
        "stderr": (raw["after"] or {}).get("stderr", ""),
        "throttle": throttle,
        "meta": raw["meta"],
        "selftests": raw["selftests"],
        "selftest_pass": passed,
        "rows": rows,
        "rows_rejected": rejected,
        "rows_discarded_failed_selftest": 0 if passed else len(raw["rows"]),
        "sizes": raw["sizes"] if passed else [],
        "token_spend": "no operation",
    }

    host = re.sub(r"[^A-Za-z0-9_.-]", "_", machine["hostname"])
    date = run_id.split("T")[0]
    date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
    stem = f"partC_{DRY_TAG}_{date}_{host}" if dry else f"partC_{date}_{host}"
    json_path = A.unique_path(os.path.join(RESULTS, stem + ".json"))
    text = json.dumps(result, indent=2).replace('{\n  "label"', '{"label"', 1)
    with open(json_path, "x") as f:
        f.write(text + "\n")
    json_rel = os.path.relpath(json_path, HERE)

    md_path = os.path.join(RESULTS, f"partC_summary_{DRY_TAG}.md" if dry else "partC_summary.md")
    with open(md_path, "w") as f:
        f.write(render_summary(result, json_rel))

    cmp_path = None
    if partA is not None:
        cmp_path = os.path.join(RESULTS, f"partC_comparison_{DRY_TAG}.md" if dry else "partC_comparison.md")
        with open(cmp_path, "w") as f:
            f.write(render_comparison(result, json_rel, partA, partA_json))
    return json_path, md_path, cmp_path


# ---------------------------------------------------------------------------

fmt = A.fmt


def daa_schemes(res):
    meta = res["meta"] or {}
    measured = {s["scheme"] for s in res["sizes"]}
    return [d for d in meta.get("daa", []) if d["scheme"] in measured]


def scheme_line(daa):
    if not daa:
        return "DAA or EPID scheme measured: none. No DAA or EPID signature row passed."
    parts = []
    for i, d in enumerate(daa):
        lead = "DAA or EPID scheme measured" if i == 0 else "Also measured"
        if d["kind"] in ("DAA", "EPID"):
            parts.append(f"{lead}: {d['scheme']} ({d['library']}). It is {d['kind']}.")
        else:
            parts.append(f"{lead}: {d['scheme']} ({d['library']}). It is not DAA or EPID: it is {d['kind']}.")
    return " ".join(parts)


def not_daa_lines(daa):
    return [f"The scheme measured is not DAA or EPID. It is {d['kind']}: {d['scheme']}."
            for d in daa if d["kind"] not in ("DAA", "EPID")]


def machine_line(m, core):
    if m["is_pi"]:
        return f"Machine: {m['model']}, {core}. Host `{m['hostname']}`."
    name = f"`{m['model']}`, {m['cpu_model']}" if m["model"] else m["cpu_model"]
    return f"Machine: {name}, {m['arch']}, host `{m['hostname']}`. This is not a Raspberry Pi."


def render_summary(res, json_rel):
    m = res["machine"]
    dry = res["label"] == DRY_LABEL
    daa = daa_schemes(res)
    L = []
    if dry:
        L += [DRY_LABEL, ""]
    L += not_daa_lines(daa)
    if not_daa_lines(daa):
        L.append("")
    L += ["# Part C summary" + (" (dry run)" if dry else f": {m['model']}"), ""]
    if dry:
        L += [f"This run is not from a Raspberry Pi. These numbers test the code path only and must not be cited "
              "as Pi results.", ""]
    L.append(f"- {machine_line(m, res['core'])}")
    L.append(f"- Run: `{res['run_id']}`. Generated {res['generated_utc']} from `{res['raw_file']}`. "
             f"Full data: `{json_rel}`.")
    L.append(f"- CPU features: {m['cpu_features']}")
    L.append(f"- Pinned to core {m['pinned_cpu']} with taskset. Governor before the run: {m['governor_before']}. "
             f"Governor during the run: {m['governor_during']}.")
    meta = res["meta"] or {}
    L.append(f"- Compiler: gcc {meta.get('compiler')}, flags `{meta.get('cflags')}`. "
             f"OpenSSL {meta.get('openssl_runtime')}. libsodium {meta.get('libsodium')}.")
    for lib in (res.get("build_info") or {}).get("libraries", []):
        L.append(f"- {lib['name']} `{lib['commit']}` ({lib['license']}): {lib['build']}.")
    L.append(f"- Temperature before {(res['before'] or {}).get('vcgencmd_measure_temp') or 'n/a'}, "
             f"after {(res['after'] or {}).get('vcgencmd_measure_temp') or 'n/a'}. Throttle: {res['throttle']}. "
             f"Exit code {res['exit_code']}.")
    L.append("")
    L.append(scheme_line(daa))
    L.append("")

    L += ["## Correctness tests", ""]
    for t in res["selftests"]:
        if t["type"] == "selftest":
            L.append(f"- {'pass' if t['pass'] else 'FAIL'}: `{t['name']}`. {t['detail']}")
    if not res["selftest_pass"]:
        L += ["", "A correctness test failed. No timing from this run is reported."]
    L.append("")
    if res["rows_rejected"]:
        L += ["Rows not reported:"]
        for r in res["rows_rejected"]:
            L.append(f"- `{r['name']}` ({r.get('scheme') or ''}): {r['reason']}.")
        L.append("")
    if res["throttle"] == "THROTTLED":
        L += ["THROTTLED: every row of this run carries the flag.", ""]

    L += ["## Results", "",
          "Times in milliseconds. n is the number of timed repeats after warm-up. The repeat minimum is 2,000 for "
          "a row under 5 ms, 200 for a row of 5 to 100 ms and 50 for a slower row, by the row's measured median.",
          ""]
    for design in (DESIGN_TOKENS, DESIGN_DAA):
        rows = [r for r in res["rows"] if r["design"] == design]
        L += [f"### {design[0].upper() + design[1:]}", ""]
        L.append("| Row | Scheme | Variant | Modulus or curve | Stated security | Bytes | n | min | median | mean | "
                 "p95 | std |")
        L.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|")
        for r in rows:
            flag = " THROTTLED" if r["throttle"] == "THROTTLED" else ""
            L.append(f"| {r['name']}{flag} | {r['scheme']} | {r['variant']} | {r['params']} | {r['security']} | "
                     f"{r['bytes'] or ''} | {r['n']} | {fmt(r['min_ms'])} | {fmt(r['median_ms'])} | "
                     f"{fmt(r['mean_ms'])} | {fmt(r['p95_ms'])} | {fmt(r['std_ms'])} |")
        L.append("")
        if design == DESIGN_TOKENS:
            L += ["Token spend: no operation. The token is a stored value sent as data.", ""]
        else:
            for s in res["sizes"]:
                L.append(f"- {s['scheme']} signature size: {s['bytes']} B ({s['description']}).")
            for d in daa:
                L.append(f"- {d['scheme']}, `member_key_generation`: {d['keygen']}.")
            L.append("")
    L += ["Row descriptions:", ""]
    seen = set()
    for r in res["rows"]:
        if (r["name"], r["scheme"]) in seen:
            continue
        seen.add((r["name"], r["scheme"]))
        L.append(f"- `{r['name']}` ({r['scheme']}): {r['description']}. Implementation: {r['impl']}.")
    L.append("")
    if dry:
        L += [f"{DRY_LABEL}. None of the numbers above is a Raspberry Pi measurement.", ""]
    return "\n".join(L)


def find_partA(partA, name, nbytes=None):
    for r in partA.get("rows", []):
        if r["variant"] == "default" and r["name"] == name and (nbytes is None or r["bytes"] == nbytes):
            return r
    return None


def find_c(res, design, name, scheme=None, variant=None, params=None):
    for r in res["rows"]:
        if r["design"] == design and r["name"] == name and (scheme is None or r["scheme"] == scheme) \
                and (variant is None or r["variant"] == variant) and (params is None or r["params"] == params):
            return r
    return None


def render_comparison(res, json_rel, partA, partA_path):
    m = res["machine"]
    dry = res["label"] == DRY_LABEL
    daa = daa_schemes(res)
    pa_rel = os.path.relpath(os.path.abspath(partA_path), HERE)
    L = []
    if dry:
        L.append(DRY_LABEL)
    L.append(machine_line(m, res["core"]))
    L.append(scheme_line(daa))
    L.append("Baseline wrap count is one, from Table 5: one relay hop.")
    L += not_daa_lines(daa)
    L.append("")
    L.append("# Part C comparison" + (" (dry run)" if dry else ""))
    L.append("")
    pam = partA.get("machine", {})
    L.append(f"- Part C: run `{res['run_id']}`, `{json_rel}`.")
    L.append(f"- Part A: run `{partA.get('run_id')}`, `{pa_rel}`.")
    if pam.get("hostname") != m["hostname"] or pam.get("model") != m["model"]:
        L.append(f"- The Part A run is from host `{pam.get('hostname')}` (`{pam.get('model') or pam.get('cpu_model')}`). "
                 f"Part C is from host `{m['hostname']}`. The two runs are from different machines.")
    L.append("")
    L.append("Each line is one device operation per capture, with the measured median, the row it comes from, and "
             "the modulus or curve and its stated security level. No total is given for any design. The paper does "
             "not fully specify their packet structures.")
    L.append("")

    x25519_sec = None
    wrap = find_c(res, DESIGN_TOKENS, "ecies_wrap_one_relay_tokens")
    if wrap:
        x25519_sec = wrap["security"]
    sha = find_partA(partA, "sha256_file_openssl", FILE_BYTES)

    def line(op, r, src, curve, sec):
        med = f"{fmt(r['median_ms'])} ms" if r else "not measured"
        return f"| {op} | {med} | {src} | {curve} | {sec} |"

    hdr = ["| Operation | Median | Row | Modulus or curve | Stated security |", "|---|---:|---|---|---|"]
    sha_line = line("ContentHash = SHA-256(file)", sha,
                    f"Part A `sha256_file_openssl`, 30,000,000 B, variant `default`"
                    + (f", {sha['path']}" if sha else ""), "none (hash)", "not applicable")

    L += ["## This design", ""] + hdr + [sha_line]
    seven = find_partA(partA, "ecies_seven_layers")
    L.append(line("Seven ECIES layers", seven, "Part A `ecies_seven_layers`. Its AEAD is inside each layer.",
                  "X25519", (x25519_sec + ", read in the Part C run") if x25519_sec else "not recorded"))
    for name, op, curve, sec in (("h_metadata", "h(metadata)", "none (hash)", "not applicable"),
                                 ("fullpackethash", "FullPacketHash", "none (hash)", "not applicable"),
                                 ("enc_fullpackethash", "Enc_FullPacketHash", "AES-256-GCM, 256-bit key",
                                  "not recorded"),
                                 ("binding_hash", "binding_hash", "none (hash)", "not applicable")):
        L.append(line(op, find_partA(partA, name), f"Part A `{name}`", curve, sec))
    L.append("")

    L += ["## Blind-signed tokens", ""] + hdr + [sha_line]
    L.append(line("One relay wrap", wrap, "Part C `ecies_wrap_one_relay_tokens`", "X25519",
                  x25519_sec or "not recorded"))
    L.append("| Token spend | no operation | none | not applicable | not applicable |")
    L.append("")
    L.append(f"Issuance, not part of the capture. Blind plus finalize for a batch of {BATCH} tokens "
             f"(`rsabssa_blind_finalize_batch20`), amortized over the batch:")
    L.append("")
    L.append("| Variant | Modulus | Stated security | Batch median | Per token |")
    L.append("|---|---|---|---:|---:|")
    batches = [r for r in res["rows"] if r["name"] == "rsabssa_blind_finalize_batch20"]
    batches.sort(key=lambda r: (r["variant"] != PRIMARY_VARIANT, r["params"]))
    for r in batches:
        L.append(f"| {r['variant']} | {r['params']} | {r['security']} | {fmt(r['median_ms'])} ms | "
                 f"{fmt(r['median_ms'] / BATCH)} ms |")
    if not batches:
        L.append("| not measured | | | | |")
    L.append("")

    L += ["## DAA or EPID signature", ""]
    if not daa:
        L += ["No DAA or EPID signature row passed.", ""]
    for d in daa:
        sig = find_c(res, DESIGN_DAA, "sign", scheme=d["scheme"])
        swrap = find_c(res, DESIGN_DAA, "ecies_wrap_one_relay_sig", scheme=d["scheme"])
        size = next((s["bytes"] for s in res["sizes"] if s["scheme"] == d["scheme"]), None)
        L += [f"### {d['scheme']} ({d['kind']})", ""] + hdr + [sha_line]
        L.append(line(f"One relay wrap (signature {size} B)", swrap,
                      "Part C `ecies_wrap_one_relay_sig`", "X25519", x25519_sec or "not recorded"))
        L.append(line("Sign, anonymous mode", sig, "Part C `sign`", d["curve"], d["security"]))
        L.append("")
    if dry:
        L += [f"{DRY_LABEL}. None of the numbers above is a Raspberry Pi measurement.", ""]
    return "\n".join(L)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_id")
    ap.add_argument("--partA-json", dest="partA_json", help="Part A results JSON for the comparison file")
    a = ap.parse_args()
    for p in summarize(a.run_id, a.partA_json):
        if p:
            print(p)

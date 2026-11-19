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

"""Part C driver: run and record the credential benchmark.

    credential/fetch_and_build.sh                       # once: libraries and the program
    python3 run_partC.py --partA-json results/partA_<date>_<host>.json
    sudo python3 run_partC.py ...                       # also sets the governor to performance

One run of credential/bench_credential, pinned to one core, variant
"default" only. The raw log goes to results/raw/ and is never overwritten.
The summary files are then built from that raw log (summarize_partC.py).
With --partA-json, the comparison file is written too.

Only standard-library Python 3.9 or later is used.
"""

import argparse
import datetime
import json
import os
import shutil
import subprocess

import run_partA as A
import summarize_partC

HERE = os.path.dirname(os.path.abspath(__file__))
CRED = os.path.join(HERE, "credential")
BUILD = os.path.join(CRED, "build")
RAW = os.path.join(HERE, "results", "raw")
MINIMUMS = {"fast": 2000, "mid": 200, "slow": 50}


def read_text(path):
    try:
        with open(path) as f:
            return f.read()
    except OSError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cpu", type=int, default=3, help="core to pin to (default 3)")
    ap.add_argument("--binary", default=os.path.join(CRED, "bench_credential"))
    ap.add_argument("--no-governor", action="store_true", help="do not try to set the governor")
    ap.add_argument("--repeats-fast", type=int, default=MINIMUMS["fast"], help="rows under 5 ms (minimum 2000)")
    ap.add_argument("--repeats-mid", type=int, default=MINIMUMS["mid"], help="rows of 5 to 100 ms (minimum 200)")
    ap.add_argument("--repeats-slow", type=int, default=MINIMUMS["slow"], help="rows over 100 ms (minimum 50)")
    ap.add_argument("--rsa-bits", default="2048,3072", help="RSA moduli; 2048 is required")
    ap.add_argument("--variants", default="pss,psszero", help="pss is required; psszero is optional")
    ap.add_argument("--schemes", default="ecdaa,epid", help="DAA or EPID libraries to measure")
    ap.add_argument("--partA-json", dest="partA_json",
                    help="Part A results JSON from the same machine; writes the comparison file")
    args = ap.parse_args()

    if (args.repeats_fast < MINIMUMS["fast"] or args.repeats_mid < MINIMUMS["mid"]
            or args.repeats_slow < MINIMUMS["slow"]):
        raise SystemExit("minimum repeats: 2000 for rows under 5 ms, 200 for rows of 5 to 100 ms, "
                         "50 for slower rows")
    if "2048" not in args.rsa_bits.split(",") or "pss" not in args.variants.split(","):
        raise SystemExit("RSA-2048 and the PSS-Deterministic variant are required")

    cpu = args.cpu if args.cpu < (os.cpu_count() or 1) else (os.cpu_count() or 1) - 1
    os.makedirs(RAW, exist_ok=True)
    machine = A.machine_info(cpu)
    host = "".join(c if c.isalnum() or c in "-_." else "_" for c in machine["hostname"])
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{stamp}_{host}" + ("" if machine["is_pi"] else f"_{summarize_partC.DRY_TAG}")
    label = machine["model"] if machine["is_pi"] else summarize_partC.DRY_LABEL

    # Build. The libraries come from credential/fetch_and_build.sh. A failed build is recorded in raw/.
    info_path = os.path.join(BUILD, "credential_build_info.json")
    rc, out, err = (None, "", "") if not os.path.exists(info_path) else A.run(["make", "-C", CRED])
    if rc != 0 or not os.path.exists(args.binary):
        path = os.path.join(RAW, f"partC_{run_id}_build_failed.txt")
        reason = (f"{info_path} is missing: run credential/fetch_and_build.sh first"
                  if rc is None else f"make -C {CRED} exited {rc}")
        with open(path, "x") as f:
            f.write(f"{label}\n{reason}\n--- stdout\n{out}\n--- stderr\n{err}\n")
        raise SystemExit(f"build failed; see {path}")
    build_info = json.loads(read_text(info_path))
    build_info["epid_build_changes_diff"] = read_text(os.path.join(BUILD, "epid_build_changes.diff"))

    if args.partA_json:
        # Refuse a Pi and dry-run mix, or two different machines, before the run, not after it.
        with open(args.partA_json) as f:
            partA = json.load(f)
        partA_dry = partA.get("label") == summarize_partC.DRY_LABEL
        if partA_dry == machine["is_pi"]:
            raise SystemExit(f"refusing to combine: this machine is {'a Raspberry Pi' if machine['is_pi'] else 'not a Pi'}"
                             f", and {args.partA_json} is {'a dry run' if partA_dry else 'from a Raspberry Pi'}")
        diffs = summarize_partC.machine_differences(partA.get("machine") or {}, machine)
        if diffs:
            raise SystemExit(f"refusing to combine: this machine and {args.partA_json} differ: " + "; ".join(diffs))

    machine["governor_before"] = A.cpufreq(cpu, "scaling_governor") or "not available"
    previous, gov_status = ({}, "not attempted (--no-governor)") if args.no_governor else A.set_governor("performance")
    machine["governor_during"] = (A.cpufreq(cpu, "scaling_governor") or "not available") + f" ({gov_status})"
    taskset = shutil.which("taskset")
    machine["taskset"] = taskset or "not found; run was not pinned"

    cmd = ([taskset, "-c", str(cpu)] if taskset else []) + [
        args.binary, "--repeats-fast", str(args.repeats_fast), "--repeats-mid", str(args.repeats_mid),
        "--repeats-slow", str(args.repeats_slow), "--rsa-bits", args.rsa_bits, "--variants", args.variants,
        "--schemes", args.schemes]
    env = dict(os.environ)
    for k in ("OPENSSL_armcap", "OPENSSL_ia32cap"):
        env.pop(k, None)
    path = os.path.join(RAW, f"partC_{run_id}_default.jsonl")
    try:
        before = A.snapshot(cpu)
        header = {"type": "header", "label": label, "run_id": run_id, "variant": "default",
                  "variant_description": "library defaults; OpenSSL picks its code path from the CPU features",
                  "env": {}, "command": cmd, "machine": machine, "build_info": build_info, "before": before}
        print(f"[default] running: {' '.join(cmd)}", flush=True)
        with open(path, "x") as f:
            f.write(json.dumps(header) + "\n")
            f.flush()
            p = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True, env=env, cwd=CRED)
            after = A.snapshot(cpu)
            f.write(json.dumps({"type": "driver_after", "exit_code": p.returncode,
                                "stderr": p.stderr, "after": after}) + "\n")
        print(f"[default] exit {p.returncode}; raw log {os.path.relpath(path, HERE)}", flush=True)
    finally:
        A.restore_governor(previous)

    outputs = [p for p in summarize_partC.summarize(run_id, args.partA_json) if p]
    A.give_back_to_sudo_user([path] + outputs)
    for p in outputs:
        print(os.path.relpath(p, HERE))
    if not args.partA_json:
        print(f"No comparison file: run python3 summarize_partC.py {run_id} --partA-json PATH")


if __name__ == "__main__":
    main()

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

"""Check that a Longfellow circuit built on x86-64 loads and proves the same way on aarch64.

Runs on an x86-64 host. The aarch64 binary is the build without PMULL
(CROSS_AARCH64=1 fetch_and_build.sh), run under qemu-aarch64 -cpu cortex-a72.
For each field:

  1. Build and save the circuit on x86-64 and on aarch64. The two files must
     be byte-identical and carry the same circuit id.
  2. Load the x86-64 circuit on aarch64 and prove. All checks must pass.
  3. Prove on x86-64 with the same circuit.
  4. Verify the aarch64 proof on x86-64 and the x86-64 proof on aarch64. Each
     must be accepted, and a copy with one flipped byte rejected.

Timings under QEMU are emulated and are not results. The raw log is labelled
DRY RUN, NOT PI.

    python3 zk/longfellow/cross_arch_check.py [--bytes 1024] [--fields gf2_128 fp64_2]
"""

import argparse
import datetime
import hashlib
import json
import os
import platform
import socket
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BENCH = os.path.dirname(os.path.dirname(HERE))
BUILD = os.path.join(BENCH, "zk", "build")
RAW = os.path.join(BENCH, "results", "raw")
X86_BIN = os.path.join(BUILD, "longfellow-build", "sha256_zk_bench")
ARM_BIN = os.path.join(BUILD, "longfellow-build-aarch64", "sha256_zk_bench")
QEMU = ["qemu-aarch64", "-cpu", "cortex-a72", "-L", "/usr/aarch64-linux-gnu"]


def run(cmd, log):
    p = subprocess.run(cmd, capture_output=True, text=True)
    lines = [json.loads(x) for x in p.stdout.splitlines() if x.startswith("{")]
    log.write(json.dumps({"type": "command", "command": cmd, "exit_code": p.returncode,
                          "stderr": p.stderr[-2000:]}) + "\n")
    for x in lines:
        log.write(json.dumps({"type": "output", "command_tag": cmd[-1], "line": x}) + "\n")
    return p.returncode, lines


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def first(lines, kind):
    return next((x for x in lines if x.get("type") == kind), {})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bytes", type=int, default=1024)
    ap.add_argument("--fields", nargs="+", default=["gf2_128", "fp64_2"])
    args = ap.parse_args()

    if platform.machine() != "x86_64":
        raise SystemExit("run this check on an x86-64 host")
    for b in (X86_BIN, ARM_BIN):
        if not os.path.exists(b):
            raise SystemExit(f"missing {b}; run fetch_and_build.sh, and again with CROSS_AARCH64=1")

    work = os.path.join(BUILD, "crossarch")
    os.makedirs(work, exist_ok=True)
    os.makedirs(RAW, exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    host = "".join(c if c.isalnum() or c in "-_." else "_" for c in socket.gethostname())
    log_path = os.path.join(RAW, f"partB_crossarch_{stamp}_{host}_DRY_RUN_NOT_PI.jsonl")
    build_info = {}
    for name in ("longfellow_build_info.json", "longfellow_build_info-aarch64.json"):
        try:
            with open(os.path.join(BUILD, name)) as f:
                build_info[name] = json.load(f)
        except (OSError, ValueError):
            build_info[name] = None

    verdicts = []
    with open(log_path, "x") as log:
        log.write(json.dumps({
            "type": "header", "label": "DRY RUN, NOT PI",
            "note": "aarch64 runs are under QEMU cortex-a72; their timings are emulated and are not results",
            "host": socket.gethostname(), "uname": " ".join(platform.uname()),
            "qemu": QEMU, "bytes": args.bytes, "build_info": build_info,
        }) + "\n")
        for field in args.fields:
            n = str(args.bytes)
            c_x86 = os.path.join(work, f"{field}_{n}_x86.circuit")
            c_arm = os.path.join(work, f"{field}_{n}_arm.circuit")
            p_x86 = os.path.join(work, f"{field}_{n}_x86.proof")
            p_arm = os.path.join(work, f"{field}_{n}_arm.proof")
            base = ["--field", field, "--bytes", n]

            rc1, out1 = run([X86_BIN, *base, "--save-circuit", c_x86], log)
            rc2, out2 = run([*QEMU, ARM_BIN, *base, "--save-circuit", c_arm], log)
            same_bytes = rc1 == 0 and rc2 == 0 and sha256_file(c_x86) == sha256_file(c_arm)
            same_id = first(out1, "setup").get("circuit_id") == first(out2, "setup").get("circuit_id") \
                and bool(first(out1, "setup").get("circuit_id"))

            rc3, out3 = run([*QEMU, ARM_BIN, *base, "--load-circuit", c_x86, "--write-proof", p_arm], log)
            arm_proves = rc3 == 0 and first(out3, "done").get("all_checks_passed") is True
            rc4, out4 = run([X86_BIN, *base, "--load-circuit", c_x86, "--write-proof", p_x86], log)
            x86_proves = rc4 == 0 and first(out4, "done").get("all_checks_passed") is True

            rc5, out5 = run([X86_BIN, *base, "--load-circuit", c_x86, "--verify-proof", p_arm], log)
            x86_verifies_arm = rc5 == 0 and first(out5, "verify_file").get("all_checks_passed") is True
            rc6, out6 = run([*QEMU, ARM_BIN, *base, "--load-circuit", c_x86, "--verify-proof", p_x86], log)
            arm_verifies_x86 = rc6 == 0 and first(out6, "verify_file").get("all_checks_passed") is True

            v = {
                "type": "verdict", "field": field, "bytes": args.bytes,
                "circuit_files_byte_identical": same_bytes,
                "circuit_ids_identical": same_id,
                "aarch64_proves_with_x86_circuit": arm_proves,
                "x86_proves_with_x86_circuit": x86_proves,
                "x86_verifies_aarch64_proof": x86_verifies_arm,
                "aarch64_verifies_x86_proof": arm_verifies_x86,
            }
            v["pass"] = all(val for k, val in v.items() if isinstance(val, bool))
            log.write(json.dumps(v) + "\n")
            verdicts.append(v)
            print(json.dumps(v))

    print(os.path.relpath(log_path, BENCH))
    sys.exit(0 if all(v["pass"] for v in verdicts) else 2)


if __name__ == "__main__":
    main()

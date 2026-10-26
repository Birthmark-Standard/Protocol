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

"""Part A driver: build, run and record the device-side capture benchmark.

    python3 run_partA.py            # no governor change
    sudo python3 run_partA.py       # also sets the cpufreq governor to performance, then restores it

Two runs of the C program are made, each pinned to one core:
  default   OpenSSL picks its code path from the CPU features.
  caps_off  OpenSSL CPU capabilities switched off (OPENSSL_armcap=0 on aarch64).

Each run writes one raw log to results/raw/ that is never overwritten. The
summary files are then built from those raw logs only (summarize_partA.py).

Only standard-library Python 3.9 or later is used.
"""

import argparse
import datetime
import glob
import json
import os
import platform
import shutil
import socket
import subprocess
import sys

import summarize_partA

HERE = os.path.dirname(os.path.abspath(__file__))
DEVICE = os.path.join(HERE, "device")
RAW = os.path.join(HERE, "results", "raw")

PI_MODELS = ("Raspberry Pi 4 Model B", "Raspberry Pi 5")
ARM_PARTS = {"0xd03": "Cortex-A53", "0xd08": "Cortex-A72", "0xd0b": "Cortex-A76"}


def read(path, default=None):
    try:
        with open(path) as f:
            return f.read().strip("\x00\n ")
    except OSError:
        return default


def run(cmd, **kw):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, **kw)
        return p.returncode, p.stdout, p.stderr
    except OSError as e:
        return None, "", str(e)


def vcgencmd(*args):
    if not shutil.which("vcgencmd"):
        return None
    rc, out, err = run(["vcgencmd", *args])
    return out.strip() if rc == 0 else f"error: {err.strip()}"


def cpuinfo_fields():
    fields = {}
    text = read("/proc/cpuinfo", "")
    for line in text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields.setdefault(k.strip(), v.strip())
    return fields


def cpuinfo_mhz(cpu):
    text = read("/proc/cpuinfo", "")
    current = None
    for line in text.splitlines():
        if line.startswith("processor"):
            current = int(line.split(":")[1])
        elif line.startswith("cpu MHz") and current == cpu:
            return float(line.split(":")[1])
    return None


def int_or_none(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None


def cpufreq(cpu, name):
    return read(f"/sys/devices/system/cpu/cpu{cpu}/cpufreq/{name}")


def machine_info(pinned_cpu):
    ci = cpuinfo_fields()
    arch = platform.machine()
    model = read("/proc/device-tree/model", "") or ""
    features = ci.get("Features") or ci.get("flags") or ""
    feature_set = set(features.split())
    if arch == "aarch64":
        sha_ext = "sha2" in feature_set
    else:
        sha_ext = "sha_ni" in feature_set
    cpu_model = ci.get("model name")
    if not cpu_model:
        part = ci.get("CPU part")
        cpu_model = ARM_PARTS.get(part, f"ARM CPU part {part}") if part else "unknown"
    mem_kb = None
    swap_kb = None
    for line in (read("/proc/meminfo", "") or "").splitlines():
        if line.startswith("MemTotal:"):
            mem_kb = int(line.split()[1])
        elif line.startswith("SwapTotal:"):
            swap_kb = int(line.split()[1])
    osr = {}
    for line in (read("/etc/os-release", "") or "").splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            osr[k] = v.strip('"')
    rc, gcc, _ = run(["gcc", "--version"])
    return {
        "hostname": socket.gethostname(),
        "model": model,
        "is_pi": model.startswith(PI_MODELS),
        "arch": arch,
        "uname": " ".join(platform.uname()),
        "cpu_model": cpu_model,
        "cpu_count": os.cpu_count(),
        "cpu_features": features,
        "sha_extensions": sha_ext,
        "aes_feature": "aes" in feature_set,
        "pmull_feature": "pmull" in feature_set,
        "mem_total_kb": mem_kb,
        "swap_total_kb": swap_kb,
        "os": osr.get("PRETTY_NAME", "unknown"),
        "gcc": gcc.splitlines()[0] if rc == 0 and gcc else None,
        "pinned_cpu": pinned_cpu,
        "cpuinfo_min_freq_khz": int_or_none(cpufreq(pinned_cpu, "cpuinfo_min_freq")),
        "cpuinfo_max_freq_khz": int_or_none(cpufreq(pinned_cpu, "cpuinfo_max_freq")),
        "scaling_available_governors": cpufreq(pinned_cpu, "scaling_available_governors"),
        "perf_event_paranoid": read("/proc/sys/kernel/perf_event_paranoid"),
        "vcgencmd_version": vcgencmd("version"),
        "python": sys.version.split()[0],
    }


def snapshot(cpu):
    return {
        "time_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "scaling_governor": cpufreq(cpu, "scaling_governor"),
        "scaling_cur_freq_khz": int_or_none(cpufreq(cpu, "scaling_cur_freq")),
        "proc_cpuinfo_mhz": cpuinfo_mhz(cpu),
        "vcgencmd_measure_temp": vcgencmd("measure_temp"),
        "vcgencmd_get_throttled": vcgencmd("get_throttled"),
        "vcgencmd_measure_clock_arm": vcgencmd("measure_clock", "arm"),
    }


def set_governor(target):
    """Set every core's governor. Returns {path: previous} for restore, and a status string."""
    paths = sorted(glob.glob("/sys/devices/system/cpu/cpu[0-9]*/cpufreq/scaling_governor"))
    if not paths:
        return {}, "no cpufreq interface"
    if os.geteuid() != 0:
        return {}, "not root; governor left unchanged"
    previous = {}
    try:
        for p in paths:
            previous[p] = read(p)
            with open(p, "w") as f:
                f.write(target)
    except OSError as e:
        restore_governor(previous)
        return {}, f"could not set governor: {e}"
    return previous, f"set to {target}"


def restore_governor(previous):
    for p, g in previous.items():
        try:
            with open(p, "w") as f:
                f.write(g)
        except OSError:
            pass


def caps_off_env(arch):
    if arch == "aarch64":
        return {"OPENSSL_armcap": "0"}
    if arch == "x86_64":
        return {"OPENSSL_ia32cap": "0x0:0x0"}
    return {}


def give_back_to_sudo_user(paths):
    """Under sudo, hand the files this run created back to the invoking user."""
    uid, gid = os.environ.get("SUDO_UID"), os.environ.get("SUDO_GID")
    if os.geteuid() != 0 or not uid or not gid:
        return
    for p in paths + [RAW, os.path.dirname(RAW)]:
        try:
            os.chown(p, int(uid), int(gid))
        except OSError:
            pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cpu", type=int, default=3, help="core to pin to (default 3)")
    ap.add_argument("--binary", default=os.path.join(DEVICE, "bench_capture"))
    ap.add_argument("--no-governor", action="store_true", help="do not try to set the governor")
    ap.add_argument("--hash-repeats", type=int, default=20)
    ap.add_argument("--hash-warmup", type=int, default=2)
    ap.add_argument("--small-repeats", type=int, default=2000)
    ap.add_argument("--small-warmup", type=int, default=200)
    ap.add_argument("--capture-repeats", type=int, default=20)
    args = ap.parse_args()

    if args.hash_repeats < 20 or args.small_repeats < 2000 or args.capture_repeats < 20:
        raise SystemExit("minimum repeats: 20 for the file hash and whole capture, 2000 for ECIES-scale rows")

    cpu = args.cpu if args.cpu < (os.cpu_count() or 1) else (os.cpu_count() or 1) - 1
    os.makedirs(RAW, exist_ok=True)
    machine = machine_info(cpu)
    host = "".join(c if c.isalnum() or c in "-_." else "_" for c in machine["hostname"])
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{stamp}_{host}" + ("" if machine["is_pi"] else f"_{summarize_partA.DRY_TAG}")
    label = machine["model"] if machine["is_pi"] else summarize_partA.DRY_LABEL

    # Build. A failed build is recorded in raw/ and stops the run.
    rc, out, err = run(["make", "-C", DEVICE])
    if rc != 0 or not os.path.exists(args.binary):
        path = os.path.join(RAW, f"partA_{run_id}_build_failed.txt")
        with open(path, "x") as f:
            f.write(f"{label}\nmake -C {DEVICE} exited {rc}\n--- stdout\n{out}\n--- stderr\n{err}\n")
        raise SystemExit(f"build failed; see {path}")

    machine["governor_before"] = cpufreq(cpu, "scaling_governor") or "not available"
    previous, gov_status = ({}, "not attempted (--no-governor)") if args.no_governor else set_governor("performance")
    machine["governor_during"] = (cpufreq(cpu, "scaling_governor") or "not available") + f" ({gov_status})"
    taskset = shutil.which("taskset")
    machine["taskset"] = taskset or "not found; run was not pinned"

    common = ["--hash-repeats", str(args.hash_repeats), "--hash-warmup", str(args.hash_warmup),
              "--small-repeats", str(args.small_repeats), "--small-warmup", str(args.small_warmup),
              "--capture-repeats", str(args.capture_repeats)]
    variants = [
        ("default", "OpenSSL picks its code path from the CPU features", {}, "all"),
        ("caps_off", "OpenSSL CPU capabilities switched off", caps_off_env(machine["arch"]),
         "a1_openssl,a3,a4,a5"),
    ]
    written = []
    try:
        for name, desc, env_extra, groups in variants:
            cmd = ([taskset, "-c", str(cpu)] if taskset else []) + [args.binary, "--groups", groups] + common
            env = dict(os.environ)
            for k in ("OPENSSL_armcap", "OPENSSL_ia32cap"):
                env.pop(k, None)
            env.update(env_extra)
            before = snapshot(cpu)
            header = {"type": "header", "label": label, "run_id": run_id, "variant": name,
                      "variant_description": desc, "env": env_extra, "command": cmd,
                      "machine": machine, "before": before}
            path = os.path.join(RAW, f"partA_{run_id}_{name}.jsonl")
            print(f"[{name}] running: {' '.join(cmd)}", flush=True)
            with open(path, "x") as f:
                f.write(json.dumps(header) + "\n")
                f.flush()
                p = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True, env=env)
                after = snapshot(cpu)
                f.write(json.dumps({"type": "driver_after", "exit_code": p.returncode,
                                    "stderr": p.stderr, "after": after}) + "\n")
            written.append(path)
            print(f"[{name}] exit {p.returncode}; raw log {os.path.relpath(path, HERE)}", flush=True)
    finally:
        restore_governor(previous)

    json_path, md_path = summarize_partA.summarize(run_id)
    give_back_to_sudo_user(written + [json_path, md_path])
    print(os.path.relpath(json_path, HERE))
    print(os.path.relpath(md_path, HERE))


if __name__ == "__main__":
    main()

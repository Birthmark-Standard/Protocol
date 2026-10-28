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

"""Part B driver: zero-knowledge proof of knowledge of M with SHA-256(M) = H, H public.

The prover is Longfellow-zk (zk/longfellow/). Build it first:
    zk/longfellow/fetch_and_build.sh

A run has three phases, each its own command. They share a run id, which
`setup` prints and the others take with --run-id.

  setup   Build each circuit and save it to zk/build/circuits/. Swap may be on.
          If it is, every setup time is labelled "setup with swap, not
          comparable".
  prove   Load each circuit and prove --repeats times, pinned to one core.
          Refuses to start while any swap is active, unless
          --allow-active-swap is given (for machines without sudo); then any
          run during which a page is swapped in or out counts as failed.
  hash    Plain SHA-256 of messages of the same sizes, plus 30,000,000 B, with
          the Part A code (OpenSSL default, OpenSSL capabilities off,
          libsodium).

    python3 run_partB.py setup --fields gf2_128 fp64_2 --sizes 4096
    sudo swapoff -a        # if sudo is available; otherwise add --allow-active-swap below
    python3 run_partB.py prove --run-id RUN_ID --fields gf2_128 fp64_2 --sizes 4096
    python3 run_partB.py hash  --run-id RUN_ID --sizes 4096
    python3 summarize_partB.py RUN_ID

sudo is optional. Run as root, the driver also sets the cpufreq governor to
performance during the prove and hash phases and restores it afterwards.
Without root it records the governor it found.

`--sizes ladder` means 1 KiB, 4 KiB, 16 KiB, 64 KiB, 130,944 B, 256 KiB,
1 MiB, 4 MiB and up, by powers of 4. The prove phase stops before the next
size when its predicted peak memory is over 80% of RAM or its predicted
prove time is over 30 minutes, and records why. A size whose circuit file
is missing, or whose setup failed, is recorded and skipped.

Every phase writes raw logs to results/raw/ that are never overwritten.
On a machine that is not a Raspberry Pi 4 Model B or 5, the run id and every
file name carry DRY_RUN_NOT_PI. Only standard-library Python 3.9 or later is
used.
"""

import argparse
import datetime
import hashlib
import json
import math
import os
import re
import shutil
import signal
import subprocess
import tempfile
import threading
import time

import run_partA
import summarize_partA

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
BUILD = os.path.join(HERE, "zk", "build")
CIRCUITS = os.path.join(BUILD, "circuits")
PROVER = os.path.join(BUILD, "longfellow-build", "sha256_zk_bench")
BUILD_INFO = os.path.join(BUILD, "longfellow_build_info.json")
BUILD_DIFF = os.path.join(BUILD, "longfellow_build_changes.diff")
HASHER = os.path.join(HERE, "device", "bench_capture")

FIELDS = ("gf2_128", "fp64_2")
VENDOR_POINT = 130944  # 2,047 compressions; approximates the vendor's unpublished "127.9 KiB"
LADDER = [1024, 4096, 16384, 65536, VENDOR_POINT, 262144] + [4 ** k for k in range(10, 16)]
HASH_REFERENCE = 30000000
MIB = 1 << 20
PROVE_LIMIT_S = 30 * 60
PROCESS_TIMEOUT_PER_REPEAT_S = 45 * 60
SETUP_TIMEOUT_S = 6 * 3600
MEMORY_FRACTION = 0.8


def compressions(n):
    return (n + 8) // 64 + 1


def swap_state():
    lines = (run_partA.read("/proc/swaps", "") or "").splitlines()
    active = [ln for ln in lines[1:] if ln.strip()]
    return {"active": bool(active), "proc_swaps": lines}


def build_info():
    info = None
    try:
        with open(BUILD_INFO) as f:
            info = json.load(f)
    except (OSError, ValueError):
        pass
    diff = run_partA.read(BUILD_DIFF, "")
    return {"info": info, "build_changes_diff": diff}


def parse_time_v(path):
    """Fields of GNU time -v output that the summary uses."""
    out = {}
    for line in (run_partA.read(path, "") or "").splitlines():
        line = line.strip()
        if line.startswith("Command terminated by signal"):
            out["terminated_by_signal"] = int(line.split()[-1])
        elif line.startswith("Maximum resident set size (kbytes):"):
            out["max_rss_kb"] = int(line.split(":")[-1])
        elif line.startswith("Elapsed (wall clock) time"):
            out["elapsed"] = line.split("):", 1)[-1].strip()
        elif line.startswith("Exit status:"):
            out["exit_status"] = int(line.split(":")[-1])
    return out


def vmstat_swap():
    """Pages swapped in and out since boot, from /proc/vmstat."""
    out = {}
    for line in (run_partA.read("/proc/vmstat", "") or "").splitlines():
        k, _, v = line.partition(" ")
        if k in ("pswpin", "pswpout"):
            out[k] = int(v)
    return out


def swap_used_kb():
    total = free = None
    for line in (run_partA.read("/proc/meminfo", "") or "").splitlines():
        if line.startswith("SwapTotal:"):
            total = int(line.split()[1])
        elif line.startswith("SwapFree:"):
            free = int(line.split()[1])
    return None if total is None or free is None else total - free


def run_logged(path, header, cmd, cpu, timeout_s, env=None, cpu_list=None):
    """Run cmd pinned with taskset, writing one raw log. Returns (exit, lines, time_v).

    Peak memory comes from GNU time -v when it is installed, otherwise from the
    rusage that wait4 returns for the child. Swap activity during the run is
    recorded either way: the change in pages swapped in and out, and the most
    swap in use, sampled every 0.5 s.
    """
    time_bin = shutil.which("time") or ("/usr/bin/time" if os.path.exists("/usr/bin/time") else None)
    taskset = shutil.which("taskset")
    time_out = None
    prefix = ([taskset, "-c", cpu_list or str(cpu)] if taskset else [])
    if time_bin:
        with tempfile.NamedTemporaryFile(prefix="partB_time_", delete=False) as t:
            time_out = t.name
        full = [time_bin, "-v", "-o", time_out] + prefix + cmd
    else:
        full = prefix + cmd
    header = dict(header, command=full, before=run_partA.snapshot(cpu), swap=swap_state(),
                  peak_rss_method="GNU time -v" if time_bin else "wait4 rusage (GNU time not installed)")
    lines, timed_out = [], False
    vm_before, used_before = vmstat_swap(), swap_used_kb()
    used_max = [used_before]
    stop = threading.Event()

    def sample():
        while not stop.wait(0.5):
            u = swap_used_kb()
            if u is not None and (used_max[0] is None or u > used_max[0]):
                used_max[0] = u

    with open(path, "x") as f:
        f.write(json.dumps(header) + "\n")
        f.flush()
        p = subprocess.Popen(full, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                             env=env, start_new_session=True)
        out_buf, err_buf = [], []
        readers = [threading.Thread(target=lambda s=src, b=buf: b.append(s.read()))
                   for src, buf in ((p.stdout, out_buf), (p.stderr, err_buf))]
        sampler = threading.Thread(target=sample)
        for t in readers + [sampler]:
            t.start()
        deadline = time.monotonic() + timeout_s
        status, rusage = None, None
        while status is None:
            pid, st, ru = os.wait4(p.pid, os.WNOHANG)
            if pid == p.pid:
                status, rusage = st, ru
            elif time.monotonic() > deadline:
                timed_out = True
                os.killpg(p.pid, signal.SIGKILL)
                _, status, rusage = os.wait4(p.pid, 0)
            else:
                time.sleep(0.2)
        p.returncode = os.waitstatus_to_exitcode(status)
        for t in readers:
            t.join()
        stop.set()
        sampler.join()
        out, err = "".join(out_buf), "".join(err_buf)
        for ln in out.splitlines():
            f.write(ln + "\n")
            if ln.startswith("{"):
                try:
                    lines.append(json.loads(ln))
                except ValueError:
                    pass
        if time_out:
            tv = parse_time_v(time_out)
        else:
            tv = {"max_rss_kb": rusage.ru_maxrss}
            if p.returncode < 0:
                tv["terminated_by_signal"] = -p.returncode
        vm_after, used_after = vmstat_swap(), swap_used_kb()
        swap_activity = {
            "pswpin_delta": vm_after.get("pswpin", 0) - vm_before.get("pswpin", 0),
            "pswpout_delta": vm_after.get("pswpout", 0) - vm_before.get("pswpout", 0),
            "swap_used_kb_before": used_before, "swap_used_kb_max": used_max[0],
            "swap_used_kb_after": used_after,
        }
        swap_activity["pages_swapped"] = swap_activity["pswpin_delta"] > 0 or swap_activity["pswpout_delta"] > 0
        f.write(json.dumps({"type": "driver_after", "exit_code": p.returncode, "timed_out": timed_out,
                            "timeout_s": timeout_s, "time_v": tv, "stderr": err[-4000:],
                            "swap_activity": swap_activity,
                            "after": run_partA.snapshot(cpu), "swap_after": swap_state()}) + "\n")
    if time_out:
        os.unlink(time_out)
    return p.returncode, lines, dict(tv, swap_activity=swap_activity, stdout=out)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(MIB), b""):
            h.update(chunk)
    return h.hexdigest()


def circuit_path(field, n):
    return os.path.join(CIRCUITS, f"{field}_{n}.circuit")


def new_run_id(machine):
    host = "".join(c if c.isalnum() or c in "-_." else "_" for c in machine["hostname"])
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{stamp}_{host}" + ("" if machine["is_pi"] else f"_{summarize_partA.DRY_TAG}")


def parse_sizes(values):
    if values == ["ladder"]:
        return list(LADDER)
    return sorted({int(v) for v in values})


def predict(points, c_next):
    """Predict a value at c_next from measured (compressions, value) points.

    Two or more points: the power law through the last two. One point: linear.
    """
    pts = sorted(points)
    if not pts:
        return None
    if len(pts) == 1 or pts[-1][0] == pts[-2][0]:
        c, y = pts[-1]
        return y * c_next / c
    (c1, y1), (c2, y2) = pts[-2], pts[-1]
    if y1 <= 0 or y2 <= 0:
        return y2 * c_next / c2
    b = math.log(y2 / y1) / math.log(c2 / c1)
    return y2 * (c_next / c2) ** b


def give_back(paths):
    run_partA.give_back_to_sudo_user([p for p in paths if os.path.exists(p)])


def phase_setup(args, machine, run_id, label):
    os.makedirs(CIRCUITS, exist_ok=True)
    if not os.path.exists(PROVER):
        raise SystemExit(f"missing {PROVER}; run zk/longfellow/fetch_and_build.sh first")
    swap = swap_state()
    note = "swap active" if swap["active"] else "no swap"
    if swap["active"]:
        print("setup: swap is active. A setup during which any page is swapped in or out is labelled "
              "\"setup with swap, not comparable\".")
    written = []
    for field in args.fields:
        for n in parse_sizes(args.sizes):
            path = os.path.join(RAW, f"partB_{run_id}_setup_{field}_{n}.jsonl")
            out = circuit_path(field, n)
            header = {"type": "header", "label": label, "run_id": run_id, "phase": "setup",
                      "field": field, "message_bytes": n, "compressions": compressions(n),
                      "swap_at_start": note, "machine": machine, "build": build_info(),
                      "circuit_file": os.path.relpath(out, HERE)}
            print(f"[setup {field} {n} B] building circuit", flush=True)
            rc, lines, tv = run_logged(path, header, [PROVER, "--field", field, "--bytes", str(n),
                                                      "--save-circuit", out], args.cpu, SETUP_TIMEOUT_S)
            written.append(path)
            saved = next((x for x in lines if x.get("type") == "circuit_saved"), {})
            ok = rc == 0 and saved.get("status") == "ok"
            if ok:
                with open(path, "a") as f:
                    f.write(json.dumps({"type": "circuit_file", "sha256": sha256_file(out),
                                        "bytes": os.path.getsize(out)}) + "\n")
                written.append(out)
            print(f"[setup {field} {n} B] {'ok' if ok else 'FAILED'}; peak RSS "
                  f"{tv.get('max_rss_kb', 0) / 1024:.0f} MiB; raw log {os.path.relpath(path, HERE)}", flush=True)
            if not ok:
                print(f"[setup {field}] stopping this field after the failure at {n} B")
                break
    give_back(written + [CIRCUITS])


def phase_prove(args, machine, run_id, label):
    swap = swap_state()
    if swap["active"] and not args.allow_active_swap:
        raise SystemExit("swap is active; turn it off (sudo swapoff -a) before timed proving. Without sudo, "
                         "--allow-active-swap proves with swap on and fails any run during which a page is "
                         "swapped in or out.")
    mem_limit_kb = MEMORY_FRACTION * machine["mem_total_kb"]
    written = []
    previous, gov_status = ({}, "not attempted (--no-governor)") if args.no_governor \
        else run_partA.set_governor("performance")
    machine = dict(machine, governor_during=(run_partA.cpufreq(args.cpu, "scaling_governor") or "not available")
                   + f" ({gov_status})")
    try:
        for field in args.fields:
            measured_time, measured_rss = [], []
            for n in parse_sizes(args.sizes):
                c = compressions(n)
                stop = None
                pt = predict(measured_time, c)
                pm = predict(measured_rss, c)
                if pm is not None and pm > mem_limit_kb:
                    stop = (f"predicted peak memory {pm / 1024:.0f} MiB is over 80% of RAM "
                            f"({mem_limit_kb / 1024:.0f} MiB)")
                elif pt is not None and pt > PROVE_LIMIT_S:
                    stop = f"predicted prove time {pt:.0f} s is over 30 minutes"
                circuit = circuit_path(field, n)
                if stop is None and not os.path.exists(circuit):
                    stop = f"no circuit file {os.path.relpath(circuit, HERE)}; run the setup phase for this size"
                if stop:
                    path = os.path.join(RAW, f"partB_{run_id}_prove_{field}_{n}_stopped.json")
                    with open(path, "x") as f:
                        json.dump({"type": "stopped", "label": label, "run_id": run_id, "field": field,
                                   "message_bytes": n, "compressions": c, "reason": stop,
                                   "predicted_prove_s": pt, "predicted_peak_rss_kb": pm,
                                   "measured_points_time": measured_time,
                                   "measured_points_rss_kb": measured_rss}, f)
                    written.append(path)
                    print(f"[prove {field}] stopped at {n} B: {stop}")
                    break
                repeats = max(args.repeats, 5) if n <= MIB else max(args.repeats, 1)
                path = os.path.join(RAW, f"partB_{run_id}_prove_{field}_{n}.jsonl")
                header = {"type": "header", "label": label, "run_id": run_id, "phase": "prove",
                          "field": field, "message_bytes": n, "compressions": c, "repeats": repeats,
                          "threads": 1, "machine": machine, "build": build_info(),
                          "circuit_file": os.path.relpath(circuit, HERE),
                          "circuit_sha256": sha256_file(circuit)}
                print(f"[prove {field} {n} B] {repeats} repeats", flush=True)
                rc, lines, tv = run_logged(path, header,
                                           [PROVER, "--field", field, "--bytes", str(n), "--repeats",
                                            str(repeats), "--load-circuit", circuit],
                                           args.cpu, PROCESS_TIMEOUT_PER_REPEAT_S * repeats)
                written.append(path)
                runs = [x for x in lines if x.get("type") == "run"]
                done = next((x for x in lines if x.get("type") == "done"), {})
                ok = rc == 0 and done.get("all_checks_passed") is True and len(runs) == repeats
                if tv["swap_activity"]["pages_swapped"]:
                    ok = False
                    print(f"[prove {field} {n} B] pages were swapped during proving; the run counts as failed")
                print(f"[prove {field} {n} B] {'ok' if ok else 'FAILED'}; peak RSS "
                      f"{tv.get('max_rss_kb', 0) / 1024:.0f} MiB; raw log {os.path.relpath(path, HERE)}", flush=True)
                if not ok:
                    print(f"[prove {field}] stopping this field after the failure at {n} B")
                    break
                times = sorted(x["time_s"]["prove"] for x in runs)
                measured_time.append((c, times[len(times) // 2]))
                measured_rss.append((c, tv.get("max_rss_kb", done.get("max_rss_kb", 0))))
    finally:
        run_partA.restore_governor(previous)
    give_back(written)


def phase_hash(args, machine, run_id, label):
    sizes = sorted(set(parse_sizes(args.sizes)) | {HASH_REFERENCE})
    small = [n for n in sizes if n <= MIB]
    large = [n for n in sizes if n > MIB]
    variants = [("default", {}), ("caps_off", run_partA.caps_off_env(machine["arch"]))]
    written = []
    previous, gov_status = ({}, "not attempted (--no-governor)") if args.no_governor \
        else run_partA.set_governor("performance")
    try:
        for name, env_extra in variants:
            for group, chunk, repeats in (("small", small, 2000), ("large", large, 20)):
                if not chunk:
                    continue
                env = dict(os.environ)
                for k in ("OPENSSL_armcap", "OPENSSL_ia32cap"):
                    env.pop(k, None)
                env.update(env_extra)
                groups = "hash_openssl,hash_libsodium" if name == "default" else "hash_openssl"
                path = os.path.join(RAW, f"partB_{run_id}_hash_{name}_{group}.jsonl")
                header = {"type": "header", "label": label, "run_id": run_id, "phase": "hash",
                          "variant": name, "env": env_extra, "machine": machine}
                cmd = [HASHER, "--groups", groups, "--hash-bytes", ",".join(map(str, chunk)),
                       "--hash-repeats", str(repeats), "--hash-warmup", "2"]
                print(f"[hash {name} {group}] {len(chunk)} sizes, {repeats} repeats", flush=True)
                rc, _, _ = run_logged(path, header, cmd, args.cpu, 6 * 3600, env=env)
                written.append(path)
                print(f"[hash {name} {group}] exit {rc}; raw log {os.path.relpath(path, HERE)}", flush=True)
    finally:
        run_partA.restore_governor(previous)
    give_back(written)


HEKATE_BIN = os.path.join(BUILD, "hekate-target", "release", "examples", "sha256")
HEKATE_INFO = os.path.join(BUILD, "hekate_build_info.json")
HEKATE_ROUNDS_PER_ROW = 4  # the example's default; 64 rounds per block gives 16 rows per block
HEKATE_EXTRA_VARS = 4      # retries with a larger trace if the example rejects the smallest one


def parse_duration_s(text):
    """Seconds from a Rust Duration Debug string such as 1.23s, 456.78ms or 12.3µs."""
    m = re.match(r"\s*([0-9.]+)\s*(ns|µs|us|ms|s)\b", text)
    if not m:
        return None
    scale = {"ns": 1e-9, "µs": 1e-6, "us": 1e-6, "ms": 1e-3, "s": 1.0}[m.group(2)]
    return float(m.group(1)) * scale


def parse_hekate(stdout):
    """The fields of Hekate's sha256 example output that the summary uses."""
    out = {"success": False}
    for line in stdout.splitlines():
        line = line.strip()
        m = re.match(r"Rows: 2\^(\d+) \((\d+) compressions, (\d+) bytes hashed, (\d+) rounds per row\)", line)
        if m:
            out.update(num_vars=int(m.group(1)), compressions=int(m.group(2)),
                       message_bytes=int(m.group(3)), rounds_per_row=int(m.group(4)))
        m = re.match(r"-> (Trace Generation|Proving|Verifying) done in (.+)$", line)
        if m:
            key = {"Trace Generation": "trace_s", "Proving": "prove_s", "Verifying": "verify_s"}[m.group(1)]
            out[key] = parse_duration_s(m.group(2))
        m = re.search(r"Total Proof size: .*\((\d+) bytes\)", line)
        if m:
            out["proof_bytes"] = int(m.group(1))
        if line.startswith("SHA-256 digest: 0x"):
            out["digest"] = line.split("0x", 1)[1]
        if line == "SUCCESS":
            out["success"] = True
    return out


def phase_hekate(args, machine, run_id, label):
    """Hekate's own sha256 example, zero-knowledge on, ct prover, one proof per process."""
    if not os.path.exists(HEKATE_BIN):
        raise SystemExit(f"missing {HEKATE_BIN}; run zk/hekate/fetch_and_build.sh first")
    swap = swap_state()
    if swap["active"] and not args.allow_active_swap:
        raise SystemExit("swap is active; turn it off (sudo swapoff -a) before timed proving, or use "
                         "--allow-active-swap where sudo is not available")
    try:
        with open(HEKATE_INFO) as f:
            info = json.load(f)
    except (OSError, ValueError):
        info = None
    threads = args.threads
    ncpu = os.cpu_count() or 1
    cpu_list = str(args.cpu) if threads == 1 else f"0-{min(threads, ncpu) - 1}"
    env = dict(os.environ, RAYON_NUM_THREADS=str(threads), RUST_LOG="warn")
    mem_limit_kb = MEMORY_FRACTION * machine["mem_total_kb"]
    written = []
    previous, gov_status = ({}, "not attempted (--no-governor)") if args.no_governor \
        else run_partA.set_governor("performance")
    machine = dict(machine, governor_during=(run_partA.cpufreq(args.cpu, "scaling_governor") or "not available")
                   + f" ({gov_status})")
    measured_time, measured_rss = [], []
    try:
        for n in parse_sizes(args.sizes):
            c = compressions(n)
            pt, pm = predict(measured_time, c), predict(measured_rss, c)
            stop = None
            if pm is not None and pm > mem_limit_kb:
                stop = (f"predicted peak memory {pm / 1024:.0f} MiB is over 80% of RAM "
                        f"({mem_limit_kb / 1024:.0f} MiB)")
            elif pt is not None and pt > PROVE_LIMIT_S:
                stop = f"predicted prove time {pt:.0f} s is over 30 minutes"
            if stop:
                path = os.path.join(RAW, f"partB_{run_id}_hekate_{threads}t_{n}_stopped.json")
                with open(path, "x") as f:
                    json.dump({"type": "stopped", "label": label, "run_id": run_id, "prover": "hekate",
                               "field": f"hekate_{threads}t", "threads": threads, "message_bytes": n,
                               "compressions": c, "reason": stop}, f)
                written.append(path)
                print(f"[hekate {threads}t] stopped at {n} B: {stop}")
                break
            repeats = max(args.repeats, 5) if n <= MIB else max(args.repeats, 1)
            num_vars = max(1, math.ceil(math.log2(c * 64 // HEKATE_ROUNDS_PER_ROW)))
            times, rss, fatal = [], [], None
            r, attempt = 0, 0
            while r < repeats:
                suffix = f"_r{r}" + (f"_vars{num_vars}" if attempt else "")
                path = os.path.join(RAW, f"partB_{run_id}_hekate_{threads}t_{n}{suffix}.jsonl")
                header = {"type": "header", "label": label, "run_id": run_id, "phase": "hekate",
                          "prover": "hekate", "threads": threads, "cpu_list": cpu_list,
                          "message_bytes": n, "compressions": c, "repeat": r, "num_vars": num_vars,
                          "zero_knowledge": True, "machine": machine, "hekate_build": info}
                cmd = [HEKATE_BIN, "--num-vars", str(num_vars), "--blocks", str(c)]
                rc, _, tv = run_logged(path, header, cmd, args.cpu, PROCESS_TIMEOUT_PER_REPEAT_S, env=env,
                                       cpu_list=cpu_list)
                parsed = parse_hekate(tv.get("stdout", ""))
                with open(path, "a") as f:
                    f.write(json.dumps(dict(parsed, type="hekate_parsed")) + "\n")
                written.append(path)
                ok = rc == 0 and parsed["success"] and not tv["swap_activity"]["pages_swapped"] \
                    and parsed.get("compressions") == c and parsed.get("prove_s") is not None
                sig = tv.get("terminated_by_signal")
                if ok:
                    times.append(parsed["prove_s"])
                    rss.append(tv.get("max_rss_kb", 0))
                    r += 1
                    continue
                if sig is None and not parsed["success"] and r == 0 and attempt < HEKATE_EXTRA_VARS \
                        and not tv["swap_activity"]["pages_swapped"]:
                    attempt += 1
                    num_vars += 1
                    print(f"[hekate {threads}t {n} B] failed at the smallest trace; retrying with 2^{num_vars} rows")
                    continue
                fatal = f"signal {sig}" if sig else f"exit {rc}"
                break
            if fatal or not times:
                print(f"[hekate {threads}t {n} B] FAILED ({fatal}); stopping the Hekate attempt")
                break
            print(f"[hekate {threads}t {n} B] ok; median prove {sorted(times)[len(times) // 2]:.3f} s")
            measured_time.append((c, sorted(times)[len(times) // 2]))
            measured_rss.append((c, max(rss)))
    finally:
        run_partA.restore_governor(previous)
    give_back(written)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("phase", choices=("setup", "prove", "hash", "hekate"))
    ap.add_argument("--run-id", help="run id printed by the setup phase (required for prove and hash)")
    ap.add_argument("--fields", nargs="+", default=list(FIELDS), choices=FIELDS)
    ap.add_argument("--sizes", nargs="+", default=["ladder"], help="message sizes in bytes, or 'ladder'")
    ap.add_argument("--repeats", type=int, default=5, help="proofs per size (at least 5 up to 1 MiB)")
    ap.add_argument("--cpu", type=int, default=3, help="core to pin to (default 3)")
    ap.add_argument("--threads", type=int, default=1, choices=(1, 4),
                    help="hekate phase only: 1 (pinned to --cpu) or 4 (cores 0-3)")
    ap.add_argument("--no-governor", action="store_true")
    ap.add_argument("--allow-active-swap", action="store_true",
                    help="prove even though swap is active (for machines without sudo); any run during "
                         "which a page is swapped in or out counts as failed")
    args = ap.parse_args()

    os.makedirs(RAW, exist_ok=True)
    cpu = args.cpu if args.cpu < (os.cpu_count() or 1) else (os.cpu_count() or 1) - 1
    args.cpu = cpu
    machine = run_partA.machine_info(cpu)
    machine["governor_before"] = run_partA.cpufreq(cpu, "scaling_governor") or "not available"
    label = machine["model"] if machine["is_pi"] else summarize_partA.DRY_LABEL

    if args.phase == "setup":
        run_id = args.run_id or new_run_id(machine)
        print(f"run id: {run_id}")
        phase_setup(args, machine, run_id, label)
    else:
        if not args.run_id:
            raise SystemExit("--run-id is required; use the id the setup phase printed")
        run_id = args.run_id
        if machine["is_pi"] == run_id.endswith(summarize_partA.DRY_TAG):
            raise SystemExit("run id and machine disagree about DRY_RUN_NOT_PI")
        if args.phase == "prove":
            phase_prove(args, machine, run_id, label)
        elif args.phase == "hekate":
            phase_hekate(args, machine, run_id, label)
        else:
            phase_hash(args, machine, run_id, label)
    print(f"run id: {run_id}")


if __name__ == "__main__":
    main()

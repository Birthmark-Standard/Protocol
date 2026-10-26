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
          Refuses to start while any swap is active.
  hash    Plain SHA-256 of messages of the same sizes, plus 30,000,000 B, with
          the Part A code (OpenSSL default, OpenSSL capabilities off,
          libsodium).

    sudo python3 run_partB.py setup --fields gf2_128 fp64_2 --sizes 4096
    sudo swapoff -a
    sudo python3 run_partB.py prove --run-id RUN_ID --fields gf2_128 fp64_2 --sizes 4096
    sudo python3 run_partB.py hash  --run-id RUN_ID --sizes 4096
    python3 summarize_partB.py RUN_ID

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
import shutil
import signal
import subprocess
import tempfile

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


def run_logged(path, header, cmd, cpu, timeout_s, env=None):
    """Run cmd under /usr/bin/time -v and taskset, writing one raw log. Returns (exit, lines, time_v)."""
    time_bin = shutil.which("time") or "/usr/bin/time"
    taskset = shutil.which("taskset")
    with tempfile.NamedTemporaryFile(prefix="partB_time_", delete=False) as t:
        time_out = t.name
    full = [time_bin, "-v", "-o", time_out] + ([taskset, "-c", str(cpu)] if taskset else []) + cmd
    header = dict(header, command=full, before=run_partA.snapshot(cpu), swap=swap_state())
    lines, timed_out = [], False
    with open(path, "x") as f:
        f.write(json.dumps(header) + "\n")
        f.flush()
        p = subprocess.Popen(full, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                             env=env, start_new_session=True)
        try:
            out, err = p.communicate(timeout=timeout_s)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(p.pid, signal.SIGKILL)
            out, err = p.communicate()
        for ln in out.splitlines():
            f.write(ln + "\n")
            if ln.startswith("{"):
                try:
                    lines.append(json.loads(ln))
                except ValueError:
                    pass
        tv = parse_time_v(time_out)
        f.write(json.dumps({"type": "driver_after", "exit_code": p.returncode, "timed_out": timed_out,
                            "timeout_s": timeout_s, "time_v": tv, "stderr": err[-4000:],
                            "after": run_partA.snapshot(cpu), "swap_after": swap_state()}) + "\n")
    os.unlink(time_out)
    return p.returncode, lines, tv


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
    note = "setup with swap, not comparable" if swap["active"] else "setup without swap"
    print(f"setup: {note}")
    written = []
    for field in args.fields:
        for n in parse_sizes(args.sizes):
            path = os.path.join(RAW, f"partB_{run_id}_setup_{field}_{n}.jsonl")
            out = circuit_path(field, n)
            header = {"type": "header", "label": label, "run_id": run_id, "phase": "setup",
                      "field": field, "message_bytes": n, "compressions": compressions(n),
                      "setup_label": note, "machine": machine, "build": build_info(),
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
    if swap["active"]:
        raise SystemExit("swap is active; turn it off (sudo swapoff -a) before timed proving")
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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("phase", choices=("setup", "prove", "hash"))
    ap.add_argument("--run-id", help="run id printed by the setup phase (required for prove and hash)")
    ap.add_argument("--fields", nargs="+", default=list(FIELDS), choices=FIELDS)
    ap.add_argument("--sizes", nargs="+", default=["ladder"], help="message sizes in bytes, or 'ladder'")
    ap.add_argument("--repeats", type=int, default=5, help="proofs per size (at least 5 up to 1 MiB)")
    ap.add_argument("--cpu", type=int, default=3, help="core to pin to (default 3)")
    ap.add_argument("--no-governor", action="store_true")
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
        else:
            phase_hash(args, machine, run_id, label)
    print(f"run id: {run_id}")


if __name__ == "__main__":
    main()

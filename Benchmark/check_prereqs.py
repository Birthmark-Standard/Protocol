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

"""List what Part A and Part B need on this machine, and what is missing.

Needs no root and installs nothing. Each missing item is printed with the
Debian / Raspberry Pi OS package that provides it, so that someone with admin
rights can install it.

    python3 check_prereqs.py
"""

import glob
import os
import shutil
import subprocess

# (what, how to check, package, needed by)
COMMANDS = [
    ("cc", "build-essential", "A"), ("make", "build-essential", "A"), ("pkg-config", "pkg-config", "A"),
    ("taskset", "util-linux", "A, B"), ("git", "git", "B"), ("cmake", "cmake", "B"),
    ("clang++", "clang", "B"), ("objdump", "binutils", "B (crypto-instruction check)"),
]
OPTIONAL_COMMANDS = [
    ("time", "/usr/bin/time", "time", "B (peak memory; without it the driver uses wait4)"),
    ("vcgencmd", None, "raspi-utils or libraspberrypi-bin", "A, B (temperature and throttle readings)"),
]
PKGCONFIG = [("libsodium", "libsodium-dev", "A"), ("libcrypto", "libssl-dev", "A, B"),
             ("libzstd", "libzstd-dev", "B"), ("zlib", "zlib1g-dev", "B")]
CMAKE_PACKAGES = [("GTest", "libgtest-dev", "B"), ("benchmark", "libbenchmark-dev", "B")]


def run(cmd):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, "", str(e)


def cmake_package_found(name):
    pats = [f"/usr/lib/*/cmake/{name}*/*Config.cmake", f"/usr/lib/cmake/{name}*/*Config.cmake",
            f"/usr/share/cmake*/Modules/Find{name}.cmake", f"/usr/lib/*/cmake/{name.lower()}*/*config.cmake",
            f"/usr/lib/*/cmake/{name}*/*-config.cmake"]
    return any(glob.glob(p) for p in pats)


def main():
    missing = []
    print("Required commands:")
    for cmd, pkg, who in COMMANDS:
        path = shutil.which(cmd)
        print(f"  {'ok     ' if path else 'MISSING'} {cmd:<12} {path or ''}  (Part {who})")
        if not path:
            missing.append(pkg)
    print("Optional commands:")
    for cmd, fallback, pkg, who in OPTIONAL_COMMANDS:
        path = shutil.which(cmd) or (fallback if fallback and os.path.exists(fallback) else None)
        print(f"  {'ok     ' if path else 'absent '} {cmd:<12} {path or ''}  (Part {who}; package {pkg})")
    print("Libraries (pkg-config):")
    for lib, pkg, who in PKGCONFIG:
        rc, out, _ = run(["pkg-config", "--modversion", lib]) if shutil.which("pkg-config") else (1, "", "")
        print(f"  {'ok     ' if rc == 0 else 'MISSING'} {lib:<12} {out if rc == 0 else ''}  (Part {who})")
        if rc != 0:
            missing.append(pkg)
    print("CMake packages:")
    for name, pkg, who in CMAKE_PACKAGES:
        ok = cmake_package_found(name)
        print(f"  {'ok     ' if ok else 'MISSING'} {name:<12} (Part {who})")
        if not ok:
            missing.append(pkg)

    print("Machine:")
    model = ""
    try:
        with open("/proc/device-tree/model") as f:
            model = f.read().strip("\x00\n ")
    except OSError:
        pass
    print(f"  model: {model or 'not a device-tree board'}")
    rc, _, _ = run(["sudo", "-n", "true"]) if shutil.which("sudo") else (None, "", "")
    print(f"  sudo without a password: {'yes' if rc == 0 else 'no'}")
    try:
        with open("/proc/swaps") as f:
            swaps = [ln for ln in f.read().splitlines()[1:] if ln.strip()]
    except OSError:
        swaps = []
    print(f"  swap active: {'yes: ' + '; '.join(' '.join(s.split()[:3]) for s in swaps) if swaps else 'no'}")
    if swaps:
        print("    The Part B prove phase refuses to run with swap active. Without sudo, use")
        print("    --allow-active-swap: any run during which a page is swapped then counts as failed.")
    try:
        with open("/proc/sys/kernel/perf_event_paranoid") as f:
            print(f"  perf_event_paranoid: {f.read().strip()} (2 or lower lets a process count its own cycles)")
    except OSError:
        pass
    gov = "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
    if os.path.exists(gov):
        with open(gov) as f:
            print(f"  cpufreq governor: {f.read().strip()} (writable: {'yes' if os.access(gov, os.W_OK) else 'no'})")

    if missing:
        pkgs = " ".join(sorted(set(missing)))
        print(f"\nMissing packages. Someone with admin rights can install them with:\n  sudo apt install {pkgs}")
    else:
        print("\nNothing required is missing.")


if __name__ == "__main__":
    main()

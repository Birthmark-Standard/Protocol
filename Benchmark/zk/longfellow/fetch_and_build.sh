#!/usr/bin/env bash
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

# Clone Longfellow-zk at a pinned commit into Benchmark/zk/build/ and build
# sha256_zk_bench against it.
#
# Dependencies (Debian, Ubuntu, Raspberry Pi OS):
#   sudo apt install build-essential clang cmake libssl-dev libzstd-dev \
#        libgtest-dev libbenchmark-dev zlib1g-dev
#
# On aarch64 without the pmull CPU feature (for example the Raspberry Pi 4),
# Longfellow's default build would execute PMULL and stop with an illegal
# instruction. This script then makes two build changes, records them as a
# diff, and checks the binary for PMULL instructions:
#   1. lib/CMakeLists.txt: -march=armv8-a+crypto becomes -march=armv8-a.
#   2. lib/gf2k/sysdep.h: the PMULL branch is taken only when the compiler
#      defines __ARM_FEATURE_AES, so the build uses Longfellow's own NEON
#      branch without PMULL.
# Set LONGFELLOW_NO_PMULL=1 to force these changes on any aarch64 CPU.
#
# Environment: JOBS (parallel compile jobs, default 2).

set -euo pipefail

LONGFELLOW_URL="https://github.com/google/longfellow-zk"
LONGFELLOW_COMMIT="8861765fbbfaca7a452da60f8ceb8c6de8e4a003"

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_ROOT="$(cd "$HERE/.." && pwd)/build"
SRC="$BUILD_ROOT/longfellow-zk"
OUT="$BUILD_ROOT/longfellow-build"
INFO="$BUILD_ROOT/longfellow_build_info.json"
DIFF="$BUILD_ROOT/longfellow_build_changes.diff"
JOBS="${JOBS:-2}"

mkdir -p "$BUILD_ROOT"

if [ ! -d "$SRC/.git" ]; then
  git init -q "$SRC"
  git -C "$SRC" remote add origin "$LONGFELLOW_URL"
fi
git -C "$SRC" fetch -q --depth 1 origin "$LONGFELLOW_COMMIT"
git -C "$SRC" checkout -q --force "$LONGFELLOW_COMMIT"
# Start from the pinned tree on every run.
git -C "$SRC" checkout -q -- .

arch="$(uname -m)"
no_pmull=0
if [ "$arch" = "aarch64" ]; then
  if [ "${LONGFELLOW_NO_PMULL:-0}" = "1" ] || ! grep -m1 '^Features' /proc/cpuinfo | grep -qw pmull; then
    no_pmull=1
  fi
fi

if [ "$no_pmull" = "1" ]; then
  sed -i 's/-march=armv8-a+crypto/-march=armv8-a/g' "$SRC/lib/CMakeLists.txt"
  count="$(grep -c '^#elif defined(__aarch64__)$' "$SRC/lib/gf2k/sysdep.h" || true)"
  if [ "$count" != "1" ]; then
    echo "expected one PMULL branch in lib/gf2k/sysdep.h, found $count" >&2
    exit 1
  fi
  sed -i 's/^#elif defined(__aarch64__)$/#elif defined(__aarch64__) \&\& defined(__ARM_FEATURE_AES)/' \
    "$SRC/lib/gf2k/sysdep.h"
fi
git -C "$SRC" diff > "$DIFF"

# Longfellow's lib/algebra/sysdep.h defines its add-with-carry helpers for
# x86 and for clang only, so an aarch64 build needs clang.
CXX_BIN="${CXX:-}"
if [ -z "$CXX_BIN" ]; then
  if command -v clang++ >/dev/null; then
    CXX_BIN=clang++
  elif [ "$arch" = "aarch64" ]; then
    echo "clang++ is required on aarch64: sudo apt install clang" >&2
    exit 1
  else
    CXX_BIN=g++
  fi
fi

CXX="$CXX_BIN" cmake -S "$HERE" -B "$OUT" -D LONGFELLOW_SRC="$SRC" -D CMAKE_BUILD_TYPE=Release >/dev/null
cmake --build "$OUT" --target sha256_zk_bench -j "$JOBS"

# Count crypto-extension instructions in the binary. The 8-bit PMULL form
# (pmull vN.8h, vN.8b, vN.8b) is base NEON and is used on purpose by
# Longfellow's fallback. Only the 64-bit form (vN.1q, vN.1d) and the AES and
# SHA instructions need the crypto extension.
BIN="$OUT/sha256_zk_bench"
crypto_count="null"
if [ "$arch" = "aarch64" ] && command -v objdump >/dev/null; then
  crypto_count="$(objdump -d "$BIN" | grep -E '\bpmull2?\b.*\.1q|\baes[edm]c?\b|\baesimc\b|\bsha(1|256|512)[a-z0-9]*\b' -c || true)"
  if [ "$no_pmull" = "1" ] && [ "$crypto_count" != "0" ]; then
    echo "build without PMULL still contains $crypto_count crypto-extension instructions" >&2
    exit 1
  fi
fi

cat > "$INFO" <<EOF
{"prover": "longfellow-zk", "url": "$LONGFELLOW_URL", "commit": "$LONGFELLOW_COMMIT",
 "arch": "$arch", "no_pmull_build_changes": $([ "$no_pmull" = "1" ] && echo true || echo false),
 "build_changes_diff": "$(basename "$DIFF")", "crypto_extension_instructions_in_binary": $crypto_count,
 "compiler": "$($CXX_BIN --version | head -1)", "build_type": "Release",
 "binary": "$BIN"}
EOF
echo "built $BIN"
cat "$INFO"

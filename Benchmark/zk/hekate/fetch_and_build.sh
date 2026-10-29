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

# Clone Hekate at a pinned commit into Benchmark/zk/build/ and build its own
# sha256 example with the constant-time ("ct") prover.
#
# Hekate's open code is AGPL-3.0-only. Its prover is a closed, signed binary
# (libhekate_prover_cdylib.so) that the build downloads from
# releases.oumuamua.dev and checks against the SHA-256 and the two signatures
# in hekate-prover-sys/artifacts/manifest.toml. Nothing here links Hekate
# code into this repository; the example is Hekate's own.
#
# Pinned commit 3268d3a pins prover 0.16.1, the version behind the vendor's
# 949 ms figure. No root is needed. Rust 1.88 or later is required; without
# root it can be installed for the current user with rustup
# (https://rustup.rs), which puts cargo in ~/.cargo/bin.
#
# After the build, the script counts crypto-extension instructions (64-bit
# PMULL, AES, SHA) in the prover library. The Raspberry Pi 4 has none of these
# instructions. A non-zero count there means the prover is expected to stop
# with an illegal instruction; the run still goes ahead so that the failure is
# recorded.
#
# Environment: JOBS (parallel compile jobs, default 2).

set -euo pipefail

HEKATE_URL="https://github.com/oumuamua-labs/hekate"
HEKATE_COMMIT="3268d3a3fe8fab6e59c87d60a84a33645369ce01"
FEATURES="std,parallel,blake3,ct"

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_ROOT="$(cd "$HERE/.." && pwd)/build"
SRC="$BUILD_ROOT/hekate"
TARGET_DIR="$BUILD_ROOT/hekate-target"
CACHE="$BUILD_ROOT/hekate-prover-cache"
INFO="$BUILD_ROOT/hekate_build_info.json"
JOBS="${JOBS:-2}"

export PATH="$HOME/.cargo/bin:$PATH"
if ! command -v cargo >/dev/null; then
  echo "cargo not found; install Rust 1.88 or later for this user with rustup (https://rustup.rs)" >&2
  exit 1
fi

mkdir -p "$BUILD_ROOT" "$CACHE"
if [ ! -d "$SRC/.git" ]; then
  git init -q "$SRC"
  git -C "$SRC" remote add origin "$HEKATE_URL"
fi
git -C "$SRC" fetch -q --depth 1 origin "$HEKATE_COMMIT"
git -C "$SRC" checkout -q --force "$HEKATE_COMMIT"
git -C "$SRC" checkout -q -- .

(cd "$SRC" && CARGO_TARGET_DIR="$TARGET_DIR" HEKATE_PROVER_CACHE_DIR="$CACHE" \
  cargo build --release -p hekate --example sha256 --no-default-features --features "$FEATURES" -j "$JOBS")

BIN="$TARGET_DIR/release/examples/sha256"
LIB="$(find "$TARGET_DIR/release/build" -name libhekate_prover_cdylib.so -path '*hekate-prover-sys*' | head -1)"
if [ ! -x "$BIN" ] || [ -z "$LIB" ]; then
  echo "build finished without $BIN or the prover library" >&2
  exit 1
fi

arch="$(uname -m)"
crypto_count="null"
if [ "$arch" = "aarch64" ] && command -v objdump >/dev/null; then
  crypto_count="$(objdump -d "$LIB" | grep -E '\bpmull2?\b.*\.1q|\baes[edm]c?\b|\baesimc\b|\bsha(1|256|512)[a-z0-9]*\b' -c || true)"
fi
cpu_pmull=false
if grep -m1 '^Features' /proc/cpuinfo 2>/dev/null | grep -qw pmull; then cpu_pmull=true; fi

cat > "$INFO" <<EOF
{"prover": "hekate", "url": "$HEKATE_URL", "commit": "$HEKATE_COMMIT", "features": "$FEATURES",
 "prover_library": "$LIB", "prover_library_sha256": "$(sha256sum "$LIB" | cut -d' ' -f1)",
 "crypto_extension_instructions_in_prover": $crypto_count, "cpu_has_pmull": $cpu_pmull,
 "rustc": "$(rustc --version)", "arch": "$arch", "binary": "$BIN"}
EOF
echo "built $BIN"
cat "$INFO"
if [ "$crypto_count" != "null" ] && [ "$crypto_count" != "0" ] && [ "$cpu_pmull" = "false" ]; then
  echo "note: the prover library contains $crypto_count crypto-extension instructions and this CPU has no pmull;" \
       "expect an illegal-instruction stop, which run_partB.py records" >&2
fi

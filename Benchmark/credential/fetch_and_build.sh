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

# Part C build. Clones three libraries at pinned commits into
# Benchmark/credential/build/, builds them, runs the ECDAA test suite, then
# builds bench_credential with the Makefile in this folder.
#
#   AMCL 4.7.3 (Xaptum fork)  pairing arithmetic for ECDAA, curve FP256BN
#   Xaptum ECDAA              FIDO ECDAA, software only (no TPM support)
#   Intel EPID SDK 8.0.0      EPID 2.0 tiny member and verifier
#
# Dependencies (Debian, Ubuntu, Raspberry Pi OS):
#   sudo apt install build-essential cmake git pkg-config python3 \
#        libsodium-dev libssl-dev
#
# The EPID SDK needs two changes to its top-level CMakeLists.txt, recorded in
# build/epid_build_changes.diff. Nothing else in any library is changed.
#   1. The line that adds -Werror is deleted. GCC 12 and later stop the build
#      with warnings in the SDK's code.
#   2. -fno-strict-aliasing is added after the SDK's -Os. The SDK's math code
#      casts between its integer types. GCC 13 at -Os then computes wrong
#      results: EpidProvisionKey rejects the SDK's own test key. At -O0, or
#      with this flag, the SDK's test signature verifies.
#
# Environment: JOBS (parallel compile jobs, default 2).

set -euo pipefail

AMCL_URL="https://github.com/xaptum/amcl"
AMCL_COMMIT="4bb6af4eb53c219fb4e5b16ef020469425826977"     # tag 4.7.3
ECDAA_URL="https://github.com/xaptum/ecdaa"
ECDAA_COMMIT="92f93059dfe23c061a2372c897bdcaad0d917487"    # master, 2021-08-13
EPID_URL="https://github.com/Intel-EPID-SDK/epid-sdk"
EPID_COMMIT="ceb0a9e77b01b5e9c67619aeddae7b42dad71134"     # tag v8.0.0

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD="$HERE/build"
SRC="$BUILD/src"
DEPS="$BUILD/deps"
INFO="$BUILD/credential_build_info.json"
EPID_DIFF="$BUILD/epid_build_changes.diff"
ECDAA_TESTS="$BUILD/ecdaa_ctest.log"
JOBS="${JOBS:-2}"

mkdir -p "$SRC" "$DEPS"

fetch() {  # url commit dir
  if [ ! -d "$3/.git" ]; then
    git init -q "$3"
    git -C "$3" remote add origin "$1"
  fi
  git -C "$3" fetch -q --depth 1 origin "$2"
  git -C "$3" checkout -q --force "$2"
  # Start from the pinned tree on every run.
  git -C "$3" checkout -q -- .
  git -C "$3" clean -q -fdx
}

fetch "$AMCL_URL" "$AMCL_COMMIT" "$SRC/amcl"
fetch "$ECDAA_URL" "$ECDAA_COMMIT" "$SRC/ecdaa"
fetch "$EPID_URL" "$EPID_COMMIT" "$SRC/epid-sdk"

# AMCL, with the options of ECDAA's own .travis/install-amcl.sh, as static libraries.
cmake -S "$SRC/amcl" -B "$BUILD/amcl-build" -D CMAKE_INSTALL_PREFIX="$DEPS" \
  -D AMCL_CURVE=FP256BN -D AMCL_RSA="" -D AMCL_INCLUDE_SUBDIR=amcl \
  -D BUILD_PYTHON=Off -D BUILD_MPIN=Off -D BUILD_WCC=Off -D BUILD_DOCS=Off \
  -D BUILD_SHARED_LIBS=Off -D BUILD_TESTING=Off >/dev/null
cmake --build "$BUILD/amcl-build" -j "$JOBS" >/dev/null
cmake --install "$BUILD/amcl-build" >/dev/null

# ECDAA, Release as in its doc/BUILDING.md, without TPM support. The build
# directory is ecdaa/build, the path its tool test expects.
CMAKE_PREFIX_PATH="$DEPS" cmake -S "$SRC/ecdaa" -B "$SRC/ecdaa/build" -D CMAKE_BUILD_TYPE=Release \
  -D CMAKE_INSTALL_PREFIX="$DEPS" -D ECDAA_CURVES=FP256BN -D ECDAA_TPM_SUPPORT=OFF \
  -D BUILD_SHARED_LIBS=OFF >/dev/null
cmake --build "$SRC/ecdaa/build" -j "$JOBS" >/dev/null
cmake --install "$SRC/ecdaa/build" >/dev/null
ecdaa_tests="pass"
if ! (cd "$SRC/ecdaa/build" && ctest --output-on-failure) > "$ECDAA_TESTS" 2>&1; then
  ecdaa_tests="FAIL"
fi
ecdaa_summary="$(grep -E 'tests passed' "$ECDAA_TESTS" | tail -1)"

# EPID SDK, with the SDK's own compiler flags, minus -Werror, plus -fno-strict-aliasing.
for pat in 'CMAKE_C_FLAGS} -Werror")' 'CMAKE_C_FLAGS} -Os")'; do
  count="$(grep -cF "$pat" "$SRC/epid-sdk/CMakeLists.txt" || true)"
  if [ "$count" != "1" ]; then
    echo "expected one line with $pat in the EPID SDK CMakeLists.txt, found $count" >&2
    exit 1
  fi
done
sed -i '/CMAKE_C_FLAGS} -Werror")/d' "$SRC/epid-sdk/CMakeLists.txt"
sed -i 's/CMAKE_C_FLAGS} -Os")/CMAKE_C_FLAGS} -Os -fno-strict-aliasing")/' "$SRC/epid-sdk/CMakeLists.txt"
git -C "$SRC/epid-sdk" diff > "$EPID_DIFF"
cmake -S "$SRC/epid-sdk" -B "$BUILD/epid-build" >/dev/null
cmake --build "$BUILD/epid-build" -j "$JOBS" --target member_tiny verifier >/dev/null

# The Part C program. Same compiler flags as Part A.
make -C "$HERE" clean >/dev/null
make -C "$HERE"
BIN="$HERE/bench_credential"

# Count crypto-extension instructions in the binary (aarch64 only).
crypto_count="null"
if [ "$(uname -m)" = "aarch64" ] && command -v objdump >/dev/null; then
  crypto_count="$(objdump -d "$BIN" | grep -E '\bpmull2?\b.*\.1q|\baes[edm]c?\b|\baesimc\b|\bsha(1|256|512)(h|h2|su0|su1|c|m|p)?\b' -c || true)"
fi

amcl_version="$(head -1 "$SRC/amcl/VERSION" 2>/dev/null || true)"

cat > "$INFO" <<EOF
{"libraries": [
  {"name": "AMCL", "url": "$AMCL_URL", "commit": "$AMCL_COMMIT", "version": "${amcl_version:-unknown}", "license": "Apache-2.0",
   "build": "CMake, AMCL's default build type Release (-O2), AMCL_CURVE=FP256BN, static libraries"},
  {"name": "Xaptum ECDAA", "url": "$ECDAA_URL", "commit": "$ECDAA_COMMIT", "license": "Apache-2.0",
   "build": "CMake Release (-O3), ECDAA_CURVES=FP256BN, ECDAA_TPM_SUPPORT=OFF, static library",
   "test_suite": "$ecdaa_tests", "test_summary": "$ecdaa_summary", "test_log": "$(basename "$ECDAA_TESTS")"},
  {"name": "Intel EPID SDK", "url": "$EPID_URL", "commit": "$EPID_COMMIT", "version": "8.0.0", "license": "Apache-2.0",
   "build": "CMake, no build type, the SDK's own C flags (-Os) without -Werror and with -fno-strict-aliasing; targets member_tiny and verifier",
   "build_changes_diff": "$(basename "$EPID_DIFF")"}],
 "program": "$BIN", "program_cflags": "-O2",
 "compiler": "$(${CC:-cc} --version | head -1)",
 "arch": "$(uname -m)", "crypto_extension_instructions_in_binary": $crypto_count}
EOF
echo "built $BIN"
cat "$INFO"
if [ "$ecdaa_tests" != "pass" ]; then
  echo "the ECDAA test suite failed; see $ECDAA_TESTS" >&2
  exit 1
fi

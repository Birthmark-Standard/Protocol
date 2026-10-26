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

# Part A build.
#   make         builds bench_capture with -O2 (the binary the driver uses by default)
#   make native  builds bench_capture_native with -O2 -march=native
#   make clean   removes both binaries

CC      ?= cc
OPT     := -O2
WARN    := -Wall -Wextra
PKGS    := libsodium libcrypto
PKG_CFLAGS := $(shell pkg-config --cflags $(PKGS))
LDLIBS  := $(shell pkg-config --libs $(PKGS))

SRC := bench_capture.c
HDR := sizes.h

.PHONY: all native clean

all: bench_capture

bench_capture: $(SRC) $(HDR)
	$(CC) $(OPT) $(WARN) $(PKG_CFLAGS) -DBUILD_CFLAGS='"$(OPT)"' -o $@ $(SRC) $(LDLIBS)

native: bench_capture_native

bench_capture_native: $(SRC) $(HDR)
	$(CC) $(OPT) -march=native $(WARN) $(PKG_CFLAGS) -DBUILD_CFLAGS='"$(OPT) -march=native"' -o $@ $(SRC) $(LDLIBS)

clean:
	rm -f bench_capture bench_capture_native

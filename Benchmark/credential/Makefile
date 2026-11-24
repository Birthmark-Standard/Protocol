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

# Part C build of bench_credential, with Part A's flags (-O2). The libraries
# under build/ come from fetch_and_build.sh, which runs this Makefile last.
#   make         builds bench_credential
#   make clean   removes it and its object files

CC      ?= cc
OPT     := -O2
WARN    := -Wall -Wextra
PKGS    := libsodium libcrypto
PKG_CFLAGS := $(shell pkg-config --cflags $(PKGS))
PKG_LIBS   := $(shell pkg-config --libs $(PKGS))

BUILD := build
DEPS  := $(BUILD)/deps
EPID  := $(BUILD)/src/epid-sdk
EPIDB := $(BUILD)/epid-build

ECDAA_INC := -I$(DEPS)/include
EPID_INC  := -I$(EPID)/epid/member/include -I$(EPID)/epid/verifier/include -I$(EPID)/epid/defs/include \
             -I$(EPID)/epid/internal/testhelper/include

ECDAA_LIBS := $(DEPS)/lib/libecdaa.a $(DEPS)/lib/libamcl_pairing_FP256BN.a \
              $(DEPS)/lib/libamcl_curve_FP256BN.a $(DEPS)/lib/libamcl_core.a
EPID_LIBS  := $(EPIDB)/epid/member/tiny/libmember_tiny.a $(EPIDB)/epid/internal/tinymath/libtinymath.a \
              $(EPIDB)/epid/internal/tinystdlib/libtinystdlib.a $(EPIDB)/epid/verifier/libverifier.a \
              $(EPIDB)/epid/internal/common/libcommon.a $(EPIDB)/epid/internal/ippmath/libipp_math.a \
              $(EPIDB)/ext/ipp-crypto/libipp-crypto.a

CFLAGS_ALL := $(OPT) $(WARN) $(PKG_CFLAGS) -DBUILD_CFLAGS='"$(OPT)"'

.PHONY: all clean

all: bench_credential

bench_credential.o: bench_credential.c rsabssa.h rfc9474_vectors.h daa.h ../device/bench_capture.c ../device/sizes.h
	$(CC) $(CFLAGS_ALL) -c -o $@ bench_credential.c

rsabssa.o: rsabssa.c rsabssa.h
	$(CC) $(CFLAGS_ALL) -c -o $@ rsabssa.c

daa_ecdaa.o: daa_ecdaa.c daa.h
	$(CC) $(CFLAGS_ALL) $(ECDAA_INC) -c -o $@ daa_ecdaa.c

daa_epid.o: daa_epid.c daa.h
	$(CC) $(CFLAGS_ALL) $(EPID_INC) -c -o $@ daa_epid.c

bench_credential: bench_credential.o rsabssa.o daa_ecdaa.o daa_epid.o
	$(CC) -o $@ $^ $(ECDAA_LIBS) $(EPID_LIBS) $(PKG_LIBS)

clean:
	rm -f bench_credential bench_credential.o rsabssa.o daa_ecdaa.o daa_epid.o

/*
 * Copyright (C) 2024-2026 The Birthmark Standard Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * One interface for the DAA or EPID signature libraries Part C measures.
 * Each library sits in its own file (daa_ecdaa.c, daa_epid.c), so their
 * headers never meet.
 */

#ifndef BENCHMARK_DAA_H
#define BENCHMARK_DAA_H

#include <stddef.h>
#include <stdint.h>

#define DAA_MAX_SIG 4096
#define DAA_MSG_LEN 32 /* ContentHash */

typedef struct {
    const char *key;           /* "ecdaa" or "epid": the --schemes name and the test-name prefix */
    const char *scheme;        /* e.g. "FIDO ECDAA" */
    const char *kind;          /* "DAA", "EPID" or "other group signature" */
    const char *library;       /* library and pinned commit */
    const char *curve;
    const char *security;      /* the library's stated security level, or that it states none */
    const char *keygen_desc;   /* what the member key generation row times */

    /* Issuer and member setup, untimed. Returns 0 on success. */
    int (*setup)(void);
    /* One member key generation. Returns elapsed nanoseconds, or -1. */
    int64_t (*keygen)(void);
    /* Sign msg in anonymous mode (no basename). Returns 0 on success. */
    int (*sign)(const uint8_t *msg, size_t msg_len, uint8_t *sig, size_t *sig_len);
    /* Verify with the library's verifier, anonymous mode. Returns 0 if valid. */
    int (*verify)(const uint8_t *msg, size_t msg_len, const uint8_t *sig, size_t sig_len);
    /* Extra correctness tests the library supports (join round trip, stored
     * test vectors). Calls report(name, pass, detail) for each. */
    void (*library_tests)(void (*report)(const char *, int, const char *));
} daa_scheme;

extern const daa_scheme DAA_ECDAA;
extern const daa_scheme DAA_EPID;

/* Monotonic clock in nanoseconds (CLOCK_MONOTONIC_RAW), defined in bench_credential.c. */
uint64_t partc_now_ns(void);
/* Random bytes from libsodium, defined in bench_credential.c. */
void partc_random(void *buf, size_t len);

#endif

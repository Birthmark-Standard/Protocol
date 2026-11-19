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
 * RSA blind signatures, client side, as RFC 9474 specifies (RSABSSA).
 *
 * Variants: RSABSSA-SHA384-PSS-Deterministic (salt length 48) and
 * RSABSSA-SHA384-PSSZERO-Deterministic (salt length 0). Deterministic
 * variants add no message prefix: the message is signed as given.
 *
 * Big-integer arithmetic is OpenSSL BIGNUM. RSASSA-PSS-VERIFY in Finalize is
 * OpenSSL's EVP verifier with PSS padding, SHA-384 and MGF1-SHA-384.
 */

#ifndef BENCHMARK_RSABSSA_H
#define BENCHMARK_RSABSSA_H

#include <stddef.h>

#include <openssl/bn.h>
#include <openssl/evp.h>

#define RSABSSA_HLEN 48 /* SHA-384 */
#define RSABSSA_MAX_MODULUS_BYTES 512

typedef struct {
    EVP_PKEY *pkey;      /* public key, used by the verifier */
    BIGNUM *n;
    BIGNUM *e;
    size_t modulus_len;  /* bytes */
    int mod_bits;
    size_t salt_len;     /* 48 for PSS, 0 for PSSZERO */
    BN_CTX *bn;
} rsabssa_pk;

/* Load the public key from pkey. Returns 0 on success. */
int rsabssa_pk_init(rsabssa_pk *pk, EVP_PKEY *pkey, size_t salt_len);
void rsabssa_pk_free(rsabssa_pk *pk);

/* EMSA-PSS-ENCODE (RFC 8017 section 9.1.1) with SHA-384, MGF1-SHA-384 and the
 * given salt. em receives modulus_len bytes. Returns 0 on success. */
int rsabssa_emsa_pss_encode(const rsabssa_pk *pk, unsigned char *em,
                            const unsigned char *msg, size_t msg_len,
                            const unsigned char *salt);

/*
 * Blind (RFC 9474 section 4.2) with the salt and the blinding factor r given
 * as inputs. This is the test entry point. blinded_msg and inv each receive
 * modulus_len bytes. Returns 0 on success.
 */
int rsabssa_blind_with(const rsabssa_pk *pk, unsigned char *blinded_msg, unsigned char *inv,
                       const unsigned char *msg, size_t msg_len,
                       const unsigned char *salt, const BIGNUM *r);

/* Blind with the salt and r drawn from OpenSSL's RNG. The timed path. */
int rsabssa_blind(const rsabssa_pk *pk, unsigned char *blinded_msg, unsigned char *inv,
                  const unsigned char *msg, size_t msg_len);

/*
 * Finalize (RFC 9474 section 4.4): sig = blind_sig * inv mod n, then
 * RSASSA-PSS-VERIFY. sig receives modulus_len bytes. Returns 0 if the
 * signature verifies, -1 otherwise.
 */
int rsabssa_finalize(const rsabssa_pk *pk, unsigned char *sig,
                     const unsigned char *blind_sig, const unsigned char *inv,
                     const unsigned char *msg, size_t msg_len);

/* RSASSA-PSS-VERIFY with the key's salt length. Returns 0 if valid. */
int rsabssa_verify(const rsabssa_pk *pk, const unsigned char *sig,
                   const unsigned char *msg, size_t msg_len);

#endif

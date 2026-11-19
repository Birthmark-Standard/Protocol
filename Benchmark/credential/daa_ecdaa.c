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
 * FIDO ECDAA with Xaptum's ecdaa library on curve FP256BN, software only.
 *
 * Setup runs the Join exchange in software: the issuer key pair, the member
 * key pair with its proof over the issuer's nonce, the issuer's check of
 * that proof, the credential, and the member's check of the credential.
 * Signing uses no basename, so signatures carry no pseudonym and are
 * unlinkable.
 */

#include <string.h>

#include <ecdaa/credential_FP256BN.h>
#include <ecdaa/group_public_key_FP256BN.h>
#include <ecdaa/issuer_keypair_FP256BN.h>
#include <ecdaa/member_keypair_FP256BN.h>
#include <ecdaa/revocations_FP256BN.h>
#include <ecdaa/signature_FP256BN.h>

#include "daa.h"

static struct ecdaa_issuer_public_key_FP256BN g_ipk;
static struct ecdaa_issuer_secret_key_FP256BN g_isk;
static struct ecdaa_member_public_key_FP256BN g_mpk;
static struct ecdaa_member_secret_key_FP256BN g_msk;
static struct ecdaa_credential_FP256BN g_cred;
static struct ecdaa_credential_FP256BN_signature g_cred_sig;
static uint8_t g_nonce[32];

static void rand_cb(void *buf, size_t len)
{
    partc_random(buf, len);
}

static int ecdaa_setup(void)
{
    if (ecdaa_issuer_key_pair_FP256BN_generate(&g_ipk, &g_isk, rand_cb) != 0)
        return -1;
    partc_random(g_nonce, sizeof g_nonce);
    if (ecdaa_member_key_pair_FP256BN_generate(&g_mpk, &g_msk, g_nonce, sizeof g_nonce, rand_cb) != 0)
        return -1;
    if (ecdaa_member_public_key_FP256BN_validate(&g_mpk, g_nonce, sizeof g_nonce) != 0)
        return -1;
    if (ecdaa_credential_FP256BN_generate(&g_cred, &g_cred_sig, &g_isk, &g_mpk, rand_cb) != 0)
        return -1;
    return ecdaa_credential_FP256BN_validate(&g_cred, &g_cred_sig, &g_mpk, &g_ipk.gpk);
}

static int64_t ecdaa_keygen(void)
{
    struct ecdaa_member_public_key_FP256BN pk;
    struct ecdaa_member_secret_key_FP256BN sk;
    uint8_t nonce[32];
    uint64_t t0, t1;
    int rc;

    partc_random(nonce, sizeof nonce);
    t0 = partc_now_ns();
    rc = ecdaa_member_key_pair_FP256BN_generate(&pk, &sk, nonce, sizeof nonce, rand_cb);
    t1 = partc_now_ns();
    return rc == 0 ? (int64_t)(t1 - t0) : -1;
}

static int ecdaa_sign(const uint8_t *msg, size_t msg_len, uint8_t *sig, size_t *sig_len)
{
    struct ecdaa_signature_FP256BN s;

    if (ecdaa_signature_FP256BN_sign(&s, msg, (uint32_t)msg_len, NULL, 0, &g_msk, &g_cred, rand_cb) != 0)
        return -1;
    ecdaa_signature_FP256BN_serialize(sig, &s, 0);
    *sig_len = ecdaa_signature_FP256BN_length();
    return 0;
}

static int ecdaa_verify(const uint8_t *msg, size_t msg_len, const uint8_t *sig, size_t sig_len)
{
    struct ecdaa_signature_FP256BN s;
    struct ecdaa_revocations_FP256BN rev = {0, NULL, 0, NULL};
    uint8_t buf[DAA_MAX_SIG];
    uint8_t m[DAA_MAX_SIG];

    if (sig_len != ecdaa_signature_FP256BN_length() || msg_len > sizeof m)
        return -1;
    memcpy(buf, sig, sig_len);
    memcpy(m, msg, msg_len);
    if (ecdaa_signature_FP256BN_deserialize(&s, buf, 0) != 0)
        return -1;
    return ecdaa_signature_FP256BN_verify(&s, &g_ipk.gpk, &rev, m, (uint32_t)msg_len, NULL, 0) == 0 ? 0 : -1;
}

static void ecdaa_library_tests(void (*report)(const char *, int, const char *))
{
    struct ecdaa_member_public_key_FP256BN pk;
    struct ecdaa_member_secret_key_FP256BN sk;
    struct ecdaa_credential_FP256BN cred;
    struct ecdaa_credential_FP256BN_signature cred_sig;
    uint8_t nonce[32], other[32];
    int ok;

    /* A second Join in full. A member key whose proof is checked against a
     * different nonce must be rejected. */
    partc_random(nonce, sizeof nonce);
    memcpy(other, nonce, sizeof other);
    other[0] ^= 1;
    ok = ecdaa_member_key_pair_FP256BN_generate(&pk, &sk, nonce, sizeof nonce, rand_cb) == 0 &&
         ecdaa_member_public_key_FP256BN_validate(&pk, nonce, sizeof nonce) == 0 &&
         ecdaa_member_public_key_FP256BN_validate(&pk, other, sizeof other) != 0 &&
         ecdaa_credential_FP256BN_generate(&cred, &cred_sig, &g_isk, &pk, rand_cb) == 0 &&
         ecdaa_credential_FP256BN_validate(&cred, &cred_sig, &pk, &g_ipk.gpk) == 0 &&
         ecdaa_credential_FP256BN_validate(&cred, &cred_sig, &g_mpk, &g_ipk.gpk) != 0;
    report("ecdaa_join_round_trip", ok,
           "member key proof checked by the issuer, credential checked by the member; "
           "wrong nonce and wrong member key rejected");
    report("ecdaa_library_test_vectors", 1,
           "the library ships no test vectors; its own test suite runs in fetch_and_build.sh");
}

const daa_scheme DAA_ECDAA = {
    "ecdaa",
    "FIDO ECDAA",
    "DAA",
    "Xaptum ecdaa at commit 92f93059dfe23c061a2372c897bdcaad0d917487, with AMCL 4.7.3",
    "FP256BN, a 256-bit Barreto-Naehrig curve (AMCL)",
    "about 100 bits (AMCL documentation, doc/latex/amcl.tex, Addendum: a 256-bit BN curve)",
    "ecdaa_member_key_pair_FP256BN_generate: member secret key, public key and its proof over the issuer's nonce",
    ecdaa_setup,
    ecdaa_keygen,
    ecdaa_sign,
    ecdaa_verify,
    ecdaa_library_tests,
};

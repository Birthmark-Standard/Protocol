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
 * Intel EPID 2.0 with the Intel EPID SDK's tiny member (software only) and
 * its verifier.
 *
 * The SDK has no issuer. Group grp_x and its member0 key come from the SDK's
 * own test data (epid/internal/testhelper/include/testhelper/testdata),
 * included at build time from the fetched SDK tree. The group's identifier
 * selects SHA-256. Signing uses no basename, so the SDK picks a random base
 * and signatures are unlinkable. No signature revocation list is set, so a
 * signature carries no non-revoked proofs.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "epid/member/api.h"
#include "epid/verifier.h"

#include "daa.h"

/* The SDK's test data files are flat byte lists; C fills the nested structs in order. */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmissing-braces"
static const GroupPubKey kGrpXKey = {
#include "testhelper/testdata/grp_x/pubkey.inc"
};

static const PrivKey kGrpXMember0PrivKey = {
#include "testhelper/testdata/grp_x/member0/mprivkey.inc"
};

/* The SDK's signature by member0 of grp_x on "msg0", SHA-256, random base. */
static const unsigned char kSigGrpXMember0Sha256RandbaseMsg0[] = {
#include "testhelper/testdata/grp_x/member0/sig_sha256_rndbase_msg0.inc"
};
#pragma GCC diagnostic pop

static MemberCtx *g_member;
static MemberCtx *g_join_member;
static size_t g_member_size;
static MemberParams g_params;
static VerifierCtx *g_verifier;

static int __STDCALL bit_supplier(unsigned int *rand_data, int num_bits, void *user_data)
{
    (void)user_data;
    if (num_bits <= 0)
        return -1;
    partc_random(rand_data, ((size_t)num_bits + 7) / 8);
    return 0;
}

/* On failure, the step and the SDK's status go to stderr, which the driver keeps in the raw log. */
static int step(const char *what, EpidStatus sts)
{
    if (sts != kEpidNoErr)
        fprintf(stderr, "EPID setup: %s returned %d\n", what, (int)sts);
    return sts == kEpidNoErr;
}

static int epid_setup(void)
{
    PrivKey priv = kGrpXMember0PrivKey;

    memset(&g_params, 0, sizeof g_params);
    /* The values of the SDK's signmsg example for the tiny member. */
    if (!step("EpidMemberSetEntropyGenerator", EpidMemberSetEntropyGenerator(bit_supplier, NULL, &g_params)) ||
        !step("EpidMemberSetMaxSigRlEntries", EpidMemberSetMaxSigRlEntries(5, &g_params)) ||
        !step("EpidMemberSetMaxAllowedBasenames", EpidMemberSetMaxAllowedBasenames(5, &g_params)) ||
        !step("EpidMemberSetMaxPrecomputedSigs", EpidMemberSetMaxPrecomputedSigs(1, &g_params)) ||
        !step("EpidMemberGetSize", EpidMemberGetSize(&g_params, &g_member_size)))
        return -1;
    g_member = calloc(1, g_member_size);
    g_join_member = calloc(1, g_member_size);
    if (!g_member || !g_join_member)
        return -1;
    if (!step("EpidMemberInit", EpidMemberInit(&g_params, g_member)) ||
        !step("EpidProvisionKey", EpidProvisionKey(g_member, &kGrpXKey, &priv, NULL)) ||
        !step("EpidMemberStartup", EpidMemberStartup(g_member)) ||
        !step("EpidVerifierCreate", EpidVerifierCreate(&kGrpXKey, NULL, &g_verifier)))
        return -1;
    return 0;
}

/* The member's part of Join: a fresh member secret f and the join request. */
static int64_t epid_keygen(void)
{
    IssuerNonce ni;
    unsigned char req[1024];
    uint64_t t0, t1;
    EpidStatus sts;

    if (EpidGetJoinRequestSize() > sizeof req)
        return -1;
    partc_random(&ni, sizeof ni);
    if (EpidMemberInit(&g_params, g_join_member) != kEpidNoErr)
        return -1;
    t0 = partc_now_ns();
    sts = EpidCreateJoinRequest(g_join_member, &kGrpXKey, &ni, (JoinRequest *)req, sizeof req);
    t1 = partc_now_ns();
    return sts == kEpidNoErr ? (int64_t)(t1 - t0) : -1;
}

static int epid_sign(const uint8_t *msg, size_t msg_len, uint8_t *sig, size_t *sig_len)
{
    size_t len = EpidGetSigSize(NULL);

    if (len > DAA_MAX_SIG)
        return -1;
    if (EpidSign(g_member, msg, msg_len, NULL, 0, (EpidSignature *)sig, len) != kEpidNoErr)
        return -1;
    *sig_len = len;
    return 0;
}

static int epid_verify(const uint8_t *msg, size_t msg_len, const uint8_t *sig, size_t sig_len)
{
    return EpidVerify(g_verifier, (EpidSignature const *)sig, sig_len, msg, msg_len) == kEpidSigValid ? 0 : -1;
}

static void epid_library_tests(void (*report)(const char *, int, const char *))
{
    static const unsigned char msg0[] = {'m', 's', 'g', '0'};
    static const unsigned char msg1[] = {'m', 's', 'g', '1'};
    unsigned char sig[sizeof kSigGrpXMember0Sha256RandbaseMsg0];
    unsigned char req[1024];
    IssuerNonce ni;
    int ok;

    ok = epid_verify(msg0, sizeof msg0, kSigGrpXMember0Sha256RandbaseMsg0,
                     sizeof kSigGrpXMember0Sha256RandbaseMsg0) == 0 &&
         epid_verify(msg1, sizeof msg1, kSigGrpXMember0Sha256RandbaseMsg0,
                     sizeof kSigGrpXMember0Sha256RandbaseMsg0) != 0;
    memcpy(sig, kSigGrpXMember0Sha256RandbaseMsg0, sizeof sig);
    sig[40] ^= 1;
    ok = ok && epid_verify(msg0, sizeof msg0, sig, sizeof sig) != 0;
    report("epid_sdk_stored_signature", ok,
           "SDK test data grp_x/member0/sig_sha256_rndbase_msg0 verifies on msg0; "
           "rejected on msg1 and with one flipped byte");

    partc_random(&ni, sizeof ni);
    ok = EpidGetJoinRequestSize() <= sizeof req &&
         EpidMemberInit(&g_params, g_join_member) == kEpidNoErr &&
         EpidCreateJoinRequest(g_join_member, &kGrpXKey, &ni, (JoinRequest *)req, sizeof req) == kEpidNoErr;
    report("epid_join_request", ok,
           "the member creates a join request; the SDK has no issuer to check it");
}

const daa_scheme DAA_EPID = {
    "epid",
    "Intel EPID 2.0",
    "EPID",
    "Intel EPID SDK 8.0.0 at commit ceb0a9e77b01b5e9c67619aeddae7b42dad71134, tiny member",
    "EPID 2.0 parameters, 256-bit prime field (epid20_q in the SDK's tinymath/src/fq.c)",
    "not stated in the SDK documentation",
    "EpidCreateJoinRequest: fresh member secret f and the join request (F, c, s)",
    epid_setup,
    epid_keygen,
    epid_sign,
    epid_verify,
    epid_library_tests,
};

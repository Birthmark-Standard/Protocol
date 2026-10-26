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
 * Part A: device-side cost of one Birthmark capture.
 *
 * X25519 comes from libsodium. SHA-256, AES-256-GCM and HKDF-SHA256 come from
 * OpenSSL EVP. libsodium's crypto_hash_sha256 is a portable-C reference for
 * the file hash.
 *
 * The program runs its correctness tests first. If any test fails it prints
 * the failure and exits with status 2 before timing anything.
 *
 * Output is one JSON object per line on stdout. Every timing row carries its
 * raw samples in nanoseconds. Statistics are computed by the Python driver.
 */

#define _GNU_SOURCE
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/perf_event.h>

#include <sodium.h>

#include <openssl/bn.h>
#include <openssl/core_names.h>
#include <openssl/crypto.h>
#include <openssl/evp.h>
#include <openssl/kdf.h>
#include <openssl/opensslv.h>
#include <openssl/params.h>

#include "sizes.h"

#ifndef BUILD_CFLAGS
#define BUILD_CFLAGS "unknown"
#endif

#define ECIES_VERSION_BYTE 0x01

/* Placeholder KDF label. The papers do not yet specify the key-derivation function. */
static const char HKDF_INFO[] = "ECIES AES-256-GCM key and nonce, HKDF-SHA256 placeholder";

/* Fixed AEAD nonce for Enc_FullPacketHash. BlindShare_key is single use. */
static const unsigned char ENC_FPH_NONCE[AEAD_NONCE_LEN] = {0};

/* ------------------------------------------------------------------------ */
/* OpenSSL state, created once and reused, as device code would.             */

static EVP_MD *g_sha256;
static EVP_MD_CTX *g_mdctx;
static EVP_CIPHER *g_gcm;
static EVP_CIPHER_CTX *g_enc;
static EVP_CIPHER_CTX *g_dec;
static EVP_KDF_CTX *g_kdf;

static int crypto_init(void)
{
    EVP_KDF *kdf;
    OSSL_PARAM p[2];

    if (sodium_init() < 0)
        return -1;
    g_sha256 = EVP_MD_fetch(NULL, "SHA256", NULL);
    g_mdctx = EVP_MD_CTX_new();
    g_gcm = EVP_CIPHER_fetch(NULL, "AES-256-GCM", NULL);
    g_enc = EVP_CIPHER_CTX_new();
    g_dec = EVP_CIPHER_CTX_new();
    kdf = EVP_KDF_fetch(NULL, "HKDF", NULL);
    if (!g_sha256 || !g_mdctx || !g_gcm || !g_enc || !g_dec || !kdf)
        return -1;
    g_kdf = EVP_KDF_CTX_new(kdf);
    EVP_KDF_free(kdf);
    if (!g_kdf)
        return -1;
    p[0] = OSSL_PARAM_construct_utf8_string(OSSL_KDF_PARAM_DIGEST, (char *)"SHA256", 0);
    p[1] = OSSL_PARAM_construct_end();
    if (EVP_KDF_CTX_set_params(g_kdf, p) != 1)
        return -1;
    if (EVP_EncryptInit_ex2(g_enc, g_gcm, NULL, NULL, NULL) != 1)
        return -1;
    if (EVP_DecryptInit_ex2(g_dec, g_gcm, NULL, NULL, NULL) != 1)
        return -1;
    return 0;
}

static int sha256_openssl(unsigned char out[32], const unsigned char *in, size_t len)
{
    unsigned int outl = 0;

    if (EVP_DigestInit_ex(g_mdctx, g_sha256, NULL) != 1)
        return -1;
    if (EVP_DigestUpdate(g_mdctx, in, len) != 1)
        return -1;
    if (EVP_DigestFinal_ex(g_mdctx, out, &outl) != 1 || outl != 32)
        return -1;
    return 0;
}

static int sha256_libsodium(unsigned char out[32], const unsigned char *in, size_t len)
{
    return crypto_hash_sha256(out, in, len);
}

static int hkdf_sha256(unsigned char *out, size_t outlen,
                       const unsigned char *ikm, size_t ikmlen,
                       const unsigned char *salt, size_t saltlen,
                       const unsigned char *info, size_t infolen)
{
    OSSL_PARAM p[4];

    p[0] = OSSL_PARAM_construct_octet_string(OSSL_KDF_PARAM_KEY, (void *)ikm, ikmlen);
    p[1] = OSSL_PARAM_construct_octet_string(OSSL_KDF_PARAM_SALT, (void *)salt, saltlen);
    p[2] = OSSL_PARAM_construct_octet_string(OSSL_KDF_PARAM_INFO, (void *)info, infolen);
    p[3] = OSSL_PARAM_construct_end();
    return EVP_KDF_derive(g_kdf, out, outlen, p) == 1 ? 0 : -1;
}

/* AES-256-GCM. ct receives len bytes, tag receives AEAD_TAG_LEN bytes. */
static int aead_seal(unsigned char *ct, unsigned char *tag,
                     const unsigned char *key, const unsigned char *nonce,
                     const unsigned char *aad, size_t aadlen,
                     const unsigned char *pt, size_t len)
{
    int outl = 0, finl = 0;

    if (EVP_EncryptInit_ex2(g_enc, NULL, key, nonce, NULL) != 1)
        return -1;
    if (aadlen && EVP_EncryptUpdate(g_enc, NULL, &outl, aad, (int)aadlen) != 1)
        return -1;
    if (EVP_EncryptUpdate(g_enc, ct, &outl, pt, (int)len) != 1)
        return -1;
    if (EVP_EncryptFinal_ex(g_enc, ct + outl, &finl) != 1 || (size_t)(outl + finl) != len)
        return -1;
    if (EVP_CIPHER_CTX_ctrl(g_enc, EVP_CTRL_GCM_GET_TAG, AEAD_TAG_LEN, tag) != 1)
        return -1;
    return 0;
}

static int aead_open(unsigned char *pt, const unsigned char *key, const unsigned char *nonce,
                     const unsigned char *aad, size_t aadlen,
                     const unsigned char *ct, size_t len, const unsigned char *tag)
{
    int outl = 0, finl = 0;

    if (EVP_DecryptInit_ex2(g_dec, NULL, key, nonce, NULL) != 1)
        return -1;
    if (aadlen && EVP_DecryptUpdate(g_dec, NULL, &outl, aad, (int)aadlen) != 1)
        return -1;
    if (EVP_DecryptUpdate(g_dec, pt, &outl, ct, (int)len) != 1)
        return -1;
    if (EVP_CIPHER_CTX_ctrl(g_dec, EVP_CTRL_GCM_SET_TAG, AEAD_TAG_LEN, (void *)tag) != 1)
        return -1;
    if (EVP_DecryptFinal_ex(g_dec, pt + outl, &finl) != 1)
        return -1;
    return (size_t)(outl + finl) == len ? 0 : -1;
}

/* ------------------------------------------------------------------------ */
/* ECIES and ECIESb.                                                          */
/*                                                                            */
/* Wire layout: version byte || EPK (32) || ciphertext || tag (16).           */
/* gp == NULL: ECIES with the standard base point, EPK = e*B.                 */
/* gp != NULL: ECIESb to a Channel Key (GP, pk), EPK = e*GP.                  */
/* Shared secret e*pk. HKDF-SHA256(ikm = shared secret, salt = EPK) gives the */
/* AES-256-GCM key and the 12-byte nonce. The nonce is not sent.              */
/* AAD = version byte || EPK.                                                 */

static int ecies_seal(unsigned char *out, const unsigned char *gp, const unsigned char *pk,
                      const unsigned char *pt, size_t len)
{
    unsigned char e[32], ss[32], okm[AEAD_KEY_LEN + AEAD_NONCE_LEN];
    unsigned char *epk = out + ECIES_VERSION_LEN;
    unsigned char *ct = epk + ECIES_EPK_LEN;
    int rc = -1;

    randombytes_buf(e, sizeof e);
    out[0] = ECIES_VERSION_BYTE;
    if (gp == NULL) {
        if (crypto_scalarmult_base(epk, e) != 0)
            goto done;
    } else if (crypto_scalarmult(epk, e, gp) != 0) {
        goto done;
    }
    if (crypto_scalarmult(ss, e, pk) != 0)
        goto done;
    if (hkdf_sha256(okm, sizeof okm, ss, sizeof ss, epk, ECIES_EPK_LEN,
                    (const unsigned char *)HKDF_INFO, sizeof HKDF_INFO - 1) != 0)
        goto done;
    if (aead_seal(ct, ct + len, okm, okm + AEAD_KEY_LEN,
                  out, ECIES_VERSION_LEN + ECIES_EPK_LEN, pt, len) != 0)
        goto done;
    rc = 0;
done:
    sodium_memzero(e, sizeof e);
    sodium_memzero(ss, sizeof ss);
    sodium_memzero(okm, sizeof okm);
    return rc;
}

/* Returns the plaintext length, or -1. */
static long ecies_open(unsigned char *pt, const unsigned char *sk, const unsigned char *in, size_t inlen)
{
    unsigned char ss[32], okm[AEAD_KEY_LEN + AEAD_NONCE_LEN];
    const unsigned char *epk = in + ECIES_VERSION_LEN;
    const unsigned char *ct = epk + ECIES_EPK_LEN;
    size_t len;
    long rc = -1;

    if (inlen < ECIES_OVERHEAD || in[0] != ECIES_VERSION_BYTE)
        return -1;
    len = inlen - ECIES_OVERHEAD;
    if (crypto_scalarmult(ss, sk, epk) != 0)
        goto done;
    if (hkdf_sha256(okm, sizeof okm, ss, sizeof ss, epk, ECIES_EPK_LEN,
                    (const unsigned char *)HKDF_INFO, sizeof HKDF_INFO - 1) != 0)
        goto done;
    if (aead_open(pt, okm, okm + AEAD_KEY_LEN, in, ECIES_VERSION_LEN + ECIES_EPK_LEN,
                  ct, len, ct + len) != 0)
        goto done;
    rc = (long)len;
done:
    sodium_memzero(ss, sizeof ss);
    sodium_memzero(okm, sizeof okm);
    return rc;
}

/* ------------------------------------------------------------------------ */
/* Channel Key generation and the prime-order subgroup check.                 */

/*
 * Map a Montgomery u-coordinate to the Edwards y-coordinate,
 * y = (u - 1) / (u + 1) mod p, encoded little-endian with sign bit 0.
 */
static int u_to_edwards_y(unsigned char y_le[32], const unsigned char u_le[32])
{
    BN_CTX *bc = BN_CTX_new();
    BIGNUM *p = BN_new(), *u = BN_new(), *one = BN_new(), *num = BN_new(), *den = BN_new(), *y = BN_new();
    unsigned char be[32];
    int i, rc = -1;

    if (!bc || !p || !u || !one || !num || !den || !y)
        goto done;
    BN_zero(p);
    if (!BN_set_bit(p, 255) || !BN_sub_word(p, 19) || !BN_one(one))
        goto done;
    for (i = 0; i < 32; i++)
        be[i] = u_le[31 - i];
    if (!BN_bin2bn(be, 32, u) || BN_cmp(u, p) >= 0)
        goto done;
    if (!BN_mod_sub(num, u, one, p, bc) || !BN_mod_add(den, u, one, p, bc) || BN_is_zero(den))
        goto done;
    if (!BN_mod_inverse(den, den, p, bc) || !BN_mod_mul(y, num, den, p, bc))
        goto done;
    if (BN_bn2binpad(y, be, 32) != 32)
        goto done;
    for (i = 0; i < 32; i++)
        y_le[i] = be[31 - i];
    rc = 0;
done:
    BN_free(p); BN_free(u); BN_free(one); BN_free(num); BN_free(den); BN_free(y);
    BN_CTX_free(bc);
    return rc;
}

/*
 * True if u is not the identity, not of small order, and lies in the
 * prime-order subgroup. libsodium's crypto_core_ed25519_is_valid_point
 * performs the subgroup check on the Edwards form.
 */
static int u_in_prime_subgroup(const unsigned char u_le[32])
{
    unsigned char y[32];

    if (u_to_edwards_y(y, u_le) != 0)
        return 0;
    return crypto_core_ed25519_is_valid_point(y) == 1;
}

typedef struct {
    unsigned char sk[32];
    unsigned char gp[32];
    unsigned char pk[32];
} channel_key;

/* GP = r*B for random r, then pk = sk*GP. Returns -1 if GP fails the check. */
static int make_channel_key(channel_key *k)
{
    unsigned char r[32];

    randombytes_buf(r, sizeof r);
    randombytes_buf(k->sk, sizeof k->sk);
    if (crypto_scalarmult_base(k->gp, r) != 0)
        return -1;
    sodium_memzero(r, sizeof r);
    if (!u_in_prime_subgroup(k->gp))
        return -1;
    return crypto_scalarmult(k->pk, k->sk, k->gp);
}

typedef struct {
    unsigned char sk[32];
    unsigned char pk[32];
} std_key;

static int make_std_key(std_key *k)
{
    randombytes_buf(k->sk, sizeof k->sk);
    return crypto_scalarmult_base(k->pk, k->sk);
}

/* ------------------------------------------------------------------------ */
/* One capture.                                                              */

typedef struct {
    std_key v_token;           /* validator Token Key, layer 1 */
    channel_key dest[3];       /* Channel Keys of C, F, I, layers 2 to 4 */
    std_key relay[3];          /* Server Transit Keys of first relays A, D, G, layers 5 to 7 */
    unsigned char routing_code[3][ROUTING_CODE_LEN];
    unsigned char cred_hw[CRED_HW_LEN];
    unsigned char key_ref[KEY_REF_LEN];
    unsigned char claim[CLAIM_LEN];
} setup_keys;

enum { DEST_C = 0, DEST_F = 1, DEST_I = 2 };

typedef struct {
    unsigned char content_hash[CONTENTHASH_LEN];
    unsigned char n[CONTENT_NONCE_LEN];
    unsigned char flags;
    unsigned char metadata_commitments[METADATA_COMMITMENTS_LEN];
    unsigned char h_metadata[H_METADATA_LEN];
    unsigned char fph_input[FULLPACKETHASH_INPUT_LEN];
    unsigned char fullpackethash[FULLPACKETHASH_LEN];
    unsigned char replay_nonce[REPLAY_NONCE_LEN];
    unsigned char blindshare_key[BLINDSHARE_KEY_LEN];
    unsigned char enc_fullpackethash[ENC_FULLPACKETHASH_LEN];
    unsigned char binding_hash[BINDING_HASH_LEN];

    unsigned char token_pt[TOKEN_PT_LEN];
    unsigned char token_ct[TOKEN_CT_LEN];
    unsigned char credp_pt[CREDP_PT_LEN];
    unsigned char credp_ct[CREDP_CT_LEN];
    unsigned char contp_pt[CONTP_PT_LEN_CAPTURE];
    unsigned char contp_f_ct[CONTP_CT_LEN_CAPTURE];
    unsigned char contp_i_ct[CONTP_CT_LEN_CAPTURE];
    unsigned char wrap_pt[3][WRAP_PADDED_PT_LEN];
    size_t wrap_pt_len[3];
    unsigned char wrap_ct[3][WRAP_PADDED_PT_LEN + ECIES_OVERHEAD];
} capture;

typedef int (*hash_fn)(unsigned char out[32], const unsigned char *in, size_t len);

/* Step 1: ContentHash = SHA-256(file). */
static int step_content_hash(capture *c, const unsigned char *file, size_t len, hash_fn h)
{
    return h(c->content_hash, file, len);
}

/*
 * Steps 2 and 3: n, h(metadata), FullPacketHash.
 * The three metadata commitments are random stand-ins. Computing them is not
 * measured.
 */
static int step_fullpackethash(capture *c)
{
    unsigned char *p = c->fph_input;

    randombytes_buf(c->n, sizeof c->n);
    c->flags = 0x01; /* h(metadata) present, no parent ContentHash */
    randombytes_buf(c->metadata_commitments, sizeof c->metadata_commitments);
    if (sha256_openssl(c->h_metadata, c->metadata_commitments, sizeof c->metadata_commitments) != 0)
        return -1;
    memcpy(p, c->content_hash, CONTENTHASH_LEN); p += CONTENTHASH_LEN;
    memcpy(p, c->n, CONTENT_NONCE_LEN); p += CONTENT_NONCE_LEN;
    *p++ = c->flags;
    memcpy(p, c->h_metadata, H_METADATA_LEN);
    return sha256_openssl(c->fullpackethash, c->fph_input, sizeof c->fph_input);
}

/* Steps 4 and 5: replay_nonce, BlindShare_key, Enc_FullPacketHash, binding_hash. */
static int step_binding(capture *c)
{
    randombytes_buf(c->replay_nonce, sizeof c->replay_nonce);
    randombytes_buf(c->blindshare_key, sizeof c->blindshare_key);
    if (aead_seal(c->enc_fullpackethash, c->enc_fullpackethash + FULLPACKETHASH_LEN,
                  c->blindshare_key, ENC_FPH_NONCE, NULL, 0,
                  c->fullpackethash, FULLPACKETHASH_LEN) != 0)
        return -1;
    return sha256_openssl(c->binding_hash, c->enc_fullpackethash, ENC_FULLPACKETHASH_LEN);
}

/* Steps 6 to 9: the seven ECIES layers, in the order of the specification. */
static int step_layers(capture *c, const setup_keys *k, int padded)
{
    unsigned char *p;
    const unsigned char *inner[3];
    size_t inner_len[3];
    int i;

    /* Layer 1: T = ECIES(V-token_pk; Cred_HW || replay_nonce || claim || binding_hash). */
    p = c->token_pt;
    memcpy(p, k->cred_hw, CRED_HW_LEN); p += CRED_HW_LEN;
    memcpy(p, c->replay_nonce, REPLAY_NONCE_LEN); p += REPLAY_NONCE_LEN;
    memcpy(p, k->claim, CLAIM_LEN); p += CLAIM_LEN;
    memcpy(p, c->binding_hash, BINDING_HASH_LEN);
    if (ecies_seal(c->token_ct, NULL, k->v_token.pk, c->token_pt, TOKEN_PT_LEN) != 0)
        return -1;

    /* Layer 2: CredP = ECIESb(Channel Key of C; T || key_ref || FullPacketHash || BlindShare_key). */
    p = c->credp_pt;
    memcpy(p, c->token_ct, TOKEN_CT_LEN); p += TOKEN_CT_LEN;
    memcpy(p, k->key_ref, KEY_REF_LEN); p += KEY_REF_LEN;
    memcpy(p, c->fullpackethash, FULLPACKETHASH_LEN); p += FULLPACKETHASH_LEN;
    memcpy(p, c->blindshare_key, BLINDSHARE_KEY_LEN);
    if (ecies_seal(c->credp_ct, k->dest[DEST_C].gp, k->dest[DEST_C].pk, c->credp_pt, CREDP_PT_LEN) != 0)
        return -1;

    /* Layers 3 and 4: ContP_F and ContP_I = ECIESb(Channel Key; flags || ContentHash || n || h(metadata)). */
    p = c->contp_pt;
    *p++ = c->flags;
    memcpy(p, c->content_hash, CONTENTHASH_LEN); p += CONTENTHASH_LEN;
    memcpy(p, c->n, CONTENT_NONCE_LEN); p += CONTENT_NONCE_LEN;
    memcpy(p, c->h_metadata, H_METADATA_LEN);
    if (ecies_seal(c->contp_f_ct, k->dest[DEST_F].gp, k->dest[DEST_F].pk, c->contp_pt, CONTP_PT_LEN_CAPTURE) != 0)
        return -1;
    if (ecies_seal(c->contp_i_ct, k->dest[DEST_I].gp, k->dest[DEST_I].pk, c->contp_pt, CONTP_PT_LEN_CAPTURE) != 0)
        return -1;

    /* Layers 5 to 7: first-relay wraps = ECIES(Server Transit Key; routing code || packet). */
    inner[0] = c->credp_ct;   inner_len[0] = CREDP_CT_LEN;
    inner[1] = c->contp_f_ct; inner_len[1] = CONTP_CT_LEN_CAPTURE;
    inner[2] = c->contp_i_ct; inner_len[2] = CONTP_CT_LEN_CAPTURE;
    for (i = 0; i < 3; i++) {
        size_t len = ROUTING_CODE_LEN + inner_len[i];
        memcpy(c->wrap_pt[i], k->routing_code[i], ROUTING_CODE_LEN);
        memcpy(c->wrap_pt[i] + ROUTING_CODE_LEN, inner[i], inner_len[i]);
        if (padded) {
            /* Zero padding. The padding format is not specified. */
            memset(c->wrap_pt[i] + len, 0, WRAP_PADDED_PT_LEN - len);
            len = WRAP_PADDED_PT_LEN;
        }
        c->wrap_pt_len[i] = len;
        if (ecies_seal(c->wrap_ct[i], NULL, k->relay[i].pk, c->wrap_pt[i], len) != 0)
            return -1;
    }
    return 0;
}

static int whole_capture(capture *c, const setup_keys *k, const unsigned char *file, size_t len,
                         hash_fn h, int padded)
{
    if (step_content_hash(c, file, len, h) != 0)
        return -1;
    if (step_fullpackethash(c) != 0)
        return -1;
    if (step_binding(c) != 0)
        return -1;
    return step_layers(c, k, padded);
}

static int make_setup_keys(setup_keys *k)
{
    int i;

    if (make_std_key(&k->v_token) != 0)
        return -1;
    for (i = 0; i < 3; i++) {
        if (make_channel_key(&k->dest[i]) != 0)
            return -1;
        if (make_std_key(&k->relay[i]) != 0)
            return -1;
        randombytes_buf(k->routing_code[i], ROUTING_CODE_LEN);
    }
    randombytes_buf(k->cred_hw, sizeof k->cred_hw);
    randombytes_buf(k->key_ref, sizeof k->key_ref);
    memset(k->claim, 0, sizeof k->claim); /* zero for a hardware capture */
    return 0;
}

/* ------------------------------------------------------------------------ */
/* Output helpers.                                                           */

static int g_selftest_failures;

static void report_test(const char *name, int pass, const char *detail)
{
    printf("{\"type\":\"selftest\",\"name\":\"%s\",\"pass\":%s,\"detail\":\"%s\"}\n",
           name, pass ? "true" : "false", detail ? detail : "");
    if (!pass)
        g_selftest_failures++;
}

static int hex_eq(const unsigned char *b, size_t len, const char *hex)
{
    unsigned char want[256];
    size_t wl = 0;

    if (sodium_hex2bin(want, sizeof want, hex, strlen(hex), NULL, &wl, NULL) != 0 || wl != len)
        return 0;
    return memcmp(b, want, len) == 0;
}

static void hex_to_bin(unsigned char *out, size_t outlen, const char *hex)
{
    size_t wl = 0;

    if (sodium_hex2bin(out, outlen, hex, strlen(hex), NULL, &wl, NULL) != 0 || wl != outlen)
        memset(out, 0, outlen);
}

/* ------------------------------------------------------------------------ */
/* Correctness tests. Run before any timing.                                 */

static void test_sha256(const unsigned char *buf, size_t buflen)
{
    static const struct { const char *msg; const char *digest; } kat[] = {
        {"", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},
        {"abc", "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"},
        {"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq",
         "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1"},
    };
    unsigned char d1[32], d2[32], *million;
    size_t i;
    int ok = 1;

    for (i = 0; i < sizeof kat / sizeof kat[0]; i++) {
        size_t l = strlen(kat[i].msg);
        if (sha256_openssl(d1, (const unsigned char *)kat[i].msg, l) != 0 || !hex_eq(d1, 32, kat[i].digest))
            ok = 0;
        if (sha256_libsodium(d2, (const unsigned char *)kat[i].msg, l) != 0 || !hex_eq(d2, 32, kat[i].digest))
            ok = 0;
    }
    million = malloc(1000000);
    if (!million) {
        ok = 0;
    } else {
        memset(million, 'a', 1000000);
        if (sha256_openssl(d1, million, 1000000) != 0 ||
            !hex_eq(d1, 32, "cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0"))
            ok = 0;
        if (sha256_libsodium(d2, million, 1000000) != 0 ||
            !hex_eq(d2, 32, "cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0"))
            ok = 0;
        free(million);
    }
    report_test("sha256_known_answer", ok, "FIPS 180-2 vectors and one million 'a', OpenSSL and libsodium");

    ok = sha256_openssl(d1, buf, buflen) == 0 && sha256_libsodium(d2, buf, buflen) == 0 &&
         memcmp(d1, d2, 32) == 0;
    report_test("sha256_openssl_equals_libsodium_on_file_buffer", ok, "largest file buffer");
}

static void test_hkdf(void)
{
    /* RFC 5869, test case 1. */
    unsigned char ikm[22], salt[13], info[10], okm[42], other[44];
    int ok;

    memset(ikm, 0x0b, sizeof ikm);
    hex_to_bin(salt, sizeof salt, "000102030405060708090a0b0c");
    hex_to_bin(info, sizeof info, "f0f1f2f3f4f5f6f7f8f9");
    /* A different derivation first, to show no state carries over between calls. */
    if (hkdf_sha256(other, sizeof other, info, sizeof info, ikm, sizeof ikm, salt, sizeof salt) != 0) {
        report_test("hkdf_sha256_known_answer", 0, "derive failed");
        return;
    }
    ok = hkdf_sha256(okm, sizeof okm, ikm, sizeof ikm, salt, sizeof salt, info, sizeof info) == 0 &&
         hex_eq(okm, sizeof okm,
                "3cb25f25faacd57a90434f64d0362f2a2d2d0a90cf1a5a4c5db02d56ecc4c5bf34007208d5b887185865");
    report_test("hkdf_sha256_known_answer", ok, "RFC 5869 test case 1");
}

static void test_x25519(void)
{
    /* RFC 7748, section 6.1. */
    unsigned char a_sk[32], b_sk[32], a_pk[32], b_pk[32], s1[32], s2[32];
    int ok;

    hex_to_bin(a_sk, 32, "77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a");
    hex_to_bin(b_sk, 32, "5dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb");
    ok = crypto_scalarmult_base(a_pk, a_sk) == 0 &&
         hex_eq(a_pk, 32, "8520f0098930a754748b7ddcb43ef75a0dbf3a0d26381af4eba4a98eaa9b4e6a") &&
         crypto_scalarmult_base(b_pk, b_sk) == 0 &&
         hex_eq(b_pk, 32, "de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f") &&
         crypto_scalarmult(s1, a_sk, b_pk) == 0 && crypto_scalarmult(s2, b_sk, a_pk) == 0 &&
         hex_eq(s1, 32, "4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742") &&
         memcmp(s1, s2, 32) == 0;
    report_test("x25519_known_answer", ok, "RFC 7748 section 6.1");
}

static void test_aes_gcm(void)
{
    /* McGrew and Viega, GCM test cases 13 and 14 (AES-256, zero key and IV). */
    unsigned char key[32] = {0}, iv[12] = {0}, pt[16] = {0}, ct[16], tag[16], back[16];
    unsigned char msg[203], enc[203], dec[203];
    int ok;

    ok = aead_seal(ct, tag, key, iv, NULL, 0, pt, 0) == 0 &&
         hex_eq(tag, 16, "530f8afbc74536b9a963b4f1c4cb738b");
    ok = ok && aead_seal(ct, tag, key, iv, NULL, 0, pt, 16) == 0 &&
         hex_eq(ct, 16, "cea7403d4d606b6e074ec5d3baf39d18") &&
         hex_eq(tag, 16, "d0d1c8a799996bf0265b98b5d48ab919");
    ok = ok && aead_open(back, key, iv, NULL, 0, ct, 16, tag) == 0 && memcmp(back, pt, 16) == 0;
    report_test("aes256gcm_known_answer", ok, "GCM spec test cases 13 and 14");

    randombytes_buf(key, sizeof key);
    randombytes_buf(iv, sizeof iv);
    randombytes_buf(msg, sizeof msg);
    ok = aead_seal(enc, tag, key, iv, iv, sizeof iv, msg, sizeof msg) == 0 &&
         aead_open(dec, key, iv, iv, sizeof iv, enc, sizeof enc, tag) == 0 &&
         memcmp(dec, msg, sizeof msg) == 0;
    enc[7] ^= 1;
    ok = ok && aead_open(dec, key, iv, iv, sizeof iv, enc, sizeof enc, tag) != 0;
    report_test("aes256gcm_round_trip_and_tamper_rejected", ok, "203 B random plaintext");
}

static void test_subgroup_check(const setup_keys *k)
{
    unsigned char y[32], order2[32], mixed[32], zero[32] = {0};
    int ok;

    /* Edwards (0, -1) has order 2. -1 mod p, little-endian. */
    hex_to_bin(order2, 32, "ecffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f");
    ok = u_in_prime_subgroup(k->dest[0].gp) && u_in_prime_subgroup(k->dest[1].gp) &&
         u_in_prime_subgroup(k->dest[2].gp);
    ok = ok && !u_in_prime_subgroup(zero);
    ok = ok && u_to_edwards_y(y, k->dest[0].gp) == 0 &&
         crypto_core_ed25519_add(mixed, y, order2) == 0 &&
         crypto_core_ed25519_is_valid_point(mixed) == 0;
    report_test("generator_point_prime_order_subgroup", ok,
                "three GP accepted; u = 0 rejected; GP plus an order-2 point rejected");
}

static void test_ecies_overhead(const setup_keys *k)
{
    char detail[160];
    unsigned char pt[CREDP_PT_LEN], ct[CREDP_CT_LEN];

    randombytes_buf(pt, sizeof pt);
    snprintf(detail, sizeof detail,
             "measured overhead %d B (version %d + EPK %d + tag %d); Table A.1 gives %d B",
             (int)(sizeof ct - sizeof pt), ECIES_VERSION_LEN, ECIES_EPK_LEN, AEAD_TAG_LEN, SPEC_ECIES_OVERHEAD);
    report_test("ecies_overhead_matches_table_a1",
                ecies_seal(ct, k->dest[0].gp, k->dest[0].pk, pt, sizeof pt) == 0 &&
                    (int)(sizeof ct - sizeof pt) == SPEC_ECIES_OVERHEAD,
                detail);
}

/* Build one full capture, then decrypt all seven layers with the matching secret keys. */
static void test_full_decrypt(const setup_keys *k, const unsigned char *file, size_t len, int padded)
{
    static capture c;
    unsigned char inner[WRAP_PADDED_PT_LEN], pkt[WRAP_PADDED_PT_LEN], tok[TOKEN_PT_LEN];
    unsigned char fph_check[FULLPACKETHASH_INPUT_LEN], d[32], enc_c[ENC_FULLPACKETHASH_LEN], fph_back[32];
    const unsigned char *exp_inner[3];
    size_t exp_len[3];
    const int dest_of_wrap[3] = {DEST_C, DEST_F, DEST_I};
    long l;
    int i, ok = 1;

    if (whole_capture(&c, k, file, len, sha256_openssl, padded) != 0) {
        report_test(padded ? "seven_layer_decrypt_padded" : "seven_layer_decrypt", 0, "build failed");
        return;
    }
    exp_inner[0] = c.credp_ct;   exp_len[0] = CREDP_CT_LEN;
    exp_inner[1] = c.contp_f_ct; exp_len[1] = CONTP_CT_LEN_CAPTURE;
    exp_inner[2] = c.contp_i_ct; exp_len[2] = CONTP_CT_LEN_CAPTURE;

    for (i = 0; i < 3 && ok; i++) {
        size_t wl = c.wrap_pt_len[i] + ECIES_OVERHEAD;
        /* Layers 5 to 7: the first relay opens its wrap. */
        l = ecies_open(inner, k->relay[i].sk, c.wrap_ct[i], wl);
        ok = l == (long)c.wrap_pt_len[i] &&
             memcmp(inner, k->routing_code[i], ROUTING_CODE_LEN) == 0 &&
             memcmp(inner + ROUTING_CODE_LEN, exp_inner[i], exp_len[i]) == 0;
        /* A wrong key must fail. */
        ok = ok && ecies_open(pkt, k->relay[(i + 1) % 3].sk, c.wrap_ct[i], wl) < 0;
        if (!ok)
            break;
        /* Layers 2 to 4: the destination opens its packet with its Channel Key sk. */
        l = ecies_open(pkt, k->dest[dest_of_wrap[i]].sk, inner + ROUTING_CODE_LEN, exp_len[i]);
        ok = l == (long)(exp_len[i] - ECIES_OVERHEAD);
        ok = ok && ecies_open(pkt + 0, k->dest[(dest_of_wrap[i] + 1) % 3].sk,
                              inner + ROUTING_CODE_LEN, exp_len[i]) < 0;
        /* Re-open, since the failed attempt may have written into pkt. */
        ok = ok && ecies_open(pkt, k->dest[dest_of_wrap[i]].sk, inner + ROUTING_CODE_LEN, exp_len[i]) == l;
        if (!ok)
            break;
        if (i == 0) {
            /* C reads CredP: T || key_ref || FullPacketHash || BlindShare_key. */
            const unsigned char *t = pkt;
            const unsigned char *kr = t + TOKEN_CT_LEN;
            const unsigned char *fph = kr + KEY_REF_LEN;
            const unsigned char *bsk = fph + FULLPACKETHASH_LEN;
            ok = memcmp(kr, k->key_ref, KEY_REF_LEN) == 0 &&
                 memcmp(fph, c.fullpackethash, FULLPACKETHASH_LEN) == 0 &&
                 memcmp(bsk, c.blindshare_key, BLINDSHARE_KEY_LEN) == 0;
            /* C recomputes Enc_FullPacketHash; it must match the device's bytes. */
            ok = ok && aead_seal(enc_c, enc_c + FULLPACKETHASH_LEN, bsk, ENC_FPH_NONCE, NULL, 0,
                                 fph, FULLPACKETHASH_LEN) == 0 &&
                 memcmp(enc_c, c.enc_fullpackethash, ENC_FULLPACKETHASH_LEN) == 0;
            ok = ok && aead_open(fph_back, bsk, ENC_FPH_NONCE, NULL, 0, enc_c, FULLPACKETHASH_LEN,
                                 enc_c + FULLPACKETHASH_LEN) == 0 &&
                 memcmp(fph_back, c.fullpackethash, 32) == 0;
            /* Layer 1: the validator opens T. */
            ok = ok && ecies_open(tok, k->v_token.sk, t, TOKEN_CT_LEN) == TOKEN_PT_LEN &&
                 memcmp(tok, k->cred_hw, CRED_HW_LEN) == 0 &&
                 memcmp(tok + CRED_HW_LEN, c.replay_nonce, REPLAY_NONCE_LEN) == 0 &&
                 memcmp(tok + CRED_HW_LEN + REPLAY_NONCE_LEN, k->claim, CLAIM_LEN) == 0;
            /* The validator compares binding_hash with SHA-256 of the Enc_FullPacketHash C sends. */
            ok = ok && sha256_openssl(d, enc_c, ENC_FULLPACKETHASH_LEN) == 0 &&
                 memcmp(tok + CRED_HW_LEN + REPLAY_NONCE_LEN + CLAIM_LEN, d, BINDING_HASH_LEN) == 0;
        } else {
            /* F or I reads flags || ContentHash || n || h(metadata) and recomputes FullPacketHash. */
            ok = memcmp(pkt, c.contp_pt, CONTP_PT_LEN_CAPTURE) == 0 &&
                 memcmp(pkt + FLAGS_LEN, c.content_hash, CONTENTHASH_LEN) == 0;
            memcpy(fph_check, pkt + FLAGS_LEN, CONTENTHASH_LEN + CONTENT_NONCE_LEN);
            fph_check[CONTENTHASH_LEN + CONTENT_NONCE_LEN] = pkt[0];
            memcpy(fph_check + CONTENTHASH_LEN + CONTENT_NONCE_LEN + FLAGS_LEN,
                   pkt + FLAGS_LEN + CONTENTHASH_LEN + CONTENT_NONCE_LEN, H_METADATA_LEN);
            ok = ok && sha256_openssl(d, fph_check, sizeof fph_check) == 0 &&
                 memcmp(d, c.fullpackethash, 32) == 0;
        }
    }
    /* ContentHash must be SHA-256 of the file. */
    ok = ok && sha256_libsodium(d, file, len) == 0 && memcmp(d, c.content_hash, 32) == 0;
    report_test(padded ? "seven_layer_decrypt_padded" : "seven_layer_decrypt", ok,
                padded ? "all seven layers opened, wraps padded to 460 B"
                       : "all seven layers opened with the matching secret keys; wrong keys rejected");
}

/* ------------------------------------------------------------------------ */
/* Timing.                                                                   */

static int g_cyc_fd = -1;
static int g_cyc_errno;

static void cycles_open(void)
{
    struct perf_event_attr a;

    memset(&a, 0, sizeof a);
    a.type = PERF_TYPE_HARDWARE;
    a.size = sizeof a;
    a.config = PERF_COUNT_HW_CPU_CYCLES;
    a.exclude_kernel = 1;
    a.exclude_hv = 1;
    g_cyc_fd = (int)syscall(__NR_perf_event_open, &a, 0, -1, -1, 0);
    if (g_cyc_fd < 0)
        g_cyc_errno = errno;
}

static uint64_t cycles_read(void)
{
    uint64_t v = 0;

    if (g_cyc_fd < 0 || read(g_cyc_fd, &v, sizeof v) != (ssize_t)sizeof v)
        return 0;
    return v;
}

static inline uint64_t now_ns(void)
{
    struct timespec t;

    clock_gettime(CLOCK_MONOTONIC_RAW, &t);
    return (uint64_t)t.tv_sec * 1000000000u + (uint64_t)t.tv_nsec;
}

typedef int (*op_fn)(void *ctx);

static void run_row(const char *part, const char *name, const char *desc, const char *impl,
                    size_t bytes, int warmup, int repeats, int want_cycles, op_fn fn, void *ctx)
{
    uint64_t *ns = calloc((size_t)repeats, sizeof *ns);
    uint64_t *cy = calloc((size_t)repeats, sizeof *cy);
    int i, failed = 0, use_cycles = want_cycles && g_cyc_fd >= 0;

    if (!ns || !cy) {
        printf("{\"type\":\"row\",\"part\":\"%s\",\"name\":\"%s\",\"status\":\"failed\",\"error\":\"out of memory\"}\n",
               part, name);
        free(ns); free(cy);
        return;
    }
    for (i = 0; i < warmup && !failed; i++)
        failed = fn(ctx) != 0;
    for (i = 0; i < repeats && !failed; i++) {
        uint64_t c0 = 0, c1 = 0, t0, t1;
        if (use_cycles)
            c0 = cycles_read();
        t0 = now_ns();
        failed = fn(ctx) != 0;
        t1 = now_ns();
        if (use_cycles)
            c1 = cycles_read();
        ns[i] = t1 - t0;
        cy[i] = c1 - c0;
    }
    if (failed) {
        printf("{\"type\":\"row\",\"part\":\"%s\",\"name\":\"%s\",\"status\":\"failed\",\"error\":\"operation returned an error\"}\n",
               part, name);
        free(ns); free(cy);
        return;
    }
    printf("{\"type\":\"row\",\"part\":\"%s\",\"name\":\"%s\",\"description\":\"%s\",\"impl\":\"%s\","
           "\"bytes\":%zu,\"warmup\":%d,\"repeats\":%d,\"status\":\"ok\",\"samples_ns\":[",
           part, name, desc, impl, bytes, warmup, repeats);
    for (i = 0; i < repeats; i++)
        printf(i ? ",%llu" : "%llu", (unsigned long long)ns[i]);
    printf("],\"cycles\":");
    if (use_cycles) {
        printf("[");
        for (i = 0; i < repeats; i++)
            printf(i ? ",%llu" : "%llu", (unsigned long long)cy[i]);
        printf("]");
    } else {
        printf("null");
    }
    printf("}\n");
    fflush(stdout);
    free(ns);
    free(cy);
}

static volatile unsigned char g_sink;

/* A1 */
typedef struct { const unsigned char *buf; size_t len; } hash_ctx;

static int op_sha_openssl(void *v)
{
    hash_ctx *h = v;
    unsigned char d[32];
    int rc = sha256_openssl(d, h->buf, h->len);
    g_sink ^= d[0];
    return rc;
}

static int op_sha_libsodium(void *v)
{
    hash_ctx *h = v;
    unsigned char d[32];
    int rc = sha256_libsodium(d, h->buf, h->len);
    g_sink ^= d[0];
    return rc;
}

/* A2 */
typedef struct { unsigned char scalar[32]; unsigned char gp[32]; } mul_ctx;

static int op_x25519_variable(void *v)
{
    mul_ctx *m = v;
    unsigned char q[32];
    int rc = crypto_scalarmult(q, m->scalar, m->gp);
    g_sink ^= q[0];
    return rc;
}

static int op_x25519_fixed(void *v)
{
    mul_ctx *m = v;
    unsigned char q[32];
    int rc = crypto_scalarmult_base(q, m->scalar);
    g_sink ^= q[0];
    return rc;
}

static int op_x25519_capture_mix(void *v)
{
    mul_ctx *m = v;
    unsigned char q[32];
    int i, rc = 0;

    for (i = 0; i < 10; i++)
        rc |= crypto_scalarmult(q, m->scalar, m->gp);
    for (i = 0; i < 4; i++)
        rc |= crypto_scalarmult_base(q, m->scalar);
    g_sink ^= q[0];
    return rc;
}

/* A3 */
typedef struct {
    const unsigned char *gp; /* NULL for the standard base point */
    const unsigned char *pk;
    unsigned char pt[MAX_PT_LEN];
    size_t len;
    unsigned char out[MAX_PT_LEN + ECIES_OVERHEAD];
} ecies_ctx;

static int op_ecies(void *v)
{
    ecies_ctx *e = v;
    int rc = ecies_seal(e->out, e->gp, e->pk, e->pt, e->len);
    g_sink ^= e->out[40];
    return rc;
}

typedef struct { capture *c; const setup_keys *k; int padded; } layers_ctx;

static int op_seven_layers(void *v)
{
    layers_ctx *l = v;
    return step_layers(l->c, l->k, l->padded);
}

typedef struct { unsigned char ikm[32]; unsigned char salt[32]; unsigned char okm[44]; } hkdf_ctx;

static int op_hkdf(void *v)
{
    hkdf_ctx *h = v;
    int rc = hkdf_sha256(h->okm, sizeof h->okm, h->ikm, sizeof h->ikm, h->salt, sizeof h->salt,
                         (const unsigned char *)HKDF_INFO, sizeof HKDF_INFO - 1);
    g_sink ^= h->okm[0];
    return rc;
}

typedef struct {
    unsigned char key[32], nonce[12], aad[33], pt[MAX_PT_LEN], ct[MAX_PT_LEN], tag[16];
    size_t len;
} gcm_ctx;

static int op_gcm(void *v)
{
    gcm_ctx *g = v;
    int rc = aead_seal(g->ct, g->tag, g->key, g->nonce, g->aad, sizeof g->aad, g->pt, g->len);
    g_sink ^= g->tag[0];
    return rc;
}

/* A4 */
static int op_h_metadata(void *v)
{
    capture *c = v;
    return sha256_openssl(c->h_metadata, c->metadata_commitments, sizeof c->metadata_commitments);
}

static int op_fullpackethash(void *v)
{
    capture *c = v;
    return sha256_openssl(c->fullpackethash, c->fph_input, sizeof c->fph_input);
}

static int op_enc_fullpackethash(void *v)
{
    capture *c = v;
    return aead_seal(c->enc_fullpackethash, c->enc_fullpackethash + FULLPACKETHASH_LEN,
                     c->blindshare_key, ENC_FPH_NONCE, NULL, 0, c->fullpackethash, FULLPACKETHASH_LEN);
}

static int op_binding_hash(void *v)
{
    capture *c = v;
    return sha256_openssl(c->binding_hash, c->enc_fullpackethash, ENC_FULLPACKETHASH_LEN);
}

/* A5 */
typedef struct {
    capture *c;
    const setup_keys *k;
    const unsigned char *buf;
    size_t len;
    hash_fn h;
    int padded;
} whole_ctx;

static int op_whole_capture(void *v)
{
    whole_ctx *w = v;
    return whole_capture(w->c, w->k, w->buf, w->len, w->h, w->padded);
}

/* ------------------------------------------------------------------------ */

static int group_on(const char *groups, const char *g)
{
    const char *p = groups;
    size_t n = strlen(g);

    if (strcmp(groups, "all") == 0)
        return 1;
    while ((p = strstr(p, g)) != NULL) {
        if ((p == groups || p[-1] == ',') && (p[n] == ',' || p[n] == '\0'))
            return 1;
        p += n;
    }
    return 0;
}

static void usage(const char *argv0)
{
    fprintf(stderr,
            "usage: %s [--groups LIST] [--hash-repeats N] [--hash-warmup N]\n"
            "          [--small-repeats N] [--small-warmup N] [--capture-repeats N]\n"
            "          [--hash-bytes N[,N...]]\n"
            "groups: all, or a comma list of a1_openssl,a1_libsodium,a2,a3,a4,a5,\n"
            "        hash_openssl,hash_libsodium (SHA-256 at the --hash-bytes sizes)\n",
            argv0);
}

int main(int argc, char **argv)
{
    const char *groups = "all";
    int hash_repeats = 20, hash_warmup = 2, small_repeats = 2000, small_warmup = 200, capture_repeats = 20;
    size_t hash_bytes[64];
    size_t n_hash_bytes = 0;
    static const size_t file_sizes[3] = {FILE_SIZE_LOW, FILE_SIZE_CENTRAL, FILE_SIZE_HIGH};
    static setup_keys keys;
    static capture cap;
    unsigned char *buf;
    size_t i;
    const char *armcap = getenv("OPENSSL_armcap");
    const char *ia32cap = getenv("OPENSSL_ia32cap");

    for (i = 1; i < (size_t)argc; i++) {
        if (strcmp(argv[i], "--groups") == 0 && i + 1 < (size_t)argc)
            groups = argv[++i];
        else if (strcmp(argv[i], "--hash-repeats") == 0 && i + 1 < (size_t)argc)
            hash_repeats = atoi(argv[++i]);
        else if (strcmp(argv[i], "--hash-warmup") == 0 && i + 1 < (size_t)argc)
            hash_warmup = atoi(argv[++i]);
        else if (strcmp(argv[i], "--small-repeats") == 0 && i + 1 < (size_t)argc)
            small_repeats = atoi(argv[++i]);
        else if (strcmp(argv[i], "--small-warmup") == 0 && i + 1 < (size_t)argc)
            small_warmup = atoi(argv[++i]);
        else if (strcmp(argv[i], "--capture-repeats") == 0 && i + 1 < (size_t)argc)
            capture_repeats = atoi(argv[++i]);
        else if (strcmp(argv[i], "--hash-bytes") == 0 && i + 1 < (size_t)argc) {
            /* Comma list of sizes, each at most FILE_SIZE_HIGH. */
            char *p = argv[++i], *end;
            while (*p) {
                unsigned long long v = strtoull(p, &end, 10);
                if (end == p || v > FILE_SIZE_HIGH || n_hash_bytes == sizeof hash_bytes / sizeof hash_bytes[0]) {
                    usage(argv[0]);
                    return 1;
                }
                hash_bytes[n_hash_bytes++] = (size_t)v;
                p = *end == ',' ? end + 1 : end;
                if (*end && *end != ',') {
                    usage(argv[0]);
                    return 1;
                }
            }
        }
        else {
            usage(argv[0]);
            return 1;
        }
    }
    if (hash_repeats < 1 || small_repeats < 1 || capture_repeats < 1 || hash_warmup < 0 || small_warmup < 0) {
        usage(argv[0]);
        return 1;
    }

    if (crypto_init() != 0) {
        printf("{\"type\":\"fatal\",\"error\":\"library initialisation failed\"}\n");
        return 2;
    }
    cycles_open();

    printf("{\"type\":\"meta\",\"compiler\":\"%s\",\"cflags\":\"%s\",\"openssl_runtime\":\"%s\","
           "\"openssl_headers\":\"%s\",\"libsodium\":\"%s\",\"OPENSSL_armcap\":%s%s%s,\"OPENSSL_ia32cap\":%s%s%s,"
           "\"clock\":\"CLOCK_MONOTONIC_RAW\",\"cycle_counter\":\"%s\",\"cycle_counter_errno\":%d,"
           "\"kdf\":\"HKDF-SHA256 (placeholder)\",\"aead\":\"AES-256-GCM, 12 B nonce from HKDF, 16 B tag\","
           "\"ecies_layout\":\"version 1 B || EPK 32 B || ciphertext || tag 16 B\",\"ecies_overhead\":%d,"
           "\"sizes\":{\"token_pt\":%d,\"credp_pt\":%d,\"contp_pt_capture\":%d,\"wrap_credp_pt\":%d,"
           "\"wrap_contp_pt\":%d,\"wrap_padded_pt\":%d,\"fullpackethash_input\":%d}}\n",
           __VERSION__, BUILD_CFLAGS, OpenSSL_version(OPENSSL_VERSION), OPENSSL_VERSION_TEXT,
           sodium_version_string(),
           armcap ? "\"" : "", armcap ? armcap : "null", armcap ? "\"" : "",
           ia32cap ? "\"" : "", ia32cap ? ia32cap : "null", ia32cap ? "\"" : "",
           g_cyc_fd >= 0 ? "perf_event_open PERF_COUNT_HW_CPU_CYCLES, user space only" : "unavailable",
           g_cyc_fd >= 0 ? 0 : g_cyc_errno, ECIES_OVERHEAD,
           TOKEN_PT_LEN, CREDP_PT_LEN, CONTP_PT_LEN_CAPTURE, WRAP_CREDP_PT_LEN, WRAP_CONTP_PT_LEN,
           WRAP_PADDED_PT_LEN, FULLPACKETHASH_INPUT_LEN);
    fflush(stdout);

    /* Random file buffer, held in RAM. Every page is written before timing. */
    buf = malloc(FILE_SIZE_HIGH);
    if (!buf) {
        printf("{\"type\":\"fatal\",\"error\":\"cannot allocate file buffer\"}\n");
        return 2;
    }
    randombytes_buf(buf, FILE_SIZE_HIGH);

    if (make_setup_keys(&keys) != 0) {
        printf("{\"type\":\"fatal\",\"error\":\"key setup failed\"}\n");
        return 2;
    }

    /* Correctness tests. No timing if any fails. */
    test_sha256(buf, FILE_SIZE_HIGH);
    test_hkdf();
    test_x25519();
    test_aes_gcm();
    test_subgroup_check(&keys);
    test_ecies_overhead(&keys);
    test_full_decrypt(&keys, buf, FILE_SIZE_CENTRAL, 0);
    test_full_decrypt(&keys, buf, FILE_SIZE_CENTRAL, 1);
    printf("{\"type\":\"selftest_summary\",\"pass\":%s,\"failures\":%d}\n",
           g_selftest_failures ? "false" : "true", g_selftest_failures);
    fflush(stdout);
    if (g_selftest_failures) {
        free(buf);
        return 2;
    }

    /* A1: ContentHash = SHA-256(file). */
    for (i = 0; i < 3; i++) {
        hash_ctx h = {buf, file_sizes[i]};
        if (group_on(groups, "a1_openssl"))
            run_row("A1", "sha256_file_openssl", "ContentHash = SHA-256(file), buffer in RAM",
                    "OpenSSL EVP SHA256", file_sizes[i], hash_warmup, hash_repeats, 1, op_sha_openssl, &h);
        if (group_on(groups, "a1_libsodium"))
            run_row("A1", "sha256_file_libsodium", "ContentHash = SHA-256(file), buffer in RAM",
                    "libsodium crypto_hash_sha256 (portable C)", file_sizes[i], hash_warmup, hash_repeats, 1,
                    op_sha_libsodium, &h);
    }

    /* Part B: SHA-256 of M at each --hash-bytes size, same code as A1. */
    for (i = 0; i < n_hash_bytes; i++) {
        hash_ctx h = {buf, hash_bytes[i]};
        if (group_on(groups, "hash_openssl"))
            run_row("B", "sha256_bytes_openssl", "SHA-256(M), M in RAM", "OpenSSL EVP SHA256",
                    hash_bytes[i], hash_warmup, hash_repeats, 1, op_sha_openssl, &h);
        if (group_on(groups, "hash_libsodium"))
            run_row("B", "sha256_bytes_libsodium", "SHA-256(M), M in RAM",
                    "libsodium crypto_hash_sha256 (portable C)", hash_bytes[i], hash_warmup, hash_repeats, 1,
                    op_sha_libsodium, &h);
    }

    /* A2: scalar multiplications. */
    if (group_on(groups, "a2")) {
        mul_ctx m;
        randombytes_buf(m.scalar, sizeof m.scalar);
        memcpy(m.gp, keys.dest[0].gp, 32);
        run_row("A2", "x25519_variable_base", "crypto_scalarmult with GP = r*B as base", "libsodium",
                0, small_warmup, small_repeats, 0, op_x25519_variable, &m);
        run_row("A2", "x25519_fixed_base", "crypto_scalarmult_base", "libsodium",
                0, small_warmup, small_repeats, 0, op_x25519_fixed, &m);
        run_row("A2", "x25519_capture_mix", "10 variable-base + 4 fixed-base, one capture", "libsodium",
                0, small_warmup, small_repeats, 0, op_x25519_capture_mix, &m);
    }

    /* A3: ECIES encryptions. */
    if (group_on(groups, "a3")) {
        static ecies_ctx e;
        static gcm_ctx g;
        static hkdf_ctx hk;
        static const struct { const char *name; const char *desc; int blinded; size_t len; } rows[] = {
            {"ecies_layer1_token", "Layer 1, token T, ECIES to V-token_pk", 0, TOKEN_PT_LEN},
            {"eciesb_layer2_credp", "Layer 2, CredP, ECIESb to Channel Key of C", 1, CREDP_PT_LEN},
            {"eciesb_layer3_4_contp_49B", "Layers 3 and 4, ContP without optional fields", 1, CONTP_PT_LEN_MIN},
            {"eciesb_layer3_4_contp_81B", "Layers 3 and 4, ContP with h(metadata)", 1, CONTP_PT_LEN_META},
            {"eciesb_layer3_4_contp_113B", "Layers 3 and 4, ContP with h(metadata) and parent ContentHash", 1,
             CONTP_PT_LEN_META_PARENT},
            {"eciesb_layer3_4_contp_300B_stress", "Layers 3 and 4, 300 B stress case outside the spec", 1,
             CONTP_PT_LEN_STRESS},
            {"ecies_layer5_wrap_credp", "Layer 5, first-relay wrap of CredP, unpadded", 0, WRAP_CREDP_PT_LEN},
            {"ecies_layer6_7_wrap_contp", "Layers 6 and 7, first-relay wrap of ContP (81 B), unpadded", 0,
             WRAP_CONTP_PT_LEN},
            {"ecies_layer5_7_wrap_padded_460B", "Layers 5 to 7, first-relay wrap padded to 460 B", 0,
             WRAP_PADDED_PT_LEN},
        };
        layers_ctx lc = {&cap, &keys, 0};
        size_t r;

        for (r = 0; r < sizeof rows / sizeof rows[0]; r++) {
            e.gp = rows[r].blinded ? keys.dest[0].gp : NULL;
            e.pk = rows[r].blinded ? keys.dest[0].pk : keys.relay[0].pk;
            e.len = rows[r].len;
            randombytes_buf(e.pt, e.len);
            run_row("A3", rows[r].name, rows[r].desc,
                    rows[r].blinded ? "ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM"
                                    : "ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM",
                    e.len, small_warmup, small_repeats, 0, op_ecies, &e);
        }

        randombytes_buf(hk.ikm, sizeof hk.ikm);
        randombytes_buf(hk.salt, sizeof hk.salt);
        run_row("A3", "hkdf_sha256_44B", "Key derivation inside one ECIES call (component)", "OpenSSL EVP_KDF HKDF",
                44, small_warmup, small_repeats, 0, op_hkdf, &hk);
        randombytes_buf(&g, sizeof g);
        g.len = CREDP_PT_LEN;
        run_row("A3", "aes256gcm_seal_203B", "AEAD inside the CredP ECIES call (component)", "OpenSSL EVP AES-256-GCM",
                g.len, small_warmup, small_repeats, 0, op_gcm, &g);

        /* The seven layers, from prepared inputs. Hashing excluded. */
        if (whole_capture(&cap, &keys, buf, FILE_SIZE_CENTRAL, sha256_openssl, 0) != 0) {
            printf("{\"type\":\"row\",\"part\":\"A3\",\"name\":\"ecies_seven_layers\",\"status\":\"failed\","
                   "\"error\":\"capture setup failed\"}\n");
        } else {
            run_row("A3", "ecies_seven_layers", "All seven ECIES layers in spec order, unpadded wraps",
                    "3 ECIESb + 4 ECIES", 0, small_warmup, small_repeats, 0, op_seven_layers, &lc);
            lc.padded = 1;
            run_row("A3", "ecies_seven_layers_padded", "All seven ECIES layers, wraps padded to 460 B",
                    "3 ECIESb + 4 ECIES", 0, small_warmup, small_repeats, 0, op_seven_layers, &lc);
        }
    }

    /* A4: small operations around ECIES. */
    if (group_on(groups, "a4")) {
        if (whole_capture(&cap, &keys, buf, FILE_SIZE_CENTRAL, sha256_openssl, 0) != 0) {
            printf("{\"type\":\"row\",\"part\":\"A4\",\"name\":\"setup\",\"status\":\"failed\","
                   "\"error\":\"capture setup failed\"}\n");
        } else {
            run_row("A4", "h_metadata", "h(metadata) = SHA-256 over three 32 B commitments", "OpenSSL EVP SHA256",
                    METADATA_COMMITMENTS_LEN, small_warmup, small_repeats, 0, op_h_metadata, &cap);
            run_row("A4", "fullpackethash", "FullPacketHash = SHA-256(ContentHash || n || flags || h(metadata))",
                    "OpenSSL EVP SHA256", FULLPACKETHASH_INPUT_LEN, small_warmup, small_repeats, 0,
                    op_fullpackethash, &cap);
            run_row("A4", "enc_fullpackethash", "Enc_FullPacketHash = AES-256-GCM(BlindShare_key; FullPacketHash), fixed nonce",
                    "OpenSSL EVP AES-256-GCM", FULLPACKETHASH_LEN, small_warmup, small_repeats, 0,
                    op_enc_fullpackethash, &cap);
            run_row("A4", "binding_hash", "binding_hash = SHA-256(Enc_FullPacketHash)", "OpenSSL EVP SHA256",
                    ENC_FULLPACKETHASH_LEN, small_warmup, small_repeats, 0, op_binding_hash, &cap);
        }
    }

    /* A5: whole capture from a 30,000,000 B buffer. */
    if (group_on(groups, "a5")) {
        whole_ctx w = {&cap, &keys, buf, FILE_SIZE_CENTRAL, sha256_openssl, 0};
        run_row("A5", "whole_capture_openssl", "ContentHash + FullPacketHash + binding + seven ECIES layers, unpadded wraps",
                "ContentHash by OpenSSL EVP SHA256", FILE_SIZE_CENTRAL, hash_warmup, capture_repeats, 1,
                op_whole_capture, &w);
        w.padded = 1;
        run_row("A5", "whole_capture_openssl_padded", "Same, wraps padded to 460 B",
                "ContentHash by OpenSSL EVP SHA256", FILE_SIZE_CENTRAL, hash_warmup, capture_repeats, 1,
                op_whole_capture, &w);
        if (group_on(groups, "a1_libsodium")) {
            w.padded = 0;
            w.h = sha256_libsodium;
            run_row("A5", "whole_capture_libsodium", "Same as whole_capture_openssl, ContentHash by portable C",
                    "ContentHash by libsodium crypto_hash_sha256", FILE_SIZE_CENTRAL, hash_warmup, capture_repeats, 1,
                    op_whole_capture, &w);
        }
    }

    printf("{\"type\":\"done\"}\n");
    free(buf);
    return 0;
}

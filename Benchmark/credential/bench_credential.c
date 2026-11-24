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
 * Part C: device-side primitives of the two designs in Protocol paper
 * Table 5 that need no online validator.
 *
 *   Blind-signed tokens       RSA blind signatures, RFC 9474, client side.
 *   DAA or EPID signature     One anonymous-mode signature over ContentHash.
 *   One relay wrap            One ECIES wrap to the first relay, by Part A's code.
 *
 * Part A's code is included, not modified: the ECIES wrap, the OpenSSL and
 * libsodium setup, and Part A's HKDF, X25519 and AES-256-GCM known-answer
 * tests come from ../device/bench_capture.c.
 *
 * The program runs its correctness tests first. If any test fails it prints
 * the failure and exits with status 2 before timing anything.
 *
 * Each row's repeat count follows from its own speed. Three calibration runs
 * give a median. Under 5 ms the row gets --repeats-fast samples, from 5 to
 * 100 ms --repeats-mid, above 100 ms --repeats-slow. If the median of the
 * samples falls in a faster class than the calibration, sampling continues
 * up to that class's count.
 */

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-function"
#define main bench_capture_main
#include "../device/bench_capture.c"
#undef main
#pragma GCC diagnostic pop

#include <openssl/core_names.h>
#include <openssl/param_build.h>
#include <openssl/rand.h>
#include <openssl/rsa.h>

#include "daa.h"
#include "rfc9474_vectors.h"
#include "rsabssa.h"

#define TOKEN_INPUT_LEN 98          /* RFC 9578 token input: 2 + 32 + 32 + 32 */
#define TOKEN_AUTHENTICATOR_LEN 256 /* RSA-2048 signature, as RFC 9578 specifies */
#define TOKEN_LEN (TOKEN_INPUT_LEN + TOKEN_AUTHENTICATOR_LEN) /* 354 */
#define BATCH 20                    /* token refill size of SNAExperiment C6 */
#define WRAP_MAX_PT (ROUTING_CODE_LEN + CONTENTHASH_LEN + DAA_MAX_SIG)

#define DESIGN_TOKENS "blind-signed tokens"
#define DESIGN_DAA "DAA or EPID signature"

uint64_t partc_now_ns(void)
{
    return now_ns();
}

void partc_random(void *buf, size_t len)
{
    randombytes_buf(buf, len);
}

/* ------------------------------------------------------------------------ */
/* Helpers.                                                                  */

static int hexdec(unsigned char **out, size_t *outlen, const char *hex)
{
    size_t n = strlen(hex) / 2, wl = 0;

    *out = malloc(n ? n : 1);
    if (!*out || sodium_hex2bin(*out, n, hex, strlen(hex), NULL, &wl, NULL) != 0 || wl != n)
        return -1;
    *outlen = n;
    return 0;
}

static BIGNUM *hex_bn(const char *hex)
{
    BIGNUM *b = NULL;
    return BN_hex2bn(&b, hex) ? b : NULL;
}

/* A public-only RSA key from n and e, as a client holds it. */
static EVP_PKEY *rsa_public_key(const BIGNUM *n, const BIGNUM *e)
{
    OSSL_PARAM_BLD *b = OSSL_PARAM_BLD_new();
    OSSL_PARAM *p = NULL;
    EVP_PKEY_CTX *ctx = EVP_PKEY_CTX_new_from_name(NULL, "RSA", NULL);
    EVP_PKEY *pkey = NULL;

    if (b && ctx && OSSL_PARAM_BLD_push_BN(b, OSSL_PKEY_PARAM_RSA_N, n) &&
        OSSL_PARAM_BLD_push_BN(b, OSSL_PKEY_PARAM_RSA_E, e) && (p = OSSL_PARAM_BLD_to_param(b)) &&
        EVP_PKEY_fromdata_init(ctx) == 1)
        EVP_PKEY_fromdata(ctx, &pkey, EVP_PKEY_PUBLIC_KEY, p);
    OSSL_PARAM_free(p);
    OSSL_PARAM_BLD_free(b);
    EVP_PKEY_CTX_free(ctx);
    return pkey;
}

/* The issuer's blind signing, RSASP1: s = m^d mod n. Not a device cost; never timed. */
typedef struct {
    EVP_PKEY *priv;
    EVP_PKEY_CTX *ctx;
} rsa_issuer;

static int issuer_init(rsa_issuer *is, int bits)
{
    is->priv = EVP_RSA_gen((unsigned)bits);
    is->ctx = is->priv ? EVP_PKEY_CTX_new(is->priv, NULL) : NULL;
    return is->ctx && EVP_PKEY_decrypt_init(is->ctx) == 1 &&
                   EVP_PKEY_CTX_set_rsa_padding(is->ctx, RSA_NO_PADDING) == 1 ? 0 : -1;
}

static int issuer_blind_sign(rsa_issuer *is, unsigned char *blind_sig, const unsigned char *blinded, size_t len)
{
    size_t outl = len;
    return EVP_PKEY_decrypt(is->ctx, blind_sig, &outl, blinded, len) == 1 && outl == len ? 0 : -1;
}

/* ------------------------------------------------------------------------ */
/* Row runner.                                                               */

static int g_repeats[3] = {2000, 200, 50};   /* fast, mid, slow */
static const int g_warmup[3] = {200, 20, 2};
static const char *const g_class_name[3] = {"under 5 ms", "5 to 100 ms", "over 100 ms"};

typedef int64_t (*timed_fn)(void *ctx); /* elapsed ns of one operation, or -1 */

typedef struct {
    const char *design;
    const char *scheme;
    const char *name;
    const char *variant;
    const char *params;
    const char *security;
    const char *description;
    const char *impl;
    size_t bytes;
} row_info;

static int cmp_i64(const void *a, const void *b)
{
    int64_t x = *(const int64_t *)a, y = *(const int64_t *)b;
    return (x > y) - (x < y);
}

static double median_ms(const int64_t *s, size_t n)
{
    int64_t *c = malloc(n * sizeof *c);
    double m;

    if (!c)
        return 0;
    memcpy(c, s, n * sizeof *c);
    qsort(c, n, sizeof *c, cmp_i64);
    m = (n % 2) ? (double)c[n / 2] : ((double)c[n / 2 - 1] + (double)c[n / 2]) / 2.0;
    free(c);
    return m / 1e6;
}

static int class_of(double ms)
{
    return ms < 5.0 ? 0 : (ms < 100.0 ? 1 : 2);
}

static void print_row_head(const row_info *r)
{
    printf("{\"type\":\"row\",\"part\":\"C\",\"design\":\"%s\",\"scheme\":\"%s\",\"name\":\"%s\","
           "\"variant\":\"%s\",\"params\":\"%s\",\"security\":\"%s\",\"description\":\"%s\",\"impl\":\"%s\","
           "\"bytes\":%zu,",
           r->design, r->scheme ? r->scheme : "", r->name, r->variant ? r->variant : "default",
           r->params, r->security, r->description, r->impl, r->bytes);
}

static void run_row_c(const row_info *r, timed_fn fn, void *ctx)
{
    int64_t cal[3], v;
    int64_t *s = NULL;
    size_t n = 0, cap = 0, need;
    int i, cls, cls_cal, failed = 0;

    for (i = 0; i < 3 && !failed; i++)
        failed = (cal[i] = fn(ctx)) < 0;
    if (!failed) {
        cls_cal = class_of(median_ms(cal, 3));
        for (i = 0; i < g_warmup[cls_cal] && !failed; i++)
            failed = fn(ctx) < 0;
        need = (size_t)g_repeats[cls_cal];
        cls = cls_cal;
        while (!failed && n < need) {
            if (n == cap) {
                int64_t *t = realloc(s, (cap = cap ? 2 * cap : need) * sizeof *s);
                if (!t) {
                    failed = 1;
                    break;
                }
                s = t;
            }
            failed = (v = fn(ctx)) < 0;
            s[n++] = v;
            if (!failed && n == need) {
                /* The class follows the measured median; a faster class needs more samples. */
                cls = class_of(median_ms(s, n));
                if ((size_t)g_repeats[cls] > need)
                    need = (size_t)g_repeats[cls];
            }
        }
    }
    print_row_head(r);
    if (failed) {
        printf("\"status\":\"failed\",\"error\":\"operation returned an error\"}\n");
        free(s);
        fflush(stdout);
        return;
    }
    printf("\"warmup\":%d,\"repeats\":%zu,\"repeat_class\":\"%s\",\"calibration_class\":\"%s\","
           "\"status\":\"ok\",\"samples_ns\":[",
           3 + g_warmup[cls_cal], n, g_class_name[cls], g_class_name[cls_cal]);
    for (need = 0; need < n; need++)
        printf(need ? ",%lld" : "%lld", (long long)s[need]);
    printf("],\"cycles\":null}\n");
    fflush(stdout);
    free(s);
}

/* ------------------------------------------------------------------------ */
/* Blind-signed tokens.                                                      */

typedef struct {
    const char *variant;
    size_t salt_len;
} bssa_variant;

static const bssa_variant VARIANTS[2] = {
    {"RSABSSA-SHA384-PSS-Deterministic", 48},
    {"RSABSSA-SHA384-PSSZERO-Deterministic", 0},
};

typedef struct {
    rsabssa_pk pk;
    rsa_issuer *issuer;
    unsigned char msg[BATCH][TOKEN_INPUT_LEN];
    unsigned char blinded[BATCH][RSABSSA_MAX_MODULUS_BYTES];
    unsigned char inv[BATCH][RSABSSA_MAX_MODULUS_BYTES];
    unsigned char blind_sig[BATCH][RSABSSA_MAX_MODULUS_BYTES];
    unsigned char sig[BATCH][RSABSSA_MAX_MODULUS_BYTES];
} bssa_ctx;

static int64_t op_blind(void *v)
{
    bssa_ctx *c = v;
    uint64_t t0, t1;
    int rc;

    t0 = now_ns();
    rc = rsabssa_blind(&c->pk, c->blinded[0], c->inv[0], c->msg[0], TOKEN_INPUT_LEN);
    t1 = now_ns();
    return rc == 0 ? (int64_t)(t1 - t0) : -1;
}

static int64_t op_finalize(void *v)
{
    bssa_ctx *c = v;
    uint64_t t0, t1;
    int rc;

    t0 = now_ns();
    rc = rsabssa_finalize(&c->pk, c->sig[0], c->blind_sig[0], c->inv[0], c->msg[0], TOKEN_INPUT_LEN);
    t1 = now_ns();
    return rc == 0 ? (int64_t)(t1 - t0) : -1;
}

/* Blind 20 (timed), the issuer signs 20 (not timed), finalize 20 (timed). */
static int64_t op_batch(void *v)
{
    bssa_ctx *c = v;
    uint64_t t0, t1, t2, t3;
    int i, rc = 0;
    size_t len = c->pk.modulus_len;

    randombytes_buf(c->msg, sizeof c->msg);
    t0 = now_ns();
    for (i = 0; i < BATCH; i++)
        rc |= rsabssa_blind(&c->pk, c->blinded[i], c->inv[i], c->msg[i], TOKEN_INPUT_LEN);
    t1 = now_ns();
    for (i = 0; i < BATCH; i++)
        rc |= issuer_blind_sign(c->issuer, c->blind_sig[i], c->blinded[i], len);
    t2 = now_ns();
    for (i = 0; i < BATCH; i++)
        rc |= rsabssa_finalize(&c->pk, c->sig[i], c->blind_sig[i], c->inv[i], c->msg[i], TOKEN_INPUT_LEN);
    t3 = now_ns();
    return rc == 0 ? (int64_t)((t1 - t0) + (t3 - t2)) : -1;
}

static void test_rfc9474_vectors(void)
{
    size_t i;

    for (i = 0; i < sizeof RFC9474_VECTORS / sizeof RFC9474_VECTORS[0]; i++) {
        const rfc9474_vector *v = &RFC9474_VECTORS[i];
        unsigned char *msg = NULL, *salt = NULL, *em = NULL, *inv = NULL, *bm = NULL, *bs = NULL, *sig = NULL;
        size_t msg_len = 0, salt_len = 0, em_len = 0, inv_len = 0, bm_len = 0, bs_len = 0, sig_len = 0;
        unsigned char out_em[RSABSSA_MAX_MODULUS_BYTES], out_bm[RSABSSA_MAX_MODULUS_BYTES];
        unsigned char out_inv[RSABSSA_MAX_MODULUS_BYTES], out_sig[RSABSSA_MAX_MODULUS_BYTES];
        BIGNUM *n = hex_bn(v->n), *e = hex_bn(v->e), *d = hex_bn(v->d), *iv = NULL, *r = NULL, *z = NULL, *chk = NULL;
        BN_CTX *bc = BN_CTX_new();
        EVP_PKEY *pub = NULL;
        rsabssa_pk pk;
        char name[96];
        int ok = 0, pk_ok = 0;

        if (!n || !e || !d || !bc || hexdec(&msg, &msg_len, v->msg) || hexdec(&salt, &salt_len, v->salt) ||
            hexdec(&em, &em_len, v->encoded_msg) || hexdec(&inv, &inv_len, v->inv) ||
            hexdec(&bm, &bm_len, v->blinded_msg) || hexdec(&bs, &bs_len, v->blind_sig) ||
            hexdec(&sig, &sig_len, v->sig))
            goto report;
        pub = rsa_public_key(n, e);
        if (!pub || salt_len != v->salt_len || rsabssa_pk_init(&pk, pub, v->salt_len) != 0)
            goto report;
        pk_ok = 1;
        /* r is the inverse of the vector's inv. */
        iv = BN_bin2bn(inv, (int)inv_len, NULL);
        r = BN_new();
        z = BN_new();
        chk = BN_new();
        if (!iv || !r || !z || !chk || !BN_mod_inverse(r, iv, n, bc))
            goto report;
        ok = em_len == pk.modulus_len &&
             rsabssa_emsa_pss_encode(&pk, out_em, msg, msg_len, salt) == 0 &&
             memcmp(out_em, em, em_len) == 0;
        ok = ok && rsabssa_blind_with(&pk, out_bm, out_inv, msg, msg_len, salt, r) == 0 &&
             bm_len == pk.modulus_len && memcmp(out_bm, bm, bm_len) == 0 &&
             memcmp(out_inv, inv, inv_len) == 0;
        /* The vector's blind_sig is blinded_msg^d mod n. */
        ok = ok && BN_bin2bn(bm, (int)bm_len, z) && BN_mod_exp(chk, z, d, n, bc) &&
             BN_bin2bn(bs, (int)bs_len, z) && BN_cmp(chk, z) == 0;
        ok = ok && rsabssa_finalize(&pk, out_sig, bs, inv, msg, msg_len) == 0 &&
             sig_len == pk.modulus_len && memcmp(out_sig, sig, sig_len) == 0;
report:
        snprintf(name, sizeof name, "rfc9474_known_answer_%s", v->name);
        report_test(name, ok, "RFC 9474 Appendix A (RSA-4096): encoded_msg, blinded_msg, inv, blind_sig, sig");
        if (pk_ok)
            rsabssa_pk_free(&pk);
        EVP_PKEY_free(pub);
        BN_free(n); BN_free(e); BN_free(d); BN_free(iv); BN_free(r); BN_free(z); BN_free(chk);
        BN_CTX_free(bc);
        free(msg); free(salt); free(em); free(inv); free(bm); free(bs); free(sig);
    }
}

static void test_bssa_key(bssa_ctx *c, const char *variant, int bits)
{
    char name[128];
    int ok;
    size_t len = c->pk.modulus_len;

    randombytes_buf(c->msg[0], TOKEN_INPUT_LEN);
    ok = rsabssa_blind(&c->pk, c->blinded[0], c->inv[0], c->msg[0], TOKEN_INPUT_LEN) == 0 &&
         issuer_blind_sign(c->issuer, c->blind_sig[0], c->blinded[0], len) == 0 &&
         rsabssa_finalize(&c->pk, c->sig[0], c->blind_sig[0], c->inv[0], c->msg[0], TOKEN_INPUT_LEN) == 0 &&
         rsabssa_verify(&c->pk, c->sig[0], c->msg[0], TOKEN_INPUT_LEN) == 0;
    c->sig[0][len / 2] ^= 1;
    ok = ok && rsabssa_verify(&c->pk, c->sig[0], c->msg[0], TOKEN_INPUT_LEN) != 0;
    c->sig[0][len / 2] ^= 1;
    c->msg[0][5] ^= 1;
    ok = ok && rsabssa_verify(&c->pk, c->sig[0], c->msg[0], TOKEN_INPUT_LEN) != 0;
    c->msg[0][5] ^= 1;
    snprintf(name, sizeof name, "blind_signed_token_%s_RSA-%d", variant, bits);
    report_test(name, ok, "blind, issuer signs, finalize; the signature verifies; "
                          "a modified signature and a modified message are rejected");
}

/* ------------------------------------------------------------------------ */
/* DAA or EPID signature.                                                    */

typedef struct {
    const daa_scheme *s;
    uint8_t msg[DAA_MSG_LEN];
    uint8_t sig[DAA_MAX_SIG];
    size_t sig_len;
} daa_ctx;

static int64_t op_daa_sign(void *v)
{
    daa_ctx *c = v;
    uint64_t t0, t1;
    int rc;

    t0 = now_ns();
    rc = c->s->sign(c->msg, sizeof c->msg, c->sig, &c->sig_len);
    t1 = now_ns();
    return rc == 0 ? (int64_t)(t1 - t0) : -1;
}

static int64_t op_daa_keygen(void *v)
{
    daa_ctx *c = v;
    return c->s->keygen();
}

static void report_cb(const char *name, int pass, const char *detail)
{
    report_test(name, pass, detail);
}

/* Returns the signature size, or 0 on failure. */
static size_t test_daa(const daa_scheme *s, int setup_ok)
{
    static uint8_t sig1[DAA_MAX_SIG], sig2[DAA_MAX_SIG];
    uint8_t msg[DAA_MSG_LEN];
    size_t l1 = 0, l2 = 0;
    char name[96];
    int ok;

    snprintf(name, sizeof name, "%s_setup", s->key);
    report_test(name, setup_ok, s->scheme);
    if (!setup_ok)
        return 0;
    s->library_tests(report_cb);
    randombytes_buf(msg, sizeof msg);
    ok = s->sign(msg, sizeof msg, sig1, &l1) == 0 && s->verify(msg, sizeof msg, sig1, l1) == 0;
    msg[0] ^= 1;
    ok = ok && s->verify(msg, sizeof msg, sig1, l1) != 0;
    msg[0] ^= 1;
    sig1[l1 / 2] ^= 1;
    ok = ok && s->verify(msg, sizeof msg, sig1, l1) != 0;
    sig1[l1 / 2] ^= 1;
    ok = ok && s->sign(msg, sizeof msg, sig2, &l2) == 0 && s->verify(msg, sizeof msg, sig2, l2) == 0 &&
         l1 == l2 && memcmp(sig1, sig2, l1) != 0;
    snprintf(name, sizeof name, "%s_sign_verify", s->key);
    report_test(name, ok, "anonymous mode over a 32 B ContentHash: the signature verifies; a modified message "
                          "and a modified signature are rejected; two signatures on the same message differ");
    return ok ? l1 : 0;
}

/* ------------------------------------------------------------------------ */
/* One relay wrap.                                                           */

typedef struct {
    const unsigned char *pk;
    unsigned char pt[WRAP_MAX_PT];
    size_t len;
    unsigned char out[WRAP_MAX_PT + ECIES_OVERHEAD];
} wrap_ctx;

static int64_t op_wrap(void *v)
{
    wrap_ctx *w = v;
    uint64_t t0, t1;
    int rc;

    t0 = now_ns();
    rc = ecies_seal(w->out, NULL, w->pk, w->pt, w->len);
    t1 = now_ns();
    g_sink ^= w->out[40];
    return rc == 0 ? (int64_t)(t1 - t0) : -1;
}

/* Plaintext: routing code (16 B) || ContentHash (32 B) || payload. */
static void wrap_fill(wrap_ctx *w, const std_key *relay, const unsigned char *routing_code, size_t payload_len)
{
    w->pk = relay->pk;
    w->len = ROUTING_CODE_LEN + CONTENTHASH_LEN + payload_len;
    memcpy(w->pt, routing_code, ROUTING_CODE_LEN);
    randombytes_buf(w->pt + ROUTING_CODE_LEN, w->len - ROUTING_CODE_LEN);
}

/* Part A's decrypt test, applied to one relay wrap. */
static void test_wrap(const char *name, wrap_ctx *w, const std_key *relay, const std_key *other)
{
    static unsigned char back[WRAP_MAX_PT];
    size_t wl = w->len + ECIES_OVERHEAD;
    int ok;

    ok = ecies_seal(w->out, NULL, w->pk, w->pt, w->len) == 0 &&
         ecies_open(back, relay->sk, w->out, wl) == (long)w->len && memcmp(back, w->pt, w->len) == 0;
    ok = ok && ecies_open(back, other->sk, w->out, wl) < 0;
    w->out[wl - 20] ^= 1;
    ok = ok && ecies_open(back, relay->sk, w->out, wl) < 0;
    report_test(name, ok, "the first relay opens the wrap and reads the routing code and payload; "
                          "a wrong key and a modified ciphertext are rejected");
}

/* ------------------------------------------------------------------------ */

static int list_has(const char *list, const char *item)
{
    return group_on(list, item);
}

static void usage_c(const char *argv0)
{
    fprintf(stderr,
            "usage: %s [--repeats-fast N] [--repeats-mid N] [--repeats-slow N]\n"
            "          [--rsa-bits 2048[,3072]] [--variants pss[,psszero]] [--schemes ecdaa[,epid]]\n",
            argv0);
}

int main(int argc, char **argv)
{
    const char *rsa_bits = "2048,3072", *variants = "pss,psszero", *schemes = "ecdaa,epid";
    static const int bits_all[2] = {2048, 3072};
    const daa_scheme *daa_all[2] = {&DAA_ECDAA, &DAA_EPID};
    static bssa_ctx bc[2][2];
    static rsa_issuer issuers[2];
    static daa_ctx dc[2];
    static wrap_ctx wtok, wsig[2];
    int have_bssa[2][2] = {{0}}, setup_ok[2] = {0};
    size_t sig_size[2] = {0};
    EVP_PKEY *pubs[2] = {NULL, NULL}, *x25519 = NULL;
    std_key relay, other;
    unsigned char routing_code[ROUTING_CODE_LEN];
    char sec_rsa[2][96], sec_x25519[96], params[64];
    int i, j;

    for (i = 1; i < argc; i++) {
        if (i + 1 >= argc) {
            usage_c(argv[0]);
            return 1;
        }
        if (strcmp(argv[i], "--repeats-fast") == 0)
            g_repeats[0] = atoi(argv[++i]);
        else if (strcmp(argv[i], "--repeats-mid") == 0)
            g_repeats[1] = atoi(argv[++i]);
        else if (strcmp(argv[i], "--repeats-slow") == 0)
            g_repeats[2] = atoi(argv[++i]);
        else if (strcmp(argv[i], "--rsa-bits") == 0)
            rsa_bits = argv[++i];
        else if (strcmp(argv[i], "--variants") == 0)
            variants = argv[++i];
        else if (strcmp(argv[i], "--schemes") == 0)
            schemes = argv[++i];
        else {
            usage_c(argv[0]);
            return 1;
        }
    }
    if (g_repeats[0] < 1 || g_repeats[1] < 1 || g_repeats[2] < 1 || !list_has(rsa_bits, "2048") ||
        !list_has(variants, "pss")) {
        usage_c(argv[0]);
        return 1;
    }

    if (crypto_init() != 0) {
        printf("{\"type\":\"fatal\",\"error\":\"library initialisation failed\"}\n");
        return 2;
    }

    printf("{\"type\":\"meta\",\"compiler\":\"%s\",\"cflags\":\"%s\",\"openssl_runtime\":\"%s\","
           "\"openssl_headers\":\"%s\",\"libsodium\":\"%s\",\"clock\":\"CLOCK_MONOTONIC_RAW\","
           "\"repeats\":{\"under_5_ms\":%d,\"5_to_100_ms\":%d,\"over_100_ms\":%d},"
           "\"rsa_bits\":\"%s\",\"variants\":\"%s\",\"schemes\":\"%s\",\"token_input_bytes\":%d,"
           "\"token_bytes\":%d,\"batch\":%d,\"ecies_overhead\":%d,"
           "\"daa\":[{\"key\":\"%s\",\"scheme\":\"%s\",\"kind\":\"%s\",\"library\":\"%s\",\"curve\":\"%s\","
           "\"security\":\"%s\",\"keygen\":\"%s\"},"
           "{\"key\":\"%s\",\"scheme\":\"%s\",\"kind\":\"%s\",\"library\":\"%s\",\"curve\":\"%s\","
           "\"security\":\"%s\",\"keygen\":\"%s\"}]}\n",
           __VERSION__, BUILD_CFLAGS, OpenSSL_version(OPENSSL_VERSION), OPENSSL_VERSION_TEXT,
           sodium_version_string(), g_repeats[0], g_repeats[1], g_repeats[2], rsa_bits, variants, schemes,
           TOKEN_INPUT_LEN, TOKEN_LEN, BATCH, ECIES_OVERHEAD,
           DAA_ECDAA.key, DAA_ECDAA.scheme, DAA_ECDAA.kind, DAA_ECDAA.library, DAA_ECDAA.curve, DAA_ECDAA.security,
           DAA_ECDAA.keygen_desc,
           DAA_EPID.key, DAA_EPID.scheme, DAA_EPID.kind, DAA_EPID.library, DAA_EPID.curve, DAA_EPID.security,
           DAA_EPID.keygen_desc);
    fflush(stdout);

    /* Setup. Keys and issuers are not timed. */
    for (i = 0; i < 2; i++) {
        BIGNUM *n = NULL, *e = NULL;
        snprintf(params, sizeof params, "%d", bits_all[i]);
        if (!list_has(rsa_bits, params))
            continue;
        if (issuer_init(&issuers[i], bits_all[i]) != 0 ||
            EVP_PKEY_get_bn_param(issuers[i].priv, OSSL_PKEY_PARAM_RSA_N, &n) != 1 ||
            EVP_PKEY_get_bn_param(issuers[i].priv, OSSL_PKEY_PARAM_RSA_E, &e) != 1 ||
            !(pubs[i] = rsa_public_key(n, e))) {
            printf("{\"type\":\"fatal\",\"error\":\"RSA-%d key setup failed\"}\n", bits_all[i]);
            return 2;
        }
        BN_free(n);
        BN_free(e);
        snprintf(sec_rsa[i], sizeof sec_rsa[i], "%d bits (OpenSSL EVP_PKEY_get_security_bits)",
                 EVP_PKEY_get_security_bits(pubs[i]));
        for (j = 0; j < 2; j++) {
            if (!list_has(variants, j == 0 ? "pss" : "psszero"))
                continue;
            if (rsabssa_pk_init(&bc[i][j].pk, pubs[i], VARIANTS[j].salt_len) != 0) {
                printf("{\"type\":\"fatal\",\"error\":\"RSA-%d client setup failed\"}\n", bits_all[i]);
                return 2;
            }
            bc[i][j].issuer = &issuers[i];
            have_bssa[i][j] = 1;
        }
    }
    x25519 = EVP_PKEY_Q_keygen(NULL, NULL, "X25519");
    snprintf(sec_x25519, sizeof sec_x25519, "%d bits (OpenSSL EVP_PKEY_get_security_bits for X25519)",
             x25519 ? EVP_PKEY_get_security_bits(x25519) : -1);
    for (i = 0; i < 2; i++) {
        dc[i].s = daa_all[i];
        if (list_has(schemes, daa_all[i]->key))
            setup_ok[i] = daa_all[i]->setup() == 0;
    }
    if (make_std_key(&relay) != 0 || make_std_key(&other) != 0) {
        printf("{\"type\":\"fatal\",\"error\":\"relay key setup failed\"}\n");
        return 2;
    }
    randombytes_buf(routing_code, sizeof routing_code);

    /* Correctness tests. No timing if any fails. */
    test_hkdf();
    test_x25519();
    test_aes_gcm();
    test_rfc9474_vectors();
    for (i = 0; i < 2; i++)
        for (j = 0; j < 2; j++)
            if (have_bssa[i][j])
                test_bssa_key(&bc[i][j], VARIANTS[j].variant, bits_all[i]);
    for (i = 0; i < 2; i++)
        if (list_has(schemes, daa_all[i]->key))
            sig_size[i] = test_daa(daa_all[i], setup_ok[i]);
    wrap_fill(&wtok, &relay, routing_code, TOKEN_LEN);
    test_wrap("ecies_wrap_one_relay_tokens_decrypt", &wtok, &relay, &other);
    for (i = 0; i < 2; i++) {
        char name[96];
        if (!sig_size[i])
            continue;
        wrap_fill(&wsig[i], &relay, routing_code, sig_size[i]);
        snprintf(name, sizeof name, "ecies_wrap_one_relay_sig_%s_decrypt", daa_all[i]->key);
        test_wrap(name, &wsig[i], &relay, &other);
    }
    printf("{\"type\":\"selftest_summary\",\"pass\":%s,\"failures\":%d}\n",
           g_selftest_failures ? "false" : "true", g_selftest_failures);
    fflush(stdout);
    if (g_selftest_failures)
        return 2;

    /* Blind-signed tokens. */
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            row_info r = {DESIGN_TOKENS, "RSA blind signatures (RFC 9474)", NULL, VARIANTS[j].variant,
                          NULL, sec_rsa[i], NULL, "OpenSSL BIGNUM; RSASSA-PSS-VERIFY by OpenSSL EVP",
                          TOKEN_INPUT_LEN};
            bssa_ctx *c = &bc[i][j];
            if (!have_bssa[i][j])
                continue;
            snprintf(params, sizeof params, "RSA-%d", bits_all[i]);
            r.params = params;
            randombytes_buf(c->msg, sizeof c->msg);
            r.name = "rsabssa_blind";
            r.description = "Blind (client): EMSA-PSS-ENCODE of the 98 B token input, then blinding";
            run_row_c(&r, op_blind, c);
            if (rsabssa_blind(&c->pk, c->blinded[0], c->inv[0], c->msg[0], TOKEN_INPUT_LEN) != 0 ||
                issuer_blind_sign(c->issuer, c->blind_sig[0], c->blinded[0], c->pk.modulus_len) != 0) {
                printf("{\"type\":\"row\",\"part\":\"C\",\"name\":\"rsabssa_finalize\",\"status\":\"failed\","
                       "\"error\":\"input setup failed\"}\n");
            } else {
                r.name = "rsabssa_finalize";
                r.description = "Finalize (client): unblinding and RSASSA-PSS-VERIFY";
                run_row_c(&r, op_finalize, c);
            }
            r.name = "rsabssa_blind_finalize_batch20";
            r.description = "Blind and finalize for a batch of 20 tokens; the issuer's signing is not timed";
            r.bytes = (size_t)BATCH * TOKEN_INPUT_LEN;
            run_row_c(&r, op_batch, c);
        }
    }

    /* DAA or EPID signature. */
    for (i = 0; i < 2; i++) {
        const daa_scheme *s = daa_all[i];
        row_info r = {DESIGN_DAA, s->scheme, NULL, NULL, s->curve, s->security, NULL, s->library, 0};
        if (!sig_size[i])
            continue;
        printf("{\"type\":\"size\",\"part\":\"C\",\"design\":\"%s\",\"scheme\":\"%s\",\"kind\":\"%s\","
               "\"name\":\"signature_size_bytes\",\"bytes\":%zu,"
               "\"description\":\"serialized anonymous-mode signature, as the library returns it\"}\n",
               DESIGN_DAA, s->scheme, s->kind, sig_size[i]);
        r.name = "member_key_generation";
        r.description = s->keygen_desc;
        run_row_c(&r, op_daa_keygen, &dc[i]);
        randombytes_buf(dc[i].msg, sizeof dc[i].msg);
        r.name = "sign";
        r.description = "Sign a 32 B ContentHash, anonymous mode (no basename)";
        r.bytes = DAA_MSG_LEN;
        run_row_c(&r, op_daa_sign, &dc[i]);
    }

    /* One relay wrap. */
    {
        row_info r = {DESIGN_TOKENS, "ECIES (Part A code)", "ecies_wrap_one_relay_tokens", NULL, "X25519",
                      sec_x25519,
                      "One ECIES wrap to the first relay: routing code 16 B + ContentHash 32 B + token 354 B",
                      "ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM", wtok.len};
        run_row_c(&r, op_wrap, &wtok);
        for (i = 0; i < 2; i++) {
            static char desc[2][160];
            if (!sig_size[i])
                continue;
            snprintf(desc[i], sizeof desc[i],
                     "One ECIES wrap to the first relay: routing code 16 B + ContentHash 32 B + %s signature %zu B",
                     daa_all[i]->scheme, sig_size[i]);
            r.design = DESIGN_DAA;
            r.scheme = daa_all[i]->scheme;
            r.name = "ecies_wrap_one_relay_sig";
            r.description = desc[i];
            r.bytes = wsig[i].len;
            run_row_c(&r, op_wrap, &wsig[i]);
        }
    }

    printf("{\"type\":\"done\"}\n");
    return 0;
}

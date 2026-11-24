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

/* RSA blind signatures, client side, RFC 9474. See rsabssa.h. */

#include "rsabssa.h"

#include <string.h>

#include <openssl/core_names.h>
#include <openssl/rand.h>
#include <openssl/rsa.h>

int rsabssa_pk_init(rsabssa_pk *pk, EVP_PKEY *pkey, size_t salt_len)
{
    memset(pk, 0, sizeof *pk);
    pk->pkey = pkey;
    pk->salt_len = salt_len;
    if (EVP_PKEY_get_bn_param(pkey, OSSL_PKEY_PARAM_RSA_N, &pk->n) != 1 ||
        EVP_PKEY_get_bn_param(pkey, OSSL_PKEY_PARAM_RSA_E, &pk->e) != 1)
        return -1;
    pk->mod_bits = BN_num_bits(pk->n);
    pk->modulus_len = (size_t)BN_num_bytes(pk->n);
    /* emLen = ceil((modBits - 1) / 8) must equal modulus_len, which holds when
     * modBits is not 1 more than a multiple of 8 (all moduli used here). */
    if (pk->modulus_len > RSABSSA_MAX_MODULUS_BYTES || (pk->mod_bits - 1) % 8 == 0)
        return -1;
    pk->bn = BN_CTX_new();
    return pk->bn ? 0 : -1;
}

void rsabssa_pk_free(rsabssa_pk *pk)
{
    BN_free(pk->n);
    BN_free(pk->e);
    BN_CTX_free(pk->bn);
    memset(pk, 0, sizeof *pk);
}

static int sha384(unsigned char out[RSABSSA_HLEN], const unsigned char *a, size_t alen,
                  const unsigned char *b, size_t blen, const unsigned char *c, size_t clen)
{
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    unsigned int outl = 0;
    int ok = ctx && EVP_DigestInit_ex(ctx, EVP_sha384(), NULL) == 1 &&
             (alen == 0 || EVP_DigestUpdate(ctx, a, alen) == 1) &&
             (blen == 0 || EVP_DigestUpdate(ctx, b, blen) == 1) &&
             (clen == 0 || EVP_DigestUpdate(ctx, c, clen) == 1) &&
             EVP_DigestFinal_ex(ctx, out, &outl) == 1 && outl == RSABSSA_HLEN;
    EVP_MD_CTX_free(ctx);
    return ok ? 0 : -1;
}

/* MGF1 with SHA-384 (RFC 8017 appendix B.2.1). XORs the mask into buf. */
static int mgf1_xor(unsigned char *buf, size_t len, const unsigned char *seed, size_t seed_len)
{
    unsigned char t[RSABSSA_HLEN], ctr[4];
    size_t done = 0, i;
    uint32_t c = 0;

    while (done < len) {
        ctr[0] = (unsigned char)(c >> 24);
        ctr[1] = (unsigned char)(c >> 16);
        ctr[2] = (unsigned char)(c >> 8);
        ctr[3] = (unsigned char)c;
        if (sha384(t, seed, seed_len, ctr, 4, NULL, 0) != 0)
            return -1;
        for (i = 0; i < RSABSSA_HLEN && done < len; i++)
            buf[done++] ^= t[i];
        c++;
    }
    return 0;
}

int rsabssa_emsa_pss_encode(const rsabssa_pk *pk, unsigned char *em,
                            const unsigned char *msg, size_t msg_len,
                            const unsigned char *salt)
{
    static const unsigned char zeros[8] = {0};
    unsigned char mhash[RSABSSA_HLEN], mprime[8 + RSABSSA_HLEN];
    size_t em_bits = (size_t)pk->mod_bits - 1;
    size_t em_len = (em_bits + 7) / 8;
    size_t db_len = em_len - RSABSSA_HLEN - 1;
    unsigned char *h = em + db_len;

    if (em_len < RSABSSA_HLEN + pk->salt_len + 2)
        return -1;
    /* mHash = Hash(M); M' = 0x00 * 8 || mHash || salt; H = Hash(M'). */
    if (sha384(mhash, msg, msg_len, NULL, 0, NULL, 0) != 0)
        return -1;
    memcpy(mprime, zeros, 8);
    memcpy(mprime + 8, mhash, RSABSSA_HLEN);
    if (sha384(h, mprime, sizeof mprime, salt, pk->salt_len, NULL, 0) != 0)
        return -1;
    /* DB = PS || 0x01 || salt; maskedDB = DB xor MGF(H, emLen - hLen - 1). */
    memset(em, 0, db_len - pk->salt_len - 1);
    em[db_len - pk->salt_len - 1] = 0x01;
    if (pk->salt_len)
        memcpy(em + db_len - pk->salt_len, salt, pk->salt_len);
    if (mgf1_xor(em, db_len, h, RSABSSA_HLEN) != 0)
        return -1;
    /* Clear the leftmost 8 * emLen - emBits bits. */
    em[0] &= (unsigned char)(0xFF >> (8 * em_len - em_bits));
    em[em_len - 1] = 0xbc;
    return 0;
}

int rsabssa_blind_with(const rsabssa_pk *pk, unsigned char *blinded_msg, unsigned char *inv,
                       const unsigned char *msg, size_t msg_len,
                       const unsigned char *salt, const BIGNUM *r)
{
    unsigned char em[RSABSSA_MAX_MODULUS_BYTES];
    BIGNUM *m, *g, *ri, *x, *z;
    int rc = -1;

    BN_CTX_start(pk->bn);
    m = BN_CTX_get(pk->bn);
    g = BN_CTX_get(pk->bn);
    ri = BN_CTX_get(pk->bn);
    x = BN_CTX_get(pk->bn);
    z = BN_CTX_get(pk->bn);
    if (!z)
        goto done;
    /* 1 to 3. encoded_msg = EMSA-PSS-ENCODE(msg); m = bytes_to_int(encoded_msg). */
    if (rsabssa_emsa_pss_encode(pk, em, msg, msg_len, salt) != 0)
        goto done;
    if (!BN_bin2bn(em, (int)pk->modulus_len, m))
        goto done;
    /* 4. m must be coprime with n. */
    if (!BN_gcd(g, m, pk->n, pk->bn) || !BN_is_one(g))
        goto done;
    /* 6. inv = inverse_mod(r, n). */
    if (!BN_mod_inverse(ri, r, pk->n, pk->bn))
        goto done;
    /* 7 and 8. x = RSAVP1(pk, r) = r^e mod n; z = m * x mod n. */
    if (!BN_mod_exp(x, r, pk->e, pk->n, pk->bn) || !BN_mod_mul(z, m, x, pk->n, pk->bn))
        goto done;
    /* 9. blinded_msg = int_to_bytes(z, modulus_len). */
    if (BN_bn2binpad(z, blinded_msg, (int)pk->modulus_len) != (int)pk->modulus_len ||
        BN_bn2binpad(ri, inv, (int)pk->modulus_len) != (int)pk->modulus_len)
        goto done;
    rc = 0;
done:
    BN_CTX_end(pk->bn);
    return rc;
}

int rsabssa_blind(const rsabssa_pk *pk, unsigned char *blinded_msg, unsigned char *inv,
                  const unsigned char *msg, size_t msg_len)
{
    unsigned char salt[RSABSSA_HLEN];
    BIGNUM *r;
    int rc = -1;

    BN_CTX_start(pk->bn);
    r = BN_CTX_get(pk->bn);
    if (!r)
        goto done;
    if (pk->salt_len && RAND_bytes(salt, (int)pk->salt_len) != 1)
        goto done;
    /* 5. r = random_integer_uniform(1, n). */
    do {
        if (!BN_rand_range(r, pk->n))
            goto done;
    } while (BN_is_zero(r));
    rc = rsabssa_blind_with(pk, blinded_msg, inv, msg, msg_len, salt, r);
done:
    BN_CTX_end(pk->bn);
    return rc;
}

int rsabssa_verify(const rsabssa_pk *pk, const unsigned char *sig,
                   const unsigned char *msg, size_t msg_len)
{
    EVP_MD_CTX *mctx = EVP_MD_CTX_new();
    EVP_PKEY_CTX *pctx = NULL;
    int ok;

    ok = mctx && EVP_DigestVerifyInit(mctx, &pctx, EVP_sha384(), NULL, pk->pkey) == 1 &&
         EVP_PKEY_CTX_set_rsa_padding(pctx, RSA_PKCS1_PSS_PADDING) == 1 &&
         EVP_PKEY_CTX_set_rsa_mgf1_md(pctx, EVP_sha384()) == 1 &&
         EVP_PKEY_CTX_set_rsa_pss_saltlen(pctx, (int)pk->salt_len) == 1 &&
         EVP_DigestVerify(mctx, sig, pk->modulus_len, msg, msg_len) == 1;
    EVP_MD_CTX_free(mctx);
    return ok ? 0 : -1;
}

int rsabssa_finalize(const rsabssa_pk *pk, unsigned char *sig,
                     const unsigned char *blind_sig, const unsigned char *inv,
                     const unsigned char *msg, size_t msg_len)
{
    BIGNUM *z, *ri, *s;
    int rc = -1;

    BN_CTX_start(pk->bn);
    z = BN_CTX_get(pk->bn);
    ri = BN_CTX_get(pk->bn);
    s = BN_CTX_get(pk->bn);
    if (!s)
        goto done;
    /* 2 to 4. s = z * inv mod n; sig = int_to_bytes(s, modulus_len). */
    if (!BN_bin2bn(blind_sig, (int)pk->modulus_len, z) || !BN_bin2bn(inv, (int)pk->modulus_len, ri))
        goto done;
    if (!BN_mod_mul(s, z, ri, pk->n, pk->bn) ||
        BN_bn2binpad(s, sig, (int)pk->modulus_len) != (int)pk->modulus_len)
        goto done;
    /* 5. RSASSA-PSS-VERIFY(pk, msg, sig). */
    rc = rsabssa_verify(pk, sig, msg, msg_len);
done:
    BN_CTX_end(pk->bn);
    return rc;
}

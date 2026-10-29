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
 * Field and packet sizes for the Part A benchmark.
 *
 * Field sizes come from Table A.1 of the Integration paper (v41) and the
 * Birthmark Protocol Messaging Structure (v119). Several are marked
 * "Estimate" there. Change them here; every other file reads them from this
 * header.
 */

#ifndef BENCHMARK_SIZES_H
#define BENCHMARK_SIZES_H

/* Input file sizes for ContentHash = SHA-256(file). */
#define FILE_SIZE_LOW      25000000u
#define FILE_SIZE_CENTRAL  30000000u /* 468,750 compressions of 64 B */
#define FILE_SIZE_HIGH     35000000u

/* Table A.1 fields. */
#define CRED_HW_LEN             32 /* Estimate in Table A.1 */
#define REPLAY_NONCE_LEN        16
#define CLAIM_LEN                2 /* Estimate in Table A.1 */
#define BINDING_HASH_LEN        32
#define KEY_REF_LEN              8 /* Estimate in Table A.1 */
#define CONTENTHASH_LEN         32
#define CONTENT_NONCE_LEN       16 /* n */
#define FLAGS_LEN                1
#define H_METADATA_LEN          32
#define PARENT_CONTENTHASH_LEN  32
#define FULLPACKETHASH_LEN      32
#define BLINDSHARE_KEY_LEN      32
#define ROUTING_CODE_LEN        16

/* h(metadata) is SHA-256 over three 32 B per-field commitments. */
#define METADATA_COMMITMENTS_LEN (3 * 32)

/* AEAD (AES-256-GCM). */
#define AEAD_KEY_LEN    32
#define AEAD_NONCE_LEN  12
#define AEAD_TAG_LEN    16

/* Enc_FullPacketHash = AEAD(BlindShare_key; FullPacketHash), 48 B. */
#define ENC_FULLPACKETHASH_LEN (FULLPACKETHASH_LEN + AEAD_TAG_LEN)

/*
 * ECIES wire layout used here: version byte || EPK || AEAD ciphertext || tag.
 * The AES-GCM nonce is derived by HKDF together with the key and is not sent.
 */
#define ECIES_VERSION_LEN    1
#define ECIES_EPK_LEN       32
#define ECIES_OVERHEAD      (ECIES_VERSION_LEN + ECIES_EPK_LEN + AEAD_TAG_LEN)
#define SPEC_ECIES_OVERHEAD 49 /* Table A.1 */

/* Layer 1: token T plaintext = Cred_HW || replay_nonce || claim || binding_hash. */
#define TOKEN_PT_LEN (CRED_HW_LEN + REPLAY_NONCE_LEN + CLAIM_LEN + BINDING_HASH_LEN) /* 82 */
#define TOKEN_CT_LEN (TOKEN_PT_LEN + ECIES_OVERHEAD)

/* Layer 2: CredP plaintext = T || key_ref || FullPacketHash || BlindShare_key. */
#define CREDP_PT_LEN (TOKEN_CT_LEN + KEY_REF_LEN + FULLPACKETHASH_LEN + BLINDSHARE_KEY_LEN) /* 203 */
#define CREDP_CT_LEN (CREDP_PT_LEN + ECIES_OVERHEAD)

/*
 * Layers 3 and 4: ContP plaintext = flags || ContentHash || n || [h(metadata)] || [parent ContentHash].
 * The spec allows 49, 81 or 113 B. 300 B is a stress case outside the spec.
 */
#define CONTP_PT_LEN_MIN          (FLAGS_LEN + CONTENTHASH_LEN + CONTENT_NONCE_LEN)  /* 49 */
#define CONTP_PT_LEN_META         (CONTP_PT_LEN_MIN + H_METADATA_LEN)                /* 81 */
#define CONTP_PT_LEN_META_PARENT  (CONTP_PT_LEN_META + PARENT_CONTENTHASH_LEN)       /* 113 */
#define CONTP_PT_LEN_STRESS       300
#define CONTP_PT_LEN_CAPTURE      CONTP_PT_LEN_META /* used in the whole-capture run */
#define CONTP_CT_LEN_CAPTURE      (CONTP_PT_LEN_CAPTURE + ECIES_OVERHEAD)

/* FullPacketHash input = ContentHash || n || flags || h(metadata). */
#define FULLPACKETHASH_INPUT_LEN (CONTENTHASH_LEN + CONTENT_NONCE_LEN + FLAGS_LEN + H_METADATA_LEN) /* 81 */

/* Layers 5 to 7: first-relay wrap plaintext = routing code || inner packet. */
#define WRAP_CREDP_PT_LEN (ROUTING_CODE_LEN + CREDP_CT_LEN)          /* 268 */
#define WRAP_CONTP_PT_LEN (ROUTING_CODE_LEN + CONTP_CT_LEN_CAPTURE)  /* 146 */

/*
 * Padded variant: Table A.2 pads legs to 420-460 B inside the transit
 * encryption. 460 B is the upper end of that range.
 */
#define WRAP_PADDED_PT_LEN 460

/* Largest plaintext any row uses. */
#define MAX_PT_LEN 512

#endif

# Part B candidates

This file surveys zero-knowledge provers for one statement: knowledge of a message M such that SHA-256(M) = H, with H public. The target is a Raspberry Pi 4 Model B, 4 GB, Cortex-A72 at 1.5 GHz, aarch64 Linux, CPU only.

Nothing here is measured. Figures marked "vendor-reported" come from the project's own README. Figures marked ESTIMATE are this survey's estimates, with the basis given. Neither kind may appear in `results/`.

Research date: 2026-10-26. Sources were read at the commits listed. This environment's network policy blocked `oumuamua.dev`, `arxiv.org` and `eprint.iacr.org`. The Flock paper's Table 2 and Hekate's online documentation were therefore not read directly. Their GitHub repositories were.

## A constraint that affects most candidates

The Pi 4's Cortex-A72 (BCM2711) has no ARMv8 crypto extensions: no `aes`, no `pmull`, no `sha2`.

- Hekate, Flock, Binius64 and Longfellow-zk all compute over the binary field GF(2^128).
- On aarch64 they use the PMULL instruction for that multiplication.
- Without PMULL they fall back to slower NEON or portable code, or need a build change.

On the Pi 4, Part A's SHA-256 also runs without SHA extensions. Both sides of the comparison lose their hardware instruction. The Part B summary must state this.

## Candidates

| Candidate | Proof system | Zero-knowledge | Trusted setup | aarch64 Linux / Pi 4 | Statement proved | Source and commit | Build effort (ESTIMATE) | Largest M in 80% of 4 GB (ESTIMATE) |
|---|---|---|---|---|---|---|---|---|
| **Hekate** (Oumuamua Labs) | Sumcheck + Brakedown PCS over binary tower fields; SHA-256 chiplet | Yes, on by default; `--no-zk` turns it off | No | A signed prover binary ships for Linux ARM64 (glibc). The prover is closed source. The open field library takes PMULL only when built with `+aes`. Whether the shipped binary needs PMULL is unknown; if it does, it stops with an illegal-instruction error on the Pi 4. No x86-64 Linux prover binary is listed. | Full message: host pads and chains blocks (`hekate/examples/sha256.rs`, `pad_message`). Whether H is a public output must be confirmed in Phase 3. | github.com/oumuamua-labs/hekate @ `3268d3a3fe8fab6e59c87d60a84a33645369ce01` (v0.38.0); prover binary 0.16.1 from `releases.oumuamua.dev`; hekate-mobile @ `e0099d48489d489076a15799dd196281385bf2b4` | Low to medium. Rust 1.88+, cargo build on the Pi with swap, binary download on the Pi. | About 1 to 4 MiB. Basis: vendor-reported peak memory of 55 MiB at 1 KiB and 142 MiB at 127.9 KiB (iPhone), linear growth of about 0.69 MiB per KiB; 3.2 GiB then gives about 4.6 MiB. Trace sizes are powers of two, so memory grows in steps. |
| **Longfellow-zk** (Google) | Sumcheck (GKR-style) + Ligero; GF(2^128) or Goldilocks Fp2 | Yes (`ZkProver`) | No | Builds from source (C++, CMake). On aarch64 the GF(2^128) code assumes PMULL. The source says to edit one `#if` to use its NEON fallback. The Goldilocks Fp2 variant (`BM_ShaZK_Fp64_2`) needs no PMULL. | Full message with chaining (`assert_message_hash`, `numBlocks`) | github.com/google/longfellow-zk @ `8861765fbbfaca7a452da60f8ceb8c6de8e4a003` | Medium. CMake build plus a small driver. The upstream benchmark stops at 33 blocks (about 2 KiB), so larger sizes need new code. | Unknown. No memory figures are published. |
| **Flock** (Bünz, Rothblum, Wang; Succinct Labs) | Zerocheck + lincheck PIOP, Ligerito PCS over GF(2^128) | No. No zero-knowledge mode found in the code. The papers also say Flock does not yet provide zero-knowledge. | No | Builds from source (Rust). NEON kernels and portable fallbacks are listed. | A batch of **independent** compressions. Not one chained message. | github.com/succinctlabs/flock @ `d2a3cc18086c010d5ddcf59470dfed8f5cdf69b5`. Mirror: argumentcomputer/flock @ `b684b12`. | Medium. Rust edition 2024. | Unknown. Its largest published batch is 262,144 compressions, run on a 36 GB machine. |
| **Binius64** (Irreducible) | Binius64 (AND/MUL constraints on 64-bit words); separately Iron Spartan (GF(2^128) R1CS) | The SHA-256 examples use Binius64, which `ARCHITECTURE.md` lists as **not** zero-knowledge. Iron Spartan is zero-knowledge, but has no SHA-256 example. | No | Builds from source (Rust 1.98.1, pinned). Without `aes` it uses the portable field code. | Full message (`crates/examples/src/circuits/sha256.rs`) | github.com/binius-zk/binius64 @ `4428e759dd27956bd5b9ae5025d67eb8ccc1accf` | Medium without zero-knowledge. High with it: an Iron Spartan SHA-256 circuit must be written. | Unknown |
| **Circom + circomlib SHA-256, rapidsnark (Groth16)** | Groth16 over BN254 | Yes | Yes, per circuit (Powers of Tau, then a per-circuit phase 2) | rapidsnark documents a Linux arm64 build (`make host_arm64`). | Full message (`Sha256(nBits)`); the size is fixed at circuit compile time | iden3/circom @ `9b4b23331644e17868c90a85768826ed3bcba59f`, iden3/circomlib @ `35e54ea21da3e8762557234298dbb553c175ea8d`, iden3/rapidsnark @ `81eddf1a536d26497b237c0b8a04fe90baf7e439` | Medium to high. Circom compiler, Node.js and snarkjs, a Powers of Tau file, and one circuit and setup per size. | Low, likely tens of KiB at most. Basis: about 30,000 constraints per circuit as reported by a third party (zk_bench, size unclear). Circuit compilation and setup memory are the limit. Not measured on this board. |
| **gnark** (Consensys) | Groth16 or PLONK over BN254 | Yes | Groth16: per circuit. PLONK: universal KZG setup. | Pure Go. Builds on aarch64. | Full message with `std/hash/sha2`; the size is fixed per circuit | github.com/Consensys/gnark @ `0be5c2ff3dbb2caafb8d48760b6f7e3ffd511b46` | Medium. A short Go circuit per size. | Unknown. No per-block constraint count was found. |
| **RISC Zero** | zk-STARK zkVM (RISC-V), SHA-256 accelerator | The docs say the zkVM "targets perfect zero-knowledge". The same page says no mathematical proof of zero-knowledge has been written. | No for STARK receipts. The Groth16 wrap has a setup and is not needed here. | `rzup` lists `aarch64-unknown-linux-gnu`. Memory is set by the segment size (`segment_limit_po2`). | Full message hashed inside the guest | github.com/risc0/risc0 @ `02d9469e91469125bc01e91cc63715fb55e62a83` | Medium. rzup toolchain, a guest program, and segment tuning. | Time is the limit, not memory: segments are proved one after another at a fixed segment size. |
| **SP1** (Succinct) | STARK zkVM | Core and compressed STARK proofs are **not** zero-knowledge (SP1 security model page). Only the Groth16 or PLONK wrap is. | The Groth16 wrap uses a ceremony | Not checked further | Full message in the guest | github.com/succinctlabs/sp1 @ `a094cb0a44e29b6075219bf5d8626ec3a01aef0b` | High | Not evaluated |
| **halo2** (zcash) | PLONKish, IPA | Yes | No | Pure Rust | No SHA-256 gadget in `zcash/halo2` at this commit. Third-party forks have one. | github.com/zcash/halo2 @ `2d54aaf07c8135d0ce54313048999b4002b4cfbf` | High | Not evaluated |
| **plonky2** | PLONK + FRI, Goldilocks | Optional (`zero_knowledge` in `CircuitConfig`) | No | Pure Rust | No SHA-256 in the repository. A third-party crate is needed. Last commit 2025-07-01. | github.com/0xPolygonZero/plonky2 @ `5d9da5a65bbcba2c66eb29c035090eb2e9ccb05f` | High | Not evaluated |
| **Plonky3** | STARK toolkit; `sha256-air`; also a `flock` crate | The binary-field SHA-256 example is "not zero knowledge" (README). Zero-knowledge exists only on the univariate STARK path with `HidingFriPcs`, and there is no SHA-256 example for it. | No | Pure Rust | Independent compressions (`prove_hash_binary`) | github.com/Plonky3/Plonky3 @ `c5eb6a19eb439280d5df345476fb5a0145e542d6` | High for a zero-knowledge SHA-256 | Not evaluated |

## Vendor-reported figures the papers rely on

- **Hekate, 949 ms.** This is in the hekate-mobile README: "SHA-256 of a 127.9 KiB message", iPhone 14 Pro Max, zero-knowledge on.
  - Prove 949 ms, verify 11 ms.
  - Proof size 1,039 to 1,046 KiB, peak memory 142 MiB.
  - Signed `ct` prover 0.16.1, hekate 0.38.0, best of three, on battery.
  - The table is on `main` at `e0099d4` (2026-10-20), where the package version reads 0.3.0. The `v0.3.0` tag (`becc92a`, 2026-10-11) has no benchmark table. The papers' citation of "hekate-mobile 0.3.0" should name the commit.
- **Flock, M4 Max.** The Flock README reports single-thread SHA-256 proving throughput of 12.6 to 58.2 thousand compressions per second on an Apple M4 Max. The rate rises with batch size, from 1,024 to 262,144. These are batches of independent compressions, without zero-knowledge. This survey could not read the paper's Table 2, so the "about 42,000 per second" figure in the papers was not checked against it.

## Recommendation

**Primary: Hekate.**

Hekate is the fairest choice for the papers' argument for four reasons:

- It is the system whose figure the papers cite.
- Its zero-knowledge is on by default.
- It proves the full statement: a padded, chained SHA-256 of one message.
- It needs no trusted setup and is built for ARM edge devices.

Three risks:

1. **The prover is a closed binary.** If it needs PMULL, it will not run on the Pi 4. That outcome would be recorded as a failure, with the error.
2. **No x86-64 dry run.** No x86-64 Linux prover binary is listed, and this environment cannot reach the download host.
3. **Licensing.** The open code is AGPL-3.0-only, with a linking exception for the prover binary. To stay out of AGPL terms, Phase 3 would run Hekate's own `sha256` example from a pinned clone and not ship code that links Hekate.

**Second: Longfellow-zk.**

- It is open source (Apache-2.0), zero-knowledge, needs no trusted setup, and proves the full chained statement.
- It builds from a pinned commit on both aarch64 and x86-64, so it can be dry-run here first.
- Its Goldilocks Fp2 variant avoids the missing PMULL entirely.
- It gives a reproducible result even if Hekate's binary fails.

**Fastest by published throughput: Flock.** It does not fit the comparison as a zero-knowledge prover, for two reasons:

- It has no zero-knowledge mode.
- It proves batches of independent compressions, not one chained message.

It could be added as a labelled non-zero-knowledge reference point.

Not recommended for the Pi 4 comparison:

- SP1, because its proofs are zero-knowledge only after a Groth16 or PLONK wrap.
- halo2, plonky2 and Plonky3, because none has a ready zero-knowledge SHA-256 at the commits read.
- circom/rapidsnark and gnark are feasible but use trusted-setup SNARKs. Their circuit size per message limits them to small messages on 4 GB.

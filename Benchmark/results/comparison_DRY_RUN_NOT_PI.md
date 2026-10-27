DRY RUN, NOT PI

# Part B comparison

Machine: Intel(R) Xeon(R) Processor @ 2.80GHz. Prover: Longfellow-zk, field gf2_128, zero-knowledge on, one thread. Run `20261026T220750Z_vm_DRY_RUN_NOT_PI`.

Hash times in milliseconds. "Without" is OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI).

| Input size | Hash time with SHA extensions | Hash time without | Prover time | Prover peak memory | Ratio (prover ÷ hash without) |
|---|---:|---:|---:|---:|---:|
| 1 KiB | not available: the CPU feature list has no sha_ni | 0.002609 | 0.4307 s | 69 MiB | 165,092 |
| 4 KiB | not available: the CPU feature list has no sha_ni | 0.009618 | 1.44 s | 234 MiB | 149,796 |
| 30,000,000 B | not available: the CPU feature list has no sha_ni | 107.6 | 4,285 s (EXTRAPOLATED, power law) | 728 GiB (EXTRAPOLATED, power law) | 39,833 (EXTRAPOLATED) |
| 30,000,000 B | not available: the CPU feature list has no sha_ni | 107.6 | 10,390 s (EXTRAPOLATED, linear from largest point) | 1,650 GiB (EXTRAPOLATED, linear from largest point) | 96,589 (EXTRAPOLATED) |

Hash times at 30,000,000 B are measured. Every prover cell at 30,000,000 B is EXTRAPOLATED.
130,944 B (2,047 compressions) approximates the vendor's unpublished byte count for the "127.9 KiB" message.

## Limitations

- One machine: Intel(R) Xeon(R) Processor @ 2.80GHz (a dry run, not a Pi).
- Core class: the Intel(R) Xeon(R) Processor @ 2.80GHz is an out-of-order core. The papers' figures are for their slowest class, an in-order Cortex-A8 at 800 MHz. These results do not show what a Cortex-A8 would measure.
- Prover: Longfellow-zk. It is open source (Apache-2.0), zero-knowledge, needs no trusted setup, proves the full chained SHA-256 of one message, and builds from a pinned commit. Hekate, the system the papers cite, has a closed prover binary. It was not run in this run.
- Zero-knowledge: on in every proof (Ligero rate 7, 132 queries; Longfellow's source states about 109 bits of statistical security).
- Setup: circuit construction is not included in the prover time. It is reported separately in partB_summary.md. Setup rows that ran with swap are labelled "setup with swap, not comparable".
- Statement: H is public and the length of M is fixed by the circuit, as in Hekate's statement. Longfellow's own SHA-256 benchmark marks no input public, so its published figures prove a different statement; this run uses its own circuit.
- Threads: one, pinned, to match the single-core hash in Part A.
- Peak memory method: GNU time -v.
- Root of unity: for Fp64_2 the driver uses the root 2752994695033296049 with order 2^29. Longfellow's BM_ShaZK_Fp64_2 benchmark passes order 2^32, with which an honest proof is rejected.
- Plain hash: M is in RAM; no disk reads.
- Failures and stops:
  - fp64_2, 16 KiB: stopped, no circuit file zk/build/circuits/fp64_2_16384.circuit; run the setup phase for this size.
  - gf2_128, 16 KiB: stopped, no circuit file zk/build/circuits/gf2_128_16384.circuit; run the setup phase for this size.

DRY RUN, NOT PI. None of the numbers above is a Raspberry Pi measurement.

DRY RUN, NOT PI

# Part B summary (dry run)

This run is not from a Raspberry Pi. The machine reports `Intel(R) Xeon(R) Processor @ 2.80GHz`. These numbers test the code path only and must not be cited as Pi results.

- Run: `20261026T220750Z_vm_DRY_RUN_NOT_PI`. Full data: `results/partB_DRY_RUN_NOT_PI_2026-10-26_vm.json`.
- Statement: knowledge of M with SHA-256(M) = H; H public; length of M fixed by the circuit. Zero-knowledge on. One thread, pinned to core 3.
- Prover: Longfellow-zk, commit `8861765fbbfaca7a452da60f8ceb8c6de8e4a003`, Ubuntu clang version 18.1.3 (1ubuntu1), build type Release.
- Build changes to Longfellow: none. The diff is in each raw log's header.
- RAM: 15.71 GiB. CPU features: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves arat umip avx512_vnni md_clear arch_capabilities
- 130,944 B (2,047 compressions) approximates the vendor's unpublished byte count for the "127.9 KiB" message.

## Setup: circuit construction

Setup is not part of the prover time. A setup row marked "setup with swap, not comparable" ran while swap was active, and its time must not be compared with anything.

| Field | Size | Compressions | Setup time (s) | Setup label | Peak memory | Circuit file | Status |
|---|---|---:|---:|---|---:|---:|---|
| fp64_2 | 1 KiB | 17 | 10.79 | on this machine, no swap | 774 MiB | 48.5 MB | ok |
| fp64_2 | 4 KiB | 65 | 78.74 | on this machine, no swap | 2,959 MiB | 185.8 MB | ok |
| gf2_128 | 1 KiB | 17 | 11.86 | on this machine, no swap | 613 MiB | 30.5 MB | ok |
| gf2_128 | 4 KiB | 65 | 51.90 | on this machine, no swap | 2,158 MiB | 116.9 MB | ok |

## Prove: measured

Times in seconds. Prove covers Longfellow's commit and prove calls. Peak memory is the whole prove process (circuit load and all repeats), from `/usr/bin/time -v`.

| Field | Size | Compressions | n | Prove min | Prove median | Prove mean | Prove p95 | Prove std | Verify median | Circuit load | Proof size | Peak memory | Checks | Flag |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| fp64_2 | 1 KiB | 17 | 5 | 0.844 | 1.20 | 1.13 | 1.29 | 0.1738 | 0.5956 | 1.12 | 225 kB | 78 MiB | honest accepted, tampered proof rejected, wrong H rejected |  |
| fp64_2 | 4 KiB | 65 | 5 | 3.84 | 4.10 | 4.52 | 6.24 | 0.9902 | 2.40 | 4.51 | 378 kB | 274 MiB | honest accepted, tampered proof rejected, wrong H rejected |  |
| gf2_128 | 1 KiB | 17 | 5 | 0.3546 | 0.4307 | 0.4202 | 0.4617 | 0.04107 | 0.1577 | 0.7815 | 464 kB | 69 MiB | honest accepted, tampered proof rejected, wrong H rejected |  |
| gf2_128 | 4 KiB | 65 | 5 | 1.31 | 1.44 | 1.48 | 1.71 | 0.1678 | 0.5894 | 2.21 | 725 kB | 234 MiB | honest accepted, tampered proof rejected, wrong H rejected |  |

## Field pilot

- 1 KiB: median prove fp64_2 1.20 s, gf2_128 0.4307 s. Faster: gf2_128.
- 4 KiB: median prove fp64_2 4.10 s, gf2_128 1.44 s. Faster: gf2_128.

Field used for the comparison and the extrapolation: gf2_128 (tie on measured sizes; lower median prove time at 4 KiB).

## Where the sweep stopped

- fp64_2, 16 KiB: no circuit file zk/build/circuits/fp64_2_16384.circuit; run the setup phase for this size.
- gf2_128, 16 KiB: no circuit file zk/build/circuits/gf2_128_16384.circuit; run the setup phase for this size.

## Plain SHA-256 of M on the same machine

Times in milliseconds, M in RAM, same code as Part A row A1.

| Size | Path | n | min | median | p95 | std | Flag |
|---|---|---:|---:|---:|---:|---:|---|
| 1 KiB | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 2000 | 0.002572 | 0.002609 | 0.003027 | 0.001796 |  |
| 1 KiB | libsodium crypto_hash_sha256 (portable C) | 2000 | 0.004502 | 0.004615 | 0.007601 | 0.00308 |  |
| 1 KiB | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 2000 | 0.004087 | 0.006901 | 0.007948 | 0.004951 |  |
| 4 KiB | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 2000 | 0.009489 | 0.009618 | 0.01576 | 0.06555 |  |
| 4 KiB | libsodium crypto_hash_sha256 (portable C) | 2000 | 0.01689 | 0.02121 | 0.03734 | 0.03545 |  |
| 4 KiB | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 2000 | 0.01388 | 0.02367 | 0.03168 | 0.008771 |  |
| 30,000,000 B | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 20 | 87.146 | 107.6 | 109.9 | 4.998 |  |
| 30,000,000 B | libsodium crypto_hash_sha256 (portable C) | 20 | 143.2 | 176.2 | 212.1 | 27.600 |  |
| 30,000,000 B | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 20 | 148.4 | 236.8 | 244.0 | 38.305 |  |

## Prover time ÷ hash time

Median prove time divided by the median plain-hash time of the same M.

| Field | Size | Prove median (s) | ÷ OpenSSL default | ÷ OpenSSL capabilities off | ÷ libsodium |
|---|---|---:|---:|---:|---:|
| fp64_2 | 1 KiB | 1.20 | 459,281 | 173,636 | 259,646 |
| fp64_2 | 4 KiB | 4.10 | 426,781 | 173,450 | 193,553 |
| gf2_128 | 1 KiB | 0.4307 | 165,092 | 62,415 | 93,331 |
| gf2_128 | 4 KiB | 1.44 | 149,796 | 60,879 | 67,935 |

## Extrapolation to 30,000,000 B (EXTRAPOLATED)

Field gf2_128. Target: 30,000,000 B, 468,750 compressions. Largest measured size: 4 KiB (65 compressions).

| Quantity | Power-law fit | Points | R² | EXTRAPOLATED: power law | EXTRAPOLATED: linear from largest point |
|---|---|---:|---:|---:|---:|
| Prove time | value ∝ compressions^0.900 | 2 | 1.0000 | 4,285 s (EXTRAPOLATED) | 10,390 s (EXTRAPOLATED) |
| Prove-process peak memory | value ∝ compressions^0.908 | 2 | 1.0000 | 728 GiB (EXTRAPOLATED) | 1,650 GiB (EXTRAPOLATED) |
| Setup peak memory | value ∝ compressions^0.939 | 2 | 1.0000 | 8,841 GiB (EXTRAPOLATED) | 15,201 GiB (EXTRAPOLATED) |

With two points the power law passes through both, so R² is 1 by construction and says nothing about the fit.

- Memory, prove process (EXTRAPOLATED): the lower of the two estimates is 728.3 GiB, which does not fit in this machine's RAM and does not fit in 8 GB. Basis: the measured growth in the rows above.
- Memory, setup (EXTRAPOLATED): the lower of the two estimates is 8,840.6 GiB, which does not fit in this machine's RAM and does not fit in 8 GB. Basis: the measured growth in the rows above.

## Hekate (attempted on this machine)

Not run in this run.

DRY RUN, NOT PI. None of the numbers above is a Raspberry Pi measurement.

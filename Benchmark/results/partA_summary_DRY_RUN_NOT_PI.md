DRY RUN, NOT PI

# Part A summary (dry run)

This run is not from a Raspberry Pi. The machine reports `Intel(R) Xeon(R) Processor @ 2.80GHz`. These numbers test the code path only and must not be cited as Pi results.

- Run: `20261026T155810Z_vm_DRY_RUN_NOT_PI`. Generated 2026-10-26T16:09:54+00:00 from the raw logs below. Full data: `results/partA_DRY_RUN_NOT_PI_2026-10-26_vm.json`.
- CPU: Intel(R) Xeon(R) Processor @ 2.80GHz, x86_64, 4 cores. Measured max frequency of the pinned core: not available.
- CPU features: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves arat umip avx512_vnni md_clear arch_capabilities
- RAM: 15.71 GiB. OS: Ubuntu 24.04.5 LTS. Kernel: Linux vm 6.18.44-fc-v153 #1 SMP PREEMPT_DYNAMIC @0 x86_64 x86_64.
- Pinned to core 3 with taskset. Governor before the run: not available. Governor during the run: not available (no cpufreq interface).
- Compiler: gcc 13.3.0, flags `-O2`. OpenSSL OpenSSL 3.0.13 30 Jan 2024. libsodium 1.0.18.
- Clock: CLOCK_MONOTONIC_RAW. Cycle counter: unavailable.

## Runs

| Variant | Environment | Self-tests | Throttle | Temp before | Temp after | Exit | Raw log |
|---|---|---|---|---|---|---|---|
| default | unchanged | pass | unknown (vcgencmd not available) | n/a | n/a | 0 | `results/raw/partA_20261026T155810Z_vm_DRY_RUN_NOT_PI_default.jsonl` |
| caps_off | OPENSSL_ia32cap=0x0:0x0 | pass | unknown (vcgencmd not available) | n/a | n/a | 0 | `results/raw/partA_20261026T155810Z_vm_DRY_RUN_NOT_PI_caps_off.jsonl` |

## Results

Times in milliseconds. n is the number of timed repeats after warm-up.

The CPU feature list has no `sha_ni`. No row used SHA extensions, so the rows "with SHA extensions" are not reported.

Capability switch check, 30,000,000 B: OpenSSL default median 79.630 ms, capabilities off 106.2 ms, ratio 1.334. The time changed by more than 5%.

| Part | Row | Path or implementation | Bytes | n | min | median | mean | p95 | std | cycles/byte | Flag |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A1 | sha256_file_openssl | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 25000000 | 20 | 63.441 | 66.708 | 67.695 | 76.204 | 4.465 | 7.47 |  |
| A1 | sha256_file_libsodium | libsodium crypto_hash_sha256 (portable C) | 25000000 | 20 | 89.979 | 93.123 | 94.703 | 99.398 | 5.060 | 10.43 |  |
| A1 | sha256_file_openssl | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 30000000 | 20 | 76.793 | 79.630 | 85.000 | 109.1 | 10.240 | 7.43 |  |
| A1 | sha256_file_libsodium | libsodium crypto_hash_sha256 (portable C) | 30000000 | 20 | 109.6 | 113.5 | 119.3 | 140.3 | 12.495 | 10.59 |  |
| A1 | sha256_file_openssl | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 35000000 | 20 | 88.187 | 93.049 | 96.245 | 111.1 | 9.027 | 7.44 |  |
| A1 | sha256_file_libsodium | libsodium crypto_hash_sha256 (portable C) | 35000000 | 20 | 127.0 | 142.2 | 142.7 | 159.8 | 12.244 | 11.38 |  |
| A2 | x25519_variable_base | libsodium |  | 2000 | 0.03772 | 0.03796 | 0.04766 | 0.06499 | 0.07645 |  |  |
| A2 | x25519_fixed_base | libsodium |  | 2000 | 0.03498 | 0.0544 | 0.05261 | 0.08034 | 0.02627 |  |  |
| A2 | x25519_capture_mix | libsodium |  | 2000 | 0.5179 | 0.5511 | 0.6095 | 0.8758 | 0.1494 |  |  |
| A3 | ecies_layer1_token | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 82 | 2000 | 0.07844 | 0.07978 | 0.09179 | 0.1271 | 0.02879 |  |  |
| A3 | eciesb_layer2_credp | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 203 | 2000 | 0.0811 | 0.08152 | 0.08992 | 0.1201 | 0.01657 |  |  |
| A3 | eciesb_layer3_4_contp_49B | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 49 | 2000 | 0.08104 | 0.08143 | 0.08767 | 0.1133 | 0.02126 |  |  |
| A3 | eciesb_layer3_4_contp_81B | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 81 | 2000 | 0.08106 | 0.08145 | 0.09431 | 0.1333 | 0.02172 |  |  |
| A3 | eciesb_layer3_4_contp_113B | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 113 | 2000 | 0.08107 | 0.1135 | 0.1072 | 0.154 | 0.0397 |  |  |
| A3 | eciesb_layer3_4_contp_300B_stress | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 300 | 2000 | 0.08106 | 0.08157 | 0.09046 | 0.1188 | 0.0396 |  |  |
| A3 | ecies_layer5_wrap_credp | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 268 | 2000 | 0.07844 | 0.07937 | 0.08782 | 0.1181 | 0.02589 |  |  |
| A3 | ecies_layer6_7_wrap_contp | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 146 | 2000 | 0.07844 | 0.07915 | 0.08695 | 0.1169 | 0.03124 |  |  |
| A3 | ecies_layer5_7_wrap_padded_460B | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM | 460 | 2000 | 0.07848 | 0.07883 | 0.08263 | 0.1024 | 0.0102 |  |  |
| A3 | hkdf_sha256_44B | OpenSSL EVP_KDF HKDF | 44 | 2000 | 0.004341 | 0.00442 | 0.00475 | 0.004564 | 0.00371 |  |  |
| A3 | aes256gcm_seal_203B | OpenSSL EVP AES-256-GCM | 203 | 2000 | 0.000479 | 0.000494 | 0.000511 | 0.000518 | 0.0004568 |  |  |
| A3 | ecies_seven_layers | 3 ECIESb + 4 ECIES |  | 2000 | 0.5577 | 0.5862 | 0.6196 | 0.8649 | 0.1036 |  |  |
| A3 | ecies_seven_layers_padded | 3 ECIESb + 4 ECIES |  | 2000 | 0.5588 | 0.588 | 0.6121 | 0.7246 | 0.1176 |  |  |
| A4 | h_metadata | OpenSSL EVP SHA256 | 96 | 2000 | 0.000416 | 0.000428 | 0.0004418 | 0.000447 | 0.0004216 |  |  |
| A4 | fullpackethash | OpenSSL EVP SHA256 | 81 | 2000 | 0.000416 | 0.000432 | 0.0004835 | 0.000635 | 0.0006206 |  |  |
| A4 | enc_fullpackethash | OpenSSL EVP AES-256-GCM | 32 | 2000 | 0.000402 | 0.000417 | 0.0004991 | 0.000703 | 0.0009935 |  |  |
| A4 | binding_hash | OpenSSL EVP SHA256 | 48 | 2000 | 0.000245 | 0.000258 | 0.0002801 | 0.00028 | 0.0005009 |  |  |
| A5 | whole_capture_openssl | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 30000000 | 20 | 75.540 | 77.215 | 78.973 | 81.380 | 5.206 |  | SANITY FLAG |
| A5 | whole_capture_openssl_padded | OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI) | 30000000 | 20 | 76.524 | 78.273 | 78.944 | 82.049 | 2.553 |  |  |
| A5 | whole_capture_libsodium | libsodium crypto_hash_sha256 (portable C) | 30000000 | 20 | 110.6 | 120.9 | 124.4 | 141.9 | 16.208 |  |  |
| A1 | sha256_file_openssl | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 25000000 | 20 | 82.144 | 85.446 | 87.622 | 100.6 | 5.968 | 9.57 |  |
| A1 | sha256_file_openssl | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 30000000 | 20 | 100.1 | 106.2 | 111.0 | 130.9 | 13.504 | 9.91 |  |
| A1 | sha256_file_openssl | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 35000000 | 20 | 112.6 | 122.4 | 130.7 | 160.0 | 21.768 | 9.80 |  |
| A3 | ecies_layer1_token | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 82 | 2000 | 0.08044 | 0.08127 | 0.08957 | 0.1131 | 0.04375 |  |  |
| A3 | eciesb_layer2_credp | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 203 | 2000 | 0.08433 | 0.08505 | 0.09665 | 0.1308 | 0.03049 |  |  |
| A3 | eciesb_layer3_4_contp_49B | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 49 | 2000 | 0.08269 | 0.08317 | 0.09329 | 0.1189 | 0.07669 |  |  |
| A3 | eciesb_layer3_4_contp_81B | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 81 | 2000 | 0.08305 | 0.08504 | 0.1017 | 0.1513 | 0.04277 |  |  |
| A3 | eciesb_layer3_4_contp_113B | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 113 | 2000 | 0.08335 | 0.0922 | 0.1153 | 0.1728 | 0.1099 |  |  |
| A3 | eciesb_layer3_4_contp_300B_stress | ECIESb: 2 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 300 | 2000 | 0.08532 | 0.08596 | 0.0916 | 0.1159 | 0.01469 |  |  |
| A3 | ecies_layer5_wrap_credp | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 268 | 2000 | 0.08241 | 0.08415 | 0.09538 | 0.123 | 0.0916 |  |  |
| A3 | ecies_layer6_7_wrap_contp | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 146 | 2000 | 0.08109 | 0.08414 | 0.09363 | 0.1267 | 0.02557 |  |  |
| A3 | ecies_layer5_7_wrap_padded_460B | ECIES: 1 fixed-base + 1 variable-base X25519 + HKDF-SHA256 + AES-256-GCM; OpenSSL capabilities off | 460 | 2000 | 0.0845 | 0.086 | 0.09843 | 0.1296 | 0.06771 |  |  |
| A3 | hkdf_sha256_44B | OpenSSL EVP_KDF HKDF; OpenSSL capabilities off | 44 | 2000 | 0.004946 | 0.00503 | 0.007291 | 0.008715 | 0.0434 |  |  |
| A3 | aes256gcm_seal_203B | OpenSSL EVP AES-256-GCM; OpenSSL capabilities off | 203 | 2000 | 0.003088 | 0.003129 | 0.003954 | 0.004408 | 0.01351 |  |  |
| A3 | ecies_seven_layers | 3 ECIESb + 4 ECIES; OpenSSL capabilities off |  | 2000 | 0.5763 | 0.6192 | 0.6781 | 0.9777 | 0.2308 |  |  |
| A3 | ecies_seven_layers_padded | 3 ECIESb + 4 ECIES; OpenSSL capabilities off |  | 2000 | 0.5855 | 0.6427 | 0.711 | 0.961 | 0.2082 |  |  |
| A4 | h_metadata | OpenSSL EVP SHA256; OpenSSL capabilities off | 96 | 2000 | 0.000494 | 0.0005145 | 0.0005559 | 0.000532 | 0.001171 |  |  |
| A4 | fullpackethash | OpenSSL EVP SHA256; OpenSSL capabilities off | 81 | 2000 | 0.000496 | 0.000516 | 0.0005291 | 0.000532 | 0.0004345 |  |  |
| A4 | enc_fullpackethash | OpenSSL EVP AES-256-GCM; OpenSSL capabilities off | 32 | 2000 | 0.001008 | 0.001027 | 0.00108 | 0.001049 | 0.001013 |  |  |
| A4 | binding_hash | OpenSSL EVP SHA256; OpenSSL capabilities off | 48 | 2000 | 0.000285 | 0.000303 | 0.0003307 | 0.00032 | 0.0008686 |  |  |
| A5 | whole_capture_openssl | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 30000000 | 20 | 97.884 | 104.4 | 110.1 | 133.0 | 14.779 |  | SANITY FLAG |
| A5 | whole_capture_openssl_padded | OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0) | 30000000 | 20 | 100.2 | 106.1 | 115.6 | 154.7 | 21.495 |  |  |

Cycles per byte method: median time x clock frequency (/proc/cpuinfo cpu MHz, mean of before and after: 2800 MHz).

## Sanity checks

The whole capture contains the 30,000,000 B hash plus the other work, so its median should not be lower than the hash-only median from the same run.

- SANITY FLAG: default, whole_capture_openssl median 77.215 ms; sha256_file_openssl 30000000 B median 79.630 ms. The whole capture is lower. This points to variation between the two rows, such as a clock change or other load. Treat both rows with caution.
- SANITY FLAG: caps_off, whole_capture_openssl median 104.4 ms; sha256_file_openssl 30000000 B median 106.2 ms. The whole capture is lower. This points to variation between the two rows, such as a clock change or other load. Treat both rows with caution.
- ok: default, whole_capture_libsodium median 120.9 ms; sha256_file_libsodium 30000000 B median 113.5 ms.

## The papers' claims

Each comparison uses the median of the named row. The labels are "within range", "below range (faster than calculated)" and "above range (slower than calculated)".

- "2 to 10 ms for encryption" (Protocol paper; Integration section 8.1):
  - Row `ecies_seven_layers`, variant `default`, 3 ECIESb + 4 ECIES: median 0.5862 ms. Below range (faster than calculated).
- "430 to 600 ms for hashing a 30 MB file without hardware extensions" (Integration section 8.2):
  - Row `sha256_file_openssl`, 30,000,000 B, variant `default`, OpenSSL default (SIMD: AVX2, AVX or SSSE3; no SHA-NI): median 79.630 ms, 7.43 cycles/byte. Below range (faster than calculated).
  - Row `sha256_file_openssl`, 30,000,000 B, variant `caps_off`, OpenSSL capabilities off (scalar, OPENSSL_ia32cap=0x0:0x0): median 106.2 ms, 9.91 cycles/byte. Below range (faster than calculated).
  - Row `sha256_file_libsodium`, 30,000,000 B, variant `default`, libsodium crypto_hash_sha256 (portable C): median 113.5 ms, 10.59 cycles/byte. Below range (faster than calculated).
  - The calculation assumes 13.7 cycles/byte on a Cortex-A8 at 800 MHz. Cycles per byte do not depend on the clock and are the closer comparison.
- "120 to 170 ms with ARMv8 crypto extensions" (Integration section 8.2):
  - Not tested: the CPU feature list has no sha_ni, so no run used SHA extensions.

The papers' calculated figures are for their slowest hardware class, a Cortex-A8 at 800 MHz. This core (Intel(R) Xeon(R) Processor @ 2.80GHz) is faster than that class, so these results do not confirm the slowest-class figures.

DRY RUN, NOT PI. None of the numbers above is a Raspberry Pi measurement.

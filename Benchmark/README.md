# Benchmark

This folder measures two things on one machine.

- **Part A.** The device-side cost of one Birthmark capture: SHA-256 over a RAW-sized file, seven ECIES encryptions, and the small AES-256-GCM and SHA-256 operations around them.
- **Part B.** The cost of proving, in zero knowledge, knowledge of a message whose SHA-256 hash is public, at growing message sizes, on the same machine. The prover is Longfellow-zk.

The target machine is a **Raspberry Pi 4 Model B, 4 GB, Cortex-A72 at 1.5 GHz**, running Raspberry Pi OS 64-bit (aarch64). A Raspberry Pi 5 is also recognised. Any other machine is a dry run. Its output files carry `DRY_RUN_NOT_PI` in the file name and `DRY RUN, NOT PI` on the first line.

The papers state device cost as "calculated from published benchmarks". This folder replaces those calculations with measurements. Every number in `results/` is computed from a raw log in `results/raw/`.

Section and table numbers refer to the versions in `Docs/`: the Protocol paper v124, the Integration paper v41 and the Messaging Structure v119.

## Part A

### Build

First check what is installed. `check_prereqs.py` needs no root and installs nothing. It lists every missing command, library and package for Parts A and B, with the `apt install` line that someone with admin rights can run:

```
cd Benchmark
python3 check_prereqs.py
```

Part A needs `build-essential pkg-config libsodium-dev libssl-dev python3`. Then:

```
cd Benchmark/device
make
```

`make` builds `bench_capture` with `-O2`. `make native` builds `bench_capture_native` with `-O2 -march=native`. The driver uses `bench_capture`. The flags are compiled into the binary and recorded in every raw log.

### Run

```
cd Benchmark
python3 run_partA.py
```

Before you run it, let the Pi cool to idle and close other programs. Use a heatsink or fan if you have one.

The driver:

- runs the C program pinned to core 3 with `taskset -c 3`;
- reads `vcgencmd measure_temp`, `vcgencmd get_throttled` and `vcgencmd measure_clock arm` before and after each run, where `vcgencmd` is available.

sudo is optional. Run as root (`sudo python3 run_partA.py`), the driver also sets the cpufreq governor to `performance`, restores it afterwards, and hands the files it created back to your user. Without root, the governor is left unchanged, and the summary records which governor was in use.

The driver runs the C program twice:

| Variant | Environment | Rows |
|---|---|---|
| `default` | unchanged | A1 to A5 |
| `caps_off` | `OPENSSL_armcap=0` (aarch64) or `OPENSSL_ia32cap=0x0:0x0` (x86-64) | A1 (OpenSSL), A3, A4, A5 |

`caps_off` switches off every CPU capability OpenSSL detects: NEON, AES, PMULL and the SHA extensions. The summary reports whether that changed the 30,000,000 B hash time by more than 5%.

The options `--cpu`, `--binary`, `--no-governor` and the repeat counts are listed by `python3 run_partA.py --help`. The driver refuses repeat counts below the minimums: 20 for the file hash and the whole capture, and 2,000 for ECIES-scale rows.

`python3 summarize_partA.py RUN_ID` rebuilds the summary from the raw logs of an earlier run.

### Output

| File | Content |
|---|---|
| `results/raw/partA_<run_id>_default.jsonl` | Raw log of the `default` run. Line 1 is a header with the machine state before the run. Then come the C program's output lines, with every timing sample in nanoseconds. The last line is the machine state after the run. Opened in exclusive-create mode, so it is never overwritten. |
| `results/raw/partA_<run_id>_caps_off.jsonl` | Same, for `caps_off`. |
| `results/raw/partA_<run_id>_build_failed.txt` | Written only if `make` fails. |
| `results/partA_<date>_<host>.json` | Statistics for every row, with the machine, the runs, the self-tests and the claim checks. A second run on the same day gets a `_2` suffix. |
| `results/partA_summary.md` | One table row per measurement, and one line for each of the papers' three claims. Rebuilt on each Pi run. |

On a machine that is not a Pi, the names are `partA_DRY_RUN_NOT_PI_<date>_<host>.json` and `partA_summary_DRY_RUN_NOT_PI.md`, and `run_id` ends in `_DRY_RUN_NOT_PI`.

### Correctness tests

The C program runs these tests before timing anything. If any test fails, it prints the failure, exits with status 2 and times nothing. The raw log keeps the failure, and the summary reports no timing from that run.

- SHA-256 known-answer tests (FIPS 180-2 vectors and one million `a`), for both OpenSSL and libsodium. Both libraries must also give the same digest on the 35,000,000 B buffer.
- HKDF-SHA256, RFC 5869 test case 1.
- X25519, RFC 7748 section 6.1.
- AES-256-GCM, GCM specification test cases 13 and 14, a round trip on 203 B, and rejection of a modified ciphertext.
- Generator Point check. Each GP is accepted. The point u = 0 is rejected, and so is GP plus an order-2 point.
- ECIES overhead equals 49 B, the figure in Table A.1.
- One full capture, then decryption of all seven layers with the matching secret keys:
  - The first relays open layers 5 to 7 and check the routing code.
  - C, F and I open layers 2 to 4.
  - The validator opens T (layer 1).
  - C recomputes Enc_FullPacketHash, which must equal the device's bytes.
  - The validator's binding_hash check must pass.
  - F and I recompute FullPacketHash.
  - A wrong key must fail on every layer.
  - The test runs with unpadded wraps and again with padded wraps.

### What is measured

Each row is timed with `clock_gettime(CLOCK_MONOTONIC_RAW)`, one sample per operation, after a warm-up. The statistics are n, min, median, mean, p95 (nearest rank) and sample standard deviation, in milliseconds.

**A1. ContentHash = SHA-256(file).**
- A buffer of random bytes, already in RAM, of 25,000,000 B, 30,000,000 B and 35,000,000 B.
- 20 repeats after 2 warm-up runs.
- Two implementations: OpenSSL EVP in both variants, and libsodium `crypto_hash_sha256`, which is portable C.
- Cycles per byte are reported for these rows. The first choice is the CPU cycle counter, read through `perf_event_open`, user space only. If it is not available, the value is median time × the clock frequency read from `scaling_cur_freq` before and after the run. The summary states which method was used.

**A2. X25519 scalar multiplications (libsodium).**
- Variable-base: `crypto_scalarmult` with base GP = r·B.
- Fixed-base: `crypto_scalarmult_base`.
- The capture mix: 10 variable-base + 4 fixed-base in one sample.
- 2,000 repeats each.

**A3. ECIES encryptions.** 2,000 repeats each.
- ECIES (layers 1, 5, 6, 7):
  - EPK = e·B, which is one fixed-base multiplication.
  - The shared secret is e·pk, which is one variable-base multiplication.
- ECIESb (layers 2, 3, 4), to a Channel Key (GP, pk):
  - EPK = e·GP and the shared secret e·pk, which are two variable-base multiplications.
- Key derivation:
  - HKDF-SHA256, with ikm = shared secret, salt = EPK, and a fixed info string.
  - It outputs the 32 B AES-256-GCM key and the 12 B nonce.
  - The nonce is fresh on every call because e is fresh. It is not sent.
- Wire layout: version byte (1) ‖ EPK (32) ‖ ciphertext ‖ tag (16). The overhead is 49 B, which matches Table A.1.
- AAD is the version byte and EPK.

| Row | Layer | Plaintext |
|---|---|---:|
| `ecies_layer1_token` | 1, token T: Cred_HW 32 + replay_nonce 16 + claim 2 + binding_hash 32 | 82 B |
| `eciesb_layer2_credp` | 2, CredP: T (131) + key_ref 8 + FullPacketHash 32 + BlindShare_key 32 | 203 B |
| `eciesb_layer3_4_contp_49B` | 3 and 4, ContP: flags + ContentHash + n | 49 B |
| `eciesb_layer3_4_contp_81B` | 3 and 4, ContP with h(metadata) | 81 B |
| `eciesb_layer3_4_contp_113B` | 3 and 4, ContP with h(metadata) and parent ContentHash | 113 B |
| `eciesb_layer3_4_contp_300B_stress` | 3 and 4, a stress case larger than the spec allows | 300 B |
| `ecies_layer5_wrap_credp` | 5, routing code 16 + CredP (252) | 268 B |
| `ecies_layer6_7_wrap_contp` | 6 and 7, routing code 16 + ContP (81 + 49) | 146 B |
| `ecies_layer5_7_wrap_padded_460B` | 5 to 7, padded to the upper end of Table A.2's 420 to 460 B | 460 B |
| `ecies_seven_layers` | All seven layers in spec order, unpadded wraps, ContP at 81 B | |
| `ecies_seven_layers_padded` | The same, wraps padded to 460 B | |

`hkdf_sha256_44B` and `aes256gcm_seal_203B` time the two symmetric parts of one ECIES call on their own.

All sizes are named constants in `device/sizes.h`.

**A4. Small operations.** 2,000 repeats each.
- `h_metadata`: SHA-256 over three 32 B commitments.
- `fullpackethash`: SHA-256(ContentHash ‖ n ‖ flags ‖ h(metadata)), 81 B.
- `enc_fullpackethash`: AES-256-GCM(BlindShare_key; FullPacketHash) with a fixed all-zero nonce, 32 B in and 48 B out.
- `binding_hash`: SHA-256(Enc_FullPacketHash), 48 B.

**A5. Whole capture.**
- Starts from a 30,000,000 B buffer in RAM. Builds every value in the order of the Messaging Structure (v119), "Device-side construction", steps 1 to 9:
  - ContentHash;
  - n and h(metadata), then FullPacketHash;
  - replay_nonce, BlindShare_key, Enc_FullPacketHash and binding_hash;
  - T, CredP, ContP_F and ContP_I;
  - the three first-relay wraps.
- The time includes generating the random values.
- 20 repeats after 2 warm-up runs.
- Rows:
  - `whole_capture_openssl`: ContentHash by OpenSSL.
  - `whole_capture_openssl_padded`: the same, with wraps padded to 460 B.
  - `whole_capture_libsodium`: ContentHash by libsodium.

### Code paths

Each SHA-256 row names its code path. The labels follow OpenSSL 3.0's own dispatch:

- On aarch64 (`crypto/sha/asm/sha512-armv8.pl`), OpenSSL uses the SHA extensions if present, else NEON, else scalar code.
- On x86-64 (`sha256-x86_64.pl`), it uses SHA-NI if present, else AVX2, AVX or SSSE3, else scalar code.

The label depends on the CPU feature list and the variant:

| CPU | `default` | `caps_off` |
|---|---|---|
| Pi 4 (`asimd`, no `sha2`) | OpenSSL default (NEON, no SHA extensions) | OpenSSL capabilities off (scalar, OPENSSL_armcap=0) |
| CPU with `sha2` (e.g. Pi 5) | OpenSSL default (ARMv8 SHA extensions) | OpenSSL capabilities off (scalar, OPENSSL_armcap=0) |

The libsodium rows are labelled "libsodium crypto_hash_sha256 (portable C)".

### Sanity check

The whole capture contains the 30,000,000 B hash. Its median should therefore not be lower than the hash-only median from the same run.

The summary compares these pairs:

- `whole_capture_openssl` against `sha256_file_openssl` at 30,000,000 B, in each variant;
- `whole_capture_libsodium` against `sha256_file_libsodium`.

If the whole capture is lower, the summary prints SANITY FLAG and marks the row.

### The papers' claims

The summary checks three claims against measured medians. Each claim line names the row, the variant and the code path it uses.

| Claim | Source | Compared rows |
|---|---|---|
| "2 to 10 ms for encryption" | Protocol paper; Integration §8.1 | `ecies_seven_layers`, variant `default` |
| "430 to 600 ms for hashing a 30 MB file without hardware extensions" | Integration §8.2 | At 30,000,000 B: `sha256_file_openssl` in `default` (only if the CPU has no SHA extensions); `sha256_file_openssl` in `caps_off`; `sha256_file_libsodium` in `default` |
| "120 to 170 ms with ARMv8 crypto extensions" | Integration §8.2 | `sha256_file_openssl` at 30,000,000 B in `default`, only if the CPU has `sha2` |

Each comparison gets one of three labels: "within range", "below range (faster than calculated)" or "above range (slower than calculated)".

The papers' figures are calculated for their slowest hardware class, a Cortex-A8 at 800 MHz. The summary states that the core measured here is faster than that class, so it does not confirm the slowest-class figures.

The Pi 4's Cortex-A72 has no ARMv8 SHA extensions. On the Pi 4 the third claim is reported as not tested, with the reason.

### What is not measured

- Reading the file from storage. The buffer is already in RAM.
- The camera sensor, the ISP and writing the file.
- Computing Cred_HW (the NUC map hash) and the three metadata commitments. The commitments are random stand-ins; only h(metadata) over them is timed.
- Padding to a random size, holds and transmission.
- Anything that happens after the device: relays, C, the validator, gatekeepers, F, I and the registry. The decrypt steps run only as correctness tests and are not timed.
- Energy use.

### Limitations

- **One machine.** The results describe one Raspberry Pi 4 Model B.
- **Core class.** The papers' figures are calculated for a Cortex-A8, an in-order core at 800 MHz. The Cortex-A72 is out of order and runs at 1.5 GHz. These results do not show what a Cortex-A8 would measure.
- **Clock.** The Cortex-A72 is named here at 1.5 GHz. Some Pi 4 boards run at 1.8 GHz. The summary records the maximum frequency the board reports and notes any difference.
- **No SHA extensions on the Pi 4.** The claim for ARMv8 crypto extensions cannot be tested on this board.
- **KDF.** HKDF-SHA256 is a placeholder. The papers say the key-derivation function is not yet specified. The HKDF call is timed as its own row.
- **Sizes.** Several field sizes are estimates in Table A.1 (Cred_HW, key_ref, claim). They are approximate. The 300 B ContP is outside the spec.
- **replay_nonce.** Integration v41 defines it as a 15-bit UTC day count, an offline bit and 14 random bytes. The benchmark fills its 16 bytes with random bytes. The size, and so the encryption cost, is the same.
- **Padding.** The format is not specified. Padded wraps use zero bytes.
- **Subgroup check.** The spec checks ℓ·GP with an unclamped multiplication. This code instead converts GP to Edwards form and calls libsodium's `crypto_core_ed25519_is_valid_point`, which includes the prime-order subgroup check. The check runs at setup and is not timed.
- **Libraries.** The results depend on the installed libsodium and OpenSSL versions. Both are recorded in every raw log.

## Part B

Part B measures the time and memory to prove, in zero knowledge, knowledge of a message M such that SHA-256(M) = H, with H public. The prover is Longfellow-zk at commit `8861765fbbfaca7a452da60f8ceb8c6de8e4a003`. `zk/CANDIDATES.md` records why it was chosen. Hekate is attempted separately and is not part of the steps below.

### The statement and the circuit

`zk/longfellow/sha256_zk_bench.cc` builds its own circuit from Longfellow's SHA-256 block circuit:

- H is a public input. The message bytes and the per-block witnesses are private inputs.
- The length of M is fixed by the circuit, as in Hekate's statement. The padding bytes are circuit constants.
- Every block is chained to the next. There is no limit on the number of blocks.

Longfellow's own SHA-256 benchmark does not prove this statement. It marks no input public, so H is private there. Its variable-length API also stores the block count in 8 bits, which stops it at 255 blocks.

Zero-knowledge is on in every proof. The Ligero parameters are rate 7 and 132 queries. Longfellow's source states these as about 109 bits of statistical security, and its version-7 mdoc proofs use them.

Two fields are available. `gf2_128` is GF(2^128). `fp64_2` is the quadratic extension of the 64-bit Goldilocks prime.

### Build

Part B needs `build-essential clang cmake git libssl-dev libzstd-dev libgtest-dev libbenchmark-dev zlib1g-dev`, and optionally `time`. Installing them needs admin rights; `python3 check_prereqs.py` lists what is missing. The build itself needs no root:

```
cd Benchmark
zk/longfellow/fetch_and_build.sh
```

clang is required on aarch64. Longfellow's add-with-carry helpers in `lib/algebra/sysdep.h` exist only for x86 and for clang, so the script stops with a message if clang is missing.

The script clones Longfellow at the pinned commit into `zk/build/`, which is git-ignored. On every run it starts from the pinned tree.

On an aarch64 CPU without `pmull` (the Pi 4), Longfellow's default build would execute PMULL and stop with an illegal instruction. The script then makes two changes, records them in `zk/build/longfellow_build_changes.diff`, and copies the diff into every raw log:

1. `lib/CMakeLists.txt`: `-march=armv8-a+crypto` becomes `-march=armv8-a`.
2. `lib/gf2k/sysdep.h`: the PMULL branch is taken only when the compiler defines `__ARM_FEATURE_AES`, so GF(2^128) uses Longfellow's own NEON code.

Afterwards the script counts crypto-extension instructions in the binary (64-bit PMULL, AES, SHA) and fails if any are present. The 8-bit PMULL form that the NEON code uses is base NEON and is not counted.

`LONGFELLOW_WIDE_LABELS=1` makes one more change: the circuit file format stores wire labels in 4 bytes, not 3. Longfellow aborts when saving a circuit with a label of 2^24 or more, which happens for the SHA-256 circuit at 16 KiB. This changes the file format only, not the proof. Circuits must be saved and loaded by builds with the same setting.

### Swap

Building a circuit needs far more memory than proving with it. In the x86 dry run `20261026T220750Z_vm_DRY_RUN_NOT_PI`, the 4 KiB GF(2^128) circuit peaked at 2,158 MiB to build and 234 MiB to prove. An earlier exploratory dry run, whose output was not kept in raw logs, peaked at about 8.3 GiB to build the 16 KiB circuit.

For every run of every phase, the driver records swap activity: the change in pages swapped in and out (`/proc/vmstat`), and the most swap in use, sampled every 0.5 s.

- **Setup.** Swap may be on. A setup during which any page was swapped in or out is labelled "setup with swap, not comparable". A setup with swap on but no page swapped is labelled "swap on, no pages swapped".
- **Prove.** Swap must be off. The driver refuses to start while `/proc/swaps` lists any swap.
- **Without sudo**, swap cannot be turned off. `--allow-active-swap` lets the prove phase run with swap on. Any run during which a page is swapped in or out then counts as failed, and the Limitations section says the flag was used.

Adding or removing swap needs sudo. To add temporary swap and remove it afterwards (the file name is an example):

```
sudo fallocate -l 4G /swapfile-partB && sudo chmod 600 /swapfile-partB
sudo mkswap /swapfile-partB && sudo swapon /swapfile-partB
# ... setup phase ...
sudo swapoff -a
```

`sudo swapoff -a` turns off all swap, including Raspberry Pi OS's default swap file.

### Run

A run has three phases. `setup` prints a run id, which the other two take.

```
cd Benchmark
python3 run_partB.py setup --fields gf2_128 fp64_2 --sizes 1024 4096
sudo swapoff -a     # with sudo; without it, add --allow-active-swap to the prove line
python3 run_partB.py prove --run-id RUN_ID --fields gf2_128 fp64_2 --sizes 1024 4096
python3 run_partB.py hash  --run-id RUN_ID --sizes 1024 4096
python3 summarize_partB.py RUN_ID
```

sudo is optional here too. Run as root, the prove and hash phases set the `performance` governor and restore it afterwards. Peak memory comes from GNU `time -v` where it is installed, otherwise from the `wait4` resource usage of the process. Each raw log names the method used.

| Phase | What it does |
|---|---|
| `setup` | Builds each circuit and saves it to `zk/build/circuits/`. Stops a field at its first failure. |
| `prove` | Loads each circuit and proves `--repeats` times in one process: at least 5 up to 1 MiB, at least 1 above. The process is pinned to one core, runs under `/usr/bin/time -v`, and has a timeout of 45 minutes per repeat. Before each size, it predicts peak memory and prove time from the sizes already measured. It stops when the prediction is over 80% of RAM or over 30 minutes, and records the reason. |
| `hash` | Plain SHA-256 of M at each size, and at 30,000,000 B, with the Part A code: OpenSSL default, OpenSSL with capabilities off, and libsodium. |

`--sizes ladder` means 1 KiB, 4 KiB, 16 KiB, 64 KiB, 130,944 B, 256 KiB, then 1 MiB and up by powers of 4. 130,944 B (2,047 compressions) approximates the byte count behind the vendor's "127.9 KiB" figure, which is not published.

Each proof run also checks three things on its first repeat:

- the honest proof verifies;
- a copy of the proof with one flipped byte is rejected;
- the honest proof is rejected against a wrong H.

Each check runs in a child process, because Longfellow aborts on some malformed inputs. A run that fails any check is recorded as a failure.

`summarize_partB.py RUN_ID [--field gf2_128|fp64_2]` chooses the field for the comparison. Without `--field` it uses the field with the most measured sizes; on a tie, the faster one at the largest common size.

### Output

| File | Content |
|---|---|
| `results/raw/partB_<run_id>_setup_<field>_<bytes>.jsonl` | One circuit build: header (machine, swap state, build changes), the driver's output, `/usr/bin/time -v` fields, the circuit file's SHA-256 |
| `results/raw/partB_<run_id>_prove_<field>_<bytes>.jsonl` | One prove process: every repeat's times, proof size and checks |
| `results/raw/partB_<run_id>_prove_<field>_<bytes>_stopped.json` | Why the sweep stopped before this size |
| `results/raw/partB_<run_id>_hash_<variant>_<small or large>.jsonl` | Plain-hash rows |
| `results/raw/partB_crossarch_*.jsonl` | The cross-architecture check, below |
| `results/partB_<date>_<host>.json` | Everything the summary uses |
| `results/partB_summary.md` | Setup table, measured prove table, field pilot, where the sweep stopped, plain-hash table, ratio table, extrapolation table |
| `results/comparison.md` | One table (input size; hash time with SHA extensions; hash time without; prover time; prover peak memory; ratio), then Limitations |

Dry-run file names carry `DRY_RUN_NOT_PI`.

### Extrapolation

The summary fits a power law in log-log space to the measured prove times and peak memory of one field, and reports the fit and R². It also gives the linear per-compression scaling from the largest measured point. Both are labelled EXTRAPOLATED wherever they appear, and no table column mixes them with measured values. With only two measured points, R² is 1 by construction, and the summary says so.

### Cross-architecture check

`python3 zk/longfellow/cross_arch_check.py` runs on an x86-64 host. It needs clang, lld, qemu-user and the arm64 development packages. First run `zk/longfellow/fetch_and_build.sh`, then the same with `CROSS_AARCH64=1`. For each field it checks that:

- the circuit built on x86-64 and the one built on aarch64 (QEMU, `-cpu cortex-a72`) are byte-identical and have the same circuit id;
- aarch64 proves with the x86-64 circuit and passes all checks;
- each architecture verifies the other's proof, and rejects a copy with one flipped byte.

Timings under QEMU are emulated and are not results.

### A defect found in Longfellow's own benchmark

`BM_ShaZK_Fp64_2` in `lib/circuits/sha/flatsha256_circuit_test.cc` passes the Goldilocks root 2752994695033296049 as a root of unity of order 2^32. Its order is 2^29. Longfellow's `lib/algebra/reed_solomon_test.cc` uses the same root with order 2^29. With order 2^32, the honest proof is rejected. The benchmark never runs the verifier, so the defect does not show there. This driver uses order 2^29.

### What is not measured

- Hekate. It is attempted separately and reported on its own.
- PMULL on the Pi 4. The board has none, so the GF(2^128) slowdown from the NEON fallback cannot be measured on it.
- Setup time without swap, for any size whose circuit build needs more memory than the Pi has.
- Message sizes beyond the stop rules.


## Licence

The source files in this folder carry an Apache-2.0 header. See `LICENSING.md` at the repository root.

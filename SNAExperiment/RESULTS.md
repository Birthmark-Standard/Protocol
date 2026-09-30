# Results

The question is whether a single compromised component can take a public registry record and name the device that produced it. A device submission is one capture's first-hop packets. Each vantage is compared with chance and with a passive observer (the baseline) on the same records.

- 200 runs per cell, 58 cells (11 no-decoy, 46 decoy, 1 sensitivity control): 11,600 runs.
- Every cell met the stability rule (at least 50 device-level successes and 50 failures), so every number below is reported as a finding.
- Intervals are 95% and resample whole runs.
- The primary measure is device-level accuracy of the per-decision attack. The submission level is secondary.
- Full tables: `results/tables.md` and `results/summary.csv`. Analysis plan: `ANALYSIS_PLAN.md`.

## Summary

1. **The validator is the one component whose compromise defeats the decoys.**
   - At the deployment volumes it names the device behind a record 89.5% of the time at R = 1 and 53.5% at R = 4. Those figures are the same at every decoy volume, identical to the last digit.
   - The baseline on the same records falls to 0.96% (R = 1) and 0.88% (R = 4) at T = 500. So the validator's contribution there is +88.5 and +52.6 points.
   - The mechanism: the validator issues the real/dummy indicator, so it knows which credentials are disposable. Decoy traffic never enters its candidate list, and each of its replies already carries a device identity.
2. **Decoys protect against every other vantage.** For the baseline, both first hops, the credential processor, the content server and the gatekeeper, device accuracy at fixed T is nearly the same whatever R is. At T = 500 all of them are between 0.87% and 1.29%, for R from 1 to 40.
3. **The gatekeeper and the credential processor add nothing over the passive observer.**
   - Their device-level contribution lies within ±0.4 points at every L, and within ±0.2 points from L = 8 up.
   - Their exact knowledge (their own postings, their own fan-out) sits on the record-to-transaction half of the path. The transaction-to-device half is the same timing problem the baseline faces.
4. **The first hops name the exact capture well above chance.** They know the source address and their own hold.
   - Credential first hop at L = 40: 13.7% of submissions right, against 1/L = 2.5% and the baseline's 5.5%.
   - Their submission-level lift rises with volume, from 5.5 at L = 40 to 13.2 at L = 500 (slope 0.357 [0.351, 0.362]).
   - At the device level their contribution is smaller: +1.1 points at L = 40.
5. **The content server adds a moderate amount:** +4.9 device-level points at L = 4, +0.9 at L = 40 and +0.1 at L = 500.
6. **The passive observer alone beats chance.**
   - Its device accuracy is 4.2 times the random-assignment rate at L = 40 and 6.1 times at L = 500.
   - Its submission accuracy is about 2.2 times 1/L from L = 8 to 500.
   - Every vantage, the baseline included, is above the random-assignment rate in every cell of both sweeps.
7. **Confidence does not let an attacker pick out its right answers at useful volume.** From L = 24 up, no vantage keeps precision above 50% on more than 0.05% of its decisions. At L = 1 to 4, the high coverages reflect accuracy itself being above 50%.

## Pre-run checks

Run with background traffic on, at R = 8 and T = 40 over 12 runs (`results/checks.json`, `results/checks.log`).

| Check | Outcome |
|---|---|
| Padding classes | Pass. 12,614 legs, none outside its class; every raw payload fits; Ring V signature 64 B with real keys, verifies. |
| Answer extraction | Pass. 340 of 340 registry submissions. 2,703 of 2,703 device and decoy first-hop packets; no background packet among the candidates. 80.5% of submission groups hold a single capture. |
| Background independence | Pass. Every vantage's and the baseline's decisions identical with background traffic on and off. |
| Cannot tell decoys: baseline | Pass. 19 features; largest deviation Cred-2 size, AUC 0.511 [0.496, 0.526]. |
| Cannot tell decoys: first hop, credential | Pass. Largest A's hold, AUC 0.490 [0.470, 0.510]. |
| Cannot tell decoys: first hop, content | Pass. Largest time since the source's previous capture, AUC 0.496 [0.470, 0.521]. |
| Cannot tell decoys: content server, before its timeout | Pass. Largest content last-leg size, AUC 0.495 [0.483, 0.508]. |
| Content server after its 30-minute timeout | Fail, as scoped. Quorum within 30 minutes separates real from decoy perfectly (AUC 1.000). |
| Can tell decoys: validator, credential processor, gatekeeper | Pass. Quorum never forms for a decoy and always forms for a real transaction; the gatekeeper's substitute posting keeps the real schedule (AUC 0.497). |

Padding-class scaling note: the gatekeeper fan-out leg's raw size is 689 B plus the Ring V signature, 32 (n + 1) B for n validators. It fits the 820 to 860 B class for n up to 3 (817 B), exceeds the class minimum at n = 4 (849 B) and exceeds the class maximum from n = 5 (881 B).

## No-decoy sweep

### Device-level accuracy

| Vantage | L = 1 | L = 2 | L = 3 | L = 4 | L = 8 | L = 24 | L = 40 | L = 50 | L = 100 | L = 200 | L = 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Random device (baseline rows) | 70.68% | 41.15% | 28.00% | 21.21% | 10.88% | 3.58% | 2.15% | 1.72% | 0.86% | 0.43% | 0.17% |
| Baseline | 87.71% | 69.59% | 57.30% | 48.89% | 31.42% | 13.53% | 8.97% | 7.54% | 4.22% | 2.33% | 1.05% |
| First hop, credential | 88.58% | 71.81% | 59.88% | 51.70% | 34.46% | 15.32% | 10.11% | 8.49% | 4.86% | 2.74% | 1.21% |
| First hop, content | 87.91% | 70.15% | 58.34% | 50.12% | 33.07% | 14.59% | 9.65% | 8.03% | 4.60% | 2.58% | 1.15% |
| Credential processor | 87.53% | 69.38% | 57.07% | 48.71% | 31.35% | 13.53% | 8.99% | 7.53% | 4.21% | 2.33% | 1.04% |
| Content server | 89.79% | 73.81% | 62.03% | 53.73% | 34.93% | 14.93% | 9.91% | 8.28% | 4.68% | 2.60% | 1.16% |
| Validator | 89.49% | 73.48% | 61.75% | 53.50% | 34.86% | 15.10% | 10.17% | 8.46% | 4.75% | 2.63% | 1.20% |
| Gatekeeper | 87.81% | 69.98% | 57.57% | 49.08% | 31.33% | 13.42% | 9.01% | 7.49% | 4.22% | 2.32% | 1.05% |

The random-assignment rate is one over the devices with a feasible submission, when the record's device is among them. It is below 1/L at large L because a record's feasible window holds more than L captures from more than L devices.

### Device-level contribution over the baseline (percentage points)

| Vantage | L = 1 | L = 2 | L = 3 | L = 4 | L = 8 | L = 24 | L = 40 | L = 50 | L = 100 | L = 200 | L = 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| First hop, credential | +0.87 [+0.70, +1.04] | +2.22 [+1.99, +2.44] | +2.58 [+2.29, +2.87] | +2.81 [+2.53, +3.10] | +3.04 [+2.76, +3.30] | +1.79 [+1.65, +1.94] | +1.14 [+1.04, +1.23] | +0.95 [+0.87, +1.02] | +0.65 [+0.60, +0.70] | +0.41 [+0.39, +0.44] | +0.16 [+0.15, +0.17] |
| First hop, content | +0.20 [+0.07, +0.34] | +0.56 [+0.37, +0.77] | +1.04 [+0.80, +1.28] | +1.24 [+0.99, +1.49] | +1.64 [+1.42, +1.87] | +1.06 [+0.95, +1.18] | +0.68 [+0.60, +0.76] | +0.49 [+0.43, +0.56] | +0.38 [+0.34, +0.42] | +0.26 [+0.24, +0.28] | +0.10 [+0.09, +0.11] |
| Credential processor | -0.18 [-0.29, -0.08] | -0.21 [-0.37, -0.06] | -0.23 [-0.39, -0.07] | -0.17 [-0.35, -0.01] | -0.07 [-0.23, +0.10] | +0.01 [-0.05, +0.07] | +0.01 [-0.02, +0.05] | -0.01 [-0.04, +0.02] | -0.00 [-0.02, +0.01] | +0.00 [-0.01, +0.01] | -0.00 [-0.00, -0.00] |
| Content server | +2.08 [+1.86, +2.28] | +4.22 [+3.88, +4.55] | +4.73 [+4.38, +5.05] | +4.85 [+4.43, +5.25] | +3.51 [+3.13, +3.86] | +1.40 [+1.21, +1.60] | +0.94 [+0.83, +1.04] | +0.73 [+0.64, +0.84] | +0.46 [+0.41, +0.52] | +0.27 [+0.24, +0.30] | +0.11 [+0.10, +0.12] |
| Validator | +1.78 [+1.47, +2.07] | +3.89 [+3.45, +4.34] | +4.45 [+3.92, +4.98] | +4.61 [+4.06, +5.12] | +3.43 [+2.98, +3.92] | +1.58 [+1.35, +1.79] | +1.20 [+1.05, +1.34] | +0.92 [+0.79, +1.04] | +0.53 [+0.46, +0.60] | +0.31 [+0.27, +0.34] | +0.15 [+0.13, +0.17] |
| Gatekeeper | +0.10 [-0.05, +0.26] | +0.39 [+0.18, +0.61] | +0.27 [+0.01, +0.54] | +0.19 [-0.09, +0.46] | -0.10 [-0.31, +0.14] | -0.10 [-0.19, -0.01] | +0.04 [-0.02, +0.09] | -0.05 [-0.10, -0.00] | +0.00 [-0.02, +0.03] | -0.01 [-0.02, +0.01] | +0.00 [-0.00, +0.00] |

The credential processor is slightly below the baseline at L = 1 to 4 (-0.17 to -0.23 points). Its likelihood nests the baseline's, so this is estimation error in its 2D model, and it is small.

### Submission-level accuracy

| Vantage | L = 1 | L = 2 | L = 3 | L = 4 | L = 8 | L = 24 | L = 40 | L = 50 | L = 100 | L = 200 | L = 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1/L | 100.00% | 50.00% | 33.33% | 25.00% | 12.50% | 4.17% | 2.50% | 2.00% | 1.00% | 0.50% | 0.20% |
| Baseline | 80.94% | 63.00% | 51.18% | 43.24% | 25.70% | 9.20% | 5.54% | 4.36% | 2.19% | 1.12% | 0.46% |
| First hop, credential | 82.39% | 66.32% | 55.01% | 47.52% | 31.99% | 17.52% | 13.74% | 12.51% | 8.69% | 5.74% | 2.65% |
| First hop, content | 81.41% | 64.16% | 53.20% | 45.72% | 30.30% | 16.42% | 12.85% | 11.53% | 8.18% | 5.38% | 2.56% |
| Credential processor | 80.65% | 62.75% | 50.87% | 43.13% | 25.54% | 9.11% | 5.52% | 4.36% | 2.19% | 1.13% | 0.45% |
| Content server | 85.30% | 69.43% | 57.61% | 49.46% | 30.47% | 11.09% | 6.71% | 5.47% | 2.73% | 1.39% | 0.55% |
| Validator | 78.01% | 62.95% | 52.12% | 44.24% | 26.17% | 9.35% | 5.74% | 4.59% | 2.31% | 1.21% | 0.50% |
| Gatekeeper | 81.21% | 63.54% | 51.26% | 43.10% | 25.51% | 9.09% | 5.60% | 4.37% | 2.19% | 1.12% | 0.45% |

### Submission-level contribution over the baseline (percentage points)

| Vantage | L = 1 | L = 2 | L = 3 | L = 4 | L = 8 | L = 24 | L = 40 | L = 50 | L = 100 | L = 200 | L = 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| First hop, credential | +1.45 [+1.23, +1.66] | +3.32 [+3.04, +3.61] | +3.84 [+3.49, +4.18] | +4.28 [+3.92, +4.65] | +6.30 [+5.92, +6.67] | +8.32 [+8.04, +8.61] | +8.20 [+8.01, +8.38] | +8.15 [+8.00, +8.29] | +6.50 [+6.41, +6.60] | +4.63 [+4.57, +4.68] | +2.19 [+2.17, +2.22] |
| First hop, content | +0.47 [+0.30, +0.62] | +1.16 [+0.92, +1.42] | +2.02 [+1.74, +2.29] | +2.48 [+2.17, +2.78] | +4.60 [+4.30, +4.91] | +7.22 [+7.01, +7.43] | +7.32 [+7.19, +7.44] | +7.17 [+7.06, +7.29] | +5.99 [+5.91, +6.07] | +4.26 [+4.22, +4.30] | +2.10 [+2.08, +2.12] |
| Credential processor | -0.30 [-0.42, -0.18] | -0.25 [-0.40, -0.09] | -0.30 [-0.47, -0.14] | -0.12 [-0.28, +0.04] | -0.16 [-0.35, +0.01] | -0.09 [-0.21, +0.03] | -0.02 [-0.08, +0.05] | +0.00 [-0.05, +0.05] | +0.01 [-0.02, +0.03] | +0.01 [-0.01, +0.02] | -0.00 [-0.01, +0.00] |
| Content server | +4.36 [+4.07, +4.65] | +6.43 [+6.02, +6.80] | +6.43 [+6.02, +6.85] | +6.22 [+5.76, +6.64] | +4.77 [+4.36, +5.17] | +1.89 [+1.66, +2.13] | +1.17 [+1.04, +1.31] | +1.11 [+0.99, +1.24] | +0.54 [+0.48, +0.59] | +0.27 [+0.24, +0.30] | +0.09 [+0.08, +0.11] |
| Validator | -2.93 [-3.42, -2.46] | -0.05 [-0.68, +0.59] | +0.94 [+0.33, +1.52] | +1.00 [+0.36, +1.59] | +0.48 [-0.09, +1.01] | +0.16 [-0.10, +0.40] | +0.20 [+0.05, +0.36] | +0.23 [+0.10, +0.37] | +0.12 [+0.05, +0.18] | +0.09 [+0.06, +0.13] | +0.04 [+0.03, +0.06] |
| Gatekeeper | +0.27 [+0.06, +0.48] | +0.54 [+0.25, +0.83] | +0.08 [-0.24, +0.39] | -0.14 [-0.45, +0.17] | -0.19 [-0.47, +0.10] | -0.10 [-0.25, +0.05] | +0.06 [-0.02, +0.15] | +0.01 [-0.06, +0.09] | +0.00 [-0.04, +0.04] | -0.00 [-0.02, +0.02] | -0.01 [-0.02, -0.00] |

The validator's submission-level contribution is negative at L = 1 (-2.9 points). Its candidates are its own replies, one per transaction. The baseline's candidates are packet groups, and a group counts as right if any member belongs to the record's capture. The two submission-level measures are therefore not the same test for this one vantage. Its device-level result is the comparable one.

### Lift from L = 40 to 500

| Vantage | Device lift (vs random) at 40 / 500 | Slope [95% CI] | Direction | Submission lift (x L) at 40 / 500 | Slope [95% CI] | Direction |
|---|---|---|---|---|---|---|
| Baseline | 4.17 / 6.07 | 0.148 [0.142, 0.154] | rises | 2.22 / 2.28 | 0.014 [0.003, 0.025] | rises |
| First hop, credential | 4.69 / 7.01 | 0.161 [0.156, 0.167] | rises | 5.50 / 13.24 | 0.357 [0.351, 0.362] | rises |
| First hop, content | 4.48 / 6.65 | 0.160 [0.155, 0.165] | rises | 5.14 / 12.79 | 0.370 [0.366, 0.375] | rises |
| Credential processor | 4.17 / 6.06 | 0.147 [0.141, 0.153] | rises | 2.21 / 2.26 | 0.013 [0.002, 0.025] | rises |
| Content server | 3.91 / 5.70 | 0.150 [0.145, 0.155] | rises | 2.68 / 2.75 | 0.008 [0.001, 0.015] | rises |
| Validator | 3.98 / 5.86 | 0.153 [0.148, 0.159] | rises | 2.29 / 2.49 | 0.035 [0.025, 0.045] | rises |
| Gatekeeper | 4.18 / 6.07 | 0.148 [0.142, 0.153] | rises | 2.24 / 2.23 | 0.003 [-0.005, 0.011] | holds flat |

At the device level every vantage's lift rises at the same rate as the baseline's (slopes 0.147 to 0.161). That is a property of the random-assignment reference, not of any compromise: the feasible window's device count grows faster than the number of devices that can plausibly match. At the submission level only the first hops rise steeply. The gatekeeper holds flat, and the others rise slightly.

Figure: `results/figures/lift_vs_L_nodecoy.png`.

## Decoy sweep

Device-level accuracy by real volume R (rows) and total volume T (columns). Every other vantage's table is in `results/tables.md`.

**Baseline**

| R \ T | 1 | 2 | 3 | 4 | 8 | 24 | 40 | 50 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 87.71% |  |  | 48.82% | 30.14% | 13.36% | 8.80% | 7.38% | 4.05% | 2.21% | 0.96% |
| 2 |  | 69.59% |  | 49.02% | 30.82% | 13.01% | 8.66% | 7.20% | 4.04% | 2.23% | 1.03% |
| 3 |  |  | 57.30% | 49.11% | 30.71% | 12.87% | 8.50% | 7.19% | 4.00% | 2.13% | 0.95% |
| 4 |  |  |  | 48.89% | 30.51% | 12.78% | 8.68% | 7.14% | 3.72% | 2.03% | 0.88% |
| 8 |  |  |  |  | 31.42% | 13.84% | 9.30% | 7.78% | 4.34% | 2.48% | 1.10% |
| 24 |  |  |  |  |  | 13.53% | 9.03% | 7.63% | 4.10% | 2.32% | 1.11% |
| 40 |  |  |  |  |  |  | 8.97% | 7.46% | 4.14% | 2.30% | 1.01% |

**Validator** (identical across T at every R, to the last digit)

| R \ T | 1 | 2 | 3 | 4 | 8 | 24 | 40 | 50 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 89.49% |  |  | 89.49% | 89.49% | 89.49% | 89.49% | 89.49% | 89.49% | 89.49% | 89.49% |
| 2 |  | 73.48% |  | 73.48% | 73.48% | 73.48% | 73.48% | 73.48% | 73.48% | 73.48% | 73.48% |
| 3 |  |  | 61.75% | 61.75% | 61.75% | 61.75% | 61.75% | 61.75% | 61.75% | 61.75% | 61.75% |
| 4 |  |  |  | 53.50% | 53.50% | 53.50% | 53.50% | 53.50% | 53.50% | 53.50% | 53.50% |
| 8 |  |  |  |  | 34.86% | 34.86% | 34.86% | 34.86% | 34.86% | 34.86% | 34.86% |
| 24 |  |  |  |  |  | 15.10% | 15.10% | 15.10% | 15.10% | 15.10% | 15.10% |
| 40 |  |  |  |  |  |  | 10.17% | 10.17% | 10.17% | 10.17% | 10.17% |

**Gatekeeper**

| R \ T | 1 | 2 | 3 | 4 | 8 | 24 | 40 | 50 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 87.81% |  |  | 49.04% | 30.38% | 13.30% | 8.85% | 7.33% | 3.98% | 2.21% | 0.96% |
| 2 |  | 69.98% |  | 49.09% | 30.91% | 13.00% | 8.64% | 7.10% | 3.91% | 2.18% | 0.98% |
| 3 |  |  | 57.57% | 49.20% | 30.64% | 12.80% | 8.40% | 7.10% | 3.90% | 2.12% | 0.93% |
| 4 |  |  |  | 49.08% | 30.55% | 12.74% | 8.60% | 6.94% | 3.76% | 2.02% | 0.87% |
| 8 |  |  |  |  | 31.33% | 13.82% | 9.28% | 7.67% | 4.33% | 2.38% | 1.08% |
| 24 |  |  |  |  |  | 13.42% | 8.96% | 7.57% | 4.08% | 2.30% | 1.10% |
| 40 |  |  |  |  |  |  | 9.01% | 7.47% | 4.17% | 2.28% | 1.01% |

**Content server**

| R \ T | 1 | 2 | 3 | 4 | 8 | 24 | 40 | 50 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 89.79% |  |  | 53.74% | 34.07% | 14.67% | 9.79% | 8.13% | 4.48% | 2.47% | 1.08% |
| 2 |  | 73.81% |  | 53.60% | 34.55% | 14.77% | 9.76% | 8.09% | 4.57% | 2.43% | 1.05% |
| 3 |  |  | 62.03% | 53.64% | 34.37% | 14.59% | 9.58% | 8.15% | 4.58% | 2.48% | 1.07% |
| 4 |  |  |  | 53.73% | 34.27% | 14.43% | 9.56% | 7.89% | 4.33% | 2.28% | 0.98% |
| 8 |  |  |  |  | 34.93% | 15.42% | 10.27% | 8.53% | 4.94% | 2.81% | 1.22% |
| 24 |  |  |  |  |  | 14.93% | 9.90% | 8.47% | 4.62% | 2.58% | 1.18% |
| 40 |  |  |  |  |  |  | 9.91% | 8.23% | 4.65% | 2.57% | 1.13% |

**First hop, credential**

| R \ T | 1 | 2 | 3 | 4 | 8 | 24 | 40 | 50 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 88.58% |  |  | 51.92% | 33.20% | 14.86% | 9.86% | 8.31% | 4.75% | 2.65% | 1.09% |
| 2 |  | 71.81% |  | 52.26% | 34.25% | 14.85% | 9.62% | 8.16% | 4.65% | 2.51% | 1.10% |
| 3 |  |  | 59.88% | 51.91% | 33.90% | 14.53% | 9.59% | 8.13% | 4.71% | 2.53% | 1.12% |
| 4 |  |  |  | 51.70% | 33.74% | 14.58% | 9.89% | 8.16% | 4.39% | 2.38% | 1.03% |
| 8 |  |  |  |  | 34.46% | 15.66% | 10.72% | 8.61% | 5.08% | 2.87% | 1.29% |
| 24 |  |  |  |  |  | 15.32% | 10.24% | 8.60% | 4.77% | 2.70% | 1.24% |
| 40 |  |  |  |  |  |  | 10.11% | 8.41% | 4.73% | 2.66% | 1.18% |

**First hop, credential, submission level** (first hop / baseline):

| R \ T | 1 | 2 | 3 | 4 | 8 | 24 | 40 | 50 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 82.39% / 80.94% |  |  | 47.96% / 43.03% | 31.64% / 25.15% | 17.47% / 9.17% | 13.86% / 5.62% | 12.26% / 4.33% | 8.68% / 2.28% | 5.72% / 1.16% | 2.64% / 0.44% |
| 4 |  |  |  | 47.52% / 43.24% | 31.33% / 25.10% | 17.02% / 8.92% | 13.49% / 5.36% | 12.06% / 4.33% | 8.61% / 2.11% | 5.62% / 1.13% | 2.58% / 0.42% |
| 40 |  |  |  |  |  |  | 13.74% / 5.54% | 12.35% / 4.45% | 8.77% / 2.28% | 5.61% / 1.15% | 2.62% / 0.46% |

With decoys, the first hop still names the exact capture at 13 times 1/T at T = 500 (2.6% against 0.2%). The baseline is at about 2 times.

Figure: `results/figures/device_accuracy_vs_T_decoy.png`.

## Calibrated confidence (device level)

Selected cells; every cell is in `results/tables.md`.

| Vantage | L | AUC [95% CI] | Precision, top 1% | Precision, top 5% | Largest coverage with precision > 50% |
|---|---|---|---|---|---|
| Baseline | 4 | 0.687 [0.683, 0.692] | 99.5% | 93.7% | 95.634% |
| Baseline | 40 | 0.568 [0.564, 0.572] | 17.2% | 14.0% | 0.000% |
| Baseline | 500 | 0.539 [0.536, 0.543] | 1.6% | 1.4% | 0.000% |
| First hop, credential | 4 | 0.689 [0.684, 0.693] | 99.2% | 95.8% | 100.000% |
| First hop, credential | 40 | 0.571 [0.567, 0.575] | 19.7% | 16.8% | 0.004% |
| First hop, credential | 500 | 0.544 [0.540, 0.548] | 1.9% | 1.7% | 0.000% |
| First hop, content | 4 | 0.680 [0.676, 0.684] | 99.4% | 93.4% | 100.000% |
| First hop, content | 40 | 0.569 [0.565, 0.573] | 18.1% | 15.3% | 0.000% |
| First hop, content | 500 | 0.541 [0.538, 0.544] | 1.9% | 1.6% | 0.000% |
| Credential processor | 4 | 0.685 [0.680, 0.689] | 100.0% | 93.0% | 95.111% |
| Credential processor | 40 | 0.567 [0.562, 0.571] | 17.3% | 13.9% | 0.000% |
| Credential processor | 500 | 0.540 [0.536, 0.543] | 1.6% | 1.4% | 0.000% |
| Content server | 4 | 0.708 [0.704, 0.713] | 100.0% | 97.1% | 100.000% |
| Content server | 40 | 0.565 [0.561, 0.568] | 12.7% | 14.4% | 0.000% |
| Content server | 500 | 0.530 [0.527, 0.532] | 0.8% | 1.2% | 0.000% |
| Validator | 4 | 0.715 [0.710, 0.719] | 100.0% | 99.0% | 100.000% |
| Validator | 40 | 0.575 [0.571, 0.579] | 19.9% | 16.7% | 0.000% |
| Validator | 500 | 0.543 [0.539, 0.546] | 1.9% | 1.7% | 0.000% |
| Gatekeeper | 4 | 0.691 [0.686, 0.695] | 99.5% | 94.9% | 96.458% |
| Gatekeeper | 40 | 0.566 [0.562, 0.570] | 17.0% | 14.0% | 0.000% |
| Gatekeeper | 500 | 0.539 [0.536, 0.543] | 1.6% | 1.4% | 0.000% |

## Controls

Sensitivity control, R = 40 with every hold off:

| Vantage | Device accuracy [95% CI] | Random device | Submission accuracy |
|---|---|---|---|
| Baseline | 99.44% [99.40%, 99.48%] | 98.61% | 99.43% |
| First hop, credential | 99.44% [99.40%, 99.48%] | 98.61% | 99.43% |
| First hop, content | 99.44% [99.40%, 99.48%] | 98.61% | 99.43% |
| Credential processor | 99.44% [99.39%, 99.48%] | 98.61% | 99.43% |
| Content server | 99.49% [99.45%, 99.53%] | 98.82% | 99.48% |
| Validator | 99.77% [99.75%, 99.80%] | 99.41% | 99.77% |
| Gatekeeper | 99.44% [99.40%, 99.48%] | 98.61% | 99.43% |

Every vantage is above the random-assignment rate, so the attacks find a timing signal when one exists. With every hold off, the random-assignment rate is itself near 99%: a record's feasible window then holds almost only its own device's capture.

Outcome-shuffle control (correctness permuted within each run): in 41 of the 406 stable cells the shuffled AUC interval excludes 0.5. 37 of these lie above 0.5 and 4 below. The plan sets a 0.03 margin because permuting within a run can leave a between-run association. 40 of the 41 lie within it. The exception is the credential first hop at R = 1, T = 500, at 0.539. Confidence AUCs at large L (0.526 to 0.544 at L = 500) are close to this effect, so they are not read as confidence signal.

## Predictions

| Prediction | Outcome |
|---|---|
| Q1. No-decoy sweep: every vantage's adjusted device-accuracy interval above the random-assignment rate at every L from 4 to 500 | Confirmed, and at L = 1 to 3 as well. |
| Q2. Gatekeeper and credential processor device-level contribution below +1 point at every L of 8 or more | Confirmed. The largest magnitude is 0.10 points. |
| Q3. Both first hops' submission-level contribution interval above zero at every L from 4 to 500 | Confirmed. From +2.1 to +8.3 points. |
| Q4. Validator's device accuracy at fixed R identical at every T | Confirmed exactly. |
| Q5. Baseline's device accuracy at fixed R falls as T rises | Confirmed at every R. |
| Q6. Sensitivity control: every vantage above the random-assignment rate | Confirmed. |
| Q7. Content server's device-level contribution interval above zero at L = 24 and 40 | Confirmed (+1.40 and +0.94 points). |

Q1, Q2, Q3, Q4 and Q6 were written after development runs that showed the same direction, as the plan discloses.

## Deviations from the plan

- **Run count recorded late.** The run count (200 per cell) was written into section 8 of the plan after the sweep, not before it. It is the count recommended from the cost estimate before the sweep started, and no sweep result had been seen when it was chosen.
- **AUC margin missing from the code.** The plan counts a confidence AUC as signal only if its adjusted interval lies above 0.5 by more than 0.03. The analysis code as run tested above 0.5 alone. That flags 381 cells; with the margin, 299 cells meet it. No cell's overall signal changes, because the accuracy test (above the random-assignment rate) is met in all 406. The code is corrected.

## Volume

Measured end-to-end delay D = 625.6 s (capture to registry finalization).

| L (in flight) | Captures per day | Devices (20-minute interval) |
|---|---|---|
| 1 | 138 | 1.9 |
| 2 | 276 | 3.8 |
| 3 | 414 | 5.8 |
| 4 | 552 | 7.7 |
| 8 | 1,105 | 15.3 |
| 24 | 3,315 | 46.0 |
| 40 | 5,525 | 76.7 |
| 50 | 6,906 | 95.9 |
| 100 | 13,811 | 191.8 |
| 200 | 27,623 | 383.6 |
| 500 | 69,057 | 959.1 |

## Scope

- **Arrival model.** Real captures arrive as one homogeneous Poisson process at a fixed rate for the whole run. Each capture is assigned to one of round(rate × 1,200 s) devices uniformly at random. There are no bursts beyond Poisson chance, no idle periods, no time-of-day pattern and no bursts from one device. Every figure above is therefore an average over the local neighbour counts a Poisson process happens to produce.
  - An exploratory breakdown, not pre-registered, was run on 20 fresh runs per volume. With no decoys, a record with no other real capture within ±600 s is linked to its device essentially every time, by every vantage the breakdown covered: the baseline 99.8% and the validator 100% at R = 1.
  - Accuracy falls as neighbours from other devices appear. At R = 1, with three or more such neighbours, the baseline falls to 55% and the validator to 66%.
  - Neighbours from the same device give much less cover: with three or more neighbours of any device, the baseline is at 79%.
  - The R = 1 figures are averages over this mix. They are neither a worst case nor a typical case for an isolated capture.
- **Decoy stream.** Decoys are a separate stationary Poisson stream at a constant rate, (T − R) / D, independent of the real traffic. Every real capture sees the same expected decoy density in its window. No controller computes decoy volume from observed real traffic, so the effect of a controller's measurement window on a capture in a lull is not tested.
- **Capture accounting.** One capture is one transaction: one credential packet and two content packets. A capture that produces two credential-side transactions on the same credential is not modelled.
- **One validator.** It sees every transaction. With several validators, each sees only its own manufacturer's share. The padded multi-validator case is outside this build.
- **Candidates.** They are device packets grouped per source by timing. Of the groups, 80.5% hold a single capture; the rest merge two captures from one device and are scored as mixed.
- **The attacks.** Each vantage uses one timing observation beyond the baseline's; the gatekeeper and the credential processor use a mixture over their own events. Stronger attacks can only raise these accuracies, so every figure here is a lower bound for its vantage.
- **Boards.** Board reads and board postings are not on the observed wire.

# Results

The question: can a single compromised component take a public registry record and name the device that produced it?

A decoy here is a genuine transaction from a registered identity, running at a steady 40 transactions in flight. The decoy identities (77 of them) each capture at a device's rate, and no party can tell a decoy from a real transaction. Each vantage is compared with chance and with a passive observer (the baseline) on the same records.

- 200 runs per cell, 8 cells: 1,600 runs.
- The cells are real volumes R = 1, 5, 15, 45 and 100 with the decoy stream (T = R + 40), R = 1 and 15 without it, and a sensitivity control.
- Every cell met the stability rule (at least 50 device-level successes and 50 failures), so every number is a finding.
- Intervals are 95% and resample whole runs.
- The primary measure is device-level accuracy of the per-decision attack. The submission level (naming the capture itself) is secondary.
- Rows are real records only.
- Full tables: `results/tables.md`. Analysis plan: `ANALYSIS_PLAN.md`, run count recorded before the sweep.

## Summary

1. **Decoys protect against every vantage, the validator included.**
   - At R = 1, the paired effect of the decoy stream on the same real records is -78.6 to -80.2 points of device accuracy for every vantage.
   - The validator falls from 89.5% to 9.8%.
   - At R = 15 the effect is -12.3 to -14.1 points.
2. **At the deployment volume (R = 1 with decoys), every vantage names the device 8.6% to 9.8% of the time,** against a random-pick rate of 2.1% to 2.5%. That is about 4 times chance.
   - The passive observer alone gets 8.75%.
   - No component adds more than 1.1 points over it at the device level.
3. **The gatekeeper and the credential processor add nothing.** Their device-level contribution is within ±0.2 points in every cell with decoys.
4. **The validator adds about a point at the device level:** +1.06 [+0.72, +1.41] at R = 1, falling to +0.46 at R = 100. It holds a device identity for each approval, but decoy approvals now look the same as real ones.
5. **The first hops name the exact capture well above chance.**
   - The credential first hop gets 13.5% of captures right at R = 1 with decoys, against 1/T = 2.4% and the baseline's 5.3%: a contribution of +8.1 points.
   - The content first hop is close behind at +7.3 points.
   - This is the largest single-component effect in this build. It comes from knowing the source address and their own hold. It holds from R = 1 to R = 100, where it is +5.6 points at 1/T = 0.7%.
6. **The content server adds +0.9 points at the device level and +1.2 at the submission level** at R = 1 with decoys.
7. **Confidence does not let an attacker pick out its right answers.** With decoys, no vantage keeps precision above 50% on more than 0.006% of its decisions, in any cell.
8. **With decoys held at 40, accuracy falls as real volume rises,** following T = R + 40. The baseline's device accuracy goes from 8.75% at R = 1 to 3.10% at R = 100.

## Pre-run checks

Run with background traffic on, at R = 15 with the decoy stream, over 12 runs (`results/checks.json`, `results/checks.log`).

| Check | Outcome |
|---|---|
| Padding classes | Pass. 17,388 legs, none outside its class; Ring V signature 64 B with real keys, verifies. |
| Answer extraction | Pass. 2,484 of 2,484 registry submissions (real and decoy). 3,726 of 3,726 device and decoy first-hop packets; no background packet among the candidates. 82.8% of submission groups hold a single capture. |
| Background independence | Pass. Every vantage's and the baseline's decisions identical with background traffic on and off. |
| Cannot tell decoys: baseline | **Fail**, marginally. 19 features; D's hold has AUC 0.488 [0.476, 0.4995] against 36 feature tests. The feature is produced by identical code for real and decoy traffic, and the interval misses 0.5 by 0.0005. This is reported as a failed check and was not re-run. |
| Cannot tell decoys: first hop, credential | Pass. Largest: time since the source's previous capture, AUC 0.509 [0.492, 0.525]. |
| Cannot tell decoys: first hop, content | Pass. Same feature and value. |
| Cannot tell decoys: credential processor | Pass. Largest: Cred-3 size, AUC 0.490 [0.478, 0.502]. |
| Cannot tell decoys: content server | Pass. Largest: content last-leg size, AUC 0.504 [0.493, 0.514]. |
| Cannot tell decoys: validator | Pass. Largest: CV-1 size, AUC 0.490 [0.475, 0.506]. |
| Cannot tell decoys: gatekeeper | Pass. Arrival to posting, AUC 0.497 [0.489, 0.506]. |
| Decoys reach the registry | Pass. 915 of 915 decoy and 327 of 327 real transactions finalized. |

Under the earlier decoy mechanism, the validator, the credential processor and the gatekeeper could tell decoys apart: through the validator's indicator, C's reading of it, and the failed σ_C check. With genuine decoys, all three pass the cannot-tell check. These passes follow from construction, since decoys now run the same code path, and they reverse the earlier result for those three vantages.

## Effect of the decoy stream on the same real records

Accuracy with decoys minus accuracy without, matched record by record (percentage points):

| Vantage | Device, R = 1 | Device, R = 15 | Submission, R = 1 | Submission, R = 15 |
|---|---|---|---|---|
| Baseline | -78.96 [-79.43, -78.53] | -12.39 [-12.71, -12.09] | -75.62 [-76.09, -75.16] | -10.23 [-10.50, -9.96] |
| First hop, credential | -78.85 [-79.31, -78.37] | -14.08 [-14.43, -13.76] | -68.95 [-69.44, -68.42] | -10.24 [-10.50, -9.98] |
| First hop, content | -78.61 [-79.04, -78.18] | -13.56 [-13.88, -13.25] | -68.82 [-69.27, -68.37] | -9.62 [-9.82, -9.41] |
| Credential processor | -78.79 [-79.27, -78.31] | -12.32 [-12.64, -12.01] | -75.36 [-75.82, -74.87] | -10.27 [-10.54, -10.00] |
| Content server | -80.16 [-80.58, -79.74] | -13.91 [-14.18, -13.65] | -78.80 [-79.18, -78.40] | -12.37 [-12.60, -12.15] |
| Validator | -79.67 [-80.15, -79.22] | -13.82 [-14.13, -13.50] | -72.15 [-72.59, -71.67] | -10.65 [-10.93, -10.38] |
| Gatekeeper | -79.18 [-79.60, -78.73] | -12.51 [-12.77, -12.24] | -75.87 [-76.28, -75.47] | -10.27 [-10.50, -10.06] |

Every interval lies below zero. Device accuracy with and without decoys:

| Vantage | Device, R = 1 | Device, R = 1 with decoys | Device, R = 15 | Device, R = 15 with decoys |
|---|---|---|---|---|
| Baseline | 87.71% | 8.75% | 19.36% | 6.97% |
| First hop, credential | 88.58% | 9.73% | 21.80% | 7.72% |
| First hop, content | 87.91% | 9.30% | 20.91% | 7.35% |
| Credential processor | 87.53% | 8.73% | 19.28% | 6.97% |
| Content server | 89.79% | 9.62% | 21.63% | 7.72% |
| Validator | 89.49% | 9.81% | 21.61% | 7.79% |
| Gatekeeper | 87.81% | 8.63% | 19.40% | 6.89% |

## Cells with decoys: device level

Accuracy [95% CI] (contribution over the baseline, in points):

| Vantage | R = 1 | R = 5 | R = 15 | R = 45 | R = 100 |
|---|---|---|---|---|---|
| Random device (baseline rows) | 2.09% | 1.90% | 1.56% | 1.01% | 0.62% |
| Baseline | 8.75% [8.39%, 9.10%] (+0.00) | 7.86% [7.49%, 8.21%] (+0.00) | 6.97% [6.69%, 7.24%] (+0.00) | 4.91% [4.79%, 5.03%] (+0.00) | 3.10% [3.05%, 3.16%] (+0.00) |
| First hop, credential | 9.73% [9.32%, 10.10%] (+0.98) | 8.74% [8.35%, 9.14%] (+0.88) | 7.72% [7.42%, 8.02%] (+0.75) | 5.55% [5.44%, 5.68%] (+0.64) | 3.65% [3.59%, 3.71%] (+0.54) |
| First hop, content | 9.30% [8.90%, 9.67%] (+0.55) | 8.35% [8.01%, 8.71%] (+0.49) | 7.35% [7.10%, 7.60%] (+0.39) | 5.30% [5.19%, 5.41%] (+0.39) | 3.44% [3.38%, 3.50%] (+0.33) |
| Credential processor | 8.73% [8.37%, 9.11%] (-0.02) | 7.84% [7.49%, 8.20%] (-0.01) | 6.97% [6.69%, 7.27%] (+0.00) | 4.91% [4.81%, 5.03%] (+0.00) | 3.10% [3.04%, 3.16%] (-0.01) |
| Content server | 9.62% [9.31%, 9.95%] (+0.87) | 8.73% [8.45%, 9.04%] (+0.88) | 7.72% [7.48%, 7.97%] (+0.75) | 5.39% [5.30%, 5.48%] (+0.48) | 3.48% [3.42%, 3.53%] (+0.37) |
| Validator | 9.81% [9.44%, 10.18%] (+1.06) | 8.84% [8.52%, 9.18%] (+0.99) | 7.79% [7.54%, 8.05%] (+0.82) | 5.60% [5.47%, 5.74%] (+0.69) | 3.56% [3.50%, 3.63%] (+0.46) |
| Gatekeeper | 8.63% [8.26%, 9.00%] (-0.12) | 7.86% [7.51%, 8.20%] (+0.00) | 6.89% [6.64%, 7.14%] (-0.08) | 4.86% [4.76%, 4.96%] (-0.05) | 3.11% [3.06%, 3.17%] (+0.01) |

## Cells with decoys: submission level

Accuracy [95% CI] (contribution over the baseline, in points):

| Vantage | R = 1 | R = 5 | R = 15 | R = 45 | R = 100 |
|---|---|---|---|---|---|
| 1/T | 2.44% | 2.22% | 1.82% | 1.18% | 0.71% |
| Baseline | 5.32% [5.11%, 5.53%] (+0.00) | 4.69% [4.49%, 4.88%] (+0.00) | 4.12% [3.96%, 4.29%] (+0.00) | 2.67% [2.59%, 2.75%] (+0.00) | 1.55% [1.51%, 1.59%] (+0.00) |
| First hop, credential | 13.45% [13.10%, 13.80%] (+8.13) | 13.33% [13.00%, 13.64%] (+8.64) | 11.86% [11.57%, 12.15%] (+7.74) | 9.53% [9.38%, 9.68%] (+6.85) | 7.15% [7.07%, 7.24%] (+5.60) |
| First hop, content | 12.59% [12.31%, 12.84%] (+7.27) | 11.98% [11.74%, 12.24%] (+7.29) | 10.94% [10.75%, 11.13%] (+6.82) | 9.01% [8.90%, 9.12%] (+6.34) | 6.75% [6.68%, 6.81%] (+5.19) |
| Credential processor | 5.29% [5.07%, 5.52%] (-0.03) | 4.66% [4.46%, 4.85%] (-0.03) | 4.06% [3.91%, 4.22%] (-0.06) | 2.66% [2.59%, 2.75%] (-0.01) | 1.55% [1.51%, 1.59%] (-0.00) |
| Content server | 6.50% [6.33%, 6.67%] (+1.18) | 5.95% [5.78%, 6.11%] (+1.26) | 4.98% [4.86%, 5.11%] (+0.86) | 3.18% [3.12%, 3.24%] (+0.50) | 1.95% [1.92%, 1.99%] (+0.40) |
| Validator | 5.86% [5.65%, 6.08%] (+0.54) | 4.98% [4.77%, 5.20%] (+0.29) | 4.18% [4.01%, 4.35%] (+0.06) | 2.72% [2.64%, 2.81%] (+0.05) | 1.68% [1.64%, 1.72%] (+0.12) |
| Gatekeeper | 5.34% [5.18%, 5.50%] (+0.02) | 4.79% [4.65%, 4.95%] (+0.10) | 4.00% [3.87%, 4.12%] (-0.12) | 2.63% [2.57%, 2.69%] (-0.05) | 1.56% [1.53%, 1.59%] (+0.01) |

Figure: `results/figures/accuracy_vs_R.png` (hollow markers: without decoys).

## Calibrated confidence (device level)

Selected cells; every cell is in `results/tables.md`.

| Vantage | Cell | AUC [95% CI] | Precision, top 1% | Precision, top 5% | Largest coverage with precision > 50% |
|---|---|---|---|---|---|
| Baseline | R = 1 with decoys | 0.569 [0.556, 0.581] | 15.5% | 13.5% | 0.000% |
| Baseline | R = 15 with decoys | 0.556 [0.545, 0.567] | 13.4% | 10.9% | 0.000% |
| Baseline | R = 100 with decoys | 0.551 [0.545, 0.556] | 5.4% | 4.5% | 0.000% |
| First hop, credential | R = 1 with decoys | 0.573 [0.562, 0.584] | 20.0% | 15.1% | 0.003% |
| First hop, credential | R = 15 with decoys | 0.567 [0.557, 0.577] | 16.3% | 12.5% | 0.000% |
| First hop, credential | R = 100 with decoys | 0.554 [0.550, 0.559] | 5.9% | 5.6% | 0.001% |
| First hop, content | R = 1 with decoys | 0.571 [0.561, 0.581] | 17.6% | 14.8% | 0.000% |
| First hop, content | R = 15 with decoys | 0.565 [0.556, 0.574] | 14.0% | 11.7% | 0.000% |
| First hop, content | R = 100 with decoys | 0.552 [0.547, 0.556] | 6.1% | 5.0% | 0.000% |
| Credential processor | R = 1 with decoys | 0.567 [0.555, 0.579] | 15.5% | 13.5% | 0.000% |
| Credential processor | R = 15 with decoys | 0.556 [0.545, 0.566] | 13.2% | 10.9% | 0.000% |
| Credential processor | R = 100 with decoys | 0.552 [0.546, 0.557] | 5.5% | 4.5% | 0.000% |
| Content server | R = 1 with decoys | 0.570 [0.561, 0.579] | 11.1% | 13.7% | 0.000% |
| Content server | R = 15 with decoys | 0.548 [0.539, 0.557] | 11.0% | 11.1% | 0.000% |
| Content server | R = 100 with decoys | 0.542 [0.538, 0.546] | 2.8% | 4.1% | 0.000% |
| Validator | R = 1 with decoys | 0.576 [0.564, 0.588] | 18.0% | 16.4% | 0.000% |
| Validator | R = 15 with decoys | 0.562 [0.551, 0.573] | 14.0% | 12.2% | 0.006% |
| Validator | R = 100 with decoys | 0.555 [0.549, 0.560] | 6.2% | 5.3% | 0.000% |
| Gatekeeper | R = 1 with decoys | 0.570 [0.559, 0.582] | 15.5% | 13.8% | 0.000% |
| Gatekeeper | R = 15 with decoys | 0.558 [0.547, 0.569] | 13.9% | 10.6% | 0.000% |
| Gatekeeper | R = 100 with decoys | 0.550 [0.545, 0.555] | 5.7% | 4.6% | 0.000% |

## Controls

Sensitivity control, R = 40 without decoys, every hold off:

| Vantage | Device accuracy [95% CI] | Random device |
|---|---|---|
| Baseline | 99.44% [99.40%, 99.48%] | 98.61% |
| First hop, credential | 99.44% [99.40%, 99.48%] | 98.61% |
| First hop, content | 99.44% [99.39%, 99.48%] | 98.61% |
| Credential processor | 99.44% [99.39%, 99.48%] | 98.61% |
| Content server | 99.49% [99.45%, 99.53%] | 98.82% |
| Validator | 99.77% [99.75%, 99.80%] | 99.41% |
| Gatekeeper | 99.44% [99.40%, 99.48%] | 98.61% |

Every vantage is above the random-assignment rate, so the attacks find a timing signal when one exists.

Outcome-shuffle control: in 7 of the 56 cells the shuffled-outcome AUC interval excludes 0.5 (0.491 to 0.512). All 7 lie within the plan's 0.03 margin.

## Predictions

| Prediction | Outcome |
|---|---|
| R1. Every vantage's device-level decoy effect interval below zero at R = 1 and R = 15 | Confirmed. |
| R2. The device-level decoy effect smaller in size at R = 15 than at R = 1, for every vantage | Confirmed (-12.3 to -14.1 against -78.6 to -80.2 points). |
| R3. With decoys, the validator's device-level contribution below +5 points in every cell | Confirmed. The largest is +1.06. |
| R4. Gatekeeper and credential processor device-level contribution below +1 point in every cell | Confirmed. The largest is +0.10 (gatekeeper, R = 1 without decoys). |
| R5. Every vantage's adjusted device-accuracy interval above the random-assignment rate in every cell | Confirmed. |
| R6. Sensitivity control: every vantage above the random-assignment rate | Confirmed. |

R2 and R3 were written after development runs that showed the same direction, as the plan discloses.

## Scope

- **One validator,** which sees every transaction.
- **Records are permanent.** Pruning is left as an implementation question and is not modelled.
- **The decoy stream is a steady Poisson process at 40 in flight,** independent of real traffic, shared by identities that each capture at a device's rate. A decoy identity's timing, paths and addresses follow the device model exactly. Any real-world difference between decoy identities and devices is outside what this tests.
- **Real traffic is a homogeneous Poisson process at a fixed rate,** with one transaction per capture. Bursty arrivals and sibling transactions (several candidate images per capture) are not modelled.
- **Candidates are device packets grouped per source by timing.** 82.8% of groups hold a single capture; the rest are scored as mixed.
- **Each vantage uses one timing observation beyond the baseline's.** Stronger attacks can only raise these accuracies, so every figure is a lower bound for its vantage.

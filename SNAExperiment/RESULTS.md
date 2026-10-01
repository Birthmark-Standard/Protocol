# Results

The question: can a single compromised component take a public registry record and name the device that produced it?

A decoy here is a genuine transaction from a registered identity, running at a steady 40 transactions in flight. The decoy identities (77 of them) each capture at a device's rate, and no party can tell a decoy from a real transaction. Each vantage is compared with chance and with a passive observer (the baseline) on the same records.

- 200 runs per cell, 8 cells: 1,600 runs.
- The cells are real volumes R = 1, 5, 15, 45 and 100 with the decoy stream (T = R + 40), R = 1 and 15 without it, and a sensitivity control.
- Every cell met the stability rule (at least 50 device-level successes and 50 failures), so every number is a finding.
- Intervals are 95% and resample whole runs.
- The primary measure is device-level accuracy of the per-decision attack. The submission level (naming the capture itself) is secondary.
- Rows are real records only.
- Full tables: `results/genuine_decoys/tables.md`. Analysis plan: `ANALYSIS_PLAN.md`; its run count was recorded before the sweep, and its section 6a was written before the first hops and credential processor were re-scored.

## Summary

1. **Decoys protect against every vantage.**
   - At R = 1, the paired effect of the decoy stream on the same real records is -78.6 to -80.2 points of device accuracy for every vantage.
   - The validator falls from 89.5% to 9.8%.
   - At R = 15 the effect is -12.3 to -14.1 points.
2. **At the deployment volume (R = 1 with decoys), every vantage names the device 8.6% to 9.8% of the time,** against a random-pick rate of 2.1% to 2.5%. That is about 4 times chance, and the passive observer alone gets 8.75%.
3. **No relay hop or credential processor adds anything over the passive observer.** Scored on every record, as they must be since they cannot tell which records they took part in, the first hops and the credential processor are within ±0.2 points of the observer in every cell, at both levels.
   - Their claims are no more accurate than the observer on the same records.
   - An earlier scoring credited the first hops with naming the exact capture at 13.4% against the observer's 5.3%. That came from scoring them only on records they had relayed, which they cannot identify. Section "Scoring on every record" below gives the correction.
4. **The gatekeeper adds nothing:** within ±0.2 points in every cell with decoys.
5. **The two components that know which records they handled add about a point at the device level.**
   - The validator holds a device identity for each approval: +1.06 [+0.72, +1.41] at R = 1 with decoys, falling to +0.46 at R = 100.
   - The content server is named on the records it submitted: +0.87 [+0.63, +1.09] at R = 1 with decoys.
6. **Confidence does not let an attacker pick out its right answers.** With decoys, no vantage keeps precision above 50% on more than 0.006% of its decisions, in any cell.
7. **With decoys held at 40, accuracy falls as real volume rises,** following T = R + 40. The baseline's device accuracy goes from 8.75% at R = 1 to 3.10% at R = 100.

## Pre-run checks

Run with background traffic on, at R = 15 with the decoy stream, over 12 runs (`results/genuine_decoys/checks.json`, `results/genuine_decoys/checks.log`).

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

## Scoring on every record

The first scoring of the first hops and the credential processor used as rows only the records each server took part in, chosen from the simulator's truth. Neither can identify those records: a registry record names F and I but no relay hop and no credential processor. A first hop's likelihood favours the captures it relayed, because it knows its own hold for them. On rows chosen to be its own, that preference is always right. On every other record it misleads.

As planned (section 6a), each compromised server is now scored on every record. Four servers per run are compromised in turn, rotating with the run id. A first hop claims a link when its top capture holds a packet it relayed. The credential processor claims one when the evidence at its pick favours its own transactions. These rows replace the earlier ones in every table of this document.

Submission level:

| Vantage | Cell | All records (submission) | Baseline | Claim rate | Claimed | Baseline on claimed | Took part (not identifiable) | Baseline on took part |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | R = 1 with decoys | 5.36% [5.20%, 5.51%] | 5.32% | 40.6% | 5.23% | 5.23% | 13.41% | 5.36% |
| First hop, credential | R = 15 with decoys | 4.05% [3.94%, 4.18%] | 4.12% | 47.9% | 3.91% | 4.05% | 11.74% | 4.17% |
| First hop, credential | R = 100 with decoys | 1.57% [1.55%, 1.59%] | 1.55% | 74.2% | 1.57% | 1.55% | 6.99% | 1.56% |
| First hop, credential | R = 15, no decoys | 14.28% [14.03%, 14.55%] | 14.35% | 24.6% | 13.34% | 13.52% | 21.96% | 14.10% |
| Credential processor | R = 1 with decoys | 5.35% [5.16%, 5.55%] | 5.32% | 51.1% | 5.27% | 5.21% | 5.47% | 5.49% |
| Credential processor | R = 15 with decoys | 4.04% [3.89%, 4.19%] | 4.12% | 53.1% | 3.97% | 4.07% | 3.87% | 4.03% |
| Credential processor | R = 100 with decoys | 1.57% [1.54%, 1.61%] | 1.55% | 54.4% | 1.56% | 1.53% | 1.57% | 1.57% |
| Credential processor | R = 15, no decoys | 14.31% [14.05%, 14.61%] | 14.35% | 36.0% | 13.58% | 13.61% | 14.25% | 14.16% |

Across every record, the first hop matches the observer. The records it claims are no more accurate than the observer on the same records. Its large advantage appears only on the records it took part in, which it cannot pick out. The two first-hop vantages are the same server scored on every record, so their claims and accuracy are identical; only their "took part" rows differ.

## Effect of the decoy stream on the same real records

Accuracy with decoys minus accuracy without, matched record by record (percentage points):

| Vantage | Device, R = 1 | Device, R = 15 | Submission, R = 1 | Submission, R = 15 |
|---|---|---|---|---|
| Baseline | -78.96 [-79.40, -78.50] | -12.39 [-12.71, -12.08] | -75.62 [-76.07, -75.15] | -10.23 [-10.51, -10.00] |
| First hop, credential | -79.03 [-79.46, -78.60] | -12.47 [-12.75, -12.19] | -75.63 [-76.04, -75.20] | -10.23 [-10.45, -10.01] |
| First hop, content | -79.03 [-79.44, -78.59] | -12.47 [-12.77, -12.20] | -75.63 [-76.05, -75.19] | -10.23 [-10.45, -10.00] |
| Credential processor | -78.96 [-79.41, -78.51] | -12.37 [-12.64, -12.07] | -75.57 [-76.02, -75.11] | -10.27 [-10.53, -10.03] |
| Content server | -80.16 [-80.59, -79.76] | -13.91 [-14.18, -13.64] | -78.80 [-79.17, -78.40] | -12.37 [-12.61, -12.15] |
| Validator | -79.67 [-80.13, -79.21] | -13.82 [-14.13, -13.51] | -72.15 [-72.57, -71.72] | -10.65 [-10.93, -10.38] |
| Gatekeeper | -79.18 [-79.59, -78.73] | -12.51 [-12.78, -12.24] | -75.87 [-76.28, -75.46] | -10.27 [-10.49, -10.06] |

Every interval lies below zero. Device accuracy with and without decoys:

| Vantage | Device, R = 1 | R = 1 with decoys | R = 15 | R = 15 with decoys |
|---|---|---|---|---|
| Baseline | 87.71% | 8.75% | 19.36% | 6.97% |
| First hop, credential | 87.73% | 8.69% | 19.34% | 6.87% |
| First hop, content | 87.73% | 8.69% | 19.34% | 6.87% |
| Credential processor | 87.70% | 8.74% | 19.31% | 6.94% |
| Content server | 89.79% | 9.62% | 21.63% | 7.72% |
| Validator | 89.49% | 9.81% | 21.61% | 7.79% |
| Gatekeeper | 87.81% | 8.63% | 19.40% | 6.89% |

## Cells with decoys: device level

Accuracy [95% CI] (contribution over the baseline, in points):

| Vantage | R = 1 | R = 5 | R = 15 | R = 45 | R = 100 |
|---|---|---|---|---|---|
| Random device (baseline rows) | 2.09% | 1.90% | 1.56% | 1.01% | 0.62% |
| Baseline | 8.75% [8.37%, 9.14%] (+0.00) | 7.86% [7.49%, 8.22%] (+0.00) | 6.97% [6.70%, 7.24%] (+0.00) | 4.91% [4.80%, 5.03%] (+0.00) | 3.10% [3.05%, 3.16%] (+0.00) |
| First hop, credential | 8.69% [8.35%, 9.05%] (-0.06) | 7.86% [7.55%, 8.20%] (+0.00) | 6.87% [6.61%, 7.13%] (-0.10) | 4.89% [4.79%, 4.99%] (-0.02) | 3.11% [3.06%, 3.16%] (+0.01) |
| First hop, content | 8.69% [8.33%, 9.07%] (-0.06) | 7.86% [7.52%, 8.20%] (+0.00) | 6.87% [6.61%, 7.11%] (-0.10) | 4.89% [4.79%, 4.99%] (-0.02) | 3.11% [3.05%, 3.16%] (+0.01) |
| Credential processor | 8.74% [8.36%, 9.10%] (-0.01) | 7.85% [7.48%, 8.22%] (-0.01) | 6.94% [6.68%, 7.20%] (-0.03) | 4.91% [4.80%, 5.03%] (-0.00) | 3.11% [3.05%, 3.16%] (+0.00) |
| Content server | 9.62% [9.30%, 9.94%] (+0.87) | 8.73% [8.43%, 9.04%] (+0.88) | 7.72% [7.47%, 7.97%] (+0.75) | 5.39% [5.30%, 5.48%] (+0.48) | 3.48% [3.42%, 3.53%] (+0.37) |
| Validator | 9.81% [9.44%, 10.19%] (+1.06) | 8.84% [8.53%, 9.17%] (+0.99) | 7.79% [7.53%, 8.05%] (+0.82) | 5.60% [5.47%, 5.73%] (+0.69) | 3.56% [3.50%, 3.63%] (+0.46) |
| Gatekeeper | 8.63% [8.29%, 8.99%] (-0.12) | 7.86% [7.52%, 8.20%] (+0.00) | 6.89% [6.62%, 7.14%] (-0.08) | 4.86% [4.76%, 4.97%] (-0.05) | 3.11% [3.06%, 3.17%] (+0.01) |

## Cells with decoys: submission level

Accuracy [95% CI] (contribution over the baseline, in points):

| Vantage | R = 1 | R = 5 | R = 15 | R = 45 | R = 100 |
|---|---|---|---|---|---|
| 1/T | 2.44% | 2.22% | 1.82% | 1.18% | 0.71% |
| Baseline | 5.32% [5.11%, 5.54%] (+0.00) | 4.69% [4.50%, 4.88%] (+0.00) | 4.12% [3.95%, 4.28%] (+0.00) | 2.67% [2.59%, 2.76%] (+0.00) | 1.55% [1.51%, 1.59%] (+0.00) |
| First hop, credential | 5.36% [5.20%, 5.51%] (+0.04) | 4.77% [4.62%, 4.92%] (+0.08) | 4.05% [3.94%, 4.18%] (-0.07) | 2.65% [2.60%, 2.70%] (-0.02) | 1.57% [1.55%, 1.59%] (+0.02) |
| First hop, content | 5.36% [5.20%, 5.51%] (+0.04) | 4.77% [4.63%, 4.92%] (+0.08) | 4.05% [3.93%, 4.17%] (-0.07) | 2.65% [2.60%, 2.71%] (-0.02) | 1.57% [1.55%, 1.59%] (+0.02) |
| Credential processor | 5.35% [5.16%, 5.55%] (+0.03) | 4.70% [4.52%, 4.89%] (+0.02) | 4.04% [3.89%, 4.19%] (-0.08) | 2.69% [2.62%, 2.76%] (+0.02) | 1.57% [1.54%, 1.61%] (+0.02) |
| Content server | 6.50% [6.34%, 6.66%] (+1.18) | 5.95% [5.77%, 6.12%] (+1.26) | 4.98% [4.85%, 5.11%] (+0.86) | 3.18% [3.12%, 3.24%] (+0.50) | 1.95% [1.92%, 1.99%] (+0.40) |
| Validator | 5.86% [5.65%, 6.08%] (+0.54) | 4.98% [4.76%, 5.21%] (+0.29) | 4.18% [4.01%, 4.34%] (+0.06) | 2.72% [2.63%, 2.81%] (+0.05) | 1.68% [1.64%, 1.72%] (+0.12) |
| Gatekeeper | 5.34% [5.18%, 5.50%] (+0.02) | 4.79% [4.64%, 4.95%] (+0.10) | 4.00% [3.87%, 4.11%] (-0.12) | 2.63% [2.57%, 2.69%] (-0.05) | 1.56% [1.53%, 1.59%] (+0.01) |

Figure: `results/genuine_decoys/figures/accuracy_vs_R.png` (hollow markers: without decoys).

## Calibrated confidence (device level)

Selected cells; every cell is in `results/genuine_decoys/tables.md`.

| Vantage | Cell | AUC [95% CI] | Precision, top 1% | Precision, top 5% | Largest coverage with precision > 50% |
|---|---|---|---|---|---|
| Baseline | R = 1 with decoys | 0.569 [0.556, 0.581] | 15.5% | 13.5% | 0.000% |
| Baseline | R = 15 with decoys | 0.556 [0.545, 0.567] | 13.4% | 10.9% | 0.000% |
| Baseline | R = 100 with decoys | 0.551 [0.545, 0.556] | 5.4% | 4.5% | 0.000% |
| First hop, credential | R = 1 with decoys | 0.568 [0.556, 0.579] | 15.8% | 13.4% | 0.000% |
| First hop, credential | R = 15 with decoys | 0.560 [0.550, 0.570] | 13.7% | 10.8% | 0.000% |
| First hop, credential | R = 100 with decoys | 0.551 [0.546, 0.556] | 5.5% | 4.5% | 0.000% |
| First hop, content | R = 1 with decoys | 0.568 [0.556, 0.579] | 15.8% | 13.4% | 0.000% |
| First hop, content | R = 15 with decoys | 0.560 [0.550, 0.570] | 13.7% | 10.8% | 0.000% |
| First hop, content | R = 100 with decoys | 0.551 [0.546, 0.556] | 5.5% | 4.5% | 0.000% |
| Credential processor | R = 1 with decoys | 0.568 [0.556, 0.580] | 15.5% | 13.2% | 0.000% |
| Credential processor | R = 15 with decoys | 0.556 [0.545, 0.567] | 13.3% | 10.8% | 0.000% |
| Credential processor | R = 100 with decoys | 0.551 [0.546, 0.557] | 5.4% | 4.5% | 0.000% |
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
| First hop, content | 99.44% [99.40%, 99.48%] | 98.61% |
| Credential processor | 99.44% [99.40%, 99.48%] | 98.61% |
| Content server | 99.49% [99.45%, 99.53%] | 98.82% |
| Validator | 99.77% [99.75%, 99.80%] | 99.41% |
| Gatekeeper | 99.44% [99.40%, 99.48%] | 98.61% |

Every vantage is above the random-assignment rate, so the attacks find a timing signal when one exists.

Outcome-shuffle control: in 11 of the 56 cells the shuffled-outcome AUC interval excludes 0.5. All lie within the plan's 0.03 margin.

## Predictions

| Prediction | Outcome |
|---|---|
| R1. Every vantage's device-level decoy effect interval below zero at R = 1 and R = 15 | Confirmed. |
| R2. The device-level decoy effect smaller in size at R = 15 than at R = 1, for every vantage | Confirmed (-12.3 to -14.1 against -78.6 to -80.2 points). |
| R3. With decoys, the validator's device-level contribution below +5 points in every cell | Confirmed. The largest is +1.06. |
| R4. Gatekeeper and credential processor device-level contribution below +1 point in every cell | Confirmed. |
| R5. Every vantage's adjusted device-accuracy interval above the random-assignment rate in every cell | Confirmed. |
| R6. Sensitivity control: every vantage above the random-assignment rate | Confirmed. |
| S1. Over every record, each first hop's submission-level contribution interval within ±1 point at every cell with decoys | Confirmed. Every interval lies within ±0.2 points. |
| S2. Over every record, the credential processor's device-level contribution within ±0.5 points in every cell | Confirmed. |

R2, R3 and S1 were written after development runs or diagnostics that showed the same direction, as the plan discloses.

## Scope

- **One validator,** which sees every transaction.
- **Records are permanent.** Pruning is left as an implementation question and is not modelled.
- **The decoy stream is a steady Poisson process at 40 in flight,** independent of real traffic, shared by identities that each capture at a device's rate. A decoy identity's timing, paths and addresses follow the device model exactly. Any real-world difference between decoy identities and devices is outside what this tests.
- **Real traffic is a homogeneous Poisson process at a fixed rate,** with one transaction per capture. Bursty arrivals and sibling transactions (several candidate images per capture) are not modelled.
- **Candidates are device packets grouped per source by timing.** 82.8% of groups hold a single capture; the rest are scored as mixed.
- **Each vantage uses one timing observation beyond the baseline's.** Stronger attacks can only raise these accuracies, so every figure is a lower bound for its vantage.

# Gatekeeper departure bundling

Plan section 6b; full tables in `results/bundling/tables.md`, checks in `results/bundling/checks.json` (run with bundling on).

Each gatekeeper's hold-clock selections wait for the next boundary of its own 30-second grid and depart together. Board postings are internal to the gatekeeper and are not on the observed wire. The sweep covered R = 1, 15 and 50 real transactions in flight, at decoy targets of 20, 40 and 60 in flight, with bundling on and off.

- 200 runs per cell, 18 cells plus the sensitivity control: 3,800 runs. Every cell met the stability rule.
- Bundling on and off carry identical traffic, so each effect below is a paired difference on the same records.
- Cells with bundling are attacked with likelihood models built with bundling on.
- The first hops and the credential processor are scored on every record.

## Summary

1. **Bundling does not protect against the passive observer here.** Its effect on the observer's device accuracy lies between -0.26 and +0.02 points in all nine (R, decoy) cells. Every vantage's effect lies between -0.42 and +0.19 points.
2. **The reason is structural in this model.** Board postings never cross the observed wire, so the observer never sees a gatekeeper departure and has no ordering signal for bundling to remove. Bundling reaches the observer only as up to 30 seconds of extra delay before quorum, against a capture-to-registry delay of about 626 seconds that already carries several lottery holds.
3. **The decoy target matters far more than bundling.** At R = 1 with bundling on, the observer names the device:
   - 14.3% of the time at 20 decoys;
   - 8.6% at 40 decoys;
   - 6.0% at 60 decoys.
4. **Bundles are small at the deployment volume.** At R = 1 with 40 decoys, a bundle holds 1.97 postings on average, and 41.5% of bundles hold fewer than two. Under 0.1% of bundles would hold fewer than two only at real volumes far above the deployment range. At R = 50 with 60 decoys the share is still 3.2%.
   - The hand estimate of 10 per bundle counted all 40 decoys in flight as held at the gatekeeper.
   - A transaction spends about 111 of its 626 seconds there, so about 7 postings wait at one gatekeeper at a time, and about 0.67 are released per 10-second tick.

## Bundle sizes

Postings per 30-second bundle at one gatekeeper, over every run of the bundling cells:

| R | Decoys | Postings per bundle (mean) | Bundles with fewer than 2 | Non-empty bundles holding 1 | Postings departing alone |
|---|---|---|---|---|---|
| 1 | 20 | 1.01 | 73.3% | 57.9% | 36.5% |
| 1 | 40 | 1.97 | 41.5% | 31.9% | 14.0% |
| 1 | 60 | 2.93 | 21.0% | 16.5% | 5.4% |
| 15 | 20 | 1.69 | 49.5% | 38.1% | 18.3% |
| 15 | 40 | 2.65 | 25.8% | 20.1% | 7.0% |
| 15 | 60 | 3.62 | 12.4% | 10.0% | 2.7% |
| 50 | 20 | 3.35 | 15.3% | 12.2% | 3.5% |
| 50 | 40 | 4.31 | 7.1% | 5.8% | 1.3% |
| 50 | 60 | 5.26 | 3.2% | 2.7% | 0.5% |

## Effect of bundling on the passive observer

Accuracy with bundling minus accuracy without, matched record by record (percentage points):

| R | Decoys | Device, off | Device, on | Device effect [95% CI] | Submission, off | Submission, on | Submission effect [95% CI] |
|---|---|---|---|---|---|---|---|
| 1 | 20 | 14.57% | 14.31% | -0.26 [-0.42, -0.11] | 10.37% | 10.23% | -0.15 [-0.44, +0.17] |
| 1 | 40 | 8.75% | 8.61% | -0.14 [-0.26, -0.03] | 5.32% | 5.27% | -0.05 [-0.28, +0.20] |
| 1 | 60 | 6.00% | 6.01% | +0.02 [-0.09, +0.11] | 3.68% | 3.49% | -0.19 [-0.43, +0.03] |
| 15 | 20 | 9.89% | 9.79% | -0.10 [-0.21, +0.02] | 6.40% | 6.15% | -0.25 [-0.50, -0.02] |
| 15 | 40 | 6.97% | 6.86% | -0.11 [-0.21, -0.01] | 4.12% | 4.01% | -0.11 [-0.30, +0.08] |
| 15 | 60 | 5.32% | 5.24% | -0.08 [-0.17, +0.00] | 2.99% | 2.92% | -0.08 [-0.25, +0.09] |
| 50 | 20 | 5.66% | 5.61% | -0.05 [-0.10, +0.00] | 3.13% | 3.13% | -0.01 [-0.10, +0.08] |
| 50 | 40 | 4.59% | 4.54% | -0.06 [-0.10, -0.01] | 2.46% | 2.44% | -0.02 [-0.11, +0.08] |
| 50 | 60 | 3.85% | 3.83% | -0.02 [-0.07, +0.02] | 2.01% | 2.01% | +0.00 [-0.09, +0.08] |

Figure: `results/bundling/figures/bundling_gpa.png`.

## Effect of bundling on every vantage

The range of each vantage's device-level effect across the nine (R, decoy) cells:

| Vantage | Smallest device effect [95% CI] | Largest device effect [95% CI] |
|---|---|---|
| Baseline | -0.26 [-0.42, -0.11] (R = 1, 20 decoys) | +0.02 [-0.09, +0.11] (R = 1, 60 decoys) |
| First hop, credential | -0.23 [-0.35, -0.10] (R = 1, 20 decoys) | -0.02 [-0.10, +0.07] (R = 1, 60 decoys) |
| First hop, content | -0.23 [-0.36, -0.10] (R = 1, 20 decoys) | -0.02 [-0.10, +0.07] (R = 1, 60 decoys) |
| Credential processor | -0.17 [-0.31, -0.04] (R = 1, 20 decoys) | +0.02 [-0.07, +0.11] (R = 1, 60 decoys) |
| Content server | -0.23 [-0.41, -0.05] (R = 1, 40 decoys) | +0.00 [-0.14, +0.15] (R = 15, 40 decoys) |
| Validator | -0.00 [-0.15, +0.14] (R = 1, 40 decoys) | +0.19 [+0.08, +0.30] (R = 15, 40 decoys) |
| Gatekeeper | -0.12 [-0.20, -0.04] (R = 15, 60 decoys) | -0.01 [-0.12, +0.11] (R = 15, 20 decoys) |

Every cell is in `results/bundling/tables.md`.

## Decoy target at R = 1 (bundling on)

Device accuracy (contribution over the baseline, in points):

| Vantage | R = 1, 20 decoys | R = 1, 40 decoys | R = 1, 60 decoys | Random device at 20 / 40 / 60 |
|---|---|---|---|---|
| Baseline | 14.31% (+0.00) | 8.61% (+0.00) | 6.01% (+0.00) | 4.08% / 2.08% / 1.40% |
| First hop, credential | 14.34% (+0.03) | 8.60% (-0.01) | 6.03% (+0.02) | 4.08% / 2.08% / 1.40% |
| First hop, content | 14.34% (+0.03) | 8.60% (-0.01) | 6.03% (+0.02) | 4.08% / 2.08% / 1.40% |
| Credential processor | 14.32% (+0.01) | 8.68% (+0.07) | 6.00% (-0.01) | 4.08% / 2.08% / 1.40% |
| Content server | 16.07% (+1.76) | 9.39% (+0.78) | 6.71% (+0.70) | 4.82% / 2.46% / 1.66% |
| Validator | 16.18% (+1.87) | 9.81% (+1.20) | 7.06% (+1.05) | 4.91% / 2.50% / 1.69% |
| Gatekeeper | 14.31% (-0.00) | 8.51% (-0.10) | 5.92% (-0.09) | 4.08% / 2.08% / 1.40% |

## Checks and controls

- **Pre-run checks** (with bundling on): every posting departs on its gatekeeper's own grid, 6.7 to 29.3 seconds after selection. Every other check passes except the same marginal baseline failure reported above (D's hold, AUC upper bound 0.4995 over the same seeds), which bundling does not touch.
- **Outcome-shuffle control:** 9 of 133 stable cells have a shuffled-outcome AUC interval excluding 0.5, all within the plan's 0.03 margin.
- **Accuracy test:** every vantage's adjusted device-accuracy interval lies above the random-assignment rate in every cell.

## Predictions

| Prediction | Outcome |
|---|---|
| B1. The passive observer's device-level bundling effect within ±1 point in every cell | Confirmed (-0.26 to +0.02). |
| B2. No vantage's device-level bundling effect interval wholly below -3 points in any cell | Confirmed. The lowest interval bound is -0.42. |
| B3. At each R, the share of bundles with fewer than two postings falls as the decoy target rises | Confirmed at R = 1, 15 and 50. |

B1 confirms development runs, as the plan discloses.

## Scope

- **Board postings are internal.** If postings crossed the wire to separate board hosts, the observer would see departures and bundling could remove an ordering signal it then has. That case is not tested here.
- **Grids.** Each gatekeeper has its own 30-second grid phase. The relay-hop lottery is unchanged.
- **Decoy stream.** The decoy stream at each target is a steady Poisson process, as in the sections above.

# Match board pushes

Plan section 6c; full tables in `results/tables_push.md`, checks in `results/push/checks.json` and `results/push/checks.log`.

Content servers never query a board. Each board pushes every match posted since its previous push to every content server, every 10 seconds on its own schedule. A content server submits once its hold has released and pushes from two boards have carried the match. Pushes are internal to the board layer and are not on the observed wire. Bundling is on in every cell.

- 200 runs per cell, 9 cells plus the sensitivity control: 2,000 runs. Every cell met the stability rule.
- The push build carries the same traffic as the bundling sweep's bundling-on cells up to the content servers, so each effect below is a paired difference on the same records.
- Likelihood models were rebuilt under the push build. The first hops and the credential processor are scored on every record.

## Summary

1. **Board pushes leave every vantage where it was.** Every vantage's device-level push effect lies between -0.04 and +0.11 points across the nine cells. The largest interval bound in either direction is 0.30 points.
2. **The ranking of vantages is unchanged.** The validator and the content server add about 0.4 to 1.9 points over the passive observer. Every other vantage stays within 0.1 points of it.
3. **The decoy target still dominates.** At R = 1, the observer names the device 14.4% of the time at 20 decoys, 8.7% at 40, and 6.0% at 60.

## Effect of board pushes on every vantage

The range of each vantage's device-level push effect across the nine cells, in points (accuracy with pushes minus accuracy with content servers checking the boards on their own clock, matched record by record):

| Vantage | Smallest device effect [95% CI] | Largest device effect [95% CI] |
|---|---|---|
| Baseline | -0.01 [-0.10, +0.07] (R = 15, 60 decoys) | +0.06 [-0.02, +0.14] (R = 15, 40 decoys) |
| First hop, credential | -0.00 [-0.04, +0.03] (R = 50, 40 decoys) | +0.07 [-0.02, +0.15] (R = 1, 40 decoys) |
| First hop, content | -0.00 [-0.04, +0.03] (R = 50, 40 decoys) | +0.07 [-0.03, +0.15] (R = 1, 40 decoys) |
| Credential processor | -0.04 [-0.11, +0.04] (R = 1, 40 decoys) | +0.03 [-0.05, +0.11] (R = 15, 20 decoys) |
| Content server | -0.04 [-0.17, +0.10] (R = 15, 40 decoys) | +0.09 [-0.10, +0.28] (R = 1, 40 decoys) |
| Validator | -0.04 [-0.16, +0.06] (R = 15, 20 decoys) | +0.11 [+0.01, +0.20] (R = 1, 60 decoys) |
| Gatekeeper | -0.01 [-0.11, +0.08] (R = 15, 20 decoys) | +0.10 [+0.00, +0.20] (R = 1, 40 decoys) |

## Device accuracy with board pushes

Device accuracy (contribution over the baseline, in points):

| Vantage | R = 1, 20 decoys | R = 1, 40 decoys | R = 1, 60 decoys | R = 15, 40 decoys | R = 50, 40 decoys |
|---|---|---|---|---|---|
| Baseline | 14.35% (+0.00) | 8.65% (+0.00) | 6.02% (+0.00) | 6.92% (+0.00) | 4.54% (+0.00) |
| First hop, credential | 14.37% (+0.02) | 8.66% (+0.01) | 6.05% (+0.02) | 6.88% (-0.03) | 4.52% (-0.02) |
| First hop, content | 14.37% (+0.02) | 8.66% (+0.01) | 6.05% (+0.02) | 6.88% (-0.03) | 4.52% (-0.02) |
| Credential processor | 14.32% (-0.02) | 8.64% (-0.02) | 6.03% (+0.00) | 6.89% (-0.03) | 4.53% (-0.01) |
| Content server | 16.15% (+1.80) | 9.48% (+0.83) | 6.70% (+0.68) | 7.68% (+0.76) | 5.09% (+0.56) |
| Validator | 16.27% (+1.93) | 9.85% (+1.19) | 7.16% (+1.14) | 7.98% (+1.07) | 5.26% (+0.72) |
| Gatekeeper | 14.35% (+0.00) | 8.61% (-0.04) | 5.94% (-0.09) | 6.89% (-0.02) | 4.51% (-0.02) |
| Random device | 4.07% | 2.08% | 1.40% | 1.55% | 0.95% |

The random rate is the baseline's. It is slightly higher for the content server and the validator, which are scored on the records they handled. Every cell is in `results/tables_push.md`.

## Sensitivity control

The control turns every hold off. It does not turn off the push schedule, which is not a hold, so each match still waits 0 to 10 seconds for its board's next push. At R = 40 without decoys:

| Vantage | Control, bundling sweep | Control, push build |
|---|---|---|
| Baseline | 99.4% | 79.6% |
| Content server | 99.5% | 98.5% |
| Random device | | 73.7% |

- With holds off, the remaining delays are network latencies of milliseconds. A push wait of up to 10 seconds is then the largest delay in the record time, and it costs the observer about 20 points.
- The content server knows its own content arrival, so it keeps 98.5%.
- The control still shows that the attacks find a link when the timing allows one.

## Checks and controls

- **Pre-run checks** (with bundling on): no content server acts before its hold releases or before its quorum push arrives, and pushes wait up to 9.4 seconds for their board's next slot (check 7). Every posting departs on its gatekeeper's own grid (check 6). Every other check passes except the same marginal baseline failure reported above (D's hold, AUC 0.488 [0.476, 0.500] over the same seeds), which pushes do not touch.
- **Outcome-shuffle control:** 5 of 70 stable cells have a shuffled-outcome AUC interval excluding 0.5, all within the plan's 0.03 margin (largest 0.513).

## Predictions

| Prediction | Outcome |
|---|---|
| P1. The passive observer's device-level push effect within ±1 point in every cell | Confirmed (-0.01 to +0.06). |
| P2. No vantage's device-level push effect interval wholly outside ±3 points in any cell | Confirmed. The interval bounds lie between -0.17 and +0.30. |
| P3. The content server's device-level push effect within ±2 points in every cell | Confirmed (-0.04 to +0.09). |

P1 to P3 follow development runs, as the plan discloses.

## Scope

- **Push schedule.** The 10-second period, the per-board phase, and keeping pushes off the observed wire are this build's choices. The specification states only that the boards regularly push all new matches to all servers.
- **One validator.** Every cell has one validator.

# Two-point gatekeeper hold and registry-level bundling

Plan section 6d; full tables in `results/tables_twopoint.md` (two-point hold) and `results/tables_regbundle.md` (two-point hold and registry bundling); checks and run log in `results/regbundle/`, run on the build with both mechanisms.

Each build adds one mechanism to the one before it:
- **push** is the build of the previous section.
- **twopoint** replaces the gatekeeper's hold with the two-point hold: release at once with probability 0.6, or hold exactly 300 seconds.
- **regbundle** adds registry-level pooled bundling: a confirmed submission waits for the next boundary of one 120-second schedule shared by every content server.

Every cell has gatekeeper departure bundling and board pushes on. The builds share every random draw outside the mechanism each adds, so each effect below is a paired difference on the same records. 200 runs per cell, 9 cells per build plus the control for regbundle: 3,800 runs. Every cell met the stability rule.

## Summary

1. **The two-point hold lowers every vantage's accuracy by 0.1 to 1.1 points.** The passive observer loses 0.30 to 0.88 points, and its interval lies below 0 in all nine cells.
2. **Most of that drop comes from a larger candidate set, not a weaker signal.** The two-point hold lengthens the end-to-end delay, so more devices remain feasible for each record: at R = 1 with 40 decoys, 51.4 against 48.5. The random-pick rate falls with it, from 2.08% to 1.96%. Measured as a multiple of the random rate, the observer moves from 4.16 [3.98, 4.34] to 4.03 [3.85, 4.21], and the intervals overlap in every cell.
3. **Registry bundling does not move the passive observer.** Its effect on the observer lies between -0.20 and +0.04 points.
4. **Registry bundling removes about half of the validator's edge.** The validator's contribution over the observer falls from 1.44 to 0.75 points at R = 1 with 40 decoys, and its accuracy falls 0.38 to 1.15 points across the nine cells.
5. **The combined cost is about 73 seconds of latency.** At R = 1 with 40 decoys, the mean time from capture to registry finalization rises from 625.5 to 698.2 seconds, and the 95th percentile from 892 to 996 seconds.
6. **The end-to-end delay does not collapse onto a few values.** Under the two-point hold, the fullest 10-second bin holds 2.8% of transactions against 3.1% before, and more bins are occupied.

## The passive observer, by build

Device accuracy, the random-pick rate, and accuracy as a multiple of the random rate [95% CI]:

| R | Decoys | push | twopoint | regbundle |
|---|---|---|---|---|
| 1 | 20 | 14.35% (random 4.07%, ×3.52 [3.41, 3.63]) | 13.47% (3.84%, ×3.50 [3.39, 3.62]) | 13.27% (3.81%, ×3.48 [3.36, 3.60]) |
| 1 | 40 | 8.65% (2.08%, ×4.16 [3.98, 4.34]) | 7.89% (1.96%, ×4.03 [3.85, 4.21]) | 7.86% (1.94%, ×4.05 [3.86, 4.23]) |
| 1 | 60 | 6.02% (1.40%, ×4.30 [4.06, 4.52]) | 5.62% (1.32%, ×4.25 [4.05, 4.46]) | 5.65% (1.31%, ×4.32 [4.11, 4.52]) |
| 15 | 20 | 9.80% (2.43%, ×4.02 [3.91, 4.14]) | 9.12% (2.30%, ×3.97 [3.86, 4.10]) | 8.94% (2.27%, ×3.93 [3.81, 4.05]) |
| 15 | 40 | 6.92% (1.55%, ×4.47 [4.31, 4.65]) | 6.41% (1.46%, ×4.39 [4.22, 4.58]) | 6.24% (1.44%, ×4.32 [4.15, 4.50]) |
| 15 | 60 | 5.22% (1.14%, ×4.60 [4.39, 4.82]) | 4.93% (1.07%, ×4.60 [4.38, 4.84]) | 4.87% (1.06%, ×4.60 [4.36, 4.83]) |
| 50 | 20 | 5.61% (1.22%, ×4.58 [4.49, 4.68]) | 5.15% (1.15%, ×4.46 [4.37, 4.55]) | 5.11% (1.14%, ×4.47 [4.38, 4.55]) |
| 50 | 40 | 4.54% (0.95%, ×4.77 [4.66, 4.88]) | 4.18% (0.90%, ×4.67 [4.56, 4.78]) | 4.17% (0.89%, ×4.70 [4.58, 4.81]) |
| 50 | 60 | 3.82% (0.78%, ×4.91 [4.78, 5.04]) | 3.49% (0.73%, ×4.76 [4.63, 4.90]) | 3.45% (0.73%, ×4.75 [4.61, 4.90]) |

Figure: `results/figures/observer_by_build.png`.

## Effect of each mechanism on the same records

Device-level effect in points [95% CI], at R = 1 with 40 decoys and across all nine cells:

| Vantage | Two-point hold, R = 1, 40 decoys | Two-point hold, range over cells | Registry bundling, R = 1, 40 decoys | Registry bundling, range over cells |
|---|---|---|---|---|
| Baseline | -0.76 [-1.00, -0.53] | -0.88 to -0.30 | -0.03 [-0.17, +0.13] | -0.20 to +0.04 |
| First hop, credential | -0.75 [-0.97, -0.54] | -0.93 to -0.34 | -0.04 [-0.17, +0.09] | -0.19 to +0.02 |
| First hop, content | -0.75 [-0.96, -0.54] | -0.93 to -0.34 | -0.04 [-0.18, +0.10] | -0.19 to +0.02 |
| Credential processor | -0.75 [-0.98, -0.52] | -0.90 to -0.32 | -0.08 [-0.22, +0.07] | -0.21 to +0.00 |
| Content server | -0.28 [-0.47, -0.08] | -0.64 to -0.13 | +0.07 [-0.13, +0.26] | -0.10 to +0.07 |
| Validator | -0.52 [-0.82, -0.21] | -0.58 to -0.25 | -0.71 [-0.96, -0.44] | -1.15 to -0.38 |
| Gatekeeper | -0.73 [-0.95, -0.53] | -1.05 to -0.34 | -0.09 [-0.21, +0.05] | -0.12 to +0.00 |

Every cell is in `results/tables_twopoint.md` and `results/tables_regbundle.md`.

## Contribution over the passive observer, R = 1 with 40 decoys

| Vantage | push | twopoint | regbundle |
|---|---|---|---|
| Content server | +0.83 | +1.31 | +1.40 |
| Validator | +1.19 | +1.44 | +0.75 |
| Every other vantage | within ±0.1 | within ±0.1 | within ±0.1 |

The two-point hold lowers the observer more than it lowers the content server, so the content server's contribution over the observer grows. Registry bundling quantizes the record time to its 120-second schedule, which the validator's reply-to-record density depends on.

## Gatekeeper hold shape

| Hold | Mean | Coefficient of variation |
|---|---|---|
| Relay lottery, as the gatekeeper used before | 106.2 s | 0.84 |
| Two-point | 119.8 s | 1.23 |

- The specification's hand estimates were 120 seconds and 0.52 for the lottery, and 0.81 for the two-point hold. The lottery's mean is below 120 seconds because its 30-tick cap truncates the geometric draw.
- In the simulator, the end-to-end delay stays continuous under the two-point hold. At R = 1 with 40 decoys, the fullest 10-second bin holds 2.79% of real transactions under twopoint and 3.14% under push, with 98 and 97 bins occupied. At R = 50 the figures are 2.54% and 2.77%, with 112 and 105 bins. Figure: `results/figures/latency_by_build.png`.

## Registry bundle sizes

Over the sweep's own runs (`results/registry_bundles_regbundle.json`), 120-second bundles pooled across every content server:

| R | Decoys | Submissions per bundle | Distinct transactions per bundle | Bundles with fewer than 2 transactions |
|---|---|---|---|---|
| 1 | 20 | 8.1 | 5.4 | 2.98% |
| 1 | 40 | 15.7 | 10.5 | 0.029% |
| 1 | 60 | 23.4 | 15.6 | under 0.001% |
| 15 | 20 | 13.5 | 9.0 | 0.073% |
| 15 | 40 | 21.2 | 14.2 | under 0.001% |
| 15 | 60 | 28.9 | 19.3 | under 0.001% |
| 50 | 20 | 26.8 | 17.8 | under 0.001% |
| 50 | 40 | 34.4 | 23.0 | under 0.001% |
| 50 | 60 | 42.1 | 28.1 | under 0.001% |

For comparison, gatekeeper departure bundles at R = 1 with 40 decoys hold 1.97 postings on average, and 41.5% of them hold fewer than two.

## Latency

From a real capture to its registry finalization, at 40 decoys (`results/latency.json`, 20 runs per cell):

| Build | R = 1: mean / median / 95th percentile | R = 15 | R = 50 |
|---|---|---|---|
| push | 625.5 / 618.2 / 892.2 s | 633.0 / 622.0 / 898.5 s | 628.1 / 618.7 / 889.7 s |
| twopoint | 638.9 / 629.3 / 918.5 s | 647.4 / 636.7 / 935.8 s | 642.4 / 633.0 / 925.9 s |
| regbundle | 698.2 / 686.4 / 996.2 s | 707.1 / 696.6 / 1005.7 s | 701.4 / 692.6 / 989.7 s |

Mean stages at R = 1 with 40 decoys, with both mechanisms:

| Stage | Mean |
|---|---|
| Capture to the gatekeepers (device hold, relay holds, validator round trip, fan-out hold) | 419.2 s |
| Gatekeeper hold | 119.7 s |
| Gatekeeper bundle wait | 15.0 s |
| Quorum to the later content server's confirmation (its own hold and the board push) | 93.6 s |
| Registry bundle wait | 61.7 s |
| Capture to finalization | 698.2 s |

Quorum forms on the second of three postings, so the stages do not sum exactly to the total.

## Sensitivity control

The control turns every hold off. Registry bundling is not a hold and stays on, so every record time is rounded up to the shared 120-second schedule. At R = 40 without decoys, the observer names the device 17.1% of the time against a random rate of 12.8%, down from 79.6% under push. The content server, which knows its own content arrival, keeps 98.5%. The control still shows that an attack with exact knowledge finds the link.

## Checks and controls

- **Pre-run checks** (regbundle, bundling on): every gatekeeper hold is immediate (60.3%) or at the cap (39.7%), with mean 119.1 seconds (check 8). Every registry submission departs on the shared grid, 0.2 to 119.4 seconds after confirmation (check 9). Every other check passes except the same marginal baseline failure as before (D's hold, AUC 0.488 [0.476, 0.500]).
- **Outcome-shuffle control:** 5 of 63 stable cells under twopoint and 5 of 70 under regbundle have a shuffled-outcome AUC interval excluding 0.5, all within the plan's 0.03 margin (largest 0.512).
- **Rates.** Real and decoy rates are those of the push build. The longer delay therefore holds more transactions in flight in each cell, and part of the effects above comes from that, as summary point 2 describes.

## Predictions

| Prediction | Outcome |
|---|---|
| M1. The two-point hold lowers the observer's device accuracy below 0 in every cell, with the interval wholly below 0 in at least 6 of 9 | Confirmed: below 0 in all 9, interval wholly below 0 in all 9. |
| M2. The two-point hold's effect on the observer lies above -3 points in every cell | Confirmed. The lowest is -0.88. |
| M3. Registry bundling's effect on the observer lies within ±1 point in every cell | Confirmed (-0.20 to +0.04). |
| M4. Registry bundling lowers the validator's device accuracy in every cell | Confirmed (-1.15 to -0.38). |

M1 to M4 follow development runs, as the plan discloses. M1 did not anticipate that most of the drop would come from a larger candidate set; that finding is reported in summary point 2.

## Scope

- **Window.** The 120-second registry window is sized to the 40-decoy target at R = 1. At the low end of the 40 ± 10 range (30 decoys), 0.33% of bundles would hold fewer than two transactions; about 150 seconds meets the 0.1% criterion there.
- **One shared schedule.** Every content server uses one registry bundle schedule.
- **Record time.** The observer times a record by its gossiped submissions. The registry's coarsened timestamp is not modelled.

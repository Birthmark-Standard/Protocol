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

# Gatekeeper occupancy and the registry bundling window

Plan section 6e. The two-point gatekeeper hold is dropped; every build below uses the relay-lottery gatekeeper hold of the push build. Full tables in `results/tables_reg60.md`, `results/tables.md` (120 s, the default build), `results/tables_reg240.md` and `results/tables_reg480.md`; checks in `results/checks.json` and `results/checks.log` (run on the 120-second build).

## Summary

1. **A gatekeeper holds about 7 packets at a time at the 40-decoy target, not 40.** A transaction spends about 106 of its 626 seconds at a gatekeeper, so the gatekeeper's own load is its arrival rate (0.066 per second) times its hold, 7.0. It selects 0.66 packets per 10-second tick, against the 3.33 the specification derived. Reaching the specification's 30-second bundle of 10 with under 0.1% degenerate bundles needs about 200 decoys in flight, or a window of about 150 seconds at 40 decoys.
2. **The registry window wears down the validator's edge, slowly at first.** At R = 1 with 40 decoys, the validator's contribution over the passive observer is 1.19 points without registry bundling, 1.15 at 60 seconds, 1.09 at 120, 0.88 at 240 and 0.35 at 480.
3. **The 120-second window does less on its own than section 6d suggested.** On the push build, it lowers the validator by 0.10 to 0.36 points. Section 6d measured 0.38 to 1.15 points, but against the two-point build, whose hold had first raised the validator's edge.
4. **A longer window strengthens the content server.** Its contribution over the observer at R = 1 with 40 decoys rises from 0.83 points without registry bundling to 1.41 at 480 seconds, so at 480 seconds the content server replaces the validator as the strongest single component. The content server knows when its own submission was confirmed, which the observer loses inside the window.
5. **The passive observer's absolute accuracy falls only at long windows, and its multiple of random barely moves.** At 480 seconds it loses 0.69 to 2.02 points, but the random rate falls with it. At R = 1 its multiple of random stays inside the push interval (4.04 [3.82, 4.26] against 4.16 [3.98, 4.34] at 40 decoys); at R = 50 it falls below it (4.55 [4.43, 4.67] against 4.77 [4.66, 4.88]).
6. **Latency grows by about half the window.** Mean capture to finalization at R = 1 with 40 decoys: 625.5 seconds without registry bundling, 656.0 at 60 seconds, 684.0 at 120, 744.8 at 240 and 861.2 at 480.

## Gatekeeper occupancy

Each active gatekeeper, under the push build at R = 1 (`results/gatekeeper_occupancy.json`, 50 runs per decoy target):

| Decoys in flight | Arrivals per second | Mean hold | Held at once (5th to 95th percentile) | Selections per 10 s tick | Postings per 30 s bundle | 30 s bundles with fewer than 2 |
|---|---|---|---|---|---|---|
| 20 | 0.034 | 106.1 s | 3.6 (1 to 7) | 0.34 | 1.0 | 73.2% |
| 30 | 0.050 | 106.2 s | 5.3 (2 to 9) | 0.50 | 1.5 | 56.0% |
| 40 | 0.066 | 106.4 s | 7.0 (3 to 12) | 0.66 | 2.0 | 41.2% |
| 50 | 0.082 | 106.4 s | 8.7 (4 to 14) | 0.82 | 2.5 | 29.8% |
| 60 | 0.098 | 106.2 s | 10.4 (5 to 16) | 0.98 | 2.9 | 21.1% |
| 100 | 0.162 | 106.1 s | 17.1 (11 to 24) | 1.62 | 4.8 | 4.5% |
| 150 | 0.242 | 106.2 s | 25.7 (18 to 34) | 2.42 | 7.2 | 0.61% |
| 175 | 0.281 | 105.9 s | 29.8 (21 to 39) | 2.81 | 8.4 | 0.19% |
| 200 | 0.321 | 106.2 s | 34.1 (25 to 44) | 3.22 | 9.6 | 0.07% |
| 250 | 0.402 | 106.2 s | 42.7 (32 to 54) | 4.02 | 12.1 | under 0.01% |
| 300 | 0.482 | 106.4 s | 51.2 (40 to 63) | 4.82 | 14.5 | under 0.01% |

The held count equals the arrival rate times the mean hold in every row, as it must for a stable queue.

Share of gatekeeper bundles with fewer than two postings, by window:

| Decoys | 30 s | 60 s | 90 s | 120 s | 135 s | 150 s | 180 s | 240 s |
|---|---|---|---|---|---|---|---|---|
| 30 | 56.0% | 20.0% | 5.9% | 1.7% | 0.85% | 0.30% | 0.13% | under 0.01% |
| 40 | 41.2% | 9.6% | 2.0% | 0.37% | 0.18% | 0.06% | under 0.01% | under 0.01% |
| 50 | 29.8% | 4.4% | 0.51% | 0.08% | 0.04% | 0.01% | under 0.01% | under 0.01% |

What the specification's criterion (mean about 10, under 0.1% of bundles below two) needs at the gatekeeper:
- **At the 30-second window:** about 200 decoys in flight (0.07% at 200, 0.19% at 175).
- **At 40 decoys:** a 150-second window (0.06%). That adds about 60 seconds of mean wait over the 30-second window.
- **At 30 decoys, the low end of 40 ± 10:** about 200 seconds (0.13% at 180, under 0.01% at 240).
- **At 50 decoys:** a 120-second window (0.08%).

Gatekeeper bundling changed no vantage's accuracy by more than half a point in the bundling sweep, because board postings are internal and the observer never sees a gatekeeper departure. A larger gatekeeper bundle would add latency without a measured gain in this model, unless postings were observable.

## The registry bundling window

Each window is compared against the push build on the same records.

### The validator and the content server

Contribution over the passive observer, device level, at R = 1 with 40 decoys [95% CI]:

| Window | Validator | Content server |
|---|---|---|
| none (push) | +1.19 [+0.90, +1.50] | +0.83 |
| 60 s | +1.15 [+0.79, +1.49] | +0.89 |
| 120 s | +1.09 [+0.76, +1.42] | +0.93 |
| 240 s | +0.88 [+0.50, +1.26] | +1.06 |
| 480 s | +0.35 [+0.01, +0.68] | +1.41 |

At 480 seconds the validator's contribution interval reaches 0 at R = 15 with 40 decoys (+0.14 [-0.10, +0.39]). Every other vantage stays within 0.13 points of the observer at every window.

### Paired effect of each window against push

Device level, in points, the range across the nine cells:

| Vantage | 60 s | 120 s | 240 s | 480 s |
|---|---|---|---|---|
| Baseline | -0.19 to +0.11 | -0.18 to +0.03 | -0.62 to -0.20 | -2.02 to -0.69 |
| First hop, credential | -0.14 to +0.07 | -0.17 to -0.02 | -0.66 to -0.25 | -2.05 to -0.67 |
| Credential processor | -0.16 to +0.09 | -0.16 to +0.01 | -0.59 to -0.23 | -1.99 to -0.68 |
| Content server | -0.10 to +0.07 | -0.19 to -0.03 | -0.54 to -0.12 | -1.48 to -0.41 |
| Validator | -0.11 to +0.03 | -0.36 to -0.10 | -1.17 to -0.35 | -3.42 to -1.14 |
| Gatekeeper | -0.15 to +0.16 | -0.22 to -0.00 | -0.56 to -0.22 | -2.10 to -0.70 |

The first hop for content matches the first hop for credentials to within 0.01 points. At 240 and 480 seconds every vantage's interval lies wholly below 0 in all nine cells.

### The passive observer

Device accuracy, random-pick rate, and accuracy as a multiple of the random rate [95% CI]:

| Window | R = 1, 40 decoys | R = 15, 40 decoys | R = 50, 40 decoys |
|---|---|---|---|
| none (push) | 8.65%, 2.08%, ×4.16 [3.98, 4.34] | 6.92%, 1.55%, ×4.47 [4.31, 4.65] | 4.54%, 0.95%, ×4.77 [4.66, 4.88] |
| 60 s | 8.63%, 2.04%, ×4.22 [4.04, 4.41] | 6.73%, 1.52%, ×4.42 [4.25, 4.60] | 4.47%, 0.93%, ×4.78 [4.66, 4.90] |
| 120 s | 8.52%, 2.05%, ×4.14 [3.97, 4.32] | 6.76%, 1.53%, ×4.42 [4.26, 4.59] | 4.48%, 0.94%, ×4.77 [4.65, 4.88] |
| 240 s | 8.03%, 1.91%, ×4.21 [4.02, 4.41] | 6.46%, 1.42%, ×4.55 [4.37, 4.73] | 4.27%, 0.87%, ×4.90 [4.77, 5.01] |
| 480 s | 7.19%, 1.78%, ×4.04 [3.82, 4.26] | 5.83%, 1.32%, ×4.40 [4.21, 4.60] | 3.70%, 0.81%, ×4.55 [4.43, 4.67] |

As with the two-point hold, a longer delay leaves more devices feasible for each record, so the random rate falls with the observer's accuracy. At 240 seconds the multiple rises slightly; at 480 seconds it falls, outside the push interval only at R = 50.

### Bundle sizes

Distinct transactions per registry bundle, and the share of bundles with fewer than two, over the sweep's own runs (`results/registry_bundles_reg<window>.json`):

| R | Decoys | 60 s | 120 s | 240 s | 480 s |
|---|---|---|---|---|---|
| 1 | 20 | 2.8 (22.6%) | 5.4 (2.9%) | 10.1 (0.056%) | 18.4 (under 0.001%) |
| 1 | 40 | 5.5 (2.6%) | 10.6 (0.032%) | 19.6 (under 0.001%) | 36.0 (under 0.001%) |
| 1 | 60 | 8.2 (0.25%) | 15.7 (under 0.001%) | 29.2 (under 0.001%) | 53.6 (under 0.001%) |
| 15 | 40 | 7.5 (0.50%) | 14.3 (under 0.001%) | 26.5 (under 0.001%) | 48.5 (under 0.001%) |
| 50 | 40 | 12.1 (0.006%) | 23.1 (under 0.001%) | 43.0 (under 0.001%) | 78.6 (under 0.001%) |

The bundle-size histogram is capped at 127 submissions, so the 480-second means at R = 50 are lower bounds. Every other cell is in the JSON files.

### Latency

Capture to registry finalization at 40 decoys (`results/latency.json`, 20 runs per cell), mean / median / 95th percentile:

| Window | R = 1 | R = 15 | R = 50 | Mean registry wait, R = 1 |
|---|---|---|---|---|
| none (push) | 625.5 / 618.2 / 892.2 s | 633.0 / 622.0 / 898.5 s | 628.1 / 618.7 / 889.7 s | 0 |
| 60 s | 656.0 / 648.1 / 921.5 s | 663.5 / 652.9 / 931.3 s | 658.0 / 648.0 / 919.5 s | 31.2 s |
| 120 s | 684.0 / 675.6 / 955.6 s | 693.3 / 683.1 / 958.8 s | 686.9 / 679.0 / 953.9 s | 61.2 s |
| 240 s | 744.8 / 736.6 / 1029.9 s | 754.7 / 744.2 / 1044.7 s | 748.2 / 742.2 / 1033.2 s | 127.1 s |
| 480 s | 861.2 / 856.0 / 1209.8 s | 872.7 / 867.6 / 1213.6 s | 866.2 / 862.8 / 1211.2 s | 252.6 s |

The mean added latency is a little under half the window. The registry wait is counted on the later of the two content servers, and part of it overlaps time that server would otherwise spend waiting for its own hold.

## Trade-off at R = 1 with 40 decoys

| Window | Mean latency added | Validator's edge removed | Content server's edge added | Observer, multiple of random |
|---|---|---|---|---|
| 60 s | 30.5 s | 0.04 points | 0.06 points | ×4.22 |
| 120 s | 58.5 s | 0.10 points | 0.10 points | ×4.14 |
| 240 s | 119.3 s | 0.31 points | 0.23 points | ×4.21 |
| 480 s | 235.7 s | 0.84 points | 0.58 points | ×4.04 |

The largest single-component edge over the observer is 1.19 points (validator) without registry bundling, 1.09 (validator) at 120 seconds, 1.06 (content server) at 240 seconds, and 1.41 (content server) at 480 seconds. The strongest single component's edge is lowest at 240 seconds, though the 120- and 240-second values differ by less than their intervals.

## Checks and controls

- **Pre-run checks** (120-second build): every registry submission departs on the shared grid, 2.3 to 119.4 seconds after confirmation (check 9). Check 8 does not apply. Every other check passes except the same marginal baseline failure as before (D's hold, AUC 0.488 [0.476, 0.500]).
- **Outcome-shuffle control:** 6, 5, 1 and 4 of 63 stable cells at 60, 120, 240 and 480 seconds have a shuffled-outcome AUC interval excluding 0.5, all within the plan's 0.03 margin (largest 0.515).

## Predictions

| Prediction | Outcome |
|---|---|
| W1. At 60 and 120 seconds, the observer's effect against push within ±1 point in every cell | Confirmed (-0.19 to +0.11). |
| W2. At 480 seconds, the observer's effect against push below 0 in every cell | Confirmed (-2.02 to -0.69). |
| W3. The validator's effect more negative at 480 than at 120 seconds in at least 7 of 9 cells | Confirmed in all 9. |
| W4. At 480 seconds, the observer's multiple of random below its push value in at least 6 of 9 cells | Confirmed in 8 of 9; the exception is R = 1 with 20 decoys (×3.53 against ×3.52). Most of the differences lie inside the push intervals. |

W1 to W4 follow development runs, as the plan discloses. The plan did not predict the content server's rise with the window; it is reported in summary point 4.

## Scope

- **One shared schedule** for every content server, as in section 6d.
- **Rates** are those of the push build. Longer windows hold more transactions in flight in each cell.
- **The sensitivity control** was not rerun for these builds.

## Correction: the strongest component in absolute terms

The trade-off table above ranks windows by each component's edge over the passive observer. That edge is not the quantity the claim is about. Measured by the strongest single component's own accuracy, and as a multiple of its own random-pick rate [95% CI], the ranking changes:

| Window | R = 1, 40 decoys | R = 15, 40 decoys | R = 50, 40 decoys |
|---|---|---|---|
| none (push) | validator 9.85%, ×3.92 [3.77, 4.06] | validator 7.98%, ×4.28 [4.15, 4.40] | validator 5.26%, ×4.58 [4.48, 4.68] |
| 60 s | validator 9.78%, ×3.99 [3.84, 4.14] | validator 7.98%, ×4.38 [4.24, 4.52] | validator 5.20%, ×4.64 [4.54, 4.74] |
| 120 s | validator 9.61%, ×4.06 [3.90, 4.23] | validator 7.84%, ×4.46 [4.32, 4.61] | validator 5.09%, ×4.71 [4.61, 4.80] |
| 240 s | content server 9.09%, ×3.84 [3.71, 3.97] | content server 7.39%, ×4.19 [4.05, 4.34] | content server 4.91%, ×4.54 [4.46, 4.62] |
| 480 s | content server 8.60%, ×3.72 [3.58, 3.85] | content server 6.93%, ×4.02 [3.89, 4.16] | content server 4.60%, ×4.35 [4.28, 4.43] |

- In absolute accuracy, the strongest component falls at every window, and furthest at 480 seconds.
- As a multiple of its own random rate, the strongest component does not improve at 60 or 120 seconds (the validator's random rate falls with its accuracy), improves slightly at 240 seconds, and improves most at 480 seconds. At R = 50, the 480-second interval lies wholly below the push interval.
- The 480-second result is therefore not a regression in the strongest component's accuracy. What grows at 480 seconds is the content server's lead over the passive observer, because the observer loses more than the content server does.

The statement above that the strongest component's edge is lowest at 240 seconds holds for the edge over the observer only.

## Why the content server gains on the observer at long windows (exploratory)

This diagnostic was run after the window sweep and is not pre-registered (`python -m sna diag-cs`, `results/diag_content_server.json`, run ids 0 to 39 of the sweep, each build's own models).

**Hypothesis.** The content server holds two independent sources of timing evidence about which device produced a record:
1. the record time, which the passive observer also has;
2. its own content arrival, which only it has.

The record time comes at the end of the credential path, which carries five lottery holds (device, A, B, the credential processor's fan-out, the gatekeeper) and, with registry bundling, the registry wait. The content arrival comes at the end of the content path, after three holds (device, D, E). Registry bundling degrades the first source and leaves the second untouched. At long windows the record time weakens below the content arrival, the content server leans on its private source, and its lead over the observer grows even as its own accuracy falls.

**Test.** The diagnostic scores the content server's rows three ways: with both sources (as in the sweep), with the record time alone, and with the content arrival alone. Device accuracy at 40 decoys:

| Build | R = 1: both / record time alone / arrival alone | R = 15: both / record time alone / arrival alone |
|---|---|---|
| push | 9.69% / 8.74% / 8.16% | 7.99% / 7.19% / 6.50% |
| 120 s | 9.99% / 8.50% / 8.16% | 7.89% / 7.08% / 6.50% |
| 240 s | 9.69% / 8.68% / 8.16% | 7.67% / 6.71% / 6.50% |
| 480 s | 8.77% / 6.94% / 8.16% | 7.12% / 5.71% / 6.50% |

- The arrival-alone score is identical at every window, as it must be: the content path does not depend on the registry schedule.
- The record-time-alone score falls with the window and drops below the arrival-alone score at 480 seconds, at both volumes.
- The content server's combined score tracks the stronger of the two.

The hypothesis is consistent with every row. Over 40 runs, the differences between push, 120 and 240 seconds lie within run-to-run noise.

**Consequences.**
- **A floor for registry-side mechanisms.** No change downstream of the content servers can bring the content server below its arrival-alone accuracy: 8.16% at R = 1 with 40 decoys, about 3.6 times its random-pick rate. A registry window, a coarser registry timestamp or any added registry delay can only remove the record-time source.
- **What would wake it.** Anything that blurs the record time more than the content arrival raises the content server's lead over the observer: a longer registry window; the registry's coarsened timestamp, if an observer had to rely on it instead of the gossiped submissions (the simulator does not model the coarsening); or more delay or variance between quorum and submission.
- **What would counter it.** Only changes on the content path itself, before the content server: more or longer holds at the device's content hold, D or E. The content server's own hold comes after arrival and does not touch this source.

## Relay lottery: current parameters

The starting point for any change to the relay holds (`sna/params.py`, `sna/lottery.py`).

| Parameter | Value |
|---|---|
| Tick | 10 s |
| Release probability per tick | 8.33% |
| Forced release | tick 30 (300 s cap) |
| Clock | one clock per node with a random phase; each gatekeeper holds on a dedicated clock; a device holds each of its three channels on a fresh random phase |
| Holds on the credential path | device, A, B, the credential processor's fan-out (one draw per gatekeeper leg), gatekeeper |
| Holds on each content path | device, D (or G), E (or H), then the content server after arrival |
| One hold, in isolation | mean 106.2 s, standard deviation 89.0 s, median 79.7 s, 95th percentile 293.7 s, coefficient of variation 0.84 |
| Share released by the forced cap | 8.0% (0.9167^29) |

Measured per stage in the simulator (R = 15, 40 decoys, 120-second registry window, 10 runs on run ids from 5,000,000 up):

| Stage | Mean | SD | Median | 95th percentile |
|---|---|---|---|---|
| Device hold, credential channel | 105.0 s | 88.6 s | 78.6 s | 294.2 s |
| A | 103.8 s | 88.6 s | 76.7 s | 293.2 s |
| B | 105.3 s | 88.4 s | 79.7 s | 293.9 s |
| Credential processor fan-out | 107.4 s | 89.9 s | 80.5 s | 294.0 s |
| Gatekeeper | 107.0 s | 88.7 s | 80.8 s | 293.6 s |
| Device hold, content channel | 107.8 s | 89.8 s | 80.6 s | 293.9 s |
| D | 107.0 s | 90.1 s | 78.0 s | 294.3 s |
| E | 107.3 s | 89.8 s | 82.4 s | 294.0 s |
| Content server hold | 104.3 s | 88.2 s | 78.8 s | 294.0 s |
| Content server: hold release to quorum push | 165.7 s | 182.0 s | 110.6 s | 527.8 s |
| Registry wait (120 s window) | 58.2 s | 34.4 s | 60.0 s | 112.1 s |
| Capture to record time (the observer's y) | 649.6 s | 149.2 s | 640.4 s | 907.8 s |

- The content packet usually waits at the content server for quorum (about 166 seconds on average after its own hold), so the record time is set by the credential path.
- The 8% point mass at the 300-second cap is present in every hold. It is the same shape the two-point gatekeeper hold placed at the cap with 40% weight.

# Decoy targets from 20 to 150

Plan section 6f. The 30-, 100- and 150-decoy cells were run on a second machine (`results/extra/`); the 20-, 40- and 60-decoy cells are those of section 6e. Results depend only on the cell, the build and the run id. Both builds use board pushes, gatekeeper departure bundling and the relay-lottery gatekeeper hold; reg120 and reg480 differ only in the registry window. 200 runs per cell; every cell met the stability rule.

## Summary

1. **Raising the decoy target lowers every component's absolute accuracy steadily.** At R = 1 under the 120-second window, the strongest single component names the device 12.2% of the time at 30 decoys, 9.6% at 40, 6.9% at 60, 4.6% at 100 and 3.3% at 150.
2. **The multiple over random rises as decoys rise.** More decoys lower the random-pick rate faster than they lower accuracy. At R = 1 under the 120-second window, the passive observer is 3.9 times random at 30 decoys and 5.0 times at 150. A higher decoy target makes a record harder to trace in absolute terms, while each component's advantage over guessing grows.
3. **The low end of 40 ± 10 costs about 2.6 points.** At 30 decoys and R = 1, the strongest component names the device 12.2% of the time (120-second window) or 10.9% (480-second window), against 9.6% and 8.6% at 40.
4. **The 480-second window beats the 120-second window on the strongest component in all 18 cells**, in accuracy and as a multiple of random. The content server is the strongest component under 480 seconds in every cell, and the validator's lead over the observer falls to between -0.08 and +0.61 points.

## The strongest single component

Device accuracy and multiple of its own random rate [95% CI]:

| R | Decoys | 120 s window | 480 s window |
|---|---|---|---|
| 1 | 20 | content server 15.98%, ×3.34 [3.26, 3.42] | content server 14.67%, ×3.23 [3.15, 3.32] |
| 1 | 30 | validator 12.22%, ×3.91 [3.77, 4.05] | content server 10.89%, ×3.56 [3.44, 3.68] |
| 1 | 40 | validator 9.61%, ×4.06 [3.90, 4.23] | content server 8.60%, ×3.72 [3.58, 3.85] |
| 1 | 60 | validator 6.90%, ×4.33 [4.12, 4.53] | content server 6.13%, ×3.93 [3.76, 4.09] |
| 1 | 100 | validator 4.56%, ×4.74 [4.41, 5.07] | content server 4.02%, ×4.27 [4.03, 4.51] |
| 1 | 150 | validator 3.30%, ×5.13 [4.74, 5.52] | content server 2.94%, ×4.66 [4.37, 4.97] |
| 15 | 20 | validator 10.96%, ×3.96 [3.85, 4.07] | content server 10.00%, ×3.69 [3.59, 3.79] |
| 15 | 30 | content server 9.16%, ×4.13 [4.01, 4.24] | content server 8.25%, ×3.93 [3.83, 4.04] |
| 15 | 40 | validator 7.84%, ×4.46 [4.32, 4.61] | content server 6.93%, ×4.02 [3.89, 4.16] |
| 15 | 60 | validator 6.15%, ×4.77 [4.56, 4.98] | content server 5.47%, ×4.32 [4.16, 4.48] |
| 15 | 100 | validator 4.37%, ×5.18 [4.95, 5.41] | content server 3.80%, ×4.61 [4.38, 4.83] |
| 15 | 150 | validator 3.26%, ×5.54 [5.21, 5.85] | content server 2.74%, ×4.76 [4.49, 5.04] |
| 50 | 20 | validator 6.35%, ×4.56 [4.48, 4.64] | content server 5.70%, ×4.18 [4.11, 4.25] |
| 50 | 30 | validator 5.64%, ×4.64 [4.55, 4.73] | content server 5.07%, ×4.26 [4.17, 4.34] |
| 50 | 40 | validator 5.09%, ×4.71 [4.61, 4.80] | content server 4.60%, ×4.35 [4.28, 4.43] |
| 50 | 60 | validator 4.32%, ×4.89 [4.76, 5.01] | content server 3.85%, ×4.44 [4.35, 4.54] |
| 50 | 100 | validator 3.30%, ×5.09 [4.93, 5.24] | content server 2.95%, ×4.64 [4.52, 4.77] |
| 50 | 150 | validator 2.58%, ×5.30 [5.12, 5.48] | content server 2.30%, ×4.83 [4.67, 4.99] |

## The passive observer

Device accuracy, random-pick rate, and multiple of random [95% CI], at R = 1:

| Decoys | 120 s window | 480 s window |
|---|---|---|
| 20 | 14.26%, 4.03%, ×3.54 [3.43, 3.65] | 12.32%, 3.49%, ×3.53 [3.39, 3.67] |
| 30 | 10.57%, 2.72%, ×3.89 [3.75, 4.03] | 9.04%, 2.35%, ×3.85 [3.66, 4.02] |
| 40 | 8.52%, 2.05%, ×4.14 [3.97, 4.32] | 7.19%, 1.78%, ×4.04 [3.82, 4.26] |
| 60 | 5.98%, 1.39%, ×4.32 [4.09, 4.54] | 4.99%, 1.20%, ×4.16 [3.90, 4.42] |
| 100 | 4.01%, 0.84%, ×4.80 [4.46, 5.13] | 3.43%, 0.72%, ×4.74 [4.36, 5.12] |
| 150 | 2.80%, 0.56%, ×5.00 [4.57, 5.43] | 2.35%, 0.48%, ×4.85 [4.35, 5.34] |

Every cell, and R = 15 and 50, is in `results/extra/tables.md`, `results/extra/tables_reg480.md` and the section 6e tables.

## Effect of the 480-second window against the 120-second window

Device level, in points [95% CI], matched record by record:

| R | Decoys | Passive observer | Content server | Validator |
|---|---|---|---|---|
| 1 | 30 | -1.52 [-1.87, -1.19] | -0.85 [-1.10, -0.61] | -2.73 [-3.14, -2.33] |
| 1 | 100 | -0.58 [-0.81, -0.36] | -0.32 [-0.47, -0.17] | -1.20 [-1.48, -0.92] |
| 1 | 150 | -0.45 [-0.65, -0.25] | -0.19 [-0.32, -0.05] | -0.90 [-1.15, -0.66] |
| 15 | 30 | -0.97 [-1.23, -0.75] | -0.90 [-1.08, -0.72] | -1.90 [-2.18, -1.61] |
| 15 | 100 | -0.42 [-0.59, -0.24] | -0.28 [-0.40, -0.17] | -1.05 [-1.27, -0.82] |
| 15 | 150 | -0.42 [-0.60, -0.25] | -0.31 [-0.42, -0.21] | -0.93 [-1.12, -0.74] |
| 50 | 30 | -0.80 [-0.90, -0.70] | -0.45 [-0.53, -0.36] | -1.26 [-1.37, -1.15] |
| 50 | 100 | -0.54 [-0.63, -0.45] | -0.22 [-0.29, -0.15] | -0.78 [-0.89, -0.68] |
| 50 | 150 | -0.37 [-0.44, -0.29] | -0.18 [-0.25, -0.12] | -0.62 [-0.71, -0.53] |

The content server loses the least in every cell, which is why it becomes the strongest component at 480 seconds, as the diagnostic above explains.

## Registry bundle sizes

Distinct transactions per bundle, and the share with fewer than two (`results/extra/registry_bundles_reg<window>.json`):

| R | Decoys | 120 s | 480 s |
|---|---|---|---|
| 1 | 30 | 8.0 (0.30%) | 27.2 (under 0.001%) |
| 1 | 100 | 26.1 (under 0.001%) | 88.6 (under 0.001%) |
| 1 | 150 | 39.0 (under 0.001%) | 124.7 (under 0.001%) |
| 15 | 30 | 11.7 (0.011%) | 39.7 (under 0.001%) |
| 50 | 30 | 20.5 (under 0.001%) | 69.9 (under 0.001%) |

The histogram is capped at 127 submissions, so the largest 480-second means are lower bounds.

## Checks and controls

- **Outcome-shuffle control:** 6 of 63 stable cells under the 120-second window and 3 of 63 under the 480-second window have a shuffled-outcome AUC interval excluding 0.5, all within the plan's 0.03 margin (largest 0.515).

## Predictions

| Prediction | Outcome |
|---|---|
| X1. At R = 1, the observer at 30 decoys lies between its 20- and 40-decoy values, in both builds | Confirmed: 10.57% (120 s) and 9.04% (480 s). |
| X2. The observer is lower at 150 than at 100 decoys at every R, in both builds | Confirmed in all 6. |
| X3. Under 120 s, the observer's multiple of random at 150 decoys is at least its 40-decoy value at R = 1 and 15 | Confirmed: ×5.00 against ×4.14, and ×5.21 against ×4.42. |
| X4. The 480-second window lowers the validator against 120 seconds in every cell | Confirmed (-2.73 to -0.62). |
| X5. Under 480 s, the content server is the strongest component in at least 7 of 9 cells | Confirmed in all 9, and in all 9 cells of section 6e as well. |

X1 to X5 follow development runs, as the plan discloses.

# Parameter decisions and the code behind them

## Decisions

| Parameter | Setting | Decided on |
|---|---|---|
| Registry-level bundling window | 120 s, one schedule shared by every content server | the author's decision, final |
| Decoy target | 40 ± 10 in flight, a flat rate independent of real traffic | the specification; raising it is under consideration |
| Gatekeeper departure bundling | 30 s window on each gatekeeper's own grid | the specification |
| Board push | every 10 s, each board on its own schedule | this build's choice for the specification's "regularly" |
| Gatekeeper hold | the relay lottery (the two-point hold is dropped) | section 6e |

The registry window was decided with these results in view: under the 480-second window the strongest single component is lower than under the 120-second window in all 18 cells measured, in accuracy and as a multiple of random, at about 177 seconds more mean latency at 40 decoys. The 120-second window is the chosen setting.

## Provenance of every result behind these decisions

Every result used for these decisions was produced by code committed to this repository and present on `main`. No result comes from an uncommitted, interim or background version of the program. Each sweep ran against the commit named below; its results were committed afterwards.

| Decision informed | Sweep | Code commit | Results commit | Run on |
|---|---|---|---|---|
| Gatekeeper departure bundling | section 6b | `e0709ec` | `0fb1fc2` | the analysis container |
| Board push | section 6c | `a0cde30` | `c5ada93` | the analysis container |
| Two-point gatekeeper hold (dropped) | section 6d | `df09686` | `f997284` | the analysis container |
| Registry window: 60, 120, 240 and 480 s, 20 to 60 decoys | section 6e | `70b4aae` | `39891f0`, `f7da551` | the analysis container |
| Registry window and decoy target: 30, 100 and 150 decoys | section 6f | `e9f27ab` | `10c5c17` | the author's machine |

- The simulator and the attacks (`sna/sim.py`, `sna/attacks.py`, `sna/params.py`, `sna/lottery.py`) are unchanged from `df09686` through `10c5c17`. The changes in between touch only the cell grid, the command line, the reports and an exploratory diagnostic. So the section 6e and 6f sweeps ran the same simulator and attack code, on two machines.
- Every result depends only on the cell, the build and the run id, never on the worker count. Across the two machines (Linux and Windows) results agree to within floating-point ties: section 6h reran the reg120 and content200 cells on the second machine, and content200 matched every decision while reg120 differed in 1 of 172,650 passive-observer decisions (R = 50) and 1 credential-processor claim (R = 1). Resampled intervals also differ slightly when a different set of cells is analysed together, because the resampling draws are taken in cell order.
- The two 480-second sweeps agree with each other. Under 480 seconds the content server is the strongest component in every cell of both, with a lead over the passive observer of 0.90 to 2.34 points.
- The re-analysis below (section "Precision at coverage") adds metrics without changing any existing value; it was checked field by field against the committed summaries.

# Zero-access baseline

Every random-pick rate above is random among the devices feasible for a record, which already assumes knowledge of which devices could have produced it. The zero-access baseline needs no such knowledge: a guess among every registered device, 1/N.

In this model N is the number of identities that capture during a run: real devices (R / D × 1,200 seconds, each capturing every 20 minutes on average) plus the decoy infrastructure's identities (decoys / D × 1,200 seconds). A deployment with many registered devices that rarely capture would have a far larger N, so the zero-access multiples below are specific to this model's device population.

Under the 120-second window, device level:

| R | Decoys | Registered devices N | 1/N | Observer | Observer × N | Observer, feasible-set multiple | Strongest component | Its × N | Its feasible-set multiple |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 20 | 40 | 2.50% | 14.26% | 5.7 | 3.54 | content server 15.98% | 6.4 | 3.34 |
| 1 | 30 | 60 | 1.67% | 10.57% | 6.3 | 3.89 | validator 12.22% | 7.3 | 3.91 |
| 1 | 40 | 79 | 1.27% | 8.52% | 6.7 | 4.14 | validator 9.61% | 7.6 | 4.06 |
| 1 | 60 | 117 | 0.85% | 5.98% | 7.0 | 4.32 | validator 6.90% | 8.1 | 4.33 |
| 1 | 100 | 194 | 0.52% | 4.01% | 7.8 | 4.80 | validator 4.56% | 8.8 | 4.74 |
| 1 | 150 | 290 | 0.34% | 2.80% | 8.1 | 5.00 | validator 3.30% | 9.6 | 5.13 |
| 15 | 40 | 106 | 0.94% | 6.76% | 7.2 | 4.42 | validator 7.84% | 8.3 | 4.46 |
| 15 | 150 | 317 | 0.32% | 2.66% | 8.4 | 5.21 | validator 3.26% | 10.3 | 5.54 |
| 50 | 40 | 173 | 0.58% | 4.48% | 7.7 | 4.77 | validator 5.09% | 8.8 | 4.71 |
| 50 | 150 | 384 | 0.26% | 2.17% | 8.3 | 5.13 | validator 2.58% | 9.9 | 5.30 |

Every cell is in `results/zero_access.json`.

- **The zero-access multiple rises with the decoy target, as the feasible-set multiple does.** It does not behave oppositely. At R = 1 the observer's zero-access multiple rises from 5.7 at 20 decoys to 8.1 at 150.
- **The reason:** N grows in proportion to the decoy rate, while accuracy falls more slowly than in proportion. Each added decoy identity enlarges both baselines' denominators by about one, and takes less than its share of the attacker's correct guesses.
- **The zero-access multiple is larger than the feasible-set multiple**, by a factor of 1.6 to 1.9. Knowing the feasible set is worth that much to a guesser on its own.

# Precision at coverage

Each vantage's calibrated confidence ranks its decisions. Precision at coverage q is the share of correct decisions among its most confident q of decisions [95% CI]. The largest coverage at more than 50% precision is the largest share of decisions, taken most confident first, that are right more often than not. These metrics are computed in every sweep; they are reported here at the settled configuration (120-second window, 40 decoys), with 10% and 25% coverage added.

R = 1, 40 decoys:

| Vantage | Accuracy (every decision) | Precision, top 1% | Top 5% | Top 10% | Top 25% | Decisions above 50% precision | AUC |
|---|---|---|---|---|---|---|---|
| Baseline | 8.52% | 14.0% [10.9, 17.7] | 13.2% [11.8, 14.8] | 12.7% | 11.5% | 0 of 39,962 | 0.569 |
| First hop, credential | 8.50% | 15.5% [13.8, 17.3] | 13.2% [12.5, 13.9] | 12.6% | 11.4% | 0 of 159,848 | 0.571 |
| First hop, content | 8.50% | 15.5% [13.8, 17.3] | 13.2% [12.5, 13.9] | 12.6% | 11.4% | 0 of 159,848 | 0.571 |
| Credential processor | 8.57% | 14.4% [12.8, 16.2] | 13.0% [12.3, 13.8] | 12.8% | 11.4% | 0 of 159,848 | 0.568 |
| Content server | 9.45% | 10.9% [8.9, 13.2] | 13.3% [12.2, 14.4] | 12.9% | 12.2% | 0 of 79,924 | 0.566 |
| Validator | 9.61% | 18.5% [15.0, 22.6] | 15.2% [13.7, 16.9] | 14.5% | 12.9% | 3 of 39,962 | 0.574 |
| Gatekeeper | 8.47% | 14.4% [12.6, 16.5] | 13.4% [12.6, 14.3] | 13.0% | 11.3% | 0 of 119,886 | 0.570 |

At R = 15 and R = 50 with 40 decoys, the highest top-1% precision of any vantage is 14.6% [11.8, 17.9] and 9.8% [8.5, 11.3] (the validator), and at most 1 decision per vantage exceeds 50% precision. Every cell is in `results/tables.md`.

Across decoy targets at R = 1 (120-second window), the highest top-1% precision of any vantage:

| Decoys | 20 | 30 | 40 | 60 | 100 | 150 |
|---|---|---|---|---|---|---|
| Highest top-1% precision | 32.5% (validator) | 25.2% (observer) | 18.5% (validator) | 13.2% (validator) | 7.8% (credential processor) | 5.3% (first hop, credential) |
| Decisions above 50% precision, any vantage | 0.058% | 0.053% | 0.008% | 0 | 0 | 0 |

- **This supports a stronger claim than accuracy over random.** At the settled configuration, a compromised component that acts only on its most confident 1% of decisions is still wrong at least 77% of the time (the validator's 18.5% upper bound is 22.6%), and no component is right more often than not on more than 3 of about 40,000 decisions.
- **Confidence buys the attacker little.** The most confident 1% of a vantage's decisions are at most about twice as accurate as its average decision (0.8 to 2.0 times across vantages at 40 decoys); the AUC of confidence against correctness lies between 0.539 and 0.574 in every vantage and cell at 40 decoys.
- **The content server's confidence ranks poorly**: its top 1% is less precise than its top 5%, and at R = 50 less precise than its average decision.

# Longer device and relay holds

Plan section 6g. Every build has the 120-second registry window, gatekeeper departure bundling, board pushes and the relay-lottery gatekeeper hold. Device and relay-hop holds are stretched by k (release probability 8.33% / k, cap at tick 30k), on every path (hold150, hold200, hold300) or on the content paths only (content200, content300). R = 1, 15 and 50 at 40 decoys; 200 runs per cell; every cell met the stability rule. Each build is compared with reg120 on the same records. Full tables in `results/tables_hold150.md`, `tables_hold200.md`, `tables_hold300.md`, `tables_content200.md` and `tables_content300.md`.

## Summary

1. **Stretching only the content-path holds removes every component's advantage over the passive observer.** Under content300, no vantage beats the observer in any cell (the largest contribution over the observer is +0.00 points); under content200 the largest is +0.01. Under reg120 the validator leads by 0.61 to 1.09 points.
2. **It also lowers the multiple over random, beyond the intervals.** The strongest component's multiple of its random rate under content300 is 3.62 [3.39, 3.87], 3.86 [3.67, 4.07] and 4.33 [4.19, 4.47] at R = 1, 15 and 50, against 4.06 [3.90, 4.23], 4.46 [4.32, 4.61] and 4.71 [4.61, 4.80] under reg120. The intervals do not overlap at any R. This is the first change in the experiment that moves the ratio and not only the absolute rate.
3. **Stretching every path lowers absolute accuracy but raises the validator's multiple.** Under hold300 the observer falls 1.7 to 3.3 points, but the validator stays the strongest component and its multiple of random rises (4.30, 4.85 and 5.27 against 4.06, 4.46 and 4.71).
4. **The cost is latency.** Mean capture to finalization at R = 1: 684 seconds under reg120, 1,014 under content200, 1,425 under content300, and 911, 1,142 and 1,595 under hold150, hold200 and hold300.
5. **Precision at coverage improves most under the content-only builds.** At R = 1 the best top-1% precision of any vantage is 15.1% under content200 and 7.8% under content300, against 18.5% under reg120.

## Why the content-only stretch works (exploratory)

The record time follows whichever path finishes later: a content server submits only once its own hold has released and quorum has formed. The diagnostic below counts how often the content server's own hold release, not the quorum push, sets the moment it confirms (R = 15, 40 decoys, 5 runs on run ids from 6,000,000 up; not pre-registered):

| Build | Confirmation set by the content path |
|---|---|
| reg120 | 32.0% |
| hold200 | 40.1% |
| hold300 | 44.1% |
| content200 | 70.4% |
| content300 | 85.6% |

Under reg120 the credential path usually sets the record time, so the components on it (the validator above all) hold events whose timing predicts the record. Stretching every path keeps the credential path in charge, so the validator keeps its lead. Stretching the content paths alone hands the record time to holds that no credential-side component sees, and the content server's own arrival is followed by its own hold and the stretched path's spread. No single component then holds timing that predicts the record better than the observer's view of the device's first-hop sends.

## The strongest single component

Device accuracy and multiple of its own random rate [95% CI], 40 decoys:

| Build | R = 1 | R = 15 | R = 50 | Mean latency, R = 1 |
|---|---|---|---|---|
| reg120 | validator 9.61%, ×4.06 [3.90, 4.23] | validator 7.84%, ×4.46 [4.32, 4.61] | validator 5.09%, ×4.71 [4.61, 4.80] | 684 s |
| hold150 | validator 8.41%, ×4.48 [4.29, 4.68] | validator 6.76%, ×4.84 [4.67, 5.02] | validator 4.67%, ×5.45 [5.31, 5.58] | 911 s |
| hold200 | validator 7.61%, ×4.51 [4.30, 4.71] | validator 5.92%, ×4.71 [4.50, 4.90] | validator 4.09%, ×5.30 [5.16, 5.45] | 1,142 s |
| hold300 | validator 6.32%, ×4.30 [4.07, 4.53] | validator 5.31%, ×4.85 [4.64, 5.07] | validator 3.54%, ×5.27 [5.12, 5.43] | 1,595 s |
| content200 | first hop, credential 6.82%, ×3.85 [3.64, 4.03] | first hop, credential 5.29%, ×4.01 [3.84, 4.18] | observer 3.82%, ×4.71 [4.58, 4.84] | 1,014 s |
| content300 | observer 5.56%, ×3.62 [3.39, 3.87] | observer 4.41%, ×3.86 [3.67, 4.07] | observer 3.04%, ×4.33 [4.19, 4.47] | 1,425 s |

## The passive observer

Device accuracy, random-pick rate, multiple of random [95% CI]:

| Build | R = 1 | R = 15 | R = 50 |
|---|---|---|---|
| reg120 | 8.52%, 2.05%, ×4.14 [3.97, 4.32] | 6.76%, 1.53%, ×4.42 [4.26, 4.59] | 4.48%, 0.94%, ×4.77 [4.65, 4.88] |
| hold150 | 6.69%, 1.74%, ×3.85 [3.65, 4.05] | 5.52%, 1.29%, ×4.27 [4.08, 4.46] | 3.76%, 0.79%, ×4.73 [4.61, 4.86] |
| hold200 | 5.98%, 1.59%, ×3.75 [3.52, 3.98] | 4.92%, 1.19%, ×4.15 [3.94, 4.37] | 3.38%, 0.73%, ×4.63 [4.51, 4.75] |
| hold300 | 5.15%, 1.45%, ×3.55 [3.29, 3.80] | 4.08%, 1.08%, ×3.77 [3.56, 3.99] | 2.82%, 0.66%, ×4.25 [4.11, 4.40] |
| content200 | 6.81%, 1.77%, ×3.84 [3.63, 4.05] | 5.24%, 1.32%, ×3.97 [3.79, 4.15] | 3.82%, 0.81%, ×4.71 [4.58, 4.84] |
| content300 | 5.56%, 1.53%, ×3.62 [3.39, 3.87] | 4.41%, 1.14%, ×3.86 [3.67, 4.07] | 3.04%, 0.70%, ×4.33 [4.19, 4.47] |

## Paired effects against reg120

Device level, in points [95% CI]:

| Build | R | Observer | Content server | Validator | Gatekeeper |
|---|---|---|---|---|---|
| hold150 | 1 | -1.78 [-2.22, -1.40] | -1.86 [-2.82, -0.88] | -1.13 [-1.63, -0.62] | -1.76 [-2.13, -1.38] |
| hold150 | 15 | -1.26 [-1.56, -0.97] | -1.57 [-2.23, -0.94] | -1.08 [-1.40, -0.74] | -1.18 [-1.46, -0.89] |
| hold150 | 50 | -0.72 [-0.86, -0.59] | -1.04 [-1.34, -0.72] | -0.40 [-0.57, -0.24] | -0.67 [-0.80, -0.54] |
| hold200 | 1 | -2.46 [-2.88, -2.05] | -3.21 [-4.05, -2.35] | -1.92 [-2.38, -1.43] | -2.40 [-2.79, -2.01] |
| hold200 | 15 | -1.89 [-2.30, -1.48] | -3.50 [-4.13, -2.87] | -1.98 [-2.35, -1.60] | -1.96 [-2.34, -1.60] |
| hold200 | 50 | -1.12 [-1.26, -0.97] | -1.81 [-2.13, -1.48] | -0.97 [-1.13, -0.82] | -1.10 [-1.24, -0.96] |
| hold300 | 1 | -3.30 [-3.73, -2.85] | -4.94 [-5.68, -4.13] | -3.20 [-3.67, -2.70] | -3.27 [-3.68, -2.86] |
| hold300 | 15 | -2.90 [-3.23, -2.54] | -4.39 [-5.11, -3.67] | -2.58 [-2.95, -2.20] | -2.89 [-3.25, -2.56] |
| hold300 | 50 | -1.69 [-1.86, -1.53] | -2.26 [-2.61, -1.91] | -1.50 [-1.67, -1.33] | -1.68 [-1.85, -1.52] |
| content200 | 1 | -1.62 [-2.06, -1.17] | -3.00 [-3.85, -2.11] | -3.17 [-3.60, -2.73] | -1.58 [-1.99, -1.16] |
| content200 | 15 | -1.56 [-1.92, -1.21] | -2.67 [-3.32, -2.04] | -2.71 [-3.06, -2.37] | -1.54 [-1.90, -1.20] |
| content200 | 50 | -0.64 [-0.80, -0.49] | -1.57 [-1.88, -1.27] | -1.53 [-1.69, -1.37] | -0.62 [-0.77, -0.48] |
| content300 | 1 | -2.91 [-3.33, -2.49] | -4.44 [-5.23, -3.59] | -4.64 [-5.07, -4.19] | -2.95 [-3.38, -2.51] |
| content300 | 15 | -2.57 [-2.97, -2.17] | -3.96 [-4.67, -3.27] | -4.19 [-4.56, -3.80] | -2.63 [-3.00, -2.29] |
| content300 | 50 | -1.45 [-1.61, -1.29] | -2.23 [-2.61, -1.92] | -2.27 [-2.45, -2.11] | -1.43 [-1.60, -1.27] |

## Precision at coverage

Best top-1% precision of any vantage [95% CI], and the most decisions any vantage gets right with more than 50% precision, at R = 1:

| Build | Best top-1% precision | Decisions above 50% precision | AUC of confidence, range over vantages |
|---|---|---|---|
| reg120 | 18.5% [15.0, 22.6] (validator) | 3 of 39,962 (validator) | 0.566 to 0.574 |
| hold150 | 19.8% [16.2, 24.0] (validator) | 17 of 39,901 (validator) | 0.555 to 0.566 |
| hold200 | 18.1% [14.6, 22.2] (validator) | 7 of 39,790 (validator) | 0.544 to 0.560 |
| hold300 | 10.2% [7.6, 13.6] (validator) | 0 | 0.523 to 0.552 |
| content200 | 15.1% [13.4, 16.9] (first hop, credential) | 19 of 39,799 (validator) | 0.545 to 0.567 |
| content300 | 7.8% [6.4, 9.4] (gatekeeper) | 0 | 0.526 to 0.545 |

## Checks and controls

- **Outcome-shuffle control:** 2, 0, 2, 0 and 4 of 21 stable cells under hold150, hold200, hold300, content200 and content300 have a shuffled-outcome AUC interval excluding 0.5, all within the plan's 0.03 margin (largest 0.518).
- **Simulation margins:** warm-up and cool-down scale with k; at k = 1 the build reproduces the committed reg120 results exactly.
- **Rates** stay those of the push build, so longer holds keep more transactions in flight.

## Predictions

| Prediction | Outcome |
|---|---|
| H1. The observer falls as k rises: reg120 > hold150 > hold200 > hold300 at every R | Confirmed at all three R. |
| H2. The content server's lead over the observer under hold200 and hold300 is below its reg120 value at every R | Confirmed (-0.40 to +0.08, against +0.53 to +0.93). |
| H3. Under content200 and content300, the content server's effect against reg120 is below 0 at every R | Confirmed (-4.44 to -1.57). |
| H4. No prediction for the strongest component's multiple | Reported: it rises under hold150 to hold300 and falls under content200 and content300. |

H1 to H3 follow development runs, as the plan discloses. The plan did not anticipate that the content-only builds would remove every component's lead over the observer.

## Scope

- **Untested middle ground.** Only stretch factors 2 and 3 were tested on the content paths. A smaller content stretch, or stretching the content paths while shortening the credential path, might keep the content path in charge of the record time at less latency. The diagnostic above suggests the property that matters is how often the content path sets the record time.

# Content paths stretched, credential path shortened

Plan section 6h, run on the second machine with `python -m sna sequence 6h` into `results/6h/` (code commit `fbb5815`, results commit `5a40a4f`, both on `main`). The content paths' device and relay-hop holds are stretched by 2; the credential path's device and relay-hop holds are scaled by 0.75, 0.5 or 0.25. Every build has the 120-second registry window, 40 decoys; 200 runs per cell; every cell met the stability rule. The sequence also reran reg120 and content200; content200 reproduced the committed section 6g results decision for decision, and reg120 differed in one observer decision in 172,650 (see Provenance).

## Summary

1. **Shortening the credential path keeps the content-only result.** In every cell of all three builds, no component leads the passive observer by more than 0.02 points.
2. **It lowers accuracy a little further, at no latency cost.** Against content ×2 alone, the observer loses up to 0.39 points at 0.25 (R = 1), and the strongest component's multiple of random falls from 3.85 to 3.68 at R = 1 and from 4.71 to 4.50 at R = 50.
3. **It saves almost no latency.** Mean capture to finalization at R = 1 falls from 1,013.6 seconds (content ×2) to 1,002.0, 996.9 and 995.1 seconds; the 95th percentile is unchanged at 1,510.8 seconds in every build, because the slowest records follow the content path.
4. **At 0.25, no component has a single decision above 50% precision**, and the best top-1% precision at R = 1 is 12.3% [9.4, 15.9], against 15.1% for content ×2 alone and 18.5% for reg120.

## The strongest single component

Device accuracy and multiple of its own random rate [95% CI], 40 decoys:

| Build | R = 1 | R = 15 | R = 50 | Mean latency, R = 1 |
|---|---|---|---|---|
| reg120 | validator 9.61%, ×4.06 [3.90, 4.24] | validator 7.84%, ×4.46 [4.31, 4.61] | validator 5.09%, ×4.71 [4.61, 4.81] | 684.0 s |
| content ×2 | first hop, credential 6.82%, ×3.85 [3.64, 4.03] | first hop, credential 5.29%, ×4.01 [3.84, 4.18] | observer 3.82%, ×4.71 [4.58, 4.84] | 1,013.6 s |
| content ×2, credential ×0.75 | observer 6.84%, ×3.88 [3.65, 4.09] | observer 5.27%, ×4.01 [3.83, 4.19] | observer 3.81%, ×4.72 [4.60, 4.84] | 1,002.0 s |
| content ×2, credential ×0.5 | first hop, credential 6.64%, ×3.78 [3.59, 3.97] | credential processor 5.17%, ×3.95 [3.76, 4.14] | observer 3.68%, ×4.58 [4.47, 4.70] | 996.9 s |
| content ×2, credential ×0.25 | first hop, credential 6.44%, ×3.68 [3.47, 3.87] | observer 5.08%, ×3.89 [3.71, 4.07] | credential processor 3.61%, ×4.50 [4.39, 4.62] | 995.1 s |

Where the strongest component is not the observer, it leads the observer by at most 0.04 points (content ×2 alone, R = 15) and by at most 0.02 points in the three new builds. Under content ×2 with credential ×0.25, the strongest component's interval lies wholly below reg120's at R = 1 and 15; at R = 50 the two intervals touch (4.62 against 4.61).

## Paired effects against content ×2 alone

Device level, in points [95% CI]:

| Build | R | Observer | First hop, credential | Validator | Content server |
|---|---|---|---|---|---|
| credential ×0.75 | 1 | +0.03 [-0.14, +0.19] | +0.01 [-0.12, +0.14] | -0.24 [-0.43, -0.04] | -0.02 [-0.19, +0.16] |
| credential ×0.75 | 15 | +0.03 [-0.11, +0.16] | -0.03 [-0.14, +0.07] | -0.19 [-0.34, -0.05] | -0.14 [-0.28, -0.01] |
| credential ×0.75 | 50 | -0.01 [-0.07, +0.06] | -0.03 [-0.07, +0.01] | -0.10 [-0.16, -0.04] | -0.09 [-0.16, -0.02] |
| credential ×0.5 | 1 | -0.18 [-0.36, +0.01] | -0.18 [-0.32, -0.03] | -0.23 [-0.46, -0.01] | -0.21 [-0.39, -0.03] |
| credential ×0.5 | 15 | -0.09 [-0.25, +0.07] | -0.16 [-0.29, -0.03] | -0.20 [-0.37, -0.02] | -0.32 [-0.46, -0.19] |
| credential ×0.5 | 50 | -0.13 [-0.21, -0.06] | -0.14 [-0.19, -0.08] | -0.13 [-0.21, -0.06] | -0.17 [-0.23, -0.10] |
| credential ×0.25 | 1 | -0.39 [-0.60, -0.18] | -0.38 [-0.56, -0.20] | -0.26 [-0.52, +0.02] | -0.58 [-0.76, -0.40] |
| credential ×0.25 | 15 | -0.17 [-0.33, -0.00] | -0.28 [-0.41, -0.14] | -0.32 [-0.51, -0.12] | -0.38 [-0.55, -0.22] |
| credential ×0.25 | 50 | -0.21 [-0.29, -0.14] | -0.22 [-0.28, -0.16] | -0.12 [-0.21, -0.04] | -0.23 [-0.31, -0.15] |

## Precision at coverage, R = 1

| Build | Best top-1% precision [95% CI] | Most decisions above 50% precision, any vantage |
|---|---|---|
| reg120 | 18.5% [15.0, 22.6] (validator) | 3 |
| content ×2 | 15.1% [13.4, 16.9] (first hop, credential) | 19 |
| credential ×0.75 | 15.6% [12.3, 19.5] (validator) | 17 |
| credential ×0.5 | 13.3% [10.3, 17.0] (validator) | 7 |
| credential ×0.25 | 12.3% [9.4, 15.9] (validator) | 0 |

## Checks and controls

- **Outcome-shuffle control:** 2, 2 and 0 of 21 stable cells under credential ×0.75, ×0.5 and ×0.25 have a shuffled-outcome AUC interval excluding 0.5, all within the plan's 0.03 margin (largest 0.508).

## Predictions

| Prediction | Outcome |
|---|---|
| S1. No vantage leads the observer by more than 0.5 points in any cell of the three new builds | Confirmed: the largest lead is +0.02. |
| S2. The observer's effect against content ×2 lies within ±1 point in every cell | Confirmed (-0.39 to +0.03). |
| S3. At R = 1, each new build's mean latency is at most 60 seconds below content ×2's | Confirmed: 11.6, 16.7 and 18.5 seconds below. |

S1 to S3 follow development runs, as the plan discloses.

## Scope

- **The credential path's own protection.** At ×0.25 a credential-path hold averages about 26 seconds. No vantage on that path gained on the observer here, but this sweep measures only the record-to-device link; it does not measure, for example, how well a first hop could link a device's credential packet to the validator's request.

# The claim criterion

Plan section 6i fixes the criterion before this comparison: in a cell, every vantage's most confident 1% of decisions must have precision below 50% (upper bound of the 95% Wilson interval), and fewer than 0.1% of its decisions may fall in the largest most-confident set whose precision exceeds 50%. Every cell below is from a committed sweep; the comparison is in `results/claim_criterion.json`.

## Primary cells: 120-second window, 40 decoys

| R | Result | Highest top-1% precision, any vantage [upper bound] | Largest share of decisions above 50% precision, any vantage |
|---|---|---|---|
| 1 | Pass | validator 18.5% [22.6%] | validator 0.008% (3 of 39,962) |
| 15 | Pass | validator 14.6% [17.9%] | validator 0.002% (1 of 52,098) |
| 50 | Pass | validator 9.8% [11.3%] | validator 0.001% (1 of 172,650) |

## Secondary cells

Every secondary cell passes as well: the 120-second build at 20, 30, 60, 100 and 150 decoys (R = 1, 15 and 50), and every hold build of sections 6g and 6h at 40 decoys. The closest to failing is the 120-second build at R = 1 with 20 decoys: the validator's top-1% precision is 32.5% with an upper bound of 37.2%, and 0.058% of its decisions fall above 50% precision.

**The criterion does not separate the designs tested.** Every configuration tested passes it, including the lowest decoy target (20 in flight). The criterion establishes the claim; it does not rank mechanisms. The accuracy ratios, top-1% precision values and leads over the observer reported in the sections above remain the measures that distinguish one design from another.

# Status reports

## The validator and the credential processor: their own timing in the simulator

Measured at R = 1 with 40 decoys under the 120-second build (10 runs on run ids from 7,000,000 up):

| Step | What the simulator does | Measured |
|---|---|---|
| Validator: CV-1 arrival to CV-2 send | Processing time drawn uniformly from 5 to 50 ms; no hold | mean 26.2 ms, range 5.1 to 50.0 ms |
| Credential processor: Cred-3 arrival to CV-1 send | Processing time drawn uniformly from 0.5 to 3 ms; no hold | mean 1.76 ms, range 0.5 to 3.0 ms |
| Credential processor: CV-2 arrival to the first gatekeeper leg | Each of the three gatekeeper legs takes its own relay-lottery draw on C's node clock, starting at CV-2's arrival | mean 40.4 s (median 26.9 s in isolation), range 0.12 to 258 s |

Every packet also carries network latency (5 to 80 ms between nodes, fixed per pair in a run) and per-packet jitter (exponential, mean 2 ms).

- **The validator has no randomizing delay** beyond tens of milliseconds of processing and network time. The gap is real in the simulator.
- **The credential processor's CV-1 send has none either**: it follows Cred-3's arrival by 0.5 to 3 ms.
- **The credential processor's reaction to CV-2 is held in the simulator.** Because each gatekeeper leg is an independent lottery draw starting at CV-2's arrival, the first leg leaves after the shortest of three draws: 40 seconds on average. If the specification's "staggered fan-out clock" means legs spaced relative to each other after an unheld first departure, the simulator models more protection for C than the specification provides. The specification's wording leaves this open.

## Decoy-identity pool size

Nothing hardcodes a pool size. The simulator derives it from the decoy rate: each identity captures every 20 minutes on average, so the pool is the decoy rate times 1,200 seconds, rounded. At the decoy targets used: 38 identities at 20 decoys, 58 at 30, 77 at 40, 115 at 60, 192 at 100 and 288 at 150. No sweep of the pool size was run, and none is planned.

## F and I submitting together

Share of real records whose two registry submissions leave within 5 seconds of each other (10 runs per cell, 40 decoys):

| Build | R | Within 5 s | Quorum outlasted both content servers' holds | Within 5 s, when it did | Within 5 s, when it did not |
|---|---|---|---|---|---|
| push (no registry bundling) | 1 | 51.3% | 49.6% | 100.0% | 3.4% |
| push | 15 | 53.5% | 52.2% | 100.0% | 2.8% |
| 120-second window | 1 | 64.4% | 49.6% | 100.0% | 29.4% |
| 120-second window | 15 | 65.6% | 52.2% | 100.0% | 28.0% |

- When quorum outlasts both content servers' holds, both learn of it from the same board pushes and submit within 5 seconds every time, as the specification's post-match lottery section describes.
- Under the 120-second registry window, every pair within 5 seconds leaves at the same instant, on the same registry boundary. The window adds coincident pairs (29% of the records whose holds outlasted quorum) but rounds every submission time to its 120-second schedule.

## Two earlier requests, already in this file

- **The zero-access baseline** (a guess among every registered device) is in the section "Zero-access baseline", side by side with the feasible-set rate for every cell of the 120-second build.
- **The cross-machine difference** is explained in "Provenance of every result behind these decisions": the second machine's rerun of section 6h matched content ×2 decision for decision and differed from reg120 in 1 of 172,650 passive-observer decisions and 1 credential-processor claim, which is floating-point tie-breaking between Linux and Windows. That rerun was of the 120-second build and content ×2, not of the 480-second build.

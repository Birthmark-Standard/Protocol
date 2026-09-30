# Results

200 runs per cell, 58 cells (11 no-decoy, 46 decoy, 1 sensitivity control), 11,600 runs in all. Every cell met the stability rule (at least 50 successes and 50 failures), so every number below is reported as a finding. Intervals are 95% and resample whole runs. Accuracy is the per-decision attack (the pre-registered primary) unless a line says joint. The analysis plan is `ANALYSIS_PLAN.md`; the full tables are `results/tables.md` and `results/summary.csv`.

## Summary

1. **The claim fails at every volume from L = 2 to L = 500.** Every vantage, including the baseline with no keys, names the right transaction more often than 1/L. The pre-registered adjusted interval lies above 1/L in every no-decoy cell from L = 2 upward, for every vantage except the content first hop at L = 2.
2. **The passive observer alone links at about twice chance.** The baseline's lift is 2.1 at every L from 24 to 500 and holds flat (slope -0.003 [-0.014, 0.009]). No component needs to be compromised for this.
3. **The gatekeeper is the one component whose own knowledge adds a large amount.** Its accuracy is 21.3% at L = 40 (1/L = 2.5%) and 3.0% at L = 500 (1/L = 0.2%). Its lift rises from 8.5 at L = 40 to 15.0 at L = 500 (slope 0.224 [0.222, 0.226]), so larger volume makes it relatively stronger.
4. **The content server adds a steady amount over its baseline** (+3.2 points at L = 40, +0.25 at L = 500) and its lift rises slightly, from 2.39 to 2.46.
5. **Decoys give no protection against any vantage that links to registry records.** At fixed real volume R, the per-decision accuracy of the baseline, both first hops, the credential processor, the validator and the gatekeeper is identical to the last digit at every decoy volume T, in all 46 decoy cells. A decoy never produces a registry record, so it never becomes a candidate. At the deployment volumes (R = 1 to 4), these vantages stay at 30% to 79% whatever T is.
6. **Decoys do protect against the content server,** whose candidates are validator replies. Its accuracy tracks T and does not depend on R: 0.50% at T = 500 for R = 1 (78.1% without decoys). It still stays at about 2.4 times 1/T.
7. **Confidence does not let an attacker pick out its right answers at useful volume.** From L = 24 upward, no vantage keeps precision above 50% on even 0.03% of its decisions. At L = 1 to 4 the high-coverage values reflect accuracy itself being above 50%.

## Pre-run checks

Run before the sweep with background traffic on, at R = 8 and T = 40 over 12 runs (`results/checks.json`).

| Check | Outcome |
|---|---|
| Padding classes | Pass. 12,614 legs, none outside its class. Every raw payload fits its class. Ring V signature 64 B with real keys, verifies. |
| Answer extraction | Pass. 340 of 340 registry submissions and 901 of 901 validator replies extracted, none extra. |
| Background independence | Pass. Every vantage's and baseline's decisions identical with background traffic on and off. |
| Cannot tell decoys: baseline | Pass. 19 features; largest deviation Cred-2 size, AUC 0.511 [0.496, 0.526]. |
| Cannot tell decoys: first hop, credential | Pass. 3 features; largest A's hold, AUC 0.490 [0.470, 0.510]. |
| Cannot tell decoys: first hop, content | Pass. 3 features; largest time since the source's previous capture, AUC 0.496 [0.470, 0.521]. |
| Cannot tell decoys: content server, before its timeout | Pass. 2 features; largest content last-leg size, AUC 0.495 [0.483, 0.508]. |
| Content server after its 30-minute timeout | Fail, as scoped. Quorum within 30 minutes separates real from decoy perfectly (AUC 1.000). A decoy never reaches quorum, so the content server's own attack guesses only for items that reached quorum. |
| Can tell decoys: validator, credential processor, gatekeeper | Pass. Quorum never forms for a decoy and always forms for a real transaction; the gatekeeper's substitute posting keeps the real schedule (AUC 0.497). |

Padding-class scaling note: the gatekeeper fan-out leg's raw size is 689 B plus the Ring V signature, 32 (n + 1) B for n validators. It fits the 820 to 860 B class for n up to 3 (817 B), exceeds the class minimum at n = 4 (849 B) and exceeds the class maximum from n = 5 (881 B).

## No-decoy sweep

### Accuracy against 1/L

| Vantage | L = 1 | L = 2 | L = 3 | L = 4 | L = 8 | L = 24 | L = 40 | L = 50 | L = 100 | L = 200 | L = 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1/L | 100.00% | 50.00% | 33.33% | 25.00% | 12.50% | 4.17% | 2.50% | 2.00% | 1.00% | 0.50% | 0.20% |
| Random assignment (registry list) | 47.18% | 27.69% | 18.97% | 14.49% | 7.23% | 2.41% | 1.45% | 1.16% | 0.58% | 0.29% | 0.12% |
| Baseline | 76.76% | 61.03% | 49.51% | 42.11% | 24.46% | 8.66% | 5.33% | 4.28% | 2.14% | 1.07% | 0.42% |
| First hop, credential | 72.89% | 56.06% | 44.16% | 37.15% | 20.81% | 7.61% | 4.46% | 3.58% | 1.85% | 0.90% | 0.36% |
| First hop, content | 66.34% | 48.05% | 36.82% | 30.29% | 16.73% | 5.63% | 3.41% | 2.72% | 1.34% | 0.66% | 0.26% |
| Credential processor | 78.80% | 63.83% | 52.70% | 44.73% | 26.66% | 9.30% | 5.66% | 4.45% | 2.18% | 1.08% | 0.41% |
| Content server | 78.14% | 63.22% | 52.28% | 44.70% | 26.98% | 9.67% | 5.98% | 4.86% | 2.43% | 1.24% | 0.49% |
| Validator | 76.70% | 61.08% | 49.44% | 41.95% | 24.53% | 8.65% | 5.28% | 4.25% | 2.07% | 1.04% | 0.42% |
| Gatekeeper | 78.14% | 65.02% | 56.54% | 51.24% | 39.28% | 26.10% | 21.29% | 19.08% | 12.46% | 7.06% | 2.99% |

The random-assignment rate (true answers among a row's feasible candidates, over the feasible candidates) is below 1/L at every L because each transaction has two registry submissions and each row's feasible band holds more than L transactions on average.

At L = 1, every vantage is below 1/L = 100% and above its random-assignment rate (for example the baseline: 76.8% against 47.2%). L is a mean, so a transaction at L = 1 usually shares its band with others, and 1/L overstates what chance is there. The pre-registered test counts these cells as no signal on accuracy. Every one of them shows signal on confidence (adjusted AUC interval above 0.5).

### Lift and its trend from L = 40 to 500

| Vantage | L = 1 | L = 2 | L = 3 | L = 4 | L = 8 | L = 24 | L = 40 | L = 50 | L = 100 | L = 200 | L = 500 | Trend 40 to 500 (slope [95% CI]) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | 0.77 | 1.22 | 1.49 | 1.68 | 1.96 | 2.08 | 2.13 | 2.14 | 2.14 | 2.14 | 2.12 | holds flat: -0.003 [-0.014, 0.009] |
| First hop, credential | 0.73 | 1.12 | 1.32 | 1.49 | 1.66 | 1.83 | 1.78 | 1.79 | 1.85 | 1.80 | 1.78 | holds flat: -0.002 [-0.013, 0.010] |
| First hop, content | 0.66 | 0.96 | 1.10 | 1.21 | 1.34 | 1.35 | 1.36 | 1.36 | 1.34 | 1.33 | 1.31 | falls: -0.017 [-0.026, -0.007] |
| Credential processor | 0.79 | 1.28 | 1.58 | 1.79 | 2.13 | 2.23 | 2.27 | 2.23 | 2.18 | 2.16 | 2.03 | falls: -0.039 [-0.050, -0.028] |
| Content server | 0.78 | 1.26 | 1.57 | 1.79 | 2.16 | 2.32 | 2.39 | 2.43 | 2.43 | 2.48 | 2.46 | rises: 0.010 [0.003, 0.018] |
| Validator | 0.77 | 1.22 | 1.48 | 1.68 | 1.96 | 2.08 | 2.11 | 2.12 | 2.07 | 2.09 | 2.09 | holds flat: -0.005 [-0.016, 0.006] |
| Gatekeeper | 0.78 | 1.30 | 1.70 | 2.05 | 3.14 | 6.26 | 8.52 | 9.54 | 12.46 | 14.12 | 14.96 | rises: 0.224 [0.222, 0.226] |

Figure: `results/figures/lift_vs_L_nodecoy.png`.

### Contribution over the paired baseline (percentage points, per-decision)

| Vantage | L = 1 | L = 2 | L = 3 | L = 4 | L = 8 | L = 24 | L = 40 | L = 50 | L = 100 | L = 200 | L = 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] |
| First hop, credential | +2.10 [+1.69, +2.51] | +2.73 [+2.23, +3.25] | +2.34 [+1.74, +2.92] | +2.81 [+2.29, +3.32] | +1.71 [+1.22, +2.22] | +0.99 [+0.77, +1.21] | +0.30 [+0.16, +0.45] | +0.28 [+0.16, +0.39] | +0.25 [+0.19, +0.30] | +0.08 [+0.05, +0.12] | +0.05 [+0.04, +0.07] |
| First hop, content | -1.38 [-1.69, -1.08] | -1.31 [-1.66, -0.95] | -1.35 [-1.73, -0.98] | -1.00 [-1.36, -0.62] | -0.33 [-0.63, -0.00] | -0.28 [-0.43, -0.12] | -0.13 [-0.22, -0.03] | -0.06 [-0.14, +0.02] | -0.07 [-0.11, -0.03] | -0.02 [-0.04, -0.00] | -0.01 [-0.02, -0.00] |
| Credential processor | +2.04 [+1.62, +2.47] | +2.80 [+2.32, +3.26] | +3.19 [+2.63, +3.77] | +2.62 [+2.06, +3.14] | +2.20 [+1.61, +2.78] | +0.64 [+0.38, +0.92] | +0.34 [+0.17, +0.51] | +0.17 [+0.05, +0.30] | +0.03 [-0.04, +0.11] | +0.01 [-0.02, +0.04] | -0.02 [-0.03, -0.00] |
| Content server | +16.59 [+16.23, +16.96] | +20.71 [+20.23, +21.19] | +20.43 [+20.00, +20.89] | +19.22 [+18.78, +19.67] | +13.37 [+12.98, +13.78] | +5.06 [+4.89, +5.23] | +3.22 [+3.11, +3.33] | +2.63 [+2.54, +2.72] | +1.29 [+1.25, +1.33] | +0.64 [+0.62, +0.67] | +0.25 [+0.24, +0.26] |
| Validator | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] |
| Gatekeeper | +3.33 [+3.08, +3.59] | +6.64 [+6.32, +6.96] | +9.62 [+9.28, +9.94] | +11.97 [+11.64, +12.27] | +16.78 [+16.47, +17.06] | +18.40 [+18.24, +18.59] | +16.66 [+16.54, +16.79] | +15.34 [+15.23, +15.44] | +10.59 [+10.53, +10.65] | +6.09 [+6.06, +6.12] | +2.58 [+2.57, +2.60] |

The baseline's contribution is zero by construction (its vantage and baseline anchor are the same event), as is the validator's (its reply send is the same wire event in both). The joint-assignment contributions in the no-decoy sweep match these within a few tenths of a point (`results/tables.md`).

Findings from this table:

- **Gatekeeper:** the largest contribution at every L from 2 upward, peaking at +18.4 points at L = 24 and still +2.6 points at L = 500, which is 13 times 1/L on its own.
- **Content server:** +19 to +21 points at L = 2 to 4, falling to +0.25 at L = 500.
- **Credential processor:** +2 to +3 points at L = 1 to 8. The interval covers zero at L = 100 and 200, and it is -0.02 [-0.03, -0.00] at L = 500.
- **First hop, credential:** a small positive contribution at every L, from +2.8 points at L = 4 to +0.05 at L = 500.
- **First hop, content:** a small negative contribution at every L (-1.4 points at L = 1, -0.01 at L = 500). Its own forward time is a worse anchor than the arrival it received. The mechanism was not tested.

## Decoy sweep

### Vantages that link to registry records

For the baseline, both first hops, the credential processor, the validator and the gatekeeper, the per-decision accuracy at every T equals the no-decoy value at the same R exactly (largest difference across all 46 cells: 0). Their rows in `results/tables.md` repeat the no-decoy values across each row. Figure: `results/figures/accuracy_vs_T_decoy.png`.

The one place decoys act on these vantages is the joint assignment of the three that cannot tell decoys apart. Decoy items join the one-to-one assignment and crowd out the real ones:

| Vantage | R | Per-decision | Joint at T = R | Joint at T = 500 |
|---|---|---|---|---|
| Baseline | 1 | 76.76% | 77.45% | 0.59% |
| Baseline | 4 | 42.11% | 42.99% | 0.55% |
| Baseline | 40 | 5.33% | 5.46% | 0.66% |
| First hop, credential | 1 | 72.89% | 72.96% | 11.85% |
| First hop, credential | 4 | 37.15% | 37.19% | 12.77% |
| First hop, credential | 40 | 4.46% | 4.43% | 4.41% |
| First hop, content | 1 | 66.34% | 66.41% | 4.77% |
| First hop, content | 4 | 30.29% | 30.31% | 5.05% |
| First hop, content | 40 | 3.41% | 3.40% | 3.45% |

An attacker is free to use the per-decision attack, which decoys leave untouched, so the joint figures are a lower bound on these vantages. For the three vantages that can tell decoys, the joint contribution over the baseline grows with T (for example the gatekeeper at R = 4: +12.6 points at T = 4, +52.0 at T = 500). This measures the baseline's joint assignment collapsing, since the vantage's own accuracy is unchanged.

### Content server

Accuracy by real volume R (rows) and total volume T (columns):

| R \ T | 1 | 2 | 3 | 4 | 8 | 24 | 40 | 50 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 78.14% |  |  | 44.73% | 26.69% | 9.87% | 5.97% | 4.77% | 2.37% | 1.24% | 0.50% |
| 2 |  | 63.22% |  | 44.77% | 26.84% | 9.86% | 5.96% | 4.82% | 2.42% | 1.21% | 0.50% |
| 3 |  |  | 52.28% | 44.54% | 26.81% | 9.82% | 5.97% | 4.78% | 2.43% | 1.18% | 0.47% |
| 4 |  |  |  | 44.70% | 27.01% | 9.78% | 5.89% | 4.80% | 2.46% | 1.22% | 0.49% |
| 8 |  |  |  |  | 26.98% | 9.87% | 5.95% | 4.65% | 2.40% | 1.28% | 0.46% |
| 24 |  |  |  |  |  | 9.67% | 5.90% | 4.66% | 2.35% | 1.22% | 0.50% |
| 40 |  |  |  |  |  |  | 5.98% | 4.81% | 2.44% | 1.21% | 0.49% |
| 1/T | 100.00% | 50.00% | 33.33% | 25.00% | 12.50% | 4.17% | 2.50% | 2.00% | 1.00% | 0.50% | 0.20% |

At fixed T the accuracy is the same whatever R is, within about 0.3 points. With decoys the content server's lift against 1/T is 2.3 to 2.5, the same as its no-decoy lift at the same L.

## Calibrated confidence

Selected cells (every cell is in `results/tables.md`):

| Vantage | L | AUC [95% CI] | Precision, top 1% | Precision, top 5% | Largest coverage with precision > 50% |
|---|---|---|---|---|---|
| Baseline | 4 | 0.686 [0.681, 0.691] | 86.9% | 74.1% | 66.223% |
| Baseline | 40 | 0.556 [0.550, 0.563] | 8.3% | 7.8% | 0.000% |
| Baseline | 500 | 0.514 [0.507, 0.521] | 0.4% | 0.5% | 0.000% |
| First hop, credential | 4 | 0.676 [0.671, 0.681] | 81.2% | 79.3% | 46.048% |
| First hop, credential | 40 | 0.550 [0.542, 0.558] | 8.5% | 6.5% | 0.000% |
| First hop, credential | 500 | 0.519 [0.512, 0.527] | 0.4% | 0.4% | 0.000% |
| First hop, content | 4 | 0.650 [0.645, 0.655] | 75.3% | 66.1% | 19.420% |
| First hop, content | 40 | 0.545 [0.539, 0.551] | 5.6% | 4.7% | 0.000% |
| First hop, content | 500 | 0.519 [0.513, 0.526] | 0.3% | 0.3% | 0.000% |
| Credential processor | 4 | 0.693 [0.688, 0.697] | 90.7% | 77.6% | 78.988% |
| Credential processor | 40 | 0.560 [0.553, 0.566] | 10.7% | 8.9% | 0.000% |
| Credential processor | 500 | 0.544 [0.537, 0.551] | 0.5% | 0.6% | 0.000% |
| Content server | 4 | 0.722 [0.718, 0.726] | 100.0% | 97.9% | 80.472% |
| Content server | 40 | 0.579 [0.574, 0.584] | 11.9% | 10.0% | 0.000% |
| Content server | 500 | 0.567 [0.563, 0.572] | 0.7% | 0.7% | 0.000% |
| Validator | 4 | 0.687 [0.682, 0.692] | 87.2% | 74.4% | 65.882% |
| Validator | 40 | 0.558 [0.552, 0.565] | 8.3% | 7.7% | 0.000% |
| Validator | 500 | 0.513 [0.506, 0.520] | 0.4% | 0.5% | 0.000% |
| Gatekeeper | 4 | 0.756 [0.753, 0.759] | 90.9% | 83.3% | 100.000% |
| Gatekeeper | 40 | 0.620 [0.617, 0.622] | 25.9% | 23.0% | 0.000% |
| Gatekeeper | 500 | 0.508 [0.506, 0.509] | 3.1% | 3.1% | 0.000% |

## Controls

Sensitivity control, R = 40 with every hold off:

| Vantage | Accuracy [95% CI] | Paired baseline |
|---|---|---|
| Baseline | 99.76% [99.73%, 99.78%] | 99.76% |
| First hop, credential | 99.53% [99.49%, 99.57%] | 99.54% |
| First hop, content | 99.37% [99.33%, 99.41%] | 99.37% |
| Credential processor | 99.76% [99.73%, 99.78%] | 99.76% |
| Content server | 99.81% [99.79%, 99.84%] | 99.33% |
| Validator | 99.77% [99.74%, 99.80%] | 99.77% |
| Gatekeeper | 99.82% [99.80%, 99.84%] | 99.83% |

Every vantage is above 1/L = 2.5%, so the attacks and likelihoods find a signal when the timing carries one.

Outcome-shuffle control: correctness permuted within each run. In 76 of the 406 cells the shuffled AUC interval excludes 0.5. Every one of the 76 lies above 0.5, between 0.503 and 0.530. Permuting within a run keeps each run's success rate, so if confidence and accuracy covary from run to run, a small between-run association survives the shuffle. That is the likely mechanism; it was not tested. The confidence AUCs above 0.52 in the main tables are well clear of this effect. The AUCs of 0.508 to 0.519 at L = 500 are the same size as it, so those are not read as signal.

## Predictions

| Prediction | Outcome |
|---|---|
| P1. Registry-list vantages' per-decision accuracy identical at every T at fixed R | Confirmed exactly, in all 46 decoy cells for all six vantages. |
| P2. Content server's accuracy falls as T rises at fixed R | Confirmed at every R. |
| P3. Gatekeeper above 1/L and above its baseline at every R of 4 or more | Confirmed. |
| P4. Validator's per-decision contribution zero in every cell | Confirmed (by construction). |
| P5. Baseline above 1/L at R = 24 and 40 | Confirmed, and at every L from 2 to 500. |
| P6. Content server's contribution positive at R = 24 and 40 | Confirmed. |
| P7. Neither first hop's contribution interval above zero at any R of 4 or more | **Failed** for the credential first hop: its interval lies above zero at every R from 4 to 500 (+2.81 points at 4, +0.05 at 500). It holds for the content first hop, whose contribution is negative. |
| P8. Sensitivity control: every vantage above 1/L | Confirmed (99.4% to 99.8%). |
| P9. Outcome-shuffle AUC covers 0.5 in every stable cell | **Failed**: 76 of 406 cells exclude 0.5, all on the high side (0.503 to 0.530). |

P3, P5 and P6 were written after development runs that showed the same direction, as the plan discloses.

## Volume

Measured end-to-end delay D = 625.6 s (capture to registry finalization, mean of 21,561 transactions).

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

- One validator. The multi-validator case, with its padding requirement, is outside this build.
- Each attack scores one timing anchor per item (two for the content server). Stronger attacks, for example a gatekeeper that also searches the wire for the other two fan-out legs, would give accuracies at least as high, so the figures here are lower bounds on each vantage.
- Board reads and board postings are not on the observed wire.

# Tables

Record-to-device linking with genuine decoys, the rmix relay hold, a static content-server hold, and the post-match lottery in the residual case. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Volume

| L (in flight) | Captures per second | Captures per day | Devices (20-minute interval) |
|---|---|---|---|
| 1 | 0.0016 | 138 | 1.9 |
| 15 | 0.0240 | 2,072 | 28.8 |
| 21 | 0.0336 | 2,900 | 40.3 |
| 31 | 0.0496 | 4,282 | 59.5 |
| 35 | 0.0559 | 4,834 | 67.1 |
| 41 | 0.0655 | 5,663 | 78.6 |
| 45 | 0.0719 | 6,215 | 86.3 |
| 50 | 0.0799 | 6,906 | 95.9 |
| 55 | 0.0879 | 7,596 | 105.5 |
| 61 | 0.0975 | 8,425 | 117.0 |
| 70 | 0.1119 | 9,668 | 134.3 |
| 75 | 0.1199 | 10,359 | 143.9 |
| 80 | 0.1279 | 11,049 | 153.5 |
| 90 | 0.1439 | 12,430 | 172.6 |
| 101 | 0.1615 | 13,950 | 193.7 |
| 110 | 0.1758 | 15,193 | 211.0 |
| 115 | 0.1838 | 15,883 | 220.6 |
| 150 | 0.2398 | 20,717 | 287.7 |
| 151 | 0.2414 | 20,855 | 289.7 |
| 165 | 0.2638 | 22,789 | 316.5 |
| 200 | 0.3197 | 27,623 | 383.6 |

## Departure bundle sizes

Postings per 30-second bundle at one gatekeeper, on its own grid, over every run of the cell. Off cells report the bundles the same selections would have formed.

| R | Decoys | Mean per bundle | Empty | Exactly 1 | Fewer than 2 | 1, of non-empty | Postings departing alone | Bundles |
|---|---|---|---|---|---|---|---|---|
| 1 | 40 | 1.97 | 14.0% | 27.5% | 41.5% | 31.9% | 14.0% | 2,501,674 |
| 15 | 40 | 2.65 | 7.1% | 18.8% | 25.9% | 20.2% | 7.1% | 215,400 |
| 50 | 40 | 4.31 | 1.4% | 5.8% | 7.2% | 5.9% | 1.4% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.18 [-0.24, +0.61] | +1.50 [+1.14, +1.86] | 38603 |
| Baseline | 15 | 40 | +0.34 [-0.10, +0.78] | +1.07 [+0.79, +1.36] | 33383 |
| Baseline | 50 | 40 | +0.38 [+0.20, +0.56] | +0.72 [+0.59, +0.85] | 110616 |
| First hop, credential | 1 | 40 | +0.23 [-0.18, +0.64] | +1.65 [+1.38, +1.91] | 154412 |
| First hop, credential | 15 | 40 | +0.31 [-0.10, +0.73] | +1.06 [+0.86, +1.26] | 133532 |
| First hop, credential | 50 | 40 | +0.37 [+0.20, +0.53] | +0.70 [+0.62, +0.78] | 442464 |
| First hop, content | 1 | 40 | +0.23 [-0.15, +0.62] | +1.65 [+1.39, +1.91] | 154412 |
| First hop, content | 15 | 40 | +0.31 [-0.12, +0.71] | +1.06 [+0.85, +1.27] | 133532 |
| First hop, content | 50 | 40 | +0.37 [+0.19, +0.54] | +0.70 [+0.62, +0.79] | 442464 |
| Credential processor | 1 | 40 | +0.14 [-0.30, +0.56] | +1.54 [+1.23, +1.86] | 154412 |
| Credential processor | 15 | 40 | +0.33 [-0.08, +0.79] | +1.08 [+0.81, +1.37] | 133532 |
| Credential processor | 50 | 40 | +0.40 [+0.21, +0.58] | +0.70 [+0.58, +0.81] | 442464 |
| Content server | 1 | 40 | +0.36 [-0.44, +1.27] | +1.26 [+0.49, +2.01] | 9128 |
| Content server | 15 | 40 | +0.57 [-0.29, +1.41] | +1.05 [+0.38, +1.73] | 7846 |
| Content server | 50 | 40 | +0.46 [+0.11, +0.79] | +0.65 [+0.34, +0.96] | 26105 |
| Validator | 1 | 40 | -3.45 [-3.92, -3.00] | -2.58 [-2.86, -2.30] | 38603 |
| Validator | 15 | 40 | -2.70 [-3.13, -2.27] | -1.91 [-2.18, -1.62] | 33383 |
| Validator | 50 | 40 | -1.75 [-1.92, -1.57] | -1.18 [-1.29, -1.08] | 110616 |
| Gatekeeper | 1 | 40 | +0.16 [-0.24, +0.55] | +1.40 [+1.13, +1.66] | 115809 |
| Gatekeeper | 15 | 40 | +0.27 [-0.14, +0.68] | +1.18 [+0.93, +1.42] | 100149 |
| Gatekeeper | 50 | 40 | +0.38 [+0.19, +0.55] | +0.66 [+0.58, +0.75] | 331848 |

## Change from the rmix_s build on the same records

Accuracy in this build minus accuracy in the rmix_s build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -0.09 [-0.17, -0.01] | -0.01 [-0.09, +0.07] | 39834 |
| Baseline | 15 | 40 | -0.09 [-0.15, -0.03] | -0.03 [-0.09, +0.03] | 51804 |
| Baseline | 50 | 40 | -0.02 [-0.04, +0.00] | -0.04 [-0.07, -0.01] | 172471 |
| First hop, credential | 1 | 40 | -0.08 [-0.14, -0.03] | -0.02 [-0.08, +0.03] | 159336 |
| First hop, credential | 15 | 40 | -0.08 [-0.13, -0.03] | -0.01 [-0.05, +0.03] | 207216 |
| First hop, credential | 50 | 40 | -0.03 [-0.05, -0.01] | -0.02 [-0.04, -0.00] | 689884 |
| First hop, content | 1 | 40 | -0.08 [-0.14, -0.03] | -0.02 [-0.08, +0.03] | 159336 |
| First hop, content | 15 | 40 | -0.08 [-0.12, -0.03] | -0.01 [-0.05, +0.03] | 207216 |
| First hop, content | 50 | 40 | -0.03 [-0.05, -0.01] | -0.02 [-0.04, -0.00] | 689884 |
| Credential processor | 1 | 40 | -0.05 [-0.11, +0.01] | -0.07 [-0.13, -0.01] | 159336 |
| Credential processor | 15 | 40 | -0.08 [-0.14, -0.03] | -0.04 [-0.09, +0.00] | 207216 |
| Credential processor | 50 | 40 | -0.03 [-0.05, -0.00] | -0.03 [-0.05, -0.01] | 689884 |
| Content server | 1 | 40 | -0.02 [-0.11, +0.07] | -0.04 [-0.15, +0.06] | 79668 |
| Content server | 15 | 40 | -0.05 [-0.13, +0.03] | -0.04 [-0.13, +0.04] | 103608 |
| Content server | 50 | 40 | -0.01 [-0.05, +0.02] | +0.01 [-0.02, +0.05] | 344942 |
| Validator | 1 | 40 | +0.08 [-0.04, +0.21] | -0.08 [-0.28, +0.10] | 39834 |
| Validator | 15 | 40 | +0.06 [-0.05, +0.16] | -0.07 [-0.23, +0.08] | 51804 |
| Validator | 50 | 40 | +0.03 [-0.02, +0.07] | +0.01 [-0.06, +0.08] | 172471 |
| Gatekeeper | 1 | 40 | -0.07 [-0.12, -0.01] | -0.09 [-0.13, -0.04] | 119502 |
| Gatekeeper | 15 | 40 | -0.11 [-0.17, -0.06] | -0.07 [-0.11, -0.04] | 155412 |
| Gatekeeper | 50 | 40 | -0.03 [-0.05, -0.01] | -0.02 [-0.04, -0.00] | 517413 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.62% [8.26%, 8.97%] | 1.56% | 8.62% | 0.00% [0.00%, 0.00%] | 6.62% [6.38%, 6.90%] | 2.44% | 6.62% | 0.00% [0.00%, 0.00%] | 0.564 [0.552, 0.576] | 19.3% | 14.1% | 0.000% | 200 | 39834 |
| R = 15, 40 decoys, bundling on | 7.12% [6.88%, 7.37%] | 1.16% | 7.12% | 0.00% [0.00%, 0.00%] | 4.90% [4.73%, 5.07%] | 1.82% | 4.90% | 0.00% [0.00%, 0.00%] | 0.566 [0.556, 0.576] | 16.2% | 12.6% | 0.014% | 200 | 51804 |
| R = 50, 40 decoys, bundling on | 4.87% [4.77%, 4.97%] | 0.71% | 4.87% | 0.00% [0.00%, 0.00%] | 3.12% [3.04%, 3.20%] | 1.11% | 3.12% | 0.00% [0.00%, 0.00%] | 0.561 [0.555, 0.568] | 9.7% | 7.6% | 0.000% | 200 | 172471 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.65% [8.31%, 8.98%] | 1.56% | 8.62% | 0.03% [-0.07%, 0.13%] | 6.72% [6.53%, 6.93%] | 2.44% | 6.62% | 0.10% [-0.03%, 0.22%] | 0.562 [0.551, 0.573] | 19.4% | 14.3% | 0.000% | 200 | 159336 |
| R = 15, 40 decoys, bundling on | 7.06% [6.85%, 7.29%] | 1.16% | 7.12% | -0.07% [-0.14%, 0.01%] | 4.98% [4.85%, 5.11%] | 1.82% | 4.90% | 0.08% [-0.03%, 0.19%] | 0.566 [0.557, 0.575] | 14.1% | 11.8% | 0.000% | 200 | 207216 |
| R = 50, 40 decoys, bundling on | 4.82% [4.73%, 4.91%] | 0.71% | 4.87% | -0.05% [-0.09%, -0.01%] | 3.15% [3.10%, 3.20%] | 1.11% | 3.12% | 0.03% [-0.03%, 0.09%] | 0.560 [0.554, 0.565] | 8.9% | 7.2% | 0.000% | 200 | 689884 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.65% [8.33%, 8.96%] | 1.56% | 8.62% | 0.03% [-0.07%, 0.14%] | 6.72% [6.52%, 6.92%] | 2.44% | 6.62% | 0.10% [-0.03%, 0.22%] | 0.562 [0.551, 0.573] | 19.4% | 14.3% | 0.000% | 200 | 159336 |
| R = 15, 40 decoys, bundling on | 7.06% [6.84%, 7.28%] | 1.16% | 7.12% | -0.07% [-0.14%, 0.01%] | 4.98% [4.84%, 5.12%] | 1.82% | 4.90% | 0.08% [-0.02%, 0.19%] | 0.566 [0.557, 0.575] | 14.1% | 11.8% | 0.000% | 200 | 207216 |
| R = 50, 40 decoys, bundling on | 4.82% [4.72%, 4.90%] | 0.71% | 4.87% | -0.05% [-0.09%, -0.01%] | 3.15% [3.10%, 3.20%] | 1.11% | 3.12% | 0.03% [-0.03%, 0.09%] | 0.560 [0.554, 0.565] | 8.9% | 7.2% | 0.000% | 200 | 689884 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.64% [8.28%, 9.00%] | 1.56% | 8.62% | 0.02% [-0.03%, 0.07%] | 6.61% [6.38%, 6.84%] | 2.44% | 6.62% | -0.01% [-0.11%, 0.08%] | 0.562 [0.550, 0.575] | 19.6% | 14.4% | 0.000% | 200 | 159336 |
| R = 15, 40 decoys, bundling on | 7.10% [6.87%, 7.36%] | 1.16% | 7.12% | -0.02% [-0.06%, 0.01%] | 4.91% [4.74%, 5.08%] | 1.82% | 4.90% | 0.01% [-0.05%, 0.07%] | 0.567 [0.557, 0.577] | 16.1% | 12.5% | 0.012% | 200 | 207216 |
| R = 50, 40 decoys, bundling on | 4.86% [4.76%, 4.96%] | 0.71% | 4.87% | -0.01% [-0.02%, 0.01%] | 3.11% [3.03%, 3.18%] | 1.11% | 3.12% | -0.01% [-0.04%, 0.01%] | 0.562 [0.556, 0.568] | 9.7% | 7.6% | 0.000% | 200 | 689884 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 10.35% [10.06%, 10.65%] | 1.58% | 8.62% | 1.74% [1.49%, 1.99%] | 8.15% [7.95%, 8.37%] | 2.44% | 6.62% | 1.53% [1.27%, 1.77%] | 0.580 [0.571, 0.588] | 13.8% | 16.1% | 0.000% | 200 | 79668 |
| R = 15, 40 decoys, bundling on | 8.33% [8.10%, 8.56%] | 1.18% | 7.12% | 1.21% [1.02%, 1.40%] | 6.08% [5.93%, 6.23%] | 1.82% | 4.90% | 1.18% [0.96%, 1.40%] | 0.580 [0.571, 0.588] | 9.7% | 12.7% | 0.000% | 200 | 103608 |
| R = 50, 40 decoys, bundling on | 5.68% [5.60%, 5.77%] | 0.72% | 4.87% | 0.81% [0.74%, 0.89%] | 3.80% [3.73%, 3.87%] | 1.11% | 3.12% | 0.68% [0.60%, 0.77%] | 0.576 [0.571, 0.580] | 5.6% | 8.2% | 0.000% | 200 | 344942 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.09% [5.73%, 6.44%] | 1.40% | 8.62% | -2.53% [-2.88%, -2.18%] | 2.81% [2.65%, 2.97%] | 2.44% | 6.62% | -3.82% [-4.12%, -3.52%] | 0.562 [0.546, 0.577] | 10.3% | 10.4% | 0.000% | 200 | 39834 |
| R = 15, 40 decoys, bundling on | 4.94% [4.70%, 5.19%] | 1.04% | 7.12% | -2.19% [-2.41%, -1.98%] | 2.14% [2.01%, 2.27%] | 1.82% | 4.90% | -2.76% [-2.98%, -2.55%] | 0.555 [0.542, 0.569] | 9.8% | 7.7% | 0.000% | 200 | 51804 |
| R = 50, 40 decoys, bundling on | 3.39% [3.29%, 3.48%] | 0.64% | 4.87% | -1.48% [-1.59%, -1.38%] | 1.32% [1.26%, 1.38%] | 1.11% | 3.12% | -1.80% [-1.90%, -1.71%] | 0.546 [0.539, 0.554] | 5.8% | 4.9% | 0.000% | 200 | 172471 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.58% [8.25%, 8.90%] | 1.56% | 8.62% | -0.04% [-0.14%, 0.07%] | 6.47% [6.26%, 6.65%] | 2.44% | 6.62% | -0.16% [-0.34%, 0.02%] | 0.561 [0.548, 0.573] | 19.7% | 14.5% | 0.000% | 200 | 119502 |
| R = 15, 40 decoys, bundling on | 7.07% [6.83%, 7.30%] | 1.16% | 7.12% | -0.05% [-0.14%, 0.03%] | 4.84% [4.69%, 5.00%] | 1.82% | 4.90% | -0.06% [-0.20%, 0.08%] | 0.566 [0.557, 0.576] | 16.0% | 12.4% | 0.016% | 200 | 155412 |
| R = 50, 40 decoys, bundling on | 4.82% [4.73%, 4.92%] | 0.71% | 4.87% | -0.04% [-0.08%, -0.01%] | 3.03% [2.97%, 3.09%] | 1.11% | 3.12% | -0.09% [-0.16%, -0.02%] | 0.564 [0.558, 0.570] | 9.8% | 7.6% | 0.000% | 200 | 517413 |

## Outcome-shuffle control (stable cells)

21 stable cells; 5 with a shuffled-outcome AUC interval excluding 0.5: R15_D40_B first_hop_cred (0.506), R15_D40_B first_hop_content (0.505), R15_D40_B validator (0.517), R50_D40_B first_hop_content (0.504), R50_D40_B gatekeeper (0.505).

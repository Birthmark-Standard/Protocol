# Tables

Record-to-device linking with genuine decoys, the r150 relay hold, a static content-server hold, and the post-match lottery in the residual case. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 1 | 40 | 1.97 | 14.0% | 27.5% | 41.5% | 31.9% | 14.0% | 2,501,686 |
| 15 | 40 | 2.65 | 7.0% | 18.7% | 25.8% | 20.1% | 7.1% | 215,400 |
| 50 | 40 | 4.31 | 1.3% | 5.7% | 7.0% | 5.8% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -0.43 [-0.84, +0.00] | -0.35 [-0.69, -0.03] | 38912 |
| Baseline | 15 | 40 | -0.24 [-0.70, +0.20] | -0.25 [-0.53, +0.02] | 37806 |
| Baseline | 50 | 40 | -0.06 [-0.23, +0.10] | -0.16 [-0.27, -0.05] | 125448 |
| First hop, credential | 1 | 40 | -0.45 [-0.87, -0.02] | -0.27 [-0.48, -0.05] | 155648 |
| First hop, credential | 15 | 40 | -0.29 [-0.70, +0.12] | -0.23 [-0.39, -0.06] | 151224 |
| First hop, credential | 50 | 40 | -0.08 [-0.24, +0.09] | -0.21 [-0.28, -0.13] | 501792 |
| First hop, content | 1 | 40 | -0.45 [-0.85, -0.04] | -0.27 [-0.49, -0.04] | 155648 |
| First hop, content | 15 | 40 | -0.29 [-0.70, +0.14] | -0.23 [-0.41, -0.04] | 151224 |
| First hop, content | 50 | 40 | -0.08 [-0.24, +0.08] | -0.21 [-0.28, -0.14] | 501792 |
| Credential processor | 1 | 40 | -0.51 [-0.92, -0.07] | -0.43 [-0.70, -0.18] | 155648 |
| Credential processor | 15 | 40 | -0.23 [-0.68, +0.19] | -0.24 [-0.48, +0.01] | 151224 |
| Credential processor | 50 | 40 | -0.05 [-0.22, +0.12] | -0.16 [-0.27, -0.06] | 501792 |
| Content server | 1 | 40 | -1.17 [-1.98, -0.36] | -1.36 [-1.99, -0.70] | 9205 |
| Content server | 15 | 40 | -0.87 [-1.59, -0.11] | -1.27 [-1.88, -0.66] | 8873 |
| Content server | 50 | 40 | -0.84 [-1.16, -0.52] | -0.65 [-0.90, -0.37] | 29448 |
| Validator | 1 | 40 | -3.57 [-4.03, -3.12] | -3.07 [-3.37, -2.77] | 38912 |
| Validator | 15 | 40 | -2.99 [-3.38, -2.56] | -2.38 [-2.61, -2.14] | 37806 |
| Validator | 50 | 40 | -1.84 [-2.01, -1.66] | -1.42 [-1.51, -1.33] | 125448 |
| Gatekeeper | 1 | 40 | -0.44 [-0.85, -0.04] | -0.43 [-0.65, -0.22] | 116736 |
| Gatekeeper | 15 | 40 | -0.32 [-0.73, +0.13] | -0.18 [-0.36, +0.02] | 113418 |
| Gatekeeper | 50 | 40 | -0.09 [-0.26, +0.08] | -0.19 [-0.26, -0.12] | 376344 |

## Change from the r150_s build on the same records

Accuracy in this build minus accuracy in the r150_s build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -0.07 [-0.17, +0.03] | +0.14 [-0.04, +0.31] | 39913 |
| Baseline | 15 | 40 | -0.04 [-0.12, +0.04] | -0.07 [-0.20, +0.06] | 51859 |
| Baseline | 50 | 40 | -0.01 [-0.05, +0.02] | +0.03 [-0.03, +0.09] | 172729 |
| First hop, credential | 1 | 40 | -0.11 [-0.18, -0.04] | +0.05 [-0.06, +0.16] | 159652 |
| First hop, credential | 15 | 40 | -0.04 [-0.10, +0.02] | -0.06 [-0.13, +0.01] | 207436 |
| First hop, credential | 50 | 40 | -0.02 [-0.04, +0.01] | -0.04 [-0.06, -0.01] | 690916 |
| First hop, content | 1 | 40 | -0.11 [-0.18, -0.04] | +0.05 [-0.06, +0.16] | 159652 |
| First hop, content | 15 | 40 | -0.04 [-0.09, +0.02] | -0.06 [-0.13, +0.01] | 207436 |
| First hop, content | 50 | 40 | -0.02 [-0.04, +0.01] | -0.04 [-0.06, -0.01] | 690916 |
| Credential processor | 1 | 40 | -0.08 [-0.17, +0.01] | -0.01 [-0.15, +0.12] | 159652 |
| Credential processor | 15 | 40 | -0.05 [-0.12, +0.01] | -0.02 [-0.13, +0.08] | 207436 |
| Credential processor | 50 | 40 | -0.01 [-0.04, +0.02] | +0.03 [-0.02, +0.08] | 690916 |
| Content server | 1 | 40 | -0.12 [-0.23, -0.01] | -0.09 [-0.20, +0.02] | 79826 |
| Content server | 15 | 40 | +0.03 [-0.05, +0.10] | +0.06 [-0.03, +0.15] | 103718 |
| Content server | 50 | 40 | -0.02 [-0.06, +0.01] | -0.02 [-0.05, +0.02] | 345458 |
| Validator | 1 | 40 | -0.02 [-0.14, +0.11] | +0.05 [-0.11, +0.21] | 39913 |
| Validator | 15 | 40 | -0.01 [-0.11, +0.09] | -0.12 [-0.26, +0.02] | 51859 |
| Validator | 50 | 40 | +0.05 [+0.00, +0.09] | +0.01 [-0.04, +0.06] | 172729 |
| Gatekeeper | 1 | 40 | -0.05 [-0.12, +0.03] | -0.05 [-0.13, +0.04] | 119739 |
| Gatekeeper | 15 | 40 | -0.05 [-0.10, +0.00] | +0.01 [-0.06, +0.07] | 155577 |
| Gatekeeper | 50 | 40 | -0.01 [-0.03, +0.02] | +0.00 [-0.03, +0.03] | 518187 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.03% [7.69%, 8.37%] | 2.01% | 8.03% | 0.00% [0.00%, 0.00%] | 4.85% [4.64%, 5.06%] | 2.44% | 4.85% | 0.00% [0.00%, 0.00%] | 0.579 [0.566, 0.593] | 16.3% | 15.1% | 0.018% | 200 | 39913 |
| R = 15, 40 decoys, bundling on | 6.55% [6.28%, 6.82%] | 1.49% | 6.55% | 0.00% [0.00%, 0.00%] | 3.47% [3.32%, 3.63%] | 1.82% | 3.47% | 0.00% [0.00%, 0.00%] | 0.568 [0.556, 0.579] | 12.7% | 10.7% | 0.000% | 200 | 51859 |
| R = 50, 40 decoys, bundling on | 4.38% [4.28%, 4.48%] | 0.92% | 4.38% | 0.00% [0.00%, 0.00%] | 2.20% [2.14%, 2.27%] | 1.11% | 2.20% | 0.00% [0.00%, 0.00%] | 0.551 [0.544, 0.558] | 8.6% | 6.9% | 0.000% | 200 | 172729 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.00% [7.68%, 8.31%] | 2.01% | 8.03% | -0.04% [-0.13%, 0.05%] | 4.86% [4.73%, 5.01%] | 2.44% | 4.85% | 0.02% [-0.14%, 0.16%] | 0.582 [0.569, 0.594] | 16.8% | 15.1% | 0.019% | 200 | 159652 |
| R = 15, 40 decoys, bundling on | 6.55% [6.31%, 6.80%] | 1.49% | 6.55% | 0.00% [-0.07%, 0.07%] | 3.60% [3.49%, 3.70%] | 1.82% | 3.47% | 0.13% [0.00%, 0.25%] | 0.568 [0.558, 0.579] | 12.9% | 10.5% | 0.000% | 200 | 207436 |
| R = 50, 40 decoys, bundling on | 4.34% [4.26%, 4.43%] | 0.92% | 4.38% | -0.04% [-0.07%, -0.00%] | 2.19% [2.16%, 2.23%] | 1.11% | 2.20% | -0.01% [-0.07%, 0.05%] | 0.554 [0.548, 0.560] | 8.5% | 6.8% | 0.000% | 200 | 690916 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.00% [7.69%, 8.31%] | 2.01% | 8.03% | -0.04% [-0.12%, 0.05%] | 4.86% [4.73%, 5.00%] | 2.44% | 4.85% | 0.02% [-0.13%, 0.16%] | 0.582 [0.569, 0.594] | 16.8% | 15.1% | 0.019% | 200 | 159652 |
| R = 15, 40 decoys, bundling on | 6.55% [6.30%, 6.79%] | 1.49% | 6.55% | 0.00% [-0.07%, 0.08%] | 3.60% [3.50%, 3.70%] | 1.82% | 3.47% | 0.13% [0.01%, 0.25%] | 0.568 [0.558, 0.579] | 12.9% | 10.5% | 0.000% | 200 | 207436 |
| R = 50, 40 decoys, bundling on | 4.34% [4.25%, 4.43%] | 0.92% | 4.38% | -0.04% [-0.07%, -0.00%] | 2.19% [2.15%, 2.23%] | 1.11% | 2.20% | -0.01% [-0.07%, 0.05%] | 0.554 [0.548, 0.560] | 8.5% | 6.8% | 0.000% | 200 | 690916 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.01% [7.69%, 8.35%] | 2.01% | 8.03% | -0.02% [-0.07%, 0.02%] | 4.72% [4.56%, 4.90%] | 2.44% | 4.85% | -0.12% [-0.24%, -0.02%] | 0.580 [0.567, 0.593] | 15.7% | 14.9% | 0.019% | 200 | 159652 |
| R = 15, 40 decoys, bundling on | 6.54% [6.28%, 6.81%] | 1.49% | 6.55% | -0.00% [-0.04%, 0.03%] | 3.53% [3.39%, 3.67%] | 1.82% | 3.47% | 0.06% [-0.02%, 0.14%] | 0.568 [0.556, 0.579] | 12.6% | 10.7% | 0.000% | 200 | 207436 |
| R = 50, 40 decoys, bundling on | 4.38% [4.28%, 4.48%] | 0.92% | 4.38% | -0.00% [-0.01%, 0.01%] | 2.23% [2.17%, 2.28%] | 1.11% | 2.20% | 0.02% [-0.00%, 0.05%] | 0.552 [0.545, 0.559] | 8.7% | 6.9% | 0.000% | 200 | 690916 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.04% [7.75%, 8.32%] | 2.11% | 8.03% | 0.01% [-0.20%, 0.21%] | 5.05% [4.89%, 5.21%] | 2.44% | 4.85% | 0.20% [-0.05%, 0.46%] | 0.571 [0.561, 0.581] | 8.8% | 11.6% | 0.001% | 200 | 79826 |
| R = 15, 40 decoys, bundling on | 6.64% [6.42%, 6.87%] | 1.57% | 6.55% | 0.09% [-0.07%, 0.25%] | 3.79% [3.68%, 3.91%] | 1.82% | 3.47% | 0.32% [0.13%, 0.51%] | 0.565 [0.555, 0.574] | 8.5% | 8.8% | 0.000% | 200 | 103718 |
| R = 50, 40 decoys, bundling on | 4.29% [4.21%, 4.38%] | 0.96% | 4.38% | -0.08% [-0.15%, -0.01%] | 2.32% [2.26%, 2.38%] | 1.11% | 2.20% | 0.12% [0.05%, 0.20%] | 0.551 [0.545, 0.557] | 4.7% | 5.6% | 0.000% | 200 | 345458 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.00% [5.65%, 6.35%] | 1.65% | 8.03% | -2.03% [-2.33%, -1.74%] | 2.36% [2.21%, 2.51%] | 2.44% | 4.85% | -2.49% [-2.73%, -2.25%] | 0.563 [0.546, 0.580] | 8.5% | 9.1% | 0.013% | 200 | 39913 |
| R = 15, 40 decoys, bundling on | 4.82% [4.60%, 5.06%] | 1.23% | 6.55% | -1.73% [-2.01%, -1.45%] | 1.62% [1.50%, 1.74%] | 1.82% | 3.47% | -1.86% [-2.06%, -1.65%] | 0.559 [0.545, 0.573] | 5.0% | 7.5% | 0.000% | 200 | 51859 |
| R = 50, 40 decoys, bundling on | 3.21% [3.11%, 3.31%] | 0.75% | 4.38% | -1.17% [-1.28%, -1.06%] | 1.04% [1.00%, 1.09%] | 1.11% | 2.20% | -1.16% [-1.23%, -1.08%] | 0.554 [0.546, 0.562] | 5.2% | 4.9% | 0.000% | 200 | 172729 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.99% [7.66%, 8.31%] | 2.01% | 8.03% | -0.04% [-0.14%, 0.05%] | 4.70% [4.54%, 4.85%] | 2.44% | 4.85% | -0.15% [-0.35%, 0.07%] | 0.582 [0.569, 0.594] | 15.1% | 14.6% | 0.019% | 200 | 119739 |
| R = 15, 40 decoys, bundling on | 6.50% [6.23%, 6.76%] | 1.49% | 6.55% | -0.05% [-0.12%, 0.02%] | 3.52% [3.41%, 3.63%] | 1.82% | 3.47% | 0.05% [-0.10%, 0.19%] | 0.568 [0.557, 0.580] | 12.0% | 10.4% | 0.000% | 200 | 155577 |
| R = 50, 40 decoys, bundling on | 4.34% [4.25%, 4.43%] | 0.92% | 4.38% | -0.04% [-0.07%, -0.01%] | 2.16% [2.11%, 2.21%] | 1.11% | 2.20% | -0.04% [-0.10%, 0.02%] | 0.554 [0.547, 0.560] | 8.9% | 6.8% | 0.000% | 200 | 518187 |

## Outcome-shuffle control (stable cells)

21 stable cells; 3 with a shuffled-outcome AUC interval excluding 0.5: R1_D40_B first_hop_cred (0.510), R15_D40_B baseline (0.510), R50_D40_B validator (0.515).

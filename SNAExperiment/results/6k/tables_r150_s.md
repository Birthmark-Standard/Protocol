# Tables

Record-to-device linking with genuine decoys, the r150 relay hold and a static content-server hold. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 40 | -0.36 [-0.75, +0.06] | -0.51 [-0.82, -0.22] | 38912 |
| Baseline | 15 | 40 | -0.17 [-0.63, +0.26] | -0.17 [-0.44, +0.12] | 37806 |
| Baseline | 50 | 40 | -0.06 [-0.22, +0.12] | -0.17 [-0.29, -0.05] | 125448 |
| First hop, credential | 1 | 40 | -0.34 [-0.76, +0.08] | -0.33 [-0.55, -0.13] | 155648 |
| First hop, credential | 15 | 40 | -0.21 [-0.63, +0.18] | -0.17 [-0.34, +0.01] | 151224 |
| First hop, credential | 50 | 40 | -0.07 [-0.24, +0.08] | -0.17 [-0.24, -0.10] | 501792 |
| First hop, content | 1 | 40 | -0.34 [-0.74, +0.09] | -0.33 [-0.54, -0.12] | 155648 |
| First hop, content | 15 | 40 | -0.21 [-0.61, +0.19] | -0.17 [-0.34, +0.01] | 151224 |
| First hop, content | 50 | 40 | -0.07 [-0.24, +0.08] | -0.17 [-0.24, -0.10] | 501792 |
| Credential processor | 1 | 40 | -0.42 [-0.84, +0.01] | -0.43 [-0.68, -0.19] | 155648 |
| Credential processor | 15 | 40 | -0.14 [-0.57, +0.29] | -0.17 [-0.41, +0.08] | 151224 |
| Credential processor | 50 | 40 | -0.06 [-0.23, +0.12] | -0.18 [-0.29, -0.08] | 501792 |
| Content server | 1 | 40 | -1.22 [-2.00, -0.37] | -1.34 [-1.95, -0.71] | 9205 |
| Content server | 15 | 40 | -0.95 [-1.71, -0.17] | -1.36 [-1.99, -0.72] | 8873 |
| Content server | 50 | 40 | -0.81 [-1.16, -0.49] | -0.57 [-0.84, -0.32] | 29448 |
| Validator | 1 | 40 | -3.55 [-4.02, -3.09] | -3.13 [-3.41, -2.83] | 38912 |
| Validator | 15 | 40 | -3.00 [-3.41, -2.57] | -2.30 [-2.53, -2.08] | 37806 |
| Validator | 50 | 40 | -1.90 [-2.07, -1.73] | -1.43 [-1.53, -1.34] | 125448 |
| Gatekeeper | 1 | 40 | -0.38 [-0.80, +0.02] | -0.39 [-0.61, -0.17] | 116736 |
| Gatekeeper | 15 | 40 | -0.26 [-0.66, +0.18] | -0.18 [-0.37, +0.02] | 113418 |
| Gatekeeper | 50 | 40 | -0.08 [-0.25, +0.09] | -0.21 [-0.28, -0.14] | 376344 |

## Change from the r150 build on the same records

Accuracy in this build minus accuracy in the r150 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +1.24 [+0.81, +1.70] | +0.80 [+0.52, +1.08] | 39106 |
| Baseline | 15 | 40 | +1.02 [+0.63, +1.40] | +0.63 [+0.37, +0.89] | 40685 |
| Baseline | 50 | 40 | +0.60 [+0.44, +0.76] | +0.32 [+0.21, +0.42] | 134833 |
| First hop, credential | 1 | 40 | +1.21 [+0.84, +1.61] | +0.83 [+0.66, +1.02] | 156424 |
| First hop, credential | 15 | 40 | +0.97 [+0.63, +1.33] | +0.70 [+0.53, +0.85] | 162740 |
| First hop, credential | 50 | 40 | +0.54 [+0.40, +0.68] | +0.39 [+0.34, +0.44] | 539332 |
| First hop, content | 1 | 40 | +1.21 [+0.82, +1.61] | +0.83 [+0.65, +1.02] | 156424 |
| First hop, content | 15 | 40 | +0.97 [+0.61, +1.31] | +0.70 [+0.54, +0.85] | 162740 |
| First hop, content | 50 | 40 | +0.54 [+0.40, +0.69] | +0.39 [+0.34, +0.44] | 539332 |
| Credential processor | 1 | 40 | +1.24 [+0.82, +1.69] | +0.78 [+0.54, +1.01] | 156424 |
| Credential processor | 15 | 40 | +1.01 [+0.62, +1.38] | +0.65 [+0.43, +0.86] | 162740 |
| Credential processor | 50 | 40 | +0.59 [+0.43, +0.74] | +0.35 [+0.26, +0.44] | 539332 |
| Content server | 1 | 40 | +0.33 [-0.55, +1.19] | +0.77 [+0.15, +1.40] | 9228 |
| Content server | 15 | 40 | +0.17 [-0.60, +0.90] | -0.34 [-0.90, +0.24] | 9501 |
| Content server | 50 | 40 | +0.08 [-0.23, +0.40] | +0.09 [-0.15, +0.34] | 32085 |
| Validator | 1 | 40 | -2.54 [-2.98, -2.12] | -2.28 [-2.55, -2.03] | 39106 |
| Validator | 15 | 40 | -2.19 [-2.57, -1.82] | -1.61 [-1.82, -1.41] | 40685 |
| Validator | 50 | 40 | -1.66 [-1.82, -1.50] | -1.12 [-1.21, -1.04] | 134833 |
| Gatekeeper | 1 | 40 | +1.14 [+0.72, +1.53] | +0.80 [+0.59, +1.00] | 117318 |
| Gatekeeper | 15 | 40 | +0.95 [+0.57, +1.33] | +0.63 [+0.47, +0.79] | 122055 |
| Gatekeeper | 50 | 40 | +0.55 [+0.40, +0.70] | +0.34 [+0.27, +0.41] | 404499 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.10% [7.76%, 8.44%] | 2.11% | 8.10% | 0.00% [0.00%, 0.00%] | 4.71% [4.51%, 4.90%] | 2.44% | 4.71% | 0.00% [0.00%, 0.00%] | 0.581 [0.568, 0.594] | 17.3% | 14.8% | 0.018% | 200 | 39913 |
| R = 15, 40 decoys, bundling on | 6.59% [6.31%, 6.86%] | 1.57% | 6.59% | 0.00% [0.00%, 0.00%] | 3.54% [3.38%, 3.71%] | 1.82% | 3.54% | 0.00% [0.00%, 0.00%] | 0.567 [0.556, 0.579] | 11.8% | 10.8% | 0.000% | 200 | 51859 |
| R = 50, 40 decoys, bundling on | 4.39% [4.28%, 4.49%] | 0.96% | 4.39% | 0.00% [0.00%, 0.00%] | 2.17% [2.11%, 2.24%] | 1.11% | 2.17% | 0.00% [0.00%, 0.00%] | 0.552 [0.545, 0.559] | 8.7% | 6.9% | 0.000% | 200 | 172729 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.10% [7.78%, 8.41%] | 2.11% | 8.10% | 0.00% [-0.08%, 0.10%] | 4.81% [4.68%, 4.94%] | 2.44% | 4.71% | 0.10% [-0.03%, 0.24%] | 0.581 [0.569, 0.594] | 17.5% | 14.9% | 0.012% | 200 | 159652 |
| R = 15, 40 decoys, bundling on | 6.59% [6.34%, 6.85%] | 1.57% | 6.59% | 0.00% [-0.07%, 0.08%] | 3.66% [3.55%, 3.76%] | 1.82% | 3.54% | 0.12% [-0.01%, 0.24%] | 0.566 [0.556, 0.577] | 12.3% | 10.5% | 0.000% | 200 | 207436 |
| R = 50, 40 decoys, bundling on | 4.36% [4.27%, 4.45%] | 0.96% | 4.39% | -0.03% [-0.06%, 0.00%] | 2.23% [2.19%, 2.26%] | 1.11% | 2.17% | 0.06% [-0.01%, 0.11%] | 0.554 [0.548, 0.560] | 8.6% | 6.8% | 0.000% | 200 | 690916 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.10% [7.80%, 8.43%] | 2.11% | 8.10% | 0.00% [-0.09%, 0.09%] | 4.81% [4.69%, 4.94%] | 2.44% | 4.71% | 0.10% [-0.03%, 0.24%] | 0.581 [0.569, 0.594] | 17.5% | 14.9% | 0.012% | 200 | 159652 |
| R = 15, 40 decoys, bundling on | 6.59% [6.36%, 6.84%] | 1.57% | 6.59% | 0.00% [-0.07%, 0.07%] | 3.66% [3.55%, 3.76%] | 1.82% | 3.54% | 0.12% [-0.01%, 0.24%] | 0.566 [0.556, 0.577] | 12.3% | 10.5% | 0.000% | 200 | 207436 |
| R = 50, 40 decoys, bundling on | 4.36% [4.27%, 4.45%] | 0.96% | 4.39% | -0.03% [-0.06%, 0.00%] | 2.23% [2.20%, 2.26%] | 1.11% | 2.17% | 0.06% [-0.01%, 0.12%] | 0.554 [0.548, 0.560] | 8.6% | 6.8% | 0.000% | 200 | 690916 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.09% [7.76%, 8.42%] | 2.11% | 8.10% | -0.01% [-0.05%, 0.04%] | 4.74% [4.57%, 4.91%] | 2.44% | 4.71% | 0.03% [-0.07%, 0.14%] | 0.581 [0.568, 0.594] | 16.9% | 14.7% | 0.019% | 200 | 159652 |
| R = 15, 40 decoys, bundling on | 6.60% [6.33%, 6.87%] | 1.57% | 6.59% | 0.01% [-0.02%, 0.04%] | 3.56% [3.42%, 3.70%] | 1.82% | 3.54% | 0.02% [-0.06%, 0.10%] | 0.567 [0.555, 0.578] | 11.7% | 10.7% | 0.000% | 200 | 207436 |
| R = 50, 40 decoys, bundling on | 4.39% [4.29%, 4.49%] | 0.96% | 4.39% | -0.00% [-0.01%, 0.01%] | 2.19% [2.13%, 2.25%] | 1.11% | 2.17% | 0.02% [-0.01%, 0.05%] | 0.552 [0.545, 0.559] | 8.8% | 7.0% | 0.000% | 200 | 690916 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.16% [7.86%, 8.45%] | 2.18% | 8.10% | 0.06% [-0.14%, 0.26%] | 5.14% [4.98%, 5.29%] | 2.44% | 4.71% | 0.43% [0.19%, 0.67%] | 0.574 [0.564, 0.584] | 12.3% | 12.4% | 0.000% | 200 | 79826 |
| R = 15, 40 decoys, bundling on | 6.62% [6.40%, 6.84%] | 1.62% | 6.59% | 0.03% [-0.13%, 0.18%] | 3.74% [3.63%, 3.85%] | 1.82% | 3.54% | 0.20% [0.00%, 0.39%] | 0.564 [0.555, 0.574] | 7.6% | 8.9% | 0.000% | 200 | 103718 |
| R = 50, 40 decoys, bundling on | 4.32% [4.23%, 4.40%] | 1.00% | 4.39% | -0.07% [-0.15%, 0.00%] | 2.34% [2.29%, 2.39%] | 1.11% | 2.17% | 0.16% [0.09%, 0.24%] | 0.549 [0.544, 0.555] | 4.8% | 5.7% | 0.000% | 200 | 345458 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.02% [5.68%, 6.35%] | 1.64% | 8.10% | -2.08% [-2.39%, -1.78%] | 2.31% [2.17%, 2.45%] | 2.44% | 4.71% | -2.40% [-2.64%, -2.16%] | 0.561 [0.544, 0.578] | 8.0% | 8.7% | 0.018% | 200 | 39913 |
| R = 15, 40 decoys, bundling on | 4.83% [4.60%, 5.08%] | 1.22% | 6.59% | -1.75% [-2.02%, -1.49%] | 1.74% [1.63%, 1.85%] | 1.82% | 3.54% | -1.80% [-1.99%, -1.61%] | 0.557 [0.543, 0.571] | 6.2% | 7.9% | 0.000% | 200 | 51859 |
| R = 50, 40 decoys, bundling on | 3.16% [3.06%, 3.26%] | 0.75% | 4.39% | -1.23% [-1.34%, -1.12%] | 1.03% [0.98%, 1.08%] | 1.11% | 2.17% | -1.14% [-1.23%, -1.06%] | 0.554 [0.546, 0.562] | 5.6% | 5.0% | 0.000% | 200 | 172729 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.04% [7.71%, 8.36%] | 2.11% | 8.10% | -0.06% [-0.16%, 0.03%] | 4.74% [4.58%, 4.91%] | 2.44% | 4.71% | 0.04% [-0.17%, 0.24%] | 0.581 [0.569, 0.594] | 15.4% | 14.7% | 0.019% | 200 | 119739 |
| R = 15, 40 decoys, bundling on | 6.55% [6.28%, 6.80%] | 1.57% | 6.59% | -0.04% [-0.12%, 0.04%] | 3.51% [3.40%, 3.62%] | 1.82% | 3.54% | -0.03% [-0.19%, 0.13%] | 0.566 [0.555, 0.577] | 12.0% | 10.6% | 0.000% | 200 | 155577 |
| R = 50, 40 decoys, bundling on | 4.35% [4.25%, 4.44%] | 0.96% | 4.39% | -0.04% [-0.08%, -0.01%] | 2.16% [2.11%, 2.21%] | 1.11% | 2.17% | -0.01% [-0.08%, 0.05%] | 0.554 [0.548, 0.561] | 8.8% | 6.9% | 0.000% | 200 | 518187 |

## Outcome-shuffle control (stable cells)

21 stable cells; 4 with a shuffled-outcome AUC interval excluding 0.5: R1_D40_B first_hop_cred (0.509), R1_D40_B gatekeeper (0.493), R15_D40_B baseline (0.510), R50_D40_B validator (0.516).

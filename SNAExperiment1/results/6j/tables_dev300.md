# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the device's content-channel hold and the content servers' own hold stretched 3 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 1 | 40 | 1.97 | 14.0% | 27.6% | 41.5% | 32.0% | 14.0% | 2,501,697 |
| 15 | 40 | 2.65 | 7.0% | 18.8% | 25.9% | 20.2% | 7.1% | 215,400 |
| 50 | 40 | 4.31 | 1.4% | 5.8% | 7.2% | 5.9% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -2.17 [-2.60, -1.73] | -1.79 [-2.10, -1.52] | 39173 |
| Baseline | 15 | 40 | -2.18 [-2.55, -1.79] | -1.18 [-1.42, -0.96] | 40564 |
| Baseline | 50 | 40 | -1.10 [-1.25, -0.95] | -0.82 [-0.93, -0.72] | 134314 |
| First hop, credential | 1 | 40 | -2.17 [-2.59, -1.75] | -1.75 [-1.94, -1.55] | 156692 |
| First hop, credential | 15 | 40 | -2.23 [-2.56, -1.88] | -1.33 [-1.47, -1.19] | 162256 |
| First hop, credential | 50 | 40 | -1.10 [-1.24, -0.95] | -0.84 [-0.90, -0.78] | 537256 |
| First hop, content | 1 | 40 | -2.17 [-2.57, -1.75] | -1.75 [-1.94, -1.55] | 156692 |
| First hop, content | 15 | 40 | -2.23 [-2.59, -1.87] | -1.33 [-1.48, -1.19] | 162256 |
| First hop, content | 50 | 40 | -1.10 [-1.25, -0.95] | -0.84 [-0.89, -0.78] | 537256 |
| Credential processor | 1 | 40 | -2.22 [-2.64, -1.79] | -1.75 [-2.01, -1.49] | 156692 |
| Credential processor | 15 | 40 | -2.16 [-2.53, -1.79] | -1.20 [-1.41, -0.98] | 162256 |
| Credential processor | 50 | 40 | -1.09 [-1.24, -0.93] | -0.84 [-0.93, -0.76] | 537256 |
| Content server | 1 | 40 | -2.88 [-3.71, -1.99] | -2.01 [-2.68, -1.32] | 9195 |
| Content server | 15 | 40 | -2.73 [-3.49, -1.96] | -1.93 [-2.48, -1.35] | 9452 |
| Content server | 50 | 40 | -1.37 [-1.69, -1.06] | -0.87 [-1.09, -0.64] | 31537 |
| Validator | 1 | 40 | -4.02 [-4.45, -3.60] | -3.32 [-3.62, -3.03] | 39173 |
| Validator | 15 | 40 | -3.72 [-4.11, -3.30] | -2.40 [-2.63, -2.17] | 40564 |
| Validator | 50 | 40 | -2.01 [-2.19, -1.84] | -1.53 [-1.62, -1.43] | 134314 |
| Gatekeeper | 1 | 40 | -2.11 [-2.51, -1.70] | -1.70 [-1.92, -1.48] | 117519 |
| Gatekeeper | 15 | 40 | -2.23 [-2.60, -1.86] | -1.14 [-1.30, -0.98] | 121692 |
| Gatekeeper | 50 | 40 | -1.07 [-1.23, -0.92] | -0.82 [-0.89, -0.75] | 402942 |

## Change from the content300 build on the same records

Accuracy in this build minus accuracy in the content300 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.74 [+0.50, +0.97] | +0.69 [+0.43, +0.93] | 39942 |
| Baseline | 15 | 40 | +0.42 [+0.24, +0.59] | +0.37 [+0.19, +0.56] | 51854 |
| Baseline | 50 | 40 | +0.36 [+0.27, +0.45] | +0.27 [+0.19, +0.34] | 172739 |
| First hop, credential | 1 | 40 | +0.90 [+0.69, +1.10] | +0.69 [+0.55, +0.83] | 159768 |
| First hop, credential | 15 | 40 | +0.46 [+0.29, +0.61] | +0.45 [+0.34, +0.55] | 207416 |
| First hop, credential | 50 | 40 | +0.42 [+0.34, +0.49] | +0.30 [+0.25, +0.34] | 690956 |
| First hop, content | 1 | 40 | +0.90 [+0.69, +1.11] | +0.69 [+0.53, +0.85] | 159768 |
| First hop, content | 15 | 40 | +0.46 [+0.30, +0.61] | +0.45 [+0.34, +0.55] | 207416 |
| First hop, content | 50 | 40 | +0.42 [+0.34, +0.49] | +0.30 [+0.26, +0.34] | 690956 |
| Credential processor | 1 | 40 | +0.74 [+0.51, +0.97] | +0.64 [+0.43, +0.82] | 159768 |
| Credential processor | 15 | 40 | +0.43 [+0.27, +0.60] | +0.39 [+0.22, +0.55] | 207416 |
| Credential processor | 50 | 40 | +0.36 [+0.27, +0.44] | +0.25 [+0.18, +0.32] | 690956 |
| Content server | 1 | 40 | +1.38 [+1.17, +1.59] | +1.12 [+0.94, +1.30] | 79884 |
| Content server | 15 | 40 | +1.15 [+0.99, +1.30] | +0.95 [+0.80, +1.09] | 103708 |
| Content server | 50 | 40 | +0.89 [+0.82, +0.96] | +0.60 [+0.54, +0.65] | 345478 |
| Validator | 1 | 40 | +0.62 [+0.40, +0.84] | +0.40 [+0.22, +0.59] | 39942 |
| Validator | 15 | 40 | +0.48 [+0.32, +0.65] | +0.46 [+0.31, +0.60] | 51854 |
| Validator | 50 | 40 | +0.29 [+0.21, +0.37] | +0.18 [+0.12, +0.24] | 172739 |
| Gatekeeper | 1 | 40 | +0.84 [+0.64, +1.04] | +0.74 [+0.57, +0.92] | 119826 |
| Gatekeeper | 15 | 40 | +0.44 [+0.29, +0.60] | +0.45 [+0.32, +0.57] | 155562 |
| Gatekeeper | 50 | 40 | +0.36 [+0.28, +0.44] | +0.25 [+0.20, +0.30] | 518217 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.30% [5.95%, 6.64%] | 1.76% | 6.30% | 0.00% [0.00%, 0.00%] | 3.42% [3.24%, 3.61%] | 2.44% | 3.42% | 0.00% [0.00%, 0.00%] | 0.535 [0.520, 0.550] | 8.0% | 8.0% | 0.000% | 200 | 39942 |
| R = 15, 40 decoys, bundling on | 4.83% [4.62%, 5.06%] | 1.31% | 4.83% | 0.00% [0.00%, 0.00%] | 2.50% [2.36%, 2.63%] | 1.82% | 2.50% | 0.00% [0.00%, 0.00%] | 0.543 [0.528, 0.557] | 4.2% | 6.0% | 0.000% | 200 | 51854 |
| R = 50, 40 decoys, bundling on | 3.40% [3.30%, 3.49%] | 0.80% | 3.40% | 0.00% [0.00%, 0.00%] | 1.55% [1.50%, 1.61%] | 1.11% | 1.55% | 0.00% [0.00%, 0.00%] | 0.545 [0.537, 0.552] | 5.2% | 4.8% | 0.000% | 200 | 172739 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.29% [5.93%, 6.64%] | 1.76% | 6.30% | -0.01% [-0.08%, 0.06%] | 3.40% [3.29%, 3.51%] | 2.44% | 3.42% | -0.03% [-0.15%, 0.10%] | 0.535 [0.521, 0.549] | 7.9% | 8.1% | 0.000% | 200 | 159768 |
| R = 15, 40 decoys, bundling on | 4.80% [4.59%, 5.01%] | 1.31% | 4.83% | -0.03% [-0.09%, 0.02%] | 2.48% [2.39%, 2.58%] | 1.82% | 2.50% | -0.01% [-0.11%, 0.08%] | 0.544 [0.530, 0.558] | 5.3% | 6.1% | 0.000% | 200 | 207416 |
| R = 50, 40 decoys, bundling on | 3.38% [3.29%, 3.47%] | 0.80% | 3.40% | -0.02% [-0.04%, 0.01%] | 1.57% [1.54%, 1.61%] | 1.11% | 1.55% | 0.02% [-0.03%, 0.06%] | 0.545 [0.539, 0.552] | 5.1% | 4.8% | 0.000% | 200 | 690956 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.29% [5.96%, 6.66%] | 1.76% | 6.30% | -0.01% [-0.08%, 0.06%] | 3.40% [3.28%, 3.51%] | 2.44% | 3.42% | -0.03% [-0.15%, 0.10%] | 0.535 [0.521, 0.549] | 7.9% | 8.1% | 0.000% | 200 | 159768 |
| R = 15, 40 decoys, bundling on | 4.80% [4.60%, 5.01%] | 1.31% | 4.83% | -0.03% [-0.09%, 0.02%] | 2.48% [2.39%, 2.57%] | 1.82% | 2.50% | -0.01% [-0.11%, 0.08%] | 0.544 [0.530, 0.558] | 5.3% | 6.1% | 0.000% | 200 | 207416 |
| R = 50, 40 decoys, bundling on | 3.38% [3.29%, 3.46%] | 0.80% | 3.40% | -0.02% [-0.04%, 0.01%] | 1.57% [1.54%, 1.61%] | 1.11% | 1.55% | 0.02% [-0.02%, 0.06%] | 0.545 [0.539, 0.552] | 5.1% | 4.8% | 0.000% | 200 | 690956 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.29% [5.96%, 6.66%] | 1.76% | 6.30% | -0.01% [-0.05%, 0.04%] | 3.39% [3.24%, 3.54%] | 2.44% | 3.42% | -0.03% [-0.12%, 0.06%] | 0.533 [0.518, 0.547] | 7.7% | 8.1% | 0.000% | 200 | 159768 |
| R = 15, 40 decoys, bundling on | 4.84% [4.62%, 5.06%] | 1.31% | 4.83% | 0.00% [-0.02%, 0.03%] | 2.52% [2.40%, 2.64%] | 1.82% | 2.50% | 0.03% [-0.03%, 0.09%] | 0.543 [0.529, 0.557] | 4.7% | 5.9% | 0.000% | 200 | 207416 |
| R = 50, 40 decoys, bundling on | 3.40% [3.30%, 3.49%] | 0.80% | 3.40% | -0.00% [-0.01%, 0.01%] | 1.55% [1.50%, 1.60%] | 1.11% | 1.55% | -0.01% [-0.03%, 0.02%] | 0.545 [0.538, 0.552] | 5.1% | 4.8% | 0.000% | 200 | 690956 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.51% [6.22%, 6.79%] | 1.90% | 6.30% | 0.21% [-0.03%, 0.44%] | 4.01% [3.88%, 4.15%] | 2.44% | 3.42% | 0.59% [0.36%, 0.83%] | 0.526 [0.517, 0.536] | 4.1% | 5.5% | 0.000% | 200 | 79884 |
| R = 15, 40 decoys, bundling on | 5.18% [4.99%, 5.37%] | 1.42% | 4.83% | 0.34% [0.18%, 0.51%] | 3.01% [2.89%, 3.11%] | 1.82% | 2.50% | 0.51% [0.34%, 0.68%] | 0.522 [0.512, 0.532] | 2.0% | 3.6% | 0.000% | 200 | 103708 |
| R = 50, 40 decoys, bundling on | 3.64% [3.56%, 3.72%] | 0.87% | 3.40% | 0.24% [0.17%, 0.31%] | 1.92% [1.87%, 1.96%] | 1.11% | 1.55% | 0.36% [0.29%, 0.44%] | 0.522 [0.516, 0.527] | 2.1% | 2.6% | 0.000% | 200 | 345478 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.54% [5.19%, 5.90%] | 1.57% | 6.30% | -0.76% [-1.05%, -0.49%] | 2.11% [1.97%, 2.26%] | 2.44% | 3.42% | -1.31% [-1.54%, -1.06%] | 0.560 [0.546, 0.575] | 6.5% | 8.0% | 0.000% | 200 | 39942 |
| R = 15, 40 decoys, bundling on | 4.34% [4.12%, 4.57%] | 1.17% | 4.83% | -0.49% [-0.70%, -0.29%] | 1.64% [1.53%, 1.75%] | 1.82% | 2.50% | -0.86% [-1.03%, -0.69%] | 0.554 [0.539, 0.569] | 6.9% | 6.7% | 0.000% | 200 | 51854 |
| R = 50, 40 decoys, bundling on | 3.05% [2.96%, 3.15%] | 0.72% | 3.40% | -0.35% [-0.43%, -0.26%] | 0.97% [0.93%, 1.02%] | 1.11% | 1.55% | -0.58% [-0.65%, -0.51%] | 0.548 [0.540, 0.556] | 4.1% | 3.8% | 0.000% | 200 | 172739 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.32% [5.99%, 6.69%] | 1.76% | 6.30% | 0.03% [-0.06%, 0.12%] | 3.43% [3.30%, 3.55%] | 2.44% | 3.42% | 0.01% [-0.15%, 0.16%] | 0.532 [0.518, 0.546] | 7.8% | 8.0% | 0.000% | 200 | 119826 |
| R = 15, 40 decoys, bundling on | 4.80% [4.60%, 5.00%] | 1.31% | 4.83% | -0.03% [-0.10%, 0.03%] | 2.50% [2.41%, 2.59%] | 1.82% | 2.50% | 0.01% [-0.11%, 0.12%] | 0.543 [0.529, 0.557] | 5.3% | 6.1% | 0.000% | 200 | 155562 |
| R = 50, 40 decoys, bundling on | 3.40% [3.30%, 3.48%] | 0.80% | 3.40% | -0.00% [-0.03%, 0.03%] | 1.54% [1.51%, 1.58%] | 1.11% | 1.55% | -0.01% [-0.06%, 0.04%] | 0.545 [0.538, 0.552] | 5.0% | 4.8% | 0.000% | 200 | 518217 |

## Outcome-shuffle control (stable cells)

21 stable cells; 1 with a shuffled-outcome AUC interval excluding 0.5: R15_D40_B gatekeeper (0.508).

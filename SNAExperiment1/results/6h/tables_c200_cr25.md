# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the content paths' device and relay-hop holds stretched 2 times and the credential path's shortened to 0.25 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 1 | 40 | 1.97 | 14.0% | 27.5% | 41.5% | 32.0% | 14.0% | 2,501,697 |
| 15 | 40 | 2.65 | 7.0% | 18.6% | 25.7% | 20.1% | 7.0% | 215,400 |
| 50 | 40 | 4.30 | 1.4% | 5.9% | 7.3% | 6.0% | 1.4% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -2.01 [-2.42, -1.57] | -1.60 [-1.89, -1.32] | 39392 |
| Baseline | 15 | 40 | -1.72 [-2.08, -1.38] | -1.09 [-1.34, -0.86] | 46360 |
| Baseline | 50 | 40 | -0.85 [-1.00, -0.70] | -0.68 [-0.78, -0.59] | 153382 |
| First hop, credential | 1 | 40 | -1.97 [-2.36, -1.59] | -1.54 [-1.72, -1.34] | 157568 |
| First hop, credential | 15 | 40 | -1.78 [-2.11, -1.46] | -1.10 [-1.24, -0.97] | 185440 |
| First hop, credential | 50 | 40 | -0.85 [-0.99, -0.71] | -0.69 [-0.74, -0.63] | 613528 |
| First hop, content | 1 | 40 | -1.97 [-2.35, -1.58] | -1.54 [-1.72, -1.35] | 157568 |
| First hop, content | 15 | 40 | -1.78 [-2.10, -1.47] | -1.10 [-1.25, -0.97] | 185440 |
| First hop, content | 50 | 40 | -0.85 [-0.99, -0.71] | -0.69 [-0.74, -0.63] | 613528 |
| Credential processor | 1 | 40 | -2.09 [-2.50, -1.66] | -1.54 [-1.77, -1.31] | 157568 |
| Credential processor | 15 | 40 | -1.72 [-2.06, -1.38] | -1.11 [-1.31, -0.92] | 185440 |
| Credential processor | 50 | 40 | -0.84 [-0.98, -0.68] | -0.69 [-0.77, -0.61] | 613528 |
| Content server | 1 | 40 | -3.14 [-4.00, -2.23] | -2.60 [-3.20, -1.99] | 8187 |
| Content server | 15 | 40 | -3.21 [-3.85, -2.54] | -1.72 [-2.17, -1.25] | 10968 |
| Content server | 50 | 40 | -1.50 [-1.80, -1.17] | -1.09 [-1.30, -0.89] | 36109 |
| Validator | 1 | 40 | -3.43 [-3.89, -2.94] | -2.77 [-3.06, -2.47] | 39392 |
| Validator | 15 | 40 | -2.98 [-3.32, -2.66] | -2.13 [-2.33, -1.93] | 46360 |
| Validator | 50 | 40 | -1.66 [-1.82, -1.51] | -1.28 [-1.36, -1.19] | 153382 |
| Gatekeeper | 1 | 40 | -2.04 [-2.45, -1.62] | -1.46 [-1.66, -1.26] | 118176 |
| Gatekeeper | 15 | 40 | -1.74 [-2.09, -1.39] | -1.02 [-1.19, -0.85] | 139080 |
| Gatekeeper | 50 | 40 | -0.83 [-0.99, -0.68] | -0.70 [-0.76, -0.63] | 460146 |

## Change from the content200 build on the same records

Accuracy in this build minus accuracy in the content200 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -0.39 [-0.60, -0.18] | -0.41 [-0.67, -0.15] | 39799 |
| Baseline | 15 | 40 | -0.17 [-0.33, -0.00] | -0.27 [-0.46, -0.08] | 52017 |
| Baseline | 50 | 40 | -0.21 [-0.29, -0.14] | -0.20 [-0.28, -0.11] | 172224 |
| First hop, credential | 1 | 40 | -0.38 [-0.56, -0.20] | -0.41 [-0.57, -0.26] | 159196 |
| First hop, credential | 15 | 40 | -0.28 [-0.41, -0.14] | -0.25 [-0.37, -0.15] | 208068 |
| First hop, credential | 50 | 40 | -0.22 [-0.28, -0.16] | -0.19 [-0.24, -0.14] | 688896 |
| First hop, content | 1 | 40 | -0.38 [-0.55, -0.21] | -0.41 [-0.57, -0.27] | 159196 |
| First hop, content | 15 | 40 | -0.28 [-0.41, -0.14] | -0.25 [-0.37, -0.15] | 208068 |
| First hop, content | 50 | 40 | -0.22 [-0.28, -0.16] | -0.19 [-0.24, -0.14] | 688896 |
| Credential processor | 1 | 40 | -0.38 [-0.60, -0.20] | -0.38 [-0.61, -0.16] | 159196 |
| Credential processor | 15 | 40 | -0.20 [-0.36, -0.04] | -0.29 [-0.44, -0.14] | 208068 |
| Credential processor | 50 | 40 | -0.21 [-0.28, -0.13] | -0.19 [-0.26, -0.11] | 688896 |
| Content server | 1 | 40 | -0.58 [-0.76, -0.40] | -0.57 [-0.76, -0.38] | 79598 |
| Content server | 15 | 40 | -0.38 [-0.55, -0.22] | -0.41 [-0.55, -0.27] | 104034 |
| Content server | 50 | 40 | -0.23 [-0.31, -0.15] | -0.21 [-0.27, -0.15] | 344448 |
| Validator | 1 | 40 | -0.26 [-0.52, +0.02] | -0.30 [-0.52, -0.09] | 39799 |
| Validator | 15 | 40 | -0.32 [-0.51, -0.12] | -0.19 [-0.34, -0.03] | 52017 |
| Validator | 50 | 40 | -0.12 [-0.21, -0.04] | -0.10 [-0.17, -0.02] | 172224 |
| Gatekeeper | 1 | 40 | -0.46 [-0.65, -0.26] | -0.32 [-0.51, -0.14] | 119397 |
| Gatekeeper | 15 | 40 | -0.20 [-0.35, -0.06] | -0.30 [-0.45, -0.15] | 156051 |
| Gatekeeper | 50 | 40 | -0.21 [-0.27, -0.14] | -0.23 [-0.29, -0.17] | 516672 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.42% [6.07%, 6.78%] | 1.75% | 6.42% | 0.00% [0.00%, 0.00%] | 3.62% [3.45%, 3.79%] | 2.44% | 3.62% | 0.00% [0.00%, 0.00%] | 0.549 [0.532, 0.566] | 9.3% | 9.9% | 0.000% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.08% [4.84%, 5.31%] | 1.30% | 5.08% | 0.00% [0.00%, 0.00%] | 2.68% [2.53%, 2.83%] | 1.82% | 2.68% | 0.00% [0.00%, 0.00%] | 0.546 [0.532, 0.559] | 8.7% | 7.7% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.61% [3.51%, 3.70%] | 0.80% | 3.61% | 0.00% [0.00%, 0.00%] | 1.70% [1.65%, 1.76%] | 1.11% | 1.70% | 0.00% [0.00%, 0.00%] | 0.553 [0.545, 0.561] | 6.6% | 5.6% | 0.000% | 200 | 172224 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.44% [6.09%, 6.77%] | 1.75% | 6.42% | 0.02% [-0.06%, 0.10%] | 3.60% [3.50%, 3.71%] | 2.44% | 3.62% | -0.02% [-0.16%, 0.12%] | 0.551 [0.536, 0.566] | 10.6% | 9.9% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.01% [4.79%, 5.23%] | 1.30% | 5.08% | -0.07% [-0.13%, -0.01%] | 2.72% [2.64%, 2.80%] | 1.82% | 2.68% | 0.04% [-0.07%, 0.15%] | 0.548 [0.536, 0.560] | 8.4% | 7.3% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.59% [3.51%, 3.68%] | 0.80% | 3.61% | -0.01% [-0.05%, 0.02%] | 1.72% [1.69%, 1.76%] | 1.11% | 1.70% | 0.02% [-0.04%, 0.07%] | 0.554 [0.547, 0.561] | 6.5% | 5.5% | 0.000% | 200 | 688896 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.44% [6.11%, 6.79%] | 1.75% | 6.42% | 0.02% [-0.06%, 0.10%] | 3.60% [3.49%, 3.71%] | 2.44% | 3.62% | -0.02% [-0.15%, 0.12%] | 0.551 [0.536, 0.566] | 10.6% | 9.9% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.01% [4.78%, 5.22%] | 1.30% | 5.08% | -0.07% [-0.13%, -0.01%] | 2.72% [2.64%, 2.80%] | 1.82% | 2.68% | 0.04% [-0.07%, 0.15%] | 0.548 [0.536, 0.560] | 8.4% | 7.3% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.59% [3.50%, 3.68%] | 0.80% | 3.61% | -0.01% [-0.05%, 0.02%] | 1.72% [1.68%, 1.75%] | 1.11% | 1.70% | 0.02% [-0.04%, 0.07%] | 0.554 [0.547, 0.561] | 6.5% | 5.5% | 0.000% | 200 | 688896 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.39% [6.03%, 6.74%] | 1.75% | 6.42% | -0.03% [-0.08%, 0.02%] | 3.62% [3.47%, 3.76%] | 2.44% | 3.62% | -0.00% [-0.11%, 0.10%] | 0.552 [0.535, 0.568] | 10.1% | 9.9% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.07% [4.83%, 5.31%] | 1.30% | 5.08% | -0.01% [-0.05%, 0.02%] | 2.71% [2.60%, 2.83%] | 1.82% | 2.68% | 0.03% [-0.04%, 0.10%] | 0.547 [0.533, 0.560] | 8.9% | 7.5% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.61% [3.51%, 3.70%] | 0.80% | 3.61% | 0.00% [-0.01%, 0.01%] | 1.70% [1.65%, 1.76%] | 1.11% | 1.70% | -0.00% [-0.03%, 0.02%] | 0.554 [0.546, 0.562] | 6.6% | 5.5% | 0.000% | 200 | 688896 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.06% [5.77%, 6.37%] | 1.80% | 6.42% | -0.36% [-0.56%, -0.16%] | 3.73% [3.59%, 3.86%] | 2.44% | 3.62% | 0.11% [-0.10%, 0.31%] | 0.540 [0.528, 0.552] | 5.9% | 6.9% | 0.000% | 200 | 79598 |
| R = 15, 40 decoys, bundling on | 4.88% [4.68%, 5.09%] | 1.34% | 5.08% | -0.19% [-0.35%, -0.04%] | 2.79% [2.70%, 2.88%] | 1.82% | 2.68% | 0.11% [-0.05%, 0.27%] | 0.540 [0.530, 0.549] | 4.1% | 5.2% | 0.000% | 200 | 104034 |
| R = 50, 40 decoys, bundling on | 3.48% [3.40%, 3.56%] | 0.83% | 3.61% | -0.13% [-0.20%, -0.06%] | 1.73% [1.68%, 1.77%] | 1.11% | 1.70% | 0.02% [-0.05%, 0.09%] | 0.531 [0.524, 0.538] | 2.4% | 3.2% | 0.000% | 200 | 344448 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.11% [5.71%, 6.49%] | 1.61% | 6.42% | -0.31% [-0.56%, -0.09%] | 2.65% [2.49%, 2.81%] | 2.44% | 3.62% | -0.97% [-1.19%, -0.76%] | 0.561 [0.545, 0.578] | 12.3% | 10.2% | 0.000% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 4.80% [4.59%, 5.03%] | 1.20% | 5.08% | -0.27% [-0.45%, -0.10%] | 1.89% [1.77%, 2.02%] | 1.82% | 2.68% | -0.79% [-0.98%, -0.60%] | 0.536 [0.522, 0.551] | 7.1% | 6.1% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.38% [3.29%, 3.48%] | 0.74% | 3.61% | -0.22% [-0.29%, -0.15%] | 1.20% [1.15%, 1.24%] | 1.11% | 1.70% | -0.51% [-0.59%, -0.43%] | 0.551 [0.543, 0.559] | 6.7% | 5.3% | 0.000% | 200 | 172224 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.35% [6.01%, 6.71%] | 1.75% | 6.42% | -0.07% [-0.16%, 0.02%] | 3.68% [3.56%, 3.81%] | 2.44% | 3.62% | 0.07% [-0.09%, 0.23%] | 0.551 [0.535, 0.567] | 9.6% | 9.7% | 0.000% | 200 | 119397 |
| R = 15, 40 decoys, bundling on | 5.07% [4.83%, 5.29%] | 1.30% | 5.08% | -0.01% [-0.07%, 0.05%] | 2.74% [2.63%, 2.84%] | 1.82% | 2.68% | 0.06% [-0.07%, 0.19%] | 0.546 [0.533, 0.559] | 8.3% | 7.3% | 0.000% | 200 | 156051 |
| R = 50, 40 decoys, bundling on | 3.60% [3.51%, 3.69%] | 0.80% | 3.61% | -0.00% [-0.04%, 0.03%] | 1.68% [1.64%, 1.72%] | 1.11% | 1.70% | -0.02% [-0.08%, 0.03%] | 0.554 [0.547, 0.561] | 6.5% | 5.5% | 0.000% | 200 | 516672 |

## Outcome-shuffle control (stable cells)

21 stable cells; 0 with a shuffled-outcome AUC interval excluding 0.5.

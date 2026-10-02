# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the device and relay-hop holds on both content paths stretched 3 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 40 | -2.91 [-3.33, -2.48] | -2.47 [-2.76, -2.21] | 39173 |
| Baseline | 15 | 40 | -2.57 [-2.96, -2.17] | -1.57 [-1.79, -1.36] | 40564 |
| Baseline | 50 | 40 | -1.45 [-1.61, -1.28] | -1.10 [-1.20, -1.01] | 134314 |
| First hop, credential | 1 | 40 | -3.07 [-3.48, -2.68] | -2.43 [-2.63, -2.24] | 156692 |
| First hop, credential | 15 | 40 | -2.67 [-2.99, -2.31] | -1.80 [-1.94, -1.65] | 162256 |
| First hop, credential | 50 | 40 | -1.50 [-1.65, -1.35] | -1.13 [-1.18, -1.08] | 537256 |
| First hop, content | 1 | 40 | -3.07 [-3.45, -2.65] | -2.43 [-2.63, -2.23] | 156692 |
| First hop, content | 15 | 40 | -2.67 [-3.01, -2.31] | -1.80 [-1.94, -1.66] | 162256 |
| First hop, content | 50 | 40 | -1.50 [-1.65, -1.34] | -1.13 [-1.19, -1.08] | 537256 |
| Credential processor | 1 | 40 | -2.97 [-3.39, -2.52] | -2.39 [-2.62, -2.16] | 156692 |
| Credential processor | 15 | 40 | -2.58 [-2.95, -2.20] | -1.60 [-1.79, -1.40] | 162256 |
| Credential processor | 50 | 40 | -1.45 [-1.61, -1.28] | -1.09 [-1.18, -1.01] | 537256 |
| Content server | 1 | 40 | -4.44 [-5.22, -3.61] | -3.32 [-3.89, -2.75] | 9195 |
| Content server | 15 | 40 | -3.96 [-4.67, -3.24] | -2.72 [-3.25, -2.15] | 9452 |
| Content server | 50 | 40 | -2.23 [-2.55, -1.92] | -1.52 [-1.74, -1.30] | 31537 |
| Validator | 1 | 40 | -4.64 [-5.08, -4.19] | -3.69 [-3.99, -3.41] | 39173 |
| Validator | 15 | 40 | -4.19 [-4.56, -3.80] | -2.83 [-3.04, -2.62] | 40564 |
| Validator | 50 | 40 | -2.27 [-2.45, -2.11] | -1.70 [-1.79, -1.60] | 134314 |
| Gatekeeper | 1 | 40 | -2.95 [-3.39, -2.51] | -2.45 [-2.64, -2.27] | 117519 |
| Gatekeeper | 15 | 40 | -2.63 [-3.00, -2.29] | -1.59 [-1.75, -1.42] | 121692 |
| Gatekeeper | 50 | 40 | -1.43 [-1.60, -1.28] | -1.08 [-1.14, -1.01] | 402942 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.56% [5.20%, 5.94%] | 1.53% | 5.56% | 0.00% [0.00%, 0.00%] | 2.74% [2.58%, 2.89%] | 2.44% | 2.74% | 0.00% [0.00%, 0.00%] | 0.540 [0.524, 0.556] | 7.3% | 6.4% | 0.000% | 200 | 39942 |
| R = 15, 40 decoys, bundling on | 4.41% [4.19%, 4.65%] | 1.14% | 4.41% | 0.00% [0.00%, 0.00%] | 2.13% [2.01%, 2.25%] | 1.82% | 2.13% | 0.00% [0.00%, 0.00%] | 0.543 [0.528, 0.558] | 6.6% | 5.8% | 0.002% | 200 | 51854 |
| R = 50, 40 decoys, bundling on | 3.04% [2.94%, 3.13%] | 0.70% | 3.04% | 0.00% [0.00%, 0.00%] | 1.28% [1.23%, 1.34%] | 1.11% | 1.28% | 0.00% [0.00%, 0.00%] | 0.544 [0.535, 0.552] | 4.0% | 4.1% | 0.000% | 200 | 172739 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.39% [5.06%, 5.72%] | 1.53% | 5.56% | -0.17% [-0.26%, -0.07%] | 2.71% [2.61%, 2.80%] | 2.44% | 2.74% | -0.03% [-0.19%, 0.12%] | 0.538 [0.524, 0.553] | 7.2% | 6.8% | 0.000% | 200 | 159768 |
| R = 15, 40 decoys, bundling on | 4.34% [4.14%, 4.55%] | 1.14% | 4.41% | -0.07% [-0.15%, 0.00%] | 2.03% [1.97%, 2.10%] | 1.82% | 2.13% | -0.09% [-0.21%, 0.02%] | 0.544 [0.531, 0.557] | 6.0% | 5.6% | 0.000% | 200 | 207416 |
| R = 50, 40 decoys, bundling on | 2.96% [2.87%, 3.06%] | 0.70% | 3.04% | -0.07% [-0.11%, -0.04%] | 1.27% [1.25%, 1.30%] | 1.11% | 1.28% | -0.01% [-0.07%, 0.04%] | 0.540 [0.533, 0.547] | 4.2% | 3.7% | 0.000% | 200 | 690956 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.39% [5.08%, 5.72%] | 1.53% | 5.56% | -0.17% [-0.26%, -0.08%] | 2.71% [2.61%, 2.80%] | 2.44% | 2.74% | -0.03% [-0.19%, 0.13%] | 0.538 [0.524, 0.553] | 7.2% | 6.8% | 0.000% | 200 | 159768 |
| R = 15, 40 decoys, bundling on | 4.34% [4.14%, 4.55%] | 1.14% | 4.41% | -0.07% [-0.15%, -0.00%] | 2.03% [1.97%, 2.10%] | 1.82% | 2.13% | -0.09% [-0.20%, 0.02%] | 0.544 [0.531, 0.557] | 6.0% | 5.6% | 0.000% | 200 | 207416 |
| R = 50, 40 decoys, bundling on | 2.96% [2.87%, 3.06%] | 0.70% | 3.04% | -0.07% [-0.11%, -0.04%] | 1.27% [1.25%, 1.30%] | 1.11% | 1.28% | -0.01% [-0.06%, 0.04%] | 0.540 [0.533, 0.547] | 4.2% | 3.7% | 0.000% | 200 | 690956 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.56% [5.21%, 5.91%] | 1.53% | 5.56% | -0.00% [-0.05%, 0.04%] | 2.76% [2.63%, 2.88%] | 2.44% | 2.74% | 0.02% [-0.07%, 0.11%] | 0.540 [0.524, 0.556] | 7.1% | 6.4% | 0.000% | 200 | 159768 |
| R = 15, 40 decoys, bundling on | 4.40% [4.18%, 4.63%] | 1.14% | 4.41% | -0.01% [-0.04%, 0.02%] | 2.13% [2.02%, 2.24%] | 1.82% | 2.13% | 0.00% [-0.05%, 0.06%] | 0.544 [0.529, 0.558] | 6.6% | 5.7% | 0.002% | 200 | 207416 |
| R = 50, 40 decoys, bundling on | 3.03% [2.93%, 3.13%] | 0.70% | 3.04% | -0.00% [-0.02%, 0.01%] | 1.30% [1.25%, 1.34%] | 1.11% | 1.28% | 0.01% [-0.01%, 0.04%] | 0.544 [0.536, 0.553] | 3.9% | 4.1% | 0.000% | 200 | 690956 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.12% [4.88%, 5.37%] | 1.55% | 5.56% | -0.44% [-0.66%, -0.23%] | 2.89% [2.77%, 3.00%] | 2.44% | 2.74% | 0.15% [-0.04%, 0.35%] | 0.526 [0.515, 0.536] | 5.3% | 5.1% | 0.000% | 200 | 79884 |
| R = 15, 40 decoys, bundling on | 4.03% [3.85%, 4.20%] | 1.16% | 4.41% | -0.39% [-0.55%, -0.23%] | 2.06% [1.96%, 2.16%] | 1.82% | 2.13% | -0.07% [-0.21%, 0.08%] | 0.524 [0.513, 0.534] | 2.4% | 3.8% | 0.000% | 200 | 103708 |
| R = 50, 40 decoys, bundling on | 2.75% [2.68%, 2.82%] | 0.71% | 3.04% | -0.29% [-0.37%, -0.22%] | 1.32% [1.28%, 1.36%] | 1.11% | 1.28% | 0.04% [-0.02%, 0.10%] | 0.517 [0.511, 0.524] | 2.1% | 2.4% | 0.000% | 200 | 345478 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 4.92% [4.58%, 5.30%] | 1.45% | 5.56% | -0.64% [-0.88%, -0.40%] | 1.71% [1.58%, 1.85%] | 2.44% | 2.74% | -1.02% [-1.22%, -0.83%] | 0.545 [0.527, 0.563] | 6.0% | 6.1% | 0.000% | 200 | 39942 |
| R = 15, 40 decoys, bundling on | 3.86% [3.65%, 4.10%] | 1.08% | 4.41% | -0.55% [-0.73%, -0.36%] | 1.18% [1.09%, 1.27%] | 1.82% | 2.13% | -0.95% [-1.09%, -0.80%] | 0.547 [0.530, 0.564] | 5.4% | 5.9% | 0.000% | 200 | 51854 |
| R = 50, 40 decoys, bundling on | 2.76% [2.67%, 2.85%] | 0.66% | 3.04% | -0.28% [-0.35%, -0.21%] | 0.79% [0.75%, 0.83%] | 1.11% | 1.28% | -0.49% [-0.56%, -0.43%] | 0.537 [0.528, 0.546] | 3.7% | 3.4% | 0.000% | 200 | 172739 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.48% [5.13%, 5.84%] | 1.53% | 5.56% | -0.08% [-0.16%, 0.00%] | 2.69% [2.57%, 2.80%] | 2.44% | 2.74% | -0.05% [-0.20%, 0.11%] | 0.539 [0.524, 0.555] | 7.8% | 6.4% | 0.000% | 200 | 119826 |
| R = 15, 40 decoys, bundling on | 4.36% [4.15%, 4.56%] | 1.14% | 4.41% | -0.05% [-0.12%, 0.01%] | 2.05% [1.97%, 2.14%] | 1.82% | 2.13% | -0.08% [-0.18%, 0.03%] | 0.543 [0.528, 0.557] | 7.1% | 5.4% | 0.001% | 200 | 155562 |
| R = 50, 40 decoys, bundling on | 3.04% [2.93%, 3.14%] | 0.70% | 3.04% | 0.00% [-0.02%, 0.03%] | 1.29% [1.26%, 1.32%] | 1.11% | 1.28% | 0.01% [-0.04%, 0.06%] | 0.544 [0.536, 0.552] | 3.6% | 4.0% | 0.000% | 200 | 518217 |

## Outcome-shuffle control (stable cells)

21 stable cells; 4 with a shuffled-outcome AUC interval excluding 0.5: R1_D40_B cred_processor (0.507), R1_D40_B gatekeeper (0.509), R15_D40_B validator (0.518), R15_D40_B gatekeeper (0.508).

# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with every device and relay-hop hold stretched 3 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 1 | 40 | 1.97 | 14.0% | 27.5% | 41.5% | 31.9% | 14.0% | 2,501,697 |
| 15 | 40 | 2.65 | 7.1% | 18.7% | 25.7% | 20.1% | 7.0% | 215,400 |
| 50 | 40 | 4.31 | 1.3% | 5.8% | 7.1% | 5.8% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -3.30 [-3.73, -2.85] | -2.74 [-2.99, -2.50] | 38580 |
| Baseline | 15 | 40 | -2.90 [-3.23, -2.54] | -1.78 [-2.01, -1.56] | 39859 |
| Baseline | 50 | 40 | -1.69 [-1.86, -1.53] | -1.28 [-1.38, -1.19] | 132224 |
| First hop, credential | 1 | 40 | -3.41 [-3.79, -3.02] | -2.67 [-2.84, -2.49] | 154320 |
| First hop, credential | 15 | 40 | -3.02 [-3.34, -2.70] | -2.02 [-2.16, -1.87] | 159436 |
| First hop, credential | 50 | 40 | -1.73 [-1.88, -1.58] | -1.27 [-1.32, -1.21] | 528896 |
| First hop, content | 1 | 40 | -3.41 [-3.80, -3.03] | -2.67 [-2.85, -2.48] | 154320 |
| First hop, content | 15 | 40 | -3.02 [-3.34, -2.70] | -2.02 [-2.16, -1.87] | 159436 |
| First hop, content | 50 | 40 | -1.73 [-1.88, -1.58] | -1.27 [-1.32, -1.21] | 528896 |
| Credential processor | 1 | 40 | -3.35 [-3.75, -2.92] | -2.63 [-2.85, -2.41] | 154320 |
| Credential processor | 15 | 40 | -2.87 [-3.20, -2.53] | -1.80 [-2.01, -1.59] | 159436 |
| Credential processor | 50 | 40 | -1.69 [-1.84, -1.52] | -1.27 [-1.35, -1.19] | 528896 |
| Content server | 1 | 40 | -4.94 [-5.68, -4.13] | -3.55 [-4.17, -2.90] | 9055 |
| Content server | 15 | 40 | -4.39 [-5.11, -3.67] | -2.81 [-3.30, -2.30] | 9299 |
| Content server | 50 | 40 | -2.26 [-2.61, -1.91] | -1.69 [-1.90, -1.47] | 31023 |
| Validator | 1 | 40 | -3.20 [-3.67, -2.70] | -2.38 [-2.69, -2.08] | 38580 |
| Validator | 15 | 40 | -2.58 [-2.95, -2.20] | -1.56 [-1.81, -1.29] | 39859 |
| Validator | 50 | 40 | -1.50 [-1.67, -1.33] | -1.06 [-1.17, -0.96] | 132224 |
| Gatekeeper | 1 | 40 | -3.27 [-3.68, -2.86] | -2.67 [-2.87, -2.48] | 115740 |
| Gatekeeper | 15 | 40 | -2.89 [-3.25, -2.56] | -1.75 [-1.91, -1.58] | 119577 |
| Gatekeeper | 50 | 40 | -1.68 [-1.85, -1.52] | -1.26 [-1.33, -1.20] | 396672 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.15% [4.79%, 5.52%] | 1.45% | 5.15% | 0.00% [0.00%, 0.00%] | 2.48% [2.33%, 2.62%] | 2.44% | 2.48% | 0.00% [0.00%, 0.00%] | 0.548 [0.530, 0.566] | 5.6% | 6.9% | 0.000% | 200 | 39336 |
| R = 15, 40 decoys, bundling on | 4.08% [3.85%, 4.32%] | 1.08% | 4.08% | 0.00% [0.00%, 0.00%] | 1.88% [1.76%, 2.00%] | 1.82% | 1.88% | 0.00% [0.00%, 0.00%] | 0.539 [0.523, 0.556] | 5.1% | 5.4% | 0.010% | 200 | 50970 |
| R = 50, 40 decoys, bundling on | 2.82% [2.73%, 2.92%] | 0.66% | 2.82% | 0.00% [0.00%, 0.00%] | 1.09% [1.05%, 1.14%] | 1.11% | 1.09% | 0.00% [0.00%, 0.00%] | 0.540 [0.530, 0.549] | 4.1% | 3.6% | 0.000% | 200 | 170047 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.02% [4.70%, 5.35%] | 1.45% | 5.15% | -0.13% [-0.23%, -0.04%] | 2.47% [2.38%, 2.55%] | 2.44% | 2.48% | -0.01% [-0.15%, 0.12%] | 0.549 [0.533, 0.566] | 5.8% | 6.5% | 0.000% | 200 | 157344 |
| R = 15, 40 decoys, bundling on | 3.98% [3.77%, 4.18%] | 1.08% | 4.08% | -0.10% [-0.18%, -0.03%] | 1.82% [1.75%, 1.88%] | 1.82% | 1.88% | -0.06% [-0.17%, 0.06%] | 0.543 [0.529, 0.557] | 4.8% | 5.7% | 0.000% | 200 | 203880 |
| R = 50, 40 decoys, bundling on | 2.75% [2.66%, 2.84%] | 0.66% | 2.82% | -0.07% [-0.11%, -0.04%] | 1.13% [1.10%, 1.15%] | 1.11% | 1.09% | 0.03% [-0.02%, 0.09%] | 0.540 [0.531, 0.548] | 4.1% | 3.6% | 0.000% | 200 | 680188 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.02% [4.71%, 5.36%] | 1.45% | 5.15% | -0.13% [-0.22%, -0.04%] | 2.47% [2.38%, 2.55%] | 2.44% | 2.48% | -0.01% [-0.15%, 0.13%] | 0.549 [0.533, 0.566] | 5.8% | 6.5% | 0.000% | 200 | 157344 |
| R = 15, 40 decoys, bundling on | 3.98% [3.76%, 4.18%] | 1.08% | 4.08% | -0.10% [-0.18%, -0.03%] | 1.82% [1.75%, 1.88%] | 1.82% | 1.88% | -0.06% [-0.17%, 0.05%] | 0.543 [0.529, 0.557] | 4.8% | 5.7% | 0.000% | 200 | 203880 |
| R = 50, 40 decoys, bundling on | 2.75% [2.66%, 2.84%] | 0.66% | 2.82% | -0.07% [-0.11%, -0.04%] | 1.13% [1.10%, 1.15%] | 1.11% | 1.09% | 0.03% [-0.02%, 0.08%] | 0.540 [0.531, 0.548] | 4.1% | 3.6% | 0.000% | 200 | 680188 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.16% [4.80%, 5.51%] | 1.45% | 5.15% | 0.00% [-0.04%, 0.05%] | 2.52% [2.38%, 2.66%] | 2.44% | 2.48% | 0.05% [-0.04%, 0.12%] | 0.547 [0.529, 0.566] | 5.7% | 6.6% | 0.000% | 200 | 157344 |
| R = 15, 40 decoys, bundling on | 4.10% [3.87%, 4.33%] | 1.08% | 4.08% | 0.02% [-0.01%, 0.06%] | 1.88% [1.78%, 1.98%] | 1.82% | 1.88% | 0.00% [-0.06%, 0.06%] | 0.537 [0.521, 0.554] | 5.0% | 5.7% | 0.007% | 200 | 203880 |
| R = 50, 40 decoys, bundling on | 2.82% [2.73%, 2.92%] | 0.66% | 2.82% | -0.00% [-0.01%, 0.01%] | 1.11% [1.07%, 1.15%] | 1.11% | 1.09% | 0.02% [-0.00%, 0.04%] | 0.540 [0.530, 0.549] | 4.3% | 3.6% | 0.000% | 200 | 680188 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 4.75% [4.50%, 5.00%] | 1.49% | 5.15% | -0.40% [-0.61%, -0.17%] | 2.66% [2.54%, 2.77%] | 2.44% | 2.48% | 0.18% [-0.01%, 0.36%] | 0.523 [0.512, 0.535] | 3.0% | 3.9% | 0.000% | 200 | 78672 |
| R = 15, 40 decoys, bundling on | 3.83% [3.67%, 4.00%] | 1.11% | 4.08% | -0.24% [-0.42%, -0.06%] | 1.93% [1.84%, 2.01%] | 1.82% | 1.88% | 0.05% [-0.09%, 0.18%] | 0.526 [0.517, 0.536] | 2.9% | 3.3% | 0.005% | 200 | 101940 |
| R = 50, 40 decoys, bundling on | 2.56% [2.49%, 2.63%] | 0.68% | 2.82% | -0.26% [-0.33%, -0.19%] | 1.22% [1.19%, 1.26%] | 1.11% | 1.09% | 0.13% [0.07%, 0.19%] | 0.511 [0.505, 0.518] | 1.9% | 2.3% | 0.000% | 200 | 340094 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.32% [5.98%, 6.65%] | 1.47% | 5.15% | 1.16% [0.79%, 1.53%] | 3.03% [2.84%, 3.23%] | 2.44% | 2.48% | 0.55% [0.30%, 0.81%] | 0.552 [0.541, 0.564] | 10.2% | 8.8% | 0.000% | 200 | 39336 |
| R = 15, 40 decoys, bundling on | 5.31% [5.08%, 5.55%] | 1.09% | 4.08% | 1.23% [0.97%, 1.47%] | 2.46% [2.32%, 2.60%] | 1.82% | 1.88% | 0.58% [0.40%, 0.77%] | 0.559 [0.546, 0.572] | 7.8% | 8.3% | 0.000% | 200 | 50970 |
| R = 50, 40 decoys, bundling on | 3.54% [3.44%, 3.65%] | 0.67% | 2.82% | 0.72% [0.60%, 0.82%] | 1.44% [1.38%, 1.49%] | 1.11% | 1.09% | 0.34% [0.27%, 0.41%] | 0.556 [0.548, 0.564] | 6.4% | 5.3% | 0.000% | 200 | 170047 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.14% [4.80%, 5.52%] | 1.45% | 5.15% | -0.02% [-0.10%, 0.07%] | 2.46% [2.35%, 2.57%] | 2.44% | 2.48% | -0.02% [-0.17%, 0.12%] | 0.545 [0.528, 0.562] | 6.7% | 6.5% | 0.000% | 200 | 118008 |
| R = 15, 40 decoys, bundling on | 4.06% [3.85%, 4.27%] | 1.08% | 4.08% | -0.02% [-0.09%, 0.04%] | 1.92% [1.84%, 2.00%] | 1.82% | 1.88% | 0.04% [-0.07%, 0.15%] | 0.539 [0.523, 0.555] | 4.7% | 5.5% | 0.000% | 200 | 152910 |
| R = 50, 40 decoys, bundling on | 2.81% [2.71%, 2.90%] | 0.66% | 2.82% | -0.02% [-0.05%, 0.01%] | 1.10% [1.07%, 1.14%] | 1.11% | 1.09% | 0.01% [-0.04%, 0.05%] | 0.541 [0.532, 0.550] | 4.2% | 3.7% | 0.000% | 200 | 510141 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R50_D40_B first_hop_cred (0.505), R50_D40_B first_hop_content (0.506).

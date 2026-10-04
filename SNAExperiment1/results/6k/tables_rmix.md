# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with every relay hop's hold drawn from a fixed-mean short/long mixture. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 15 | 40 | 2.65 | 7.1% | 18.7% | 25.7% | 20.1% | 7.0% | 215,400 |
| 50 | 40 | 4.31 | 1.3% | 5.8% | 7.1% | 5.9% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -1.75 [-2.15, -1.34] | -1.05 [-1.36, -0.76] | 38720 |
| Baseline | 15 | 40 | -1.21 [-1.65, -0.78] | -0.58 [-0.84, -0.31] | 34668 |
| Baseline | 50 | 40 | -0.82 [-0.99, -0.63] | -0.44 [-0.55, -0.34] | 114977 |
| First hop, credential | 1 | 40 | -1.75 [-2.15, -1.36] | -0.97 [-1.17, -0.77] | 154880 |
| First hop, credential | 15 | 40 | -1.29 [-1.70, -0.87] | -0.80 [-0.97, -0.63] | 138672 |
| First hop, credential | 50 | 40 | -0.86 [-1.03, -0.69] | -0.58 [-0.65, -0.52] | 459908 |
| First hop, content | 1 | 40 | -1.75 [-2.15, -1.37] | -0.97 [-1.17, -0.77] | 154880 |
| First hop, content | 15 | 40 | -1.29 [-1.70, -0.88] | -0.80 [-0.98, -0.63] | 138672 |
| First hop, content | 50 | 40 | -0.86 [-1.03, -0.69] | -0.58 [-0.65, -0.51] | 459908 |
| Credential processor | 1 | 40 | -1.83 [-2.25, -1.41] | -1.04 [-1.29, -0.78] | 154880 |
| Credential processor | 15 | 40 | -1.18 [-1.59, -0.77] | -0.73 [-0.95, -0.50] | 138672 |
| Credential processor | 50 | 40 | -0.81 [-0.99, -0.62] | -0.47 [-0.57, -0.37] | 459908 |
| Content server | 1 | 40 | -0.01 [-0.88, +0.83] | +0.83 [+0.01, +1.63] | 9465 |
| Content server | 15 | 40 | -0.60 [-1.39, +0.20] | -0.30 [-0.93, +0.31] | 8133 |
| Content server | 50 | 40 | +0.21 [-0.15, +0.57] | +0.41 [+0.13, +0.68] | 27334 |
| Validator | 1 | 40 | -1.08 [-1.60, -0.60] | -0.85 [-1.17, -0.51] | 38720 |
| Validator | 15 | 40 | -0.93 [-1.38, -0.45] | -0.45 [-0.74, -0.15] | 34668 |
| Validator | 50 | 40 | -0.64 [-0.82, -0.46] | -0.44 [-0.55, -0.33] | 114977 |
| Gatekeeper | 1 | 40 | -1.73 [-2.15, -1.34] | -0.92 [-1.14, -0.71] | 116160 |
| Gatekeeper | 15 | 40 | -1.26 [-1.69, -0.83] | -0.55 [-0.74, -0.36] | 104004 |
| Gatekeeper | 50 | 40 | -0.82 [-1.00, -0.64] | -0.48 [-0.55, -0.41] | 344931 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.69% [6.37%, 7.02%] | 1.46% | 6.69% | 0.00% [0.00%, 0.00%] | 4.18% [3.99%, 4.38%] | 2.44% | 4.18% | 0.00% [0.00%, 0.00%] | 0.564 [0.551, 0.578] | 12.3% | 10.4% | 0.000% | 200 | 39883 |
| R = 15, 40 decoys, bundling on | 5.54% [5.30%, 5.79%] | 1.09% | 5.54% | 0.00% [0.00%, 0.00%] | 3.13% [2.98%, 3.31%] | 1.82% | 3.13% | 0.00% [0.00%, 0.00%] | 0.554 [0.541, 0.568] | 11.8% | 9.2% | 0.000% | 200 | 51761 |
| R = 50, 40 decoys, bundling on | 3.71% [3.61%, 3.81%] | 0.67% | 3.71% | 0.00% [0.00%, 0.00%] | 1.91% [1.85%, 1.97%] | 1.11% | 1.91% | 0.00% [0.00%, 0.00%] | 0.555 [0.548, 0.563] | 6.2% | 5.4% | 0.000% | 200 | 172368 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.66% [6.35%, 6.95%] | 1.46% | 6.69% | -0.03% [-0.11%, 0.07%] | 4.16% [4.03%, 4.30%] | 2.44% | 4.18% | -0.01% [-0.14%, 0.12%] | 0.565 [0.553, 0.577] | 11.1% | 9.9% | 0.000% | 200 | 159532 |
| R = 15, 40 decoys, bundling on | 5.47% [5.26%, 5.68%] | 1.09% | 5.54% | -0.07% [-0.14%, -0.01%] | 3.08% [2.97%, 3.17%] | 1.82% | 3.13% | -0.06% [-0.16%, 0.06%] | 0.551 [0.539, 0.563] | 9.9% | 8.3% | 0.000% | 200 | 207044 |
| R = 50, 40 decoys, bundling on | 3.64% [3.56%, 3.73%] | 0.67% | 3.71% | -0.07% [-0.10%, -0.04%] | 1.81% [1.78%, 1.85%] | 1.11% | 1.91% | -0.10% [-0.15%, -0.04%] | 0.550 [0.544, 0.557] | 5.5% | 4.9% | 0.000% | 200 | 689472 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.66% [6.38%, 6.95%] | 1.46% | 6.69% | -0.03% [-0.12%, 0.07%] | 4.16% [4.03%, 4.29%] | 2.44% | 4.18% | -0.01% [-0.15%, 0.11%] | 0.565 [0.553, 0.577] | 11.1% | 9.9% | 0.000% | 200 | 159532 |
| R = 15, 40 decoys, bundling on | 5.47% [5.24%, 5.70%] | 1.09% | 5.54% | -0.07% [-0.14%, -0.00%] | 3.08% [2.98%, 3.18%] | 1.82% | 3.13% | -0.06% [-0.16%, 0.05%] | 0.551 [0.539, 0.563] | 9.9% | 8.3% | 0.000% | 200 | 207044 |
| R = 50, 40 decoys, bundling on | 3.64% [3.56%, 3.73%] | 0.67% | 3.71% | -0.07% [-0.10%, -0.04%] | 1.81% [1.78%, 1.85%] | 1.11% | 1.91% | -0.10% [-0.15%, -0.04%] | 0.550 [0.544, 0.557] | 5.5% | 4.9% | 0.000% | 200 | 689472 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.66% [6.34%, 7.00%] | 1.46% | 6.69% | -0.03% [-0.06%, 0.01%] | 4.13% [3.96%, 4.30%] | 2.44% | 4.18% | -0.05% [-0.12%, 0.03%] | 0.566 [0.553, 0.579] | 12.4% | 10.4% | 0.000% | 200 | 159532 |
| R = 15, 40 decoys, bundling on | 5.56% [5.32%, 5.79%] | 1.09% | 5.54% | 0.02% [-0.01%, 0.06%] | 3.07% [2.93%, 3.21%] | 1.82% | 3.13% | -0.06% [-0.13%, -0.00%] | 0.555 [0.543, 0.568] | 11.8% | 9.4% | 0.000% | 200 | 207044 |
| R = 50, 40 decoys, bundling on | 3.70% [3.60%, 3.79%] | 0.67% | 3.71% | -0.01% [-0.02%, 0.00%] | 1.90% [1.84%, 1.95%] | 1.11% | 1.91% | -0.01% [-0.04%, 0.01%] | 0.556 [0.548, 0.564] | 6.2% | 5.4% | 0.000% | 200 | 689472 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 9.59% [9.29%, 9.91%] | 1.51% | 6.69% | 2.90% [2.61%, 3.17%] | 7.21% [7.02%, 7.40%] | 2.44% | 4.18% | 3.04% [2.80%, 3.29%] | 0.574 [0.566, 0.582] | 10.2% | 12.8% | 0.000% | 200 | 79766 |
| R = 15, 40 decoys, bundling on | 7.54% [7.32%, 7.75%] | 1.12% | 5.54% | 1.99% [1.78%, 2.20%] | 5.35% [5.20%, 5.51%] | 1.82% | 3.13% | 2.22% [2.02%, 2.42%] | 0.572 [0.563, 0.580] | 7.6% | 9.3% | 0.000% | 200 | 103522 |
| R = 50, 40 decoys, bundling on | 5.16% [5.07%, 5.25%] | 0.69% | 3.71% | 1.46% [1.38%, 1.54%] | 3.30% [3.24%, 3.36%] | 1.11% | 1.91% | 1.39% [1.31%, 1.47%] | 0.562 [0.558, 0.566] | 4.4% | 5.7% | 0.000% | 200 | 344736 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.46% [8.08%, 8.87%] | 1.50% | 6.69% | 1.77% [1.37%, 2.15%] | 4.56% [4.36%, 4.76%] | 2.44% | 4.18% | 0.38% [0.09%, 0.67%] | 0.565 [0.552, 0.577] | 13.5% | 12.4% | 0.008% | 200 | 39883 |
| R = 15, 40 decoys, bundling on | 6.80% [6.53%, 7.06%] | 1.12% | 5.54% | 1.26% [0.99%, 1.52%] | 3.50% [3.35%, 3.66%] | 1.82% | 3.13% | 0.37% [0.15%, 0.59%] | 0.561 [0.549, 0.572] | 14.1% | 10.9% | 0.025% | 200 | 51761 |
| R = 50, 40 decoys, bundling on | 4.53% [4.43%, 4.64%] | 0.69% | 3.71% | 0.82% [0.72%, 0.92%] | 2.10% [2.03%, 2.17%] | 1.11% | 1.91% | 0.19% [0.10%, 0.28%] | 0.552 [0.546, 0.558] | 8.4% | 6.8% | 0.000% | 200 | 172368 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.67% [6.37%, 7.00%] | 1.46% | 6.69% | -0.02% [-0.11%, 0.08%] | 4.21% [4.07%, 4.36%] | 2.44% | 4.18% | 0.03% [-0.14%, 0.20%] | 0.567 [0.554, 0.579] | 13.2% | 10.5% | 0.000% | 200 | 119649 |
| R = 15, 40 decoys, bundling on | 5.52% [5.29%, 5.73%] | 1.09% | 5.54% | -0.02% [-0.10%, 0.05%] | 3.13% [3.02%, 3.24%] | 1.82% | 3.13% | -0.00% [-0.14%, 0.14%] | 0.553 [0.541, 0.565] | 11.7% | 9.2% | 0.000% | 200 | 155283 |
| R = 50, 40 decoys, bundling on | 3.69% [3.60%, 3.79%] | 0.67% | 3.71% | -0.01% [-0.04%, 0.02%] | 1.87% [1.83%, 1.92%] | 1.11% | 1.91% | -0.04% [-0.09%, 0.02%] | 0.557 [0.550, 0.564] | 6.4% | 5.4% | 0.000% | 200 | 517104 |

## Outcome-shuffle control (stable cells)

21 stable cells; 1 with a shuffled-outcome AUC interval excluding 0.5: R50_D40_B first_hop_content (0.504).

# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with every relay hop's hold stretched 1.5 times on every path. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 1 | 40 | 1.97 | 13.9% | 27.5% | 41.5% | 32.0% | 14.0% | 2,501,697 |
| 15 | 40 | 2.65 | 7.2% | 18.5% | 25.7% | 19.9% | 7.0% | 215,400 |
| 50 | 40 | 4.30 | 1.4% | 5.8% | 7.1% | 5.9% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -1.61 [-2.01, -1.20] | -1.34 [-1.63, -1.06] | 39656 |
| Baseline | 15 | 40 | -1.24 [-1.55, -0.92] | -0.76 [-0.99, -0.54] | 49168 |
| Baseline | 50 | 40 | -0.64 [-0.78, -0.51] | -0.53 [-0.63, -0.43] | 162956 |
| First hop, credential | 1 | 40 | -1.56 [-1.94, -1.17] | -1.18 [-1.38, -0.99] | 158624 |
| First hop, credential | 15 | 40 | -1.17 [-1.45, -0.88] | -0.82 [-0.96, -0.68] | 196672 |
| First hop, credential | 50 | 40 | -0.59 [-0.73, -0.47] | -0.57 [-0.62, -0.51] | 651824 |
| First hop, content | 1 | 40 | -1.56 [-1.94, -1.15] | -1.18 [-1.37, -0.98] | 158624 |
| First hop, content | 15 | 40 | -1.17 [-1.45, -0.88] | -0.82 [-0.97, -0.68] | 196672 |
| First hop, content | 50 | 40 | -0.59 [-0.72, -0.47] | -0.57 [-0.62, -0.51] | 651824 |
| Credential processor | 1 | 40 | -1.67 [-2.07, -1.25] | -1.22 [-1.46, -0.98] | 158624 |
| Credential processor | 15 | 40 | -1.20 [-1.51, -0.90] | -0.79 [-0.99, -0.60] | 196672 |
| Credential processor | 50 | 40 | -0.62 [-0.75, -0.49] | -0.56 [-0.64, -0.47] | 651824 |
| Content server | 1 | 40 | -1.71 [-2.59, -0.81] | -0.93 [-1.75, -0.16] | 7209 |
| Content server | 15 | 40 | -1.21 [-1.84, -0.59] | -1.40 [-1.95, -0.90] | 11757 |
| Content server | 50 | 40 | -0.96 [-1.25, -0.65] | -0.72 [-0.95, -0.49] | 38283 |
| Validator | 1 | 40 | -0.94 [-1.45, -0.43] | -0.84 [-1.15, -0.53] | 39656 |
| Validator | 15 | 40 | -0.88 [-1.19, -0.55] | -0.72 [-0.95, -0.50] | 49168 |
| Validator | 50 | 40 | -0.28 [-0.42, -0.13] | -0.34 [-0.43, -0.25] | 162956 |
| Gatekeeper | 1 | 40 | -1.52 [-1.92, -1.11] | -1.21 [-1.40, -1.03] | 118968 |
| Gatekeeper | 15 | 40 | -1.23 [-1.52, -0.93] | -0.82 [-0.96, -0.67] | 147504 |
| Gatekeeper | 50 | 40 | -0.60 [-0.74, -0.47] | -0.58 [-0.64, -0.52] | 488868 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.86% [6.51%, 7.21%] | 1.81% | 6.86% | 0.00% [0.00%, 0.00%] | 3.88% [3.70%, 4.07%] | 2.44% | 3.88% | 0.00% [0.00%, 0.00%] | 0.550 [0.535, 0.565] | 12.8% | 9.9% | 0.000% | 200 | 39901 |
| R = 15, 40 decoys, bundling on | 5.57% [5.32%, 5.79%] | 1.34% | 5.57% | 0.00% [0.00%, 0.00%] | 3.00% [2.86%, 3.16%] | 1.82% | 3.00% | 0.00% [0.00%, 0.00%] | 0.554 [0.541, 0.567] | 10.2% | 9.0% | 0.000% | 200 | 52047 |
| R = 50, 40 decoys, bundling on | 3.85% [3.75%, 3.95%] | 0.83% | 3.85% | 0.00% [0.00%, 0.00%] | 1.84% [1.78%, 1.91%] | 1.11% | 1.84% | 0.00% [0.00%, 0.00%] | 0.550 [0.542, 0.558] | 5.6% | 5.7% | 0.000% | 200 | 172341 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.90% [6.57%, 7.24%] | 1.81% | 6.86% | 0.04% [-0.06%, 0.12%] | 3.97% [3.85%, 4.08%] | 2.44% | 3.88% | 0.09% [-0.05%, 0.22%] | 0.551 [0.538, 0.565] | 12.0% | 9.7% | 0.000% | 200 | 159604 |
| R = 15, 40 decoys, bundling on | 5.62% [5.40%, 5.86%] | 1.34% | 5.57% | 0.05% [-0.02%, 0.11%] | 3.01% [2.92%, 3.10%] | 1.82% | 3.00% | 0.01% [-0.12%, 0.12%] | 0.553 [0.541, 0.565] | 10.4% | 9.2% | 0.000% | 200 | 208188 |
| R = 50, 40 decoys, bundling on | 3.87% [3.76%, 3.96%] | 0.83% | 3.85% | 0.02% [-0.01%, 0.04%] | 1.83% [1.80%, 1.86%] | 1.11% | 1.84% | -0.01% [-0.07%, 0.05%] | 0.550 [0.543, 0.557] | 5.8% | 5.7% | 0.000% | 200 | 689364 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.90% [6.56%, 7.22%] | 1.81% | 6.86% | 0.04% [-0.05%, 0.13%] | 3.97% [3.85%, 4.09%] | 2.44% | 3.88% | 0.09% [-0.03%, 0.22%] | 0.551 [0.538, 0.565] | 12.0% | 9.7% | 0.000% | 200 | 159604 |
| R = 15, 40 decoys, bundling on | 5.62% [5.39%, 5.85%] | 1.34% | 5.57% | 0.05% [-0.02%, 0.12%] | 3.01% [2.93%, 3.10%] | 1.82% | 3.00% | 0.01% [-0.11%, 0.13%] | 0.553 [0.541, 0.565] | 10.4% | 9.2% | 0.000% | 200 | 208188 |
| R = 50, 40 decoys, bundling on | 3.87% [3.77%, 3.96%] | 0.83% | 3.85% | 0.02% [-0.01%, 0.04%] | 1.83% [1.80%, 1.86%] | 1.11% | 1.84% | -0.01% [-0.07%, 0.05%] | 0.550 [0.543, 0.557] | 5.8% | 5.7% | 0.000% | 200 | 689364 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.86% [6.52%, 7.19%] | 1.81% | 6.86% | -0.01% [-0.06%, 0.04%] | 3.93% [3.77%, 4.09%] | 2.44% | 3.88% | 0.05% [-0.04%, 0.14%] | 0.551 [0.536, 0.566] | 11.7% | 10.0% | 0.000% | 200 | 159604 |
| R = 15, 40 decoys, bundling on | 5.58% [5.34%, 5.82%] | 1.34% | 5.57% | 0.01% [-0.01%, 0.04%] | 3.01% [2.88%, 3.14%] | 1.82% | 3.00% | 0.01% [-0.06%, 0.08%] | 0.554 [0.541, 0.568] | 10.7% | 9.0% | 0.000% | 200 | 208188 |
| R = 50, 40 decoys, bundling on | 3.86% [3.76%, 3.97%] | 0.83% | 3.85% | 0.01% [-0.00%, 0.02%] | 1.83% [1.77%, 1.88%] | 1.11% | 1.84% | -0.01% [-0.04%, 0.01%] | 0.549 [0.541, 0.557] | 5.6% | 5.7% | 0.000% | 200 | 689364 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.56% [7.31%, 7.83%] | 2.08% | 6.86% | 0.70% [0.48%, 0.92%] | 4.61% [4.47%, 4.76%] | 2.44% | 3.88% | 0.73% [0.52%, 0.95%] | 0.555 [0.545, 0.564] | 9.6% | 9.6% | 0.000% | 200 | 79802 |
| R = 15, 40 decoys, bundling on | 6.11% [5.91%, 6.32%] | 1.55% | 5.57% | 0.55% [0.39%, 0.71%] | 3.61% [3.50%, 3.72%] | 1.82% | 3.00% | 0.61% [0.41%, 0.80%] | 0.541 [0.532, 0.550] | 6.8% | 7.2% | 0.001% | 200 | 104094 |
| R = 50, 40 decoys, bundling on | 4.16% [4.07%, 4.24%] | 0.95% | 3.85% | 0.31% [0.23%, 0.38%] | 2.25% [2.20%, 2.30%] | 1.11% | 1.84% | 0.41% [0.33%, 0.49%] | 0.550 [0.544, 0.555] | 3.9% | 5.0% | 0.000% | 200 | 344682 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.59% [8.24%, 8.93%] | 2.00% | 6.86% | 1.73% [1.38%, 2.08%] | 4.58% [4.39%, 4.76%] | 2.44% | 3.88% | 0.70% [0.45%, 0.97%] | 0.567 [0.554, 0.579] | 16.8% | 12.9% | 0.028% | 200 | 39901 |
| R = 15, 40 decoys, bundling on | 6.93% [6.70%, 7.17%] | 1.49% | 5.57% | 1.37% [1.10%, 1.64%] | 3.31% [3.17%, 3.47%] | 1.82% | 3.00% | 0.31% [0.10%, 0.52%] | 0.560 [0.548, 0.571] | 12.9% | 10.8% | 0.006% | 200 | 52047 |
| R = 50, 40 decoys, bundling on | 4.81% [4.70%, 4.92%] | 0.91% | 3.85% | 0.96% [0.84%, 1.07%] | 2.14% [2.08%, 2.21%] | 1.11% | 1.84% | 0.30% [0.21%, 0.39%] | 0.562 [0.555, 0.568] | 8.2% | 7.4% | 0.000% | 200 | 172341 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.90% [6.57%, 7.26%] | 1.81% | 6.86% | 0.04% [-0.06%, 0.15%] | 3.94% [3.80%, 4.08%] | 2.44% | 3.88% | 0.06% [-0.13%, 0.23%] | 0.553 [0.539, 0.567] | 12.5% | 10.0% | 0.000% | 200 | 119703 |
| R = 15, 40 decoys, bundling on | 5.58% [5.33%, 5.81%] | 1.34% | 5.57% | 0.01% [-0.06%, 0.08%] | 2.90% [2.80%, 3.01%] | 1.82% | 3.00% | -0.10% [-0.23%, 0.04%] | 0.553 [0.540, 0.566] | 11.1% | 9.0% | 0.000% | 200 | 156141 |
| R = 50, 40 decoys, bundling on | 3.85% [3.76%, 3.96%] | 0.83% | 3.85% | 0.00% [-0.03%, 0.04%] | 1.79% [1.75%, 1.83%] | 1.11% | 1.84% | -0.05% [-0.11%, 0.01%] | 0.549 [0.542, 0.557] | 5.7% | 5.7% | 0.000% | 200 | 517023 |

## Outcome-shuffle control (stable cells)

21 stable cells; 1 with a shuffled-outcome AUC interval excluding 0.5: R1_D40_B cred_processor (0.508).

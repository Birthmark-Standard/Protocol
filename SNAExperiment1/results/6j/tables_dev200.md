# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the device's content-channel hold and the content servers' own hold stretched 2 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 15 | 40 | 2.65 | 7.0% | 18.7% | 25.7% | 20.1% | 7.1% | 215,400 |
| 50 | 40 | 4.30 | 1.4% | 5.8% | 7.2% | 5.9% | 1.4% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -1.11 [-1.52, -0.68] | -0.75 [-1.05, -0.43] | 39392 |
| Baseline | 15 | 40 | -1.08 [-1.45, -0.73] | -0.46 [-0.67, -0.24] | 46360 |
| Baseline | 50 | 40 | -0.37 [-0.53, -0.22] | -0.27 [-0.37, -0.18] | 153382 |
| First hop, credential | 1 | 40 | -1.03 [-1.42, -0.63] | -0.68 [-0.91, -0.45] | 157568 |
| First hop, credential | 15 | 40 | -1.09 [-1.44, -0.73] | -0.44 [-0.60, -0.28] | 185440 |
| First hop, credential | 50 | 40 | -0.36 [-0.51, -0.22] | -0.31 [-0.37, -0.25] | 613528 |
| First hop, content | 1 | 40 | -1.03 [-1.42, -0.64] | -0.68 [-0.92, -0.44] | 157568 |
| First hop, content | 15 | 40 | -1.09 [-1.43, -0.74] | -0.44 [-0.60, -0.28] | 185440 |
| First hop, content | 50 | 40 | -0.36 [-0.52, -0.22] | -0.31 [-0.37, -0.25] | 613528 |
| Credential processor | 1 | 40 | -1.15 [-1.55, -0.71] | -0.63 [-0.91, -0.34] | 157568 |
| Credential processor | 15 | 40 | -1.06 [-1.43, -0.71] | -0.52 [-0.73, -0.31] | 185440 |
| Credential processor | 50 | 40 | -0.37 [-0.52, -0.21] | -0.27 [-0.36, -0.19] | 613528 |
| Content server | 1 | 40 | -1.98 [-2.84, -1.04] | -1.07 [-1.85, -0.35] | 8187 |
| Content server | 15 | 40 | -1.99 [-2.68, -1.27] | -1.28 [-1.84, -0.74] | 10968 |
| Content server | 50 | 40 | -0.75 [-1.06, -0.43] | -0.35 [-0.59, -0.12] | 36109 |
| Validator | 1 | 40 | -2.31 [-2.76, -1.87] | -2.10 [-2.38, -1.83] | 39392 |
| Validator | 15 | 40 | -2.38 [-2.74, -2.04] | -1.44 [-1.66, -1.22] | 46360 |
| Validator | 50 | 40 | -1.13 [-1.28, -0.99] | -0.81 [-0.91, -0.71] | 153382 |
| Gatekeeper | 1 | 40 | -1.09 [-1.46, -0.70] | -0.69 [-0.90, -0.48] | 118176 |
| Gatekeeper | 15 | 40 | -1.11 [-1.50, -0.78] | -0.44 [-0.60, -0.28] | 139080 |
| Gatekeeper | 50 | 40 | -0.38 [-0.55, -0.22] | -0.32 [-0.39, -0.26] | 460146 |

## Change from the content200 build on the same records

Accuracy in this build minus accuracy in the content200 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.51 [+0.29, +0.74] | +0.42 [+0.14, +0.70] | 39799 |
| Baseline | 15 | 40 | +0.47 [+0.30, +0.63] | +0.37 [+0.16, +0.58] | 52017 |
| Baseline | 50 | 40 | +0.27 [+0.18, +0.35] | +0.19 [+0.11, +0.28] | 172224 |
| First hop, credential | 1 | 40 | +0.57 [+0.38, +0.76] | +0.44 [+0.26, +0.62] | 159196 |
| First hop, credential | 15 | 40 | +0.43 [+0.30, +0.56] | +0.41 [+0.29, +0.53] | 208068 |
| First hop, credential | 50 | 40 | +0.26 [+0.19, +0.33] | +0.18 [+0.12, +0.23] | 688896 |
| First hop, content | 1 | 40 | +0.57 [+0.38, +0.76] | +0.44 [+0.26, +0.63] | 159196 |
| First hop, content | 15 | 40 | +0.43 [+0.29, +0.56] | +0.41 [+0.29, +0.53] | 208068 |
| First hop, content | 50 | 40 | +0.26 [+0.18, +0.33] | +0.18 [+0.12, +0.23] | 688896 |
| Credential processor | 1 | 40 | +0.57 [+0.35, +0.77] | +0.52 [+0.29, +0.76] | 159196 |
| Credential processor | 15 | 40 | +0.45 [+0.30, +0.60] | +0.27 [+0.10, +0.47] | 208068 |
| Credential processor | 50 | 40 | +0.26 [+0.18, +0.35] | +0.23 [+0.15, +0.30] | 688896 |
| Content server | 1 | 40 | +1.05 [+0.86, +1.24] | +0.99 [+0.77, +1.22] | 79598 |
| Content server | 15 | 40 | +0.85 [+0.69, +0.99] | +0.58 [+0.42, +0.74] | 104034 |
| Content server | 50 | 40 | +0.69 [+0.61, +0.76] | +0.47 [+0.41, +0.54] | 344448 |
| Validator | 1 | 40 | +0.87 [+0.66, +1.09] | +0.35 [+0.11, +0.57] | 39799 |
| Validator | 15 | 40 | +0.41 [+0.25, +0.58] | +0.52 [+0.37, +0.68] | 52017 |
| Validator | 50 | 40 | +0.42 [+0.33, +0.50] | +0.38 [+0.30, +0.45] | 172224 |
| Gatekeeper | 1 | 40 | +0.51 [+0.31, +0.71] | +0.44 [+0.25, +0.64] | 119397 |
| Gatekeeper | 15 | 40 | +0.42 [+0.28, +0.56] | +0.30 [+0.16, +0.43] | 156051 |
| Gatekeeper | 50 | 40 | +0.24 [+0.16, +0.32] | +0.15 [+0.09, +0.22] | 516672 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.32% [6.94%, 7.70%] | 2.00% | 7.32% | 0.00% [0.00%, 0.00%] | 4.46% [4.24%, 4.67%] | 2.44% | 4.46% | 0.00% [0.00%, 0.00%] | 0.551 [0.537, 0.565] | 15.6% | 12.0% | 0.000% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.71% [5.47%, 5.95%] | 1.49% | 5.71% | 0.00% [0.00%, 0.00%] | 3.31% [3.17%, 3.46%] | 1.82% | 3.31% | 0.00% [0.00%, 0.00%] | 0.560 [0.548, 0.572] | 10.6% | 8.4% | 0.002% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 4.08% [3.98%, 4.19%] | 0.91% | 4.08% | 0.00% [0.00%, 0.00%] | 2.09% [2.03%, 2.16%] | 1.11% | 2.09% | 0.00% [0.00%, 0.00%] | 0.554 [0.546, 0.562] | 8.1% | 6.1% | 0.000% | 200 | 172224 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.39% [7.03%, 7.74%] | 2.00% | 7.32% | 0.07% [-0.01%, 0.13%] | 4.46% [4.29%, 4.62%] | 2.44% | 4.46% | -0.00% [-0.13%, 0.13%] | 0.549 [0.536, 0.563] | 15.6% | 12.2% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.71% [5.49%, 5.95%] | 1.49% | 5.71% | 0.01% [-0.05%, 0.06%] | 3.38% [3.28%, 3.48%] | 1.82% | 3.31% | 0.07% [-0.02%, 0.17%] | 0.562 [0.550, 0.573] | 10.8% | 8.4% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 4.07% [3.97%, 4.16%] | 0.91% | 4.08% | -0.02% [-0.04%, 0.01%] | 2.09% [2.05%, 2.13%] | 1.11% | 2.09% | -0.01% [-0.06%, 0.04%] | 0.555 [0.548, 0.562] | 8.0% | 6.2% | 0.000% | 200 | 688896 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.39% [7.03%, 7.75%] | 2.00% | 7.32% | 0.07% [-0.01%, 0.14%] | 4.46% [4.29%, 4.62%] | 2.44% | 4.46% | -0.00% [-0.13%, 0.12%] | 0.549 [0.536, 0.563] | 15.6% | 12.2% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.71% [5.48%, 5.94%] | 1.49% | 5.71% | 0.01% [-0.06%, 0.06%] | 3.38% [3.28%, 3.49%] | 1.82% | 3.31% | 0.07% [-0.03%, 0.17%] | 0.562 [0.550, 0.573] | 10.8% | 8.4% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 4.07% [3.97%, 4.16%] | 0.91% | 4.08% | -0.02% [-0.04%, 0.01%] | 2.09% [2.04%, 2.13%] | 1.11% | 2.09% | -0.01% [-0.06%, 0.04%] | 0.555 [0.548, 0.562] | 8.0% | 6.2% | 0.000% | 200 | 688896 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.34% [6.98%, 7.69%] | 2.00% | 7.32% | 0.02% [-0.03%, 0.06%] | 4.52% [4.34%, 4.71%] | 2.44% | 4.46% | 0.06% [-0.03%, 0.15%] | 0.552 [0.538, 0.565] | 15.5% | 12.0% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.72% [5.47%, 5.96%] | 1.49% | 5.71% | 0.01% [-0.02%, 0.03%] | 3.28% [3.16%, 3.41%] | 1.82% | 3.31% | -0.03% [-0.11%, 0.04%] | 0.559 [0.547, 0.570] | 10.7% | 8.5% | 0.003% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 4.08% [3.97%, 4.18%] | 0.91% | 4.08% | -0.01% [-0.02%, 0.01%] | 2.12% [2.07%, 2.18%] | 1.11% | 2.09% | 0.03% [-0.00%, 0.05%] | 0.555 [0.547, 0.563] | 8.0% | 6.2% | 0.000% | 200 | 688896 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.69% [7.41%, 8.00%] | 2.16% | 7.32% | 0.37% [0.14%, 0.60%] | 5.29% [5.14%, 5.45%] | 2.44% | 4.46% | 0.83% [0.60%, 1.06%] | 0.553 [0.542, 0.564] | 7.7% | 9.9% | 0.000% | 200 | 79598 |
| R = 15, 40 decoys, bundling on | 6.11% [5.89%, 6.33%] | 1.61% | 5.71% | 0.40% [0.23%, 0.57%] | 3.77% [3.67%, 3.89%] | 1.82% | 3.31% | 0.46% [0.28%, 0.65%] | 0.539 [0.531, 0.548] | 5.1% | 6.6% | 0.000% | 200 | 104034 |
| R = 50, 40 decoys, bundling on | 4.39% [4.30%, 4.49%] | 0.99% | 4.08% | 0.31% [0.23%, 0.39%] | 2.41% [2.36%, 2.47%] | 1.11% | 2.09% | 0.32% [0.24%, 0.40%] | 0.535 [0.530, 0.541] | 3.1% | 4.2% | 0.000% | 200 | 344448 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.23% [6.88%, 7.57%] | 1.83% | 7.32% | -0.09% [-0.41%, 0.24%] | 3.31% [3.13%, 3.49%] | 2.44% | 4.46% | -1.15% [-1.43%, -0.88%] | 0.559 [0.547, 0.572] | 13.8% | 11.6% | 0.018% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.53% [5.28%, 5.77%] | 1.36% | 5.71% | -0.17% [-0.40%, 0.05%] | 2.60% [2.49%, 2.72%] | 1.82% | 3.31% | -0.71% [-0.90%, -0.52%] | 0.548 [0.535, 0.562] | 8.7% | 7.5% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.93% [3.83%, 4.02%] | 0.84% | 4.08% | -0.16% [-0.27%, -0.05%] | 1.67% [1.62%, 1.73%] | 1.11% | 2.09% | -0.42% [-0.51%, -0.33%] | 0.553 [0.544, 0.561] | 6.7% | 5.9% | 0.000% | 200 | 172224 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.31% [6.97%, 7.66%] | 2.00% | 7.32% | -0.01% [-0.11%, 0.09%] | 4.45% [4.30%, 4.60%] | 2.44% | 4.46% | -0.01% [-0.22%, 0.20%] | 0.551 [0.538, 0.564] | 14.7% | 11.9% | 0.000% | 200 | 119397 |
| R = 15, 40 decoys, bundling on | 5.69% [5.46%, 5.91%] | 1.49% | 5.71% | -0.02% [-0.09%, 0.05%] | 3.33% [3.23%, 3.43%] | 1.82% | 3.31% | 0.02% [-0.13%, 0.16%] | 0.559 [0.548, 0.570] | 10.5% | 8.5% | 0.001% | 200 | 156051 |
| R = 50, 40 decoys, bundling on | 4.05% [3.94%, 4.14%] | 0.91% | 4.08% | -0.04% [-0.07%, -0.00%] | 2.06% [2.02%, 2.11%] | 1.11% | 2.09% | -0.03% [-0.09%, 0.03%] | 0.556 [0.549, 0.564] | 7.8% | 6.2% | 0.000% | 200 | 516672 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R1_D40_B content_server (0.510), R50_D40_B baseline (0.507).

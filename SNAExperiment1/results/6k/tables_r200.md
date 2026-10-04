# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with every relay hop's hold stretched 2 times on every path. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 15 | 40 | 2.65 | 7.0% | 18.7% | 25.7% | 20.1% | 7.0% | 215,400 |
| 50 | 40 | 4.31 | 1.4% | 5.8% | 7.1% | 5.9% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -2.32 [-2.73, -1.90] | -2.15 [-2.44, -1.87] | 39392 |
| Baseline | 15 | 40 | -1.92 [-2.31, -1.56] | -1.31 [-1.56, -1.08] | 46360 |
| Baseline | 50 | 40 | -1.02 [-1.17, -0.87] | -0.90 [-0.99, -0.81] | 153382 |
| First hop, credential | 1 | 40 | -2.31 [-2.70, -1.93] | -2.02 [-2.23, -1.82] | 157568 |
| First hop, credential | 15 | 40 | -1.95 [-2.29, -1.60] | -1.42 [-1.55, -1.28] | 185440 |
| First hop, credential | 50 | 40 | -0.99 [-1.14, -0.86] | -0.92 [-0.97, -0.87] | 613528 |
| First hop, content | 1 | 40 | -2.31 [-2.69, -1.92] | -2.02 [-2.21, -1.82] | 157568 |
| First hop, content | 15 | 40 | -1.95 [-2.28, -1.59] | -1.42 [-1.56, -1.28] | 185440 |
| First hop, content | 50 | 40 | -0.99 [-1.13, -0.86] | -0.92 [-0.97, -0.87] | 613528 |
| Credential processor | 1 | 40 | -2.36 [-2.76, -1.94] | -2.05 [-2.31, -1.79] | 157568 |
| Credential processor | 15 | 40 | -1.90 [-2.28, -1.53] | -1.41 [-1.61, -1.20] | 185440 |
| Credential processor | 50 | 40 | -1.00 [-1.15, -0.85] | -0.92 [-0.99, -0.84] | 613528 |
| Content server | 1 | 40 | -2.70 [-3.60, -1.81] | -2.55 [-3.30, -1.82] | 8187 |
| Content server | 15 | 40 | -2.98 [-3.67, -2.29] | -1.77 [-2.24, -1.25] | 10968 |
| Content server | 50 | 40 | -1.62 [-1.92, -1.31] | -1.22 [-1.45, -1.00] | 36109 |
| Validator | 1 | 40 | -1.75 [-2.22, -1.28] | -1.20 [-1.51, -0.89] | 39392 |
| Validator | 15 | 40 | -1.73 [-2.07, -1.39] | -0.96 [-1.20, -0.72] | 46360 |
| Validator | 50 | 40 | -0.67 [-0.83, -0.50] | -0.57 [-0.67, -0.47] | 153382 |
| Gatekeeper | 1 | 40 | -2.22 [-2.62, -1.81] | -2.01 [-2.22, -1.81] | 118176 |
| Gatekeeper | 15 | 40 | -1.87 [-2.25, -1.50] | -1.34 [-1.50, -1.17] | 139080 |
| Gatekeeper | 50 | 40 | -0.97 [-1.13, -0.83] | -0.90 [-0.96, -0.84] | 460146 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.11% [5.76%, 6.48%] | 1.63% | 6.11% | 0.00% [0.00%, 0.00%] | 3.05% [2.87%, 3.22%] | 2.44% | 3.05% | 0.00% [0.00%, 0.00%] | 0.563 [0.547, 0.579] | 13.3% | 10.0% | 0.048% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 4.90% [4.64%, 5.16%] | 1.22% | 4.90% | 0.00% [0.00%, 0.00%] | 2.48% [2.33%, 2.62%] | 1.82% | 2.48% | 0.00% [0.00%, 0.00%] | 0.544 [0.530, 0.558] | 5.8% | 6.0% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.46% [3.37%, 3.56%] | 0.75% | 3.46% | 0.00% [0.00%, 0.00%] | 1.47% [1.42%, 1.53%] | 1.11% | 1.47% | 0.00% [0.00%, 0.00%] | 0.556 [0.548, 0.564] | 5.9% | 5.5% | 0.000% | 200 | 172224 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.11% [5.74%, 6.43%] | 1.63% | 6.11% | -0.00% [-0.08%, 0.08%] | 3.11% [3.00%, 3.21%] | 2.44% | 3.05% | 0.06% [-0.07%, 0.19%] | 0.561 [0.546, 0.577] | 12.3% | 10.0% | 0.013% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 4.87% [4.65%, 5.11%] | 1.22% | 4.90% | -0.03% [-0.10%, 0.03%] | 2.41% [2.34%, 2.49%] | 1.82% | 2.48% | -0.07% [-0.19%, 0.04%] | 0.541 [0.529, 0.554] | 6.9% | 6.1% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.45% [3.36%, 3.54%] | 0.75% | 3.46% | -0.01% [-0.04%, 0.03%] | 1.49% [1.46%, 1.52%] | 1.11% | 1.47% | 0.01% [-0.04%, 0.07%] | 0.556 [0.549, 0.563] | 6.1% | 5.3% | 0.000% | 200 | 688896 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.11% [5.80%, 6.45%] | 1.63% | 6.11% | -0.00% [-0.08%, 0.08%] | 3.11% [3.01%, 3.21%] | 2.44% | 3.05% | 0.06% [-0.08%, 0.19%] | 0.561 [0.546, 0.577] | 12.3% | 10.0% | 0.013% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 4.87% [4.63%, 5.11%] | 1.22% | 4.90% | -0.03% [-0.09%, 0.03%] | 2.41% [2.33%, 2.49%] | 1.82% | 2.48% | -0.07% [-0.18%, 0.05%] | 0.541 [0.529, 0.554] | 6.9% | 6.1% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.45% [3.36%, 3.54%] | 0.75% | 3.46% | -0.01% [-0.04%, 0.03%] | 1.49% [1.46%, 1.52%] | 1.11% | 1.47% | 0.01% [-0.03%, 0.06%] | 0.556 [0.549, 0.563] | 6.1% | 5.3% | 0.000% | 200 | 688896 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.13% [5.79%, 6.46%] | 1.63% | 6.11% | 0.01% [-0.03%, 0.06%] | 3.09% [2.95%, 3.24%] | 2.44% | 3.05% | 0.04% [-0.03%, 0.12%] | 0.561 [0.545, 0.577] | 12.7% | 9.9% | 0.047% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 4.91% [4.65%, 5.17%] | 1.22% | 4.90% | 0.01% [-0.02%, 0.03%] | 2.43% [2.31%, 2.55%] | 1.82% | 2.48% | -0.05% [-0.12%, 0.01%] | 0.543 [0.529, 0.556] | 5.8% | 6.1% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.47% [3.37%, 3.56%] | 0.75% | 3.46% | 0.01% [-0.00%, 0.02%] | 1.47% [1.41%, 1.52%] | 1.11% | 1.47% | -0.01% [-0.03%, 0.01%] | 0.556 [0.548, 0.564] | 5.9% | 5.4% | 0.000% | 200 | 688896 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.58% [6.30%, 6.89%] | 1.85% | 6.11% | 0.47% [0.26%, 0.69%] | 3.91% [3.78%, 4.05%] | 2.44% | 3.05% | 0.87% [0.66%, 1.07%] | 0.547 [0.536, 0.558] | 5.7% | 8.5% | 0.000% | 200 | 79598 |
| R = 15, 40 decoys, bundling on | 5.16% [4.96%, 5.36%] | 1.37% | 4.90% | 0.25% [0.09%, 0.42%] | 2.91% [2.82%, 3.02%] | 1.82% | 2.48% | 0.44% [0.28%, 0.59%] | 0.541 [0.532, 0.550] | 5.6% | 6.2% | 0.000% | 200 | 104034 |
| R = 50, 40 decoys, bundling on | 3.58% [3.50%, 3.66%] | 0.84% | 3.46% | 0.12% [0.05%, 0.20%] | 1.78% [1.73%, 1.82%] | 1.11% | 1.47% | 0.30% [0.23%, 0.37%] | 0.546 [0.540, 0.552] | 4.0% | 4.1% | 0.000% | 200 | 344448 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.77% [7.41%, 8.13%] | 1.89% | 6.11% | 1.66% [1.28%, 2.05%] | 4.21% [4.03%, 4.40%] | 2.44% | 3.05% | 1.16% [0.91%, 1.40%] | 0.570 [0.557, 0.584] | 14.6% | 13.0% | 0.038% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 6.17% [5.93%, 6.41%] | 1.41% | 4.90% | 1.27% [1.00%, 1.55%] | 3.00% [2.85%, 3.16%] | 1.82% | 2.48% | 0.52% [0.32%, 0.72%] | 0.551 [0.539, 0.563] | 10.0% | 9.4% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 4.37% [4.26%, 4.49%] | 0.86% | 3.46% | 0.92% [0.79%, 1.03%] | 1.92% [1.86%, 1.98%] | 1.11% | 1.47% | 0.45% [0.37%, 0.53%] | 0.555 [0.548, 0.562] | 7.4% | 6.7% | 0.000% | 200 | 172224 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.17% [5.82%, 6.52%] | 1.63% | 6.11% | 0.06% [-0.04%, 0.16%] | 3.13% [3.02%, 3.26%] | 2.44% | 3.05% | 0.09% [-0.05%, 0.23%] | 0.561 [0.546, 0.577] | 12.0% | 9.8% | 0.023% | 200 | 119397 |
| R = 15, 40 decoys, bundling on | 4.93% [4.68%, 5.19%] | 1.22% | 4.90% | 0.03% [-0.04%, 0.10%] | 2.42% [2.32%, 2.52%] | 1.82% | 2.48% | -0.06% [-0.18%, 0.08%] | 0.541 [0.528, 0.555] | 5.9% | 5.9% | 0.000% | 200 | 156051 |
| R = 50, 40 decoys, bundling on | 3.47% [3.37%, 3.56%] | 0.75% | 3.46% | 0.01% [-0.02%, 0.04%] | 1.47% [1.43%, 1.51%] | 1.11% | 1.47% | -0.00% [-0.06%, 0.05%] | 0.556 [0.548, 0.563] | 5.9% | 5.5% | 0.000% | 200 | 516672 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R1_D40_B first_hop_cred (0.507), R50_D40_B first_hop_content (0.504).

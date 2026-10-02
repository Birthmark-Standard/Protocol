# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the content paths' device and relay-hop holds stretched 2 times and the credential path's shortened to 0.75 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 15 | 40 | 2.65 | 7.0% | 18.6% | 25.6% | 20.0% | 7.0% | 215,400 |
| 50 | 40 | 4.30 | 1.4% | 5.8% | 7.2% | 5.9% | 1.4% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -1.58 [-2.01, -1.12] | -1.38 [-1.67, -1.10] | 39392 |
| Baseline | 15 | 40 | -1.54 [-1.90, -1.19] | -0.86 [-1.09, -0.63] | 46360 |
| Baseline | 50 | 40 | -0.65 [-0.80, -0.51] | -0.52 [-0.63, -0.43] | 153382 |
| First hop, credential | 1 | 40 | -1.59 [-1.99, -1.18] | -1.22 [-1.42, -1.00] | 157568 |
| First hop, credential | 15 | 40 | -1.55 [-1.89, -1.23] | -0.96 [-1.10, -0.81] | 185440 |
| First hop, credential | 50 | 40 | -0.66 [-0.79, -0.52] | -0.55 [-0.61, -0.49] | 613528 |
| First hop, content | 1 | 40 | -1.59 [-1.97, -1.19] | -1.22 [-1.43, -1.02] | 157568 |
| First hop, content | 15 | 40 | -1.55 [-1.89, -1.21] | -0.96 [-1.11, -0.81] | 185440 |
| First hop, content | 50 | 40 | -0.66 [-0.79, -0.52] | -0.55 [-0.61, -0.49] | 613528 |
| Credential processor | 1 | 40 | -1.67 [-2.11, -1.21] | -1.23 [-1.46, -1.00] | 157568 |
| Credential processor | 15 | 40 | -1.52 [-1.89, -1.17] | -0.84 [-1.03, -0.65] | 185440 |
| Credential processor | 50 | 40 | -0.64 [-0.78, -0.49] | -0.52 [-0.61, -0.44] | 613528 |
| Content server | 1 | 40 | -3.05 [-3.94, -2.10] | -2.26 [-3.00, -1.56] | 8187 |
| Content server | 15 | 40 | -3.14 [-3.74, -2.51] | -1.60 [-2.04, -1.12] | 10968 |
| Content server | 50 | 40 | -1.43 [-1.76, -1.11] | -1.06 [-1.28, -0.85] | 36109 |
| Validator | 1 | 40 | -3.40 [-3.84, -2.93] | -2.79 [-3.06, -2.54] | 39392 |
| Validator | 15 | 40 | -2.91 [-3.27, -2.57] | -2.10 [-2.31, -1.89] | 46360 |
| Validator | 50 | 40 | -1.64 [-1.79, -1.48] | -1.24 [-1.33, -1.15] | 153382 |
| Gatekeeper | 1 | 40 | -1.58 [-1.99, -1.16] | -1.27 [-1.47, -1.08] | 118176 |
| Gatekeeper | 15 | 40 | -1.54 [-1.89, -1.18] | -0.75 [-0.91, -0.60] | 139080 |
| Gatekeeper | 50 | 40 | -0.64 [-0.79, -0.50] | -0.55 [-0.62, -0.49] | 460146 |

## Change from the content200 build on the same records

Accuracy in this build minus accuracy in the content200 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.03 [-0.14, +0.19] | -0.20 [-0.46, +0.05] | 39799 |
| Baseline | 15 | 40 | +0.03 [-0.11, +0.16] | -0.03 [-0.21, +0.14] | 52017 |
| Baseline | 50 | 40 | -0.01 [-0.07, +0.06] | -0.05 [-0.14, +0.04] | 172224 |
| First hop, credential | 1 | 40 | +0.01 [-0.12, +0.14] | -0.09 [-0.25, +0.07] | 159196 |
| First hop, credential | 15 | 40 | -0.03 [-0.14, +0.07] | -0.09 [-0.20, +0.02] | 208068 |
| First hop, credential | 50 | 40 | -0.03 [-0.07, +0.01] | -0.05 [-0.10, -0.01] | 688896 |
| First hop, content | 1 | 40 | +0.01 [-0.12, +0.14] | -0.09 [-0.26, +0.07] | 159196 |
| First hop, content | 15 | 40 | -0.03 [-0.13, +0.08] | -0.09 [-0.19, +0.02] | 208068 |
| First hop, content | 50 | 40 | -0.03 [-0.08, +0.02] | -0.05 [-0.10, -0.00] | 688896 |
| Credential processor | 1 | 40 | +0.04 [-0.13, +0.19] | -0.07 [-0.28, +0.14] | 159196 |
| Credential processor | 15 | 40 | -0.00 [-0.14, +0.13] | -0.04 [-0.17, +0.11] | 208068 |
| Credential processor | 50 | 40 | -0.00 [-0.06, +0.05] | -0.03 [-0.10, +0.04] | 688896 |
| Content server | 1 | 40 | -0.02 [-0.19, +0.16] | -0.23 [-0.43, -0.02] | 79598 |
| Content server | 15 | 40 | -0.14 [-0.28, -0.01] | -0.18 [-0.33, -0.04] | 104034 |
| Content server | 50 | 40 | -0.09 [-0.16, -0.02] | -0.03 [-0.10, +0.04] | 344448 |
| Validator | 1 | 40 | -0.24 [-0.43, -0.04] | -0.34 [-0.54, -0.14] | 39799 |
| Validator | 15 | 40 | -0.19 [-0.34, -0.05] | -0.17 [-0.33, -0.02] | 52017 |
| Validator | 50 | 40 | -0.10 [-0.16, -0.04] | -0.07 [-0.13, +0.00] | 172224 |
| Gatekeeper | 1 | 40 | -0.00 [-0.14, +0.14] | -0.14 [-0.31, +0.04] | 119397 |
| Gatekeeper | 15 | 40 | -0.02 [-0.14, +0.09] | -0.05 [-0.17, +0.07] | 156051 |
| Gatekeeper | 50 | 40 | -0.02 [-0.08, +0.03] | -0.08 [-0.14, -0.03] | 516672 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.84% [6.44%, 7.22%] | 1.76% | 6.84% | 0.00% [0.00%, 0.00%] | 3.83% [3.64%, 4.03%] | 2.44% | 3.83% | 0.00% [0.00%, 0.00%] | 0.551 [0.535, 0.566] | 12.8% | 10.2% | 0.008% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.27% [5.03%, 5.51%] | 1.31% | 5.27% | 0.00% [0.00%, 0.00%] | 2.91% [2.78%, 3.04%] | 1.82% | 2.91% | 0.00% [0.00%, 0.00%] | 0.542 [0.529, 0.554] | 8.5% | 7.4% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.81% [3.72%, 3.90%] | 0.81% | 3.81% | 0.00% [0.00%, 0.00%] | 1.85% [1.78%, 1.92%] | 1.11% | 1.85% | 0.00% [0.00%, 0.00%] | 0.554 [0.545, 0.563] | 8.1% | 5.9% | 0.000% | 200 | 172224 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.83% [6.45%, 7.17%] | 1.76% | 6.84% | -0.02% [-0.11%, 0.08%] | 3.93% [3.80%, 4.06%] | 2.44% | 3.83% | 0.09% [-0.04%, 0.23%] | 0.549 [0.535, 0.563] | 12.4% | 10.4% | 0.009% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.26% [5.04%, 5.48%] | 1.31% | 5.27% | -0.01% [-0.08%, 0.05%] | 2.88% [2.80%, 2.97%] | 1.82% | 2.91% | -0.03% [-0.14%, 0.08%] | 0.542 [0.531, 0.554] | 8.6% | 7.3% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.78% [3.69%, 3.86%] | 0.81% | 3.81% | -0.03% [-0.06%, -0.00%] | 1.86% [1.82%, 1.90%] | 1.11% | 1.85% | 0.01% [-0.05%, 0.07%] | 0.553 [0.546, 0.561] | 7.5% | 5.8% | 0.000% | 200 | 688896 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.83% [6.47%, 7.20%] | 1.76% | 6.84% | -0.02% [-0.11%, 0.08%] | 3.93% [3.80%, 4.06%] | 2.44% | 3.83% | 0.09% [-0.04%, 0.23%] | 0.549 [0.535, 0.563] | 12.4% | 10.4% | 0.009% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.26% [5.03%, 5.48%] | 1.31% | 5.27% | -0.01% [-0.08%, 0.05%] | 2.88% [2.80%, 2.97%] | 1.82% | 2.91% | -0.03% [-0.13%, 0.08%] | 0.542 [0.531, 0.554] | 8.6% | 7.3% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.78% [3.69%, 3.86%] | 0.81% | 3.81% | -0.03% [-0.07%, -0.00%] | 1.86% [1.82%, 1.90%] | 1.11% | 1.85% | 0.01% [-0.05%, 0.07%] | 0.553 [0.546, 0.561] | 7.5% | 5.8% | 0.000% | 200 | 688896 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.81% [6.44%, 7.18%] | 1.76% | 6.84% | -0.03% [-0.07%, 0.01%] | 3.92% [3.76%, 4.08%] | 2.44% | 3.83% | 0.09% [-0.01%, 0.19%] | 0.551 [0.535, 0.566] | 12.8% | 10.3% | 0.011% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.27% [5.02%, 5.51%] | 1.31% | 5.27% | -0.00% [-0.04%, 0.03%] | 2.97% [2.85%, 3.09%] | 1.82% | 2.91% | 0.06% [-0.01%, 0.13%] | 0.540 [0.527, 0.552] | 8.4% | 7.5% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.81% [3.72%, 3.91%] | 0.81% | 3.81% | -0.00% [-0.01%, 0.01%] | 1.86% [1.81%, 1.92%] | 1.11% | 1.85% | 0.02% [-0.01%, 0.04%] | 0.553 [0.544, 0.562] | 7.9% | 5.9% | 0.000% | 200 | 688896 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.63% [6.35%, 6.95%] | 1.81% | 6.84% | -0.21% [-0.43%, 0.00%] | 4.06% [3.92%, 4.20%] | 2.44% | 3.83% | 0.23% [-0.00%, 0.45%] | 0.550 [0.539, 0.562] | 7.5% | 8.2% | 0.001% | 200 | 79598 |
| R = 15, 40 decoys, bundling on | 5.12% [4.92%, 5.31%] | 1.35% | 5.27% | -0.15% [-0.31%, -0.01%] | 3.01% [2.91%, 3.12%] | 1.82% | 2.91% | 0.10% [-0.08%, 0.26%] | 0.536 [0.527, 0.546] | 5.4% | 5.4% | 0.003% | 200 | 104034 |
| R = 50, 40 decoys, bundling on | 3.62% [3.54%, 3.70%] | 0.83% | 3.81% | -0.19% [-0.26%, -0.12%] | 1.91% [1.87%, 1.96%] | 1.11% | 1.85% | 0.06% [-0.02%, 0.14%] | 0.542 [0.535, 0.548] | 2.8% | 3.8% | 0.000% | 200 | 344448 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.13% [5.76%, 6.48%] | 1.64% | 6.84% | -0.72% [-1.01%, -0.41%] | 2.61% [2.46%, 2.76%] | 2.44% | 3.83% | -1.22% [-1.46%, -1.00%] | 0.563 [0.547, 0.579] | 15.6% | 10.4% | 0.038% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 4.93% [4.69%, 5.16%] | 1.22% | 5.27% | -0.34% [-0.56%, -0.12%] | 1.91% [1.80%, 2.02%] | 1.82% | 2.91% | -1.00% [-1.19%, -0.81%] | 0.537 [0.523, 0.551] | 7.1% | 6.5% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.41% [3.31%, 3.51%] | 0.75% | 3.81% | -0.40% [-0.50%, -0.31%] | 1.23% [1.18%, 1.28%] | 1.11% | 1.85% | -0.62% [-0.71%, -0.53%] | 0.553 [0.544, 0.561] | 5.3% | 5.2% | 0.000% | 200 | 172224 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.81% [6.47%, 7.19%] | 1.76% | 6.84% | -0.04% [-0.12%, 0.05%] | 3.87% [3.74%, 3.99%] | 2.44% | 3.83% | 0.03% [-0.14%, 0.20%] | 0.546 [0.531, 0.561] | 12.1% | 10.2% | 0.013% | 200 | 119397 |
| R = 15, 40 decoys, bundling on | 5.25% [5.03%, 5.48%] | 1.31% | 5.27% | -0.02% [-0.08%, 0.05%] | 2.98% [2.89%, 3.07%] | 1.82% | 2.91% | 0.07% [-0.06%, 0.20%] | 0.543 [0.530, 0.555] | 8.3% | 7.5% | 0.000% | 200 | 156051 |
| R = 50, 40 decoys, bundling on | 3.78% [3.69%, 3.88%] | 0.81% | 3.81% | -0.03% [-0.06%, 0.00%] | 1.83% [1.78%, 1.87%] | 1.11% | 1.85% | -0.02% [-0.08%, 0.04%] | 0.554 [0.545, 0.562] | 7.8% | 5.8% | 0.000% | 200 | 516672 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R15_D40_B first_hop_cred (0.508), R50_D40_B first_hop_content (0.505).

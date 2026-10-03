# Tables

Record-to-device linking with genuine decoys, the r200 relay hold and a static content-server hold. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 15 | 40 | 2.65 | 7.0% | 18.7% | 25.7% | 20.1% | 7.1% | 215,400 |
| 50 | 40 | 4.31 | 1.4% | 5.8% | 7.2% | 5.9% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -1.52 [-1.91, -1.10] | -1.40 [-1.69, -1.12] | 38809 |
| Baseline | 15 | 40 | -1.37 [-1.78, -0.92] | -1.08 [-1.34, -0.83] | 35318 |
| Baseline | 50 | 40 | -0.74 [-0.93, -0.55] | -0.65 [-0.76, -0.53] | 117103 |
| First hop, credential | 1 | 40 | -1.49 [-1.84, -1.10] | -1.44 [-1.64, -1.25] | 155236 |
| First hop, credential | 15 | 40 | -1.32 [-1.75, -0.91] | -1.12 [-1.29, -0.96] | 141272 |
| First hop, credential | 50 | 40 | -0.73 [-0.91, -0.54] | -0.68 [-0.74, -0.62] | 468412 |
| First hop, content | 1 | 40 | -1.49 [-1.86, -1.13] | -1.44 [-1.64, -1.24] | 155236 |
| First hop, content | 15 | 40 | -1.32 [-1.73, -0.92] | -1.12 [-1.30, -0.96] | 141272 |
| First hop, content | 50 | 40 | -0.73 [-0.90, -0.55] | -0.68 [-0.74, -0.62] | 468412 |
| Credential processor | 1 | 40 | -1.57 [-1.97, -1.19] | -1.39 [-1.64, -1.13] | 155236 |
| Credential processor | 15 | 40 | -1.36 [-1.76, -0.94] | -1.12 [-1.34, -0.86] | 141272 |
| Credential processor | 50 | 40 | -0.73 [-0.92, -0.54] | -0.65 [-0.75, -0.56] | 468412 |
| Content server | 1 | 40 | -2.80 [-3.59, -1.98] | -2.49 [-3.21, -1.80] | 9118 |
| Content server | 15 | 40 | -2.51 [-3.30, -1.66] | -1.70 [-2.24, -1.18] | 8302 |
| Content server | 50 | 40 | -1.23 [-1.58, -0.88] | -1.29 [-1.53, -1.06] | 27609 |
| Validator | 1 | 40 | -4.13 [-4.59, -3.64] | -3.63 [-3.90, -3.36] | 38809 |
| Validator | 15 | 40 | -3.44 [-3.88, -2.97] | -2.65 [-2.90, -2.42] | 35318 |
| Validator | 50 | 40 | -2.27 [-2.45, -2.10] | -1.73 [-1.83, -1.63] | 117103 |
| Gatekeeper | 1 | 40 | -1.47 [-1.85, -1.08] | -1.37 [-1.58, -1.17] | 116427 |
| Gatekeeper | 15 | 40 | -1.36 [-1.79, -0.94] | -0.86 [-1.06, -0.68] | 105954 |
| Gatekeeper | 50 | 40 | -0.73 [-0.91, -0.54] | -0.65 [-0.72, -0.58] | 351309 |

## Change from the r200 build on the same records

Accuracy in this build minus accuracy in the r200 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.83 [+0.44, +1.21] | +0.75 [+0.52, +0.98] | 39045 |
| Baseline | 15 | 40 | +0.58 [+0.19, +0.96] | +0.16 [-0.05, +0.37] | 40975 |
| Baseline | 50 | 40 | +0.22 [+0.06, +0.37] | +0.24 [+0.16, +0.33] | 135945 |
| First hop, credential | 1 | 40 | +0.84 [+0.49, +1.20] | +0.58 [+0.43, +0.73] | 156180 |
| First hop, credential | 15 | 40 | +0.64 [+0.29, +1.00] | +0.34 [+0.22, +0.46] | 163900 |
| First hop, credential | 50 | 40 | +0.23 [+0.09, +0.36] | +0.23 [+0.18, +0.28] | 543780 |
| First hop, content | 1 | 40 | +0.84 [+0.48, +1.21] | +0.58 [+0.43, +0.74] | 156180 |
| First hop, content | 15 | 40 | +0.64 [+0.28, +1.02] | +0.34 [+0.22, +0.46] | 163900 |
| First hop, content | 50 | 40 | +0.23 [+0.10, +0.37] | +0.23 [+0.18, +0.28] | 543780 |
| Credential processor | 1 | 40 | +0.82 [+0.41, +1.23] | +0.66 [+0.43, +0.86] | 156180 |
| Credential processor | 15 | 40 | +0.56 [+0.17, +0.94] | +0.21 [+0.02, +0.41] | 163900 |
| Credential processor | 50 | 40 | +0.21 [+0.07, +0.37] | +0.25 [+0.18, +0.33] | 543780 |
| Content server | 1 | 40 | +0.13 [-0.62, +0.85] | -0.26 [-0.82, +0.28] | 9147 |
| Content server | 15 | 40 | +0.60 [+0.02, +1.24] | -0.01 [-0.52, +0.52] | 9558 |
| Content server | 50 | 40 | -0.02 [-0.31, +0.28] | +0.17 [-0.05, +0.38] | 32000 |
| Validator | 1 | 40 | -2.34 [-2.81, -1.89] | -2.46 [-2.67, -2.25] | 39045 |
| Validator | 15 | 40 | -1.93 [-2.35, -1.54] | -1.57 [-1.78, -1.38] | 40975 |
| Validator | 50 | 40 | -1.62 [-1.79, -1.45] | -1.13 [-1.22, -1.05] | 135945 |
| Gatekeeper | 1 | 40 | +0.78 [+0.40, +1.15] | +0.62 [+0.44, +0.80] | 117135 |
| Gatekeeper | 15 | 40 | +0.59 [+0.21, +0.97] | +0.38 [+0.21, +0.54] | 122925 |
| Gatekeeper | 50 | 40 | +0.21 [+0.06, +0.35] | +0.25 [+0.18, +0.32] | 407835 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.97% [6.61%, 7.31%] | 1.88% | 6.97% | 0.00% [0.00%, 0.00%] | 3.81% [3.63%, 3.99%] | 2.44% | 3.81% | 0.00% [0.00%, 0.00%] | 0.569 [0.554, 0.584] | 13.5% | 11.0% | 0.000% | 200 | 39921 |
| R = 15, 40 decoys, bundling on | 5.51% [5.23%, 5.79%] | 1.40% | 5.51% | 0.00% [0.00%, 0.00%] | 2.74% [2.61%, 2.88%] | 1.82% | 2.74% | 0.00% [0.00%, 0.00%] | 0.553 [0.541, 0.565] | 11.8% | 9.3% | 0.000% | 200 | 51794 |
| R = 50, 40 decoys, bundling on | 3.72% [3.62%, 3.82%] | 0.86% | 3.72% | 0.00% [0.00%, 0.00%] | 1.73% [1.67%, 1.79%] | 1.11% | 1.73% | 0.00% [0.00%, 0.00%] | 0.558 [0.551, 0.566] | 6.7% | 6.0% | 0.002% | 200 | 172702 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.98% [6.66%, 7.28%] | 1.88% | 6.97% | 0.01% [-0.08%, 0.10%] | 3.69% [3.58%, 3.81%] | 2.44% | 3.81% | -0.12% [-0.28%, 0.02%] | 0.568 [0.554, 0.581] | 13.8% | 10.8% | 0.000% | 200 | 159684 |
| R = 15, 40 decoys, bundling on | 5.54% [5.30%, 5.79%] | 1.40% | 5.51% | 0.03% [-0.04%, 0.10%] | 2.76% [2.68%, 2.84%] | 1.82% | 2.74% | 0.01% [-0.09%, 0.12%] | 0.554 [0.542, 0.565] | 12.6% | 9.2% | 0.000% | 200 | 207176 |
| R = 50, 40 decoys, bundling on | 3.74% [3.65%, 3.83%] | 0.86% | 3.72% | 0.02% [-0.01%, 0.05%] | 1.72% [1.69%, 1.75%] | 1.11% | 1.73% | -0.01% [-0.07%, 0.05%] | 0.559 [0.552, 0.565] | 6.7% | 5.9% | 0.000% | 200 | 690808 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.98% [6.65%, 7.28%] | 1.88% | 6.97% | 0.01% [-0.08%, 0.10%] | 3.69% [3.58%, 3.80%] | 2.44% | 3.81% | -0.12% [-0.27%, 0.03%] | 0.568 [0.554, 0.581] | 13.8% | 10.8% | 0.000% | 200 | 159684 |
| R = 15, 40 decoys, bundling on | 5.54% [5.30%, 5.78%] | 1.40% | 5.51% | 0.03% [-0.04%, 0.10%] | 2.76% [2.68%, 2.84%] | 1.82% | 2.74% | 0.01% [-0.09%, 0.12%] | 0.554 [0.542, 0.565] | 12.6% | 9.2% | 0.000% | 200 | 207176 |
| R = 50, 40 decoys, bundling on | 3.74% [3.66%, 3.82%] | 0.86% | 3.72% | 0.02% [-0.02%, 0.05%] | 1.72% [1.69%, 1.75%] | 1.11% | 1.73% | -0.01% [-0.07%, 0.05%] | 0.559 [0.552, 0.565] | 6.7% | 5.9% | 0.000% | 200 | 690808 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.97% [6.64%, 7.30%] | 1.88% | 6.97% | -0.00% [-0.05%, 0.05%] | 3.77% [3.62%, 3.93%] | 2.44% | 3.81% | -0.04% [-0.14%, 0.05%] | 0.568 [0.553, 0.583] | 13.7% | 11.0% | 0.000% | 200 | 159684 |
| R = 15, 40 decoys, bundling on | 5.49% [5.22%, 5.75%] | 1.40% | 5.51% | -0.02% [-0.05%, 0.00%] | 2.71% [2.60%, 2.84%] | 1.82% | 2.74% | -0.03% [-0.09%, 0.03%] | 0.555 [0.543, 0.567] | 12.0% | 9.4% | 0.000% | 200 | 207176 |
| R = 50, 40 decoys, bundling on | 3.72% [3.63%, 3.82%] | 0.86% | 3.72% | 0.00% [-0.01%, 0.01%] | 1.72% [1.67%, 1.77%] | 1.11% | 1.73% | -0.00% [-0.04%, 0.03%] | 0.558 [0.550, 0.565] | 6.7% | 5.9% | 0.002% | 200 | 690808 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.92% [6.66%, 7.19%] | 1.94% | 6.97% | -0.05% [-0.26%, 0.18%] | 4.06% [3.92%, 4.21%] | 2.44% | 3.81% | 0.25% [0.03%, 0.46%] | 0.566 [0.555, 0.577] | 8.9% | 9.6% | 0.000% | 200 | 79842 |
| R = 15, 40 decoys, bundling on | 5.48% [5.25%, 5.70%] | 1.44% | 5.51% | -0.03% [-0.19%, 0.12%] | 3.03% [2.92%, 3.13%] | 1.82% | 2.74% | 0.29% [0.12%, 0.45%] | 0.554 [0.544, 0.564] | 7.1% | 7.9% | 0.000% | 200 | 103588 |
| R = 50, 40 decoys, bundling on | 3.70% [3.62%, 3.78%] | 0.89% | 3.72% | -0.02% [-0.10%, 0.05%] | 1.85% [1.80%, 1.89%] | 1.11% | 1.73% | 0.12% [0.05%, 0.19%] | 0.550 [0.544, 0.556] | 4.1% | 4.6% | 0.000% | 200 | 345404 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.44% [5.08%, 5.78%] | 1.55% | 6.97% | -1.53% [-1.87%, -1.18%] | 1.76% [1.63%, 1.90%] | 2.44% | 3.81% | -2.05% [-2.28%, -1.83%] | 0.547 [0.530, 0.565] | 11.3% | 9.0% | 0.000% | 200 | 39921 |
| R = 15, 40 decoys, bundling on | 4.37% [4.11%, 4.63%] | 1.15% | 5.51% | -1.15% [-1.41%, -0.87%] | 1.38% [1.29%, 1.49%] | 1.82% | 2.74% | -1.36% [-1.52%, -1.19%] | 0.558 [0.541, 0.576] | 10.0% | 7.2% | 0.002% | 200 | 51794 |
| R = 50, 40 decoys, bundling on | 2.80% [2.70%, 2.90%] | 0.71% | 3.72% | -0.92% [-1.01%, -0.82%] | 0.79% [0.75%, 0.83%] | 1.11% | 1.73% | -0.94% [-1.01%, -0.87%] | 0.551 [0.541, 0.561] | 4.3% | 4.3% | 0.000% | 200 | 172702 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.98% [6.67%, 7.30%] | 1.88% | 6.97% | 0.01% [-0.08%, 0.10%] | 3.77% [3.65%, 3.89%] | 2.44% | 3.81% | -0.04% [-0.20%, 0.12%] | 0.567 [0.553, 0.581] | 12.7% | 10.4% | 0.000% | 200 | 119763 |
| R = 15, 40 decoys, bundling on | 5.51% [5.26%, 5.76%] | 1.40% | 5.51% | -0.00% [-0.07%, 0.07%] | 2.81% [2.71%, 2.90%] | 1.82% | 2.74% | 0.07% [-0.07%, 0.20%] | 0.556 [0.544, 0.568] | 12.4% | 9.3% | 0.000% | 200 | 155382 |
| R = 50, 40 decoys, bundling on | 3.73% [3.64%, 3.83%] | 0.86% | 3.72% | 0.01% [-0.03%, 0.04%] | 1.74% [1.70%, 1.78%] | 1.11% | 1.73% | 0.01% [-0.05%, 0.07%] | 0.559 [0.551, 0.566] | 6.6% | 5.9% | 0.001% | 200 | 518106 |

## Outcome-shuffle control (stable cells)

21 stable cells; 3 with a shuffled-outcome AUC interval excluding 0.5: R15_D40_B baseline (0.512), R50_D40_B first_hop_cred (0.504), R50_D40_B first_hop_content (0.505).

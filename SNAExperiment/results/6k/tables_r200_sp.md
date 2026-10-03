# Tables

Record-to-device linking with genuine decoys, the r200 relay hold, a static content-server hold, and the post-match lottery in the residual case. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 40 | -1.49 [-1.89, -1.06] | -1.40 [-1.71, -1.11] | 38809 |
| Baseline | 15 | 40 | -1.32 [-1.75, -0.87] | -1.06 [-1.32, -0.80] | 35318 |
| Baseline | 50 | 40 | -0.76 [-0.94, -0.57] | -0.65 [-0.77, -0.53] | 117103 |
| First hop, credential | 1 | 40 | -1.52 [-1.90, -1.13] | -1.43 [-1.63, -1.23] | 155236 |
| First hop, credential | 15 | 40 | -1.31 [-1.72, -0.89] | -1.16 [-1.32, -0.99] | 141272 |
| First hop, credential | 50 | 40 | -0.75 [-0.92, -0.57] | -0.68 [-0.74, -0.61] | 468412 |
| First hop, content | 1 | 40 | -1.52 [-1.90, -1.14] | -1.43 [-1.63, -1.23] | 155236 |
| First hop, content | 15 | 40 | -1.31 [-1.72, -0.89] | -1.16 [-1.33, -0.99] | 141272 |
| First hop, content | 50 | 40 | -0.75 [-0.92, -0.57] | -0.68 [-0.74, -0.61] | 468412 |
| Credential processor | 1 | 40 | -1.59 [-2.00, -1.20] | -1.35 [-1.61, -1.08] | 155236 |
| Credential processor | 15 | 40 | -1.33 [-1.75, -0.90] | -1.10 [-1.34, -0.86] | 141272 |
| Credential processor | 50 | 40 | -0.74 [-0.92, -0.55] | -0.67 [-0.78, -0.57] | 468412 |
| Content server | 1 | 40 | -2.64 [-3.45, -1.81] | -2.33 [-3.05, -1.63] | 9118 |
| Content server | 15 | 40 | -2.64 [-3.47, -1.81] | -1.73 [-2.25, -1.24] | 8302 |
| Content server | 50 | 40 | -1.28 [-1.61, -0.92] | -1.24 [-1.48, -0.99] | 27609 |
| Validator | 1 | 40 | -4.09 [-4.54, -3.58] | -3.59 [-3.86, -3.32] | 38809 |
| Validator | 15 | 40 | -3.41 [-3.83, -2.97] | -2.68 [-2.91, -2.44] | 35318 |
| Validator | 50 | 40 | -2.26 [-2.44, -2.06] | -1.71 [-1.81, -1.60] | 117103 |
| Gatekeeper | 1 | 40 | -1.51 [-1.91, -1.11] | -1.41 [-1.62, -1.21] | 116427 |
| Gatekeeper | 15 | 40 | -1.35 [-1.78, -0.91] | -0.88 [-1.07, -0.70] | 105954 |
| Gatekeeper | 50 | 40 | -0.74 [-0.93, -0.56] | -0.65 [-0.73, -0.57] | 351309 |

## Change from the r200_s build on the same records

Accuracy in this build minus accuracy in the r200_s build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.03 [-0.06, +0.11] | +0.01 [-0.13, +0.14] | 39921 |
| Baseline | 15 | 40 | +0.01 [-0.06, +0.08] | -0.01 [-0.12, +0.09] | 51794 |
| Baseline | 50 | 40 | -0.00 [-0.03, +0.03] | +0.01 [-0.04, +0.06] | 172702 |
| First hop, credential | 1 | 40 | -0.03 [-0.10, +0.03] | +0.02 [-0.06, +0.09] | 159684 |
| First hop, credential | 15 | 40 | -0.00 [-0.05, +0.04] | -0.04 [-0.09, +0.02] | 207176 |
| First hop, credential | 50 | 40 | -0.01 [-0.04, +0.01] | -0.00 [-0.03, +0.02] | 690808 |
| First hop, content | 1 | 40 | -0.03 [-0.10, +0.04] | +0.02 [-0.06, +0.09] | 159684 |
| First hop, content | 15 | 40 | -0.00 [-0.05, +0.04] | -0.04 [-0.09, +0.02] | 207176 |
| First hop, content | 50 | 40 | -0.01 [-0.04, +0.01] | -0.00 [-0.03, +0.02] | 690808 |
| Credential processor | 1 | 40 | -0.02 [-0.09, +0.06] | +0.03 [-0.08, +0.14] | 159684 |
| Credential processor | 15 | 40 | +0.02 [-0.04, +0.07] | -0.00 [-0.09, +0.08] | 207176 |
| Credential processor | 50 | 40 | +0.00 [-0.03, +0.03] | -0.00 [-0.04, +0.03] | 690808 |
| Content server | 1 | 40 | -0.03 [-0.12, +0.06] | -0.02 [-0.12, +0.09] | 79842 |
| Content server | 15 | 40 | +0.02 [-0.06, +0.10] | +0.02 [-0.07, +0.10] | 103588 |
| Content server | 50 | 40 | +0.00 [-0.03, +0.04] | -0.02 [-0.05, +0.02] | 345404 |
| Validator | 1 | 40 | +0.03 [-0.06, +0.11] | +0.04 [-0.05, +0.13] | 39921 |
| Validator | 15 | 40 | +0.05 [-0.02, +0.12] | -0.03 [-0.09, +0.04] | 51794 |
| Validator | 50 | 40 | +0.03 [+0.00, +0.06] | +0.02 [-0.01, +0.05] | 172702 |
| Gatekeeper | 1 | 40 | -0.03 [-0.10, +0.03] | -0.05 [-0.14, +0.03] | 119763 |
| Gatekeeper | 15 | 40 | -0.02 [-0.07, +0.03] | -0.01 [-0.08, +0.06] | 155382 |
| Gatekeeper | 50 | 40 | -0.01 [-0.03, +0.01] | -0.00 [-0.03, +0.02] | 518106 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.99% [6.64%, 7.34%] | 1.88% | 6.99% | 0.00% [0.00%, 0.00%] | 3.82% [3.62%, 4.00%] | 2.44% | 3.82% | 0.00% [0.00%, 0.00%] | 0.567 [0.552, 0.582] | 14.8% | 10.6% | 0.000% | 200 | 39921 |
| R = 15, 40 decoys, bundling on | 5.52% [5.23%, 5.80%] | 1.40% | 5.52% | 0.00% [0.00%, 0.00%] | 2.73% [2.60%, 2.88%] | 1.82% | 2.73% | 0.00% [0.00%, 0.00%] | 0.557 [0.545, 0.569] | 12.5% | 9.4% | 0.000% | 200 | 51794 |
| R = 50, 40 decoys, bundling on | 3.72% [3.62%, 3.82%] | 0.86% | 3.72% | 0.00% [0.00%, 0.00%] | 1.74% [1.68%, 1.79%] | 1.11% | 1.74% | 0.00% [0.00%, 0.00%] | 0.557 [0.549, 0.565] | 6.6% | 6.0% | 0.002% | 200 | 172702 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.95% [6.61%, 7.25%] | 1.88% | 6.99% | -0.05% [-0.13%, 0.04%] | 3.70% [3.60%, 3.82%] | 2.44% | 3.82% | -0.11% [-0.27%, 0.04%] | 0.568 [0.555, 0.582] | 14.1% | 10.7% | 0.000% | 200 | 159684 |
| R = 15, 40 decoys, bundling on | 5.54% [5.30%, 5.79%] | 1.40% | 5.52% | 0.02% [-0.05%, 0.09%] | 2.72% [2.64%, 2.80%] | 1.82% | 2.73% | -0.01% [-0.13%, 0.10%] | 0.554 [0.543, 0.565] | 12.7% | 9.1% | 0.000% | 200 | 207176 |
| R = 50, 40 decoys, bundling on | 3.72% [3.64%, 3.82%] | 0.86% | 3.72% | 0.00% [-0.03%, 0.03%] | 1.72% [1.68%, 1.75%] | 1.11% | 1.74% | -0.02% [-0.08%, 0.03%] | 0.559 [0.552, 0.566] | 6.5% | 5.9% | 0.000% | 200 | 690808 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.95% [6.62%, 7.25%] | 1.88% | 6.99% | -0.05% [-0.13%, 0.04%] | 3.70% [3.60%, 3.81%] | 2.44% | 3.82% | -0.11% [-0.27%, 0.04%] | 0.568 [0.555, 0.582] | 14.1% | 10.7% | 0.000% | 200 | 159684 |
| R = 15, 40 decoys, bundling on | 5.54% [5.28%, 5.78%] | 1.40% | 5.52% | 0.02% [-0.06%, 0.09%] | 2.72% [2.64%, 2.80%] | 1.82% | 2.73% | -0.01% [-0.12%, 0.10%] | 0.554 [0.543, 0.565] | 12.7% | 9.1% | 0.000% | 200 | 207176 |
| R = 50, 40 decoys, bundling on | 3.72% [3.64%, 3.81%] | 0.86% | 3.72% | 0.00% [-0.03%, 0.04%] | 1.72% [1.68%, 1.75%] | 1.11% | 1.74% | -0.02% [-0.08%, 0.03%] | 0.559 [0.552, 0.566] | 6.5% | 5.9% | 0.000% | 200 | 690808 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.95% [6.62%, 7.28%] | 1.88% | 6.99% | -0.04% [-0.08%, -0.00%] | 3.80% [3.63%, 3.97%] | 2.44% | 3.82% | -0.02% [-0.11%, 0.06%] | 0.569 [0.554, 0.584] | 14.2% | 10.6% | 0.000% | 200 | 159684 |
| R = 15, 40 decoys, bundling on | 5.51% [5.23%, 5.77%] | 1.40% | 5.52% | -0.01% [-0.05%, 0.02%] | 2.71% [2.60%, 2.83%] | 1.82% | 2.73% | -0.02% [-0.09%, 0.04%] | 0.557 [0.545, 0.569] | 12.3% | 9.2% | 0.000% | 200 | 207176 |
| R = 50, 40 decoys, bundling on | 3.72% [3.63%, 3.82%] | 0.86% | 3.72% | 0.00% [-0.01%, 0.01%] | 1.72% [1.67%, 1.77%] | 1.11% | 1.74% | -0.02% [-0.05%, 0.01%] | 0.557 [0.550, 0.565] | 6.6% | 5.9% | 0.003% | 200 | 690808 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.89% [6.62%, 7.16%] | 1.94% | 6.99% | -0.10% [-0.30%, 0.13%] | 4.05% [3.91%, 4.19%] | 2.44% | 3.82% | 0.23% [0.02%, 0.44%] | 0.566 [0.555, 0.577] | 8.9% | 9.3% | 0.001% | 200 | 79842 |
| R = 15, 40 decoys, bundling on | 5.50% [5.29%, 5.70%] | 1.45% | 5.52% | -0.02% [-0.19%, 0.14%] | 3.05% [2.93%, 3.16%] | 1.82% | 2.73% | 0.31% [0.14%, 0.49%] | 0.555 [0.545, 0.565] | 7.9% | 8.0% | 0.001% | 200 | 103588 |
| R = 50, 40 decoys, bundling on | 3.70% [3.62%, 3.78%] | 0.89% | 3.72% | -0.02% [-0.09%, 0.05%] | 1.83% [1.79%, 1.88%] | 1.11% | 1.74% | 0.09% [0.02%, 0.16%] | 0.551 [0.545, 0.558] | 4.3% | 4.5% | 0.000% | 200 | 345404 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.46% [5.10%, 5.81%] | 1.55% | 6.99% | -1.53% [-1.86%, -1.19%] | 1.80% [1.67%, 1.93%] | 2.44% | 3.82% | -2.01% [-2.24%, -1.81%] | 0.548 [0.531, 0.564] | 11.3% | 8.8% | 0.023% | 200 | 39921 |
| R = 15, 40 decoys, bundling on | 4.42% [4.17%, 4.68%] | 1.16% | 5.52% | -1.10% [-1.38%, -0.82%] | 1.36% [1.26%, 1.46%] | 1.82% | 2.73% | -1.37% [-1.55%, -1.21%] | 0.559 [0.542, 0.577] | 10.0% | 7.4% | 0.002% | 200 | 51794 |
| R = 50, 40 decoys, bundling on | 2.83% [2.73%, 2.93%] | 0.71% | 3.72% | -0.89% [-0.98%, -0.78%] | 0.81% [0.77%, 0.85%] | 1.11% | 1.74% | -0.93% [-1.00%, -0.86%] | 0.549 [0.540, 0.558] | 4.6% | 4.5% | 0.000% | 200 | 172702 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.95% [6.62%, 7.27%] | 1.88% | 6.99% | -0.05% [-0.13%, 0.04%] | 3.72% [3.59%, 3.85%] | 2.44% | 3.82% | -0.10% [-0.26%, 0.06%] | 0.567 [0.552, 0.581] | 13.4% | 10.3% | 0.000% | 200 | 119763 |
| R = 15, 40 decoys, bundling on | 5.49% [5.24%, 5.74%] | 1.40% | 5.52% | -0.03% [-0.10%, 0.04%] | 2.80% [2.71%, 2.89%] | 1.82% | 2.73% | 0.07% [-0.06%, 0.20%] | 0.556 [0.544, 0.567] | 12.3% | 9.2% | 0.000% | 200 | 155382 |
| R = 50, 40 decoys, bundling on | 3.72% [3.62%, 3.82%] | 0.86% | 3.72% | -0.00% [-0.03%, 0.03%] | 1.73% [1.69%, 1.78%] | 1.11% | 1.74% | -0.01% [-0.06%, 0.05%] | 0.559 [0.551, 0.566] | 6.7% | 5.9% | 0.002% | 200 | 518106 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R50_D40_B first_hop_cred (0.504), R50_D40_B first_hop_content (0.505).

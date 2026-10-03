# Tables

Record-to-device linking with genuine decoys, the rmix relay hold and a static content-server hold. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 1 | 40 | 1.97 | 14.0% | 27.5% | 41.5% | 31.9% | 14.0% | 2,501,674 |
| 15 | 40 | 2.65 | 7.1% | 18.8% | 25.9% | 20.2% | 7.1% | 215,400 |
| 50 | 40 | 4.31 | 1.4% | 5.8% | 7.2% | 5.9% | 1.4% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.26 [-0.15, +0.67] | +1.50 [+1.15, +1.84] | 38603 |
| Baseline | 15 | 40 | +0.45 [+0.04, +0.90] | +1.10 [+0.82, +1.39] | 33383 |
| Baseline | 50 | 40 | +0.39 [+0.21, +0.58] | +0.76 [+0.63, +0.89] | 110616 |
| First hop, credential | 1 | 40 | +0.31 [-0.10, +0.72] | +1.67 [+1.40, +1.93] | 154412 |
| First hop, credential | 15 | 40 | +0.39 [-0.02, +0.81] | +1.07 [+0.87, +1.27] | 133532 |
| First hop, credential | 50 | 40 | +0.39 [+0.21, +0.56] | +0.73 [+0.65, +0.80] | 442464 |
| First hop, content | 1 | 40 | +0.31 [-0.05, +0.69] | +1.67 [+1.41, +1.93] | 154412 |
| First hop, content | 15 | 40 | +0.39 [-0.05, +0.81] | +1.07 [+0.86, +1.27] | 133532 |
| First hop, content | 50 | 40 | +0.39 [+0.22, +0.56] | +0.73 [+0.65, +0.80] | 442464 |
| Credential processor | 1 | 40 | +0.18 [-0.23, +0.59] | +1.60 [+1.28, +1.91] | 154412 |
| Credential processor | 15 | 40 | +0.42 [-0.01, +0.86] | +1.12 [+0.87, +1.39] | 133532 |
| Credential processor | 50 | 40 | +0.41 [+0.23, +0.60] | +0.73 [+0.61, +0.84] | 442464 |
| Content server | 1 | 40 | +0.67 [-0.13, +1.55] | +1.73 [+0.94, +2.52] | 9128 |
| Content server | 15 | 40 | +0.66 [-0.20, +1.53] | +1.12 [+0.44, +1.82] | 7846 |
| Content server | 50 | 40 | +0.45 [+0.13, +0.79] | +0.59 [+0.27, +0.90] | 26105 |
| Validator | 1 | 40 | -3.53 [-3.98, -3.09] | -2.50 [-2.78, -2.21] | 38603 |
| Validator | 15 | 40 | -2.76 [-3.18, -2.34] | -1.90 [-2.16, -1.63] | 33383 |
| Validator | 50 | 40 | -1.75 [-1.92, -1.58] | -1.21 [-1.32, -1.11] | 110616 |
| Gatekeeper | 1 | 40 | +0.22 [-0.19, +0.60] | +1.48 [+1.21, +1.74] | 115809 |
| Gatekeeper | 15 | 40 | +0.39 [-0.03, +0.81] | +1.24 [+0.99, +1.49] | 100149 |
| Gatekeeper | 50 | 40 | +0.40 [+0.22, +0.59] | +0.69 [+0.60, +0.77] | 331848 |

## Change from the rmix build on the same records

Accuracy in this build minus accuracy in the rmix build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +2.04 [+1.65, +2.45] | +2.49 [+2.19, +2.80] | 39597 |
| Baseline | 15 | 40 | +1.67 [+1.37, +1.96] | +1.81 [+1.56, +2.06] | 50385 |
| Baseline | 50 | 40 | +1.17 [+1.04, +1.29] | +1.25 [+1.15, +1.34] | 167592 |
| First hop, credential | 1 | 40 | +2.10 [+1.75, +2.45] | +2.60 [+2.37, +2.84] | 158388 |
| First hop, credential | 15 | 40 | +1.66 [+1.40, +1.93] | +1.92 [+1.74, +2.09] | 201540 |
| First hop, credential | 50 | 40 | +1.19 [+1.08, +1.29] | +1.35 [+1.30, +1.41] | 670368 |
| First hop, content | 1 | 40 | +2.10 [+1.75, +2.45] | +2.60 [+2.37, +2.85] | 158388 |
| First hop, content | 15 | 40 | +1.66 [+1.41, +1.92] | +1.92 [+1.74, +2.08] | 201540 |
| First hop, content | 50 | 40 | +1.19 [+1.07, +1.29] | +1.35 [+1.30, +1.41] | 670368 |
| Credential processor | 1 | 40 | +2.04 [+1.65, +2.42] | +2.59 [+2.30, +2.87] | 158388 |
| Credential processor | 15 | 40 | +1.61 [+1.32, +1.90] | +1.90 [+1.68, +2.13] | 201540 |
| Credential processor | 50 | 40 | +1.17 [+1.05, +1.30] | +1.24 [+1.15, +1.33] | 670368 |
| Content server | 1 | 40 | +0.69 [-0.29, +1.64] | +1.24 [+0.38, +2.17] | 6207 |
| Content server | 15 | 40 | +1.20 [+0.48, +1.92] | +1.00 [+0.44, +1.60] | 11787 |
| Content server | 50 | 40 | +0.58 [+0.29, +0.88] | +0.40 [+0.14, +0.68] | 39306 |
| Validator | 1 | 40 | -2.44 [-2.89, -2.01] | -1.67 [-1.92, -1.41] | 39597 |
| Validator | 15 | 40 | -1.90 [-2.20, -1.58] | -1.26 [-1.46, -1.07] | 50385 |
| Validator | 50 | 40 | -1.18 [-1.31, -1.05] | -0.79 [-0.88, -0.70] | 167592 |
| Gatekeeper | 1 | 40 | +1.99 [+1.61, +2.37] | +2.36 [+2.12, +2.61] | 118791 |
| Gatekeeper | 15 | 40 | +1.67 [+1.41, +1.93] | +1.79 [+1.61, +1.99] | 151155 |
| Gatekeeper | 50 | 40 | +1.14 [+1.01, +1.26] | +1.18 [+1.10, +1.25] | 502776 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.70% [8.36%, 9.05%] | 1.56% | 8.70% | 0.00% [0.00%, 0.00%] | 6.64% [6.39%, 6.91%] | 2.44% | 6.64% | 0.00% [0.00%, 0.00%] | 0.564 [0.552, 0.577] | 19.3% | 14.5% | 0.000% | 200 | 39834 |
| R = 15, 40 decoys, bundling on | 7.21% [6.98%, 7.45%] | 1.16% | 7.21% | 0.00% [0.00%, 0.00%] | 4.92% [4.75%, 5.10%] | 1.82% | 4.92% | 0.00% [0.00%, 0.00%] | 0.565 [0.555, 0.575] | 16.4% | 13.1% | 0.014% | 200 | 51804 |
| R = 50, 40 decoys, bundling on | 4.89% [4.79%, 4.99%] | 0.71% | 4.89% | 0.00% [0.00%, 0.00%] | 3.15% [3.08%, 3.24%] | 1.11% | 3.15% | 0.00% [0.00%, 0.00%] | 0.563 [0.557, 0.569] | 9.9% | 7.7% | 0.000% | 200 | 172471 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.74% [8.42%, 9.06%] | 1.56% | 8.70% | 0.03% [-0.07%, 0.13%] | 6.74% [6.55%, 6.96%] | 2.44% | 6.64% | 0.11% [-0.01%, 0.23%] | 0.564 [0.553, 0.575] | 19.5% | 14.5% | 0.000% | 200 | 159336 |
| R = 15, 40 decoys, bundling on | 7.14% [6.93%, 7.36%] | 1.16% | 7.21% | -0.08% [-0.15%, -0.00%] | 4.99% [4.85%, 5.12%] | 1.82% | 4.92% | 0.06% [-0.05%, 0.16%] | 0.565 [0.556, 0.573] | 14.4% | 12.0% | 0.000% | 200 | 207216 |
| R = 50, 40 decoys, bundling on | 4.84% [4.76%, 4.93%] | 0.71% | 4.89% | -0.04% [-0.08%, -0.01%] | 3.17% [3.12%, 3.22%] | 1.11% | 3.15% | 0.02% [-0.04%, 0.07%] | 0.561 [0.555, 0.567] | 9.2% | 7.4% | 0.000% | 200 | 689884 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.74% [8.42%, 9.05%] | 1.56% | 8.70% | 0.03% [-0.06%, 0.14%] | 6.74% [6.54%, 6.94%] | 2.44% | 6.64% | 0.11% [-0.01%, 0.23%] | 0.564 [0.553, 0.575] | 19.5% | 14.5% | 0.000% | 200 | 159336 |
| R = 15, 40 decoys, bundling on | 7.14% [6.92%, 7.35%] | 1.16% | 7.21% | -0.08% [-0.15%, -0.00%] | 4.99% [4.85%, 5.12%] | 1.82% | 4.92% | 0.06% [-0.04%, 0.17%] | 0.565 [0.556, 0.573] | 14.4% | 12.0% | 0.000% | 200 | 207216 |
| R = 50, 40 decoys, bundling on | 4.84% [4.75%, 4.93%] | 0.71% | 4.89% | -0.04% [-0.08%, -0.01%] | 3.17% [3.12%, 3.22%] | 1.11% | 3.15% | 0.02% [-0.04%, 0.07%] | 0.561 [0.555, 0.567] | 9.2% | 7.4% | 0.000% | 200 | 689884 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.68% [8.34%, 9.03%] | 1.56% | 8.70% | -0.02% [-0.07%, 0.03%] | 6.68% [6.44%, 6.92%] | 2.44% | 6.64% | 0.04% [-0.05%, 0.13%] | 0.566 [0.554, 0.578] | 20.0% | 14.4% | 0.000% | 200 | 159336 |
| R = 15, 40 decoys, bundling on | 7.19% [6.95%, 7.44%] | 1.16% | 7.21% | -0.03% [-0.06%, 0.01%] | 4.95% [4.78%, 5.13%] | 1.82% | 4.92% | 0.03% [-0.04%, 0.10%] | 0.566 [0.556, 0.576] | 16.5% | 13.0% | 0.013% | 200 | 207216 |
| R = 50, 40 decoys, bundling on | 4.89% [4.79%, 4.99%] | 0.71% | 4.89% | 0.00% [-0.01%, 0.01%] | 3.14% [3.06%, 3.21%] | 1.11% | 3.15% | -0.02% [-0.04%, 0.01%] | 0.563 [0.557, 0.569] | 10.0% | 7.7% | 0.000% | 200 | 689884 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 10.37% [10.07%, 10.68%] | 1.58% | 8.70% | 1.67% [1.40%, 1.93%] | 8.19% [7.99%, 8.41%] | 2.44% | 6.64% | 1.56% [1.29%, 1.83%] | 0.579 [0.570, 0.588] | 16.2% | 16.3% | 0.000% | 200 | 79668 |
| R = 15, 40 decoys, bundling on | 8.39% [8.15%, 8.62%] | 1.18% | 7.21% | 1.17% [0.98%, 1.37%] | 6.12% [5.97%, 6.28%] | 1.82% | 4.92% | 1.20% [0.99%, 1.42%] | 0.579 [0.570, 0.587] | 10.2% | 13.0% | 0.000% | 200 | 103608 |
| R = 50, 40 decoys, bundling on | 5.70% [5.61%, 5.78%] | 0.72% | 4.89% | 0.81% [0.73%, 0.89%] | 3.79% [3.72%, 3.86%] | 1.11% | 3.15% | 0.63% [0.55%, 0.72%] | 0.576 [0.571, 0.581] | 6.1% | 8.3% | 0.000% | 200 | 344942 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.00% [5.65%, 6.34%] | 1.40% | 8.70% | -2.70% [-3.06%, -2.35%] | 2.89% [2.73%, 3.06%] | 2.44% | 6.64% | -3.75% [-4.06%, -3.46%] | 0.561 [0.545, 0.577] | 11.6% | 10.3% | 0.000% | 200 | 39834 |
| R = 15, 40 decoys, bundling on | 4.88% [4.66%, 5.13%] | 1.04% | 7.21% | -2.33% [-2.55%, -2.12%] | 2.21% [2.09%, 2.33%] | 1.82% | 4.92% | -2.71% [-2.92%, -2.51%] | 0.558 [0.544, 0.572] | 9.8% | 8.3% | 0.000% | 200 | 51804 |
| R = 50, 40 decoys, bundling on | 3.36% [3.27%, 3.45%] | 0.64% | 4.89% | -1.53% [-1.63%, -1.43%] | 1.31% [1.25%, 1.37%] | 1.11% | 3.15% | -1.84% [-1.93%, -1.75%] | 0.550 [0.542, 0.558] | 6.2% | 5.1% | 0.000% | 200 | 172471 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.65% [8.33%, 8.96%] | 1.56% | 8.70% | -0.06% [-0.17%, 0.05%] | 6.55% [6.35%, 6.74%] | 2.44% | 6.64% | -0.08% [-0.27%, 0.10%] | 0.563 [0.551, 0.575] | 20.3% | 14.9% | 0.000% | 200 | 119502 |
| R = 15, 40 decoys, bundling on | 7.19% [6.95%, 7.42%] | 1.16% | 7.21% | -0.03% [-0.11%, 0.06%] | 4.91% [4.76%, 5.07%] | 1.82% | 4.92% | -0.01% [-0.16%, 0.13%] | 0.565 [0.555, 0.575] | 16.2% | 12.7% | 0.016% | 200 | 155412 |
| R = 50, 40 decoys, bundling on | 4.85% [4.76%, 4.95%] | 0.71% | 4.89% | -0.04% [-0.07%, -0.01%] | 3.05% [2.99%, 3.11%] | 1.11% | 3.15% | -0.11% [-0.17%, -0.04%] | 0.565 [0.559, 0.571] | 10.2% | 7.8% | 0.000% | 200 | 517413 |

## Outcome-shuffle control (stable cells)

21 stable cells; 3 with a shuffled-outcome AUC interval excluding 0.5: R15_D40_B first_hop_cred (0.506), R15_D40_B validator (0.518), R50_D40_B gatekeeper (0.506).

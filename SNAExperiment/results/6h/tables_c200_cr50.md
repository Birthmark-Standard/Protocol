# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the content paths' device and relay-hop holds stretched 2 times and the credential path's shortened to 0.5 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 50 | 40 | 4.30 | 1.4% | 5.8% | 7.2% | 5.9% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -1.79 [-2.19, -1.37] | -1.29 [-1.58, -1.00] | 39392 |
| Baseline | 15 | 40 | -1.64 [-2.00, -1.29] | -0.95 [-1.18, -0.73] | 46360 |
| Baseline | 50 | 40 | -0.78 [-0.94, -0.64] | -0.64 [-0.74, -0.54] | 153382 |
| First hop, credential | 1 | 40 | -1.77 [-2.17, -1.40] | -1.27 [-1.48, -1.06] | 157568 |
| First hop, credential | 15 | 40 | -1.64 [-1.97, -1.32] | -1.08 [-1.23, -0.94] | 185440 |
| First hop, credential | 50 | 40 | -0.78 [-0.91, -0.64] | -0.68 [-0.74, -0.63] | 613528 |
| First hop, content | 1 | 40 | -1.77 [-2.14, -1.38] | -1.27 [-1.48, -1.07] | 157568 |
| First hop, content | 15 | 40 | -1.64 [-1.96, -1.30] | -1.08 [-1.23, -0.94] | 185440 |
| First hop, content | 50 | 40 | -0.78 [-0.91, -0.64] | -0.68 [-0.74, -0.63] | 613528 |
| Credential processor | 1 | 40 | -1.84 [-2.24, -1.42] | -1.17 [-1.42, -0.92] | 157568 |
| Credential processor | 15 | 40 | -1.60 [-1.97, -1.25] | -1.00 [-1.19, -0.81] | 185440 |
| Credential processor | 50 | 40 | -0.78 [-0.92, -0.63] | -0.67 [-0.75, -0.59] | 613528 |
| Content server | 1 | 40 | -3.18 [-4.03, -2.30] | -2.63 [-3.34, -1.90] | 8187 |
| Content server | 15 | 40 | -2.87 [-3.48, -2.26] | -1.68 [-2.15, -1.19] | 10968 |
| Content server | 50 | 40 | -1.55 [-1.86, -1.23] | -1.06 [-1.30, -0.84] | 36109 |
| Validator | 1 | 40 | -3.40 [-3.84, -2.95] | -2.79 [-3.06, -2.54] | 39392 |
| Validator | 15 | 40 | -2.90 [-3.27, -2.54] | -2.04 [-2.24, -1.83] | 46360 |
| Validator | 50 | 40 | -1.67 [-1.83, -1.52] | -1.26 [-1.35, -1.16] | 153382 |
| Gatekeeper | 1 | 40 | -1.79 [-2.18, -1.39] | -1.38 [-1.60, -1.17] | 118176 |
| Gatekeeper | 15 | 40 | -1.64 [-1.99, -1.30] | -1.00 [-1.15, -0.85] | 139080 |
| Gatekeeper | 50 | 40 | -0.77 [-0.92, -0.62] | -0.63 [-0.69, -0.56] | 460146 |

## Change from the content200 build on the same records

Accuracy in this build minus accuracy in the content200 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -0.18 [-0.36, +0.01] | -0.11 [-0.38, +0.17] | 39799 |
| Baseline | 15 | 40 | -0.09 [-0.25, +0.07] | -0.10 [-0.29, +0.09] | 52017 |
| Baseline | 50 | 40 | -0.13 [-0.21, -0.06] | -0.17 [-0.25, -0.09] | 172224 |
| First hop, credential | 1 | 40 | -0.18 [-0.32, -0.03] | -0.14 [-0.30, +0.02] | 159196 |
| First hop, credential | 15 | 40 | -0.16 [-0.29, -0.03] | -0.22 [-0.32, -0.12] | 208068 |
| First hop, credential | 50 | 40 | -0.14 [-0.19, -0.08] | -0.18 [-0.23, -0.13] | 688896 |
| First hop, content | 1 | 40 | -0.18 [-0.32, -0.03] | -0.14 [-0.30, +0.03] | 159196 |
| First hop, content | 15 | 40 | -0.16 [-0.29, -0.03] | -0.22 [-0.32, -0.12] | 208068 |
| First hop, content | 50 | 40 | -0.14 [-0.20, -0.08] | -0.18 [-0.23, -0.13] | 688896 |
| Credential processor | 1 | 40 | -0.14 [-0.32, +0.04] | -0.01 [-0.23, +0.21] | 159196 |
| Credential processor | 15 | 40 | -0.10 [-0.25, +0.05] | -0.17 [-0.33, -0.01] | 208068 |
| Credential processor | 50 | 40 | -0.14 [-0.21, -0.06] | -0.19 [-0.26, -0.12] | 688896 |
| Content server | 1 | 40 | -0.21 [-0.39, -0.03] | -0.47 [-0.67, -0.27] | 79598 |
| Content server | 15 | 40 | -0.32 [-0.46, -0.19] | -0.29 [-0.42, -0.15] | 104034 |
| Content server | 50 | 40 | -0.17 [-0.23, -0.10] | -0.11 [-0.17, -0.05] | 344448 |
| Validator | 1 | 40 | -0.23 [-0.46, -0.01] | -0.32 [-0.52, -0.11] | 39799 |
| Validator | 15 | 40 | -0.20 [-0.37, -0.02] | -0.09 [-0.24, +0.06] | 52017 |
| Validator | 50 | 40 | -0.13 [-0.21, -0.06] | -0.09 [-0.16, -0.01] | 172224 |
| Gatekeeper | 1 | 40 | -0.21 [-0.38, -0.04] | -0.24 [-0.43, -0.05] | 119397 |
| Gatekeeper | 15 | 40 | -0.13 [-0.27, +0.01] | -0.25 [-0.39, -0.11] | 156051 |
| Gatekeeper | 50 | 40 | -0.14 [-0.20, -0.08] | -0.15 [-0.21, -0.10] | 516672 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.64% [6.26%, 7.00%] | 1.76% | 6.64% | 0.00% [0.00%, 0.00%] | 3.92% [3.73%, 4.12%] | 2.44% | 3.92% | 0.00% [0.00%, 0.00%] | 0.548 [0.532, 0.564] | 10.3% | 10.7% | 0.000% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.15% [4.91%, 5.39%] | 1.31% | 5.15% | 0.00% [0.00%, 0.00%] | 2.85% [2.72%, 2.98%] | 1.82% | 2.85% | 0.00% [0.00%, 0.00%] | 0.546 [0.533, 0.559] | 8.5% | 7.3% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.68% [3.59%, 3.77%] | 0.80% | 3.68% | 0.00% [0.00%, 0.00%] | 1.73% [1.68%, 1.79%] | 1.11% | 1.73% | 0.00% [0.00%, 0.00%] | 0.555 [0.547, 0.564] | 7.3% | 5.6% | 0.000% | 200 | 172224 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.64% [6.31%, 6.98%] | 1.76% | 6.64% | 0.01% [-0.08%, 0.09%] | 3.88% [3.76%, 4.01%] | 2.44% | 3.92% | -0.04% [-0.18%, 0.10%] | 0.551 [0.537, 0.565] | 10.4% | 10.6% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.13% [4.90%, 5.35%] | 1.31% | 5.15% | -0.03% [-0.10%, 0.04%] | 2.75% [2.68%, 2.84%] | 1.82% | 2.85% | -0.09% [-0.22%, 0.02%] | 0.547 [0.535, 0.559] | 8.4% | 7.0% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.67% [3.59%, 3.76%] | 0.80% | 3.68% | -0.02% [-0.05%, 0.02%] | 1.73% [1.70%, 1.76%] | 1.11% | 1.73% | -0.00% [-0.06%, 0.06%] | 0.555 [0.547, 0.563] | 7.1% | 5.7% | 0.000% | 200 | 688896 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.64% [6.31%, 7.00%] | 1.76% | 6.64% | 0.01% [-0.08%, 0.09%] | 3.88% [3.76%, 4.00%] | 2.44% | 3.92% | -0.04% [-0.19%, 0.11%] | 0.551 [0.537, 0.565] | 10.4% | 10.6% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.13% [4.91%, 5.34%] | 1.31% | 5.15% | -0.03% [-0.10%, 0.04%] | 2.75% [2.68%, 2.83%] | 1.82% | 2.85% | -0.09% [-0.22%, 0.02%] | 0.547 [0.535, 0.559] | 8.4% | 7.0% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.67% [3.58%, 3.76%] | 0.80% | 3.68% | -0.02% [-0.05%, 0.02%] | 1.73% [1.70%, 1.76%] | 1.11% | 1.73% | -0.00% [-0.06%, 0.05%] | 0.555 [0.547, 0.563] | 7.1% | 5.7% | 0.000% | 200 | 688896 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.64% [6.29%, 6.97%] | 1.76% | 6.64% | 0.00% [-0.05%, 0.05%] | 3.99% [3.83%, 4.16%] | 2.44% | 3.92% | 0.06% [-0.03%, 0.15%] | 0.546 [0.530, 0.561] | 10.4% | 10.6% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.17% [4.92%, 5.41%] | 1.31% | 5.15% | 0.01% [-0.02%, 0.04%] | 2.83% [2.73%, 2.96%] | 1.82% | 2.85% | -0.02% [-0.09%, 0.05%] | 0.545 [0.532, 0.558] | 8.2% | 7.3% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.68% [3.59%, 3.77%] | 0.80% | 3.68% | -0.01% [-0.02%, 0.01%] | 1.71% [1.66%, 1.76%] | 1.11% | 1.73% | -0.02% [-0.05%, 0.00%] | 0.555 [0.547, 0.564] | 7.3% | 5.7% | 0.000% | 200 | 688896 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.43% [6.15%, 6.74%] | 1.81% | 6.64% | -0.20% [-0.41%, 0.00%] | 3.82% [3.69%, 3.97%] | 2.44% | 3.92% | -0.10% [-0.33%, 0.14%] | 0.541 [0.529, 0.552] | 6.7% | 7.5% | 0.000% | 200 | 79598 |
| R = 15, 40 decoys, bundling on | 4.94% [4.74%, 5.13%] | 1.34% | 5.15% | -0.22% [-0.37%, -0.07%] | 2.91% [2.81%, 3.02%] | 1.82% | 2.85% | 0.06% [-0.10%, 0.22%] | 0.538 [0.529, 0.547] | 4.7% | 5.2% | 0.000% | 200 | 104034 |
| R = 50, 40 decoys, bundling on | 3.54% [3.46%, 3.62%] | 0.83% | 3.68% | -0.14% [-0.22%, -0.08%] | 1.83% [1.79%, 1.87%] | 1.11% | 1.73% | 0.10% [0.03%, 0.17%] | 0.538 [0.532, 0.544] | 2.8% | 3.8% | 0.000% | 200 | 344448 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.13% [5.75%, 6.51%] | 1.62% | 6.64% | -0.51% [-0.77%, -0.25%] | 2.63% [2.48%, 2.78%] | 2.44% | 3.92% | -1.29% [-1.54%, -1.06%] | 0.565 [0.549, 0.581] | 13.3% | 10.2% | 0.018% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 4.93% [4.68%, 5.17%] | 1.21% | 5.15% | -0.23% [-0.41%, -0.03%] | 2.00% [1.88%, 2.12%] | 1.82% | 2.85% | -0.85% [-1.03%, -0.67%] | 0.532 [0.518, 0.547] | 7.5% | 6.0% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.37% [3.27%, 3.47%] | 0.74% | 3.68% | -0.31% [-0.39%, -0.22%] | 1.21% [1.16%, 1.26%] | 1.11% | 1.73% | -0.52% [-0.60%, -0.44%] | 0.550 [0.541, 0.559] | 5.9% | 5.2% | 0.000% | 200 | 172224 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.60% [6.25%, 6.94%] | 1.76% | 6.64% | -0.04% [-0.13%, 0.05%] | 3.77% [3.63%, 3.90%] | 2.44% | 3.92% | -0.15% [-0.32%, 0.02%] | 0.550 [0.535, 0.565] | 10.2% | 10.4% | 0.000% | 200 | 119397 |
| R = 15, 40 decoys, bundling on | 5.14% [4.91%, 5.37%] | 1.31% | 5.15% | -0.01% [-0.07%, 0.05%] | 2.78% [2.68%, 2.89%] | 1.82% | 2.85% | -0.07% [-0.19%, 0.06%] | 0.547 [0.535, 0.560] | 7.6% | 7.2% | 0.000% | 200 | 156051 |
| R = 50, 40 decoys, bundling on | 3.67% [3.57%, 3.76%] | 0.80% | 3.68% | -0.02% [-0.05%, 0.02%] | 1.75% [1.71%, 1.79%] | 1.11% | 1.73% | 0.02% [-0.04%, 0.08%] | 0.556 [0.548, 0.564] | 7.4% | 5.8% | 0.000% | 200 | 516672 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R15_D40_B first_hop_cred (0.506), R50_D40_B gatekeeper (0.505).

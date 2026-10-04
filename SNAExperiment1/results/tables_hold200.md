# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with every device and relay-hop hold stretched 2 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 15 | 40 | 2.65 | 7.0% | 18.7% | 25.7% | 20.1% | 7.0% | 215,400 |
| 50 | 40 | 4.30 | 1.4% | 5.8% | 7.2% | 5.9% | 1.4% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -2.46 [-2.88, -2.05] | -2.07 [-2.34, -1.81] | 39384 |
| Baseline | 15 | 40 | -1.89 [-2.30, -1.48] | -1.30 [-1.52, -1.08] | 46349 |
| Baseline | 50 | 40 | -1.12 [-1.26, -0.97] | -0.82 [-0.91, -0.73] | 153346 |
| First hop, credential | 1 | 40 | -2.37 [-2.76, -1.99] | -1.97 [-2.16, -1.79] | 157536 |
| First hop, credential | 15 | 40 | -1.96 [-2.32, -1.60] | -1.39 [-1.54, -1.26] | 185396 |
| First hop, credential | 50 | 40 | -1.12 [-1.25, -0.99] | -0.89 [-0.94, -0.83] | 613384 |
| First hop, content | 1 | 40 | -2.37 [-2.74, -1.98] | -1.97 [-2.15, -1.80] | 157536 |
| First hop, content | 15 | 40 | -1.96 [-2.32, -1.60] | -1.39 [-1.53, -1.26] | 185396 |
| First hop, content | 50 | 40 | -1.12 [-1.25, -0.99] | -0.89 [-0.94, -0.84] | 613384 |
| Credential processor | 1 | 40 | -2.54 [-2.95, -2.11] | -1.96 [-2.20, -1.72] | 157536 |
| Credential processor | 15 | 40 | -1.87 [-2.28, -1.48] | -1.30 [-1.49, -1.11] | 185396 |
| Credential processor | 50 | 40 | -1.11 [-1.25, -0.98] | -0.83 [-0.91, -0.74] | 613384 |
| Content server | 1 | 40 | -3.21 [-4.05, -2.35] | -2.69 [-3.30, -2.02] | 8185 |
| Content server | 15 | 40 | -3.50 [-4.13, -2.87] | -1.81 [-2.27, -1.34] | 10966 |
| Content server | 50 | 40 | -1.81 [-2.13, -1.48] | -1.07 [-1.31, -0.86] | 36100 |
| Validator | 1 | 40 | -1.92 [-2.38, -1.43] | -1.58 [-1.89, -1.27] | 39384 |
| Validator | 15 | 40 | -1.98 [-2.35, -1.60] | -1.18 [-1.41, -0.94] | 46349 |
| Validator | 50 | 40 | -0.97 [-1.13, -0.82] | -0.72 [-0.82, -0.63] | 153346 |
| Gatekeeper | 1 | 40 | -2.40 [-2.79, -2.01] | -1.89 [-2.08, -1.70] | 118152 |
| Gatekeeper | 15 | 40 | -1.96 [-2.34, -1.60] | -1.28 [-1.45, -1.11] | 139047 |
| Gatekeeper | 50 | 40 | -1.10 [-1.24, -0.96] | -0.84 [-0.90, -0.78] | 460038 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.98% [5.60%, 6.34%] | 1.59% | 5.98% | 0.00% [0.00%, 0.00%] | 3.14% [2.97%, 3.33%] | 2.44% | 3.14% | 0.00% [0.00%, 0.00%] | 0.560 [0.544, 0.576] | 12.6% | 9.3% | 0.000% | 200 | 39790 |
| R = 15, 40 decoys, bundling on | 4.92% [4.68%, 5.18%] | 1.19% | 4.92% | 0.00% [0.00%, 0.00%] | 2.40% [2.27%, 2.54%] | 1.82% | 2.40% | 0.00% [0.00%, 0.00%] | 0.538 [0.524, 0.553] | 7.1% | 6.2% | 0.000% | 200 | 52005 |
| R = 50, 40 decoys, bundling on | 3.38% [3.29%, 3.46%] | 0.73% | 3.38% | 0.00% [0.00%, 0.00%] | 1.54% [1.48%, 1.60%] | 1.11% | 1.54% | 0.00% [0.00%, 0.00%] | 0.548 [0.540, 0.557] | 5.7% | 4.9% | 0.000% | 200 | 172186 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.06% [5.72%, 6.38%] | 1.59% | 5.98% | 0.08% [-0.01%, 0.17%] | 3.16% [3.05%, 3.27%] | 2.44% | 3.14% | 0.01% [-0.14%, 0.16%] | 0.557 [0.542, 0.571] | 12.1% | 9.6% | 0.000% | 200 | 159160 |
| R = 15, 40 decoys, bundling on | 4.84% [4.61%, 5.08%] | 1.19% | 4.92% | -0.08% [-0.15%, -0.01%] | 2.41% [2.34%, 2.49%] | 1.82% | 2.40% | 0.01% [-0.11%, 0.13%] | 0.541 [0.528, 0.554] | 6.9% | 6.3% | 0.000% | 200 | 208020 |
| R = 50, 40 decoys, bundling on | 3.35% [3.26%, 3.43%] | 0.73% | 3.38% | -0.03% [-0.06%, 0.00%] | 1.52% [1.49%, 1.54%] | 1.11% | 1.54% | -0.03% [-0.08%, 0.03%] | 0.548 [0.540, 0.556] | 5.7% | 4.9% | 0.000% | 200 | 688744 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.06% [5.73%, 6.38%] | 1.59% | 5.98% | 0.08% [-0.01%, 0.17%] | 3.16% [3.05%, 3.27%] | 2.44% | 3.14% | 0.01% [-0.13%, 0.16%] | 0.557 [0.542, 0.571] | 12.1% | 9.6% | 0.000% | 200 | 159160 |
| R = 15, 40 decoys, bundling on | 4.84% [4.62%, 5.07%] | 1.19% | 4.92% | -0.08% [-0.15%, -0.01%] | 2.41% [2.34%, 2.49%] | 1.82% | 2.40% | 0.01% [-0.10%, 0.13%] | 0.541 [0.528, 0.554] | 6.9% | 6.3% | 0.000% | 200 | 208020 |
| R = 50, 40 decoys, bundling on | 3.35% [3.26%, 3.42%] | 0.73% | 3.38% | -0.03% [-0.06%, 0.00%] | 1.52% [1.49%, 1.55%] | 1.11% | 1.54% | -0.03% [-0.08%, 0.03%] | 0.548 [0.540, 0.556] | 5.7% | 4.9% | 0.000% | 200 | 688744 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 5.94% [5.60%, 6.30%] | 1.59% | 5.98% | -0.03% [-0.07%, 0.01%] | 3.19% [3.04%, 3.34%] | 2.44% | 3.14% | 0.05% [-0.04%, 0.13%] | 0.560 [0.544, 0.576] | 11.9% | 9.5% | 0.000% | 200 | 159160 |
| R = 15, 40 decoys, bundling on | 4.93% [4.68%, 5.19%] | 1.19% | 4.92% | 0.01% [-0.02%, 0.05%] | 2.45% [2.34%, 2.57%] | 1.82% | 2.40% | 0.05% [-0.01%, 0.10%] | 0.538 [0.524, 0.553] | 7.5% | 6.2% | 0.000% | 200 | 208020 |
| R = 50, 40 decoys, bundling on | 3.37% [3.28%, 3.45%] | 0.73% | 3.38% | -0.01% [-0.02%, 0.00%] | 1.55% [1.50%, 1.60%] | 1.11% | 1.54% | 0.01% [-0.02%, 0.04%] | 0.549 [0.540, 0.558] | 5.6% | 4.9% | 0.000% | 200 | 688744 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.06% [5.77%, 6.35%] | 1.71% | 5.98% | 0.08% [-0.14%, 0.31%] | 3.70% [3.58%, 3.83%] | 2.44% | 3.14% | 0.56% [0.34%, 0.78%] | 0.544 [0.534, 0.555] | 5.5% | 7.3% | 0.000% | 200 | 79580 |
| R = 15, 40 decoys, bundling on | 4.74% [4.55%, 4.94%] | 1.27% | 4.92% | -0.18% [-0.37%, -0.00%] | 2.76% [2.65%, 2.86%] | 1.82% | 2.40% | 0.35% [0.19%, 0.51%] | 0.529 [0.519, 0.538] | 3.8% | 4.3% | 0.000% | 200 | 104010 |
| R = 50, 40 decoys, bundling on | 3.31% [3.24%, 3.38%] | 0.78% | 3.38% | -0.06% [-0.14%, 0.02%] | 1.73% [1.69%, 1.77%] | 1.11% | 1.54% | 0.19% [0.12%, 0.26%] | 0.530 [0.524, 0.536] | 2.4% | 3.0% | 0.000% | 200 | 344372 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.61% [7.26%, 7.95%] | 1.69% | 5.98% | 1.63% [1.28%, 2.00%] | 3.83% [3.63%, 4.03%] | 2.44% | 3.14% | 0.69% [0.42%, 0.94%] | 0.560 [0.545, 0.575] | 18.1% | 13.2% | 0.018% | 200 | 39790 |
| R = 15, 40 decoys, bundling on | 5.92% [5.66%, 6.16%] | 1.26% | 4.92% | 0.99% [0.72%, 1.27%] | 2.83% [2.69%, 2.97%] | 1.82% | 2.40% | 0.42% [0.22%, 0.63%] | 0.543 [0.531, 0.555] | 10.0% | 8.4% | 0.000% | 200 | 52005 |
| R = 50, 40 decoys, bundling on | 4.09% [3.99%, 4.20%] | 0.77% | 3.38% | 0.71% [0.59%, 0.83%] | 1.75% [1.69%, 1.82%] | 1.11% | 1.54% | 0.21% [0.13%, 0.30%] | 0.552 [0.545, 0.560] | 7.2% | 6.3% | 0.000% | 200 | 172186 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.00% [5.66%, 6.37%] | 1.59% | 5.98% | 0.03% [-0.07%, 0.13%] | 3.25% [3.14%, 3.36%] | 2.44% | 3.14% | 0.10% [-0.09%, 0.28%] | 0.556 [0.540, 0.571] | 12.4% | 9.5% | 0.000% | 200 | 119370 |
| R = 15, 40 decoys, bundling on | 4.86% [4.61%, 5.11%] | 1.19% | 4.92% | -0.06% [-0.13%, 0.01%] | 2.43% [2.34%, 2.53%] | 1.82% | 2.40% | 0.03% [-0.09%, 0.15%] | 0.540 [0.526, 0.554] | 6.8% | 5.9% | 0.002% | 200 | 156015 |
| R = 50, 40 decoys, bundling on | 3.34% [3.25%, 3.43%] | 0.73% | 3.38% | -0.03% [-0.06%, -0.00%] | 1.54% [1.50%, 1.57%] | 1.11% | 1.54% | -0.01% [-0.06%, 0.05%] | 0.550 [0.541, 0.558] | 5.6% | 4.9% | 0.000% | 200 | 516558 |

## Outcome-shuffle control (stable cells)

21 stable cells; 0 with a shuffled-outcome AUC interval excluding 0.5.

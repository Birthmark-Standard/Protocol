# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the device and relay-hop holds on both content paths stretched 2 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 40 | -1.62 [-2.05, -1.17] | -1.18 [-1.49, -0.89] | 39392 |
| Baseline | 15 | 40 | -1.56 [-1.91, -1.22] | -0.80 [-1.03, -0.58] | 46360 |
| Baseline | 50 | 40 | -0.64 [-0.80, -0.50] | -0.47 [-0.57, -0.37] | 153382 |
| First hop, credential | 1 | 40 | -1.60 [-2.00, -1.21] | -1.13 [-1.32, -0.95] | 157568 |
| First hop, credential | 15 | 40 | -1.52 [-1.85, -1.18] | -0.87 [-1.02, -0.72] | 185440 |
| First hop, credential | 50 | 40 | -0.63 [-0.77, -0.49] | -0.49 [-0.56, -0.43] | 613528 |
| First hop, content | 1 | 40 | -1.60 [-1.99, -1.17] | -1.13 [-1.32, -0.93] | 157568 |
| First hop, content | 15 | 40 | -1.52 [-1.85, -1.19] | -0.87 [-1.02, -0.72] | 185440 |
| First hop, content | 50 | 40 | -0.63 [-0.77, -0.49] | -0.49 [-0.56, -0.43] | 613528 |
| Credential processor | 1 | 40 | -1.70 [-2.12, -1.27] | -1.16 [-1.41, -0.91] | 157568 |
| Credential processor | 15 | 40 | -1.53 [-1.89, -1.19] | -0.80 [-1.01, -0.60] | 185440 |
| Credential processor | 50 | 40 | -0.63 [-0.78, -0.48] | -0.50 [-0.58, -0.41] | 613528 |
| Content server | 1 | 40 | -3.00 [-3.85, -2.13] | -2.52 [-3.20, -1.76] | 8187 |
| Content server | 15 | 40 | -2.67 [-3.32, -2.02] | -1.29 [-1.76, -0.81] | 10968 |
| Content server | 50 | 40 | -1.57 [-1.88, -1.27] | -0.99 [-1.23, -0.76] | 36109 |
| Validator | 1 | 40 | -3.17 [-3.60, -2.73] | -2.47 [-2.74, -2.19] | 39392 |
| Validator | 15 | 40 | -2.71 [-3.05, -2.35] | -1.96 [-2.15, -1.75] | 46360 |
| Validator | 50 | 40 | -1.53 [-1.69, -1.37] | -1.18 [-1.26, -1.09] | 153382 |
| Gatekeeper | 1 | 40 | -1.58 [-1.99, -1.16] | -1.13 [-1.33, -0.95] | 118176 |
| Gatekeeper | 15 | 40 | -1.54 [-1.90, -1.21] | -0.69 [-0.85, -0.54] | 139080 |
| Gatekeeper | 50 | 40 | -0.62 [-0.78, -0.48] | -0.48 [-0.55, -0.42] | 460146 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.81% [6.43%, 7.17%] | 1.77% | 6.81% | 0.00% [0.00%, 0.00%] | 4.03% [3.84%, 4.22%] | 2.44% | 4.03% | 0.00% [0.00%, 0.00%] | 0.558 [0.542, 0.573] | 14.6% | 11.0% | 0.000% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.24% [5.00%, 5.48%] | 1.32% | 5.24% | 0.00% [0.00%, 0.00%] | 2.95% [2.81%, 3.09%] | 1.82% | 2.95% | 0.00% [0.00%, 0.00%] | 0.545 [0.532, 0.559] | 7.5% | 7.5% | 0.006% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.82% [3.71%, 3.92%] | 0.81% | 3.82% | 0.00% [0.00%, 0.00%] | 1.90% [1.84%, 1.96%] | 1.11% | 1.90% | 0.00% [0.00%, 0.00%] | 0.555 [0.547, 0.563] | 7.3% | 6.2% | 0.000% | 200 | 172224 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.82% [6.46%, 7.14%] | 1.77% | 6.81% | 0.01% [-0.07%, 0.09%] | 4.02% [3.91%, 4.13%] | 2.44% | 4.03% | -0.02% [-0.16%, 0.11%] | 0.558 [0.544, 0.572] | 15.1% | 10.9% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.29% [5.07%, 5.51%] | 1.32% | 5.24% | 0.04% [-0.03%, 0.11%] | 2.97% [2.89%, 3.05%] | 1.82% | 2.95% | 0.03% [-0.09%, 0.15%] | 0.544 [0.532, 0.555] | 7.8% | 7.5% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.81% [3.71%, 3.90%] | 0.81% | 3.82% | -0.01% [-0.04%, 0.02%] | 1.91% [1.87%, 1.95%] | 1.11% | 1.90% | 0.01% [-0.05%, 0.07%] | 0.555 [0.547, 0.562] | 7.2% | 6.0% | 0.000% | 200 | 688896 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.82% [6.47%, 7.17%] | 1.77% | 6.81% | 0.01% [-0.07%, 0.09%] | 4.02% [3.91%, 4.12%] | 2.44% | 4.03% | -0.02% [-0.16%, 0.12%] | 0.558 [0.544, 0.572] | 15.1% | 10.9% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.29% [5.07%, 5.51%] | 1.32% | 5.24% | 0.04% [-0.03%, 0.11%] | 2.97% [2.89%, 3.05%] | 1.82% | 2.95% | 0.03% [-0.09%, 0.14%] | 0.544 [0.532, 0.555] | 7.8% | 7.5% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.81% [3.71%, 3.91%] | 0.81% | 3.82% | -0.01% [-0.04%, 0.02%] | 1.91% [1.87%, 1.95%] | 1.11% | 1.90% | 0.01% [-0.05%, 0.06%] | 0.555 [0.547, 0.562] | 7.2% | 6.0% | 0.000% | 200 | 688896 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.77% [6.41%, 7.13%] | 1.77% | 6.81% | -0.04% [-0.08%, 0.01%] | 4.00% [3.83%, 4.16%] | 2.44% | 4.03% | -0.04% [-0.14%, 0.06%] | 0.559 [0.544, 0.575] | 14.6% | 10.9% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.27% [5.02%, 5.51%] | 1.32% | 5.24% | 0.03% [-0.00%, 0.06%] | 3.01% [2.89%, 3.12%] | 1.82% | 2.95% | 0.06% [0.00%, 0.12%] | 0.544 [0.530, 0.557] | 7.5% | 7.4% | 0.007% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.81% [3.71%, 3.92%] | 0.81% | 3.82% | -0.00% [-0.01%, 0.01%] | 1.89% [1.84%, 1.95%] | 1.11% | 1.90% | -0.01% [-0.03%, 0.02%] | 0.555 [0.547, 0.563] | 7.2% | 6.2% | 0.000% | 200 | 688896 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.64% [6.36%, 6.95%] | 1.82% | 6.81% | -0.17% [-0.37%, 0.03%] | 4.29% [4.15%, 4.44%] | 2.44% | 4.03% | 0.26% [0.03%, 0.50%] | 0.545 [0.533, 0.556] | 6.3% | 8.3% | 0.000% | 200 | 79598 |
| R = 15, 40 decoys, bundling on | 5.26% [5.07%, 5.46%] | 1.35% | 5.24% | 0.02% [-0.14%, 0.18%] | 3.20% [3.09%, 3.29%] | 1.82% | 2.95% | 0.25% [0.10%, 0.41%] | 0.538 [0.528, 0.547] | 4.6% | 5.7% | 0.000% | 200 | 104034 |
| R = 50, 40 decoys, bundling on | 3.71% [3.63%, 3.78%] | 0.83% | 3.82% | -0.11% [-0.19%, -0.04%] | 1.94% [1.90%, 1.99%] | 1.11% | 1.90% | 0.04% [-0.04%, 0.11%] | 0.537 [0.531, 0.544] | 3.0% | 3.8% | 0.000% | 200 | 344448 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.36% [6.01%, 6.71%] | 1.67% | 6.81% | -0.45% [-0.75%, -0.11%] | 2.95% [2.80%, 3.12%] | 2.44% | 4.03% | -1.08% [-1.33%, -0.83%] | 0.567 [0.552, 0.582] | 14.1% | 10.5% | 0.048% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.12% [4.89%, 5.34%] | 1.25% | 5.24% | -0.12% [-0.35%, 0.11%] | 2.09% [1.98%, 2.20%] | 1.82% | 2.95% | -0.86% [-1.03%, -0.69%] | 0.533 [0.518, 0.548] | 7.9% | 6.7% | 0.002% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.51% [3.41%, 3.60%] | 0.77% | 3.82% | -0.31% [-0.41%, -0.21%] | 1.30% [1.25%, 1.35%] | 1.11% | 1.90% | -0.60% [-0.69%, -0.52%] | 0.551 [0.542, 0.560] | 5.6% | 5.2% | 0.000% | 200 | 172224 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.81% [6.44%, 7.18%] | 1.77% | 6.81% | -0.00% [-0.09%, 0.08%] | 4.01% [3.87%, 4.15%] | 2.44% | 4.03% | -0.02% [-0.22%, 0.16%] | 0.555 [0.541, 0.569] | 13.9% | 10.9% | 0.009% | 200 | 119397 |
| R = 15, 40 decoys, bundling on | 5.27% [5.05%, 5.49%] | 1.32% | 5.24% | 0.03% [-0.04%, 0.10%] | 3.03% [2.93%, 3.14%] | 1.82% | 2.95% | 0.09% [-0.05%, 0.21%] | 0.546 [0.534, 0.559] | 7.6% | 7.6% | 0.001% | 200 | 156051 |
| R = 50, 40 decoys, bundling on | 3.81% [3.71%, 3.91%] | 0.81% | 3.82% | -0.01% [-0.04%, 0.02%] | 1.91% [1.86%, 1.95%] | 1.11% | 1.90% | 0.01% [-0.05%, 0.07%] | 0.556 [0.548, 0.564] | 7.5% | 6.0% | 0.000% | 200 | 516672 |

## Outcome-shuffle control (stable cells)

21 stable cells; 0 with a shuffled-outcome AUC interval excluding 0.5.

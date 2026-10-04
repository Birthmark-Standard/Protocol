# Tables

Record-to-device linking with genuine decoys, gatekeeper departure bundling, match board pushes, and 120-second registry-level pooled bundling. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 15 | 40 | 2.65 | 7.1% | 18.7% | 25.8% | 20.1% | 7.0% | 215,400 |
| 50 | 40 | 4.31 | 1.4% | 5.7% | 7.1% | 5.8% | 1.3% | 215,400 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.52% [8.15%, 8.88%] | 2.05% | 8.52% | 0.00% [0.00%, 0.00%] | 5.21% [5.01%, 5.43%] | 2.44% | 5.21% | 0.00% [0.00%, 0.00%] | 0.569 [0.557, 0.581] | 14.0% | 13.2% | 0.000% | 200 | 39962 |
| R = 15, 40 decoys, bundling on | 6.76% [6.50%, 7.02%] | 1.53% | 6.76% | 0.00% [0.00%, 0.00%] | 3.77% [3.61%, 3.93%] | 1.82% | 3.77% | 0.00% [0.00%, 0.00%] | 0.557 [0.546, 0.568] | 12.7% | 9.7% | 0.000% | 200 | 52098 |
| R = 50, 40 decoys, bundling on | 4.48% [4.37%, 4.58%] | 0.94% | 4.48% | 0.00% [0.00%, 0.00%] | 2.40% [2.33%, 2.47%] | 1.11% | 2.40% | 0.00% [0.00%, 0.00%] | 0.550 [0.544, 0.557] | 8.1% | 6.2% | 0.000% | 200 | 172650 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.50% [8.13%, 8.84%] | 2.05% | 8.52% | -0.02% [-0.09%, 0.05%] | 5.13% [4.98%, 5.28%] | 2.44% | 5.21% | -0.08% [-0.20%, 0.04%] | 0.571 [0.560, 0.582] | 15.5% | 13.2% | 0.000% | 200 | 159848 |
| R = 15, 40 decoys, bundling on | 6.76% [6.52%, 7.00%] | 1.53% | 6.76% | 0.00% [-0.05%, 0.06%] | 3.84% [3.73%, 3.95%] | 1.82% | 3.77% | 0.07% [-0.04%, 0.17%] | 0.558 [0.548, 0.567] | 13.7% | 10.2% | 0.000% | 200 | 208392 |
| R = 50, 40 decoys, bundling on | 4.45% [4.35%, 4.55%] | 0.94% | 4.48% | -0.03% [-0.06%, 0.00%] | 2.40% [2.36%, 2.45%] | 1.11% | 2.40% | 0.00% [-0.06%, 0.06%] | 0.551 [0.544, 0.557] | 7.7% | 6.3% | 0.000% | 200 | 690600 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.50% [8.16%, 8.85%] | 2.05% | 8.52% | -0.02% [-0.09%, 0.05%] | 5.13% [4.98%, 5.29%] | 2.44% | 5.21% | -0.08% [-0.20%, 0.04%] | 0.571 [0.560, 0.582] | 15.5% | 13.2% | 0.000% | 200 | 159848 |
| R = 15, 40 decoys, bundling on | 6.76% [6.51%, 7.01%] | 1.53% | 6.76% | 0.00% [-0.06%, 0.06%] | 3.84% [3.73%, 3.94%] | 1.82% | 3.77% | 0.07% [-0.04%, 0.17%] | 0.558 [0.548, 0.567] | 13.7% | 10.2% | 0.000% | 200 | 208392 |
| R = 50, 40 decoys, bundling on | 4.45% [4.35%, 4.55%] | 0.94% | 4.48% | -0.03% [-0.06%, 0.00%] | 2.40% [2.36%, 2.44%] | 1.11% | 2.40% | 0.00% [-0.06%, 0.06%] | 0.551 [0.544, 0.557] | 7.7% | 6.3% | 0.000% | 200 | 690600 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.57% [8.21%, 8.92%] | 2.05% | 8.52% | 0.05% [0.01%, 0.10%] | 5.15% [4.97%, 5.32%] | 2.44% | 5.21% | -0.06% [-0.15%, 0.03%] | 0.568 [0.556, 0.579] | 14.4% | 13.0% | 0.000% | 200 | 159848 |
| R = 15, 40 decoys, bundling on | 6.75% [6.48%, 7.01%] | 1.53% | 6.76% | -0.01% [-0.05%, 0.01%] | 3.80% [3.66%, 3.95%] | 1.82% | 3.77% | 0.03% [-0.04%, 0.10%] | 0.557 [0.546, 0.567] | 12.6% | 9.8% | 0.000% | 200 | 208392 |
| R = 50, 40 decoys, bundling on | 4.47% [4.36%, 4.57%] | 0.94% | 4.48% | -0.01% [-0.02%, 0.00%] | 2.40% [2.34%, 2.46%] | 1.11% | 2.40% | 0.01% [-0.02%, 0.04%] | 0.551 [0.544, 0.558] | 8.0% | 6.3% | 0.000% | 200 | 690600 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 9.45% [9.12%, 9.77%] | 2.45% | 8.52% | 0.93% [0.71%, 1.16%] | 6.41% [6.23%, 6.58%] | 2.44% | 5.21% | 1.20% [0.94%, 1.45%] | 0.566 [0.556, 0.575] | 10.9% | 13.3% | 0.000% | 200 | 79924 |
| R = 15, 40 decoys, bundling on | 7.63% [7.36%, 7.88%] | 1.82% | 6.76% | 0.87% [0.71%, 1.05%] | 4.83% [4.71%, 4.95%] | 1.82% | 3.77% | 1.05% [0.86%, 1.25%] | 0.553 [0.545, 0.561] | 8.2% | 9.8% | 0.000% | 200 | 104196 |
| R = 50, 40 decoys, bundling on | 5.01% [4.92%, 5.10%] | 1.12% | 4.48% | 0.53% [0.44%, 0.61%] | 2.92% [2.87%, 2.97%] | 1.11% | 2.40% | 0.52% [0.43%, 0.61%] | 0.539 [0.534, 0.544] | 3.9% | 5.5% | 0.000% | 200 | 345300 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 9.61% [9.22%, 10.03%] | 2.36% | 8.52% | 1.09% [0.78%, 1.42%] | 5.45% [5.21%, 5.67%] | 2.44% | 5.21% | 0.24% [-0.06%, 0.54%] | 0.574 [0.562, 0.586] | 18.5% | 15.2% | 0.008% | 200 | 39962 |
| R = 15, 40 decoys, bundling on | 7.84% [7.57%, 8.10%] | 1.76% | 6.76% | 1.07% [0.82%, 1.34%] | 4.02% [3.85%, 4.20%] | 1.82% | 3.77% | 0.25% [0.02%, 0.48%] | 0.564 [0.553, 0.575] | 14.6% | 12.5% | 0.002% | 200 | 52098 |
| R = 50, 40 decoys, bundling on | 5.09% [4.98%, 5.20%] | 1.08% | 4.48% | 0.61% [0.50%, 0.72%] | 2.48% [2.41%, 2.55%] | 1.11% | 2.40% | 0.08% [-0.02%, 0.17%] | 0.562 [0.555, 0.568] | 9.8% | 8.5% | 0.001% | 200 | 172650 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.47% [8.11%, 8.82%] | 2.05% | 8.52% | -0.04% [-0.15%, 0.07%] | 5.15% [5.00%, 5.30%] | 2.44% | 5.21% | -0.06% [-0.26%, 0.13%] | 0.570 [0.559, 0.581] | 14.4% | 13.4% | 0.000% | 200 | 119886 |
| R = 15, 40 decoys, bundling on | 6.76% [6.52%, 7.01%] | 1.53% | 6.76% | -0.00% [-0.07%, 0.07%] | 3.73% [3.62%, 3.84%] | 1.82% | 3.77% | -0.04% [-0.20%, 0.11%] | 0.556 [0.546, 0.566] | 12.1% | 10.1% | 0.001% | 200 | 156294 |
| R = 50, 40 decoys, bundling on | 4.44% [4.34%, 4.55%] | 0.94% | 4.48% | -0.03% [-0.07%, -0.00%] | 2.39% [2.34%, 2.43%] | 1.11% | 2.40% | -0.01% [-0.08%, 0.05%] | 0.551 [0.544, 0.557] | 8.2% | 6.4% | 0.000% | 200 | 517950 |

## Outcome-shuffle control (stable cells)

21 stable cells; 4 with a shuffled-outcome AUC interval excluding 0.5: R1_D40_B first_hop_content (0.505), R50_D40_B first_hop_cred (0.504), R50_D40_B first_hop_content (0.505), R50_D40_B cred_processor (0.504).

# Tables

Record-to-device linking with genuine decoys, build run10_no_pm. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Volume

| L (in flight) | Captures per second | Captures per day | Devices (20-minute interval) |
|---|---|---|---|
| 1 | 0.0010 | 83 | 1.2 |
| 15 | 0.0145 | 1,250 | 17.4 |
| 21 | 0.0203 | 1,750 | 24.3 |
| 31 | 0.0299 | 2,584 | 35.9 |
| 35 | 0.0338 | 2,917 | 40.5 |
| 41 | 0.0396 | 3,417 | 47.5 |
| 45 | 0.0434 | 3,751 | 52.1 |
| 50 | 0.0482 | 4,168 | 57.9 |
| 55 | 0.0531 | 4,584 | 63.7 |
| 61 | 0.0588 | 5,084 | 70.6 |
| 70 | 0.0675 | 5,835 | 81.0 |
| 75 | 0.0724 | 6,251 | 86.8 |
| 80 | 0.0772 | 6,668 | 92.6 |
| 90 | 0.0868 | 7,502 | 104.2 |
| 101 | 0.0974 | 8,419 | 116.9 |
| 110 | 0.1061 | 9,169 | 127.3 |
| 115 | 0.1109 | 9,585 | 133.1 |
| 150 | 0.1447 | 12,503 | 173.7 |
| 151 | 0.1457 | 12,586 | 174.8 |
| 165 | 0.1592 | 13,753 | 191.0 |
| 200 | 0.1929 | 16,670 | 231.5 |

## Departure bundle sizes

Postings per 30-second bundle at one gatekeeper, on its own grid, over every run of the cell. Off cells report the bundles the same selections would have formed.

| R | Decoys | Mean per bundle | Empty | Exactly 1 | Fewer than 2 | 1, of non-empty | Postings departing alone | Bundles |
|---|---|---|---|---|---|---|---|---|
| 1 | 60 | 1.77 | 17.1% | 30.2% | 47.3% | 36.4% | 17.1% | 4,145,670 |

## Change from the run10 build on the same records

Accuracy in this build minus accuracy in the run10 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 60 | -0.03 [-0.19, +0.14] | +0.25 [-0.02, +0.51] | 39857 |
| First hop, credential | 1 | 60 | -0.05 [-0.17, +0.07] | +0.09 [-0.07, +0.24] | 159428 |
| First hop, content | 1 | 60 | -0.05 [-0.19, +0.08] | +0.09 [-0.08, +0.25] | 159428 |
| Credential processor | 1 | 60 | -0.02 [-0.16, +0.12] | +0.23 [+0.02, +0.45] | 159428 |
| Content server | 1 | 60 | -0.04 [-0.22, +0.14] | +0.02 [-0.16, +0.20] | 79714 |
| Validator | 1 | 60 | -0.10 [-0.29, +0.09] | -0.03 [-0.27, +0.22] | 39857 |
| Gatekeeper | 1 | 60 | -0.12 [-0.24, +0.01] | +0.09 [-0.10, +0.26] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.88% [9.46%, 10.28%] | 2.01% | 9.88% | 0.00% [0.00%, 0.00%] | 4.75% [4.57%, 4.93%] | 1.64% | 4.75% | 0.00% [0.00%, 0.00%] | 0.582 [0.570, 0.594] | 24.3% | 18.4% | 0.013% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.37% [6.06%, 6.68%] | 1.53% | 6.37% | 0.00% [0.00%, 0.00%] | 3.70% [3.54%, 3.86%] | 1.25% | 3.70% | 0.00% [0.00%, 0.00%] | 0.555 [0.542, 0.569] | 14.4% | 10.3% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.54% [3.46%, 3.62%] | 0.76% | 3.54% | 0.00% [0.00%, 0.00%] | 1.76% [1.70%, 1.82%] | 0.62% | 1.76% | 0.00% [0.00%, 0.00%] | 0.549 [0.542, 0.556] | 6.7% | 5.4% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.84% [9.42%, 10.23%] | 2.01% | 9.88% | -0.04% [-0.12%, 0.04%] | 4.70% [4.56%, 4.84%] | 1.64% | 4.75% | -0.05% [-0.16%, 0.08%] | 0.582 [0.570, 0.593] | 23.4% | 17.9% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.38% [6.09%, 6.67%] | 1.53% | 6.37% | 0.00% [-0.07%, 0.08%] | 3.57% [3.46%, 3.68%] | 1.25% | 3.70% | -0.14% [-0.24%, -0.02%] | 0.556 [0.544, 0.569] | 13.5% | 10.6% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.54% [3.46%, 3.62%] | 0.76% | 3.54% | -0.00% [-0.03%, 0.02%] | 1.76% [1.73%, 1.80%] | 0.62% | 1.76% | -0.00% [-0.05%, 0.04%] | 0.549 [0.543, 0.555] | 6.5% | 5.5% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.84% [9.45%, 10.24%] | 2.01% | 9.88% | -0.04% [-0.12%, 0.04%] | 4.70% [4.56%, 4.83%] | 1.64% | 4.75% | -0.05% [-0.18%, 0.07%] | 0.582 [0.570, 0.593] | 23.4% | 17.9% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.38% [6.09%, 6.66%] | 1.53% | 6.37% | 0.00% [-0.07%, 0.07%] | 3.57% [3.45%, 3.68%] | 1.25% | 3.70% | -0.14% [-0.26%, -0.02%] | 0.556 [0.544, 0.569] | 13.5% | 10.6% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.54% [3.46%, 3.61%] | 0.76% | 3.54% | -0.00% [-0.03%, 0.02%] | 1.76% [1.73%, 1.80%] | 0.62% | 1.76% | -0.00% [-0.05%, 0.04%] | 0.549 [0.543, 0.555] | 6.5% | 5.5% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.89% [9.47%, 10.30%] | 2.01% | 9.88% | 0.01% [-0.03%, 0.06%] | 4.71% [4.55%, 4.88%] | 1.64% | 4.75% | -0.04% [-0.12%, 0.06%] | 0.582 [0.570, 0.594] | 23.2% | 18.3% | 0.014% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.36% [6.05%, 6.66%] | 1.53% | 6.37% | -0.02% [-0.06%, 0.02%] | 3.61% [3.46%, 3.76%] | 1.25% | 3.70% | -0.09% [-0.18%, 0.00%] | 0.555 [0.542, 0.569] | 14.5% | 10.4% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.54% [3.46%, 3.62%] | 0.76% | 3.54% | -0.00% [-0.01%, 0.01%] | 1.75% [1.70%, 1.80%] | 0.62% | 1.76% | -0.02% [-0.04%, 0.01%] | 0.550 [0.543, 0.557] | 6.6% | 5.4% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.80% [9.45%, 10.15%] | 2.16% | 9.88% | -0.08% [-0.32%, 0.17%] | 5.36% [5.20%, 5.51%] | 1.64% | 4.75% | 0.61% [0.39%, 0.84%] | 0.564 [0.556, 0.573] | 7.8% | 11.7% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 6.58% [6.32%, 6.83%] | 1.65% | 6.37% | 0.20% [-0.00%, 0.39%] | 3.92% [3.81%, 4.05%] | 1.25% | 3.70% | 0.22% [0.04%, 0.40%] | 0.548 [0.538, 0.558] | 6.1% | 7.2% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.70% [3.62%, 3.77%] | 0.82% | 3.54% | 0.16% [0.09%, 0.22%] | 2.00% [1.96%, 2.04%] | 0.62% | 1.76% | 0.24% [0.17%, 0.30%] | 0.526 [0.520, 0.531] | 2.4% | 3.6% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.41% [9.01%, 9.82%] | 1.83% | 9.88% | -0.46% [-0.82%, -0.13%] | 4.79% [4.59%, 5.00%] | 1.64% | 4.75% | 0.05% [-0.23%, 0.33%] | 0.587 [0.574, 0.601] | 20.1% | 17.4% | 0.033% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.31% [6.04%, 6.61%] | 1.40% | 6.37% | -0.06% [-0.34%, 0.19%] | 3.73% [3.57%, 3.90%] | 1.25% | 3.70% | 0.03% [-0.22%, 0.27%] | 0.559 [0.546, 0.573] | 9.1% | 9.3% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.41% [3.34%, 3.50%] | 0.70% | 3.54% | -0.13% [-0.21%, -0.04%] | 1.87% [1.82%, 1.92%] | 0.62% | 1.76% | 0.10% [0.03%, 0.18%] | 0.549 [0.543, 0.555] | 5.6% | 5.2% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.83% [9.42%, 10.25%] | 2.01% | 9.88% | -0.05% [-0.15%, 0.06%] | 4.79% [4.64%, 4.94%] | 1.64% | 4.75% | 0.04% [-0.14%, 0.23%] | 0.583 [0.571, 0.594] | 23.2% | 18.4% | 0.009% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 6.37% [6.07%, 6.65%] | 1.53% | 6.37% | -0.01% [-0.10%, 0.08%] | 3.53% [3.41%, 3.64%] | 1.25% | 3.70% | -0.18% [-0.34%, -0.02%] | 0.554 [0.541, 0.567] | 13.8% | 10.5% | 0.018% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.55% [3.47%, 3.63%] | 0.76% | 3.54% | 0.01% [-0.02%, 0.03%] | 1.77% [1.73%, 1.81%] | 0.62% | 1.76% | 0.01% [-0.04%, 0.06%] | 0.548 [0.542, 0.555] | 6.6% | 5.5% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R1_D60_B validator (0.509), R100_D60_B first_hop_cred (0.504).

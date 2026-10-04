# Tables

Record-to-device linking with genuine decoys, build run10. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.91% [9.48%, 10.33%] | 2.03% | 9.91% | 0.00% [0.00%, 0.00%] | 4.49% [4.27%, 4.70%] | 1.64% | 4.49% | 0.00% [0.00%, 0.00%] | 0.581 [0.569, 0.594] | 25.8% | 17.7% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.46% [6.15%, 6.78%] | 1.55% | 6.46% | 0.00% [0.00%, 0.00%] | 3.52% [3.36%, 3.68%] | 1.25% | 3.52% | 0.00% [0.00%, 0.00%] | 0.557 [0.544, 0.571] | 13.4% | 11.1% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.48% [3.40%, 3.56%] | 0.77% | 3.48% | 0.00% [0.00%, 0.00%] | 1.74% [1.68%, 1.80%] | 0.62% | 1.74% | 0.00% [0.00%, 0.00%] | 0.552 [0.544, 0.559] | 6.5% | 5.4% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.89% [9.46%, 10.30%] | 2.03% | 9.91% | -0.02% [-0.11%, 0.06%] | 4.61% [4.45%, 4.77%] | 1.64% | 4.49% | 0.12% [-0.01%, 0.25%] | 0.582 [0.570, 0.593] | 25.4% | 17.5% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.47% [6.17%, 6.79%] | 1.55% | 6.46% | 0.01% [-0.07%, 0.09%] | 3.50% [3.39%, 3.62%] | 1.25% | 3.52% | -0.02% [-0.12%, 0.09%] | 0.559 [0.546, 0.572] | 13.7% | 10.9% | 0.017% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.47% [3.40%, 3.54%] | 0.77% | 3.48% | -0.01% [-0.04%, 0.01%] | 1.73% [1.70%, 1.77%] | 0.62% | 1.74% | -0.01% [-0.05%, 0.04%] | 0.550 [0.544, 0.557] | 6.2% | 5.4% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.89% [9.48%, 10.28%] | 2.03% | 9.91% | -0.02% [-0.10%, 0.06%] | 4.61% [4.45%, 4.78%] | 1.64% | 4.49% | 0.12% [-0.01%, 0.24%] | 0.582 [0.570, 0.593] | 25.4% | 17.5% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.47% [6.17%, 6.77%] | 1.55% | 6.46% | 0.01% [-0.07%, 0.09%] | 3.50% [3.39%, 3.63%] | 1.25% | 3.52% | -0.02% [-0.13%, 0.09%] | 0.559 [0.546, 0.572] | 13.7% | 10.9% | 0.017% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.47% [3.39%, 3.54%] | 0.77% | 3.48% | -0.01% [-0.03%, 0.01%] | 1.73% [1.70%, 1.76%] | 0.62% | 1.74% | -0.01% [-0.05%, 0.04%] | 0.550 [0.544, 0.557] | 6.2% | 5.4% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.91% [9.48%, 10.33%] | 2.03% | 9.91% | 0.00% [-0.05%, 0.05%] | 4.48% [4.29%, 4.67%] | 1.64% | 4.49% | -0.01% [-0.13%, 0.10%] | 0.581 [0.569, 0.593] | 25.5% | 17.6% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.46% [6.14%, 6.77%] | 1.55% | 6.46% | -0.01% [-0.04%, 0.03%] | 3.46% [3.32%, 3.60%] | 1.25% | 3.52% | -0.06% [-0.15%, 0.03%] | 0.557 [0.544, 0.571] | 13.5% | 11.0% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.47% [3.39%, 3.54%] | 0.77% | 3.48% | -0.01% [-0.02%, 0.00%] | 1.75% [1.70%, 1.80%] | 0.62% | 1.74% | 0.01% [-0.02%, 0.03%] | 0.553 [0.546, 0.560] | 6.4% | 5.4% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.84% [9.52%, 10.15%] | 2.18% | 9.91% | -0.07% [-0.31%, 0.16%] | 5.34% [5.19%, 5.47%] | 1.64% | 4.49% | 0.85% [0.61%, 1.08%] | 0.564 [0.555, 0.574] | 7.9% | 12.7% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 6.60% [6.35%, 6.84%] | 1.66% | 6.46% | 0.14% [-0.06%, 0.35%] | 4.01% [3.88%, 4.14%] | 1.25% | 3.52% | 0.49% [0.28%, 0.69%] | 0.546 [0.536, 0.556] | 3.7% | 7.1% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.72% [3.64%, 3.79%] | 0.83% | 3.48% | 0.24% [0.18%, 0.30%] | 2.01% [1.96%, 2.05%] | 0.62% | 1.74% | 0.27% [0.20%, 0.34%] | 0.529 [0.525, 0.534] | 2.2% | 3.5% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.51% [9.10%, 9.93%] | 1.84% | 9.91% | -0.40% [-0.79%, -0.05%] | 4.82% [4.63%, 5.03%] | 1.64% | 4.49% | 0.33% [0.04%, 0.63%] | 0.583 [0.569, 0.596] | 22.1% | 17.5% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.32% [6.05%, 6.59%] | 1.40% | 6.46% | -0.14% [-0.42%, 0.12%] | 3.84% [3.64%, 4.03%] | 1.25% | 3.52% | 0.32% [0.07%, 0.59%] | 0.559 [0.545, 0.573] | 9.4% | 9.7% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.41% [3.33%, 3.49%] | 0.70% | 3.48% | -0.06% [-0.15%, 0.02%] | 1.95% [1.89%, 2.01%] | 0.62% | 1.74% | 0.21% [0.13%, 0.30%] | 0.551 [0.544, 0.557] | 5.3% | 5.0% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.95% [9.54%, 10.38%] | 2.03% | 9.91% | 0.04% [-0.06%, 0.14%] | 4.70% [4.54%, 4.85%] | 1.64% | 4.49% | 0.20% [0.01%, 0.41%] | 0.580 [0.568, 0.591] | 26.5% | 18.1% | 0.008% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 6.45% [6.14%, 6.74%] | 1.55% | 6.46% | -0.01% [-0.10%, 0.07%] | 3.49% [3.37%, 3.61%] | 1.25% | 3.52% | -0.03% [-0.17%, 0.11%] | 0.559 [0.545, 0.572] | 13.8% | 10.8% | 0.018% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.46% [3.39%, 3.55%] | 0.77% | 3.48% | -0.01% [-0.04%, 0.01%] | 1.74% [1.71%, 1.78%] | 0.62% | 1.74% | 0.00% [-0.05%, 0.06%] | 0.551 [0.544, 0.557] | 6.7% | 5.4% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R100_D60_B first_hop_cred (0.504), R100_D60_B first_hop_content (0.504).

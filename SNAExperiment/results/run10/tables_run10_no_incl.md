# Tables

Record-to-device linking with genuine decoys, build run10_no_incl. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | +0.06 [-0.15, +0.27] | +0.27 [-0.02, +0.56] | 39857 |
| First hop, credential | 1 | 60 | +0.05 [-0.12, +0.21] | +0.07 [-0.12, +0.25] | 159428 |
| First hop, content | 1 | 60 | +0.05 [-0.11, +0.22] | +0.07 [-0.12, +0.26] | 159428 |
| Credential processor | 1 | 60 | +0.03 [-0.16, +0.21] | +0.24 [+0.02, +0.48] | 159428 |
| Content server | 1 | 60 | -0.08 [-0.27, +0.11] | -0.10 [-0.30, +0.09] | 79714 |
| Validator | 1 | 60 | -0.27 [-0.51, -0.02] | -0.53 [-0.82, -0.22] | 39857 |
| Gatekeeper | 1 | 60 | -0.05 [-0.22, +0.12] | -0.06 [-0.25, +0.14] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.97% [9.53%, 10.39%] | 2.02% | 9.97% | 0.00% [0.00%, 0.00%] | 4.77% [4.54%, 4.98%] | 1.64% | 4.77% | 0.00% [0.00%, 0.00%] | 0.580 [0.568, 0.593] | 26.8% | 18.3% | 0.008% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.36% [6.05%, 6.69%] | 1.54% | 6.36% | 0.00% [0.00%, 0.00%] | 3.40% [3.23%, 3.56%] | 1.25% | 3.40% | 0.00% [0.00%, 0.00%] | 0.561 [0.547, 0.576] | 13.4% | 10.3% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.52% [3.44%, 3.61%] | 0.77% | 3.52% | 0.00% [0.00%, 0.00%] | 1.73% [1.67%, 1.79%] | 0.62% | 1.73% | 0.00% [0.00%, 0.00%] | 0.547 [0.540, 0.554] | 6.4% | 5.5% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.93% [9.49%, 10.35%] | 2.02% | 9.97% | -0.03% [-0.12%, 0.05%] | 4.68% [4.54%, 4.83%] | 1.64% | 4.77% | -0.09% [-0.21%, 0.05%] | 0.580 [0.568, 0.592] | 26.3% | 17.9% | 0.036% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.40% [6.11%, 6.70%] | 1.54% | 6.36% | 0.04% [-0.03%, 0.11%] | 3.42% [3.31%, 3.54%] | 1.25% | 3.40% | 0.03% [-0.08%, 0.14%] | 0.562 [0.549, 0.575] | 13.5% | 10.7% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.50% [3.42%, 3.57%] | 0.77% | 3.52% | -0.02% [-0.05%, 0.00%] | 1.74% [1.70%, 1.77%] | 0.62% | 1.73% | 0.01% [-0.04%, 0.05%] | 0.548 [0.542, 0.554] | 6.3% | 5.5% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.93% [9.52%, 10.35%] | 2.02% | 9.97% | -0.03% [-0.12%, 0.05%] | 4.68% [4.54%, 4.83%] | 1.64% | 4.77% | -0.09% [-0.22%, 0.05%] | 0.580 [0.568, 0.592] | 26.3% | 17.9% | 0.036% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.40% [6.10%, 6.70%] | 1.54% | 6.36% | 0.04% [-0.03%, 0.12%] | 3.42% [3.31%, 3.54%] | 1.25% | 3.40% | 0.03% [-0.09%, 0.14%] | 0.562 [0.549, 0.575] | 13.5% | 10.7% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.50% [3.42%, 3.57%] | 0.77% | 3.52% | -0.02% [-0.05%, 0.00%] | 1.74% [1.70%, 1.77%] | 0.62% | 1.73% | 0.01% [-0.04%, 0.05%] | 0.548 [0.542, 0.554] | 6.3% | 5.5% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.94% [9.51%, 10.36%] | 2.02% | 9.97% | -0.03% [-0.08%, 0.02%] | 4.73% [4.53%, 4.91%] | 1.64% | 4.77% | -0.04% [-0.13%, 0.05%] | 0.581 [0.569, 0.594] | 26.3% | 18.4% | 0.012% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.35% [6.04%, 6.65%] | 1.54% | 6.36% | -0.01% [-0.05%, 0.03%] | 3.43% [3.29%, 3.57%] | 1.25% | 3.40% | 0.03% [-0.05%, 0.12%] | 0.562 [0.549, 0.576] | 13.8% | 10.4% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.51% [3.43%, 3.60%] | 0.77% | 3.52% | -0.01% [-0.02%, 0.00%] | 1.73% [1.68%, 1.78%] | 0.62% | 1.73% | 0.00% [-0.02%, 0.02%] | 0.548 [0.541, 0.555] | 6.4% | 5.5% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.75% [9.41%, 10.09%] | 2.17% | 9.97% | -0.21% [-0.47%, 0.03%] | 5.24% [5.07%, 5.41%] | 1.64% | 4.77% | 0.47% [0.20%, 0.73%] | 0.566 [0.558, 0.575] | 6.6% | 12.2% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 6.65% [6.39%, 6.90%] | 1.65% | 6.36% | 0.29% [0.10%, 0.48%] | 3.97% [3.84%, 4.10%] | 1.25% | 3.40% | 0.57% [0.39%, 0.75%] | 0.542 [0.532, 0.552] | 4.2% | 7.0% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.68% [3.61%, 3.76%] | 0.82% | 3.52% | 0.16% [0.09%, 0.23%] | 2.02% [1.98%, 2.06%] | 0.62% | 1.73% | 0.29% [0.22%, 0.35%] | 0.526 [0.521, 0.532] | 2.1% | 3.4% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.25% [8.87%, 9.63%] | 1.84% | 9.97% | -0.72% [-1.07%, -0.39%] | 4.29% [4.08%, 4.51%] | 1.64% | 4.77% | -0.47% [-0.77%, -0.16%] | 0.577 [0.565, 0.590] | 26.3% | 17.0% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.05% [5.75%, 6.35%] | 1.40% | 6.36% | -0.31% [-0.61%, -0.04%] | 3.45% [3.28%, 3.62%] | 1.25% | 3.40% | 0.05% [-0.18%, 0.30%] | 0.557 [0.542, 0.572] | 8.9% | 9.5% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.24% [3.16%, 3.32%] | 0.70% | 3.52% | -0.28% [-0.36%, -0.18%] | 1.87% [1.82%, 1.93%] | 0.62% | 1.73% | 0.14% [0.07%, 0.22%] | 0.546 [0.539, 0.553] | 5.5% | 4.7% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.90% [9.48%, 10.32%] | 2.02% | 9.97% | -0.07% [-0.18%, 0.03%] | 4.64% [4.48%, 4.79%] | 1.64% | 4.77% | -0.12% [-0.32%, 0.08%] | 0.580 [0.568, 0.592] | 25.0% | 18.2% | 0.029% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 6.37% [6.08%, 6.67%] | 1.54% | 6.36% | 0.01% [-0.07%, 0.10%] | 3.39% [3.28%, 3.51%] | 1.25% | 3.40% | -0.01% [-0.17%, 0.16%] | 0.561 [0.548, 0.574] | 13.1% | 10.2% | 0.018% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.51% [3.42%, 3.59%] | 0.77% | 3.52% | -0.01% [-0.04%, 0.01%] | 1.73% [1.69%, 1.77%] | 0.62% | 1.73% | -0.00% [-0.05%, 0.04%] | 0.547 [0.540, 0.554] | 6.3% | 5.3% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 3 with a shuffled-outcome AUC interval excluding 0.5: R1_D60_B validator (0.513), R100_D60_B baseline (0.507), R100_D60_B first_hop_cred (0.506).

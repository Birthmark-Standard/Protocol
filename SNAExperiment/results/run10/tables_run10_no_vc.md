# Tables

Record-to-device linking with genuine decoys, build run10_no_vc. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | -0.01 [-0.18, +0.16] | +0.27 [-0.01, +0.56] | 39857 |
| First hop, credential | 1 | 60 | -0.05 [-0.18, +0.08] | +0.10 [-0.09, +0.31] | 159428 |
| First hop, content | 1 | 60 | -0.05 [-0.17, +0.09] | +0.10 [-0.09, +0.29] | 159428 |
| Credential processor | 1 | 60 | -0.01 [-0.17, +0.14] | +0.29 [+0.07, +0.52] | 159428 |
| Content server | 1 | 60 | -0.06 [-0.24, +0.12] | -0.11 [-0.30, +0.09] | 79714 |
| Validator | 1 | 60 | -0.44 [-0.66, -0.23] | -1.69 [-1.94, -1.45] | 39857 |
| Gatekeeper | 1 | 60 | -0.10 [-0.23, +0.05] | +0.03 [-0.14, +0.22] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.90% [9.47%, 10.34%] | 2.02% | 9.90% | 0.00% [0.00%, 0.00%] | 4.76% [4.54%, 4.98%] | 1.64% | 4.76% | 0.00% [0.00%, 0.00%] | 0.584 [0.571, 0.596] | 24.3% | 17.7% | 0.048% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.36% [6.04%, 6.68%] | 1.54% | 6.36% | 0.00% [0.00%, 0.00%] | 3.49% [3.32%, 3.67%] | 1.25% | 3.49% | 0.00% [0.00%, 0.00%] | 0.557 [0.543, 0.570] | 13.9% | 10.6% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.50% [3.42%, 3.59%] | 0.77% | 3.50% | 0.00% [0.00%, 0.00%] | 1.74% [1.69%, 1.79%] | 0.62% | 1.74% | 0.00% [0.00%, 0.00%] | 0.550 [0.543, 0.557] | 6.7% | 5.4% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.84% [9.41%, 10.25%] | 2.02% | 9.90% | -0.06% [-0.14%, 0.01%] | 4.71% [4.56%, 4.87%] | 1.64% | 4.76% | -0.05% [-0.18%, 0.09%] | 0.583 [0.571, 0.595] | 24.3% | 17.4% | 0.016% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.37% [6.07%, 6.68%] | 1.54% | 6.36% | 0.01% [-0.06%, 0.07%] | 3.43% [3.31%, 3.55%] | 1.25% | 3.49% | -0.07% [-0.18%, 0.05%] | 0.557 [0.544, 0.570] | 14.1% | 10.9% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.49% [3.42%, 3.57%] | 0.77% | 3.50% | -0.01% [-0.03%, 0.01%] | 1.73% [1.70%, 1.76%] | 0.62% | 1.74% | -0.01% [-0.05%, 0.03%] | 0.549 [0.542, 0.556] | 6.5% | 5.4% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.84% [9.43%, 10.26%] | 2.02% | 9.90% | -0.06% [-0.14%, 0.01%] | 4.71% [4.57%, 4.87%] | 1.64% | 4.76% | -0.05% [-0.18%, 0.08%] | 0.583 [0.571, 0.595] | 24.3% | 17.4% | 0.016% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.37% [6.07%, 6.67%] | 1.54% | 6.36% | 0.01% [-0.06%, 0.08%] | 3.43% [3.30%, 3.56%] | 1.25% | 3.49% | -0.07% [-0.19%, 0.06%] | 0.557 [0.544, 0.570] | 14.1% | 10.9% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.49% [3.41%, 3.57%] | 0.77% | 3.50% | -0.01% [-0.03%, 0.02%] | 1.73% [1.71%, 1.76%] | 0.62% | 1.74% | -0.01% [-0.05%, 0.03%] | 0.549 [0.542, 0.556] | 6.5% | 5.4% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.90% [9.47%, 10.32%] | 2.02% | 9.90% | -0.01% [-0.05%, 0.04%] | 4.77% [4.59%, 4.96%] | 1.64% | 4.76% | 0.01% [-0.09%, 0.12%] | 0.583 [0.570, 0.595] | 24.3% | 17.5% | 0.042% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.35% [6.02%, 6.66%] | 1.54% | 6.36% | -0.02% [-0.06%, 0.02%] | 3.45% [3.30%, 3.60%] | 1.25% | 3.49% | -0.04% [-0.12%, 0.04%] | 0.557 [0.543, 0.570] | 13.8% | 10.7% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.50% [3.42%, 3.59%] | 0.77% | 3.50% | 0.00% [-0.01%, 0.01%] | 1.76% [1.72%, 1.81%] | 0.62% | 1.74% | 0.02% [-0.00%, 0.04%] | 0.550 [0.543, 0.557] | 6.7% | 5.4% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.77% [9.44%, 10.12%] | 2.17% | 9.90% | -0.13% [-0.37%, 0.12%] | 5.23% [5.10%, 5.38%] | 1.64% | 4.76% | 0.47% [0.21%, 0.72%] | 0.566 [0.556, 0.575] | 8.7% | 12.3% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 6.59% [6.32%, 6.83%] | 1.65% | 6.36% | 0.22% [0.01%, 0.43%] | 3.92% [3.78%, 4.05%] | 1.25% | 3.49% | 0.43% [0.22%, 0.64%] | 0.546 [0.537, 0.556] | 4.3% | 7.4% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.68% [3.61%, 3.75%] | 0.83% | 3.50% | 0.18% [0.11%, 0.25%] | 2.01% [1.96%, 2.05%] | 0.62% | 1.74% | 0.26% [0.20%, 0.33%] | 0.528 [0.523, 0.534] | 2.0% | 3.5% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.07% [8.67%, 9.47%] | 1.82% | 9.90% | -0.83% [-1.18%, -0.53%] | 3.13% [2.96%, 3.30%] | 1.64% | 4.76% | -1.64% [-1.90%, -1.38%] | 0.581 [0.569, 0.594] | 28.3% | 17.1% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 5.98% [5.69%, 6.23%] | 1.39% | 6.36% | -0.39% [-0.66%, -0.13%] | 2.38% [2.25%, 2.53%] | 1.25% | 3.49% | -1.11% [-1.32%, -0.91%] | 0.561 [0.547, 0.574] | 7.7% | 9.0% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.25% [3.17%, 3.32%] | 0.69% | 3.50% | -0.26% [-0.34%, -0.17%] | 1.23% [1.18%, 1.27%] | 0.62% | 1.74% | -0.52% [-0.59%, -0.45%] | 0.544 [0.537, 0.550] | 5.1% | 4.6% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.85% [9.44%, 10.27%] | 2.02% | 9.90% | -0.05% [-0.15%, 0.05%] | 4.73% [4.58%, 4.88%] | 1.64% | 4.76% | -0.04% [-0.23%, 0.15%] | 0.582 [0.571, 0.594] | 24.2% | 17.6% | 0.071% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 6.34% [6.04%, 6.64%] | 1.54% | 6.36% | -0.02% [-0.10%, 0.06%] | 3.47% [3.34%, 3.60%] | 1.25% | 3.49% | -0.02% [-0.17%, 0.13%] | 0.560 [0.547, 0.573] | 14.3% | 10.8% | 0.018% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.50% [3.41%, 3.58%] | 0.77% | 3.50% | -0.01% [-0.03%, 0.02%] | 1.74% [1.70%, 1.77%] | 0.62% | 1.74% | -0.01% [-0.05%, 0.04%] | 0.549 [0.543, 0.556] | 6.8% | 5.4% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 4 with a shuffled-outcome AUC interval excluding 0.5: R1_D60_B gatekeeper (0.506), R20_D60_B baseline (0.488), R100_D60_B first_hop_cred (0.506), R100_D60_B first_hop_content (0.505).

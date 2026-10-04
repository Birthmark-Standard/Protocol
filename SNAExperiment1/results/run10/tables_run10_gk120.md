# Tables

Record-to-device linking with genuine decoys, build run10_gk120. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | +0.02 [-0.17, +0.21] | +0.29 [-0.02, +0.59] | 39857 |
| First hop, credential | 1 | 60 | -0.05 [-0.21, +0.11] | +0.03 [-0.17, +0.23] | 159428 |
| First hop, content | 1 | 60 | -0.05 [-0.22, +0.11] | +0.03 [-0.17, +0.23] | 159428 |
| Credential processor | 1 | 60 | +0.03 [-0.16, +0.20] | +0.25 [+0.00, +0.51] | 159428 |
| Content server | 1 | 60 | +0.07 [-0.12, +0.26] | +0.11 [-0.09, +0.31] | 79714 |
| Validator | 1 | 60 | +0.25 [+0.02, +0.47] | +0.32 [+0.04, +0.62] | 39857 |
| Gatekeeper | 1 | 60 | -0.04 [-0.19, +0.13] | -0.09 [-0.29, +0.11] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.93% [9.50%, 10.37%] | 2.04% | 9.93% | 0.00% [0.00%, 0.00%] | 4.79% [4.56%, 5.02%] | 1.64% | 4.79% | 0.00% [0.00%, 0.00%] | 0.577 [0.564, 0.589] | 24.6% | 17.5% | 0.013% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.36% [6.02%, 6.67%] | 1.56% | 6.36% | 0.00% [0.00%, 0.00%] | 3.41% [3.24%, 3.58%] | 1.25% | 3.41% | 0.00% [0.00%, 0.00%] | 0.559 [0.545, 0.572] | 14.4% | 10.7% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.45% [3.37%, 3.54%] | 0.78% | 3.45% | 0.00% [0.00%, 0.00%] | 1.74% [1.68%, 1.79%] | 0.62% | 1.74% | 0.00% [0.00%, 0.00%] | 0.549 [0.541, 0.556] | 6.3% | 5.5% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.84% [9.40%, 10.26%] | 2.04% | 9.93% | -0.10% [-0.18%, -0.01%] | 4.65% [4.50%, 4.81%] | 1.64% | 4.79% | -0.14% [-0.29%, 0.00%] | 0.579 [0.567, 0.591] | 24.1% | 17.4% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.34% [6.04%, 6.64%] | 1.56% | 6.36% | -0.02% [-0.09%, 0.06%] | 3.40% [3.29%, 3.51%] | 1.25% | 3.41% | -0.01% [-0.14%, 0.11%] | 0.561 [0.547, 0.574] | 14.5% | 10.6% | 0.020% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.42% [3.35%, 3.50%] | 0.78% | 3.45% | -0.03% [-0.05%, -0.01%] | 1.70% [1.67%, 1.74%] | 0.62% | 1.74% | -0.03% [-0.08%, 0.02%] | 0.549 [0.542, 0.555] | 6.3% | 5.4% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.84% [9.42%, 10.26%] | 2.04% | 9.93% | -0.10% [-0.18%, -0.01%] | 4.65% [4.49%, 4.81%] | 1.64% | 4.79% | -0.14% [-0.29%, -0.00%] | 0.579 [0.567, 0.591] | 24.1% | 17.4% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.34% [6.04%, 6.64%] | 1.56% | 6.36% | -0.02% [-0.09%, 0.06%] | 3.40% [3.29%, 3.51%] | 1.25% | 3.41% | -0.01% [-0.15%, 0.12%] | 0.561 [0.547, 0.574] | 14.5% | 10.6% | 0.020% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.42% [3.34%, 3.50%] | 0.78% | 3.45% | -0.03% [-0.05%, -0.00%] | 1.70% [1.67%, 1.74%] | 0.62% | 1.74% | -0.03% [-0.08%, 0.02%] | 0.549 [0.542, 0.555] | 6.3% | 5.4% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.94% [9.51%, 10.37%] | 2.04% | 9.93% | 0.01% [-0.04%, 0.05%] | 4.73% [4.55%, 4.93%] | 1.64% | 4.79% | -0.06% [-0.18%, 0.06%] | 0.577 [0.564, 0.590] | 24.5% | 17.7% | 0.014% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.33% [6.00%, 6.64%] | 1.56% | 6.36% | -0.03% [-0.07%, 0.01%] | 3.45% [3.30%, 3.59%] | 1.25% | 3.41% | 0.04% [-0.05%, 0.13%] | 0.560 [0.547, 0.574] | 14.5% | 10.7% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.44% [3.36%, 3.53%] | 0.78% | 3.45% | -0.01% [-0.02%, 0.00%] | 1.74% [1.69%, 1.79%] | 0.62% | 1.74% | 0.00% [-0.03%, 0.03%] | 0.549 [0.542, 0.556] | 6.3% | 5.4% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.90% [9.58%, 10.24%] | 2.19% | 9.93% | -0.03% [-0.30%, 0.25%] | 5.45% [5.31%, 5.59%] | 1.64% | 4.79% | 0.66% [0.37%, 0.94%] | 0.562 [0.553, 0.571] | 6.3% | 12.2% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 6.69% [6.43%, 6.93%] | 1.67% | 6.36% | 0.33% [0.11%, 0.56%] | 4.02% [3.89%, 4.15%] | 1.25% | 3.41% | 0.61% [0.41%, 0.80%] | 0.548 [0.538, 0.558] | 5.3% | 8.1% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.71% [3.63%, 3.79%] | 0.83% | 3.45% | 0.26% [0.19%, 0.33%] | 2.05% [2.01%, 2.09%] | 0.62% | 1.74% | 0.31% [0.25%, 0.38%] | 0.532 [0.527, 0.538] | 2.2% | 3.6% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.76% [9.37%, 10.17%] | 1.84% | 9.93% | -0.17% [-0.55%, 0.19%] | 5.15% [4.94%, 5.35%] | 1.64% | 4.79% | 0.36% [0.03%, 0.69%] | 0.587 [0.574, 0.600] | 19.8% | 17.9% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.70% [6.43%, 6.96%] | 1.40% | 6.36% | 0.35% [0.05%, 0.63%] | 4.04% [3.84%, 4.23%] | 1.25% | 3.41% | 0.63% [0.36%, 0.90%] | 0.558 [0.544, 0.571] | 11.5% | 9.7% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.58% [3.50%, 3.66%] | 0.70% | 3.45% | 0.13% [0.04%, 0.22%] | 2.03% [1.98%, 2.09%] | 0.62% | 1.74% | 0.30% [0.22%, 0.37%] | 0.547 [0.540, 0.554] | 6.0% | 5.2% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.91% [9.49%, 10.35%] | 2.04% | 9.93% | -0.02% [-0.11%, 0.07%] | 4.61% [4.45%, 4.78%] | 1.64% | 4.79% | -0.18% [-0.40%, 0.03%] | 0.580 [0.568, 0.592] | 24.0% | 17.5% | 0.014% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 6.38% [6.07%, 6.69%] | 1.56% | 6.36% | 0.03% [-0.06%, 0.11%] | 3.44% [3.32%, 3.56%] | 1.25% | 3.41% | 0.03% [-0.14%, 0.20%] | 0.561 [0.549, 0.574] | 13.7% | 10.7% | 0.018% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.43% [3.35%, 3.51%] | 0.78% | 3.45% | -0.02% [-0.05%, 0.01%] | 1.72% [1.69%, 1.76%] | 0.62% | 1.74% | -0.01% [-0.07%, 0.04%] | 0.550 [0.544, 0.557] | 6.4% | 5.4% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 4 with a shuffled-outcome AUC interval excluding 0.5: R1_D60_B validator (0.510), R100_D60_B first_hop_content (0.505), R100_D60_B cred_processor (0.504), R100_D60_B gatekeeper (0.504).

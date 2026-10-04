# Tables

Record-to-device linking with genuine decoys, build run10_no_reg. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | +0.06 [-0.10, +0.23] | +0.21 [-0.06, +0.48] | 39857 |
| First hop, credential | 1 | 60 | -0.01 [-0.14, +0.13] | +0.04 [-0.17, +0.23] | 159428 |
| First hop, content | 1 | 60 | -0.01 [-0.14, +0.13] | +0.04 [-0.16, +0.23] | 159428 |
| Credential processor | 1 | 60 | +0.04 [-0.11, +0.20] | +0.26 [+0.04, +0.48] | 159428 |
| Content server | 1 | 60 | -0.05 [-0.23, +0.13] | +0.01 [-0.19, +0.21] | 79714 |
| Validator | 1 | 60 | -0.05 [-0.19, +0.10] | +0.12 [-0.16, +0.39] | 39857 |
| Gatekeeper | 1 | 60 | -0.02 [-0.14, +0.12] | -0.00 [-0.20, +0.18] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.97% [9.54%, 10.40%] | 2.09% | 9.97% | 0.00% [0.00%, 0.00%] | 4.71% [4.52%, 4.90%] | 1.64% | 4.71% | 0.00% [0.00%, 0.00%] | 0.577 [0.564, 0.589] | 25.1% | 17.7% | 0.003% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.50% [6.19%, 6.80%] | 1.59% | 6.50% | 0.00% [0.00%, 0.00%] | 3.43% [3.25%, 3.61%] | 1.25% | 3.43% | 0.00% [0.00%, 0.00%] | 0.553 [0.539, 0.567] | 14.4% | 10.6% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.53% [3.45%, 3.62%] | 0.79% | 3.53% | 0.00% [0.00%, 0.00%] | 1.76% [1.70%, 1.83%] | 0.62% | 1.76% | 0.00% [0.00%, 0.00%] | 0.549 [0.542, 0.556] | 6.2% | 5.4% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.88% [9.45%, 10.30%] | 2.09% | 9.97% | -0.09% [-0.17%, -0.01%] | 4.65% [4.51%, 4.79%] | 1.64% | 4.71% | -0.06% [-0.18%, 0.07%] | 0.579 [0.568, 0.590] | 25.5% | 17.9% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.52% [6.22%, 6.83%] | 1.59% | 6.50% | 0.02% [-0.05%, 0.09%] | 3.47% [3.36%, 3.60%] | 1.25% | 3.43% | 0.04% [-0.07%, 0.15%] | 0.555 [0.542, 0.567] | 14.4% | 10.6% | 0.021% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.50% [3.43%, 3.58%] | 0.79% | 3.53% | -0.03% [-0.06%, -0.01%] | 1.73% [1.70%, 1.76%] | 0.62% | 1.76% | -0.03% [-0.09%, 0.02%] | 0.551 [0.544, 0.557] | 6.2% | 5.4% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.88% [9.47%, 10.29%] | 2.09% | 9.97% | -0.09% [-0.17%, -0.01%] | 4.65% [4.51%, 4.79%] | 1.64% | 4.71% | -0.06% [-0.19%, 0.07%] | 0.579 [0.568, 0.590] | 25.5% | 17.9% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.52% [6.22%, 6.82%] | 1.59% | 6.50% | 0.02% [-0.05%, 0.09%] | 3.47% [3.35%, 3.59%] | 1.25% | 3.43% | 0.04% [-0.07%, 0.16%] | 0.555 [0.542, 0.567] | 14.4% | 10.6% | 0.021% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.50% [3.42%, 3.58%] | 0.79% | 3.53% | -0.03% [-0.05%, -0.01%] | 1.73% [1.70%, 1.76%] | 0.62% | 1.76% | -0.03% [-0.09%, 0.02%] | 0.551 [0.544, 0.557] | 6.2% | 5.4% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.95% [9.53%, 10.36%] | 2.09% | 9.97% | -0.01% [-0.06%, 0.03%] | 4.74% [4.57%, 4.92%] | 1.64% | 4.71% | 0.04% [-0.07%, 0.14%] | 0.578 [0.566, 0.590] | 25.3% | 17.9% | 0.001% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 6.48% [6.17%, 6.79%] | 1.59% | 6.50% | -0.01% [-0.05%, 0.02%] | 3.41% [3.26%, 3.57%] | 1.25% | 3.43% | -0.02% [-0.10%, 0.06%] | 0.555 [0.541, 0.569] | 14.2% | 10.5% | 0.019% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.53% [3.45%, 3.61%] | 0.79% | 3.53% | -0.00% [-0.01%, 0.01%] | 1.77% [1.71%, 1.82%] | 0.62% | 1.76% | 0.00% [-0.03%, 0.03%] | 0.549 [0.542, 0.556] | 6.3% | 5.4% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.79% [9.46%, 10.12%] | 2.22% | 9.97% | -0.18% [-0.44%, 0.06%] | 5.34% [5.20%, 5.50%] | 1.64% | 4.71% | 0.64% [0.39%, 0.88%] | 0.562 [0.553, 0.571] | 7.2% | 12.5% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 6.73% [6.46%, 6.99%] | 1.69% | 6.50% | 0.23% [0.02%, 0.44%] | 4.02% [3.89%, 4.16%] | 1.25% | 3.43% | 0.59% [0.38%, 0.81%] | 0.544 [0.535, 0.554] | 3.8% | 7.1% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.69% [3.62%, 3.77%] | 0.84% | 3.53% | 0.16% [0.09%, 0.23%] | 2.04% [2.00%, 2.09%] | 0.62% | 1.76% | 0.28% [0.21%, 0.35%] | 0.536 [0.531, 0.540] | 2.1% | 3.5% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.47% [9.07%, 9.88%] | 1.88% | 9.97% | -0.50% [-0.86%, -0.17%] | 4.94% [4.72%, 5.17%] | 1.64% | 4.71% | 0.24% [-0.04%, 0.51%] | 0.589 [0.576, 0.602] | 22.3% | 17.9% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.38% [6.12%, 6.66%] | 1.43% | 6.50% | -0.12% [-0.41%, 0.14%] | 3.96% [3.78%, 4.15%] | 1.25% | 3.43% | 0.53% [0.27%, 0.80%] | 0.556 [0.543, 0.569] | 10.8% | 9.2% | 0.017% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.47% [3.39%, 3.55%] | 0.71% | 3.53% | -0.07% [-0.15%, 0.02%] | 1.97% [1.91%, 2.03%] | 0.62% | 1.76% | 0.20% [0.12%, 0.29%] | 0.545 [0.538, 0.551] | 5.3% | 5.0% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.93% [9.51%, 10.37%] | 2.09% | 9.97% | -0.04% [-0.13%, 0.06%] | 4.70% [4.56%, 4.85%] | 1.64% | 4.71% | -0.01% [-0.18%, 0.17%] | 0.580 [0.568, 0.592] | 25.3% | 18.1% | 0.000% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 6.52% [6.21%, 6.82%] | 1.59% | 6.50% | 0.02% [-0.06%, 0.09%] | 3.49% [3.37%, 3.62%] | 1.25% | 3.43% | 0.06% [-0.10%, 0.22%] | 0.554 [0.541, 0.567] | 13.3% | 10.4% | 0.018% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.50% [3.41%, 3.58%] | 0.79% | 3.53% | -0.03% [-0.06%, -0.01%] | 1.78% [1.75%, 1.82%] | 0.62% | 1.76% | 0.02% [-0.03%, 0.07%] | 0.551 [0.545, 0.557] | 6.2% | 5.4% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R100_D60_B first_hop_cred (0.506), R100_D60_B first_hop_content (0.506).

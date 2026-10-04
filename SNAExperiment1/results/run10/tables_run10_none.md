# Tables

Record-to-device linking with genuine decoys, build run10_none. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | +1.46 [+1.16, +1.76] | +1.74 [+1.41, +2.05] | 39857 |
| First hop, credential | 1 | 60 | +1.48 [+1.19, +1.77] | +1.60 [+1.38, +1.82] | 159428 |
| First hop, content | 1 | 60 | +1.48 [+1.20, +1.75] | +1.60 [+1.36, +1.81] | 159428 |
| Credential processor | 1 | 60 | +1.47 [+1.17, +1.76] | +1.66 [+1.39, +1.94] | 159428 |
| Content server | 1 | 60 | +1.67 [+1.42, +1.91] | +1.41 [+1.17, +1.63] | 79714 |
| Validator | 1 | 60 | +3.03 [+2.74, +3.31] | +2.58 [+2.25, +2.90] | 39857 |
| Gatekeeper | 1 | 60 | +1.47 [+1.20, +1.75] | +1.26 [+1.04, +1.48] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 11.37% [10.97%, 11.79%] | 2.43% | 11.37% | 0.00% [0.00%, 0.00%] | 6.23% [6.01%, 6.48%] | 1.64% | 6.23% | 0.00% [0.00%, 0.00%] | 0.586 [0.576, 0.596] | 24.8% | 21.0% | 0.033% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 7.77% [7.46%, 8.08%] | 1.85% | 7.77% | 0.00% [0.00%, 0.00%] | 4.32% [4.11%, 4.51%] | 1.25% | 4.32% | 0.00% [0.00%, 0.00%] | 0.562 [0.551, 0.574] | 13.7% | 11.9% | 0.022% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 4.21% [4.13%, 4.30%] | 0.92% | 4.21% | 0.00% [0.00%, 0.00%] | 2.35% [2.28%, 2.43%] | 0.62% | 2.35% | 0.00% [0.00%, 0.00%] | 0.559 [0.553, 0.564] | 7.8% | 6.7% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 11.36% [10.95%, 11.75%] | 2.43% | 11.37% | -0.01% [-0.09%, 0.07%] | 6.21% [6.04%, 6.38%] | 1.64% | 6.23% | -0.02% [-0.17%, 0.12%] | 0.585 [0.575, 0.594] | 24.8% | 21.1% | 0.026% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 7.79% [7.50%, 8.11%] | 1.85% | 7.77% | 0.02% [-0.06%, 0.11%] | 4.42% [4.30%, 4.54%] | 1.25% | 4.32% | 0.10% [-0.04%, 0.23%] | 0.562 [0.551, 0.572] | 14.8% | 12.0% | 0.021% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 4.24% [4.16%, 4.32%] | 0.92% | 4.21% | 0.03% [0.00%, 0.06%] | 2.32% [2.29%, 2.36%] | 0.62% | 2.35% | -0.03% [-0.09%, 0.03%] | 0.555 [0.550, 0.560] | 7.9% | 6.7% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 11.36% [10.98%, 11.75%] | 2.43% | 11.37% | -0.01% [-0.08%, 0.07%] | 6.21% [6.03%, 6.38%] | 1.64% | 6.23% | -0.02% [-0.17%, 0.12%] | 0.585 [0.575, 0.594] | 24.8% | 21.1% | 0.026% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 7.79% [7.50%, 8.06%] | 1.85% | 7.77% | 0.02% [-0.06%, 0.11%] | 4.42% [4.30%, 4.54%] | 1.25% | 4.32% | 0.10% [-0.03%, 0.24%] | 0.562 [0.551, 0.572] | 14.8% | 12.0% | 0.021% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 4.24% [4.16%, 4.32%] | 0.92% | 4.21% | 0.03% [0.00%, 0.06%] | 2.32% [2.29%, 2.36%] | 0.62% | 2.35% | -0.03% [-0.09%, 0.03%] | 0.555 [0.550, 0.560] | 7.9% | 6.7% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 11.38% [10.97%, 11.79%] | 2.43% | 11.37% | 0.01% [-0.04%, 0.05%] | 6.14% [5.94%, 6.36%] | 1.64% | 6.23% | -0.09% [-0.18%, 0.01%] | 0.587 [0.577, 0.597] | 25.2% | 21.0% | 0.032% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 7.76% [7.44%, 8.06%] | 1.85% | 7.77% | -0.01% [-0.05%, 0.03%] | 4.31% [4.14%, 4.48%] | 1.25% | 4.32% | -0.01% [-0.10%, 0.08%] | 0.562 [0.550, 0.573] | 14.3% | 11.9% | 0.022% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 4.21% [4.12%, 4.30%] | 0.92% | 4.21% | -0.00% [-0.01%, 0.01%] | 2.33% [2.26%, 2.39%] | 0.62% | 2.35% | -0.02% [-0.05%, 0.01%] | 0.559 [0.554, 0.565] | 7.8% | 6.6% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 11.50% [11.15%, 11.86%] | 2.61% | 11.37% | 0.13% [-0.07%, 0.33%] | 6.75% [6.54%, 6.94%] | 1.64% | 6.23% | 0.51% [0.21%, 0.81%] | 0.577 [0.569, 0.585] | 16.1% | 18.3% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 8.07% [7.80%, 8.32%] | 1.99% | 7.77% | 0.30% [0.08%, 0.51%] | 5.14% [5.00%, 5.28%] | 1.25% | 4.32% | 0.82% [0.57%, 1.06%] | 0.556 [0.547, 0.566] | 9.6% | 10.2% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 4.46% [4.38%, 4.53%] | 0.99% | 4.21% | 0.25% [0.17%, 0.32%] | 2.57% [2.52%, 2.61%] | 0.62% | 2.35% | 0.22% [0.13%, 0.30%] | 0.548 [0.544, 0.552] | 3.9% | 5.3% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 12.54% [12.14%, 12.95%] | 2.31% | 11.37% | 1.17% [0.82%, 1.51%] | 7.40% [7.16%, 7.64%] | 1.64% | 6.23% | 1.17% [0.81%, 1.53%] | 0.593 [0.583, 0.602] | 27.3% | 23.9% | 0.048% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 8.68% [8.37%, 9.02%] | 1.76% | 7.77% | 0.91% [0.58%, 1.23%] | 5.70% [5.46%, 5.94%] | 1.25% | 4.32% | 1.38% [1.07%, 1.70%] | 0.573 [0.562, 0.584] | 13.9% | 15.0% | 0.000% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 4.86% [4.77%, 4.94%] | 0.88% | 4.21% | 0.64% [0.54%, 0.74%] | 2.85% [2.79%, 2.91%] | 0.62% | 2.35% | 0.50% [0.40%, 0.59%] | 0.561 [0.555, 0.566] | 8.0% | 7.7% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 11.42% [11.03%, 11.83%] | 2.43% | 11.37% | 0.05% [-0.05%, 0.16%] | 5.96% [5.79%, 6.12%] | 1.64% | 6.23% | -0.28% [-0.49%, -0.06%] | 0.583 [0.573, 0.592] | 23.4% | 20.6% | 0.028% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 7.67% [7.39%, 7.95%] | 1.85% | 7.77% | -0.10% [-0.20%, -0.00%] | 4.45% [4.31%, 4.59%] | 1.25% | 4.32% | 0.13% [-0.06%, 0.32%] | 0.561 [0.549, 0.572] | 13.7% | 12.0% | 0.020% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 4.22% [4.13%, 4.30%] | 0.92% | 4.21% | 0.01% [-0.02%, 0.04%] | 2.29% [2.24%, 2.33%] | 0.62% | 2.35% | -0.06% [-0.14%, 0.00%] | 0.558 [0.553, 0.563] | 7.7% | 6.6% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 3 with a shuffled-outcome AUC interval excluding 0.5: R1_D60_B first_hop_cred (0.505), R1_D60_B content_server (0.493), R100_D60_B first_hop_cred (0.503).

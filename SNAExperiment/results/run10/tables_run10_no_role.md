# Tables

Record-to-device linking with genuine decoys, build run10_no_role. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | +0.70 [+0.37, +1.05] | +1.02 [+0.71, +1.33] | 39857 |
| First hop, credential | 1 | 60 | +0.73 [+0.42, +1.04] | +0.81 [+0.60, +1.01] | 159428 |
| First hop, content | 1 | 60 | +0.73 [+0.43, +1.02] | +0.81 [+0.60, +1.01] | 159428 |
| Credential processor | 1 | 60 | +0.73 [+0.39, +1.07] | +0.97 [+0.70, +1.25] | 159428 |
| Content server | 1 | 60 | +1.45 [+1.19, +1.71] | +1.17 [+0.95, +1.41] | 79714 |
| Validator | 1 | 60 | +3.10 [+2.79, +3.42] | +4.03 [+3.69, +4.36] | 39857 |
| Gatekeeper | 1 | 60 | +0.65 [+0.34, +0.97] | +0.64 [+0.40, +0.86] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 10.61% [10.18%, 11.04%] | 2.14% | 10.61% | 0.00% [0.00%, 0.00%] | 5.51% [5.29%, 5.74%] | 1.64% | 5.51% | 0.00% [0.00%, 0.00%] | 0.592 [0.581, 0.603] | 26.1% | 19.8% | 0.018% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 7.33% [7.02%, 7.66%] | 1.63% | 7.33% | 0.00% [0.00%, 0.00%] | 4.17% [3.95%, 4.37%] | 1.25% | 4.17% | 0.00% [0.00%, 0.00%] | 0.551 [0.538, 0.564] | 13.2% | 11.8% | 0.022% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.91% [3.83%, 4.00%] | 0.81% | 3.91% | 0.00% [0.00%, 0.00%] | 2.04% [1.98%, 2.10%] | 0.62% | 2.04% | 0.00% [0.00%, 0.00%] | 0.552 [0.546, 0.559] | 6.8% | 5.8% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 10.61% [10.16%, 11.03%] | 2.14% | 10.61% | 0.01% [-0.08%, 0.09%] | 5.42% [5.25%, 5.58%] | 1.64% | 5.51% | -0.09% [-0.24%, 0.05%] | 0.591 [0.581, 0.602] | 26.3% | 19.9% | 0.021% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 7.30% [7.00%, 7.62%] | 1.63% | 7.33% | -0.03% [-0.10%, 0.05%] | 4.07% [3.93%, 4.21%] | 1.25% | 4.17% | -0.09% [-0.21%, 0.03%] | 0.553 [0.542, 0.565] | 13.4% | 11.3% | 0.022% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.90% [3.82%, 3.98%] | 0.81% | 3.91% | -0.01% [-0.03%, 0.01%] | 2.00% [1.97%, 2.04%] | 0.62% | 2.04% | -0.04% [-0.08%, 0.00%] | 0.551 [0.546, 0.557] | 6.8% | 5.9% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 10.61% [10.20%, 11.03%] | 2.14% | 10.61% | 0.01% [-0.08%, 0.09%] | 5.42% [5.24%, 5.58%] | 1.64% | 5.51% | -0.09% [-0.24%, 0.05%] | 0.591 [0.581, 0.602] | 26.3% | 19.9% | 0.021% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 7.30% [6.98%, 7.60%] | 1.63% | 7.33% | -0.03% [-0.09%, 0.05%] | 4.07% [3.92%, 4.22%] | 1.25% | 4.17% | -0.09% [-0.22%, 0.02%] | 0.553 [0.542, 0.565] | 13.4% | 11.3% | 0.022% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.90% [3.82%, 3.98%] | 0.81% | 3.91% | -0.01% [-0.03%, 0.01%] | 2.00% [1.97%, 2.04%] | 0.62% | 2.04% | -0.04% [-0.08%, 0.01%] | 0.551 [0.546, 0.557] | 6.8% | 5.9% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 10.64% [10.20%, 11.08%] | 2.14% | 10.61% | 0.03% [-0.02%, 0.08%] | 5.46% [5.25%, 5.67%] | 1.64% | 5.51% | -0.06% [-0.16%, 0.04%] | 0.591 [0.580, 0.601] | 25.9% | 19.9% | 0.019% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 7.29% [6.97%, 7.59%] | 1.63% | 7.33% | -0.04% [-0.08%, 0.00%] | 4.21% [4.01%, 4.40%] | 1.25% | 4.17% | 0.04% [-0.03%, 0.11%] | 0.553 [0.540, 0.566] | 13.4% | 11.5% | 0.025% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.91% [3.83%, 4.00%] | 0.81% | 3.91% | -0.00% [-0.01%, 0.01%] | 2.03% [1.98%, 2.09%] | 0.62% | 2.04% | -0.01% [-0.03%, 0.02%] | 0.552 [0.546, 0.558] | 6.8% | 5.8% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 11.29% [10.95%, 11.65%] | 2.46% | 10.61% | 0.68% [0.43%, 0.92%] | 6.51% [6.33%, 6.69%] | 1.64% | 5.51% | 1.00% [0.72%, 1.29%] | 0.560 [0.551, 0.570] | 16.7% | 17.7% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 8.10% [7.85%, 8.36%] | 1.87% | 7.33% | 0.77% [0.55%, 0.99%] | 5.07% [4.93%, 5.22%] | 1.25% | 4.17% | 0.91% [0.67%, 1.13%] | 0.556 [0.546, 0.565] | 10.3% | 10.3% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 4.33% [4.26%, 4.41%] | 0.94% | 3.91% | 0.42% [0.35%, 0.50%] | 2.52% [2.47%, 2.56%] | 0.62% | 2.04% | 0.48% [0.41%, 0.55%] | 0.545 [0.540, 0.550] | 3.3% | 5.0% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 12.62% [12.19%, 13.04%] | 2.34% | 10.61% | 2.01% [1.58%, 2.42%] | 8.85% [8.61%, 9.09%] | 1.64% | 5.51% | 3.34% [3.02%, 3.67%] | 0.595 [0.584, 0.606] | 27.3% | 23.0% | 0.073% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 8.82% [8.54%, 9.10%] | 1.78% | 7.33% | 1.49% [1.16%, 1.81%] | 6.87% [6.63%, 7.14%] | 1.25% | 4.17% | 2.71% [2.39%, 3.04%] | 0.564 [0.553, 0.574] | 14.9% | 14.0% | 0.000% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 4.95% [4.85%, 5.05%] | 0.89% | 3.91% | 1.04% [0.92%, 1.15%] | 3.39% [3.32%, 3.46%] | 0.62% | 2.04% | 1.35% [1.25%, 1.45%] | 0.557 [0.552, 0.563] | 8.8% | 8.2% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 10.60% [10.19%, 11.05%] | 2.14% | 10.61% | -0.00% [-0.11%, 0.10%] | 5.33% [5.15%, 5.51%] | 1.64% | 5.51% | -0.18% [-0.36%, 0.01%] | 0.590 [0.579, 0.600] | 25.8% | 19.7% | 0.019% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 7.29% [6.98%, 7.60%] | 1.63% | 7.33% | -0.03% [-0.12%, 0.05%] | 4.09% [3.96%, 4.24%] | 1.25% | 4.17% | -0.08% [-0.24%, 0.10%] | 0.554 [0.541, 0.567] | 13.7% | 11.4% | 0.023% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.90% [3.82%, 3.98%] | 0.81% | 3.91% | -0.01% [-0.04%, 0.01%] | 2.00% [1.96%, 2.04%] | 0.62% | 2.04% | -0.04% [-0.09%, 0.01%] | 0.554 [0.548, 0.560] | 6.8% | 5.8% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 1 with a shuffled-outcome AUC interval excluding 0.5: R100_D60_B gatekeeper (0.504).

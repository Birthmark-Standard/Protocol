# Tables

Record-to-device linking with genuine decoys, build run10_relay180. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | -0.62 [-0.83, -0.41] | -0.70 [-0.97, -0.43] | 39857 |
| First hop, credential | 1 | 60 | -0.72 [-0.89, -0.56] | -0.70 [-0.88, -0.52] | 159428 |
| First hop, content | 1 | 60 | -0.72 [-0.88, -0.57] | -0.70 [-0.88, -0.51] | 159428 |
| Credential processor | 1 | 60 | -0.68 [-0.87, -0.48] | -0.65 [-0.86, -0.42] | 159428 |
| Content server | 1 | 60 | -0.98 [-1.20, -0.76] | -0.85 [-1.05, -0.64] | 79714 |
| Validator | 1 | 60 | -0.60 [-0.86, -0.33] | -0.52 [-0.79, -0.25] | 39857 |
| Gatekeeper | 1 | 60 | -0.71 [-0.88, -0.53] | -0.75 [-0.93, -0.57] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.29% [8.87%, 9.72%] | 1.87% | 9.29% | 0.00% [0.00%, 0.00%] | 3.80% [3.60%, 4.00%] | 1.64% | 3.80% | 0.00% [0.00%, 0.00%] | 0.581 [0.567, 0.595] | 23.6% | 16.2% | 0.013% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 5.89% [5.58%, 6.19%] | 1.43% | 5.89% | 0.00% [0.00%, 0.00%] | 2.93% [2.77%, 3.10%] | 1.25% | 2.93% | 0.00% [0.00%, 0.00%] | 0.552 [0.537, 0.567] | 13.4% | 9.7% | 0.012% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.18% [3.11%, 3.26%] | 0.71% | 3.18% | 0.00% [0.00%, 0.00%] | 1.51% [1.46%, 1.56%] | 0.62% | 1.51% | 0.00% [0.00%, 0.00%] | 0.550 [0.543, 0.557] | 5.5% | 4.8% | 0.000% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.16% [8.74%, 9.57%] | 1.87% | 9.29% | -0.13% [-0.23%, -0.02%] | 3.91% [3.79%, 4.04%] | 1.64% | 3.80% | 0.12% [-0.03%, 0.26%] | 0.580 [0.567, 0.592] | 22.0% | 16.2% | 0.014% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 5.87% [5.59%, 6.17%] | 1.43% | 5.89% | -0.02% [-0.10%, 0.05%] | 2.93% [2.82%, 3.03%] | 1.25% | 2.93% | 0.00% [-0.14%, 0.13%] | 0.555 [0.542, 0.568] | 13.2% | 9.8% | 0.015% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.16% [3.09%, 3.23%] | 0.71% | 3.18% | -0.02% [-0.05%, 0.01%] | 1.46% [1.43%, 1.49%] | 0.62% | 1.51% | -0.05% [-0.09%, 0.00%] | 0.549 [0.542, 0.555] | 5.8% | 4.8% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.16% [8.75%, 9.56%] | 1.87% | 9.29% | -0.13% [-0.23%, -0.03%] | 3.91% [3.79%, 4.04%] | 1.64% | 3.80% | 0.12% [-0.03%, 0.26%] | 0.580 [0.567, 0.592] | 22.0% | 16.2% | 0.014% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 5.87% [5.58%, 6.16%] | 1.43% | 5.89% | -0.02% [-0.10%, 0.05%] | 2.93% [2.83%, 3.03%] | 1.25% | 2.93% | 0.00% [-0.13%, 0.14%] | 0.555 [0.542, 0.568] | 13.2% | 9.8% | 0.015% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.16% [3.09%, 3.24%] | 0.71% | 3.18% | -0.02% [-0.05%, 0.01%] | 1.46% [1.44%, 1.49%] | 0.62% | 1.51% | -0.05% [-0.09%, 0.00%] | 0.549 [0.542, 0.555] | 5.8% | 4.8% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.23% [8.80%, 9.66%] | 1.87% | 9.29% | -0.05% [-0.11%, 0.00%] | 3.83% [3.66%, 4.00%] | 1.64% | 3.80% | 0.04% [-0.06%, 0.14%] | 0.582 [0.569, 0.595] | 23.4% | 16.1% | 0.014% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 5.89% [5.59%, 6.19%] | 1.43% | 5.89% | -0.00% [-0.03%, 0.04%] | 2.90% [2.75%, 3.05%] | 1.25% | 2.93% | -0.02% [-0.10%, 0.05%] | 0.552 [0.538, 0.567] | 13.6% | 9.8% | 0.014% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 3.18% [3.10%, 3.26%] | 0.71% | 3.18% | -0.00% [-0.01%, 0.01%] | 1.49% [1.45%, 1.54%] | 0.62% | 1.51% | -0.01% [-0.03%, 0.01%] | 0.551 [0.544, 0.558] | 5.5% | 4.8% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.86% [8.53%, 9.19%] | 1.96% | 9.29% | -0.43% [-0.71%, -0.16%] | 4.49% [4.34%, 4.64%] | 1.64% | 3.80% | 0.70% [0.45%, 0.93%] | 0.563 [0.554, 0.572] | 7.7% | 10.7% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 5.88% [5.63%, 6.11%] | 1.50% | 5.89% | -0.01% [-0.22%, 0.20%] | 3.30% [3.17%, 3.43%] | 1.25% | 2.93% | 0.37% [0.17%, 0.59%] | 0.542 [0.532, 0.552] | 5.3% | 6.4% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.20% [3.13%, 3.27%] | 0.75% | 3.18% | 0.02% [-0.05%, 0.09%] | 1.68% [1.64%, 1.72%] | 0.62% | 1.51% | 0.18% [0.12%, 0.24%] | 0.532 [0.527, 0.538] | 2.3% | 3.1% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.92% [8.53%, 9.30%] | 1.74% | 9.29% | -0.37% [-0.78%, -0.00%] | 4.30% [4.08%, 4.50%] | 1.64% | 3.80% | 0.50% [0.23%, 0.79%] | 0.577 [0.564, 0.590] | 20.8% | 15.0% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 6.00% [5.74%, 6.26%] | 1.32% | 5.89% | 0.10% [-0.18%, 0.37%] | 3.62% [3.46%, 3.79%] | 1.25% | 2.93% | 0.69% [0.44%, 0.94%] | 0.564 [0.549, 0.578] | 10.6% | 8.5% | 0.000% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 3.24% [3.16%, 3.33%] | 0.66% | 3.18% | 0.06% [-0.03%, 0.15%] | 1.88% [1.82%, 1.94%] | 0.62% | 1.51% | 0.37% [0.29%, 0.45%] | 0.549 [0.542, 0.555] | 6.2% | 4.8% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 9.24% [8.83%, 9.68%] | 1.87% | 9.29% | -0.04% [-0.16%, 0.07%] | 3.95% [3.79%, 4.10%] | 1.64% | 3.80% | 0.15% [-0.03%, 0.34%] | 0.581 [0.568, 0.595] | 21.9% | 16.8% | 0.000% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 5.88% [5.59%, 6.18%] | 1.43% | 5.89% | -0.01% [-0.10%, 0.07%] | 2.93% [2.82%, 3.05%] | 1.25% | 2.93% | 0.01% [-0.14%, 0.16%] | 0.554 [0.540, 0.568] | 13.4% | 9.8% | 0.014% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 3.17% [3.09%, 3.25%] | 0.71% | 3.18% | -0.01% [-0.04%, 0.01%] | 1.48% [1.44%, 1.52%] | 0.62% | 1.51% | -0.02% [-0.07%, 0.02%] | 0.551 [0.544, 0.558] | 5.6% | 4.9% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 3 with a shuffled-outcome AUC interval excluding 0.5: R100_D60_B first_hop_cred (0.504), R100_D60_B first_hop_content (0.504), R100_D60_B validator (0.513).

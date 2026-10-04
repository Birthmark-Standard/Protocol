# Tables

Record-to-device linking with genuine decoys, build run10_role360. Measured end-to-end delay D = 1036.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| Baseline | 1 | 60 | -1.33 [-1.64, -1.01] | -0.94 [-1.23, -0.66] | 39857 |
| First hop, credential | 1 | 60 | -1.28 [-1.56, -1.00] | -1.06 [-1.26, -0.85] | 159428 |
| First hop, content | 1 | 60 | -1.28 [-1.54, -1.01] | -1.06 [-1.26, -0.86] | 159428 |
| Credential processor | 1 | 60 | -1.32 [-1.60, -1.05] | -0.89 [-1.14, -0.63] | 159428 |
| Content server | 1 | 60 | -1.41 [-1.63, -1.18] | -1.12 [-1.31, -0.90] | 79714 |
| Validator | 1 | 60 | -1.58 [-1.88, -1.27] | -2.28 [-2.53, -2.03] | 39857 |
| Gatekeeper | 1 | 60 | -1.39 [-1.66, -1.10] | -1.26 [-1.45, -1.06] | 119571 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.58% [8.19%, 8.97%] | 1.81% | 8.58% | 0.00% [0.00%, 0.00%] | 3.55% [3.37%, 3.74%] | 1.64% | 3.55% | 0.00% [0.00%, 0.00%] | 0.588 [0.573, 0.603] | 19.0% | 16.7% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 5.04% [4.77%, 5.32%] | 1.38% | 5.04% | 0.00% [0.00%, 0.00%] | 2.54% [2.38%, 2.70%] | 1.25% | 2.54% | 0.00% [0.00%, 0.00%] | 0.562 [0.547, 0.578] | 12.0% | 9.2% | 0.000% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 2.91% [2.82%, 2.99%] | 0.69% | 2.91% | 0.00% [0.00%, 0.00%] | 1.31% [1.26%, 1.37%] | 0.62% | 1.31% | 0.00% [0.00%, 0.00%] | 0.547 [0.539, 0.555] | 4.9% | 4.3% | 0.001% | 200 | 207570 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.61% [8.21%, 8.99%] | 1.81% | 8.58% | 0.03% [-0.04%, 0.11%] | 3.56% [3.41%, 3.70%] | 1.64% | 3.55% | 0.00% [-0.12%, 0.12%] | 0.588 [0.574, 0.601] | 19.4% | 16.9% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 5.08% [4.82%, 5.36%] | 1.38% | 5.04% | 0.03% [-0.03%, 0.10%] | 2.58% [2.48%, 2.68%] | 1.25% | 2.54% | 0.04% [-0.07%, 0.15%] | 0.557 [0.543, 0.572] | 11.7% | 9.0% | 0.000% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 2.89% [2.82%, 2.97%] | 0.69% | 2.91% | -0.02% [-0.04%, 0.01%] | 1.31% [1.28%, 1.34%] | 0.62% | 1.31% | -0.01% [-0.05%, 0.04%] | 0.546 [0.539, 0.552] | 5.0% | 4.3% | 0.000% | 200 | 830280 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.61% [8.21%, 8.99%] | 1.81% | 8.58% | 0.03% [-0.05%, 0.11%] | 3.56% [3.42%, 3.69%] | 1.64% | 3.55% | 0.00% [-0.12%, 0.12%] | 0.588 [0.574, 0.601] | 19.4% | 16.9% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 5.08% [4.80%, 5.34%] | 1.38% | 5.04% | 0.03% [-0.03%, 0.10%] | 2.58% [2.48%, 2.68%] | 1.25% | 2.54% | 0.04% [-0.06%, 0.15%] | 0.557 [0.543, 0.572] | 11.7% | 9.0% | 0.000% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 2.89% [2.81%, 2.97%] | 0.69% | 2.91% | -0.02% [-0.04%, 0.01%] | 1.31% [1.28%, 1.33%] | 0.62% | 1.31% | -0.01% [-0.05%, 0.04%] | 0.546 [0.539, 0.552] | 5.0% | 4.3% | 0.000% | 200 | 830280 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.59% [8.20%, 9.01%] | 1.81% | 8.58% | 0.01% [-0.05%, 0.06%] | 3.59% [3.41%, 3.77%] | 1.64% | 3.55% | 0.04% [-0.05%, 0.13%] | 0.588 [0.574, 0.602] | 18.9% | 16.6% | 0.000% | 200 | 159428 |
| R = 20, 60 decoys, bundling on | 5.04% [4.75%, 5.32%] | 1.38% | 5.04% | 0.00% [-0.04%, 0.04%] | 2.55% [2.42%, 2.68%] | 1.25% | 2.54% | 0.01% [-0.06%, 0.07%] | 0.560 [0.545, 0.576] | 11.6% | 9.1% | 0.000% | 200 | 166912 |
| R = 100, 60 decoys, bundling on | 2.90% [2.81%, 2.99%] | 0.69% | 2.91% | -0.00% [-0.01%, 0.01%] | 1.33% [1.28%, 1.37%] | 0.62% | 1.31% | 0.01% [-0.01%, 0.03%] | 0.547 [0.540, 0.555] | 5.0% | 4.3% | 0.000% | 200 | 830280 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.43% [8.12%, 8.73%] | 1.94% | 8.58% | -0.15% [-0.41%, 0.12%] | 4.22% [4.07%, 4.38%] | 1.64% | 3.55% | 0.67% [0.43%, 0.91%] | 0.552 [0.543, 0.561] | 5.8% | 7.7% | 0.000% | 200 | 79714 |
| R = 20, 60 decoys, bundling on | 5.55% [5.33%, 5.78%] | 1.48% | 5.04% | 0.51% [0.31%, 0.69%] | 3.11% [3.00%, 3.22%] | 1.25% | 2.54% | 0.57% [0.40%, 0.75%] | 0.525 [0.515, 0.535] | 2.8% | 3.8% | 0.000% | 200 | 83456 |
| R = 100, 60 decoys, bundling on | 3.10% [3.04%, 3.17%] | 0.74% | 2.91% | 0.20% [0.13%, 0.27%] | 1.61% [1.57%, 1.65%] | 0.62% | 1.31% | 0.30% [0.24%, 0.35%] | 0.505 [0.500, 0.511] | 1.6% | 1.8% | 0.000% | 200 | 415140 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 7.94% [7.54%, 8.35%] | 1.66% | 8.58% | -0.64% [-0.96%, -0.30%] | 2.54% [2.39%, 2.69%] | 1.64% | 3.55% | -1.01% [-1.25%, -0.78%] | 0.569 [0.555, 0.583] | 22.3% | 15.2% | 0.000% | 200 | 39857 |
| R = 20, 60 decoys, bundling on | 4.87% [4.60%, 5.13%] | 1.26% | 5.04% | -0.17% [-0.41%, 0.06%] | 1.97% [1.85%, 2.11%] | 1.25% | 2.54% | -0.57% [-0.75%, -0.37%] | 0.554 [0.537, 0.570] | 9.4% | 7.3% | 0.002% | 200 | 41728 |
| R = 100, 60 decoys, bundling on | 2.63% [2.55%, 2.71%] | 0.63% | 2.91% | -0.28% [-0.36%, -0.20%] | 1.07% [1.03%, 1.11%] | 0.62% | 1.31% | -0.24% [-0.31%, -0.18%] | 0.543 [0.535, 0.551] | 3.6% | 3.6% | 0.000% | 200 | 207570 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 60 decoys, bundling on | 8.56% [8.17%, 8.98%] | 1.81% | 8.58% | -0.02% [-0.13%, 0.08%] | 3.44% [3.31%, 3.58%] | 1.64% | 3.55% | -0.11% [-0.28%, 0.05%] | 0.584 [0.570, 0.597] | 19.5% | 16.5% | 0.000% | 200 | 119571 |
| R = 20, 60 decoys, bundling on | 5.18% [4.89%, 5.44%] | 1.38% | 5.04% | 0.13% [0.06%, 0.21%] | 2.62% [2.51%, 2.73%] | 1.25% | 2.54% | 0.08% [-0.07%, 0.23%] | 0.557 [0.542, 0.572] | 12.1% | 9.3% | 0.000% | 200 | 125184 |
| R = 100, 60 decoys, bundling on | 2.91% [2.83%, 2.99%] | 0.69% | 2.91% | -0.00% [-0.03%, 0.02%] | 1.33% [1.29%, 1.36%] | 0.62% | 1.31% | 0.02% [-0.04%, 0.06%] | 0.547 [0.540, 0.554] | 5.0% | 4.3% | 0.000% | 200 | 622710 |

## Outcome-shuffle control (stable cells)

21 stable cells; 1 with a shuffled-outcome AUC interval excluding 0.5: R1_D60_B validator (0.512).

# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with the device's content-channel hold and the content servers' own hold stretched 2 times and every relay hop's hold stretched 1.5 times on every path. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Volume

| L (in flight) | Captures per second | Captures per day | Devices (20-minute interval) |
|---|---|---|---|
| 1 | 0.0016 | 138 | 1.9 |
| 15 | 0.0240 | 2,072 | 28.8 |
| 21 | 0.0336 | 2,900 | 40.3 |
| 31 | 0.0496 | 4,282 | 59.5 |
| 35 | 0.0559 | 4,834 | 67.1 |
| 41 | 0.0655 | 5,663 | 78.6 |
| 45 | 0.0719 | 6,215 | 86.3 |
| 50 | 0.0799 | 6,906 | 95.9 |
| 55 | 0.0879 | 7,596 | 105.5 |
| 61 | 0.0975 | 8,425 | 117.0 |
| 70 | 0.1119 | 9,668 | 134.3 |
| 75 | 0.1199 | 10,359 | 143.9 |
| 80 | 0.1279 | 11,049 | 153.5 |
| 90 | 0.1439 | 12,430 | 172.6 |
| 101 | 0.1615 | 13,950 | 193.7 |
| 110 | 0.1758 | 15,193 | 211.0 |
| 115 | 0.1838 | 15,883 | 220.6 |
| 150 | 0.2398 | 20,717 | 287.7 |
| 151 | 0.2414 | 20,855 | 289.7 |
| 165 | 0.2638 | 22,789 | 316.5 |
| 200 | 0.3197 | 27,623 | 383.6 |

## Departure bundle sizes

Postings per 30-second bundle at one gatekeeper, on its own grid, over every run of the cell. Off cells report the bundles the same selections would have formed.

| R | Decoys | Mean per bundle | Empty | Exactly 1 | Fewer than 2 | 1, of non-empty | Postings departing alone | Bundles |
|---|---|---|---|---|---|---|---|---|
| 1 | 40 | 1.97 | 14.0% | 27.4% | 41.5% | 31.9% | 14.0% | 2,501,697 |
| 15 | 40 | 2.65 | 7.0% | 18.8% | 25.8% | 20.2% | 7.1% | 215,400 |
| 50 | 40 | 4.30 | 1.4% | 5.8% | 7.2% | 5.9% | 1.3% | 215,400 |

## Change from the dev200 build on the same records

Accuracy in this build minus accuracy in the dev200 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -0.59 [-0.78, -0.40] | -0.48 [-0.74, -0.24] | 39799 |
| Baseline | 15 | 40 | -0.42 [-0.55, -0.27] | -0.30 [-0.48, -0.12] | 52017 |
| Baseline | 50 | 40 | -0.35 [-0.42, -0.27] | -0.29 [-0.37, -0.21] | 172224 |
| First hop, credential | 1 | 40 | -0.65 [-0.81, -0.47] | -0.56 [-0.74, -0.38] | 159196 |
| First hop, credential | 15 | 40 | -0.48 [-0.60, -0.37] | -0.47 [-0.58, -0.36] | 208068 |
| First hop, credential | 50 | 40 | -0.35 [-0.42, -0.29] | -0.30 [-0.35, -0.26] | 688896 |
| First hop, content | 1 | 40 | -0.65 [-0.82, -0.49] | -0.56 [-0.74, -0.38] | 159196 |
| First hop, content | 15 | 40 | -0.48 [-0.59, -0.36] | -0.47 [-0.58, -0.36] | 208068 |
| First hop, content | 50 | 40 | -0.35 [-0.42, -0.29] | -0.30 [-0.35, -0.26] | 688896 |
| Credential processor | 1 | 40 | -0.62 [-0.80, -0.44] | -0.59 [-0.80, -0.37] | 159196 |
| Credential processor | 15 | 40 | -0.44 [-0.57, -0.31] | -0.27 [-0.41, -0.13] | 208068 |
| Credential processor | 50 | 40 | -0.35 [-0.43, -0.28] | -0.29 [-0.36, -0.22] | 688896 |
| Content server | 1 | 40 | -0.91 [-1.11, -0.69] | -1.03 [-1.22, -0.80] | 79598 |
| Content server | 15 | 40 | -0.77 [-0.93, -0.61] | -0.66 [-0.82, -0.51] | 104034 |
| Content server | 50 | 40 | -0.61 [-0.69, -0.54] | -0.40 [-0.48, -0.34] | 344448 |
| Validator | 1 | 40 | -0.61 [-0.88, -0.35] | -0.10 [-0.32, +0.14] | 39799 |
| Validator | 15 | 40 | -0.32 [-0.50, -0.14] | -0.26 [-0.42, -0.09] | 52017 |
| Validator | 50 | 40 | -0.22 [-0.30, -0.13] | -0.19 [-0.26, -0.11] | 172224 |
| Gatekeeper | 1 | 40 | -0.66 [-0.83, -0.49] | -0.55 [-0.72, -0.37] | 119397 |
| Gatekeeper | 15 | 40 | -0.41 [-0.52, -0.29] | -0.38 [-0.51, -0.26] | 156051 |
| Gatekeeper | 50 | 40 | -0.35 [-0.41, -0.28] | -0.26 [-0.31, -0.20] | 516672 |

## Change from the dev300 build on the same records

Accuracy in this build minus accuracy in the dev300 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | +0.40 [+0.01, +0.79] | +0.57 [+0.30, +0.85] | 39433 |
| Baseline | 15 | 40 | +0.58 [+0.25, +0.94] | +0.48 [+0.29, +0.67] | 46221 |
| Baseline | 50 | 40 | +0.37 [+0.24, +0.50] | +0.28 [+0.20, +0.37] | 153156 |
| First hop, credential | 1 | 40 | +0.43 [+0.07, +0.77] | +0.51 [+0.34, +0.67] | 157732 |
| First hop, credential | 15 | 40 | +0.56 [+0.25, +0.87] | +0.43 [+0.31, +0.55] | 184884 |
| First hop, credential | 50 | 40 | +0.37 [+0.25, +0.48] | +0.24 [+0.19, +0.29] | 612624 |
| First hop, content | 1 | 40 | +0.43 [+0.08, +0.78] | +0.51 [+0.35, +0.69] | 157732 |
| First hop, content | 15 | 40 | +0.56 [+0.24, +0.85] | +0.43 [+0.31, +0.55] | 184884 |
| First hop, content | 50 | 40 | +0.37 [+0.24, +0.49] | +0.24 [+0.18, +0.29] | 612624 |
| Credential processor | 1 | 40 | +0.40 [+0.01, +0.77] | +0.56 [+0.34, +0.77] | 157732 |
| Credential processor | 15 | 40 | +0.56 [+0.23, +0.88] | +0.47 [+0.29, +0.66] | 184884 |
| Credential processor | 50 | 40 | +0.36 [+0.24, +0.49] | +0.30 [+0.22, +0.38] | 612624 |
| Content server | 1 | 40 | -0.56 [-1.38, +0.23] | +0.44 [-0.12, +0.96] | 8223 |
| Content server | 15 | 40 | +0.29 [-0.26, +0.85] | +0.07 [-0.42, +0.53] | 10686 |
| Content server | 50 | 40 | +0.29 [+0.04, +0.54] | -0.05 [-0.27, +0.16] | 36078 |
| Validator | 1 | 40 | +1.04 [+0.64, +1.46] | +1.12 [+0.91, +1.32] | 39433 |
| Validator | 15 | 40 | +0.98 [+0.66, +1.30] | +0.72 [+0.55, +0.89] | 46221 |
| Validator | 50 | 40 | +0.70 [+0.56, +0.84] | +0.50 [+0.43, +0.58] | 153156 |
| Gatekeeper | 1 | 40 | +0.30 [-0.09, +0.66] | +0.49 [+0.31, +0.68] | 118299 |
| Gatekeeper | 15 | 40 | +0.60 [+0.28, +0.92] | +0.46 [+0.31, +0.60] | 138663 |
| Gatekeeper | 50 | 40 | +0.33 [+0.21, +0.45] | +0.28 [+0.22, +0.33] | 459468 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.73% [6.33%, 7.11%] | 1.78% | 6.73% | 0.00% [0.00%, 0.00%] | 3.98% [3.78%, 4.17%] | 2.44% | 3.98% | 0.00% [0.00%, 0.00%] | 0.542 [0.527, 0.557] | 16.1% | 10.4% | 0.000% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.29% [5.03%, 5.55%] | 1.33% | 5.29% | 0.00% [0.00%, 0.00%] | 3.01% [2.88%, 3.14%] | 1.82% | 3.01% | 0.00% [0.00%, 0.00%] | 0.545 [0.532, 0.557] | 9.2% | 6.8% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.73% [3.64%, 3.83%] | 0.82% | 3.73% | 0.00% [0.00%, 0.00%] | 1.81% [1.75%, 1.87%] | 1.11% | 1.81% | 0.00% [0.00%, 0.00%] | 0.550 [0.542, 0.558] | 7.5% | 5.8% | 0.000% | 200 | 172224 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.74% [6.38%, 7.10%] | 1.78% | 6.73% | 0.01% [-0.08%, 0.10%] | 3.90% [3.78%, 4.02%] | 2.44% | 3.98% | -0.08% [-0.20%, 0.05%] | 0.541 [0.527, 0.556] | 15.1% | 10.7% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.24% [5.01%, 5.48%] | 1.33% | 5.29% | -0.06% [-0.13%, 0.02%] | 2.92% [2.84%, 2.99%] | 1.82% | 3.01% | -0.09% [-0.20%, 0.01%] | 0.546 [0.534, 0.558] | 9.0% | 7.0% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.71% [3.62%, 3.80%] | 0.82% | 3.73% | -0.02% [-0.05%, 0.00%] | 1.78% [1.75%, 1.81%] | 1.11% | 1.81% | -0.03% [-0.08%, 0.03%] | 0.554 [0.547, 0.561] | 6.9% | 5.6% | 0.000% | 200 | 688896 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.74% [6.39%, 7.09%] | 1.78% | 6.73% | 0.01% [-0.07%, 0.09%] | 3.90% [3.78%, 4.02%] | 2.44% | 3.98% | -0.08% [-0.20%, 0.04%] | 0.541 [0.527, 0.556] | 15.1% | 10.7% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.24% [5.01%, 5.46%] | 1.33% | 5.29% | -0.06% [-0.13%, 0.01%] | 2.92% [2.84%, 3.00%] | 1.82% | 3.01% | -0.09% [-0.20%, 0.01%] | 0.546 [0.534, 0.558] | 9.0% | 7.0% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.71% [3.62%, 3.80%] | 0.82% | 3.73% | -0.02% [-0.05%, 0.01%] | 1.78% [1.75%, 1.81%] | 1.11% | 1.81% | -0.03% [-0.08%, 0.03%] | 0.554 [0.547, 0.561] | 6.9% | 5.6% | 0.000% | 200 | 688896 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.72% [6.36%, 7.08%] | 1.78% | 6.73% | -0.01% [-0.06%, 0.03%] | 3.93% [3.77%, 4.09%] | 2.44% | 3.98% | -0.04% [-0.13%, 0.04%] | 0.541 [0.526, 0.557] | 15.5% | 10.6% | 0.000% | 200 | 159196 |
| R = 15, 40 decoys, bundling on | 5.28% [5.02%, 5.52%] | 1.33% | 5.29% | -0.02% [-0.05%, 0.01%] | 3.01% [2.89%, 3.13%] | 1.82% | 3.01% | -0.00% [-0.07%, 0.06%] | 0.545 [0.532, 0.557] | 9.1% | 7.0% | 0.000% | 200 | 208068 |
| R = 50, 40 decoys, bundling on | 3.72% [3.63%, 3.82%] | 0.82% | 3.73% | -0.01% [-0.02%, 0.00%] | 1.83% [1.77%, 1.88%] | 1.11% | 1.81% | 0.02% [-0.01%, 0.05%] | 0.551 [0.544, 0.559] | 7.3% | 5.8% | 0.000% | 200 | 688896 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.79% [6.49%, 7.11%] | 1.91% | 6.73% | 0.06% [-0.15%, 0.27%] | 4.26% [4.12%, 4.41%] | 2.44% | 3.98% | 0.28% [0.04%, 0.51%] | 0.543 [0.533, 0.553] | 6.8% | 8.8% | 0.000% | 200 | 79598 |
| R = 15, 40 decoys, bundling on | 5.34% [5.14%, 5.56%] | 1.42% | 5.29% | 0.05% [-0.12%, 0.22%] | 3.11% [3.01%, 3.21%] | 1.82% | 3.01% | 0.10% [-0.06%, 0.26%] | 0.537 [0.528, 0.546] | 5.1% | 6.2% | 0.000% | 200 | 104034 |
| R = 50, 40 decoys, bundling on | 3.78% [3.70%, 3.85%] | 0.87% | 3.73% | 0.05% [-0.02%, 0.11%] | 2.01% [1.96%, 2.06%] | 1.11% | 1.81% | 0.20% [0.13%, 0.27%] | 0.541 [0.535, 0.547] | 2.8% | 4.1% | 0.000% | 200 | 344448 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.62% [6.25%, 6.96%] | 1.73% | 6.73% | -0.11% [-0.45%, 0.23%] | 3.21% [3.05%, 3.37%] | 2.44% | 3.98% | -0.77% [-1.01%, -0.53%] | 0.561 [0.547, 0.575] | 13.1% | 10.8% | 0.053% | 200 | 39799 |
| R = 15, 40 decoys, bundling on | 5.21% [4.97%, 5.44%] | 1.29% | 5.29% | -0.08% [-0.35%, 0.16%] | 2.35% [2.22%, 2.47%] | 1.82% | 3.01% | -0.67% [-0.85%, -0.48%] | 0.543 [0.530, 0.557] | 7.9% | 7.1% | 0.000% | 200 | 52017 |
| R = 50, 40 decoys, bundling on | 3.71% [3.61%, 3.81%] | 0.79% | 3.73% | -0.03% [-0.13%, 0.07%] | 1.48% [1.43%, 1.54%] | 1.11% | 1.81% | -0.33% [-0.41%, -0.24%] | 0.553 [0.546, 0.561] | 5.7% | 5.6% | 0.000% | 200 | 172224 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.65% [6.29%, 7.02%] | 1.78% | 6.73% | -0.08% [-0.19%, 0.02%] | 3.90% [3.77%, 4.04%] | 2.44% | 3.98% | -0.07% [-0.25%, 0.10%] | 0.545 [0.531, 0.559] | 14.7% | 10.4% | 0.000% | 200 | 119397 |
| R = 15, 40 decoys, bundling on | 5.28% [5.05%, 5.52%] | 1.33% | 5.29% | -0.01% [-0.08%, 0.06%] | 2.95% [2.85%, 3.04%] | 1.82% | 3.01% | -0.06% [-0.19%, 0.07%] | 0.544 [0.531, 0.556] | 9.1% | 6.8% | 0.000% | 200 | 156051 |
| R = 50, 40 decoys, bundling on | 3.70% [3.61%, 3.79%] | 0.82% | 3.73% | -0.03% [-0.07%, -0.00%] | 1.80% [1.76%, 1.85%] | 1.11% | 1.81% | -0.00% [-0.06%, 0.05%] | 0.554 [0.546, 0.561] | 7.1% | 5.6% | 0.000% | 200 | 516672 |

## Outcome-shuffle control (stable cells)

21 stable cells; 0 with a shuffled-outcome AUC interval excluding 0.5.

# Tables

Record-to-device linking with genuine decoys, the 120-second registry window, with every device and relay-hop hold stretched 1.5 times. Measured end-to-end delay D = 625.6 s. Per-decision attack; intervals resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

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
| 1 | 40 | 1.97 | 14.0% | 27.5% | 41.5% | 32.0% | 14.0% | 2,501,697 |
| 15 | 40 | 2.65 | 7.1% | 18.6% | 25.7% | 20.0% | 7.0% | 215,400 |
| 50 | 40 | 4.30 | 1.3% | 5.8% | 7.1% | 5.9% | 1.3% | 215,400 |

## Change from the reg120 build on the same records

Accuracy in this build minus accuracy in the reg120 build, matched record by record (percentage points). The two builds share every random draw outside the mechanisms they differ in.

| Vantage | R | Decoys | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|---|
| Baseline | 1 | 40 | -1.78 [-2.22, -1.40] | -1.11 [-1.41, -0.82] | 39656 |
| Baseline | 15 | 40 | -1.26 [-1.56, -0.97] | -0.84 [-1.05, -0.63] | 49168 |
| Baseline | 50 | 40 | -0.72 [-0.86, -0.59] | -0.52 [-0.61, -0.43] | 162956 |
| First hop, credential | 1 | 40 | -1.76 [-2.15, -1.39] | -1.11 [-1.31, -0.91] | 158624 |
| First hop, credential | 15 | 40 | -1.25 [-1.52, -0.97] | -0.82 [-0.95, -0.69] | 196672 |
| First hop, credential | 50 | 40 | -0.67 [-0.79, -0.55] | -0.55 [-0.61, -0.50] | 651824 |
| First hop, content | 1 | 40 | -1.76 [-2.14, -1.37] | -1.11 [-1.31, -0.90] | 158624 |
| First hop, content | 15 | 40 | -1.25 [-1.52, -0.98] | -0.82 [-0.96, -0.69] | 196672 |
| First hop, content | 50 | 40 | -0.67 [-0.79, -0.55] | -0.55 [-0.61, -0.50] | 651824 |
| Credential processor | 1 | 40 | -1.87 [-2.28, -1.48] | -1.01 [-1.26, -0.75] | 158624 |
| Credential processor | 15 | 40 | -1.25 [-1.55, -0.96] | -0.86 [-1.05, -0.65] | 196672 |
| Credential processor | 50 | 40 | -0.71 [-0.84, -0.57] | -0.51 [-0.60, -0.43] | 651824 |
| Content server | 1 | 40 | -1.86 [-2.82, -0.88] | -0.64 [-1.41, +0.16] | 7209 |
| Content server | 15 | 40 | -1.57 [-2.23, -0.94] | -1.56 [-2.04, -1.05] | 11757 |
| Content server | 50 | 40 | -1.04 [-1.34, -0.72] | -0.66 [-0.89, -0.44] | 38283 |
| Validator | 1 | 40 | -1.13 [-1.63, -0.62] | -1.05 [-1.34, -0.74] | 39656 |
| Validator | 15 | 40 | -1.08 [-1.40, -0.74] | -0.59 [-0.83, -0.35] | 49168 |
| Validator | 50 | 40 | -0.40 [-0.57, -0.24] | -0.43 [-0.52, -0.33] | 162956 |
| Gatekeeper | 1 | 40 | -1.76 [-2.13, -1.38] | -1.07 [-1.27, -0.88] | 118968 |
| Gatekeeper | 15 | 40 | -1.18 [-1.46, -0.89] | -0.77 [-0.93, -0.62] | 147504 |
| Gatekeeper | 50 | 40 | -0.67 [-0.80, -0.54] | -0.54 [-0.60, -0.48] | 488868 |

## Every cell

### Baseline

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.69% [6.34%, 7.04%] | 1.74% | 6.69% | 0.00% [0.00%, 0.00%] | 4.10% [3.89%, 4.31%] | 2.44% | 4.10% | 0.00% [0.00%, 0.00%] | 0.558 [0.543, 0.572] | 13.5% | 9.3% | 0.000% | 200 | 39901 |
| R = 15, 40 decoys, bundling on | 5.52% [5.28%, 5.76%] | 1.29% | 5.52% | 0.00% [0.00%, 0.00%] | 2.94% [2.80%, 3.07%] | 1.82% | 2.94% | 0.00% [0.00%, 0.00%] | 0.556 [0.542, 0.570] | 11.0% | 8.7% | 0.000% | 200 | 52047 |
| R = 50, 40 decoys, bundling on | 3.76% [3.66%, 3.86%] | 0.79% | 3.76% | 0.00% [0.00%, 0.00%] | 1.87% [1.81%, 1.93%] | 1.11% | 1.87% | 0.00% [0.00%, 0.00%] | 0.557 [0.548, 0.565] | 5.9% | 5.7% | 0.000% | 200 | 172341 |

### First hop, credential

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.70% [6.38%, 7.05%] | 1.74% | 6.69% | 0.01% [-0.08%, 0.09%] | 4.03% [3.91%, 4.17%] | 2.44% | 4.10% | -0.07% [-0.19%, 0.06%] | 0.555 [0.542, 0.568] | 12.8% | 9.5% | 0.000% | 200 | 159604 |
| R = 15, 40 decoys, bundling on | 5.53% [5.30%, 5.75%] | 1.29% | 5.52% | 0.01% [-0.06%, 0.07%] | 3.02% [2.94%, 3.10%] | 1.82% | 2.94% | 0.09% [-0.02%, 0.20%] | 0.555 [0.542, 0.567] | 11.4% | 8.8% | 0.000% | 200 | 208188 |
| R = 50, 40 decoys, bundling on | 3.79% [3.69%, 3.88%] | 0.79% | 3.76% | 0.03% [0.00%, 0.06%] | 1.85% [1.82%, 1.89%] | 1.11% | 1.87% | -0.02% [-0.08%, 0.04%] | 0.554 [0.546, 0.562] | 6.1% | 5.6% | 0.000% | 200 | 689364 |

### First hop, content

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.70% [6.38%, 7.02%] | 1.74% | 6.69% | 0.01% [-0.07%, 0.09%] | 4.03% [3.90%, 4.16%] | 2.44% | 4.10% | -0.07% [-0.20%, 0.07%] | 0.555 [0.542, 0.568] | 12.8% | 9.5% | 0.000% | 200 | 159604 |
| R = 15, 40 decoys, bundling on | 5.53% [5.29%, 5.75%] | 1.29% | 5.52% | 0.01% [-0.06%, 0.07%] | 3.02% [2.94%, 3.11%] | 1.82% | 2.94% | 0.09% [-0.03%, 0.20%] | 0.555 [0.542, 0.567] | 11.4% | 8.8% | 0.000% | 200 | 208188 |
| R = 50, 40 decoys, bundling on | 3.79% [3.69%, 3.88%] | 0.79% | 3.76% | 0.03% [0.00%, 0.06%] | 1.85% [1.82%, 1.89%] | 1.11% | 1.87% | -0.02% [-0.07%, 0.04%] | 0.554 [0.546, 0.562] | 6.1% | 5.6% | 0.000% | 200 | 689364 |

### Credential processor

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.65% [6.32%, 6.98%] | 1.74% | 6.69% | -0.04% [-0.09%, 0.00%] | 4.13% [3.94%, 4.32%] | 2.44% | 4.10% | 0.03% [-0.07%, 0.13%] | 0.559 [0.544, 0.573] | 12.6% | 9.3% | 0.000% | 200 | 159604 |
| R = 15, 40 decoys, bundling on | 5.51% [5.29%, 5.75%] | 1.29% | 5.52% | -0.00% [-0.04%, 0.03%] | 2.96% [2.85%, 3.08%] | 1.82% | 2.94% | 0.03% [-0.05%, 0.10%] | 0.557 [0.543, 0.570] | 10.9% | 8.8% | 0.000% | 200 | 208188 |
| R = 50, 40 decoys, bundling on | 3.76% [3.66%, 3.86%] | 0.79% | 3.76% | 0.00% [-0.01%, 0.02%] | 1.88% [1.83%, 1.93%] | 1.11% | 1.87% | 0.01% [-0.02%, 0.04%] | 0.556 [0.548, 0.564] | 6.0% | 5.6% | 0.000% | 200 | 689364 |

### Content server

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 7.16% [6.87%, 7.45%] | 1.94% | 6.69% | 0.46% [0.22%, 0.70%] | 4.71% [4.56%, 4.87%] | 2.44% | 4.10% | 0.61% [0.38%, 0.84%] | 0.559 [0.549, 0.568] | 4.8% | 8.4% | 0.000% | 200 | 79802 |
| R = 15, 40 decoys, bundling on | 5.85% [5.64%, 6.06%] | 1.45% | 5.52% | 0.33% [0.16%, 0.51%] | 3.44% [3.32%, 3.56%] | 1.82% | 2.94% | 0.50% [0.34%, 0.66%] | 0.540 [0.531, 0.549] | 4.5% | 6.7% | 0.000% | 200 | 104094 |
| R = 50, 40 decoys, bundling on | 3.98% [3.89%, 4.06%] | 0.89% | 3.76% | 0.22% [0.14%, 0.30%] | 2.18% [2.13%, 2.22%] | 1.11% | 1.87% | 0.31% [0.24%, 0.37%] | 0.535 [0.529, 0.541] | 2.4% | 3.9% | 0.000% | 200 | 344682 |

### Validator

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 8.41% [8.05%, 8.77%] | 1.88% | 6.69% | 1.72% [1.38%, 2.05%] | 4.38% [4.18%, 4.57%] | 2.44% | 4.10% | 0.28% [-0.02%, 0.58%] | 0.566 [0.553, 0.580] | 19.8% | 14.3% | 0.043% | 200 | 39901 |
| R = 15, 40 decoys, bundling on | 6.76% [6.52%, 7.01%] | 1.40% | 5.52% | 1.24% [0.97%, 1.50%] | 3.43% [3.28%, 3.57%] | 1.82% | 2.94% | 0.49% [0.30%, 0.69%] | 0.566 [0.554, 0.577] | 13.3% | 10.0% | 0.013% | 200 | 52047 |
| R = 50, 40 decoys, bundling on | 4.67% [4.55%, 4.79%] | 0.86% | 3.76% | 0.91% [0.80%, 1.02%] | 2.05% [1.99%, 2.11%] | 1.11% | 1.87% | 0.18% [0.09%, 0.27%] | 0.558 [0.551, 0.565] | 9.2% | 7.3% | 0.001% | 200 | 172341 |

### Gatekeeper

| Cell | Device accuracy [95% CI] | Random device | Baseline | Contribution [95% CI] | Submission accuracy [95% CI] | 1/T | Baseline | Contribution [95% CI] | AUC [95% CI] | Precision top 1% | Precision top 5% | Coverage at >50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R = 1, 40 decoys, bundling on | 6.66% [6.33%, 7.01%] | 1.74% | 6.69% | -0.03% [-0.12%, 0.06%] | 4.08% [3.93%, 4.22%] | 2.44% | 4.10% | -0.02% [-0.20%, 0.14%] | 0.562 [0.549, 0.576] | 13.3% | 9.6% | 0.000% | 200 | 119703 |
| R = 15, 40 decoys, bundling on | 5.59% [5.36%, 5.81%] | 1.29% | 5.52% | 0.07% [-0.01%, 0.14%] | 2.95% [2.85%, 3.04%] | 1.82% | 2.94% | 0.01% [-0.12%, 0.16%] | 0.554 [0.541, 0.567] | 11.1% | 8.9% | 0.000% | 200 | 156141 |
| R = 50, 40 decoys, bundling on | 3.78% [3.68%, 3.87%] | 0.79% | 3.76% | 0.02% [-0.02%, 0.05%] | 1.84% [1.80%, 1.89%] | 1.11% | 1.87% | -0.03% [-0.08%, 0.03%] | 0.556 [0.548, 0.563] | 6.2% | 5.8% | 0.000% | 200 | 517023 |

## Outcome-shuffle control (stable cells)

21 stable cells; 2 with a shuffled-outcome AUC interval excluding 0.5: R15_D40_B validator (0.509), R50_D40_B first_hop_cred (0.504).

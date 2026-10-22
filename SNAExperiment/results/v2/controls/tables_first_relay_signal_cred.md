# permitted overlap, credential path dominates the record time

Build `first_relay_signal_cred`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1108.8 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.58% [8.96%, 10.14%] | 1.95% | 9.58% | 0.00% [0.00%, 0.00%] | 3.61% [3.35%, 3.85%] | 1.64% | 3.61% | 0.00% [0.00%, 0.00%] | 0.568 [0.553, 0.582] | 19.0% | 14.0% | 0.000% | 100 | 19976 |
| 20 | 6.60% [6.08%, 7.12%] | 1.49% | 6.60% | 0.00% [0.00%, 0.00%] | 2.77% [2.55%, 3.01%] | 1.25% | 2.77% | 0.00% [0.00%, 0.00%] | 0.554 [0.534, 0.575] | 15.6% | 9.6% | 0.000% | 100 | 19897 |
| 100 | 3.78% [3.63%, 3.94%] | 0.74% | 3.78% | 0.00% [0.00%, 0.00%] | 1.43% [1.36%, 1.49%] | 0.62% | 1.43% | 0.00% [0.00%, 0.00%] | 0.549 [0.538, 0.560] | 5.9% | 5.5% | 0.000% | 100 | 97151 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.63% [9.04%, 10.18%] | 1.95% | 9.58% | 0.05% [-0.00%, 0.11%] | 3.82% [3.67%, 3.98%] | 1.64% | 3.61% | 0.21% [0.11%, 0.32%] | 0.568 [0.554, 0.582] | 18.8% | 14.2% | 0.000% | 100 | 399520 |
| 20 | 6.61% [6.13%, 7.09%] | 1.49% | 6.60% | 0.01% [-0.05%, 0.05%] | 2.96% [2.84%, 3.10%] | 1.25% | 2.77% | 0.20% [0.08%, 0.30%] | 0.555 [0.535, 0.575] | 15.0% | 9.7% | 0.000% | 100 | 397940 |
| 100 | 3.78% [3.63%, 3.94%] | 0.74% | 3.78% | -0.00% [-0.02%, 0.01%] | 1.58% [1.55%, 1.61%] | 0.62% | 1.43% | 0.15% [0.10%, 0.20%] | 0.551 [0.541, 0.562] | 5.9% | 5.5% | 0.000% | 100 | 1943020 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.63% [9.07%, 10.21%] | 1.95% | 9.58% | 0.05% [-0.00%, 0.11%] | 3.82% [3.67%, 3.99%] | 1.64% | 3.61% | 0.21% [0.11%, 0.32%] | 0.568 [0.554, 0.582] | 18.8% | 14.2% | 0.000% | 100 | 399520 |
| 20 | 6.61% [6.14%, 7.09%] | 1.49% | 6.60% | 0.01% [-0.05%, 0.06%] | 2.96% [2.84%, 3.09%] | 1.25% | 2.77% | 0.20% [0.08%, 0.31%] | 0.555 [0.535, 0.575] | 15.0% | 9.7% | 0.000% | 100 | 397940 |
| 100 | 3.78% [3.63%, 3.93%] | 0.74% | 3.78% | -0.00% [-0.02%, 0.01%] | 1.58% [1.55%, 1.61%] | 0.62% | 1.43% | 0.15% [0.11%, 0.20%] | 0.551 [0.541, 0.562] | 5.9% | 5.5% | 0.000% | 100 | 1943020 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.57% [9.00%, 10.16%] | 1.95% | 9.58% | -0.00% [-0.05%, 0.04%] | 3.63% [3.41%, 3.85%] | 1.64% | 3.61% | 0.02% [-0.05%, 0.09%] | 0.568 [0.553, 0.583] | 19.5% | 14.3% | 0.000% | 100 | 339592 |
| 20 | 6.58% [6.11%, 7.03%] | 1.49% | 6.60% | -0.02% [-0.06%, 0.02%] | 2.82% [2.62%, 3.02%] | 1.25% | 2.77% | 0.05% [-0.03%, 0.13%] | 0.555 [0.535, 0.575] | 15.3% | 9.8% | 0.000% | 100 | 338249 |
| 100 | 3.77% [3.62%, 3.92%] | 0.74% | 3.78% | -0.01% [-0.02%, 0.00%] | 1.43% [1.37%, 1.48%] | 0.62% | 1.43% | 0.00% [-0.02%, 0.03%] | 0.550 [0.539, 0.561] | 5.9% | 5.5% | 0.000% | 100 | 1651567 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 17.09% [16.45%, 17.77%] | 3.20% | 9.58% | 7.51% [6.88%, 8.20%] | 12.34% [11.96%, 12.75%] | 1.64% | 3.61% | 8.74% [8.30%, 9.21%] | 0.617 [0.605, 0.628] | 37.5% | 34.7% | 0.005% | 100 | 19976 |
| 20 | 12.77% [12.24%, 13.30%] | 2.44% | 6.60% | 6.16% [5.69%, 6.66%] | 9.22% [8.85%, 9.61%] | 1.25% | 2.77% | 6.45% [6.04%, 6.88%] | 0.600 [0.587, 0.612] | 27.6% | 22.1% | 0.085% | 100 | 19897 |
| 100 | 7.49% [7.36%, 7.63%] | 1.22% | 3.78% | 3.71% [3.52%, 3.89%] | 4.76% [4.65%, 4.86%] | 0.62% | 1.43% | 3.33% [3.21%, 3.46%] | 0.590 [0.584, 0.596] | 16.3% | 12.9% | 0.000% | 100 | 97151 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.57% [9.01%, 10.14%] | 1.95% | 9.58% | -0.01% [-0.21%, 0.19%] | 3.50% [3.32%, 3.66%] | 1.64% | 3.61% | -0.11% [-0.34%, 0.13%] | 0.571 [0.555, 0.587] | 18.9% | 14.6% | 0.008% | 100 | 59928 |
| 20 | 6.53% [6.05%, 7.03%] | 1.49% | 6.60% | -0.08% [-0.22%, 0.06%] | 2.72% [2.57%, 2.87%] | 1.25% | 2.77% | -0.05% [-0.25%, 0.15%] | 0.555 [0.534, 0.576] | 17.8% | 9.8% | 0.000% | 100 | 59691 |
| 100 | 3.76% [3.61%, 3.91%] | 0.74% | 3.78% | -0.02% [-0.06%, 0.02%] | 1.44% [1.40%, 1.49%] | 0.62% | 1.43% | 0.01% [-0.05%, 0.08%] | 0.553 [0.542, 0.563] | 5.7% | 5.6% | 0.000% | 100 | 291453 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 11.24% [10.75%, 11.72%] | 2.33% | 9.58% | 1.66% [1.31%, 2.02%] | 4.67% [4.47%, 4.85%] | 1.64% | 3.61% | 1.06% [0.76%, 1.36%] | 0.575 [0.563, 0.587] | 21.5% | 18.1% | 0.000% | 100 | 39952 |
| 20 | 8.14% [7.70%, 8.59%] | 1.78% | 6.60% | 1.54% [1.25%, 1.85%] | 3.63% [3.44%, 3.83%] | 1.25% | 2.77% | 0.86% [0.55%, 1.16%] | 0.569 [0.555, 0.583] | 15.8% | 12.7% | 0.000% | 100 | 39794 |
| 100 | 4.74% [4.62%, 4.87%] | 0.89% | 3.78% | 0.96% [0.86%, 1.06%] | 1.89% [1.82%, 1.96%] | 0.62% | 1.43% | 0.46% [0.37%, 0.55%] | 0.557 [0.548, 0.566] | 7.8% | 6.7% | 0.000% | 100 | 194302 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

The rows cover every record; every record the node can select because it held a destination role; and the split by whether it held a first relay, which it cannot tell.

| R | Records | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | all records | 399,520 | 3995 | 9.77% | 9.58% | +0.20 [+0.10, +0.29] | 19.8% | 0.0000% | pass |
| 20 | all records | 397,940 | 3979 | 6.73% | 6.60% | +0.12 [+0.05, +0.21] | 15.5% | 0.0000% | pass |
| 100 | all records | 1,943,020 | 19430 | 3.87% | 3.78% | +0.09 [+0.07, +0.12] | 6.6% | 0.0000% | pass |
| 1 | every record the node can select | 59,928 | 599 | 10.67% | 9.58% | +1.09 [+0.84, +1.33] | 22.7% | 0.0000% | pass |
| 1 | first relay held | 19,100 | 191 | 10.66% | 9.83% | +0.83 [+0.54, +1.10] | 30.6% | 0.0157% | pass |
| 1 | no first relay held | 380,420 | 3804 | 9.73% | 9.56% | +0.17 [+0.07, +0.26] | 19.6% | 0.0000% | pass |
| 20 | every record the node can select | 59,691 | 597 | 7.59% | 6.60% | +0.98 [+0.77, +1.20] | 17.6% | 0.0000% | pass |
| 20 | first relay held | 19,052 | 191 | 7.16% | 6.49% | +0.67 [+0.42, +0.92] | 18.6% | 0.0000% | pass |
| 20 | no first relay held | 378,888 | 3789 | 6.71% | 6.61% | +0.10 [+0.01, +0.17] | 15.8% | 0.0000% | pass |
| 100 | every record the node can select | 291,453 | 2915 | 4.40% | 3.78% | +0.62 [+0.55, +0.69] | 8.5% | 0.0000% | pass |
| 100 | first relay held | 93,076 | 931 | 4.22% | 3.78% | +0.43 [+0.35, +0.52] | 10.5% | 0.0000% | pass |
| 100 | no first relay held | 1,849,944 | 18499 | 3.86% | 3.78% | +0.08 [+0.05, +0.10] | 6.5% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there. Prevalence is the class's share of the node's decisions. Combined minus the sum is the combined lead minus the two single-role leads, paired on the same rows.

| R | Roles held | Prevalence | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined minus the sum [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 11.95% | 47,729 | 477 | 10.57% | 9.49% | +1.07 [+0.81, +1.34] | +0.01 [-0.07, +0.09] | +1.13 [+0.86, +1.40] | -0.06 [-0.17, +0.04] | 21.1% | 0.0000% | pass |
| 1 | credential first relay + content destination | 0.51% | 2,033 | 20 | 12.49% | 9.89% | +2.61 [+1.20, +4.00] | +0.84 [+0.28, +1.43] | +2.21 [+0.91, +3.47] | -0.44 [-1.20, +0.34] | 51.9% | 0.0000% | fail |
| 1 | content first relay + content destination | 0.50% | 1,981 | 20 | 11.86% | 10.55% | +1.31 [+0.25, +2.44] | +0.05 [-0.56, +0.62] | +0.86 [-0.25, +1.99] | +0.40 [-0.46, +1.22] | 51.9% | 0.0505% | fail |
| 1 | content first relay + credential destination | 0.52% | 2,093 | 21 | 10.89% | 10.51% | +0.38 [-0.05, +0.81] | +0.14 [-0.23, +0.56] | -0.05 [-0.35, +0.28] | +0.29 [-0.05, +0.63] | 28.9% | 0.0478% | pass |
| 1 | second relay + destination | 1.38% | 5,518 | 55 | 10.37% | 9.64% | +0.72 [-0.02, +1.43] | +0.04 [-0.16, +0.23] | +0.85 [+0.12, +1.59] | -0.16 [-0.42, +0.09] | 40.2% | 0.0000% | pass |
| 1 | three or more roles, with a destination | 0.14% | 574 | 6 | 10.63% | 8.19% | +2.44 [+0.37, +4.33] | +0.52 [-0.35, +1.47] | +2.09 [+0.17, +4.06] | -0.17 [-1.44, +1.04] | 39.0% | 0.0000% | pass |
| 20 | destination only | 11.94% | 47,502 | 475 | 7.67% | 6.75% | +0.92 [+0.69, +1.14] | -0.04 [-0.12, +0.04] | +1.01 [+0.78, +1.24] | -0.05 [-0.15, +0.06] | 18.2% | 0.0000% | pass |
| 20 | credential first relay + content destination | 0.50% | 1,995 | 20 | 9.12% | 6.22% | +2.91 [+1.75, +4.03] | +0.95 [+0.36, +1.61] | +2.46 [+1.40, +3.54] | -0.50 [-1.39, +0.40] | 41.6% | 0.0000% | pass |
| 20 | content first relay + content destination | 0.51% | 2,032 | 20 | 7.63% | 5.71% | +1.92 [+0.87, +2.97] | +0.20 [-0.15, +0.56] | +1.48 [+0.36, +2.55] | +0.25 [-0.43, +0.91] | 30.1% | 0.0000% | pass |
| 20 | content first relay + credential destination | 0.52% | 2,067 | 21 | 6.63% | 6.05% | +0.58 [+0.14, +1.04] | +0.39 [-0.09, +0.90] | +0.15 [-0.10, +0.44] | +0.05 [-0.29, +0.39] | 22.7% | 0.0000% | pass |
| 20 | second relay + destination | 1.39% | 5,550 | 56 | 6.58% | 5.96% | +0.61 [+0.00, +1.22] | +0.02 [-0.16, +0.20] | +0.65 [+0.07, +1.24] | -0.05 [-0.29, +0.18] | 25.7% | 0.0000% | pass |
| 20 | three or more roles, with a destination | 0.14% | 545 | 5 | unstable: 105 runs needed | | | | | | | | |
| 100 | destination only | 11.95% | 232,253 | 2323 | 4.37% | 3.78% | +0.59 [+0.52, +0.66] | -0.03 [-0.06, -0.01] | +0.64 [+0.57, +0.71] | -0.01 [-0.04, +0.02] | 8.0% | 0.0000% | pass |
| 100 | credential first relay + content destination | 0.49% | 9,599 | 96 | 5.23% | 3.63% | +1.60 [+1.17, +2.09] | +0.34 [+0.21, +0.49] | +1.15 [+0.75, +1.57] | +0.11 [-0.10, +0.32] | 15.6% | 0.0000% | pass |
| 100 | content first relay + content destination | 0.51% | 9,891 | 99 | 5.04% | 3.72% | +1.32 [+0.95, +1.71] | +0.21 [+0.05, +0.38] | +1.00 [+0.61, +1.37] | +0.11 [-0.14, +0.35] | 15.1% | 0.0000% | pass |
| 100 | content first relay + credential destination | 0.52% | 10,159 | 102 | 4.09% | 4.09% | +0.01 [-0.14, +0.16] | -0.01 [-0.16, +0.13] | +0.04 [-0.03, +0.12] | -0.02 [-0.11, +0.08] | 13.5% | 0.0000% | pass |
| 100 | second relay + destination | 1.39% | 27,052 | 271 | 4.30% | 3.81% | +0.49 [+0.29, +0.69] | -0.01 [-0.07, +0.06] | +0.55 [+0.36, +0.75] | -0.06 [-0.14, +0.03] | 13.3% | 0.0000% | pass |
| 100 | three or more roles, with a destination | 0.13% | 2,499 | 25 | 4.44% | 3.48% | +0.96 [+0.24, +1.69] | +0.20 [-0.08, +0.49] | +0.52 [-0.12, +1.24] | +0.24 [-0.04, +0.54] | 34.7% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 198,610 | 1986 | 9.55% | 9.58% | -0.04 [-0.11, +0.03] | 20.7% | 0.0000% | pass |
| 1 | one relay or gatekeeper role | 116,616 | 1166 | 9.69% | 9.57% | +0.12 [-0.02, +0.25] | 21.4% | 0.0026% | pass |
| 1 | second relay + first relay | 4,569 | 46 | 9.70% | 9.06% | +0.63 [+0.29, +1.00] | 40.3% | 0.0000% | pass |
| 1 | second relay + second relay | 2,034 | 20 | 9.83% | 9.64% | +0.20 [-0.15, +0.54] | 51.9% | 0.1475% | fail |
| 1 | gatekeeper + first relay | 8,424 | 84 | 10.40% | 9.90% | +0.50 [+0.13, +0.88] | 32.6% | 0.1306% | fail |
| 1 | gatekeeper + second relay | 7,719 | 77 | 9.43% | 9.51% | -0.08 [-0.39, +0.22] | 26.8% | 0.0000% | pass |
| 1 | three or more roles, no destination | 1,620 | 16 | 9.07% | 9.07% | +0.00 [-0.83, +0.77] | 55.6% | 0.3086% | fail |
| 20 | no role | 197,684 | 1977 | 6.52% | 6.59% | -0.06 [-0.13, +0.00] | 15.8% | 0.0000% | pass |
| 20 | one relay or gatekeeper role | 116,422 | 1164 | 6.63% | 6.61% | +0.02 [-0.08, +0.12] | 19.1% | 0.0000% | pass |
| 20 | second relay + first relay | 4,579 | 46 | 6.66% | 6.55% | +0.11 [-0.16, +0.37] | 25.7% | 0.0000% | pass |
| 20 | second relay + second relay | 2,093 | 21 | 7.36% | 7.50% | -0.14 [-0.35, +0.05] | 34.6% | 0.0000% | pass |
| 20 | gatekeeper + first relay | 8,379 | 84 | 6.99% | 6.83% | +0.17 [-0.10, +0.42] | 24.7% | 0.0119% | pass |
| 20 | gatekeeper + second relay | 7,502 | 75 | 6.34% | 6.45% | -0.11 [-0.42, +0.17] | 24.4% | 0.0000% | pass |
| 20 | three or more roles, no destination | 1,590 | 16 | 6.86% | 6.92% | -0.06 [-0.76, +0.65] | 43.0% | 0.0000% | pass |
| 100 | no role | 965,013 | 9650 | 3.75% | 3.78% | -0.03 [-0.05, -0.02] | 6.4% | 0.0003% | pass |
| 100 | one relay or gatekeeper role | 568,481 | 5685 | 3.82% | 3.78% | +0.04 [+0.01, +0.07] | 6.3% | 0.0047% | pass |
| 100 | second relay + first relay | 22,569 | 226 | 4.01% | 3.85% | +0.16 [+0.05, +0.27] | 10.7% | 0.0222% | pass |
| 100 | second relay + second relay | 10,074 | 101 | 3.50% | 3.54% | -0.04 [-0.15, +0.08] | 8.4% | 0.0000% | pass |
| 100 | gatekeeper + first relay | 40,858 | 409 | 3.92% | 3.72% | +0.20 [+0.10, +0.29] | 10.0% | 0.0000% | pass |
| 100 | gatekeeper + second relay | 36,728 | 367 | 3.86% | 3.95% | -0.09 [-0.19, +0.01] | 9.2% | 0.0000% | pass |
| 100 | three or more roles, no destination | 7,844 | 78 | 3.71% | 3.57% | +0.14 [-0.04, +0.32] | 12.5% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | +0.05 [-0.00, +0.11] | +0.08 [+0.01, +0.16] | n/a |
| First hop, credential | 20 | +0.01 [-0.05, +0.05] | -0.02 [-0.08, +0.05] | n/a |
| First hop, credential | 100 | -0.00 [-0.02, +0.01] | -0.00 [-0.02, +0.02] | n/a |
| First hop, content | 1 | +0.05 [-0.00, +0.11] | +0.08 [+0.01, +0.15] | n/a |
| First hop, content | 20 | +0.01 [-0.05, +0.06] | -0.02 [-0.08, +0.05] | n/a |
| First hop, content | 100 | -0.00 [-0.02, +0.01] | -0.00 [-0.02, +0.02] | n/a |
| Credential processor | 1 | -0.00 [-0.05, +0.04] | -0.04 [-0.11, +0.02] | n/a |
| Credential processor | 20 | -0.02 [-0.06, +0.02] | -0.04 [-0.08, +0.01] | n/a |
| Credential processor | 100 | -0.01 [-0.02, +0.00] | -0.01 [-0.03, +0.00] | n/a |

## Outcome-shuffle control

80 stable rows; 11 with a shuffled-outcome AUC interval excluding 0.5: R = 1 First hop, credential (0.504), R = 20 First hop, credential (0.505), R = 20 Credential processor (0.505), R = 100 Gatekeeper (0.506), R = 1 combined: all records (0.504), R = 1 combined: no role (0.506), R = 1 cred_processor (four nodes per run) (0.510), R = 20 combined: one relay or gatekeeper role (0.508), R = 20 combined: content first relay + credential destination (0.561), R = 100 combined: all records (0.504), R = 100 combined: gatekeeper + second relay (0.485).

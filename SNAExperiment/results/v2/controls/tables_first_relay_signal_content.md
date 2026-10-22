# permitted overlap, content paths dominate the record time

Build `first_relay_signal_content`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1108.8 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.29% [8.75%, 9.86%] | 1.91% | 9.29% | 0.00% [0.00%, 0.00%] | 3.27% [3.03%, 3.51%] | 1.64% | 3.27% | 0.00% [0.00%, 0.00%] | 0.585 [0.569, 0.601] | 26.0% | 16.7% | 0.000% | 100 | 19976 |
| 20 | 6.84% [6.34%, 7.33%] | 1.45% | 6.84% | 0.00% [0.00%, 0.00%] | 2.54% [2.32%, 2.76%] | 1.25% | 2.54% | 0.00% [0.00%, 0.00%] | 0.551 [0.531, 0.571] | 14.1% | 10.9% | 0.000% | 100 | 19897 |
| 100 | 3.75% [3.61%, 3.87%] | 0.73% | 3.75% | 0.00% [0.00%, 0.00%] | 1.27% [1.20%, 1.34%] | 0.62% | 1.27% | 0.00% [0.00%, 0.00%] | 0.542 [0.532, 0.553] | 6.6% | 5.3% | 0.000% | 100 | 97151 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.34% [8.78%, 9.92%] | 1.91% | 9.29% | 0.05% [-0.01%, 0.11%] | 3.43% [3.30%, 3.57%] | 1.64% | 3.27% | 0.16% [0.05%, 0.27%] | 0.585 [0.569, 0.600] | 25.0% | 16.7% | 0.000% | 100 | 399520 |
| 20 | 6.84% [6.39%, 7.33%] | 1.45% | 6.84% | 0.00% [-0.05%, 0.05%] | 2.70% [2.59%, 2.82%] | 1.25% | 2.54% | 0.16% [0.04%, 0.28%] | 0.552 [0.533, 0.571] | 15.0% | 10.4% | 0.000% | 100 | 397940 |
| 100 | 3.77% [3.63%, 3.89%] | 0.73% | 3.75% | 0.02% [0.00%, 0.04%] | 1.41% [1.39%, 1.43%] | 0.62% | 1.27% | 0.14% [0.08%, 0.19%] | 0.543 [0.533, 0.553] | 6.4% | 5.3% | 0.000% | 100 | 1943020 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.34% [8.79%, 9.90%] | 1.91% | 9.29% | 0.05% [-0.01%, 0.11%] | 3.43% [3.30%, 3.56%] | 1.64% | 3.27% | 0.16% [0.04%, 0.28%] | 0.585 [0.569, 0.600] | 25.0% | 16.7% | 0.000% | 100 | 399520 |
| 20 | 6.84% [6.38%, 7.30%] | 1.45% | 6.84% | 0.00% [-0.05%, 0.05%] | 2.70% [2.59%, 2.82%] | 1.25% | 2.54% | 0.16% [0.02%, 0.28%] | 0.552 [0.533, 0.571] | 15.0% | 10.4% | 0.000% | 100 | 397940 |
| 100 | 3.77% [3.65%, 3.90%] | 0.73% | 3.75% | 0.02% [0.00%, 0.04%] | 1.41% [1.39%, 1.44%] | 0.62% | 1.27% | 0.14% [0.09%, 0.19%] | 0.543 [0.533, 0.553] | 6.4% | 5.3% | 0.000% | 100 | 1943020 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.28% [8.74%, 9.85%] | 1.91% | 9.29% | -0.01% [-0.05%, 0.03%] | 3.25% [3.08%, 3.42%] | 1.64% | 3.27% | -0.02% [-0.14%, 0.09%] | 0.585 [0.569, 0.601] | 25.3% | 16.6% | 0.000% | 100 | 339592 |
| 20 | 6.82% [6.35%, 7.28%] | 1.45% | 6.84% | -0.01% [-0.04%, 0.02%] | 2.51% [2.34%, 2.68%] | 1.25% | 2.54% | -0.03% [-0.12%, 0.06%] | 0.552 [0.533, 0.572] | 14.2% | 10.6% | 0.000% | 100 | 338249 |
| 100 | 3.74% [3.60%, 3.88%] | 0.73% | 3.75% | -0.00% [-0.01%, 0.01%] | 1.28% [1.22%, 1.35%] | 0.62% | 1.27% | 0.01% [-0.02%, 0.04%] | 0.542 [0.532, 0.553] | 6.5% | 5.3% | 0.000% | 100 | 1651567 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7.87% [7.34%, 8.40%] | 2.14% | 9.29% | -1.42% [-1.83%, -1.00%] | 2.64% [2.44%, 2.85%] | 1.64% | 3.27% | -0.63% [-0.95%, -0.29%] | 0.583 [0.565, 0.601] | 22.5% | 16.2% | 0.000% | 100 | 19976 |
| 20 | 5.37% [5.00%, 5.76%] | 1.63% | 6.84% | -1.46% [-1.83%, -1.11%] | 2.09% [1.91%, 2.27%] | 1.25% | 2.54% | -0.45% [-0.70%, -0.18%] | 0.549 [0.524, 0.573] | 11.1% | 6.8% | 0.000% | 100 | 19897 |
| 100 | 3.02% [2.90%, 3.14%] | 0.82% | 3.75% | -0.72% [-0.84%, -0.60%] | 1.02% [0.96%, 1.08%] | 0.62% | 1.27% | -0.25% [-0.36%, -0.14%] | 0.546 [0.535, 0.558] | 4.8% | 3.6% | 0.000% | 100 | 97151 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.39% [8.84%, 9.96%] | 1.91% | 9.29% | 0.10% [-0.01%, 0.21%] | 3.30% [3.12%, 3.46%] | 1.64% | 3.27% | 0.02% [-0.21%, 0.27%] | 0.583 [0.567, 0.599] | 26.2% | 16.9% | 0.000% | 100 | 59928 |
| 20 | 6.78% [6.31%, 7.25%] | 1.45% | 6.84% | -0.05% [-0.16%, 0.05%] | 2.44% [2.29%, 2.61%] | 1.25% | 2.54% | -0.10% [-0.30%, 0.09%] | 0.553 [0.533, 0.574] | 15.6% | 10.2% | 0.000% | 100 | 59691 |
| 100 | 3.75% [3.63%, 3.88%] | 0.73% | 3.75% | 0.01% [-0.03%, 0.04%] | 1.25% [1.20%, 1.30%] | 0.62% | 1.27% | -0.02% [-0.09%, 0.04%] | 0.543 [0.533, 0.554] | 6.4% | 5.3% | 0.000% | 100 | 291453 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.14% [9.62%, 10.65%] | 1.92% | 9.29% | 0.85% [0.63%, 1.06%] | 3.82% [3.64%, 3.99%] | 1.64% | 3.27% | 0.55% [0.25%, 0.85%] | 0.595 [0.582, 0.608] | 24.2% | 19.2% | 0.000% | 100 | 39952 |
| 20 | 7.40% [6.96%, 7.83%] | 1.46% | 6.84% | 0.56% [0.35%, 0.80%] | 2.91% [2.77%, 3.06%] | 1.25% | 2.54% | 0.37% [0.12%, 0.62%] | 0.570 [0.555, 0.586] | 16.1% | 11.8% | 0.000% | 100 | 39794 |
| 100 | 4.22% [4.10%, 4.34%] | 0.73% | 3.75% | 0.48% [0.40%, 0.56%] | 1.49% [1.43%, 1.54%] | 0.62% | 1.27% | 0.22% [0.13%, 0.30%] | 0.560 [0.552, 0.569] | 7.6% | 6.5% | 0.000% | 100 | 194302 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

The rows cover every record; every record the node can select because it held a destination role; and the split by whether it held a first relay, which it cannot tell.

| R | Records | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | all records | 399,520 | 3995 | 9.45% | 9.29% | +0.15 [+0.08, +0.23] | 26.6% | 0.0000% | pass |
| 20 | all records | 397,940 | 3979 | 6.88% | 6.84% | +0.05 [-0.03, +0.12] | 15.6% | 0.0003% | pass |
| 100 | all records | 1,943,020 | 19430 | 3.81% | 3.75% | +0.07 [+0.04, +0.09] | 6.8% | 0.0000% | pass |
| 1 | every record the node can select | 59,928 | 599 | 9.90% | 9.29% | +0.61 [+0.44, +0.79] | 28.0% | 0.0000% | pass |
| 1 | first relay held | 19,100 | 191 | 10.38% | 9.59% | +0.79 [+0.58, +1.01] | 38.3% | 0.0471% | pass |
| 1 | no first relay held | 380,420 | 3804 | 9.40% | 9.28% | +0.12 [+0.05, +0.20] | 26.3% | 0.0000% | pass |
| 20 | every record the node can select | 59,691 | 597 | 7.21% | 6.84% | +0.38 [+0.22, +0.54] | 18.7% | 0.0017% | pass |
| 20 | first relay held | 19,052 | 191 | 7.29% | 6.74% | +0.55 [+0.32, +0.79] | 16.2% | 0.0052% | pass |
| 20 | no first relay held | 378,888 | 3789 | 6.86% | 6.84% | +0.02 [-0.05, +0.10] | 15.9% | 0.0000% | pass |
| 100 | every record the node can select | 291,453 | 2915 | 4.07% | 3.75% | +0.32 [+0.26, +0.38] | 8.4% | 0.0000% | pass |
| 100 | first relay held | 93,076 | 931 | 4.08% | 3.73% | +0.35 [+0.28, +0.44] | 8.3% | 0.0000% | pass |
| 100 | no first relay held | 1,849,944 | 18499 | 3.80% | 3.75% | +0.05 [+0.03, +0.08] | 6.8% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there. Prevalence is the class's share of the node's decisions. Combined minus the sum is the combined lead minus the two single-role leads, paired on the same rows.

| R | Roles held | Prevalence | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined minus the sum [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 11.95% | 47,729 | 477 | 9.64% | 9.09% | +0.54 [+0.34, +0.75] | +0.01 [-0.06, +0.08] | +0.55 [+0.39, +0.72] | -0.02 [-0.11, +0.06] | 29.0% | 0.0000% | pass |
| 1 | credential first relay + content destination | 0.51% | 2,033 | 20 | 10.77% | 9.59% | +1.18 [+0.35, +2.00] | -0.10 [-0.56, +0.36] | +1.33 [+0.55, +2.16] | -0.05 [-0.70, +0.68] | 46.9% | 0.4427% | fail |
| 1 | content first relay + content destination | 0.50% | 1,981 | 20 | 12.17% | 10.15% | +2.02 [+1.02, +3.01] | +0.91 [+0.25, +1.61] | +0.76 [-0.25, +1.80] | +0.35 [-0.54, +1.16] | 56.7% | 0.0000% | fail |
| 1 | content first relay + credential destination | 0.52% | 2,093 | 21 | 11.37% | 10.89% | +0.48 [+0.05, +0.90] | +0.53 [+0.05, +1.05] | -0.10 [-0.24, +0.00] | +0.05 [-0.28, +0.36] | 45.1% | 0.0000% | pass |
| 1 | second relay + destination | 1.38% | 5,518 | 55 | 10.49% | 10.11% | +0.38 [-0.09, +0.85] | -0.27 [-0.51, -0.05] | +0.49 [+0.05, +0.94] | +0.16 [-0.11, +0.44] | 26.2% | 0.0000% | pass |
| 1 | three or more roles, with a destination | 0.14% | 574 | 6 | 10.28% | 8.19% | +2.09 [+0.53, +3.71] | +1.22 [+0.34, +2.19] | +0.70 [-0.55, +2.12] | +0.17 [-0.84, +1.22] | 56.4% | 0.0000% | fail |
| 20 | destination only | 11.94% | 47,502 | 475 | 7.17% | 6.92% | +0.25 [+0.07, +0.42] | -0.05 [-0.12, +0.01] | +0.30 [+0.14, +0.47] | +0.00 [-0.08, +0.09] | 18.7% | 0.0000% | pass |
| 20 | credential first relay + content destination | 0.50% | 1,995 | 20 | 8.07% | 6.22% | +1.85 [+0.94, +2.79] | +0.05 [-0.31, +0.43] | +1.55 [+0.70, +2.41] | +0.25 [-0.27, +0.84] | 41.6% | 0.0501% | pass |
| 20 | content first relay + content destination | 0.51% | 2,032 | 20 | 7.28% | 6.84% | +0.44 [-0.40, +1.32] | +0.25 [-0.29, +0.76] | -0.30 [-1.15, +0.52] | +0.49 [-0.10, +1.13] | 36.0% | 0.0000% | pass |
| 20 | content first relay + credential destination | 0.52% | 2,067 | 21 | 6.68% | 6.05% | +0.63 [+0.15, +1.06] | +0.58 [+0.15, +1.00] | +0.15 [+0.00, +0.33] | -0.10 [-0.37, +0.15] | 22.7% | 0.0000% | pass |
| 20 | second relay + destination | 1.39% | 5,550 | 56 | 7.32% | 6.68% | +0.63 [+0.13, +1.09] | +0.23 [+0.02, +0.46] | +0.76 [+0.29, +1.24] | -0.36 [-0.60, -0.13] | 31.8% | 0.0541% | pass |
| 20 | three or more roles, with a destination | 0.14% | 545 | 5 | unstable: 112 runs needed | | | | | | | | |
| 100 | destination only | 11.95% | 232,253 | 2323 | 4.02% | 3.74% | +0.28 [+0.23, +0.34] | -0.02 [-0.05, +0.01] | +0.31 [+0.26, +0.37] | -0.01 [-0.04, +0.02] | 8.5% | 0.0000% | pass |
| 100 | credential first relay + content destination | 0.49% | 9,599 | 96 | 3.99% | 3.38% | +0.61 [+0.32, +0.91] | +0.03 [-0.11, +0.18] | +0.57 [+0.28, +0.88] | +0.01 [-0.22, +0.26] | 11.6% | 0.0000% | pass |
| 100 | content first relay + content destination | 0.51% | 9,891 | 99 | 4.88% | 4.08% | +0.80 [+0.48, +1.11] | +0.23 [+0.09, +0.38] | +0.48 [+0.16, +0.80] | +0.09 [-0.15, +0.33] | 13.9% | 0.0000% | pass |
| 100 | content first relay + credential destination | 0.52% | 10,159 | 102 | 4.38% | 4.00% | +0.38 [+0.22, +0.57] | +0.39 [+0.21, +0.58] | +0.00 [-0.06, +0.06] | -0.01 [-0.10, +0.08] | 13.5% | 0.0000% | pass |
| 100 | second relay + destination | 1.39% | 27,052 | 271 | 3.98% | 3.65% | +0.33 [+0.17, +0.49] | -0.03 [-0.10, +0.03] | +0.32 [+0.16, +0.49] | +0.04 [-0.03, +0.12] | 11.1% | 0.0000% | pass |
| 100 | three or more roles, with a destination | 0.13% | 2,499 | 25 | 4.68% | 4.08% | +0.60 [+0.04, +1.13] | +0.28 [+0.00, +0.58] | +0.44 [-0.04, +0.96] | -0.12 [-0.45, +0.20] | 25.0% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 198,610 | 1986 | 9.30% | 9.33% | -0.03 [-0.09, +0.04] | 27.0% | 0.0000% | pass |
| 1 | one relay or gatekeeper role | 116,616 | 1166 | 9.42% | 9.25% | +0.17 [+0.08, +0.26] | 27.7% | 0.0000% | pass |
| 1 | second relay + first relay | 4,569 | 46 | 9.30% | 8.80% | +0.50 [+0.13, +0.92] | 40.3% | 0.0000% | pass |
| 1 | second relay + second relay | 2,034 | 20 | 9.39% | 9.14% | +0.25 [-0.10, +0.59] | 51.9% | 0.4425% | fail |
| 1 | gatekeeper + first relay | 8,424 | 84 | 10.20% | 9.57% | +0.63 [+0.37, +0.91] | 40.2% | 0.3680% | fail |
| 1 | gatekeeper + second relay | 7,719 | 77 | 9.34% | 9.12% | +0.22 [-0.04, +0.49] | 39.5% | 0.0000% | pass |
| 1 | three or more roles, no destination | 1,620 | 16 | 9.57% | 9.14% | +0.43 [-0.18, +1.01] | 43.0% | 0.0000% | pass |
| 20 | no role | 197,684 | 1977 | 6.75% | 6.81% | -0.06 [-0.12, -0.00] | 15.3% | 0.0000% | pass |
| 20 | one relay or gatekeeper role | 116,422 | 1164 | 6.92% | 6.88% | +0.04 [-0.06, +0.14] | 18.0% | 0.0000% | pass |
| 20 | second relay + first relay | 4,579 | 46 | 7.29% | 7.03% | +0.26 [-0.04, +0.56] | 25.7% | 0.0218% | pass |
| 20 | second relay + second relay | 2,093 | 21 | 6.45% | 6.69% | -0.24 [-0.59, +0.10] | 28.9% | 0.0000% | pass |
| 20 | gatekeeper + first relay | 8,379 | 84 | 7.26% | 6.85% | +0.41 [+0.09, +0.72] | 23.3% | 0.0000% | pass |
| 20 | gatekeeper + second relay | 7,502 | 75 | 6.45% | 6.58% | -0.13 [-0.35, +0.08] | 25.9% | 0.0133% | pass |
| 20 | three or more roles, no destination | 1,590 | 16 | 7.42% | 7.04% | +0.38 [-0.13, +0.95] | 43.0% | 0.0000% | pass |
| 100 | no role | 965,013 | 9650 | 3.74% | 3.75% | -0.01 [-0.03, +0.01] | 6.8% | 0.0000% | pass |
| 100 | one relay or gatekeeper role | 568,481 | 5685 | 3.80% | 3.74% | +0.06 [+0.03, +0.09] | 7.1% | 0.0000% | pass |
| 100 | second relay + first relay | 22,569 | 226 | 4.03% | 3.79% | +0.23 [+0.13, +0.34] | 10.7% | 0.0000% | pass |
| 100 | second relay + second relay | 10,074 | 101 | 3.48% | 3.41% | +0.07 [-0.07, +0.21] | 8.4% | 0.0000% | pass |
| 100 | gatekeeper + first relay | 40,858 | 409 | 3.87% | 3.62% | +0.24 [+0.15, +0.34] | 9.2% | 0.0000% | pass |
| 100 | gatekeeper + second relay | 36,728 | 367 | 3.87% | 3.90% | -0.03 [-0.11, +0.06] | 11.4% | 0.0000% | pass |
| 100 | three or more roles, no destination | 7,844 | 78 | 4.19% | 3.99% | +0.20 [+0.00, +0.41] | 10.7% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | +0.05 [-0.01, +0.11] | +0.07 [-0.01, +0.14] | n/a |
| First hop, credential | 20 | +0.00 [-0.05, +0.05] | +0.03 [-0.06, +0.11] | n/a |
| First hop, credential | 100 | +0.02 [+0.00, +0.04] | +0.02 [-0.00, +0.04] | n/a |
| First hop, content | 1 | +0.05 [-0.01, +0.11] | +0.07 [-0.01, +0.15] | n/a |
| First hop, content | 20 | +0.00 [-0.05, +0.05] | +0.03 [-0.05, +0.11] | n/a |
| First hop, content | 100 | +0.02 [+0.00, +0.04] | +0.02 [-0.00, +0.04] | n/a |
| Credential processor | 1 | -0.01 [-0.05, +0.03] | -0.03 [-0.08, +0.02] | n/a |
| Credential processor | 20 | -0.01 [-0.04, +0.02] | -0.02 [-0.06, +0.02] | n/a |
| Credential processor | 100 | -0.00 [-0.01, +0.01] | -0.00 [-0.01, +0.01] | n/a |

## Outcome-shuffle control

80 stable rows; 2 with a shuffled-outcome AUC interval excluding 0.5: R = 100 combined: one relay or gatekeeper role (0.506), R = 100 combined: first relay held (0.513).

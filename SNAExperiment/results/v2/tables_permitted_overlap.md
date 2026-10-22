# permitted overlap

Build `permitted_overlap`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1108.8 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Paired against InternalCompromiseRun

Accuracy under this build minus accuracy under InternalCompromiseRun, matched record by record on identical traffic (percentage points).

| Vantage | R | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|
| Passive observer | 1 | +0.03 [-0.03, +0.09] | -0.02 [-0.13, +0.09] | 39888 |
| Passive observer | 20 | -0.02 [-0.07, +0.03] | -0.04 [-0.16, +0.08] | 40033 |
| Passive observer | 100 | +0.01 [-0.01, +0.02] | +0.02 [-0.02, +0.06] | 194130 |
| First hop, credential | 1 | +0.05 [-0.01, +0.11] | -0.03 [-0.14, +0.08] | 159552 |
| First hop, credential | 20 | -0.01 [-0.07, +0.05] | +0.09 [+0.00, +0.17] | 160132 |
| First hop, credential | 100 | +0.00 [-0.02, +0.02] | -0.01 [-0.04, +0.01] | 776520 |
| First hop, content | 1 | +0.05 [-0.01, +0.11] | -0.03 [-0.14, +0.08] | 159552 |
| First hop, content | 20 | -0.01 [-0.07, +0.05] | +0.09 [+0.01, +0.18] | 160132 |
| First hop, content | 100 | +0.00 [-0.02, +0.02] | -0.01 [-0.04, +0.02] | 776520 |
| Credential processor | 1 | +0.01 [-0.04, +0.06] | -0.02 [-0.11, +0.07] | 159552 |
| Credential processor | 20 | +0.01 [-0.04, +0.06] | -0.03 [-0.11, +0.05] | 160132 |
| Credential processor | 100 | +0.00 [-0.01, +0.01] | +0.01 [-0.02, +0.03] | 776520 |
| Validator | 1 | +0.07 [-0.07, +0.20] | +0.16 [-0.04, +0.36] | 39888 |
| Validator | 20 | +0.06 [-0.05, +0.16] | +0.22 [+0.03, +0.42] | 40033 |
| Validator | 100 | -0.03 [-0.06, +0.01] | +0.01 [-0.05, +0.07] | 194130 |
| Gatekeeper | 1 | +0.03 [-0.02, +0.08] | -0.05 [-0.13, +0.03] | 119664 |
| Gatekeeper | 20 | -0.02 [-0.08, +0.03] | +0.01 [-0.06, +0.08] | 120099 |
| Gatekeeper | 100 | +0.00 [-0.01, +0.02] | -0.02 [-0.04, +0.00] | 582390 |
| Content server | 1 | +0.09 [-0.03, +0.22] | -0.12 [-0.28, +0.05] | 79776 |
| Content server | 20 | +0.05 [-0.07, +0.17] | +0.19 [+0.05, +0.34] | 80066 |
| Content server | 100 | -0.00 [-0.04, +0.04] | +0.00 [-0.05, +0.05] | 388260 |

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8.49% [8.09%, 8.91%] | 1.72% | 8.49% | 0.00% [0.00%, 0.00%] | 2.53% [2.40%, 2.68%] | 1.64% | 2.53% | 0.00% [0.00%, 0.00%] | 0.575 [0.562, 0.588] | 18.8% | 14.5% | 0.048% | 200 | 39888 |
| 20 | 5.81% [5.46%, 6.13%] | 1.31% | 5.81% | 0.00% [0.00%, 0.00%] | 1.89% [1.77%, 2.02%] | 1.25% | 1.89% | 0.00% [0.00%, 0.00%] | 0.560 [0.545, 0.575] | 14.5% | 9.6% | 0.000% | 200 | 40033 |
| 100 | 3.25% [3.16%, 3.34%] | 0.66% | 3.25% | 0.00% [0.00%, 0.00%] | 1.02% [0.98%, 1.07%] | 0.62% | 1.02% | 0.00% [0.00%, 0.00%] | 0.548 [0.539, 0.557] | 5.4% | 4.5% | 0.000% | 200 | 194130 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8.49% [8.07%, 8.92%] | 1.72% | 8.49% | -0.00% [-0.04%, 0.03%] | 2.59% [2.53%, 2.67%] | 1.64% | 2.53% | 0.06% [-0.02%, 0.14%] | 0.575 [0.562, 0.589] | 18.9% | 14.7% | 0.003% | 200 | 797760 |
| 20 | 5.81% [5.46%, 6.15%] | 1.31% | 5.81% | -0.01% [-0.04%, 0.02%] | 1.97% [1.91%, 2.02%] | 1.25% | 1.89% | 0.07% [-0.01%, 0.15%] | 0.561 [0.547, 0.576] | 14.5% | 9.6% | 0.000% | 200 | 800660 |
| 100 | 3.26% [3.17%, 3.34%] | 0.66% | 3.25% | 0.00% [-0.01%, 0.01%] | 1.01% [1.00%, 1.02%] | 0.62% | 1.02% | -0.01% [-0.05%, 0.03%] | 0.548 [0.539, 0.556] | 5.4% | 4.5% | 0.000% | 200 | 3882600 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8.49% [8.10%, 8.91%] | 1.72% | 8.49% | -0.00% [-0.04%, 0.03%] | 2.59% [2.52%, 2.67%] | 1.64% | 2.53% | 0.06% [-0.02%, 0.14%] | 0.575 [0.562, 0.589] | 18.9% | 14.7% | 0.003% | 200 | 797760 |
| 20 | 5.81% [5.45%, 6.15%] | 1.31% | 5.81% | -0.01% [-0.04%, 0.02%] | 1.97% [1.91%, 2.02%] | 1.25% | 1.89% | 0.07% [-0.01%, 0.16%] | 0.561 [0.547, 0.576] | 14.5% | 9.6% | 0.000% | 200 | 800660 |
| 100 | 3.26% [3.17%, 3.35%] | 0.66% | 3.25% | 0.00% [-0.01%, 0.01%] | 1.01% [1.00%, 1.02%] | 0.62% | 1.02% | -0.01% [-0.05%, 0.02%] | 0.548 [0.539, 0.556] | 5.4% | 4.5% | 0.000% | 200 | 3882600 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8.47% [8.05%, 8.89%] | 1.72% | 8.49% | -0.02% [-0.06%, 0.01%] | 2.54% [2.44%, 2.64%] | 1.64% | 2.53% | 0.00% [-0.08%, 0.08%] | 0.575 [0.562, 0.589] | 18.7% | 14.6% | 0.005% | 200 | 678096 |
| 20 | 5.80% [5.48%, 6.14%] | 1.31% | 5.81% | -0.01% [-0.03%, 0.01%] | 1.91% [1.82%, 2.01%] | 1.25% | 1.89% | 0.02% [-0.05%, 0.09%] | 0.561 [0.546, 0.576] | 14.8% | 9.6% | 0.000% | 200 | 680561 |
| 100 | 3.25% [3.16%, 3.34%] | 0.66% | 3.25% | -0.01% [-0.01%, 0.00%] | 1.01% [0.98%, 1.04%] | 0.62% | 1.02% | -0.01% [-0.03%, 0.01%] | 0.548 [0.540, 0.557] | 5.4% | 4.5% | 0.000% | 200 | 3300210 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8.07% [7.69%, 8.46%] | 1.85% | 8.49% | -0.43% [-0.72%, -0.14%] | 3.51% [3.33%, 3.68%] | 1.64% | 2.53% | 0.98% [0.75%, 1.19%] | 0.569 [0.555, 0.583] | 16.8% | 14.0% | 0.003% | 200 | 39888 |
| 20 | 5.39% [5.11%, 5.69%] | 1.40% | 5.81% | -0.42% [-0.67%, -0.19%] | 2.76% [2.59%, 2.92%] | 1.25% | 1.89% | 0.86% [0.67%, 1.07%] | 0.547 [0.531, 0.562] | 11.2% | 8.5% | 0.000% | 200 | 40033 |
| 100 | 2.91% [2.82%, 3.00%] | 0.70% | 3.25% | -0.35% [-0.43%, -0.27%] | 1.44% [1.39%, 1.48%] | 0.62% | 1.02% | 0.41% [0.35%, 0.47%] | 0.548 [0.539, 0.557] | 4.7% | 4.3% | 0.000% | 200 | 194130 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8.46% [8.05%, 8.88%] | 1.72% | 8.49% | -0.03% [-0.11%, 0.04%] | 2.55% [2.45%, 2.65%] | 1.64% | 2.53% | 0.02% [-0.14%, 0.17%] | 0.576 [0.562, 0.589] | 18.7% | 14.5% | 0.004% | 200 | 119664 |
| 20 | 5.80% [5.50%, 6.13%] | 1.31% | 5.81% | -0.01% [-0.08%, 0.05%] | 1.97% [1.88%, 2.05%] | 1.25% | 1.89% | 0.07% [-0.06%, 0.21%] | 0.536 [0.521, 0.551] | 9.9% | 8.2% | 0.000% | 200 | 120099 |
| 100 | 3.26% [3.17%, 3.34%] | 0.66% | 3.25% | 0.00% [-0.02%, 0.02%] | 0.98% [0.95%, 1.00%] | 0.62% | 1.02% | -0.04% [-0.09%, 0.00%] | 0.548 [0.540, 0.557] | 5.5% | 4.5% | 0.000% | 200 | 582390 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.06% [9.65%, 10.44%] | 1.81% | 8.49% | 1.56% [1.34%, 1.79%] | 3.64% [3.52%, 3.76%] | 1.64% | 2.53% | 1.10% [0.91%, 1.29%] | 0.577 [0.567, 0.588] | 22.6% | 17.0% | 0.039% | 200 | 79776 |
| 20 | 7.11% [6.82%, 7.40%] | 1.37% | 5.81% | 1.30% [1.11%, 1.49%] | 2.90% [2.79%, 3.02%] | 1.25% | 1.89% | 1.01% [0.85%, 1.17%] | 0.565 [0.552, 0.578] | 13.9% | 11.3% | 0.000% | 200 | 80066 |
| 100 | 3.98% [3.90%, 4.06%] | 0.69% | 3.25% | 0.72% [0.65%, 0.79%] | 1.40% [1.37%, 1.44%] | 0.62% | 1.02% | 0.38% [0.32%, 0.44%] | 0.552 [0.546, 0.559] | 6.3% | 5.8% | 0.000% | 200 | 388260 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

The rows cover every record; every record the node can select because it held a destination role; and the split by whether it held a first relay, which it cannot tell.

| R | Records | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | all records | 797,760 | 7978 | 8.63% | 8.49% | +0.14 [+0.08, +0.19] | 20.9% | 0.0000% | pass |
| 20 | all records | 800,660 | 8007 | 5.93% | 5.81% | +0.12 [+0.08, +0.17] | 14.9% | 0.0000% | pass |
| 100 | all records | 3,882,600 | 38826 | 3.32% | 3.25% | +0.07 [+0.05, +0.09] | 6.0% | 0.0000% | pass |
| 1 | every record the node can select | 119,664 | 1197 | 9.53% | 8.49% | +1.03 [+0.87, +1.19] | 23.9% | 0.0000% | pass |
| 1 | first relay held | 38,459 | 385 | 8.96% | 8.46% | +0.50 [+0.35, +0.66] | 25.4% | 0.0338% | pass |
| 1 | no first relay held | 759,301 | 7593 | 8.61% | 8.50% | +0.12 [+0.06, +0.17] | 20.7% | 0.0000% | pass |
| 20 | every record the node can select | 120,099 | 1201 | 6.68% | 5.81% | +0.87 [+0.73, +1.00] | 15.6% | 0.0000% | pass |
| 20 | first relay held | 38,438 | 384 | 6.10% | 5.83% | +0.27 [+0.13, +0.41] | 17.9% | 0.0000% | pass |
| 20 | no first relay held | 762,222 | 7622 | 5.93% | 5.81% | +0.11 [+0.07, +0.16] | 15.0% | 0.0000% | pass |
| 100 | every record the node can select | 582,390 | 5824 | 3.72% | 3.25% | +0.46 [+0.41, +0.51] | 7.0% | 0.0000% | pass |
| 100 | first relay held | 186,082 | 1861 | 3.44% | 3.30% | +0.14 [+0.09, +0.19] | 6.8% | 0.0000% | pass |
| 100 | no first relay held | 3,696,518 | 36965 | 3.32% | 3.25% | +0.07 [+0.05, +0.08] | 6.0% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there. Prevalence is the class's share of the node's decisions. Combined minus the sum is the combined lead minus the two single-role leads, paired on the same rows.

| R | Roles held | Prevalence | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined minus the sum [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 11.93% | 95,156 | 952 | 9.43% | 8.42% | +1.02 [+0.85, +1.19] | -0.02 [-0.07, +0.03] | +1.04 [+0.87, +1.19] | -0.00 [-0.06, +0.06] | 24.4% | 0.0000% | pass |
| 1 | credential first relay + content destination | 0.50% | 3,995 | 40 | 10.66% | 8.31% | +2.35 [+1.47, +3.24] | +0.05 [-0.28, +0.38] | +2.23 [+1.33, +3.13] | +0.08 [-0.38, +0.52] | 42.8% | 0.1252% | fail |
| 1 | content first relay + content destination | 0.52% | 4,132 | 41 | 10.70% | 9.24% | +1.45 [+0.71, +2.23] | +0.12 [-0.17, +0.39] | +1.43 [+0.71, +2.20] | -0.10 [-0.55, +0.34] | 41.9% | 0.1210% | fail |
| 1 | content first relay + credential destination | 0.52% | 4,182 | 42 | 9.01% | 8.99% | +0.02 [-0.28, +0.31] | -0.12 [-0.36, +0.12] | -0.07 [-0.19, +0.02] | +0.22 [+0.07, +0.40] | 33.3% | 0.1674% | fail |
| 1 | second relay + destination | 1.39% | 11,117 | 111 | 9.71% | 8.77% | +0.94 [+0.50, +1.40] | -0.05 [-0.17, +0.06] | +0.87 [+0.46, +1.28] | +0.13 [-0.06, +0.31] | 28.2% | 0.1169% | fail |
| 1 | three or more roles, with a destination | 0.14% | 1,082 | 11 | 9.15% | 8.32% | +0.83 [-0.47, +2.32] | +0.09 [-0.38, +0.57] | +0.83 [-0.58, +2.29] | -0.09 [-0.81, +0.63] | 37.7% | 0.0000% | pass |
| 20 | destination only | 11.96% | 95,732 | 957 | 6.67% | 5.84% | +0.83 [+0.67, +0.97] | +0.01 [-0.04, +0.05] | +0.85 [+0.70, +1.00] | -0.03 [-0.07, +0.02] | 15.8% | 0.0000% | pass |
| 20 | credential first relay + content destination | 0.50% | 4,010 | 40 | 7.03% | 5.44% | +1.60 [+0.91, +2.28] | +0.22 [+0.00, +0.45] | +1.40 [+0.72, +2.08] | -0.02 [-0.38, +0.35] | 29.1% | 0.0000% | pass |
| 20 | content first relay + content destination | 0.51% | 4,067 | 41 | 6.54% | 5.66% | +0.89 [+0.13, +1.63] | +0.02 [-0.22, +0.29] | +0.76 [-0.02, +1.58] | +0.10 [-0.31, +0.54] | 16.1% | 0.0000% | pass |
| 20 | content first relay + credential destination | 0.51% | 4,122 | 41 | 6.04% | 6.09% | -0.05 [-0.24, +0.14] | -0.10 [-0.30, +0.08] | -0.12 [-0.25, +0.00] | +0.17 [+0.03, +0.34] | 19.4% | 0.0000% | pass |
| 20 | second relay + destination | 1.38% | 11,073 | 111 | 6.87% | 5.54% | +1.34 [+0.95, +1.73] | +0.11 [+0.00, +0.23] | +1.26 [+0.89, +1.66] | -0.04 [-0.18, +0.12] | 28.2% | 0.0000% | pass |
| 20 | three or more roles, with a destination | 0.14% | 1,095 | 11 | 7.21% | 6.85% | +0.37 [-0.74, +1.43] | -0.37 [-0.74, -0.09] | +0.18 [-0.93, +1.23] | +0.55 [+0.00, +1.13] | 37.7% | 0.0000% | pass |
| 100 | destination only | 11.95% | 463,781 | 4638 | 3.71% | 3.23% | +0.48 [+0.43, +0.53] | -0.00 [-0.02, +0.01] | +0.50 [+0.46, +0.55] | -0.03 [-0.04, -0.01] | 7.1% | 0.0000% | pass |
| 100 | credential first relay + content destination | 0.50% | 19,257 | 193 | 3.76% | 3.32% | +0.44 [+0.19, +0.69] | +0.07 [-0.02, +0.16] | +0.48 [+0.25, +0.73] | -0.11 [-0.24, +0.02] | 11.2% | 0.0000% | pass |
| 100 | content first relay + content destination | 0.51% | 19,935 | 199 | 4.13% | 3.53% | +0.60 [+0.32, +0.88] | +0.02 [-0.09, +0.13] | +0.51 [+0.23, +0.77] | +0.08 [-0.08, +0.23] | 11.5% | 0.0000% | pass |
| 100 | content first relay + credential destination | 0.52% | 20,275 | 203 | 3.50% | 3.46% | +0.04 [-0.05, +0.13] | +0.03 [-0.05, +0.12] | -0.00 [-0.04, +0.02] | +0.01 [-0.03, +0.05] | 10.6% | 0.0000% | pass |
| 100 | second relay + destination | 1.39% | 54,063 | 541 | 3.67% | 3.25% | +0.42 [+0.30, +0.54] | -0.01 [-0.06, +0.02] | +0.44 [+0.32, +0.55] | -0.00 [-0.06, +0.05] | 8.9% | 0.0000% | pass |
| 100 | three or more roles, with a destination | 0.13% | 5,079 | 51 | 3.80% | 3.09% | +0.71 [+0.29, +1.10] | +0.06 [-0.10, +0.23] | +0.57 [+0.16, +0.95] | +0.08 [-0.13, +0.30] | 18.5% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 396,722 | 3967 | 8.47% | 8.50% | -0.04 [-0.09, +0.01] | 20.2% | 0.0038% | pass |
| 1 | one relay or gatekeeper role | 232,662 | 2327 | 8.49% | 8.50% | -0.00 [-0.08, +0.06] | 19.8% | 0.0417% | pass |
| 1 | second relay + first relay | 9,333 | 93 | 8.38% | 8.19% | +0.19 [+0.02, +0.39] | 22.5% | 0.0536% | pass |
| 1 | second relay + second relay | 4,086 | 41 | 8.32% | 8.25% | +0.07 [-0.15, +0.30] | 44.5% | 0.4161% | fail |
| 1 | gatekeeper + first relay | 16,817 | 168 | 8.44% | 8.32% | +0.12 [-0.04, +0.29] | 28.2% | 0.0892% | pass |
| 1 | gatekeeper + second relay | 15,247 | 152 | 8.51% | 8.69% | -0.18 [-0.36, +0.01] | 28.2% | 0.0000% | pass |
| 1 | three or more roles, no destination | 3,229 | 32 | 8.45% | 8.49% | -0.03 [-0.32, +0.28] | 20.1% | 0.0000% | pass |
| 20 | no role | 397,718 | 3977 | 5.78% | 5.81% | -0.03 [-0.07, +0.00] | 10.6% | 0.0000% | pass |
| 20 | one relay or gatekeeper role | 234,185 | 2342 | 5.83% | 5.81% | +0.02 [-0.04, +0.07] | 16.7% | 0.0000% | pass |
| 20 | second relay + first relay | 9,357 | 94 | 6.15% | 6.09% | +0.05 [-0.10, +0.21] | 27.1% | 0.0000% | pass |
| 20 | second relay + second relay | 4,229 | 42 | 6.20% | 6.08% | +0.12 [-0.10, +0.34] | 25.0% | 0.0000% | pass |
| 20 | gatekeeper + first relay | 16,882 | 169 | 5.77% | 5.76% | +0.01 [-0.15, +0.16] | 16.2% | 0.0000% | pass |
| 20 | gatekeeper + second relay | 14,935 | 149 | 5.59% | 5.66% | -0.07 [-0.21, +0.07] | 16.7% | 0.0000% | pass |
| 20 | three or more roles, no destination | 3,255 | 33 | 6.39% | 5.99% | +0.40 [+0.06, +0.76] | 34.4% | 0.0000% | pass |
| 100 | no role | 1,928,578 | 19286 | 3.26% | 3.26% | -0.00 [-0.01, +0.01] | 5.7% | 0.0000% | pass |
| 100 | one relay or gatekeeper role | 1,135,901 | 11359 | 3.24% | 3.24% | +0.00 [-0.02, +0.02] | 5.9% | 0.0000% | pass |
| 100 | second relay + first relay | 45,108 | 451 | 3.37% | 3.32% | +0.05 [-0.00, +0.11] | 8.8% | 0.0000% | pass |
| 100 | second relay + second relay | 20,167 | 202 | 3.00% | 2.98% | +0.02 [-0.03, +0.08] | 7.6% | 0.0000% | pass |
| 100 | gatekeeper + first relay | 81,507 | 815 | 3.22% | 3.19% | +0.03 [-0.02, +0.08] | 7.2% | 0.0000% | pass |
| 100 | gatekeeper + second relay | 73,198 | 732 | 3.35% | 3.36% | -0.01 [-0.07, +0.05] | 9.0% | 0.0000% | pass |
| 100 | three or more roles, no destination | 15,751 | 158 | 3.40% | 3.36% | +0.04 [-0.05, +0.15] | 8.9% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | -0.00 [-0.04, +0.03] | +0.00 [-0.04, +0.05] | -0.02 [-0.07, +0.03] |
| First hop, credential | 20 | -0.01 [-0.04, +0.02] | -0.01 [-0.05, +0.04] | -0.02 [-0.06, +0.02] |
| First hop, credential | 100 | +0.00 [-0.01, +0.01] | +0.01 [-0.01, +0.02] | +0.01 [-0.00, +0.03] |
| First hop, content | 1 | -0.00 [-0.04, +0.03] | +0.00 [-0.04, +0.05] | -0.02 [-0.06, +0.03] |
| First hop, content | 20 | -0.01 [-0.04, +0.02] | -0.01 [-0.05, +0.04] | -0.02 [-0.06, +0.03] |
| First hop, content | 100 | +0.00 [-0.01, +0.01] | +0.01 [-0.01, +0.02] | +0.01 [-0.00, +0.03] |
| Credential processor | 1 | -0.02 [-0.06, +0.01] | -0.02 [-0.06, +0.01] | -0.00 [-0.04, +0.03] |
| Credential processor | 20 | -0.01 [-0.03, +0.01] | -0.02 [-0.04, +0.01] | -0.04 [-0.07, -0.02] |
| Credential processor | 100 | -0.01 [-0.01, +0.00] | -0.01 [-0.02, +0.00] | +0.00 [-0.01, +0.01] |

## Paired against InternalCompromiseRun, records with no coincidence

Accuracy under this build minus accuracy under InternalCompromiseRun, matched record by record, on the records whose transaction has no node in roles on two different paths (percentage points).

| Vantage | R | Device effect [95% CI] | Matched rows |
|---|---|---|---|
| Passive observer | 1 | +0.01 [-0.10, +0.11] | 10367 |
| Passive observer | 20 | +0.01 [-0.08, +0.09] | 10447 |
| Passive observer | 100 | +0.03 [-0.00, +0.06] | 51019 |
| First hop, credential | 1 | +0.07 [-0.04, +0.18] | 41468 |
| First hop, credential | 20 | +0.03 [-0.07, +0.14] | 41788 |
| First hop, credential | 100 | +0.01 [-0.02, +0.04] | 204076 |
| First hop, content | 1 | +0.07 [-0.04, +0.18] | 41468 |
| First hop, content | 20 | +0.03 [-0.07, +0.14] | 41788 |
| First hop, content | 100 | +0.01 [-0.02, +0.04] | 204076 |
| Credential processor | 1 | -0.00 [-0.10, +0.10] | 41468 |
| Credential processor | 20 | +0.05 [-0.02, +0.13] | 41788 |
| Credential processor | 100 | +0.01 [-0.01, +0.04] | 204076 |
| Validator | 1 | +0.04 [-0.20, +0.27] | 10367 |
| Validator | 20 | +0.12 [-0.08, +0.31] | 10447 |
| Validator | 100 | -0.02 [-0.09, +0.06] | 51019 |
| Gatekeeper | 1 | -0.01 [-0.10, +0.08] | 31101 |
| Gatekeeper | 20 | +0.01 [-0.07, +0.09] | 31341 |
| Gatekeeper | 100 | +0.01 [-0.01, +0.04] | 153057 |
| Content server | 1 | +0.13 [-0.11, +0.36] | 20734 |
| Content server | 20 | +0.07 [-0.14, +0.30] | 20894 |
| Content server | 100 | +0.04 [-0.05, +0.12] | 102038 |

## Outcome-shuffle control

81 stable rows; 11 with a shuffled-outcome AUC interval excluding 0.5: R = 1 Passive observer (0.512), R = 1 Gatekeeper (0.508), R = 20 First hop, credential (0.508), R = 20 First hop, content (0.505), R = 100 First hop, content (0.503), R = 100 Credential processor (0.503), R = 1 combined: three or more roles, with a destination (0.565), R = 20 combined: second relay + destination (0.526), R = 100 combined: all records (0.502), R = 100 combined: one relay or gatekeeper role (0.504), R = 20 combined: no first relay held (0.506).

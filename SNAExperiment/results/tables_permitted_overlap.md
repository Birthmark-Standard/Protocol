# permitted overlap

Build `permitted_overlap`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1036.6 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Paired against InternalCompromiseRun

Accuracy under this build minus accuracy under InternalCompromiseRun, matched record by record on identical traffic (percentage points).

| Vantage | R | Device effect [95% CI] | Submission effect [95% CI] | Matched rows |
|---|---|---|---|---|
| Passive observer | 1 | +0.04 [-0.05, +0.13] | -0.08 [-0.26, +0.10] | 39857 |
| Passive observer | 20 | +0.01 [-0.06, +0.08] | -0.12 [-0.27, +0.04] | 41728 |
| Passive observer | 100 | +0.01 [-0.01, +0.04] | +0.02 [-0.03, +0.07] | 207570 |
| First hop, credential | 1 | +0.03 [-0.08, +0.13] | -0.10 [-0.24, +0.06] | 159428 |
| First hop, credential | 20 | -0.08 [-0.15, -0.01] | -0.02 [-0.14, +0.10] | 166912 |
| First hop, credential | 100 | +0.01 [-0.01, +0.03] | +0.00 [-0.03, +0.04] | 830280 |
| First hop, content | 1 | +0.03 [-0.07, +0.13] | -0.10 [-0.24, +0.05] | 159428 |
| First hop, content | 20 | -0.08 [-0.15, -0.01] | -0.02 [-0.14, +0.10] | 166912 |
| First hop, content | 100 | +0.01 [-0.01, +0.04] | +0.00 [-0.03, +0.04] | 830280 |
| Credential processor | 1 | +0.06 [-0.02, +0.14] | +0.08 [-0.04, +0.22] | 159428 |
| Credential processor | 20 | -0.01 [-0.07, +0.04] | -0.04 [-0.15, +0.07] | 166912 |
| Credential processor | 100 | +0.02 [-0.01, +0.03] | +0.02 [-0.02, +0.06] | 830280 |
| Validator | 1 | -0.10 [-0.25, +0.04] | -0.06 [-0.31, +0.20] | 39857 |
| Validator | 20 | -0.09 [-0.20, +0.03] | +0.01 [-0.22, +0.26] | 41728 |
| Validator | 100 | +0.04 [+0.00, +0.08] | +0.02 [-0.06, +0.10] | 207570 |
| Gatekeeper | 1 | +0.05 [-0.03, +0.13] | -0.01 [-0.11, +0.09] | 119571 |
| Gatekeeper | 20 | -0.03 [-0.09, +0.03] | +0.02 [-0.07, +0.11] | 125184 |
| Gatekeeper | 100 | +0.02 [+0.00, +0.04] | +0.00 [-0.03, +0.04] | 622710 |
| Content server | 1 | -0.02 [-0.20, +0.17] | +0.06 [-0.14, +0.26] | 79714 |
| Content server | 20 | +0.07 [-0.09, +0.24] | -0.02 [-0.19, +0.17] | 83456 |
| Content server | 100 | -0.01 [-0.06, +0.05] | -0.00 [-0.06, +0.05] | 415140 |

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.95% [9.52%, 10.39%] | 2.03% | 9.95% | 0.00% [0.00%, 0.00%] | 4.42% [4.19%, 4.63%] | 1.64% | 4.42% | 0.00% [0.00%, 0.00%] | 0.581 [0.568, 0.593] | 26.3% | 18.0% | 0.000% | 200 | 39857 |
| 20 | 6.47% [6.15%, 6.78%] | 1.55% | 6.47% | 0.00% [0.00%, 0.00%] | 3.40% [3.22%, 3.58%] | 1.25% | 3.40% | 0.00% [0.00%, 0.00%] | 0.555 [0.541, 0.569] | 13.7% | 11.0% | 0.017% | 200 | 41728 |
| 100 | 3.49% [3.41%, 3.57%] | 0.77% | 3.49% | 0.00% [0.00%, 0.00%] | 1.76% [1.70%, 1.82%] | 0.62% | 1.76% | 0.00% [0.00%, 0.00%] | 0.551 [0.545, 0.558] | 6.5% | 5.4% | 0.000% | 200 | 207570 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.91% [9.48%, 10.31%] | 2.03% | 9.95% | -0.04% [-0.10%, 0.03%] | 4.51% [4.38%, 4.64%] | 1.64% | 4.42% | 0.09% [-0.01%, 0.19%] | 0.580 [0.569, 0.591] | 25.4% | 18.1% | 0.000% | 200 | 797140 |
| 20 | 6.45% [6.17%, 6.74%] | 1.55% | 6.47% | -0.02% [-0.07%, 0.03%] | 3.45% [3.35%, 3.54%] | 1.25% | 3.40% | 0.04% [-0.05%, 0.14%] | 0.556 [0.544, 0.569] | 14.4% | 10.8% | 0.020% | 200 | 834560 |
| 100 | 3.49% [3.41%, 3.56%] | 0.77% | 3.49% | -0.00% [-0.02%, 0.01%] | 1.72% [1.70%, 1.75%] | 0.62% | 1.76% | -0.03% [-0.08%, 0.01%] | 0.550 [0.544, 0.556] | 6.5% | 5.4% | 0.000% | 200 | 4151400 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.91% [9.53%, 10.31%] | 2.03% | 9.95% | -0.04% [-0.10%, 0.03%] | 4.51% [4.38%, 4.64%] | 1.64% | 4.42% | 0.09% [-0.01%, 0.19%] | 0.580 [0.569, 0.591] | 25.4% | 18.1% | 0.000% | 200 | 797140 |
| 20 | 6.45% [6.17%, 6.75%] | 1.55% | 6.47% | -0.02% [-0.07%, 0.03%] | 3.45% [3.35%, 3.54%] | 1.25% | 3.40% | 0.04% [-0.06%, 0.14%] | 0.556 [0.544, 0.569] | 14.4% | 10.8% | 0.020% | 200 | 834560 |
| 100 | 3.49% [3.41%, 3.56%] | 0.77% | 3.49% | -0.00% [-0.02%, 0.01%] | 1.72% [1.70%, 1.75%] | 0.62% | 1.76% | -0.03% [-0.08%, 0.01%] | 0.550 [0.544, 0.556] | 6.5% | 5.4% | 0.000% | 200 | 4151400 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.96% [9.54%, 10.37%] | 2.03% | 9.95% | 0.01% [-0.03%, 0.06%] | 4.58% [4.40%, 4.75%] | 1.64% | 4.42% | 0.16% [0.06%, 0.26%] | 0.581 [0.568, 0.593] | 25.8% | 17.9% | 0.000% | 200 | 677569 |
| 20 | 6.45% [6.13%, 6.76%] | 1.55% | 6.47% | -0.02% [-0.06%, 0.01%] | 3.41% [3.27%, 3.55%] | 1.25% | 3.40% | 0.01% [-0.07%, 0.09%] | 0.556 [0.543, 0.570] | 14.1% | 10.8% | 0.019% | 200 | 709376 |
| 100 | 3.49% [3.40%, 3.56%] | 0.77% | 3.49% | -0.00% [-0.01%, 0.00%] | 1.76% [1.71%, 1.81%] | 0.62% | 1.76% | -0.00% [-0.03%, 0.02%] | 0.552 [0.546, 0.559] | 6.5% | 5.4% | 0.000% | 200 | 3528690 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.42% [9.02%, 9.80%] | 1.83% | 9.95% | -0.53% [-0.90%, -0.19%] | 4.76% [4.58%, 4.98%] | 1.64% | 4.42% | 0.35% [0.07%, 0.62%] | 0.586 [0.572, 0.599] | 21.8% | 17.7% | 0.000% | 200 | 39857 |
| 20 | 6.23% [5.96%, 6.51%] | 1.40% | 6.47% | -0.24% [-0.51%, 0.04%] | 3.85% [3.67%, 4.04%] | 1.25% | 3.40% | 0.45% [0.19%, 0.71%] | 0.565 [0.551, 0.579] | 8.6% | 9.8% | 0.017% | 200 | 41728 |
| 100 | 3.45% [3.37%, 3.54%] | 0.70% | 3.49% | -0.04% [-0.13%, 0.05%] | 1.97% [1.92%, 2.03%] | 0.62% | 1.76% | 0.21% [0.12%, 0.31%] | 0.549 [0.542, 0.556] | 5.6% | 5.2% | 0.000% | 200 | 207570 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.00% [9.56%, 10.45%] | 2.03% | 9.95% | 0.05% [-0.05%, 0.14%] | 4.69% [4.52%, 4.85%] | 1.64% | 4.42% | 0.27% [0.08%, 0.46%] | 0.580 [0.568, 0.592] | 26.7% | 18.3% | 0.000% | 200 | 119571 |
| 20 | 6.42% [6.14%, 6.72%] | 1.55% | 6.47% | -0.05% [-0.13%, 0.03%] | 3.51% [3.38%, 3.63%] | 1.25% | 3.40% | 0.10% [-0.06%, 0.26%] | 0.558 [0.545, 0.571] | 13.7% | 10.8% | 0.018% | 200 | 125184 |
| 100 | 3.49% [3.41%, 3.56%] | 0.77% | 3.49% | -0.00% [-0.03%, 0.02%] | 1.75% [1.71%, 1.78%] | 0.62% | 1.76% | -0.01% [-0.06%, 0.05%] | 0.551 [0.544, 0.557] | 6.7% | 5.4% | 0.000% | 200 | 622710 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.82% [9.47%, 10.17%] | 2.18% | 9.95% | -0.13% [-0.38%, 0.12%] | 5.39% [5.23%, 5.56%] | 1.64% | 4.42% | 0.98% [0.73%, 1.22%] | 0.566 [0.556, 0.575] | 7.4% | 12.6% | 0.000% | 200 | 79714 |
| 20 | 6.68% [6.41%, 6.92%] | 1.66% | 6.47% | 0.20% [-0.01%, 0.42%] | 3.99% [3.86%, 4.13%] | 1.25% | 3.40% | 0.59% [0.37%, 0.80%] | 0.547 [0.537, 0.557] | 5.3% | 8.0% | 0.000% | 200 | 83456 |
| 100 | 3.71% [3.63%, 3.78%] | 0.83% | 3.49% | 0.22% [0.15%, 0.28%] | 2.00% [1.96%, 2.04%] | 0.62% | 1.76% | 0.24% [0.17%, 0.32%] | 0.530 [0.525, 0.535] | 2.0% | 3.4% | 0.000% | 200 | 415140 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

The rows cover every record; every record the node can select because it held a destination role; and the split by whether it held a first relay, which it cannot tell.

| R | Records | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | all records | 797,140 | 7971 | 9.89% | 9.95% | -0.06 [-0.15, +0.03] | 21.4% | 0.0000% | pass |
| 20 | all records | 834,560 | 8346 | 6.46% | 6.47% | -0.01 [-0.09, +0.06] | 12.5% | 0.0000% | pass |
| 100 | all records | 4,151,400 | 41514 | 3.50% | 3.49% | +0.01 [-0.01, +0.04] | 5.4% | 0.0000% | pass |
| 1 | every record the node can select | 119,571 | 1196 | 9.70% | 9.95% | -0.25 [-0.42, -0.06] | 12.1% | 0.0000% | pass |
| 1 | first relay held | 38,327 | 383 | 10.66% | 10.08% | +0.58 [+0.33, +0.82] | 25.0% | 0.0000% | pass |
| 1 | no first relay held | 758,813 | 7588 | 9.85% | 9.94% | -0.09 [-0.18, -0.00] | 21.4% | 0.0000% | pass |
| 20 | every record the node can select | 125,184 | 1252 | 6.56% | 6.47% | +0.09 [-0.07, +0.25] | 6.9% | 0.0000% | pass |
| 20 | first relay held | 39,970 | 400 | 7.03% | 6.35% | +0.68 [+0.46, +0.89] | 15.6% | 0.0000% | pass |
| 20 | no first relay held | 794,590 | 7946 | 6.43% | 6.48% | -0.05 [-0.12, +0.03] | 12.5% | 0.0000% | pass |
| 100 | every record the node can select | 622,710 | 6227 | 3.58% | 3.49% | +0.09 [+0.04, +0.14] | 3.0% | 0.0000% | pass |
| 100 | first relay held | 199,460 | 1995 | 3.90% | 3.47% | +0.44 [+0.37, +0.51] | 8.8% | 0.0000% | pass |
| 100 | no first relay held | 3,951,940 | 39519 | 3.48% | 3.49% | -0.01 [-0.03, +0.01] | 5.3% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there. Prevalence is the class's share of the node's decisions. Combined minus the sum is the combined lead minus the two single-role leads, paired on the same rows.

| R | Roles held | Prevalence | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined minus the sum [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 11.94% | 95,147 | 951 | 9.57% | 9.92% | -0.35 [-0.55, -0.15] | -0.11 [-0.19, -0.03] | -0.07 [-0.26, +0.11] | -0.17 [-0.27, -0.07] | 11.5% | 0.0000% | pass |
| 1 | credential first relay + content destination | 0.49% | 3,904 | 39 | 11.65% | 10.19% | +1.46 [+0.50, +2.44] | +0.20 [-0.31, +0.76] | -0.49 [-1.32, +0.32] | +1.74 [+1.01, +2.49] | 16.9% | 0.0000% | pass |
| 1 | content first relay + content destination | 0.53% | 4,247 | 42 | 10.67% | 9.89% | +0.78 [-0.12, +1.70] | +0.82 [+0.23, +1.39] | +0.12 [-0.70, +0.94] | -0.16 [-0.98, +0.64] | 27.8% | 0.0000% | pass |
| 1 | content first relay + credential destination | 0.53% | 4,216 | 42 | 10.46% | 10.27% | +0.19 [-0.33, +0.72] | +0.24 [-0.35, +0.78] | -0.05 [-0.21, +0.12] | +0.00 [-0.22, +0.22] | 30.6% | 0.0712% | pass |
| 1 | second relay + destination | 1.39% | 11,046 | 110 | 9.51% | 10.07% | -0.55 [-1.04, -0.06] | -0.31 [-0.53, -0.10] | -0.17 [-0.60, +0.27] | -0.07 [-0.35, +0.21] | 18.1% | 0.0000% | pass |
| 1 | three or more roles, with a destination | 0.13% | 1,011 | 10 | 9.30% | 9.20% | +0.10 [-1.28, +1.53] | +0.59 [-0.38, +1.48] | -0.20 [-1.59, +1.14] | -0.30 [-1.26, +0.72] | 27.8% | 0.0000% | pass |
| 20 | destination only | 11.93% | 99,523 | 995 | 6.43% | 6.47% | -0.04 [-0.21, +0.14] | -0.11 [-0.18, -0.04] | +0.11 [-0.05, +0.27] | -0.04 [-0.11, +0.03] | 6.8% | 0.0000% | pass |
| 20 | credential first relay + content destination | 0.50% | 4,137 | 41 | 7.98% | 6.82% | +1.16 [+0.35, +1.98] | +0.73 [+0.24, +1.22] | +0.12 [-0.70, +0.95] | +0.31 [-0.40, +0.99] | 16.1% | 0.0000% | pass |
| 20 | content first relay + content destination | 0.50% | 4,214 | 42 | 7.52% | 6.62% | +0.90 [-0.05, +1.82] | +0.21 [-0.33, +0.75] | +0.21 [-0.60, +1.02] | +0.47 [-0.29, +1.22] | 19.0% | 0.0712% | pass |
| 20 | content first relay + credential destination | 0.53% | 4,392 | 44 | 6.90% | 6.63% | +0.27 [-0.21, +0.75] | +0.23 [-0.24, +0.72] | +0.02 [-0.14, +0.18] | +0.02 [-0.16, +0.20] | 29.4% | 0.0000% | pass |
| 20 | second relay + destination | 1.42% | 11,831 | 118 | 6.67% | 6.37% | +0.30 [-0.10, +0.69] | +0.14 [-0.06, +0.34] | +0.40 [+0.01, +0.79] | -0.25 [-0.48, +0.00] | 11.7% | 0.0000% | pass |
| 20 | three or more roles, with a destination | 0.13% | 1,087 | 11 | 5.89% | 4.97% | +0.92 [-0.27, +2.09] | +0.09 [-0.74, +0.91] | +0.18 [-0.81, +1.18] | +0.64 [-0.46, +1.69] | 47.7% | 0.0000% | pass |
| 100 | destination only | 11.93% | 495,300 | 4953 | 3.52% | 3.49% | +0.03 [-0.02, +0.08] | -0.05 [-0.08, -0.03] | +0.15 [+0.10, +0.20] | -0.07 [-0.10, -0.04] | 2.5% | 0.0000% | pass |
| 100 | credential first relay + content destination | 0.50% | 20,742 | 207 | 4.47% | 3.41% | +1.06 [+0.75, +1.36] | +0.42 [+0.26, +0.58] | +0.18 [-0.09, +0.45] | +0.45 [+0.21, +0.70] | 11.6% | 0.0000% | pass |
| 100 | content first relay + content destination | 0.51% | 21,311 | 213 | 4.22% | 3.49% | +0.74 [+0.47, +1.01] | +0.22 [+0.07, +0.36] | +0.21 [-0.04, +0.46] | +0.31 [+0.10, +0.51] | 8.4% | 0.0000% | pass |
| 100 | content first relay + credential destination | 0.53% | 22,021 | 220 | 3.66% | 3.49% | +0.17 [+0.01, +0.34] | +0.24 [+0.08, +0.41] | -0.02 [-0.05, +0.01] | -0.05 [-0.10, +0.00] | 12.0% | 0.0000% | pass |
| 100 | second relay + destination | 1.40% | 57,951 | 580 | 3.48% | 3.50% | -0.02 [-0.15, +0.12] | -0.05 [-0.12, +0.02] | +0.11 [-0.02, +0.24] | -0.08 [-0.17, +0.01] | 4.4% | 0.0000% | pass |
| 100 | three or more roles, with a destination | 0.13% | 5,385 | 54 | 4.01% | 3.57% | +0.45 [-0.06, +0.94] | +0.20 [-0.06, +0.45] | +0.06 [-0.35, +0.45] | +0.19 [-0.13, +0.52] | 12.5% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 396,119 | 3961 | 9.79% | 9.95% | -0.16 [-0.23, -0.08] | 26.1% | 0.0000% | pass |
| 1 | one relay or gatekeeper role | 232,971 | 2330 | 10.08% | 9.95% | +0.13 [+0.02, +0.25] | 27.1% | 0.0000% | pass |
| 1 | second relay + first relay | 9,188 | 92 | 10.71% | 10.09% | +0.62 [+0.25, +0.99] | 28.8% | 0.0000% | pass |
| 1 | second relay + second relay | 4,104 | 41 | 9.67% | 9.94% | -0.27 [-0.68, +0.12] | 36.7% | 0.0244% | pass |
| 1 | gatekeeper + first relay | 16,772 | 168 | 10.45% | 10.05% | +0.40 [+0.11, +0.69] | 31.4% | 0.0537% | pass |
| 1 | gatekeeper + second relay | 15,137 | 151 | 9.86% | 9.92% | -0.06 [-0.30, +0.18] | 41.6% | 0.1387% | fail |
| 1 | three or more roles, no destination | 3,278 | 33 | 9.91% | 9.24% | +0.67 [+0.03, +1.34] | 44.2% | 0.0000% | pass |
| 20 | no role | 414,588 | 4146 | 6.36% | 6.46% | -0.10 [-0.15, -0.04] | 15.1% | 0.0186% | pass |
| 20 | one relay or gatekeeper role | 244,267 | 2443 | 6.52% | 6.51% | +0.02 [-0.07, +0.11] | 16.6% | 0.0242% | pass |
| 20 | second relay + first relay | 9,629 | 96 | 6.61% | 6.08% | +0.53 [+0.23, +0.82] | 24.2% | 0.0935% | pass |
| 20 | second relay + second relay | 4,285 | 43 | 6.30% | 6.21% | +0.09 [-0.23, +0.41] | 24.5% | 0.0000% | pass |
| 20 | gatekeeper + first relay | 17,598 | 176 | 6.95% | 6.25% | +0.70 [+0.42, +0.98] | 22.0% | 0.0000% | pass |
| 20 | gatekeeper + second relay | 15,591 | 156 | 6.52% | 6.71% | -0.19 [-0.41, +0.03] | 16.8% | 0.0000% | pass |
| 20 | three or more roles, no destination | 3,418 | 34 | 7.08% | 6.82% | +0.26 [-0.29, +0.81] | 26.6% | 0.0000% | pass |
| 100 | no role | 2,063,187 | 20632 | 3.43% | 3.49% | -0.06 [-0.08, -0.04] | 6.7% | 0.0000% | pass |
| 100 | one relay or gatekeeper role | 1,213,242 | 12132 | 3.55% | 3.48% | +0.06 [+0.04, +0.10] | 6.8% | 0.0000% | pass |
| 100 | second relay + first relay | 48,122 | 481 | 3.78% | 3.49% | +0.30 [+0.20, +0.39] | 9.7% | 0.0000% | pass |
| 100 | second relay + second relay | 21,507 | 215 | 3.59% | 3.70% | -0.10 [-0.21, +0.01] | 9.5% | 0.0000% | pass |
| 100 | gatekeeper + first relay | 87,264 | 873 | 3.82% | 3.46% | +0.36 [+0.28, +0.44] | 9.6% | 0.0000% | pass |
| 100 | gatekeeper + second relay | 78,203 | 782 | 3.51% | 3.56% | -0.05 [-0.12, +0.02] | 9.0% | 0.0000% | pass |
| 100 | three or more roles, no destination | 17,165 | 172 | 3.47% | 3.38% | +0.09 [-0.08, +0.26] | 13.2% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | -0.04 [-0.10, +0.03] | -0.04 [-0.12, +0.04] | -0.02 [-0.11, +0.06] |
| First hop, credential | 20 | -0.02 [-0.07, +0.03] | -0.08 [-0.15, -0.01] | +0.01 [-0.07, +0.09] |
| First hop, credential | 100 | -0.00 [-0.02, +0.01] | -0.01 [-0.04, +0.01] | -0.01 [-0.04, +0.01] |
| First hop, content | 1 | -0.04 [-0.10, +0.03] | -0.04 [-0.12, +0.05] | -0.02 [-0.10, +0.06] |
| First hop, content | 20 | -0.02 [-0.07, +0.03] | -0.08 [-0.15, -0.01] | +0.01 [-0.07, +0.09] |
| First hop, content | 100 | -0.00 [-0.02, +0.01] | -0.01 [-0.04, +0.01] | -0.01 [-0.03, +0.01] |
| Credential processor | 1 | +0.01 [-0.03, +0.06] | +0.02 [-0.03, +0.08] | +0.00 [-0.05, +0.05] |
| Credential processor | 20 | -0.02 [-0.06, +0.01] | -0.03 [-0.07, +0.01] | -0.01 [-0.04, +0.03] |
| Credential processor | 100 | -0.00 [-0.01, +0.00] | -0.00 [-0.01, +0.01] | -0.01 [-0.02, +0.00] |

## Paired against InternalCompromiseRun, records with no coincidence

Accuracy under this build minus accuracy under InternalCompromiseRun, matched record by record, on the records whose transaction has no node in roles on two different paths (percentage points).

| Vantage | R | Device effect [95% CI] | Matched rows |
|---|---|---|---|
| Passive observer | 1 | +0.10 [-0.07, +0.28] | 10492 |
| Passive observer | 20 | +0.06 [-0.10, +0.22] | 10817 |
| Passive observer | 100 | -0.04 [-0.08, +0.00] | 54269 |
| First hop, credential | 1 | +0.11 [-0.06, +0.30] | 41968 |
| First hop, credential | 20 | -0.02 [-0.18, +0.14] | 43268 |
| First hop, credential | 100 | -0.01 [-0.06, +0.04] | 217076 |
| First hop, content | 1 | +0.11 [-0.07, +0.29] | 41968 |
| First hop, content | 20 | -0.02 [-0.18, +0.14] | 43268 |
| First hop, content | 100 | -0.01 [-0.05, +0.04] | 217076 |
| Credential processor | 1 | +0.17 [+0.04, +0.31] | 41968 |
| Credential processor | 20 | +0.02 [-0.11, +0.14] | 43268 |
| Credential processor | 100 | -0.03 [-0.07, +0.01] | 217076 |
| Validator | 1 | -0.09 [-0.33, +0.14] | 10492 |
| Validator | 20 | +0.04 [-0.21, +0.28] | 10817 |
| Validator | 100 | +0.10 [+0.02, +0.17] | 54269 |
| Gatekeeper | 1 | +0.09 [-0.06, +0.24] | 31476 |
| Gatekeeper | 20 | -0.05 [-0.17, +0.07] | 32451 |
| Gatekeeper | 100 | +0.00 [-0.03, +0.04] | 162807 |
| Content server | 1 | +0.21 [-0.16, +0.54] | 20984 |
| Content server | 20 | +0.13 [-0.17, +0.43] | 21634 |
| Content server | 100 | +0.01 [-0.09, +0.11] | 108538 |

## Outcome-shuffle control

81 stable rows; 13 with a shuffled-outcome AUC interval excluding 0.5: R = 100 First hop, content (0.503), R = 100 Credential processor (0.502), R = 100 Validator (0.511), R = 100 Gatekeeper (0.504), R = 1 combined: destination only (0.493), R = 1 combined: content first relay + credential destination (0.531), R = 1 combined: three or more roles, with a destination (0.566), R = 20 combined: gatekeeper + second relay (0.520), R = 100 combined: no role (0.503), R = 100 first_hop_content (four nodes per run) (0.504), R = 100 cred_processor (four nodes per run) (0.507), R = 1 combined: no first relay held (0.503), R = 100 combined: no first relay held (0.502).

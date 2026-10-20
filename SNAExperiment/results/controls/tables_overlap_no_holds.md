# permitted overlap, every hold off

Build `overlap_no_holds`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1036.6 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 58.99% [57.01%, 61.17%] | 40.92% | 58.99% | 0.00% [0.00%, 0.00%] | 56.28% [54.11%, 58.36%] | 1.64% | 56.28% | 0.00% [0.00%, 0.00%] | 0.757 [0.744, 0.769] | 100.0% | 100.0% | 100.000% | 50 | 9963 |
| 20 | 50.71% [48.49%, 52.90%] | 33.57% | 50.71% | 0.00% [0.00%, 0.00%] | 48.17% [46.12%, 50.51%] | 1.25% | 48.17% | 0.00% [0.00%, 0.00%] | 0.733 [0.720, 0.746] | 100.0% | 100.0% | 100.000% | 50 | 10338 |
| 100 | 31.45% [29.63%, 33.36%] | 17.66% | 31.45% | 0.00% [0.00%, 0.00%] | 29.74% [27.85%, 31.67%] | 0.62% | 29.74% | 0.00% [0.00%, 0.00%] | 0.658 [0.650, 0.666] | 92.9% | 72.3% | 25.155% | 50 | 51930 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 58.97% [57.08%, 61.02%] | 40.92% | 58.99% | -0.02% [-0.03%, -0.01%] | 56.28% [54.28%, 58.32%] | 1.64% | 56.28% | 0.00% [-0.01%, 0.01%] | 0.757 [0.744, 0.769] | 100.0% | 100.0% | 100.000% | 50 | 199260 |
| 20 | 50.70% [48.61%, 52.93%] | 33.57% | 50.71% | -0.01% [-0.02%, -0.00%] | 48.17% [46.04%, 50.27%] | 1.25% | 48.17% | -0.00% [-0.01%, 0.01%] | 0.733 [0.720, 0.746] | 100.0% | 100.0% | 100.000% | 50 | 206760 |
| 100 | 31.44% [29.62%, 33.31%] | 17.66% | 31.45% | -0.01% [-0.01%, -0.00%] | 29.73% [27.87%, 31.72%] | 0.62% | 29.74% | -0.00% [-0.00%, -0.00%] | 0.658 [0.650, 0.666] | 92.9% | 72.3% | 25.156% | 50 | 1038600 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 58.97% [56.87%, 61.13%] | 40.92% | 58.99% | -0.02% [-0.03%, -0.01%] | 56.28% [54.30%, 58.37%] | 1.64% | 56.28% | 0.00% [-0.01%, 0.01%] | 0.757 [0.744, 0.769] | 100.0% | 100.0% | 100.000% | 50 | 199260 |
| 20 | 50.70% [48.54%, 52.91%] | 33.57% | 50.71% | -0.01% [-0.02%, -0.00%] | 48.17% [45.95%, 50.38%] | 1.25% | 48.17% | -0.00% [-0.01%, 0.01%] | 0.733 [0.720, 0.746] | 100.0% | 100.0% | 100.000% | 50 | 206760 |
| 100 | 31.44% [29.41%, 33.39%] | 17.66% | 31.45% | -0.01% [-0.01%, -0.00%] | 29.73% [27.89%, 31.62%] | 0.62% | 29.74% | -0.00% [-0.00%, -0.00%] | 0.658 [0.650, 0.666] | 92.9% | 72.3% | 25.156% | 50 | 1038600 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 58.99% [56.94%, 61.04%] | 40.92% | 58.99% | 0.00% [0.00%, 0.00%] | 56.28% [54.17%, 58.54%] | 1.64% | 56.28% | 0.00% [0.00%, 0.00%] | 0.757 [0.744, 0.769] | 100.0% | 100.0% | 100.000% | 50 | 169371 |
| 20 | 50.71% [48.61%, 52.88%] | 33.57% | 50.71% | 0.00% [0.00%, 0.00%] | 48.17% [46.11%, 50.52%] | 1.25% | 48.17% | 0.00% [0.00%, 0.00%] | 0.733 [0.720, 0.746] | 100.0% | 100.0% | 100.000% | 50 | 175746 |
| 100 | 31.45% [29.50%, 33.27%] | 17.66% | 31.45% | 0.00% [0.00%, 0.00%] | 29.74% [27.85%, 31.70%] | 0.62% | 29.74% | 0.00% [0.00%, 0.00%] | 0.658 [0.650, 0.666] | 92.9% | 72.3% | 25.157% | 50 | 882810 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 58.76% [56.75%, 60.76%] | 40.96% | 58.99% | -0.23% [-0.46%, 0.00%] | 56.23% [54.22%, 58.26%] | 1.64% | 56.28% | -0.05% [-0.29%, 0.17%] | 0.759 [0.746, 0.771] | 100.0% | 100.0% | 100.000% | 50 | 9963 |
| 20 | 50.48% [48.32%, 52.69%] | 33.60% | 50.71% | -0.22% [-0.50%, 0.04%] | 48.11% [46.06%, 50.41%] | 1.25% | 48.17% | -0.06% [-0.38%, 0.25%] | 0.734 [0.720, 0.747] | 100.0% | 100.0% | 100.000% | 50 | 10338 |
| 100 | 31.32% [29.39%, 33.34%] | 17.68% | 31.45% | -0.12% [-0.22%, -0.03%] | 29.68% [27.67%, 31.55%] | 0.62% | 29.74% | -0.05% [-0.17%, 0.06%] | 0.659 [0.652, 0.667] | 92.5% | 72.2% | 24.824% | 50 | 51930 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 58.71% [56.56%, 60.87%] | 40.92% | 58.99% | -0.28% [-0.86%, 0.25%] | 56.06% [54.01%, 58.17%] | 1.64% | 56.28% | -0.21% [-0.79%, 0.34%] | 0.768 [0.759, 0.776] | 100.0% | 100.0% | 100.000% | 50 | 29889 |
| 20 | 50.92% [48.88%, 53.10%] | 33.57% | 50.71% | 0.22% [-0.62%, 1.09%] | 48.68% [46.79%, 50.71%] | 1.25% | 48.17% | 0.51% [-0.32%, 1.33%] | 0.735 [0.726, 0.745] | 100.0% | 100.0% | 100.000% | 50 | 31014 |
| 100 | 32.22% [30.45%, 34.10%] | 17.66% | 31.45% | 0.78% [0.42%, 1.14%] | 30.71% [28.87%, 32.68%] | 0.62% | 29.74% | 0.98% [0.60%, 1.37%] | 0.663 [0.655, 0.670] | 95.1% | 73.9% | 27.538% | 50 | 155790 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 82.31% [81.01%, 83.69%] | 76.11% | 58.99% | 23.33% [21.07%, 25.53%] | 79.64% [78.29%, 81.11%] | 1.64% | 56.28% | 23.36% [21.30%, 25.61%] | 0.891 [0.885, 0.897] | 100.0% | 100.0% | 100.000% | 50 | 19926 |
| 20 | 77.74% [76.12%, 79.16%] | 70.42% | 50.71% | 27.03% [24.68%, 29.35%] | 74.85% [73.36%, 76.39%] | 1.25% | 48.17% | 26.67% [24.37%, 28.87%] | 0.868 [0.859, 0.877] | 100.0% | 100.0% | 100.000% | 50 | 20676 |
| 100 | 63.87% [62.00%, 65.85%] | 51.57% | 31.45% | 32.42% [29.92%, 34.78%] | 60.41% [58.63%, 62.31%] | 0.62% | 29.74% | 30.68% [28.26%, 33.07%] | 0.817 [0.807, 0.827] | 100.0% | 100.0% | 100.000% | 50 | 103860 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

| R | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| 1 | 199,260 | 1993 | 61.26% | 58.99% | +2.27 [+2.02, +2.48] | 100.0% | 100.0000% | fail |
| 20 | 206,760 | 2068 | 53.43% | 50.71% | +2.72 [+2.42, +3.02] | 100.0% | 100.0000% | fail |
| 100 | 1,038,600 | 10386 | 34.80% | 31.45% | +3.35 [+3.08, +3.62] | 100.0% | 42.1249% | fail |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there. Prevalence is the class's share of the node's decisions. Combined minus the sum is the combined lead minus the two single-role leads, paired on the same rows.

| R | Roles held | Prevalence | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined minus the sum [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 11.99% | 23,894 | 239 | 74.37% | 58.65% | +15.72 [+14.14, +17.18] | -0.02 [-0.04, -0.00] | +15.73 [+14.16, +17.24] | +0.01 [+0.00, +0.03] | 100.0% | 100.0000% | fail |
| 1 | credential first relay + content destination | 0.48% | 952 | 10 | 84.14% | 61.87% | +22.27 [+18.82, +25.86] | +0.00 [+0.00, +0.00] | +22.27 [+18.78, +25.78] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 1 | content first relay + content destination | 0.50% | 987 | 10 | 82.98% | 58.46% | +24.52 [+21.00, +28.31] | +0.00 [+0.00, +0.00] | +24.52 [+20.83, +28.25] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 1 | content first relay + credential destination | 0.52% | 1,028 | 10 | 60.70% | 60.70% | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 1 | second relay + destination | 1.39% | 2,762 | 28 | 74.44% | 60.07% | +14.37 [+12.67, +16.07] | +0.00 [+0.00, +0.00] | +14.37 [+12.81, +16.07] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 1 | three or more roles, with a destination | 0.13% | 266 | 3 | 77.44% | 63.16% | +14.29 [+10.08, +18.82] | +0.00 [+0.00, +0.00] | +14.29 [+10.07, +18.85] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 20 | destination only | 11.94% | 24,689 | 247 | 68.69% | 50.78% | +17.91 [+16.33, +19.41] | -0.02 [-0.05, -0.00] | +17.93 [+16.40, +19.40] | +0.01 [+0.00, +0.02] | 100.0% | 100.0000% | fail |
| 20 | credential first relay + content destination | 0.49% | 1,009 | 10 | 80.08% | 54.51% | +25.57 [+22.21, +28.73] | +0.10 [+0.00, +0.31] | +25.57 [+22.45, +28.77] | -0.10 [-0.31, +0.00] | 100.0% | 100.0000% | fail |
| 20 | content first relay + content destination | 0.50% | 1,030 | 10 | 76.60% | 49.51% | +27.09 [+23.03, +31.22] | +0.00 [+0.00, +0.00] | +27.09 [+22.92, +31.22] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 20 | content first relay + credential destination | 0.51% | 1,045 | 10 | 49.47% | 49.47% | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | 100.0% | 98.4689% | fail |
| 20 | second relay + destination | 1.43% | 2,955 | 30 | 69.37% | 50.08% | +19.29 [+17.16, +21.53] | +0.00 [+0.00, +0.00] | +19.29 [+17.15, +21.47] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 20 | three or more roles, with a destination | 0.14% | 286 | 3 | 66.08% | 46.50% | +19.58 [+14.50, +24.91] | +0.00 [+0.00, +0.00] | +19.58 [+14.46, +24.57] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 100 | destination only | 11.91% | 123,705 | 1237 | 53.14% | 31.44% | +21.70 [+19.96, +23.42] | -0.01 [-0.02, -0.00] | +21.71 [+20.10, +23.29] | +0.00 [-0.00, +0.00] | 100.0% | 100.0000% | fail |
| 100 | credential first relay + content destination | 0.49% | 5,103 | 51 | 62.79% | 30.59% | +32.20 [+29.54, +34.81] | +0.00 [+0.00, +0.00] | +32.18 [+29.59, +34.93] | +0.02 [+0.00, +0.06] | 100.0% | 100.0000% | fail |
| 100 | content first relay + content destination | 0.52% | 5,351 | 54 | 63.69% | 31.47% | +32.22 [+29.60, +34.75] | +0.06 [+0.00, +0.12] | +32.14 [+29.52, +34.67] | +0.02 [+0.00, +0.06] | 100.0% | 100.0000% | fail |
| 100 | content first relay + credential destination | 0.54% | 5,643 | 56 | 31.60% | 31.56% | +0.04 [+0.00, +0.09] | +0.04 [+0.00, +0.09] | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | 98.2% | 24.8627% | fail |
| 100 | second relay + destination | 1.41% | 14,605 | 146 | 53.31% | 31.76% | +21.55 [+19.78, +23.25] | -0.01 [-0.02, +0.00] | +21.55 [+19.82, +23.34] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 100 | three or more roles, with a destination | 0.13% | 1,383 | 14 | 53.51% | 31.02% | +22.49 [+19.70, +25.39] | +0.00 [+0.00, +0.00] | +22.49 [+19.68, +25.32] | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 98,915 | 989 | 59.07% | 59.10% | -0.03 [-0.04, -0.02] | 100.0% | 100.0000% | fail |
| 1 | one relay or gatekeeper role | 58,329 | 583 | 58.77% | 58.82% | -0.05 [-0.28, +0.17] | 100.0% | 100.0000% | fail |
| 1 | second relay + first relay | 2,302 | 23 | 58.64% | 58.64% | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 1 | second relay + second relay | 999 | 10 | 57.86% | 57.86% | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 1 | gatekeeper + first relay | 4,172 | 42 | 57.91% | 58.60% | -0.70 [-1.93, +0.58] | 100.0% | 100.0000% | fail |
| 1 | gatekeeper + second relay | 3,850 | 38 | 57.77% | 58.96% | -1.19 [-2.51, +0.21] | 100.0% | 100.0000% | fail |
| 1 | three or more roles, no destination | 804 | 8 | 62.94% | 62.31% | +0.62 [-1.41, +2.59] | 100.0% | 100.0000% | fail |
| 20 | no role | 102,583 | 1026 | 50.67% | 50.69% | -0.02 [-0.03, -0.01] | 100.0% | 100.0000% | fail |
| 20 | one relay or gatekeeper role | 60,727 | 607 | 50.74% | 50.76% | -0.02 [-0.36, +0.32] | 100.0% | 100.0000% | fail |
| 20 | second relay + first relay | 2,365 | 24 | 51.67% | 51.67% | +0.00 [+0.00, +0.00] | 100.0% | 100.0000% | fail |
| 20 | second relay + second relay | 1,000 | 10 | 49.70% | 49.70% | +0.00 [+0.00, +0.00] | 100.0% | 99.1000% | fail |
| 20 | gatekeeper + first relay | 4,341 | 43 | 50.93% | 49.46% | +1.47 [+0.14, +2.75] | 100.0% | 100.0000% | fail |
| 20 | gatekeeper + second relay | 3,917 | 39 | 50.83% | 50.70% | +0.13 [-1.12, +1.43] | 100.0% | 100.0000% | fail |
| 20 | three or more roles, no destination | 813 | 8 | 54.86% | 53.87% | +0.98 [-1.68, +3.64] | 100.0% | 100.0000% | fail |
| 100 | no role | 516,193 | 5162 | 31.43% | 31.44% | -0.01 [-0.02, -0.01] | 93.4% | 24.9258% | fail |
| 100 | one relay or gatekeeper role | 303,738 | 3037 | 31.71% | 31.44% | +0.27 [+0.13, +0.40] | 95.3% | 26.2512% | fail |
| 100 | second relay + first relay | 11,932 | 119 | 31.85% | 31.82% | +0.03 [+0.00, +0.05] | 94.1% | 25.0670% | fail |
| 100 | second relay + second relay | 5,288 | 53 | 31.24% | 31.26% | -0.02 [-0.06, +0.00] | 99.7% | 23.4304% | fail |
| 100 | gatekeeper + first relay | 21,690 | 217 | 32.14% | 31.43% | +0.71 [+0.11, +1.34] | 96.8% | 26.3762% | fail |
| 100 | gatekeeper + second relay | 19,670 | 197 | 32.57% | 31.50% | +1.07 [+0.31, +1.83] | 95.7% | 29.8475% | fail |
| 100 | three or more roles, no destination | 4,299 | 43 | 31.87% | 30.82% | +1.05 [-0.30, +2.34] | 96.3% | 25.9363% | fail |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | -0.02 [-0.03, -0.01] | -0.02 [-0.03, -0.01] | n/a |
| First hop, credential | 20 | -0.01 [-0.02, -0.00] | -0.01 [-0.03, -0.00] | n/a |
| First hop, credential | 100 | -0.01 [-0.01, -0.00] | -0.01 [-0.01, -0.00] | n/a |
| First hop, content | 1 | -0.02 [-0.03, -0.01] | -0.02 [-0.03, -0.01] | n/a |
| First hop, content | 20 | -0.01 [-0.02, -0.00] | -0.01 [-0.03, -0.00] | n/a |
| First hop, content | 100 | -0.01 [-0.01, -0.00] | -0.01 [-0.01, -0.00] | n/a |
| Credential processor | 1 | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | n/a |
| Credential processor | 20 | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | n/a |
| Credential processor | 100 | +0.00 [+0.00, +0.00] | +0.00 [+0.00, +0.00] | n/a |

## Outcome-shuffle control

72 stable rows; 9 with a shuffled-outcome AUC interval excluding 0.5: R = 100 Validator (0.490), R = 1 combined: content first relay + content destination (0.549), R = 1 combined: three or more roles, with a destination (0.588), R = 1 combined: gatekeeper + first relay (0.517), R = 1 combined: gatekeeper + second relay (0.523), R = 1 cred_processor (four nodes per run) (0.492), R = 20 combined: three or more roles, with a destination (0.590), R = 20 combined: second relay + second relay (0.545), R = 100 cred_processor (four nodes per run) (0.494).

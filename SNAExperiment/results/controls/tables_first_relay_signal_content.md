# permitted overlap, content paths dominate the record time

Build `first_relay_signal_content`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1036.6 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.49% [10.18%, 10.81%] | 2.80% | 10.49% | 0.00% [0.00%, 0.00%] | 6.18% [5.97%, 6.39%] | 1.64% | 6.18% | 0.00% [0.00%, 0.00%] | 0.585 [0.576, 0.594] | 22.8% | 18.7% | 0.000% | 300 | 59972 |
| 20 | 7.15% [6.71%, 7.59%] | 2.14% | 7.15% | 0.00% [0.00%, 0.00%] | 4.26% [3.99%, 4.52%] | 1.25% | 4.26% | 0.00% [0.00%, 0.00%] | 0.554 [0.536, 0.573] | 13.5% | 10.3% | 0.053% | 100 | 20700 |
| 100 | 3.96% [3.84%, 4.07%] | 1.06% | 3.96% | 0.00% [0.00%, 0.00%] | 2.17% [2.09%, 2.26%] | 0.62% | 2.17% | 0.00% [0.00%, 0.00%] | 0.556 [0.546, 0.566] | 7.5% | 6.2% | 0.000% | 100 | 103937 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.41% [10.12%, 10.70%] | 2.80% | 10.49% | -0.09% [-0.14%, -0.03%] | 6.20% [6.06%, 6.32%] | 1.64% | 6.18% | 0.02% [-0.06%, 0.10%] | 0.583 [0.575, 0.592] | 23.3% | 18.6% | 0.000% | 300 | 1199440 |
| 20 | 7.06% [6.64%, 7.45%] | 2.14% | 7.15% | -0.09% [-0.18%, -0.01%] | 4.47% [4.30%, 4.65%] | 1.25% | 4.26% | 0.22% [0.09%, 0.34%] | 0.556 [0.540, 0.572] | 13.3% | 10.2% | 0.050% | 100 | 414000 |
| 100 | 3.94% [3.83%, 4.04%] | 1.06% | 3.96% | -0.02% [-0.05%, 0.00%] | 2.30% [2.26%, 2.34%] | 0.62% | 2.17% | 0.13% [0.06%, 0.19%] | 0.556 [0.547, 0.564] | 7.4% | 6.2% | 0.000% | 100 | 2078740 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.41% [10.12%, 10.69%] | 2.80% | 10.49% | -0.09% [-0.14%, -0.03%] | 6.20% [6.06%, 6.32%] | 1.64% | 6.18% | 0.02% [-0.07%, 0.10%] | 0.583 [0.575, 0.592] | 23.3% | 18.6% | 0.000% | 300 | 1199440 |
| 20 | 7.06% [6.65%, 7.46%] | 2.14% | 7.15% | -0.09% [-0.18%, -0.02%] | 4.47% [4.30%, 4.65%] | 1.25% | 4.26% | 0.22% [0.09%, 0.34%] | 0.556 [0.540, 0.572] | 13.3% | 10.2% | 0.050% | 100 | 414000 |
| 100 | 3.94% [3.83%, 4.04%] | 1.06% | 3.96% | -0.02% [-0.05%, 0.00%] | 2.30% [2.26%, 2.34%] | 0.62% | 2.17% | 0.13% [0.07%, 0.18%] | 0.556 [0.547, 0.564] | 7.4% | 6.2% | 0.000% | 100 | 2078740 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.48% [10.19%, 10.79%] | 2.80% | 10.49% | -0.01% [-0.04%, 0.02%] | 6.13% [5.96%, 6.30%] | 1.64% | 6.18% | -0.05% [-0.11%, 0.02%] | 0.584 [0.575, 0.593] | 23.1% | 18.7% | 0.000% | 300 | 1019524 |
| 20 | 7.10% [6.67%, 7.55%] | 2.14% | 7.15% | -0.05% [-0.10%, -0.00%] | 4.32% [4.07%, 4.55%] | 1.25% | 4.26% | 0.06% [-0.04%, 0.15%] | 0.556 [0.538, 0.574] | 13.6% | 10.3% | 0.057% | 100 | 351900 |
| 100 | 3.96% [3.85%, 4.07%] | 1.06% | 3.96% | 0.00% [-0.01%, 0.01%] | 2.18% [2.10%, 2.26%] | 0.62% | 2.17% | 0.01% [-0.03%, 0.04%] | 0.555 [0.546, 0.565] | 7.5% | 6.2% | 0.000% | 100 | 1766929 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.33% [10.05%, 10.62%] | 2.27% | 10.49% | -0.17% [-0.51%, 0.16%] | 6.88% [6.67%, 7.08%] | 1.64% | 6.18% | 0.70% [0.42%, 1.02%] | 0.574 [0.567, 0.582] | 20.2% | 16.5% | 0.000% | 300 | 59972 |
| 20 | 7.59% [7.21%, 7.95%] | 1.73% | 7.15% | 0.44% [-0.03%, 0.90%] | 5.68% [5.33%, 6.04%] | 1.25% | 4.26% | 1.43% [0.94%, 1.92%] | 0.565 [0.549, 0.581] | 15.5% | 13.2% | 0.043% | 100 | 20700 |
| 100 | 4.26% [4.12%, 4.42%] | 0.86% | 3.96% | 0.30% [0.13%, 0.49%] | 3.34% [3.19%, 3.52%] | 0.62% | 2.17% | 1.17% [0.98%, 1.36%] | 0.545 [0.536, 0.554] | 8.6% | 6.3% | 0.000% | 100 | 103937 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.43% [10.11%, 10.75%] | 2.80% | 10.49% | -0.07% [-0.16%, 0.02%] | 6.10% [5.93%, 6.26%] | 1.64% | 6.18% | -0.08% [-0.25%, 0.09%] | 0.585 [0.576, 0.593] | 24.3% | 18.6% | 0.000% | 300 | 179916 |
| 20 | 7.00% [6.58%, 7.41%] | 2.14% | 7.15% | -0.15% [-0.30%, -0.01%] | 4.39% [4.19%, 4.60%] | 1.25% | 4.26% | 0.13% [-0.07%, 0.34%] | 0.556 [0.538, 0.574] | 13.0% | 9.6% | 0.050% | 100 | 62100 |
| 100 | 3.97% [3.86%, 4.08%] | 1.06% | 3.96% | 0.01% [-0.03%, 0.05%] | 2.22% [2.15%, 2.28%] | 0.62% | 2.17% | 0.04% [-0.03%, 0.12%] | 0.553 [0.544, 0.562] | 7.5% | 6.3% | 0.000% | 100 | 311811 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.05% [9.78%, 10.32%] | 2.83% | 10.49% | -0.44% [-0.63%, -0.25%] | 6.31% [6.17%, 6.45%] | 1.64% | 6.18% | 0.13% [-0.10%, 0.37%] | 0.557 [0.549, 0.565] | 9.3% | 13.2% | 0.000% | 300 | 119944 |
| 20 | 7.13% [6.72%, 7.53%] | 2.16% | 7.15% | -0.02% [-0.32%, 0.29%] | 4.80% [4.58%, 5.01%] | 1.25% | 4.26% | 0.54% [0.19%, 0.87%] | 0.538 [0.523, 0.553] | 7.2% | 8.8% | 0.000% | 100 | 41400 |
| 100 | 3.96% [3.85%, 4.07%] | 1.08% | 3.96% | 0.00% [-0.08%, 0.09%] | 2.38% [2.30%, 2.44%] | 0.62% | 2.17% | 0.20% [0.09%, 0.32%] | 0.526 [0.518, 0.534] | 2.7% | 3.9% | 0.000% | 100 | 207874 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

| R | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| 1 | 1,199,440 | 11994 | 10.34% | 10.49% | -0.15 [-0.23, -0.08] | 21.7% | 0.0000% | pass |
| 20 | 414,000 | 4140 | 7.02% | 7.15% | -0.13 [-0.24, -0.01] | 12.9% | 0.0000% | pass |
| 100 | 2,078,740 | 20787 | 3.93% | 3.96% | -0.03 [-0.06, +0.01] | 6.3% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there. Prevalence is the class's share of the node's decisions. Combined minus the sum is the combined lead minus the two single-role leads, paired on the same rows.

| R | Roles held | Prevalence | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined minus the sum [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 11.93% | 143,125 | 1431 | 9.72% | 10.50% | -0.78 [-0.93, -0.62] | -0.48 [-0.56, -0.40] | -0.27 [-0.41, -0.13] | -0.03 [-0.12, +0.06] | 11.4% | 0.0000% | pass |
| 1 | credential first relay + content destination | 0.49% | 5,873 | 59 | 11.03% | 10.40% | +0.63 [-0.27, +1.46] | +1.41 [+0.86, +1.99] | -0.78 [-1.53, +0.00] | +0.00 [-0.71, +0.72] | 22.5% | 0.0000% | pass |
| 1 | content first relay + content destination | 0.52% | 6,268 | 63 | 11.44% | 10.34% | +1.10 [+0.24, +1.95] | +1.71 [+1.11, +2.31] | -0.75 [-1.47, -0.05] | +0.14 [-0.60, +0.90] | 26.8% | 0.0000% | pass |
| 1 | content first relay + credential destination | 0.53% | 6,333 | 63 | 12.90% | 10.83% | +2.07 [+1.49, +2.67] | +2.24 [+1.65, +2.86] | -0.03 [-0.24, +0.16] | -0.14 [-0.41, +0.13] | 37.3% | 0.2369% | fail |
| 1 | second relay + destination | 1.40% | 16,753 | 168 | 9.79% | 10.51% | -0.72 [-1.09, -0.35] | -0.43 [-0.63, -0.22] | -0.30 [-0.67, +0.07] | +0.01 [-0.25, +0.25] | 18.4% | 0.0000% | pass |
| 1 | three or more roles, with a destination | 0.13% | 1,564 | 16 | 11.32% | 9.27% | +2.05 [+0.68, +3.51] | +2.37 [+1.23, +3.53] | +0.45 [-0.73, +1.57] | -0.77 [-1.89, +0.33] | 43.0% | 0.0000% | pass |
| 20 | destination only | 11.96% | 49,505 | 495 | 6.78% | 7.12% | -0.34 [-0.59, -0.11] | -0.38 [-0.49, -0.27] | -0.03 [-0.26, +0.21] | +0.07 [-0.05, +0.19] | 9.4% | 0.0000% | pass |
| 20 | credential first relay + content destination | 0.49% | 2,039 | 20 | 8.97% | 8.24% | +0.74 [-0.54, +1.96] | +0.59 [-0.34, +1.44] | -0.20 [-1.20, +0.84] | +0.34 [-0.78, +1.46] | 41.6% | 0.0000% | pass |
| 20 | content first relay + content destination | 0.50% | 2,057 | 21 | 9.63% | 7.49% | +2.14 [+0.66, +3.56] | +1.75 [+0.84, +2.68] | -0.19 [-1.21, +0.80] | +0.58 [-0.49, +1.67] | 34.6% | 0.0000% | pass |
| 20 | content first relay + credential destination | 0.51% | 2,117 | 21 | 9.26% | 7.18% | +2.08 [+1.31, +2.84] | +2.22 [+1.42, +3.04] | +0.09 [-0.14, +0.33] | -0.24 [-0.58, +0.09] | 34.6% | 0.0000% | pass |
| 20 | second relay + destination | 1.41% | 5,831 | 58 | 6.79% | 7.03% | -0.24 [-0.76, +0.30] | -0.46 [-0.80, -0.15] | +0.22 [-0.26, +0.69] | +0.00 [-0.38, +0.38] | 18.6% | 0.0000% | pass |
| 20 | three or more roles, with a destination | 0.13% | 551 | 6 | unstable: 125 runs needed | | | | | | | | |
| 100 | destination only | 11.93% | 247,893 | 2479 | 3.74% | 3.97% | -0.22 [-0.29, -0.16] | -0.19 [-0.23, -0.15] | +0.01 [-0.05, +0.07] | -0.04 [-0.08, -0.00] | 2.8% | 0.0000% | pass |
| 100 | credential first relay + content destination | 0.49% | 10,252 | 103 | 4.85% | 3.81% | +1.03 [+0.64, +1.44] | +0.69 [+0.44, +0.95] | -0.11 [-0.45, +0.24] | +0.45 [+0.11, +0.81] | 13.4% | 0.0000% | pass |
| 100 | content first relay + content destination | 0.51% | 10,692 | 107 | 5.25% | 3.82% | +1.43 [+0.96, +1.88] | +0.82 [+0.53, +1.11] | +0.06 [-0.32, +0.43] | +0.55 [+0.19, +0.95] | 6.6% | 0.0000% | pass |
| 100 | content first relay + credential destination | 0.53% | 11,064 | 111 | 4.80% | 4.05% | +0.75 [+0.46, +1.03] | +0.79 [+0.51, +1.06] | +0.05 [-0.02, +0.13] | -0.09 [-0.19, +0.01] | 19.0% | 0.0000% | pass |
| 100 | second relay + destination | 1.41% | 29,235 | 292 | 3.69% | 3.92% | -0.23 [-0.42, -0.06] | -0.18 [-0.30, -0.07] | -0.09 [-0.26, +0.08] | +0.04 [-0.07, +0.17] | 5.8% | 0.0000% | pass |
| 100 | three or more roles, with a destination | 0.13% | 2,675 | 27 | 4.93% | 4.26% | +0.67 [-0.00, +1.38] | +0.56 [-0.04, +1.14] | +0.00 [-0.52, +0.52] | +0.11 [-0.44, +0.67] | 28.1% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 596,015 | 5960 | 9.95% | 10.48% | -0.53 [-0.59, -0.47] | 23.9% | 0.0000% | pass |
| 1 | one relay or gatekeeper role | 350,709 | 3507 | 10.93% | 10.53% | +0.40 [+0.30, +0.50] | 25.9% | 0.0000% | pass |
| 1 | second relay + first relay | 13,868 | 139 | 12.98% | 10.25% | +2.73 [+2.31, +3.16] | 37.5% | 0.0000% | pass |
| 1 | second relay + second relay | 6,209 | 62 | 10.23% | 10.66% | -0.43 [-0.82, -0.10] | 36.2% | 0.1772% | fail |
| 1 | gatekeeper + first relay | 25,201 | 252 | 12.68% | 10.54% | +2.13 [+1.84, +2.44] | 38.1% | 0.0000% | pass |
| 1 | gatekeeper + second relay | 22,551 | 226 | 10.04% | 10.50% | -0.46 [-0.70, -0.20] | 25.6% | 0.0310% | pass |
| 1 | three or more roles, no destination | 4,971 | 50 | 11.18% | 9.98% | +1.21 [+0.57, +1.85] | 41.7% | 0.0000% | pass |
| 20 | no role | 205,592 | 2056 | 6.71% | 7.13% | -0.41 [-0.51, -0.32] | 14.1% | 0.0540% | pass |
| 20 | one relay or gatekeeper role | 121,243 | 1212 | 7.42% | 7.22% | +0.20 [+0.06, +0.34] | 16.1% | 0.0503% | pass |
| 20 | second relay + first relay | 4,756 | 48 | 8.26% | 6.79% | +1.47 [+0.88, +2.05] | 24.7% | 0.0000% | pass |
| 20 | second relay + second relay | 2,045 | 20 | 6.60% | 7.38% | -0.78 [-1.26, -0.34] | 51.9% | 0.3423% | fail |
| 20 | gatekeeper + first relay | 8,723 | 87 | 8.78% | 7.04% | +1.74 [+1.25, +2.21] | 22.6% | 0.0000% | pass |
| 20 | gatekeeper + second relay | 7,799 | 78 | 6.37% | 7.21% | -0.83 [-1.23, -0.46] | 15.8% | 0.0128% | pass |
| 20 | three or more roles, no destination | 1,742 | 17 | 6.66% | 6.14% | +0.52 [-0.28, +1.38] | 41.0% | 0.2870% | fail |
| 100 | no role | 1,033,176 | 10332 | 3.82% | 3.97% | -0.15 [-0.18, -0.12] | 7.6% | 0.0000% | pass |
| 100 | one relay or gatekeeper role | 607,527 | 6075 | 4.08% | 3.93% | +0.15 [+0.11, +0.20] | 8.4% | 0.0000% | pass |
| 100 | second relay + first relay | 24,038 | 240 | 4.58% | 3.83% | +0.75 [+0.54, +0.95] | 13.0% | 0.0000% | pass |
| 100 | second relay + second relay | 10,687 | 107 | 3.91% | 4.03% | -0.12 [-0.29, +0.06] | 16.4% | 0.0000% | pass |
| 100 | gatekeeper + first relay | 43,592 | 436 | 4.70% | 4.03% | +0.67 [+0.53, +0.80] | 11.2% | 0.0000% | pass |
| 100 | gatekeeper + second relay | 39,263 | 393 | 3.73% | 4.02% | -0.30 [-0.41, -0.18] | 11.0% | 0.0000% | pass |
| 100 | three or more roles, no destination | 8,646 | 86 | 4.37% | 4.45% | -0.08 [-0.39, +0.23] | 12.9% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | -0.09 [-0.14, -0.03] | -0.16 [-0.23, -0.08] | n/a |
| First hop, credential | 20 | -0.09 [-0.18, -0.01] | -0.05 [-0.16, +0.07] | n/a |
| First hop, credential | 100 | -0.02 [-0.05, +0.00] | -0.03 [-0.06, +0.01] | n/a |
| First hop, content | 1 | -0.09 [-0.14, -0.03] | -0.16 [-0.24, -0.08] | n/a |
| First hop, content | 20 | -0.09 [-0.18, -0.02] | -0.05 [-0.15, +0.06] | n/a |
| First hop, content | 100 | -0.02 [-0.05, +0.00] | -0.03 [-0.06, +0.01] | n/a |
| Credential processor | 1 | -0.01 [-0.04, +0.02] | +0.01 [-0.03, +0.06] | n/a |
| Credential processor | 20 | -0.05 [-0.10, -0.00] | -0.03 [-0.08, +0.03] | n/a |
| Credential processor | 100 | +0.00 [-0.01, +0.01] | +0.00 [-0.01, +0.01] | n/a |

## Outcome-shuffle control

71 stable rows; 5 with a shuffled-outcome AUC interval excluding 0.5: R = 1 Credential processor (0.503), R = 1 combined: gatekeeper + second relay (0.486), R = 20 combined: all records (0.506), R = 20 combined: no role (0.507), R = 20 cred_processor (four nodes per run) (0.510).

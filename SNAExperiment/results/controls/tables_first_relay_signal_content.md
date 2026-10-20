# permitted overlap, content paths dominate the record time

Build `first_relay_signal_content`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1036.6 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.47% [9.65%, 11.31%] | 2.79% | 10.47% | 0.00% [0.00%, 0.00%] | 6.43% [5.77%, 7.07%] | 1.64% | 6.43% | 0.00% [0.00%, 0.00%] | 0.588 [0.562, 0.615] | 17.2% | 16.8% | 0.000% | 43 | 8684 |
| 20 | 7.05% [6.41%, 7.75%] | 2.13% | 7.05% | 0.00% [0.00%, 0.00%] | 4.27% [3.81%, 4.70%] | 1.25% | 4.27% | 0.00% [0.00%, 0.00%] | 0.553 [0.522, 0.584] | 8.0% | 9.5% | 0.000% | 42 | 8803 |
| 100 | 3.95% [3.79%, 4.12%] | 1.06% | 3.95% | 0.00% [0.00%, 0.00%] | 2.24% [2.12%, 2.35%] | 0.62% | 2.24% | 0.00% [0.00%, 0.00%] | 0.561 [0.545, 0.578] | 7.4% | 6.9% | 0.000% | 44 | 45691 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.41% [9.65%, 11.17%] | 2.79% | 10.47% | -0.06% [-0.19%, 0.07%] | 6.32% [5.92%, 6.75%] | 1.64% | 6.43% | -0.10% [-0.40%, 0.18%] | 0.587 [0.563, 0.611] | 16.2% | 16.7% | 0.000% | 43 | 173680 |
| 20 | 6.99% [6.42%, 7.62%] | 2.13% | 7.05% | -0.07% [-0.19%, 0.06%] | 4.50% [4.23%, 4.78%] | 1.25% | 4.27% | 0.23% [0.04%, 0.43%] | 0.554 [0.527, 0.581] | 8.7% | 9.0% | 0.000% | 42 | 176060 |
| 100 | 3.96% [3.81%, 4.11%] | 1.06% | 3.95% | 0.00% [-0.04%, 0.04%] | 2.32% [2.27%, 2.37%] | 0.62% | 2.24% | 0.08% [-0.00%, 0.16%] | 0.560 [0.546, 0.574] | 7.6% | 6.8% | 0.000% | 44 | 913820 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.41% [9.61%, 11.21%] | 2.79% | 10.47% | -0.06% [-0.18%, 0.06%] | 6.32% [5.91%, 6.75%] | 1.64% | 6.43% | -0.10% [-0.39%, 0.18%] | 0.587 [0.563, 0.611] | 16.2% | 16.7% | 0.000% | 43 | 173680 |
| 20 | 6.99% [6.39%, 7.61%] | 2.13% | 7.05% | -0.07% [-0.20%, 0.06%] | 4.50% [4.23%, 4.78%] | 1.25% | 4.27% | 0.23% [0.02%, 0.44%] | 0.554 [0.527, 0.581] | 8.7% | 9.0% | 0.000% | 42 | 176060 |
| 100 | 3.96% [3.82%, 4.11%] | 1.06% | 3.95% | 0.00% [-0.03%, 0.04%] | 2.32% [2.27%, 2.38%] | 0.62% | 2.24% | 0.08% [-0.00%, 0.16%] | 0.560 [0.546, 0.574] | 7.6% | 6.8% | 0.000% | 44 | 913820 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.40% [9.61%, 11.20%] | 2.79% | 10.47% | -0.07% [-0.16%, 0.01%] | 6.30% [5.75%, 6.87%] | 1.64% | 6.43% | -0.13% [-0.31%, 0.04%] | 0.588 [0.562, 0.614] | 16.9% | 16.6% | 0.000% | 43 | 147628 |
| 20 | 7.05% [6.43%, 7.72%] | 2.13% | 7.05% | -0.01% [-0.09%, 0.07%] | 4.29% [3.89%, 4.67%] | 1.25% | 4.27% | 0.02% [-0.12%, 0.16%] | 0.554 [0.524, 0.584] | 7.7% | 9.4% | 0.000% | 42 | 149651 |
| 100 | 3.96% [3.79%, 4.13%] | 1.06% | 3.95% | 0.00% [-0.02%, 0.02%] | 2.25% [2.14%, 2.35%] | 0.62% | 2.24% | 0.01% [-0.04%, 0.05%] | 0.559 [0.543, 0.575] | 7.4% | 6.9% | 0.000% | 44 | 776747 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.80% [9.95%, 11.61%] | 2.27% | 10.47% | 0.33% [-0.39%, 1.17%] | 7.05% [6.40%, 7.74%] | 1.64% | 6.43% | 0.62% [-0.23%, 1.48%] | 0.578 [0.559, 0.598] | 28.7% | 17.3% | 0.127% | 43 | 8684 |
| 20 | 7.40% [6.85%, 7.94%] | 1.73% | 7.05% | 0.34% [-0.36%, 1.00%] | 5.52% [4.97%, 6.04%] | 1.25% | 4.27% | 1.25% [0.48%, 2.03%] | 0.556 [0.530, 0.582] | 14.8% | 13.2% | 0.000% | 42 | 8803 |
| 100 | 4.40% [4.16%, 4.64%] | 0.86% | 3.95% | 0.45% [0.17%, 0.71%] | 3.30% [3.08%, 3.53%] | 0.62% | 2.24% | 1.06% [0.80%, 1.32%] | 0.540 [0.527, 0.552] | 8.5% | 6.6% | 0.002% | 44 | 45691 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.31% [9.48%, 11.13%] | 2.79% | 10.47% | -0.16% [-0.36%, 0.05%] | 6.33% [5.93%, 6.76%] | 1.64% | 6.43% | -0.10% [-0.52%, 0.32%] | 0.585 [0.561, 0.610] | 16.5% | 15.9% | 0.000% | 43 | 26052 |
| 20 | 7.01% [6.41%, 7.62%] | 2.13% | 7.05% | -0.05% [-0.24%, 0.13%] | 4.39% [4.05%, 4.74%] | 1.25% | 4.27% | 0.12% [-0.26%, 0.48%] | 0.553 [0.522, 0.584] | 6.4% | 9.3% | 0.000% | 42 | 26409 |
| 100 | 4.01% [3.85%, 4.17%] | 1.06% | 3.95% | 0.05% [-0.02%, 0.13%] | 2.30% [2.20%, 2.40%] | 0.62% | 2.24% | 0.06% [-0.05%, 0.18%] | 0.556 [0.541, 0.571] | 7.4% | 6.8% | 0.000% | 44 | 137073 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.98% [9.31%, 10.64%] | 2.83% | 10.47% | -0.49% [-0.98%, 0.01%] | 5.91% [5.54%, 6.28%] | 1.64% | 6.43% | -0.52% [-1.16%, 0.11%] | 0.565 [0.539, 0.590] | 8.6% | 13.0% | 0.000% | 43 | 17368 |
| 20 | 7.15% [6.52%, 7.77%] | 2.16% | 7.05% | 0.09% [-0.40%, 0.61%] | 4.78% [4.42%, 5.12%] | 1.25% | 4.27% | 0.51% [-0.03%, 1.04%] | 0.533 [0.509, 0.557] | 5.7% | 7.5% | 0.000% | 42 | 17606 |
| 100 | 4.07% [3.90%, 4.23%] | 1.08% | 3.95% | 0.11% [-0.03%, 0.25%] | 2.38% [2.27%, 2.48%] | 0.62% | 2.24% | 0.13% [-0.02%, 0.29%] | 0.528 [0.517, 0.540] | 3.2% | 4.5% | 0.000% | 44 | 91382 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

| R | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| 1 | 173,680 | 1737 | 10.32% | 10.47% | -0.15 [-0.33, +0.03] | 17.1% | 0.0000% | pass |
| 20 | 176,060 | 1761 | 6.99% | 7.05% | -0.06 [-0.24, +0.12] | 8.9% | 0.0000% | pass |
| 100 | 913,820 | 9138 | 3.96% | 3.95% | +0.01 [-0.04, +0.06] | 6.5% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined above the sum | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 20,656 | 207 | 9.68% | 10.59% | -0.91 [-1.30, -0.51] | -0.41 [-0.60, -0.22] | -0.30 [-0.66, +0.07] | no | 22.1% | 0.0000% | pass |
| 1 | credential first relay + content destination | 851 | 9 | 10.34% | 10.69% | -0.35 [-2.48, +1.84] | +0.71 [-0.69, +2.14] | -1.41 [-3.48, +0.59] | yes | 43.5% | 0.0000% | pass |
| 1 | content first relay + content destination | 927 | 9 | 11.97% | 9.28% | +2.70 [+0.89, +4.50] | +2.16 [+0.34, +4.00] | +0.32 [-1.43, +2.22] | yes | 29.9% | 0.0000% | pass |
| 1 | content first relay + credential destination | 947 | 9 | 12.04% | 10.67% | +1.37 [-0.58, +3.15] | +1.80 [-0.11, +3.76] | -0.11 [-0.64, +0.43] | no | 29.9% | 0.0000% | pass |
| 1 | second relay + destination | 2,447 | 24 | 9.56% | 9.93% | -0.37 [-1.09, +0.36] | -0.45 [-1.07, +0.16] | -0.33 [-1.07, +0.48] | yes | 20.2% | 0.0000% | pass |
| 1 | three or more roles, with a destination | 224 | 2 | unstable: 120 runs needed | | | | | | | | |
| 20 | destination only | 21,104 | 211 | 6.90% | 6.99% | -0.09 [-0.46, +0.26] | -0.23 [-0.39, -0.07] | +0.11 [-0.24, +0.48] | yes | 8.5% | 0.0000% | pass |
| 20 | credential first relay + content destination | 869 | 9 | 9.78% | 8.86% | +0.92 [-1.54, +3.33] | +0.58 [-0.81, +1.88] | -0.69 [-2.69, +1.21] | yes | 54.7% | 0.0000% | fail |
| 20 | content first relay + content destination | 872 | 9 | 9.17% | 6.54% | +2.64 [+0.34, +4.71] | +0.92 [-0.59, +2.43] | +0.11 [-1.34, +1.53] | yes | 43.5% | 0.0000% | pass |
| 20 | content first relay + credential destination | 907 | 9 | 9.26% | 7.50% | +1.76 [+0.70, +2.91] | +1.87 [+0.77, +3.00] | +0.11 [+0.00, +0.34] | no | 43.5% | 0.0000% | pass |
| 20 | second relay + destination | 2,434 | 24 | 6.49% | 7.07% | -0.58 [-1.46, +0.24] | -0.53 [-1.07, +0.00] | +0.08 [-0.74, +0.86] | no | 20.2% | 0.0000% | pass |
| 20 | three or more roles, with a destination | 223 | 2 | unstable: 132 runs needed | | | | | | | | |
| 100 | destination only | 109,064 | 1091 | 3.80% | 3.95% | -0.15 [-0.25, -0.06] | -0.16 [-0.22, -0.11] | +0.11 [+0.02, +0.20] | no | 3.7% | 0.0000% | pass |
| 100 | credential first relay + content destination | 4,523 | 45 | 5.22% | 3.74% | +1.48 [+0.81, +2.17] | +0.84 [+0.41, +1.26] | +0.11 [-0.42, +0.65] | yes | 23.5% | 0.0000% | pass |
| 100 | content first relay + content destination | 4,687 | 47 | 5.06% | 3.46% | +1.60 [+1.00, +2.20] | +1.02 [+0.59, +1.45] | +0.02 [-0.47, +0.52] | yes | 14.2% | 0.0000% | pass |
| 100 | content first relay + credential destination | 4,761 | 48 | 5.19% | 4.45% | +0.74 [+0.33, +1.19] | +0.74 [+0.33, +1.15] | +0.11 [-0.02, +0.22] | no | 24.7% | 0.0000% | pass |
| 100 | second relay + destination | 12,889 | 129 | 3.66% | 4.02% | -0.36 [-0.65, -0.06] | -0.26 [-0.45, -0.09] | -0.13 [-0.39, +0.11] | yes | 7.7% | 0.0000% | pass |
| 100 | three or more roles, with a destination | 1,149 | 11 | 4.61% | 4.35% | +0.26 [-0.77, +1.27] | +0.17 [-0.52, +0.91] | +0.09 [-0.82, +0.96] | no | 47.7% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 86,404 | 864 | 9.87% | 10.44% | -0.57 [-0.72, -0.42] | 19.3% | 0.0000% | pass |
| 1 | one relay or gatekeeper role | 50,652 | 507 | 10.96% | 10.47% | +0.48 [+0.25, +0.72] | 20.1% | 0.0000% | pass |
| 1 | second relay + first relay | 2,025 | 20 | 14.07% | 11.11% | +2.96 [+2.05, +3.91] | 41.6% | 0.1481% | fail |
| 1 | second relay + second relay | 898 | 9 | 10.02% | 9.69% | +0.33 [-0.56, +1.10] | 43.5% | 0.0000% | pass |
| 1 | gatekeeper + first relay | 3,647 | 36 | 12.78% | 10.80% | +1.97 [+1.35, +2.61] | 25.3% | 0.0274% | pass |
| 1 | gatekeeper + second relay | 3,279 | 33 | 10.77% | 10.67% | +0.09 [-0.62, +0.84] | 23.6% | 0.0000% | pass |
| 1 | three or more roles, no destination | 723 | 7 | 10.93% | 9.54% | +1.38 [-0.54, +3.22] | 64.1% | 0.0000% | fail |
| 20 | no role | 87,511 | 875 | 6.68% | 7.01% | -0.33 [-0.47, -0.19] | 9.9% | 0.0000% | pass |
| 20 | one relay or gatekeeper role | 51,389 | 514 | 7.37% | 7.18% | +0.18 [-0.02, +0.41] | 12.8% | 0.0000% | pass |
| 20 | second relay + first relay | 2,043 | 20 | 7.59% | 6.61% | +0.98 [+0.10, +1.91] | 30.1% | 0.0000% | pass |
| 20 | second relay + second relay | 887 | 9 | 6.54% | 6.99% | -0.45 [-0.97, +0.00] | 29.9% | 0.0000% | pass |
| 20 | gatekeeper + first relay | 3,718 | 37 | 8.85% | 6.91% | +1.94 [+1.24, +2.63] | 24.7% | 0.0000% | pass |
| 20 | gatekeeper + second relay | 3,312 | 33 | 6.40% | 7.22% | -0.82 [-1.44, -0.21] | 10.4% | 0.0000% | pass |
| 20 | three or more roles, no destination | 791 | 8 | unstable: 53 runs needed | | | | | |
| 100 | no role | 454,289 | 4543 | 3.86% | 3.97% | -0.11 [-0.15, -0.07] | 7.9% | 0.0000% | pass |
| 100 | one relay or gatekeeper role | 266,791 | 2668 | 4.07% | 3.91% | +0.16 [+0.09, +0.24] | 8.9% | 0.0000% | pass |
| 100 | second relay + first relay | 10,621 | 106 | 4.95% | 4.11% | +0.84 [+0.52, +1.13] | 19.9% | 0.0000% | pass |
| 100 | second relay + second relay | 4,760 | 48 | 3.63% | 3.72% | -0.08 [-0.34, +0.19] | 24.7% | 0.0000% | pass |
| 100 | gatekeeper + first relay | 19,186 | 192 | 4.74% | 4.05% | +0.69 [+0.50, +0.90] | 13.1% | 0.0000% | pass |
| 100 | gatekeeper + second relay | 17,257 | 173 | 3.63% | 3.85% | -0.22 [-0.40, -0.05] | 13.8% | 0.0000% | pass |
| 100 | three or more roles, no destination | 3,843 | 38 | 4.71% | 4.84% | -0.13 [-0.57, +0.31] | 20.8% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | -0.06 [-0.19, +0.07] | -0.08 [-0.27, +0.12] | n/a |
| First hop, credential | 20 | -0.07 [-0.19, +0.06] | -0.02 [-0.16, +0.14] | n/a |
| First hop, credential | 100 | +0.00 [-0.04, +0.04] | -0.00 [-0.06, +0.05] | n/a |
| First hop, content | 1 | -0.06 [-0.18, +0.06] | -0.08 [-0.29, +0.11] | n/a |
| First hop, content | 20 | -0.07 [-0.20, +0.06] | -0.02 [-0.16, +0.13] | n/a |
| First hop, content | 100 | +0.00 [-0.03, +0.04] | -0.00 [-0.06, +0.05] | n/a |
| Credential processor | 1 | -0.07 [-0.16, +0.01] | -0.07 [-0.18, +0.03] | n/a |
| Credential processor | 20 | -0.01 [-0.09, +0.07] | +0.03 [-0.06, +0.11] | n/a |
| Credential processor | 100 | +0.00 [-0.02, +0.02] | -0.00 [-0.03, +0.02] | n/a |

## Outcome-shuffle control

69 stable rows; 6 with a shuffled-outcome AUC interval excluding 0.5: R = 1 First hop, content (0.507), R = 20 Credential processor (0.509), R = 20 Content server (0.519), R = 100 First hop, credential (0.505), R = 100 Validator (0.516), R = 20 combined: no role (0.509).

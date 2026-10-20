# permitted overlap, credential path dominates the record time

Build `first_relay_signal_cred`. Record-to-device linking with 60 decoy transactions in flight; end-to-end delay D = 1036.6 s. Per-decision attack; intervals are 95% and resample whole runs. Device level (primary): the named device is the record's. Submission level: the named submission group contains a packet of the record's capture. Rows are real records only. The first hops and the credential processor are scored on every record.

## Every cell

### Passive observer

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.47% [9.88%, 11.04%] | 2.24% | 10.47% | 0.00% [0.00%, 0.00%] | 4.92% [4.63%, 5.21%] | 1.64% | 4.92% | 0.00% [0.00%, 0.00%] | 0.581 [0.565, 0.596] | 24.5% | 18.3% | 0.000% | 100 | 19959 |
| 20 | 6.94% [6.54%, 7.34%] | 1.72% | 6.94% | 0.00% [0.00%, 0.00%] | 3.59% [3.29%, 3.89%] | 1.25% | 3.59% | 0.00% [0.00%, 0.00%] | 0.564 [0.546, 0.581] | 13.5% | 9.2% | 0.014% | 100 | 20700 |
| 100 | 3.86% [3.74%, 3.97%] | 0.85% | 3.86% | 0.00% [0.00%, 0.00%] | 1.83% [1.76%, 1.91%] | 0.62% | 1.83% | 0.00% [0.00%, 0.00%] | 0.545 [0.536, 0.554] | 5.2% | 5.2% | 0.000% | 100 | 103937 |

### First hop, credential

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.41% [9.81%, 10.96%] | 2.24% | 10.47% | -0.06% [-0.14%, 0.03%] | 4.95% [4.78%, 5.11%] | 1.64% | 4.92% | 0.03% [-0.10%, 0.17%] | 0.581 [0.567, 0.595] | 24.6% | 18.6% | 0.000% | 100 | 399180 |
| 20 | 6.90% [6.54%, 7.26%] | 1.72% | 6.94% | -0.05% [-0.12%, 0.03%] | 3.65% [3.49%, 3.81%] | 1.25% | 3.59% | 0.06% [-0.08%, 0.22%] | 0.564 [0.547, 0.580] | 13.5% | 9.1% | 0.019% | 100 | 414000 |
| 100 | 3.83% [3.71%, 3.93%] | 0.85% | 3.86% | -0.03% [-0.06%, -0.00%] | 1.85% [1.82%, 1.89%] | 0.62% | 1.83% | 0.02% [-0.03%, 0.07%] | 0.546 [0.537, 0.554] | 5.5% | 5.3% | 0.000% | 100 | 2078740 |

### First hop, content

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.41% [9.87%, 10.98%] | 2.24% | 10.47% | -0.06% [-0.14%, 0.03%] | 4.95% [4.77%, 5.12%] | 1.64% | 4.92% | 0.03% [-0.11%, 0.17%] | 0.581 [0.567, 0.595] | 24.6% | 18.6% | 0.000% | 100 | 399180 |
| 20 | 6.90% [6.52%, 7.28%] | 1.72% | 6.94% | -0.05% [-0.12%, 0.03%] | 3.65% [3.49%, 3.82%] | 1.25% | 3.59% | 0.06% [-0.08%, 0.21%] | 0.564 [0.547, 0.580] | 13.5% | 9.1% | 0.019% | 100 | 414000 |
| 100 | 3.83% [3.71%, 3.94%] | 0.85% | 3.86% | -0.03% [-0.06%, -0.00%] | 1.85% [1.82%, 1.89%] | 0.62% | 1.83% | 0.02% [-0.03%, 0.07%] | 0.546 [0.537, 0.554] | 5.5% | 5.3% | 0.000% | 100 | 2078740 |

### Credential processor

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.44% [9.87%, 11.02%] | 2.24% | 10.47% | -0.03% [-0.08%, 0.03%] | 4.93% [4.68%, 5.16%] | 1.64% | 4.92% | 0.01% [-0.07%, 0.10%] | 0.581 [0.566, 0.596] | 23.9% | 18.3% | 0.000% | 100 | 339303 |
| 20 | 6.89% [6.50%, 7.30%] | 1.72% | 6.94% | -0.05% [-0.09%, -0.01%] | 3.57% [3.35%, 3.80%] | 1.25% | 3.59% | -0.02% [-0.11%, 0.07%] | 0.563 [0.546, 0.580] | 13.4% | 9.2% | 0.020% | 100 | 351900 |
| 100 | 3.84% [3.73%, 3.96%] | 0.85% | 3.86% | -0.01% [-0.03%, 0.01%] | 1.82% [1.76%, 1.88%] | 0.62% | 1.83% | -0.01% [-0.05%, 0.02%] | 0.546 [0.537, 0.555] | 5.3% | 5.3% | 0.000% | 100 | 1766929 |

### Validator

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 44.02% [42.75%, 45.31%] | 3.53% | 10.47% | 33.55% [32.12%, 34.97%] | 42.23% [40.97%, 43.53%] | 1.64% | 4.92% | 37.32% [36.01%, 38.71%] | 0.672 [0.664, 0.680] | 84.5% | 78.4% | 73.997% | 100 | 19959 |
| 20 | 37.57% [36.49%, 38.69%] | 2.70% | 6.94% | 30.63% [29.54%, 31.77%] | 36.35% [35.26%, 37.50%] | 1.25% | 3.59% | 32.76% [31.66%, 33.90%] | 0.660 [0.652, 0.667] | 78.3% | 69.3% | 43.309% | 100 | 20700 |
| 100 | 23.04% [22.12%, 23.94%] | 1.34% | 3.86% | 19.18% [18.22%, 20.13%] | 22.08% [21.18%, 23.01%] | 0.62% | 1.83% | 20.25% [19.33%, 21.17%] | 0.608 [0.604, 0.613] | 49.5% | 42.2% | 0.707% | 100 | 103937 |

### Gatekeeper

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.06% [9.49%, 10.67%] | 2.24% | 10.47% | -0.40% [-0.64%, -0.18%] | 4.89% [4.67%, 5.11%] | 1.64% | 4.92% | -0.03% [-0.31%, 0.23%] | 0.582 [0.570, 0.595] | 27.7% | 19.1% | 0.008% | 100 | 59877 |
| 20 | 6.67% [6.31%, 6.99%] | 1.72% | 6.94% | -0.28% [-0.45%, -0.10%] | 3.58% [3.41%, 3.74%] | 1.25% | 3.59% | -0.01% [-0.28%, 0.27%] | 0.571 [0.556, 0.586] | 12.4% | 9.6% | 0.021% | 100 | 62100 |
| 100 | 3.70% [3.59%, 3.80%] | 0.85% | 3.86% | -0.16% [-0.23%, -0.09%] | 1.77% [1.72%, 1.82%] | 0.62% | 1.83% | -0.07% [-0.15%, 0.01%] | 0.551 [0.542, 0.559] | 5.8% | 5.4% | 0.000% | 100 | 311811 |

### Content server

| R | Device accuracy [95% CI] | Chance, feasible set | Observer | Lead over observer [95% CI] | Submission accuracy [95% CI] | 1/T | Observer | Lead over observer [95% CI] | AUC [95% CI] | Top 1% right | Top 5% right | Coverage above 50% | Runs | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.83% [10.40%, 11.25%] | 2.88% | 10.47% | 0.36% [-0.05%, 0.78%] | 6.69% [6.46%, 6.92%] | 1.64% | 4.92% | 1.77% [1.40%, 2.14%] | 0.551 [0.539, 0.562] | 7.8% | 12.4% | 0.000% | 100 | 39918 |
| 20 | 7.60% [7.26%, 7.95%] | 2.20% | 6.94% | 0.65% [0.35%, 0.97%] | 5.04% [4.82%, 5.27%] | 1.25% | 3.59% | 1.45% [1.12%, 1.80%] | 0.546 [0.533, 0.558] | 7.5% | 8.8% | 0.000% | 100 | 41400 |
| 100 | 4.36% [4.25%, 4.47%] | 1.09% | 3.86% | 0.50% [0.40%, 0.61%] | 2.68% [2.61%, 2.76%] | 0.62% | 1.83% | 0.85% [0.74%, 0.96%] | 0.524 [0.517, 0.531] | 2.5% | 3.9% | 0.000% | 100 | 207874 |

## Combined view of one node

One compromised node scores every record with all the evidence its roles give it, combined as likelihood ratios against the passive observer. Leads are over the passive observer on the same records, in points. The claim columns are the upper bound of the 95% interval on the precision of the most confident 1% of matches, the share of matches in a most-confident group right more than half the time, and the verdict. A row that misses the stability rule (at least 50 right and 50 wrong device-level decisions) shows only the runs it needs.

### Every record

| R | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| 1 | 399,180 | 3992 | 10.38% | 10.47% | -0.09 [-0.22, +0.04] | 16.7% | 0.0000% | pass |
| 20 | 414,000 | 4140 | 6.87% | 6.94% | -0.07 [-0.18, +0.03] | 11.5% | 0.0000% | pass |
| 100 | 2,078,740 | 20787 | 3.84% | 3.86% | -0.01 [-0.05, +0.02] | 5.1% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Identifiable classes

A class is identifiable when the node held a destination role (C, F or I) in the record's transaction, so it can select those records by the plaintext hash it reads there.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Combined lead [95% CI] | First relay alone [95% CI] | Destination alone [95% CI] | Combined above the sum | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | destination only | 47,726 | 477 | 10.29% | 10.48% | -0.18 [-0.51, +0.16] | -0.19 [-0.32, -0.08] | +0.17 [-0.15, +0.50] | no | 12.4% | 0.0000% | pass |
| 1 | credential first relay + content destination | 1,945 | 19 | 15.78% | 11.00% | +4.78 [+3.15, +6.42] | +1.23 [+0.46, +2.00] | +0.46 [-1.20, +2.12] | yes | 31.4% | 0.0000% | pass |
| 1 | content first relay + content destination | 2,071 | 21 | 11.97% | 10.53% | +1.45 [+0.05, +3.02] | +0.14 [-0.86, +1.17] | +0.10 [-1.27, +1.35] | yes | 28.9% | 0.0000% | pass |
| 1 | content first relay + credential destination | 2,104 | 21 | 11.17% | 11.26% | -0.10 [-0.93, +0.73] | +0.29 [-0.42, +1.05] | -0.29 [-0.87, +0.34] | no | 40.0% | 0.0000% | pass |
| 1 | second relay + destination | 5,514 | 55 | 10.12% | 9.83% | +0.29 [-0.57, +1.11] | -0.04 [-0.36, +0.28] | +0.69 [-0.15, +1.53] | no | 21.8% | 0.0000% | pass |
| 1 | three or more roles, with a destination | 517 | 5 | 12.77% | 10.83% | +1.93 [-1.25, +4.87] | -0.19 [-1.72, +1.29] | -0.19 [-2.62, +2.24] | yes | 43.4% | 0.0000% | pass |
| 20 | destination only | 49,505 | 495 | 7.05% | 6.95% | +0.09 [-0.17, +0.34] | -0.20 [-0.31, -0.09] | +0.43 [+0.18, +0.66] | no | 10.8% | 0.0000% | pass |
| 20 | credential first relay + content destination | 2,039 | 20 | 9.51% | 6.96% | +2.55 [+1.16, +3.91] | +1.86 [+1.00, +2.72] | +0.64 [-0.65, +1.95] | yes | 41.6% | 0.0000% | pass |
| 20 | content first relay + content destination | 2,057 | 21 | 9.09% | 7.39% | +1.70 [+0.43, +2.98] | -0.10 [-0.83, +0.62] | -0.24 [-1.41, +0.91] | yes | 34.6% | 0.0000% | pass |
| 20 | content first relay + credential destination | 2,117 | 21 | 7.09% | 7.27% | -0.19 [-0.77, +0.38] | +0.33 [-0.23, +0.95] | -0.43 [-0.98, +0.09] | no | 40.0% | 0.0000% | pass |
| 20 | second relay + destination | 5,831 | 58 | 6.71% | 6.60% | +0.10 [-0.49, +0.66] | -0.27 [-0.52, -0.03] | +0.43 [-0.10, +1.00] | no | 6.2% | 0.0000% | pass |
| 20 | three or more roles, with a destination | 551 | 6 | 9.07% | 6.35% | +2.72 [+0.18, +5.20] | +0.18 [-1.11, +1.55] | +0.91 [-0.74, +2.48] | yes | 70.0% | 0.0000% | fail |
| 100 | destination only | 247,893 | 2479 | 3.95% | 3.86% | +0.10 [+0.01, +0.18] | -0.11 [-0.15, -0.07] | +0.32 [+0.23, +0.41] | no | 2.4% | 0.0000% | pass |
| 100 | credential first relay + content destination | 10,252 | 103 | 5.91% | 3.75% | +2.17 [+1.68, +2.65] | +0.61 [+0.35, +0.88] | +0.34 [-0.08, +0.75] | yes | 9.6% | 0.0000% | pass |
| 100 | content first relay + content destination | 10,692 | 107 | 5.25% | 3.91% | +1.34 [+0.88, +1.80] | +0.15 [-0.06, +0.35] | +0.70 [+0.28, +1.13] | yes | 12.9% | 0.0000% | pass |
| 100 | content first relay + credential destination | 11,064 | 111 | 4.01% | 3.81% | +0.21 [-0.05, +0.46] | +0.17 [-0.08, +0.41] | -0.01 [-0.12, +0.11] | yes | 10.1% | 0.0000% | pass |
| 100 | second relay + destination | 29,235 | 292 | 4.13% | 3.87% | +0.26 [+0.05, +0.49] | -0.15 [-0.25, -0.04] | +0.49 [+0.28, +0.70] | no | 5.3% | 0.0000% | pass |
| 100 | three or more roles, with a destination | 2,675 | 27 | 4.86% | 4.19% | +0.67 [-0.15, +1.49] | +0.04 [-0.38, +0.45] | +0.15 [-0.67, +1.01] | yes | 18.3% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

### Oracle-conditioned classes

A class is oracle-conditioned when the node held only relay or gatekeeper roles, or none, in the record's transaction: it cannot select those records, so the row is a single-role lead on a subset the node cannot pick, not an attack.

| R | Roles held | Decisions | Top 1% group | Device named | Observer | Lead [95% CI] | Top 1% upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|
| 1 | no role | 198,360 | 1984 | 10.21% | 10.47% | -0.26 [-0.35, -0.17] | 26.1% | 0.0000% | pass |
| 1 | one relay or gatekeeper role | 116,616 | 1166 | 10.47% | 10.44% | +0.03 [-0.15, +0.21] | 27.5% | 0.0043% | pass |
| 1 | second relay + first relay | 4,622 | 46 | 11.94% | 10.80% | +1.15 [+0.59, +1.73] | 30.7% | 0.1082% | fail |
| 1 | second relay + second relay | 2,035 | 20 | 10.71% | 10.17% | +0.54 [+0.05, +1.08] | 65.8% | 0.0000% | fail |
| 1 | gatekeeper + first relay | 8,370 | 84 | 10.88% | 10.31% | +0.57 [+0.05, +1.14] | 48.8% | 0.1792% | fail |
| 1 | gatekeeper + second relay | 7,645 | 76 | 9.74% | 10.61% | -0.86 [-1.39, -0.34] | 38.6% | 0.1439% | fail |
| 1 | three or more roles, no destination | 1,655 | 17 | 12.21% | 10.82% | +1.39 [+0.19, +2.58] | 53.1% | 0.0000% | fail |
| 20 | no role | 205,592 | 2056 | 6.73% | 6.93% | -0.20 [-0.28, -0.11] | 15.2% | 0.0199% | pass |
| 20 | one relay or gatekeeper role | 121,243 | 1212 | 6.89% | 6.99% | -0.10 [-0.23, +0.04] | 14.6% | 0.0223% | pass |
| 20 | second relay + first relay | 4,756 | 48 | 7.23% | 6.35% | +0.88 [+0.44, +1.37] | 27.2% | 0.1051% | fail |
| 20 | second relay + second relay | 2,045 | 20 | 6.94% | 7.14% | -0.20 [-0.65, +0.24] | 23.6% | 0.0489% | pass |
| 20 | gatekeeper + first relay | 8,723 | 87 | 7.41% | 6.81% | +0.60 [+0.20, +1.02] | 18.5% | 0.0000% | pass |
| 20 | gatekeeper + second relay | 7,799 | 78 | 7.04% | 7.10% | -0.06 [-0.45, +0.32] | 25.0% | 0.0128% | pass |
| 20 | three or more roles, no destination | 1,742 | 17 | 6.49% | 6.95% | -0.46 [-1.45, +0.48] | 53.1% | 0.0574% | fail |
| 100 | no role | 1,033,176 | 10332 | 3.73% | 3.86% | -0.12 [-0.16, -0.09] | 5.9% | 0.0000% | pass |
| 100 | one relay or gatekeeper role | 607,527 | 6075 | 3.88% | 3.86% | +0.03 [-0.02, +0.08] | 5.9% | 0.0000% | pass |
| 100 | second relay + first relay | 24,038 | 240 | 4.40% | 3.87% | +0.53 [+0.36, +0.71] | 9.0% | 0.0042% | pass |
| 100 | second relay + second relay | 10,687 | 107 | 3.24% | 3.37% | -0.13 [-0.32, +0.04] | 11.7% | 0.0000% | pass |
| 100 | gatekeeper + first relay | 43,592 | 436 | 4.15% | 3.85% | +0.30 [+0.14, +0.46] | 9.4% | 0.0000% | pass |
| 100 | gatekeeper + second relay | 39,263 | 393 | 3.60% | 3.94% | -0.34 [-0.49, -0.19] | 10.4% | 0.0025% | pass |
| 100 | three or more roles, no destination | 8,646 | 86 | 3.89% | 3.93% | -0.05 [-0.41, +0.32] | 15.9% | 0.0000% | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Rotation of the compromised node

The first hops and the credential processor are scored with every eligible node compromised in every run. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises. Leads over the passive observer, in points [95% CI].

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | -0.06 [-0.14, +0.03] | -0.11 [-0.24, +0.00] | n/a |
| First hop, credential | 20 | -0.05 [-0.12, +0.03] | -0.03 [-0.13, +0.06] | n/a |
| First hop, credential | 100 | -0.03 [-0.06, -0.00] | -0.03 [-0.06, +0.01] | n/a |
| First hop, content | 1 | -0.06 [-0.14, +0.03] | -0.11 [-0.23, +0.01] | n/a |
| First hop, content | 20 | -0.05 [-0.12, +0.03] | -0.03 [-0.13, +0.06] | n/a |
| First hop, content | 100 | -0.03 [-0.06, -0.00] | -0.03 [-0.07, +0.01] | n/a |
| Credential processor | 1 | -0.03 [-0.08, +0.03] | -0.01 [-0.09, +0.07] | n/a |
| Credential processor | 20 | -0.05 [-0.09, -0.01] | -0.07 [-0.12, -0.01] | n/a |
| Credential processor | 100 | -0.01 [-0.03, +0.01] | -0.02 [-0.04, +0.01] | n/a |

## Outcome-shuffle control

72 stable rows; 6 with a shuffled-outcome AUC interval excluding 0.5: R = 1 First hop, credential (0.504), R = 1 Credential processor (0.504), R = 20 First hop, credential (0.506), R = 20 Gatekeeper (0.514), R = 100 Credential processor (0.504), R = 20 first_hop_content (four nodes per run) (0.509).

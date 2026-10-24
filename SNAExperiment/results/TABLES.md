# Tables

Main run: D = 1170.1 s; rates are R / D and 60 / D. Intervals are 95% and resample whole runs. Device named: the vantage names the device behind a registry record. Chance, feasible set: a uniform guess among the devices whose packets could have produced the record. A row with fewer than 50 right or 50 wrong device-level decisions is unstable and shows no estimate.

## In flight

| Configuration | Cell | Real in flight (target) | Decoys in flight (target) | Runs |
|---|---|---|---|---|
| Main run | R1_D60 | 0.99 (1) | 59.85 (60) | 200 |
| Main run | R20_D60 | 19.76 (20) | 59.52 (60) | 200 |
| Main run | R100_D60 | 98.98 (100) | 59.49 (60) | 200 |
| Every hold off | R1_D60 | 0.99 (1) | 59.68 (60) | 50 |
| Every hold off | R20_D60 | 19.29 (20) | 58.54 (60) | 50 |
| Every hold off | R100_D60 | 99.70 (100) | 60.27 (60) | 50 |
| Credential path sets the record time | R1_D60 | 1.00 (1) | 60.19 (60) | 100 |
| Credential path sets the record time | R20_D60 | 19.94 (20) | 59.73 (60) | 100 |
| Credential path sets the record time | R100_D60 | 100.12 (100) | 60.05 (60) | 100 |
| Content paths set the record time | R1_D60 | 0.99 (1) | 59.87 (60) | 100 |
| Content paths set the record time | R20_D60 | 19.72 (20) | 59.65 (60) | 100 |
| Content paths set the record time | R100_D60 | 99.68 (100) | 59.78 (60) | 100 |
| F content path sets the record time | R1_D60 | 0.99 (1) | 60.12 (60) | 100 |
| F content path sets the record time | R20_D60 | 19.94 (20) | 59.89 (60) | 100 |
| F content path sets the record time | R100_D60 | 100.22 (100) | 60.24 (60) | 100 |

## Timing (main run, R = 20)

| Stage | Mean | Std dev | Maximum |
|---|---|---|---|
| device, credential channel | 121.0 s | 103.6 s | 360.0 s |
| device, content channels | 240.3 s | 206.3 s | 720.0 s |
| first relay hops (A, D, G) | 60.4 s | 51.3 s | 180.0 s |
| second relay hops (B, E, H) | 300.2 s | 258.8 s | 900.0 s |
| C before CV-1 | 30.0 s | 25.3 s | 90.0 s |
| V before CV-2 | 30.0 s | 25.3 s | 90.0 s |
| C fan-out, per leg | 45.2 s | 31.0 s | 179.7 s |
| gatekeeper hold | 30.1 s | 25.3 s | 90.0 s |
| departure bundling wait | 101.5 s | 91.2 s | 360.0 s |
| F/I pre-match hold | 119.7 s | 102.8 s | 360.0 s |
| post-match lottery | 30.1 s | 25.3 s | 90.0 s |
| registry bundle wait | 59.8 s | 34.7 s | 120.0 s |
| registry posting wait | 59.9 s | 34.2 s | 119.4 s |
| capture to finalization | 1164.1 s | 299.9 s | 2330.1 s |

| Cell | Mean capture to finalization [95% CI] |
|---|---|
| R1_D60 | 1164.2 s [1158.2, 1169.7] |
| R20_D60 | 1164.1 s [1158.5, 1170.0] |
| R100_D60 | 1161.7 s [1156.9, 1166.8] |

## R1_D60: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 7.28% [6.86%, 7.71%] | 1.80% | ×4.04 [3.81, 4.28] | reference | 39,879 | 12.0% | 0.000% | pass |
| First hop, credential | 7.28% [6.87%, 7.70%] | 1.80% | ×4.04 [3.81, 4.27] | +0.00 [-0.03, +0.03] | 797,580 | 9.3% | 0.000% | pass |
| First hop, content | 7.28% [6.85%, 7.69%] | 1.80% | ×4.04 [3.80, 4.27] | +0.00 [-0.03, +0.03] | 797,580 | 9.3% | 0.000% | pass |
| Credential processor | 7.28% [6.88%, 7.71%] | 1.80% | ×4.04 [3.82, 4.28] | -0.00 [-0.03, +0.03] | 677,943 | 9.4% | 0.000% | pass |
| Validator | 7.82% [7.45%, 8.20%] | 1.93% | ×4.05 [3.86, 4.25] | +0.54 [+0.21, +0.89] | 39,879 | 16.1% | 0.000% | pass |
| Gatekeeper | 7.33% [6.90%, 7.78%] | 1.80% | ×4.07 [3.83, 4.32] | +0.04 [-0.04, +0.12] | 119,637 | 16.7% | 0.000% | pass |
| Content server | 8.37% [7.98%, 8.74%] | 1.84% | ×4.54 [4.33, 4.74] | +1.08 [+0.88, +1.28] | 79,758 | 19.9% | 0.000% | pass |
| Combined | 7.39% [6.98%, 7.81%] | 1.81% | ×4.09 [3.86, 4.32] | +0.11 [+0.06, +0.15] | 797,580 | 9.9% | 0.000% | pass |

### R1_D60: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 7.28% [6.86%, 7.70%] | 1.80% | ×4.04 [3.81, 4.27] | -0.00 [-0.03, +0.03] | 724,404 | 9.2% | 0.000% | pass |
| First hop, content | 7.28% [6.85%, 7.71%] | 1.80% | ×4.04 [3.80, 4.28] | -0.00 [-0.03, +0.03] | 724,404 | 9.2% | 0.000% | pass |
| Credential processor | 7.28% [6.87%, 7.70%] | 1.80% | ×4.04 [3.81, 4.28] | +0.00 [-0.03, +0.03] | 639,634 | 9.4% | 0.000% | pass |
| Gatekeeper | 7.34% [6.91%, 7.80%] | 1.80% | ×4.08 [3.83, 4.33] | +0.03 [-0.06, +0.12] | 84,770 | 10.4% | 0.000% | pass |
| Content server | 8.34% [7.98%, 8.72%] | 1.84% | ×4.52 [4.33, 4.73] | +1.13 [+0.92, +1.34] | 63,431 | 20.8% | 0.000% | pass |

### R1_D60: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.74% | 7.28% [6.87%, 7.68%] | 1.80% | ×4.04 | -0.01 [-0.04, +0.03] | 396,680 | 9.8% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.17% | 7.29% [6.87%, 7.72%] | 1.80% | ×4.05 | +0.00 [-0.05, +0.06] | 232,631 | 9.8% | 0.000% | pass |
| destination only | yes | 11.92% | 7.98% [7.62%, 8.35%] | 1.83% | ×4.36 | +0.75 [+0.61, +0.91] | 95,093 | 19.3% | 0.000% | pass |
| credential first relay + content destination | yes | 0.51% | 8.69% [7.73%, 9.63%] | 1.85% | ×4.71 | +0.97 [+0.18, +1.75] | 4,029 | 29.1% | 0.000% | pass |
| content first relay + content destination | yes | 0.52% | 8.42% [7.56%, 9.32%] | 1.85% | ×4.56 | +0.79 [+0.10, +1.51] | 4,167 | 30.6% | 0.072% | pass |
| content first relay + credential destination | yes | 0.51% | 7.30% [6.46%, 8.13%] | 1.80% | ×4.05 | -0.07 [-0.29, +0.14] | 4,094 | 19.4% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 7.94% [7.37%, 8.52%] | 1.83% | ×4.34 | +0.47 [+0.13, +0.82] | 11,193 | 22.0% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 8.86% [7.05%, 10.75%] | 1.83% | ×4.84 | +1.41 [+0.20, +2.65] | 1,061 | 47.7% | 0.000% | pass |
| second relay + first relay | no | 1.16% | 7.44% [6.82%, 8.05%] | 1.80% | ×4.13 | +0.05 [-0.08, +0.20] | 9,274 | 27.3% | 0.075% | pass |
| second relay + second relay | no | 0.51% | 7.07% [6.29%, 7.97%] | 1.80% | ×3.92 | -0.15 [-0.34, +0.05] | 4,103 | 25.5% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 7.29% [6.76%, 7.84%] | 1.80% | ×4.05 | +0.01 [-0.16, +0.17] | 16,753 | 21.7% | 0.000% | pass |
| gatekeeper + second relay | no | 1.90% | 7.27% [6.74%, 7.82%] | 1.80% | ×4.04 | +0.11 [-0.03, +0.25] | 15,167 | 17.9% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 6.81% [5.87%, 7.74%] | 1.80% | ×3.78 | -0.06 [-0.38, +0.24] | 3,335 | 27.3% | 0.000% | pass |
| every record the node can select |  | 15.00% | 8.00% [7.64%, 8.38%] | 1.83% | ×4.37 | +0.71 [+0.57, +0.84] | 119,637 | 18.8% | 0.000% | pass |
| first relay held |  | 4.80% | 7.60% [7.16%, 8.06%] | 1.81% | ×4.20 | +0.20 [+0.07, +0.34] | 38,317 | 13.0% | 0.000% | pass |
| no first relay held |  | 95.20% | 7.38% [6.96%, 7.78%] | 1.81% | ×4.09 | +0.10 [+0.05, +0.15] | 759,263 | 9.8% | 0.000% | pass |

## R20_D60: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 5.31% [4.98%, 5.65%] | 1.37% | ×3.87 [3.63, 4.12] | reference | 39,774 | 12.6% | 0.000% | pass |
| First hop, credential | 5.31% [4.97%, 5.64%] | 1.37% | ×3.87 [3.62, 4.11] | -0.01 [-0.03, +0.02] | 795,480 | 10.3% | 0.000% | pass |
| First hop, content | 5.31% [4.98%, 5.64%] | 1.37% | ×3.87 [3.63, 4.11] | -0.01 [-0.03, +0.02] | 795,480 | 10.3% | 0.000% | pass |
| Credential processor | 5.31% [4.99%, 5.66%] | 1.37% | ×3.87 [3.64, 4.13] | -0.00 [-0.03, +0.02] | 676,158 | 10.4% | 0.000% | pass |
| Validator | 5.81% [5.53%, 6.10%] | 1.47% | ×3.95 [3.76, 4.14] | +0.50 [+0.19, +0.80] | 39,774 | 12.3% | 0.000% | pass |
| Gatekeeper | 5.32% [5.00%, 5.65%] | 1.37% | ×3.88 [3.64, 4.12] | +0.01 [-0.06, +0.07] | 119,322 | 12.3% | 0.000% | pass |
| Content server | 6.29% [6.03%, 6.59%] | 1.40% | ×4.48 [4.30, 4.69] | +0.98 [+0.77, +1.19] | 79,548 | 14.3% | 0.000% | pass |
| Combined | 5.41% [5.12%, 5.72%] | 1.37% | ×3.93 [3.72, 4.16] | +0.10 [+0.05, +0.14] | 795,480 | 10.5% | 0.000% | pass |

### R20_D60: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 5.31% [4.99%, 5.62%] | 1.37% | ×3.87 [3.64, 4.10] | -0.01 [-0.03, +0.02] | 722,865 | 10.2% | 0.000% | pass |
| First hop, content | 5.31% [4.98%, 5.65%] | 1.37% | ×3.87 [3.63, 4.12] | -0.01 [-0.03, +0.02] | 722,865 | 10.2% | 0.000% | pass |
| Credential processor | 5.31% [4.98%, 5.64%] | 1.37% | ×3.87 [3.63, 4.11] | -0.00 [-0.03, +0.02] | 638,110 | 10.4% | 0.000% | pass |
| Gatekeeper | 5.31% [4.99%, 5.63%] | 1.37% | ×3.87 [3.64, 4.11] | +0.01 [-0.06, +0.08] | 84,755 | 12.0% | 0.000% | pass |
| Content server | 6.31% [6.02%, 6.60%] | 1.40% | ×4.49 [4.28, 4.70] | +0.96 [+0.75, +1.18] | 63,372 | 14.7% | 0.000% | pass |

### R20_D60: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 5.31% [4.99%, 5.63%] | 1.37% | ×3.87 | -0.00 [-0.03, +0.03] | 395,215 | 10.7% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.26% | 5.31% [4.97%, 5.63%] | 1.37% | ×3.87 | +0.01 [-0.04, +0.05] | 232,722 | 11.1% | 0.000% | pass |
| destination only | yes | 11.93% | 5.96% [5.69%, 6.26%] | 1.39% | ×4.28 | +0.61 [+0.46, +0.77] | 94,928 | 13.4% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 5.69% [4.94%, 6.50%] | 1.40% | ×4.05 | +0.52 [-0.17, +1.26] | 4,004 | 19.9% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 6.21% [5.53%, 6.89%] | 1.40% | ×4.42 | +0.81 [+0.12, +1.50] | 4,077 | 12.6% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 5.09% [4.46%, 5.76%] | 1.37% | ×3.71 | +0.07 [-0.14, +0.28] | 4,147 | 25.5% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 6.10% [5.60%, 6.66%] | 1.39% | ×4.38 | +0.93 [+0.60, +1.29] | 11,103 | 19.0% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 5.74% [4.46%, 7.14%] | 1.39% | ×4.12 | +0.85 [-0.10, +1.80] | 1,063 | 37.7% | 0.000% | pass |
| second relay + first relay | no | 1.16% | 5.37% [4.85%, 5.92%] | 1.37% | ×3.92 | +0.08 [-0.05, +0.21] | 9,231 | 13.5% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 5.65% [4.88%, 6.41%] | 1.37% | ×4.11 | -0.02 [-0.17, +0.12] | 4,074 | 25.5% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 5.18% [4.79%, 5.56%] | 1.37% | ×3.78 | +0.02 [-0.10, +0.15] | 16,655 | 17.1% | 0.000% | pass |
| gatekeeper + second relay | no | 1.89% | 5.53% [5.08%, 5.99%] | 1.37% | ×4.03 | -0.03 [-0.15, +0.10] | 15,001 | 21.2% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 5.40% [4.60%, 6.26%] | 1.37% | ×3.93 | +0.03 [-0.22, +0.30] | 3,260 | 23.6% | 0.000% | pass |
| every record the node can select |  | 15.00% | 5.94% [5.66%, 6.22%] | 1.39% | ×4.27 | +0.63 [+0.48, +0.78] | 119,322 | 12.8% | 0.000% | pass |
| first relay held |  | 4.79% | 5.38% [5.07%, 5.71%] | 1.38% | ×3.90 | +0.18 [+0.03, +0.32] | 38,114 | 12.5% | 0.000% | pass |
| no first relay held |  | 95.21% | 5.41% [5.09%, 5.74%] | 1.37% | ×3.94 | +0.09 [+0.04, +0.14] | 757,366 | 10.4% | 0.000% | pass |

## R100_D60: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 3.03% [2.95%, 3.11%] | 0.69% | ×4.40 [4.28, 4.52] | reference | 199,239 | 5.8% | 0.000% | pass |
| First hop, credential | 3.03% [2.95%, 3.12%] | 0.69% | ×4.40 [4.28, 4.53] | -0.00 [-0.01, +0.01] | 3,984,780 | 5.0% | 0.000% | pass |
| First hop, content | 3.03% [2.94%, 3.11%] | 0.69% | ×4.40 [4.28, 4.52] | -0.00 [-0.01, +0.01] | 3,984,780 | 5.0% | 0.000% | pass |
| Credential processor | 3.03% [2.94%, 3.11%] | 0.69% | ×4.40 [4.27, 4.52] | -0.00 [-0.01, +0.00] | 3,387,063 | 5.0% | 0.000% | pass |
| Validator | 3.34% [3.26%, 3.42%] | 0.74% | ×4.52 [4.42, 4.63] | +0.31 [+0.21, +0.41] | 199,239 | 6.6% | 0.000% | pass |
| Gatekeeper | 3.02% [2.94%, 3.10%] | 0.69% | ×4.39 [4.27, 4.50] | -0.01 [-0.03, +0.01] | 597,717 | 5.2% | 0.000% | pass |
| Content server | 3.59% [3.51%, 3.67%] | 0.70% | ×5.10 [4.98, 5.21] | +0.56 [+0.50, +0.63] | 398,478 | 7.4% | 0.000% | pass |
| Combined | 3.08% [3.00%, 3.16%] | 0.69% | ×4.46 [4.34, 4.59] | +0.05 [+0.04, +0.06] | 3,984,780 | 5.6% | 0.000% | pass |

### R100_D60: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 3.03% [2.94%, 3.11%] | 0.69% | ×4.40 [4.27, 4.52] | -0.00 [-0.01, +0.01] | 3,620,625 | 4.9% | 0.000% | pass |
| First hop, content | 3.03% [2.94%, 3.11%] | 0.69% | ×4.40 [4.27, 4.52] | -0.00 [-0.01, +0.01] | 3,620,625 | 4.9% | 0.000% | pass |
| Credential processor | 3.03% [2.95%, 3.12%] | 0.69% | ×4.40 [4.29, 4.53] | -0.00 [-0.01, +0.00] | 3,196,513 | 5.0% | 0.000% | pass |
| Gatekeeper | 3.00% [2.91%, 3.09%] | 0.69% | ×4.36 [4.23, 4.49] | -0.00 [-0.03, +0.02] | 424,112 | 5.3% | 0.000% | pass |
| Content server | 3.59% [3.51%, 3.67%] | 0.70% | ×5.09 [4.99, 5.20] | +0.56 [+0.49, +0.63] | 317,424 | 7.2% | 0.000% | pass |

### R100_D60: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.69% | 3.03% [2.94%, 3.11%] | 0.69% | ×4.40 | -0.01 [-0.02, +0.00] | 1,980,041 | 5.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.24% | 3.02% [2.93%, 3.11%] | 0.69% | ×4.39 | -0.00 [-0.02, +0.01] | 1,165,185 | 4.7% | 0.000% | pass |
| destination only | yes | 11.93% | 3.39% [3.32%, 3.46%] | 0.70% | ×4.85 | +0.36 [+0.32, +0.41] | 475,399 | 6.6% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 3.65% [3.40%, 3.93%] | 0.70% | ×5.18 | +0.45 [+0.24, +0.67] | 19,935 | 12.7% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 3.70% [3.42%, 3.99%] | 0.70% | ×5.25 | +0.76 [+0.53, +0.98] | 20,406 | 11.8% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 2.93% [2.68%, 3.18%] | 0.69% | ×4.25 | -0.03 [-0.10, +0.03] | 20,670 | 9.9% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 3.44% [3.27%, 3.62%] | 0.70% | ×4.93 | +0.39 [+0.29, +0.50] | 56,012 | 8.0% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 3.32% [2.85%, 3.81%] | 0.70% | ×4.75 | +0.19 [-0.15, +0.55] | 5,295 | 15.4% | 0.000% | pass |
| second relay + first relay | no | 1.15% | 2.91% [2.74%, 3.08%] | 0.69% | ×4.22 | -0.02 [-0.08, +0.03] | 45,757 | 8.2% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 2.77% [2.56%, 2.97%] | 0.69% | ×4.02 | +0.00 [-0.06, +0.05] | 20,688 | 11.6% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 3.12% [3.00%, 3.25%] | 0.69% | ×4.54 | -0.02 [-0.07, +0.03] | 83,960 | 7.1% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 3.01% [2.88%, 3.14%] | 0.69% | ×4.37 | -0.02 [-0.07, +0.02] | 75,098 | 6.0% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 3.11% [2.85%, 3.37%] | 0.69% | ×4.52 | +0.01 [-0.08, +0.09] | 16,334 | 9.4% | 0.000% | pass |
| every record the node can select |  | 15.00% | 3.40% [3.32%, 3.48%] | 0.70% | ×4.86 | +0.37 [+0.33, +0.41] | 597,717 | 6.8% | 0.000% | pass |
| first relay held |  | 4.79% | 3.17% [3.07%, 3.27%] | 0.69% | ×4.58 | +0.11 [+0.07, +0.16] | 190,728 | 7.5% | 0.000% | pass |
| no first relay held |  | 95.21% | 3.08% [2.99%, 3.15%] | 0.69% | ×4.46 | +0.05 [+0.03, +0.06] | 3,794,052 | 5.6% | 0.000% | pass |

## Diagnostics

| Cell | Variant | Device named [95% CI] | Chance | Multiple of chance | Posted-time number [95% CI] | Change [95% CI] |
|---|---|---|---|---|---|---|
| R1_D60 | observer, timing evidence off | 5.42% [4.98%, 5.86%] | 1.80% | ×3.01 | 7.28% [6.86%, 7.72%] | n/a |
| R1_D60 | observer, record time at the midpoint | 7.92% [7.51%, 8.34%] | 1.84% | ×4.31 | 7.28% [6.88%, 7.71%] | +0.63 [+0.43, +0.82] |
| R1_D60 | content server, record time at the midpoint | 9.02% [8.64%, 9.39%] | 1.87% | ×4.83 | 8.37% [7.99%, 8.73%] | +0.65 [+0.47, +0.83] |
| R20_D60 | observer, timing evidence off | 3.69% [3.38%, 4.03%] | 1.37% | ×2.69 | 5.31% [4.98%, 5.64%] | n/a |
| R20_D60 | observer, record time at the midpoint | 5.82% [5.48%, 6.14%] | 1.40% | ×4.16 | 5.31% [5.00%, 5.64%] | +0.50 [+0.33, +0.67] |
| R20_D60 | content server, record time at the midpoint | 6.77% [6.49%, 7.06%] | 1.42% | ×4.76 | 6.29% [6.01%, 6.57%] | +0.48 [+0.33, +0.63] |
| R100_D60 | observer, timing evidence off | 2.11% [2.03%, 2.20%] | 0.69% | ×3.07 | 3.03% [2.95%, 3.11%] | n/a |
| R100_D60 | observer, record time at the midpoint | 3.27% [3.18%, 3.35%] | 0.70% | ×4.66 | 3.03% [2.95%, 3.12%] | +0.24 [+0.18, +0.29] |
| R100_D60 | content server, record time at the midpoint | 3.85% [3.78%, 3.93%] | 0.71% | ×5.40 | 3.59% [3.52%, 3.67%] | +0.26 [+0.21, +0.31] |

| Cell | Packet type | Observer submission hit [95% CI] | Random rate | Delay to record time, mean | Std dev |
|---|---|---|---|---|---|
| R1_D60 | credential | 0.76% [0.68%, 0.86%] | 0.28% | 1044.3 s | 304.0 s |
| R1_D60 | F content | 0.72% [0.63%, 0.81%] | 0.28% | 924.2 s | 311.5 s |
| R1_D60 | I content | 0.73% [0.64%, 0.82%] | 0.28% | 923.9 s | 312.0 s |
| R20_D60 | credential | 0.54% [0.47%, 0.61%] | 0.22% | 1043.1 s | 304.2 s |
| R20_D60 | F content | 0.54% [0.47%, 0.61%] | 0.22% | 924.0 s | 312.6 s |
| R20_D60 | I content | 0.55% [0.48%, 0.62%] | 0.22% | 923.5 s | 309.9 s |
| R100_D60 | credential | 0.30% [0.28%, 0.32%] | 0.11% | 1042.1 s | 304.8 s |
| R100_D60 | F content | 0.28% [0.25%, 0.30%] | 0.11% | 921.6 s | 310.9 s |
| R100_D60 | I content | 0.29% [0.26%, 0.31%] | 0.11% | 922.4 s | 311.6 s |

| Cell | Packet | Departure to arrival at its destination, mean | Std dev |
|---|---|---|---|
| R1_D60 | credential (at C) | 360.0 s | 263.8 s |
| R1_D60 | F content (at F) | 358.4 s | 262.0 s |
| R1_D60 | I content (at I) | 359.2 s | 263.7 s |
| R20_D60 | credential (at C) | 362.8 s | 265.0 s |
| R20_D60 | F content (at F) | 361.1 s | 263.6 s |
| R20_D60 | I content (at I) | 358.3 s | 262.9 s |
| R100_D60 | credential (at C) | 359.7 s | 263.2 s |
| R100_D60 | F content (at F) | 360.8 s | 264.1 s |
| R100_D60 | I content (at I) | 359.9 s | 263.0 s |

| Cell | F and I confirmations set by the match board |
|---|---|
| R1_D60 | 50.0% |
| R20_D60 | 50.5% |
| R100_D60 | 50.1% |

## Label shuffle

| Configuration | Cell | Vantage | Shuffled accuracy [95% CI] | Chance | Pass |
|---|---|---|---|---|---|
| Main run | R1_D60 | Passive observer | 1.67% [1.51%, 1.84%] | 1.59% | pass |
| Main run | R1_D60 | First hop | 1.66% [1.50%, 1.83%] | 1.59% | pass |
| Main run | R1_D60 | Credential processor | 1.67% [1.50%, 1.84%] | 1.59% | pass |
| Main run | R1_D60 | Validator | 1.61% [1.46%, 1.78%] | 1.59% | pass |
| Main run | R1_D60 | Gatekeeper | 1.64% [1.48%, 1.81%] | 1.59% | pass |
| Main run | R1_D60 | Content server | 1.72% [1.57%, 1.89%] | 1.59% | pass |
| Main run | R1_D60 | Combined | 1.67% [1.51%, 1.84%] | 1.59% | pass |
| Main run | R20_D60 | Passive observer | 1.26% [1.13%, 1.38%] | 1.21% | pass |
| Main run | R20_D60 | First hop | 1.26% [1.14%, 1.39%] | 1.21% | pass |
| Main run | R20_D60 | Credential processor | 1.26% [1.14%, 1.38%] | 1.21% | pass |
| Main run | R20_D60 | Validator | 1.19% [1.09%, 1.31%] | 1.21% | pass |
| Main run | R20_D60 | Gatekeeper | 1.25% [1.13%, 1.38%] | 1.21% | pass |
| Main run | R20_D60 | Content server | 1.27% [1.16%, 1.38%] | 1.21% | pass |
| Main run | R20_D60 | Combined | 1.26% [1.14%, 1.38%] | 1.21% | pass |
| Main run | R100_D60 | Passive observer | 0.60% [0.57%, 0.65%] | 0.61% | pass |
| Main run | R100_D60 | First hop | 0.60% [0.57%, 0.64%] | 0.61% | pass |
| Main run | R100_D60 | Credential processor | 0.60% [0.56%, 0.64%] | 0.61% | pass |
| Main run | R100_D60 | Validator | 0.63% [0.59%, 0.67%] | 0.61% | pass |
| Main run | R100_D60 | Gatekeeper | 0.60% [0.56%, 0.64%] | 0.61% | pass |
| Main run | R100_D60 | Content server | 0.63% [0.59%, 0.66%] | 0.61% | pass |
| Main run | R100_D60 | Combined | 0.61% [0.57%, 0.64%] | 0.61% | pass |
| Every hold off | R1_D60 | Passive observer | 0.03% [0.00%, 0.07%] | 0.03% | pass |
| Every hold off | R1_D60 | First hop | 0.03% [0.00%, 0.07%] | 0.03% | pass |
| Every hold off | R1_D60 | Credential processor | 0.03% [0.00%, 0.06%] | 0.03% | pass |
| Every hold off | R1_D60 | Validator | 0.03% [0.00%, 0.07%] | 0.03% | pass |
| Every hold off | R1_D60 | Gatekeeper | 0.02% [0.00%, 0.04%] | 0.03% | pass |
| Every hold off | R1_D60 | Content server | 0.02% [0.00%, 0.05%] | 0.03% | pass |
| Every hold off | R1_D60 | Combined | 0.03% [0.00%, 0.05%] | 0.03% | pass |
| Every hold off | R20_D60 | Passive observer | 0.04% [0.00%, 0.09%] | 0.07% | pass |
| Every hold off | R20_D60 | First hop | 0.04% [0.00%, 0.09%] | 0.07% | pass |
| Every hold off | R20_D60 | Credential processor | 0.04% [0.00%, 0.09%] | 0.07% | pass |
| Every hold off | R20_D60 | Validator | 0.04% [0.00%, 0.09%] | 0.07% | pass |
| Every hold off | R20_D60 | Gatekeeper | 0.07% [0.03%, 0.11%] | 0.07% | pass |
| Every hold off | R20_D60 | Content server | 0.08% [0.03%, 0.13%] | 0.07% | pass |
| Every hold off | R20_D60 | Combined | 0.05% [0.01%, 0.09%] | 0.07% | pass |
| Every hold off | R100_D60 | Passive observer | 0.04% [0.02%, 0.06%] | 0.04% | pass |
| Every hold off | R100_D60 | First hop | 0.04% [0.02%, 0.06%] | 0.04% | pass |
| Every hold off | R100_D60 | Credential processor | 0.04% [0.02%, 0.06%] | 0.04% | pass |
| Every hold off | R100_D60 | Validator | 0.04% [0.02%, 0.06%] | 0.04% | pass |
| Every hold off | R100_D60 | Gatekeeper | 0.03% [0.02%, 0.05%] | 0.04% | pass |
| Every hold off | R100_D60 | Content server | 0.03% [0.02%, 0.04%] | 0.04% | fail |
| Every hold off | R100_D60 | Combined | 0.04% [0.02%, 0.05%] | 0.04% | pass |
| Credential path sets the record time | R1_D60 | Passive observer | 1.63% [1.37%, 1.93%] | 1.62% | pass |
| Credential path sets the record time | R1_D60 | First hop | 1.63% [1.37%, 1.92%] | 1.62% | pass |
| Credential path sets the record time | R1_D60 | Credential processor | 1.63% [1.40%, 1.91%] | 1.62% | pass |
| Credential path sets the record time | R1_D60 | Validator | 1.78% [1.52%, 2.10%] | 1.63% | pass |
| Credential path sets the record time | R1_D60 | Gatekeeper | 1.65% [1.41%, 1.97%] | 1.62% | pass |
| Credential path sets the record time | R1_D60 | Content server | 1.60% [1.37%, 1.90%] | 1.62% | pass |
| Credential path sets the record time | R1_D60 | Combined | 1.63% [1.40%, 1.94%] | 1.62% | pass |
| Credential path sets the record time | R20_D60 | Passive observer | 1.25% [1.07%, 1.44%] | 1.22% | pass |
| Credential path sets the record time | R20_D60 | First hop | 1.25% [1.07%, 1.43%] | 1.22% | pass |
| Credential path sets the record time | R20_D60 | Credential processor | 1.25% [1.06%, 1.44%] | 1.22% | pass |
| Credential path sets the record time | R20_D60 | Validator | 1.20% [1.01%, 1.38%] | 1.22% | pass |
| Credential path sets the record time | R20_D60 | Gatekeeper | 1.24% [1.07%, 1.42%] | 1.22% | pass |
| Credential path sets the record time | R20_D60 | Content server | 1.26% [1.11%, 1.40%] | 1.22% | pass |
| Credential path sets the record time | R20_D60 | Combined | 1.25% [1.08%, 1.42%] | 1.22% | pass |
| Credential path sets the record time | R100_D60 | Passive observer | 0.59% [0.54%, 0.65%] | 0.61% | pass |
| Credential path sets the record time | R100_D60 | First hop | 0.60% [0.54%, 0.65%] | 0.61% | pass |
| Credential path sets the record time | R100_D60 | Credential processor | 0.60% [0.54%, 0.65%] | 0.61% | pass |
| Credential path sets the record time | R100_D60 | Validator | 0.61% [0.56%, 0.65%] | 0.61% | pass |
| Credential path sets the record time | R100_D60 | Gatekeeper | 0.59% [0.55%, 0.63%] | 0.61% | pass |
| Credential path sets the record time | R100_D60 | Content server | 0.59% [0.55%, 0.62%] | 0.61% | pass |
| Credential path sets the record time | R100_D60 | Combined | 0.59% [0.55%, 0.64%] | 0.61% | pass |
| Content paths set the record time | R1_D60 | Passive observer | 12.17% [11.16%, 13.10%] | 12.50% | pass |
| Content paths set the record time | R1_D60 | First hop | 12.19% [11.20%, 13.16%] | 12.50% | pass |
| Content paths set the record time | R1_D60 | Credential processor | 12.16% [11.13%, 13.12%] | 12.50% | pass |
| Content paths set the record time | R1_D60 | Validator | 12.17% [11.14%, 13.17%] | 12.50% | pass |
| Content paths set the record time | R1_D60 | Gatekeeper | 12.24% [11.20%, 13.21%] | 12.50% | pass |
| Content paths set the record time | R1_D60 | Content server | 12.29% [11.30%, 13.17%] | 12.50% | pass |
| Content paths set the record time | R1_D60 | Combined | 12.20% [11.21%, 13.10%] | 12.50% | pass |
| Content paths set the record time | R20_D60 | Passive observer | 11.07% [9.67%, 12.56%] | 11.11% | pass |
| Content paths set the record time | R20_D60 | First hop | 11.07% [9.61%, 12.55%] | 11.11% | pass |
| Content paths set the record time | R20_D60 | Credential processor | 11.10% [9.71%, 12.61%] | 11.11% | pass |
| Content paths set the record time | R20_D60 | Validator | 11.03% [9.65%, 12.64%] | 11.11% | pass |
| Content paths set the record time | R20_D60 | Gatekeeper | 11.04% [9.58%, 12.47%] | 11.11% | pass |
| Content paths set the record time | R20_D60 | Content server | 11.10% [9.67%, 12.70%] | 11.11% | pass |
| Content paths set the record time | R20_D60 | Combined | 11.09% [9.72%, 12.65%] | 11.11% | pass |
| Content paths set the record time | R100_D60 | Passive observer | 5.50% [5.27%, 5.73%] | 5.56% | pass |
| Content paths set the record time | R100_D60 | First hop | 5.51% [5.28%, 5.74%] | 5.56% | pass |
| Content paths set the record time | R100_D60 | Credential processor | 5.51% [5.27%, 5.73%] | 5.56% | pass |
| Content paths set the record time | R100_D60 | Validator | 5.63% [5.37%, 5.88%] | 5.56% | pass |
| Content paths set the record time | R100_D60 | Gatekeeper | 5.54% [5.31%, 5.77%] | 5.56% | pass |
| Content paths set the record time | R100_D60 | Content server | 5.49% [5.26%, 5.71%] | 5.56% | pass |
| Content paths set the record time | R100_D60 | Combined | 5.52% [5.30%, 5.73%] | 5.56% | pass |
| F content path sets the record time | R1_D60 | Passive observer | 9.44% [8.68%, 10.19%] | 9.09% | pass |
| F content path sets the record time | R1_D60 | First hop | 9.47% [8.72%, 10.21%] | 9.09% | pass |
| F content path sets the record time | R1_D60 | Credential processor | 9.48% [8.68%, 10.25%] | 9.09% | pass |
| F content path sets the record time | R1_D60 | Validator | 8.93% [8.17%, 9.68%] | 9.09% | pass |
| F content path sets the record time | R1_D60 | Gatekeeper | 9.47% [8.71%, 10.18%] | 9.09% | pass |
| F content path sets the record time | R1_D60 | Content server | 9.28% [8.78%, 9.77%] | 9.09% | pass |
| F content path sets the record time | R1_D60 | Combined | 9.49% [8.75%, 10.18%] | 9.09% | pass |
| F content path sets the record time | R20_D60 | Passive observer | 7.38% [6.69%, 8.12%] | 7.69% | pass |
| F content path sets the record time | R20_D60 | First hop | 7.36% [6.66%, 8.07%] | 7.69% | pass |
| F content path sets the record time | R20_D60 | Credential processor | 7.36% [6.67%, 8.05%] | 7.69% | pass |
| F content path sets the record time | R20_D60 | Validator | 7.67% [6.83%, 8.52%] | 7.69% | pass |
| F content path sets the record time | R20_D60 | Gatekeeper | 7.24% [6.54%, 7.96%] | 7.69% | pass |
| F content path sets the record time | R20_D60 | Content server | 7.17% [6.51%, 7.87%] | 7.69% | pass |
| F content path sets the record time | R20_D60 | Combined | 7.32% [6.61%, 7.99%] | 7.69% | pass |
| F content path sets the record time | R100_D60 | Passive observer | 3.93% [3.77%, 4.09%] | 3.85% | pass |
| F content path sets the record time | R100_D60 | First hop | 3.93% [3.78%, 4.09%] | 3.85% | pass |
| F content path sets the record time | R100_D60 | Credential processor | 3.93% [3.77%, 4.09%] | 3.85% | pass |
| F content path sets the record time | R100_D60 | Validator | 3.95% [3.78%, 4.11%] | 3.85% | pass |
| F content path sets the record time | R100_D60 | Gatekeeper | 3.98% [3.81%, 4.14%] | 3.85% | pass |
| F content path sets the record time | R100_D60 | Content server | 3.91% [3.75%, 4.08%] | 3.85% | pass |
| F content path sets the record time | R100_D60 | Combined | 3.94% [3.79%, 4.10%] | 3.85% | pass |

### Shuffle test (observer)

| Cell | Shuffle mismatches | Feasible-count mismatches | Exact expected accuracy | Exact expected chance | Mean accuracy over permutations (sd) | Mean chance over permutations | Interval coverage | Scored accuracy | Scored percentile |
|---|---|---|---|---|---|---|---|---|---|
| R1_D60 | 1 | 0 | 1.587% | 1.587% | 1.587% (0.091%) | 1.587% | 94.0% | 1.479% | 10.5% |
| R20_D60 | 10 | 0 | 1.205% | 1.205% | 1.200% (0.065%) | 1.205% | 91.0% | 1.285% | 91.5% |
| R100_D60 | 18 | 0 | 0.606% | 0.606% | 0.606% (0.017%) | 0.606% | 96.5% | 0.583% | 9.5% |

## Controls

### Every hold off

#### R1_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.41% [2.01%, 2.84%] | 0.91% | ×2.65 [2.22, 3.13] | reference | 9,966 | 13.7% | 0.000% | pass |
| First hop, credential | 2.41% [2.01%, 2.87%] | 0.91% | ×2.65 [2.21, 3.16] | +0.00 [+0.00, +0.00] | 199,320 | 8.2% | 0.000% | pass |
| Combined | 3.93% [3.56%, 4.35%] | 1.17% | ×3.37 [3.05, 3.72] | +1.53 [+1.34, +1.70] | 199,320 | 56.1% | 1.438% | fail |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.77% | 2.37% [1.98%, 2.84%] | 0.91% | ×2.61 | +0.00 [+0.00, +0.00] | 99,199 | 8.9% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.08% | 2.47% [2.11%, 2.87%] | 0.91% | ×2.72 | -0.03 [-0.14, +0.09] | 57,967 | 7.1% | 0.000% | pass |
| destination only | yes | 11.93% | 12.71% [11.55%, 13.91%] | 2.65% | ×4.80 | +10.22 [+9.09, +11.44] | 23,782 | 76.0% | 10.071% | fail |
| credential first relay + content destination | yes | 0.52% | 16.97% [14.83%, 19.11%] | 3.52% | ×4.83 | +15.14 [+13.20, +17.14] | 1,037 | 98.2% | 11.668% | fail |
| content first relay + content destination | yes | 0.49% | 17.79% [15.35%, 20.30%] | 3.48% | ×5.11 | +14.93 [+12.11, +17.72] | 978 | 100.0% | 9.305% | fail |
| content first relay + credential destination | yes | 0.51% | unstable | 0.91% | | | 1,014 | | | unstable (132 runs needed) |
| second relay + destination | yes | 1.42% | 11.96% [10.33%, 13.51%] | 2.59% | ×4.62 | +9.95 [+8.31, +11.58] | 2,825 | 89.8% | 9.310% | fail |
| three or more roles, with a destination | yes | 0.13% | unstable | 2.72% | | | 262 | | | unstable (87 runs needed) |
| second relay + first relay | no | 1.17% | 2.58% [1.83%, 3.41%] | 0.91% | ×2.84 | +0.00 [+0.00, +0.00] | 2,324 | 26.8% | 0.000% | pass |
| second relay + second relay | no | 0.52% | unstable | 0.91% | | | 1,032 | | | unstable (125 runs needed) |
| gatekeeper + first relay | no | 2.10% | 2.30% [1.83%, 2.82%] | 0.91% | ×2.52 | +0.48 [+0.02, +0.94] | 4,183 | 15.8% | 0.000% | pass |
| gatekeeper + second relay | no | 1.96% | 2.69% [2.16%, 3.25%] | 0.91% | ×2.97 | +0.03 [-0.41, +0.46] | 3,899 | 16.9% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.91% | | | 818 | | | unstable (148 runs needed) |
| every record the node can select |  | 15.00% | 12.57% [11.35%, 13.77%] | 2.64% | ×4.76 | +10.16 [+9.01, +11.33] | 29,898 | 76.1% | 9.589% | fail |
| first relay held |  | 4.78% | 5.51% [4.98%, 6.03%] | 1.46% | ×3.78 | +3.39 [+2.93, +3.85] | 9,536 | 71.2% | 2.003% | fail |
| no first relay held |  | 95.22% | 3.85% [3.49%, 4.28%] | 1.15% | ×3.34 | +1.43 [+1.25, +1.60] | 189,784 | 55.4% | 1.399% | fail |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 9,966 |
| D or G | +0.00 [+0.00, +0.00] | 19,932 |

#### R20_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 1.96% [1.64%, 2.29%] | 0.70% | ×2.81 [2.35, 3.27] | reference | 9,852 | 5.5% | 0.000% | pass |
| First hop, credential | 1.96% [1.66%, 2.30%] | 0.70% | ×2.81 [2.37, 3.30] | +0.00 [+0.00, +0.00] | 197,040 | 1.6% | 0.000% | pass |
| Combined | 3.27% [2.95%, 3.60%] | 0.89% | ×3.67 [3.31, 4.04] | +1.31 [+1.18, +1.45] | 197,040 | 46.0% | 0.451% | fail |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.66% | 1.93% [1.62%, 2.25%] | 0.70% | ×2.77 | +0.00 [+0.00, +0.00] | 97,847 | 1.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.28% | 2.03% [1.73%, 2.35%] | 0.70% | ×2.90 | +0.02 [-0.05, +0.09] | 57,696 | 2.7% | 0.000% | pass |
| destination only | yes | 11.95% | 10.89% [9.93%, 11.82%] | 2.00% | ×5.46 | +8.87 [+7.95, +9.81] | 23,545 | 70.5% | 4.396% | fail |
| credential first relay + content destination | yes | 0.49% | 14.88% [12.17%, 17.68%] | 2.59% | ×5.74 | +13.95 [+11.34, +16.72] | 968 | 68.7% | 1.343% | fail |
| content first relay + content destination | yes | 0.51% | 13.25% [11.20%, 15.40%] | 2.59% | ×5.12 | +11.47 [+9.44, +13.48] | 1,011 | 94.3% | 3.264% | fail |
| content first relay + credential destination | yes | 0.55% | unstable | 0.70% | | | 1,075 | | | unstable (167 runs needed) |
| second relay + destination | yes | 1.37% | 9.76% [8.50%, 11.07%] | 1.96% | ×4.97 | +7.62 [+6.27, +8.95] | 2,705 | 72.4% | 2.847% | fail |
| three or more roles, with a destination | yes | 0.13% | unstable | 2.06% | | | 252 | | | unstable (74 runs needed) |
| second relay + first relay | no | 1.12% | unstable | 0.70% | | | 2,214 | | | unstable (57 runs needed) |
| second relay + second relay | no | 0.54% | unstable | 0.70% | | | 1,066 | | | unstable (114 runs needed) |
| gatekeeper + first relay | no | 2.09% | 1.83% [1.35%, 2.30%] | 0.70% | ×2.61 | -0.29 [-0.72, +0.12] | 4,109 | 8.6% | 0.000% | pass |
| gatekeeper + second relay | no | 1.90% | 1.82% [1.32%, 2.31%] | 0.70% | ×2.60 | +0.11 [-0.29, +0.51] | 3,746 | 21.3% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.70% | | | 806 | | | unstable (167 runs needed) |
| every record the node can select |  | 15.00% | 10.68% [9.79%, 11.58%] | 1.99% | ×5.38 | +8.72 [+7.89, +9.61] | 29,556 | 68.5% | 4.124% | fail |
| first relay held |  | 4.76% | 4.39% [3.92%, 4.90%] | 1.10% | ×4.01 | +2.55 [+2.15, +2.97] | 9,377 | 51.6% | 0.437% | fail |
| no first relay held |  | 95.24% | 3.21% [2.90%, 3.55%] | 0.88% | ×3.65 | +1.25 [+1.12, +1.39] | 187,663 | 46.3% | 0.570% | fail |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 9,852 |
| D or G | +0.00 [+0.00, +0.00] | 19,704 |

#### R100_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 1.07% [0.97%, 1.17%] | 0.35% | ×3.09 [2.81, 3.38] | reference | 49,967 | 2.6% | 0.000% | pass |
| First hop, credential | 1.07% [0.97%, 1.16%] | 0.35% | ×3.09 [2.82, 3.37] | +0.00 [+0.00, +0.00] | 999,340 | 1.4% | 0.000% | pass |
| Combined | 1.87% [1.77%, 1.98%] | 0.44% | ×4.21 [3.98, 4.45] | +0.80 [+0.73, +0.87] | 999,340 | 26.2% | 0.007% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.70% | 1.07% [0.98%, 1.17%] | 0.35% | ×3.10 | +0.00 [+0.00, +0.00] | 496,649 | 1.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.24% | 1.07% [0.98%, 1.16%] | 0.35% | ×3.09 | +0.00 [-0.02, +0.02] | 292,160 | 2.0% | 0.000% | pass |
| destination only | yes | 11.91% | 6.33% [5.89%, 6.77%] | 1.00% | ×6.31 | +5.26 [+4.84, +5.70] | 119,053 | 34.4% | 0.041% | pass |
| credential first relay + content destination | yes | 0.52% | 9.13% [7.96%, 10.30%] | 1.35% | ×6.74 | +8.14 [+7.05, +9.27] | 5,171 | 52.0% | 0.367% | fail |
| content first relay + content destination | yes | 0.51% | 9.08% [8.10%, 10.06%] | 1.35% | ×6.71 | +8.00 [+7.00, +9.03] | 5,053 | 51.0% | 0.653% | fail |
| content first relay + credential destination | yes | 0.52% | 1.34% [1.03%, 1.65%] | 0.35% | ×3.89 | +0.00 [+0.00, +0.00] | 5,212 | 10.1% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 6.87% [6.26%, 7.48%] | 1.00% | ×6.84 | +5.84 [+5.21, +6.46] | 14,136 | 42.9% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 6.82% [5.02%, 8.74%] | 1.00% | ×6.85 | +5.64 [+3.85, +7.55] | 1,276 | 76.8% | 1.332% | fail |
| second relay + first relay | no | 1.16% | 0.98% [0.81%, 1.14%] | 0.35% | ×2.82 | +0.00 [+0.00, +0.00] | 11,589 | 3.2% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 1.26% [0.97%, 1.57%] | 0.35% | ×3.64 | +0.00 [+0.00, +0.00] | 5,093 | 10.3% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 1.04% [0.89%, 1.19%] | 0.35% | ×3.02 | -0.06 [-0.17, +0.04] | 21,016 | 2.6% | 0.000% | pass |
| gatekeeper + second relay | no | 1.89% | 1.12% [0.97%, 1.26%] | 0.35% | ×3.24 | +0.07 [-0.04, +0.19] | 18,876 | 4.6% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.35% | | | 4,056 | | | unstable (57 runs needed) |
| every record the node can select |  | 15.00% | 6.40% [5.95%, 6.84%] | 1.00% | ×6.37 | +5.33 [+4.87, +5.79] | 149,901 | 35.2% | 0.042% | pass |
| first relay held |  | 4.81% | 2.77% [2.57%, 2.99%] | 0.56% | ×4.95 | +1.69 [+1.49, +1.89] | 48,041 | 35.5% | 0.027% | pass |
| no first relay held |  | 95.19% | 1.82% [1.72%, 1.93%] | 0.44% | ×4.16 | +0.75 [+0.69, +0.82] | 951,299 | 25.7% | 0.006% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 49,967 |
| D or G | +0.00 [+0.00, +0.00] | 99,934 |

### Credential path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D60 | 95.8% |
| R20_D60 | 96.2% |
| R100_D60 | 96.0% |

#### R1_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 7.24% [6.77%, 7.70%] | 1.80% | ×4.02 [3.75, 4.27] | reference | 19,481 | 16.5% | 0.000% | pass |
| First hop, credential | 7.26% [6.79%, 7.75%] | 1.80% | ×4.03 [3.77, 4.30] | +0.02 [-0.01, +0.05] | 389,620 | 12.6% | 0.000% | pass |
| Combined | 7.47% [7.01%, 7.92%] | 1.84% | ×4.05 [3.80, 4.30] | +0.23 [+0.17, +0.30] | 389,620 | 14.8% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.70% | 7.21% [6.77%, 7.70%] | 1.80% | ×4.00 | -0.00 [-0.04, +0.04] | 193,625 | 13.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.21% | 7.33% [6.87%, 7.78%] | 1.80% | ×4.06 | -0.01 [-0.09, +0.07] | 113,821 | 14.4% | 0.000% | pass |
| destination only | yes | 11.97% | 8.64% [8.20%, 9.06%] | 2.07% | ×4.17 | +1.46 [+1.15, +1.74] | 46,624 | 22.9% | 0.000% | pass |
| credential first relay + content destination | yes | 0.52% | 9.62% [8.34%, 11.00%] | 2.22% | ×4.34 | +1.97 [+0.50, +3.42] | 2,027 | 41.6% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 11.04% [9.60%, 12.54%] | 2.20% | ×5.01 | +2.94 [+1.45, +4.40] | 1,975 | 36.0% | 0.051% | pass |
| content first relay + credential destination | yes | 0.52% | 8.12% [6.92%, 9.36%] | 1.80% | ×4.50 | -0.05 [-0.39, +0.26] | 2,008 | 46.9% | 0.000% | pass |
| second relay + destination | yes | 1.36% | 9.37% [8.45%, 10.39%] | 2.07% | ×4.53 | +2.04 [+1.24, +2.86] | 5,302 | 31.4% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 2.06% | | | 507 | | | unstable (139 runs needed) |
| second relay + first relay | no | 1.14% | 6.78% [6.01%, 7.61%] | 1.81% | ×3.76 | +0.05 [-0.18, +0.29] | 4,423 | 24.0% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 6.99% [6.12%, 7.89%] | 1.80% | ×3.88 | +0.00 [-0.20, +0.20] | 2,031 | 36.0% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 7.08% [6.43%, 7.77%] | 1.80% | ×3.93 | +0.12 [-0.22, +0.46] | 8,132 | 19.8% | 0.000% | pass |
| gatekeeper + second relay | no | 1.92% | 7.32% [6.62%, 8.08%] | 1.80% | ×4.06 | -0.08 [-0.40, +0.23] | 7,464 | 18.0% | 0.000% | pass |
| three or more roles, no destination | no | 0.43% | 6.60% [5.49%, 7.71%] | 1.80% | ×3.66 | +0.12 [-0.66, +0.94] | 1,681 | 41.0% | 0.000% | pass |
| every record the node can select |  | 15.00% | 8.79% [8.36%, 9.23%] | 2.07% | ×4.24 | +1.55 [+1.28, +1.81] | 58,443 | 21.8% | 0.000% | pass |
| first relay held |  | 4.76% | 7.82% [7.28%, 8.42%] | 1.89% | ×4.13 | +0.59 [+0.33, +0.85] | 18,565 | 18.5% | 0.000% | pass |
| no first relay held |  | 95.24% | 7.46% [6.99%, 7.91%] | 1.84% | ×4.05 | +0.21 [+0.14, +0.27] | 371,055 | 14.8% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.09 [+0.01, +0.18] | 19,481 |
| D or G | +0.09 [+0.01, +0.17] | 38,962 |

#### R20_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 5.80% [5.34%, 6.24%] | 1.38% | ×4.20 [3.86, 4.51] | reference | 19,398 | 14.2% | 0.000% | pass |
| First hop, credential | 5.83% [5.38%, 6.26%] | 1.38% | ×4.21 [3.89, 4.53] | +0.02 [-0.01, +0.05] | 387,960 | 10.2% | 0.000% | pass |
| Combined | 6.01% [5.59%, 6.42%] | 1.41% | ×4.25 [3.95, 4.54] | +0.21 [+0.14, +0.27] | 387,960 | 12.7% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 5.82% [5.39%, 6.26%] | 1.38% | ×4.20 | +0.02 [-0.03, +0.06] | 192,728 | 10.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.27% | 5.82% [5.40%, 6.24%] | 1.38% | ×4.21 | -0.01 [-0.10, +0.07] | 113,569 | 12.1% | 0.000% | pass |
| destination only | yes | 11.92% | 7.13% [6.72%, 7.52%] | 1.59% | ×4.48 | +1.36 [+1.11, +1.63] | 46,254 | 17.7% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 6.99% [5.70%, 8.29%] | 1.70% | ×4.12 | +1.46 [+0.10, +2.84] | 1,917 | 48.8% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 8.30% [7.09%, 9.55%] | 1.70% | ×4.89 | +1.35 [+0.05, +2.68] | 1,927 | 37.6% | 0.000% | pass |
| content first relay + credential destination | yes | 0.54% | 5.83% [4.85%, 6.86%] | 1.38% | ×4.21 | +0.05 [-0.24, +0.33] | 2,092 | 22.7% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 7.22% [6.41%, 8.03%] | 1.59% | ×4.53 | +1.28 [+0.66, +1.93] | 5,468 | 21.8% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 1.59% | | | 536 | | | unstable (143 runs needed) |
| second relay + first relay | no | 1.13% | 6.18% [5.42%, 6.94%] | 1.38% | ×4.47 | +0.32 [+0.09, +0.56] | 4,370 | 21.2% | 0.000% | pass |
| second relay + second relay | no | 0.54% | 5.91% [4.85%, 7.06%] | 1.38% | ×4.27 | -0.19 [-0.45, +0.05] | 2,080 | 28.9% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 5.87% [5.23%, 6.51%] | 1.38% | ×4.24 | -0.09 [-0.46, +0.26] | 8,176 | 19.6% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 5.48% [4.88%, 6.09%] | 1.38% | ×3.96 | +0.00 [-0.31, +0.30] | 7,275 | 16.8% | 0.000% | pass |
| three or more roles, no destination | no | 0.40% | 5.55% [4.30%, 6.94%] | 1.38% | ×4.01 | +0.45 [-0.26, +1.15] | 1,568 | 36.0% | 0.000% | pass |
| every record the node can select |  | 15.00% | 7.12% [6.72%, 7.53%] | 1.59% | ×4.48 | +1.32 [+1.09, +1.56] | 58,194 | 17.2% | 0.000% | pass |
| first relay held |  | 4.76% | 6.31% [5.82%, 6.81%] | 1.45% | ×4.35 | +0.34 [+0.11, +0.58] | 18,482 | 19.2% | 0.000% | pass |
| no first relay held |  | 95.24% | 6.00% [5.56%, 6.43%] | 1.41% | ×4.24 | +0.20 [+0.13, +0.26] | 369,478 | 12.5% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.03 [-0.06, +0.11] | 19,398 |
| D or G | +0.10 [+0.03, +0.17] | 38,796 |

#### R100_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.93% [2.81%, 3.06%] | 0.69% | ×4.26 [4.08, 4.45] | reference | 97,502 | 4.2% | 0.000% | pass |
| First hop, credential | 2.93% [2.81%, 3.05%] | 0.69% | ×4.25 [4.09, 4.43] | -0.01 [-0.02, +0.01] | 1,950,040 | 3.2% | 0.000% | pass |
| Combined | 3.05% [2.93%, 3.16%] | 0.70% | ×4.33 [4.17, 4.49] | +0.12 [+0.09, +0.14] | 1,950,040 | 5.8% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 2.91% [2.78%, 3.03%] | 0.69% | ×4.23 | -0.01 [-0.03, +0.00] | 968,704 | 3.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.25% | 2.95% [2.84%, 3.06%] | 0.69% | ×4.29 | -0.01 [-0.04, +0.03] | 570,480 | 3.8% | 0.000% | pass |
| destination only | yes | 11.94% | 3.78% [3.67%, 3.90%] | 0.79% | ×4.79 | +0.83 [+0.74, +0.91] | 232,900 | 7.9% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 4.16% [3.78%, 4.52%] | 0.84% | ×4.95 | +1.14 [+0.73, +1.53] | 9,560 | 11.6% | 0.000% | pass |
| content first relay + content destination | yes | 0.52% | 4.06% [3.64%, 4.49%] | 0.84% | ×4.82 | +1.33 [+0.86, +1.78] | 10,093 | 17.3% | 0.000% | pass |
| content first relay + credential destination | yes | 0.53% | 3.03% [2.69%, 3.40%] | 0.69% | ×4.40 | +0.06 [-0.04, +0.16] | 10,346 | 10.9% | 0.000% | pass |
| second relay + destination | yes | 1.39% | 3.66% [3.46%, 3.85%] | 0.79% | ×4.63 | +0.89 [+0.67, +1.09] | 27,061 | 11.6% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 3.46% [2.76%, 4.13%] | 0.79% | ×4.38 | +0.94 [+0.39, +1.56] | 2,546 | 30.0% | 0.000% | pass |
| second relay + first relay | no | 1.15% | 2.85% [2.59%, 3.11%] | 0.69% | ×4.14 | -0.02 [-0.09, +0.04] | 22,496 | 9.1% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 2.98% [2.63%, 3.37%] | 0.69% | ×4.34 | -0.01 [-0.10, +0.08] | 10,131 | 8.4% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 2.78% [2.57%, 2.98%] | 0.69% | ×4.04 | -0.07 [-0.17, +0.02] | 40,786 | 4.1% | 0.000% | pass |
| gatekeeper + second relay | no | 1.89% | 2.95% [2.75%, 3.15%] | 0.69% | ×4.29 | +0.01 [-0.11, +0.13] | 36,930 | 4.2% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 3.06% [2.71%, 3.40%] | 0.69% | ×4.45 | +0.04 [-0.21, +0.28] | 8,007 | 6.7% | 0.000% | pass |
| every record the node can select |  | 15.00% | 3.76% [3.65%, 3.86%] | 0.79% | ×4.76 | +0.83 [+0.76, +0.91] | 292,506 | 8.1% | 0.000% | pass |
| first relay held |  | 4.78% | 3.10% [2.94%, 3.27%] | 0.72% | ×4.31 | +0.23 [+0.15, +0.31] | 93,281 | 8.9% | 0.000% | pass |
| no first relay held |  | 95.22% | 3.04% [2.93%, 3.15%] | 0.70% | ×4.34 | +0.11 [+0.09, +0.13] | 1,856,759 | 5.8% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.00 [-0.03, +0.03] | 97,502 |
| D or G | +0.03 [+0.01, +0.05] | 195,004 |

### Content paths set the record time

| Cell | Intended path's share |
|---|---|
| R1_D60 | 97.9% |
| R20_D60 | 97.9% |
| R100_D60 | 98.1% |

#### R1_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | unstable | 12.50% | | | 19,917 | | | unstable (1667 runs needed) |
| First hop, credential | 0.02% [0.00%, 0.05%] | 12.50% | ×0.00 [0.00, 0.00] | +0.00 [-0.00, +0.01] | 398,340 | 0.1% | 0.000% | pass |
| Combined | 0.05% [0.03%, 0.09%] | 12.50% | ×0.00 [0.00, 0.01] | +0.04 [+0.03, +0.05] | 398,340 | 0.2% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.78% | 0.03% [0.00%, 0.06%] | 12.50% | ×0.00 | +0.01 [-0.00, +0.03] | 198,304 | 0.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.10% | unstable | 12.50% | | | 115,913 | | | unstable (132 runs needed) |
| destination only | yes | 11.90% | 0.18% [0.13%, 0.24%] | 12.50% | ×0.01 | +0.16 [+0.13, +0.20] | 47,395 | 1.5% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | unstable | 12.50% | | | 2,002 | | | unstable (556 runs needed) |
| content first relay + content destination | yes | 0.51% | unstable | 12.50% | | | 2,051 | | | unstable (1000 runs needed) |
| content first relay + credential destination | yes | 0.53% | unstable | 12.50% | | | 2,097 | | | unstable (inf runs needed) |
| second relay + destination | yes | 1.42% | unstable | 12.50% | | | 5,673 | | | unstable (278 runs needed) |
| three or more roles, with a destination | yes | 0.13% | unstable | 12.50% | | | 533 | | | unstable (5000 runs needed) |
| second relay + first relay | no | 1.15% | unstable | 12.50% | | | 4,597 | | | unstable (1667 runs needed) |
| second relay + second relay | no | 0.53% | unstable | 12.50% | | | 2,115 | | | unstable (inf runs needed) |
| gatekeeper + first relay | no | 2.09% | unstable | 12.50% | | | 8,340 | | | unstable (1667 runs needed) |
| gatekeeper + second relay | no | 1.92% | unstable | 12.50% | | | 7,650 | | | unstable (2500 runs needed) |
| three or more roles, no destination | no | 0.42% | unstable | 12.50% | | | 1,670 | | | unstable (5000 runs needed) |
| every record the node can select |  | 15.00% | 0.20% [0.15%, 0.25%] | 12.50% | ×0.02 | +0.18 [+0.15, +0.22] | 59,751 | 1.2% | 0.000% | pass |
| first relay held |  | 4.79% | unstable | 12.50% | | | 19,087 | | | unstable (250 runs needed) |
| no first relay held |  | 95.21% | 0.05% [0.03%, 0.09%] | 12.50% | ×0.00 | +0.04 [+0.02, +0.05] | 379,253 | 0.2% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.01 [+0.00, +0.02] | 19,917 |
| D or G | +0.02 [-0.00, +0.04] | 39,834 |

#### R20_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 35.11% [33.53%, 36.56%] | 11.11% | ×3.16 [3.02, 3.29] | reference | 19,751 | 82.1% | 21.928% | fail |
| First hop, credential | 35.14% [33.66%, 36.64%] | 11.11% | ×3.16 [3.03, 3.30] | +0.03 [-0.03, +0.09] | 395,020 | 77.4% | 22.111% | fail |
| Combined | 35.37% [33.89%, 36.79%] | 11.11% | ×3.18 [3.05, 3.31] | +0.26 [+0.14, +0.38] | 395,020 | 78.1% | 23.348% | fail |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.63% | 35.00% [33.43%, 36.49%] | 11.11% | ×3.15 | -0.13 [-0.23, -0.04] | 196,051 | 76.8% | 21.418% | fail |
| one relay or gatekeeper role | no | 29.32% | 35.14% [33.66%, 36.71%] | 11.11% | ×3.16 | +0.09 [-0.07, +0.26] | 115,820 | 76.8% | 22.339% | fail |
| destination only | yes | 11.99% | 36.87% [35.47%, 38.26%] | 11.11% | ×3.32 | +1.85 [+1.51, +2.21] | 47,363 | 81.9% | 32.386% | fail |
| credential first relay + content destination | yes | 0.49% | 37.08% [34.84%, 39.40%] | 11.11% | ×3.34 | +1.66 [-0.00, +3.35] | 1,931 | 84.6% | 27.706% | fail |
| content first relay + content destination | yes | 0.50% | 37.85% [35.58%, 40.22%] | 11.11% | ×3.41 | +4.00 [+2.18, +5.93] | 1,976 | 85.5% | 42.257% | fail |
| content first relay + credential destination | yes | 0.50% | 37.44% [34.98%, 39.92%] | 11.11% | ×3.37 | +1.46 [+0.72, +2.27] | 1,982 | 88.8% | 27.497% | fail |
| second relay + destination | yes | 1.39% | 37.42% [36.06%, 38.96%] | 11.11% | ×3.37 | +1.24 [+0.36, +2.17] | 5,473 | 92.4% | 39.960% | fail |
| three or more roles, with a destination | yes | 0.13% | 33.33% [28.88%, 37.89%] | 11.11% | ×3.00 | +0.76 [-2.44, +3.89] | 528 | 88.2% | 10.417% | fail |
| second relay + first relay | no | 1.17% | 36.18% [34.24%, 38.02%] | 11.11% | ×3.26 | +0.43 [+0.00, +0.88] | 4,627 | 90.9% | 27.037% | fail |
| second relay + second relay | no | 0.49% | 34.16% [31.58%, 36.95%] | 11.11% | ×3.07 | -0.05 [-0.47, +0.36] | 1,938 | 88.2% | 24.097% | fail |
| gatekeeper + first relay | no | 2.09% | 36.11% [34.08%, 38.00%] | 11.11% | ×3.25 | +0.76 [+0.28, +1.22] | 8,244 | 78.4% | 24.757% | fail |
| gatekeeper + second relay | no | 1.88% | 35.22% [33.63%, 36.90%] | 11.11% | ×3.17 | -0.03 [-0.53, +0.48] | 7,411 | 85.1% | 17.447% | fail |
| three or more roles, no destination | no | 0.42% | 34.67% [31.59%, 37.83%] | 11.11% | ×3.12 | +0.48 [-0.49, +1.52] | 1,676 | 99.0% | 23.807% | fail |
| every record the node can select |  | 15.00% | 36.95% [35.56%, 38.30%] | 11.11% | ×3.33 | +1.84 [+1.51, +2.16] | 59,253 | 82.0% | 33.262% | fail |
| first relay held |  | 4.75% | 36.55% [34.94%, 38.18%] | 11.11% | ×3.29 | +1.19 [+0.79, +1.60] | 18,760 | 81.1% | 28.364% | fail |
| no first relay held |  | 95.25% | 35.31% [33.76%, 36.77%] | 11.11% | ×3.18 | +0.21 [+0.09, +0.33] | 376,260 | 78.3% | 23.075% | fail |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.07 [-0.19, +0.05] | 19,751 |
| D or G | +0.86 [+0.68, +1.03] | 39,502 |

#### R100_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 15.57% [15.28%, 15.86%] | 5.56% | ×2.80 [2.75, 2.85] | reference | 99,758 | 30.9% | 0.003% | pass |
| First hop, credential | 15.60% [15.32%, 15.87%] | 5.56% | ×2.81 [2.76, 2.86] | +0.02 [+0.00, +0.05] | 1,995,160 | 28.4% | 0.006% | pass |
| Combined | 15.89% [15.62%, 16.17%] | 5.56% | ×2.86 [2.81, 2.91] | +0.31 [+0.28, +0.35] | 1,995,160 | 31.6% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.67% | 15.53% [15.25%, 15.82%] | 5.56% | ×2.80 | -0.04 [-0.07, -0.00] | 990,966 | 28.1% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.26% | 15.70% [15.43%, 15.98%] | 5.56% | ×2.83 | +0.13 [+0.09, +0.17] | 583,775 | 29.4% | 0.003% | pass |
| destination only | yes | 11.95% | 17.40% [17.14%, 17.68%] | 5.56% | ×3.13 | +1.77 [+1.65, +1.89] | 238,506 | 39.6% | 0.008% | pass |
| credential first relay + content destination | yes | 0.50% | 18.17% [17.36%, 19.01%] | 5.56% | ×3.27 | +2.81 [+2.20, +3.49] | 9,955 | 51.8% | 0.432% | fail |
| content first relay + content destination | yes | 0.50% | 18.67% [17.87%, 19.48%] | 5.56% | ×3.36 | +3.33 [+2.74, +3.94] | 10,002 | 53.8% | 0.050% | fail |
| content first relay + credential destination | yes | 0.51% | 16.17% [15.39%, 17.01%] | 5.56% | ×2.91 | +0.70 [+0.47, +0.94] | 10,269 | 37.5% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 17.37% [16.86%, 17.90%] | 5.56% | ×3.13 | +2.13 [+1.85, +2.41] | 27,938 | 42.4% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 18.55% [17.05%, 20.17%] | 5.56% | ×3.34 | +2.53 [+1.46, +3.58] | 2,604 | 53.8% | 0.000% | fail |
| second relay + first relay | no | 1.16% | 16.06% [15.60%, 16.55%] | 5.56% | ×2.89 | +0.46 [+0.31, +0.62] | 23,144 | 32.4% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 15.68% [14.98%, 16.41%] | 5.56% | ×2.82 | -0.02 [-0.20, +0.16] | 10,203 | 29.4% | 0.029% | pass |
| gatekeeper + first relay | no | 2.11% | 16.31% [15.84%, 16.74%] | 5.56% | ×2.94 | +0.42 [+0.28, +0.55] | 42,096 | 34.7% | 0.040% | pass |
| gatekeeper + second relay | no | 1.88% | 15.41% [14.99%, 15.81%] | 5.56% | ×2.77 | -0.10 [-0.25, +0.04] | 37,494 | 33.0% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 15.36% [14.52%, 16.23%] | 5.56% | ×2.77 | +0.34 [+0.06, +0.65] | 8,208 | 42.4% | 0.061% | pass |
| every record the node can select |  | 15.00% | 17.43% [17.17%, 17.71%] | 5.56% | ×3.14 | +1.86 [+1.75, +1.97] | 299,274 | 39.8% | 0.000% | pass |
| first relay held |  | 4.78% | 16.68% [16.34%, 16.99%] | 5.56% | ×3.00 | +1.01 [+0.88, +1.14] | 95,466 | 38.4% | 0.014% | pass |
| no first relay held |  | 95.22% | 15.85% [15.59%, 16.12%] | 5.56% | ×2.85 | +0.28 [+0.24, +0.31] | 1,899,694 | 31.3% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.02 [-0.03, +0.07] | 99,758 |
| D or G | +0.60 [+0.55, +0.66] | 199,516 |

### F content path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D60 | 96.7% |
| R20_D60 | 96.9% |
| R100_D60 | 97.1% |

#### R1_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | unstable | 9.09% | | | 19,882 | | | unstable (239 runs needed) |
| First hop, credential | 0.11% [0.07%, 0.15%] | 9.09% | ×0.01 [0.01, 0.02] | -0.00 [-0.01, +0.00] | 397,640 | 0.1% | 0.000% | pass |
| Combined | 0.51% [0.46%, 0.56%] | 9.09% | ×0.06 [0.05, 0.06] | +0.41 [+0.38, +0.44] | 397,640 | 10.0% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 0.13% [0.09%, 0.18%] | 9.09% | ×0.01 | +0.03 [+0.01, +0.05] | 197,537 | 0.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.25% | 0.14% [0.10%, 0.18%] | 9.09% | ×0.02 | +0.03 [+0.01, +0.06] | 116,313 | 0.3% | 0.000% | pass |
| destination only | yes | 11.94% | 2.65% [2.50%, 2.81%] | 9.09% | ×0.29 | +2.55 [+2.40, +2.71] | 47,493 | 16.8% | 0.000% | pass |
| credential first relay + content destination | yes | 0.52% | 4.18% [3.30%, 5.09%] | 9.09% | ×0.46 | +4.09 [+3.21, +4.95] | 2,056 | 50.0% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 3.86% [3.10%, 4.64%] | 9.09% | ×0.42 | +3.76 [+3.05, +4.49] | 1,996 | 36.0% | 0.000% | pass |
| content first relay + credential destination | yes | 0.51% | unstable | 9.09% | | | 2,041 | | | unstable (1667 runs needed) |
| second relay + destination | yes | 1.39% | 2.54% [2.18%, 2.91%] | 9.09% | ×0.28 | +2.44 [+2.09, +2.79] | 5,543 | 28.3% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 9.09% | | | 517 | | | unstable (500 runs needed) |
| second relay + first relay | no | 1.14% | unstable | 9.09% | | | 4,537 | | | unstable (1250 runs needed) |
| second relay + second relay | no | 0.50% | unstable | 9.09% | | | 2,004 | | | unstable (715 runs needed) |
| gatekeeper + first relay | no | 2.11% | unstable | 9.09% | | | 8,400 | | | unstable (500 runs needed) |
| gatekeeper + second relay | no | 1.90% | unstable | 9.09% | | | 7,575 | | | unstable (500 runs needed) |
| three or more roles, no destination | no | 0.41% | unstable | 9.09% | | | 1,628 | | | unstable (1250 runs needed) |
| every record the node can select |  | 15.00% | 2.64% [2.51%, 2.78%] | 9.09% | ×0.29 | +2.54 [+2.41, +2.68] | 59,646 | 17.1% | 0.000% | pass |
| first relay held |  | 4.79% | 0.95% [0.81%, 1.10%] | 9.09% | ×0.10 | +0.86 [+0.73, +0.99] | 19,030 | 15.7% | 0.000% | pass |
| no first relay held |  | 95.21% | 0.49% [0.44%, 0.54%] | 9.09% | ×0.05 | +0.38 [+0.36, +0.41] | 378,610 | 9.7% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.01 [-0.03, +0.01] | 19,882 |
| D or G | +0.02 [+0.00, +0.04] | 39,764 |

#### R20_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 20.74% [19.74%, 21.73%] | 7.69% | ×2.70 [2.57, 2.82] | reference | 19,770 | 45.3% | 0.035% | pass |
| First hop, credential | 20.77% [19.76%, 21.78%] | 7.69% | ×2.70 [2.57, 2.83] | +0.03 [-0.02, +0.08] | 395,400 | 40.2% | 0.038% | pass |
| Combined | 21.21% [20.30%, 22.11%] | 7.69% | ×2.76 [2.64, 2.87] | +0.47 [+0.33, +0.61] | 395,400 | 48.0% | 0.603% | fail |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.70% | 20.47% [19.45%, 21.40%] | 7.69% | ×2.66 | -0.28 [-0.40, -0.16] | 196,523 | 40.4% | 0.039% | pass |
| one relay or gatekeeper role | no | 29.19% | 20.69% [19.73%, 21.63%] | 7.69% | ×2.69 | -0.09 [-0.26, +0.07] | 115,417 | 40.7% | 0.000% | pass |
| destination only | yes | 11.93% | 24.78% [23.95%, 25.57%] | 7.69% | ×3.22 | +4.11 [+3.72, +4.53] | 47,160 | 64.9% | 5.274% | fail |
| credential first relay + content destination | yes | 0.49% | 25.64% [23.55%, 27.67%] | 7.69% | ×3.33 | +4.94 [+3.22, +6.70] | 1,942 | 68.3% | 7.467% | fail |
| content first relay + content destination | yes | 0.52% | 29.00% [26.59%, 31.46%] | 7.69% | ×3.77 | +6.79 [+4.70, +8.76] | 2,062 | 75.5% | 2.473% | fail |
| content first relay + credential destination | yes | 0.53% | 21.50% [19.55%, 23.43%] | 7.69% | ×2.79 | +0.62 [+0.05, +1.20] | 2,098 | 79.2% | 2.050% | fail |
| second relay + destination | yes | 1.41% | 25.43% [24.26%, 26.65%] | 7.69% | ×3.31 | +4.74 [+3.77, +5.76] | 5,588 | 75.5% | 4.671% | fail |
| three or more roles, with a destination | yes | 0.12% | 27.61% [23.62%, 32.03%] | 7.69% | ×3.59 | +5.22 [+2.15, +8.51] | 460 | 100.0% | 7.174% | fail |
| second relay + first relay | no | 1.16% | 20.48% [18.91%, 22.00%] | 7.69% | ×2.66 | +0.07 [-0.35, +0.47] | 4,595 | 57.8% | 0.283% | fail |
| second relay + second relay | no | 0.52% | 20.63% [18.93%, 22.39%] | 7.69% | ×2.68 | +0.05 [-0.42, +0.49] | 2,075 | 40.0% | 0.145% | fail |
| gatekeeper + first relay | no | 2.12% | 20.35% [19.18%, 21.58%] | 7.69% | ×2.65 | +0.19 [-0.35, +0.72] | 8,393 | 45.2% | 0.000% | pass |
| gatekeeper + second relay | no | 1.90% | 21.21% [19.98%, 22.47%] | 7.69% | ×2.76 | +0.05 [-0.49, +0.58] | 7,525 | 51.3% | 0.226% | fail |
| three or more roles, no destination | no | 0.40% | 20.49% [18.31%, 22.65%] | 7.69% | ×2.66 | +0.13 [-0.90, +1.09] | 1,562 | 49.5% | 0.064% | pass |
| every record the node can select |  | 15.00% | 24.92% [24.08%, 25.81%] | 7.69% | ×3.24 | +4.18 [+3.83, +4.51] | 59,310 | 65.2% | 5.458% | fail |
| first relay held |  | 4.83% | 21.98% [20.89%, 23.08%] | 7.69% | ×2.86 | +1.40 [+1.01, +1.78] | 19,090 | 59.8% | 2.048% | fail |
| no first relay held |  | 95.17% | 21.17% [20.24%, 22.07%] | 7.69% | ×2.75 | +0.42 [+0.27, +0.56] | 376,310 | 47.5% | 0.559% | fail |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.03 [-0.15, +0.10] | 19,770 |
| D or G | +0.47 [+0.34, +0.58] | 39,540 |

#### R100_D60

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 9.53% [9.32%, 9.74%] | 3.85% | ×2.48 [2.42, 2.53] | reference | 99,860 | 16.9% | 0.000% | pass |
| First hop, credential | 9.55% [9.33%, 9.76%] | 3.85% | ×2.48 [2.43, 2.54] | +0.02 [-0.00, +0.04] | 1,997,200 | 15.2% | 0.000% | pass |
| Combined | 10.01% [9.82%, 10.21%] | 3.85% | ×2.60 [2.55, 2.66] | +0.48 [+0.44, +0.53] | 1,997,200 | 27.9% | 0.006% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.70% | 9.50% [9.31%, 9.69%] | 3.85% | ×2.47 | -0.04 [-0.08, +0.00] | 992,595 | 15.4% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.22% | 9.57% [9.36%, 9.79%] | 3.85% | ×2.49 | +0.04 [-0.00, +0.09] | 583,642 | 15.3% | 0.000% | pass |
| destination only | yes | 11.94% | 12.71% [12.49%, 12.93%] | 3.85% | ×3.31 | +3.21 [+3.09, +3.32] | 238,420 | 38.1% | 0.034% | pass |
| credential first relay + content destination | yes | 0.49% | 14.64% [13.93%, 15.36%] | 3.85% | ×3.81 | +4.68 [+4.09, +5.27] | 9,865 | 46.2% | 0.152% | fail |
| content first relay + content destination | yes | 0.51% | 14.24% [13.51%, 14.95%] | 3.85% | ×3.70 | +5.04 [+4.36, +5.70] | 10,148 | 46.4% | 0.049% | pass |
| content first relay + credential destination | yes | 0.53% | 10.17% [9.61%, 10.78%] | 3.85% | ×2.64 | +0.42 [+0.21, +0.63] | 10,522 | 27.6% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 12.66% [12.28%, 13.04%] | 3.85% | ×3.29 | +3.08 [+2.78, +3.39] | 27,999 | 43.7% | 0.232% | fail |
| three or more roles, with a destination | yes | 0.13% | 12.03% [10.74%, 13.41%] | 3.85% | ×3.13 | +2.17 [+1.21, +3.17] | 2,626 | 53.8% | 0.267% | fail |
| second relay + first relay | no | 1.16% | 9.81% [9.44%, 10.18%] | 3.85% | ×2.55 | +0.23 [+0.10, +0.36] | 23,134 | 22.2% | 0.004% | pass |
| second relay + second relay | no | 0.52% | 9.67% [9.10%, 10.29%] | 3.85% | ×2.51 | -0.17 [-0.38, +0.03] | 10,473 | 22.2% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 9.86% [9.52%, 10.18%] | 3.85% | ×2.56 | +0.30 [+0.15, +0.44] | 41,852 | 18.8% | 0.002% | pass |
| gatekeeper + second relay | no | 1.88% | 9.36% [9.04%, 9.68%] | 3.85% | ×2.43 | +0.07 [-0.08, +0.23] | 37,565 | 15.6% | 0.024% | pass |
| three or more roles, no destination | no | 0.42% | 9.58% [8.90%, 10.31%] | 3.85% | ×2.49 | +0.01 [-0.28, +0.32] | 8,359 | 27.4% | 0.036% | pass |
| every record the node can select |  | 15.00% | 12.73% [12.53%, 12.93%] | 3.85% | ×3.31 | +3.20 [+3.10, +3.29] | 299,580 | 38.1% | 0.039% | pass |
| first relay held |  | 4.78% | 10.84% [10.61%, 11.06%] | 3.85% | ×2.82 | +1.25 [+1.12, +1.38] | 95,521 | 32.1% | 0.024% | pass |
| no first relay held |  | 95.22% | 9.97% [9.77%, 10.18%] | 3.85% | ×2.59 | +0.44 [+0.40, +0.48] | 1,901,679 | 27.5% | 0.005% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.02 [-0.02, +0.07] | 99,860 |
| D or G | +0.30 [+0.25, +0.35] | 199,720 |

## Cost per run

| Configuration | Cell | Simulation | Scoring | Shuffle test |
|---|---|---|---|---|
| Main run | R1_D60 | 1.2 s | 23.9 s | 0.1 s |
| Main run | R20_D60 | 0.1 s | 4.2 s | 0.0 s |
| Main run | R100_D60 | 0.2 s | 32.0 s | 0.1 s |
| Every hold off | R1_D60 | 1.1 s | 4.3 s | 0.0 s |
| Every hold off | R20_D60 | 0.1 s | 1.3 s | 0.0 s |
| Every hold off | R100_D60 | 0.2 s | 11.7 s | 0.0 s |
| Credential path sets the record time | R1_D60 | 1.3 s | 18.6 s | 0.0 s |
| Credential path sets the record time | R20_D60 | 0.1 s | 4.2 s | 0.0 s |
| Credential path sets the record time | R100_D60 | 0.2 s | 34.4 s | 0.0 s |
| Content paths set the record time | R1_D60 | 1.1 s | 31.2 s | 0.0 s |
| Content paths set the record time | R20_D60 | 0.1 s | 5.2 s | 0.0 s |
| Content paths set the record time | R100_D60 | 0.2 s | 38.1 s | 0.0 s |
| F content path sets the record time | R1_D60 | 1.0 s | 32.7 s | 0.0 s |
| F content path sets the record time | R20_D60 | 0.1 s | 7.3 s | 0.0 s |
| F content path sets the record time | R100_D60 | 0.2 s | 58.1 s | 0.0 s |

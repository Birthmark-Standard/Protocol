# Tables

Main run: D = 1168.2 s; rates are R / D and 100 / D. Intervals are 95% and resample whole runs. Device named: the vantage names the device behind a registry record. Chance, feasible set: a uniform guess among the devices whose packets could have produced the record. A row with fewer than 50 right or 50 wrong device-level decisions is unstable and shows no estimate.

## In flight

| Configuration | Cell | Real in flight (target) | Decoys in flight (target) | Runs |
|---|---|---|---|---|
| Main run | R1_D100 | 0.99 (1) | 99.73 (100) | 100 |
| Main run | R100_D100 | 98.48 (100) | 99.46 (100) | 100 |
| Main run | R300_D100 | 299.32 (300) | 99.13 (100) | 100 |
| Every hold off | R1_D100 | 0.98 (1) | 98.75 (100) | 100 |
| Every hold off | R100_D100 | 98.86 (100) | 99.46 (100) | 100 |
| Every hold off | R300_D100 | 298.83 (300) | 98.54 (100) | 100 |
| Credential path sets the record time | R1_D100 | 1.00 (1) | 100.14 (100) | 100 |
| Credential path sets the record time | R100_D100 | 99.25 (100) | 100.14 (100) | 100 |
| Credential path sets the record time | R300_D100 | 300.74 (300) | 99.85 (100) | 100 |
| Content paths set the record time | R1_D100 | 1.00 (1) | 100.11 (100) | 100 |
| Content paths set the record time | R100_D100 | 99.05 (100) | 99.53 (100) | 100 |
| Content paths set the record time | R300_D100 | 300.79 (300) | 100.00 (100) | 100 |
| F content path sets the record time | R1_D100 | 0.99 (1) | 100.04 (100) | 100 |
| F content path sets the record time | R100_D100 | 99.75 (100) | 100.23 (100) | 100 |
| F content path sets the record time | R300_D100 | 300.10 (300) | 99.73 (100) | 100 |

## Windows

| Configuration | Longest capture to finalization in the calibration | Warm-up | Scored window | Cool-down |
|---|---|---|---|---|
| Main run | 2316.8 s | 2616.8 s | 3600.0 s | 2616.8 s |
| Every hold off | 37.6 s | 42.4 s | 58.4 s | 42.4 s |
| Credential path sets the record time | 2406.0 s | 2717.5 s | 3738.7 s | 2717.5 s |
| Content paths set the record time | 22673.7 s | 25609.8 s | 35232.7 s | 25609.8 s |
| F content path sets the record time | 22673.7 s | 25609.8 s | 35232.7 s | 25609.8 s |

The scored window at R = 1 is extended until it holds 200 real transactions per run on average.

| Cell | Records scored | Passive observer, device named [95% CI] | Half-width of the interval |
|---|---|---|---|
| R1_D100 | 19,943 | 4.77% [4.28%, 5.29%] | 0.50 points |
| R100_D100 | 30,574 | 2.33% [2.12%, 2.55%] | 0.21 points |
| R300_D100 | 92,714 | 1.39% [1.31%, 1.46%] | 0.07 points |

## Timing (main run, R = 300, the largest cell)

| Stage | Mean | Std dev | Maximum |
|---|---|---|---|
| device, credential channel | 120.0 s | 102.9 s | 360.0 s |
| device, content channels | 240.1 s | 206.9 s | 720.0 s |
| first relay hops (A, D, G) | 60.2 s | 51.4 s | 180.0 s |
| second relay hops (B, E, H) | 300.7 s | 259.2 s | 900.0 s |
| C before CV-1 | 29.9 s | 25.2 s | 90.0 s |
| V before CV-2 | 30.1 s | 25.3 s | 90.0 s |
| C fan-out, per leg | 44.8 s | 30.9 s | 180.0 s |
| gatekeeper hold | 29.9 s | 25.2 s | 90.0 s |
| departure bundling wait | 100.8 s | 90.6 s | 360.0 s |
| F/I pre-match hold | 119.8 s | 103.2 s | 360.0 s |
| post-match lottery | 29.9 s | 25.2 s | 90.0 s |
| registry bundle wait | 59.8 s | 34.6 s | 120.0 s |
| registry posting wait | 58.4 s | 34.6 s | 119.5 s |
| capture to finalization | 1162.7 s | 301.2 s | 2371.1 s |

| Cell | Mean capture to finalization [95% CI] |
|---|---|
| R1_D100 | 1159.1 s [1151.5, 1166.6] |
| R100_D100 | 1162.6 s [1155.7, 1169.7] |
| R300_D100 | 1162.7 s [1155.2, 1170.0] |

## R1_D100: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 4.77% [4.28%, 5.29%] | 1.11% | ×4.28 [3.85, 4.75] | reference | 19,943 | 15.6% | 0.000% | pass |
| First hop, credential | 4.77% [4.27%, 5.25%] | 1.11% | ×4.28 [3.84, 4.72] | -0.00 [-0.03, +0.03] | 398,860 | 11.5% | 0.000% | pass |
| First hop, content | 4.77% [4.27%, 5.27%] | 1.11% | ×4.28 [3.84, 4.73] | -0.00 [-0.03, +0.03] | 398,860 | 11.5% | 0.000% | pass |
| Credential processor | 4.78% [4.28%, 5.29%] | 1.11% | ×4.29 [3.84, 4.75] | +0.01 [-0.01, +0.03] | 339,031 | 11.3% | 0.000% | pass |
| Validator | 5.26% [4.85%, 5.66%] | 1.19% | ×4.42 [4.08, 4.76] | +0.49 [-0.01, +0.94] | 19,943 | 12.7% | 0.000% | pass |
| Gatekeeper | 4.79% [4.31%, 5.29%] | 1.11% | ×4.31 [3.87, 4.76] | +0.03 [-0.07, +0.10] | 59,829 | 12.3% | 0.000% | pass |
| Content server | 5.53% [5.12%, 5.93%] | 1.14% | ×4.86 [4.50, 5.21] | +0.76 [+0.49, +1.01] | 39,886 | 15.0% | 0.000% | pass |
| Combined | 4.85% [4.41%, 5.30%] | 1.12% | ×4.35 [3.95, 4.75] | +0.08 [+0.03, +0.13] | 398,860 | 12.1% | 0.000% | pass |

### R1_D100: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 4.76% [4.30%, 5.24%] | 1.11% | ×4.28 [3.87, 4.71] | -0.00 [-0.03, +0.03] | 362,040 | 11.6% | 0.000% | pass |
| First hop, content | 4.76% [4.28%, 5.26%] | 1.11% | ×4.28 [3.85, 4.73] | -0.00 [-0.03, +0.03] | 362,040 | 11.6% | 0.000% | pass |
| Credential processor | 4.78% [4.33%, 5.27%] | 1.11% | ×4.29 [3.89, 4.73] | +0.01 [-0.01, +0.03] | 319,732 | 11.3% | 0.000% | pass |
| Gatekeeper | 4.74% [4.24%, 5.18%] | 1.11% | ×4.26 [3.81, 4.65] | +0.03 [-0.06, +0.13] | 42,308 | 12.9% | 0.000% | pass |
| Content server | 5.54% [5.13%, 5.97%] | 1.14% | ×4.86 [4.51, 5.24] | +0.74 [+0.46, +1.02] | 31,689 | 17.1% | 0.000% | pass |

### R1_D100: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.80% | 4.77% [4.29%, 5.26%] | 1.11% | ×4.29 | -0.01 [-0.05, +0.03] | 198,630 | 11.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.07% | 4.78% [4.31%, 5.23%] | 1.11% | ×4.29 | +0.03 [-0.02, +0.09] | 115,940 | 12.2% | 0.000% | pass |
| destination only | yes | 11.90% | 5.27% [4.86%, 5.69%] | 1.13% | ×4.67 | +0.53 [+0.34, +0.71] | 47,470 | 14.8% | 0.000% | pass |
| credential first relay + content destination | yes | 0.51% | 5.36% [4.33%, 6.45%] | 1.14% | ×4.71 | +0.68 [-0.20, +1.56] | 2,053 | 22.7% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 6.00% [4.97%, 7.08%] | 1.14% | ×5.28 | +1.19 [+0.25, +2.16] | 2,015 | 30.1% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 5.42% [4.36%, 6.51%] | 1.11% | ×4.87 | -0.14 [-0.37, +0.05] | 2,084 | 22.7% | 0.000% | pass |
| second relay + destination | yes | 1.42% | 5.06% [4.43%, 5.73%] | 1.13% | ×4.48 | +0.51 [+0.04, +0.98] | 5,654 | 23.2% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 1.13% | | | 553 | | | unstable (143 runs needed) |
| second relay + first relay | no | 1.16% | 4.63% [4.06%, 5.27%] | 1.11% | ×4.16 | +0.02 [-0.19, +0.23] | 4,642 | 17.5% | 0.000% | pass |
| second relay + second relay | no | 0.53% | 4.47% [3.48%, 5.54%] | 1.11% | ×4.02 | +0.00 [-0.14, +0.14] | 2,104 | 15.5% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 5.04% [4.35%, 5.77%] | 1.11% | ×4.53 | -0.06 [-0.23, +0.11] | 8,377 | 19.1% | 0.000% | pass |
| gatekeeper + second relay | no | 1.92% | 4.63% [4.07%, 5.22%] | 1.11% | ×4.16 | -0.10 [-0.27, +0.06] | 7,662 | 20.7% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 4.59% [3.52%, 5.65%] | 1.11% | ×4.13 | +0.06 [-0.35, +0.49] | 1,676 | 27.0% | 0.000% | pass |
| every record the node can select |  | 15.00% | 5.30% [4.88%, 5.72%] | 1.13% | ×4.69 | +0.53 [+0.35, +0.71] | 59,829 | 13.6% | 0.000% | pass |
| first relay held |  | 4.81% | 5.12% [4.58%, 5.70%] | 1.12% | ×4.58 | +0.16 [-0.02, +0.32] | 19,171 | 16.1% | 0.000% | pass |
| no first relay held |  | 95.19% | 4.84% [4.35%, 5.32%] | 1.12% | ×4.34 | +0.08 [+0.03, +0.12] | 379,689 | 12.1% | 0.000% | pass |

## R100_D100: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.33% [2.12%, 2.55%] | 0.55% | ×4.23 [3.85, 4.62] | reference | 30,574 | 4.2% | 0.000% | pass |
| First hop, credential | 2.31% [2.10%, 2.52%] | 0.55% | ×4.20 [3.81, 4.58] | -0.02 [-0.04, +0.00] | 611,480 | 2.3% | 0.000% | pass |
| First hop, content | 2.31% [2.10%, 2.51%] | 0.55% | ×4.20 [3.82, 4.55] | -0.02 [-0.04, +0.00] | 611,480 | 2.3% | 0.000% | pass |
| Credential processor | 2.32% [2.11%, 2.54%] | 0.55% | ×4.22 [3.83, 4.61] | -0.01 [-0.02, +0.01] | 519,758 | 2.4% | 0.000% | pass |
| Validator | 2.66% [2.46%, 2.85%] | 0.59% | ×4.50 [4.16, 4.83] | +0.33 [+0.09, +0.55] | 30,574 | 6.7% | 0.000% | pass |
| Gatekeeper | 2.31% [2.11%, 2.52%] | 0.55% | ×4.20 [3.83, 4.58] | -0.02 [-0.06, +0.02] | 91,722 | 3.1% | 0.000% | pass |
| Content server | 2.78% [2.58%, 2.98%] | 0.56% | ×4.93 [4.58, 5.29] | +0.45 [+0.30, +0.60] | 61,148 | 5.4% | 0.000% | pass |
| Combined | 2.35% [2.14%, 2.54%] | 0.55% | ×4.27 [3.89, 4.61] | +0.03 [-0.00, +0.05] | 611,480 | 3.6% | 0.000% | pass |

### R100_D100: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 2.30% [2.10%, 2.51%] | 0.55% | ×4.18 [3.81, 4.56] | -0.02 [-0.04, -0.00] | 555,722 | 2.3% | 0.000% | pass |
| First hop, content | 2.30% [2.10%, 2.51%] | 0.55% | ×4.18 [3.81, 4.57] | -0.02 [-0.04, -0.00] | 555,722 | 2.3% | 0.000% | pass |
| Credential processor | 2.32% [2.11%, 2.54%] | 0.55% | ×4.22 [3.84, 4.61] | -0.01 [-0.02, +0.01] | 490,563 | 2.3% | 0.000% | pass |
| Gatekeeper | 2.25% [2.04%, 2.46%] | 0.55% | ×4.08 [3.70, 4.47] | -0.01 [-0.05, +0.03] | 65,159 | 3.0% | 0.000% | pass |
| Content server | 2.81% [2.60%, 3.01%] | 0.56% | ×4.99 [4.61, 5.33] | +0.46 [+0.31, +0.62] | 48,727 | 5.3% | 0.000% | pass |

### R100_D100: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.67% | 2.32% [2.11%, 2.54%] | 0.55% | ×4.21 | -0.02 [-0.04, +0.00] | 303,698 | 2.7% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.28% | 2.25% [2.06%, 2.46%] | 0.55% | ×4.09 | -0.03 [-0.06, +0.00] | 179,041 | 2.2% | 0.000% | pass |
| destination only | yes | 11.94% | 2.64% [2.44%, 2.84%] | 0.56% | ×4.73 | +0.30 [+0.20, +0.41] | 72,983 | 4.0% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 2.83% [2.29%, 3.43%] | 0.56% | ×5.02 | +0.36 [-0.20, +0.91] | 3,070 | 20.7% | 0.000% | pass |
| content first relay + content destination | yes | 0.52% | 2.49% [1.92%, 3.05%] | 0.56% | ×4.41 | +0.44 [-0.06, +0.90] | 3,176 | 15.7% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 2.47% [1.90%, 3.01%] | 0.55% | ×4.48 | -0.03 [-0.28, +0.22] | 3,203 | 20.1% | 0.000% | pass |
| second relay + destination | yes | 1.39% | 2.51% [2.18%, 2.85%] | 0.56% | ×4.48 | +0.26 [+0.01, +0.51] | 8,501 | 13.0% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.56% | | | 789 | | | unstable (239 runs needed) |
| second relay + first relay | no | 1.16% | 2.38% [1.95%, 2.81%] | 0.55% | ×4.33 | +0.00 [-0.11, +0.11] | 7,094 | 7.6% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 2.26% [1.67%, 2.91%] | 0.55% | ×4.10 | +0.10 [+0.00, +0.22] | 3,101 | 20.7% | 0.000% | pass |
| gatekeeper + first relay | no | 2.08% | 2.50% [2.18%, 2.84%] | 0.55% | ×4.54 | +0.01 [-0.09, +0.09] | 12,708 | 7.8% | 0.000% | pass |
| gatekeeper + second relay | no | 1.90% | 2.53% [2.18%, 2.87%] | 0.55% | ×4.60 | -0.01 [-0.11, +0.10] | 11,613 | 4.7% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 2.40% [1.80%, 3.00%] | 0.55% | ×4.35 | +0.04 [-0.08, +0.17] | 2,503 | 25.0% | 0.040% | pass |
| every record the node can select |  | 15.00% | 2.63% [2.44%, 2.82%] | 0.56% | ×4.69 | +0.30 [+0.19, +0.39] | 91,722 | 4.5% | 0.000% | pass |
| first relay held |  | 4.78% | 2.50% [2.24%, 2.77%] | 0.55% | ×4.52 | +0.09 [-0.01, +0.18] | 29,251 | 5.3% | 0.000% | pass |
| no first relay held |  | 95.22% | 2.35% [2.15%, 2.55%] | 0.55% | ×4.25 | +0.02 [-0.00, +0.05] | 582,229 | 3.6% | 0.000% | pass |

## R300_D100: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 1.39% [1.31%, 1.46%] | 0.28% | ×5.04 [4.77, 5.31] | reference | 92,714 | 2.9% | 0.000% | pass |
| First hop, credential | 1.39% [1.31%, 1.46%] | 0.28% | ×5.04 [4.77, 5.31] | +0.00 [-0.01, +0.01] | 1,854,280 | 2.1% | 0.000% | pass |
| First hop, content | 1.39% [1.32%, 1.46%] | 0.28% | ×5.04 [4.79, 5.31] | +0.00 [-0.01, +0.01] | 1,854,280 | 2.1% | 0.000% | pass |
| Credential processor | 1.38% [1.31%, 1.46%] | 0.28% | ×5.03 [4.76, 5.30] | -0.00 [-0.01, +0.00] | 1,576,138 | 2.1% | 0.000% | pass |
| Validator | 1.52% [1.44%, 1.61%] | 0.30% | ×5.15 [4.87, 5.44] | +0.13 [+0.04, +0.22] | 92,714 | 3.0% | 0.000% | pass |
| Gatekeeper | 1.38% [1.31%, 1.45%] | 0.28% | ×5.01 [4.74, 5.28] | -0.01 [-0.03, +0.01] | 278,142 | 2.6% | 0.000% | pass |
| Content server | 1.64% [1.57%, 1.71%] | 0.28% | ×5.82 [5.57, 6.07] | +0.25 [+0.20, +0.31] | 185,428 | 2.6% | 0.000% | pass |
| Combined | 1.41% [1.34%, 1.48%] | 0.28% | ×5.11 [4.86, 5.36] | +0.02 [+0.01, +0.04] | 1,854,280 | 2.2% | 0.000% | pass |

### R300_D100: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 1.39% [1.31%, 1.46%] | 0.28% | ×5.03 [4.76, 5.30] | +0.00 [-0.01, +0.01] | 1,684,965 | 2.1% | 0.000% | pass |
| First hop, content | 1.39% [1.31%, 1.46%] | 0.28% | ×5.03 [4.76, 5.29] | +0.00 [-0.01, +0.01] | 1,684,965 | 2.1% | 0.000% | pass |
| Credential processor | 1.38% [1.30%, 1.46%] | 0.28% | ×5.02 [4.73, 5.29] | -0.00 [-0.01, +0.00] | 1,487,277 | 2.1% | 0.000% | pass |
| Gatekeeper | 1.38% [1.30%, 1.45%] | 0.28% | ×5.00 [4.73, 5.28] | -0.00 [-0.03, +0.02] | 197,688 | 2.9% | 0.000% | pass |
| Content server | 1.62% [1.54%, 1.70%] | 0.28% | ×5.74 [5.46, 6.04] | +0.24 [+0.17, +0.31] | 147,740 | 2.4% | 0.000% | pass |

### R300_D100: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 1.39% [1.31%, 1.47%] | 0.28% | ×5.05 | -0.00 [-0.01, +0.01] | 921,223 | 2.1% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.26% | 1.37% [1.30%, 1.45%] | 0.28% | ×4.98 | -0.00 [-0.02, +0.02] | 542,608 | 2.5% | 0.000% | pass |
| destination only | yes | 11.93% | 1.52% [1.46%, 1.60%] | 0.28% | ×5.45 | +0.15 [+0.11, +0.19] | 221,134 | 2.7% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 1.83% [1.57%, 2.10%] | 0.28% | ×6.48 | +0.28 [-0.01, +0.55] | 9,197 | 5.9% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 1.61% [1.39%, 1.85%] | 0.28% | ×5.72 | +0.16 [-0.05, +0.38] | 9,549 | 7.4% | 0.000% | pass |
| content first relay + credential destination | yes | 0.53% | 1.43% [1.19%, 1.69%] | 0.28% | ×5.20 | -0.05 [-0.11, +0.01] | 9,839 | 5.6% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 1.63% [1.48%, 1.77%] | 0.28% | ×5.82 | +0.27 [+0.13, +0.42] | 25,995 | 4.4% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.28% | | | 2,428 | | | unstable (122 runs needed) |
| second relay + first relay | no | 1.16% | 1.44% [1.29%, 1.60%] | 0.28% | ×5.22 | +0.04 [-0.01, +0.09] | 21,583 | 3.3% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 1.63% [1.39%, 1.87%] | 0.28% | ×5.90 | -0.02 [-0.06, +0.02] | 9,470 | 7.4% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 1.38% [1.27%, 1.51%] | 0.28% | ×5.02 | -0.01 [-0.05, +0.04] | 39,049 | 3.0% | 0.000% | pass |
| gatekeeper + second relay | no | 1.87% | 1.49% [1.36%, 1.61%] | 0.28% | ×5.40 | +0.03 [-0.01, +0.07] | 34,636 | 3.3% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 1.12% [0.87%, 1.36%] | 0.28% | ×4.08 | -0.04 [-0.14, +0.05] | 7,569 | 7.1% | 0.000% | pass |
| every record the node can select |  | 15.00% | 1.54% [1.48%, 1.61%] | 0.28% | ×5.52 | +0.16 [+0.12, +0.20] | 278,142 | 2.6% | 0.000% | pass |
| first relay held |  | 4.81% | 1.47% [1.38%, 1.56%] | 0.28% | ×5.32 | +0.05 [+0.00, +0.09] | 89,217 | 2.8% | 0.000% | pass |
| no first relay held |  | 95.19% | 1.41% [1.34%, 1.48%] | 0.28% | ×5.10 | +0.02 [+0.01, +0.04] | 1,765,063 | 2.1% | 0.000% | pass |

## Diagnostics

| Cell | Variant | Device named [95% CI] | Chance | Multiple of chance | Posted-time number [95% CI] | Change [95% CI] |
|---|---|---|---|---|---|---|
| R1_D100 | observer, timing evidence off | 3.30% [2.83%, 3.78%] | 1.11% | ×2.96 | 4.77% [4.26%, 5.27%] | n/a |
| R1_D100 | observer, record time at the midpoint | 5.22% [4.74%, 5.70%] | 1.13% | ×4.61 | 4.77% [4.28%, 5.25%] | +0.45 [+0.20, +0.69] |
| R1_D100 | content server, record time at the midpoint | 5.88% [5.51%, 6.28%] | 1.15% | ×5.11 | 5.53% [5.15%, 5.93%] | +0.36 [+0.15, +0.57] |
| R100_D100 | observer, timing evidence off | 1.43% [1.26%, 1.62%] | 0.55% | ×2.60 | 2.33% [2.11%, 2.54%] | n/a |
| R100_D100 | observer, record time at the midpoint | 2.55% [2.35%, 2.75%] | 0.56% | ×4.54 | 2.33% [2.11%, 2.54%] | +0.22 [+0.09, +0.35] |
| R100_D100 | content server, record time at the midpoint | 3.06% [2.87%, 3.26%] | 0.57% | ×5.35 | 2.78% [2.59%, 2.98%] | +0.28 [+0.16, +0.39] |
| R300_D100 | observer, timing evidence off | 0.93% [0.87%, 1.00%] | 0.28% | ×3.38 | 1.39% [1.31%, 1.46%] | n/a |
| R300_D100 | observer, record time at the midpoint | 1.53% [1.45%, 1.61%] | 0.28% | ×5.46 | 1.39% [1.31%, 1.46%] | +0.14 [+0.08, +0.20] |
| R300_D100 | content server, record time at the midpoint | 1.78% [1.70%, 1.86%] | 0.29% | ×6.23 | 1.64% [1.57%, 1.71%] | +0.14 [+0.08, +0.20] |

| Cell | Packet type | Observer submission hit [95% CI] | Random rate | Delay to record time, mean | Std dev |
|---|---|---|---|---|---|
| R1_D100 | credential | 0.43% [0.35%, 0.51%] | 0.17% | 1039.8 s | 302.4 s |
| R1_D100 | F content | 0.44% [0.34%, 0.54%] | 0.17% | 919.3 s | 309.6 s |
| R1_D100 | I content | 0.48% [0.38%, 0.58%] | 0.17% | 918.3 s | 312.3 s |
| R100_D100 | credential | 0.19% [0.14%, 0.24%] | 0.09% | 1043.2 s | 305.6 s |
| R100_D100 | F content | 0.24% [0.18%, 0.29%] | 0.09% | 924.2 s | 312.7 s |
| R100_D100 | I content | 0.24% [0.19%, 0.30%] | 0.09% | 921.8 s | 312.5 s |
| R300_D100 | credential | 0.12% [0.10%, 0.14%] | 0.04% | 1042.7 s | 305.9 s |
| R300_D100 | F content | 0.09% [0.07%, 0.10%] | 0.04% | 921.9 s | 311.4 s |
| R300_D100 | I content | 0.11% [0.09%, 0.13%] | 0.04% | 923.3 s | 313.1 s |

| Cell | Packet | Departure to arrival at its destination, mean | Std dev |
|---|---|---|---|
| R1_D100 | credential (at C) | 358.0 s | 262.9 s |
| R1_D100 | F content (at F) | 357.6 s | 262.0 s |
| R1_D100 | I content (at I) | 357.5 s | 263.3 s |
| R100_D100 | credential (at C) | 359.1 s | 263.0 s |
| R100_D100 | F content (at F) | 358.6 s | 262.7 s |
| R100_D100 | I content (at I) | 360.1 s | 263.4 s |
| R300_D100 | credential (at C) | 360.1 s | 263.5 s |
| R300_D100 | F content (at F) | 361.7 s | 264.6 s |
| R300_D100 | I content (at I) | 361.4 s | 264.4 s |

| Cell | Observer, first half of the window [95% CI] | Second half [95% CI] | Second minus first [95% CI] | Agree |
|---|---|---|---|---|
| R1_D100 | 5.03% [4.30%, 5.71%] | 4.51% [3.84%, 5.18%] | -0.51 [-1.51, +0.52] | yes |
| R100_D100 | 2.14% [1.87%, 2.41%] | 2.52% [2.21%, 2.82%] | +0.38 [-0.01, +0.77] | yes |
| R300_D100 | 1.38% [1.26%, 1.50%] | 1.39% [1.29%, 1.49%] | +0.01 [-0.14, +0.16] | yes |

| Configuration | Cell | Real transactions introduced in the window | Never finalized (quorum timeout) |
|---|---|---|---|
| Main run | R1_D100 | 19,943 | 0 |
| Main run | R100_D100 | 30,574 | 0 |
| Main run | R300_D100 | 92,714 | 0 |
| Every hold off | R1_D100 | 19,917 | 0 |
| Every hold off | R100_D100 | 28,202 | 0 |
| Every hold off | R300_D100 | 85,744 | 0 |
| Credential path sets the record time | R1_D100 | 19,947 | 456 |
| Credential path sets the record time | R100_D100 | 31,590 | 784 |
| Credential path sets the record time | R300_D100 | 95,746 | 2,225 |
| Content paths set the record time | R1_D100 | 19,948 | 0 |
| Content paths set the record time | R100_D100 | 31,955 | 0 |
| Content paths set the record time | R300_D100 | 96,773 | 0 |
| F content path sets the record time | R1_D100 | 19,915 | 0 |
| F content path sets the record time | R100_D100 | 46,418 | 0 |
| F content path sets the record time | R300_D100 | 139,860 | 0 |

| Cell | F and I confirmations set by the match board |
|---|---|
| R1_D100 | 49.8% |
| R100_D100 | 50.1% |
| R300_D100 | 50.0% |

## Packet type revealed

The observer scored as if told each packet's true type, one density per type, on the same records as the pooled observer. It covers the first hop only: no likelihood follows packets across later links. The typed observer can have fewer feasible devices, so both chance rates and both multiples are shown.

| Configuration | Cell | Pooled observer [95% CI] | Chance | Multiple | Told the type [95% CI] | Chance | Multiple | Lead over pooled [95% CI] | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Main run | R1_D100 | 4.77% [4.28%, 5.27%] | 1.11% | ×4.28 | 4.77% [4.31%, 5.25%] | 1.13% | ×4.24 | +0.00 [-0.11, +0.11] | 16.2% | 0.000% | pass |
| Main run | R100_D100 | 2.33% [2.12%, 2.55%] | 0.55% | ×4.23 | 2.26% [2.05%, 2.47%] | 0.56% | ×4.06 | -0.07 [-0.14, +0.01] | 4.2% | 0.000% | pass |
| Main run | R300_D100 | 1.39% [1.31%, 1.46%] | 0.28% | ×5.04 | 1.41% [1.32%, 1.48%] | 0.28% | ×5.04 | +0.02 [-0.01, +0.05] | 2.5% | 0.000% | pass |
| Every hold off | R1_D100 | 1.49% [1.26%, 1.71%] | 0.55% | ×2.72 | 1.49% [1.26%, 1.71%] | 0.55% | ×2.71 | -0.01 [-0.02, +0.00] | 5.7% | 0.025% | pass |
| Every hold off | R100_D100 | 0.85% [0.74%, 0.95%] | 0.28% | ×3.04 | 0.85% [0.74%, 0.96%] | 0.28% | ×3.04 | +0.00 [+0.00, +0.00] | 3.1% | 0.000% | pass |
| Every hold off | R300_D100 | 0.46% [0.43%, 0.50%] | 0.14% | ×3.34 | 0.46% [0.43%, 0.50%] | 0.14% | ×3.34 | +0.00 [+0.00, +0.00] | 1.5% | 0.000% | pass |
| Credential path sets the record time | R1_D100 | 4.66% [4.27%, 5.06%] | 1.10% | ×4.23 | 4.69% [4.27%, 5.09%] | 1.12% | ×4.18 | +0.04 [-0.09, +0.16] | 10.4% | 0.000% | pass |
| Credential path sets the record time | R100_D100 | 2.26% [2.03%, 2.48%] | 0.55% | ×4.11 | 2.25% [2.03%, 2.49%] | 0.56% | ×4.02 | -0.00 [-0.07, +0.06] | 4.2% | 0.000% | pass |
| Credential path sets the record time | R300_D100 | 1.34% [1.25%, 1.42%] | 0.27% | ×4.89 | 1.31% [1.23%, 1.39%] | 0.28% | ×4.67 | -0.03 [-0.07, +0.00] | 2.2% | 0.000% | pass |
| Content paths set the record time | R1_D100 | 10.92% [10.40%, 11.43%] | 1.04% | ×10.51 | 14.94% [14.40%, 15.46%] | 1.04% | ×14.36 | +4.02 [+3.58, +4.47] | 37.4% | 0.000% | pass |
| Content paths set the record time | R100_D100 | 11.79% [11.24%, 12.31%] | 4.55% | ×2.59 | 14.38% [13.84%, 14.90%] | 4.55% | ×3.16 | +2.60 [+2.26, +2.94] | 30.0% | 0.016% | pass |
| Content paths set the record time | R300_D100 | 6.78% [6.60%, 6.97%] | 2.27% | ×2.98 | 8.06% [7.88%, 8.25%] | 2.27% | ×3.55 | +1.28 [+1.11, +1.45] | 15.9% | 0.000% | pass |
| F content path sets the record time | R1_D100 | 5.38% [5.01%, 5.76%] | 1.01% | ×5.33 | 16.35% [15.79%, 16.91%] | 1.04% | ×15.68 | +10.97 [+10.38, +11.52] | 43.1% | 0.000% | pass |
| F content path sets the record time | R100_D100 | 7.52% [7.20%, 7.85%] | 3.12% | ×2.41 | 13.87% [13.49%, 14.24%] | 3.12% | ×4.44 | +6.36 [+6.01, +6.70] | 27.8% | 0.000% | pass |
| F content path sets the record time | R300_D100 | 4.05% [3.93%, 4.17%] | 1.56% | ×2.59 | 7.99% [7.85%, 8.12%] | 1.56% | ×5.11 | +3.94 [+3.79, +4.08] | 15.6% | 0.000% | pass |

| Configuration | Cell | Packet type | Pooled observer submission hit [95% CI] | Told the type [95% CI] | Random rate, pooled | Random rate, told the type |
|---|---|---|---|---|---|---|
| Main run | R1_D100 | credential | 0.43% [0.35%, 0.51%] | 0.61% [0.50%, 0.71%] | 0.17% | 0.18% |
| Main run | R1_D100 | F content | 0.44% [0.34%, 0.54%] | 0.39% [0.31%, 0.46%] | 0.17% | 0.18% |
| Main run | R1_D100 | I content | 0.48% [0.38%, 0.58%] | 0.45% [0.36%, 0.52%] | 0.17% | 0.18% |
| Main run | R100_D100 | credential | 0.19% [0.14%, 0.24%] | 0.27% [0.21%, 0.33%] | 0.09% | 0.09% |
| Main run | R100_D100 | F content | 0.24% [0.18%, 0.29%] | 0.13% [0.09%, 0.18%] | 0.09% | 0.09% |
| Main run | R100_D100 | I content | 0.24% [0.19%, 0.30%] | 0.32% [0.26%, 0.39%] | 0.09% | 0.09% |
| Main run | R300_D100 | credential | 0.12% [0.10%, 0.14%] | 0.07% [0.05%, 0.09%] | 0.04% | 0.04% |
| Main run | R300_D100 | F content | 0.09% [0.07%, 0.10%] | 0.05% [0.04%, 0.07%] | 0.04% | 0.04% |
| Main run | R300_D100 | I content | 0.11% [0.09%, 0.13%] | 0.21% [0.19%, 0.25%] | 0.04% | 0.04% |
| Every hold off | R1_D100 | credential | 0.32% [0.22%, 0.42%] | 0.48% [0.37%, 0.61%] | 0.18% | 0.18% |
| Every hold off | R1_D100 | F content | 0.36% [0.28%, 0.45%] | 0.51% [0.42%, 0.61%] | 0.18% | 0.18% |
| Every hold off | R1_D100 | I content | 0.32% [0.24%, 0.40%] | 0.02% [0.00%, 0.04%] | 0.18% | 0.18% |
| Every hold off | R100_D100 | credential | 0.12% [0.08%, 0.17%] | 0.21% [0.16%, 0.25%] | 0.09% | 0.09% |
| Every hold off | R100_D100 | F content | 0.21% [0.16%, 0.26%] | 0.30% [0.24%, 0.37%] | 0.09% | 0.09% |
| Every hold off | R100_D100 | I content | 0.18% [0.13%, 0.22%] | 0.00% [0.00%, 0.00%] | 0.09% | 0.09% |
| Every hold off | R300_D100 | credential | 0.09% [0.07%, 0.11%] | 0.14% [0.11%, 0.16%] | 0.05% | 0.05% |
| Every hold off | R300_D100 | F content | 0.09% [0.07%, 0.11%] | 0.14% [0.12%, 0.16%] | 0.05% | 0.05% |
| Every hold off | R300_D100 | I content | 0.09% [0.07%, 0.11%] | 0.00% [0.00%, 0.00%] | 0.05% | 0.05% |
| Credential path sets the record time | R1_D100 | credential | 0.81% [0.69%, 0.93%] | 0.62% [0.52%, 0.73%] | 0.15% | 0.16% |
| Credential path sets the record time | R1_D100 | F content | 0.42% [0.33%, 0.51%] | 0.40% [0.31%, 0.48%] | 0.15% | 0.16% |
| Credential path sets the record time | R1_D100 | I content | 0.46% [0.36%, 0.55%] | 0.62% [0.51%, 0.73%] | 0.15% | 0.16% |
| Credential path sets the record time | R100_D100 | credential | 0.40% [0.33%, 0.47%] | 0.18% [0.13%, 0.23%] | 0.08% | 0.08% |
| Credential path sets the record time | R100_D100 | F content | 0.30% [0.24%, 0.36%] | 0.26% [0.20%, 0.32%] | 0.08% | 0.08% |
| Credential path sets the record time | R100_D100 | I content | 0.19% [0.14%, 0.24%] | 0.40% [0.33%, 0.47%] | 0.08% | 0.08% |
| Credential path sets the record time | R300_D100 | credential | 0.24% [0.21%, 0.28%] | 0.04% [0.03%, 0.05%] | 0.04% | 0.04% |
| Credential path sets the record time | R300_D100 | F content | 0.09% [0.07%, 0.11%] | 0.15% [0.12%, 0.18%] | 0.04% | 0.04% |
| Credential path sets the record time | R300_D100 | I content | 0.09% [0.08%, 0.11%] | 0.23% [0.20%, 0.27%] | 0.04% | 0.04% |
| Content paths set the record time | R1_D100 | credential | 0.00% [0.00%, 0.00%] | 0.00% [0.00%, 0.00%] | 0.16% | 0.16% |
| Content paths set the record time | R1_D100 | F content | 3.69% [3.41%, 3.99%] | 5.36% [5.05%, 5.69%] | 0.16% | 0.16% |
| Content paths set the record time | R1_D100 | I content | 3.78% [3.55%, 4.03%] | 5.67% [5.36%, 5.98%] | 0.16% | 0.16% |
| Content paths set the record time | R100_D100 | credential | 0.00% [0.00%, 0.00%] | 0.00% [0.00%, 0.00%] | 0.08% | 0.08% |
| Content paths set the record time | R100_D100 | F content | 2.01% [1.86%, 2.16%] | 3.14% [2.95%, 3.33%] | 0.08% | 0.08% |
| Content paths set the record time | R100_D100 | I content | 2.00% [1.87%, 2.14%] | 2.75% [2.57%, 2.93%] | 0.08% | 0.08% |
| Content paths set the record time | R300_D100 | credential | 0.00% [0.00%, 0.00%] | 0.00% [0.00%, 0.00%] | 0.04% | 0.04% |
| Content paths set the record time | R300_D100 | F content | 0.97% [0.91%, 1.04%] | 1.93% [1.84%, 2.02%] | 0.04% | 0.04% |
| Content paths set the record time | R300_D100 | I content | 1.01% [0.95%, 1.06%] | 0.98% [0.92%, 1.04%] | 0.04% | 0.04% |
| F content path sets the record time | R1_D100 | credential | 0.01% [0.00%, 0.03%] | 0.00% [0.00%, 0.00%] | 0.11% | 0.16% |
| F content path sets the record time | R1_D100 | F content | 7.80% [7.48%, 8.16%] | 14.97% [14.52%, 15.42%] | 0.11% | 0.16% |
| F content path sets the record time | R1_D100 | I content | 0.00% [0.00%, 0.00%] | 0.00% [0.00%, 0.00%] | 0.11% | 0.16% |
| F content path sets the record time | R100_D100 | credential | 0.00% [0.00%, 0.01%] | 0.00% [0.00%, 0.00%] | 0.06% | 0.08% |
| F content path sets the record time | R100_D100 | F content | 3.93% [3.78%, 4.08%] | 7.72% [7.49%, 7.99%] | 0.06% | 0.08% |
| F content path sets the record time | R100_D100 | I content | 0.00% [0.00%, 0.01%] | 0.00% [0.00%, 0.00%] | 0.06% | 0.08% |
| F content path sets the record time | R300_D100 | credential | 0.00% [0.00%, 0.01%] | 0.00% [0.00%, 0.00%] | 0.03% | 0.04% |
| F content path sets the record time | R300_D100 | F content | 1.94% [1.87%, 2.02%] | 3.86% [3.76%, 3.96%] | 0.03% | 0.04% |
| F content path sets the record time | R300_D100 | I content | 0.00% [0.00%, 0.00%] | 0.00% [0.00%, 0.00%] | 0.03% | 0.04% |

## Label shuffle

| Configuration | Cell | Vantage | Shuffled accuracy [95% CI] | Chance | Pass |
|---|---|---|---|---|---|
| Main run | R1_D100 | Passive observer | 1.06% [0.88%, 1.25%] | 0.99% | pass |
| Main run | R1_D100 | First hop | 1.07% [0.90%, 1.26%] | 0.99% | pass |
| Main run | R1_D100 | Credential processor | 1.07% [0.90%, 1.26%] | 0.99% | pass |
| Main run | R1_D100 | Validator | 1.00% [0.85%, 1.17%] | 0.99% | pass |
| Main run | R1_D100 | Gatekeeper | 1.09% [0.91%, 1.29%] | 0.99% | pass |
| Main run | R1_D100 | Content server | 1.04% [0.89%, 1.20%] | 0.99% | pass |
| Main run | R1_D100 | Combined | 1.08% [0.90%, 1.26%] | 0.99% | pass |
| Main run | R100_D100 | Passive observer | 0.45% [0.38%, 0.53%] | 0.48% | pass |
| Main run | R100_D100 | First hop | 0.45% [0.38%, 0.53%] | 0.48% | pass |
| Main run | R100_D100 | Credential processor | 0.45% [0.38%, 0.53%] | 0.48% | pass |
| Main run | R100_D100 | Validator | 0.52% [0.43%, 0.61%] | 0.48% | pass |
| Main run | R100_D100 | Gatekeeper | 0.44% [0.37%, 0.52%] | 0.48% | pass |
| Main run | R100_D100 | Content server | 0.45% [0.38%, 0.52%] | 0.48% | pass |
| Main run | R100_D100 | Combined | 0.45% [0.38%, 0.53%] | 0.48% | pass |
| Main run | R300_D100 | Passive observer | 0.25% [0.21%, 0.28%] | 0.24% | pass |
| Main run | R300_D100 | First hop | 0.25% [0.21%, 0.28%] | 0.24% | pass |
| Main run | R300_D100 | Credential processor | 0.25% [0.21%, 0.29%] | 0.24% | pass |
| Main run | R300_D100 | Validator | 0.25% [0.21%, 0.28%] | 0.24% | pass |
| Main run | R300_D100 | Gatekeeper | 0.25% [0.21%, 0.28%] | 0.24% | pass |
| Main run | R300_D100 | Content server | 0.23% [0.21%, 0.26%] | 0.24% | pass |
| Main run | R300_D100 | Combined | 0.25% [0.21%, 0.28%] | 0.24% | pass |
| Every hold off | R1_D100 | Passive observer | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | First hop | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | Credential processor | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | Validator | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | Gatekeeper | 0.02% [0.01%, 0.03%] | 0.02% | pass |
| Every hold off | R1_D100 | Content server | 0.01% [0.00%, 0.02%] | 0.02% | fail |
| Every hold off | R1_D100 | Combined | 0.02% [0.01%, 0.04%] | 0.02% | pass |
| Every hold off | R100_D100 | Passive observer | 0.07% [0.04%, 0.10%] | 0.08% | pass |
| Every hold off | R100_D100 | First hop | 0.07% [0.04%, 0.10%] | 0.08% | pass |
| Every hold off | R100_D100 | Credential processor | 0.07% [0.04%, 0.10%] | 0.08% | pass |
| Every hold off | R100_D100 | Validator | 0.07% [0.04%, 0.10%] | 0.08% | pass |
| Every hold off | R100_D100 | Gatekeeper | 0.09% [0.06%, 0.12%] | 0.08% | pass |
| Every hold off | R100_D100 | Content server | 0.10% [0.07%, 0.14%] | 0.08% | pass |
| Every hold off | R100_D100 | Combined | 0.07% [0.05%, 0.10%] | 0.08% | pass |
| Every hold off | R300_D100 | Passive observer | 0.04% [0.02%, 0.05%] | 0.04% | pass |
| Every hold off | R300_D100 | First hop | 0.04% [0.03%, 0.05%] | 0.04% | pass |
| Every hold off | R300_D100 | Credential processor | 0.04% [0.03%, 0.05%] | 0.04% | pass |
| Every hold off | R300_D100 | Validator | 0.04% [0.03%, 0.05%] | 0.04% | pass |
| Every hold off | R300_D100 | Gatekeeper | 0.03% [0.02%, 0.04%] | 0.04% | pass |
| Every hold off | R300_D100 | Content server | 0.03% [0.02%, 0.04%] | 0.04% | pass |
| Every hold off | R300_D100 | Combined | 0.04% [0.03%, 0.05%] | 0.04% | pass |
| Credential path sets the record time | R1_D100 | Passive observer | 0.92% [0.73%, 1.14%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | First hop | 0.94% [0.74%, 1.15%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | Credential processor | 0.93% [0.73%, 1.15%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | Validator | 0.92% [0.74%, 1.13%] | 1.00% | pass |
| Credential path sets the record time | R1_D100 | Gatekeeper | 0.95% [0.78%, 1.15%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | Content server | 1.08% [0.91%, 1.28%] | 1.00% | pass |
| Credential path sets the record time | R1_D100 | Combined | 0.96% [0.77%, 1.16%] | 0.99% | pass |
| Credential path sets the record time | R100_D100 | Passive observer | 0.45% [0.38%, 0.52%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | First hop | 0.46% [0.39%, 0.53%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Credential processor | 0.46% [0.39%, 0.53%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Validator | 0.45% [0.37%, 0.53%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Gatekeeper | 0.46% [0.39%, 0.52%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Content server | 0.48% [0.42%, 0.54%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Combined | 0.46% [0.40%, 0.53%] | 0.49% | pass |
| Credential path sets the record time | R300_D100 | Passive observer | 0.26% [0.23%, 0.29%] | 0.24% | pass |
| Credential path sets the record time | R300_D100 | First hop | 0.25% [0.23%, 0.29%] | 0.24% | pass |
| Credential path sets the record time | R300_D100 | Credential processor | 0.26% [0.23%, 0.29%] | 0.24% | pass |
| Credential path sets the record time | R300_D100 | Validator | 0.23% [0.20%, 0.27%] | 0.24% | pass |
| Credential path sets the record time | R300_D100 | Gatekeeper | 0.25% [0.22%, 0.27%] | 0.24% | pass |
| Credential path sets the record time | R300_D100 | Content server | 0.27% [0.24%, 0.30%] | 0.24% | pass |
| Credential path sets the record time | R300_D100 | Combined | 0.25% [0.23%, 0.28%] | 0.24% | pass |
| Content paths set the record time | R1_D100 | Passive observer | 0.88% [0.73%, 1.02%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | First hop | 0.88% [0.74%, 1.02%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | Credential processor | 0.88% [0.74%, 1.03%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | Validator | 1.09% [0.93%, 1.26%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | Gatekeeper | 0.82% [0.69%, 0.95%] | 0.99% | fail |
| Content paths set the record time | R1_D100 | Content server | 0.78% [0.68%, 0.90%] | 0.99% | fail |
| Content paths set the record time | R1_D100 | Combined | 0.87% [0.73%, 1.01%] | 0.99% | pass |
| Content paths set the record time | R100_D100 | Passive observer | 4.67% [4.36%, 4.97%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | First hop | 4.66% [4.38%, 4.96%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Credential processor | 4.65% [4.35%, 4.94%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Validator | 4.86% [4.46%, 5.28%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Gatekeeper | 4.66% [4.36%, 4.96%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Content server | 4.64% [4.37%, 4.91%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Combined | 4.65% [4.37%, 4.96%] | 4.55% | pass |
| Content paths set the record time | R300_D100 | Passive observer | 2.23% [2.14%, 2.33%] | 2.27% | pass |
| Content paths set the record time | R300_D100 | First hop | 2.23% [2.14%, 2.33%] | 2.27% | pass |
| Content paths set the record time | R300_D100 | Credential processor | 2.23% [2.13%, 2.33%] | 2.27% | pass |
| Content paths set the record time | R300_D100 | Validator | 2.23% [2.11%, 2.35%] | 2.27% | pass |
| Content paths set the record time | R300_D100 | Gatekeeper | 2.24% [2.14%, 2.34%] | 2.27% | pass |
| Content paths set the record time | R300_D100 | Content server | 2.23% [2.13%, 2.33%] | 2.27% | pass |
| Content paths set the record time | R300_D100 | Combined | 2.23% [2.14%, 2.33%] | 2.27% | pass |
| F content path sets the record time | R1_D100 | Passive observer | 1.06% [0.86%, 1.29%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | First hop | 1.06% [0.87%, 1.28%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Credential processor | 1.07% [0.87%, 1.29%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Validator | 1.02% [0.85%, 1.21%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Gatekeeper | 1.05% [0.84%, 1.28%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Content server | 1.39% [0.93%, 1.97%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Combined | 1.10% [0.90%, 1.37%] | 0.99% | pass |
| F content path sets the record time | R100_D100 | Passive observer | 3.07% [2.86%, 3.28%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | First hop | 3.07% [2.87%, 3.27%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Credential processor | 3.07% [2.86%, 3.27%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Validator | 3.17% [2.94%, 3.40%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Gatekeeper | 3.11% [2.92%, 3.32%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Content server | 3.19% [3.00%, 3.39%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Combined | 3.09% [2.90%, 3.29%] | 3.12% | pass |
| F content path sets the record time | R300_D100 | Passive observer | 1.55% [1.49%, 1.62%] | 1.56% | pass |
| F content path sets the record time | R300_D100 | First hop | 1.55% [1.50%, 1.62%] | 1.56% | pass |
| F content path sets the record time | R300_D100 | Credential processor | 1.55% [1.49%, 1.62%] | 1.56% | pass |
| F content path sets the record time | R300_D100 | Validator | 1.56% [1.48%, 1.63%] | 1.56% | pass |
| F content path sets the record time | R300_D100 | Gatekeeper | 1.57% [1.50%, 1.63%] | 1.56% | pass |
| F content path sets the record time | R300_D100 | Content server | 1.54% [1.48%, 1.59%] | 1.56% | pass |
| F content path sets the record time | R300_D100 | Combined | 1.55% [1.49%, 1.61%] | 1.56% | pass |

### Shuffle test (observer)

| Cell | Shuffle mismatches | Feasible-count mismatches | Exact expected accuracy | Exact expected chance | Mean accuracy over permutations (sd) | Mean chance over permutations | Interval coverage | Scored accuracy | Scored percentile |
|---|---|---|---|---|---|---|---|---|---|
| R1_D100 | 1 | 0 | 0.990% | 0.990% | 0.984% (0.092%) | 0.990% | 94.0% | 0.862% | 5.5% |
| R100_D100 | 0 | 0 | 0.486% | 0.486% | 0.482% (0.043%) | 0.486% | 95.0% | 0.530% | 87.5% |
| R300_D100 | 0 | 0 | 0.243% | 0.243% | 0.241% (0.017%) | 0.243% | 93.0% | 0.228% | 21.0% |

## Controls

### Every hold off

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 1.49% [1.27%, 1.73%] | 0.55% | ×2.72 [2.32, 3.15] | reference | 19,917 | 5.7% | 0.025% | pass |
| First hop, credential | 1.49% [1.27%, 1.73%] | 0.55% | ×2.72 [2.32, 3.15] | +0.00 [+0.00, +0.00] | 398,340 | 3.0% | 0.030% | pass |
| Combined | 2.57% [2.37%, 2.78%] | 0.70% | ×3.67 [3.37, 3.95] | +1.08 [+0.99, +1.17] | 398,340 | 40.3% | 0.148% | fail |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.74% | 1.49% [1.26%, 1.73%] | 0.55% | ×2.71 | +0.00 [+0.00, +0.00] | 198,154 | 3.3% | 0.030% | pass |
| one relay or gatekeeper role | no | 29.13% | 1.49% [1.27%, 1.72%] | 0.55% | ×2.72 | -0.01 [-0.06, +0.04] | 116,056 | 4.6% | 0.000% | pass |
| destination only | yes | 11.93% | 8.74% [8.15%, 9.35%] | 1.58% | ×5.54 | +7.22 [+6.61, +7.84] | 47,515 | 52.9% | 0.810% | fail |
| credential first relay + content destination | yes | 0.50% | 12.10% [10.42%, 13.87%] | 2.09% | ×5.78 | +10.75 [+9.16, +12.42] | 2,009 | 78.1% | 4.430% | fail |
| content first relay + content destination | yes | 0.50% | 11.94% [10.39%, 13.43%] | 2.07% | ×5.76 | +11.04 [+9.52, +12.67] | 2,001 | 81.9% | 2.949% | fail |
| content first relay + credential destination | yes | 0.53% | unstable | 0.55% | | | 2,094 | | | unstable (152 runs needed) |
| second relay + destination | yes | 1.41% | 8.78% [8.01%, 9.57%] | 1.58% | ×5.57 | +7.25 [+6.41, +8.08] | 5,616 | 64.3% | 2.083% | fail |
| three or more roles, with a destination | yes | 0.13% | unstable | 1.56% | | | 516 | | | unstable (162 runs needed) |
| second relay + first relay | no | 1.16% | 1.62% [1.25%, 2.01%] | 0.55% | ×2.96 | +0.00 [+0.00, +0.00] | 4,632 | 14.5% | 0.022% | pass |
| second relay + second relay | no | 0.53% | unstable | 0.55% | | | 2,101 | | | unstable (173 runs needed) |
| gatekeeper + first relay | no | 2.10% | 1.69% [1.39%, 2.02%] | 0.55% | ×3.09 | +0.11 [-0.13, +0.36] | 8,348 | 8.4% | 0.000% | pass |
| gatekeeper + second relay | no | 1.92% | 1.49% [1.20%, 1.80%] | 0.55% | ×2.72 | +0.14 [-0.13, +0.42] | 7,646 | 7.1% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.55% | | | 1,652 | | | unstable (218 runs needed) |
| every record the node can select |  | 15.00% | 8.69% [8.12%, 9.23%] | 1.57% | ×5.52 | +7.20 [+6.62, +7.79] | 59,751 | 53.7% | 0.989% | fail |
| first relay held |  | 4.79% | 3.83% [3.52%, 4.14%] | 0.87% | ×4.40 | +2.34 [+2.05, +2.63] | 19,084 | 50.5% | 0.582% | fail |
| no first relay held |  | 95.21% | 2.51% [2.30%, 2.73%] | 0.69% | ×3.62 | +1.02 [+0.93, +1.10] | 379,256 | 40.2% | 0.139% | fail |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 19,917 |
| D or G | +0.00 [+0.00, +0.00] | 39,834 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 0.85% [0.73%, 0.95%] | 0.28% | ×3.04 [2.64, 3.43] | reference | 28,202 | 3.1% | 0.000% | pass |
| First hop, credential | 0.85% [0.74%, 0.96%] | 0.28% | ×3.04 [2.65, 3.44] | +0.00 [+0.00, +0.00] | 564,040 | 1.4% | 0.000% | pass |
| Combined | 1.52% [1.41%, 1.63%] | 0.36% | ×4.25 [3.94, 4.54] | +0.67 [+0.62, +0.72] | 564,040 | 22.3% | 0.003% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 0.85% [0.74%, 0.96%] | 0.28% | ×3.06 | +0.00 [+0.00, +0.00] | 280,240 | 1.5% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.25% | 0.86% [0.75%, 0.96%] | 0.28% | ×3.09 | +0.01 [-0.01, +0.04] | 164,955 | 2.4% | 0.000% | pass |
| destination only | yes | 11.94% | 5.27% [4.93%, 5.62%] | 0.81% | ×6.49 | +4.47 [+4.12, +4.84] | 67,347 | 29.8% | 0.013% | pass |
| credential first relay + content destination | yes | 0.49% | 8.00% [6.79%, 9.18%] | 1.10% | ×7.26 | +6.66 [+5.49, +7.91] | 2,762 | 67.4% | 1.050% | fail |
| content first relay + content destination | yes | 0.50% | 7.52% [6.51%, 8.62%] | 1.06% | ×7.07 | +6.45 [+5.44, +7.50] | 2,805 | 54.2% | 0.178% | fail |
| content first relay + credential destination | yes | 0.53% | unstable | 0.28% | | | 2,999 | | | unstable (179 runs needed) |
| second relay + destination | yes | 1.41% | 5.43% [4.89%, 5.95%] | 0.80% | ×6.79 | +4.43 [+3.90, +4.97] | 7,960 | 43.4% | 0.013% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.84% | | | 733 | | | unstable (112 runs needed) |
| second relay + first relay | no | 1.16% | 0.79% [0.57%, 1.02%] | 0.28% | ×2.85 | +0.00 [+0.00, +0.00] | 6,552 | 5.5% | 0.000% | pass |
| second relay + second relay | no | 0.51% | unstable | 0.28% | | | 2,887 | | | unstable (228 runs needed) |
| gatekeeper + first relay | no | 2.12% | 0.70% [0.54%, 0.85%] | 0.28% | ×2.50 | +0.00 [-0.13, +0.13] | 11,932 | 5.9% | 0.008% | pass |
| gatekeeper + second relay | no | 1.87% | 1.00% [0.81%, 1.22%] | 0.28% | ×3.58 | +0.09 [-0.08, +0.24] | 10,526 | 6.7% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | unstable | 0.28% | | | 2,342 | | | unstable (218 runs needed) |
| every record the node can select |  | 15.00% | 5.30% [4.97%, 5.62%] | 0.81% | ×6.55 | +4.45 [+4.13, +4.78] | 84,606 | 31.3% | 0.015% | pass |
| first relay held |  | 4.80% | 2.20% [1.98%, 2.41%] | 0.44% | ×4.95 | +1.35 [+1.15, +1.56] | 27,050 | 32.2% | 0.026% | pass |
| no first relay held |  | 95.20% | 1.49% [1.38%, 1.59%] | 0.35% | ×4.20 | +0.64 [+0.59, +0.69] | 536,990 | 21.5% | 0.003% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 28,202 |
| D or G | +0.00 [+0.00, +0.00] | 56,404 |

#### R300_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 0.46% [0.43%, 0.50%] | 0.14% | ×3.34 [3.10, 3.59] | reference | 85,744 | 1.5% | 0.000% | pass |
| First hop, credential | 0.46% [0.43%, 0.50%] | 0.14% | ×3.34 [3.09, 3.62] | +0.00 [+0.00, +0.00] | 1,714,880 | 0.8% | 0.000% | pass |
| Combined | 0.76% [0.72%, 0.80%] | 0.18% | ×4.32 [4.11, 4.53] | +0.30 [+0.28, +0.33] | 1,714,880 | 10.7% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.69% | 0.46% [0.42%, 0.49%] | 0.14% | ×3.32 | +0.00 [+0.00, +0.00] | 852,056 | 0.8% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.25% | 0.47% [0.44%, 0.50%] | 0.14% | ×3.41 | -0.00 [-0.01, +0.01] | 501,628 | 0.8% | 0.000% | pass |
| destination only | yes | 11.93% | 2.47% [2.30%, 2.64%] | 0.39% | ×6.28 | +2.00 [+1.82, +2.17] | 204,521 | 14.0% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 3.37% [2.93%, 3.80%] | 0.52% | ×6.47 | +2.76 [+2.35, +3.17] | 8,581 | 20.1% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 3.52% [3.03%, 4.00%] | 0.52% | ×6.73 | +3.20 [+2.75, +3.69] | 8,754 | 22.3% | 0.011% | pass |
| content first relay + credential destination | yes | 0.53% | unstable | 0.14% | | | 9,028 | | | unstable (143 runs needed) |
| second relay + destination | yes | 1.41% | 2.39% [2.17%, 2.62%] | 0.39% | ×6.06 | +1.96 [+1.72, +2.19] | 24,132 | 19.5% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 2.66% [2.05%, 3.35%] | 0.40% | ×6.61 | +1.99 [+1.31, +2.68] | 2,216 | 38.5% | 0.000% | pass |
| second relay + first relay | no | 1.16% | 0.45% [0.37%, 0.55%] | 0.14% | ×3.28 | +0.00 [+0.00, +0.00] | 19,890 | 3.6% | 0.000% | pass |
| second relay + second relay | no | 0.52% | unstable | 0.14% | | | 8,875 | | | unstable (136 runs needed) |
| gatekeeper + first relay | no | 2.10% | 0.49% [0.42%, 0.56%] | 0.14% | ×3.54 | +0.03 [-0.03, +0.08] | 36,044 | 2.8% | 0.000% | pass |
| gatekeeper + second relay | no | 1.87% | 0.49% [0.41%, 0.58%] | 0.14% | ×3.58 | +0.03 [-0.04, +0.10] | 32,127 | 2.7% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.14% | | | 7,028 | | | unstable (162 runs needed) |
| every record the node can select |  | 15.00% | 2.45% [2.28%, 2.62%] | 0.39% | ×6.25 | +1.99 [+1.82, +2.16] | 257,232 | 14.1% | 0.000% | pass |
| first relay held |  | 4.80% | 1.09% [1.01%, 1.18%] | 0.22% | ×4.99 | +0.64 [+0.57, +0.72] | 82,297 | 13.4% | 0.001% | pass |
| no first relay held |  | 95.20% | 0.75% [0.71%, 0.78%] | 0.17% | ×4.28 | +0.28 [+0.26, +0.31] | 1,632,583 | 10.4% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 85,744 |
| D or G | +0.00 [+0.00, +0.00] | 171,488 |

### Credential path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 96.0% |
| R100_D100 | 96.0% |
| R300_D100 | 96.0% |

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 4.66% [4.23%, 5.07%] | 1.10% | ×4.23 [3.84, 4.60] | reference | 19,491 | 10.4% | 0.000% | pass |
| First hop, credential | 4.66% [4.24%, 5.07%] | 1.10% | ×4.23 [3.84, 4.60] | +0.01 [-0.02, +0.03] | 389,820 | 7.0% | 0.000% | pass |
| Combined | 4.80% [4.40%, 5.18%] | 1.13% | ×4.26 [3.91, 4.60] | +0.14 [+0.08, +0.20] | 389,820 | 10.3% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.76% | 4.65% [4.24%, 5.07%] | 1.10% | ×4.22 | -0.01 [-0.05, +0.03] | 193,969 | 7.1% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.12% | 4.62% [4.23%, 5.02%] | 1.10% | ×4.19 | -0.03 [-0.10, +0.05] | 113,510 | 8.5% | 0.000% | pass |
| destination only | yes | 11.93% | 5.69% [5.31%, 6.08%] | 1.26% | ×4.50 | +1.04 [+0.80, +1.26] | 46,501 | 10.8% | 0.000% | pass |
| credential first relay + content destination | yes | 0.51% | 6.00% [4.95%, 7.08%] | 1.34% | ×4.47 | +0.85 [-0.20, +1.87] | 2,001 | 30.1% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 5.79% [4.65%, 6.99%] | 1.34% | ×4.31 | +1.66 [+0.65, +2.56] | 1,986 | 36.0% | 0.000% | pass |
| content first relay + credential destination | yes | 0.51% | 5.16% [4.17%, 6.20%] | 1.10% | ×4.69 | -0.15 [-0.39, +0.05] | 1,976 | 16.1% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 5.77% [5.07%, 6.43%] | 1.26% | ×4.57 | +1.39 [+0.89, +1.90] | 5,478 | 12.3% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 1.26% | | | 531 | | | unstable (120 runs needed) |
| second relay + first relay | no | 1.17% | 4.34% [3.73%, 4.99%] | 1.10% | ×3.93 | -0.04 [-0.19, +0.09] | 4,542 | 14.8% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 4.59% [3.66%, 5.54%] | 1.10% | ×4.17 | -0.05 [-0.24, +0.10] | 2,025 | 23.6% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 4.67% [4.06%, 5.28%] | 1.10% | ×4.23 | -0.22 [-0.49, +0.06] | 8,166 | 21.0% | 0.000% | pass |
| gatekeeper + second relay | no | 1.92% | 4.70% [4.14%, 5.26%] | 1.10% | ×4.27 | -0.05 [-0.37, +0.24] | 7,504 | 11.1% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 4.29% [3.23%, 5.41%] | 1.10% | ×3.90 | +0.18 [-0.32, +0.75] | 1,631 | 28.3% | 0.000% | pass |
| every record the node can select |  | 15.00% | 5.71% [5.35%, 6.08%] | 1.26% | ×4.52 | +1.05 [+0.84, +1.26] | 58,473 | 10.7% | 0.000% | pass |
| first relay held |  | 4.79% | 4.90% [4.45%, 5.36%] | 1.15% | ×4.25 | +0.14 [-0.07, +0.37] | 18,671 | 17.2% | 0.000% | pass |
| no first relay held |  | 95.21% | 4.79% [4.40%, 5.19%] | 1.13% | ×4.26 | +0.14 [+0.08, +0.20] | 371,149 | 10.1% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [-0.07, +0.07] | 19,491 |
| D or G | +0.05 [-0.02, +0.11] | 38,982 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.26% [2.03%, 2.49%] | 0.55% | ×4.11 [3.69, 4.53] | reference | 30,806 | 3.7% | 0.000% | pass |
| First hop, credential | 2.25% [2.04%, 2.48%] | 0.55% | ×4.10 [3.71, 4.51] | -0.00 [-0.02, +0.02] | 616,120 | 2.0% | 0.000% | pass |
| Combined | 2.35% [2.14%, 2.56%] | 0.56% | ×4.19 [3.81, 4.55] | +0.10 [+0.06, +0.13] | 616,120 | 4.5% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.64% | 2.24% [2.03%, 2.47%] | 0.55% | ×4.08 | -0.00 [-0.03, +0.02] | 305,868 | 2.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.33% | 2.24% [2.02%, 2.47%] | 0.55% | ×4.08 | -0.04 [-0.09, +0.01] | 180,716 | 1.6% | 0.000% | pass |
| destination only | yes | 11.95% | 2.99% [2.82%, 3.18%] | 0.63% | ×4.74 | +0.69 [+0.55, +0.83] | 73,626 | 8.4% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 3.51% [2.79%, 4.19%] | 0.67% | ×5.21 | +1.36 [+0.56, +2.10] | 3,024 | 21.3% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 2.95% [2.32%, 3.65%] | 0.67% | ×4.37 | +0.79 [+0.13, +1.46] | 3,056 | 20.7% | 0.000% | pass |
| content first relay + credential destination | yes | 0.53% | 2.03% [1.51%, 2.60%] | 0.55% | ×3.70 | +0.06 [-0.09, +0.25] | 3,249 | 15.7% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 2.87% [2.49%, 3.29%] | 0.63% | ×4.53 | +0.84 [+0.49, +1.20] | 8,621 | 14.4% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 0.63% | | | 842 | | | unstable (152 runs needed) |
| second relay + first relay | no | 1.14% | 2.65% [2.25%, 3.07%] | 0.55% | ×4.82 | +0.06 [-0.04, +0.17] | 7,023 | 9.8% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 2.31% [1.79%, 2.88%] | 0.55% | ×4.20 | +0.06 [-0.06, +0.19] | 3,121 | 16.2% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 1.91% [1.64%, 2.21%] | 0.55% | ×3.49 | -0.02 [-0.19, +0.16] | 12,849 | 8.8% | 0.000% | pass |
| gatekeeper + second relay | no | 1.87% | 2.33% [2.01%, 2.68%] | 0.55% | ×4.25 | -0.03 [-0.23, +0.16] | 11,525 | 8.6% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 2.50% [1.90%, 3.08%] | 0.55% | ×4.55 | +0.12 [-0.34, +0.55] | 2,600 | 18.9% | 0.000% | pass |
| every record the node can select |  | 15.00% | 2.97% [2.79%, 3.18%] | 0.63% | ×4.70 | +0.72 [+0.59, +0.83] | 92,418 | 7.9% | 0.000% | pass |
| first relay held |  | 4.74% | 2.38% [2.09%, 2.67%] | 0.58% | ×4.13 | +0.24 [+0.10, +0.38] | 29,201 | 6.6% | 0.000% | pass |
| no first relay held |  | 95.26% | 2.35% [2.14%, 2.56%] | 0.56% | ×4.19 | +0.09 [+0.05, +0.13] | 586,919 | 4.5% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.02 [-0.06, +0.03] | 30,806 |
| D or G | +0.05 [+0.00, +0.09] | 61,612 |

#### R300_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 1.34% [1.25%, 1.43%] | 0.27% | ×4.89 [4.57, 5.21] | reference | 93,521 | 2.8% | 0.000% | pass |
| First hop, credential | 1.34% [1.26%, 1.42%] | 0.27% | ×4.90 [4.60, 5.19] | +0.00 [-0.01, +0.01] | 1,870,420 | 1.9% | 0.000% | pass |
| Combined | 1.39% [1.31%, 1.47%] | 0.28% | ×4.97 [4.69, 5.24] | +0.05 [+0.03, +0.07] | 1,870,420 | 3.0% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.71% | 1.34% [1.25%, 1.43%] | 0.27% | ×4.89 | -0.00 [-0.01, +0.01] | 929,874 | 1.8% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.20% | 1.34% [1.26%, 1.42%] | 0.27% | ×4.89 | -0.00 [-0.03, +0.02] | 546,245 | 2.4% | 0.000% | pass |
| destination only | yes | 11.92% | 1.71% [1.64%, 1.79%] | 0.32% | ×5.42 | +0.38 [+0.31, +0.44] | 222,872 | 4.3% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 1.74% [1.49%, 1.99%] | 0.34% | ×5.18 | +0.39 [+0.14, +0.66] | 9,242 | 9.2% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 2.01% [1.72%, 2.31%] | 0.34% | ×5.97 | +0.67 [+0.38, +0.95] | 9,622 | 5.7% | 0.000% | pass |
| content first relay + credential destination | yes | 0.53% | 1.32% [1.09%, 1.56%] | 0.27% | ×4.83 | +0.03 [-0.05, +0.11] | 9,828 | 7.1% | 0.000% | pass |
| second relay + destination | yes | 1.42% | 1.75% [1.58%, 1.93%] | 0.32% | ×5.55 | +0.34 [+0.17, +0.50] | 26,547 | 7.7% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.32% | | | 2,452 | | | unstable (117 runs needed) |
| second relay + first relay | no | 1.17% | 1.26% [1.10%, 1.40%] | 0.27% | ×4.58 | +0.02 [-0.03, +0.08] | 21,902 | 2.5% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 1.13% [0.92%, 1.37%] | 0.27% | ×4.14 | -0.03 [-0.08, +0.02] | 9,612 | 3.8% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 1.38% [1.24%, 1.51%] | 0.27% | ×5.03 | -0.05 [-0.13, +0.03] | 39,419 | 2.2% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 1.25% [1.13%, 1.36%] | 0.27% | ×4.55 | -0.08 [-0.16, +0.01] | 35,145 | 2.9% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 1.24% [0.97%, 1.52%] | 0.27% | ×4.53 | -0.05 [-0.21, +0.11] | 7,660 | 4.8% | 0.000% | pass |
| every record the node can select |  | 15.00% | 1.71% [1.64%, 1.78%] | 0.32% | ×5.42 | +0.37 [+0.31, +0.43] | 280,563 | 4.2% | 0.000% | pass |
| first relay held |  | 4.81% | 1.45% [1.35%, 1.54%] | 0.29% | ×5.04 | +0.10 [+0.03, +0.16] | 90,013 | 4.6% | 0.000% | pass |
| no first relay held |  | 95.19% | 1.39% [1.31%, 1.47%] | 0.28% | ×4.96 | +0.05 [+0.03, +0.07] | 1,780,407 | 3.0% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.01 [-0.03, +0.00] | 93,521 |
| D or G | +0.02 [+0.01, +0.04] | 187,042 |

### Content paths set the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 98.0% |
| R100_D100 | 98.1% |
| R300_D100 | 98.1% |

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 10.92% [10.43%, 11.43%] | 1.04% | ×10.51 [10.03, 10.99] | reference | 19,948 | 21.3% | 0.000% | pass |
| First hop, credential | 11.00% [10.51%, 11.49%] | 1.04% | ×10.58 [10.11, 11.05] | +0.07 [+0.04, +0.11] | 398,960 | 17.1% | 0.000% | pass |
| Combined | 11.77% [11.30%, 12.22%] | 1.04% | ×11.32 [10.87, 11.75] | +0.84 [+0.76, +0.92] | 398,960 | 21.5% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.76% | 10.81% [10.31%, 11.29%] | 1.04% | ×10.39 | -0.09 [-0.15, -0.02] | 198,521 | 16.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.12% | 11.29% [10.81%, 11.79%] | 1.04% | ×10.86 | +0.30 [+0.20, +0.41] | 116,180 | 18.9% | 0.000% | pass |
| destination only | yes | 11.93% | 15.90% [15.43%, 16.37%] | 1.04% | ×15.29 | +4.88 [+4.59, +5.17] | 47,585 | 41.8% | 0.002% | pass |
| credential first relay + content destination | yes | 0.51% | 18.79% [17.10%, 20.55%] | 1.04% | ×18.06 | +7.77 [+6.06, +9.40] | 2,033 | 70.1% | 1.230% | fail |
| content first relay + content destination | yes | 0.51% | 18.79% [17.34%, 20.25%] | 1.04% | ×18.08 | +9.08 [+7.59, +10.57] | 2,038 | 74.2% | 1.619% | fail |
| content first relay + credential destination | yes | 0.51% | 12.95% [11.59%, 14.37%] | 1.04% | ×12.45 | +1.84 [+1.14, +2.57] | 2,016 | 41.6% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 15.29% [14.41%, 16.27%] | 1.04% | ×14.70 | +4.96 [+4.21, +5.69] | 5,625 | 41.5% | 0.018% | pass |
| three or more roles, with a destination | yes | 0.14% | 15.72% [12.91%, 18.75%] | 1.04% | ×15.13 | +3.66 [+1.46, +5.88] | 547 | 62.4% | 0.000% | fail |
| second relay + first relay | no | 1.17% | 12.57% [11.45%, 13.62%] | 1.04% | ×12.09 | +1.01 [+0.62, +1.44] | 4,653 | 34.9% | 0.021% | pass |
| second relay + second relay | no | 0.52% | 9.71% [8.53%, 10.87%] | 1.04% | ×9.35 | -0.10 [-0.40, +0.19] | 2,059 | 40.0% | 0.146% | fail |
| gatekeeper + first relay | no | 2.10% | 12.32% [11.53%, 13.10%] | 1.04% | ×11.85 | +1.30 [+0.98, +1.64] | 8,360 | 21.9% | 0.000% | pass |
| gatekeeper + second relay | no | 1.92% | 10.83% [10.04%, 11.63%] | 1.04% | ×10.41 | +0.10 [-0.25, +0.48] | 7,667 | 22.3% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 11.22% [9.71%, 12.74%] | 1.04% | ×10.79 | +0.89 [+0.12, +1.64] | 1,676 | 41.0% | 0.000% | pass |
| every record the node can select |  | 15.00% | 15.94% [15.52%, 16.38%] | 1.04% | ×15.33 | +5.01 [+4.75, +5.27] | 59,844 | 40.6% | 0.002% | pass |
| first relay held |  | 4.79% | 13.83% [13.20%, 14.45%] | 1.04% | ×13.30 | +2.81 [+2.47, +3.14] | 19,100 | 33.4% | 0.047% | pass |
| no first relay held |  | 95.21% | 11.66% [11.20%, 12.11%] | 1.04% | ×11.22 | +0.74 [+0.66, +0.82] | 379,860 | 21.2% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.05 [-0.16, +0.06] | 19,948 |
| D or G | +1.56 [+1.40, +1.71] | 39,896 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 11.79% [11.24%, 12.35%] | 4.55% | ×2.59 [2.47, 2.72] | reference | 31,955 | 23.4% | 0.000% | pass |
| First hop, credential | 11.85% [11.32%, 12.36%] | 4.55% | ×2.61 [2.49, 2.72] | +0.06 [+0.02, +0.10] | 639,100 | 20.3% | 0.000% | pass |
| Combined | 12.16% [11.65%, 12.67%] | 4.55% | ×2.68 [2.56, 2.79] | +0.38 [+0.32, +0.44] | 639,100 | 22.7% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 11.85% [11.35%, 12.38%] | 4.55% | ×2.61 | +0.02 [-0.02, +0.07] | 317,517 | 20.4% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.27% | 11.88% [11.37%, 12.41%] | 4.55% | ×2.61 | +0.19 [+0.12, +0.27] | 187,072 | 21.3% | 0.000% | pass |
| destination only | yes | 11.92% | 13.70% [13.18%, 14.24%] | 4.55% | ×3.01 | +1.92 [+1.72, +2.11] | 76,208 | 34.7% | 0.000% | pass |
| credential first relay + content destination | yes | 0.51% | 15.02% [13.70%, 16.30%] | 4.55% | ×3.30 | +2.22 [+1.29, +3.21] | 3,243 | 48.6% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 14.66% [13.49%, 15.89%] | 4.55% | ×3.23 | +3.47 [+2.47, +4.53] | 3,260 | 44.2% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 12.44% [11.39%, 13.48%] | 4.55% | ×2.74 | +0.87 [+0.48, +1.26] | 3,335 | 30.9% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 13.25% [12.48%, 14.05%] | 4.55% | ×2.91 | +1.64 [+1.18, +2.09] | 8,939 | 38.2% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | 15.45% [12.76%, 18.17%] | 4.55% | ×3.40 | +2.39 [+0.87, +3.97] | 880 | 29.9% | 0.000% | pass |
| second relay + first relay | no | 1.14% | 12.88% [11.95%, 13.90%] | 4.55% | ×2.83 | +0.51 [+0.30, +0.71] | 7,274 | 35.6% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 10.75% [9.60%, 11.90%] | 4.55% | ×2.37 | +0.03 [-0.21, +0.30] | 3,338 | 27.3% | 0.030% | pass |
| gatekeeper + first relay | no | 2.09% | 12.31% [11.65%, 12.99%] | 4.55% | ×2.71 | +0.41 [+0.19, +0.64] | 13,388 | 22.8% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 12.10% [11.33%, 12.81%] | 4.55% | ×2.66 | +0.17 [-0.05, +0.39] | 12,023 | 27.1% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 12.92% [11.74%, 14.14%] | 4.55% | ×2.84 | +0.00 [-0.44, +0.45] | 2,623 | 46.1% | 0.000% | pass |
| every record the node can select |  | 15.00% | 13.71% [13.22%, 14.22%] | 4.55% | ×3.02 | +1.92 [+1.76, +2.10] | 95,865 | 33.5% | 0.000% | pass |
| first relay held |  | 4.77% | 13.00% [12.42%, 13.58%] | 4.55% | ×2.86 | +1.00 [+0.81, +1.20] | 30,500 | 31.1% | 0.000% | pass |
| no first relay held |  | 95.23% | 12.12% [11.57%, 12.65%] | 4.55% | ×2.67 | +0.34 [+0.28, +0.40] | 608,600 | 22.6% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.04 [-0.04, +0.13] | 31,955 |
| D or G | +0.52 [+0.42, +0.63] | 63,910 |

#### R300_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 6.78% [6.60%, 6.97%] | 2.27% | ×2.98 [2.90, 3.07] | reference | 96,773 | 13.6% | 0.000% | pass |
| First hop, credential | 6.81% [6.64%, 7.00%] | 2.27% | ×3.00 [2.92, 3.08] | +0.03 [+0.01, +0.05] | 1,935,460 | 11.9% | 0.000% | pass |
| Combined | 6.98% [6.79%, 7.16%] | 2.27% | ×3.07 [2.99, 3.15] | +0.20 [+0.17, +0.23] | 1,935,460 | 14.3% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.69% | 6.77% [6.59%, 6.95%] | 2.27% | ×2.98 | -0.01 [-0.03, +0.02] | 961,709 | 12.0% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.25% | 6.87% [6.67%, 7.05%] | 2.27% | ×3.02 | +0.08 [+0.04, +0.11] | 566,098 | 12.3% | 0.000% | pass |
| destination only | yes | 11.92% | 7.92% [7.74%, 8.08%] | 2.27% | ×3.48 | +1.11 [+1.02, +1.19] | 230,784 | 19.8% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 8.92% [8.41%, 9.45%] | 2.27% | ×3.93 | +2.07 [+1.55, +2.59] | 9,762 | 33.9% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 8.84% [8.22%, 9.44%] | 2.27% | ×3.89 | +1.98 [+1.48, +2.51] | 9,927 | 29.2% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 6.81% [6.35%, 7.23%] | 2.27% | ×3.00 | +0.34 [+0.15, +0.53] | 10,048 | 18.6% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 7.68% [7.35%, 7.96%] | 2.27% | ×3.38 | +1.00 [+0.76, +1.21] | 27,150 | 25.8% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | 7.78% [6.78%, 8.81%] | 2.27% | ×3.42 | +1.25 [+0.50, +2.02] | 2,648 | 42.1% | 0.189% | fail |
| second relay + first relay | no | 1.16% | 7.02% [6.67%, 7.39%] | 2.27% | ×3.09 | +0.25 [+0.13, +0.37] | 22,465 | 11.2% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 6.91% [6.39%, 7.43%] | 2.27% | ×3.04 | -0.06 [-0.18, +0.06] | 9,927 | 21.2% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 7.07% [6.76%, 7.39%] | 2.27% | ×3.11 | +0.20 [+0.10, +0.30] | 40,617 | 15.6% | 0.000% | pass |
| gatekeeper + second relay | no | 1.89% | 6.76% [6.49%, 7.02%] | 2.27% | ×2.97 | +0.02 [-0.06, +0.10] | 36,486 | 14.9% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 6.95% [6.45%, 7.44%] | 2.27% | ×3.06 | +0.37 [+0.15, +0.59] | 7,839 | 26.5% | 0.000% | pass |
| every record the node can select |  | 15.00% | 7.92% [7.76%, 8.08%] | 2.27% | ×3.48 | +1.14 [+1.05, +1.22] | 290,319 | 20.1% | 0.000% | pass |
| first relay held |  | 4.80% | 7.41% [7.20%, 7.62%] | 2.27% | ×3.26 | +0.62 [+0.52, +0.72] | 92,819 | 18.2% | 0.000% | pass |
| no first relay held |  | 95.20% | 6.96% [6.77%, 7.14%] | 2.27% | ×3.06 | +0.18 [+0.15, +0.21] | 1,842,641 | 14.2% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.00 [-0.04, +0.04] | 96,773 |
| D or G | +0.37 [+0.32, +0.42] | 193,546 |

### F content path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 97.0% |
| R100_D100 | 96.9% |
| R300_D100 | 96.9% |

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 5.38% [5.01%, 5.75%] | 1.01% | ×5.33 [4.96, 5.69] | reference | 19,915 | 12.7% | 0.000% | pass |
| First hop, credential | 5.37% [5.01%, 5.73%] | 1.01% | ×5.32 [4.96, 5.67] | -0.01 [-0.04, +0.02] | 398,300 | 9.4% | 0.000% | pass |
| Combined | 6.17% [5.82%, 6.54%] | 1.01% | ×6.11 [5.76, 6.47] | +0.79 [+0.72, +0.88] | 398,300 | 28.6% | 0.021% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.67% | 5.22% [4.85%, 5.58%] | 1.01% | ×5.17 | -0.17 [-0.23, -0.10] | 197,844 | 8.5% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.26% | 5.30% [4.93%, 5.68%] | 1.01% | ×5.24 | -0.05 [-0.14, +0.05] | 116,550 | 13.5% | 0.000% | pass |
| destination only | yes | 11.96% | 11.25% [10.87%, 11.63%] | 1.01% | ×11.14 | +5.89 [+5.65, +6.14] | 47,634 | 45.2% | 0.149% | fail |
| credential first relay + content destination | yes | 0.52% | 14.13% [12.85%, 15.51%] | 1.01% | ×14.00 | +9.32 [+7.93, +10.78] | 2,059 | 45.1% | 0.340% | fail |
| content first relay + content destination | yes | 0.49% | 16.34% [14.81%, 17.89%] | 1.01% | ×16.18 | +10.84 [+9.36, +12.31] | 1,965 | 46.9% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 6.05% [4.98%, 7.25%] | 1.01% | ×5.99 | +0.14 [-0.29, +0.58] | 2,083 | 22.7% | 0.000% | pass |
| second relay + destination | yes | 1.37% | 11.29% [10.43%, 12.09%] | 1.01% | ×11.18 | +5.61 [+4.92, +6.29] | 5,475 | 65.3% | 1.187% | fail |
| three or more roles, with a destination | yes | 0.13% | 10.59% [8.05%, 13.23%] | 1.01% | ×10.48 | +6.43 [+4.33, +8.67] | 529 | 62.4% | 0.189% | fail |
| second relay + first relay | no | 1.12% | 5.94% [5.19%, 6.64%] | 1.01% | ×5.89 | +0.16 [-0.15, +0.45] | 4,458 | 14.8% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 5.62% [4.64%, 6.63%] | 1.01% | ×5.57 | -0.05 [-0.34, +0.24] | 2,081 | 34.6% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 5.27% [4.77%, 5.76%] | 1.01% | ×5.22 | -0.05 [-0.30, +0.20] | 8,309 | 14.9% | 0.012% | pass |
| gatekeeper + second relay | no | 1.92% | 5.35% [4.83%, 5.86%] | 1.01% | ×5.30 | -0.20 [-0.51, +0.12] | 7,628 | 11.0% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 5.04% [4.02%, 6.12%] | 1.01% | ×4.99 | +0.24 [-0.30, +0.86] | 1,685 | 34.3% | 0.000% | pass |
| every record the node can select |  | 15.00% | 11.33% [10.97%, 11.73%] | 1.01% | ×11.22 | +5.95 [+5.72, +6.19] | 59,745 | 44.4% | 0.139% | fail |
| first relay held |  | 4.74% | 7.63% [7.14%, 8.14%] | 1.01% | ×7.56 | +2.18 [+1.90, +2.48] | 18,874 | 40.9% | 0.000% | pass |
| no first relay held |  | 95.26% | 6.10% [5.73%, 6.44%] | 1.01% | ×6.04 | +0.73 [+0.65, +0.80] | 379,426 | 27.9% | 0.025% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.04 [-0.13, +0.05] | 19,915 |
| D or G | +0.37 [+0.27, +0.48] | 39,830 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 7.52% [7.18%, 7.86%] | 3.12% | ×2.41 [2.30, 2.52] | reference | 46,418 | 15.1% | 0.000% | pass |
| First hop, credential | 7.54% [7.21%, 7.87%] | 3.12% | ×2.41 [2.31, 2.52] | +0.02 [-0.01, +0.04] | 928,360 | 12.3% | 0.000% | pass |
| Combined | 7.97% [7.66%, 8.29%] | 3.12% | ×2.55 [2.45, 2.65] | +0.46 [+0.41, +0.51] | 928,360 | 23.8% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.67% | 7.50% [7.17%, 7.81%] | 3.12% | ×2.40 | -0.02 [-0.07, +0.02] | 461,074 | 12.0% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.29% | 7.59% [7.28%, 7.93%] | 3.12% | ×2.43 | +0.09 [+0.02, +0.15] | 271,947 | 13.1% | 0.000% | pass |
| destination only | yes | 11.94% | 10.43% [10.15%, 10.74%] | 3.12% | ×3.34 | +2.89 [+2.76, +3.02] | 110,800 | 30.9% | 0.003% | pass |
| credential first relay + content destination | yes | 0.49% | 12.57% [11.63%, 13.48%] | 3.12% | ×4.02 | +4.96 [+4.11, +5.79] | 4,576 | 53.5% | 0.066% | fail |
| content first relay + content destination | yes | 0.51% | 11.02% [10.06%, 12.08%] | 3.12% | ×3.53 | +3.83 [+2.97, +4.67] | 4,729 | 50.5% | 0.444% | fail |
| content first relay + credential destination | yes | 0.53% | 8.14% [7.31%, 9.00%] | 3.12% | ×2.60 | +0.26 [-0.04, +0.56] | 4,917 | 16.5% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 10.43% [9.81%, 11.08%] | 3.12% | ×3.34 | +3.09 [+2.67, +3.57] | 13,023 | 44.7% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 9.51% [7.83%, 11.28%] | 3.12% | ×3.04 | +2.89 [+1.47, +4.35] | 1,209 | 35.4% | 0.000% | pass |
| second relay + first relay | no | 1.13% | 7.49% [6.95%, 8.01%] | 3.12% | ×2.40 | +0.13 [-0.06, +0.32] | 10,519 | 18.9% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 7.73% [6.86%, 8.57%] | 3.12% | ×2.47 | -0.19 [-0.40, +0.02] | 4,853 | 26.7% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 7.70% [7.24%, 8.13%] | 3.12% | ×2.46 | +0.32 [+0.15, +0.50] | 19,449 | 17.2% | 0.000% | pass |
| gatekeeper + second relay | no | 1.87% | 7.57% [7.05%, 8.13%] | 3.12% | ×2.42 | -0.09 [-0.25, +0.06] | 17,380 | 15.8% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 8.29% [7.39%, 9.26%] | 3.12% | ×2.65 | +0.05 [-0.26, +0.36] | 3,884 | 29.7% | 0.000% | pass |
| every record the node can select |  | 15.00% | 10.43% [10.15%, 10.73%] | 3.12% | ×3.34 | +2.92 [+2.78, +3.06] | 139,254 | 31.4% | 0.000% | pass |
| first relay held |  | 4.76% | 8.56% [8.18%, 8.93%] | 3.12% | ×2.74 | +1.12 [+0.99, +1.26] | 44,190 | 31.7% | 0.025% | pass |
| no first relay held |  | 95.24% | 7.94% [7.62%, 8.27%] | 3.12% | ×2.54 | +0.42 [+0.38, +0.47] | 884,170 | 23.4% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.03 [-0.09, +0.03] | 46,418 |
| D or G | +0.32 [+0.25, +0.38] | 92,836 |

#### R300_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 4.05% [3.92%, 4.17%] | 1.56% | ×2.59 [2.51, 2.67] | reference | 139,860 | 7.2% | 0.000% | pass |
| First hop, credential | 4.05% [3.93%, 4.17%] | 1.56% | ×2.59 [2.52, 2.67] | +0.00 [-0.01, +0.02] | 2,797,200 | 6.2% | 0.000% | pass |
| Combined | 4.31% [4.20%, 4.42%] | 1.56% | ×2.76 [2.69, 2.83] | +0.26 [+0.24, +0.28] | 2,797,200 | 13.2% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.67% | 4.02% [3.89%, 4.14%] | 1.56% | ×2.57 | -0.02 [-0.04, -0.00] | 1,389,365 | 6.4% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.27% | 4.08% [3.96%, 4.20%] | 1.56% | ×2.61 | +0.01 [-0.02, +0.03] | 818,823 | 6.4% | 0.000% | pass |
| destination only | yes | 11.94% | 5.82% [5.71%, 5.93%] | 1.56% | ×3.72 | +1.75 [+1.68, +1.82] | 334,084 | 19.1% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 6.80% [6.40%, 7.20%] | 1.56% | ×4.36 | +2.81 [+2.44, +3.17] | 13,814 | 27.0% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 6.56% [6.16%, 6.98%] | 1.56% | ×4.20 | +2.60 [+2.23, +2.98] | 14,289 | 30.6% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 4.31% [3.94%, 4.67%] | 1.56% | ×2.76 | +0.32 [+0.20, +0.44] | 14,460 | 13.9% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 5.71% [5.46%, 5.97%] | 1.56% | ×3.65 | +1.77 [+1.59, +1.95] | 39,301 | 17.8% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 5.64% [4.91%, 6.41%] | 1.56% | ×3.61 | +1.35 [+0.78, +1.92] | 3,632 | 31.9% | 0.000% | pass |
| second relay + first relay | no | 1.14% | 3.96% [3.73%, 4.20%] | 1.56% | ×2.53 | +0.04 [-0.04, +0.12] | 31,895 | 10.6% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 4.08% [3.69%, 4.45%] | 1.56% | ×2.61 | -0.06 [-0.15, +0.04] | 14,392 | 14.0% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 4.19% [4.00%, 4.37%] | 1.56% | ×2.68 | +0.18 [+0.11, +0.24] | 59,002 | 8.3% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 4.05% [3.90%, 4.20%] | 1.56% | ×2.59 | -0.08 [-0.16, -0.00] | 52,499 | 9.1% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 3.86% [3.49%, 4.22%] | 1.56% | ×2.47 | +0.20 [+0.04, +0.36] | 11,644 | 11.9% | 0.000% | pass |
| every record the node can select |  | 15.00% | 5.81% [5.70%, 5.92%] | 1.56% | ×3.72 | +1.76 [+1.71, +1.82] | 419,580 | 18.7% | 0.000% | pass |
| first relay held |  | 4.77% | 4.67% [4.52%, 4.83%] | 1.56% | ×2.99 | +0.69 [+0.63, +0.75] | 133,460 | 17.4% | 0.000% | pass |
| no first relay held |  | 95.23% | 4.29% [4.18%, 4.41%] | 1.56% | ×2.75 | +0.24 [+0.22, +0.26] | 2,663,740 | 13.1% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.02 [-0.05, +0.01] | 139,860 |
| D or G | +0.19 [+0.16, +0.22] | 279,720 |

## Cost per run

| Configuration | Cell | Simulation | Scoring | Shuffle test |
|---|---|---|---|---|
| Main run | R1_D100 | 2.6 s | 23.5 s | 0.2 s |
| Main run | R100_D100 | 0.3 s | 40.9 s | 0.2 s |
| Main run | R300_D100 | 0.5 s | 311.1 s | 1.0 s |
| Every hold off | R1_D100 | 2.5 s | 19.5 s | 0.0 s |
| Every hold off | R100_D100 | 0.3 s | 15.0 s | 0.0 s |
| Every hold off | R300_D100 | 0.5 s | 78.5 s | 0.0 s |
| Credential path sets the record time | R1_D100 | 2.6 s | 26.2 s | 0.0 s |
| Credential path sets the record time | R100_D100 | 0.3 s | 52.5 s | 0.0 s |
| Credential path sets the record time | R300_D100 | 0.5 s | 383.7 s | 0.0 s |
| Content paths set the record time | R1_D100 | 2.6 s | 24.9 s | 0.0 s |
| Content paths set the record time | R100_D100 | 0.3 s | 51.5 s | 0.0 s |
| Content paths set the record time | R300_D100 | 0.5 s | 358.2 s | 0.0 s |
| F content path sets the record time | R1_D100 | 2.7 s | 35.3 s | 0.0 s |
| F content path sets the record time | R100_D100 | 0.4 s | 130.0 s | 0.0 s |
| F content path sets the record time | R300_D100 | 0.7 s | 877.4 s | 0.0 s |

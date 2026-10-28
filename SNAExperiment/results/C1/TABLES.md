# Tables

Main run: D = 1168.2 s; rates are R / D and 100 / D. Intervals are 95% and resample whole runs. Device named: the vantage names the device behind a registry record. Chance, feasible set: a uniform guess among the devices whose packets could have produced the record. A row with fewer than 50 right or 50 wrong device-level decisions is unstable and shows no estimate.

## In flight

| Configuration | Cell | Real in flight (target) | Decoys in flight (target) | Runs |
|---|---|---|---|---|
| Main run | R1_D100 | 0.99 (1) | 99.73 (100) | 100 |
| Main run | R150_D100 | 149.85 (150) | 99.74 (100) | 100 |
| Every hold off | R1_D100 | 0.98 (1) | 98.75 (100) | 100 |
| Every hold off | R150_D100 | 147.97 (150) | 98.11 (100) | 100 |
| Credential path sets the record time | R1_D100 | 1.00 (1) | 100.14 (100) | 100 |
| Credential path sets the record time | R150_D100 | 150.24 (150) | 99.55 (100) | 100 |
| Content paths set the record time | R1_D100 | 1.00 (1) | 100.11 (100) | 100 |
| Content paths set the record time | R150_D100 | 149.69 (150) | 100.46 (100) | 100 |
| F content path sets the record time | R1_D100 | 0.99 (1) | 100.04 (100) | 100 |
| F content path sets the record time | R150_D100 | 149.90 (150) | 100.85 (100) | 100 |

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
| R150_D100 | 46,087 | 2.02% [1.86%, 2.18%] | 0.16 points |

## Timing (main run, R = 150)

| Stage | Mean | Std dev | Maximum |
|---|---|---|---|
| device, credential channel | 119.6 s | 102.9 s | 360.0 s |
| device, content channels | 240.1 s | 206.7 s | 720.0 s |
| first relay hops (A, D, G) | 60.1 s | 51.3 s | 180.0 s |
| second relay hops (B, E, H) | 299.7 s | 258.2 s | 900.0 s |
| C before CV-1 | 30.1 s | 25.3 s | 90.0 s |
| V before CV-2 | 29.8 s | 25.1 s | 90.0 s |
| C fan-out, per leg | 45.1 s | 30.9 s | 179.5 s |
| gatekeeper hold | 30.0 s | 25.3 s | 90.0 s |
| departure bundling wait | 101.1 s | 90.9 s | 360.0 s |
| F/I pre-match hold | 120.0 s | 102.9 s | 360.0 s |
| post-match lottery | 30.0 s | 25.2 s | 90.0 s |
| registry bundle wait | 60.1 s | 34.6 s | 120.0 s |
| registry posting wait | 61.5 s | 35.6 s | 119.2 s |
| capture to finalization | 1166.2 s | 299.2 s | 2317.6 s |

| Cell | Mean capture to finalization [95% CI] |
|---|---|
| R1_D100 | 1159.1 s [1151.5, 1166.6] |
| R150_D100 | 1166.2 s [1158.8, 1173.9] |

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

## R150_D100: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.02% [1.86%, 2.18%] | 0.44% | ×4.59 [4.23, 4.94] | reference | 46,087 | 7.4% | 0.000% | pass |
| First hop, credential | 2.04% [1.88%, 2.19%] | 0.44% | ×4.62 [4.26, 4.96] | +0.01 [-0.00, +0.03] | 921,740 | 5.2% | 0.000% | pass |
| First hop, content | 2.04% [1.88%, 2.20%] | 0.44% | ×4.62 [4.26, 4.99] | +0.01 [-0.00, +0.03] | 921,740 | 5.2% | 0.000% | pass |
| Credential processor | 2.03% [1.87%, 2.19%] | 0.44% | ×4.60 [4.24, 4.96] | +0.01 [-0.00, +0.01] | 783,479 | 5.4% | 0.000% | pass |
| Validator | 2.32% [2.17%, 2.48%] | 0.47% | ×4.90 [4.58, 5.23] | +0.29 [+0.11, +0.47] | 46,087 | 6.3% | 0.000% | pass |
| Gatekeeper | 2.04% [1.87%, 2.20%] | 0.44% | ×4.62 [4.24, 4.99] | +0.02 [-0.01, +0.04] | 138,261 | 6.0% | 0.000% | pass |
| Content server | 2.39% [2.26%, 2.53%] | 0.45% | ×5.30 [5.00, 5.60] | +0.37 [+0.24, +0.49] | 92,174 | 4.4% | 0.000% | pass |
| Combined | 2.07% [1.92%, 2.23%] | 0.44% | ×4.69 [4.35, 5.04] | +0.05 [+0.03, +0.07] | 921,740 | 4.6% | 0.000% | pass |

### R150_D100: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 2.04% [1.88%, 2.21%] | 0.44% | ×4.62 [4.25, 5.00] | +0.01 [-0.00, +0.03] | 837,506 | 5.3% | 0.000% | pass |
| First hop, content | 2.04% [1.88%, 2.20%] | 0.44% | ×4.62 [4.26, 4.98] | +0.01 [-0.00, +0.03] | 837,506 | 5.3% | 0.000% | pass |
| Credential processor | 2.03% [1.87%, 2.20%] | 0.44% | ×4.61 [4.24, 4.98] | +0.00 [-0.00, +0.01] | 739,399 | 5.5% | 0.000% | pass |
| Gatekeeper | 2.01% [1.84%, 2.18%] | 0.44% | ×4.55 [4.18, 4.94] | +0.02 [-0.02, +0.05] | 98,107 | 5.6% | 0.000% | pass |
| Content server | 2.40% [2.25%, 2.55%] | 0.45% | ×5.31 [4.98, 5.64] | +0.39 [+0.27, +0.51] | 73,481 | 5.0% | 0.000% | pass |

### R150_D100: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.69% | 2.04% [1.88%, 2.20%] | 0.44% | ×4.62 | +0.01 [-0.00, +0.03] | 457,979 | 5.5% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.23% | 2.04% [1.88%, 2.19%] | 0.44% | ×4.62 | +0.01 [-0.02, +0.03] | 269,463 | 5.5% | 0.000% | pass |
| destination only | yes | 11.94% | 2.27% [2.13%, 2.42%] | 0.45% | ×5.07 | +0.26 [+0.18, +0.35] | 110,064 | 4.1% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 2.31% [1.90%, 2.73%] | 0.45% | ×5.11 | +0.24 [-0.13, +0.61] | 4,550 | 11.3% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 2.41% [1.99%, 2.85%] | 0.45% | ×5.34 | +0.41 [+0.06, +0.77] | 4,602 | 14.5% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 2.04% [1.64%, 2.45%] | 0.44% | ×4.62 | +0.00 [-0.17, +0.16] | 4,807 | 22.2% | 0.021% | pass |
| second relay + destination | yes | 1.41% | 2.27% [2.01%, 2.57%] | 0.45% | ×5.07 | +0.15 [-0.07, +0.36] | 12,981 | 12.6% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 0.45% | | | 1,257 | | | unstable (132 runs needed) |
| second relay + first relay | no | 1.17% | 1.61% [1.35%, 1.89%] | 0.44% | ×3.66 | +0.06 [+0.00, +0.14] | 10,775 | 6.5% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 2.06% [1.65%, 2.49%] | 0.44% | ×4.67 | +0.04 [-0.04, +0.13] | 4,705 | 17.2% | 0.000% | pass |
| gatekeeper + first relay | no | 2.12% | 2.15% [1.94%, 2.37%] | 0.44% | ×4.88 | +0.05 [-0.02, +0.11] | 19,521 | 10.4% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 2.13% [1.88%, 2.38%] | 0.44% | ×4.83 | +0.05 [-0.03, +0.12] | 17,329 | 9.6% | 0.000% | pass |
| three or more roles, no destination | no | 0.40% | 2.35% [1.85%, 2.91%] | 0.44% | ×5.32 | +0.19 [+0.03, +0.38] | 3,707 | 21.3% | 0.000% | pass |
| every record the node can select |  | 15.00% | 2.27% [2.14%, 2.41%] | 0.45% | ×5.08 | +0.25 [+0.17, +0.33] | 138,261 | 4.2% | 0.000% | pass |
| first relay held |  | 4.80% | 2.05% [1.88%, 2.22%] | 0.44% | ×4.63 | +0.10 [+0.03, +0.18] | 44,255 | 4.7% | 0.000% | pass |
| no first relay held |  | 95.20% | 2.08% [1.93%, 2.23%] | 0.44% | ×4.70 | +0.05 [+0.03, +0.07] | 877,485 | 4.7% | 0.000% | pass |

## Diagnostics

| Cell | Variant | Device named [95% CI] | Chance | Multiple of chance | Posted-time number [95% CI] | Change [95% CI] |
|---|---|---|---|---|---|---|
| R1_D100 | observer, timing evidence off | 3.30% [2.83%, 3.78%] | 1.11% | ×2.96 | 4.77% [4.26%, 5.27%] | n/a |
| R1_D100 | observer, record time at the midpoint | 5.22% [4.74%, 5.70%] | 1.13% | ×4.61 | 4.77% [4.28%, 5.25%] | +0.45 [+0.20, +0.69] |
| R1_D100 | content server, record time at the midpoint | 5.88% [5.51%, 6.28%] | 1.15% | ×5.11 | 5.53% [5.15%, 5.93%] | +0.36 [+0.15, +0.57] |
| R150_D100 | observer, timing evidence off | 1.56% [1.42%, 1.70%] | 0.44% | ×3.53 | 2.02% [1.86%, 2.18%] | n/a |
| R150_D100 | observer, record time at the midpoint | 2.22% [2.08%, 2.38%] | 0.45% | ×4.94 | 2.02% [1.87%, 2.19%] | +0.20 [+0.09, +0.30] |
| R150_D100 | content server, record time at the midpoint | 2.56% [2.41%, 2.70%] | 0.46% | ×5.59 | 2.39% [2.26%, 2.54%] | +0.16 [+0.06, +0.27] |

| Cell | Packet type | Observer submission hit [95% CI] | Random rate | Delay to record time, mean | Std dev |
|---|---|---|---|---|---|
| R1_D100 | credential | 0.43% [0.35%, 0.51%] | 0.17% | 1039.8 s | 302.4 s |
| R1_D100 | F content | 0.44% [0.34%, 0.54%] | 0.17% | 919.3 s | 309.6 s |
| R1_D100 | I content | 0.48% [0.38%, 0.58%] | 0.17% | 918.3 s | 312.3 s |
| R150_D100 | credential | 0.16% [0.12%, 0.19%] | 0.07% | 1046.5 s | 304.5 s |
| R150_D100 | F content | 0.20% [0.16%, 0.24%] | 0.07% | 926.0 s | 309.5 s |
| R150_D100 | I content | 0.20% [0.16%, 0.24%] | 0.07% | 926.3 s | 310.5 s |

| Cell | Packet | Departure to arrival at its destination, mean | Std dev |
|---|---|---|---|
| R1_D100 | credential (at C) | 358.0 s | 262.9 s |
| R1_D100 | F content (at F) | 357.6 s | 262.0 s |
| R1_D100 | I content (at I) | 357.5 s | 263.3 s |
| R150_D100 | credential (at C) | 358.7 s | 262.0 s |
| R150_D100 | F content (at F) | 360.7 s | 264.5 s |
| R150_D100 | I content (at I) | 360.5 s | 262.5 s |

| Cell | Observer, first half of the window [95% CI] | Second half [95% CI] | Second minus first [95% CI] | Agree |
|---|---|---|---|---|
| R1_D100 | 5.03% [4.30%, 5.71%] | 4.51% [3.84%, 5.18%] | -0.51 [-1.51, +0.52] | yes |
| R150_D100 | 2.08% [1.88%, 2.29%] | 1.96% [1.75%, 2.18%] | -0.12 [-0.41, +0.17] | yes |

| Configuration | Cell | Real transactions introduced in the window | Never finalized (quorum timeout) |
|---|---|---|---|
| Main run | R1_D100 | 19,943 | 0 |
| Main run | R150_D100 | 46,087 | 0 |
| Every hold off | R1_D100 | 19,917 | 0 |
| Every hold off | R150_D100 | 42,578 | 0 |
| Credential path sets the record time | R1_D100 | 19,947 | 456 |
| Credential path sets the record time | R150_D100 | 47,607 | 1,108 |
| Content paths set the record time | R1_D100 | 19,948 | 0 |
| Content paths set the record time | R150_D100 | 48,148 | 0 |
| F content path sets the record time | R1_D100 | 19,915 | 0 |
| F content path sets the record time | R150_D100 | 69,477 | 0 |

| Cell | F and I confirmations set by the match board |
|---|---|
| R1_D100 | 49.8% |
| R150_D100 | 50.0% |

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
| Main run | R150_D100 | Passive observer | 0.38% [0.32%, 0.43%] | 0.39% | pass |
| Main run | R150_D100 | First hop | 0.38% [0.32%, 0.44%] | 0.39% | pass |
| Main run | R150_D100 | Credential processor | 0.38% [0.32%, 0.44%] | 0.39% | pass |
| Main run | R150_D100 | Validator | 0.39% [0.33%, 0.46%] | 0.39% | pass |
| Main run | R150_D100 | Gatekeeper | 0.37% [0.32%, 0.42%] | 0.39% | pass |
| Main run | R150_D100 | Content server | 0.40% [0.36%, 0.45%] | 0.39% | pass |
| Main run | R150_D100 | Combined | 0.38% [0.33%, 0.43%] | 0.39% | pass |
| Every hold off | R1_D100 | Passive observer | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | First hop | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | Credential processor | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | Validator | 0.03% [0.01%, 0.05%] | 0.02% | pass |
| Every hold off | R1_D100 | Gatekeeper | 0.02% [0.01%, 0.03%] | 0.02% | pass |
| Every hold off | R1_D100 | Content server | 0.01% [0.00%, 0.02%] | 0.02% | fail |
| Every hold off | R1_D100 | Combined | 0.02% [0.01%, 0.04%] | 0.02% | pass |
| Every hold off | R150_D100 | Passive observer | 0.05% [0.03%, 0.07%] | 0.06% | pass |
| Every hold off | R150_D100 | First hop | 0.05% [0.03%, 0.07%] | 0.06% | pass |
| Every hold off | R150_D100 | Credential processor | 0.05% [0.03%, 0.07%] | 0.06% | pass |
| Every hold off | R150_D100 | Validator | 0.05% [0.03%, 0.08%] | 0.06% | pass |
| Every hold off | R150_D100 | Gatekeeper | 0.05% [0.04%, 0.07%] | 0.06% | pass |
| Every hold off | R150_D100 | Content server | 0.07% [0.04%, 0.09%] | 0.06% | pass |
| Every hold off | R150_D100 | Combined | 0.05% [0.04%, 0.07%] | 0.06% | pass |
| Credential path sets the record time | R1_D100 | Passive observer | 0.92% [0.73%, 1.14%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | First hop | 0.94% [0.74%, 1.15%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | Credential processor | 0.93% [0.73%, 1.15%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | Validator | 0.92% [0.74%, 1.13%] | 1.00% | pass |
| Credential path sets the record time | R1_D100 | Gatekeeper | 0.95% [0.78%, 1.15%] | 0.99% | pass |
| Credential path sets the record time | R1_D100 | Content server | 1.08% [0.91%, 1.28%] | 1.00% | pass |
| Credential path sets the record time | R1_D100 | Combined | 0.96% [0.77%, 1.16%] | 0.99% | pass |
| Credential path sets the record time | R150_D100 | Passive observer | 0.45% [0.38%, 0.51%] | 0.39% | pass |
| Credential path sets the record time | R150_D100 | First hop | 0.45% [0.39%, 0.52%] | 0.39% | pass |
| Credential path sets the record time | R150_D100 | Credential processor | 0.45% [0.39%, 0.51%] | 0.39% | pass |
| Credential path sets the record time | R150_D100 | Validator | 0.34% [0.29%, 0.40%] | 0.39% | pass |
| Credential path sets the record time | R150_D100 | Gatekeeper | 0.45% [0.40%, 0.50%] | 0.39% | fail |
| Credential path sets the record time | R150_D100 | Content server | 0.37% [0.33%, 0.41%] | 0.39% | pass |
| Credential path sets the record time | R150_D100 | Combined | 0.44% [0.38%, 0.50%] | 0.39% | pass |
| Content paths set the record time | R1_D100 | Passive observer | 0.88% [0.73%, 1.02%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | First hop | 0.88% [0.74%, 1.02%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | Credential processor | 0.88% [0.74%, 1.03%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | Validator | 1.09% [0.93%, 1.26%] | 0.99% | pass |
| Content paths set the record time | R1_D100 | Gatekeeper | 0.82% [0.69%, 0.95%] | 0.99% | fail |
| Content paths set the record time | R1_D100 | Content server | 0.78% [0.68%, 0.90%] | 0.99% | fail |
| Content paths set the record time | R1_D100 | Combined | 0.87% [0.73%, 1.01%] | 0.99% | pass |
| Content paths set the record time | R150_D100 | Passive observer | 3.63% [3.39%, 3.88%] | 3.70% | pass |
| Content paths set the record time | R150_D100 | First hop | 3.62% [3.39%, 3.87%] | 3.70% | pass |
| Content paths set the record time | R150_D100 | Credential processor | 3.63% [3.38%, 3.87%] | 3.70% | pass |
| Content paths set the record time | R150_D100 | Validator | 3.57% [3.28%, 3.89%] | 3.70% | pass |
| Content paths set the record time | R150_D100 | Gatekeeper | 3.60% [3.35%, 3.84%] | 3.70% | pass |
| Content paths set the record time | R150_D100 | Content server | 3.68% [3.45%, 3.89%] | 3.70% | pass |
| Content paths set the record time | R150_D100 | Combined | 3.63% [3.39%, 3.87%] | 3.70% | pass |
| F content path sets the record time | R1_D100 | Passive observer | 1.06% [0.86%, 1.29%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | First hop | 1.06% [0.87%, 1.28%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Credential processor | 1.07% [0.87%, 1.29%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Validator | 1.02% [0.85%, 1.21%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Gatekeeper | 1.05% [0.84%, 1.28%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Content server | 1.39% [0.93%, 1.97%] | 0.99% | pass |
| F content path sets the record time | R1_D100 | Combined | 1.10% [0.90%, 1.37%] | 0.99% | pass |
| F content path sets the record time | R150_D100 | Passive observer | 2.54% [2.39%, 2.68%] | 2.50% | pass |
| F content path sets the record time | R150_D100 | First hop | 2.53% [2.38%, 2.69%] | 2.50% | pass |
| F content path sets the record time | R150_D100 | Credential processor | 2.52% [2.38%, 2.67%] | 2.50% | pass |
| F content path sets the record time | R150_D100 | Validator | 2.50% [2.36%, 2.65%] | 2.50% | pass |
| F content path sets the record time | R150_D100 | Gatekeeper | 2.53% [2.38%, 2.67%] | 2.50% | pass |
| F content path sets the record time | R150_D100 | Content server | 2.61% [2.49%, 2.73%] | 2.50% | pass |
| F content path sets the record time | R150_D100 | Combined | 2.53% [2.39%, 2.67%] | 2.50% | pass |

### Shuffle test (observer)

| Cell | Shuffle mismatches | Feasible-count mismatches | Exact expected accuracy | Exact expected chance | Mean accuracy over permutations (sd) | Mean chance over permutations | Interval coverage | Scored accuracy | Scored percentile |
|---|---|---|---|---|---|---|---|---|---|
| R1_D100 | 1 | 0 | 0.990% | 0.990% | 0.984% (0.092%) | 0.990% | 94.0% | 0.862% | 5.5% |
| R150_D100 | 0 | 0 | 0.389% | 0.389% | 0.394% (0.029%) | 0.389% | 96.0% | 0.408% | 70.0% |

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

#### R150_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 0.73% [0.66%, 0.80%] | 0.22% | ×3.28 [2.96, 3.62] | reference | 42,578 | 2.0% | 0.000% | pass |
| First hop, credential | 0.73% [0.66%, 0.80%] | 0.22% | ×3.28 [2.97, 3.62] | +0.00 [+0.00, +0.00] | 851,560 | 0.9% | 0.000% | pass |
| Combined | 1.25% [1.17%, 1.32%] | 0.28% | ×4.41 [4.14, 4.67] | +0.52 [+0.47, +0.57] | 851,560 | 18.1% | 0.001% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 0.73% [0.66%, 0.80%] | 0.22% | ×3.29 | +0.00 [+0.00, +0.00] | 423,020 | 1.0% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.27% | 0.73% [0.66%, 0.80%] | 0.22% | ×3.30 | +0.01 [-0.01, +0.03] | 249,242 | 1.5% | 0.000% | pass |
| destination only | yes | 11.93% | 4.18% [3.88%, 4.49%] | 0.63% | ×6.64 | +3.45 [+3.16, +3.74] | 101,552 | 26.2% | 0.005% | pass |
| credential first relay + content destination | yes | 0.50% | 6.44% [5.61%, 7.35%] | 0.83% | ×7.73 | +5.85 [+5.01, +6.76] | 4,236 | 53.2% | 0.543% | fail |
| content first relay + content destination | yes | 0.50% | 6.10% [5.33%, 6.90%] | 0.83% | ×7.32 | +5.63 [+4.82, +6.43] | 4,264 | 45.1% | 0.164% | fail |
| content first relay + credential destination | yes | 0.52% | unstable | 0.22% | | | 4,457 | | | unstable (125 runs needed) |
| second relay + destination | yes | 1.42% | 4.09% [3.67%, 4.54%] | 0.64% | ×6.42 | +3.33 [+2.90, +3.80] | 12,122 | 30.5% | 0.008% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.63% | | | 1,103 | | | unstable (139 runs needed) |
| second relay + first relay | no | 1.14% | 0.68% [0.52%, 0.85%] | 0.22% | ×3.08 | +0.00 [+0.00, +0.00] | 9,676 | 7.2% | 0.000% | pass |
| second relay + second relay | no | 0.51% | unstable | 0.22% | | | 4,349 | | | unstable (167 runs needed) |
| gatekeeper + first relay | no | 2.12% | 0.71% [0.58%, 0.84%] | 0.22% | ×3.20 | -0.03 [-0.12, +0.06] | 18,056 | 2.1% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 0.67% [0.54%, 0.81%] | 0.22% | ×3.01 | -0.09 [-0.20, +0.04] | 16,005 | 2.3% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.22% | | | 3,478 | | | unstable (186 runs needed) |
| every record the node can select |  | 15.00% | 4.19% [3.90%, 4.50%] | 0.63% | ×6.65 | +3.46 [+3.16, +3.78] | 127,734 | 26.5% | 0.009% | pass |
| first relay held |  | 4.78% | 1.89% [1.72%, 2.06%] | 0.35% | ×5.39 | +1.18 [+1.03, +1.34] | 40,689 | 24.3% | 0.042% | pass |
| no first relay held |  | 95.22% | 1.22% [1.15%, 1.29%] | 0.28% | ×4.35 | +0.49 [+0.44, +0.53] | 810,871 | 17.7% | 0.001% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 42,578 |
| D or G | +0.00 [+0.00, +0.00] | 85,156 |

### Credential path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 96.0% |
| R150_D100 | 95.9% |

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

#### R150_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.18% [2.05%, 2.31%] | 0.44% | ×4.96 [4.66, 5.25] | reference | 46,499 | 6.3% | 0.000% | pass |
| First hop, credential | 2.19% [2.06%, 2.32%] | 0.44% | ×4.98 [4.69, 5.27] | +0.01 [-0.01, +0.02] | 929,980 | 4.6% | 0.000% | pass |
| Combined | 2.26% [2.14%, 2.38%] | 0.45% | ×5.03 [4.75, 5.30] | +0.08 [+0.06, +0.10] | 929,980 | 4.7% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.70% | 2.20% [2.07%, 2.34%] | 0.44% | ×5.01 | +0.01 [-0.01, +0.03] | 462,164 | 4.7% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.24% | 2.16% [2.03%, 2.29%] | 0.44% | ×4.92 | +0.01 [-0.02, +0.04] | 271,958 | 4.7% | 0.000% | pass |
| destination only | yes | 11.92% | 2.67% [2.55%, 2.80%] | 0.51% | ×5.28 | +0.49 [+0.40, +0.60] | 110,819 | 6.3% | 0.000% | pass |
| credential first relay + content destination | yes | 0.51% | 2.98% [2.48%, 3.49%] | 0.54% | ×5.52 | +0.70 [+0.12, +1.28] | 4,701 | 14.2% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 3.35% [2.86%, 3.87%] | 0.54% | ×6.24 | +0.72 [+0.17, +1.27] | 4,711 | 19.9% | 0.064% | pass |
| content first relay + credential destination | yes | 0.52% | 2.08% [1.66%, 2.52%] | 0.44% | ×4.73 | +0.06 [-0.08, +0.21] | 4,857 | 7.3% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 2.58% [2.30%, 2.87%] | 0.51% | ×5.09 | +0.56 [+0.31, +0.83] | 13,139 | 7.6% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 0.51% | | | 1,270 | | | unstable (152 runs needed) |
| second relay + first relay | no | 1.17% | 2.25% [1.99%, 2.51%] | 0.44% | ×5.12 | +0.06 [-0.01, +0.14] | 10,877 | 9.1% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 2.37% [1.94%, 2.77%] | 0.44% | ×5.40 | -0.02 [-0.13, +0.08] | 4,759 | 19.6% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 2.12% [1.91%, 2.34%] | 0.44% | ×4.82 | -0.03 [-0.16, +0.10] | 19,532 | 10.4% | 0.000% | pass |
| gatekeeper + second relay | no | 1.87% | 2.20% [1.97%, 2.46%] | 0.44% | ×5.01 | -0.14 [-0.29, +0.01] | 17,425 | 7.3% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 2.28% [1.83%, 2.73%] | 0.44% | ×5.19 | +0.05 [-0.21, +0.31] | 3,768 | 9.2% | 0.000% | pass |
| every record the node can select |  | 15.00% | 2.68% [2.56%, 2.79%] | 0.51% | ×5.29 | +0.50 [+0.42, +0.58] | 139,497 | 6.5% | 0.000% | pass |
| first relay held |  | 4.80% | 2.37% [2.20%, 2.53%] | 0.46% | ×5.14 | +0.16 [+0.07, +0.25] | 44,678 | 8.6% | 0.000% | pass |
| no first relay held |  | 95.20% | 2.26% [2.13%, 2.38%] | 0.45% | ×5.03 | +0.08 [+0.05, +0.10] | 885,302 | 4.5% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.02 [-0.02, +0.06] | 46,499 |
| D or G | +0.04 [+0.01, +0.07] | 92,998 |

### Content paths set the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 98.0% |
| R150_D100 | 98.1% |

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

#### R150_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 10.96% [10.58%, 11.34%] | 3.70% | ×2.96 [2.86, 3.06] | reference | 48,148 | 24.4% | 0.000% | pass |
| First hop, credential | 10.99% [10.62%, 11.37%] | 3.70% | ×2.97 [2.87, 3.07] | +0.03 [+0.00, +0.06] | 962,960 | 21.5% | 0.000% | pass |
| Combined | 11.21% [10.85%, 11.58%] | 3.70% | ×3.03 [2.93, 3.13] | +0.26 [+0.21, +0.30] | 962,960 | 24.6% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.64% | 10.94% [10.58%, 11.30%] | 3.70% | ×2.95 | -0.03 [-0.07, +0.01] | 477,971 | 21.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.34% | 11.03% [10.65%, 11.41%] | 3.70% | ×2.98 | +0.11 [+0.05, +0.17] | 282,502 | 23.0% | 0.000% | pass |
| destination only | yes | 11.94% | 12.48% [12.11%, 12.84%] | 3.70% | ×3.37 | +1.54 [+1.39, +1.70] | 115,024 | 30.0% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 12.74% [11.76%, 13.81%] | 3.70% | ×3.44 | +1.87 [+1.08, +2.67] | 4,859 | 48.7% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 13.80% [12.72%, 14.92%] | 3.70% | ×3.73 | +2.78 [+2.00, +3.59] | 4,861 | 44.5% | 0.309% | fail |
| content first relay + credential destination | yes | 0.52% | 11.48% [10.53%, 12.47%] | 3.70% | ×3.10 | +0.50 [+0.14, +0.84] | 5,002 | 30.8% | 0.000% | pass |
| second relay + destination | yes | 1.39% | 12.55% [11.95%, 13.21%] | 3.70% | ×3.39 | +1.47 [+1.10, +1.85] | 13,406 | 31.8% | 0.007% | pass |
| three or more roles, with a destination | yes | 0.13% | 11.46% [9.76%, 13.15%] | 3.70% | ×3.09 | +0.46 [-0.71, +1.69] | 1,292 | 70.9% | 0.000% | fail |
| second relay + first relay | no | 1.15% | 10.80% [10.23%, 11.38%] | 3.70% | ×2.92 | +0.42 [+0.23, +0.62] | 11,085 | 28.2% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 10.97% [9.96%, 11.91%] | 3.70% | ×2.96 | -0.04 [-0.29, +0.18] | 5,032 | 33.0% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 11.26% [10.74%, 11.78%] | 3.70% | ×3.04 | +0.22 [+0.03, +0.41] | 20,154 | 30.1% | 0.000% | pass |
| gatekeeper + second relay | no | 1.85% | 11.40% [10.84%, 11.95%] | 3.70% | ×3.08 | -0.05 [-0.22, +0.13] | 17,827 | 30.9% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 11.18% [10.03%, 12.31%] | 3.70% | ×3.02 | +0.13 [-0.20, +0.45] | 3,945 | 54.1% | 0.000% | fail |
| every record the node can select |  | 15.00% | 12.50% [12.16%, 12.83%] | 3.70% | ×3.37 | +1.54 [+1.41, +1.68] | 144,444 | 30.0% | 0.000% | pass |
| first relay held |  | 4.77% | 11.60% [11.20%, 11.99%] | 3.70% | ×3.13 | +0.74 [+0.59, +0.90] | 45,961 | 31.0% | 0.024% | pass |
| no first relay held |  | 95.23% | 11.19% [10.85%, 11.54%] | 3.70% | ×3.02 | +0.23 [+0.19, +0.28] | 916,999 | 24.5% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.05 [-0.11, +0.01] | 48,148 |
| D or G | +0.52 [+0.45, +0.60] | 96,296 |

### F content path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 97.0% |
| R150_D100 | 96.9% |

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

#### R150_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 6.19% [5.96%, 6.42%] | 2.50% | ×2.48 [2.38, 2.57] | reference | 69,477 | 9.4% | 0.000% | pass |
| First hop, credential | 6.21% [5.98%, 6.45%] | 2.50% | ×2.48 [2.39, 2.58] | +0.02 [+0.00, +0.04] | 1,389,540 | 7.9% | 0.000% | pass |
| Combined | 6.58% [6.36%, 6.80%] | 2.50% | ×2.63 [2.54, 2.72] | +0.39 [+0.36, +0.43] | 1,389,540 | 18.5% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | 6.19% [5.96%, 6.42%] | 2.50% | ×2.48 | +0.00 [-0.03, +0.04] | 690,305 | 8.0% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.26% | 6.24% [6.01%, 6.49%] | 2.50% | ×2.50 | +0.05 [+0.01, +0.10] | 406,530 | 8.9% | 0.000% | pass |
| destination only | yes | 11.94% | 8.64% [8.42%, 8.86%] | 2.50% | ×3.46 | +2.48 [+2.38, +2.58] | 165,928 | 27.3% | 0.001% | pass |
| credential first relay + content destination | yes | 0.50% | 9.95% [9.19%, 10.73%] | 2.50% | ×3.98 | +3.47 [+2.73, +4.21] | 6,947 | 36.0% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 9.29% [8.56%, 10.07%] | 2.50% | ×3.72 | +3.04 [+2.44, +3.68] | 6,963 | 43.0% | 0.014% | pass |
| content first relay + credential destination | yes | 0.52% | 6.39% [5.78%, 7.01%] | 2.50% | ×2.55 | +0.17 [-0.03, +0.36] | 7,233 | 11.5% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 8.70% [8.31%, 9.08%] | 2.50% | ×3.48 | +2.36 [+1.97, +2.68] | 19,560 | 33.7% | 0.005% | pass |
| three or more roles, with a destination | yes | 0.13% | 8.06% [6.83%, 9.39%] | 2.50% | ×3.22 | +2.39 [+1.40, +3.31] | 1,800 | 39.2% | 0.000% | pass |
| second relay + first relay | no | 1.15% | 6.31% [5.85%, 6.73%] | 2.50% | ×2.52 | +0.16 [+0.03, +0.29] | 15,938 | 12.7% | 0.000% | pass |
| second relay + second relay | no | 0.51% | 6.38% [5.82%, 6.96%] | 2.50% | ×2.55 | +0.11 [-0.07, +0.31] | 7,131 | 15.4% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 6.28% [5.93%, 6.64%] | 2.50% | ×2.51 | +0.29 [+0.13, +0.44] | 29,245 | 12.3% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 6.37% [5.99%, 6.72%] | 2.50% | ×2.55 | +0.13 [-0.03, +0.29] | 26,189 | 12.8% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 6.39% [5.63%, 7.18%] | 2.50% | ×2.56 | +0.03 [-0.23, +0.29] | 5,771 | 14.1% | 0.000% | pass |
| every record the node can select |  | 15.00% | 8.63% [8.40%, 8.85%] | 2.50% | ×3.45 | +2.44 [+2.35, +2.53] | 208,431 | 27.2% | 0.001% | pass |
| first relay held |  | 4.77% | 7.00% [6.72%, 7.28%] | 2.50% | ×2.80 | +0.87 [+0.73, +1.00] | 66,326 | 22.8% | 0.002% | pass |
| no first relay held |  | 95.23% | 6.56% [6.34%, 6.78%] | 2.50% | ×2.62 | +0.37 [+0.34, +0.40] | 1,323,214 | 18.3% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.01 [-0.06, +0.05] | 69,477 |
| D or G | +0.23 [+0.19, +0.27] | 138,954 |

## Cost per run

| Configuration | Cell | Simulation | Scoring | Shuffle test |
|---|---|---|---|---|
| Main run | R1_D100 | 2.5 s | 22.8 s | 0.2 s |
| Main run | R150_D100 | 0.3 s | 86.7 s | 0.3 s |
| Every hold off | R1_D100 | 2.3 s | 17.2 s | 0.0 s |
| Every hold off | R150_D100 | 0.3 s | 25.2 s | 0.0 s |
| Credential path sets the record time | R1_D100 | 2.3 s | 23.1 s | 0.0 s |
| Credential path sets the record time | R150_D100 | 0.3 s | 98.5 s | 0.0 s |
| Content paths set the record time | R1_D100 | 2.2 s | 21.6 s | 0.0 s |
| Content paths set the record time | R150_D100 | 0.3 s | 92.2 s | 0.0 s |
| F content path sets the record time | R1_D100 | 2.5 s | 31.6 s | 0.0 s |
| F content path sets the record time | R150_D100 | 0.4 s | 214.1 s | 0.0 s |

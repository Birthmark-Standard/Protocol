# Tables

Main run: D = 1171.3 s; rates are R / D and 100 / D. Intervals are 95% and resample whole runs. Device named: the vantage names the device behind a registry record. Chance, feasible set: a uniform guess among the devices whose packets could have produced the record. A row with fewer than 50 right or 50 wrong device-level decisions is unstable and shows no estimate.

## In flight

| Configuration | Cell | Real in flight (target) | Decoys in flight (target) | Runs |
|---|---|---|---|---|
| Main run | R1_D100 | 0.99 (1) | 99.63 (100) | 200 |
| Main run | R100_D100 | 98.12 (100) | 99.03 (100) | 200 |
| Main run | R500_D100 | 496.99 (500) | 99.12 (100) | 200 |
| Every hold off | R1_D100 | 0.99 (1) | 99.96 (100) | 50 |
| Every hold off | R100_D100 | 100.58 (100) | 102.05 (100) | 50 |
| Every hold off | R500_D100 | 507.22 (500) | 101.43 (100) | 50 |
| Credential path sets the record time | R1_D100 | 1.00 (1) | 100.01 (100) | 100 |
| Credential path sets the record time | R100_D100 | 99.03 (100) | 99.85 (100) | 100 |
| Credential path sets the record time | R500_D100 | 499.97 (500) | 99.44 (100) | 100 |
| Content paths set the record time | R1_D100 | 1.00 (1) | 100.43 (100) | 100 |
| Content paths set the record time | R100_D100 | 99.55 (100) | 100.24 (100) | 100 |
| Content paths set the record time | R500_D100 | 501.82 (500) | 99.97 (100) | 100 |
| F content path sets the record time | R1_D100 | 1.00 (1) | 100.98 (100) | 100 |
| F content path sets the record time | R100_D100 | 99.78 (100) | 100.60 (100) | 100 |
| F content path sets the record time | R500_D100 | 505.64 (500) | 102.02 (100) | 100 |

## Timing (main run, R = 100)

| Stage | Mean | Std dev | Maximum |
|---|---|---|---|
| device, credential channel | 119.6 s | 102.9 s | 360.0 s |
| device, content channels | 240.8 s | 207.7 s | 720.0 s |
| first relay hops (A, D, G) | 59.9 s | 51.2 s | 180.0 s |
| second relay hops (B, E, H) | 298.4 s | 257.4 s | 900.0 s |
| C before CV-1 | 30.1 s | 25.4 s | 90.0 s |
| V before CV-2 | 29.9 s | 25.2 s | 90.0 s |
| C fan-out, per leg | 45.0 s | 31.0 s | 179.6 s |
| gatekeeper hold | 30.0 s | 25.2 s | 90.0 s |
| departure bundling wait | 101.6 s | 90.9 s | 360.0 s |
| F/I pre-match hold | 119.7 s | 103.3 s | 360.0 s |
| post-match lottery | 30.0 s | 25.2 s | 90.0 s |
| registry bundle wait | 59.9 s | 34.6 s | 120.0 s |
| registry posting wait | 58.8 s | 34.1 s | 119.0 s |
| capture to finalization | 1160.3 s | 299.3 s | 2330.6 s |

| Cell | Mean capture to finalization [95% CI] |
|---|---|
| R1_D100 | 1164.2 s [1158.7, 1169.6] |
| R100_D100 | 1160.3 s [1154.6, 1165.7] |
| R500_D100 | 1164.0 s [1158.3, 1169.5] |

## R1_D100: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 4.88% [4.53%, 5.23%] | 1.10% | ×4.44 [4.12, 4.76] | reference | 39,880 | 13.1% | 0.000% | pass |
| First hop, credential | 4.88% [4.53%, 5.22%] | 1.10% | ×4.44 [4.12, 4.75] | -0.01 [-0.03, +0.02] | 797,600 | 10.3% | 0.000% | pass |
| First hop, content | 4.88% [4.53%, 5.22%] | 1.10% | ×4.44 [4.12, 4.75] | -0.01 [-0.03, +0.02] | 797,600 | 10.3% | 0.000% | pass |
| Credential processor | 4.87% [4.54%, 5.22%] | 1.10% | ×4.43 [4.14, 4.75] | -0.01 [-0.03, +0.01] | 677,960 | 10.5% | 0.000% | pass |
| Validator | 5.21% [4.91%, 5.50%] | 1.18% | ×4.42 [4.17, 4.67] | +0.32 [+0.03, +0.64] | 39,880 | 11.1% | 0.000% | pass |
| Gatekeeper | 4.89% [4.55%, 5.22%] | 1.10% | ×4.45 [4.14, 4.75] | +0.00 [-0.06, +0.06] | 119,640 | 11.3% | 0.000% | pass |
| Content server | 5.63% [5.31%, 5.94%] | 1.12% | ×5.01 [4.72, 5.29] | +0.75 [+0.58, +0.92] | 79,760 | 13.9% | 0.001% | pass |
| Combined | 4.95% [4.60%, 5.29%] | 1.10% | ×4.50 [4.18, 4.80] | +0.07 [+0.03, +0.11] | 797,600 | 10.3% | 0.000% | pass |

### R1_D100: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 4.87% [4.53%, 5.19%] | 1.10% | ×4.43 [4.13, 4.73] | -0.01 [-0.03, +0.02] | 724,426 | 10.4% | 0.000% | pass |
| First hop, content | 4.87% [4.54%, 5.21%] | 1.10% | ×4.43 [4.13, 4.74] | -0.01 [-0.03, +0.02] | 724,426 | 10.4% | 0.000% | pass |
| Credential processor | 4.87% [4.52%, 5.20%] | 1.10% | ×4.43 [4.12, 4.74] | -0.01 [-0.03, +0.01] | 639,655 | 10.5% | 0.000% | pass |
| Gatekeeper | 4.87% [4.53%, 5.22%] | 1.10% | ×4.43 [4.12, 4.75] | +0.01 [-0.05, +0.07] | 84,771 | 12.2% | 0.000% | pass |
| Content server | 5.62% [5.28%, 5.93%] | 1.12% | ×5.00 [4.70, 5.27] | +0.80 [+0.62, +1.00] | 63,425 | 14.7% | 0.000% | pass |

### R1_D100: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.74% | 4.89% [4.55%, 5.24%] | 1.10% | ×4.45 | -0.01 [-0.04, +0.02] | 396,689 | 10.3% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.17% | 4.85% [4.49%, 5.20%] | 1.10% | ×4.42 | +0.00 [-0.04, +0.05] | 232,645 | 11.2% | 0.000% | pass |
| destination only | yes | 11.92% | 5.36% [5.06%, 5.68%] | 1.12% | ×4.81 | +0.53 [+0.40, +0.66] | 95,092 | 13.3% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 5.52% [4.79%, 6.25%] | 1.12% | ×4.91 | +0.47 [-0.15, +1.13] | 4,020 | 29.1% | 0.000% | pass |
| content first relay + content destination | yes | 0.52% | 5.23% [4.58%, 5.91%] | 1.12% | ×4.65 | +0.07 [-0.54, +0.67] | 4,167 | 19.0% | 0.024% | pass |
| content first relay + credential destination | yes | 0.51% | 5.06% [4.32%, 5.86%] | 1.10% | ×4.61 | +0.17 [+0.00, +0.35] | 4,088 | 8.6% | 0.000% | pass |
| second relay + destination | yes | 1.41% | 5.56% [5.04%, 6.05%] | 1.12% | ×4.98 | +0.44 [+0.08, +0.79] | 11,207 | 18.9% | 0.027% | pass |
| three or more roles, with a destination | yes | 0.13% | 5.53% [4.17%, 6.94%] | 1.12% | ×4.95 | +0.56 [-0.45, +1.64] | 1,066 | 25.9% | 0.000% | pass |
| second relay + first relay | no | 1.16% | 4.89% [4.36%, 5.46%] | 1.10% | ×4.45 | -0.01 [-0.14, +0.13] | 9,260 | 18.7% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 4.69% [4.01%, 5.41%] | 1.10% | ×4.27 | -0.12 [-0.27, +0.00] | 4,111 | 19.4% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 4.92% [4.46%, 5.39%] | 1.10% | ×4.48 | +0.11 [-0.00, +0.21] | 16,753 | 17.7% | 0.000% | pass |
| gatekeeper + second relay | no | 1.90% | 5.03% [4.59%, 5.51%] | 1.10% | ×4.58 | -0.02 [-0.15, +0.11] | 15,169 | 11.7% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | 4.98% [4.23%, 5.80%] | 1.10% | ×4.54 | +0.15 [-0.09, +0.39] | 3,333 | 19.6% | 0.000% | pass |
| every record the node can select |  | 15.00% | 5.37% [5.07%, 5.68%] | 1.12% | ×4.82 | +0.49 [+0.37, +0.61] | 119,640 | 12.9% | 0.001% | pass |
| first relay held |  | 4.80% | 5.03% [4.63%, 5.41%] | 1.10% | ×4.55 | +0.12 [+0.01, +0.24] | 38,288 | 13.6% | 0.003% | pass |
| no first relay held |  | 95.20% | 4.95% [4.61%, 5.29%] | 1.10% | ×4.49 | +0.07 [+0.03, +0.11] | 759,312 | 10.3% | 0.000% | pass |

## R100_D100: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.60% [2.42%, 2.78%] | 0.56% | ×4.69 [4.37, 5.02] | reference | 43,631 | 4.7% | 0.000% | pass |
| First hop, credential | 2.60% [2.42%, 2.78%] | 0.56% | ×4.68 [4.36, 5.00] | -0.00 [-0.02, +0.02] | 872,620 | 3.2% | 0.000% | pass |
| First hop, content | 2.60% [2.43%, 2.78%] | 0.56% | ×4.68 [4.37, 5.00] | -0.00 [-0.02, +0.02] | 872,620 | 3.2% | 0.000% | pass |
| Credential processor | 2.60% [2.43%, 2.78%] | 0.56% | ×4.69 [4.37, 5.01] | +0.00 [-0.01, +0.01] | 741,727 | 3.1% | 0.000% | pass |
| Validator | 2.69% [2.52%, 2.86%] | 0.59% | ×4.52 [4.23, 4.81] | +0.09 [-0.10, +0.27] | 43,631 | 6.2% | 0.000% | pass |
| Gatekeeper | 2.61% [2.44%, 2.78%] | 0.56% | ×4.71 [4.39, 5.00] | +0.01 [-0.03, +0.05] | 130,893 | 4.0% | 0.000% | pass |
| Content server | 3.12% [2.95%, 3.28%] | 0.57% | ×5.50 [5.20, 5.78] | +0.52 [+0.40, +0.64] | 87,262 | 5.9% | 0.000% | pass |
| Combined | 2.65% [2.48%, 2.82%] | 0.56% | ×4.77 [4.46, 5.07] | +0.05 [+0.02, +0.08] | 872,620 | 3.3% | 0.000% | pass |

### R100_D100: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 2.60% [2.42%, 2.77%] | 0.56% | ×4.67 [4.37, 4.99] | -0.00 [-0.02, +0.02] | 793,133 | 3.1% | 0.000% | pass |
| First hop, content | 2.60% [2.42%, 2.77%] | 0.56% | ×4.67 [4.36, 4.99] | -0.00 [-0.02, +0.02] | 793,133 | 3.1% | 0.000% | pass |
| Credential processor | 2.60% [2.43%, 2.78%] | 0.56% | ×4.69 [4.38, 5.01] | +0.00 [-0.01, +0.01] | 700,241 | 3.1% | 0.000% | pass |
| Gatekeeper | 2.59% [2.41%, 2.77%] | 0.56% | ×4.67 [4.34, 5.00] | +0.02 [-0.03, +0.07] | 92,892 | 3.7% | 0.000% | pass |
| Content server | 3.15% [2.98%, 3.34%] | 0.57% | ×5.55 [5.24, 5.87] | +0.51 [+0.37, +0.64] | 69,773 | 6.4% | 0.000% | pass |

### R100_D100: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.65% | 2.60% [2.44%, 2.78%] | 0.56% | ×4.69 | +0.00 [-0.02, +0.02] | 433,230 | 3.7% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.28% | 2.59% [2.42%, 2.76%] | 0.56% | ×4.67 | +0.01 [-0.03, +0.04] | 255,470 | 3.1% | 0.000% | pass |
| destination only | yes | 11.97% | 2.94% [2.77%, 3.12%] | 0.56% | ×5.22 | +0.32 [+0.23, +0.42] | 104,433 | 5.8% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 2.71% [2.25%, 3.19%] | 0.57% | ×4.76 | +0.65 [+0.23, +1.09] | 4,285 | 15.5% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 2.95% [2.45%, 3.45%] | 0.57% | ×5.20 | +0.27 [-0.16, +0.73] | 4,403 | 8.0% | 0.000% | pass |
| content first relay + credential destination | yes | 0.51% | 2.69% [2.22%, 3.16%] | 0.56% | ×4.84 | +0.07 [-0.05, +0.18] | 4,464 | 20.7% | 0.000% | pass |
| second relay + destination | yes | 1.39% | 2.99% [2.67%, 3.31%] | 0.56% | ×5.31 | +0.39 [+0.18, +0.61] | 12,171 | 8.1% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.56% | | | 1,137 | | | unstable (239 runs needed) |
| second relay + first relay | no | 1.15% | 2.70% [2.33%, 3.07%] | 0.56% | ×4.87 | -0.03 [-0.10, +0.03] | 10,070 | 5.4% | 0.000% | pass |
| second relay + second relay | no | 0.53% | 2.30% [1.91%, 2.74%] | 0.56% | ×4.14 | -0.11 [-0.26, +0.02] | 4,616 | 14.5% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 2.75% [2.48%, 3.04%] | 0.56% | ×4.96 | +0.01 [-0.09, +0.10] | 18,451 | 8.3% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 2.72% [2.41%, 3.04%] | 0.56% | ×4.90 | +0.09 [-0.01, +0.19] | 16,401 | 4.3% | 0.000% | pass |
| three or more roles, no destination | no | 0.40% | 2.49% [2.00%, 3.03%] | 0.56% | ×4.49 | +0.03 [-0.12, +0.20] | 3,489 | 26.0% | 0.000% | pass |
| every record the node can select |  | 15.00% | 2.94% [2.77%, 3.09%] | 0.56% | ×5.21 | +0.34 [+0.26, +0.42] | 130,893 | 5.8% | 0.000% | pass |
| first relay held |  | 4.78% | 2.75% [2.54%, 2.96%] | 0.56% | ×4.93 | +0.10 [+0.01, +0.19] | 41,673 | 4.1% | 0.000% | pass |
| no first relay held |  | 95.22% | 2.65% [2.48%, 2.81%] | 0.56% | ×4.76 | +0.05 [+0.02, +0.08] | 830,947 | 3.5% | 0.000% | pass |

## R500_D100: every vantage on all its records

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 0.93% [0.84%, 1.01%] | 0.18% | ×5.02 [4.55, 5.50] | reference | 44,055 | 3.8% | 0.000% | pass |
| First hop, credential | 0.93% [0.85%, 1.02%] | 0.18% | ×5.05 [4.58, 5.51] | +0.01 [-0.00, +0.02] | 881,100 | 2.3% | 0.000% | pass |
| First hop, content | 0.93% [0.85%, 1.02%] | 0.18% | ×5.05 [4.58, 5.53] | +0.01 [-0.00, +0.02] | 881,100 | 2.3% | 0.000% | pass |
| Credential processor | 0.93% [0.84%, 1.01%] | 0.18% | ×5.01 [4.55, 5.47] | -0.00 [-0.01, +0.00] | 748,935 | 2.4% | 0.000% | pass |
| Validator | 1.02% [0.93%, 1.11%] | 0.20% | ×5.16 [4.69, 5.62] | +0.10 [-0.01, +0.20] | 44,055 | 3.5% | 0.000% | pass |
| Gatekeeper | 0.94% [0.85%, 1.02%] | 0.18% | ×5.09 [4.63, 5.55] | +0.01 [-0.01, +0.03] | 132,165 | 2.9% | 0.000% | pass |
| Content server | 1.13% [1.05%, 1.22%] | 0.19% | ×6.00 [5.54, 6.44] | +0.21 [+0.13, +0.28] | 88,110 | 4.4% | 0.000% | pass |
| Combined | 0.95% [0.88%, 1.03%] | 0.18% | ×5.15 [4.73, 5.56] | +0.03 [+0.01, +0.04] | 881,100 | 2.3% | 0.000% | pass |

### R500_D100: each node vantage on the records in which the node held no coincident role

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| First hop, credential | 0.93% [0.85%, 1.02%] | 0.18% | ×5.04 [4.59, 5.52] | +0.00 [-0.01, +0.01] | 800,085 | 2.3% | 0.000% | pass |
| First hop, content | 0.93% [0.84%, 1.02%] | 0.18% | ×5.04 [4.56, 5.52] | +0.00 [-0.01, +0.01] | 800,085 | 2.3% | 0.000% | pass |
| Credential processor | 0.93% [0.84%, 1.01%] | 0.18% | ×5.02 [4.55, 5.47] | -0.00 [-0.01, +0.00] | 706,482 | 2.4% | 0.000% | pass |
| Gatekeeper | 0.92% [0.84%, 1.00%] | 0.18% | ×4.98 [4.54, 5.44] | +0.01 [-0.01, +0.04] | 93,603 | 3.0% | 0.000% | pass |
| Content server | 1.14% [1.05%, 1.24%] | 0.19% | ×6.06 [5.56, 6.54] | +0.25 [+0.16, +0.33] | 70,026 | 5.1% | 0.000% | pass |

### R500_D100: the combined view by the roles the node held

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.75% | 0.93% [0.84%, 1.02%] | 0.18% | ×5.05 | +0.00 [-0.01, +0.01] | 438,349 | 2.4% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.15% | 0.93% [0.85%, 1.02%] | 0.18% | ×5.04 | +0.01 [-0.00, +0.03] | 256,884 | 2.8% | 0.000% | pass |
| destination only | yes | 11.90% | 1.08% [1.00%, 1.16%] | 0.19% | ×5.77 | +0.16 [+0.10, +0.22] | 104,852 | 4.3% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | unstable | 0.19% | | | 4,435 | | | unstable (233 runs needed) |
| content first relay + content destination | yes | 0.52% | 1.16% [0.87%, 1.47%] | 0.19% | ×6.13 | -0.04 [-0.38, +0.28] | 4,580 | 11.3% | 0.000% | pass |
| content first relay + credential destination | yes | 0.54% | unstable | 0.18% | | | 4,714 | | | unstable (239 runs needed) |
| second relay + destination | yes | 1.41% | 0.93% [0.76%, 1.10%] | 0.19% | ×4.97 | +0.06 [-0.09, +0.21] | 12,453 | 5.6% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.19% | | | 1,131 | | | unstable (910 runs needed) |
| second relay + first relay | no | 1.15% | 0.93% [0.75%, 1.12%] | 0.18% | ×5.03 | +0.06 [+0.02, +0.11] | 10,126 | 8.4% | 0.000% | pass |
| second relay + second relay | no | 0.52% | unstable | 0.18% | | | 4,586 | | | unstable (278 runs needed) |
| gatekeeper + first relay | no | 2.12% | 1.01% [0.85%, 1.16%] | 0.18% | ×5.45 | +0.01 [-0.04, +0.06] | 18,696 | 5.4% | 0.000% | pass |
| gatekeeper + second relay | no | 1.89% | 0.99% [0.82%, 1.15%] | 0.18% | ×5.35 | +0.05 [-0.01, +0.10] | 16,611 | 5.2% | 0.000% | pass |
| three or more roles, no destination | no | 0.42% | unstable | 0.18% | | | 3,683 | | | unstable (257 runs needed) |
| every record the node can select |  | 15.00% | 1.06% [0.98%, 1.13%] | 0.19% | ×5.64 | +0.13 [+0.08, +0.18] | 132,165 | 3.7% | 0.000% | pass |
| first relay held |  | 4.83% | 0.99% [0.88%, 1.10%] | 0.19% | ×5.32 | +0.04 [-0.02, +0.09] | 42,551 | 4.0% | 0.000% | pass |
| no first relay held |  | 95.17% | 0.95% [0.87%, 1.03%] | 0.18% | ×5.14 | +0.03 [+0.01, +0.04] | 838,549 | 2.4% | 0.000% | pass |

## Diagnostics

| Cell | Variant | Device named [95% CI] | Chance | Multiple of chance | Posted-time number [95% CI] | Change [95% CI] |
|---|---|---|---|---|---|---|
| R1_D100 | observer, timing evidence off | 3.40% [3.06%, 3.76%] | 1.10% | ×3.09 | 4.88% [4.54%, 5.22%] | n/a |
| R1_D100 | observer, record time at the midpoint | 5.16% [4.82%, 5.51%] | 1.12% | ×4.61 | 4.88% [4.54%, 5.23%] | +0.28 [+0.12, +0.43] |
| R1_D100 | content server, record time at the midpoint | 6.06% [5.76%, 6.35%] | 1.14% | ×5.32 | 5.63% [5.32%, 5.94%] | +0.43 [+0.28, +0.57] |
| R100_D100 | observer, timing evidence off | 1.76% [1.58%, 1.93%] | 0.56% | ×3.16 | 2.60% [2.43%, 2.78%] | n/a |
| R100_D100 | observer, record time at the midpoint | 2.81% [2.62%, 2.99%] | 0.57% | ×4.96 | 2.60% [2.42%, 2.78%] | +0.21 [+0.10, +0.32] |
| R100_D100 | content server, record time at the midpoint | 3.28% [3.11%, 3.46%] | 0.58% | ×5.69 | 3.12% [2.96%, 3.28%] | +0.15 [+0.04, +0.26] |
| R500_D100 | observer, timing evidence off | 0.67% [0.58%, 0.74%] | 0.18% | ×3.60 | 0.93% [0.84%, 1.01%] | n/a |
| R500_D100 | observer, record time at the midpoint | 1.11% [1.01%, 1.22%] | 0.19% | ×5.92 | 0.93% [0.84%, 1.01%] | +0.19 [+0.11, +0.26] |
| R500_D100 | content server, record time at the midpoint | 1.23% [1.14%, 1.32%] | 0.19% | ×6.44 | 1.13% [1.05%, 1.22%] | +0.10 [+0.02, +0.17] |

| Cell | Packet type | Observer submission hit [95% CI] | Random rate | Delay to record time, mean | Std dev |
|---|---|---|---|---|---|
| R1_D100 | credential | 0.51% [0.45%, 0.58%] | 0.17% | 1044.1 s | 303.9 s |
| R1_D100 | F content | 0.44% [0.38%, 0.51%] | 0.17% | 924.1 s | 311.6 s |
| R1_D100 | I content | 0.44% [0.37%, 0.50%] | 0.17% | 923.6 s | 311.8 s |
| R100_D100 | credential | 0.23% [0.19%, 0.28%] | 0.09% | 1040.7 s | 304.3 s |
| R100_D100 | F content | 0.21% [0.17%, 0.25%] | 0.09% | 920.6 s | 312.2 s |
| R100_D100 | I content | 0.23% [0.19%, 0.27%] | 0.09% | 918.3 s | 310.4 s |
| R500_D100 | credential | 0.05% [0.03%, 0.07%] | 0.03% | 1044.0 s | 306.2 s |
| R500_D100 | F content | 0.08% [0.06%, 0.11%] | 0.03% | 923.0 s | 311.9 s |
| R500_D100 | I content | 0.08% [0.05%, 0.11%] | 0.03% | 923.9 s | 311.9 s |

| Cell | Packet | Departure to arrival at its destination, mean | Std dev |
|---|---|---|---|
| R1_D100 | credential (at C) | 359.9 s | 263.7 s |
| R1_D100 | F content (at F) | 358.3 s | 261.9 s |
| R1_D100 | I content (at I) | 359.3 s | 263.7 s |
| R100_D100 | credential (at C) | 359.1 s | 261.5 s |
| R100_D100 | F content (at F) | 357.1 s | 262.6 s |
| R100_D100 | I content (at I) | 359.4 s | 263.0 s |
| R500_D100 | credential (at C) | 360.1 s | 263.4 s |
| R500_D100 | F content (at F) | 358.6 s | 263.4 s |
| R500_D100 | I content (at I) | 361.1 s | 264.3 s |

| Cell | Observer, first half of the window [95% CI] | Second half [95% CI] | Second minus first [95% CI] | Agree |
|---|---|---|---|---|
| R1_D100 | 5.39% [4.90%, 5.92%] | 4.38% [3.90%, 4.84%] | -1.01 [-1.71, -0.30] | no |
| R100_D100 | 2.60% [2.35%, 2.86%] | 2.60% [2.34%, 2.85%] | -0.00 [-0.39, +0.36] | yes |
| R500_D100 | 0.95% [0.83%, 1.07%] | 0.90% [0.78%, 1.04%] | -0.04 [-0.22, +0.14] | yes |

| Configuration | Cell | Real transactions introduced in the window | Never finalized (quorum timeout) |
|---|---|---|---|
| Main run | R1_D100 | 39,880 | 0 |
| Main run | R100_D100 | 43,631 | 0 |
| Main run | R500_D100 | 44,055 | 0 |
| Every hold off | R1_D100 | 9,964 | 0 |
| Every hold off | R100_D100 | 10,928 | 0 |
| Every hold off | R500_D100 | 11,182 | 0 |
| Credential path sets the record time | R1_D100 | 19,954 | 465 |
| Credential path sets the record time | R100_D100 | 21,886 | 505 |
| Credential path sets the record time | R500_D100 | 22,138 | 518 |
| Content paths set the record time | R1_D100 | 19,911 | 0 |
| Content paths set the record time | R100_D100 | 21,906 | 0 |
| Content paths set the record time | R500_D100 | 22,017 | 0 |
| F content path sets the record time | R1_D100 | 19,907 | 0 |
| F content path sets the record time | R100_D100 | 21,897 | 0 |
| F content path sets the record time | R500_D100 | 22,115 | 0 |

| Cell | F and I confirmations set by the match board |
|---|---|
| R1_D100 | 50.0% |
| R100_D100 | 50.2% |
| R500_D100 | 50.4% |

## Label shuffle

| Configuration | Cell | Vantage | Shuffled accuracy [95% CI] | Chance | Pass |
|---|---|---|---|---|---|
| Main run | R1_D100 | Passive observer | 0.96% [0.84%, 1.08%] | 0.97% | pass |
| Main run | R1_D100 | First hop | 0.96% [0.85%, 1.07%] | 0.97% | pass |
| Main run | R1_D100 | Credential processor | 0.96% [0.85%, 1.08%] | 0.97% | pass |
| Main run | R1_D100 | Validator | 0.88% [0.78%, 0.97%] | 0.96% | pass |
| Main run | R1_D100 | Gatekeeper | 0.97% [0.85%, 1.08%] | 0.97% | pass |
| Main run | R1_D100 | Content server | 0.92% [0.82%, 1.01%] | 0.97% | pass |
| Main run | R1_D100 | Combined | 0.96% [0.85%, 1.07%] | 0.97% | pass |
| Main run | R100_D100 | Passive observer | 0.39% [0.33%, 0.46%] | 0.49% | fail |
| Main run | R100_D100 | First hop | 0.40% [0.34%, 0.46%] | 0.49% | fail |
| Main run | R100_D100 | Credential processor | 0.40% [0.34%, 0.47%] | 0.49% | fail |
| Main run | R100_D100 | Validator | 0.45% [0.38%, 0.52%] | 0.49% | pass |
| Main run | R100_D100 | Gatekeeper | 0.40% [0.34%, 0.47%] | 0.49% | fail |
| Main run | R100_D100 | Content server | 0.44% [0.39%, 0.50%] | 0.49% | pass |
| Main run | R100_D100 | Combined | 0.40% [0.35%, 0.47%] | 0.49% | fail |
| Main run | R500_D100 | Passive observer | 0.15% [0.11%, 0.18%] | 0.16% | pass |
| Main run | R500_D100 | First hop | 0.15% [0.12%, 0.18%] | 0.16% | pass |
| Main run | R500_D100 | Credential processor | 0.15% [0.12%, 0.18%] | 0.16% | pass |
| Main run | R500_D100 | Validator | 0.15% [0.11%, 0.19%] | 0.16% | pass |
| Main run | R500_D100 | Gatekeeper | 0.15% [0.12%, 0.18%] | 0.16% | pass |
| Main run | R500_D100 | Content server | 0.13% [0.10%, 0.15%] | 0.16% | fail |
| Main run | R500_D100 | Combined | 0.15% [0.12%, 0.18%] | 0.16% | pass |
| Every hold off | R1_D100 | Passive observer | 0.01% [0.00%, 0.03%] | 0.02% | pass |
| Every hold off | R1_D100 | First hop | 0.01% [0.00%, 0.03%] | 0.02% | pass |
| Every hold off | R1_D100 | Credential processor | 0.01% [0.00%, 0.03%] | 0.02% | pass |
| Every hold off | R1_D100 | Validator | 0.00% [0.00%, 0.00%] | 0.02% | fail |
| Every hold off | R1_D100 | Gatekeeper | 0.03% [0.01%, 0.06%] | 0.02% | pass |
| Every hold off | R1_D100 | Content server | 0.01% [0.00%, 0.03%] | 0.02% | pass |
| Every hold off | R1_D100 | Combined | 0.01% [0.00%, 0.03%] | 0.02% | pass |
| Every hold off | R100_D100 | Passive observer | 0.03% [0.00%, 0.06%] | 0.05% | pass |
| Every hold off | R100_D100 | First hop | 0.03% [0.00%, 0.06%] | 0.05% | pass |
| Every hold off | R100_D100 | Credential processor | 0.03% [0.00%, 0.06%] | 0.05% | pass |
| Every hold off | R100_D100 | Validator | 0.03% [0.00%, 0.06%] | 0.05% | pass |
| Every hold off | R100_D100 | Gatekeeper | 0.03% [0.01%, 0.06%] | 0.05% | pass |
| Every hold off | R100_D100 | Content server | 0.03% [0.00%, 0.06%] | 0.05% | pass |
| Every hold off | R100_D100 | Combined | 0.03% [0.00%, 0.06%] | 0.05% | pass |
| Every hold off | R500_D100 | Passive observer | 0.02% [0.00%, 0.04%] | 0.02% | pass |
| Every hold off | R500_D100 | First hop | 0.02% [0.00%, 0.04%] | 0.02% | pass |
| Every hold off | R500_D100 | Credential processor | 0.02% [0.00%, 0.04%] | 0.02% | pass |
| Every hold off | R500_D100 | Validator | 0.02% [0.00%, 0.04%] | 0.02% | pass |
| Every hold off | R500_D100 | Gatekeeper | 0.02% [0.00%, 0.05%] | 0.02% | pass |
| Every hold off | R500_D100 | Content server | 0.04% [0.01%, 0.07%] | 0.02% | pass |
| Every hold off | R500_D100 | Combined | 0.02% [0.00%, 0.04%] | 0.02% | pass |
| Credential path sets the record time | R1_D100 | Passive observer | 0.92% [0.77%, 1.07%] | 0.97% | pass |
| Credential path sets the record time | R1_D100 | First hop | 0.92% [0.78%, 1.07%] | 0.97% | pass |
| Credential path sets the record time | R1_D100 | Credential processor | 0.91% [0.77%, 1.06%] | 0.97% | pass |
| Credential path sets the record time | R1_D100 | Validator | 0.86% [0.73%, 0.99%] | 0.97% | pass |
| Credential path sets the record time | R1_D100 | Gatekeeper | 0.94% [0.80%, 1.08%] | 0.97% | pass |
| Credential path sets the record time | R1_D100 | Content server | 0.88% [0.75%, 1.01%] | 0.97% | pass |
| Credential path sets the record time | R1_D100 | Combined | 0.91% [0.77%, 1.04%] | 0.97% | pass |
| Credential path sets the record time | R100_D100 | Passive observer | 0.52% [0.42%, 0.64%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | First hop | 0.53% [0.41%, 0.65%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Credential processor | 0.52% [0.41%, 0.65%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Validator | 0.52% [0.43%, 0.63%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Gatekeeper | 0.51% [0.41%, 0.62%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Content server | 0.50% [0.42%, 0.59%] | 0.49% | pass |
| Credential path sets the record time | R100_D100 | Combined | 0.52% [0.42%, 0.63%] | 0.49% | pass |
| Credential path sets the record time | R500_D100 | Passive observer | 0.15% [0.10%, 0.20%] | 0.16% | pass |
| Credential path sets the record time | R500_D100 | First hop | 0.14% [0.09%, 0.20%] | 0.16% | pass |
| Credential path sets the record time | R500_D100 | Credential processor | 0.15% [0.10%, 0.20%] | 0.16% | pass |
| Credential path sets the record time | R500_D100 | Validator | 0.18% [0.13%, 0.24%] | 0.16% | pass |
| Credential path sets the record time | R500_D100 | Gatekeeper | 0.14% [0.10%, 0.19%] | 0.16% | pass |
| Credential path sets the record time | R500_D100 | Content server | 0.18% [0.14%, 0.23%] | 0.16% | pass |
| Credential path sets the record time | R500_D100 | Combined | 0.15% [0.10%, 0.19%] | 0.16% | pass |
| Content paths set the record time | R1_D100 | Passive observer | 8.60% [8.06%, 9.13%] | 8.33% | pass |
| Content paths set the record time | R1_D100 | First hop | 8.60% [8.09%, 9.14%] | 8.33% | pass |
| Content paths set the record time | R1_D100 | Credential processor | 8.62% [8.07%, 9.15%] | 8.33% | pass |
| Content paths set the record time | R1_D100 | Validator | 8.70% [8.05%, 9.32%] | 8.33% | pass |
| Content paths set the record time | R1_D100 | Gatekeeper | 8.70% [8.18%, 9.26%] | 8.33% | pass |
| Content paths set the record time | R1_D100 | Content server | 8.77% [8.25%, 9.26%] | 8.33% | pass |
| Content paths set the record time | R1_D100 | Combined | 8.65% [8.13%, 9.17%] | 8.33% | pass |
| Content paths set the record time | R100_D100 | Passive observer | 4.30% [3.96%, 4.63%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | First hop | 4.31% [4.00%, 4.63%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Credential processor | 4.31% [4.00%, 4.65%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Validator | 4.54% [4.13%, 4.96%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Gatekeeper | 4.35% [4.02%, 4.67%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Content server | 4.42% [4.12%, 4.73%] | 4.55% | pass |
| Content paths set the record time | R100_D100 | Combined | 4.33% [4.03%, 4.67%] | 4.55% | pass |
| Content paths set the record time | R500_D100 | Passive observer | 1.43% [1.27%, 1.60%] | 1.52% | pass |
| Content paths set the record time | R500_D100 | First hop | 1.45% [1.29%, 1.60%] | 1.52% | pass |
| Content paths set the record time | R500_D100 | Credential processor | 1.44% [1.28%, 1.60%] | 1.52% | pass |
| Content paths set the record time | R500_D100 | Validator | 1.54% [1.36%, 1.72%] | 1.52% | pass |
| Content paths set the record time | R500_D100 | Gatekeeper | 1.43% [1.28%, 1.60%] | 1.52% | pass |
| Content paths set the record time | R500_D100 | Content server | 1.48% [1.34%, 1.62%] | 1.52% | pass |
| Content paths set the record time | R500_D100 | Combined | 1.45% [1.31%, 1.60%] | 1.52% | pass |
| F content path sets the record time | R1_D100 | Passive observer | 5.68% [5.08%, 6.26%] | 5.88% | pass |
| F content path sets the record time | R1_D100 | First hop | 5.69% [5.12%, 6.22%] | 5.88% | pass |
| F content path sets the record time | R1_D100 | Credential processor | 5.69% [5.11%, 6.23%] | 5.88% | pass |
| F content path sets the record time | R1_D100 | Validator | 5.76% [5.17%, 6.32%] | 5.88% | pass |
| F content path sets the record time | R1_D100 | Gatekeeper | 5.61% [5.07%, 6.15%] | 5.88% | pass |
| F content path sets the record time | R1_D100 | Content server | 5.73% [5.30%, 6.17%] | 5.88% | pass |
| F content path sets the record time | R1_D100 | Combined | 5.68% [5.14%, 6.22%] | 5.88% | pass |
| F content path sets the record time | R100_D100 | Passive observer | 2.89% [2.65%, 3.14%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | First hop | 2.91% [2.67%, 3.17%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Credential processor | 2.90% [2.67%, 3.14%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Validator | 3.11% [2.81%, 3.40%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Gatekeeper | 2.92% [2.67%, 3.16%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Content server | 2.95% [2.75%, 3.14%] | 3.12% | pass |
| F content path sets the record time | R100_D100 | Combined | 2.92% [2.70%, 3.16%] | 3.12% | pass |
| F content path sets the record time | R500_D100 | Passive observer | 1.03% [0.88%, 1.18%] | 1.04% | pass |
| F content path sets the record time | R500_D100 | First hop | 1.03% [0.88%, 1.18%] | 1.04% | pass |
| F content path sets the record time | R500_D100 | Credential processor | 1.02% [0.86%, 1.18%] | 1.04% | pass |
| F content path sets the record time | R500_D100 | Validator | 1.04% [0.91%, 1.16%] | 1.04% | pass |
| F content path sets the record time | R500_D100 | Gatekeeper | 1.04% [0.88%, 1.20%] | 1.04% | pass |
| F content path sets the record time | R500_D100 | Content server | 0.98% [0.87%, 1.09%] | 1.04% | pass |
| F content path sets the record time | R500_D100 | Combined | 1.02% [0.88%, 1.17%] | 1.04% | pass |

### Shuffle test (observer)

| Cell | Shuffle mismatches | Feasible-count mismatches | Exact expected accuracy | Exact expected chance | Mean accuracy over permutations (sd) | Mean chance over permutations | Interval coverage | Scored accuracy | Scored percentile |
|---|---|---|---|---|---|---|---|---|---|
| R1_D100 | 3 | 0 | 0.971% | 0.971% | 0.966% (0.061%) | 0.971% | 96.5% | 1.013% | 73.5% |
| R100_D100 | 0 | 0 | 0.491% | 0.491% | 0.491% (0.037%) | 0.491% | 94.5% | 0.424% | 2.0% |
| R500_D100 | 0 | 0 | 0.164% | 0.164% | 0.164% (0.018%) | 0.164% | 96.5% | 0.175% | 74.0% |

## Controls

### Every hold off

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 1.43% [1.12%, 1.74%] | 0.55% | ×2.61 [2.06, 3.19] | reference | 9,964 | 11.2% | 0.030% | pass |
| First hop, credential | 1.43% [1.13%, 1.75%] | 0.55% | ×2.61 [2.07, 3.20] | +0.00 [+0.00, +0.00] | 199,280 | 6.1% | 0.040% | pass |
| Combined | 2.48% [2.18%, 2.79%] | 0.70% | ×3.54 [3.11, 3.98] | +1.06 [+0.93, +1.19] | 199,280 | 40.2% | 0.161% | fail |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.76% | 1.40% [1.10%, 1.71%] | 0.55% | ×2.57 | +0.00 [+0.00, +0.00] | 99,162 | 6.7% | 0.062% | pass |
| one relay or gatekeeper role | no | 29.09% | 1.51% [1.22%, 1.78%] | 0.55% | ×2.76 | +0.04 [-0.03, +0.11] | 57,970 | 6.5% | 0.000% | pass |
| destination only | yes | 11.94% | 8.57% [7.63%, 9.43%] | 1.59% | ×5.40 | +7.07 [+6.21, +7.94] | 23,797 | 57.1% | 1.114% | fail |
| credential first relay + content destination | yes | 0.52% | 11.77% [9.49%, 13.91%] | 2.10% | ×5.61 | +10.80 [+8.55, +12.94] | 1,028 | 89.2% | 3.405% | fail |
| content first relay + content destination | yes | 0.49% | 12.18% [9.65%, 14.73%] | 2.10% | ×5.79 | +11.16 [+8.76, +13.50] | 977 | 83.2% | 1.945% | fail |
| content first relay + credential destination | yes | 0.50% | unstable | 0.55% | | | 1,005 | | | unstable (313 runs needed) |
| second relay + destination | yes | 1.41% | 7.70% [6.54%, 8.89%] | 1.58% | ×4.88 | +6.35 [+5.21, +7.53] | 2,818 | 64.2% | 0.674% | fail |
| three or more roles, with a destination | yes | 0.13% | unstable | 1.59% | | | 267 | | | unstable (100 runs needed) |
| second relay + first relay | no | 1.17% | unstable | 0.55% | | | 2,332 | | | unstable (109 runs needed) |
| second relay + second relay | no | 0.52% | unstable | 0.55% | | | 1,036 | | | unstable (228 runs needed) |
| gatekeeper + first relay | no | 2.09% | 1.32% [0.94%, 1.74%] | 0.55% | ×2.41 | -0.19 [-0.51, +0.12] | 4,174 | 19.0% | 0.000% | pass |
| gatekeeper + second relay | no | 1.96% | 1.51% [1.06%, 2.00%] | 0.55% | ×2.77 | -0.10 [-0.54, +0.28] | 3,900 | 13.2% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.55% | | | 814 | | | unstable (278 runs needed) |
| every record the node can select |  | 15.00% | 8.46% [7.55%, 9.36%] | 1.59% | ×5.33 | +7.04 [+6.18, +7.89] | 29,892 | 56.5% | 1.074% | fail |
| first relay held |  | 4.78% | 3.43% [3.00%, 3.85%] | 0.87% | ×3.92 | +2.23 [+1.82, +2.62] | 9,516 | 51.1% | 0.410% | fail |
| no first relay held |  | 95.22% | 2.44% [2.14%, 2.76%] | 0.69% | ×3.52 | +1.00 [+0.87, +1.12] | 189,764 | 39.6% | 0.153% | fail |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 9,964 |
| D or G | +0.00 [+0.00, +0.00] | 19,928 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 0.76% [0.59%, 0.93%] | 0.27% | ×2.77 [2.15, 3.39] | reference | 10,928 | 3.4% | 0.000% | pass |
| First hop, credential | 0.76% [0.59%, 0.94%] | 0.27% | ×2.77 [2.15, 3.42] | +0.00 [+0.00, +0.00] | 218,560 | 0.2% | 0.000% | pass |
| Combined | 1.41% [1.24%, 1.59%] | 0.35% | ×3.99 [3.51, 4.52] | +0.65 [+0.56, +0.74] | 218,560 | 22.1% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.63% | 0.76% [0.60%, 0.93%] | 0.27% | ×2.79 | +0.00 [+0.00, +0.00] | 108,473 | 0.4% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.38% | 0.77% [0.61%, 0.96%] | 0.27% | ×2.81 | +0.04 [-0.00, +0.07] | 64,211 | 1.6% | 0.000% | pass |
| destination only | yes | 11.91% | 5.12% [4.55%, 5.71%] | 0.80% | ×6.40 | +4.33 [+3.73, +4.94] | 26,030 | 32.6% | 0.000% | pass |
| credential first relay + content destination | yes | 0.48% | 6.74% [5.40%, 8.17%] | 1.08% | ×6.25 | +6.06 [+4.58, +7.65] | 1,039 | 51.0% | 0.000% | fail |
| content first relay + content destination | yes | 0.55% | 5.77% [4.31%, 7.29%] | 1.04% | ×5.53 | +5.44 [+4.00, +7.03] | 1,195 | 68.0% | 0.000% | fail |
| content first relay + credential destination | yes | 0.52% | unstable | 0.27% | | | 1,128 | | | unstable (500 runs needed) |
| second relay + destination | yes | 1.41% | 4.86% [4.05%, 5.71%] | 0.80% | ×6.10 | +4.08 [+3.29, +4.96] | 3,086 | 43.2% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 0.76% | | | 306 | | | unstable (193 runs needed) |
| second relay + first relay | no | 1.12% | unstable | 0.27% | | | 2,455 | | | unstable (139 runs needed) |
| second relay + second relay | no | 0.51% | unstable | 0.27% | | | 1,123 | | | unstable (278 runs needed) |
| gatekeeper + first relay | no | 2.08% | unstable | 0.27% | | | 4,554 | | | unstable (53 runs needed) |
| gatekeeper + second relay | no | 1.87% | unstable | 0.27% | | | 4,084 | | | unstable (76 runs needed) |
| three or more roles, no destination | no | 0.40% | unstable | 0.27% | | | 876 | | | unstable (417 runs needed) |
| every record the node can select |  | 15.00% | 5.00% [4.43%, 5.58%] | 0.80% | ×6.26 | +4.24 [+3.70, +4.78] | 32,784 | 30.9% | 0.000% | pass |
| first relay held |  | 4.75% | 2.02% [1.72%, 2.33%] | 0.44% | ×4.57 | +1.25 [+1.01, +1.50] | 10,371 | 25.7% | 0.000% | pass |
| no first relay held |  | 95.25% | 1.38% [1.20%, 1.56%] | 0.35% | ×3.95 | +0.62 [+0.53, +0.71] | 208,189 | 22.8% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 10,928 |
| D or G | +0.00 [+0.00, +0.00] | 21,856 |

#### R500_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | unstable | 0.09% | | | 11,182 | | | unstable (109 runs needed) |
| First hop, credential | 0.21% [0.12%, 0.30%] | 0.09% | ×2.26 [1.29, 3.31] | +0.00 [+0.00, +0.00] | 223,640 | 0.2% | 0.000% | pass |
| Combined | 0.42% [0.33%, 0.52%] | 0.12% | ×3.61 [2.85, 4.43] | +0.22 [+0.15, +0.28] | 223,640 | 7.6% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.67% | 0.21% [0.12%, 0.30%] | 0.09% | ×2.27 | +0.00 [+0.00, +0.00] | 111,088 | 0.3% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.26% | 0.22% [0.15%, 0.31%] | 0.09% | ×2.45 | +0.03 [+0.00, +0.05] | 65,438 | 1.3% | 0.000% | pass |
| destination only | yes | 11.95% | 1.62% [1.22%, 2.10%] | 0.26% | ×6.23 | +1.41 [+0.98, +1.87] | 26,720 | 13.5% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | unstable | 0.35% | | | 1,097 | | | unstable (120 runs needed) |
| content first relay + content destination | yes | 0.50% | unstable | 0.34% | | | 1,111 | | | unstable (97 runs needed) |
| content first relay + credential destination | yes | 0.52% | unstable | 0.09% | | | 1,166 | | | unstable (500 runs needed) |
| second relay + destination | yes | 1.41% | unstable | 0.26% | | | 3,163 | | | unstable (61 runs needed) |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.25% | | | 289 | | | unstable (625 runs needed) |
| second relay + first relay | no | 1.11% | unstable | 0.09% | | | 2,481 | | | unstable (358 runs needed) |
| second relay + second relay | no | 0.51% | unstable | 0.09% | | | 1,139 | | | unstable (834 runs needed) |
| gatekeeper + first relay | no | 2.16% | unstable | 0.09% | | | 4,830 | | | unstable (278 runs needed) |
| gatekeeper + second relay | no | 1.88% | unstable | 0.09% | | | 4,194 | | | unstable (193 runs needed) |
| three or more roles, no destination | no | 0.41% | unstable | 0.09% | | | 924 | | | unstable (834 runs needed) |
| every record the node can select |  | 15.00% | 1.58% [1.18%, 2.00%] | 0.26% | ×6.08 | +1.38 [+0.95, +1.85] | 33,546 | 11.8% | 0.000% | pass |
| first relay held |  | 4.78% | 0.64% [0.45%, 0.86%] | 0.14% | ×4.43 | +0.37 [+0.19, +0.58] | 10,685 | 12.9% | 0.000% | pass |
| no first relay held |  | 95.22% | 0.41% [0.33%, 0.50%] | 0.12% | ×3.56 | +0.21 [+0.15, +0.27] | 212,955 | 7.5% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 11,182 |
| D or G | +0.00 [+0.00, +0.00] | 22,364 |

### Credential path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 95.8% |
| R100_D100 | 95.8% |
| R500_D100 | 96.0% |

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 4.67% [4.23%, 5.11%] | 1.09% | ×4.30 [3.89, 4.70] | reference | 19,489 | 12.9% | 0.000% | pass |
| First hop, credential | 4.67% [4.24%, 5.13%] | 1.09% | ×4.29 [3.90, 4.72] | -0.00 [-0.04, +0.03] | 389,780 | 8.7% | 0.000% | pass |
| Combined | 4.83% [4.41%, 5.24%] | 1.11% | ×4.34 [3.97, 4.71] | +0.15 [+0.08, +0.23] | 389,780 | 9.8% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.70% | 4.63% [4.20%, 5.06%] | 1.09% | ×4.26 | -0.02 [-0.06, +0.02] | 193,703 | 9.0% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.21% | 4.73% [4.30%, 5.14%] | 1.09% | ×4.35 | -0.01 [-0.10, +0.07] | 113,871 | 10.1% | 0.000% | pass |
| destination only | yes | 11.97% | 5.78% [5.41%, 6.13%] | 1.25% | ×4.62 | +1.07 [+0.80, +1.35] | 46,642 | 11.7% | 0.000% | pass |
| credential first relay + content destination | yes | 0.52% | 6.60% [5.44%, 7.79%] | 1.34% | ×4.93 | +1.87 [+0.63, +3.08] | 2,029 | 46.9% | 0.049% | pass |
| content first relay + content destination | yes | 0.51% | 7.03% [5.78%, 8.34%] | 1.33% | ×5.29 | +1.82 [+0.31, +3.34] | 1,976 | 41.6% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 4.88% [3.94%, 5.84%] | 1.09% | ×4.49 | +0.15 [-0.10, +0.43] | 2,008 | 30.1% | 0.000% | pass |
| second relay + destination | yes | 1.36% | 6.20% [5.42%, 7.02%] | 1.25% | ×4.97 | +1.83 [+1.31, +2.41] | 5,305 | 31.4% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 1.25% | | | 507 | | | unstable (193 runs needed) |
| second relay + first relay | no | 1.13% | 3.98% [3.40%, 4.58%] | 1.09% | ×3.66 | -0.02 [-0.23, +0.16] | 4,423 | 15.1% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 4.82% [3.84%, 5.84%] | 1.09% | ×4.44 | -0.15 [-0.39, +0.10] | 2,032 | 16.1% | 0.000% | pass |
| gatekeeper + first relay | no | 2.09% | 4.33% [3.77%, 4.91%] | 1.09% | ×3.98 | -0.14 [-0.50, +0.20] | 8,136 | 16.8% | 0.000% | pass |
| gatekeeper + second relay | no | 1.92% | 4.51% [3.86%, 5.20%] | 1.09% | ×4.15 | -0.39 [-0.73, -0.07] | 7,467 | 14.7% | 0.000% | pass |
| three or more roles, no destination | no | 0.43% | 4.40% [3.44%, 5.37%] | 1.09% | ×4.05 | -0.24 [-0.75, +0.29] | 1,681 | 27.0% | 0.000% | pass |
| every record the node can select |  | 15.00% | 5.85% [5.47%, 6.25%] | 1.25% | ×4.68 | +1.18 [+0.91, +1.45] | 58,467 | 13.2% | 0.000% | pass |
| first relay held |  | 4.76% | 4.84% [4.41%, 5.31%] | 1.14% | ×4.24 | +0.35 [+0.09, +0.62] | 18,572 | 22.1% | 0.005% | pass |
| no first relay held |  | 95.24% | 4.83% [4.41%, 5.25%] | 1.11% | ×4.35 | +0.14 [+0.07, +0.21] | 371,208 | 9.4% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.01 [-0.07, +0.09] | 19,489 |
| D or G | +0.04 [-0.03, +0.11] | 38,978 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.59% [2.32%, 2.86%] | 0.55% | ×4.71 [4.22, 5.20] | reference | 21,381 | 6.0% | 0.000% | pass |
| First hop, credential | 2.60% [2.34%, 2.87%] | 0.55% | ×4.72 [4.25, 5.22] | +0.01 [-0.01, +0.03] | 427,620 | 3.1% | 0.000% | pass |
| Combined | 2.68% [2.43%, 2.93%] | 0.56% | ×4.77 [4.33, 5.21] | +0.09 [+0.06, +0.13] | 427,620 | 5.4% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.63% | 2.60% [2.33%, 2.88%] | 0.55% | ×4.72 | -0.01 [-0.03, +0.02] | 212,217 | 3.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.34% | 2.55% [2.28%, 2.80%] | 0.55% | ×4.63 | -0.02 [-0.07, +0.03] | 125,444 | 3.0% | 0.000% | pass |
| destination only | yes | 11.95% | 3.31% [3.07%, 3.55%] | 0.63% | ×5.22 | +0.74 [+0.58, +0.89] | 51,115 | 8.3% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 3.91% [3.12%, 4.75%] | 0.68% | ×5.79 | +0.93 [+0.05, +1.85] | 2,146 | 22.7% | 0.000% | pass |
| content first relay + content destination | yes | 0.50% | 3.03% [2.36%, 3.71%] | 0.67% | ×4.49 | +0.42 [-0.47, +1.29] | 2,147 | 15.5% | 0.000% | pass |
| content first relay + credential destination | yes | 0.51% | 2.30% [1.70%, 2.96%] | 0.55% | ×4.18 | +0.09 [-0.09, +0.28] | 2,172 | 14.9% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 3.35% [2.92%, 3.80%] | 0.63% | ×5.30 | +0.70 [+0.34, +1.07] | 5,996 | 15.9% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 0.63% | | | 567 | | | unstable (228 runs needed) |
| second relay + first relay | no | 1.15% | 2.62% [2.16%, 3.13%] | 0.55% | ×4.77 | +0.00 [-0.12, +0.12] | 4,920 | 16.5% | 0.000% | pass |
| second relay + second relay | no | 0.53% | 2.82% [2.06%, 3.65%] | 0.55% | ×5.12 | +0.09 [-0.18, +0.32] | 2,269 | 14.3% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 2.58% [2.25%, 2.93%] | 0.55% | ×4.69 | +0.07 [-0.13, +0.28] | 9,026 | 7.7% | 0.011% | pass |
| gatekeeper + second relay | no | 1.84% | 2.38% [2.04%, 2.75%] | 0.55% | ×4.32 | -0.19 [-0.38, +0.00] | 7,873 | 8.8% | 0.000% | pass |
| three or more roles, no destination | no | 0.40% | 2.89% [2.19%, 3.63%] | 0.55% | ×5.26 | -0.06 [-0.43, +0.30] | 1,728 | 27.0% | 0.000% | pass |
| every record the node can select |  | 15.00% | 3.29% [3.06%, 3.52%] | 0.63% | ×5.20 | +0.70 [+0.56, +0.84] | 64,143 | 8.4% | 0.000% | pass |
| first relay held |  | 4.77% | 2.75% [2.47%, 3.03%] | 0.58% | ×4.77 | +0.18 [+0.02, +0.35] | 20,411 | 11.2% | 0.000% | pass |
| no first relay held |  | 95.23% | 2.68% [2.43%, 2.93%] | 0.56% | ×4.77 | +0.09 [+0.05, +0.13] | 407,209 | 5.2% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.06 [+0.01, +0.11] | 21,381 |
| D or G | +0.05 [+0.00, +0.10] | 42,762 |

#### R500_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 1.09% [0.96%, 1.22%] | 0.18% | ×5.96 [5.26, 6.67] | reference | 21,620 | 4.7% | 0.000% | pass |
| First hop, credential | 1.08% [0.96%, 1.20%] | 0.18% | ×5.88 [5.24, 6.56] | -0.01 [-0.03, -0.00] | 432,400 | 2.4% | 0.000% | pass |
| Combined | 1.10% [0.99%, 1.22%] | 0.19% | ×5.87 [5.28, 6.51] | +0.01 [-0.02, +0.04] | 432,400 | 2.7% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.69% | 1.08% [0.95%, 1.21%] | 0.18% | ×5.89 | -0.02 [-0.03, +0.00] | 214,842 | 2.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.25% | 1.04% [0.92%, 1.16%] | 0.18% | ×5.68 | -0.04 [-0.07, -0.00] | 126,473 | 2.2% | 0.000% | pass |
| destination only | yes | 11.93% | 1.28% [1.17%, 1.40%] | 0.21% | ×6.09 | +0.18 [+0.08, +0.28] | 51,604 | 5.7% | 0.000% | pass |
| credential first relay + content destination | yes | 0.51% | unstable | 0.22% | | | 2,190 | | | unstable (186 runs needed) |
| content first relay + content destination | yes | 0.50% | unstable | 0.22% | | | 2,141 | | | unstable (173 runs needed) |
| content first relay + credential destination | yes | 0.52% | unstable | 0.18% | | | 2,259 | | | unstable (218 runs needed) |
| second relay + destination | yes | 1.41% | 1.40% [1.13%, 1.69%] | 0.21% | ×6.64 | +0.23 [-0.07, +0.53] | 6,080 | 15.7% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 0.21% | | | 586 | | | unstable (1250 runs needed) |
| second relay + first relay | no | 1.15% | unstable | 0.18% | | | 4,963 | | | unstable (120 runs needed) |
| second relay + second relay | no | 0.53% | unstable | 0.18% | | | 2,288 | | | unstable (239 runs needed) |
| gatekeeper + first relay | no | 2.11% | 1.16% [0.93%, 1.42%] | 0.18% | ×6.34 | -0.02 [-0.14, +0.10] | 9,130 | 9.2% | 0.000% | pass |
| gatekeeper + second relay | no | 1.87% | 1.24% [0.99%, 1.49%] | 0.18% | ×6.77 | -0.04 [-0.21, +0.13] | 8,068 | 6.7% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 0.18% | | | 1,776 | | | unstable (239 runs needed) |
| every record the node can select |  | 15.00% | 1.28% [1.18%, 1.38%] | 0.21% | ×6.08 | +0.19 [+0.10, +0.28] | 64,860 | 6.3% | 0.000% | pass |
| first relay held |  | 4.78% | 1.10% [0.94%, 1.26%] | 0.19% | ×5.72 | +0.07 [-0.04, +0.17] | 20,683 | 5.5% | 0.000% | pass |
| no first relay held |  | 95.22% | 1.10% [0.99%, 1.22%] | 0.19% | ×5.88 | +0.00 [-0.03, +0.03] | 411,717 | 2.6% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.01 [-0.02, +0.04] | 21,620 |
| D or G | -0.00 [-0.03, +0.03] | 43,240 |

### Content paths set the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 98.0% |
| R100_D100 | 98.0% |
| R500_D100 | 98.0% |

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | unstable | 8.33% | | | 19,911 | | | unstable (inf runs needed) |
| First hop, credential | unstable | 8.33% | | | 398,220 | | | unstable (2500 runs needed) |
| Combined | unstable | 8.33% | | | 398,220 | | | unstable (228 runs needed) |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.79% | unstable | 8.33% | | | 198,280 | | | unstable (5000 runs needed) |
| one relay or gatekeeper role | no | 29.08% | unstable | 8.33% | | | 115,803 | | | unstable (5000 runs needed) |
| destination only | yes | 11.90% | unstable | 8.33% | | | 47,382 | | | unstable (313 runs needed) |
| credential first relay + content destination | yes | 0.50% | unstable | 8.33% | | | 2,003 | | | unstable (inf runs needed) |
| content first relay + content destination | yes | 0.52% | unstable | 8.33% | | | 2,051 | | | unstable (2500 runs needed) |
| content first relay + credential destination | yes | 0.53% | unstable | 8.33% | | | 2,100 | | | unstable (inf runs needed) |
| second relay + destination | yes | 1.42% | unstable | 8.33% | | | 5,669 | | | unstable (2500 runs needed) |
| three or more roles, with a destination | yes | 0.13% | unstable | 8.33% | | | 528 | | | unstable (inf runs needed) |
| second relay + first relay | no | 1.16% | unstable | 8.33% | | | 4,616 | | | unstable (inf runs needed) |
| second relay + second relay | no | 0.53% | unstable | 8.33% | | | 2,125 | | | unstable (inf runs needed) |
| gatekeeper + first relay | no | 2.10% | unstable | 8.33% | | | 8,344 | | | unstable (inf runs needed) |
| gatekeeper + second relay | no | 1.92% | unstable | 8.33% | | | 7,647 | | | unstable (inf runs needed) |
| three or more roles, no destination | no | 0.42% | unstable | 8.33% | | | 1,672 | | | unstable (inf runs needed) |
| every record the node can select |  | 15.00% | unstable | 8.33% | | | 59,733 | | | unstable (250 runs needed) |
| first relay held |  | 4.80% | unstable | 8.33% | | | 19,114 | | | unstable (2500 runs needed) |
| no first relay held |  | 95.20% | unstable | 8.33% | | | 379,106 | | | unstable (250 runs needed) |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 19,911 |
| D or G | +0.00 [+0.00, +0.01] | 39,822 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 12.20% [11.60%, 12.81%] | 4.55% | ×2.68 [2.55, 2.82] | reference | 21,906 | 25.4% | 0.000% | pass |
| First hop, credential | 12.18% [11.62%, 12.75%] | 4.55% | ×2.68 [2.56, 2.81] | -0.01 [-0.06, +0.03] | 438,120 | 21.6% | 0.000% | pass |
| Combined | 12.45% [11.90%, 13.04%] | 4.55% | ×2.74 [2.62, 2.87] | +0.26 [+0.18, +0.33] | 438,120 | 25.2% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.76% | 12.11% [11.53%, 12.68%] | 4.55% | ×2.66 | -0.07 [-0.13, -0.01] | 218,010 | 21.9% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.13% | 12.29% [11.69%, 12.86%] | 4.55% | ×2.70 | +0.07 [-0.01, +0.16] | 127,609 | 23.1% | 0.000% | pass |
| destination only | yes | 11.92% | 13.92% [13.30%, 14.50%] | 4.55% | ×3.06 | +1.65 [+1.42, +1.88] | 52,205 | 34.1% | 0.000% | pass |
| credential first relay + content destination | yes | 0.50% | 13.28% [11.77%, 14.76%] | 4.55% | ×2.92 | +2.28 [+1.13, +3.41] | 2,191 | 33.3% | 0.000% | pass |
| content first relay + content destination | yes | 0.53% | 14.87% [13.30%, 16.36%] | 4.55% | ×3.27 | +3.09 [+1.78, +4.39] | 2,327 | 59.2% | 0.645% | fail |
| content first relay + credential destination | yes | 0.53% | 12.80% [11.38%, 14.19%] | 4.55% | ×2.82 | +0.47 [+0.00, +0.96] | 2,320 | 46.5% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 13.95% [13.00%, 14.92%] | 4.55% | ×3.07 | +1.81 [+1.20, +2.46] | 6,124 | 38.4% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.13% | 13.07% [10.59%, 15.80%] | 4.55% | ×2.87 | +1.09 [-1.21, +3.36] | 551 | 56.4% | 0.000% | fail |
| second relay + first relay | no | 1.19% | 12.55% [11.50%, 13.61%] | 4.55% | ×2.76 | +0.55 [+0.17, +0.97] | 5,227 | 27.5% | 0.000% | pass |
| second relay + second relay | no | 0.50% | 12.17% [10.73%, 13.72%] | 4.55% | ×2.68 | -0.18 [-0.52, +0.14] | 2,185 | 48.2% | 0.000% | pass |
| gatekeeper + first relay | no | 2.12% | 12.62% [11.70%, 13.53%] | 4.55% | ×2.78 | +0.52 [+0.23, +0.80] | 9,296 | 29.7% | 0.000% | pass |
| gatekeeper + second relay | no | 1.87% | 12.66% [11.88%, 13.42%] | 4.55% | ×2.79 | +0.01 [-0.27, +0.28] | 8,213 | 29.4% | 0.110% | fail |
| three or more roles, no destination | no | 0.42% | 12.24% [10.71%, 13.77%] | 4.55% | ×2.69 | +0.59 [-0.11, +1.35] | 1,862 | 43.3% | 0.161% | fail |
| every record the node can select |  | 15.00% | 13.89% [13.33%, 14.48%] | 4.55% | ×3.06 | +1.69 [+1.49, +1.89] | 65,718 | 32.5% | 0.000% | pass |
| first relay held |  | 4.88% | 12.93% [12.20%, 13.67%] | 4.55% | ×2.85 | +0.98 [+0.72, +1.23] | 21,361 | 28.0% | 0.023% | pass |
| no first relay held |  | 95.12% | 12.43% [11.86%, 13.00%] | 4.55% | ×2.73 | +0.22 [+0.15, +0.29] | 416,759 | 25.2% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.09 [-0.21, +0.03] | 21,906 |
| D or G | +0.49 [+0.38, +0.60] | 43,812 |

#### R500_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 4.64% [4.36%, 4.93%] | 1.52% | ×3.06 [2.88, 3.25] | reference | 22,017 | 14.2% | 0.000% | pass |
| First hop, credential | 4.68% [4.41%, 4.93%] | 1.52% | ×3.09 [2.91, 3.26] | +0.04 [+0.00, +0.08] | 440,340 | 10.3% | 0.000% | pass |
| Combined | 4.82% [4.56%, 5.09%] | 1.52% | ×3.18 [3.01, 3.36] | +0.19 [+0.13, +0.24] | 440,340 | 11.2% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.69% | 4.63% [4.35%, 4.89%] | 1.52% | ×3.05 | +0.01 [-0.03, +0.05] | 218,811 | 10.2% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.23% | 4.75% [4.47%, 5.03%] | 1.52% | ×3.14 | +0.05 [-0.02, +0.12] | 128,719 | 11.2% | 0.000% | pass |
| destination only | yes | 11.95% | 5.71% [5.47%, 5.96%] | 1.52% | ×3.77 | +1.03 [+0.88, +1.19] | 52,611 | 14.8% | 0.000% | pass |
| credential first relay + content destination | yes | 0.51% | 6.11% [5.11%, 7.21%] | 1.52% | ×4.03 | +1.48 [+0.67, +2.37] | 2,225 | 33.3% | 0.000% | pass |
| content first relay + content destination | yes | 0.51% | 5.43% [4.53%, 6.51%] | 1.52% | ×3.59 | +0.98 [+0.05, +1.89] | 2,246 | 33.3% | 0.000% | pass |
| content first relay + credential destination | yes | 0.52% | 5.01% [4.14%, 5.90%] | 1.52% | ×3.30 | +0.30 [-0.04, +0.63] | 2,297 | 21.0% | 0.000% | pass |
| second relay + destination | yes | 1.38% | 5.50% [4.83%, 6.12%] | 1.52% | ×3.63 | +1.11 [+0.62, +1.57] | 6,059 | 25.7% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 1.52% | | | 613 | | | unstable (125 runs needed) |
| second relay + first relay | no | 1.15% | 4.39% [3.87%, 4.95%] | 1.52% | ×2.90 | +0.16 [-0.06, +0.39] | 5,052 | 18.5% | 0.000% | pass |
| second relay + second relay | no | 0.53% | 4.35% [3.53%, 5.22%] | 1.52% | ×2.87 | +0.04 [-0.17, +0.26] | 2,347 | 14.3% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 5.00% [4.54%, 5.50%] | 1.52% | ×3.30 | +0.22 [+0.07, +0.37] | 9,243 | 12.1% | 0.000% | pass |
| gatekeeper + second relay | no | 1.88% | 4.44% [4.01%, 4.89%] | 1.52% | ×2.93 | +0.10 [-0.07, +0.28] | 8,294 | 16.4% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 5.27% [4.15%, 6.35%] | 1.52% | ×3.48 | +0.22 [-0.11, +0.60] | 1,823 | 25.8% | 0.000% | pass |
| every record the node can select |  | 15.00% | 5.68% [5.43%, 5.92%] | 1.52% | ×3.75 | +1.04 [+0.91, +1.17] | 66,051 | 15.1% | 0.000% | pass |
| first relay held |  | 4.78% | 5.02% [4.69%, 5.37%] | 1.52% | ×3.31 | +0.43 [+0.28, +0.58] | 21,063 | 14.2% | 0.000% | pass |
| no first relay held |  | 95.22% | 4.81% [4.55%, 5.08%] | 1.52% | ×3.18 | +0.17 [+0.12, +0.23] | 419,277 | 11.2% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.02 [-0.06, +0.11] | 22,017 |
| D or G | +0.27 [+0.17, +0.36] | 44,034 |

### F content path sets the record time

| Cell | Intended path's share |
|---|---|
| R1_D100 | 96.7% |
| R100_D100 | 97.0% |
| R500_D100 | 96.9% |

#### R1_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | unstable | 5.88% | | | 19,907 | | | unstable (2500 runs needed) |
| First hop, credential | 0.01% [0.00%, 0.03%] | 5.88% | ×0.00 [0.00, 0.00] | +0.00 [+0.00, +0.01] | 398,140 | 0.1% | 0.000% | pass |
| Combined | 0.18% [0.16%, 0.21%] | 5.88% | ×0.03 [0.03, 0.04] | +0.17 [+0.16, +0.19] | 398,140 | 4.7% | 0.002% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.68% | unstable | 5.88% | | | 197,805 | | | unstable (103 runs needed) |
| one relay or gatekeeper role | no | 29.24% | unstable | 5.88% | | | 116,431 | | | unstable (125 runs needed) |
| destination only | yes | 11.94% | 1.03% [0.93%, 1.14%] | 5.88% | ×0.18 | +1.02 [+0.93, +1.12] | 47,534 | 11.0% | 0.015% | pass |
| credential first relay + content destination | yes | 0.52% | unstable | 5.88% | | | 2,061 | | | unstable (125 runs needed) |
| content first relay + content destination | yes | 0.50% | unstable | 5.88% | | | 2,008 | | | unstable (148 runs needed) |
| content first relay + credential destination | yes | 0.52% | unstable | 5.88% | | | 2,066 | | | unstable (inf runs needed) |
| second relay + destination | yes | 1.39% | 1.05% [0.80%, 1.31%] | 5.88% | ×0.18 | +1.03 [+0.78, +1.29] | 5,546 | 26.2% | 0.018% | pass |
| three or more roles, with a destination | yes | 0.13% | unstable | 5.88% | | | 506 | | | unstable (1000 runs needed) |
| second relay + first relay | no | 1.14% | unstable | 5.88% | | | 4,552 | | | unstable (inf runs needed) |
| second relay + second relay | no | 0.51% | unstable | 5.88% | | | 2,012 | | | unstable (inf runs needed) |
| gatekeeper + first relay | no | 2.10% | unstable | 5.88% | | | 8,377 | | | unstable (834 runs needed) |
| gatekeeper + second relay | no | 1.91% | unstable | 5.88% | | | 7,605 | | | unstable (1250 runs needed) |
| three or more roles, no destination | no | 0.41% | unstable | 5.88% | | | 1,637 | | | unstable (2500 runs needed) |
| every record the node can select |  | 15.00% | 1.05% [0.96%, 1.15%] | 5.88% | ×0.18 | +1.04 [+0.96, +1.13] | 59,721 | 11.4% | 0.012% | pass |
| first relay held |  | 4.79% | 0.42% [0.34%, 0.50%] | 5.88% | ×0.07 | +0.41 [+0.34, +0.49] | 19,064 | 8.0% | 0.000% | pass |
| no first relay held |  | 95.21% | 0.17% [0.15%, 0.20%] | 5.88% | ×0.03 | +0.16 [+0.14, +0.18] | 379,076 | 4.6% | 0.002% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | +0.00 [+0.00, +0.00] | 19,907 |
| D or G | +0.01 [+0.00, +0.02] | 39,814 |

#### R100_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 7.43% [6.97%, 7.90%] | 3.12% | ×2.38 [2.23, 2.53] | reference | 21,897 | 14.7% | 0.000% | pass |
| First hop, credential | 7.46% [7.01%, 7.93%] | 3.12% | ×2.39 [2.24, 2.54] | +0.03 [-0.01, +0.07] | 437,940 | 11.3% | 0.000% | pass |
| Combined | 7.88% [7.44%, 8.31%] | 3.12% | ×2.52 [2.38, 2.66] | +0.45 [+0.38, +0.52] | 437,940 | 21.6% | 0.008% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.66% | 7.42% [6.98%, 7.91%] | 3.12% | ×2.37 | +0.00 [-0.06, +0.06] | 217,489 | 11.6% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.29% | 7.57% [7.12%, 8.03%] | 3.12% | ×2.42 | +0.11 [+0.03, +0.20] | 128,260 | 14.0% | 0.000% | pass |
| destination only | yes | 11.93% | 10.25% [9.82%, 10.67%] | 3.12% | ×3.28 | +2.83 [+2.60, +3.06] | 52,257 | 34.7% | 0.052% | pass |
| credential first relay + content destination | yes | 0.50% | 10.56% [9.38%, 11.75%] | 3.12% | ×3.38 | +3.46 [+2.41, +4.58] | 2,197 | 33.3% | 0.137% | fail |
| content first relay + content destination | yes | 0.50% | 10.61% [9.23%, 11.93%] | 3.12% | ×3.39 | +3.28 [+2.12, +4.42] | 2,197 | 33.3% | 0.046% | pass |
| content first relay + credential destination | yes | 0.53% | 8.52% [7.41%, 9.62%] | 3.12% | ×2.73 | +0.26 [-0.21, +0.71] | 2,325 | 32.1% | 0.000% | pass |
| second relay + destination | yes | 1.40% | 9.57% [8.86%, 10.29%] | 3.12% | ×3.06 | +2.20 [+1.59, +2.83] | 6,146 | 45.3% | 0.569% | fail |
| three or more roles, with a destination | yes | 0.13% | unstable | 3.12% | | | 569 | | | unstable (103 runs needed) |
| second relay + first relay | no | 1.16% | 7.44% [6.68%, 8.21%] | 3.12% | ×2.38 | +0.12 [-0.16, +0.41] | 5,083 | 18.5% | 0.000% | pass |
| second relay + second relay | no | 0.52% | 6.44% [5.39%, 7.52%] | 3.12% | ×2.06 | -0.17 [-0.50, +0.13] | 2,297 | 46.5% | 0.000% | pass |
| gatekeeper + first relay | no | 2.10% | 7.62% [6.98%, 8.29%] | 3.12% | ×2.44 | +0.19 [-0.09, +0.50] | 9,181 | 16.2% | 0.000% | pass |
| gatekeeper + second relay | no | 1.86% | 7.74% [7.09%, 8.43%] | 3.12% | ×2.48 | -0.02 [-0.27, +0.23] | 8,163 | 18.1% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | 7.49% [6.08%, 8.96%] | 3.12% | ×2.40 | +0.73 [+0.23, +1.26] | 1,776 | 45.2% | 0.000% | pass |
| every record the node can select |  | 15.00% | 10.13% [9.74%, 10.55%] | 3.12% | ×3.24 | +2.70 [+2.49, +2.92] | 65,691 | 32.5% | 0.050% | pass |
| first relay held |  | 4.79% | 8.30% [7.77%, 8.82%] | 3.12% | ×2.66 | +0.84 [+0.61, +1.08] | 20,983 | 26.4% | 0.014% | pass |
| no first relay held |  | 95.21% | 7.86% [7.42%, 8.31%] | 3.12% | ×2.51 | +0.43 [+0.35, +0.50] | 416,957 | 21.8% | 0.007% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.02 [-0.11, +0.07] | 21,897 |
| D or G | +0.34 [+0.25, +0.43] | 43,794 |

#### R500_D100

| Vantage | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|
| Passive observer | 2.81% [2.57%, 3.09%] | 1.04% | ×2.70 [2.46, 2.96] | reference | 22,115 | 9.2% | 0.000% | pass |
| First hop, credential | 2.79% [2.55%, 3.04%] | 1.04% | ×2.68 [2.45, 2.92] | -0.02 [-0.05, +0.01] | 442,300 | 5.7% | 0.000% | pass |
| Combined | 2.99% [2.73%, 3.23%] | 1.04% | ×2.87 [2.62, 3.10] | +0.18 [+0.13, +0.22] | 442,300 | 9.7% | 0.000% | pass |

| Roles the node held | Identifiable | Prevalence | Device named [95% CI] | Chance | Multiple of chance | Lead over observer [95% CI] | Decisions | Top 1% right, upper bound | Coverage above 50% | Claim |
|---|---|---|---|---|---|---|---|---|---|---|
| no role | no | 49.67% | 2.80% [2.53%, 3.07%] | 1.04% | ×2.68 | -0.03 [-0.07, +0.01] | 219,706 | 5.5% | 0.000% | pass |
| one relay or gatekeeper role | no | 29.25% | 2.81% [2.55%, 3.09%] | 1.04% | ×2.70 | +0.03 [-0.02, +0.07] | 129,377 | 6.0% | 0.000% | pass |
| destination only | yes | 11.96% | 4.04% [3.81%, 4.27%] | 1.04% | ×3.88 | +1.29 [+1.12, +1.45] | 52,891 | 14.9% | 0.000% | pass |
| credential first relay + content destination | yes | 0.49% | 5.19% [4.20%, 6.21%] | 1.04% | ×4.99 | +2.07 [+1.19, +2.94] | 2,176 | 48.2% | 0.414% | fail |
| content first relay + content destination | yes | 0.50% | 4.26% [3.40%, 5.15%] | 1.04% | ×4.09 | +1.30 [+0.57, +2.04] | 2,228 | 48.2% | 0.000% | pass |
| content first relay + credential destination | yes | 0.53% | 2.91% [2.18%, 3.68%] | 1.04% | ×2.79 | -0.09 [-0.35, +0.17] | 2,340 | 21.0% | 0.000% | pass |
| second relay + destination | yes | 1.38% | 4.10% [3.60%, 4.64%] | 1.04% | ×3.94 | +1.03 [+0.61, +1.45] | 6,098 | 19.8% | 0.000% | pass |
| three or more roles, with a destination | yes | 0.14% | unstable | 1.04% | | | 612 | | | unstable (218 runs needed) |
| second relay + first relay | no | 1.17% | 2.61% [2.13%, 3.10%] | 1.04% | ×2.51 | -0.06 [-0.19, +0.08] | 5,166 | 13.0% | 0.000% | pass |
| second relay + second relay | no | 0.53% | 3.08% [2.37%, 3.81%] | 1.04% | ×2.96 | -0.09 [-0.33, +0.16] | 2,339 | 14.3% | 0.000% | pass |
| gatekeeper + first relay | no | 2.11% | 3.00% [2.59%, 3.39%] | 1.04% | ×2.88 | +0.01 [-0.15, +0.17] | 9,342 | 10.5% | 0.000% | pass |
| gatekeeper + second relay | no | 1.86% | 2.59% [2.25%, 2.93%] | 1.04% | ×2.49 | -0.02 [-0.16, +0.11] | 8,217 | 8.5% | 0.000% | pass |
| three or more roles, no destination | no | 0.41% | unstable | 1.04% | | | 1,808 | | | unstable (103 runs needed) |
| every record the node can select |  | 15.00% | 4.05% [3.83%, 4.26%] | 1.04% | ×3.88 | +1.24 [+1.09, +1.38] | 66,345 | 15.6% | 0.000% | pass |
| first relay held |  | 4.80% | 3.25% [2.94%, 3.59%] | 1.04% | ×3.12 | +0.33 [+0.17, +0.49] | 21,252 | 17.8% | 0.000% | pass |
| no first relay held |  | 95.20% | 2.97% [2.72%, 3.23%] | 1.04% | ×2.85 | +0.17 [+0.13, +0.21] | 421,048 | 9.7% | 0.000% | pass |

| First relay as | Lead over observer [95% CI] | Decisions |
|---|---|---|
| A | -0.03 [-0.08, +0.02] | 22,115 |
| D or G | +0.06 [-0.00, +0.11] | 44,230 |

## Cost per run

| Configuration | Cell | Simulation | Scoring | Shuffle test |
|---|---|---|---|---|
| Main run | R1_D100 | 6.7 s | 349.3 s | 0.6 s |
| Main run | R100_D100 | 0.9 s | 92.4 s | 0.3 s |
| Main run | R500_D100 | 1.3 s | 463.8 s | 1.0 s |
| Every hold off | R1_D100 | 6.3 s | 50.7 s | 0.0 s |
| Every hold off | R100_D100 | 1.1 s | 33.4 s | 0.0 s |
| Every hold off | R500_D100 | 2.2 s | 83.2 s | 0.0 s |
| Credential path sets the record time | R1_D100 | 6.7 s | 288.8 s | 0.0 s |
| Credential path sets the record time | R100_D100 | 1.1 s | 113.8 s | 0.0 s |
| Credential path sets the record time | R500_D100 | 1.8 s | 527.9 s | 0.0 s |
| Content paths set the record time | R1_D100 | 5.6 s | 366.7 s | 0.0 s |
| Content paths set the record time | R100_D100 | 0.7 s | 98.0 s | 0.0 s |
| Content paths set the record time | R500_D100 | 1.1 s | 415.3 s | 0.0 s |
| F content path sets the record time | R1_D100 | 5.2 s | 363.0 s | 0.0 s |
| F content path sets the record time | R100_D100 | 0.7 s | 150.0 s | 0.0 s |
| F content path sets the record time | R500_D100 | 1.3 s | 650.0 s | 0.0 s |

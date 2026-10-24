# Paper table

How often each single compromised component names the device behind a registry record, with 100 decoy transactions in flight and every node compromised in turn. Intervals are 95% and resample whole runs.

## R1_D100

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

## R100_D100

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

## R500_D100

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


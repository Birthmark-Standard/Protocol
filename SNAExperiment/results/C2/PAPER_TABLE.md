# Paper table

How often each single compromised component names the device behind a registry record, with 100 decoy transactions in flight and every node compromised in turn. Intervals are 95% and resample whole runs.

## R1_D100

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

## R100_D100

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

## R300_D100

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


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

## R150_D100

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


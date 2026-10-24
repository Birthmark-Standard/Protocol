# Paper table

How often each single compromised component names the device behind a registry record, with 60 decoy transactions in flight and every node compromised in turn. Intervals are 95% and resample whole runs.

## R1_D60

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

## R20_D60

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

## R100_D60

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


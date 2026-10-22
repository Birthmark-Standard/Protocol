# Shuffle control check: result

Prediction: `shuffle_check_prediction.md`, committed at 0281bd5 before this check ran. Script: `audit/shuffle_check.py`. Numbers: `shuffle_check.json`. R = 20, `permitted_overlap`.

| Runs and seeds | Vantage | Shuffled accuracy [95% CI] | Feasible chance | Runs fixing no real device | Runs fixing a real device |
|---|---|---|---|---|---|
| committed seeds, runs 0 to 19 | observer | 0.90% [0.64, 1.15] | 1.15% | 1.00% | 0.00% |
| committed seeds, runs 0 to 19 | credential processor | 0.89% [0.63, 1.16] | 1.15% | 0.99% | 0.00% |
| fresh seeds, runs 0 to 99 | observer | 1.07% [0.91, 1.24] | 1.16% | 1.06% | 1.11% |
| fresh seeds, runs 0 to 99 | credential processor | 1.08% [0.93, 1.24] | 1.16% | 1.07% | 1.11% |

- **Prediction 1 fails.** On the committed runs, the runs whose permutation fixes a real device scored lower, not higher. The fixed-point mechanism does not explain the shortfall.
- **Prediction 2 holds.** On 100 runs with fresh seeds, both intervals contain the chance rate, and both point estimates lie within 0.95% to 1.35%.
- **The explanation as stated fails**, because prediction 1 fails.
- The committed failure is at the boundary. Its upper bound is 1.15% against a chance rate of 1.15%. A different bootstrap draw on the same 20 runs gives an upper bound of 1.16%, which passes.
- In every look so far the shuffled point estimate at R = 20 sits below chance: version 1 (0.93% against 1.09%), the committed 20 runs (0.88% against 1.15%), and the 100 fresh runs (1.07% against 1.16%). The cause of that gap is not identified.

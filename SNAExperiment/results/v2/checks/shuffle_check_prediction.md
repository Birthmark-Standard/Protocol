# Shuffle control check: prediction

Written before the check runs. Committed before the check runs; the commit time is the timestamp.

**Observation.** In `results/v2/shuffle_control.json`, the credential processor at R = 20 is 0.88% [0.64, 1.15] against a feasible chance rate of 1.15%. Every vantage at R = 20 is below chance, the observer at 0.90%. Version 1 showed the same pattern at R = 20 on the same 20 runs and the same permutation seeds.

**Explanation under test.** Within a run, one permutation relabels every candidate. A run scores above chance only when the permutation leaves a real device on its own label, because then that device's records are right at the observer's rate. Most runs have no such device and score below chance. The per-run accuracy is therefore skewed, and 20 runs can fall below chance by the draw of permutations. The expected accuracy is still the chance rate.

**Predictions.**
1. On the 20 committed runs at R = 20, the runs whose permutation fixes no real device have a lower shuffled accuracy than the runs whose permutation fixes one.
2. On 100 runs at R = 20 (run ids 0 to 99) with fresh permutation seeds (`[SHUFFLE_SEED + 1, R, run id]`), under `permitted_overlap`, the 95% interval on shuffled accuracy contains the feasible chance rate for both the observer and the credential processor, and both point estimates lie within 0.95% to 1.35%.

**The explanation fails if** prediction 2's interval excludes the chance rate for either vantage, or prediction 1 does not hold.

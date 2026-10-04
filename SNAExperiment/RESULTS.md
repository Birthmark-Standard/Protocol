# Results

InternalCompromiseRun: can a single compromised component of the Birthmark Protocol take a public registry record and name the device that produced it?

- Every hold follows the timing in `README.md`: 10-second ticks, geometric release, each capped at three times its own mean.
- Departure bundling is by inclusion lottery. Registry bundling uses one shared 120-second schedule. The post-match lottery is on.
- R = 1, 20 and 100 real transactions in flight, with 60 decoys in flight; 200 runs per cell.
- Every cell of every build met the stability rule: at least 50 right and 50 wrong decisions at the device level for every vantage.
- The full generated tables are in `results/TABLES.md`. The figures are `results/figures/device_named.png` and `confidence_reliability.png`.

## Summary

1. **No single compromised component does meaningfully better than a passive observer.**
   - Across the 18 component-and-cell combinations, the largest lead over the observer is +0.24 points [+0.18, +0.30] (content server, R = 100).
   - It is the only lead whose interval lies above 0.
   - The validator, which holds a device identity for every approval, is 0.06 to 0.40 points below the observer.
2. **Every component, the observer included, names the device about 4 to 5 times as often as a guess among the devices that could have produced the record.**

   | | R = 1 | R = 20 | R = 100 |
   |---|---|---|---|
   | Observer | 9.91% | 6.46% | 3.48% |
   | Best component | 9.95% | 6.60% | 3.72% |
   | Feasible-set guess | 2.03% | 1.55% | 0.77% |
   | One in N registered devices | 1.43% | 1.09% | 0.54% |

3. **The adversary cannot tell which of its matches are right.**
   - A component's average confidence in its own match is 6.7% to 8.1% at R = 1, 5.3% to 6.5% at R = 20 and 2.8% to 3.6% at R = 100.
   - Its 99th-percentile confidence never exceeds 13.6%.
   - The most confident 1% of any component's matches are right at most 26.5% of the time, with an upper bound of 30.3%.
   - In no cell do more than 0.019% of a component's decisions fall in a most-confident set that is right more than half the time.
4. **InternalCompromiseRun passes the claim criterion at R = 1, 20 and 100.**
   - So does every other build, including the one with all five mechanisms removed.
   - At 60 decoys, the builds differ in the leads and in the observer's accuracy, which the sections below report.
5. **Of the five timing mechanisms, the role-aware holds matter most.**
   - Without them, the validator leads the observer by +2.01, +1.49 and +1.04 points, and the content server by +0.42 to +0.77.
   - The observer itself gains 0.43 to 0.87 points.
   - Removed one at a time, the four other mechanisms each change the observer by at most 0.10 points.
6. **Mean capture to finalization is 1,033 to 1,042 seconds.** The 95th percentile is 1,523 to 1,530 seconds.
   - Without the role-aware holds the mean is 807 seconds.
   - With all five mechanisms removed it is 647 to 650 seconds.

## The adversary against InternalCompromiseRun

Device named, in percent [95% CI]. The lead is over the passive observer on the same records, in points [95% CI]. Top 1% is the share of a component's most confident 1% of matches that are right.

| Component | R = 1 | Lead | R = 20 | Lead | R = 100 | Lead | Top 1% right, R = 1 / 20 / 100 |
|---|---|---|---|---|---|---|---|
| Passive observer | 9.91 [9.48, 10.33] | reference | 6.46 [6.15, 6.78] | reference | 3.48 [3.40, 3.56] | reference | 25.8 / 13.4 / 6.5 |
| First hop, credential | 9.89 [9.46, 10.30] | -0.02 [-0.11, +0.06] | 6.47 [6.17, 6.79] | +0.01 [-0.07, +0.09] | 3.47 [3.40, 3.54] | -0.01 [-0.04, +0.01] | 25.4 / 13.7 / 6.2 |
| First hop, content | 9.89 [9.48, 10.28] | -0.02 [-0.10, +0.06] | 6.47 [6.17, 6.77] | +0.01 [-0.07, +0.09] | 3.47 [3.39, 3.54] | -0.01 [-0.03, +0.01] | 25.4 / 13.7 / 6.2 |
| Credential processor | 9.91 [9.48, 10.33] | +0.00 [-0.05, +0.05] | 6.46 [6.14, 6.77] | -0.01 [-0.04, +0.03] | 3.47 [3.39, 3.54] | -0.01 [-0.02, +0.00] | 25.5 / 13.5 / 6.4 |
| Validator | 9.51 [9.10, 9.93] | -0.40 [-0.79, -0.05] | 6.32 [6.05, 6.59] | -0.14 [-0.42, +0.12] | 3.41 [3.33, 3.49] | -0.06 [-0.15, +0.02] | 22.1 / 9.4 / 5.3 |
| Gatekeeper | 9.95 [9.54, 10.38] | +0.04 [-0.06, +0.14] | 6.45 [6.14, 6.74] | -0.01 [-0.10, +0.07] | 3.46 [3.39, 3.55] | -0.01 [-0.04, +0.01] | 26.5 / 13.8 / 6.7 |
| Content server | 9.84 [9.52, 10.15] | -0.07 [-0.31, +0.16] | 6.60 [6.35, 6.84] | +0.14 [-0.06, +0.35] | 3.72 [3.64, 3.79] | +0.24 [+0.18, +0.30] | 7.9 / 3.7 / 2.2 |

The content server is the most accurate component at R = 20 and 100. Its confidence is the least useful, though: its most confident 1% of matches are right 2.2% to 7.9% of the time, against 5.3% to 26.5% for every other component.

## The adversary's confidence

Each component's confidence is calibrated on half the runs and scored on the other half (cross-fitted by run parity).

- **Calibration is close for every component except the content server.**
  - At R = 20, the mean absolute gap between stated confidence and the share of matches that are right is 0.24 to 0.47 points for six components, and 1.35 points for the content server.
  - Across the ten deciles at R = 20, the content server's stated confidence runs from 3.8% to 8.2%. The share of its matches that are right runs from 5.2% to 8.3%. It is underconfident below its top decile.
- **The highest confidence any component gives a single match** is 7.8% to 20.9% for the observer, credential processor, validator and gatekeeper. It is 22% to 43% for the first hops and 79% to 86% for the content server.
  - These are single records.
  - At most 0.017% of a first hop's decisions fall in a most-confident set right more than half the time. None of the content server's do.

## Claim criterion

The criterion is defined in `README.md`. InternalCompromiseRun passes it in every cell:

| R | Highest upper bound on top-1% precision, any component | Largest share of decisions in a most-confident set right more than half the time |
|---|---|---|
| 1 | 30.3% (passive observer) | 0.0075% (gatekeeper) |
| 20 | 17.0% (passive observer) | 0.0186% (credential processor) |
| 100 | 7.6% (passive observer) | 0.0000% |

Every other build also passes in every cell. Across all ten builds the highest upper bound is 32.9% and the largest share is 0.0728%.

## What each mechanism contributes

Each build removes one mechanism from InternalCompromiseRun and keeps the rest. It is paired with InternalCompromiseRun on the same records: the effect is the build minus InternalCompromiseRun, in points [95% CI].

| Build | R | Observer: effect vs InternalCompromiseRun | Validator's lead | Content server's lead | Mean latency |
|---|---|---|---|---|---|
| InternalCompromiseRun | 1 | reference | -0.40 [-0.79, -0.05] | -0.07 [-0.31, +0.16] | 1,042 s |
| InternalCompromiseRun | 20 | reference | -0.14 [-0.42, +0.12] | +0.14 [-0.06, +0.35] | 1,033 s |
| InternalCompromiseRun | 100 | reference | -0.06 [-0.15, +0.02] | +0.24 [+0.18, +0.30] | 1,037 s |
| without V's and C's holds | 1 / 20 / 100 | -0.01 [-0.18, +0.16] / -0.10 [-0.26, +0.07] / +0.02 [-0.02, +0.07] | see `results/TABLES.md` | see `results/TABLES.md` | 1,020 to 1,030 s |
| without the inclusion lottery | 1 / 20 / 100 | +0.06 [-0.15, +0.27] / -0.10 [-0.26, +0.07] / +0.04 [-0.01, +0.10] | | | 1,017 to 1,026 s |
| without the post-match lottery | 1 / 20 / 100 | -0.03 [-0.19, +0.14] / -0.09 [-0.24, +0.07] / +0.06 [+0.02, +0.11] | | | 999 to 1,010 s |
| without registry bundling | 1 / 20 / 100 | +0.06 [-0.10, +0.23] / +0.04 [-0.10, +0.18] / +0.06 [+0.01, +0.10] | | | 973 to 983 s |
| without role-aware holds | 1 | +0.70 [+0.37, +1.05] | +2.01 [+1.58, +2.42] | +0.68 [+0.43, +0.92] | 807 s |
| without role-aware holds | 20 | +0.87 [+0.60, +1.14] | +1.49 [+1.16, +1.81] | +0.77 [+0.55, +0.99] | 807 s |
| without role-aware holds | 100 | +0.43 [+0.37, +0.50] | +1.04 [+0.92, +1.15] | +0.42 [+0.35, +0.50] | 807 s |
| without all five | 1 | +1.46 [+1.16, +1.76] | +1.17 [+0.82, +1.51] | +0.13 [-0.07, +0.33] | 650 s |
| without all five | 20 | +1.31 [+1.05, +1.59] | +0.91 [+0.58, +1.23] | +0.30 [+0.08, +0.51] | 647 s |
| without all five | 100 | +0.73 [+0.66, +0.81] | +0.64 [+0.54, +0.74] | +0.25 [+0.17, +0.32] | 649 s |

- **Role-aware holds** (device content channels and F/I pre-match hold at 240 s, against 120 s everywhere else) are the only single mechanism whose removal moves any number by more than 0.10 points.
  - Removing them makes the observer more accurate.
  - It also hands the validator a lead of 1 to 2 points.
- **V's and C's holds, the inclusion lottery, the post-match lottery and registry bundling** each move the observer by 0.10 points or less when removed alone.
  - Two of the twelve effects have intervals above 0: the post-match lottery and registry bundling, both at R = 100, +0.06 points each.
  - None moves the best component's accuracy by more than 0.13 points (`results/TABLES.md`).
- **Removed together, the five raise the observer by 0.73 to 1.46 points.** That is about twice the effect of removing the role-aware holds alone.
  - The difference points to the four smaller mechanisms mattering together more than any one of them alone.
  - That contrast (all five removed, against role-aware holds removed) has no paired interval here.
- **The four smaller mechanisms cost about 160 seconds of mean latency between them.** The difference between 807 and 650 seconds measures this. The role-aware holds cost about 230 seconds.

## Alternative settings

Each build changes one setting of InternalCompromiseRun and is paired with it on the same records.

| Build | R | Observer: effect vs InternalCompromiseRun | Validator's lead | Content server's lead | Mean latency |
|---|---|---|---|---|---|
| relay hops at 180 s | 1 | -0.62 [-0.83, -0.41] | -0.37 [-0.78, -0.00] | -0.43 [-0.71, -0.16] | 1,199 s |
| relay hops at 180 s | 20 | -0.57 [-0.73, -0.40] | +0.10 [-0.18, +0.37] | -0.01 [-0.22, +0.20] | 1,189 s |
| relay hops at 180 s | 100 | -0.30 [-0.35, -0.24] | +0.06 [-0.03, +0.15] | +0.02 [-0.05, +0.09] | 1,192 s |
| role-aware holds at 360 s | 1 | -1.33 [-1.64, -1.01] | -0.64 [-0.96, -0.30] | -0.15 [-0.41, +0.12] | 1,337 s |
| role-aware holds at 360 s | 20 | -1.42 [-1.65, -1.17] | -0.17 [-0.41, +0.06] | +0.51 [+0.31, +0.69] | 1,324 s |
| role-aware holds at 360 s | 100 | -0.57 [-0.65, -0.49] | -0.28 [-0.36, -0.20] | +0.20 [+0.13, +0.27] | 1,328 s |
| gatekeeper hold at 120 s | 1 | +0.02 [-0.17, +0.21] | -0.17 [-0.55, +0.19] | -0.03 [-0.30, +0.25] | 1,068 s |
| gatekeeper hold at 120 s | 20 | -0.11 [-0.28, +0.06] | +0.35 [+0.05, +0.63] | +0.33 [+0.11, +0.56] | 1,059 s |
| gatekeeper hold at 120 s | 100 | -0.03 [-0.08, +0.03] | +0.13 [+0.04, +0.22] | +0.26 [+0.19, +0.33] | 1,062 s |

- **Relay hops at 180 s** lower the observer's accuracy by 0.30 to 0.62 points and the strongest component's by 0.51 to 0.72 points. Every lead stays at or below +0.10.
  - Latency rises by about 155 seconds.
  - Of the three alternative settings it is the only one that lowers accuracy without opening a lead.
- **Role-aware holds at 360 s** lower the observer the most, by 0.57 to 1.42 points, at about 290 seconds more latency.
  - At R = 20 and 100 the content server's lead rises to +0.51 and +0.20.
  - Its absolute accuracy still falls: 5.55% against 6.60% at R = 20.
- **The gatekeeper hold at 120 s** leaves the observer unchanged and opens small leads for the validator and the content server at R = 20 and 100 (+0.13 to +0.35).
  - It costs about 26 seconds.
  - It gives no gain in accuracy over InternalCompromiseRun.

## F and I submitting together

Real records at 60 decoys, 20 runs per cell (`results/pair_gaps.json`). Each entry gives the range over R = 1, 20 and 100.

| Build | Within 5 s at submission | Within 5 s as they leave | Separated pairs put back in one bundle |
|---|---|---|---|
| InternalCompromiseRun | 3.7% to 4.0% | 25.3% to 26.3% | 22.5% to 23.3% |
| without the post-match lottery | 21.3% to 21.8% | 30.8% to 31.4% | 11.8% to 12.5% |
| without registry bundling | 3.7% to 4.0% | 3.7% to 4.0% | not applicable |
| without role-aware holds | 8.2% to 8.6% | 50.1% to 51.2% | 45.9% to 46.7% |
| without all five | 31.2% to 31.7% | 31.2% to 31.7% | not applicable |
| role-aware holds at 360 s | 2.0% to 2.2% | 14.4% to 14.9% | 12.7% to 13.1% |

- **The post-match lottery separates F's and I's submissions.**
  - Without it, 21% to 22% of pairs submit within 5 seconds of each other; with it, 4%.
  - Removing it changes the observer's and the strongest component's accuracy by at most 0.12 points.
- **Registry bundling puts about a quarter of the separated pairs back into one bundle.** Under InternalCompromiseRun, 25% to 26% of pairs leave the registry together.

## Checks and controls

- **Timing.** Measured on 10 runs at R = 20 (`results/timing_check.json`). Every stage's mean lies within 1.2 seconds of its target, and every maximum sits at its cap. The full table is in `README.md`.
- **Outcome-shuffle control.**
  - In 25 of the 210 component-and-cell rows across the ten builds, the shuffled-outcome AUC interval excludes 0.5. About 10 would be expected by chance.
  - Every one lies within 0.013 of 0.5. Confidence AUCs within 0.03 of 0.5 are not read as signal, because permuting within a run keeps each run's success rate, so a small association between runs can survive the shuffle.

## Scope

- **One decoy level (60).** At 60 decoys every build passes the claim criterion. At lower decoy levels the mechanisms may matter for the criterion itself, as well as for the leads.
- **Single compromised component.** Collusion between components is not modelled.
- **The board's posting order is not modelled as a vantage.**

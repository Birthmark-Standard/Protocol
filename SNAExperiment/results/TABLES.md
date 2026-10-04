# InternalCompromiseRun tables

End-to-end delay under InternalCompromiseRun: D = 1036.6 s; rates are R / D and 60 / D, so R real and 60 decoy transactions are in flight. Device level: the vantage names the device behind a registry record. Intervals are 95%, resampling whole runs.

## Timing as simulated (R = 20)

| Stage | Mean | Std dev | Maximum |
|---|---|---|---|
| device, credential channel | 118.8 s | 103.1 s | 360.0 s |
| device, content channels | 237.8 s | 205.4 s | 720.0 s |
| relay hops | 119.7 s | 103.0 s | 360.0 s |
| C before CV-1 | 30.3 s | 25.3 s | 90.0 s |
| V before CV-2 | 30.2 s | 25.3 s | 90.0 s |
| C fan-out, per leg | 59.6 s | 51.2 s | 180.0 s |
| gatekeeper hold | 30.4 s | 25.3 s | 90.0 s |
| departure bundling wait | 101.0 s | 90.9 s | 359.9 s |
| F/I pre-match hold | 240.8 s | 206.9 s | 720.0 s |
| post-match lottery | 30.1 s | 25.3 s | 90.0 s |
| registry bundle wait | 60.1 s | 34.7 s | 120.0 s |
| capture to finalization | 1033.8 s | 270.6 s | 2248.7 s |

Postings per departure bundle at one gatekeeper: mean 2.33; 32.4% of bundles hold fewer than two; 10.0% are empty.

## The adversary against InternalCompromiseRun

For each single compromised component: how often it names the right device, against two chance rates (a guess among the devices that could have produced the record, and a guess among every registered device), its lead over a passive observer, and its own confidence that a match is right.

### R = 1, 60 decoys (70 registered devices; one in 70 is 1.43%)

| Component | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Multiple of one in N | Lead over observer [95% CI] | Mean confidence in its match | Confidence, 99th percentile | Top 1% right [95% CI] | Decisions in a most-confident set right more than half the time |
|---|---|---|---|---|---|---|---|---|---|
| Passive observer | 9.91% [9.48%, 10.33%] | 2.03% | ×4.88 [4.66, 5.09] | ×6.9 | reference | 7.58% | 12.61% | 25.8% [21.8%, 30.3%] | 0 of 39,857 |
| First hop, credential | 9.89% [9.46%, 10.30%] | 2.03% | ×4.87 [4.66, 5.07] | ×6.9 | -0.02 [-0.11, +0.06] | 7.63% | 12.74% | 25.4% [23.3%, 27.6%] | 0 of 159,428 |
| First hop, content | 9.89% [9.48%, 10.28%] | 2.03% | ×4.87 [4.67, 5.06] | ×6.9 | -0.02 [-0.10, +0.06] | 7.63% | 12.74% | 25.4% [23.3%, 27.6%] | 0 of 159,428 |
| Credential processor | 9.91% [9.48%, 10.33%] | 2.03% | ×4.88 [4.67, 5.09] | ×6.9 | +0.00 [-0.05, +0.05] | 7.58% | 12.61% | 25.5% [23.5%, 27.7%] | 0 of 159,428 |
| Validator | 9.51% [9.10%, 9.93%] | 1.84% | ×5.17 [4.95, 5.40] | ×6.7 | -0.40 [-0.79, -0.05] | 8.15% | 13.64% | 22.1% [18.3%, 26.4%] | 0 of 39,857 |
| Gatekeeper | 9.95% [9.54%, 10.38%] | 2.03% | ×4.90 [4.69, 5.11] | ×7.0 | +0.04 [-0.06, +0.14] | 7.62% | 12.76% | 26.5% [24.1%, 29.1%] | 9 of 119,571 |
| Content server | 9.84% [9.52%, 10.15%] | 2.18% | ×4.52 [4.37, 4.66] | ×6.9 | -0.07 [-0.31, +0.16] | 6.67% | 12.74% | 7.9% [6.2%, 10.0%] | 0 of 79,714 |

Claim criterion: **pass**. Mean capture to finalization: 1042 s (median 1023 s, 95th percentile 1524 s).

### R = 20, 60 decoys (92 registered devices; one in 92 is 1.09%)

| Component | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Multiple of one in N | Lead over observer [95% CI] | Mean confidence in its match | Confidence, 99th percentile | Top 1% right [95% CI] | Decisions in a most-confident set right more than half the time |
|---|---|---|---|---|---|---|---|---|---|
| Passive observer | 6.46% [6.15%, 6.78%] | 1.55% | ×4.17 [3.97, 4.38] | ×5.9 | reference | 6.03% | 9.82% | 13.4% [10.5%, 17.0%] | 7 of 41,728 |
| First hop, credential | 6.47% [6.17%, 6.79%] | 1.55% | ×4.18 [3.98, 4.39] | ×6.0 | +0.01 [-0.07, +0.09] | 6.07% | 9.84% | 13.7% [12.1%, 15.4%] | 29 of 166,912 |
| First hop, content | 6.47% [6.17%, 6.77%] | 1.55% | ×4.18 [3.98, 4.37] | ×6.0 | +0.01 [-0.07, +0.09] | 6.07% | 9.84% | 13.7% [12.1%, 15.4%] | 29 of 166,912 |
| Credential processor | 6.46% [6.14%, 6.77%] | 1.55% | ×4.17 [3.96, 4.37] | ×5.9 | -0.01 [-0.04, +0.03] | 6.02% | 9.81% | 13.5% [11.9%, 15.2%] | 31 of 166,912 |
| Validator | 6.32% [6.05%, 6.59%] | 1.40% | ×4.50 [4.32, 4.70] | ×5.8 | -0.14 [-0.42, +0.12] | 6.51% | 10.50% | 9.4% [6.9%, 12.5%] | 7 of 41,728 |
| Gatekeeper | 6.45% [6.14%, 6.74%] | 1.55% | ×4.16 [3.96, 4.35] | ×5.9 | -0.01 [-0.10, +0.07] | 6.06% | 9.84% | 13.8% [12.0%, 15.8%] | 23 of 125,184 |
| Content server | 6.60% [6.35%, 6.84%] | 1.66% | ×3.98 [3.83, 4.12] | ×6.1 | +0.14 [-0.06, +0.35] | 5.25% | 9.94% | 3.7% [2.6%, 5.2%] | 0 of 83,456 |

Claim criterion: **pass**. Mean capture to finalization: 1033 s (median 1010 s, 95th percentile 1523 s).

### R = 100, 60 decoys (185 registered devices; one in 185 is 0.54%)

| Component | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Multiple of one in N | Lead over observer [95% CI] | Mean confidence in its match | Confidence, 99th percentile | Top 1% right [95% CI] | Decisions in a most-confident set right more than half the time |
|---|---|---|---|---|---|---|---|---|---|
| Passive observer | 3.48% [3.40%, 3.56%] | 0.77% | ×4.50 [4.41, 4.61] | ×6.4 | reference | 3.32% | 5.09% | 6.5% [5.5%, 7.6%] | 0 of 207,570 |
| First hop, credential | 3.47% [3.40%, 3.54%] | 0.77% | ×4.49 [4.40, 4.58] | ×6.4 | -0.01 [-0.04, +0.01] | 3.34% | 5.14% | 6.2% [5.7%, 6.7%] | 0 of 830,280 |
| First hop, content | 3.47% [3.39%, 3.54%] | 0.77% | ×4.49 [4.39, 4.58] | ×6.4 | -0.01 [-0.03, +0.01] | 3.34% | 5.14% | 6.2% [5.7%, 6.7%] | 0 of 830,280 |
| Credential processor | 3.47% [3.39%, 3.54%] | 0.77% | ×4.50 [4.40, 4.59] | ×6.4 | -0.01 [-0.02, +0.00] | 3.32% | 5.09% | 6.4% [5.9%, 7.0%] | 0 of 830,280 |
| Validator | 3.41% [3.33%, 3.49%] | 0.70% | ×4.89 [4.77, 5.00] | ×6.3 | -0.06 [-0.15, +0.02] | 3.60% | 5.63% | 5.3% [4.5%, 6.4%] | 0 of 207,570 |
| Gatekeeper | 3.46% [3.39%, 3.55%] | 0.77% | ×4.49 [4.39, 4.59] | ×6.4 | -0.01 [-0.04, +0.01] | 3.33% | 5.11% | 6.7% [6.1%, 7.4%] | 0 of 622,710 |
| Content server | 3.72% [3.64%, 3.79%] | 0.83% | ×4.49 [4.40, 4.58] | ×6.9 | +0.24 [+0.18, +0.30] | 2.80% | 5.30% | 2.2% [1.8%, 2.7%] | 0 of 415,140 |

Claim criterion: **pass**. Mean capture to finalization: 1037 s (median 1009 s, 95th percentile 1530 s).

## Reliability of the adversary's confidence (R = 20)

Matches sorted into ten equal groups by the component's own calibrated confidence; each row compares the group's mean confidence with how often its matches were right.

| Component | Lowest decile: confidence / right | Median decile | Highest decile | Mean absolute gap |
|---|---|---|---|---|
| Passive observer | 4.4% / 4.9% | 6.0% / 6.7% | 8.6% / 9.6% | 0.43 points |
| First hop, credential | 4.4% / 4.6% | 6.0% / 6.8% | 8.6% / 9.7% | 0.42 points |
| First hop, content | 4.4% / 4.6% | 6.0% / 6.8% | 8.6% / 9.7% | 0.42 points |
| Credential processor | 4.4% / 4.8% | 6.0% / 6.8% | 8.6% / 9.6% | 0.47 points |
| Validator | 4.7% / 4.6% | 6.5% / 6.1% | 9.3% / 8.7% | 0.24 points |
| Gatekeeper | 4.4% / 4.5% | 6.0% / 6.3% | 8.6% / 9.5% | 0.39 points |
| Content server | 3.8% / 5.2% | 5.1% / 6.9% | 8.2% / 8.3% | 1.35 points |

## What each mechanism contributes: InternalCompromiseRun with one mechanism removed

Paired against InternalCompromiseRun on the same records (the effect is the build minus InternalCompromiseRun, in points).

| Build | R | Strongest component | Device named | Multiple of chance [95% CI] | Largest lead over observer | Observer: effect [95% CI] | Strongest InternalCompromiseRun component: effect [95% CI] | Top 1% right, best component | Mean latency |
|---|---|---|---|---|---|---|---|---|---|
| InternalCompromiseRun | 1 | Gatekeeper | 9.95% | ×4.90 [4.69, 5.11] | +0.04 | reference | reference | 26.5% | 1042 s |
| without V's and C's holds | 1 | Passive observer | 9.90% | ×4.89 [4.68, 5.11] | -0.01 | -0.01 [-0.18, +0.16] | -0.10 [-0.23, +0.05] | 28.3% | 1030 s |
| without the inclusion lottery (next-boundary bundling) | 1 | Passive observer | 9.97% | ×4.94 [4.72, 5.15] | -0.03 | +0.06 [-0.15, +0.27] | -0.05 [-0.22, +0.12] | 26.8% | 1026 s |
| without the post-match lottery | 1 | Credential processor | 9.89% | ×4.93 [4.72, 5.13] | +0.01 | -0.03 [-0.19, +0.14] | -0.12 [-0.24, +0.01] | 24.3% | 1010 s |
| without registry bundling | 1 | Passive observer | 9.97% | ×4.77 [4.57, 4.98] | -0.01 | +0.06 [-0.10, +0.23] | -0.02 [-0.14, +0.12] | 25.5% | 983 s |
| without role-aware holds (device content and F/I at 120 s) | 1 | Validator | 12.62% | ×5.40 [5.22, 5.58] | +2.01 | +0.70 [+0.37, +1.05] | +0.65 [+0.34, +0.97] | 27.3% | 807 s |
| without all five | 1 | Validator | 12.54% | ×5.42 [5.25, 5.60] | +1.17 | +1.46 [+1.16, +1.76] | +1.47 [+1.20, +1.75] | 27.3% | 650 s |
| InternalCompromiseRun | 20 | Content server | 6.60% | ×3.98 [3.83, 4.12] | +0.14 | reference | reference | 13.8% | 1033 s |
| without V's and C's holds | 20 | Content server | 6.59% | ×3.98 [3.82, 4.13] | +0.22 | -0.10 [-0.26, +0.07] | -0.02 [-0.18, +0.14] | 14.3% | 1020 s |
| without the inclusion lottery (next-boundary bundling) | 20 | Content server | 6.65% | ×4.03 [3.87, 4.18] | +0.29 | -0.10 [-0.26, +0.07] | +0.05 [-0.12, +0.20] | 13.8% | 1017 s |
| without the post-match lottery | 20 | Content server | 6.58% | ×4.00 [3.84, 4.15] | +0.20 | -0.09 [-0.24, +0.07] | -0.03 [-0.19, +0.13] | 14.5% | 999 s |
| without registry bundling | 20 | Content server | 6.73% | ×3.99 [3.83, 4.14] | +0.23 | +0.04 [-0.10, +0.18] | +0.13 [-0.06, +0.31] | 14.4% | 973 s |
| without role-aware holds (device content and F/I at 120 s) | 20 | Validator | 8.82% | ×4.95 [4.79, 5.11] | +1.49 | +0.87 [+0.60, +1.14] | +1.50 [+1.27, +1.71] | 14.9% | 807 s |
| without all five | 20 | Validator | 8.68% | ×4.93 [4.75, 5.12] | +0.91 | +1.31 [+1.05, +1.59] | +1.46 [+1.22, +1.69] | 14.8% | 647 s |
| InternalCompromiseRun | 100 | Content server | 3.72% | ×4.49 [4.40, 4.58] | +0.24 | reference | reference | 6.7% | 1037 s |
| without V's and C's holds | 100 | Content server | 3.68% | ×4.46 [4.38, 4.55] | +0.18 | +0.02 [-0.02, +0.07] | -0.03 [-0.09, +0.02] | 6.8% | 1025 s |
| without the inclusion lottery (next-boundary bundling) | 100 | Content server | 3.68% | ×4.47 [4.38, 4.56] | +0.16 | +0.04 [-0.01, +0.10] | -0.03 [-0.10, +0.03] | 6.4% | 1021 s |
| without the post-match lottery | 100 | Content server | 3.70% | ×4.51 [4.42, 4.59] | +0.16 | +0.06 [+0.02, +0.11] | -0.02 [-0.07, +0.03] | 6.7% | 1003 s |
| without registry bundling | 100 | Content server | 3.69% | ×4.38 [4.29, 4.47] | +0.16 | +0.06 [+0.01, +0.10] | -0.03 [-0.09, +0.04] | 6.3% | 976 s |
| without role-aware holds (device content and F/I at 120 s) | 100 | Validator | 4.95% | ×5.57 [5.46, 5.68] | +1.04 | +0.43 [+0.37, +0.50] | +0.62 [+0.54, +0.69] | 8.8% | 807 s |
| without all five | 100 | Validator | 4.86% | ×5.52 [5.42, 5.62] | +0.64 | +0.73 [+0.66, +0.81] | +0.74 [+0.67, +0.81] | 8.0% | 649 s |

## Alternative settings

Paired against InternalCompromiseRun on the same records (the effect is the build minus InternalCompromiseRun, in points).

| Build | R | Strongest component | Device named | Multiple of chance [95% CI] | Largest lead over observer | Observer: effect [95% CI] | Strongest InternalCompromiseRun component: effect [95% CI] | Top 1% right, best component | Mean latency |
|---|---|---|---|---|---|---|---|---|---|
| InternalCompromiseRun | 1 | Gatekeeper | 9.95% | ×4.90 [4.69, 5.11] | +0.04 | reference | reference | 26.5% | 1042 s |
| relay hops at 180 s | 1 | Passive observer | 9.29% | ×4.97 [4.74, 5.20] | -0.04 | -0.62 [-0.83, -0.41] | -0.71 [-0.88, -0.53] | 23.6% | 1199 s |
| device content and F/I at 360 s | 1 | First hop, credential | 8.61% | ×4.75 [4.53, 4.96] | +0.03 | -1.33 [-1.64, -1.01] | -1.39 [-1.66, -1.10] | 22.3% | 1337 s |
| gatekeeper hold at 120 s | 1 | Credential processor | 9.94% | ×4.87 [4.65, 5.08] | +0.01 | +0.02 [-0.17, +0.21] | -0.04 [-0.19, +0.13] | 24.6% | 1068 s |
| InternalCompromiseRun | 20 | Content server | 6.60% | ×3.98 [3.83, 4.12] | +0.14 | reference | reference | 13.8% | 1033 s |
| relay hops at 180 s | 20 | Validator | 6.00% | ×4.53 [4.34, 4.73] | +0.10 | -0.57 [-0.73, -0.40] | -0.72 [-0.92, -0.53] | 13.6% | 1189 s |
| device content and F/I at 360 s | 20 | Content server | 5.55% | ×3.76 [3.61, 3.91] | +0.51 | -1.42 [-1.65, -1.17] | -1.05 [-1.25, -0.86] | 12.1% | 1324 s |
| gatekeeper hold at 120 s | 20 | Validator | 6.70% | ×4.78 [4.58, 4.97] | +0.35 | -0.11 [-0.28, +0.06] | +0.09 [-0.08, +0.25] | 14.5% | 1059 s |
| InternalCompromiseRun | 100 | Content server | 3.72% | ×4.49 [4.40, 4.58] | +0.24 | reference | reference | 6.7% | 1037 s |
| relay hops at 180 s | 100 | Validator | 3.24% | ×4.92 [4.79, 5.04] | +0.06 | -0.30 [-0.35, -0.24] | -0.51 [-0.57, -0.45] | 6.2% | 1192 s |
| device content and F/I at 360 s | 100 | Content server | 3.10% | ×4.22 [4.13, 4.30] | +0.20 | -0.57 [-0.65, -0.49] | -0.61 [-0.68, -0.54] | 5.0% | 1328 s |
| gatekeeper hold at 120 s | 100 | Content server | 3.71% | ×4.46 [4.36, 4.55] | +0.26 | -0.03 [-0.08, +0.03] | -0.01 [-0.07, +0.06] | 6.4% | 1062 s |

## F and I submitting together

| Build | R | Within 5 s at submission | Within 5 s as they leave |
|---|---|---|---|
| InternalCompromiseRun | 1 | 3.9% | 26.2% |
| InternalCompromiseRun | 20 | 3.7% | 25.3% |
| InternalCompromiseRun | 100 | 4.0% | 26.3% |
| without V's and C's holds | 1 | 3.1% | 22.6% |
| without V's and C's holds | 20 | 3.5% | 22.8% |
| without V's and C's holds | 100 | 3.4% | 22.8% |
| without the inclusion lottery (next-boundary bundling) | 1 | 2.9% | 22.1% |
| without the inclusion lottery (next-boundary bundling) | 20 | 3.0% | 20.8% |
| without the inclusion lottery (next-boundary bundling) | 100 | 3.0% | 21.4% |
| without the post-match lottery | 1 | 21.6% | 31.4% |
| without the post-match lottery | 20 | 21.8% | 31.0% |
| without the post-match lottery | 100 | 21.3% | 30.8% |
| without registry bundling | 1 | 3.9% | 3.9% |
| without registry bundling | 20 | 3.7% | 3.7% |
| without registry bundling | 100 | 4.0% | 4.0% |
| without role-aware holds (device content and F/I at 120 s) | 1 | 8.6% | 50.6% |
| without role-aware holds (device content and F/I at 120 s) | 20 | 8.2% | 50.1% |
| without role-aware holds (device content and F/I at 120 s) | 100 | 8.6% | 51.2% |
| without all five | 1 | 31.7% | 31.7% |
| without all five | 20 | 31.2% | 31.2% |
| without all five | 100 | 31.6% | 31.6% |
| relay hops at 180 s | 1 | 4.1% | 26.2% |
| relay hops at 180 s | 20 | 4.0% | 25.6% |
| relay hops at 180 s | 100 | 4.3% | 26.6% |
| device content and F/I at 360 s | 1 | 2.2% | 14.9% |
| device content and F/I at 360 s | 20 | 2.0% | 14.4% |
| device content and F/I at 360 s | 100 | 2.0% | 14.9% |
| gatekeeper hold at 120 s | 1 | 5.0% | 32.8% |
| gatekeeper hold at 120 s | 20 | 5.3% | 31.3% |
| gatekeeper hold at 120 s | 100 | 5.0% | 32.2% |

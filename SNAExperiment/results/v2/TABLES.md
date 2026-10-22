# InternalCompromiseRun tables

End-to-end delay under InternalCompromiseRun: D = 1108.8 s; rates are R / D and 60 / D, so R real and 60 decoy transactions are in flight. Device level: the vantage names the device behind a registry record. Intervals are 95%, resampling whole runs.

## Timing as simulated (R = 20)

| Stage | Mean | Std dev | Maximum |
|---|---|---|---|
| device, credential channel | 120.1 s | 103.2 s | 359.9 s |
| device, content channels | 240.3 s | 206.1 s | 720.0 s |
| relay hops | 120.2 s | 103.0 s | 360.0 s |
| C before CV-1 | 29.4 s | 24.9 s | 90.0 s |
| V before CV-2 | 29.9 s | 25.2 s | 90.0 s |
| C fan-out, per leg | 45.0 s | 30.9 s | 178.7 s |
| gatekeeper hold | 30.3 s | 25.3 s | 90.0 s |
| departure bundling wait | 101.8 s | 91.4 s | 359.9 s |
| F/I pre-match hold | 244.2 s | 208.4 s | 720.0 s |
| post-match lottery | 30.1 s | 25.4 s | 90.0 s |
| registry bundle wait | 60.0 s | 34.5 s | 120.0 s |
| registry posting wait | 52.9 s | 28.9 s | 109.6 s |
| capture to finalization | 1090.0 s | 277.1 s | 2217.8 s |

Postings per departure bundle at one gatekeeper: mean 2.19; 36.2% of bundles hold fewer than two; 11.1% are empty.

## The adversary against InternalCompromiseRun

For each single compromised component: how often it names the right device, against two chance rates (a guess among the devices that could have produced the record, and a guess among every registered device), its lead over a passive observer, and its own confidence that a match is right.

### R = 1, 60 decoys (66 registered devices; one in 66 is 1.52%)

| Component | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Multiple of one in N | Lead over observer [95% CI] | Mean confidence in its match | Confidence, 99th percentile | Top 1% right [95% CI] | Decisions in a most-confident set right more than half the time |
|---|---|---|---|---|---|---|---|---|---|
| Passive observer | 8.47% [8.07%, 8.88%] | 1.72% | ×4.92 [4.69, 5.17] | ×5.6 | reference | 10.55% | 20.24% | 18.3% [14.8%, 22.4%] | 19 of 39,888 |
| First hop, credential | 8.45% [8.03%, 8.88%] | 1.72% | ×4.91 [4.67, 5.16] | ×5.6 | -0.02 [-0.07, +0.03] | 10.56% | 20.24% | 18.1% [16.3%, 20.1%] | 1 of 159,552 |
| First hop, content | 8.45% [8.03%, 8.87%] | 1.72% | ×4.91 [4.67, 5.16] | ×5.6 | -0.02 [-0.06, +0.03] | 10.56% | 20.24% | 18.1% [16.3%, 20.1%] | 1 of 159,552 |
| Credential processor | 8.46% [8.05%, 8.89%] | 1.72% | ×4.92 [4.68, 5.17] | ×5.6 | -0.00 [-0.04, +0.03] | 10.55% | 20.24% | 18.3% [16.5%, 20.3%] | 7 of 159,552 |
| Validator | 8.00% [7.61%, 8.39%] | 1.84% | ×4.34 [4.13, 4.55] | ×5.3 | -0.47 [-0.78, -0.17] | 6.86% | 11.07% | 18.8% [15.3%, 22.9%] | 1 of 39,888 |
| Gatekeeper | 8.43% [8.01%, 8.85%] | 1.72% | ×4.90 [4.66, 5.15] | ×5.6 | -0.04 [-0.11, +0.03] | 10.57% | 20.26% | 18.0% [16.0%, 20.3%] | 77 of 119,664 |
| Content server | 9.97% [9.56%, 10.36%] | 1.81% | ×5.52 [5.29, 5.74] | ×6.6 | +1.50 [+1.26, +1.72] | 12.06% | 23.78% | 21.9% [19.2%, 24.9%] | 0 of 79,776 |

Claim criterion: **pass**. Mean capture to finalization: 1099 s (median 1077 s, 95th percentile 1619 s).

### R = 20, 60 decoys (87 registered devices; one in 87 is 1.15%)

| Component | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Multiple of one in N | Lead over observer [95% CI] | Mean confidence in its match | Confidence, 99th percentile | Top 1% right [95% CI] | Decisions in a most-confident set right more than half the time |
|---|---|---|---|---|---|---|---|---|---|
| Passive observer | 5.83% [5.49%, 6.18%] | 1.31% | ×4.46 [4.20, 4.73] | ×5.1 | reference | 8.57% | 16.15% | 13.8% [10.7%, 17.5%] | 0 of 40,033 |
| First hop, credential | 5.81% [5.48%, 6.14%] | 1.31% | ×4.45 [4.20, 4.70] | ×5.1 | -0.02 [-0.06, +0.02] | 8.57% | 16.18% | 14.0% [12.4%, 15.8%] | 0 of 160,132 |
| First hop, content | 5.81% [5.48%, 6.15%] | 1.31% | ×4.45 [4.19, 4.71] | ×5.1 | -0.02 [-0.06, +0.03] | 8.57% | 16.18% | 14.0% [12.4%, 15.8%] | 0 of 160,132 |
| Credential processor | 5.79% [5.47%, 6.13%] | 1.31% | ×4.43 [4.18, 4.69] | ×5.0 | -0.04 [-0.07, -0.02] | 8.56% | 16.12% | 13.9% [12.3%, 15.7%] | 0 of 160,132 |
| Validator | 5.33% [5.03%, 5.62%] | 1.40% | ×3.80 [3.59, 4.01] | ×4.6 | -0.50 [-0.76, -0.24] | 5.44% | 8.54% | 9.8% [7.2%, 13.1%] | 0 of 40,033 |
| Gatekeeper | 5.82% [5.49%, 6.16%] | 1.31% | ×4.46 [4.20, 4.71] | ×5.1 | -0.01 [-0.06, +0.05] | 6.89% | 14.81% | 9.6% [8.0%, 11.4%] | 0 of 120,099 |
| Content server | 7.06% [6.78%, 7.37%] | 1.37% | ×5.14 [4.94, 5.37] | ×6.1 | +1.23 [+1.01, +1.44] | 9.84% | 19.35% | 14.2% [12.0%, 16.8%] | 0 of 80,066 |

Claim criterion: **pass**. Mean capture to finalization: 1089 s (median 1070 s, 95th percentile 1569 s).

### R = 100, 60 decoys (173 registered devices; one in 173 is 0.58%)

| Component | Device named [95% CI] | Chance, feasible set | Multiple of chance [95% CI] | Multiple of one in N | Lead over observer [95% CI] | Mean confidence in its match | Confidence, 99th percentile | Top 1% right [95% CI] | Decisions in a most-confident set right more than half the time |
|---|---|---|---|---|---|---|---|---|---|
| Passive observer | 3.25% [3.16%, 3.34%] | 0.66% | ×4.95 [4.82, 5.09] | ×5.6 | reference | 4.99% | 9.16% | 5.4% [4.5%, 6.5%] | 0 of 194,130 |
| First hop, credential | 3.26% [3.17%, 3.35%] | 0.66% | ×4.97 [4.83, 5.11] | ×5.6 | +0.01 [-0.00, +0.03] | 4.99% | 9.16% | 5.5% [5.0%, 6.0%] | 0 of 776,520 |
| First hop, content | 3.26% [3.17%, 3.35%] | 0.66% | ×4.97 [4.84, 5.10] | ×5.6 | +0.01 [-0.00, +0.03] | 4.99% | 9.16% | 5.5% [5.0%, 6.0%] | 0 of 776,520 |
| Credential processor | 3.25% [3.16%, 3.34%] | 0.66% | ×4.95 [4.82, 5.09] | ×5.6 | +0.00 [-0.01, +0.01] | 4.99% | 9.16% | 5.4% [4.9%, 5.9%] | 0 of 776,520 |
| Validator | 2.94% [2.85%, 3.03%] | 0.70% | ×4.18 [4.06, 4.30] | ×5.1 | -0.31 [-0.40, -0.23] | 3.01% | 4.54% | 4.7% [3.9%, 5.8%] | 0 of 194,130 |
| Gatekeeper | 3.25% [3.17%, 3.34%] | 0.66% | ×4.96 [4.84, 5.10] | ×5.6 | +0.01 [-0.01, +0.03] | 4.99% | 9.16% | 5.6% [5.0%, 6.2%] | 0 of 582,390 |
| Content server | 3.98% [3.90%, 4.06%] | 0.69% | ×5.78 [5.66, 5.89] | ×6.9 | +0.73 [+0.67, +0.80] | 5.80% | 11.02% | 6.2% [5.5%, 7.0%] | 0 of 388,260 |

Claim criterion: **pass**. Mean capture to finalization: 1089 s (median 1062 s, 95th percentile 1585 s).

## Reliability of the adversary's confidence (R = 20)

Matches sorted into ten equal groups by the component's own calibrated confidence; each row compares the group's mean confidence with how often its matches were right.

| Component | Lowest decile: confidence / right | Median decile | Highest decile | Mean absolute gap |
|---|---|---|---|---|
| Passive observer | 5.6% / 4.1% | 8.4% / 5.5% | 13.6% / 8.3% | 2.73 points |
| First hop, credential | 5.6% / 4.1% | 8.4% / 5.6% | 13.6% / 8.3% | 2.76 points |
| First hop, content | 5.6% / 4.1% | 8.4% / 5.6% | 13.6% / 8.3% | 2.76 points |
| Credential processor | 5.6% / 4.0% | 8.4% / 5.4% | 13.6% / 8.3% | 2.78 points |
| Validator | 4.0% / 4.1% | 5.4% / 5.8% | 7.6% / 7.7% | 0.26 points |
| Gatekeeper | 4.1% / 4.2% | 6.6% / 5.4% | 12.3% / 7.8% | 1.46 points |
| Content server | 6.2% / 4.7% | 9.6% / 6.5% | 16.1% / 10.2% | 2.78 points |

## What each mechanism contributes: InternalCompromiseRun with one mechanism removed

Paired against InternalCompromiseRun on the same records (the effect is the build minus InternalCompromiseRun, in points).

| Build | R | Strongest component | Device named | Multiple of chance [95% CI] | Largest lead over observer | Observer: effect [95% CI] | Strongest InternalCompromiseRun component: effect [95% CI] | Top 1% right, best component | Mean latency |
|---|---|---|---|---|---|---|---|---|---|
| InternalCompromiseRun | 1 | Content server | 9.97% | ×5.52 [5.29, 5.74] | +1.50 | reference | reference | 21.9% | 1099 s |
| without V's and C's holds | 1 | Content server | 9.88% | ×5.46 [5.24, 5.69] | +1.56 | -0.15 [-0.26, -0.04] | -0.09 [-0.19, +0.01] | 21.1% | 1089 s |
| without the inclusion lottery (next-boundary bundling) | 1 | Content server | 9.90% | ×5.47 [5.25, 5.69] | +1.60 | -0.17 [-0.30, -0.03] | -0.07 [-0.17, +0.04] | 21.7% | 1086 s |
| without the post-match lottery | 1 | Content server | 10.02% | ×5.54 [5.32, 5.77] | +1.72 | -0.17 [-0.31, -0.03] | +0.05 [-0.09, +0.20] | 22.1% | 1067 s |
| without registry bundling | 1 | Content server | 9.95% | ×5.49 [5.27, 5.71] | +1.52 | -0.03 [-0.19, +0.13] | -0.02 [-0.14, +0.11] | 22.7% | 1040 s |
| without role-aware holds (device content and F/I at 120 s) | 1 | Content server | 11.59% | ×5.49 [5.30, 5.67] | +1.39 | +1.73 [+1.39, +2.08] | +1.63 [+1.35, +1.92] | 23.4% | 860 s |
| without all five | 1 | Content server | 11.48% | ×5.31 [5.13, 5.51] | +1.04 | +1.98 [+1.62, +2.34] | +1.52 [+1.25, +1.81] | 27.1% | 707 s |
| InternalCompromiseRun | 20 | Content server | 7.06% | ×5.14 [4.94, 5.37] | +1.23 | reference | reference | 14.2% | 1089 s |
| without V's and C's holds | 20 | Content server | 7.03% | ×5.12 [4.90, 5.34] | +1.30 | -0.09 [-0.20, +0.00] | -0.03 [-0.11, +0.05] | 14.6% | 1077 s |
| without the inclusion lottery (next-boundary bundling) | 20 | Content server | 7.02% | ×5.11 [4.90, 5.33] | +1.32 | -0.12 [-0.25, -0.01] | -0.04 [-0.13, +0.04] | 15.0% | 1074 s |
| without the post-match lottery | 20 | Content server | 6.95% | ×5.06 [4.84, 5.28] | +1.21 | -0.08 [-0.22, +0.06] | -0.11 [-0.22, +0.01] | 13.1% | 1054 s |
| without registry bundling | 20 | Content server | 7.04% | ×5.12 [4.91, 5.34] | +1.16 | +0.05 [-0.09, +0.19] | -0.02 [-0.14, +0.11] | 14.1% | 1031 s |
| without role-aware holds (device content and F/I at 120 s) | 20 | Content server | 8.24% | ×5.13 [4.96, 5.30] | +1.30 | +1.11 [+0.85, +1.35] | +1.18 [+0.97, +1.40] | 18.2% | 854 s |
| without all five | 20 | Content server | 8.05% | ×4.90 [4.72, 5.08] | +1.01 | +1.21 [+0.95, +1.47] | +0.99 [+0.76, +1.22] | 15.7% | 704 s |
| InternalCompromiseRun | 100 | Content server | 3.98% | ×5.78 [5.66, 5.89] | +0.73 | reference | reference | 6.2% | 1089 s |
| without V's and C's holds | 100 | Content server | 3.95% | ×5.72 [5.61, 5.83] | +0.72 | -0.02 [-0.06, +0.01] | -0.03 [-0.06, -0.00] | 5.9% | 1077 s |
| without the inclusion lottery (next-boundary bundling) | 100 | Content server | 3.93% | ×5.70 [5.58, 5.81] | +0.71 | -0.03 [-0.06, +0.01] | -0.05 [-0.08, -0.02] | 6.3% | 1074 s |
| without the post-match lottery | 100 | Content server | 4.00% | ×5.80 [5.69, 5.91] | +0.75 | +0.00 [-0.04, +0.04] | +0.02 [-0.02, +0.06] | 6.0% | 1055 s |
| without registry bundling | 100 | Content server | 3.99% | ×5.77 [5.66, 5.89] | +0.77 | -0.03 [-0.08, +0.02] | +0.01 [-0.03, +0.05] | 6.4% | 1031 s |
| without role-aware holds (device content and F/I at 120 s) | 100 | Content server | 4.68% | ×5.80 [5.69, 5.90] | +0.71 | +0.72 [+0.63, +0.81] | +0.69 [+0.62, +0.76] | 8.3% | 856 s |
| without all five | 100 | Content server | 4.64% | ×5.63 [5.53, 5.74] | +0.58 | +0.81 [+0.73, +0.90] | +0.66 [+0.59, +0.73] | 7.9% | 705 s |

## Alternative settings

Paired against InternalCompromiseRun on the same records (the effect is the build minus InternalCompromiseRun, in points).

| Build | R | Strongest component | Device named | Multiple of chance [95% CI] | Largest lead over observer | Observer: effect [95% CI] | Strongest InternalCompromiseRun component: effect [95% CI] | Top 1% right, best component | Mean latency |
|---|---|---|---|---|---|---|---|---|---|
| InternalCompromiseRun | 1 | Content server | 9.97% | ×5.52 [5.29, 5.74] | +1.50 | reference | reference | 21.9% | 1099 s |
| relay hops at 180 s | 1 | Content server | 8.86% | ×5.15 [4.93, 5.38] | +0.95 | -0.55 [-0.72, -0.38] | -1.10 [-1.28, -0.93] | 19.5% | 1255 s |
| device content and F/I at 360 s | 1 | Content server | 9.00% | ×5.39 [5.16, 5.62] | +1.85 | -1.32 [-1.57, -1.06] | -0.97 [-1.19, -0.72] | 18.9% | 1400 s |
| gatekeeper hold at 120 s | 1 | Content server | 10.07% | ×5.59 [5.36, 5.81] | +1.65 | -0.05 [-0.19, +0.10] | +0.10 [-0.01, +0.21] | 22.7% | 1124 s |
| InternalCompromiseRun | 20 | Content server | 7.06% | ×5.14 [4.94, 5.37] | +1.23 | reference | reference | 14.2% | 1089 s |
| relay hops at 180 s | 20 | Content server | 6.11% | ×4.67 [4.47, 4.90] | +0.68 | -0.40 [-0.56, -0.24] | -0.95 [-1.10, -0.78] | 11.6% | 1241 s |
| device content and F/I at 360 s | 20 | Content server | 6.45% | ×5.09 [4.89, 5.33] | +1.74 | -1.13 [-1.39, -0.86] | -0.61 [-0.79, -0.44] | 12.0% | 1381 s |
| gatekeeper hold at 120 s | 20 | Content server | 7.11% | ×5.19 [4.98, 5.42] | +1.21 | +0.07 [-0.06, +0.20] | +0.05 [-0.04, +0.14] | 13.9% | 1114 s |
| InternalCompromiseRun | 100 | Content server | 3.98% | ×5.78 [5.66, 5.89] | +0.73 | reference | reference | 6.2% | 1089 s |
| relay hops at 180 s | 100 | Content server | 3.45% | ×5.25 [5.13, 5.37] | +0.37 | -0.17 [-0.22, -0.11] | -0.53 [-0.58, -0.48] | 5.5% | 1245 s |
| device content and F/I at 360 s | 100 | Content server | 3.63% | ×5.70 [5.57, 5.83] | +0.97 | -0.59 [-0.66, -0.52] | -0.35 [-0.42, -0.29] | 5.3% | 1381 s |
| gatekeeper hold at 120 s | 100 | Content server | 4.04% | ×5.87 [5.75, 5.99] | +0.72 | +0.07 [+0.02, +0.11] | +0.06 [+0.01, +0.10] | 6.4% | 1113 s |

## F and I submitting together

| Build | R | Within 5 s at submission | Within 5 s as they leave |
|---|---|---|---|
| InternalCompromiseRun | 1 | 3.7% | 25.7% |
| InternalCompromiseRun | 20 | 4.0% | 24.7% |
| InternalCompromiseRun | 100 | 3.7% | 25.2% |
| without V's and C's holds | 1 | 2.8% | 22.2% |
| without V's and C's holds | 20 | 3.4% | 21.0% |
| without V's and C's holds | 100 | 3.0% | 21.8% |
| without the inclusion lottery (next-boundary bundling) | 1 | 3.0% | 21.8% |
| without the inclusion lottery (next-boundary bundling) | 20 | 3.4% | 20.5% |
| without the inclusion lottery (next-boundary bundling) | 100 | 3.0% | 21.0% |
| without the post-match lottery | 1 | 20.5% | 29.7% |
| without the post-match lottery | 20 | 20.0% | 29.7% |
| without the post-match lottery | 100 | 20.0% | 29.9% |
| without registry bundling | 1 | 3.7% | 3.7% |
| without registry bundling | 20 | 4.0% | 4.0% |
| without registry bundling | 100 | 3.7% | 3.7% |
| without role-aware holds (device content and F/I at 120 s) | 1 | 8.6% | 50.3% |
| without role-aware holds (device content and F/I at 120 s) | 20 | 8.4% | 49.5% |
| without role-aware holds (device content and F/I at 120 s) | 100 | 8.2% | 48.9% |
| without all five | 1 | 31.0% | 31.0% |
| without all five | 20 | 31.6% | 31.6% |
| without all five | 100 | 30.1% | 30.1% |
| relay hops at 180 s | 1 | 3.7% | 26.0% |
| relay hops at 180 s | 20 | 4.4% | 26.3% |
| relay hops at 180 s | 100 | 3.9% | 25.2% |
| device content and F/I at 360 s | 1 | 1.7% | 14.3% |
| device content and F/I at 360 s | 20 | 2.2% | 14.7% |
| device content and F/I at 360 s | 100 | 1.9% | 14.0% |
| gatekeeper hold at 120 s | 1 | 5.0% | 32.4% |
| gatekeeper hold at 120 s | 20 | 5.1% | 31.6% |
| gatekeeper hold at 120 s | 100 | 4.8% | 31.0% |
| permitted overlap | 1 | 3.8% | 25.3% |
| permitted overlap | 20 | 3.8% | 24.7% |
| permitted overlap | 100 | 3.7% | 25.3% |

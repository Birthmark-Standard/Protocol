# Paper table

## Run10: the specified protocol

How often a single compromised component, starting from a public registry record, names the device that produced it. Every hold follows the specification's timing. 60 decoy transactions are in flight; decoys are genuine transactions from registered identities, indistinguishable to every party. 200 runs per cell.

The bracket gives each component's lead over a passive observer on the same records, in percentage points. The first hops and the credential processor are scored on every record, because they cannot identify the records they took part in.

| Component | Holds | R = 1 | R = 20 | R = 100 | Its average confidence in a match (R = 1 / 20 / 100) |
|---|---|---|---|---|---|
| Passive observer | nothing | 9.91% | 6.46% | 3.48% | 7.6% / 6.0% / 3.3% |
| First hop, credential | relay transit key; source address | 9.89% (-0.02) | 6.47% (+0.01) | 3.47% (-0.01) | 7.6% / 6.1% / 3.3% |
| First hop, content | relay transit key; source address | 9.89% (-0.02) | 6.47% (+0.01) | 3.47% (-0.01) | 7.6% / 6.1% / 3.3% |
| Credential processor | transit and ring-signing keys | 9.91% (+0.00) | 6.46% (-0.01) | 3.47% (-0.01) | 7.6% / 6.0% / 3.3% |
| Validator | token-decryption and signing keys; device identity | 9.51% (-0.40) | 6.32% (-0.14) | 3.41% (-0.06) | 8.1% / 6.5% / 3.6% |
| Gatekeeper | transit and countersignature keys | 9.95% (+0.04) | 6.45% (-0.01) | 3.46% (-0.01) | 7.6% / 6.1% / 3.3% |
| Content server | transit and registry-signing keys | 9.84% (-0.07) | 6.60% (+0.14) | 3.72% (+0.24) | 6.7% / 5.3% / 2.8% |
| *Guess among devices that could have produced the record* | | *2.03%* | *1.55%* | *0.77%* | |
| *Guess among all registered devices* | | *1.43% (1 in 70)* | *1.09% (1 in 92)* | *0.54% (1 in 185)* | |

- **No single component gains more than a quarter of a point over the passive observer.**
- **The adversary's confidence identifies no record.**
  - Every component's most confident 1% of matches is right at most 26.5% of the time.
  - At most 0.019% of any component's decisions fall in a set of matches that is right more than half the time.
- **Mean time from capture to finalization is about 1,040 seconds**, with a 95th percentile of about 1,525 seconds.

### What each timing mechanism contributes (R = 20)

Paired with Run10 on the same records, in points.

| Build | Observer's accuracy (Run10), or its change from Run10 in points | Largest lead of any component over the observer | Mean latency |
|---|---|---|---|
| Run10 | 6.5% | +0.1 (content server) | 1,033 s |
| any one of V's and C's holds, the inclusion lottery, the post-match lottery or registry bundling removed | within 0.1 points of Run10 | at most +0.3 | 973 to 1,020 s |
| role-aware holds removed | +0.9 | +1.5 (validator) | 807 s |
| all five removed | +1.3 | +0.9 (validator) | 647 s |
| relay hops at 180 s | -0.6 | +0.1 (validator) | 1,189 s |
| role-aware holds at 360 s | -1.4 | +0.5 (content server) | 1,324 s |

The role-aware holds keep the validator, which knows each approving device, level with a passive observer. The other four mechanisms each make little difference alone, and some together: removing all five raises the observer by more than removing the role-aware holds alone. Longer relay holds lower the observer's accuracy further, at about 155 seconds of extra latency.

## Decoys at 40 in flight, before the specified timing

How often each compromised component, starting from a public registry record, names the device that produced it. Decoys are genuine transactions at a steady 40 in flight, indistinguishable to every party. Per-decision attack, 200 runs per cell.

Each accuracy cell gives, in brackets, the contribution over a passive observer on the same records, in percentage points. The first hops and the credential processor are scored on every record, because they cannot identify the records they took part in. The last column is accuracy with the decoy stream minus accuracy without it, on the same real records. Intervals and every other cell are in RESULTS.md.

| Vantage | Holds | Device named, R = 1 with decoys (random 2.1%) | Device named, R = 15 with decoys (random 1.6%) | Exact capture named, R = 1 with decoys (1/T = 2.4%) | Decoy effect on device accuracy, R = 1 |
|---|---|---|---|---|---|
| Baseline | nothing | 8.8% (+0.0) | 7.0% (+0.0) | 5.3% (+0.0) | -79.0 points |
| First hop, credential | relay transit key; source address | 8.7% (-0.1) | 6.9% (-0.1) | 5.4% (+0.0) | -79.0 points |
| First hop, content | relay transit key; source address | 8.7% (-0.1) | 6.9% (-0.1) | 5.4% (+0.0) | -79.0 points |
| Credential processor | transit and ring-signing keys | 8.7% (-0.0) | 6.9% (-0.0) | 5.4% (+0.0) | -79.0 points |
| Content server | transit and registry-signing keys | 9.6% (+0.9) | 7.7% (+0.8) | 6.5% (+1.2) | -80.2 points |
| Validator | token-decryption and signing keys; device identity | 9.8% (+1.1) | 7.8% (+0.8) | 5.9% (+0.5) | -79.7 points |
| Gatekeeper | transit and countersignature keys | 8.6% (-0.1) | 6.9% (-0.1) | 5.3% (+0.0) | -79.2 points |

With decoys, every component names the device behind a record at about 4 times the random-pick rate, and within about a point of what a passive observer achieves. Only the validator and the content server, which know which records they handled, add about a point. Decoys cut every component's accuracy at R = 1 by about 79 points.

## Gatekeeper departure bundling

Passive observer, device named, R = 1 (paired effect of bundling on the same records, in points). Board postings are internal, so the observer never sees a departure.

| Decoys in flight | Bundling off | Bundling on | Effect | Postings per bundle | Bundles with fewer than 2 |
|---|---|---|---|---|---|
| 20 | 14.6% | 14.3% | -0.26 | 1.01 | 73.3% |
| 40 | 8.8% | 8.6% | -0.14 | 1.97 | 41.5% |
| 60 | 6.0% | 6.0% | +0.02 | 2.93 | 21.0% |

Bundling changes no vantage's accuracy by more than half a point; the decoy target changes the observer's accuracy by more than 8 points between 20 and 60 decoys.

## Match board pushes

Device named, bundling on, with match boards pushing new matches to every content server every 10 seconds (contribution over the passive observer, in points):

| Vantage | R = 1, 40 decoys (random 2.1%) | R = 15, 40 decoys (random 1.6%) | Push effect, R = 1, 40 decoys |
|---|---|---|---|
| Baseline | 8.7% (+0.0) | 6.9% (+0.0) | +0.04 |
| First hop, credential | 8.7% (+0.0) | 6.9% (-0.0) | +0.07 |
| First hop, content | 8.7% (+0.0) | 6.9% (-0.0) | +0.07 |
| Credential processor | 8.6% (-0.0) | 6.9% (-0.0) | -0.04 |
| Content server | 9.5% (+0.8) | 7.7% (+0.8) | +0.09 |
| Validator | 9.9% (+1.2) | 8.0% (+1.1) | +0.04 |
| Gatekeeper | 8.6% (-0.0) | 6.9% (-0.0) | +0.10 |

Board pushes move no vantage's accuracy by more than 0.11 points in any cell.

## Two-point gatekeeper hold and registry-level bundling

Device named at R = 1 with 40 decoys, each build adding one mechanism to the row above (bundling and board pushes on throughout):

| Build | Passive observer | Random pick | Observer as a multiple of random [95% CI] | Validator's edge over the observer | Capture to finalization, mean |
|---|---|---|---|---|---|
| Board pushes | 8.65% | 2.08% | ×4.16 [3.98, 4.34] | +1.19 points | 625.5 s |
| + two-point gatekeeper hold | 7.89% | 1.96% | ×4.03 [3.85, 4.21] | +1.44 points | 638.9 s |
| + registry-level bundling (120 s) | 7.86% | 1.94% | ×4.05 [3.86, 4.23] | +0.75 points | 698.2 s |

The two-point hold lowers the observer by 0.76 points on the same records, mostly by leaving more devices feasible for each record; as a multiple of the random rate, the observer is unchanged within its interval. Registry bundling leaves the observer unchanged and halves the validator's edge, at a cost of about 60 seconds of latency.

## Registry bundling window

R = 1 with 40 decoys, bundling and board pushes on, relay-lottery gatekeeper hold:

| Registry window | Mean capture to finalization | Observer named the device | Observer as a multiple of random [95% CI] | Validator's edge over the observer | Content server's edge over the observer |
|---|---|---|---|---|---|
| none | 625.5 s | 8.65% | ×4.16 [3.98, 4.34] | +1.19 points | +0.83 points |
| 60 s | 656.0 s | 8.63% | ×4.22 [4.04, 4.41] | +1.15 points | +0.89 points |
| 120 s | 684.0 s | 8.52% | ×4.14 [3.97, 4.32] | +1.09 points | +0.93 points |
| 240 s | 744.8 s | 8.03% | ×4.21 [4.02, 4.41] | +0.88 points | +1.06 points |
| 480 s | 861.2 s | 7.19% | ×4.04 [3.82, 4.26] | +0.35 points | +1.41 points |

A longer registry window moves the validator's edge over the observer to the content server. Measured by the strongest single component's own accuracy and its multiple of random, the windows rank differently:

| Registry window | Strongest component | Its accuracy | Its multiple of random [95% CI] |
|---|---|---|---|
| none | validator | 9.85% | ×3.92 [3.77, 4.06] |
| 120 s | validator | 9.61% | ×4.06 [3.90, 4.23] |
| 240 s | content server | 9.09% | ×3.84 [3.71, 3.97] |
| 480 s | content server | 8.60% | ×3.72 [3.58, 3.85] |

The content server's own content arrival gives it 8.16% at this cell whatever the window, a floor no registry-side mechanism can lower.

## Decoy target

Strongest single component, R = 1, device named (multiple of its own random rate):

| Decoys in flight | 120 s registry window | 480 s registry window |
|---|---|---|
| 20 | 15.98% (×3.34) | 14.67% (×3.23) |
| 30 | 12.22% (×3.91) | 10.89% (×3.56) |
| 40 | 9.61% (×4.06) | 8.60% (×3.72) |
| 60 | 6.90% (×4.33) | 6.13% (×3.93) |
| 100 | 4.56% (×4.74) | 4.02% (×4.27) |
| 150 | 3.30% (×5.13) | 2.94% (×4.66) |

Mean capture to finalization at 40 decoys: 684 s (120 s window) and 861 s (480 s window). A higher decoy target lowers every component's absolute accuracy while its multiple over random rises; the 480-second window is lower than the 120-second window on both measures in every cell tested.

## Longer device and relay holds

R = 1, 40 decoys, 120-second registry window. Strongest single component, device named, and its multiple of random [95% CI]:

| Holds stretched | Strongest component | Device named | Multiple of random | Its lead over the observer | Mean capture to finalization |
|---|---|---|---|---|---|
| none | validator | 9.61% | ×4.06 [3.90, 4.23] | +1.09 points | 684 s |
| every path ×2 | validator | 7.61% | ×4.51 [4.30, 4.71] | +1.63 points | 1,142 s |
| every path ×3 | validator | 6.32% | ×4.30 [4.07, 4.53] | +1.16 points | 1,595 s |
| content paths ×2 | first hop, credential | 6.82% | ×3.85 [3.64, 4.03] | +0.01 points | 1,014 s |
| content paths ×3 | none (observer) | 5.56% | ×3.62 [3.39, 3.87] | +0.00 points | 1,425 s |

Stretching the content-path holds alone hands the record time to timing no credential-side component sees: no compromised component beats a passive observer, and the multiple over random falls outside its interval at every volume tested.

## Content paths stretched, credential path shortened

R = 1, 40 decoys, 120-second registry window:

| Holds | Strongest component | Device named | Multiple of random [95% CI] | Its lead over the observer | Best top-1% precision | Mean latency |
|---|---|---|---|---|---|---|
| unchanged | validator | 9.61% | ×4.06 [3.90, 4.24] | +1.09 points | 18.5% | 684 s |
| content ×2 | first hop, credential | 6.82% | ×3.85 [3.64, 4.03] | +0.01 points | 15.1% | 1,014 s |
| content ×2, credential ×0.5 | first hop, credential | 6.64% | ×3.78 [3.59, 3.97] | +0.01 points | 13.3% | 997 s |
| content ×2, credential ×0.25 | first hop, credential | 6.44% | ×3.68 [3.47, 3.87] | +0.02 points | 12.3% | 995 s |

Shortening the credential path while the content paths are stretched keeps every component level with a passive observer, lowers accuracy slightly further, and costs no latency.

## Content-side holds at role-aware stages, and the post-match lottery

R = 1, 40 decoys, 120-second registry window:

| Configuration | Strongest component | Device named | Multiple of random [95% CI] | Validator's lead | Content server's lead | Mean latency |
|---|---|---|---|---|---|---|
| current | validator | 9.61% | ×4.06 [3.90, 4.23] | +1.09 | +0.93 | 684 s |
| device content hold and content-server hold ×2 | content server | 7.69% | ×3.56 [3.43, 3.71] | -0.09 | +0.37 | 898 s |
| device content hold and content-server hold ×3 | content server | 6.51% | ×3.42 [3.27, 3.57] | -0.76 | +0.21 | 1,169 s |
| post-match lottery | content server | 9.19% | ×3.89 [3.77, 4.02] | +0.52 | +0.94 | 825 s |

Stretching the content-side holds where the specification allows it (the device's content channels and the content servers' own hold) removes the validator's lead and lowers the strongest component's multiple of random outside the current interval at every volume tested. The post-match lottery separates F's and I's submissions (3% within 5 seconds, against 53%) but leaves the content server as the strongest component.

## Relay-hop variability and a static content-server hold, against role-aware scaling

R = 1, 40 decoys, 120-second registry window:

| Configuration | Validator's lead | Content server's lead | Strongest component | Multiple of random [95% CI] | Mean latency |
|---|---|---|---|---|---|
| current | +1.09 | +0.93 | validator 9.61% | ×4.06 [3.90, 4.24] | 684 s |
| role-aware ×2 | -0.09 | +0.37 | content server 7.69% | ×3.56 [3.43, 3.71] | 897 s |
| role-aware ×3 | -0.76 | +0.21 | content server 6.51% | ×3.42 [3.27, 3.57] | 1,169 s |
| relay ×1.5, static hold | -2.08 | +0.06 | content server 8.16% | ×3.74 [3.60, 3.87] | 1,349 s |
| relay ×2, static hold | -1.53 | -0.05 | gatekeeper 6.98% | ×3.71 [3.54, 3.88] | 1,625 s |
| relay ×2, static hold, residual lottery | -1.53 | -0.10 | observer 6.99% | ×3.71 [3.52, 3.90] | 1,629 s |
| relay mixture, static hold | -2.70 | +1.67 | content server 10.37% | ×6.56 [6.37, 6.75] | 1,499 s |

The static hold leaves no component ahead of a passive observer, but partly by making the observer more accurate, and at 1.5 to 2.4 times the current latency; role-aware scaling reaches a lower strongest-component accuracy and multiple of random at less latency. The fixed-mean relay mixture raises every multiple.

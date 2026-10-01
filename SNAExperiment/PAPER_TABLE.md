# Paper table

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

# Results

The run has two cells: R = 1 and R = 150 real transactions in flight. Each cell has 100 decoys in flight and 100 runs. Every node is compromised in turn. Intervals are 95% and resample whole runs. The tables are in `results/`.

Device-named accuracy is how often a vantage names the device behind a registry record. It is the correlation rate.

## Correlation rates

| Vantage | R = 1 | R = 150 |
|---|---|---|
| Passive observer | 4.77% [4.28%, 5.29%] | 2.02% [1.86%, 2.18%] |
| First hop, credential | 4.77% [4.27%, 5.25%] | 2.04% [1.88%, 2.19%] |
| First hop, content | 4.77% [4.27%, 5.27%] | 2.04% [1.88%, 2.20%] |
| Credential processor | 4.78% [4.28%, 5.29%] | 2.03% [1.87%, 2.19%] |
| Validator | 5.26% [4.85%, 5.66%] | 2.32% [2.17%, 2.48%] |
| Gatekeeper | 4.79% [4.31%, 5.29%] | 2.04% [1.87%, 2.20%] |
| Content server | 5.53% [5.12%, 5.93%] | 2.39% [2.26%, 2.53%] |
| Combined | 4.85% [4.41%, 5.30%] | 2.07% [1.92%, 2.23%] |

Chance among the feasible devices is 1.11% at R = 1 and 0.44% at R = 150. Every vantage passes the claim criterion in both cells.

## Lead over the observer

The lead is a vantage's rate minus the observer's rate, in points.

| Vantage | R = 1 | R = 150 |
|---|---|---|
| Credential processor | +0.01 [-0.01, +0.03] | +0.01 [-0.00, +0.01] |
| Validator | +0.49 [-0.01, +0.94] | +0.29 [+0.11, +0.47] |
| Gatekeeper | +0.03 [-0.07, +0.10] | +0.02 [-0.01, +0.04] |
| Content server | +0.76 [+0.49, +1.01] | +0.37 [+0.24, +0.49] |
| Combined | +0.08 [+0.03, +0.13] | +0.05 [+0.03, +0.07] |

The content server leads the observer in both cells. The validator leads at R = 150. The credential processor and the gatekeeper match the observer.

## Rate against volume

The product of the rate in percent and (100 + R) is the rate scaled by everything in flight.

| Vantage | R = 1 | R = 150 |
|---|---|---|
| Passive observer | 482 | 505 |
| Content server | 559 | 598 |

The product rises with R. The rate falls more slowly than 1 / (100 + R).

## Windows and records

| Configuration | Longest capture to finalization | Warm-up and cool-down | Scored window |
|---|---|---|---|
| Main run | 2,316.8 s | 2,616.8 s | 3,600.0 s |
| Every hold off | 37.6 s | 42.4 s | 58.4 s |
| Credential path sets the record time | 2,406.0 s | 2,717.5 s | 3,738.7 s |
| Content paths set the record time | 22,673.7 s | 25,609.8 s | 35,232.7 s |
| F content path sets the record time | 22,673.7 s | 25,609.8 s | 35,232.7 s |

The scored window at R = 1 is extended until it holds 200 real transactions per run on average. No transaction exceeded its warm-up.

| Cell | Real records scored | Half-width of the observer's interval |
|---|---|---|
| R = 1 | 19,943 | 0.50 points |
| R = 150 | 46,087 | 0.16 points |

## Decoy identities

Each decoy identity captures at the real device's rate. At R = 1 the real device captures 3.08 times per hour and each of the 100 decoy identities captures 3.08 times per hour. At R = 150 the rates are 3.00 and 2.99 per hour.

## Predicted against measured

`PREDICTIONS.md` states each prediction, its basis and its failure rule. A correlation-rate prediction fails only when the rate is above its bound.

| Prediction | Predicted | Measured | Result |
|---|---|---|---|
| 1. D and capture to finalization | D within 1% of 1,170.4 s; mean capture to finalization 1,140 s to 1,190 s | D = 1,168.2 s; 1,159.1 s and 1,166.2 s | Holds |
| 2. Counts in flight | Real within 3% of R, decoys within 3% of 100, in every cell of every configuration | Largest gap: every hold off at R = 150, with 147.97 real (-1.4%) and 98.11 decoys (-1.9%) | Holds |
| 3. Match board share | 47% to 53%; each control's intended path at least 95% | 49.8% and 50.0%; controls 95.9% to 98.1% | Holds |
| 4. Departure to arrival | Mean 355.6 s to 364.7 s; standard deviation 258 s to 270 s | Means 357.5 s to 360.7 s; standard deviations 262.0 s to 264.5 s | Holds |
| 5. Shuffle test | Mismatches under 0.1%, no feasible-count change, means within 3% of exact, coverage 90% to 97% | 1 mismatch in 19,943 records, a tie; no feasible-count change; means within 1.3% of exact; coverage 94.0% and 96.0% | Holds |
| 6. Window halves | The observer's two halves agree in every cell | -0.51 [-1.51, +0.52] and -0.12 [-0.41, +0.17] | Holds |
| 7. Observer, R = 1 | At most 4.8% | 4.77% | Holds |
| 7. Content server, R = 1 | At most 5.7% | 5.53% | Holds |
| 7. Observer, R = 150 | At most 1.9% | 2.02% | Fails |
| 7. Content server, R = 150 | At most 2.3% | 2.39% | Fails |
| 8. Cost | Run phase 2.1 to 4.2 hours on 8 workers | 135.7 minutes (2.3 hours) on 8 workers; 140.9 minutes in all | Holds |

Prediction 7 fails at R = 150 for both vantages. The observer is 0.12 points above its bound, and the content server is 0.09 points above it. Both bounds lie inside the measured intervals: [1.86%, 2.18%] for the observer and [2.26%, 2.53%] for the content server.

## Diagnostics

| Cell | Observer, timing evidence off | Multiple of chance | Observer, record time at the midpoint | Content server, record time at the midpoint |
|---|---|---|---|---|
| R = 1 | 3.30% [2.83%, 3.78%] | ×2.96 | +0.45 [+0.20, +0.69] | +0.36 [+0.15, +0.57] |
| R = 150 | 1.56% [1.42%, 1.70%] | ×3.53 | +0.20 [+0.09, +0.30] | +0.16 [+0.06, +0.27] |

The observer stays above chance with its timing evidence off. A record time at the midpoint, which the protocol does not publish, raises both rates.

The credential path control leaves 456 real transactions at R = 1 and 1,108 at R = 150 unfinalized at their quorum timeout. Every other configuration finalizes every transaction.

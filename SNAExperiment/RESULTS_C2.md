# Results

The run has three cells: R = 1, 100 and 300 real transactions in flight. Each cell has 100 decoys in flight and 100 runs. Every node is compromised in turn. Intervals are 95% and resample whole runs. The tables are in `results/C2/`.

Device-named accuracy is how often a vantage names the device behind a registry record. It is the correlation rate.

## Correlation rates

| Vantage | R = 1 | R = 100 | R = 300 |
|---|---|---|---|
| Passive observer | 4.77% [4.28%, 5.29%] | 2.33% [2.12%, 2.55%] | 1.39% [1.31%, 1.46%] |
| First hop, credential | 4.77% [4.27%, 5.25%] | 2.31% [2.10%, 2.52%] | 1.39% [1.31%, 1.46%] |
| First hop, content | 4.77% [4.27%, 5.27%] | 2.31% [2.10%, 2.51%] | 1.39% [1.32%, 1.46%] |
| Credential processor | 4.78% [4.28%, 5.29%] | 2.32% [2.11%, 2.54%] | 1.38% [1.31%, 1.46%] |
| Validator | 5.26% [4.85%, 5.66%] | 2.66% [2.46%, 2.85%] | 1.52% [1.44%, 1.61%] |
| Gatekeeper | 4.79% [4.31%, 5.29%] | 2.31% [2.11%, 2.52%] | 1.38% [1.31%, 1.45%] |
| Content server | 5.53% [5.12%, 5.93%] | 2.78% [2.58%, 2.98%] | 1.64% [1.57%, 1.71%] |
| Combined | 4.85% [4.41%, 5.30%] | 2.35% [2.14%, 2.54%] | 1.41% [1.34%, 1.48%] |

Chance among the feasible devices is 1.11% at R = 1, 0.55% at R = 100 and 0.28% at R = 300. Every vantage passes the claim criterion in every cell.

## Lead over the observer

The lead is a vantage's rate minus the observer's rate, in points.

| Vantage | R = 1 | R = 100 | R = 300 |
|---|---|---|---|
| Credential processor | +0.01 [-0.01, +0.03] | -0.01 [-0.02, +0.01] | -0.00 [-0.01, +0.00] |
| Validator | +0.49 [-0.01, +0.94] | +0.33 [+0.09, +0.55] | +0.13 [+0.04, +0.22] |
| Gatekeeper | +0.03 [-0.07, +0.10] | -0.02 [-0.06, +0.02] | -0.01 [-0.03, +0.01] |
| Content server | +0.76 [+0.49, +1.01] | +0.45 [+0.30, +0.60] | +0.25 [+0.20, +0.31] |
| Combined | +0.08 [+0.03, +0.13] | +0.03 [-0.00, +0.05] | +0.02 [+0.01, +0.04] |

The content server leads the observer in every cell. The validator leads at R = 100 and 300. The credential processor and the gatekeeper match the observer.

## Rate against volume

The product of the rate in percent and (100 + R) is the rate scaled by everything in flight.

| Vantage | R = 1 | R = 100 | R = 300 |
|---|---|---|---|
| Passive observer | 482 [432, 534] | 466 [424, 509] | 555 [525, 585] |
| Content server | 558 [517, 599] | 556 [516, 597] | 656 [628, 684] |

The product falls from R = 1 to R = 100 and rises from R = 100 to R = 300. The law tested in prediction 7 (481.6 + 0.156 R for the observer, 558.3 + 0.262 R for the content server) gives 497.2 and 528.4 for the observer and 584.5 and 636.9 for the content server at R = 100 and 300. Each lies inside its measured interval.

Two other statements of the law were not predictions. They are set against the measured rates here for comparison only.

| Law | Observer, R = 100 | Observer, R = 300 | Content server, R = 100 | Content server, R = 300 |
|---|---|---|---|---|
| A. Constants 485 and 574 | 2.43% | 1.21% | 2.87% | 1.44% |
| B. Constants 505 and 598 | 2.53% | 1.26% | 2.99% | 1.50% |
| Measured | 2.33% | 1.39% | 2.78% | 1.64% |

At R = 100 both measured rates are below both bounds. At R = 300 both are above both bounds.

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
| R = 100 | 30,574 | 0.21 points |
| R = 300 | 92,714 | 0.07 points |

## Decoy identities

Each decoy identity captures at the real device's rate. At R = 1 the real device and each of the 100 decoy identities capture 3.08 times per hour. At R = 100 both rates are 2.99 per hour. At R = 300 they are 3.00 and 2.99 per hour.

## Packet type revealed

The observer is scored again as if told each packet's true type, with one record-time density per type, on the same records as the pooled observer. It covers the first hop only.

| Configuration | Cell | Pooled observer | Told the type | Lead [95% CI] | Ratio |
|---|---|---|---|---|---|
| Main run | R = 1 | 4.77% | 4.77% | +0.00 [-0.12, +0.11] | 1.00 |
| Main run | R = 100 | 2.33% | 2.26% | -0.07 [-0.14, +0.01] | 0.97 |
| Main run | R = 300 | 1.39% | 1.40% | +0.02 [-0.01, +0.05] | 1.01 |
| Every hold off | R = 1 | 1.49% | 1.49% | -0.01 [-0.02, +0.00] | 1.00 |
| Every hold off | R = 100 | 0.85% | 0.85% | +0.00 [+0.00, +0.00] | 1.00 |
| Every hold off | R = 300 | 0.46% | 0.46% | +0.00 [+0.00, +0.00] | 1.00 |
| Credential path sets the record time | R = 1 | 4.66% | 4.69% | +0.04 [-0.09, +0.17] | 1.01 |
| Credential path sets the record time | R = 100 | 2.26% | 2.25% | -0.00 [-0.07, +0.07] | 1.00 |
| Credential path sets the record time | R = 300 | 1.34% | 1.31% | -0.03 [-0.07, +0.00] | 0.98 |
| Content paths set the record time | R = 1 | 10.92% | 14.94% | +4.02 [+3.58, +4.47] | 1.37 |
| Content paths set the record time | R = 100 | 11.79% | 14.38% | +2.60 [+2.26, +2.94] | 1.22 |
| Content paths set the record time | R = 300 | 6.78% | 8.06% | +1.28 [+1.11, +1.45] | 1.19 |
| F content path sets the record time | R = 1 | 5.38% | 16.35% | +10.97 [+10.38, +11.53] | 3.04 |
| F content path sets the record time | R = 100 | 7.52% | 13.87% | +6.36 [+6.01, +6.70] | 1.85 |
| F content path sets the record time | R = 300 | 4.05% | 7.99% | +3.94 [+3.79, +4.08] | 1.97 |

In the main configuration, telling the observer each packet's type changes its rate by -0.07 to +0.02 points, and every one of those intervals contains zero. When the content paths or the F content path alone set the record time, the observer told the type names the device 1.19 to 3.04 times as often as the pooled observer.

The typed observer passes the claim criterion in every cell of every configuration. Its chance rates and multiples are in `results/C2/TABLES.md`.

In the every-hold-off control, the typed observer's hits split by packet type carry no information. A capture's three packets leave within 2.5 ms of each other and share one delay distribution, so the three typed densities differ only by sampling noise. Its correct picks fall where the delay distribution peaks, and there one type's density is highest by that noise. Its I content hits are 0.02%, 0.00% and 0.00% for that reason. The device it names does not depend on which of the capture's packets it picks.

## Predicted against measured

`PREDICTIONS_C2.md` states each prediction, its basis and its failure rule.

| Prediction | Predicted | Measured | Result |
|---|---|---|---|
| 1. D and capture to finalization | D = 1,168.2 s within 0.1 s; mean capture to finalization 1,140 s to 1,190 s | D = 1,168.2 s; 1,159.1 s, 1,162.6 s and 1,162.7 s | Holds |
| 2. Counts in flight | Real within 3% of R, decoys within 3% of 100, in every cell of every configuration | Largest gaps: real -1.7% (every hold off, R = 1); decoys -1.5% (every hold off, R = 300) | Holds |
| 3. Match board share | 47% to 53%; each control's intended path at least 95% | 49.8%, 50.1% and 50.0%; controls 95.96% to 98.11% | Holds |
| 4. Departure to arrival | Mean 355.6 s to 364.7 s; standard deviation 258 s to 270 s | Means 357.5 s to 361.7 s; standard deviations 262.0 s to 264.6 s | Holds |
| 5. Shuffle test | Mismatches under 0.1%, no feasible-count change, means within 3% of exact, coverage 90% to 99% | 1, 0 and 0 mismatches; no feasible-count change; means within 0.9% of exact; coverage 94.0%, 95.0% and 93.0% | Holds |
| 6. Window halves | The observer's two halves agree in every cell | -0.51 [-1.51, +0.52], +0.38 [-0.01, +0.77] and +0.01 [-0.14, +0.16] | Holds |
| 7. Observer product, R = 100 | 497.2 inside the interval | 466 [424, 509] | Holds |
| 7. Observer product, R = 300 | 528.4 inside the interval | 555 [525, 585] | Holds |
| 7. Content-server product, R = 100 | 584.5 inside the interval | 556 [516, 597] | Holds |
| 7. Content-server product, R = 300 | 636.9 inside the interval | 656 [628, 684] | Holds |
| 8. Cost: run phase, from the first run to the last | 5.3 to 7.2 hours on 8 workers; fails above 8.0 hours | 513.7 minutes (8.56 hours) on 8 workers | Fails |
| 9. R = 1 reproduces the committed R = 1 cell | Same decisions | Holds at figure level: 0 of 29,615 stored R = 1 figures differ. The decision-level check was not run because the C1 raw files do not exist. | Holds at figure level |
| 10. Typed observer, main | Lead within ±1.2, ±0.6 and ±0.3 points | +0.00, -0.07 and +0.02 | Holds |
| 11. Typed observer, credential path | Lead within ±1.2, ±0.6 and ±0.3 points | +0.04, -0.00 and -0.03 | Holds |
| 12. Typed observer, every hold off | Interval on the lead contains zero; lead within ±0.1 points | -0.01 [-0.02, +0.00], +0.00 [+0.00, +0.00] and +0.00 [+0.00, +0.00] | Holds |
| 13. Typed observer, content paths, direction | Lead's interval above zero in every cell | Lower ends +3.58, +2.26 and +1.11 | Holds |
| 13. Typed observer, content paths, size | Ratio 1.00 to 1.60 at R = 1; 1.05 to 1.40 at R = 100 and 300 | 1.37, 1.22 and 1.19 | Holds |
| 14. Typed observer, F content path, direction | Lead's interval above zero in every cell | Lower ends +10.38, +6.01 and +3.79 | Holds |
| 14. Typed observer, F content path, size | Ratio 1.20 to 2.50 at R = 1; 1.40 to 2.10 at R = 100 and 300 | 3.04, 1.85 and 1.97 | Fails at R = 1 |

Prediction 8 is judged on the run phase, as the prediction states: 513.7 minutes (8.56 hours) from the first run to the last, 0.56 hours over the limit. The whole command took 521.0 minutes (8.68 hours). The other 7.3 minutes are the windows, the calibration and the models before the runs, and the tables and figures after them. The prediction fails on either number.

Prediction 14's size range fails at R = 1. The ratio is 3.04 against an upper end of 2.50. Its direction holds in every cell.

Prediction 12's interval at R = 1 ends at exactly zero, so it contains zero.

Prediction 9 holds at figure level, across two platforms. C2 ran on Windows 11 with Python 3.13.3, numpy 2.4.4 and scipy 1.18.1. C1 did not record its versions.

## Diagnostics

| Cell | Observer, timing evidence off | Multiple of chance | Observer, record time at the midpoint | Content server, record time at the midpoint |
|---|---|---|---|---|
| R = 1 | 3.30% [2.83%, 3.78%] | ×2.96 | +0.45 [+0.20, +0.69] | +0.36 [+0.15, +0.57] |
| R = 100 | 1.43% [1.26%, 1.62%] | ×2.60 | +0.22 [+0.09, +0.35] | +0.28 [+0.16, +0.39] |
| R = 300 | 0.93% [0.87%, 1.00%] | ×3.38 | +0.14 [+0.08, +0.20] | +0.14 [+0.08, +0.20] |

The observer stays above chance with its timing evidence off. A record time at the midpoint, which the protocol does not publish, raises both rates.

The credential path control leaves 456 real transactions at R = 1, 784 at R = 100 and 2,225 at R = 300 unfinalized at their quorum timeout. Every other configuration finalizes every transaction.

In the controls, some combined-view classes that hold a destination fail the claim criterion, as they do in C1 at R = 1. No row of the main configuration fails it.

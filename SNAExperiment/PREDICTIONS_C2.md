# Predictions for the run with cells R = 1, 100 and 300

Written before the run. A prediction counts as made before the run once this file is committed. Each item states the prediction, its basis, what counts as a failure, and whether it can fail.

The run has cells R = 1, 100 and 300 real transactions in flight, 100 decoys in flight in every cell, and 100 runs per cell. It adds one control, the observer told each packet's true type (`observer_typed`).

Two sources of numbers are used:

- **The committed run:** `results/` on `main`, cells R = 1 and 150. Its R = 1 cell is the same traffic as the new R = 1 cell.
- **Prototype numbers:** runs made while building the control, at R = 150, on run ids 5000 to 5004 of the traffic seed. R = 150 is not a cell of this run, so none of these records is scored in it. They used the committed D and windows, full-size models and the run's own code. Each prediction that rests on them says so.

Terms:

- **Pooled observer:** the passive observer of the main tables, whose likelihood is pooled over a capture's three packets.
- **Typed observer:** `observer_typed`.
- **Lead:** typed accuracy minus pooled accuracy on the same records, in points.
- **Ratio:** typed accuracy divided by pooled accuracy on the same records.

## 1. D and capture to finalization

**Prediction.** D is 1,168.2 s, within 0.1 s, under the main configuration. The mean capture-to-posting time of real transactions is between 1,140 s and 1,190 s in every cell of the main configuration.

**Basis.** The calibration runs at R = 150 on fixed seeds, and none of its code or seeds changed. The committed run gave D = 1,168.2274 s. Delays do not depend on volume, because there is no queueing. The committed means are 1,159.1 s at R = 1 and 1,166.2 s at R = 150.

**Fails if** D differs from 1,168.2 s by more than 0.1 s, or any main cell's mean lies outside 1,140 to 1,190 s.

**Can fail.** A changed calibration, a platform that computes it differently, or a delay that depends on volume would show.

## 2. Counts in flight

**Prediction.** In every cell of every configuration, the mean number of real transactions in flight is within 3% of R, and the mean number of decoys in flight is within 3% of 100.

**Basis.** D is the mean time a transaction stays in the system, so by Little's law the rates R / D and 100 / D give R and 100 in flight. In the committed run the largest gaps were 1.4% (real) and 1.9% (decoys), both in the every-hold-off control at R = 150.

**Fails if** any cell of any configuration is more than 3% from either target.

**Can fail.** A volume effect on residence time, or a short window with few transactions, would show. R = 300 is twice the largest committed volume.

## 3. Confirmations set by the match board

**Prediction.** The match board sets between 47% and 53% of F's and I's confirmations in every cell of the main configuration. In every cell of every first-relay control, the intended path sets at least 95%.

**Basis.** The committed run measured 49.8% and 50.0% in the main cells, and 95.9% to 98.1% in the controls. The credential-path control is the closest to its bound, at 95.9% and 96.0%.

**Fails if** any main cell is outside 47% to 53%, or any control cell is below 95%.

**Can fail.** The credential-path control sits about one point above its bound.

## 4. Departure to arrival at C, F or I

**Prediction.** For credential packets (at C) and for F and I content packets (at F or I), in every cell of the main configuration, the delay from the packet's departure to its arrival has a mean between 355.6 s and 364.7 s and a standard deviation between 258 s and 270 s.

**Basis.** The two relay holds have means of 60 s and 300 s. Their sum has a mean of 360.0 s and a standard deviation of 263.7 s before network time, which adds about 0.16 s. The committed run measured means of 357.5 s to 360.7 s and standard deviations of 262.0 s to 264.5 s.

**Fails if** any packet type in any main cell has a mean outside 355.6 to 364.7 s or a standard deviation outside 258 to 270 s.

**Can fail.** A relay hold that depended on the path or the volume would show.

## 5. The shuffle test

**Prediction.** In every main cell:

- Every shuffled pick is the permuted unshuffled pick, apart from tied scores, in more than 99.9% of records.
- Feasible counts never change.
- Over 200 permutations per run, the mean shuffled accuracy and the mean chance rate each lie within 3% of their exact expectation.
- The estimator's 95% interval covers the exact expectation in 90% to 99% of permutation draws.

**Basis.** Permuting the labels renames the groups the posterior is summed over and changes no score. The committed run had 1 and 0 mismatches, no feasible-count change, means within 1.3% of exact, and coverage of 94.0% and 96.0%.

**Fails if** mismatches reach 0.1% of records in a cell, any feasible count changes, a mean over permutations is more than 3% from exact, or coverage lies outside 90% to 99% in a cell.

**Can fail.** Coverage is a count over 200 draws. At a true 95%, a cell lies above 99% with probability 0.04% by chance, and below 90% with probability 0.12%. With three cells, the chance that at least one cell fails this way is 0.47%. A failure would show an estimator whose interval does not hold its stated level.

**Why the upper limit is 99%.** The earlier limit of 97% failed by chance in at least one of three cells 18% of the time at a true 95%. The change rests on those computed odds, not on any result. Coverage above 95% means a conservative interval, not a defect.

## 6. Window halves

**Prediction.** The observer's accuracy in the first and the second half of the window agrees in every cell: the 95% interval on the difference contains zero.

**Basis.** Traffic in flight is steady through the window. The committed run agreed in both cells: -0.51 [-1.51, +0.52] at R = 1 and -0.12 [-0.41, +0.17] at R = 150.

**Fails if** any cell's interval excludes zero.

**Can fail.** With three cells and no real difference, the chance that at least one interval excludes zero is about 14%.

## 7. The correlation-rate law

**What was predicted and what happened.** The committed run tested this law: accuracy in percent, times (100 + R), is at most 485 for the observer and 574 for the content server. At R = 1 it held: 4.77% × 101 = 482, and 5.53% × 101 = 559. At R = 150 it missed: 2.02% × 250 = 505 against 485 for the observer, and 2.39% × 250 = 598 against 574 for the content server. The product rose with R.

**Prediction.** The product rises linearly with R. At R = 100 and 300:

| Vantage | Law | R = 100 | R = 300 |
|---|---|---|---|
| Passive observer | 481.6 + 0.156 R | 497.2 | 528.4 |
| Content server | 558.3 + 0.262 R | 584.5 | 636.9 |

R = 1 is covered by prediction 9.

**Basis.**

- The line passes through the committed run's two point products: (1, 482) and (150, 505) for the observer, and (1, 559) and (150, 598) for the content server.
- An earlier run with 100 decoys was weighed in choosing this law. It is in the history of PR #27 and used an earlier version of the code, at R = 1, 100 and 500.
  - Its observer products were 493, 520 and 558. Its content-server products were 569, 624 and 678.
  - At R = 500 they lie within 0.3% (observer) and 1.6% (content server) of this line.
  - At R = 100 they lie 4.6% (observer) and 6.8% (content server) above it.

**Fails if** the 95% interval on a vantage's measured product in a cell excludes the law's value. The measured product is the accuracy in percent, and its interval, times (100 + R). That is four tests: two vantages at R = 100 and 300. With the law exactly right, each excludes its value 5% of the time, so the chance that at least one of the four fails is 18.5%.

**Can fail.** A product that rises faster or slower than the line, by more than the interval allows, would show. The earlier run's R = 100 products sit above the line.

**Two other statements of the law are not predictions.** The results show their bounds beside the measured rates, as a comparison only.

- **Law A**, the old constants (485 and 574), already failed at R = 150.
- **Law B**, constants refit to the committed run's largest products (505 and 598), is a ceiling fitted to the committed points.

| Law | Observer, R = 100 | Observer, R = 300 | Content server, R = 100 | Content server, R = 300 |
|---|---|---|---|---|
| A. 485 and 574 | 2.43% | 1.21% | 2.87% | 1.44% |
| B. 505 and 598 | 2.53% | 1.26% | 2.99% | 1.50% |

## 8. Cost

**Prediction.** The run phase, from the first run to the last, takes between 5.3 and 7.2 hours on the default 8 workers of the machine that ran the committed run.

**Basis.** The committed run's measured cost per run on that machine, in seconds of simulation plus scoring plus the shuffle test:

| Configuration | R = 1 | R = 150 |
|---|---|---|
| Main | 25.5 | 87.3 |
| Every hold off | 19.5 | 25.5 |
| Credential path | 25.4 | 98.8 |
| Content paths | 23.8 | 92.5 |
| F content path | 34.1 | 214.5 |
| All five | 128.3 | 518.6 |

- **Scaling.** The R = 1 cell keeps its committed cost. Scoring grows with the records scored (proportional to R at a fixed window) and between not at all and in proportion to the candidates per record (proportional to 100 + R).
  - **Low end:** cost proportional to R alone. That gives R = 100 at 0.67 times the R = 150 cost and R = 300 at 2 times.
  - **High end:** cost proportional to R × (100 + R). That gives 0.53 times and 3.2 times.
  - Per run of every cell, that is 1,511 s to 2,064 s of worker time, and 100 runs make 42 to 57 worker-hours.
- **Throughput.** The committed run did 64,700 worker-seconds in 135.7 minutes on 8 workers, which is 7.95 workers' worth. At that throughput, the run phase takes 5.3 to 7.2 hours.
- The typed control adds one density pass to the observer's pass, which is small next to the 20 node passes, and is ignored here.

**Fails if** the run phase takes more than 8.0 hours on the default 8 workers.

**Can fail.** A cost that grows faster than R × (100 + R), memory pressure at R = 300, or a slower machine would show.

## 9. The R = 1 cell reproduces the committed R = 1 cell

**Prediction.** Same decisions. Every device-level decision of every vantage, in every configuration, at R = 1 is the same as in the committed run. The platform and package versions are recorded on both sides.

**Basis.**

- The R = 1 traffic, the per-run scoring seeds, the model seeds, D and the windows are all unchanged.
- The typed control draws nothing from the run's random generator. Its diagnostic uses its own generator in the report.
- On one platform, the committed code and the new code gave 0 differing decisions out of 28,628, on R = 1 runs 0 and 1 of the main configuration (Python 3.11.17, numpy 2.4.6, scipy 1.17.1, Linux x86-64).
- The committed run did not record its versions. They are recorded from this run on.

**Fails if** 1 or more device-level decisions differ. Where the committed raw files are not available, the check falls back to the committed figures: it fails if any R = 1 figure in `summary.json` or `controls/*.json` differs, intervals included.

**Can fail.** A changed package version, a platform difference in floating point, or a code change that touched the existing scoring would show.

## 10. Typed observer, main configuration

**Prediction.** Telling the observer the packet type changes its accuracy by little, in either direction. In every main cell, the lead lies within ±1.2 points at R = 1, ±0.6 points at R = 100 and ±0.3 points at R = 300. That is about a quarter of the pooled accuracy expected in each cell. No direction is predicted.

**Basis.**

- **Prototype numbers, R = 150, 5 runs, 2,270 records.**
  - Pooled 2.33%, typed 2.20%, lead -0.13 points.
  - The two observers disagreed on 9 decisions: typed only right on 3, pooled only right on 6. The net of -3 has a standard error of about 3 decisions, so the ratio is 0.94 with a 95% range of about 0.83 to 1.05.
- **Structure.** In the main configuration, F and I content have the same delay to the record (908 s and 909 s mean in the models' samples). Credential differs by about 118 s, against standard deviations of about 310 s. So the control mostly separates credential from content, and the types carry little extra timing.
- **Why no direction.** The device score sums per-packet likelihoods. A sharper typed density can also raise a decoy's score, so no gain is guaranteed.
- **R = 1 and R = 300 rest on extrapolation.** The pooled accuracies used for the bounds are 4.77% at R = 1 (committed) and about 2.5% and 1.3% at R = 100 and 300 (prediction 7). The prototype covers R = 150 only.

**Fails if** the lead's point estimate is outside its bound in any main cell.

**Can fail.** The bound is a quarter of the pooled accuracy, which is a typed-to-pooled ratio outside 0.75 to 1.25. The content-paths control's prototype ratio of 1.18 would not fail it. Only a ratio like the F content control's 1.73 would.

## 11. Typed observer, credential path sets the record time

**Prediction.** As in prediction 10. The lead lies within ±1.2 points at R = 1, ±0.6 at R = 100 and ±0.3 at R = 300. No direction is predicted.

**Basis.**

- **Prototype numbers, R = 150, 5 runs, 2,287 records.**
  - Pooled 1.88%, typed 2.10%, lead +0.22 points.
  - The observers disagreed on 5 decisions, all typed only right. The ratio is 1.12, with a 95% range of about 1.01 to 1.22.
- **Structure.** The content packets leave at capture and the credential packet after its 150 s device hold. Both follow the credential path's timing, offset by that hold. The models' samples give 1,006 s (sd 312 s) for credential and 1,151 s (sd 329 s) for content.
- **Held-out density fit.** At 100,000 model samples, each type's density fits held-out true packets better than the pooled one: by 0.047 nats per packet for credential and 0.013 for content. That is a small gap.
- The committed pooled accuracy was 4.66% at R = 1 and 2.18% at R = 150.

**Fails if** the lead's point estimate is outside its bound in any cell of this control.

**Can fail.** The bound is a quarter of the pooled accuracy, which is a typed-to-pooled ratio outside 0.75 to 1.25. The content-paths control's prototype ratio of 1.18 would not fail it. Only a ratio like the F content control's 1.73 would.

## 12. Typed observer, every hold off

**Prediction.** The typed and the pooled observer agree within noise. In every cell, the 95% interval on the lead contains zero, and the lead lies within ±0.1 points.

**Basis.**

- With every hold off, the device holds are zero, so a capture's three packets leave together and share one delay to the record. The three typed densities then differ from the pooled one only by sampling noise.
- **Prototype numbers** (the fast test, R = 20, small models): 0 of 2,398 decisions differed.
- The committed pooled accuracy was 1.49% at R = 1 and 0.73% at R = 150.

**Fails if** any cell's interval on the lead excludes zero, or its point estimate lies outside ±0.1 points.

**Can fail.** Packets that did not leave together, or typed densities biased by their smaller samples, would show. The interval criterion alone fails by chance about 14% of the time across three cells, so the ±0.1-point bound is the main test.

## 13. Typed observer, content paths set the record time

**Prediction.** The typed observer names the device more often than the pooled one in every cell. The ratio lies between 1.05 and 1.40 at R = 100 and 300, and between 1.00 and 1.60 at R = 1.

**Basis.**

- **Prototype numbers, R = 150, 3 runs, 1,452 records.**
  - Pooled 11.71%, typed 13.77%, lead +2.07 points.
  - Per-run leads were +1.45, +2.48 and +2.27.
  - The observers disagreed on 116 decisions: typed only right on 73, pooled only right on 43. The ratio is 1.18, with a 95% range of about 1.05 to 1.30.
- **Structure.** The device holds both content packets for 7,200 s and the credential packet not at all. The record follows the content packets, and the credential packet carries almost no timing. The pooled density gives the tight content shape two thirds of its weight. The typed density gives it all of it on content packets, and gives the credential packet its own wide shape.
- **Confidence across R.**
  - R = 100 and 300 lie near the prototype's R = 150, so the ranges there widen the prototype's interval a little for the change in competition.
  - R = 1 differs more. Its window is extended, its competition is the 100 decoys alone, and the committed pooled accuracy there (10.92%) sits beside a much lower chance rate (1.04% against 3.70% at R = 150). So the ratio there is less certain, and its range is wider.
  - I am moderately sure of the direction in every cell. I am less sure of the size range at R = 1 than at R = 100 and 300.

**Fails if** the lead's 95% interval includes zero or lies below it in any cell (the direction). Separately, the size prediction fails if the ratio's point estimate lies outside its range in any cell.

**Can fail.** A direction failure would show as an interval reaching zero. A size failure would show as a ratio outside its range.

## 14. Typed observer, F content path sets the record time

**Prediction.** The typed observer names the device more often than the pooled one in every cell. The ratio lies between 1.40 and 2.10 at R = 100 and 300, and between 1.20 and 2.50 at R = 1.

**Basis.**

- **Prototype numbers, R = 150, 3 runs, 2,149 records.**
  - Pooled 6.79%, typed 11.73%, lead +4.93 points.
  - Per-run leads were +3.49, +5.30 and +6.00.
  - The observers disagreed on 254 decisions: typed only right on 180, pooled only right on 74. The ratio is 1.73, with a 95% range of about 1.51 to 1.94.
- **Structure.** The device holds only its F packet, for 7,200 s. The record follows the F packet alone. The pooled density gives the F packet's tight shape one third of its weight; the typed density gives it all of it. This is the largest separation of the four controls.
- **Fast test.** At R = 20 with small models, typed beat pooled on 2 runs.
- **Confidence across R.** As in prediction 13: moderately sure of the direction in every cell, less sure of the size range at R = 1. The committed pooled accuracy was 5.38% at R = 1 and 6.19% at R = 150, with chance rates of 1.01% and 2.50%.

**Fails if** the lead's 95% interval includes zero or lies below it in any cell (the direction). Separately, the size prediction fails if the ratio's point estimate lies outside its range in any cell.

**Can fail.** A direction failure would show as an interval reaching zero. A size failure would show as a ratio outside its range.

## Dropped

None. Every prediction above can fail.

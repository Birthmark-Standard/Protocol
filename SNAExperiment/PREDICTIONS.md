# Predictions

Written and committed before the run. Each prediction comes from the model or from a pilot. The pilot ran the run's own code on 30 runs per cell of the main configuration, on run ids 900,000 to 900,029, which the run does not use. It used the run's calibration seeds, so its D is the run's D.

Each item states what counts as a failure. `RESULTS.md` sets every prediction against its measured value.

## 1. Mean capture to finalization

**Prediction.** D = 1,137.7 s. The mean capture-to-posting time of real transactions is between 1,105 s and 1,155 s in every cell of the main configuration.

**Basis.** The calibration is deterministic on its seeds and gives D = 1,137.7 s. The pilot measured 1,123.7 s [1,108.3, 1,138.8] at R = 1, 1,129.6 s [1,116.2, 1,143.1] at R = 20 and 1,141.0 s [1,129.8, 1,151.6] at R = 100. Delays do not depend on volume, because there is no queueing.

**Fails if** D differs from 1,137.7 s, or any cell's mean lies outside 1,105 to 1,155 s.

## 2. Counts in flight

**Prediction.** In every cell of every configuration, the mean number of real transactions in flight is within 3% of R, and the mean number of decoys in flight is within 3% of 60.

**Basis.** D is the mean time a transaction stays in the system, so by Little's law the rates R / D and 60 / D give R and 60 in flight. The pilot measured 1.01, 19.43 and 100.62 real, and 59.51, 59.25 and 59.79 decoys.

**Fails if** any cell of any configuration is more than 3% from either target.

## 3. Confirmations set by the match board

**Prediction.** The match board sets between 47% and 53% of F's and I's confirmations in every cell of the main configuration.

**Basis.** A content server confirms at the later of its own pre-match hold release (content arrival plus a 120 s hold) and the second board push carrying the match. The credential path's holds and the content path's holds put the two at similar times. The pilot measured 49.8%, 49.5% and 50.1%.

**Fails if** any main cell is outside 47% to 53%.

**Controls.** The intended path's share is at least 95% in every cell of every first-relay control. The small simulations that set the controls measured 96.7% for the credential path, 98.4% for the content paths and 97.2% for the F content path. A control fails this prediction if any cell is below 95%.

## 4. Device named: passive observer and content server

**Prediction.** The point estimates lie in these ranges:

| Cell | Passive observer | Content server |
|---|---|---|
| R = 1 | 8.5% to 10.9% | 9.1% to 11.3% |
| R = 20 | 5.2% to 6.9% | 5.4% to 6.9% |
| R = 100 | 3.1% to 3.6% | 3.5% to 3.9% |

**Basis.** The ranges are the pilot's 95% intervals. The pilot measured the observer at 9.68%, 5.99% and 3.35%, and the content server at 10.17%, 6.19% and 3.70%.

**Fails if** any point estimate lies outside its range.

## 5. Credential processor, validator and gatekeeper against the observer

**Prediction.** None of the three gains over the observer. In every cell, each one's lead has a 95% interval that contains zero or lies below it.

**Basis.**
- **Credential processor.** Its evidence is its own fan-out sends. It holds that evidence only on the 1 in 17 transactions for which it was C. The fan-out median sits several holds before the record time: the gatekeeper hold, departure bundling, the board push, the post-match lottery and the two registry schedules. The pilot leads were +0.04, +0.02 and +0.01 points, each with an interval containing zero.
- **Validator.** Its candidates are its own replies, one per transaction. Each names the device, but the observer has three packets per capture. The delay from the reply to the record time is long and wide. The pilot leads were -0.86, -0.03 and +0.02 points.
- **Gatekeeper.** Its postings carry the credential path's timing. That timing sets the record only when the board sets the confirmation, about half the time. The posting-to-record delay then passes through the board push, the post-match lottery and both registry schedules. The pilot leads were +0.12, +0.03 and +0.02 points, each with an interval containing zero.

**Fails if** any of the three has a positive lead whose 95% interval excludes zero in any cell.

## 6. Observer with its timing evidence off

**Prediction.** It sits above the feasible chance rate in every cell: the lower bound of its 95% interval is above the chance rate. Its multiple of chance lies between 2.5 and 4.5 in every cell. It is flat across R: the largest multiple is at most 1.5 times the smallest.

**Basis.** The feasible set holds every device with a packet inside the likelihood's support around the record time. With a flat likelihood, a device's summed posterior is its number of packets in that window. The record's own device always has its capture's three packets there, while a random feasible device has fewer on average. The window and the capture rate scale together with R, so the multiple does not depend on R. The pilot measured 6.65%, 3.72% and 2.11%, against chance rates of 1.77%, 1.35% and 0.67%. Those are multiples of 3.8, 2.8 and 3.1.

**Fails if** any cell's lower bound is at or below chance, any multiple is outside 2.5 to 4.5, or the largest multiple exceeds 1.5 times the smallest.

## 7. Record time at the midpoint

**Prediction.** For both the observer and the content server, no cell shows a negative change whose 95% interval excludes zero. Pooled over the three cells, each change is positive. No cell's change exceeds +1.0 point.

**Basis.** F's and I's submissions leave on the shared 120 s registry bundle schedule. Their midpoint is free of the posting schedule's fixed offset, which the pooled likelihood can only smear. It is still coarse, so the gain is small. The pilot measured the observer at +0.47, +0.05 and +0.21 points, and the content server at +0.39, +0.58 and +0.22 points.

**Fails if** any cell shows a negative change whose interval excludes zero, a pooled change is zero or negative, or any cell's change exceeds +1.0 point.

## 8. The shuffle test

**Prediction.** The test finds no shortfall from the shuffle or from the feasible-set calculation.
- Every shuffled pick is the permuted unshuffled pick, apart from tied scores, in fewer than 0.1% of records.
- Feasible counts never change.
- Over 200 permutations per run, the mean shuffled accuracy and the mean chance rate each lie within 3% of their exact expectation, one over the number of devices.
- The estimator's 95% interval covers the exact expectation in 90% to 97% of permutation draws.

**Basis.** Permuting the labels renames the groups the posterior is summed over and changes no score. So the expected accuracy and the expected chance rate are both one over the number of devices. The pilot found 0, 0 and 12 mismatches in 6,136, 5,814 and 30,019 records, all ties at R = 100, and no feasible-count change. The means over permutations were within 2.3% of exact, and coverage was 88.5% to 91.5% on 30 runs.

**Fails if** mismatches reach 0.1% of records in a cell, any feasible count changes, a mean over permutations is more than 3% from exact, or coverage lies outside 90% to 97% in a cell.

# Predictions

Written and committed before the run. Each prediction comes from the model or from a pilot. The pilot ran the run's own code on 30 runs per cell of the main configuration, on run ids 900,000 to 900,029, which the run does not use. It used the run's calibration seeds, so its D is the run's D.

Each item states what counts as a failure. `RESULTS.md` sets every prediction against its measured value.

## 1. Mean capture to finalization

**Prediction.** D = 1,170.1 s. The mean capture-to-posting time of real transactions is between 1,140 s and 1,190 s in every cell of the main configuration.

**Basis.** The calibration is deterministic on its seeds and gives D = 1,170.1 s. The pilot measured 1,158.3 s [1,142.3, 1,173.9] at R = 1, 1,163.5 s [1,148.8, 1,177.6] at R = 20 and 1,174.4 s [1,162.3, 1,186.3] at R = 100. Delays do not depend on volume, because there is no queueing.

**Fails if** D differs from 1,170.1 s, or any cell's mean lies outside 1,140 to 1,190 s.

## 2. Counts in flight

**Prediction.** In every cell of every configuration, the mean number of real transactions in flight is within 3% of R, and the mean number of decoys in flight is within 3% of 60.

**Basis.** D is the mean time a transaction stays in the system, so by Little's law the rates R / D and 60 / D give R and 60 in flight. The pilot measured 1.01, 19.42 and 100.61 real, and 59.57, 59.19 and 60.11 decoys. Its 19.42 at R = 20 follows from its runs drawing 3% fewer arrivals than expected (193.9 against 200 per run). The measured count equals arrivals per second times the mean residence in every pilot cell.

**Fails if** any cell of any configuration is more than 3% from either target.

## 3. Confirmations set by the match board

**Prediction.** The match board sets between 47% and 53% of F's and I's confirmations in every cell of the main configuration.

**Basis.** A content server confirms at the later of two events: its own pre-match hold release (content arrival plus a 120 s hold), or the second board push carrying the match. The credential path's holds and the content path's holds put the two at similar times. The pilot measured 50.1%, 49.7% and 50.2%.

**Fails if** any main cell is outside 47% to 53%.

**Controls.** The intended path's share is at least 95% in every cell of every first-relay control. The small simulations that set the controls measured 96.1% for the credential path, 98.1% for the content paths and 96.8% for the F content path. A control fails this prediction if any cell is below 95%.

## 4. Device named: passive observer and content server

**Prediction.** The point estimates lie in these ranges:

| Cell | Passive observer | Content server |
|---|---|---|
| R = 1 | 7.6% to 9.5% | 8.3% to 10.1% |
| R = 20 | 4.1% to 5.6% | 5.4% to 6.8% |
| R = 100 | 3.0% to 3.5% | 3.4% to 3.8% |

**Basis.** The ranges are the pilot's 95% intervals. The pilot measured the observer at 8.58%, 4.83% and 3.23%, and the content server at 9.20%, 6.12% and 3.62%.

**Fails if** any point estimate lies outside its range.

## 5. Credential processor, validator and gatekeeper against the observer

**Prediction.** None of the three gains over the observer. In every cell, each one's lead has a 95% interval that contains zero or lies below it.

**Basis.**
- **Credential processor.** Its evidence is its own fan-out sends. It holds that evidence only on the 1 in 17 transactions for which it was C. The fan-out median sits several holds before the record time: the gatekeeper hold, departure bundling, the board push, the post-match lottery and the two registry schedules. The pilot leads were +0.05, -0.05 and +0.00 points, each with an interval containing zero.
- **Validator.** Its candidates are its own replies, one per transaction. Each names the device, but the observer has three packets per capture. The delay from the reply to the record time is long and wide. The pilot leads were -0.39, +0.58 and +0.12 points, each with an interval containing zero.
- **Gatekeeper.** Its postings carry the credential path's timing. That timing sets the record only when the board sets the confirmation, about half the time. The posting-to-record delay then passes through the board push, the post-match lottery and both registry schedules. The pilot leads were +0.05, +0.04 and +0.01 points, each with an interval containing zero.

**Fails if** any of the three has a positive lead whose 95% interval excludes zero in any cell.

## 6. Observer with its timing evidence off

**Prediction.** It sits above the feasible chance rate in every cell: the lower bound of its 95% interval is above the chance rate. Its multiple of chance lies between 2.2 and 4.5 in every cell. It is flat across R: the largest multiple is at most 1.6 times the smallest.

**Basis.** The feasible set holds every device with a packet inside the likelihood's support around the record time. With a flat likelihood, a device's summed posterior is its number of packets in that window. The record's own device always has its capture's three packets there, while a random feasible device has fewer on average. The window and the capture rate scale together with R, so the multiple does not depend on R. The pilot measured 6.61%, 3.63% and 2.10%, against chance rates of 1.80%, 1.37% and 0.69%. Those are multiples of 3.67, 2.64 and 3.04.

**Fails if** any cell's lower bound is at or below chance, any multiple is outside 2.2 to 4.5, or the largest multiple exceeds 1.6 times the smallest.

## 7. Record time at the midpoint

**Prediction.** For both the observer and the content server, no cell shows a negative change whose 95% interval excludes zero. Pooled over the three cells, each change is positive. No cell's change exceeds +1.0 point.

**Basis.** F's and I's submissions leave on the shared 120 s registry bundle schedule. Their midpoint is free of the posting schedule's fixed offset, which the pooled likelihood can only smear. It is still coarse, so the gain is small. The pilot measured the observer at +0.46, +0.53 and +0.15 points, and the content server at +0.68, +0.06 and +0.23 points.

**Fails if** any cell shows a negative change whose interval excludes zero, a pooled change is zero or negative, or any cell's change exceeds +1.0 point.

## 8. Departure to arrival at C, F or I

**Prediction.** For credential packets (at C) and for F and I content packets (at F or I), in every cell of the main configuration, the delay from the packet's departure to its arrival has a mean between 355.6 s and 364.7 s and a standard deviation between 258 s and 270 s.

**Basis.** The two relay holds have means of 60 s and 300 s and standard deviations of 51.25 s and 258.72 s. Their sum has a mean of 360.0 s and a standard deviation of 263.7 s before network time. A relay picks its hold from its hop position only, so all three packet types share this distribution. Network time adds three link latencies, three jitters and the two relays' processing.
- **Link latencies:** about 65 ms from the device to the first relay, and about 42.5 ms on each of the two links between nodes.
- **Jitter:** 2 ms on each link.
- **Processing:** 1.75 ms at each relay.

Together these add about 0.16 s to the mean. Their spread of tens of milliseconds leaves the standard deviation at 263.7 s. The predicted mean is 360.2 s. With about 40,000 packets per type in the R = 1 and R = 20 cells, the standard error of the mean is about 1.3 s. The standard error of the standard deviation is about 1.9 s, because the geometric holds have heavy tails. The ranges are about 3.5 standard errors either side. The pilot measured means of 358.0 s to 365.2 s and standard deviations of 263.0 s to 268.2 s, on about 6,000 packets per type per cell.

**Fails if** any packet type in any main cell has a mean outside 355.6 to 364.7 s or a standard deviation outside 258 to 270 s.

## 9. The shuffle test

**Prediction.** The test finds no shortfall from the shuffle or from the feasible-set calculation.
- Every shuffled pick is the permuted unshuffled pick, apart from tied scores, in fewer than 0.1% of records.
- Feasible counts never change.
- Over 200 permutations per run, the mean shuffled accuracy and the mean chance rate each lie within 3% of their exact expectation, one over the number of devices.
- The estimator's 95% interval covers the exact expectation in 90% to 97% of permutation draws.

**Basis.** Permuting the labels renames the groups the posterior is summed over and changes no score. So the expected accuracy and the expected chance rate are both one over the number of devices. The pilot found 0, 3 and 9 mismatches in 6,139, 5,816 and 30,019 records, all ties, and no feasible-count change. The means over permutations were within 1.5% of exact, and coverage was 92% to 93% on 30 runs.

**Fails if** mismatches reach 0.1% of records in a cell, any feasible count changes, a mean over permutations is more than 3% from exact, or coverage lies outside 90% to 97% in a cell.

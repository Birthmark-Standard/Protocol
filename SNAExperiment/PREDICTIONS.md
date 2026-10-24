# Predictions

Written and committed before the run. Each item states what counts as a failure. `RESULTS.md` sets every prediction against its measured value.

## 1. Mean capture to finalization

**Prediction.** D is within 1% of 1,170.4 s. The mean capture-to-posting time of real transactions is between 1,140 s and 1,190 s in every cell of the main configuration.

**Basis.** A calibration at 100 decoys gives D = 1,170.4 s. Delays do not depend on volume, because there is no queueing.

**Fails if** D differs from 1,170.4 s by more than 1%, or any cell's mean lies outside 1,140 to 1,190 s.

## 2. Counts in flight

**Prediction.** In every cell of every configuration, the mean number of real transactions in flight is within 3% of R, and the mean number of decoys in flight is within 3% of 100.

**Basis.** D is the mean time a transaction stays in the system, so by Little's law the rates R / D and 100 / D give R and 100 in flight.

**Fails if** any cell of any configuration is more than 3% from either target.

## 3. Confirmations set by the match board

**Prediction.** The match board sets between 47% and 53% of F's and I's confirmations in every cell of the main configuration.

**Basis.** A content server confirms at the later of two events: its own pre-match hold release (content arrival plus a 120 s hold), or the second board push carrying the match. The credential path's holds and the content path's holds put the two at similar times.

**Fails if** any main cell is outside 47% to 53%.

**Controls.** The intended path's share is at least 95% in every cell of every first-relay control. The small simulations that set the controls measured 96.1% for the credential path, 98.1% for the content paths and 96.8% for the F content path. A control fails this prediction if any cell is below 95%.

## 4. Departure to arrival at C, F or I

**Prediction.** For credential packets (at C) and for F and I content packets (at F or I), in every cell of the main configuration, the delay from the packet's departure to its arrival has a mean between 355.6 s and 364.7 s and a standard deviation between 258 s and 270 s.

**Basis.** The two relay holds have means of 60 s and 300 s and standard deviations of 51.25 s and 258.72 s. Their sum has a mean of 360.0 s and a standard deviation of 263.7 s before network time. A relay picks its hold from its hop position only, so all three packet types share this distribution. Network time adds three link latencies, three jitters and the two relays' processing.
- **Link latencies:** about 65 ms from the device to the first relay, and about 42.5 ms on each of the two links between nodes.
- **Jitter:** 2 ms on each link.
- **Processing:** 1.75 ms at each relay.

Together these add about 0.16 s to the mean. Their spread of tens of milliseconds leaves the standard deviation at 263.7 s. The predicted mean is 360.2 s. The ranges are about 3.5 standard errors either side.

**Fails if** any packet type in any main cell has a mean outside 355.6 to 364.7 s or a standard deviation outside 258 to 270 s.

## 5. The shuffle test

**Prediction.** The test finds no shortfall from the shuffle or from the feasible-set calculation.
- Every shuffled pick is the permuted unshuffled pick, apart from tied scores, in fewer than 0.1% of records.
- Feasible counts never change.
- Over 200 permutations per run, the mean shuffled accuracy and the mean chance rate each lie within 3% of their exact expectation, one over the number of devices.
- The estimator's 95% interval covers the exact expectation in 90% to 97% of permutation draws.

**Basis.** Permuting the labels renames the groups the posterior is summed over and changes no score. So the expected accuracy and the expected chance rate are both one over the number of devices.

**Fails if** mismatches reach 0.1% of records in a cell, any feasible count changes, a mean over permutations is more than 3% from exact, or coverage lies outside 90% to 97% in a cell.

## 6. Window halves

**Prediction.** The observer's accuracy in the first and the second half of the window agrees in every cell: the 95% interval on the difference contains zero.

**Basis.** Traffic in flight is steady through the window, so nothing changes between its halves.

**Fails if** any cell's interval excludes zero.

## 7. Correlation rate bounds

**Prediction.** A vantage's device-named accuracy falls with everything in flight, real and decoy. Accuracy in percent times (100 + R) is at most 485 for the observer and 574 for the content server. Divided by (100 + R), these give the bounds:

| Cell | Passive observer, at most | Content server, at most |
|---|---|---|
| R = 1 | 4.8% | 5.7% |
| R = 150 | 1.9% | 2.3% |

**Basis.** The number of feasible candidates grows with the transactions in flight, decoys and real together.

**Fails if** a vantage's point estimate is above its bound in either cell. A rate below its bound is not a failure.

## 8. Cost

**Prediction.** One run of every cell of every configuration costs 204 s of worker time on the machine that profiled it, 94% of it scoring. 100 runs cost 5.7 worker-hours there. Scaled to Sam's machine by its measured speed against the profiling machine, the run phase takes 2.1 to 4.2 hours on the default 8 workers. The low end assumes 8 workers deliver the throughput of 16. The high end assumes each worker runs at the speed it has with 16.

**Fails if** the run phase, from the first run to the last, takes more than 4.2 hours on the default workers.

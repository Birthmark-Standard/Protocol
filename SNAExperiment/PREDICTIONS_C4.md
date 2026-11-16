# Predictions for C4: link-level tracer, Registry Node, K records and workloads

Written before the run. A prediction counts as made before the run once this file is committed. Each item states the prediction, its basis, what counts as a failure, and whether it can fail.

C4 has cells R = 1 and 100. R = 300 runs only if time remains, last in the job queue.

## Parameters

| Parameter | Value | Reason |
|---|---|---|
| W1 | Each identity's rate is a device's rate times a factor drawn from a lognormal with σ = 0.90, then scaled so each population's mean factor is 1. Real devices and decoy identities draw alike | A slow and a fast device (10th and 90th percentiles) differ by a factor of 10.0. The scaling keeps R and 100 in flight |
| W1 at R = 1 | The one real device keeps the rate of the cell | R fixes that device's rate |
| W2 | W1, plus sessions for 20% of identities. A session starts at 1 per 12 hours, lasts a uniform 10 to 60 minutes, and multiplies the identity's rate by 10. Rates between sessions are scaled down so each population's mean rate holds | A photographer at an event. 30.4% of a session identity's captures fall in sessions |
| W2 at R = 1 | The one real device has sessions; decoy identities have them with probability 0.2 | At R = 1 the case of interest is the one device at an event. W1 covers a device without sessions |
| W-mismatch | Real devices follow W2. Decoy identities keep C2's single rate | Decoy operators who do not copy real behavior |
| K values | R = 1: 1, 2, 3, 5, 10, 20. R = 100: 1, 2, 3, 5, with a 2-hour window; 10 and 20 under W1 and W2 only | As agreed. At R = 100 a device makes 2.99 captures per hour |
| Edit chains: share of captures edited | 30% | Most captures are published as shot; a minority are edited |
| Edit chains: edits per edited capture | 1 + Poisson(0.5), at most 4 | A capture and a few edits: chains of 2 to 5 records, mean 2.5 for an edited capture |
| Edit chains: delay from the parent's posting to the edit's capture | 5 minutes plus an exponential with mean 30 minutes | The editor opens a file that verifies against the registry, so the edit follows the parent's posting. A short delay keeps chains inside the window |
| Edit chains: same-source share | 100% and 50% | 100% is the upper bound. Otherwise the edit comes from the user's machine: one second source address per device, used only for its edits |
| Edit chains: decoys | Decoy identities edit with the same parameters. A decoy edit points to an earlier record of the same decoy identity | Decoys copy the real mix |
| Edit chains: volume | Capture rates are divided by 1.45 (1 + 0.3 × 1.5), so captures and edits together keep R and 100 in flight | The cell's volume counts every transaction |

## Sources of numbers

- **C2:** `results/C2`. Observer 4.77% and 2.33% at R = 1 and 100. Chance 1.11% and 0.55%.
- **Model-seed numbers:** the main configuration on seeds from 1,700,000,000, which no evaluation run and no model uses, as in `PREDICTIONS_C3.md`. No attacker was run on them.

## How the tracer treats the ambiguity inside a hold

A relay's hold is geometric on its node's 10-second ticks. For one release probability p, an assignment of k arrivals to k departures has likelihood Π p (1 − p)^(n_i − 1), where n_i is the number of ticks packet i waited. The sum of the n_i is fixed by the arrival and departure times, whatever the assignment. So every assignment that respects causality, the cap and the tick grid has the same likelihood. The tracer does not guess among them. It counts them. A packet's posterior over departures is the share of valid assignments that give it each departure. Two positions mix at one node: a first relay (mean 60 s) and a second relay (mean 300 s). Their p differ, so an assignment that swaps a first-relay packet and a second-relay packet has a different weight, and the tracer weighs it so. The position is visible on the inbound link: a packet from an external host is at a first relay.

A node's problem splits into independent pieces, the connected components of its possible pairings. For a piece with at most 10 arrivals the tracer counts every complete pairing exactly, by a forward and backward sum over the sets of arrivals used. A larger piece is approximated by matrix scaling (Sinkhorn), which balances the weight matrix until each departure is used once and each arrival once. On 396 small cases built from the hold weights, the Sinkhorn share of a pairing differs from brute-force enumeration by at most 0.035 in the median case, 0.15 at the 90th percentile and 0.23 in the worst; the exact count differs by under 10^−14. Pieces with more than 10 arrivals occur when a node is busy: a second relay holds packets for up to 900 s.

The tracer follows every leg the wire shows, as a global passive observer can: the relays; at a destination, an arrival that stays to C's CV-1 or to one of the node's registry submissions (the origin of a submission is on the wire, because the origin floods it to every peer at once); the validator's CV-1 to CV-2; and each reply reaching C to the two submissions it leads to, by the quorum timing. It estimates when each node learns of quorum by following the protocol from the reply: C's fan-out tick, the gatekeeper's hold tick, the gatekeeper's 30-second departure grid, the board's 10-second push, and the link to the node. It measures each link's latency on the wire and is given each clock's, grid's and push schedule's phase. A global observer can read those phases from the times departures and submissions leave, so giving them is an upper bound on what it learns. It scores every device with at least three packets near the record by its triples of packets, one packet as the credential packet and two as content packets, jointly: the reply, the two submissions at two different nodes, their timing after the reply, and the record time after the later submission. It uses every end point a packet keeps.

Its densities come from model seeds that carry the cell's whole load. Each density has a uniform tail of weight 1 / (n + 1) over 5% of its span past each end, so a value just past the samples is unlikely rather than impossible. A delay that is exactly zero in some cases has a point mass at zero: in the every-hold-off control, the record time is the moment the later submission has reached every node, exactly. The schedules are modeled, not fitted: under registry-level bundling a submission's time tells only the 120-second interval its ready time fell in, so the tracer uses the probability of that interval; under the posting schedule any record time within one period after the later submission's flood is equally likely. Each credential packet spreads one unit of probability over the pairs of the device's packets that could be its content packets, so a device with more packets near the record gains only by having more transactions. The Registry Node uses the same score with the record's two submissions fixed.

## Arithmetic used throughout

**Bound from the posting schedule.** As in `PREDICTIONS_C3.md`: every record posted at one 120 s boundary carries the same time. So any vantage that names a device from the record time alone is right at most E[k / n] of the time, where n is the records in the posting and k those of the record's device. With λ = 120 (R + 100) / D other records per posting and 0.10 records of one device per posting, that is 10.5% at R = 1 and 5.3% at R = 100 under W0. Finding one record, as in C5, is bound by E[1 / (1 + Poisson(λ))] instead: 9.64% and 4.87%. This holds for the observer, the tracer and every timing vantage, however good its timing. Linking records across postings, as the K-record attacker does, is not bound by it.

**Packets pending at a relay.** Packets enter the relays at 3 (R + 100) / D per second: 0.26 at R = 1 and 0.51 at R = 100. Each packet passes one first relay and one second relay, over 20 nodes. By Little's law, pending at a second relay = 0.26 / 20 × 300 = 3.9 at R = 1 and 7.7 at R = 100. At a first relay it is 0.26 / 20 × 60 = 0.78 at R = 1 and 1.5 at R = 100.

## 1. Tracer, every hold off

**Prediction.** In the every-hold-off control the tracer names the device on 11% to 28% of records at R = 1 and 5.5% to 16% at R = 100.

A second control is added for the tracer: every hold and every schedule off, including the departure grid and the board push. In it, the tracer names the device on at least 99.0% of records at R = 1 and at least 98.1% at R = 100.

**Basis, every-hold-off control.**
- This control has no posting schedule. A record's time is the moment the later of its two submissions has reached every node. So the record time names that submission. It does not name the earlier one: any submission that reached every node before it fits.
- The control keeps the gatekeepers' 30-second departure grid and the boards' 10-second push. So every transaction whose quorum falls in one grid interval learns of quorum on one push tick at a node, and submits on that tick. On the wire, the submissions on one tick at one node cannot be told apart by their content packets or their replies.
- So a record is ambiguous between its own transaction and each other transaction that submitted at the same node on the same tick and whose other submission reached every node before the record. Call these look-alikes. The tracer cannot do better than one over one plus the number of look-alikes.
- Arithmetic. D = 20.49 s, so a 30-second grid interval holds (R + 100) / D × 30 transactions: 148 at R = 1 and 294 at R = 100. A given node is F or I of a transaction with probability 2 / 17. So 17.4 other transactions share the record's node and tick at R = 1, and 34.5 at R = 100. About half of them had their other submission reach every node first: 8.7 and 17.2 look-alikes. Poisson counts give E[1 / (1 + k)] = 11.5% and 5.8%. This is the low end of each range.
- The three gatekeepers have their own grid phases, and quorum is the second posting, so quorum times spread over more ticks than one grid interval. Counting the look-alikes of every real record on three development runs (seeds from 1,700,000,600; no attacker run on them) gives E[1 / (1 + k)] = 22% to 28% (mean 25%) at R = 1 and 14% to 16% (mean 15%) at R = 100. The high end of each range is the largest run.

**Basis, second control.**
- With every schedule off, a node learns of quorum at its own time, so no two transactions share a tick. Two things can still go wrong.
- The quorum step. The tracer knows when a node learns of quorum up to the gatekeepers' processing (1 to 10 ms), the nodes' processing and the jitter. On development seeds the gap between a submission and its estimate runs from −3.5 ms to 13.3 ms between its 0.5th and 99.5th percentiles. Two submissions at one node closer than that can swap. With the gap's own density, a swap costs 0.22% of records at R = 1 (0.58 submissions per second at a node) and 0.43% at R = 100 (1.15 per second).
- Relay ties. Two packets at one relay within 3 ms of processing can swap. A node relays 1.48 packets per second at R = 1 and 2.93 at R = 100, so another packet arrives within 2.5 ms of a given one for 0.74% and 1.46% of packets. Only the credential packet and the content packet of the later submission matter. If every such tie were lost, that would cost at most 0.74% and 1.46% of records.
- So accuracy is at least 99.0% at R = 1 and 98.1% at R = 100.

**Gate.** The tracer's sanity check is the second control: at least 99.0% at R = 1 and at least 98.1% at R = 100. If it fails, nothing else of C4 is run until the cause is found. The every-hold-off control is reported with its range and is not a gate.

**Fails if** either cell of the every-hold-off control lies outside its range, or the second control is below its bound.

**Can fail.** The tracer pairs a content packet with a submission by the time it waited at the node. If that pairing loses the true submission more often than the look-alike count assumes, the rate falls below the low end.

## 2a. Ceiling attacker

The ceiling attacker is told each transaction's true posting. For a record it picks one of that posting's records at random and names its device. It needs no tracer and runs first.

**Prediction.** Its device-named accuracy, beside the bound:

| Workload | R = 1 | R = 100 | R = 300 |
|---|---|---|---|
| W0 | 10.5% (10.0% to 11.0%) | 5.3% (5.1% to 5.6%) | 2.67% (2.55% to 2.80%) |
| W1 | 10.5% (10.0% to 11.0%) | 5.9% (5.5% to 6.3%) | — |
| W2 | 12.0% (11.0% to 13.0%) | 6.3% (5.7% to 6.9%) | — |
| W-mismatch | 12.0% (11.0% to 13.0%) | 6.3% (5.7% to 6.9%) | — |

For comparison, (1 − e^(−λ)) / λ is 9.64%, 4.87% and 2.43%.

**Basis.**
- A record from a device that makes x records per posting shares its posting with 1 + Poisson(x) of its own records and Poisson(λ − x) others. Its accuracy is the mean of (1 + X) / (1 + X + Y), from 400,000 draws.
- Under W0, x = 0.10 in every cell.
- Under W1, records come more often from fast devices, so x is larger on average. At R = 1 the one device keeps its rate.
- Under W2 and W-mismatch at R = 1, 30.4% of the device's records fall in sessions, where x = 0.71.

**Fails if** a cell lies outside its range.

**Can fail.** Postings are not exactly Poisson: the registry bundle and the posting schedule line up records. The model-seed E[1 / size] at R = 100 (4.88%) matches the formula (4.87%), which suggests they are close.

## 2. Tracer, main configuration

**Prediction.**

| Cell | Tracer | Multiple of the observer | Upper bound |
|---|---|---|---|
| R = 1 | 5.0% to 10.5% (point 7.5%) | 1.0 to 2.2 | 10.5% |
| R = 100 | 2.4% to 5.3% (point 3.9%) | 1.0 to 2.3 | 5.3% |

The tracer is never reliably below the observer on the same records. The label shuffle returns it to chance. With no decoys at R = 1 it names the device on 100% of records, because one device is left. On small cases the pairing shares it counts exactly equal brute-force enumeration to within 10^−9.

**Basis.**
- The bound from the posting schedule caps any vantage that uses the record time.
- The observer already reaches about 45% of it: 4.77 / 10.5 = 0.45 at R = 1, and 2.33 / 5.3 = 0.44 at R = 100.
- The tracer knows where each packet went with little ambiguity at the first relays (0.78 to 1.5 pending), and with more at the second relays (3.9 to 7.7 pending). So it gets more of the bound, but not all.
- The point estimates assume about 0.75 of the bound.

**Fails if** the tracer exceeds the bound by more than its interval, lies outside its range, or is reliably below the observer.

**Can fail.** If the tracer's gain is small, it falls below 5.0% at R = 1.

## 3. Registry Node

A Registry Node takes part in the registry's consensus, so it reads each submission. It knows which F and I submitted each record, and when. A link observer sees the same submissions arrive as constant-size frames from their origins, but not which record each one belongs to. `sim.py` floods each submission from its origin to every peer, so the origin and the time are on the wire. The Registry Node adds the link from each record to its two submissions.

**Prediction.** The Registry Node with the tracer names the device on 25% to 65% of records at R = 1, and on 8% to 30% at R = 100. It is not bound by the posting schedule.

**Basis.**
- Knowing the record's F and I, the candidates are the content packets that reached F, and those that reached I, in the window before the submission. That window is about 570 s when F's hold sets the time, and longer when quorum does. A node receives content packets at 2 (R + 100) / (17 D) per second: 0.0102 at R = 1 and 0.0201 at R = 100. That gives about 6 and 12 per side, of which about half are plausible by timing.
- Each candidate traces back through a second relay to about 3 devices at R = 1 and 6 at R = 100.
- The true device is in both sides. A false device is in both by chance about 9 × 9 / 101 ≈ 0.8 times at R = 1, and 36 × 36 / 206 ≈ 6.3 times at R = 100.
- So the rate is about 1 / 1.8 = 55% at R = 1 and 1 / 7.3 = 14% at R = 100, before timing weights. The ranges allow for the weights in either direction.

**Fails if** either cell lies outside its range.

**Can fail.** The counts of devices per side are rough.

## 4. K records

The K-record attacker runs first on the passive observer's posteriors. It runs on the tracer's posteriors afterwards, if time allows.

**Prediction, on the observer's posteriors.**

| K | R = 1, W0 | R = 100, W0 |
|---|---|---|
| 1 | equal to the observer, decision by decision | equal to the observer |
| 2 | 7.9% (4.7% to 12.6%) | 3.9% (2.3% to 6.2%) |
| 3 | 11.2% (6.7% to 17.9%) | 5.6% (3.4% to 9.0%) |
| 5 | 18.2% (10.9% to 29.1%) | 9.5% (5.7% to 15.2%) |
| 10 | 36.7% (22% to 59%) | — |
| 20 | 67.5% (40% to 100%) | — |

- At R = 1 the smallest tested K above 50% is 20.
- At R = 100 no K up to 5 reaches 50%.
- Under W1 and W2 the curve keeps its shape, starting from each workload's K = 1 rate.

**Basis.** The Gaussian score model below with d = 0.66 at R = 1 and 0.58 at R = 100, fitted to the observer's C2 rates. The ranges are 0.6 to 1.6 times each value. The model gives K = 14 for 50% at R = 1.

**Prediction, on the tracer's posteriors.**
- At K = 1 the K-record attacker equals the tracer, decision by decision.
- Accuracy rises with K in every cell and workload.
- At R = 1, W0, the smallest K at which accuracy exceeds 50% is between 2 and 10, point estimate 5.
- At R = 100, W0, accuracy at K = 5 is between 20% and 99.9%, point estimate 50%.
- The devices with at least K records in the 2-hour window at R = 100 (of 103):

| K | W0 | W1 | W2 |
|---|---|---|---|
| 2 | 101 | 81 | 80 |
| 3 | 97 | 68 | 67 |
| 5 | 73 | 47 | 46 |
| 10 | 8.5 | 19 | 19 |
| 20 | 0 | 4.5 | 4.9 |

**Basis.** Two cases bracket the tracer.
- **Sharp posterior.** If each record's posterior is spread evenly over the devices behind its posting, a false device survives K records only by being in all K postings. Each identity is in a given posting with probability p = 1 − e^(−λ / N): 0.098 at R = 1 (N = 101) and 0.095 at R = 100 (N = 206). The rate is then E[1 / (1 + Bin(N − 1, p^K))]:

  | K | R = 1 | R = 100 |
  |---|---|---|
  | 2 | 64% | 46% |
  | 3 | 96% | 92% |
  | 5 | 100% | 99.9% |

- **Soft posterior.** If each record adds a Gaussian score with true-device advantage d, set so K = 1 gives 0.8 of the bound (d = 0.92 at R = 1, 0.82 at R = 100), then summing K records gives advantage d√K. The rate first exceeds 50% at K = 7 at R = 1 and K = 11 at R = 100.
- The observer's own posterior (d = 0.66 at R = 1) would need K = 14.
- The table of devices is Poisson with mean 2.99 per hour over 2 hours, mixed over each workload's rate factors, from 2,000 draws.

**Fails if** the K = 1 decisions differ from the tracer's, accuracy falls with K by more than its interval, or a value lies outside its range.

**Can fail.** The R = 100 range is wide because the two cases differ that much. The R = 1 range excludes 20 and "never".

**Reporting.** The K-record rows are marked not applicable for the bound from the posting schedule, because they link records across postings.

## 5. Edit chains

**Prediction.**
- At a 100% same-source share, accuracy on a chain of L records equals the K-record accuracy at K = L, with the same posteriors, within its interval, and is at most 10% higher (relative) from the parent's posting.
- At 50% it is lower than at 100% for every L of 2 or more. It is about the K-record accuracy at K = 1 + (L − 1) / 2.
- At L = 1 both shares equal the tracer.

**Basis.**
- A chain is a public set of records that share a user. At 100% they share a source address, so the attacker sums over L records as the K-record attacker does.
- At 50%, the edits from the user's machine add evidence for a different address, not the camera's. So on average the camera's sum covers 1 + (L − 1) / 2 records.
- An edit's capture follows its parent's posting by at least 5 minutes, so the lower bound removes only candidates that are already unlikely.

**Fails if** 50% is not below 100% at some L of 2 or more, or the 100% curve leaves the K-record interval.

**Can fail.** Chains of 4 and 5 records are rare (about 1.4% of edited captures have 4 edits), so those rows may not meet the stability rule.

## 6. Workloads

**Prediction.** Chance and the passive observer:

| Workload | Chance, R = 1 | Observer, R = 1 | Chance, R = 100 | Observer, R = 100 |
|---|---|---|---|---|
| W0 | 1.11% | equal to C2 | 0.55% | equal to C2 |
| W1 | 1.36% | 3.3% to 4.8% | 0.68% | 2.0% to 2.7% |
| W2 | 1.39% | 4% to 8% | 0.68% | 2.0% to 2.8% |
| W-mismatch | 1.11% | 5.5% to 9% | 0.55% | 2.2% to 2.9% |

The tracer and the K-record attacker keep the order W0 ≤ W-mismatch for every K at R = 1. The counts in flight are within 3% of their targets in every workload and cell.

**Basis.**
- **Chance.** Chance rises under W1 and W2 because a slow identity is feasible less often: p(m) = 1 − e^(−2.23 m), mixed over the factors (4,000 draws).
- **W1.** Fast decoys outscore the one real device more often, so the observer falls at R = 1.
- **Session bound.** In a session the real device makes 21.4 captures per hour, 0.71 per posting. Its posting then holds about 1.71 of its records out of 11.1, so the posting bound for its in-session records is about 15%.
- **W-mismatch at R = 1.** The real device's sum dominates in a session, and 30.4% of its records are in sessions, so: 0.304 × (12% to 15%) + 0.696 × (3.5% to 4.8%) = 6% to 8%.
- **W2 at R = 1.** About one decoy identity is in a session at any time (20 × 0.049), so the real device is the top only about half the time in a session.
- **At R = 100,** only 8% of real records fall in sessions (26.5% of captures come from session devices, times 30.4%), so the effect is small.

**Fails if** a measured chance differs by more than 10%, a rate lies outside its range, or a count in flight is off by more than 3%.

**Can fail.** The W1 and W2 ranges rest on a direction argument and the bound, not on a fitted model.

## 7. Sanity

**Prediction.** With default options the code reproduces C2's R = 1 decisions exactly.

**Basis.** New behavior sits behind new options whose defaults are C2's.

**Fails if** any R = 1 decision differs.

**Can fail.** A new option that draws from a C2 stream would change every later draw.

## Reporting the bound

Every table shows the bound from the posting schedule beside each row it applies to. Rows with a link from a record to its transaction (the Registry Node) or across postings (K records, edit chains) are marked not applicable.

## Changes before the run

- The device-naming bound was first given as the record bound (9.64% and 4.87%). It is E[k / n], 10.5% and 5.3%, because a device can have two records in one posting. The tracer's ranges were raised to match.
- Item 2a, the ceiling attacker, was added.
- The K-record attacker runs first on the observer's posteriors, with its own predictions.
- The tracer's gate is the every-hold-and-schedule-off control.
- The tracer section first said the tracer counts valid assignments exactly per busy period. The code approximated every node by matrix scaling. It now counts pieces of up to 10 arrivals exactly and approximates larger ones, and the section states the approximation and its error against brute force. The brute-force prediction in item 2 now applies to the pieces counted exactly. This corrects a description that did not match the code.
- The tracer section now says the tracer follows the destination, validator and quorum legs, and scores a transaction's three packets jointly. The first tracer used only the relays and pooled densities from a packet's arrival to the record, and so ignored legs a global passive observer sees. This is a modeling error in the attacker; the predictions in items 1 to 4 are unchanged.
- Evaluation seeds were used in development. The tracer and the Registry Node ran on the traffic seeds of runs 0 and 1 at R = 1 and R = 100: in the main configuration, in the every-hold-off control and in the every-hold-and-schedule-off control. The gate test used run 0. The C4 observer job ran on runs 0 and 1 in a trial. No prediction in this file was changed because of those runs. From here on the tracer is developed on model seeds and on the controls only. The gate test uses a model seed.
- Item 1 first predicted 70% to 95% at R = 1 and 55% to 88% at R = 100 in the every-hold-off control. That arithmetic assumed the record time names both of a record's submissions, so that only a transaction sharing the record's F, its I and its tick was a look-alike. A link observer's record time names only the later submission; the earlier one is only known to come before it. And every transaction whose quorum falls in one grid interval submits on one push tick. This is a modeling error in the prediction. The new range comes from the corrected arithmetic and a count of look-alikes on development seeds, on which no attacker was run. The tracer's development runs on model seeds were seen before this change; the range does not come from them.
- The gate was first at least 99% in both cells. Its arithmetic counted only two packets at one relay within 3 ms. It left out the quorum step, where two submissions at one node within the spread of the gatekeepers' processing can swap. This is a modeling error in the gate's arithmetic. The gate is now set from the corrected calculation in item 1: at least 99.0% at R = 1 and 98.1% at R = 100. An earlier tracer gave 98.7% at R = 100 on an evaluation seed; the new gate does not come from that number.
- The tracer section now describes a tracer that estimates when a node learns of quorum by following the protocol's schedules (fan-out tick, gatekeeper hold tick, departure grid, board push), fits its densities at the cell's load with a uniform tail and a point mass at zero, models the bundle and posting schedules, normalizes each credential packet's pairs, and scores every device with every end point. The tracer before this change estimated the quorum from link latencies alone; fitted its densities on lighter traffic, with hard edges, and with one-second bins over the bundle and posting schedules, so each density followed the model runs' schedule phases; summed a device's triples without normalizing them, so devices with many packets near a record won; kept 12 submissions per packet; and scored only 60 devices per record. Each of these lost the true transaction on records it should have named. These are modeling errors in the attacker. The predictions in items 2 to 4 are unchanged.

# Analysis plan

This plan is fixed before the first sweep run. Every section below states what is run, how each number is computed, and what counts as a finding. If a result disagrees with a prediction, it is reported as a failed prediction. If a check fails, the failure is reported and the check stays as written.

## 1. Question

Semantic Non-Assembly claims that no single compromised component can link a piece of content to the credential transaction that produced it better than chance among the L transactions in flight.

The harm this protects against is a public registry record being traced to the device that produced it. This experiment tests the claim on that link. Starting from a registry record, each vantage tries to name the device submission behind it. Each vantage holds:

- its real keys;
- its own exact event timing;
- a passive view of the sizes and timing of all network traffic.

The test is whether its own knowledge lets it name the right device, or the right capture, more often than chance and more often than a passive observer on the same records.

## 2. Simulated system

The simulator follows the per-leg message specification. Its design choices are:

**Pool and roles**
- 20 submission servers, one validator, and one active set of three gatekeepers per run.
- Nine distinct nodes serve each transaction.
- The paths {A, B, C}, {D, E, F} and {G, H, I} share no node.
- C, F and I are never gatekeepers. A gatekeeper may relay.

**Timing lottery**
- Every relay hop holds each packet on its node clock: 10-second ticks, 8.33% release per tick, released at tick 30 at the latest.
- A device holds each of its three first-hop packets on a fresh random phase.
- The credential processor draws each gatekeeper fan-out leg separately on its node clock.
- Each gatekeeper verifies, holds on its own dedicated hold clock, then posts to its board. Section 6d alone replaces it with a two-point hold, dropped again in section 6e.

**Content servers**
- A content server holds on its node clock. It never queries a board (section 6c).
- Each match board pushes every match posted since its previous push to every content server, every 10 seconds on its own schedule.
- A content server submits to the registry once its hold has released and pushes from two boards have carried a posting with a valid σ_C. From section 6d on, the submission then waits for the next registry-level bundle.
- It drops the packet if quorum has not formed 30 minutes after arrival.

**Registry submissions**
- Submissions are 98-byte messages gossiped with gossipsub.
- The originating node flood-publishes to every peer. Every peer forwards to its six mesh peers.

**Padding**
- Every transit leg is padded to a size drawn uniformly from 420 to 460 bytes.
- The gatekeeper fan-out leg is padded to 820 to 860 bytes.
- The measured TLS 1.3 record overhead of 22 bytes is added on the wire.
- The Ring V signature over one validator is 64 bytes, so the fan-out leg's raw size is 753 bytes.

**Decoys**
- A decoy is a genuine transaction from a genuinely registered device credential. The credentials belong to a pool of identities held by the decoy infrastructure.
- It passes every stage exactly as a real transaction does: V approves it, C fans it out with a valid σ_C, the gatekeepers verify and post it, quorum forms, and F and I finalize a permanent registry record.
- No party can tell a decoy from a real transaction.
- The decoy stream is a steady Poisson process at 40 transactions in flight (rate 40 / D), independent of real traffic.
- The pool has as many identities as the decoy rate needs for each identity to capture every 20 minutes on average, like a device: 77 identities at D = 625.6 s. A decoy identity's packets come from its own external address, with the same latency model as a device.
- Registry records are permanent. No pruning is modelled.
- Decoy transactions draw their random numbers from their own streams, and their registry submissions are gossiped on their own stream. So a cell with decoys carries exactly the real traffic of the cell without them at the same R. The one exception is the observer's timing of a registry burst: when a real and a decoy submission leave one node on the same clock tick, the burst is timed by its first frame (under 2 ms apart).

**Background traffic**
- 25 clients per node exchange TLS sessions whose record sizes come from a measured pool, plus DNS lookups, bulk transfers and keepalives.
- Check 3 below tests whether background traffic changes any decision. If it passes, the sweeps run without background traffic, because it then enters no attack's inputs.

**Volume**
- L is the number of transactions in flight, by Little's law: L = rate × D.
- D is the simulator's measured mean end-to-end delay, from capture to registry finalization (the later of the two submissions).
- D = 625.6 s was measured from 10 seeded runs, 21,561 transactions, none dropped. It is stored in `results/calibration.json`.
- Each device captures every 20 minutes on average, so devices = rate × 1,200 s.

## 3. Vantages and attacks

### 3.1 Rows and candidates

**Rows: registry records.** A passive observer finds each registry submission as a flood-publish burst: gossip-size frames that one node sends to nearly every peer within 2 ms. When several submissions leave one node on the same tick, the burst carries one frame per submission to every peer, and the observer counts them as the smallest per-peer frame count. The public record names both submitting servers, so the observer pairs a record's two submissions. A record is timed at their midpoint, u. Every real record whose capture falls in the scored window is a row.

**Candidates: device submissions on the wire.**
- A device packet is a relay-class application record sent from an external host to a pool node.
- An external source that ever sends anything else (a handshake, a DNS lookup, a record outside the class) is not treated as a device, and all its packets are dropped. Check 2 confirms that this removes every background client.
- Each source's packets are grouped greedily in time order: a group holds up to three packets within one device hold (310 s) of its first. A group is timed at its members' mean send time, s.
- Decoy identities' packets are candidates for every vantage.

**Success**, scored at two levels:
- **Device (primary).** The vantage names a device: the source with the largest summed posterior over its groups. It is right if that is the record's device. A source address is visible on the wire, so every vantage can aggregate this way.
- **Submission.** The vantage names a group. It is right if the group contains a packet of the record's own capture.

### 3.2 What each vantage knows, and how it enters

Each vantage scores a row against every candidate with a likelihood of the record time given that candidate. Every vantage's likelihood nests the baseline's: it is the baseline density conditioned on the vantage's extra observation. So a vantage whose extra observation carries no information scores exactly as the baseline does.

The rows of each vantage are the records it took part in:

| Vantage | Rows | Likelihood of record r from candidate group k |
|---|---|---|
| Baseline | every record | g(y), where y = u_r − s_k |
| First hop, credential | records whose credential it relayed as A | p(y given its own hold) for groups containing a packet it relayed; g(y) for the rest |
| First hop, content | records whose content it relayed as D or G | the same |
| Credential processor | records whose credential it processed as C | mixture over its own transactions j: 1/17 × Σ_j w_kj p(y given x_kj) plus the remaining weight × g(y). Here x_kj is transaction j's fan-out median minus s_k, and w_kj is the posterior that j is k's transaction |
| Content server | records it submitted (as F or I) | the joint density of y and x = its own content arrival − s_k |
| Validator | every record | its own replies are its candidates, each labelled with its credential's identity; density of u_r minus the reply send time. Decoy approvals are candidates, since nothing marks them |
| Gatekeeper | every record (all three gatekeepers see every transaction) | mixture over its own postings j: Σ_j w_kj p(y given x_kj), where x_kj is posting j minus s_k |

Notes on the model choices:
- The first hop's own hold does not depend on which candidate is the source, so the conditional density is the right likelihood.
- The content server's arrival offset does depend on the source, so the joint density is used.
- In the mixtures, w_kj ∝ q(x_kj), where q is the density of x for the true pair, normalised over the server's events.

**Densities.** Each density is a histogram built from Monte Carlo runs on seeds disjoint from the evaluation seeds:
- g: 1 s bins.
- The conditional densities: 2D histograms with 10 s bins in x, each shrunk towards g with 20 pseudo-samples per x bin, so a sparse or unseen x falls back to g.
- Every density is −inf outside the simulated support of y.

Delays do not depend on volume, so one model set serves every cell. The sensitivity control has its own models, with 0.05 s bins in y and 0.5 s bins in x.

**Paired baseline.** Every vantage's rows are also scored by the baseline, so each vantage's contribution is a paired difference on the same records.

**Decision.** Per decision: each row picks its highest-scoring candidate, at each level. No joint assignment is used.

## 4. Pre-run checks

`python -m sna checks` runs these checks. Each outcome is reported.

1. **Padding classes**
   - Every credential, content, validator and fan-out leg lies in its class on the wire.
   - Every raw payload fits its class minimum. This includes the reply's one-byte indicator.
   - A Ring V signature made and verified with real keys is 64 bytes.
   - A padding-class scaling note lists the fan-out leg's raw size against the number of Ring V members. It is a size question and does not bear on decoys.
2. **Answer extraction.** The observer extracts exactly the true registry submissions, with none missing and none extra. Its device candidates hold every device and decoy first-hop packet and no background packet. The share of submission groups that hold a single capture is reported.
3. **Background independence.** Every vantage's and baseline's decisions are identical with background traffic on and off, on the same seed.
4. **Cannot tell decoys** (all seven vantages)
   - Each feature a vantage observes is tested:
     - the baseline and the first hops: sizes, holds, processing delays, the spread of a source's three first-hop sends, and the time since the source's previous capture;
     - the credential processor: its processing delays and received sizes;
     - the content server: its last-leg size and hold;
     - the validator: its request-to-reply delay, request size, and the time since the same credential's previous request;
     - the gatekeeper: its arrival-to-posting delay.
   - The test is the AUC of that feature for real against decoy, with a run-clustered interval, Bonferroni-adjusted across every feature test (36).
   - Pass: every adjusted interval covers 0.5.
   - Decoys run the same code as real transactions, so a pass is expected by construction. The check confirms nothing in the simulator separates them.
5. **Decoys reach the registry.** Every decoy transaction reaches quorum and produces a registry record, as every real one does.
6. **Departure bundling.** Every gatekeeper posting departs on its gatekeeper's own 30-second grid, at least 0 and under 30 seconds after the hold clock selected it.
7. **Board pushes.** No content server acts before its hold releases or before the second board push carrying the match reaches it. Every push lands on its board's own 10-second schedule.
8. **Gatekeeper hold shape** (section 6d builds only). Every gatekeeper hold is either immediate or the full 5-minute cap, with about 40% at the cap. On other builds the check reports that it does not apply.
9. **Registry-level bundling** (section 6d). Every registry submission departs on the one shared schedule, at least 0 and under one window after its content server confirmed it.

The checks run at R = 15 with the decoy stream, departure bundling and background traffic on, over 12 seeded runs, on the latest build.

## 5. Cells, runs and metrics

### 5.1 Cells

A cell is a real volume R (real transactions in flight), with or without the decoy stream.

- **With decoys:** R = 1, 5, 15, 45 and 100, each with 40 decoys in flight (T = R + 40).
- **Without decoys:** R = 1 and 15, the paired references.

All seven vantages are scored in every cell. Decoys are indistinguishable to every vantage, so there is no split by vantage.

**Sensitivity control.** R = 40 with every hold off: device, relay, fan-out, gatekeeper and content server. It uses its own likelihood models, with 0.05 s bins.

**Traffic seeds.** A run's traffic seed depends on R and the run id only. So:
- the cell with decoys carries the real traffic of the cell without them at the same R (section 2);
- every vantage reads the same run.

**Scored window.** Real records whose capture falls in the scored window are scored; decoy records are never rows. The window is 3 hours, extended to hold 200 real transactions on average: 200 × D / R, which is 34.7 hours at R = 1. Warm-up is 20 minutes and cool-down 40 minutes.

**Run count.** Recorded in section 8, before the first sweep run. The re-scoring of section 6a uses the same 200 runs.

Probe runs use run ids from 1,000,000 upward and are written to `results/probe/`. They are used only to measure cost and successes per run, and they are never reported as findings.

### 5.2 Metrics per cell and vantage

At each level (device primary, submission secondary):

- **Accuracy.** Per-decision accuracy with a 95% interval from resampling whole runs (2,000 replicates). A Bonferroni-adjusted interval is also computed across the 7 vantages × 2 tests in the cell.
- **Chance references.**
  - The random-assignment rate: one over the feasible devices, if the true device is among them (device level); the true groups among the feasible groups (submission level).
  - 1/T at the submission level, where T = R + 40 with decoys and T = R without.
- **Lift.** Device level: accuracy over the random-assignment rate. Submission level: accuracy × T. Both with intervals.
- **Contribution over the baseline.** Vantage correct minus paired baseline correct, on the same rows, with a run-resampled interval.

At the device level only:

- **Calibrated confidence.** The softmax posterior of the device pick, with its temperature fitted on the other half of the runs (split by run-id parity). From it:
  - AUC for right against wrong, with Obuchowski's clustered variance;
  - precision in the top 1% and top 5% most confident decisions, with Wilson intervals;
  - the largest coverage whose precision exceeds 50%.
- **Outcome-shuffle control.** Correctness is permuted within each run and the confidence AUC recomputed. Permuting within a run keeps each run's success rate, so a small between-run association can survive the shuffle. Confidence AUCs within 0.03 of 0.5 are therefore not read as signal.

**Signal.** A cell shows signal if either:
- the adjusted device-accuracy interval lies above the random-assignment rate; or
- the finding is stable and the adjusted AUC interval lies above 0.5 by more than 0.03.

**Stability.** A cell's numbers are a finding only when it has at least 50 device-level successes and 50 failures. Otherwise the report gives the number of runs needed at the observed rate and does not treat the numbers as a finding.

**Effect of the decoy stream.** At R = 1 and 15, for each vantage and level: accuracy with decoys minus accuracy without, matched record by record on (run, transaction, server), with a 95% interval from resampling runs.

**Volume table.** L against devices and captures per day at D = 625.6 s.

## 6. Predictions

Development runs on this build were made before this section was written, to verify the pipeline:
- 6 runs of R = 1 with decoys to 40 in flight, and 4 runs of R = 4 with decoys to 100, against no-decoy runs at 40 and 100 in flight;
- one run of R = 15 with and without decoys;
- 2 runs of every cell in section 5.1.

They showed every vantage's device accuracy falling sharply with decoys, the validator included, and the validator close to the baseline with decoys (within about 2 points).

The pre-run checks were also run before this section was written. Check 4 failed marginally for one baseline feature, D's hold: AUC 0.488 [0.476, 0.4995], against 36 tests. The feature is produced by identical code for real and decoy traffic. The failure is reported as it stands; the check is not re-run with more runs.

Predictions R2 and R3 confirm development observations; they are not blind.

- **R1.** At R = 1 and at R = 15, every vantage's device-level decoy effect interval lies below zero.
- **R2.** For every vantage, the device-level decoy effect is smaller in size at R = 15 than at R = 1.
- **R3.** With decoys, the validator's device-level contribution over the baseline is below +5 points in every cell.
- **R4.** The gatekeeper's and the credential processor's device-level contribution is below +1 point in every cell.
- **R5.** Every vantage's adjusted device-accuracy interval lies above the random-assignment rate in every cell.
- **R6.** Sensitivity control: every vantage's device-accuracy interval lies above the random-assignment rate.

## 6a. Scoring on every record (first hops and credential processor)

Written after the sweep of section 5.1 and before the re-scoring it describes. The first scoring of the first hops and the credential processor used as rows only the records each server took part in, chosen from the simulator's truth. Neither vantage can identify those records: a registry record names F and I but no relay hop and no credential processor. A diagnostic on 10 runs at R = 1 with decoys showed the selection is what drove the first hops' submission-level advantage:

| Records | First hop | Baseline |
|---|---|---|
| The ~5% it relayed | 13.4% | 5.5% |
| The ~95% it did not relay | 4.9% | 5.5% |
| All records | 5.4% | 5.5% |

The content server's rows are legitimate (it submitted those records, and the record names it). So are the validator's and gatekeeper's (every record).

**Re-scoring.**
- **Rows.** Each first hop and each credential processor is scored on every real record in the scored window.
- **Which servers.** Four servers per run are compromised in turn, rotating with the run id: server (4 × run + i) mod pool, for i = 0 to 3. The pool is all 20 nodes for a first hop and the 17 non-gatekeepers for a credential processor.
- **Likelihoods.** Unchanged.
- **Traffic.** The same runs (run ids 0 to 199, the same traffic seeds) are re-simulated and re-scored for these vantages and the baseline. These records replace the earlier rows of the first hops and the credential processor.
- **The two first hops.** Scored on every record, the credential and content first hops are the same compromised server with the same knowledge, so their claims and accuracy are identical. They differ only in which records count as ones the server took part in: those whose credential it relayed, or those whose content it relayed.

**Claims.**
- A first hop claims a link when its top capture holds a packet it relayed.
- A credential processor claims a link when the evidence at its pick favours its own transactions over the baseline. That is a likelihood ratio above 1, which is an own-transaction share of the pick's likelihood above its prior of 1/17.
- The credential processor's rule was first set at an own share above 1/2. A single-run pipeline test showed that this can never fire, because the prior caps the share. The rule was changed to the likelihood ratio before any re-scoring run.

**Reported, at both levels.**
- Accuracy and contribution over the baseline on every record (the primary result for these vantages).
- The claim rate.
- Accuracy on claimed records, against the baseline's accuracy on the same records.
- Accuracy on the records the server took part in, labelled as not identifiable to the server.

**Predictions.**
- **S1.** Over every record, each first hop's submission-level contribution interval lies within ±1 point at every cell with decoys.
- **S2.** Over every record, the credential processor's device-level contribution lies within ±0.5 points in every cell.
- No direction is predicted for the precision of claims.

S1 confirms the diagnostic above; it is not blind.

## 6b. Gatekeeper departure bundling

Written after the sweeps above and before the bundling sweep.

**Mechanism.** Each gatekeeper's hold clock is unchanged. A posting the clock selects waits for the next boundary of a 30-second grid and departs with every posting selected since the previous boundary. Each gatekeeper has its own grid, with a random phase drawn on a separate random stream. So bundling on and off share every other random draw, and only the postings and what follows them move. Board postings are internal to the gatekeeper and are not on the observed wire. The relay-hop lottery is unchanged.

**Cells.** Real volume R = 1, 15 and 50 × decoy target 20, 40 and 60 in flight × bundling on and off: 18 cells, plus the sensitivity control. 200 runs per cell, run ids 0 to 199, recorded here before the first run of this sweep. Within one R, every cell carries the same real traffic. Bundling on and off at one (R, decoy target) carry identical traffic.

**Models.** An attacker knows the protocol, so cells with bundling are attacked with likelihood models built with bundling on. The first hops and the credential processor are scored on every record, as in section 6a.

**Reported.**
- The bundle-size distribution per gatekeeper over each cell's runs: mean, share of empty bundles, share of bundles of one, share of bundles with fewer than two, and share of postings that depart alone.
- Each vantage's accuracy in every cell.
- The paired effect of bundling: accuracy with bundling minus accuracy without, matched record by record, with a run-resampled interval.

**Development runs**, made before this section was written:
- One bundle-size measurement: 5 runs each at R = 1 with 10 to 40 decoys, and at R = 15 and R = 100 with 40 decoys. It showed about 2 postings per bundle at R = 1 with 40 decoys, and 40% of bundles with fewer than two.
- 8 paired runs at R = 1 with 40 decoys and at R = 15 with 20 decoys. They showed the passive observer's device accuracy changing by under 0.4 points with bundling, and the content server losing about 1 point.
- The pre-run checks were run with bundling on. Check 4 again fails marginally for the baseline's D hold, the same feature and seeds as in section 6, because bundling does not touch relay holds.

**Predictions** (B1 confirms the development runs):
- **B1.** The passive observer's device-level bundling effect lies within ±1 point in every cell.
- **B2.** No vantage's device-level bundling effect interval lies wholly below -3 points in any cell.
- **B3.** At each R, the share of bundles with fewer than two postings falls as the decoy target rises.

## 6c. Match board pushes

Written after the bundling sweep and before the board-push sweep.

**Mechanism.** In the sweeps above, a content server held on its node clock and then checked the boards on every tick of that clock. In this build a content server never queries a board:
- Each board pushes every match posted since its previous push to every content server, every 10 seconds.
- Each board pushes on its own schedule, with a random phase drawn on a separate random stream. So the push build shares every other random draw with the build before it, and the real and decoy traffic up to the content servers is identical.
- A push reaches a content server after the internal latency between the two nodes.
- A content server submits once its hold has released and pushes from two of the three boards have carried the match, whichever is later.
- Pushes go to every content server on a fixed schedule whatever they carry, and are internal to the board layer, so they are not on the observed wire.

The 10-second period matches the relay tick. The period, the per-board phase, and keeping pushes off the observed wire are this build's choices. The specification states only that the boards regularly push all new matches to all servers.

**Cells.** Bundling on, at real volume R = 1, 15 and 50 × decoy target 20, 40 and 60 in flight: 9 cells, plus the sensitivity control. 200 runs per cell, run ids 0 to 199, recorded here before the first run of this sweep.

**Models.** The likelihood models are rebuilt under the push build. The first hops and the credential processor are scored on every record, as in section 6a.

**Reported.**
- Each vantage's accuracy in every cell.
- The paired effect of board pushes: accuracy in the push build minus accuracy in the bundling sweep's bundling-on cell at the same R and decoy target, matched record by record on identical traffic, with a run-resampled interval.

**Development runs**, made before this section was written:
- The pre-run checks were run on the push build. Checks 1 to 3 and 5 to 7 pass. Check 4 fails marginally for the baseline's D hold, the same feature and seeds as before (AUC 0.488 [0.476, 0.500]), because pushes do not touch relay holds.
- 8 paired runs in each of the 9 cells. Every vantage's device-level push effect lay within ±1.4 points. The largest was the content server at R = 1 with 20 decoys, at -1.37 points.

**Predictions:**
- **P1.** The passive observer's device-level push effect lies within ±1 point in every cell.
- **P2.** No vantage's device-level push effect interval lies wholly outside ±3 points in any cell.
- **P3.** The content server's device-level push effect lies within ±2 points in every cell.

## 6d. Two-point gatekeeper hold and registry-level bundling

Written after the board-push sweep and before the sweeps of the two builds below.

**Builds.** Each build adds one mechanism to the one before it:

| Build | Adds | Records |
|---|---|---|
| push | the build of section 6c | `link_push` |
| twopoint | the two-point gatekeeper hold | `link_twopoint` |
| regbundle | registry-level pooled bundling, on top of twopoint | `link_regbundle` |

**Two-point gatekeeper hold.** A gatekeeper releases a packet at once with probability 0.6, or holds it for exactly 300 seconds with probability 0.4. The release does not wait for a tick of the gatekeeper's hold clock. Departure bundling then applies as before: the released posting waits for the next boundary of the gatekeeper's own 30-second grid. The draw comes from a separate random stream, and the relay-lottery draw it replaces is still consumed. So twopoint shares every other random draw with push.

**Registry-level pooled bundling.** A content server's confirmed submission waits for the next boundary of one schedule shared by every content server, with a phase drawn on a separate random stream, and departs with every submission confirmed since the previous boundary. The registry submissions are gossiped as before, so the observer sees them depart together at each boundary. regbundle shares every random draw with twopoint, so only the registry submissions move.

**Window size.** Measured before this section was written, over 20 runs per cell (run ids from 1,000 up, never used by a sweep), with the two-point hold, gatekeeper bundling and board pushes on:

| R | Decoys | Confirmed submissions per second | Per 120 s bundle: submissions | Per 120 s bundle: distinct transactions | Bundles with fewer than 2 transactions |
|---|---|---|---|---|---|
| 1 | 20 | 0.067 | 8.0 | 5.4 | 2.9% |
| 1 | 30 | 0.099 | 11.9 | 7.9 | 0.33% |
| 1 | 40 | 0.131 | 15.7 | 10.5 | 0.038% |
| 1 | 60 | 0.195 | 23.4 | 15.6 | under 0.001% |
| 15 | 40 | 0.177 | 21.2 | 14.2 | under 0.001% |
| 50 | 40 | 0.290 | 34.8 | 23.2 | under 0.001% |

- Confirmed submissions arrive in bursts: the gaps between them have a coefficient of variation of 1.4 to 1.6, above the 1.0 of a Poisson stream.
- A bundle holding only one transaction's two submissions mixes nothing, so the criterion counts distinct transactions.
- The window is the smallest multiple of 30 seconds that keeps bundles with fewer than two distinct transactions under 0.1% at R = 1 with the 40-decoy target, the criterion the specification uses for gatekeeper bundling. That is 120 seconds (90 seconds gives 0.29%).

**Rates.** Real and decoy rates stay those of the push build (R / D and decoys / D, with D = 625.6 s). The new mechanisms lengthen the end-to-end delay, so the number of transactions in flight in a cell rises in proportion; the decoy stream's rate is fixed, as the specification requires.

**Cells.** Bundling and board pushes on, at R = 1, 15 and 50 × decoy target 20, 40 and 60: 9 cells per build. The sensitivity control is run for regbundle only; with every hold off, the twopoint control is the push control. 200 runs per cell, run ids 0 to 199, recorded here before the first run of these sweeps. Models are rebuilt under each build. The first hops and the credential processor are scored on every record.

**Reported.**
- Each vantage's accuracy in every cell of each build, and the passive observer's accuracy minus the random rate.
- The paired effect of each mechanism on its own: twopoint minus push, and regbundle minus twopoint, matched record by record. regbundle minus push is reported as the combined effect.
- The registry bundle sizes, as in the table above, for every cell.
- The end-to-end delay with both mechanisms active, from a real capture to its registry finalization: mean, median and 95th percentile, with the stages that make it up, at R = 1, 15 and 50 with 40 decoys (`python -m sna latency`, 20 runs per cell on run ids from 3,000,000 up).
- Whether the end-to-end delay collapses onto a few values under the two-point hold: the share of transactions in the fullest 10-second bin and the number of occupied 10-second bins, for each build.

**Development runs**, made before this section was written:
- The pre-run checks were run on regbundle. Checks 1 to 3 and 5 to 9 pass. Check 4 fails marginally for the baseline's D hold, the same feature and seeds as before (AUC 0.488 [0.476, 0.500]).
- In isolation, the relay-lottery hold the gatekeeper used before has mean 106.2 s and coefficient of variation 0.84; the two-point hold has mean 119.8 s and coefficient of variation 1.23.
- Over 20 runs at R = 1 with 40 decoys, the fullest 10-second bin of the end-to-end delay held 2.7% of transactions under push and 2.5% under twopoint, with 118 and 128 bins occupied.
- 8 paired runs per cell for each build:
  - twopoint minus push: the observer's device effect ranged from -1.24 to -0.20 points;
  - regbundle minus twopoint: the observer's device effect ranged from -0.39 to +0.26 points, and the validator's from -2.48 to -0.27 points.

**Predictions:**
- **M1.** The two-point hold lowers the passive observer's device accuracy: its effect (twopoint minus push) is below 0 in every cell, and its interval lies wholly below 0 in at least 6 of the 9 cells.
- **M2.** The two-point hold's effect on the observer lies above -3 points in every cell.
- **M3.** Registry bundling's effect on the observer (regbundle minus twopoint) lies within ±1 point in every cell.
- **M4.** Registry bundling lowers the validator's device accuracy: its effect is below 0 in every cell.

## 6e. Gatekeeper occupancy and the registry bundling window

Written after the sweeps of section 6d and before the window sweep below.

**The two-point gatekeeper hold is dropped.** Section 6d found that it does not change the passive observer's accuracy as a multiple of the random rate, and that it adds about 13 seconds of latency. From this section on, the gatekeeper holds on the relay lottery again, as in section 6c.

**Gatekeeper occupancy**, measured directly at each active gatekeeper (`python -m sna gatekeeper`, push build, R = 1, 50 runs per decoy target on run ids from 4,000,000 up, never used by a sweep). This measurement was made before this section was written; it involves no attack and no prediction. It reports, per gatekeeper:
- the arrival rate and the mean hold;
- the number of packets held at once, sampled at evenly spaced instants;
- selections per tick of the gatekeeper's hold clock;
- postings per departure bundle for windows of 30 to 300 seconds, with the share of bundles holding fewer than two.

From it, the plan reports the decoy target that gives fewer than 0.1% of 30-second bundles below two postings, and the window that does so at 30, 40 and 50 decoys.

**Registry window sweep.** Four builds add registry-level pooled bundling to the push build, without the two-point hold, at windows of 60, 120, 240 and 480 seconds (builds reg60, reg120, reg240 and reg480). Each shares every random draw with push, so each window's effect is a paired difference against the push sweep on the same records. The default build is reg120.

- **Cells.** Bundling and board pushes on, at R = 1, 15 and 50 × decoy target 20, 40 and 60: 9 cells per window. 200 runs per cell, run ids 0 to 199, recorded here before the first run of this sweep. Models are rebuilt under each window. The first hops and the credential processor are scored on every record. The sensitivity control is not rerun: section 6d showed that with every hold off, a registry window alone rounds every record time to its schedule.
- **Reported.**
  - Each vantage's accuracy in every cell, the passive observer's accuracy as a multiple of the random rate, and the validator's contribution over the observer.
  - Each window's paired effect against push, for every vantage.
  - Registry bundle sizes for every window and cell, over the sweep's own runs.
  - The end-to-end delay for every window at 40 decoys, with its stages.
- **Rates.** Real and decoy rates stay those of the push build, as in section 6d.

**Development runs**, made before this section was written: 8 paired runs per cell for each window. The observer's mean device effect against push across the nine cells was +0.10 points at 60 seconds, -0.12 at 120, -0.37 at 240 and -1.35 at 480. The validator's was -0.20, -0.25, -0.78 and -1.89 points.

**Predictions:**
- **W1.** At 60 and 120 seconds, the observer's device-level effect against push lies within ±1 point in every cell.
- **W2.** At 480 seconds, the observer's device-level effect against push is below 0 in every cell.
- **W3.** The validator's device-level effect against push is more negative at 480 seconds than at 120 seconds in at least 7 of the 9 cells.
- **W4.** At 480 seconds, the observer's accuracy as a multiple of the random rate is below its value under push in at least 6 of the 9 cells.

## 7. Deliverables

- `README.md`
- `RESULTS.md`, with every finding, including nulls, failed predictions and failed checks
- `PAPER_TABLE.md`, one row per vantage
- the figures in `results/figures/`

## 8. Run count

200 runs per cell, run ids 0 to 199, for the 8 cells in section 5 (5 with decoys, 2 without, and the sensitivity control). Recorded before the first sweep run. Sections 6b to 6e record their own cells and run counts.

## 9. Amendment record

Sections 1, 3, 5.2 and 6 and check 2 were rewritten before any sweep of the record-to-device target. An earlier sweep scored a different link (registry record to credential transaction); none of its records are used here. The earlier text of this plan is in the repository history at commit 5bc4a08.

A second amendment followed a change to the decoy mechanism in the specification. Decoys became genuine transactions from registered identities, and the decoy stream a steady 40 in flight independent of real traffic. Sections 2 (Decoys), 4, 5.1, 5.2, 6 and 8 were rewritten before any sweep of this build. Sweeps of earlier builds are not used here; their text and results are in the repository history.

A third amendment followed a change to the content servers in the specification: the match boards push new matches to every content server, and a content server no longer checks the boards itself. Section 2 (Content servers), section 4 (checks 6 and 7) and section 6c were written before any sweep of this build. The bundling sweep's results are kept in `results/bundling/`.

A fourth amendment followed two additions to the specification: the two-point gatekeeper hold and registry-level pooled bundling. Section 4 (checks 8 and 9) and section 6d were written before any sweep of these builds. The board-push sweep's results are kept as `results/summary_push.json` and `results/tables_push.md`, with its run log and checks in `results/push/`.

A fifth amendment drops the two-point gatekeeper hold and sweeps the registry bundling window. Section 4 (check 8's scope) and section 6e were written before any sweep of these builds.

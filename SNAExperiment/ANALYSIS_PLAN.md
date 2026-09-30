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
- Each gatekeeper verifies, holds on its own dedicated hold clock, then posts to its board.

**Content servers**
- A content server holds on its node clock, then checks the boards on every tick of that clock.
- It submits to the registry once two boards carry a posting with a valid σ_C.
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
- A decoy source is modelled as indistinguishable from a device. It sends one decoy credential packet and two decoy content packets per capture, on the same schedule and through the same role rules as a device.
- The validator signs every approval identically and adds a plaintext real/dummy indicator.
- The credential processor sends a same-size placeholder in place of σ_C on a dummy.
- Each gatekeeper's σ_C check fails on the placeholder. The gatekeeper then posts a substitute value on the real hold-and-post schedule.
- A decoy never reaches quorum at a content server, so it never produces a registry submission.
- The decoy rate is (T − R) / D credential transactions per second, which is `dummy = max(0, TARGET − real)` in transactions in flight.

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
- Decoy sources' packets are candidates wherever a vantage cannot tell decoys apart.

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
| Credential processor | records whose credential it processed as C | mixture over its own transactions j: 1/17 × Σ_j w_kj real_j p(y given x_kj) plus the remaining weight × g(y). Here x_kj is transaction j's fan-out median minus s_k, and w_kj is the posterior that j is k's transaction |
| Content server | records it submitted (as F or I) | the joint density of y and x = its own content arrival − s_k |
| Validator | every record | its own replies are its candidates, each labelled with its device identity; density of u_r minus the reply send time. It knows which credentials are disposable, so decoys are not candidates |
| Gatekeeper | every record (all three gatekeepers see every transaction) | mixture over its own postings j: Σ_j w_kj real_j p(y given x_kj), where x_kj is posting j minus s_k. A decoy's substitute posting takes weight but never produces a record |

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

`python -m sna checks` runs these checks with background traffic on, at R = 8 and T = 40, over 12 seeded runs. Each outcome is reported.

1. **Padding classes**
   - Every credential, content, validator and fan-out leg lies in its class on the wire.
   - Every raw payload fits its class minimum. This includes the reply's one-byte indicator.
   - A Ring V signature made and verified with real keys is 64 bytes.
   - A padding-class scaling note lists the fan-out leg's raw size against the number of Ring V members. It is a size question and does not bear on decoys.
2. **Answer extraction.** The observer extracts exactly the true registry submissions, with none missing and none extra. Its device candidates hold every device and decoy first-hop packet and no background packet. The share of submission groups that hold a single capture is reported.
3. **Background independence.** Every vantage's and baseline's decisions are identical with background traffic on and off, on the same seed.
4. **Cannot tell decoys** (baseline, both first hops, content server)
   - Each feature the vantage observes is tested: sizes, holds, processing delays, the spread of a source's three first-hop sends, and the time since the source's previous capture.
   - The test is the AUC of that feature for real against decoy, with a run-clustered interval, Bonferroni-adjusted across every feature test.
   - Pass: every adjusted interval covers 0.5.
   - The content server is also tested on whether quorum forms within 30 minutes. The prediction is that it separates real from decoy perfectly after the timeout. This is reported as a scoped failure of the cannot-tell rule: it is too late for the vantage's own decision, and it is the reason the content server guesses only for items that reached quorum.
5. **Can tell decoys** (validator, credential processor, gatekeeper)
   - The indicator, its use at C, and the σ_C check agree with the truth for every transaction: quorum never forms for a decoy and always forms for a real transaction.
   - The gatekeeper's substitute posting keeps the real schedule: the AUC of arrival-to-posting for real against decoy covers 0.5.

## 5. Cells, runs and metrics

### 5.1 Cells

A cell is (R, T): R real transactions in flight and T total.

**No-decoy sweep (T = R).**
- R = 4, 8, 24, 40, 50, 100, 200, 500 for the baseline and the four vantages that cannot tell decoys.
- R = 1, 2, 3, 4, 8, 24, 40 as the low range for the three vantages that can.
- Every vantage is scored in every cell. For the can-tell vantages, any row above R = 40 is labelled an upper bound.

**Decoy sweep.**
- For each R in {1, 2, 3, 4, 8, 24, 40}, T runs through {4, 8, 24, 40, 50, 100, 200, 500} with T > R. That gives 46 cells.
- The decoy sweep's chance references are the random-assignment rates and, at the submission level, 1/T.
- For the can-tell vantages, a decoy cell's L counts decoys they remove, so their decoy rows are labelled upper bounds.

The two sweeps are reported as two separate, equally load-bearing results.

**Sensitivity control.** R = 40 with every hold off: device, relay, fan-out, gatekeeper and content server. It uses its own likelihood models, with 0.05 s bins.

**Traffic seeds.** A run's traffic seed depends on R and the run id only. So:
- every decoy cell carries, event for event, the real traffic of the no-decoy cell at the same R;
- every vantage reads the same run.

**Scored window.** Transactions captured in the scored window are scored. The window is 3 hours, extended to hold 200 real transactions on average: 200 × D / R, which is 34.7 hours at R = 1. Warm-up is 20 minutes and cool-down 40 minutes.

**Run count.** The run count per cell is set after the cost estimate (`python -m sna estimate`) and recorded in section 8 before the first sweep run.

Probe runs use run ids from 1,000,000 upward and are written to `results/probe/`. They are used only to measure cost and successes per run, and they are never reported as findings.

### 5.2 Metrics per cell and vantage

At each level (device primary, submission secondary):

- **Accuracy.** Per-decision accuracy with a 95% interval from resampling whole runs (2,000 replicates). A Bonferroni-adjusted interval is also computed across the 7 vantages × 2 tests in the cell.
- **Chance references.**
  - The random-assignment rate: one over the feasible devices, if the true device is among them (device level); the true groups among the feasible groups (submission level).
  - 1/L (= 1/T) at the submission level.
- **Lift.** Device level: accuracy over the random-assignment rate. Submission level: accuracy × L. Both with intervals.
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

**Lift trend from 40 to 500.** For each vantage on the no-decoy sweep, at each level, the slope of log lift against log L over L = 40, 50, 100, 200 and 500, with a 95% interval from resampling runs within each cell. It rises or falls if the interval excludes zero. Otherwise it holds flat.

**Volume table.** L against devices and captures per day at D = 625.6 s.

## 6. Predictions

Development runs of this attack were made before this section was written, to verify the pipeline and its speed:

- six runs at R = 40;
- one run each at R = 500, R = 1 with T = 500, R = 4 with T = 500, R = 40 with T = 500, and the sensitivity control.

They showed:
- every vantage's device accuracy above the random-assignment rate at R = 40;
- the first hops gaining several points at the submission level;
- the gatekeeper and credential processor close to the baseline;
- the validator unaffected by decoys (91% device accuracy at R = 1, T = 500).

Q1, Q2, Q3, Q4 and Q6 therefore confirm development observations; they are not blind predictions.

- **Q1.** On the no-decoy sweep, every vantage's device accuracy (the baseline's included) has its adjusted interval above the random-assignment rate at every L from 4 to 500.
- **Q2.** The gatekeeper's and the credential processor's device-level contribution is below +1 point at every L of 8 or more.
- **Q3.** Both first hops' submission-level contribution interval lies above zero at every L from 4 to 500.
- **Q4.** The validator's device accuracy at fixed R is identical at every T: it knows which credentials are disposable, so decoys never become its candidates.
- **Q5.** At fixed R, the baseline's device accuracy falls as T rises, because decoy packets are candidates.
- **Q6.** Sensitivity control: every vantage's device-accuracy interval lies above the random-assignment rate.
- **Q7.** The content server's device-level contribution interval lies above zero at L = 24 and 40.

No direction is predicted for the lift trend from 40 to 500.

## 7. Deliverables

- `README.md`
- `RESULTS.md`, with every finding, including nulls, failed predictions and failed checks
- `PAPER_TABLE.md`, one row per vantage
- the figures in `results/figures/`

## 8. Run count

To be set from the cost estimate for this attack (`python -m sna estimate`) and recorded here before the first sweep run.

## 9. Amendment record

Sections 1, 3, 5.2 and 6 and check 2 were rewritten before any sweep of the record-to-device target. An earlier sweep scored a different link (registry record to credential transaction); none of its records are used here. The earlier text of this plan is in the repository history at commit 5bc4a08.

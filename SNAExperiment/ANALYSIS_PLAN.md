# Analysis plan

This plan is fixed before the first sweep run. Every section below states what is run, how each number is computed, and what counts as a finding. If a result disagrees with a prediction, it is reported as a failed prediction. If a check fails, the failure is reported and the check stays as written.

## 1. Question

Semantic Non-Assembly claims that no single compromised component can link a piece of content to the credential transaction that produced it better than chance among the L transactions in flight.

This experiment tests that claim directly. Each vantage point holds:

- its real keys;
- its own exact event timing;
- a passive view of the sizes and timing of all network traffic.

The test is whether it can name the right transaction more often than 1/L.

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

Each vantage guesses for every item it holds. Decoys are included whenever it cannot tell them apart. Scoring counts real items only.

### 3.1 Answer lists

**Registry list.** Most vantages pick a registry submission on the wire. A passive observer finds a submission as a flood-publish burst: gossip-size frames that one node sends to nearly every peer within 2 ms. When several submissions leave one node on the same tick, the burst carries one frame per submission to every peer. The observer counts them as the smallest per-peer frame count. Both of a transaction's submissions (F's and I's) are right answers.

**Validator-reply list.** The content server picks a validator reply (CV-2) on the wire. The answer list is every relay-class message from the validator to a pool node, timed at arrival. Decoy replies are on the list. The right answer is the transaction's own reply.

### 3.2 Anchors

Each vantage is scored twice on the same run:

- with its own anchor (the vantage attack);
- with the paired baseline's anchor, which is the same anchoring event with the vantage's extra keys and knowledge removed. It uses only what the wire shows and guesses for every item, decoys included.

| Vantage | Rows (items it holds) | Vantage anchor | Paired baseline anchor | Answer list |
|---|---|---|---|---|
| Baseline | every validator reply on the wire | reply arrival at the credential processor | the same | registry |
| First hop, credential | credential packets it receives as A, decoys included | its own forward to B (own hold known) | the packet's arrival at A | registry |
| First hop, content | content packets it receives as D or G, decoys included | its own forward to E or H | the packet's arrival at D or G | registry |
| Credential processor | real transactions (reads the indicator) | the median of its own three fan-out sends | reply arrival at C (the nearest event a passive observer can attribute to C without searching the fan-out legs) | registry |
| Content server | items that reached quorum (a decoy never does) | quorum-detection tick and content arrival, with a flag for quorum present at the first check | content arrival | validator replies |
| Validator | real transactions (knows which credentials are disposable) | its reply send | its reply send (the same wire event) | registry |
| Gatekeeper | real transactions (σ_C check) | its own board posting time | its fan-out leg's arrival | registry |

For the baseline, both anchors are the same event, so its contribution is zero by construction. For the validator, the anchors coincide too, so its per-decision contribution is zero by construction. Its baseline also guesses for decoys, so the two can still differ under joint assignment.

### 3.3 Likelihoods and decisions

**Likelihoods.** Each vantage's likelihood is a histogram of (answer time − anchor time), with 0.5 s bins, built from Monte Carlo runs on seeds disjoint from the evaluation seeds. It is −inf outside the simulated support, so every candidate outside that band is excluded exactly.

The content server combines its two timing features as independent terms within its quorum class:

- quorum present at the first board check;
- quorum detected on a later tick.

Delays do not depend on volume, so one model set serves every cell.

**Per-decision attack (primary).** Each row picks its highest-scoring answer.

**Joint assignment (secondary).** One compromised server's rows are assigned one-to-one to answers, maximising the summed score over each row's 64 best candidates. Every server that can hold the role is compromised in turn. The joint assignment is solved per server.

## 4. Pre-run checks

`python -m sna checks` runs these checks with background traffic on, at R = 8 and T = 40, over 12 seeded runs. Each outcome is reported.

1. **Padding classes**
   - Every credential, content, validator and fan-out leg lies in its class on the wire.
   - Every raw payload fits its class minimum. This includes the reply's one-byte indicator.
   - A Ring V signature made and verified with real keys is 64 bytes.
   - A padding-class scaling note lists the fan-out leg's raw size against the number of Ring V members. It is a size question and does not bear on decoys.
2. **Answer extraction.** The observer extracts exactly the true registry submissions and validator replies, with none missing and none extra.
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
- The decoy sweep's chance level is 1/T.
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

- **Accuracy.** Per-decision accuracy with a 95% interval from resampling whole runs (2,000 replicates). A Bonferroni-adjusted interval is also computed across the 7 vantages × 2 tests in the cell.
- **Joint-assignment accuracy.**
- **Chance references.** 1/L (= 1/T), 1/R, and the random-assignment rate: the true answers among a row's feasible candidates divided by the feasible candidates, averaged.
- **Lift.** Accuracy × L, with its interval.
- **Contribution over the baseline.** Vantage correct minus paired baseline correct, on the same rows, with a run-resampled interval. It is computed for the per-decision and the joint attack.
- **Calibrated confidence.** The softmax posterior of the pick, with its temperature fitted on the other half of the runs (split by run-id parity). From it:
  - AUC for right against wrong, with Obuchowski's clustered variance;
  - precision in the top 1% and top 5% most confident decisions, with Wilson intervals;
  - the largest coverage whose precision exceeds 50%.
- **Outcome-shuffle control.** Correctness is permuted within each run. The confidence AUC must then cover 0.5.

**Signal.** A cell shows signal if either:
- the adjusted accuracy interval lies above 1/L; or
- the finding is stable and the adjusted AUC interval lies above 0.5.

**Stability.** A cell's numbers are a finding only when it has at least 50 successes and 50 failures. Otherwise the report gives the number of runs needed at the observed rate and does not treat the numbers as a finding.

**Lift trend from 40 to 500.** For each vantage on the no-decoy sweep, the slope of log lift against log L over L = 40, 50, 100, 200 and 500, with a 95% interval from resampling runs within each cell. It rises or falls if the interval excludes zero. Otherwise it holds flat.

**Volume table.** L against devices and captures per day at D = 625.6 s.

## 6. Predictions

Development runs were made before this plan, to verify the pipeline:

- single runs at R = 24 and R = 40;
- one run each of R = 1, 4, 40 and 500, and of the decoy cells R = 1, T = 500 and R = 4, T = 100.

They showed three things:
- the gatekeeper well above 1/L and above its baseline;
- the baseline above 1/L at R = 24 and 40;
- the content server's accuracy falling sharply when decoys are added.

A four-run trial of check 4 flagged one baseline feature: a processing delay produced by identical code for real and decoy traffic. With 12 runs it passed. The predictions below were written after seeing these runs, so P3, P5 and P6 are confirmations of development observations rather than blind predictions.

- **P1.** For every registry-list vantage, the per-decision accuracy at fixed R is identical at every T. Decoys create no registry submissions and leave the real traffic unchanged, so they add no candidates to a registry list. Under the joint assignment, decoy rows can change the result for the vantages that cannot tell.
- **P2.** At fixed R, the content server's accuracy falls as T rises, because decoy validator replies are genuine candidates on its list.
- **P3.** The gatekeeper's accuracy exceeds 1/L and its paired baseline at every R ≥ 4 on the no-decoy sweep.
- **P4.** The validator's per-decision contribution is zero in every cell.
- **P5.** On the no-decoy sweep, the baseline's accuracy exceeds 1/L at R = 24 and 40.
- **P6.** On the no-decoy sweep, the content server's contribution is positive at R = 24 and 40.
- **P7.** Neither first hop's contribution interval lies above zero at any R ≥ 4.
- **P8.** Sensitivity control: every vantage's accuracy interval lies above 1/L.
- **P9.** The outcome-shuffle AUC interval covers 0.5 in every stable cell.

No direction is predicted for the lift trend from 40 to 500.

## 7. Deliverables

- `README.md`
- `RESULTS.md`, with every finding, including nulls, failed predictions and failed checks
- `PAPER_TABLE.md`, one row per vantage
- the figures in `results/figures/`

## 8. Run count

To be filled in before the first sweep run, from the cost estimate.

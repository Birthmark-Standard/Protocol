# Analysis plan: null case, roles A, C, D, F, V and a gatekeeper, adversary confidence, scale

This plan is committed before the first run of this extension. Results that follow it are reported
as confirmatory. Anything added after the first run is labelled exploratory in `RESULTS.md`.

## 1. Question

Can one compromised element, holding its own keys, exact knowledge of its own events, and the
passive network view of the GPA experiment, link a transaction's content-side record to its
credential side better than chance? And when its guess is right, can it tell?

## 2. Setup

### 2.1 Rounds

| Round | Settings | Meaning |
|---|---|---|
| 1 | `role_rules="catalog"`, plain C signature, no gatekeeper exclusion, no gatekeeper hold | unmitigated design |
| 2 | `role_rules="insider_v2"`, ring signature, gatekeeper exclusion, 3-way fan-out | redesign |
| 3 | Round 2 plus the gatekeeper posting hold (`gk_hold="gatekeeper"`) | adopted design |

All other settings are the adopted GPA settings: node-wide relay clock, per-channel device phase,
F/I hold on each server's own clock, no CV-1/2 hold, 25 background clients per node, record type
read by the observer.

### 2.2 Load and L

- Interval between a device's captures: 20 minutes. Devices = 10 × L, where L is the workbook's
  Little's-law value (devices ÷ 20 × 2 minutes). L = 4, 8, 24, 40, 200, 1000 means 40, 80, 240,
  400, 2,000 and 10,000 devices.
- The chance baseline is 1/L with the workbook L, so every point stays comparable with Rounds 1 to 3.
- The volume table also reports captures per day (devices × 72) and the in-flight count implied by
  the simulator's measured capture-to-registry delay.

### 2.3 Runs

- One run simulates warm-up (20 min), a scored window of **3 hours**, and cool-down (30 min).
  Only transactions that start in the scored window are scored.
- **Common random numbers.** A run's traffic seed depends on (base seed, L, run id, pool size)
  only. Every scenario and every round reads the same traffic, so differences between scenarios,
  and between rounds, are paired. Each attack's own random choices (the random-assignment
  baseline) use a seed that also includes the scenario.
- **Every server is scored.** In each run, the attack is computed from the point of view of each
  server that can hold the role, in turn: every pool node for A, C, D, F; every validator for V;
  each of the three active gatekeepers for GK. One simulation therefore gives about 90 × L
  scored decisions per role.
- Confidence intervals resample whole runs (cluster bootstrap, 2,000 resamples), because
  decisions within one run share traffic.

## 3. Decisions and attacks

A **decision** is one guess: for one transaction the compromised server handled, which item in the
answer list belongs to the same transaction. Guesses are made jointly: for each server, one
one-to-one assignment over all its transactions in the run (optimal assignment maximising summed
log-likelihood, as in Rounds 1 to 3). The per-decision variant (each transaction's highest score,
chosen independently) is also reported. Joint is primary.

**Answer lists.**
- **Registry answer list** (A, C, D, V, GK, and N for those roles): the registry postings seen on
  the wire (F's and I's gossip origination). A guess is right if the chosen posting belongs to the
  same transaction.
- **Credential answer list** (F, and N for F): the validator replies (CV-2) seen arriving at C
  servers, as in Rounds 1 to 3.

**Likelihoods** are Monte Carlo densities from the shared simulator, built under the same round's
settings on seeds disjoint from the evaluation seeds. A role's model is fitted on the same
estimator the attack uses, so estimation error is inside the model.

**Principle for the new roles.** A role scores candidates from its latest exactly-known event on
the transaction's path to the registry. Everything after that event is independent lottery draws,
so earlier events add nothing once a later one is known.

| Scenario | Label the adversary holds | Anchor and variants | Answer list |
|---|---|---|---|
| **F** | content (ContentHash) | Rounds 2 and 3: *timing* (own detection tick and content arrival), *full* (plus the GK-leg search with quorum agreement), *legs* (the search alone). Round 1: *timing* and *full* (identity disclosure plus own GK leg when F is a gatekeeper). Primary: *full*. | credential |
| **C** | transaction (manufacturer via key_ref) | quorum computed from its own GK legs (unchanged from Rounds 1 to 3) | registry |
| **V** | device identity | *timing*: its CV-2 send time. *full*: C's GK legs found on the wire after the CV-2 arrival at C (best leg per active gatekeeper by hop likelihood), giving an estimated quorum. Primary: *full*. | registry |
| **GK** | transaction (manufacturer known, device not) | *timing*: its own board-post time. *full*: its own post plus the other two gatekeepers' legs from C found on the wire, giving an estimated quorum (other gatekeepers' holds are unknown, so their expected hold is added and the model absorbs the error). Primary: *full*. | registry |
| **A** | network address (the simulator's device id) | its forward time (Cred-2 send) | registry |
| **D** | network address (the simulator's device id) | its forward time (ContA-2 send) | registry |
| **N** | none | see 3.1 | same as the role compared |

A first hop is assumed to know which kind of packet it holds, credential or content: in the
simulator's construction it learns the unpadded length when it removes padding (credential about
202 B, content about 114 B inside the transit layer). This is revisited after the results.

### 3.1 Null case N (no compromised element)

**N(a), paired.** For each role, N makes the same decisions on the same transactions with the same
answer list, using only what the outside observer sees. It is generous to the observer: it is told
which transaction each row is.
- Registry answer list: the published GPA sequencing likelihood, anchored at that transaction's
  CV-2 arrival at C.
- Credential answer list (F): the likelihood of the content arrival time at F alone (no detection
  tick, which is internal to F).

The **insider's contribution** is role minus N(a): the paired difference in accuracy per
transaction, with a cluster-bootstrap CI.

**N(b), published.** The two published GPA attacks run unchanged on the same traffic: the main
attack (chain reconstruction, then origin-time grouping) and the sequencing attack. Each is scored
per transaction and compared with each role on the same transactions. The main attack's dense
assignment does not fit in memory above L = 40, so it runs at L ≤ 40 only; there it was at chance in
the published sweep.

## 4. Metrics

Per scenario, variant, round and L:

1. **Accuracy** with cluster-bootstrap 95% CI, against 1/L and against random assignment over the
   same feasible pairs. **Top-3 accuracy** (the true item ranks in the top 3 of the row's scores).
   **Lift** = accuracy × L (1.0 = chance).
2. **Confidence** per decision, two measures:
   - *gap*: top score minus runner-up (as in Rounds 1 to 3);
   - *calibrated posterior*: the softmax over the row's candidate scores at temperature T, for
     the chosen candidate. T is fitted by minimising the negative log-likelihood of the true
     candidate on held-out runs: two folds by run-id parity, fitted on one fold and applied to the
     other (no leakage). Scores stored per row: the top 32 exactly, the rest as a 64-bin histogram
     of distance from the top score.
3. Confidence given correct vs given incorrect: ECDFs, medians, IQR.
4. **AUC** of confidence as a predictor of correctness, cluster-bootstrap 95% CI.
5. **Precision at coverage** q ∈ {1, 5, 10, 25, 50, 100}%: the most confident q% of decisions,
   with Wilson 95% CIs.
6. **Calibration**: reliability diagram (15 equal-width bins) and expected calibration error (ECE),
   for the calibrated posterior.
7. **Actionable yield**: the largest coverage at which precision is at least 50%, and the best
   precision at coverage of at least 1%.

**Sample size rule for AUC.** An AUC is reported as a finding only with at least 50 correct and
50 incorrect decisions. Otherwise the table shows the number of successes and the runs needed to
reach 50.

## 5. What counts as a signal

A scenario shows a **signal** at a (round, L) point if either:
- its accuracy CI lies above 1/L, or
- its AUC CI lies above 0.5.

The insider shows a **contribution beyond the outside observer** if the paired role − N(a) CI lies
above zero.

**Multiple comparisons.** Each (round, L) point is one family: 7 scenarios (N and six roles, primary
variant each) × 2 tests = 14. Signal claims use Bonferroni-adjusted intervals (99.64%); 95%
intervals are reported alongside for description. Secondary analyses (other variants, joint vs
per-decision, validator shares, pool size, N(b)) are exploratory and labelled so.

## 6. Hypotheses (stated in advance)

| Scenario | Expectation |
|---|---|
| N | below 1/L at every point; its sequencing accuracy matches the published GPA result at the same L |
| F | Round 1: above 1/L (known signal, 85.6% at L = 4). Round 3: below 1/L (6.3% at L = 8, 1.9% at L = 24, 1.2% at L = 40) |
| C | below 1/L |
| V | at most C's result (V − C ≤ 0). If V beats C, suspect a modelling error and investigate before reporting |
| A | null: no signal, A − N(a) CI includes 0 (long, noisy chain) |
| D | null, with a shorter chain than A (D ≥ A) |
| GK | no stated direction (unlike C, it knows its own hold outcome) |

**Scale (40 → 200 → 1000).** For each scenario, lift is classified as:
- **worsening** if the lift CI at 200 or 1000 lies entirely above the lift CI at 40;
- **improving** if the lift CI at 1000 lies entirely below the lift CI at 40;
- **flat** otherwise.

A worsening scenario gets a follow-up point at the geometric midpoint of the two bracketing L
values (for example L = 90 between 40 and 200, L = 450 between 200 and 1000).

## 7. Controls (must pass before results count)

- **Positive:** Round 3 with the lottery off and the gatekeeper hold off, L = 4, every role.
  Passes if F's and C's accuracy is at least 90% and every role's AUC CI (where computable)
  lies above 0.5.
- **Negative, shuffled labels:** for every cell, the true transaction of each decision is permuted
  among the same server's decisions in the same run, and every metric is recomputed. Passes if
  the accuracy CI contains the random-assignment rate and the AUC CI contains 0.5.
- **Known signal:** Round 1, F at L = 4. Passes if accuracy and AUC both show a signal.

## 8. Run sizes

Decisions per cell: the stricter of
- Wilson half-width at the 1/L baseline ≤ 1 percentage point, and
- half-width ≤ 0.25/L (lift measured to ± 0.25).

| L | 4 | 8 | 24 | 40 | 200 | 1000 |
|---|---|---|---|---|---|---|
| decisions needed | 7,203 | 4,202 | 1,537 | 2,400 | 12,230 | 61,400 |
| decisions per run per role (about) | 360 | 720 | 2,160 | 3,600 | 18,000 | 90,000 |

Runs per cell: the larger of 20 and the runs needed for the table above (so 20 at every L up to 200).
At L = 1000, at least 10 runs and a target of 20, fixed by compute cost and not by results; the count
used is reported.

## 9. Grid

**Tier 1 (L = 4):** Round 3: N, A, C, D, F, V, GK. Round 2: V, GK (and N). Round 1: F (and N).
Controls: positive, negative (all cells), Round 1 F.

**Tier 2 (Round 3):** N, A, C, D, F, V, GK at L ∈ {4, 8, 24, 40, 200, 1000}; F at Round 1 at L ∈ {40, 200,
1000} for comparison with the unmitigated design.

**Exploratory:**
- V at validator shares s ∈ {1.0, 0.5, 0.1} (validator 0 compromised; registry records carry no
  manufacturer, so the answer list is still every posting), Round 3, L ∈ {40, 200}.
- Pool size 20 vs 40 nodes at the same per-node load, Round 3: 400 devices on 20 nodes vs 800 on
  40 (L = 40 vs 80).

## 10. Regression and currency (done before this plan's runs)

- Round 1 F full: 85.6% at L = 4, 32.6% at L = 40. Round 3 F full: 6.3% at L = 8, 1.9% at L = 24,
  1.2% at L = 40. Reproduced with the original code and seeds (`python -m harness regress`).
- The simulator's wire trace is unchanged under the current per-leg specification's raw sizes
  (`GPAExperiment/tests/test_spec_currency.py`).

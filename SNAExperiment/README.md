# SNA Experiment: InternalCompromiseRun

InternalCompromiseRun tests one property of the Birthmark Protocol: whether any single compromised component can take a public registry record and name the device that produced it more often than a passive network observer can.

A record reaching the registry should not be traceable to its device. The experiment simulates the protocol's full message flow, with real and decoy traffic, and attacks it from each internal vantage point. Each attacker has:
- every key its component holds;
- its component's exact event timing;
- a passive view of the sizes and timing of all traffic on every link.

Each attacker is compared with chance and with a passive observer on the same records.

- `RESULTS.md` has every finding.
- `PAPER_TABLE.md` has the headline tables.
- `results/TABLES.md` has the full generated tables.

## What is measured

**Primary measure: how often the attacker names the right device.** Every vantage starts from a registry record and names one device. A decision is right when the named device produced the record. This is the correlation an attacker achieves between device submissions and the posted record.

**Second measure: the attacker's confidence that a match is right.** Each vantage's match score is turned into a calibrated probability that the match is right. It is fitted on half the runs and applied to the other half (cross-fitted by run parity). This answers how sure an attacker can be about any single match it attempts.

Accuracy is read against three references:

| Reference | Meaning |
|---|---|
| Chance, feasible set | A uniform guess among the devices whose submissions could have produced the record, given the protocol's timing. |
| One in N | A uniform guess among every registered device: real devices and decoy identities. |
| Passive observer | An attacker with no keys and no internal timing, who sees only sizes and timing on every link. A component's **lead** is its accuracy minus the observer's on the same records. |

## Vantages

| Vantage | Holds | Knows exactly |
|---|---|---|
| Passive observer | nothing | sizes and timing on every link |
| First hop, credential (A) | relay transit key | the device's network address and packet arrival; its own hold and forward times |
| First hop, content (D or G) | relay transit key | the same, for one content copy |
| Credential processor (C) | transit and ring-signing keys | packet hash, key reference, its own fan-out sends, the validator's reply |
| Validator (V) | token-decryption and signing keys | device identity, request arrival, reply moment |
| Gatekeeper | transit and countersignature keys | packet hash, sender's address, its own arrival, hold release and posting |
| Content server (F or I) | transit and registry-signing keys | content hash, content arrival, when the board pushes showed quorum, its own submission |

- **First hops and the credential processor** cannot tell which records they took part in. They are therefore scored on every record. Four servers per run are compromised in turn, rotating with the run id.
- **The content server** is scored on the records it submitted, which it can identify because the record names it.
- **The gatekeeper** is scored once for each of the three active gatekeepers.

## The protocol as simulated

**Pool and roles**
- 20 submission servers, one validator, and three active gatekeepers per run.
- Each transaction uses nine distinct nodes: a credential path (A → B → C) and two content paths (D → E → F, G → H → I) that share no node.
- C, F and I are never active gatekeepers.

**Padding**
- Every transit leg is padded to a size drawn uniformly from 420 to 460 bytes.
- The gatekeeper fan-out uses 820 to 860 bytes.
- A 22-byte TLS 1.3 record overhead, measured on real sessions, is added on the wire.
- Registry submissions travel as gossipsub frames.

**Decoys**
- A decoy is a genuine transaction from a registered identity held by the decoy infrastructure. It is approved, fanned out, posted and finalized exactly as a real transaction, and it produces a permanent registry record.
- 60 decoy transactions are in flight at every level of real traffic. The specification sets the target at 60 ± 10; the simulation holds it at the centre of that range.
- Each decoy identity captures at a device's rate (every 20 minutes on average), so 69 decoy identities share the stream.

**Board and registry**
- Each match board pushes its new matches to every content server every 10 seconds, on its own schedule.
- A content server confirms a transaction once its own pre-match hold has released and two boards' pushes carry the match. It drops the transaction after 30 minutes without quorum.
- The registry finalizes a record when both content servers' submissions have arrived.

**Simulation scope**
- The simulation contains protocol traffic only.
- Network latency is fixed per pair of hosts within a run, with per-packet jitter. There is no queueing.

## Hold timing

Every hold uses the same lottery shape:
- a 10-second tick on the holding node's own clock;
- geometric release at a fixed probability per tick;
- unconditional release at three times the hold's mean.

The release probability is set so that, with the cap, the hold averages its target mean.

**Departure bundling.** After the gatekeeper's own hold, a posting draws for a place in each 30-second bundle of that gatekeeper's grid. Its chance is 25% at each boundary, and it boards unconditionally at the 12th boundary.

**Registry bundling.** Confirmed submissions from every content server leave together on one shared 120-second schedule.

Measured values come from 10 runs at R = 20 (`results/timing_check.json`).

| Stage | Target mean (spec) | Tick | Release probability per tick | Cap | Measured mean | Measured std dev |
|---|---|---|---|---|---|---|
| Relay hops (A, B, D, E, G, H), every path | 120 s | 10 s | 7.52% | 360 s | 119.7 s | 103.0 s |
| Device's credential-channel hold | 120 s | 10 s | 7.52% | 360 s | 118.8 s | 103.1 s |
| Device's content-channel holds (both) | 240 s | 10 s | 3.84% | 720 s | 237.8 s | 205.4 s |
| C's hold before sending CV-1 | 30 s | 10 s | 26.86% | 90 s | 30.3 s | 25.3 s |
| V's hold before sending CV-2 | 30 s | 10 s | 26.86% | 90 s | 30.2 s | 25.3 s |
| C's fan-out to each gatekeeper (independent per leg) | 60 s | 10 s | 14.46% | 180 s | 59.6 s | 51.2 s |
| Gatekeeper's own hold | 30 s | 10 s | 26.86% | 90 s | 30.4 s | 25.3 s |
| Departure bundle inclusion lottery | 101 s | 30 s | 25% | 12 boundaries | 101.0 s | 90.9 s |
| F/I's pre-match hold | 240 s | 10 s | 3.84% | 720 s | 240.8 s | 206.9 s |
| Post-match lottery | 30 s | 10 s | 26.86% | 90 s | 30.1 s | 25.3 s |
| Registry bundle wait | 60 s | shared 120 s schedule | not applicable | 120 s | 60.1 s | 34.7 s |

Mean capture to finalization is 1,033.8 seconds, with a standard deviation of 270.6 seconds.

Departure bundles at one gatekeeper hold 2.33 postings on average. 32.4% of them hold fewer than two, and 10.0% are empty.

## The attack

- **Records.** Each record is a registry entry whose two submissions (F's and I's) a passive observer finds in the gossip traffic. The record names both servers, so its two submissions are paired and timed at their midpoint.
- **Candidates.** The candidates are device submissions on the wire: each source's first-hop packets, grouped into captures. Decoy identities' packets are included for every vantage, because no vantage can tell them apart.
- **Scoring.** Each vantage scores every candidate by the likelihood of the record time given that candidate. The likelihoods are built by Monte Carlo simulation of the protocol on seeds separate from every scored run. Each vantage's likelihood adds its own exact knowledge to the observer's.
- **Decision.** For each record, a vantage names the device with the highest summed posterior.
- **Pairing.** Every vantage is paired with the passive observer on the same records.

## The claim criterion

In a cell, the claim holds when both conditions are met for every vantage:

1. **Top 1% precision.** Take the 1% of the vantage's matches that it is most confident in. The upper bound of the 95% interval on the share of them that are right must be below 50%.
2. **Coverage.** Fewer than 0.1% of the vantage's matches may fall in a most-confident set whose matches are right more than half the time.

A vantage that passes cannot select any meaningful set of its own matches and be right about most of them.

## Builds and cells

**InternalCompromiseRun** (build `internal_compromise`) is the protocol with every hold at the timing above.

Each other build changes one thing and is paired against InternalCompromiseRun record by record. Every build carries the same traffic in the same cell and run.

| Build | Change |
|---|---|
| `internal_compromise` | none |
| `no_vc_holds` | C's and V's holds removed |
| `no_inclusion_lottery` | every ready posting departs at the next 30-second boundary |
| `no_post_match_lottery` | post-match lottery removed |
| `no_registry_bundling` | each confirmed submission leaves at once |
| `no_role_aware_holds` | device content channels and F/I pre-match hold at 120 s, like every other stage |
| `no_mechanisms` | all five of the above removed together |
| `relay_180s` | relay hops at a 180 s mean |
| `role_aware_360s` | device content channels and F/I pre-match hold at a 360 s mean |
| `gatekeeper_120s` | gatekeeper hold at a 120 s mean |

**Cells**
- Real volume is R = 1, 20 and 100 transactions in flight, each with 60 decoy transactions in flight.
- Rates are R / D and 60 / D. D = 1,036.6 seconds is the mean capture-to-finalization time measured under InternalCompromiseRun (`results/calibration.json`).
- R = 1, 20 and 100 correspond to 1, 23 and 116 real devices; with the decoy identities, 70, 92 and 185 registered devices.

**Runs**
- 200 runs per cell, run ids 0 to 199, for every build.
- A run's traffic depends only on its real volume and run id.
- The scored window is 3 hours. At R = 1 it is extended to hold 200 real transactions per run on average.
- Every cell of every build had at least 50 right and 50 wrong decisions at the device level for every vantage.
- Latency and F/I pair timing use 20 further runs per cell, on run ids no scored run uses.

## Reproducing the run

Requires Python 3.10 or later. Run from this directory.

```
pip install -r requirements.txt
python -m sna reproduce
```

On Windows, use `py -m pip install -r requirements.txt` and `py -m sna reproduce`.

**What `reproduce` does**
- It runs the whole experiment in order:
  1. calibration;
  2. the hold-timing measurement;
  3. every build's 200 runs per cell;
  4. every build's analysis;
  5. latency;
  6. F/I pair timing;
  7. `results/TABLES.md` and the figures.
- It took 116 minutes on 16 worker processes.
- It is resumable: an interrupted run loses at most the runs in flight, and rerunning the same command continues.
- Results depend only on the cell and run id, never on the worker count or the order runs finish in.

**Reproduction across platforms**
- The committed results were produced on Windows.
- A rerun of the `internal_compromise` build on Linux matched them in all but 3 of 5,493,945 decisions, each differing by one correct decision at R = 100.
- The difference comes from floating-point ties breaking differently between platforms. No reported figure changes at the precision shown.

**Smoke test.** `python -m sna reproduce --runs 2 --out results/quick` runs every step on two runs per cell.

| Command | What it does |
|---|---|
| `reproduce` | the whole experiment, as above |
| `run --build <name>` | one build's runs |
| `analyze --build <name>` | one build's summary and tables from its records |
| `tables` | every build's CSV and tables, `TABLES.md` and the figures, from the summaries |
| `latency` | capture-to-finalization time under every build (`results/latency.json`) |
| `pairs` | how often a record's two registry submissions leave together (`results/pair_gaps.json`) |
| `timing` | every stage's simulated hold and the departure bundle sizes (`results/timing_check.json`) |

Fast tests: `python -m pytest tests -q`.

## Contents

| Path | Contents |
|---|---|
| `README.md` | this description |
| `RESULTS.md` | every finding |
| `PAPER_TABLE.md` | headline tables |
| `results/TABLES.md` | full generated tables |
| `results/summary_<build>.json`, `.csv` | every metric for every vantage and cell under one build |
| `results/tables_<build>.md` | one build's tables, with its paired effects against InternalCompromiseRun |
| `results/calibration.json` | the end-to-end delay D |
| `results/cells.json` | the cells and their scored windows |
| `results/timing_check.json` | every stage's simulated hold and the departure bundle sizes |
| `results/latency.json` | capture-to-finalization time by build and stage |
| `results/pair_gaps.json` | F and I submission timing |
| `results/figures/device_named.png` | how often each vantage names the device, against chance |
| `results/figures/confidence_reliability.png` | each vantage's confidence against how often it is right |
| `results/figures/latency_by_build.png` | capture-to-finalization time under each build |
| `sna/params.py` | every numeric input |
| `sna/lottery.py` | the hold lottery and the likelihood densities |
| `sna/sim.py` | the simulator |
| `sna/attacks.py` | record and candidate extraction, likelihood models, scoring of every vantage |
| `sna/analyze.py` | metrics and intervals |
| `sna/experiment.py` | builds, cells, seeds, calibration, the run worker, latency, pair timing and hold timing |
| `sna/report.py` | summaries, tables and figures |
| `sna/runner.py` | resumable parallel execution |
| `tests/` | fast tests |

### Fields in the summaries

| Field | Meaning |
|---|---|
| `dev_accuracy`, `dev_ci_lo`, `dev_ci_hi` | share of records whose device the vantage names, with its 95% interval |
| `dev_random` | chance of a uniform guess among the feasible devices |
| `dev_lift_random` | `dev_accuracy` over `dev_random` |
| `dev_contribution` | lead over the passive observer on the same records, with `_lo` and `_hi` |
| `sub_*` | the same at the submission level: the named capture is the record's own |
| `conf_mean`, `conf_p50`, `conf_p90`, `conf_p99`, `conf_max` | the vantage's calibrated confidence in its matches |
| `reliability`, `calibration_error` | confidence against outcome in ten equal groups, and the mean absolute gap |
| `p_at_1`, `p_at_5`, `p_at_10`, `p_at_25` | share right among the most confident 1%, 5%, 10% and 25% of matches, with Wilson intervals |
| `coverage_p50`, `count_p50` | the largest most-confident set whose matches are right more than half the time, as a share and a count of decisions |
| `auc`, `shuffle_auc` | how well confidence separates right from wrong matches, and the same with outcomes permuted within each run |
| `stable` | at least 50 right and 50 wrong decisions at the device level |
| `bundle_*` | hold releases per 30-second window at one gatekeeper (the departure bundle sizes are in `timing_check.json`) |
| `paired_effects` | each vantage's accuracy under the build minus under InternalCompromiseRun, matched record by record |

Intervals on accuracy resample whole runs (cluster bootstrap, 2,000 resamples). AUC intervals use the clustered-data variance of Obuchowski (1997).

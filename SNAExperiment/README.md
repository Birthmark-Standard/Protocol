# SNA Experiment

This experiment tests the Semantic Non-Assembly property of the Birthmark Protocol. The question is whether one compromised component can take a public registry record and name the device that produced it more often than a passive network observer can.

The experiment simulates the protocol's full message flow, with real and decoy traffic. It attacks every record from each internal vantage, with every node of the pool compromised in turn.

- `RESULTS.md` has every finding.
- `results/PAPER_TABLE.md` has the headline tables.
- `results/TABLES.md` has the full generated tables.
- `PREDICTIONS.md` has the predictions written before the run.

## What is measured

**Device named.** Every vantage starts from a registry record and names one device. A decision is right when the named device produced the record. This is the primary measure.

**Calibrated confidence.** Each vantage's match score is turned into a probability that the match is right. The fit uses half the runs and is applied to the other half, split by run parity.

Accuracy is read against two references:

| Reference | Meaning |
|---|---|
| Chance, feasible set | A uniform guess among the devices whose packets could have produced the record, given the protocol's timing. Multiple of chance is accuracy divided by this rate. |
| Passive observer | An attacker with no keys and no internal timing. A vantage's **lead** is its accuracy minus the observer's on the same records. |

## Vantages

There are six component vantages, the passive observer, and the combined view of one node.

| Vantage | Holds | Knows exactly |
|---|---|---|
| Passive observer | nothing | the posted record time and each device packet's departure |
| First hop, credential (A) | relay transit key | its own hold, on the device packets it relayed |
| First hop, content (D or G) | relay transit key | its own hold, on the device packets it relayed |
| Credential processor (C) | transit and ring-signing keys | the median of its own three fan-out sends, over its own transactions, with a prior of 1/17 that it was the record's C |
| Validator (V) | token-decryption and signing keys | its own reply times, which name the device |
| Gatekeeper | transit and countersignature keys | its own postings |
| Content server (F or I) | transit and registry-signing keys | its content arrival, on the records it submitted |
| Combined view of one node | every key of every role the node held | every entry above for each role the node held |

"Knows exactly" lists what each likelihood uses. Every vantage also sees the posted record time and the device packets on the wire. Other links carry legs padded to one size class or gossip frames of one constant size. No likelihood uses them.

- **Every node is compromised in turn.** One run scores every node as the compromised one, on every record.
- **First hops** cannot tell which records they took part in, so they are scored on every record. A first relay cannot tell whether it relays a credential or a content packet, so one first-relay model serves A, D and G. The two first-hop rows differ only in which records count as ones the node took part in.
- **The credential processor** is scored on every record, as every node outside the active gatekeeper set.
- **The content server** is scored on the records it submitted, which it identifies by the content hash it submitted.
- **The gatekeeper** is scored as each of the three active gatekeepers.
- **The combined view** combines a node's roles as likelihood ratios against the passive observer. A second relay holds no evidence in this framework. Its decisions are classed by the roles the node held in the record's own transaction. A class is **identifiable** when it includes a destination role (C, F or I), because the node reads the plaintext hash there and can select those records. Every other class is **oracle-conditioned**: the node cannot select those records, so the row is not an attack.
- **No coincident role.** For each node vantage, the rows on the records in which the node held at most one role are reported on their own. They are the comparison for the single-role vantages.

## The protocol as simulated

**Pool and roles**
- 20 Registry Nodes serve as submission servers. There is one validator, and three nodes are active gatekeepers in each run.
- A transaction has a credential path (A → B → C) and two content paths (D → E → F and G → H → I).
- C, F and I are distinct and never active gatekeepers.
- The relays are drawn under the routing design's guarantees only. A, D and G are pairwise distinct, and each differs from its own path's destination. B, E and H each differ from their own path's first relay and destination. Every other coincidence is allowed, so one node can hold roles on two paths.

**Padding**
- Every transit leg is padded to a size drawn uniformly from 420 to 460 bytes.
- The gatekeeper fan-out uses 820 to 860 bytes.
- A 22-byte TLS 1.3 record overhead, measured on real sessions, is added on the wire.
- Registry submissions are not transit legs. They travel as gossipsub frames of a constant 284 bytes on the wire.

**Decoys**
- A decoy is a genuine transaction from a registered identity held by the decoy infrastructure. It is approved, fanned out, posted and finalized exactly as a real transaction, and it produces a permanent registry record.
- 100 decoy transactions are in flight at every level of real traffic.
- Each decoy identity captures at a device's rate, every 20 minutes on average.

**Board and registry**
- Each match board pushes its new matches to every content server every 10 seconds, on its own schedule.
- A content server confirms a transaction once its own pre-match hold has released and two boards' pushes carry the match. It drops the transaction after 30 minutes without quorum.
- The registry merges F's and I's submissions into one record at intake, once both have reached every Registry Node.
- The registry posts merged records on its own 120-second schedule. The posted time is the record time. The record names neither F nor I.
- A passive observer sees the submissions' gossip frames but cannot tell which record they belong to.

**Simulation scope**
- The simulation contains protocol traffic only.
- Network latency is fixed per pair of hosts within a run, with per-packet jitter. There is no queueing.
- Processing before each send is uniform: 0.5 to 3 ms per node, 5 to 50 ms at the validator, 1 to 10 ms at a gatekeeper, and 5 to 50 ms for each gossip validation.

## Hold timing

Every hold is a geometric lottery on a 10-second tick, released unconditionally at three times its own mean. Each stage's release probability is set so the stage hits its target mean.

A relay picks its hold from its hop position only. A first relay re-encrypts the routing code with the payload, and a second relay forwards the payload alone. A relay cannot tell whether a packet is on the credential path or a content path. The two relay holds add to a mean of 360 s along every path, with a standard deviation of 263.7 s before network time.

Each hold releases on one of three kinds of clock:
- **The node's own clock:** relays, C, and F's and I's pre-match holds.
- **The validator's own clock.**
- **A separate gatekeeper hold clock:** a gatekeeper's own hold.

The device's channels and the post-match lottery use a fresh random phase for each packet.

**Serialized fan-out.** From C's receipt of CV-2, the transaction's three gatekeeper legs share one draw per tick of C's node clock. Each successful draw sends the next leg, in a random order. The next draw starts at the following tick, so no two legs leave on the same tick.

**Departure bundling.** After the gatekeeper's own hold, a posting draws for a place in each 30-second bundle of that gatekeeper's grid. It has a 25% chance at each boundary and boards unconditionally at the 12th.

**Registry bundling.** Confirmed submissions from every content server leave together on one shared 120-second schedule.

**Registry posting.** The registry posts each merged record at the next boundary of its own 120-second schedule. Both submissions reach the registry just after a boundary of the registry bundle schedule, which has the same period. Within a run, the posting wait is one fixed offset between the two schedules' phases.

| Stage | Target mean | Tick | Release probability per tick | Cap |
|---|---|---|---|---|
| First relay hop (A, D, G), every path | 60 s | 10 s | 14.46% | 180 s |
| Second relay hop (B, E, H), every path | 300 s | 10 s | 3.08% | 900 s |
| Device's credential-channel hold | 120 s | 10 s | 7.52% | 360 s |
| Device's content-channel holds, each drawn separately | 240 s | 10 s | 3.84% | 720 s |
| C's hold before sending CV-1 | 30 s | 10 s | 26.86% | 90 s |
| V's hold before sending CV-2 | 30 s | 10 s | 26.86% | 90 s |
| C's serialized fan-out, per draw | 20 s | 10 s | 37.65% | 60 s per draw |
| Gatekeeper's own hold | 30 s | 10 s | 26.86% | 90 s |
| Departure bundle inclusion lottery | 25% per boundary | 30 s | 25% | 12 boundaries |
| F's and I's pre-match hold | 120 s | 10 s | 7.52% | 360 s |
| Post-match lottery | 30 s | 10 s | 26.86% | 90 s |
| Registry bundle wait | uniform | shared 120 s schedule | not applicable | 120 s |
| Registry posting wait | one offset per run | registry's 120 s schedule | not applicable | 120 s |

The measured mean, standard deviation and maximum of every stage are in `results/timing.json` and `results/TABLES.md`.

## The attack

- **Records.** Each record is a posted registry entry. Its record time is the posted time.
- **Candidates.** Every first-hop packet from a device is a candidate on its own. Decoy identities' packets are included for every vantage, because no vantage can tell them apart.
- **Scoring.** Each vantage scores every candidate by the likelihood of the record time given that candidate. The likelihoods are built by Monte Carlo simulation of the protocol, on seeds separate from every scored run. A capture's three packets cannot be told apart on the wire, so each likelihood is pooled over the three.
- **Decision.** For each record, a vantage names the device with the highest posterior summed over that device's packets. Ties break in a random order of the devices.
- **Pairing.** Every vantage is paired with the passive observer on the same records.

## The claim criterion

For one vantage or class in one cell, the claim criterion passes when both conditions hold:

1. **Top 1% precision.** Take the 1% of the vantage's matches that it is most confident in. The upper bound of the 95% interval on the share of them that are right must be below 50%.
2. **Coverage.** Fewer than 0.1% of the vantage's matches may belong to any most-confident group in which the matches are right more than half the time.

A vantage that passes cannot identify a meaningful subset of its own guesses and be right about most of them.

**Stability rule.** A row needs at least 50 right and 50 wrong decisions at the device level. A row that misses it is unstable. It is reported as unstable and is not read as a finding.

## Diagnostics

Each diagnostic is a scoring variant on the same simulated traffic.

| Diagnostic | What it does |
|---|---|
| Timing evidence off | The observer with a flat timing likelihood. The candidate set, source addresses and priors are unchanged. |
| Record time at the midpoint | The observer and the content server score with the record time at the midpoint of F's and I's registry submissions. |
| Hits by packet type | The observer's submission-level hits split by the type of the packet it named (credential, F content or I content), each against its random rate, with the delay from each packet type's departure to the record time. |
| Match board share | The share of F's and I's confirmations set by the match board rather than by their own hold release. |
| Path delay | For credential packets (arrival at C) and F and I content packets (arrival at F or I), the mean and standard deviation of the delay from the packet's departure to its arrival, network time included. |
| Window halves | The observer's device-named accuracy in the first and the second half of the scored window, in every cell. The two agree when the 95% interval on their difference contains zero. |

## Controls

| Control | What changes | What it shows |
|---|---|---|
| Label shuffle | Within each run, every candidate's device label is permuted at random on the same scores. | Accuracy falls to the feasible chance rate for every vantage. |
| Shuffle test | For the observer, the shuffled picks are compared with the permuted unshuffled picks, the feasible counts with the unshuffled ones, and the estimator with 200 further permutations per run. | Whether any shortfall below chance comes from the shuffle, the feasible-set calculation or the estimator. |
| Every hold off | Every hold, lottery and schedule is set to zero. The 30-second departure grid and the 10-second board push remain. | The combined view's detection passes through when no hold hides it. |
| Credential path sets the record time | Relays as in the main run, and every credential-side stage at a 150 s mean: the device's credential channel, C, V, the fan-out at 50 s per draw, the gatekeeper and the inclusion lottery. Everything else is off. About 2% of transactions miss quorum within 30 minutes and are dropped. | The match board sets at least 95% of the confirmations, so the record time follows the credential path. |
| Content paths set the record time | Relays as in the main run, and the device holds both content channels at a 7,200 s mean. Everything else is off. | Content arrival sets at least 95% of the confirmations. |
| F content path sets the record time | Relays as in the main run, and the device holds its F channel at a 7,200 s mean. Everything else is off. | F's own content arrival sets F's confirmation, and F's submission is the later one, on at least 95% of the records. |

A device hold delays the packet before it leaves the device, so it adds no noise to a candidate's timing. Each control's measured share is reported with it.

## Cells and runs

- Real volume is R = 1, 100 and 500 transactions in flight, each with 100 decoy transactions in flight.
- Rates are R / D and 100 / D. D is the mean time a transaction stays in the system, from capture to the registry posting its record. It is calibrated under each configuration's own holds on 40 runs at R = 100. The calibration repeats until both counts in flight are within 3% of their targets.
- The counts in flight are measured in every run and reported beside their targets in `results/run_info.json`.
- Real and decoy transactions arrive at their normal rates from time zero to the end of the run.
- The warm-up lasts the configuration's longest possible delay: the sum of the caps along the longest path, plus 60 seconds. For the main configuration that is 2,650 seconds. Scoring starts after it, once traffic in flight is steady.
- The scored window holds about 200 real transactions per run on average: 200 D at R = 1, 2.2 D at R = 100 and 0.44 D at R = 500. The cap at 220 real transactions per run keeps the run within its cost. Only records introduced in the window are scored. The in-flight counts, the chance rates and every table use the window only.
- The cool-down after the window also lasts the longest possible delay, so every record introduced in the window finalizes. A real transaction introduced in the window that never finalizes, which only a quorum timeout can cause, is counted and reported.
- Packets from the warm-up and the cool-down stay in every vantage's candidate list.
- The main configuration runs 200 runs per cell. The controls run 50 (every hold off) or 100 runs per cell.
- A run's traffic depends only on its real volume and run id.

Intervals on accuracy resample whole runs, with a cluster bootstrap of 2,000 resamples. AUC intervals use the clustered-data variance of Obuchowski (1997).

## Running it

Requires Python 3.10 or later. Run from this directory.

```
pip install -r requirements.txt
python -m sna run
```

On Windows, use `py -m pip install -r requirements.txt` and `py -m sna run`.

`run` does every step:
1. calibrates D;
2. builds the attacker's models;
3. simulates and scores every run of the main configuration and the controls;
4. writes every file in `results/`.

It is resumable: rerunning the same command skips the runs already on disk. Results depend only on the cell and run id, not on the worker count or completion order. A results directory written under other settings is refused.

- `--runs N` sets the main configuration's runs per cell. Each control runs its own count or N, whichever is smaller.
- `--workers N` sets the worker processes. The default is half the cores. Workers run at below-normal priority, so the machine stays usable. The run prints the elapsed time and an estimate of the time remaining as it goes.
- `--out DIR` sets the results directory.
- `python -m sna run --runs 2 --out results/quick` runs every step on two runs per cell.
- Fast tests: `python -m pytest tests -q`.

## Contents

| Path | Contents |
|---|---|
| `RESULTS.md` | every finding |
| `PREDICTIONS.md` | the predictions, written and committed before the run |
| `results/summary.json`, `summary.csv` | every row of the main configuration, with the shuffle and the diagnostics |
| `results/TABLES.md` | the full tables |
| `results/PAPER_TABLE.md` | the headline tables |
| `results/controls/` | each control's rows, and the shuffle test |
| `results/timing.json` | every stage's delay, capture to finalization, packet-type delays and the match board share, per configuration and cell |
| `results/run_info.json` | seeds, runs per cell, D and its calibration, the counts in flight, the cost per run |
| `results/figures/device_named.png` | how often each vantage names the device, against chance |
| `results/figures/confidence_reliability.png` | each vantage's confidence against how often it is right |
| `results/figures/latency.png` | capture to registry posting |
| `sna/params.py` | every numeric input |
| `sna/lottery.py` | the hold lottery and the likelihood densities |
| `sna/sim.py` | the simulator |
| `sna/attacks.py` | record and candidate extraction, likelihood models, scoring of every vantage, the shuffle test |
| `sna/analyze.py` | metrics and intervals |
| `sna/experiment.py` | configurations, cells, seeds, calibration, the run worker |
| `sna/report.py` | every file in `results/` |
| `sna/runner.py` | resumable parallel execution |
| `audit/` | the audit of the code against its documentation |
| `tests/` | fast tests |

## What this experiment does not test

The simulation uses the 20-node pool and the transaction described above. It does not model:

- the jurisdiction filter or the skew in the device's choice of destinations;
- the grouping of device-table lines by destination pseudonym;
- a first-hop vantage that is told which destination a routing code leads to;
- any evidence a second relay holds.

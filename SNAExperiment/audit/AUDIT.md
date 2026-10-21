# Audit of SNAExperiment against its documentation

This audit compares the code in `SNAExperiment/sna/` with `README.md`, `RESULTS.md`, `PAPER_TABLE.md`, the docstrings and comments in `sna/`, the spec at `../Docs/Birthmark_Protocol_Per-Leg_Message_Specification_v102design.md`, and the paper excerpts (Section 3.4 Table 3, Appendix D.1, Appendix D.2).

- The code was audited at commit 5d2c254, branch `permitted-overlap`.
- No existing file was changed, and no result build was rerun.
- Traces use run ids that no committed result uses:
  - 50,000 and up for `trace_audit.py`;
  - 60,000 and up for `scoring_audit.py` and `tie_audit.py`;
  - 70,000 and up for `control_trace.py`.
- Every trace takes D from `results/calibration.json`.
- The outputs are in `audit/out/*.json`.

| Script | Measures |
|---|---|
| `trace_audit.py` | Roles, holds, clocks, padding, record time, traffic and candidates. 10 runs of `internal_compromise` at R = 20. |
| `scoring_audit.py` | Models, rows, ties, feasible sets, pairing, the loader, and the build configurations. Models are built in `audit/out/models` (not committed). |
| `tie_audit.py` | Ties and how they are broken, at R = 1 and R = 20. |
| `control_trace.py` | Every wait that remains under each control. 5 runs at R = 20. |

"Read only" means the row was checked by reading the code. Every other row gives the number measured.

## Counts by verdict

| Verdict | Rows |
|---|---|
| matches | 29 |
| differs | 13 |
| not documented | 3 |
| ambiguous | 2 |
| total | 47 |

## Rows that are not "matches"

| Item | Verdict | Finding |
|---|---|---|
| B1b | differs | The spec gives a standard deviation of 100.7 s (CoV 0.84) for 120 s stages. The code gives 103.6 s (CoV 0.86). For the registry bundle wait, the spec gives an SD of 50.3 s. The code draws it uniformly on a shared 120 s schedule, with SD 34.8 s. |
| B1c | differs | The `lottery.py` docstring says every node holds on a node-wide clock. Two holds do not use the node clock. The post-match lottery draws a fresh phase per packet. The gatekeeper hold runs on a separate gatekeeper clock. |
| B4b | differs | Paper Table 3 says the three fan-out legs "do not depart together". In 22.8% of transactions, two or more legs leave within 10 ms of each other. |
| B5b | differs | Paper Table 3 says the post-match lottery keeps F and I from submitting within seconds of each other. 25.9% of pairs leave the registry within 5 s of each other. |
| B6c | differs | Paper Table 3 omits three delays that the code applies: the gatekeeper's own 30 s hold, the 120 s registry bundle, and the 10 s board push. |
| B7 | not documented | The code adds per-hop processing times: 0.5 to 3 ms per node, 5 to 50 ms at the validator, 1 to 10 ms at a gatekeeper, and 5 to 50 ms for gossip validation. No document states them. |
| C3 | ambiguous | Registry submissions and gossip relays are a constant 284 B on the wire, with no padding. The paper says every transit leg is padded to 420 to 460 B. Neither document says whether a registry submission counts as a transit leg. |
| E1 | differs | The spec says decoys are "60 ± 10" and top up whatever real traffic falls short of the target. The code holds the decoy rate at 60 / D at every R. At R = 20, 19.4 real and 61.0 decoy transactions are in flight. |
| F1 | ambiguous | Appendix D.1 names seven vantages, each holding its component's keys. The code has six component vantages and the keyless observer. |
| F2 | differs | Each vantage is documented with a passive view of every link. The likelihoods use only two inputs: the device-originated first-hop packets and the registry gossip. Board postings are not simulated as wire events. |
| F3 | differs | The README's "Knows exactly" column lists more than three of the likelihoods use. |
| G1 | differs | The documents say candidates are grouped into captures. 61.5% of candidate groups hold exactly one capture's three packets. 61.4% of scored captures have a whole group. |
| G3 | not documented | One first-relay model (`fh`) is pooled over the A, D and G paths and used for every first relay. No document states this. |
| G4b | not documented | When scores tie, the lowest device id wins. 0% to 0.25% of device decisions tie at R = 20, by vantage. |
| I2b | differs | `first_relay_signal_cred` is documented so that "the record time then follows the credential path". The board, which is the credential path, sets 83% of F and I confirmations. The content paths set 17%. |
| I2c | differs | `first_relay_signal_content` is documented so that "the record time then follows the content paths". Content arrival sets 76% of F and I confirmations. The board sets 24%. |
| I2d | differs | `first_relay_signal_one_content` is documented as "signal on the F content path only". The G path's relays still hold for 120 s. I's own content arrival sets 45% of I's confirmations. |
| I3b | differs | README line 184 gives the `first-relay-paths` output as `results/first_relay_paths.json`. The committed file is `results/controls/first_relay_paths.json`. README line 183 says `run --build first_relay_signal_one_content` writes to `results/controls/`. No summary for that control is committed. The command ignores `--runs`. |

The two rows below explain the counts in I2b to I2d.

- **A confirmation set by the board.** F (or I) confirms at max(own hold release, board knowledge). The confirmation is set by the board when board knowledge comes last.
- **The board follows the credential path.** Board knowledge waits on the gatekeepers' postings, which come at the end of the credential path.

## Audit table

Code locations are relative to `SNAExperiment/`. "Every build" means the eleven builds in `sna/experiment.py` BUILDS.

### A. Roles

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| A1 | The documented draw (README, D.2):<br>• nine distinct nodes per transaction;<br>• credential path A → B → C;<br>• content paths D → E → F and G → H → I;<br>• the paths share no node. | `sna/sim.py:126` `_roles`, `sna/sim.py:152` `pick` | With `overlap` False, all nine roles are distinct in 16,719 of 16,719 transactions. | matches | trace: 16,719 transactions, 100% distinct |
| A2 | 20 Registry Nodes, 1 validator, 3 active gatekeepers per run. | `sna/params.py:26`, `sna/params.py:28`, `sna/sim.py:81` | 20 nodes. 3 gatekeepers in every run. One validator clock (`v_phase`). | matches | trace: 20 nodes, 3 gatekeepers |
| A3 | C, F and I are never active gatekeepers. The spec (line 81) says a gatekeeper may serve as a first relay for another transaction. | `sna/sim.py:126` | C, F or I is a gatekeeper 0 times. A relay is a gatekeeper in 12,602 of 16,719 transactions. | matches | trace: 0 of 16,719 |

### B. Holds

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| B1a | Lottery shape:<br>• geometric release on a 10 s tick;<br>• unconditional at 3× the mean;<br>• release probability set to hit the mean;<br>• 120 s gives 7.52% and a 360 s cap. | `sna/lottery.py:27` `stage_lottery`, `sna/lottery.py:44` `hold` | p = 0.0752 and K = 36 ticks.<br>• Released at the first tick: 7.40%.<br>• Maximum: 36 ticks.<br>• At the cap: 6.51%, against 6.48% expected. | matches | trace: 50,088 relay holds |
| B1b | Spec table (`../Docs/...v102design.md:171-181`):<br>• SD 100.7 s (CoV 0.84) for 120 s stages;<br>• registry wait SD 50.3 s. | `sna/lottery.py:27`, `sna/sim.py:287-292` | 120 s stages: SD 102.6 to 104.3 s (CoV 0.86).<br>Registry wait: mean 60.7 s, SD 34.8 s, max 120 s (uniform). | differs | trace: relay SD 103.6 s, registry SD 34.8 s |
| B1c | `sna/lottery.py:1-7`: every node holds packets on a node-wide clock. A device uses an independent phase per channel. | `sna/sim.py:189`, `sna/sim.py:243`, `sna/sim.py:258`, `sna/sim.py:275`, `sna/sim.py:282` | Share of releases exactly on the clock tested:<br>• F pre-match on F's node clock: 99.7%.<br>• F post-match on F's node clock: 0.0%. It uses a fresh phase per packet, as the comment at `sim.py:282` states.<br>• Gatekeeper hold on its node clock: 0.0%. On its own hold clock (`gk_phase`): 99.98%.<br>• Validator on `v_phase`: 99.9%. | differs | trace: share on tick per clock |
| B2 | Device holds:<br>• credential 120 s;<br>• each content channel 240 s, with a separate draw per channel;<br>• the I channel defaults to the F channel's mean. | `sna/sim.py:178-184`, `sna/params.py:66-68` | Credential mean 121.5 s, SD 104.3 s, max 360.0 s.<br>F mean 240.9 s, SD 206.5 s, max 720.0 s.<br>I mean 240.4 s, SD 206.4 s, max 720.0 s.<br>Correlations of hold durations: F with I −0.012; credential with F −0.024.<br>• F and I release within 1 s of each other: 0.48%.<br>• Correlation of F and I release times: 0.996, through the shared capture time.<br>• `dev_content_i_mean` defaults to −1, which means "same as F". | matches | trace: 8,348 transactions |
| B3 | Relay hops A, B, D, E, G, H: 120 s each, on the node's own clock, with independent draws. | `sna/sim.py:189` | Means 119.2 to 121.5 s. SD 102.6 to 103.6 s. Max 360 s.<br>• 100% of releases fall within 3 ms after the node's own tick.<br>• Correlation of A and B holds on the same packet: 0.023. | matches | trace: 8,348 per hop |
| B4a | C before CV-1: 30 s. V before CV-2: 30 s. | `sna/sim.py:239`, `sna/sim.py:243` | C: mean 29.8 s, max 90 s.<br>V, including validator processing: mean 29.8 s, max 90 s. | matches | trace: 8,348 |
| B4b | C fan-out:<br>• 60 s with an independent draw per leg (README, Table 3);<br>• Table 3: "the three legs do not depart together". | `sna/sim.py:252` | Leg means 59.9, 59.6 and 60.2 s. Max 180 s.<br>• Correlation between legs: 0.027 and 0.0002.<br>• All legs release on C's node clock, so independent draws can land on the same tick.<br>• Two or more legs leave within 10 ms of each other in 22.8% of transactions. | differs | trace: 22.8% of 8,348 |
| B5a | F and I: 240 s pre-match and 30 s post-match, independent. | `sna/sim.py:275`, `sna/sim.py:282-284` | Pre-match F 241.2 s, I 244.5 s, correlation −0.0015.<br>Post-match F 30.1 s, I 30.2 s, correlation 0.0006. | matches | trace: 8,348 |
| B5b | Table 3: the independent post-match lottery "keeps the two servers from submitting within seconds of each other". | `sna/sim.py:282-292` | F and I within 5 s of each other:<br>• at post-match release: 3.7%;<br>• as they leave, after registry bundling: 25.9%.<br>RESULTS.md lines 152-154 report the same effect. | differs | trace: 25.9% of 8,348 |
| B6a | Gatekeeper's own 30 s hold. Departure lottery: 30 s boundaries, 25% at each, unconditional at the 12th. | `sna/sim.py:258`, `sna/sim.py:260-266`, `sna/lottery.py:58` | Gatekeeper hold: mean 30.2 s, max 90 s.<br>Departure lottery:<br>• Boarding rate at boundaries 1 to 11: 0.236 to 0.266. At boundary 12: 1.0.<br>• 100% of departures fall on the gatekeeper's own boundary.<br>• Bundling wait: mean 99.6 s. | matches | trace: 25,044 postings |
| B6b | Registry bundling: one shared 120 s schedule (README). | `sna/sim.py:287-292` | 100% of departures fall within 3 ms after the shared boundary. Wait: mean 60.7 s, max 120 s. | matches | trace: 8,348 |
| B6c | Table 3 lists the holds:<br>• device channels;<br>• relays;<br>• C and V;<br>• fan-out;<br>• F and I;<br>• the departure lottery. | `sna/sim.py:258`, `sna/sim.py:287-292`, `sna/sim.py:205-215` | The code also applies three delays not in Table 3:<br>• the gatekeeper's own hold: 30.2 s;<br>• the registry bundle wait: 60.7 s;<br>• the board push wait: 5.3 s.<br>The README documents all three. | differs | trace: means as listed |
| B7 | README: latency fixed per host pair, with per-packet jitter, and no queueing. No processing times are documented. | `sna/params.py:39-45`, `sna/sim.py:197-201` | Link latency per leg: mean 46 ms.<br>Processing times:<br>• per node: 0.5 to 3 ms;<br>• validator: 5 to 50 ms;<br>• gatekeeper: 1 to 10 ms;<br>• gossip validation: 5 to 50 ms.<br>Quorum timeouts: 0. | not documented | trace: 551,727 legs; processing ranges read from params |

### C. Packets and padding

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| C1 | Every transit leg is padded uniformly to 420 to 460 B, plus 22 B TLS overhead. | `sna/sim.py:108-112`, `sna/params.py:16-17` | The Cred-1/2/3, ContA-1/2/3, ContB-1/2/3, CV-1 and CV-2 legs all have a payload of 420 to 460 B and a wire size of 442 to 482 B. Chi-square against uniform: 32.7 to 64.6 on 41 bins. | matches | trace: 16,719 per leg |
| C2 | Gatekeeper fan-out: 820 to 860 B. | `sna/sim.py:254` | GK-1/2/3 payload 820 to 860 B. Wire 842 to 882 B. | matches | trace: 16,719 per leg |
| C3 | README: registry submissions travel as gossipsub frames. D.2: padding of 420 to 460 B "for every transit leg". | `sna/params.py:32`, `sna/sim.py:313` | Reg-F, Reg-I and every gossip relay are a constant 284 B on the wire. | ambiguous | trace: 3.6 million gossip relays, all 284 B |

### D. Record time

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| D1 | The record time is the midpoint of F's and I's submissions. | `sna/attacks.py:101` | Record time minus the true midpoint: mean −0.3 ms, range −2.3 to +0.2 ms. The difference is gossip latency. | matches | trace: 16,719 records |
| D2 | A server confirms when its own pre-match hold has released and two boards' pushes carry the match. It drops the transaction after 30 minutes without quorum. | `sna/sim.py:275-278` | det − max(hold, known) = 0 exactly. Board push wait: mean 5.3 s, max 9.9 s. Timeouts: 0. | matches | trace: 8,348 |

### E. Traffic

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| E1 | README and D.2: 60 decoys in flight at every level. Spec line 159: "60 ± 10", and decoy volume "tops up whatever real traffic falls short". | `sna/experiment.py:34`, `sna/experiment.py:114-117` | The decoy rate is 60 / D at every R, independent of real volume. At R = 20: 19.4 real and 61.0 decoy transactions in flight. 100% of decoys finalize. | differs | trace: 10 runs. Matches the README and D.2; differs from the spec. |
| E2 | N_real = 1, 20 and 100. Rates are R / D. | `sna/experiment.py:33`, `sna/experiment.py:114` | Real transactions in flight at R = 20: 19.4. | matches | trace: 10 runs |
| E3 | Mean latency 1,034 s (D.2). 1,033.8 s (README). | `sna/experiment.py:246` | Mean capture to finalization: 1,037.9 s at R = 20. | matches | trace: 10 runs |

### F. Vantages

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| F1 | D.1: seven passive vantages, each holding its component's keys. README: seven rows including the keyless observer, with:<br>• four servers per run for the first hops and C;<br>• the content server scored on its own records;<br>• the gatekeeper scored once per active gatekeeper. | `sna/attacks.py:35`, `sna/attacks.py:511-550` | VANTAGES holds six component vantages and the observer. Rows per run, as a multiple of the record count:<br>• first hops and C: 4×;<br>• content server: 2×;<br>• gatekeeper: 3×;<br>• validator and observer: 1×. | ambiguous | trace: rows in 3 runs |
| F2 | Each vantage has a passive view of traffic sizes and timing on every link (README line 8, D.1). | `sna/attacks.py:111-152`, `sna/attacks.py:553-622` | The likelihoods take only two inputs:<br>• the candidates' first-hop packets from devices;<br>• the record time from registry gossip.<br>No other link enters any score. Board postings are not simulated as wire events. | differs | read only |
| F3 | The README "Knows exactly" column per vantage. | `sna/attacks.py:579-587`, `sna/attacks.py:602-608`, `sna/attacks.py:613-622` | Three vantages use less than the column lists:<br>• **Content server:** only its content arrival (`arr_f` / `arr_i`). It does not use board pushes or its own submission.<br>• **Gatekeeper:** only its postings. It does not use packet arrival or hold release.<br>• **C:** only the median of its three fan-out sends, with a prior of 1/17. It does not use the validator's reply. | differs | read only |
| F4 | The first-relay vantage is not told the destination behind a routing code. | `sna/attacks.py:566-577` | The first-hop score uses only the candidate's node and that node's own hold. | matches | read only |

### G. Candidates and scoring

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| G1 | Candidates are each source's first-hop packets, grouped into captures, decoys included. | `sna/attacks.py:111-152` (span at line 131) | Packets are grouped greedily per source: up to 3 within 3 × max(device mean) + 10 s.<br>• Groups holding exactly one capture's three packets: 61.5%.<br>• Scored captures with a whole group: 61.4%.<br>• Sources in candidates: 92. Sources in truth: 92. | differs | trace: 10 runs at R = 20 |
| G2 | Likelihoods come from Monte Carlo on independent seeds. | `sna/attacks.py:244`, `sna/experiment.py:96`, `sna/experiment.py:158-164` | The models use seeds from 1,000,000,000 up, a range no scored run uses. 113 Monte Carlo runs. | matches | trace: 113 runs; seed ranges read only |
| G3 | Not stated in README, RESULTS or the paper. Spec line 228: a first relay cannot tell which of A, D or G it plays. | `sna/attacks.py:229` | One `fh` model is pooled over all three first-relay paths (900,924 samples). The model keys are c, cs, fh, g, gV and gk, each with its `_q` variant. | not documented | trace: model keys |
| G4a | The highest summed posterior names the device. | `sna/attacks.py:303-361` | Scores are combined by logsumexp per device, then argmax. | matches | read only |
| G4b | Not documented. README line 168 mentions floating-point ties between platforms. | `sna/attacks.py:286`, `sna/attacks.py:305`, `sna/attacks.py:361` | `np.unique` sorts device labels ascending, and argmax takes the first maximum, so the lowest device id wins. Tied decisions at R = 20: 0% to 0.25% by vantage. In the tie audit, 10 of 8,778 decisions tie and 2 of the 10 are right. | not documented | trace: 10 ties |
| G5 | README: feasible-set chance is a uniform guess among the devices that could have produced the record. | `sna/attacks.py:374-382` | Median feasible devices at R = 20:<br>• about 65.3 for most vantages;<br>• 62.0 for the content server;<br>• 71.7 for the validator;<br>out of 92 registered. | matches | trace: 3 runs |
| G6 | Every vantage is paired with the observer on the same records. | `sna/analyze.py:241`, `sna/analyze.py:304-322` | Leads match rows on (run, sub, group). | matches | read only |

### H. Metrics

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| H1 | Claim: the top 1% precision upper bound is below 50%, and coverage is below 0.1%, for every vantage. | `sna/report.py:258-262`, `sna/analyze.py:107-120` | The code tests `p_at_1_hi < 0.5` and `coverage_p50 < 0.001` for every vantage. | matches | read only |
| H2 | 200 runs per cell. Cluster bootstrap with 2,000 resamples. At least 50 right and 50 wrong per vantage per cell. | `sna/analyze.py:20-25`, `sna/experiment.py:35` | All 291 committed summary rows have runs = 200 and at least 50 right and 50 wrong. | matches | committed summaries: 291 rows |
| H3 | Each build is paired with the baseline record by record on identical traffic. `permitted_overlap` changes only the relays. | `sna/experiment.py:120`, `sna/sim.py:165-175` | `no_mechanisms` has the same t0 and src as the baseline. `permitted_overlap` has the same t0, src, C, F and I, with different relays. | matches | trace: 3 runs |
| H3b | `no_mechanisms` is documented as "all five of the above removed together". | `sna/experiment.py:40-56` | It sets:<br>• device content and F/I to 120 s;<br>• C and V holds to 0;<br>• inclusion off;<br>• post-match off;<br>• registry bundling to 0.<br>The fan-out (60 s) and the gatekeeper hold (30 s) remain. They are not among the five. | matches | configuration read from Config |

### I. Overlap work

| Item | Documented behavior | Code location | Observed behavior | Verdict | Verification |
|---|---|---|---|---|---|
| I1 | The `permitted_overlap` draw:<br>• C, F and I are kept;<br>• A, D and G are pairwise distinct and differ from their own destination;<br>• B, E and H differ from their own first relay and destination;<br>• other coincidences are allowed;<br>• the relays come from a separate stream;<br>• every node is compromised in every run. | `sna/sim.py:152-175`, `sna/attacks.py:514-522` | All nine roles are distinct in 4,479 of 16,719 transactions. A cross-path coincidence occurs in 12,240.<br>• Path repeats, first-relay repeats, destination repeats, and C/F/I as gatekeeper: 0 each.<br>• t0, src, C, F and I are unchanged.<br>• `servers_for` returns every node when `overlap` is True. | matches | trace: 16,719 transactions; all-nodes rule read only |
| I2a | `overlap_no_holds`: every hold and lottery off. | `sna/experiment.py:57-60` | Every hold measures 0.0 s. Two waits remain, and they are not holds or lotteries:<br>• the 30 s departure grid: 14.9 s;<br>• the board push: 6.3 s.<br>Capture to finalization: 21.6 s. | matches | trace: 5 runs |
| I2b | `first_relay_signal_cred`:<br>• only the relay holds (120 s) and the device credential hold (240 s) are on;<br>• "the record time then follows the credential path". | `sna/experiment.py:61-65` | Device credential hold: 242.1 s. Relays on every path: 118.8 to 123.1 s. Every other hold: 0. The board sets 83% of F and I confirmations. | differs | trace: 5 runs |
| I2c | `first_relay_signal_content`:<br>• only the relay holds and the device content holds (240 s) are on;<br>• "the record time then follows the content paths". | `sna/experiment.py:66-68` | Device F hold 237.0 s and I hold 237.9 s. Relays: 118.9 to 123.1 s. Content arrival sets 76% of confirmations. The board sets 24%. | differs | trace: 5 runs |
| I2d | `first_relay_signal_one_content`: "the device holds only its F channel"; "signal on the F content path only". | `sna/experiment.py:69-72` | Device F hold: 237.0 s. Device I hold: 0. Relays D, E, G and H still hold for 120 s. The board sets 24% of F's confirmations and 55% of I's. I's own content arrival sets 45% of I's. | differs | trace: 5 runs |
| I3a | `first-relay-paths` runs 300 held-out runs (2,000 to 2,299) per control. | `sna/experiment.py:546-568` | The control summaries are scored on run ids 0 to 299, with models from 1,000,000,000 up. The committed file records run0 = 2000 and runs = 300. | matches | committed file; run ranges read only |
| I3b | README line 184: output at `results/first_relay_paths.json`. README line 183: `run --build <control>` writes the four controls to `results/controls/`. | `sna/cli.py:15-16`, `sna/cli.py:70`, `sna/experiment.py:546` | The command writes to `<--out>/first_relay_paths.json`. The committed file is `results/controls/first_relay_paths.json`. No summary for `first_relay_signal_one_content` is committed. The command ignores `--runs`. | differs | committed files listed; flags read only |
| I4 | The loader skips a gzip member cut off by an interruption and still reads every intact member after it. | `sna/runner.py:35-68` | With the cut member last: runs [0] are read. After two resumed members: runs [0, 5, 6, 7, 8]. | matches | trace: synthetic file |

## Committed builds and controls on each code path that is not "matches"

**Groups used below:**
- The eleven builds:
  - `internal_compromise`;
  - `no_vc_holds`;
  - `no_inclusion_lottery`;
  - `no_post_match_lottery`;
  - `no_registry_bundling`;
  - `no_role_aware_holds`;
  - `no_mechanisms`;
  - `relay_180s`;
  - `role_aware_360s`;
  - `gatekeeper_120s`;
  - `permitted_overlap`.
- The four controls: `overlap_no_holds`, `first_relay_signal_cred`, `first_relay_signal_content` and `first_relay_signal_one_content`.
- The derived results:
  - `results/shuffle_control.json`, which uses the `permitted_overlap` configuration;
  - `results/controls/first_relay_paths.json`, which uses the three signal controls;
  - `results/latency.json`;
  - `results/pair_gaps.json`;
  - `results/timing_check.json`.

**Registry bundling.** "The nine registry-bundled builds" are the eleven builds except `no_registry_bundling` and `no_mechanisms`. Every control sets registry bundling to 0.

| Row | Code path | Used by |
|---|---|---|
| B1b | `lottery.hold` for every stage | Every build and every control. |
| B1b | Registry bundle wait (`reg_bundle_s` = 120) | The nine registry-bundled builds and the shuffle control. |
| B1c | Post-match fresh phase (`post_match` True) | The eleven builds except `no_post_match_lottery` and `no_mechanisms`, plus the shuffle control. Every control sets `post_match` False. |
| B1c | Gatekeeper hold on `gk_phase` (`gk_mean` > 0) | The eleven builds and the shuffle control. Every control sets `gk_mean` to 0, and the measured gatekeeper hold there is 0.01 s. |
| B4b | Fan-out on C's node clock (`fanout_mean` = 60) | The eleven builds and the shuffle control. Every control sets `fanout_mean` to 0, and the measured fan-out wait there is 0.0 s. |
| B5b | Post-match lottery followed by registry bundling | The nine registry-bundled builds except `no_post_match_lottery`, plus the shuffle control. `pair_gaps.json` measures this path for the ten builds other than `permitted_overlap`. |
| B6c | Gatekeeper hold | The eleven builds and the shuffle control. |
| B6c | Registry bundle | The nine registry-bundled builds and the shuffle control. |
| B6c | Board push | Every build and every control. |
| B7 | Processing times | Every build and every control. |
| C3 | Gossip frames at 284 B, the record time | Every build and every control. |
| E1 | Fixed decoy rate of 60 / D | Every build and every control, at every R. |
| F1 | VANTAGES set | Every build. The combined view is scored under `permitted_overlap`, the controls, the shuffle control and `first-relay-paths`. |
| F2 | Likelihood inputs | Every build, every control, the shuffle control and `first-relay-paths`. |
| F3 | Content server, gatekeeper and C likelihoods | Every build, every control and the shuffle control. Under `permitted_overlap` and the controls, the combined view adds these terms. |
| G1 | `candidates` grouping | Every build, every control, the shuffle control and `first-relay-paths`. |
| G3 | Pooled `fh` model | Every build, every control, the shuffle control and `first-relay-paths`. `first-relay-paths` scores A, D and G with it. |
| G4b | Tie-breaking by lowest device id | Every build, every control, the shuffle control and `first-relay-paths`. |
| I2b | `first_relay_signal_cred` configuration | `results/controls/summary_first_relay_signal_cred.json`, RESULTS.md line 316, and the "credential path only" rows of `first_relay_paths.json`. |
| I2c | `first_relay_signal_content` configuration | `results/controls/summary_first_relay_signal_content.json`, RESULTS.md line 317, and the "both content paths" rows of `first_relay_paths.json`. |
| I2d | `first_relay_signal_one_content` configuration | The "F content path only" rows of `first_relay_paths.json` and RESULTS.md lines 319 to 327. |
| I3b | `first-relay-paths` output location | `results/controls/first_relay_paths.json`. |

## Checks not done

- **Board posting traffic seen by a passive observer.** Board postings are not wire events in the simulator, so there is no trace to measure.
- **The cross-platform tie differences stated in README line 168.** Checking them needs a rerun of committed builds on a second platform, and this audit reruns no build.

# Results

InternalCompromiseRun: can a single compromised component of the Birthmark Protocol take a public registry record and name the device that produced it?

**Simulator version 1.** Every number below was produced by simulator version 1. In version 1, the three fan-out legs drew independent holds, the record time was the midpoint of F's and I's submissions, and candidates were device packets grouped greedily into captures. The code in this folder is version 2 (`README.md`). These numbers stand for version 1 until a version 2 run replaces them.

- Every hold follows the timing in `README.md`: 10-second ticks, geometric release, each capped at three times its own mean.
- Departure bundling is by inclusion lottery. Registry bundling uses one shared 120-second schedule. The post-match lottery is on.
- R = 1, 20 and 100 real transactions in flight, with 60 decoys in flight; 200 runs per cell.
- Every cell of every build met the stability rule: at least 50 right and 50 wrong decisions at the device level for every vantage.
- The full generated tables are in `results/TABLES.md`. The figures are `results/figures/device_named.png` and `confidence_reliability.png`.

## Summary

1. **No single compromised component does meaningfully better than a passive observer.**
   - Across the 18 component-and-cell combinations, the largest lead over the observer is +0.24 points [+0.18, +0.30] (content server, R = 100).
   - It is the only lead whose interval lies above 0.
   - The validator, which holds a device identity for every approval, is 0.06 to 0.40 points below the observer.
2. **Every component, the observer included, names the device about 4 to 5 times as often as a guess among the devices that could have produced the record.**

   | | R = 1 | R = 20 | R = 100 |
   |---|---|---|---|
   | Observer | 9.91% | 6.46% | 3.48% |
   | Best component | 9.95% | 6.60% | 3.72% |
   | Feasible-set guess | 2.03% | 1.55% | 0.77% |
   | One in N registered devices | 1.43% | 1.09% | 0.54% |

3. **The adversary cannot tell which of its matches are right.**
   - A component's average confidence in its own match is 6.7% to 8.1% at R = 1, 5.3% to 6.5% at R = 20 and 2.8% to 3.6% at R = 100.
   - Its 99th-percentile confidence never exceeds 13.6%.
   - The most confident 1% of any component's matches are right at most 26.5% of the time, with an upper bound of 30.3%.
   - In no cell do more than 0.019% of a component's decisions fall in a most-confident set that is right more than half the time.
4. **InternalCompromiseRun passes the claim criterion at R = 1, 20 and 100.**
   - So does every other build, including the one with all five mechanisms removed.
   - At 60 decoys, the builds differ in the leads and in the observer's accuracy, which the sections below report.
5. **Of the five timing mechanisms, the role-aware holds matter most.**
   - Without them, the validator leads the observer by +2.01, +1.49 and +1.04 points, and the content server by +0.42 to +0.77.
   - The observer itself gains 0.43 to 0.87 points.
   - Removed one at a time, the four other mechanisms each change the observer by at most 0.10 points.
6. **Mean capture to finalization is 1,033 to 1,042 seconds.** The 95th percentile is 1,523 to 1,530 seconds.
   - Without the role-aware holds the mean is 807 seconds.
   - With all five mechanisms removed it is 647 to 650 seconds.

## The adversary against InternalCompromiseRun

Device named, in percent [95% CI]. The lead is over the passive observer on the same records, in points [95% CI]. Top 1% is the share of a component's most confident 1% of matches that are right.

| Component | R = 1 | Lead | R = 20 | Lead | R = 100 | Lead | Top 1% right, R = 1 / 20 / 100 |
|---|---|---|---|---|---|---|---|
| Passive observer | 9.91 [9.48, 10.33] | reference | 6.46 [6.15, 6.78] | reference | 3.48 [3.40, 3.56] | reference | 25.8 / 13.4 / 6.5 |
| First hop, credential | 9.89 [9.46, 10.30] | -0.02 [-0.11, +0.06] | 6.47 [6.17, 6.79] | +0.01 [-0.07, +0.09] | 3.47 [3.40, 3.54] | -0.01 [-0.04, +0.01] | 25.4 / 13.7 / 6.2 |
| First hop, content | 9.89 [9.48, 10.28] | -0.02 [-0.10, +0.06] | 6.47 [6.17, 6.77] | +0.01 [-0.07, +0.09] | 3.47 [3.39, 3.54] | -0.01 [-0.03, +0.01] | 25.4 / 13.7 / 6.2 |
| Credential processor | 9.91 [9.48, 10.33] | +0.00 [-0.05, +0.05] | 6.46 [6.14, 6.77] | -0.01 [-0.04, +0.03] | 3.47 [3.39, 3.54] | -0.01 [-0.02, +0.00] | 25.5 / 13.5 / 6.4 |
| Validator | 9.51 [9.10, 9.93] | -0.40 [-0.79, -0.05] | 6.32 [6.05, 6.59] | -0.14 [-0.42, +0.12] | 3.41 [3.33, 3.49] | -0.06 [-0.15, +0.02] | 22.1 / 9.4 / 5.3 |
| Gatekeeper | 9.95 [9.54, 10.38] | +0.04 [-0.06, +0.14] | 6.45 [6.14, 6.74] | -0.01 [-0.10, +0.07] | 3.46 [3.39, 3.55] | -0.01 [-0.04, +0.01] | 26.5 / 13.8 / 6.7 |
| Content server | 9.84 [9.52, 10.15] | -0.07 [-0.31, +0.16] | 6.60 [6.35, 6.84] | +0.14 [-0.06, +0.35] | 3.72 [3.64, 3.79] | +0.24 [+0.18, +0.30] | 7.9 / 3.7 / 2.2 |

The content server is the most accurate component at R = 20 and 100. Its confidence is the least useful, though: its most confident 1% of matches are right 2.2% to 7.9% of the time, against 5.3% to 26.5% for every other component.

## The adversary's confidence

Each component's confidence is calibrated on half the runs and scored on the other half (cross-fitted by run parity).

- **Calibration is close for every component except the content server.**
  - At R = 20, the mean absolute gap between stated confidence and the share of matches that are right is 0.24 to 0.47 points for six components, and 1.35 points for the content server.
  - Across the ten deciles at R = 20, the content server's stated confidence runs from 3.8% to 8.2%. The share of its matches that are right runs from 5.2% to 8.3%. It is underconfident below its top decile.
- **The highest confidence any component gives a single match** is 7.8% to 20.9% for the observer, credential processor, validator and gatekeeper. It is 22% to 43% for the first hops and 79% to 86% for the content server.
  - These are single records.
  - At most 0.017% of a first hop's decisions fall in a most-confident set right more than half the time. None of the content server's do.

## Claim criterion

The criterion is defined in `README.md`. InternalCompromiseRun passes it in every cell:

| R | Highest upper bound on top-1% precision, any component | Largest share of decisions in a most-confident set right more than half the time |
|---|---|---|
| 1 | 30.3% (passive observer) | 0.0075% (gatekeeper) |
| 20 | 17.0% (passive observer) | 0.0186% (credential processor) |
| 100 | 7.6% (passive observer) | 0.0000% |

Every other build also passes in every cell. Across all ten builds the highest upper bound is 32.9% and the largest share is 0.0728%.

## What each mechanism contributes

Each build removes one mechanism from InternalCompromiseRun and keeps the rest. It is paired with InternalCompromiseRun on the same records: the effect is the build minus InternalCompromiseRun, in points [95% CI].

| Build | R | Observer: effect vs InternalCompromiseRun | Validator's lead | Content server's lead | Mean latency |
|---|---|---|---|---|---|
| InternalCompromiseRun | 1 | reference | -0.40 [-0.79, -0.05] | -0.07 [-0.31, +0.16] | 1,042 s |
| InternalCompromiseRun | 20 | reference | -0.14 [-0.42, +0.12] | +0.14 [-0.06, +0.35] | 1,033 s |
| InternalCompromiseRun | 100 | reference | -0.06 [-0.15, +0.02] | +0.24 [+0.18, +0.30] | 1,037 s |
| without V's and C's holds | 1 / 20 / 100 | -0.01 [-0.18, +0.16] / -0.10 [-0.26, +0.07] / +0.02 [-0.02, +0.07] | see `results/TABLES.md` | see `results/TABLES.md` | 1,020 to 1,030 s |
| without the inclusion lottery | 1 / 20 / 100 | +0.06 [-0.15, +0.27] / -0.10 [-0.26, +0.07] / +0.04 [-0.01, +0.10] | | | 1,017 to 1,026 s |
| without the post-match lottery | 1 / 20 / 100 | -0.03 [-0.19, +0.14] / -0.09 [-0.24, +0.07] / +0.06 [+0.02, +0.11] | | | 999 to 1,010 s |
| without registry bundling | 1 / 20 / 100 | +0.06 [-0.10, +0.23] / +0.04 [-0.10, +0.18] / +0.06 [+0.01, +0.10] | | | 973 to 983 s |
| without role-aware holds | 1 | +0.70 [+0.37, +1.05] | +2.01 [+1.58, +2.42] | +0.68 [+0.43, +0.92] | 807 s |
| without role-aware holds | 20 | +0.87 [+0.60, +1.14] | +1.49 [+1.16, +1.81] | +0.77 [+0.55, +0.99] | 807 s |
| without role-aware holds | 100 | +0.43 [+0.37, +0.50] | +1.04 [+0.92, +1.15] | +0.42 [+0.35, +0.50] | 807 s |
| without all five | 1 | +1.46 [+1.16, +1.76] | +1.17 [+0.82, +1.51] | +0.13 [-0.07, +0.33] | 650 s |
| without all five | 20 | +1.31 [+1.05, +1.59] | +0.91 [+0.58, +1.23] | +0.30 [+0.08, +0.51] | 647 s |
| without all five | 100 | +0.73 [+0.66, +0.81] | +0.64 [+0.54, +0.74] | +0.25 [+0.17, +0.32] | 649 s |

- **Role-aware holds** (device content channels and F/I pre-match hold at 240 s, against 120 s everywhere else) are the only single mechanism whose removal moves any number by more than 0.10 points.
  - Removing them makes the observer more accurate.
  - It also hands the validator a lead of 1 to 2 points.
- **V's and C's holds, the inclusion lottery, the post-match lottery and registry bundling** each move the observer by 0.10 points or less when removed alone.
  - Two of the twelve effects have intervals above 0: the post-match lottery and registry bundling, both at R = 100, +0.06 points each.
  - None moves the best component's accuracy by more than 0.13 points (`results/TABLES.md`).
- **Removed together, the five raise the observer by 0.73 to 1.46 points.** That is about twice the effect of removing the role-aware holds alone.
  - The difference points to the four smaller mechanisms mattering together more than any one of them alone.
  - That contrast (all five removed, against role-aware holds removed) has no paired interval here.
- **The four smaller mechanisms cost about 160 seconds of mean latency between them.** The difference between 807 and 650 seconds measures this. The role-aware holds cost about 230 seconds.

## Alternative settings

Each build changes one setting of InternalCompromiseRun and is paired with it on the same records.

| Build | R | Observer: effect vs InternalCompromiseRun | Validator's lead | Content server's lead | Mean latency |
|---|---|---|---|---|---|
| relay hops at 180 s | 1 | -0.62 [-0.83, -0.41] | -0.37 [-0.78, -0.00] | -0.43 [-0.71, -0.16] | 1,199 s |
| relay hops at 180 s | 20 | -0.57 [-0.73, -0.40] | +0.10 [-0.18, +0.37] | -0.01 [-0.22, +0.20] | 1,189 s |
| relay hops at 180 s | 100 | -0.30 [-0.35, -0.24] | +0.06 [-0.03, +0.15] | +0.02 [-0.05, +0.09] | 1,192 s |
| role-aware holds at 360 s | 1 | -1.33 [-1.64, -1.01] | -0.64 [-0.96, -0.30] | -0.15 [-0.41, +0.12] | 1,337 s |
| role-aware holds at 360 s | 20 | -1.42 [-1.65, -1.17] | -0.17 [-0.41, +0.06] | +0.51 [+0.31, +0.69] | 1,324 s |
| role-aware holds at 360 s | 100 | -0.57 [-0.65, -0.49] | -0.28 [-0.36, -0.20] | +0.20 [+0.13, +0.27] | 1,328 s |
| gatekeeper hold at 120 s | 1 | +0.02 [-0.17, +0.21] | -0.17 [-0.55, +0.19] | -0.03 [-0.30, +0.25] | 1,068 s |
| gatekeeper hold at 120 s | 20 | -0.11 [-0.28, +0.06] | +0.35 [+0.05, +0.63] | +0.33 [+0.11, +0.56] | 1,059 s |
| gatekeeper hold at 120 s | 100 | -0.03 [-0.08, +0.03] | +0.13 [+0.04, +0.22] | +0.26 [+0.19, +0.33] | 1,062 s |

- **Relay hops at 180 s** lower the observer's accuracy by 0.30 to 0.62 points and the strongest component's by 0.51 to 0.72 points. Every lead stays at or below +0.10.
  - Latency rises by about 155 seconds.
  - Of the three alternative settings it is the only one that lowers accuracy without opening a lead.
- **Role-aware holds at 360 s** lower the observer the most, by 0.57 to 1.42 points, at about 290 seconds more latency.
  - At R = 20 and 100 the content server's lead rises to +0.51 and +0.20.
  - Its absolute accuracy still falls: 5.55% against 6.60% at R = 20.
- **The gatekeeper hold at 120 s** leaves the observer unchanged and opens small leads for the validator and the content server at R = 20 and 100 (+0.13 to +0.35).
  - It costs about 26 seconds.
  - It gives no gain in accuracy over InternalCompromiseRun.

## F and I submitting together

Real records at 60 decoys, 20 runs per cell (`results/pair_gaps.json`). Each entry gives the range over R = 1, 20 and 100.

| Build | Within 5 s at submission | Within 5 s as they leave | Separated pairs put back in one bundle |
|---|---|---|---|
| InternalCompromiseRun | 3.7% to 4.0% | 25.3% to 26.3% | 22.5% to 23.3% |
| without the post-match lottery | 21.3% to 21.8% | 30.8% to 31.4% | 11.8% to 12.5% |
| without registry bundling | 3.7% to 4.0% | 3.7% to 4.0% | not applicable |
| without role-aware holds | 8.2% to 8.6% | 50.1% to 51.2% | 45.9% to 46.7% |
| without all five | 31.2% to 31.7% | 31.2% to 31.7% | not applicable |
| role-aware holds at 360 s | 2.0% to 2.2% | 14.4% to 14.9% | 12.7% to 13.1% |

- **The post-match lottery separates F's and I's submissions.**
  - Without it, 21% to 22% of pairs submit within 5 seconds of each other; with it, 4%.
  - Removing it changes the observer's and the strongest component's accuracy by at most 0.12 points.
- **Registry bundling puts about a quarter of the separated pairs back into one bundle.** Under InternalCompromiseRun, 25% to 26% of pairs leave the registry together.

## Checks and controls

- **Timing.** Measured on 10 runs at R = 20 (`results/timing_check.json`). Every stage's mean lies within 1.2 seconds of its target, and every maximum sits at its cap. The full table is in `README.md`.
- **Outcome-shuffle control.**
  - In 25 of the 210 component-and-cell rows across the ten builds, the shuffled-outcome AUC interval excludes 0.5. About 10 would be expected by chance.
  - Every one lies within 0.013 of 0.5. Confidence AUCs within 0.03 of 0.5 are not read as signal, because permuting within a run keeps each run's success rate, so a small association between runs can survive the shuffle.

## Scope

- **One decoy level (60).** At 60 decoys every build passes the claim criterion. At lower decoy levels the mechanisms may matter for the criterion itself, as well as for the leads.
- **Single compromised component.** Collusion between components is not modelled.
- **The board's posting order is not modelled as a vantage.**

# Permitted Overlap

The build `permitted_overlap` changes one thing from InternalCompromiseRun: the role draw. The routing design guarantees only that the three first relays are distinct, that the three destinations are distinct, and that the three nodes of one path are distinct. The build draws roles under exactly those guarantees.

- **Role draw.** C, F and I are the baseline's destinations: distinct, never an active gatekeeper. The relays are drawn in order, each uniform over the nodes its constraints allow: A, then D, then G, pairwise distinct and each different from its own path's destination; then B, E and H, each different from its own path's first relay and destination. A first relay may be another path's destination. A second relay may be another path's first relay, second relay or destination. A gatekeeper may relay.
- **Pairing.** The relays come from their own random stream. Every other draw is the same as in InternalCompromiseRun, so every vantage pairs with it record by record.
- **Rotation.** Every node is compromised in every run, for the first hops, the credential processor and the combined view.
- **Combined view.** One compromised node scores every record with all the evidence its roles give it:
  - its own hold, on the candidates it relayed as a first hop;
  - its content arrival, on the records that name it as F or I;
  - its credential-processor mixture over its own transactions;
  - its postings, if it is an active gatekeeper.

  The pieces combine as likelihood ratios against the passive observer: log g(y) plus, for each role, log L(role) minus log g(y). A second relay holds no evidence in this framework. Decisions are classed by the roles the node held in the record's own transaction.
- **Identifiable and oracle-conditioned.** A class is identifiable when the node held a destination role (C, F or I) in the record's transaction. The node reads the plaintext hash there, so it can select those records. Every other class is oracle-conditioned. It is a single-role lead on a subset the node cannot select, and it is not an attack.

R = 1, 20 and 100 real transactions in flight with 60 decoys; 200 runs per cell. Every class in every cell meets the stability rule. Full tables: `results/tables_permitted_overlap.md`.

## Summary

1. **Over every record a node can select, the combined view does not lead the observer by more than a tenth of a point.** A node can select the records for which it held a destination role, 15.00% of its decisions. Its lead there is -0.25 [-0.42, -0.06] at R = 1, +0.09 [-0.07, +0.25] at R = 20 and +0.09 [+0.04, +0.14] at R = 100.
2. **Inside those records, the classes in which the node also held a first relay lead by more than a quarter of a point.** The node cannot select them: it cannot tell which records it relayed.
   - Credential first relay with a content destination leads by +1.46 [+0.50, +2.44] at R = 1, +1.16 [+0.35, +1.98] at R = 20 and +1.06 [+0.75, +1.36] at R = 100.
   - Content first relay with a content destination leads by +0.74 [+0.47, +1.01] at R = 100 and +0.90 [-0.05, +1.82] at R = 20.
   - Each class covers about 0.5% of a node's decisions. The node names the device 4.47% of the time against the observer's 3.41% at R = 100.
   - A first relay's evidence favours the candidates it forwarded. That raises accuracy on the records it took part in and lowers it on the others: on every record where the node held a first relay the lead is +0.58, +0.68 and +0.44, and on every other record -0.09, -0.05 and -0.01.
3. **With a content destination, the combined lead exceeds the sum of the two single-role leads.** For the credential first relay with a content destination, combined minus the sum is +1.74 [+1.01, +2.49] at R = 1 and +0.45 [+0.21, +0.70] at R = 100. A content destination knows the content arrival of the record that names it, and that evidence combines with the first relay's on the same candidates.
4. **With the credential destination, the combined lead equals the first relay's alone.** C cannot select the record, because the record does not name it. Its mixture over all its transactions adds nothing on any candidate: combined minus the sum is +0.00 [-0.22, +0.22], +0.02 [-0.16, +0.20] and -0.05 [-0.10, +0.00].
5. **Across every record a node scores, the combined view equals the observer:** -0.06 [-0.15, +0.03], -0.01 [-0.09, +0.06] and +0.01 [-0.01, +0.04] points.
6. **No single-role vantage changes.** Every single-role paired effect against InternalCompromiseRun lies within ±0.10 points. The largest single-role lead is the content server at R = 100, +0.22 [+0.15, +0.28].
7. **Every single-role vantage and every identifiable class passes the claim criterion in every cell.** One oracle-conditioned class fails: gatekeeper with a second relay at R = 1, with coverage 0.139% on a top group of 151 decisions.

## How often roles coincide

The role draw alone, 100,000 transactions per pool, three active gatekeepers (`results/overlap_counts.json`).

| Pool | Any node on two paths | First relay is another path's destination | Second relay holds another path's role | Gatekeeper relays | One node on two paths | One node: first relay and destination |
|---|---|---|---|---|---|---|
| 20 nodes | 73.91% | 29.98% | 59.72% | 66.40% | 5.58% | 1.88% |
| 50 nodes | 36.90% | 12.09% | 27.55% | 32.26% | 0.84% | 0.27% |
| 100 nodes | 19.63% | 5.87% | 14.43% | 16.98% | 0.20% | 0.06% |

At 20 nodes, a first relay is another path's destination in:
- 29.98% of simulated transactions;
- 29.83% exactly, under the sequential draw;
- 30.46% under a uniform draw over all valid combinations (`RoutingModels/coincidence_exact.py`).

The sequential draw fixes the destinations first and then gives each first relay an equal chance among the nodes left to it, which weights the valid combinations unequally.

## Records a node can select

The node held a destination role (C, F or I) in the record's transaction. The split below is by whether it also held a first relay, which it cannot tell.

| R | Records | Prevalence | Device named | Observer | Lead | Decisions | Top 1% group | Claim |
|---|---|---|---|---|---|---|---|---|
| 1 | every record the node can select | 15.00% | 9.70% | 9.95% | -0.25 [-0.42, -0.06] | 119,571 | 1,196 | pass |
| 1 | every record, first relay held | 4.81% | 10.66% | 10.08% | +0.58 [+0.33, +0.82] | 38,327 | 383 | pass |
| 1 | every record, no first relay held | 95.19% | 9.85% | 9.94% | -0.09 [-0.18, -0.00] | 758,813 | 7,588 | pass |
| 20 | every record the node can select | 15.00% | 6.56% | 6.47% | +0.09 [-0.07, +0.25] | 125,184 | 1,252 | pass |
| 20 | every record, first relay held | 4.79% | 7.03% | 6.35% | +0.68 [+0.46, +0.89] | 39,970 | 400 | pass |
| 20 | every record, no first relay held | 95.21% | 6.43% | 6.48% | -0.05 [-0.12, +0.03] | 794,590 | 7,946 | pass |
| 100 | every record the node can select | 15.00% | 3.58% | 3.49% | +0.09 [+0.04, +0.14] | 622,710 | 6,227 | pass |
| 100 | every record, first relay held | 4.80% | 3.90% | 3.47% | +0.44 [+0.37, +0.51] | 199,460 | 1,995 | pass |
| 100 | every record, no first relay held | 95.20% | 3.48% | 3.49% | -0.01 [-0.03, +0.01] | 3,951,940 | 39,519 | pass |

## Identifiable classes

The node held a destination role in the record's transaction and can select those records. A pair class is also defined by the node's other role, which it cannot tell. The lead the node can realise is the lead over every record it can select, in the table above.

- Leads are in points [95% CI], over the passive observer on the same records.
- Prevalence is the class's share of a node's decisions.
- First relay alone and destination alone are those single-role vantages for the same node on the same records.

| R | Roles held | Prevalence | Device named | Observer | Combined lead | First relay alone | Destination alone | Combined minus the sum | Decisions | Top 1% group | Claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | credential first relay + content destination | 0.49% | 11.65% | 10.19% | +1.46 [+0.50, +2.44] | +0.20 [-0.31, +0.76] | -0.49 [-1.32, +0.32] | +1.74 [+1.01, +2.49] | 3,904 | 39 | pass |
| 1 | content first relay + content destination | 0.53% | 10.67% | 9.89% | +0.78 [-0.12, +1.70] | +0.82 [+0.23, +1.39] | +0.12 [-0.70, +0.94] | -0.16 [-0.98, +0.64] | 4,247 | 42 | pass |
| 1 | content first relay + credential destination | 0.53% | 10.46% | 10.27% | +0.19 [-0.33, +0.72] | +0.24 [-0.35, +0.78] | -0.05 [-0.21, +0.12] | +0.00 [-0.22, +0.22] | 4,216 | 42 | pass |
| 1 | second relay + destination | 1.39% | 9.51% | 10.07% | -0.55 [-1.04, -0.06] | -0.31 [-0.53, -0.10] | -0.17 [-0.60, +0.27] | -0.07 [-0.35, +0.21] | 11,046 | 110 | pass |
| 1 | three or more roles, with a destination | 0.13% | 9.30% | 9.20% | +0.10 [-1.28, +1.53] | +0.59 [-0.38, +1.48] | -0.20 [-1.59, +1.14] | -0.30 [-1.26, +0.72] | 1,011 | 10 | pass |
| 1 | destination only | 11.94% | 9.57% | 9.92% | -0.35 [-0.55, -0.15] | -0.11 [-0.19, -0.03] | -0.07 [-0.26, +0.11] | -0.17 [-0.27, -0.07] | 95,147 | 951 | pass |
| 20 | credential first relay + content destination | 0.50% | 7.98% | 6.82% | +1.16 [+0.35, +1.98] | +0.73 [+0.24, +1.22] | +0.12 [-0.70, +0.95] | +0.31 [-0.40, +0.99] | 4,137 | 41 | pass |
| 20 | content first relay + content destination | 0.50% | 7.52% | 6.62% | +0.90 [-0.05, +1.82] | +0.21 [-0.33, +0.75] | +0.21 [-0.60, +1.02] | +0.47 [-0.29, +1.22] | 4,214 | 42 | pass |
| 20 | content first relay + credential destination | 0.53% | 6.90% | 6.63% | +0.27 [-0.21, +0.75] | +0.23 [-0.24, +0.72] | +0.02 [-0.14, +0.18] | +0.02 [-0.16, +0.20] | 4,392 | 44 | pass |
| 20 | second relay + destination | 1.42% | 6.67% | 6.37% | +0.30 [-0.10, +0.69] | +0.14 [-0.06, +0.34] | +0.40 [+0.01, +0.79] | -0.25 [-0.48, +0.00] | 11,831 | 118 | pass |
| 20 | three or more roles, with a destination | 0.13% | 5.89% | 4.97% | +0.92 [-0.27, +2.09] | +0.09 [-0.74, +0.91] | +0.18 [-0.81, +1.18] | +0.64 [-0.46, +1.69] | 1,087 | 11 | pass |
| 20 | destination only | 11.93% | 6.43% | 6.47% | -0.04 [-0.21, +0.14] | -0.11 [-0.18, -0.04] | +0.11 [-0.05, +0.27] | -0.04 [-0.11, +0.03] | 99,523 | 995 | pass |
| 100 | credential first relay + content destination | 0.50% | 4.47% | 3.41% | +1.06 [+0.75, +1.36] | +0.42 [+0.26, +0.58] | +0.18 [-0.09, +0.45] | +0.45 [+0.21, +0.70] | 20,742 | 207 | pass |
| 100 | content first relay + content destination | 0.51% | 4.22% | 3.49% | +0.74 [+0.47, +1.01] | +0.22 [+0.07, +0.36] | +0.21 [-0.04, +0.46] | +0.31 [+0.10, +0.51] | 21,311 | 213 | pass |
| 100 | content first relay + credential destination | 0.53% | 3.66% | 3.49% | +0.17 [+0.01, +0.34] | +0.24 [+0.08, +0.41] | -0.02 [-0.05, +0.01] | -0.05 [-0.10, +0.00] | 22,021 | 220 | pass |
| 100 | second relay + destination | 1.40% | 3.48% | 3.50% | -0.02 [-0.15, +0.12] | -0.05 [-0.12, +0.02] | +0.11 [-0.02, +0.24] | -0.08 [-0.17, +0.01] | 57,951 | 580 | pass |
| 100 | three or more roles, with a destination | 0.13% | 4.01% | 3.57% | +0.45 [-0.06, +0.94] | +0.20 [-0.06, +0.45] | +0.06 [-0.35, +0.45] | +0.19 [-0.13, +0.52] | 5,385 | 54 | pass |
| 100 | destination only | 11.93% | 3.52% | 3.49% | +0.03 [-0.02, +0.08] | -0.05 [-0.08, -0.03] | +0.15 [+0.10, +0.20] | -0.07 [-0.10, -0.04] | 495,300 | 4,953 | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

## Oracle-conditioned classes

The node held only relay or gatekeeper roles, or none, in the record's transaction. It cannot select those records.

| R | Roles held | Prevalence | Device named | Observer | Lead | Decisions | Top 1% group | Claim |
|---|---|---|---|---|---|---|---|---|
| 1 | second relay + first relay | 1.15% | 10.71% | 10.09% | +0.62 [+0.25, +0.99] | 9,188 | 92 | pass |
| 1 | gatekeeper + first relay | 2.10% | 10.45% | 10.05% | +0.40 [+0.11, +0.69] | 16,772 | 168 | pass |
| 1 | gatekeeper + second relay | 1.90% | 9.86% | 9.92% | -0.06 [-0.30, +0.18] | 15,137 | 151 | fail (coverage 0.139%) |
| 1 | second relay + second relay | 0.51% | 9.67% | 9.94% | -0.27 [-0.68, +0.12] | 4,104 | 41 | pass |
| 1 | three or more roles, no destination | 0.41% | 9.91% | 9.24% | +0.67 [+0.03, +1.34] | 3,278 | 33 | pass |
| 1 | one relay or gatekeeper role | 29.23% | 10.08% | 9.95% | +0.13 [+0.02, +0.25] | 232,971 | 2,330 | pass |
| 1 | no role | 49.69% | 9.79% | 9.95% | -0.16 [-0.23, -0.08] | 396,119 | 3,961 | pass |
| 20 | second relay + first relay | 1.15% | 6.61% | 6.08% | +0.53 [+0.23, +0.82] | 9,629 | 96 | pass |
| 20 | gatekeeper + first relay | 2.11% | 6.95% | 6.25% | +0.70 [+0.42, +0.98] | 17,598 | 176 | pass |
| 20 | gatekeeper + second relay | 1.87% | 6.52% | 6.71% | -0.19 [-0.41, +0.03] | 15,591 | 156 | pass |
| 20 | second relay + second relay | 0.51% | 6.30% | 6.21% | +0.09 [-0.23, +0.41] | 4,285 | 43 | pass |
| 20 | three or more roles, no destination | 0.41% | 7.08% | 6.82% | +0.26 [-0.29, +0.81] | 3,418 | 34 | pass |
| 20 | one relay or gatekeeper role | 29.27% | 6.52% | 6.51% | +0.02 [-0.07, +0.11] | 244,267 | 2,443 | pass |
| 20 | no role | 49.68% | 6.36% | 6.46% | -0.10 [-0.15, -0.04] | 414,588 | 4,146 | pass |
| 100 | second relay + first relay | 1.16% | 3.78% | 3.49% | +0.30 [+0.20, +0.39] | 48,122 | 481 | pass |
| 100 | gatekeeper + first relay | 2.10% | 3.82% | 3.46% | +0.36 [+0.28, +0.44] | 87,264 | 873 | pass |
| 100 | gatekeeper + second relay | 1.88% | 3.51% | 3.56% | -0.05 [-0.12, +0.02] | 78,203 | 782 | pass |
| 100 | second relay + second relay | 0.52% | 3.59% | 3.70% | -0.10 [-0.21, +0.01] | 21,507 | 215 | pass |
| 100 | three or more roles, no destination | 0.41% | 3.47% | 3.38% | +0.09 [-0.08, +0.26] | 17,165 | 172 | pass |
| 100 | one relay or gatekeeper role | 29.22% | 3.55% | 3.48% | +0.06 [+0.04, +0.10] | 1,213,242 | 12,132 | pass |
| 100 | no role | 49.70% | 3.43% | 3.49% | -0.06 [-0.08, -0.04] | 2,063,187 | 20,632 | pass |

A top group of fewer than 50 decisions cannot resolve the criterion. A failure there reflects the size of the group.

The oracle-conditioned classes with a first relay lead by about as much as a first relay leads on the records it took part in. That lead already exists in InternalCompromiseRun: +0.90, +0.65 and +0.42 points at R = 1, 20 and 100. A first relay cannot identify those records, so it is scored on every record, where its lead is -0.02 to +0.01.

## Single-role vantages

Leads over the passive observer, in points [95% CI]. The four-node column restricts the same decisions to the four nodes per run that InternalCompromiseRun compromises.

| Vantage | R | Every node | Four nodes per run | InternalCompromiseRun |
|---|---|---|---|---|
| First hop, credential | 1 | -0.04 [-0.10, +0.03] | -0.04 [-0.12, +0.04] | -0.02 [-0.11, +0.06] |
| First hop, credential | 20 | -0.02 [-0.07, +0.03] | -0.08 [-0.15, -0.01] | +0.01 [-0.07, +0.09] |
| First hop, credential | 100 | -0.00 [-0.02, +0.01] | -0.01 [-0.04, +0.01] | -0.01 [-0.04, +0.01] |
| Credential processor | 1 | +0.01 [-0.03, +0.06] | +0.02 [-0.03, +0.07] | +0.00 [-0.05, +0.05] |
| Credential processor | 20 | -0.02 [-0.06, +0.01] | -0.03 [-0.07, +0.01] | -0.01 [-0.04, +0.03] |
| Credential processor | 100 | -0.00 [-0.01, +0.00] | -0.00 [-0.01, +0.01] | -0.01 [-0.02, +0.00] |

The first hop for content gives the same values as the first hop for credentials. Validator, gatekeeper and content server leads under `permitted_overlap` are -0.53, -0.24 and -0.04 (validator), +0.05, -0.05 and -0.00 (gatekeeper), and -0.13, +0.20 and +0.22 (content server) at R = 1, 20 and 100. Paired against InternalCompromiseRun on the same records, every single-role effect lies within ±0.10 points.

## Controls

- **Negative control.** Within each run the device labels of every candidate and every validator reply are permuted at random (`results/shuffle_control.json`, 20 runs per cell). For every vantage in every cell, the 95% interval on accuracy contains the feasible chance rate. The combined view names the device 1.27% [0.91, 1.64] of the time against a feasible chance rate of 1.40% at R = 1, 0.93% [0.71, 1.14] against 1.09% at R = 20, and 0.56% [0.49, 0.63] against 0.54% at R = 100.
- **Positive control, content half.** With every hold and lottery off (`overlap_no_holds`, 50 runs per cell), the combined view on a first relay with a content destination names the device far more often than the observer: 84.14% against 61.87% at R = 1 (952 decisions), 80.08% against 54.51% at R = 20 (1,009) and 62.79% against 30.59% at R = 100 (5,103). The lead comes from the destination: with no relay hold, a first relay's own hold carries nothing.
- **Positive control, first-relay half, credential path.** Only the relay holds (120 s) and the device's credential hold (240 s) are on (`first_relay_signal_cred`, 100 runs per cell). The record time then follows the credential path. On the credential first relay with a content destination, the combined lead is +4.78 [+3.08, +6.41] (1,945 decisions), +2.55 [+1.09, +4.01] (2,039) and +2.17 [+1.67, +2.65] (10,252), against a destination-alone lead of +0.46, +0.64 and +0.34. Combined minus the sum is +3.08 [+1.76, +4.39], +0.05 [-1.03, +1.18] and +1.21 [+0.85, +1.58].
- **Positive control, first-relay half, content path.** Only the relay holds (120 s) and the device's content holds (240 s) are on (`first_relay_signal_content`, 300 runs at R = 1 and 100 runs at R = 20 and 100). The record time then follows the content paths. On the content first relay with the credential destination, the combined lead is +2.07 [+1.49, +2.67] (6,333 decisions), +2.08 [+1.31, +2.84] (2,117) and +0.75 [+0.46, +1.03] (11,064), against a destination-alone lead of -0.03, +0.09 and +0.05. Combined minus the first relay alone is -0.17 [-0.39, +0.05], -0.14 [-0.38, +0.09] and -0.04 [-0.11, +0.03].
- **The two first-relay controls differ in the destination half.** The content destination's evidence adds to the first relay's on the same candidate. The credential destination's adds nothing.
- **First relays by path.** Each first relay's lead on the records it took part in, at R = 1, 300 runs per control on run ids 2,000 to 2,299 (`results/controls/first_relay_paths.json`, 60,345 decisions per path):

  | Timing signal on | A | D | G |
  |---|---|---|---|
  | credential path | +1.42 [+1.25, +1.58] | +0.55 [+0.41, +0.70] | +0.56 [+0.42, +0.70] |
  | both content paths | +2.01 [+1.82, +2.20] | +2.41 [+2.21, +2.61] | +2.41 [+2.19, +2.60] |
  | F content path only | +2.43 [+2.24, +2.62] | +1.92 [+1.73, +2.11] | +1.95 [+1.76, +2.14] |

  A first relay's lead does not follow whether its own path carries the timing signal. With the signal on the F path only, D (on that path) and G (on the other) lead by the same amount, and A leads by more. The lead is set by the control as a whole. With the signal on both content paths, D and G lead by +2.41 on held-out runs, which reproduces the content-path control's +2.24 for the first relay alone at R = 1.

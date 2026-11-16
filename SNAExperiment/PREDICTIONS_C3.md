# Predictions for C3: decoy knowledge, coalitions, decoy concentration and decoy volume

Written before the run. A prediction counts as made before the run once this file is committed. Each item states the prediction, its basis, what counts as a failure, and whether it can fail.

C3 has cells R = 1 and 100 for every item, and R = 300 for items 1 and 2. Traffic, seeds and models are those of C2 unless an item changes the traffic.

## Parameters

| Parameter | Value | Reason |
|---|---|---|
| Decoy operators | Two. Each decoy identity belongs to one, drawn with probability one half from a seed set by the configuration and the run id | As the protocol describes the decoy infrastructure |
| Decoy concentration factors | 1, 5 and 25 | 1 is C2. 5 and 25 give 20 and 4 decoy identities at R = 1 |
| Decoy volume | 100, 50, 10 and 0 decoys in flight | 100 is C2. 0 is no cover |
| Same-role coalitions | First relays and second relays: 2, 3 and 6 nodes. Gatekeepers: two of the three active, and all three. F with I: the record's own F and I | Several nodes in one role. 6 of 20 is about one third |
| Compromised nodes | k = 1 to 6 nodes, each in every role it holds | Up to about one third of 20 nodes |
| Choice of the nodes | One set per run, per vantage and per k, uniform over the nodes the role allows, from a seed set by the configuration, the cell and the run id | Every node is as likely as any other |
| Rate model of the discounting attacker | Poisson counts of captures per source address over the run's observed span, with one rate for a real device and one for a decoy identity, both built on the model seeds | The attacker knows the rates, as it knows the hold distributions |

## Sources of numbers

- **C2:** `results/C2`, the committed run. Its observer rates are 4.77%, 2.33% and 1.39% at R = 1, 100 and 300, with chance 1.11%, 0.55% and 0.28%.
- **Model-seed numbers:** the main configuration simulated on seeds from 1,700,000,000, which no evaluation run and no model uses. 3 runs at R = 1 and 20 runs at R = 100. No attacker was run on them.

## Arithmetic used throughout

**Feasibility.** A device is feasible for a record when one of its packets could have produced it. Each identity is feasible with the same probability p, because every identity captures at the same rate. Chance is E[1 / (1 + Bin(n, p))] = (1 − (1 − p)^(n+1)) / ((n + 1) p), with n the other identities. C2's chance gives p = 0.892 at R = 1, 0.883 at R = 100 and 0.869 at R = 300.

**Competition.** A device-named rate of the form 1 / (1 + N b), where N is the number of other identities and b a constant per vantage and cell. b comes from C2. At R = 1 the observer gives b = 0.1996. With that b, the formula gives 2.39% at R = 100 (C2: 2.33%) and 1.21% at R = 300 (C2: 1.39%). So it holds within about 15%. Removing decoys removes their share of N.

**Bound from the posting schedule.** The registry posts records every 120 s, and every record posted at one boundary carries the same time. No vantage that names a device from the record time can tell two records of one posting apart. Records are posted at (R + 100) / D per second, so a posting holds on average λ = 120 (R + 100) / D other records: 10.37 at R = 1, 20.54 at R = 100 and 41.09 at R = 300. Finding one record is then right at most E[1 / (1 + Poisson(λ))] = (1 − e^(−λ)) / λ of the time: 9.64%, 4.87% and 2.43%. Naming a device is right at most E[k / n] of the time, where n is the records in the posting and k those of the record's device, because a device can have more than one record in a posting. A device makes 0.10 records per posting, so this bound is 10.5% at R = 1, 5.3% at R = 100 and 2.67% at R = 300 (Poisson arithmetic, 400,000 draws). Model-seed numbers agree: a real record shares its posting with 21.4 records on average at R = 100, and E[1 / size] is 4.88%. The bound does not hold for a vantage that learns more than the time of each record, such as a party with a cryptographic link.

## 1. Decoy knowledge: chance

**Prediction.** Chance in each variant:

| Variant | R = 1 | R = 100 | R = 300 |
|---|---|---|---|
| None known (C2) | 1.11% | 0.55% | 0.28% |
| One operator's decoys known | 2.20% | 0.73% | 0.32% |
| Both operators' decoys known | 100% | 1.10% | 0.37% |
| Validator with a record-keeping manufacturer (validator only) | 100% | 1.10% | 0.37% |

**Basis.** The feasibility formula, with n the identities left. One operator holds Bin(100, 1/2) decoy identities, 50 on average. At R = 1 there is one real device, so with both operators' decoys known it is the only candidate.

**Fails if** any measured chance differs from its value by more than 10% of that value.

**Can fail.** The split is random per run, and feasibility may not be the same for every identity.

## 2. Decoy knowledge: device-named accuracy

**Prediction.**

| Variant | Vantage | R = 1 | R = 100 | R = 300 |
|---|---|---|---|---|
| None known | every vantage | equal to C2, decision by decision | equal to C2 | equal to C2 |
| One operator known | Passive observer | 9.1% (7.3% to 10.9%), ×1.91 | 3.1% (2.5% to 3.7%), ×1.33 | 1.6% (1.3% to 1.9%), ×1.14 |
| One operator known | Validator | 10.0% (8.0% to 12.0%) | 3.5% (2.8% to 4.2%) | 1.7% (1.4% to 2.1%) |
| One operator known | Content server | 10.5% (8.4% to 12.6%) | 3.7% (2.9% to 4.4%) | 1.9% (1.5% to 2.2%) |
| Both known | Passive observer | 100% | 4.6% (3.7% to 5.5%), ×1.96 | 1.85% (1.5% to 2.2%), ×1.33 |
| Both known | Validator | 100% | 5.2% (4.2% to 6.3%) | 2.0% (1.6% to 2.4%) |
| Validator with a record-keeping manufacturer | Validator | 100% | 5.2% (4.2% to 6.3%) | 2.0% (1.6% to 2.4%) |

Every other vantage moves by the same multiple as the observer, within the same ±20%. The leads over the observer keep their sign. The one-operator multiple at R = 1 is about 2, so it falls on the dividing line of the pre-registered reading (less than 2 times, or more).

**Basis.** The competition formula with C2's b for each vantage, and N the other identities left: 100, 50 and 0 at R = 1; 205, 153.5 and 102 at R = 100; 410, 358.5 and 307 at R = 300. The ranges are ±20%, which covers the formula's 15% miss at R = 300. Every rate at R = 1 with both operators known is 100% because one device is left, not because of any timing.

**Fails if** a variant's rate lies outside its range, or "none known" differs from C2 in any decision.

**Can fail.** The formula treats every decoy identity as an equal competitor. If decoys that sit close in time to real records compete more than the average, the gain is larger.

## 3. Coalition vantages

The combined-view machinery multiplies a node's likelihood ratios across the roles it held in a record's transaction. A coalition holds the roles of both its parties.

**Prediction.**

| Coalition (class) | R = 1 | R = 100 | R = 300 |
|---|---|---|---|
| Validator with a gatekeeper (every record) | 6.0% to 10.5%, lead +1.2 to +5.7 points | 3.0% to 5.3%, lead +0.7 to +3.0 points | 1.5% to 2.67% |
| Validator with C (records whose credential path ended at that node) | 25% to 65% | 15% to 45% | 8% to 35% |
| First relay with C on its path | 88% to 100% | 80% to 99% | 65% to 97% |
| First relay with F or I on its path | 100% | 100% | 100% |

Every coalition rate is at least the larger of its two parties' rates, within its interval.

**Basis.**
- Validator with a gatekeeper. Every transaction passes all three gatekeepers. The validator names the device of every credential, and the gatekeeper knows when each of its postings left. Together they know each transaction's device and posting time. The record still carries only its time, so the bound from the posting schedule caps the coalition: 10.5%, 5.3% and 2.67%. Its floor is the validator alone (C2: 5.26%, 2.66% and 1.52%), plus the gatekeeper's timing. The range runs from just above the validator to the bound.
- Validator with C. C sends CV-1 and receives CV-2 for its own transactions, so the coalition knows the device of each one, and when C fanned it out. C handles 1/17 of transactions: 0.0051 per second at R = 1 and 0.0101 at R = 100. From fan-out to record, about 600 s holds most of the spread, so about 3 (R = 1) and 6 (R = 100) of C's transactions compete for each record. The record's own posting narrows this to the few in one 120 s slot. The rate is then about one over the competitors with a plausible slot: 1/3 to 2/3 at R = 1. This class is not capped by the posting schedule, because only one of the 10 to 20 records in a posting usually comes from C's transactions.
- A first relay and the destination on its own path share a packet. A relay decrypts its transit layer and forwards the rest, so the inner packet (CredP, ContP_F or ContP_I) is byte-identical at the first relay and at the destination. Its ciphertext is fresh for every packet, so the pair matches it exactly, with no timing, and the first relay holds the source address it came from.
- First relay with F or I. F holds the record's ContentHash, so the pair names the device of every record whose content path it holds: 100%.
- First relay with C. The pair names the device of each of C's transactions that came through A. C holds FullPacketHash, which the record does not carry, so the link from transaction to record is still timing: as a Registry Node C reads the match boards and finds its transaction's postings by FullPacketHash. The competitors are C's other transactions that also came through A, at (R + 100) / D / 17 / 19 per second: 2.7 × 10^−4 at R = 1, 5.3 × 10^−4 at R = 100 and 1.06 × 10^−3 at R = 300. The record time after quorum has most of its mass within about 600 s, so 0.16, 0.32 and 0.64 compete on average. With equal weights the rate would be (1 − e^(−x)) / x: 92%, 86% and 74%. The record time's density separates some of them, so each range runs from a little below that to near certain.

**Fails if** a class rate lies outside its range, or a coalition rate is reliably below either party's rate.

**Can fail.** The validator-with-C range rests on a rough count of competitors. The first relay with F or I fails only if the model of the exact link is wrong. A class with few records may not meet the stability rule, and is then reported as unstable, not judged.

## 4. Decoy concentration

**Prediction.** Decoy identities and chance:

| Factor | Identities, R = 1 | Chance, R = 1 | Identities, R = 100 | Chance, R = 100 |
|---|---|---|---|---|
| 1 | 100 | 1.11% | 103 | 0.55% |
| 5 | 20 | 4.76% | 21 | 0.89% |
| 25 | 4 | 20.0% | 4 | 1.05% |

Passive observer without the discount:

| Factor | R = 1 | R = 100 |
|---|---|---|
| 1 | equal to C2 | equal to C2 |
| 5 | 3% to 15% | 1.5% to 2.6% |
| 25 | 0.5% to 10%, below chance | 1.2% to 2.6% |

Passive observer with the discount: at least 99% at R = 1 at factors 5 and 25. At R = 100 it is 3.7% to 5.5% at factors 5 and 25, the same as both operators' decoys known (item 2).

**Basis.** The decoy volume stays at 100 in flight, so each identity at factor f captures at f times a device's rate, and is feasible almost surely. Without the discount the observer sums each device's likelihood over its packets. An identity at 25 times the rate has 25 times the packets near any record, so the 4 decoys outscore the one real device almost always. That puts the rate below chance. With the discount the attacker counts each address's captures over the observed span. At R = 1 the span is about 66 hours: the real device makes about 204 captures, a decoy at factor 5 about 1,020. The Poisson counts do not overlap, so every decoy is discounted away and one candidate is left. At R = 100 the span is 8,834 s: a device makes Poisson(7.4) captures, a decoy at factor 5 Poisson(36.8). P(a device count of 19 or more) is about 3 × 10^−4 and P(a decoy count of 18 or fewer) about 5 × 10^−4, so again the decoys are removed.

**Fails if** a measured chance differs from its value by more than 10%, the discounted rate at R = 1 is below 99%, or a rate lies outside its range.

**Can fail.** The undiscounted ranges are wide because the argument gives a direction, not a value.

## 5. Decoy volume

**Prediction.**

| Volume | Chance, R = 1 | Passive observer, R = 1 | Chance, R = 100 | Passive observer, R = 100 |
|---|---|---|---|---|
| 100 | 1.11% | equal to C2 | 0.55% | equal to C2 |
| 50 | 2.20% | 9.1% (7.3% to 10.9%) | 0.73% | 3.1% (2.5% to 3.7%) |
| 10 | 10.2% | 33% (25% to 42%) | 1.00% | 4.2% (3.3% to 5.0%) |
| 0 | 100% | 100% | 1.10% | 4.6% (3.7% to 5.5%) |

Every component vantage moves by the same multiple as the observer, within ±20%. At volume 0 and R = 1 every vantage names the device on every record, and fails the claim criterion.

**Basis.** The feasibility and competition formulas with 50, 10 and 0 decoy identities. Volume 50 is the same arithmetic as one operator known in item 2, and volume 0 the same as both known.

**Fails if** a chance differs by more than 10%, or a rate lies outside its range.

**Can fail.** At volume 10 and R = 1 the formula is far from C2's operating point. The range is wider there.

## 6. Sanity

**Prediction.** With default options the code reproduces C2's R = 1 decisions exactly. In every cell and variant, the counts in flight are within 3% of their targets.

**Basis.** New behavior sits behind new options whose defaults are C2's. New randomness comes from streams C2 does not draw from.

**Fails if** any R = 1 decision differs, or a count in flight is off by more than 3%.

**Can fail.** A new option that draws from a C2 stream would change every later draw.

## 7. Same-role coalitions

Each coalition pools what its nodes see in one role, on top of the passive observer's view of the wire.
- **First relays.** Each node knows its own hold of every packet it relayed first. The holds of different nodes are of different packets, so they add.
- **Second relays.** Each node knows, for every packet it relayed second, which node it came from, when it arrived, and when it left. With the wire this gives the time the packet reached its destination. The coalition does not know which device packet it was: that is the first relay's hold, which it weighs by the hold density.
- **Gatekeepers.** Two gatekeepers know the later of their two postings of every transaction; three know every transaction's quorum (the second posting). A transaction is linked to a device packet only by timing, as for one gatekeeper.
- **F with I.** The record's own F and I each know their content packet's arrival and, by the content hash, that it is this record's. Together they know both content packets' arrivals. Each device is scored by the density of each arrival after one of its packets' sends.

**Prediction.** Device-named accuracy, as the lead over the passive observer on the same records, or as a rate:

| Coalition | Records | R = 1 | R = 100 |
|---|---|---|---|
| First relays, 2, 3 or 6 | every class | lead −0.3 to +0.5 points | lead −0.2 to +0.3 points |
| Second relays, 2, 3 or 6 | at least one of the record's second relays held | lead −0.3 to +1.0 points | lead −0.2 to +0.6 points |
| Second relays, 2, 3 or 6 | none held | lead −0.3 to +0.3 points | lead −0.2 to +0.2 points |
| Gatekeepers, two or three | every record | lead −0.3 to +1.5 points | lead −0.2 to +0.8 points |
| F with I | every record | 6.5% to 12.5% (point 9.5%) | 3.3% to 6.5% (point 4.9%) |

Every relay and gatekeeper row stays at or below the bound from the posting schedule (10.5% and 5.3%). F with I is not bound by it.

**Basis.**
- The spread of the record time after a packet's send is 314 s (standard deviation, development seeds). Knowing a first relay's hold removes its variance (51 s), knowing when the packet reached its destination leaves 290 s, and knowing the quorum leaves 266 s.
- The Gaussian score model of `PREDICTIONS_C4.md` item 4 (d = 0.66 at R = 1 and 0.58 at R = 100, fitted to the observer's C2 rates) gives, with d scaled by 314 over the spread that is left: 4.85% and 2.37% for all three first holds known, 5.30% and 2.59% for all three destination arrivals, 5.98% and 2.94% for the quorum. These are upper estimates: they assume the coalition knows which device packet each of its events belongs to. For relays and gatekeepers that link is itself timing, and C2 shows how much that costs: one first hop leads the observer by −0.00 points [−0.03, +0.03] at R = 1, and one gatekeeper by +0.03 [−0.07, +0.10].
- So each relay or gatekeeper range runs from a little below the observer to a little above its upper estimate.
- F with I. C2's content server names the device on 5.53% and 2.78% of the records naming it: d = 0.74 and 0.66 in the same model. Two independent arrivals of one device's packets add their evidence: d √2, which gives 9.5% and 4.9%. The ranges are 0.7 to 1.3 times that.

**Fails if** a row lies outside its range, or a relay or gatekeeper row is above the bound by more than its interval.

**Can fail.** The Gaussian model treats evidence as additive. If the second relays' or gatekeepers' timing links are sharper than one gatekeeper's in C2, their rows can exceed the upper end.

## 8. Compromised nodes

A coalition of k nodes, k = 1 to 6, each in every role it holds in each transaction. It pools everything items 3 and 7 give, and its byte-identical links:
- **Content path held at both ends.** A node is the record's F (or I) and another is that path's first relay. The inner packet is byte-identical at the first relay and the destination, so the pair names the device exactly.
- **Credential path held at both ends.** A node is C and another is A. As item 3: the device of each of C's transactions through A, linked to the record by the time after quorum on the match boards.
- **Destination and second relay.** A node is the record's F (or I) and another is that path's second relay, but not its first relay. The second relay knows the first relay it came from and when. The coalition weighs the device packets that arrived at that first relay by the first relay's hold.
- **Destination only.** A node is the record's F or I, or both, without the above. As F with I in item 7, with one or both arrivals.
- **Timing roles only.** The coalition holds a relay, C or gatekeeper role in the transaction, and none of the above. As items 7 and C2's combined view.
- **No role.** The observer.

**Prediction.** Device-named accuracy per class, with the class's expected share of records at k = 6:

| Class | Share at k = 6 | R = 1 | R = 100 |
|---|---|---|---|
| Content path held at both ends | 15.2% | 100% | 100% |
| Credential path held at both ends | 6.9% | 88% to 100% | 80% to 99% |
| Destination and second relay | 10.2% | 45% to 90% | 30% to 75% |
| Destination only | 23.8% | 5.0% to 12.5% | 2.4% to 6.5% |
| Timing roles only | 43.2% | lead −0.3 to +1.5 points | lead −0.2 to +0.8 points |
| No role | 0.7% | lead −0.3 to +0.3 points | lead −0.2 to +0.2 points |

The shares at k = 2 are 1.1%, 0.5%, 1.0%, 17.4%, 56.4% and 23.6%; at k = 4 they are 6.2%, 3.0%, 5.2%, 24.7%, 56.3% and 4.6%. Over every record, the rate at k = 6 is 29% to 37% at R = 1 and 25% to 33% at R = 100, and it rises with k.

**Basis.**
- Shares: the simulator's path rules (C, F and I from the 17 nodes outside the active gatekeepers; six distinct relays from the other 17), 200,000 draws per k.
- Content path at both ends: the exact link of item 3.
- Credential path at both ends: item 3's range.
- Destination and second relay: device packets reach a first relay at 3 (R + 100) / D / 20 per second. Within its mean hold (60 s) that is 0.78 other packets at R = 1 and 1.54 at R = 100. With equal weights the rate would be (1 − e^(−x)) / x: 69% and 51%. The hold density separates some and confuses others, so the ranges run about 20 points either side.
- Destination only: from C2's content server (5.53% and 2.78%) for one arrival to item 7's F with I for two.
- Timing roles only and no role: item 7 and C2.
- The overall rate is the share-weighted sum of the class ranges.

**Fails if** a class with at least 50 right and 50 wrong decisions lies outside its range, the content-path class is below 100%, or the overall rate does not rise with k.

**Can fail.** The destination-and-second-relay range rests on a rough count. Classes at small k are rare and may not meet the stability rule; they are then reported as unstable, not judged.

## Reporting the bound

Every table shows the bound from the posting schedule beside each row it applies to. Rows with a link from a record to its transaction (F, I, a first relay with F or I, F with I, and the classes of item 8 that hold a destination or both ends of the credential path) are marked not applicable.

## Changes before the run

The device-naming bound was first given as the record bound (9.64%, 4.87% and 2.43%). It is E[k / n], which is about a tenth higher, because a device can have two records in one posting. The validator-with-a-gatekeeper ranges were raised to match.

The first-relay-with-destination rows were first predicted as a timing attack (20% to 60%, 12% to 40% and 6% to 30% with C; 60% to 85%, 45% to 75% and 30% to 65% with F or I). The reason for the change is the specification, not the dry run: its per-leg table and packet layouts carry the same CredP or ContP on every leg of a path, and its relay rule forwards what remains after the transit layer, so the first relay and the destination hold the same bytes. The pair's link is exact. For C the link to the record is still timing, now from the transaction's quorum on the match boards, which C reads as a Registry Node.

Evaluation seeds were used in development. The coalition vantages were debugged on the traffic seeds of runs 1 to 4, and the path coalitions on run 2. The committed dry run used runs 0 and 1. No prediction in this file was changed because of those runs.

Items 7 and 8 were added after the dry run, to answer reviewers who found the attacker too weak. They were written before their code and before any run of them.

A fresh evaluation seed set replaces C2's traffic seeds for every full run of C3 to C5, because C2's were used in development (logged above). A run's traffic seed is the first 8 bytes of SHA-256 of `sna-c3-c5-fresh|R=<R>|run=<run id>`, little-endian, shifted right by one bit. No code ran on these seeds before this entry was committed. From here on, development, debugging and dry runs use model seeds only: a dry run's traffic seed is 1,000,300,000 + 1,000 R + the run id.

The flag for a badly miscalibrated attacker first fired when the calibration error exceeded both 2 points and a quarter of the larger of the accuracy and the mean confidence. A dry run showed that rule flagged sampling noise: with about 60 decisions per confidence decile and hit rates near 4%, sampling alone gives an error near 2 points. The flag now also requires the error to exceed the 99th percentile a perfectly calibrated attacker would reach by sampling at the same confidences. This is a modeling error in the rule; no prediction depends on the flag.

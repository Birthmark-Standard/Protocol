# Predictions for C5: delay marking and drop with resubmission

Written before the run. A prediction counts as made before the run once this file is committed. Each item states the prediction, its basis, what counts as a failure, and whether it can fail.

C5 has cells R = 1 and 100. Flooding is not simulated. The device does not choose its second relays: the device routing table does not name them. Every hold is also drawn per packet, so packets an attacker injects and knows do not change the posterior among the packets it does not know.

## Parameters

| Parameter | Value | Reason |
|---|---|---|
| Target | One real device per run: the real device at R = 1, a device drawn from the run's seed at R = 100 | One target, as the metric defines |
| Window | 67 hours in both cells, so the target makes about 200 transactions per run | At R = 100 a 1-hour window gives the target 3 transactions. R = 1 already uses about 65 hours |
| First relay | Each of the target's transactions is marked by one of its three first relays, drawn at random. The share a fixed node recognises is counted separately | Holds are drawn per packet, so one node's marks do not interact with another's. This gives about 200 marked transactions per run, not 30 |
| Access-network adversary | Marks all three of the target's packets. A second setting marks one packet, drawn at random | All three as specified. One packet is the stronger use of the same position (item 3) |
| Validator | Marks CV-2 of the target's transactions | It recognises the device on the credential path |
| Mark sizes Δ | 0, 60, 300, 600, 900, 1,200, 1,500, 1,800, 2,400 and 3,600 s | From inside the natural spread to past the quorum timeout and past the natural maximum delay |
| Quorum timeouts | 1,800 s (the specification), 1,500 s and 1,200 s | 1,500 s is near the longest natural gap (1,544 s). 1,200 s is about its 99th percentile (1,122 s) |
| Match board window | An option: a board keeps postings for 1,800 s, and F or I cannot confirm against a posting older than that. Off in C2 and by default; reported both ways for content marks | The specification keeps postings for 30 minutes. The simulator does not model it |
| Resubmission | The device waits 2,400 s from capture for its record, then resubmits after an exponential delay with mean 30 minutes, 1 hour, 2 hours or 6 hours. The resubmission is a new transaction with fresh lines and fresh holds, from the same source address | 2,400 s is just past the longest natural delay (2,326 s). No paper gives the delay distribution |

## Sources of numbers

- **C2:** `results/C2`. D = 1,168.2274 s.
- **Model-seed numbers:** the main configuration on seeds from 1,700,000,000, which no evaluation run and no model uses. 3 runs at R = 1 and 20 runs at R = 100 (6,165 real records). No mark and no attacker was run on them. "Best slot" is the share of transactions whose record falls in the single posting slot an attacker would pick, given its act time and the natural delay.

## Arithmetic used throughout

**Bound from the posting schedule.** The registry posts every 120 s, and every record posted at one boundary carries the same time. So no actor can find a record more often than E[1 / (1 + Poisson(λ))], with λ = 120 (R + 100) / D:

- **R = 1:** λ = 10.37, bound 9.64%;
- **R = 100:** λ = 20.54, bound 4.87%.

A mark moves a record to another posting, but every posting at every time is full of other records. A record past the natural maximum delay does not stand out, because no record shows when its capture was made. What a mark can do is make the marked path set the record time. That removes the other paths' spread, as the C2 path controls did.

**Record-finding accuracy** is the share of marked transactions whose record the actor picks. It is the share of marked transactions that finalize, times the best-slot share, times about E[1 / posting size].

**The gap.** The gap is the time F or I learns of quorum minus its content packet's arrival. A transaction drops when the gap exceeds the timeout at F or at I. A credential-side mark adds Δ to both gaps. A content-side mark shortens one gap. A mark on all three packets leaves both unchanged. Model-seed gap at R = 100:

| Statistic | Value |
|---|---|
| Median | 125 s |
| 95th percentile | 842 s |
| 99th percentile | 1,122 s |
| 99.9th percentile | 1,361 s |
| Maximum | 1,544 s |
| Quorum known before content arrives | 38% |

## 1. Shares recognised

**Prediction.** A fixed first relay recognises 15% of the target's transactions (14% to 16%). The access-network adversary and the validator recognise 100%.

**Basis.** A transaction's three first relays are three different nodes of 20, so a given node is one of them with probability 3 / 20.

**Fails if** the first relay's share lies outside 14% to 16%.

**Can fail.** A routing rule that made some nodes first relays more often would show.

## 2. Bound

**Prediction.** No actor, at any Δ or timeout, finds the marked record more often than 9.64% at R = 1 or 4.87% at R = 100, beyond its interval.

**Basis.** The bound from the posting schedule.

**Fails if** any row's interval lies wholly above the bound.

**Can fail.** It fails only if records in one posting can be told apart, which would be a bug or a field the record carries that this file does not know of.

## 3. Unmarked baseline (Δ = 0) and chance

**Prediction.**

| Actor | R = 1 | R = 100 |
|---|---|---|
| First relay | 1.6% (1.1% to 2.3%) | 0.69% (0.45% to 1.0%) |
| Access-network adversary | 1.8% (1.2% to 2.6%) | 0.79% (0.5% to 1.2%) |
| Validator | 2.2% (1.5% to 3.0%) | 1.05% (0.7% to 1.4%) |
| Chance | about 0.6% | about 0.3% |

**Basis.** Model-seed delays from each act to the record:

| Act | Mean | Standard deviation | Best slot, R = 1 | Best slot, R = 100 |
|---|---|---|---|---|
| First relay departure | 890 to 1,000 s | 300 to 310 s | 0.146 to 0.158 | 0.139 to 0.143 |
| Latest of the device's three sends | 800 s | 275 s | 0.168 | 0.162 |
| CV-2 send | 625 s | 320 s | 0.206 | 0.214 |

Times the bound, these give the values. The access-network row uses only the latest send. Using all three sends could raise it by up to a third, and the range allows for that. Chance is one over the records in the support: about 15 slots × 10.4 records at R = 1 and 17 × 20.5 at R = 100.

**Fails if** a baseline lies outside its range.

**Can fail.** The actor scores with the full density, not with one slot, so it may do somewhat better.

## 4. Validator marks

**Prediction.**

| Δ (s) | Drop share, R = 1 | Drop share, R = 100 |
|---|---|---|
| 300 | 0% | 0% |
| 600 | 0.6% | 0.9% |
| 900 | 8% | 6% |
| 1,200 | 25% | 20% |
| 1,500 | 50% | 49% |
| 1,800 | 81% | 80% |
| 2,400 | 100% | 100% |
| 3,600 | 100% | 100% |

- Each drop share holds within ±3 points, or ±1 point where it is under 2%.
- Record-finding peaks at Δ of 600 to 900 s: 3.5% to 6.5% at R = 1 and 1.6% to 3.2% at R = 100. That is 1.6 to 3.0 times the validator's baseline.
- Above 1,200 s it falls as drops rise. It does not rise past the natural maximum delay.

**Basis.**
- Δ on CV-2 delays quorum by Δ, so the drop share is P(max(gap_F, gap_I) + Δ > 1,800 s), read from the model-seed gaps.
- Once quorum is known after F's hold releases, the credential path sets the record time. That happens when the gap + Δ is above about 120 s: 90% of transactions at Δ = 600 and 98% at Δ = 900.
- Then the record minus (CV-2 send + Δ) has a standard deviation of 90 s, and the best slot holds 0.47 at R = 1 and 0.49 at R = 100. Times the bound, that is 4.5% to 5.1% at R = 1 and 2.4% at R = 100, before drops.

**Fails if** a drop share or the peak lies outside its range, or record-finding rises past Δ = 1,800 s.

**Can fail.** The drop shares rest on 600 R = 1 records, so the R = 1 tolerance is the binding one.

## 5. First-relay marks

**Prediction.**
- Record-finding rises from the baseline to 2.0% (1.4% to 2.8%) at R = 1, and to 0.9% (0.6% to 1.3%) at R = 100. It does so by Δ = 1,500 s.
- That is 1.0 to 1.6 times the first relay's baseline.
- Content marks never drop without the match board window.
- With the window, content marks drop as follows:

  | Δ (s) | 600 | 900 | 1,200 | 1,500 | 1,800 | 2,400 |
  |---|---|---|---|---|---|---|
  | Drop share | 0.5% | 2.8% | 11% | 25% | 47% | 90% |

- Credential marks (a third of the packets) drop as in item 4.

**Basis.**
- A content packet held long enough makes its path set the record time. That takes Δ above the gap: 96% at 900 s and 99.9% at 1,400 s.
- From the content packet's release, the second relay's hold (sd 259 s), F's hold, the post-match lottery, the registry bundle and the posting give a standard deviation of 283 s. The best slot then holds 0.19, so 0.19 × 9.64% = 2.1% at R = 1 and 0.93% at R = 100.
- A credential packet held long enough gives a similar spread after the second relay.
- The drop shares with the window are P(content arrival + Δ + F's hold − the second posting > 1,800 s), from the model seeds.

**Fails if** the peak lies outside its range, or a content mark drops without the window.

**Can fail.** The first relay does not know which path its packet is on, so its gain is the mix of the two.

## 6. Access-network marks

**Prediction.**
- **All three packets.** Record-finding equals the unmarked baseline at every Δ, within its interval. No marked transaction drops at any Δ, at any timeout, with or without the match board window.
- **One packet.** It behaves like the first relay of item 5: about 2.0% at R = 1 and 0.9% at R = 100.

**Basis.**
- Delaying all three packets by Δ shifts the whole transaction by Δ. The gap is unchanged, so neither the timeout nor the board window can see it.
- The actor knows when it released each packet. Its view from the release is the unmarked view, so the record is no easier to find.
- The quorum timeout is therefore no lever against this actor, and none is needed: the mark gains nothing.

**Fails if** any all-three row differs from the baseline beyond its interval, or any all-three transaction drops.

**Can fail.** It would fail if something downstream depended on absolute time, such as a schedule phase the actor could aim at.

## 7. Shorter quorum timeouts

**Prediction.**
- **Natural drops.** With no mark, a 1,500 s timeout drops 0.0% to 0.1% of transactions, and a 1,200 s timeout drops 0.6% to 1.0%.
- **Validator.** Its drop shares move to Δ smaller by 300 s and 600 s. Its peak record-finding falls to 3.0% to 5.5% at R = 1 at 1,500 s, and to 2.5% to 5.0% at 1,200 s.
- **Access-network adversary, all three packets.** Unchanged.

**Basis.** The drop rule is gap + Δ > the timeout, so a shorter timeout is the same as a larger Δ: 300 or 600 s more. The model-seed natural drop shares are 0.00% and 0.64% at R = 1, and 0.02% and 0.92% at R = 100. A shorter timeout leaves less room between the Δ that makes the credential path set the record time and the Δ that drops it.

**Fails if** a natural drop share lies outside its range, or the access-network rows change.

**Can fail.** The peak ranges overlap item 4's. The direction (lower) is the prediction.

## 8. Drop with resubmission

**Prediction.** Record-finding for the resubmitted transaction:

| Actor and cell | Mean 30 minutes | Mean 1 hour | Mean 2 hours | Mean 6 hours |
|---|---|---|---|---|
| First relay, R = 1 | 0.5% (0.2% to 1.0%) | 0.3% (0.1% to 0.6%) | 0.15% (0.05% to 0.4%) | under 0.2% |
| Access-network adversary, R = 1 | 0.3% to 1.8% | 0.3% to 1.8% | 0.3% to 1.8% | 0.3% to 1.8% |

- At R = 100 each value is about half of its R = 1 value.
- Every value is at or below the actor's unmarked baseline.
- Dropped transactions not resubmitted within the window: 1.7%, 2.5%, 4.0% and 10.0% (±1 point).

**Basis.**
- **First relay.** It knows only when it dropped the packet. The record's delay from then is 2,400 s, plus the exponential, plus the natural delay. The exponential dominates the spread, so the best slot holds about 120 × 0.8 / M of the mass: 0.053, 0.027, 0.013 and 0.004. Times 9.64%, that gives the values.
- **Access-network adversary.** It sees every later transaction of the target, but cannot tell which one is the resubmission, since all are built alike. So it is at most its baseline (1.8%), times the share of times it picks the resubmission among the target's transactions in that span.
- **Not resubmitted.** About (2,400 s + M) out of the 241,200 s window.

**Fails if** any value lies outside its range, or any exceeds the actor's baseline beyond its interval.

**Can fail.** The access-network range is wide because the choice among the target's transactions is not modeled here.

## 9. What this would mean for the paper's active-timing row

If items 2 to 8 hold, the paper's argued row on active timing attacks would read:
- "A delay is a longer hold": true in effect. A mark helps only by making one path set the record time. The registry's posting schedule bounds it, at 9.64% and 4.87% here. The first relay and the validator reach about 2.0% and 5.1% at R = 1.
- The quorum timeout bounds only credential-side marks.
- Marks on all three packets are unbounded but gain nothing.
- "A late packet is a drop the device can resubmit": a randomized resubmission delay leaves the actor at or below its unmarked baseline.

The gameplan expected a mark past the natural maximum delay to make the record stand out. This file predicts that it does not.

## 10. Sanity

**Prediction.** Δ = 0 reproduces the unmarked run, transaction by transaction. With default options the code reproduces C2's R = 1 decisions exactly.

**Basis.** A mark of zero adds nothing. New randomness comes from streams C2 does not draw from.

**Fails if** any time or decision differs.

**Can fail.** A mark option that draws from a C2 stream would change every later draw.

# Predictions for C6: the credential path and blind-issued one-time certificates

Written before the run. A prediction counts as made before the run once this file is committed. Each item states the prediction, its basis, what counts as a failure, and whether it can fail.

C6 simulates two candidates on the same relay layer and compares them. Neither is a baseline and neither is assumed to win. Cells R = 1 and 100, with the windows of C4: C2's window at R = 1 (64.9 hours, about 200 real records) and 2 hours at R = 100.

## Parameters

| Parameter | Value | Reason |
|---|---|---|
| Candidates | "credential path" (C2's main configuration) and "blind-issued one-time certificates" (`sna/onetime.py`) | As decided |
| Held identical | Relay holds and schedules, node count, capture and decoy rates, workloads, the registry's 120-second submission and posting schedules, seeds, metrics, the definition of chance, and the attackers both have | As decided. Rates, not counts in flight, are held: the same devices capture at the same times in both candidates, so the faster candidate has fewer transactions in flight |
| Rates | Real devices R / D and decoys 100 / D per second, with C2's D = 1,168.2 s, in both candidates | C2's cells |
| One-time certificates: packet and path | One packet per capture; first relay, second relay, destination Registry Node; the destination uniform over the 20 nodes, the two relays distinct from it and from each other; the same device routing table and wrapping as a content packet | As decided |
| One-time certificates: device hold | None (natural variant); 693 s mean on the holds' 10-second lottery (lengthened-hold variant) | As decided. 693 s brings the mean end-to-end latency to the credential path's D (1,165 s and 1,175 s at 680 s and 690 s on development seeds) |
| Issuers | 3, real devices and decoys each split 50/30/20, one issuing key each | As the validators |
| Refills (main) | When the stock falls to 5, the device fetches 20, directly from its issuer | As decided |
| Refills (random variant) | Each identity fetches 20 at the times of a Poisson process that does not depend on its captures, at 1.25 × its long-run capture rate / 20; a capture with no certificate waits for the next refill | As decided: the fair counterpart of the threshold rule, which leaks capture times |
| Certificate expiry | Two weeks | As decided |
| Stock at the window's start | Each identity's long-run state: uniform over the stocks 6 to 25 just before a capture | Agreed modeling choice |
| Registry Nodes | Verify the certificate and the device signature, then drop them; the posted record carries neither | As decided |
| Edits | The editing software takes the device role, with certificates from the developer's issuer; the record carries the parent ContentHash; the issuer vantages do not score the developer's issuer | As decided |
| Evaluation seeds | The first 8 bytes of SHA-256 of `sna-c3-c5-fresh|R=<R>|run=<run id>`, as C3 to C5; both candidates on the same seeds | No code has run on them |

## Sources of numbers

- **C2:** `results/C2`. Observer 4.77% and 2.33%; validator 5.26% and 2.66%; content server 5.53% and 2.78%; chance 1.11% and 0.55%.
- **Model-seed numbers:** both candidates simulated on seeds from 1,700,000,900 (three runs per cell). No attacker was run on them. The one-time certificate candidate's natural latency from capture to posted record is 485 s on average (sd 268 s, longest 1,283 s); with the 693-s device hold it is about 1,168 s (sd about 645 s, longest about 3,300 s). The credential path's is C2's 1,168 s (sd of the record time after a packet's send 314 s).
- **The Gaussian score model** of `PREDICTIONS_C4.md` item 4: a device's score advantage d, fitted to C2's observer (0.66 at R = 1, 0.58 at R = 100) and content server (0.74 and 0.66). A vantage's d scales with the inverse of the spread of the delay it sees.

## Arithmetic used throughout

**Bound from the posting schedule.** Both candidates post on the same schedule at the same rates, so a posting holds λ = 120 (R + 100) / D other records in both: 10.37 at R = 1 and 20.54 at R = 100. Naming a device from the record time is right at most 10.5% and 5.3% of the time in both.

**Counts in flight.** The credential path has R and 100 in flight. The one-time certificate candidate, natural variant, has (R + 100) × 485 / 1,168: 41.9 at R = 1 and 83.0 at R = 100. With the lengthened hold, the same as the credential path.

**One packet against three.** The credential path's observer sees three packets per capture; the one-time certificate candidate's sees one, with a smaller spread. Two readings bracket its d: the credential path's d scaled by the spreads (314 / 268 natural, 314 / 645 lengthened), and the same divided by √3, as if the three packets were three independent looks.

## 1. Passive observer

**Prediction.**

| Candidate | R = 1 | R = 100 |
|---|---|---|
| Credential path | 4.77% (4.0% to 5.6%) | 2.33% (1.9% to 2.8%) |
| One-time certificates, natural | 3.1% to 5.9% | 1.5% to 2.9% |
| One-time certificates, lengthened hold | 1.7% to 2.4% | 0.85% to 1.15% |

**Basis.** The credential path is C2's configuration on fresh seeds: C2's rate within ±17%. For the one-time certificates, the Gaussian model with the two readings of d above.

**Fails if** a row lies outside its range.

**Can fail.** The two readings may not bracket the truth: the credential path's three packets are not independent looks, since one device hold covers both content packets' sends only in distribution.

## 2. First relay

**Prediction.** In both candidates, the first relay's lead over the observer on the same records is −0.3 to +0.3 points at R = 1 and −0.2 to +0.2 points at R = 100.

**Basis.** A first relay knows its own hold (sd 51 s). That is 2.7% of the variance of the credential path's record time and 3.6% of the one-time certificates' natural one. C2's first hop leads the observer by −0.00 points.

**Fails if** a lead lies outside its range.

**Can fail.** No.

## 3. Destination

The destination knows its packet's arrival and, through the content hash, the record: C2's content server (F or I) in the credential path, the destination Registry Node in the other. Both are scored with the same formula, the density of the record time and the arrival after each packet's send.

**Prediction.** On the records naming the node:

| Candidate | R = 1 | R = 100 |
|---|---|---|
| Credential path (F or I) | 5.53% (4.6% to 6.5%) | 2.78% (2.3% to 3.3%) |
| One-time certificates, natural | 8.0% (5.6% to 10.4%) | 4.1% (2.9% to 5.3%) |
| One-time certificates, lengthened hold | 2.7% (1.9% to 3.5%) | 1.3% (0.9% to 1.7%) |

**What the destination learns from the key.** In the one-time certificate candidate every Registry Node verifies the certificate, so it learns which issuer signed it: the packet's manufacturer. The posted record does not show it. A destination also told which issuer each source address belongs to (an upper bound, as the keyed C of `PREDICTIONS_C3.md` item 9) competes only among that issuer's identities:

| Issuer's share | Natural, R = 1 | Natural, R = 100 | Lengthened, R = 1 | Lengthened, R = 100 |
|---|---|---|---|---|
| 50% | 12.7% | 6.7% | 4.8% | 2.4% |
| 30% | 17.2% | 9.5% | 7.2% | 3.8% |
| 20% | 21.9% | 12.5% | 10.0% | 5.3% |

Each within ±30%. In the credential path, F and I never learn the validator (key_ref travels in CredP to C only).

**Basis.** The arrival's spread after the send: 335 s for a credential-path content packet (its device hold and the relays), 263 s for the one-time certificate packet (the relays), 655 s with the 693-s hold. The content server's d scales by 335 over each.

**Fails if** a row lies outside its range.

**Can fail.** The scaling assumes the spread alone sets the evidence.

## 4. First relay with the destination on its path

**Prediction.** 100% in both candidates, on every record whose path the pair holds (in the credential path, its content paths). Not bound by the posting schedule.

**Basis.** The relay rule of the Messaging Structure: a relay "decrypts its transit layer … and forwards the rest", and a second relay "forwards the payload alone". The one-time certificate packet uses the same wrapping as a content packet, so the first relay and the destination hold the same bytes, and the first relay holds the source address. The simulation scores the link as exact; this item checks the bookkeeping, the specification supplies the link.

**Fails if** any such record is not named.

**Can fail.** Only if the model of the link is wrong.

## 5. Issuer

The issuer sees each refill request of its own identities: who, when, how many. It scores each device by the density of the record time after each of its refills (a refill fires right after the capture that left the stock at 5), plus its rate for every other capture. It can name only its own identities.

**Prediction.** On the records of its own devices, W0:

| Issuer's share | Natural, R = 1 | Natural, R = 100 | Lengthened, R = 1 | Lengthened, R = 100 |
|---|---|---|---|---|
| 50% | 3.9% (2.0% to 6.3%) | 2.3% (1.2% to 3.7%) | 1.0% to 3.9% | 0.6% to 2.3% |
| 30% | 5.1% (2.6% to 8.2%) | 3.5% (1.7% to 5.5%) | 1.3% to 5.1% | 0.9% to 3.5% |
| 20% | 5.9% (3.0% to 9.4%) | 4.4% (2.2% to 7.1%) | 1.5% to 5.9% | 1.1% to 4.4% |

On the records of other issuers' devices: 0%. Under W1 and W2 the issuer's rate rises above its W0 rate, at most three times it, because it knows each identity's long-run refill rate.

**Basis.**
- One capture in 20 triggers a refill. For that record the issuer knows the capture time. Other identities of the same issuer refill at 3 / 20 per hour each, so within the latency's central 800 s about K = 1.7 (R = 1, share 50%) to 3.4 (R = 100, share 50%) others refill; the issuer names the right one about (1 − e^(−K)) / K of the time: 48% and 28%.
- For the other 19 captures in 20 the issuer has nothing but the rate, and names a recently refilled device, right only when that device made the record: about 3.3% times the same share.
- Total: 0.05 × (1 − e^(−K)) / K + 0.95 × 0.033 × (1 − e^(−K)) / K. The ranges are 0.5 to 1.6 times that.
- With the lengthened hold the latency spread is 2.4 times wider, so K is 2.4 times larger: the ranges run from a quarter of the natural point to the natural point.

**Fails if** a row lies outside its range, or the issuer names a device of another issuer.

**Can fail.** The share of captures that trigger a refill is exactly one in 20 only at W0; resubmissions and sessions change it.

## 6. Issuer with the passive observer

**Prediction.** At W0, equal to the observer within ±0.3 points at R = 1 and ±0.2 at R = 100, in both variants. Under W1 and W2, above the observer.

**Basis.** A refill marks a capture whose packet the observer already sees leaving the same address, so it adds no timing the observer lacks. What it adds is each identity's long-run rate and its issuer, which matter only when rates differ. A passive observer that sees each device's connection to its issuer would hold the same: this row is that observer too.

**Fails if** a W0 row lies outside its range.

**Can fail.** Yes, if refills sharpen timing more than this argument allows.

## 7. Coalitions

**Prediction.**

| Coalition | Candidate | R = 1 | R = 100 |
|---|---|---|---|
| Issuer with a first relay | one-time certificates, natural | lead over the observer −0.3 to +0.5 points | −0.2 to +0.3 points |
| Issuer with the destination Registry Node | one-time certificates, natural | share 50%: 14.4% (10% to 19%); 30%: 19.5% (13% to 25%); 20%: 24.4% (17% to 32%) | 50%: 7.8% (5% to 10%); 30%: 11.2% (8% to 15%); 20%: 14.6% (10% to 19%) |
| Issuer with the destination Registry Node | lengthened hold | 0.4 to 1.0 times the natural row | the same |
| First relay with the destination | both | item 4 | item 4 |

**Basis.**
- Issuer with a first relay: the first relay's hold and the issuer's refills each add little (items 2 and 6).
- Issuer with the destination: the destination sees the packet's issuer, so when it is this issuer's, the pair competes only among this issuer's identities, without an upper-bound assumption. For one capture in 20 the refill gives the capture time against the known arrival: right (1 − e^(−K)) / K of the time. For the others, the destination's d (item 3) among the issuer's identities.
- The lengthened hold widens both spreads.

**Fails if** a row lies outside its range.

**Can fail.** As items 3 and 5.

## 8. Issuer withholding or delaying refills

Inside each window, the issuer serves its target's refills and withholds, or delays to the window's end, every other identity's refill. It then finds the record of a target capture that triggered a refill in the window, from that refill's time. Windows of 10, 30, 60 and 120 minutes, as C5.

**Prediction.** At every window length and in both modes, the same as with nothing withheld within ±1 point: 1.0% to 4.0% at R = 1 and 0.5% to 2.5% at R = 100 (natural variant).

**Basis.**
- A device holds 6 to 25 certificates just before a capture and makes 3 captures an hour. In 2 hours it makes about 6, so about 3% of devices run out inside a 120-minute window, and fewer in shorter ones. Withholding refills empties almost nothing.
- With nothing withheld, the issuer finds the record from the capture time: records post at (R + 100) / D per second, and the latency spreads over about 670 s, so about 58 records compete at R = 1 and 115 at R = 100, capped by the posting schedule.

**Fails if** a row lies outside its range.

**Can fail.** Yes, if stocks run lower than the long-run start assumes.

## 9. K records

**Prediction.** The K-record attacker on each candidate's observer posteriors:

| K | Credential path, R = 1 | One-time certificates natural, R = 1 | One-time certificates lengthened, R = 1 |
|---|---|---|---|
| 1 | equal to the observer | equal to the observer | equal to the observer |
| 2 | 4.7% to 12.6% | 4.5% to 10.4% | 2.1% to 3.1% |
| 3 | 6.7% to 17.9% | 5.9% to 15.2% | 2.4% to 3.9% |
| 5 | 10.9% to 29.1% | 8.9% to 25.2% | 2.9% to 5.3% |
| 10 | 22% to 59% | 16.8% to 49.9% | 4.1% to 9.1% |
| 20 | 40% to 100% | 33.8% to 82.2% | 6.6% to 17.3% |

| K | Credential path, R = 100 | One-time certificates natural, R = 100 | One-time certificates lengthened, R = 100 |
|---|---|---|---|
| 2 | 2.3% to 6.2% | 2.2% to 5.2% | 1.0% to 1.5% |
| 3 | 3.4% to 9.0% | 2.9% to 7.8% | 1.1% to 1.9% |
| 5 | 5.7% to 15.2% | 4.4% to 13.7% | 1.4% to 2.6% |

Accuracy rises with K in every row.

**Basis.** The credential path's rows are `PREDICTIONS_C4.md` item 4. The one-time certificates' rows are the Gaussian model with d √K, at the two readings of d of item 1.

**Fails if** a value lies outside its range, or accuracy falls with K by more than its interval.

**Can fail.** The ranges are wide where the two readings of d differ.

## 10. Edit chains

**Prediction.** In both candidates, as `PREDICTIONS_C4.md` item 5: at a 100% same-source share, accuracy on a chain of L records equals the K-record accuracy at K = L within its interval; at 50% it is lower than at 100% for every L of 2 or more.

**Basis.** A chain is a public set of records that share a user. Neither candidate changes that.

**Fails if** 50% is not below 100% at some L of 2 or more, or the 100% curve leaves its K-record interval.

**Can fail.** Chains of 4 and 5 records are rare.

## 11. Workloads

**Prediction.** In each candidate, the observer and the K-record attacker keep `PREDICTIONS_C4.md` item 6's order: W0 ≤ W-mismatch at R = 1, for every K. Chance in each workload is the same in both candidates within 10%.

**Basis.** The workloads change who captures when, the same in both candidates.

**Fails if** the order fails or a chance differs by more than 10%.

**Can fail.** Yes.

## 12. End-to-end latency

**Prediction.** Mean capture to posted record: credential path 1,168 s (1,150 to 1,185 s); one-time certificates natural 485 s (470 to 500 s); lengthened hold 1,168 s (1,150 to 1,185 s).

**Basis.** Model seeds; the lengthened hold is set to match.

**Fails if** a mean lies outside its range.

**Can fail.** No.

## 13. Revocation delay at a batch of 20

**Prediction.** When the issuer stops serving a device, the certificates it already holds stay usable: 15.5 on average (6 to 25). At its normal rate (3 an hour) the device uses them in 5.2 hours on average (2.0 to 8.3 hours); a device that keeps them can use them for up to two weeks, their expiry.

**Basis.** The long-run stock just before a capture is uniform over 6 to 25.

**Fails if** the measured mean differs by more than 5%.

**Can fail.** No.

## 14. Sanity

**Prediction.** With the candidate switched off (the default), the code reproduces C2's R = 1 decisions exactly. For one seed, both candidates have the same capture times and sources.

**Basis.** The one-time certificate candidate lives in its own module and draws captures from the credential path's streams in the same order.

**Fails if** any R = 1 decision differs, or a capture differs.

**Can fail.** Yes, if a shared stream is drawn in another order.

## 15. Random refill schedule

Both variants (natural and lengthened hold) run with the random refill schedule as well as the threshold rule. Each identity's stock at the window starts from its long-run state: every certificate issued in the two weeks before the window. The issuer knows the schedule, so it gives refill times no weight.

**Prediction.**
- Every vantage that does not use refills (observer, first relay, destination, destination told each address's issuer, first relay with the destination, K records, edit chains) equals the threshold variant decision by decision: the captures, paths and holds are the same, and no device runs dry.
- Issuer alone, W0, on its own devices' records: equal to chance among its identities within ±30% of it: 1/51, 1/31 and 1/21 at R = 1 (2.0%, 3.2%, 4.8% for shares 50%, 30%, 20%); 1/103, 1/62 and 1/41 at R = 100 (0.97%, 1.6%, 2.4%). Under W1 and W2 it is above chance, because volume still shows each identity's rate.
- Issuer with the observer, and issuer with a first relay: equal to the observer, and to the first relay, decision by decision.
- Issuer with the destination Registry Node: equal to the destination told each address's issuer on the same records, decision by decision.
- Stock: about 1,260 certificates per W0 device (1,200 to 1,320). Revocation delay: two weeks both at the normal rate of use and for a device that keeps them, because the stock outlasts the expiry.
- The issuer's withholding attack is not run under this schedule: it finds records from the refills the target's captures trigger, and here none do.

**Basis.**
- Refills are independent of captures, so a refill time says nothing about a record; only each identity's rate remains, which is the same for every identity at W0.
- Stock: certificates arrive at 1.25 λ and are used oldest first, so each stays about two weeks, until it is used or expires. By Little's law the stock is 1.25 × 3 per hour × 336 hours = 1,260.

**Fails if** a decision differs where equality is predicted, the issuer's rate lies outside its range at W0, or the stock lies outside its range.

**Can fail.** Yes.

## Second C6 run

Items 16 to 19 are a second C6 run with their own jobs (`c6_batch`, `c6_dest`, and the long windows of `c6_issuer`). Cells R = 1 and 100.

### Parameters of the second run

| Parameter | Value | Reason |
|---|---|---|
| Batch sweep | Batches of 1, 5, 20 and 100; a refill when the stock falls to a quarter of the batch, rounded down (0, 1, 5, 25) | As decided |
| Batch sweep scope | Natural variant, threshold rule, W0 | Logged assumption: under the random schedule neither the stock (about two weeks of issuance) nor the issuer's chance-level result depends on the batch (item 15) |
| Resubmission | A device that sees no record of its ContentHash resubmits with a new certificate after waiting just past its candidate's longest natural delay, then an exponential delay with mean 30 minutes, 1 hour, 2 hours or 6 hours, as C5 | As decided. Waits: 2,400 s for the credential path (C5's), 1,400 s for blind-issued one-time certificates natural (longest natural delay 180 + 900 + 120 + 120 s plus links), 3,500 s with the lengthened hold (its 2,079-s hold cap added) |
| Dropping or delaying destination | One node per run, drawn from the cell and the run id, drops (or delays by Δ = 600 or 1,800 s before submitting) every packet it is the destination of: in the credential path every content packet it receives as F or I, so the transaction fails and the device resubmits it; in the other candidate every packet it receives | Logged assumption: a destination cannot single out a device, so it acts on everything it receives. The C5 windows (67 hours) |
| Issuer windows | 6, 12 and 24 hours, withhold, delay, and nothing withheld | As decided |

## 16. Batch sweep: the issuer and the revocation delay

**Prediction.** The issuer alone on its own devices' records, natural variant, W0:

| Batch | R = 1, shares 50% / 30% / 20% | R = 100, shares 50% / 30% / 20% |
|---|---|---|
| 1 | 1.8–10.2% / 2.9–14.9% / 4.3–20.3% | 0.9–5.2% / 1.5–8.0% / 2.2–11.2% |
| 5 | 2.7–9.0% / 4.4–13.4% / 6.2–16.7% | 1.3–4.9% / 2.2–7.7% / 3.3–10.8% |
| 20 | as item 5 | as item 5 |
| 100 | 0.7–2.1% / 0.7–2.3% / 0.7–2.3% | 0.65–1.8% / 0.7–2.0% / 0.7–2.2% |

Stock just before a capture, and the revocation delay (the stock at the device's normal rate of 3 an hour; for a device that keeps them, two weeks):

| Batch | Stock | At normal use | Kept |
|---|---|---|---|
| 1 | 1.0 | 0.33 h | two weeks |
| 5 | 4.0 | 1.33 h | two weeks |
| 20 | 15.5 | 5.2 h | two weeks |
| 100 | 75.5 | 25.2 h | two weeks |

Each stock within 5%.

**Basis.**
- One capture in b triggers a refill, which tells the issuer that capture's time. Smaller batches tell it more captures, but the more of its identities refill near any moment, the less each refill singles one out. Two methods bracket each cell: item 5's count of competing refills, and, for the triggered records, the Gaussian score model with the observer's single-packet d among the identities that refill nearby. The ranges are 0.6 times the lower and 1.5 times the upper.
- The stock just before a capture is uniform over k + 1 to k + b, with k the threshold: its mean is k + (b + 1) / 2.

**Fails if** a cell lies outside its range or a stock differs by more than 5%.

**Can fail.** Yes.

## 17. A destination that drops packets

**Prediction.** The dropping node names the device of a dropped transaction, once its resubmission posts, from two looks: the dropped packet's arrival and the resubmission's record time.

| Candidate | R = 1 | R = 100 |
|---|---|---|
| Credential path | 8.7% (6.1% to 11.3%) | 4.4% (3.1% to 5.7%) |
| Blind-issued one-time certificates, natural | 6.7% to 16.4% | 3.4% to 8.5% |
| Lengthened hold | 2.0% to 4.4% | 1.0% to 2.2% |

In every candidate this is above the destination alone on its normal records (item 3), and it does not change with the resubmission's mean delay beyond its interval. The dropping node causes a resubmission of 2 / 17 of transactions in the credential path (11.8%) and 1 / 20 in the other (5%).

**Basis.** The node knows the dropped packet's ContentHash, so it recognizes the resubmission's record. The two looks are independent timing evidence of one device: in the Gaussian score model their advantages add in quadrature, d = √(d_destination² + d_observer²), with each candidate's d from items 1 and 3.

**Fails if** a row lies outside its range, or a row is not above the destination alone.

**Can fail.** The two looks are not fully independent when the device's packets cluster in time.

## 18. A destination that delays its submissions

**Prediction.** At Δ = 600 and 1,800 s, in both candidates, the delaying node's own accuracy on its records equals the destination's (item 3) within its interval: the delay changes nothing it knows. The passive observer on those records falls below its rate on the others.

**Basis.** The node knows its packet's arrival and, by the ContentHash, its record; it also knows its own Δ. Every other party sees a record later than its packets imply.

**Fails if** the node's accuracy leaves item 3's interval, or the observer's rate on the delayed records is not below its rate on the others.

**Can fail.** Yes.

## 19. The issuer's long withholding windows

**Prediction.** Record-finding from the target's refills (natural variant):

| Window | Nothing withheld, R = 1 | Withhold or delay, R = 1, target's issuer 50% | 30% or 20% | Nothing withheld, R = 100 | Withhold or delay, R = 100, 50% | 30% or 20% |
|---|---|---|---|---|---|---|
| 6 h | 1.0% to 4.0% | 1.0% to 4.7% | 1.0% to 4.4% | 0.5% to 2.5% | 0.5% to 3.0% | 0.5% to 2.8% |
| 12 h | 1.0% to 4.0% | 1.0% to 5.7% | 1.0% to 4.9% | 0.5% to 2.5% | 0.5% to 3.6% | 0.5% to 3.0% |
| 24 h | 1.0% to 4.0% | 1.0% to 6.7% | 1.0% to 5.3% | 0.5% to 2.5% | 0.5% to 4.2% | 0.5% to 3.0% |

Under withhold, the share of the issuer's other identities' captures that wait for a certificate inside a window is 20% to 40% at 6 hours, 45% to 70% at 12 hours and 65% to 90% at 24 hours.

**Basis.** A device's stock (6 to 25) lasts 2 to 8 hours at 3 captures an hour, so over a window of L hours the issuer's other identities are dry for a share f of it: about 0.3, 0.6 and 0.8 at 6, 12 and 24 hours. Their records then leave the postings, which thins the competitors of a target record by the issuer's share s times f: record-finding rises by 1 / (1 − s f) over nothing withheld. Item 8 gives the baseline.

**Fails if** a row lies outside its range, or the waiting share lies outside its range.

**Can fail.** Yes.

## What would favor each candidate

Stated before any result, at equal latency (the lengthened-hold variant), since a longer latency spreads every timing vantage.

- **Favors blind-issued one-time certificates:** on every vantage both candidates have (observer, first relay, destination, first relay with the destination, K records, edit chains), its rate is at or below the credential path's within their intervals; and the issuer, alone and with a destination, names devices no more often than C2's validator does (5.26% and 2.66%).
- **Favors the credential path:** the one-time certificate candidate's rate is above the credential path's on a shared vantage at equal latency; or the issuer with one other party (a destination Registry Node) names devices more often than any single party or pair of the credential path does outside the exact first-relay-with-destination link.
- **Not settled by these rates:** the natural variant's lower latency, the revocation delay (item 13), and that every Registry Node learns each packet's issuer in the one-time certificate candidate while no destination learns the validator in the credential path. These are reported beside the rates, not folded into them.
- **The tracer** enters the comparison only if it meets its entry conditions in both candidates.
- **The issuer** is compared under both refill rules. A result that favors one candidate under the threshold rule and not under the random schedule is reported as depending on the refill rule.

## Changes before the run

- C6 uses the evaluation seed set of C3 to C5, which no code had run on when it was defined; development, debugging and dry runs use model seeds only.
- Logged assumptions, decided on the reasons given, before the run: both candidates keep the same capture rates (the same devices capture at the same times), not the same counts in flight; one developer's issuer serves all editing software and is not scored as a vantage; a device refused a refill asks again at each later capture, and a device with no certificate left gets its refill when the withholding window ends. Each follows the recommendation the specification's owner accepted.
- Item 15, the random refill schedule, was added with its parameters, before its code.
- The first C6 run is items 1 to 15. The batch sweep, the destination's drop and delay, and the issuer's 6, 12 and 24-hour windows are a second C6 run with its own predictions.
- Item 15 first said the random schedule's stock starts from refills and captures simulated from two weeks and a day before the window. With 25% more issued than used, the queue of certificates, used oldest first, grows by 0.75 an hour and reaches its long-run size only after about 70 days, so that start-up was not the long-run state. The long-run state holds every certificate issued in the last two weeks, and the stock now starts there. This is a modeling error in the start-up; the prediction (about 1,260) is unchanged.
- Items 16 to 19, the second C6 run, were added with their parameters and logged assumptions (batch sweep scope; a dropping or delaying destination acts on every packet it receives; the resubmission waits per candidate), before their code.

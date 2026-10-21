# Paper table

InternalCompromiseRun: how often a single compromised component, starting from a public registry record, names the device that produced it. Every hold follows the timing in `README.md`. 60 decoy transactions are in flight; decoys are genuine transactions from registered identities, indistinguishable to every party. 200 runs per cell.

**Simulator version 1.** Every number below was produced by simulator version 1. In version 1, the three fan-out legs drew independent holds, the record time was the midpoint of F's and I's submissions, and candidates were device packets grouped greedily into captures. The code in this folder is version 2 (`README.md`). These numbers stand for version 1 until a version 2 run replaces them.

The bracket gives each component's lead over a passive observer on the same records, in percentage points. The first hops and the credential processor are scored on every record, because they cannot identify the records they took part in.

| Component | Holds | R = 1 | R = 20 | R = 100 | Its average confidence in a match (R = 1 / 20 / 100) |
|---|---|---|---|---|---|
| Passive observer | nothing | 9.91% | 6.46% | 3.48% | 7.6% / 6.0% / 3.3% |
| First hop, credential | relay transit key; source address | 9.89% (-0.02) | 6.47% (+0.01) | 3.47% (-0.01) | 7.6% / 6.1% / 3.3% |
| First hop, content | relay transit key; source address | 9.89% (-0.02) | 6.47% (+0.01) | 3.47% (-0.01) | 7.6% / 6.1% / 3.3% |
| Credential processor | transit and ring-signing keys | 9.91% (+0.00) | 6.46% (-0.01) | 3.47% (-0.01) | 7.6% / 6.0% / 3.3% |
| Validator | token-decryption and signing keys; device identity | 9.51% (-0.40) | 6.32% (-0.14) | 3.41% (-0.06) | 8.1% / 6.5% / 3.6% |
| Gatekeeper | transit and countersignature keys | 9.95% (+0.04) | 6.45% (-0.01) | 3.46% (-0.01) | 7.6% / 6.1% / 3.3% |
| Content server | transit and registry-signing keys | 9.84% (-0.07) | 6.60% (+0.14) | 3.72% (+0.24) | 6.7% / 5.3% / 2.8% |
| *Guess among devices that could have produced the record* | | *2.03%* | *1.55%* | *0.77%* | |
| *Guess among all registered devices* | | *1.43% (1 in 70)* | *1.09% (1 in 92)* | *0.54% (1 in 185)* | |

- **No single component gains more than a quarter of a point over the passive observer.**
- **The adversary's confidence identifies no record.**
  - Every component's most confident 1% of matches is right at most 26.5% of the time.
  - At most 0.019% of any component's decisions fall in a set of matches that is right more than half the time.
- **Mean time from capture to finalization is about 1,040 seconds**, with a 95th percentile of about 1,525 seconds.

## What each timing mechanism contributes (R = 20)

Paired with InternalCompromiseRun on the same records, in points.

| Build | Observer's accuracy (InternalCompromiseRun), or its change from InternalCompromiseRun in points | Largest lead of any component over the observer | Mean latency |
|---|---|---|---|
| InternalCompromiseRun | 6.5% | +0.1 (content server) | 1,033 s |
| any one of V's and C's holds, the inclusion lottery, the post-match lottery or registry bundling removed | within 0.1 points of InternalCompromiseRun | at most +0.3 | 973 to 1,020 s |
| role-aware holds removed | +0.9 | +1.5 (validator) | 807 s |
| all five removed | +1.3 | +0.9 (validator) | 647 s |
| relay hops at 180 s | -0.6 | +0.1 (validator) | 1,189 s |
| role-aware holds at 360 s | -1.4 | +0.5 (content server) | 1,324 s |

The role-aware holds keep the validator, which knows each approving device, level with a passive observer. The other four mechanisms each make little difference alone; removing all five raises the observer by more than removing the role-aware holds alone. Longer relay holds lower the observer's accuracy further, at about 155 seconds of extra latency.

## Permitted overlap

The role draw allows every coincidence the routing design permits: a first relay may be another path's destination, and a second relay may hold any role on another path. Leads over a passive observer on the same records, in points.

### Single-role vantages

| Component | R = 1: InternalCompromiseRun / permitted overlap | R = 20 | R = 100 |
|---|---|---|---|
| First hop, credential | -0.02 / -0.04 | +0.01 / -0.02 | -0.01 / -0.00 |
| First hop, content | -0.02 / -0.04 | +0.01 / -0.02 | -0.01 / -0.00 |
| Credential processor | +0.00 / +0.01 | -0.01 / -0.02 | -0.01 / -0.00 |
| Validator | -0.40 / -0.53 | -0.14 / -0.24 | -0.06 / -0.04 |
| Gatekeeper | +0.04 / +0.05 | -0.01 / -0.05 | -0.01 / -0.00 |
| Content server | -0.07 / -0.13 | +0.14 / +0.20 | +0.24 / +0.22 |

### One node in two roles: identifiable classes

Every record a node can select, because it held a destination role (15.00% of its decisions): -0.25 [-0.42, -0.06]; 9.70% vs 9.95% at R = 1, +0.09 [-0.07, +0.25]; 6.56% vs 6.47% at R = 20, and +0.09 [+0.04, +0.14]; 3.58% vs 3.49% at R = 100.

The classes below split those records by the node's other role, which the node cannot tell. The node held a destination role in the record's transaction and can select those records. Each cell gives the combined lead [95% CI], the share of decisions right against the observer's, and the class's share of the node's decisions. The two rows under each class give the first relay alone and the destination alone on the same records.

| Roles held | R = 1 | R = 20 | R = 100 |
|---|---|---|---|
| Credential first relay + content destination | +1.46 [+0.50, +2.44]; 11.65% vs 10.19%; 0.49% | +1.16 [+0.35, +1.98]; 7.98% vs 6.82%; 0.50% | +1.06 [+0.75, +1.36]; 4.47% vs 3.41%; 0.50% |
| first relay alone | +0.20 | +0.73 | +0.42 |
| destination alone | -0.49 | +0.12 | +0.18 |
| Content first relay + content destination | +0.78 [-0.12, +1.70]; 10.67% vs 9.89%; 0.53% | +0.90 [-0.05, +1.82]; 7.52% vs 6.62%; 0.50% | +0.74 [+0.47, +1.01]; 4.22% vs 3.49%; 0.51% |
| first relay alone | +0.82 | +0.21 | +0.22 |
| destination alone | +0.12 | +0.21 | +0.21 |
| Content first relay + credential destination | +0.19 [-0.33, +0.72]; 10.46% vs 10.27%; 0.53% | +0.27 [-0.21, +0.75]; 6.90% vs 6.63%; 0.53% | +0.17 [+0.01, +0.34]; 3.66% vs 3.49%; 0.53% |
| first relay alone | +0.24 | +0.23 | +0.24 |
| destination alone | -0.05 | +0.02 | -0.02 |
| Second relay + destination | -0.55 [-1.04, -0.06]; 9.51% vs 10.07%; 1.39% | +0.30 [-0.10, +0.69]; 6.67% vs 6.37%; 1.42% | -0.02 [-0.15, +0.12]; 3.48% vs 3.50%; 1.40% |
| destination alone | -0.17 | +0.40 | +0.11 |

- With a content destination, the combined lead is above the sum of the two single-role leads: +1.74 at R = 1 and +0.45 at R = 100 for a credential first relay.
- With the credential destination, the combined lead equals the first relay's alone.
- Every identifiable class passes the claim criterion in every cell.

### Oracle-conditioned

The node held only relay or gatekeeper roles in the record's transaction and cannot select those records. Each row is a single-role lead on a subset the node cannot pick.

| Roles held | R = 1 | R = 20 | R = 100 |
|---|---|---|---|
| Second relay + first relay | +0.62 [+0.25, +0.99] | +0.53 [+0.23, +0.82] | +0.30 [+0.20, +0.39] |
| Gatekeeper + first relay | +0.40 [+0.11, +0.69] | +0.70 [+0.42, +0.98] | +0.36 [+0.28, +0.44] |
| Gatekeeper + second relay | -0.06 [-0.30, +0.18] | -0.19 [-0.41, +0.03] | -0.05 [-0.12, +0.02] |
| Second relay + second relay | -0.27 [-0.68, +0.12] | +0.09 [-0.23, +0.41] | -0.10 [-0.21, +0.01] |

Gatekeeper with a second relay fails the claim criterion at R = 1, with coverage 0.139% on a top group of 151 decisions.

Over every record it can select, a node in two roles leads the observer by at most +0.09 points. Within those records, the subsets in which it also held a first relay lead by +0.74 to +1.46 points, but the node cannot tell which records those are. Each such pair covers about 0.5% of a node's decisions in a 20-node pool.

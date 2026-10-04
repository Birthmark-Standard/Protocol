# Paper table

InternalCompromiseRun: how often a single compromised component, starting from a public registry record, names the device that produced it. Every hold follows the timing in `README.md`. 60 decoy transactions are in flight; decoys are genuine transactions from registered identities, indistinguishable to every party. 200 runs per cell.

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

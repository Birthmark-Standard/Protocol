# Catalog update: rows for the Insider Experiment Design tab

Rows to add to `Birthmark_Insider_Compromise_Catalog.xlsx`, tab *Insider Experiment Design*, after
row 10. Columns follow the tab: Item, Detail, Rationale. A second table suggests rows for the
*Insider Results* tab, if you want the outcome recorded there too.

## Insider Experiment Design, rows 11 to 20

| Row | Item | Detail | Rationale |
|---|---|---|---|
| 11 | Null case N (no compromised element) | The outside observer of the GPA experiment, holding no keys, makes the same guesses on the same transactions with the same answer list as each role (told which transaction each row is), using the published GPA sequencing likelihood; for F, content arrival time alone. The two published GPA attacks (main and sequencing) also run unchanged on the same traffic and are compared per transaction. | Separates what the insider's knowledge adds from what any outside observer already gets. Every role is reported as a paired difference from N. |
| 12 | Roles added: V, A, D, GK | V: a validator (device identity, CV-1 arrival, CV-2 send, C's address). A: the credential first hop (source address, its own hold and forward times). D: a content first hop (the same, for one content copy). GK: one active gatekeeper (PacketHash, vk_id, C's address, its GK-leg arrival, own hold outcome and posting time). Each uses the latest event it knows exactly on the path to the registry; V and GK also search C's GK legs on the wire. | Covers every single element with a distinct view. B, E, G, H and I are left out as bounded by or mirroring C, F and D. |
| 13 | Answer list per role | A, C, D, V and GK guess which registry posting on the wire belongs to their transaction. F guesses which validator reply belongs to its content, as in earlier runs. Guesses are one-to-one per compromised server (optimal assignment); the per-decision attack (each row's highest score) is also reported. | Every attack links a label the adversary holds to the transaction's public record, against the 1/L baseline. |
| 14 | First-hop channel knowledge (assumption) | A first hop is assumed to know whether it holds a credential or a content packet. In the simulator it learns the unpadded length when it removes padding (about 202 B credential, 114 B content inside the transit layer). FLAGGED ASSUMPTION: whether the real design hides this is to be settled; if it does, A and D become one adversary scored on all its first-hop packets. | Scores A and D separately as specified. The length a hop learns on unpadding is a design detail the specification does not yet address. |
| 15 | Runs: one simulation, every server | Each run simulates the network once; every scenario and every round reads the same traffic (common random numbers). Each attack is computed from every server that can hold the role in turn. Confidence intervals resample whole runs. Scored window 3 hours (40 minutes at L = 1000). | Paired comparisons across roles and rounds, and roughly 17 times the decisions per simulation. |
| 16 | Adversary confidence | For every decision: the top two scores, the true answer's score and rank, the score gap, and a softmax posterior with its temperature fitted on held-out runs. Reported: confidence given right vs wrong, AUC of confidence as a predictor of being right, precision at coverage 1 to 100%, calibration (ECE), and the coverage reachable at precision of at least 50%. | Asks whether the adversary can tell its successes from luck. A success it cannot pick out is not actionable. |
| 17 | Controls | Positive: lottery and gatekeeper hold off. Negative: labels shuffled. Known signal: Round 1 F. Controls must pass before results count. | Shows the attack and the confidence metrics can see a signal when one exists, and read null when none does. |
| 18 | Scale | L = 4, 8, 24, 40, 200, 1000 (devices = 10 x L, 20-minute interval), Round 3 for every role, plus Round 1 F at 40, 200, 1000. Lift = accuracy x L. The volume table maps L to captures per day and to the in-flight count implied by the measured capture-to-registry delay (723 s). | The target deployment is far above L = 40. The unmitigated design's lift grew with L, so a larger L is not automatically safer. |
| 19 | Validator share and pool size | V at manufacturer share s = 1.0, 0.5, 0.1 (L = 40 and 200). Pool of 40 nodes against 20 at the same load per node. | V sees only its manufacturer's share; registry records carry no manufacturer, so its answer list is still every posting. First hops see about 1/nodes of traffic. |
| 20 | Expected outcome, stated in advance | N below 1/L. F: Round 1 above 1/L, Round 3 below. C below 1/L. V at most C. A null. D null with a shorter chain than A (D at least A). GK no direction. Signal: accuracy CI above 1/L or AUC CI above 0.5, with Bonferroni-adjusted intervals across the 7 scenarios x 2 tests at each (round, L). | Stated before running (ANALYSIS_PLAN.md), so a result that does not match is flagged as a finding. |

## Suggested rows for the Insider Results tab

| Finding | Result | Read |
|---|---|---|
| Every role, adopted design | No compromised element beats 1/L at any L from 4 to 1000. F is highest (lift 0.55 at L = 4, 0.37 at L = 1000). No attack keeps precision at 50% beyond 0.03% of its guesses. | PASS |
| Insider over outside observer | F adds 8.2 points at L = 4 and 0.74 at L = 40; C and GK add about 1 point at L = 4 and nothing from L = 8 on; V adds nothing; A and D are below the outside observer. | PASS |
| Adversary confidence | AUC 0.51 to 0.63 at L = 4 to 40, about 0.5 from L = 200. The metrics see the known Round 1 signal (AUC 0.77, top 1% right 100% of the time). | PASS |
| Scale | Every role's lift falls from L = 40 to L = 1000 (improving). Round 1 F's lift peaks at L = 40 (13.2) and falls to 10.2 at L = 1000. | PASS |
| V sanity check | V never beats C (for example -0.6 points at L = 4). | PASS |
| Prediction D at least A | Failed: D is below A at every L. | WATCH |
| Controls | Known signal passes. Positive control: C reaches 81.9% against a 90% threshold (a 10-second polling ceiling that caps every registry-list attack near 82%). Negative control failed as specified; a post-hoc outcome-shuffle control passes. | WATCH |
| Joint vs per-decision attack | At L = 200 and above, the one-to-one joint attack understates the adversary; the per-decision attack is stronger and also stays below chance. | NOTE |
| Protocol currency | Wire-visible sizes unchanged under the current per-leg specification. The specification's content-leg sizes omit the 1-byte mod_level; unpadded registry postings are 1 B larger on the wire. | NOTE |

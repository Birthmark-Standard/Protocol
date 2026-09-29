# Paper table: one compromised element against the passive-observer baseline

For Appendix D. One row per role under the adopted design (ring signature, gatekeeper exclusion and
gatekeeper posting hold).

| Role | Knows exactly | Label | L = 4 (1/L = 25.0%) | L = 8 (1/L = 12.5%) | L = 24 (1/L = 4.2%) | L = 40 (1/L = 2.5%) | L = 200 (1/L = 0.5%) | L = 1000 (1/L = 0.1%) | AUC, L = 4 |
|---|---|---|---|---|---|---|---|---|---|
| N | sizes and timing on every link; no keys | none | 8.15% [7.68%, 8.62%] | 4.17% [3.82%, 4.54%] | 1.34% [1.27%, 1.42%] | 0.82% [0.76%, 0.87%] | 0.09% [0.08%, 0.10%] | 0.00% [0.00%, 0.01%] | 0.57 [0.56, 0.59] |
| A | credential packet's source address and arrival; its own hold and forward times | network address | 7.25% [6.87%, 7.63%] | 3.91% [3.59%, 4.22%] | 1.26% [1.15%, 1.37%] | 0.75% [0.68%, 0.82%] | 0.10% [0.09%, 0.11%] | 0.01% [0.00%, 0.01%] | 0.56 [0.54, 0.58] |
| D | one content copy's source address and arrival; its own hold and forward times | network address | 5.24% [4.93%, 5.55%] | 2.74% [2.45%, 3.03%] | 0.88% [0.81%, 0.96%] | 0.50% [0.44%, 0.55%] | 0.07% [0.06%, 0.07%] | 0.00% [0.00%, 0.00%] | 0.56 [0.54, 0.58] |
| C | PacketHash, key_ref, its own GK-leg sends and CV-2 arrival | transaction (manufacturer) | 9.11% [8.65%, 9.59%] | 4.61% [4.27%, 4.93%] | 1.51% [1.37%, 1.64%] | 0.80% [0.73%, 0.87%] | 0.12% [0.11%, 0.13%] | 0.00% [0.00%, 0.01%] | 0.57 [0.55, 0.58] |
| F | ContentHash, content arrival, its quorum-detection tick, board postings | content | 13.65% [13.12%, 14.22%] | 6.81% [6.41%, 7.21%] | 2.34% [2.22%, 2.47%] | 1.30% [1.20%, 1.39%] | 0.21% [0.20%, 0.23%] | 0.04% [0.03%, 0.04%] | 0.63 [0.62, 0.64] |
| V | device identity, CV-1 arrival, CV-2 send, C's address | device identity | 8.48% [7.96%, 9.02%] | 4.07% [3.80%, 4.36%] | 1.25% [1.15%, 1.35%] | 0.74% [0.67%, 0.81%] | 0.11% [0.09%, 0.12%] | 0.01% [0.00%, 0.01%] | 0.57 [0.56, 0.59] |
| GK | PacketHash, vk_id, C's address, its GK-leg arrival, own hold and post | transaction (manufacturer) | 9.38% [9.04%, 9.75%] | 3.90% [3.68%, 4.15%] | 1.34% [1.29%, 1.38%] | 0.68% [0.64%, 0.71%] | 0.06% [0.05%, 0.06%] | 0.00% [0.00%, 0.01%] | 0.58 [0.57, 0.59] |

**Reading the table.**
- **What is measured.** Each cell is the share of transactions for which the compromised element's
  best attack names the right record, with a 95% confidence interval from resampling whole runs.
- **The chance baseline.** 1/L is the rate of guessing at random among the L transactions in flight
  (workbook Little's-law value). Every cell is below its column's 1/L.
- **What each role is linking.** "Label" is what the adversary already holds about the transaction:
  a network address (the first hops A and D), a device identity (the validator V), the manufacturer
  (the credential processor C and a gatekeeper GK), or the content itself (the content server F).
  Every role except F links its label to the transaction's registry record; F links its content to
  the transaction's validator reply. N is the outside observer holding no keys.
- **AUC.** AUC measures whether the adversary can tell its right guesses from its wrong ones (0.5:
  it cannot). At L = 4 every role is slightly above 0.5, and no attack keeps precision at 50% beyond
  0.03% of its guesses.

**Setup.** Simulated deployment, 20-node pool, 10 devices per unit of L, a 20-minute mean interval
between captures, and a 3-hour scored window. L = 1000 uses a 40-minute window and 10 runs; every
other column uses 20 runs, 40 at L = 4. L = 1000 corresponds to about 720,000 captures a day; with
the measured capture-to-registry delay of 12 minutes, about 6,000 transactions are in flight at once.

**For comparison.** Under the original design, a compromised content server links content to the
credential transaction for 86.2% of transactions at L = 4 and 1.0% at L = 1000, against 1/L of 25%
and 0.1%.

**Source.** `InsiderCompromiseExperiment/RESULTS.md`, extension section; machine-readable:
`paper_table.csv`.

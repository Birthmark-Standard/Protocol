# Paper table

How often each compromised component, starting from a public registry record, names the device that produced it. Per-decision attack, 200 runs per cell. Each cell gives accuracy and, in brackets, the contribution over a passive observer on the same records in percentage points. L is the number of real transactions in flight. "Random" is the rate of a uniformly random pick among the feasible devices. The decoy columns hold the real volume at R = 1 or 4 and fill the total to T = 500. Intervals and every other cell are in RESULTS.md.

| Vantage | Holds | Exact knowledge used | Device named, L = 4 (random 21.2%) | L = 40 (random 2.2%) | L = 500 (random 0.17%) | R = 1, T = 500 decoys | R = 4, T = 500 decoys | Exact capture named, L = 40 (1/L = 2.5%) |
|---|---|---|---|---|---|---|---|---|
| Baseline | nothing | sizes and timing on every link | 48.9% (+0.0) | 9.0% (+0.0) | 1.0% (+0.0) | 1.0% (+0.0) | 0.9% (+0.0) | 5.5% (+0.0) |
| First hop, credential | relay transit key | source address; own hold and forward | 51.7% (+2.8) | 10.1% (+1.1) | 1.2% (+0.2) | 1.1% (+0.1) | 1.0% (+0.2) | 13.7% (+8.2) |
| First hop, content | relay transit key | the same, for one content copy | 50.1% (+1.2) | 9.7% (+0.7) | 1.1% (+0.1) | 1.1% (+0.1) | 0.9% (+0.1) | 12.9% (+7.3) |
| Credential processor | transit and ring-signing keys | own transactions' fan-out times | 48.7% (-0.2) | 9.0% (+0.0) | 1.0% (-0.0) | 1.0% (-0.0) | 0.9% (-0.0) | 5.5% (-0.0) |
| Content server | transit and registry-signing keys | the records it submitted; its own content arrivals | 53.7% (+4.8) | 9.9% (+0.9) | 1.2% (+0.1) | 1.1% (+0.1) | 1.0% (+0.1) | 6.7% (+1.2) |
| Validator | token-decryption and signing keys | device identity of each reply; which credentials are disposable | 53.5% (+4.6) | 10.2% (+1.2) | 1.2% (+0.2) | 89.5% (+88.5) | 53.5% (+52.6) | 5.7% (+0.2) |
| Gatekeeper | transit and countersignature keys | own postings; which transactions are decoys | 49.1% (+0.2) | 9.0% (+0.0) | 1.0% (+0.0) | 1.0% (+0.0) | 0.9% (-0.0) | 5.6% (+0.1) |

Decoys bring every vantage to about 1% except the validator. It knows which credentials are disposable and names the device 89.5% of the time at R = 1 whatever the decoy volume. The gatekeeper and the credential processor add nothing over the passive observer. The first hops name the exact capture well above chance.

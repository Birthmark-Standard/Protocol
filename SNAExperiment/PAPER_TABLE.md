# Paper table

How often each compromised component, starting from a public registry record, names the device that produced it. Decoys are genuine transactions at a steady 40 in flight, indistinguishable to every party. Per-decision attack, 200 runs per cell. Each accuracy cell gives, in brackets, the contribution over a passive observer on the same records, in percentage points. The last column is accuracy with the decoy stream minus accuracy without it, on the same real records. Intervals and every other cell are in RESULTS.md.

| Vantage | Holds | Device named, R = 1 with decoys (random 2.1%) | Device named, R = 15 with decoys (random 1.6%) | Exact capture named, R = 1 with decoys (1/T = 2.4%) | Decoy effect on device accuracy, R = 1 |
|---|---|---|---|---|---|
| Baseline | nothing | 8.8% (+0.0) | 7.0% (+0.0) | 5.3% (+0.0) | -79.0 points |
| First hop, credential | relay transit key; source address | 9.7% (+1.0) | 7.7% (+0.8) | 13.4% (+8.1) | -78.9 points |
| First hop, content | relay transit key; source address | 9.3% (+0.5) | 7.4% (+0.4) | 12.6% (+7.3) | -78.6 points |
| Credential processor | transit and ring-signing keys | 8.7% (-0.0) | 7.0% (+0.0) | 5.3% (-0.0) | -78.8 points |
| Content server | transit and registry-signing keys | 9.6% (+0.9) | 7.7% (+0.8) | 6.5% (+1.2) | -80.2 points |
| Validator | token-decryption and signing keys; device identity | 9.8% (+1.1) | 7.8% (+0.8) | 5.9% (+0.5) | -79.7 points |
| Gatekeeper | transit and countersignature keys | 8.6% (-0.1) | 6.9% (-0.1) | 5.3% (+0.0) | -79.2 points |

With decoys, every component names the device behind a record at about 4 times the random-pick rate, and within about a point of what a passive observer achieves. Decoys cut every component's accuracy at R = 1 by about 79 points. The first hops remain the one component that names the exact capture well above chance.

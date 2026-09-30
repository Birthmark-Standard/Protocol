# Paper table

Per-decision accuracy of each vantage at naming the credential transaction behind a piece of content, against chance 1/L, where L is the number of transactions in flight. 200 runs per cell; intervals are 95% and resample whole runs. "Upper bound" marks a vantage that can tell decoys apart at a volume above 40, the top of its deployment range. Details and every other cell are in RESULTS.md.

| Vantage | Holds | Knows exactly | Label | Accuracy, L = 4 (1/L = 25%) | L = 40 (1/L = 2.5%) | L = 500 (1/L = 0.2%) | Lift, L = 40 to 500 | Contribution over baseline, L = 40 | With decoys, R = 4, T = 500 (1/T = 0.2%) | Confidence AUC, L = 40 |
|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | nothing | sizes and timing on every link | none | 42.11% [41.54%, 42.68%] | 5.33% [5.21%, 5.45%] | 0.42% [0.41%, 0.43%] | 2.13 to 2.12, holds flat | +0.00 pts [+0.00, +0.00] | 42.11% | 0.556 [0.550, 0.563] |
| First hop, credential | relay transit key | source address and arrival; own hold and forward | network address | 37.15% [36.64%, 37.69%] | 4.46% [4.35%, 4.56%] | 0.36% [0.35%, 0.37%] | 1.78 to 1.78, holds flat | +0.30 pts [+0.16, +0.45] | 37.15% | 0.550 [0.542, 0.558] |
| First hop, content | relay transit key | the same, for one content copy | network address | 30.29% [29.90%, 30.70%] | 3.41% [3.34%, 3.47%] | 0.26% [0.26%, 0.27%] | 1.36 to 1.31, falls | -0.13 pts [-0.22, -0.03] | 30.29% | 0.545 [0.539, 0.551] |
| Credential processor | transit and ring-signing keys | packet hash, key reference, own fan-out sends, reply arrival | transaction (manufacturer) | 44.73% [44.19%, 45.31%] | 5.66% [5.54%, 5.79%] | 0.41% [0.40%, 0.42%] (upper bound) | 2.27 to 2.03, falls | +0.34 pts [+0.17, +0.51] | 44.73% | 0.560 [0.553, 0.566] |
| Content server | transit and registry-signing keys | content hash, content arrival, own quorum record, board postings | content | 44.70% [44.23%, 45.17%] | 5.98% [5.89%, 6.08%] | 0.49% [0.48%, 0.50%] | 2.39 to 2.46, rises | +3.22 pts [+3.11, +3.33] | 0.49% | 0.579 [0.574, 0.584] |
| Validator | token-decryption and signing keys | device identity, request arrival, reply moment | device identity | 41.95% [41.45%, 42.50%] | 5.28% [5.15%, 5.40%] | 0.42% [0.41%, 0.43%] (upper bound) | 2.11 to 2.09, holds flat | +0.00 pts [+0.00, +0.00] | 41.95% | 0.558 [0.552, 0.565] |
| Gatekeeper | transit and countersignature keys | packet hash, sender's address, own arrival, hold outcome and posting | transaction | 51.24% [50.94%, 51.55%] | 21.29% [21.18%, 21.40%] | 2.99% [2.98%, 3.01%] (upper bound) | 8.52 to 14.96, rises | +16.66 pts [+16.54, +16.79] | 51.24% | 0.620 [0.617, 0.622] |

Every vantage is above 1/L at L = 4, 40 and 500, including the baseline with no keys. Decoys leave every registry-linking vantage exactly where it was without them (the R = 4, T = 500 column equals the L = 4 column), and lower only the content server, to about 2.5 times 1/T. The gatekeeper's lift rises with volume, to 15 at L = 500.

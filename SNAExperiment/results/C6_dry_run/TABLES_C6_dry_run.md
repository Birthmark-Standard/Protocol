DRY RUN: fewer runs than the full count. These numbers are not results.

# Experiment C6: the credential path and blind-issued one-time certificates

Chance is the expected accuracy of naming, for each decision, one candidate drawn uniformly from those the vantage finds feasible; zero when the truth is not feasible. Latency: the mean time from capture to posted record of each candidate in that cell.


## passive observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | observer | 2 | 413 | 6.78% [5.39%, 8.13%] | 1.11% | ×6.13 | +0.00 | 0.440 | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | observer | 2 | 413 | 6.05% [4.41%, 7.66%] | 1.46% | ×4.14 | +0.00 | 0.671 | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | observer | 2 | 413 | 2.66% [1.47%, 3.83%] | 1.46% | ×1.82 | +0.00 | 0.643 | no | 10.50% |
| R1 | W1 | credential path | 1186 s | observer | 2 | 388 | 0.00% [0.00%, 0.00%] | 1.37% | ×0.00 | +0.00 | — | no | 10.50% |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | observer | 2 | 388 | 0.77% [0.00%, 1.46%] | 1.84% | ×0.42 | +0.00 | 0.033 | no | 10.50% |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | observer | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.137 | no | 10.50% |
| R1 | W2 | credential path | 1195 s | observer | 2 | 366 | 8.20% [4.44%, 11.83%] | 1.40% | ×5.86 | +0.00 | 0.347 | no | 10.50% |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | observer | 2 | 366 | 7.92% [6.67%, 9.14%] | 1.86% | ×4.25 | +0.00 | 0.511 | no | 10.50% |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | observer | 2 | 366 | 5.74% [4.84%, 6.67%] | 1.87% | ×3.07 | +0.00 | 0.365 | no | 10.50% |
| R1 | Wmis | credential path | 1195 s | observer | 2 | 366 | 20.77% [15.56%, 25.81%] | 1.11% | ×18.70 | +0.00 | 0.879 | yes | 10.50% |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | observer | 2 | 366 | 20.49% [17.22%, 23.66%] | 1.47% | ×13.98 | +0.00 | 0.715 | yes | 10.50% |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | observer | 2 | 366 | 16.12% [15.00%, 17.20%] | 1.48% | ×10.92 | +0.00 | 0.682 | yes | 10.50% |
| R1 | chain100 | credential path | 1213 s | observer | 2 | 420 | 7.14% [5.16%, 9.18%] | 1.12% | ×6.36 | +0.00 | 0.478 | no | 10.50% |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | observer | 2 | 421 | 4.75% [1.41%, 8.17%] | 1.48% | ×3.22 | +0.00 | 0.490 | no | 10.50% |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | observer | 2 | 420 | 5.48% [3.29%, 7.73%] | 1.48% | ×3.71 | +0.00 | 0.519 | no | 10.50% |
| R1 | chain50 | credential path | 1208 s | observer | 2 | 421 | 4.51% [2.35%, 6.73%] | 0.88% | ×5.11 | +0.00 | 0.420 | no | 10.50% |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | observer | 2 | 421 | 4.51% [3.29%, 5.77%] | 1.27% | ×3.56 | +0.00 | 0.499 | no | 10.50% |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | observer | 2 | 421 | 6.41% [3.29%, 9.62%] | 1.27% | ×5.05 | +0.00 | 0.465 | no | 10.50% |
| R100 | W0 | credential path | 1208 s | observer | 2 | 1,216 | 1.73% [1.16%, 2.28%] | 0.55% | ×3.12 | +0.00 | 0.427 | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | observer | 2 | 1,216 | 3.04% [2.33%, 3.75%] | 0.74% | ×4.13 | +0.00 | 0.498 | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | observer | 2 | 1,216 | 2.88% [2.33%, 3.42%] | 0.75% | ×3.84 | +0.00 | 0.542 | no | 5.33% |
| R100 | W1 | credential path | 1197 s | observer | 2 | 1,312 | 6.94% [3.56%, 10.50%] | 0.70% | ×9.94 | +0.00 | 0.635 | yes | 5.33% |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | observer | 2 | 1,312 | 7.16% [4.01%, 10.50%] | 0.94% | ×7.61 | +0.00 | 0.613 | yes | 5.33% |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | observer | 2 | 1,312 | 6.10% [4.45%, 7.84%] | 0.94% | ×6.51 | +0.00 | 0.639 | yes | 5.33% |
| R100 | W2 | credential path | 1210 s | observer | 2 | 1,221 | 7.13% [5.33%, 8.97%] | 0.70% | ×10.13 | +0.00 | 0.554 | yes | 5.33% |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | observer | 2 | 1,221 | 6.63% [4.68%, 8.64%] | 0.96% | ×6.94 | +0.00 | 0.590 | yes | 5.33% |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | observer | 2 | 1,221 | 5.81% [3.23%, 8.47%] | 0.94% | ×6.19 | +0.00 | 0.586 | yes | 5.33% |
| R100 | Wmis | credential path | 1210 s | observer | 2 | 1,221 | 9.83% [9.05%, 10.63%] | 0.62% | ×15.94 | +0.00 | 0.597 | yes | 5.33% |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | observer | 2 | 1,221 | 9.58% [7.75%, 11.46%] | 0.83% | ×11.59 | +0.00 | 0.613 | yes | 5.33% |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | observer | 2 | 1,221 | 9.17% [7.11%, 11.30%] | 0.83% | ×11.04 | +0.00 | 0.605 | yes | 5.33% |
| R100 | chain100 | credential path | 1189 s | observer | 2 | 1,234 | 1.78% [1.73%, 1.84%] | 0.56% | ×3.18 | +0.00 | 0.535 | no | 5.33% |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | observer | 2 | 1,224 | 2.45% [2.38%, 2.53%] | 0.75% | ×3.27 | +0.00 | 0.608 | no | 5.33% |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | observer | 2 | 1,243 | 3.14% [3.12%, 3.16%] | 0.74% | ×4.23 | +0.00 | 0.644 | no | 5.33% |
| R100 | chain50 | credential path | 1201 s | observer | 2 | 1,242 | 2.17% [2.17%, 2.18%] | 0.44% | ×4.94 | +0.00 | 0.506 | no | 5.33% |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | observer | 2 | 1,223 | 2.37% [2.06%, 2.70%] | 0.64% | ×3.69 | +0.00 | 0.562 | no | 5.33% |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | observer | 2 | 1,246 | 3.13% [2.65%, 3.64%] | 0.64% | ×4.86 | +0.00 | 0.526 | no | 5.33% |

## first relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | first_hop | 2 | 8,260 | 6.59% [5.17%, 7.97%] | 1.11% | ×5.95 | -0.19 | 0.438 | yes | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | first_hop | 2 | 8,260 | 6.13% [4.51%, 7.70%] | 1.46% | ×4.19 | +0.07 | 0.661 | yes | 10.50% |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | first_hop | 2 | 8,260 | 2.93% [1.76%, 4.07%] | 1.46% | ×2.00 | +0.27 | 0.438 | yes | 10.50% |
| R1 | W1 | credential path | 1186 s | first_hop | 2 | 7,760 | 0.00% [0.00%, 0.00%] | 1.37% | ×0.00 | +0.00 | — | no | 10.50% |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | first_hop | 2 | 7,760 | 0.71% [0.03%, 1.31%] | 1.84% | ×0.39 | -0.06 | 0.044 | yes | 10.50% |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | first_hop | 2 | 7,760 | 0.67% [0.00%, 1.26%] | 1.83% | ×0.37 | +0.15 | 0.134 | yes | 10.50% |
| R1 | W2 | credential path | 1195 s | first_hop | 2 | 7,320 | 8.33% [4.28%, 12.26%] | 1.40% | ×5.96 | +0.14 | 0.341 | yes | 10.50% |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | first_hop | 2 | 7,320 | 7.98% [6.44%, 9.46%] | 1.86% | ×4.28 | +0.05 | 0.503 | yes | 10.50% |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | first_hop | 2 | 7,320 | 5.67% [4.76%, 6.61%] | 1.87% | ×3.03 | -0.07 | 0.376 | yes | 10.50% |
| R1 | Wmis | credential path | 1195 s | first_hop | 2 | 7,320 | 20.92% [15.92%, 25.75%] | 1.11% | ×18.83 | +0.15 | 0.878 | yes | 10.50% |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | first_hop | 2 | 7,320 | 20.15% [16.69%, 23.49%] | 1.47% | ×13.75 | -0.34 | 0.713 | yes | 10.50% |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | first_hop | 2 | 7,320 | 16.12% [14.83%, 17.37%] | 1.48% | ×10.92 | +0.00 | 0.677 | yes | 10.50% |
| R1 | chain100 | credential path | 1213 s | first_hop | 2 | 8,400 | 7.37% [5.68%, 9.11%] | 1.12% | ×6.56 | +0.23 | 0.484 | yes | 10.50% |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | first_hop | 2 | 8,420 | 4.70% [1.50%, 7.98%] | 1.48% | ×3.19 | -0.05 | 0.496 | yes | 10.50% |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | first_hop | 2 | 8,400 | 5.39% [3.29%, 7.56%] | 1.48% | ×3.65 | -0.08 | 0.533 | yes | 10.50% |
| R1 | chain50 | credential path | 1208 s | first_hop | 2 | 8,420 | 4.50% [2.44%, 6.61%] | 0.88% | ×5.10 | -0.01 | 0.423 | yes | 10.50% |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | first_hop | 2 | 8,420 | 4.57% [3.17%, 6.01%] | 1.27% | ×3.61 | +0.06 | 0.506 | yes | 10.50% |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | first_hop | 2 | 8,420 | 6.22% [3.22%, 9.30%] | 1.27% | ×4.90 | -0.19 | 0.464 | yes | 10.50% |
| R100 | W0 | credential path | 1208 s | first_hop | 2 | 24,320 | 1.74% [1.21%, 2.26%] | 0.55% | ×3.15 | +0.02 | 0.440 | yes | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | first_hop | 2 | 24,320 | 3.10% [2.40%, 3.79%] | 0.74% | ×4.21 | +0.06 | 0.495 | yes | 5.33% |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | first_hop | 2 | 24,320 | 2.92% [2.45%, 3.39%] | 0.75% | ×3.90 | +0.05 | 0.534 | yes | 5.33% |
| R100 | W1 | credential path | 1197 s | first_hop | 2 | 26,240 | 6.93% [3.61%, 10.44%] | 0.70% | ×9.93 | -0.00 | 0.633 | yes | 5.33% |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | first_hop | 2 | 26,240 | 7.22% [4.09%, 10.53%] | 0.94% | ×7.68 | +0.06 | 0.612 | yes | 5.33% |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | first_hop | 2 | 26,240 | 6.19% [4.58%, 7.90%] | 0.94% | ×6.62 | +0.10 | 0.631 | yes | 5.33% |
| R100 | W2 | credential path | 1210 s | first_hop | 2 | 24,420 | 7.08% [5.25%, 8.97%] | 0.70% | ×10.07 | -0.04 | 0.556 | yes | 5.33% |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | first_hop | 2 | 24,420 | 6.61% [4.70%, 8.57%] | 0.96% | ×6.92 | -0.02 | 0.591 | yes | 5.33% |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | first_hop | 2 | 24,420 | 5.86% [3.31%, 8.48%] | 0.94% | ×6.24 | +0.05 | 0.582 | yes | 5.33% |
| R100 | Wmis | credential path | 1210 s | first_hop | 2 | 24,420 | 9.81% [9.01%, 10.63%] | 0.62% | ×15.91 | -0.02 | 0.597 | yes | 5.33% |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | first_hop | 2 | 24,420 | 9.56% [7.91%, 11.25%] | 0.83% | ×11.56 | -0.02 | 0.612 | yes | 5.33% |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | first_hop | 2 | 24,420 | 9.28% [7.30%, 11.30%] | 0.83% | ×11.16 | +0.10 | 0.601 | yes | 5.33% |
| R100 | chain100 | credential path | 1189 s | first_hop | 2 | 24,680 | 1.82% [1.75%, 1.89%] | 0.56% | ×3.24 | +0.03 | 0.532 | yes | 5.33% |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | first_hop | 2 | 24,480 | 2.59% [2.40%, 2.79%] | 0.75% | ×3.45 | +0.14 | 0.601 | yes | 5.33% |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | first_hop | 2 | 24,860 | 3.15% [3.14%, 3.16%] | 0.74% | ×4.24 | +0.01 | 0.637 | yes | 5.33% |
| R100 | chain50 | credential path | 1201 s | first_hop | 2 | 24,840 | 2.16% [2.12%, 2.20%] | 0.44% | ×4.91 | -0.02 | 0.499 | yes | 5.33% |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | first_hop | 2 | 24,460 | 2.34% [1.97%, 2.74%] | 0.64% | ×3.64 | -0.03 | 0.573 | yes | 5.33% |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | first_hop | 2 | 24,920 | 3.04% [2.70%, 3.39%] | 0.64% | ×4.72 | -0.09 | 0.530 | yes | 5.33% |

## destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | content_server | 2 | 826 | 6.42% [5.39%, 7.42%] | 1.13% | ×5.67 | -0.36 | 0.476 | yes | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | destination | 2 | 413 | 7.02% [4.90%, 9.09%] | 1.62% | ×4.34 | +0.97 | 0.444 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | destination | 2 | 413 | 4.12% [1.96%, 6.22%] | 1.61% | ×2.55 | +1.45 | 0.390 | no | not applicable |
| R1 | W1 | credential path | 1186 s | content_server | 2 | 776 | 0.39% [0.00%, 0.73%] | 1.41% | ×0.27 | +0.39 | 0.448 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | destination | 2 | 388 | 1.80% [1.10%, 2.43%] | 2.02% | ×0.89 | +1.03 | 0.358 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | destination | 2 | 388 | 1.29% [0.00%, 2.43%] | 2.00% | ×0.65 | +0.77 | 0.085 | no | not applicable |
| R1 | W2 | credential path | 1195 s | content_server | 2 | 732 | 9.02% [5.56%, 12.37%] | 1.43% | ×6.28 | +0.82 | 0.419 | yes | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | destination | 2 | 366 | 7.38% [4.44%, 10.22%] | 2.05% | ×3.60 | -0.55 | 0.472 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | destination | 2 | 366 | 4.92% [4.44%, 5.38%] | 2.05% | ×2.39 | -0.82 | 0.447 | no | not applicable |
| R1 | Wmis | credential path | 1195 s | content_server | 2 | 732 | 20.49% [15.28%, 25.54%] | 1.13% | ×18.09 | -0.27 | 0.723 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | destination | 2 | 366 | 17.76% [15.56%, 19.89%] | 1.62% | ×10.94 | -2.73 | 0.719 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | destination | 2 | 366 | 13.11% [12.22%, 13.98%] | 1.63% | ×8.05 | -3.01 | 0.647 | no | not applicable |
| R1 | chain100 | credential path | 1213 s | content_server | 2 | 840 | 7.14% [3.76%, 10.63%] | 1.15% | ×6.24 | +0.00 | 0.425 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | destination | 2 | 421 | 4.75% [2.35%, 7.21%] | 1.62% | ×2.93 | +0.00 | 0.356 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | destination | 2 | 420 | 5.71% [2.82%, 8.70%] | 1.63% | ×3.50 | +0.24 | 0.683 | no | not applicable |
| R1 | chain50 | credential path | 1208 s | content_server | 2 | 842 | 5.11% [3.99%, 6.25%] | 0.91% | ×5.61 | +0.59 | 0.483 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | destination | 2 | 421 | 4.04% [2.82%, 5.29%] | 1.43% | ×2.83 | -0.48 | 0.419 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | destination | 2 | 421 | 4.28% [1.88%, 6.73%] | 1.44% | ×2.97 | -2.14 | 0.674 | no | not applicable |
| R100 | W0 | credential path | 1208 s | content_server | 2 | 2,432 | 2.59% [1.99%, 3.18%] | 0.57% | ×4.58 | +0.86 | 0.472 | yes | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | destination | 2 | 1,216 | 2.30% [1.33%, 3.26%] | 0.82% | ×2.82 | -0.74 | 0.544 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | destination | 2 | 1,216 | 2.80% [2.44%, 3.16%] | 0.83% | ×3.38 | -0.08 | 0.500 | no | not applicable |
| R100 | W1 | credential path | 1197 s | content_server | 2 | 2,624 | 7.05% [4.53%, 9.72%] | 0.72% | ×9.84 | +0.11 | 0.576 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | destination | 2 | 1,312 | 7.24% [4.60%, 10.03%] | 1.03% | ×7.02 | +0.08 | 0.626 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | destination | 2 | 1,312 | 6.33% [5.34%, 7.37%] | 1.02% | ×6.17 | +0.23 | 0.582 | yes | not applicable |
| R100 | W2 | credential path | 1210 s | content_server | 2 | 2,442 | 6.84% [4.85%, 8.89%] | 0.72% | ×9.47 | -0.29 | 0.594 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | destination | 2 | 1,221 | 5.90% [5.17%, 6.64%] | 1.05% | ×5.60 | -0.74 | 0.622 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | destination | 2 | 1,221 | 5.81% [3.07%, 8.64%] | 1.03% | ×5.65 | +0.00 | 0.440 | yes | not applicable |
| R100 | Wmis | credential path | 1210 s | content_server | 2 | 2,442 | 9.17% [8.00%, 10.38%] | 0.63% | ×14.53 | -0.66 | 0.651 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | destination | 2 | 1,221 | 8.60% [7.75%, 9.47%] | 0.92% | ×9.40 | -0.98 | 0.633 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | destination | 2 | 1,221 | 8.85% [6.79%, 10.96%] | 0.92% | ×9.64 | -0.33 | 0.590 | yes | not applicable |
| R100 | chain100 | credential path | 1189 s | content_server | 2 | 2,468 | 3.08% [3.07%, 3.09%] | 0.57% | ×5.39 | +1.30 | 0.536 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | destination | 2 | 1,224 | 3.59% [3.33%, 3.87%] | 0.83% | ×4.34 | +1.14 | 0.517 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | destination | 2 | 1,243 | 3.22% [2.33%, 4.05%] | 0.82% | ×3.92 | +0.08 | 0.502 | no | not applicable |
| R100 | chain50 | credential path | 1201 s | content_server | 2 | 2,484 | 2.98% [2.65%, 3.33%] | 0.45% | ×6.56 | +0.81 | 0.550 | yes | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | destination | 2 | 1,223 | 3.43% [3.38%, 3.49%] | 0.73% | ×4.74 | +1.06 | 0.480 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | destination | 2 | 1,246 | 3.53% [3.15%, 3.89%] | 0.73% | ×4.84 | +0.40 | 0.500 | no | not applicable |

## first relay with the destination on its path

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | first_relay_with_destination | 2 | 826 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +93.22 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | first_relay_with_destination | 2 | 413 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +93.95 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | first_relay_with_destination | 2 | 413 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +97.34 | — | no | not applicable |
| R1 | W1 | credential path | 1186 s | first_relay_with_destination | 2 | 776 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +100.00 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | first_relay_with_destination | 2 | 388 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +99.23 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | first_relay_with_destination | 2 | 388 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +99.48 | — | no | not applicable |
| R1 | W2 | credential path | 1195 s | first_relay_with_destination | 2 | 732 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +91.80 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | first_relay_with_destination | 2 | 366 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +92.08 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | first_relay_with_destination | 2 | 366 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +94.26 | — | no | not applicable |
| R1 | Wmis | credential path | 1195 s | first_relay_with_destination | 2 | 732 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +79.23 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | first_relay_with_destination | 2 | 366 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +79.51 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | first_relay_with_destination | 2 | 366 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +83.88 | — | no | not applicable |
| R1 | chain100 | credential path | 1213 s | first_relay_with_destination | 2 | 840 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +92.86 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | first_relay_with_destination | 2 | 421 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +95.25 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | first_relay_with_destination | 2 | 420 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +94.52 | — | no | not applicable |
| R1 | chain50 | credential path | 1208 s | first_relay_with_destination | 2 | 842 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +95.49 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | first_relay_with_destination | 2 | 421 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +95.49 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | first_relay_with_destination | 2 | 421 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +93.59 | — | no | not applicable |
| R100 | W0 | credential path | 1208 s | first_relay_with_destination | 2 | 2,432 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +98.27 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | first_relay_with_destination | 2 | 1,216 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +96.96 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | first_relay_with_destination | 2 | 1,216 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +97.12 | — | no | not applicable |
| R100 | W1 | credential path | 1197 s | first_relay_with_destination | 2 | 2,624 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +93.06 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | first_relay_with_destination | 2 | 1,312 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +92.84 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | first_relay_with_destination | 2 | 1,312 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +93.90 | — | no | not applicable |
| R100 | W2 | credential path | 1210 s | first_relay_with_destination | 2 | 2,442 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +92.87 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | first_relay_with_destination | 2 | 1,221 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +93.37 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | first_relay_with_destination | 2 | 1,221 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +94.19 | — | no | not applicable |
| R100 | Wmis | credential path | 1210 s | first_relay_with_destination | 2 | 2,442 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +90.17 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | first_relay_with_destination | 2 | 1,221 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +90.42 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | first_relay_with_destination | 2 | 1,221 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +90.83 | — | no | not applicable |
| R100 | chain100 | credential path | 1189 s | first_relay_with_destination | 2 | 2,468 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +98.22 | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | first_relay_with_destination | 2 | 1,224 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +97.55 | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | first_relay_with_destination | 2 | 1,243 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +96.86 | — | no | not applicable |
| R100 | chain50 | credential path | 1201 s | first_relay_with_destination | 2 | 2,484 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +97.83 | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | first_relay_with_destination | 2 | 1,223 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +97.63 | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | first_relay_with_destination | 2 | 1,246 | 100.00% [100.00%, 100.00%] | 100.00% | ×1.00 | +96.87 | — | no | not applicable |

## destination_keyed

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | destination_keyed | 2 | 413 | 14.29% [9.31%, 19.14%] | 5.25% | ×2.72 | +8.23 | 0.488 | yes | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | destination_keyed | 2 | 413 | 15.50% [12.75%, 18.18%] | 5.29% | ×2.93 | +12.83 | 0.461 | yes | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | destination_keyed | 2 | 388 | 6.96% [6.04%, 7.77%] | 6.95% | ×1.00 | +6.19 | 0.495 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | destination_keyed | 2 | 388 | 5.93% [5.49%, 6.31%] | 6.90% | ×0.86 | +5.41 | 0.461 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | destination_keyed | 2 | 366 | 19.67% [18.28%, 21.11%] | 6.73% | ×2.92 | +11.75 | 0.633 | yes | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | destination_keyed | 2 | 366 | 15.85% [9.14%, 22.78%] | 6.83% | ×2.32 | +10.11 | 0.617 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | destination_keyed | 2 | 366 | 25.14% [22.22%, 27.96%] | 5.27% | ×4.77 | +4.64 | 0.744 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | destination_keyed | 2 | 366 | 26.23% [23.33%, 29.03%] | 5.32% | ×4.93 | +10.11 | 0.636 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | destination_keyed | 2 | 421 | 1.43% [0.47%, 2.40%] | 0.52% | ×2.73 | -3.33 | 0.785 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | destination_keyed | 2 | 420 | 2.14% [1.41%, 2.90%] | 0.53% | ×4.06 | -3.33 | 0.888 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | destination_keyed | 2 | 421 | 0.95% [0.47%, 1.44%] | 0.46% | ×2.07 | -3.56 | 0.784 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | destination_keyed | 2 | 421 | 0.95% [0.47%, 1.44%] | 0.46% | ×2.05 | -5.46 | 0.914 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | destination_keyed | 2 | 1,216 | 7.32% [6.15%, 8.47%] | 2.37% | ×3.09 | +4.28 | 0.597 | yes | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | destination_keyed | 2 | 1,216 | 7.24% [6.51%, 7.97%] | 2.41% | ×3.00 | +4.36 | 0.587 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | destination_keyed | 2 | 1,312 | 13.87% [11.72%, 16.14%] | 3.05% | ×4.55 | +6.71 | 0.666 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | destination_keyed | 2 | 1,312 | 12.04% [10.68%, 13.48%] | 3.03% | ×3.98 | +5.95 | 0.695 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | destination_keyed | 2 | 1,221 | 11.71% [11.63%, 11.79%] | 3.08% | ×3.81 | +5.08 | 0.603 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | destination_keyed | 2 | 1,221 | 13.35% [12.60%, 14.12%] | 3.01% | ×4.43 | +7.53 | 0.526 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | destination_keyed | 2 | 1,221 | 16.38% [16.16%, 16.61%] | 2.64% | ×6.21 | +6.80 | 0.655 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | destination_keyed | 2 | 1,221 | 15.23% [14.22%, 16.28%] | 2.64% | ×5.77 | +6.06 | 0.647 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | destination_keyed | 2 | 1,224 | 2.37% [2.22%, 2.53%] | 1.10% | ×2.16 | -0.08 | 0.604 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | destination_keyed | 2 | 1,243 | 1.61% [1.40%, 1.83%] | 1.15% | ×1.40 | -1.53 | 0.664 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | destination_keyed | 2 | 1,223 | 3.76% [3.17%, 4.39%] | 2.32% | ×1.62 | +1.39 | 0.638 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | destination_keyed | 2 | 1,246 | 4.57% [3.58%, 5.63%] | 2.06% | ×2.22 | +1.44 | 0.600 | yes | not applicable |

## issuer_0

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_0 [share 50%, all records] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.05 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_0 [share 50%, all records] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -2.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_0 [share 50%, other issuers' devices] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.05 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_0 [share 50%, other issuers' devices] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -2.66 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_0 [share 50%, all records] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.77 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_0 [share 50%, all records] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.52 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_0 [share 50%, other issuers' devices] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.77 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_0 [share 50%, other issuers' devices] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.52 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_0 [share 50%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.92 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0 [share 50%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.74 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_0 [share 50%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.92 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0 [share 50%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.74 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_0 [share 50%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -20.49 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0 [share 50%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -16.12 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_0 [share 50%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -20.49 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0 [share 50%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -16.12 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_0 [share 50%, all records] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.75 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_0 [share 50%, all records] | 2 | 420 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.48 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_0 [share 50%, other issuers' devices] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.75 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_0 [share 50%, other issuers' devices] | 2 | 420 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.48 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_0 [share 50%, all records] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.51 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_0 [share 50%, all records] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.41 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_0 [share 50%, other issuers' devices] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.51 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_0 [share 50%, other issuers' devices] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.41 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0 [share 50%, all records] | 2 | 1,216 | 2.06% [1.83%, 2.28%] | 0.62% | ×3.30 | -0.99 | 0.600 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0 [share 50%, all records] | 2 | 1,216 | 1.48% [1.16%, 1.79%] | 0.62% | ×2.37 | -1.40 | 0.404 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0 [share 50%, its own devices] | 2 | 663 | 3.77% [3.18%, 4.42%] | 1.14% | ×3.30 | +1.21 | 0.611 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0 [share 50%, its own devices] | 2 | 663 | 2.71% [2.02%, 3.47%] | 1.14% | ×2.37 | +0.15 | 0.384 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0 [share 50%, other issuers' devices] | 2 | 553 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -3.62 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0 [share 50%, other issuers' devices] | 2 | 553 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -3.25 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0 [share 50%, all records] | 2 | 1,312 | 5.49% [0.15%, 11.13%] | 0.99% | ×5.54 | -1.68 | 0.310 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0 [share 50%, all records] | 2 | 1,312 | 5.64% [0.00%, 11.60%] | 0.99% | ×5.70 | -0.46 | 0.220 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0 [share 50%, its own devices] | 2 | 689 | 10.45% [0.27%, 22.12%] | 1.88% | ×5.54 | +0.29 | 0.305 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0 [share 50%, its own devices] | 2 | 689 | 10.74% [0.00%, 23.05%] | 1.88% | ×5.70 | +3.05 | 0.195 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0 [share 50%, other issuers' devices] | 2 | 623 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -3.85 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0 [share 50%, other issuers' devices] | 2 | 623 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.33 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0 [share 50%, all records] | 2 | 1,221 | 4.50% [0.00%, 9.14%] | 1.06% | ×4.25 | -2.13 | 0.770 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0 [share 50%, all records] | 2 | 1,221 | 4.50% [0.00%, 9.14%] | 1.06% | ×4.25 | -1.31 | 0.794 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0 [share 50%, its own devices] | 2 | 704 | 7.81% [0.00%, 15.62%] | 1.84% | ×4.25 | -0.14 | 0.780 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0 [share 50%, its own devices] | 2 | 704 | 7.81% [0.00%, 15.62%] | 1.84% | ×4.25 | -0.57 | 0.802 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0 [share 50%, other issuers' devices] | 2 | 517 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.84 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0 [share 50%, other issuers' devices] | 2 | 517 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -2.32 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0 [share 50%, all records] | 2 | 1,221 | 7.13% [5.17%, 9.14%] | 0.94% | ×7.56 | -2.46 | 0.573 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0 [share 50%, all records] | 2 | 1,221 | 7.37% [5.65%, 9.14%] | 0.94% | ×7.82 | -1.80 | 0.568 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0 [share 50%, its own devices] | 2 | 704 | 12.36% [9.09%, 15.62%] | 1.63% | ×7.56 | +0.57 | 0.574 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0 [share 50%, its own devices] | 2 | 704 | 12.78% [9.94%, 15.62%] | 1.63% | ×7.82 | +1.56 | 0.570 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0 [share 50%, other issuers' devices] | 2 | 517 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.58 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0 [share 50%, other issuers' devices] | 2 | 517 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.38 | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0 [share 50%, all records] | 2 | 1,224 | 1.55% [0.84%, 2.22%] | 0.61% | ×2.53 | -0.90 | 0.522 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0 [share 50%, all records] | 2 | 1,243 | 1.29% [0.50%, 2.02%] | 0.62% | ×2.09 | -1.85 | 0.392 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0 [share 50%, its own devices] | 2 | 466 | 3.43% [2.45%, 4.20%] | 1.13% | ×3.04 | +0.00 | 0.595 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0 [share 50%, its own devices] | 2 | 466 | 2.36% [1.47%, 3.05%] | 1.13% | ×2.09 | -0.43 | 0.456 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0 [share 50%, other issuers' devices] | 2 | 758 | 0.40% [0.00%, 0.82%] | 0.30% | ×1.32 | -1.45 | 0.143 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0 [share 50%, other issuers' devices] | 2 | 777 | 0.64% [0.00%, 1.32%] | 0.31% | ×2.08 | -2.70 | 0.326 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0 [share 50%, all records] | 2 | 1,223 | 1.55% [1.01%, 2.06%] | 0.49% | ×3.15 | -0.82 | 0.537 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0 [share 50%, all records] | 2 | 1,246 | 1.12% [0.66%, 1.56%] | 0.49% | ×2.27 | -2.01 | 0.459 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0 [share 50%, its own devices] | 2 | 466 | 3.43% [2.45%, 4.20%] | 1.13% | ×3.04 | -0.86 | 0.595 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0 [share 50%, its own devices] | 2 | 466 | 2.36% [1.47%, 3.05%] | 1.13% | ×2.09 | -0.64 | 0.456 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0 [share 50%, other issuers' devices] | 2 | 757 | 0.40% [0.26%, 0.54%] | 0.10% | ×3.88 | -0.79 | 0.355 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0 [share 50%, other issuers' devices] | 2 | 780 | 0.38% [0.25%, 0.53%] | 0.12% | ×3.29 | -2.82 | 0.597 | no | not applicable |

## issuer_0_with_observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_0_with_observer [share 50%, all records] | 2 | 413 | 3.15% [2.94%, 3.35%] | 1.46% | ×2.15 | -2.91 | 0.350 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_0_with_observer [share 50%, all records] | 2 | 413 | 2.66% [0.49%, 4.78%] | 1.46% | ×1.82 | +0.00 | 0.336 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 413 | 3.15% [2.94%, 3.35%] | 1.46% | ×2.15 | -2.91 | 0.350 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 413 | 2.66% [0.49%, 4.78%] | 1.46% | ×1.82 | +0.00 | 0.336 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_observer [share 50%, all records] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.84% | ×0.28 | -0.26 | 0.018 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_0_with_observer [share 50%, all records] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.140 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.84% | ×0.28 | -0.26 | 0.018 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.140 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_0_with_observer [share 50%, all records] | 2 | 366 | 6.56% [4.44%, 8.60%] | 1.86% | ×3.52 | -1.37 | 0.444 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_observer [share 50%, all records] | 2 | 366 | 4.92% [4.84%, 5.00%] | 1.87% | ×2.63 | -0.82 | 0.390 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 366 | 6.56% [4.44%, 8.60%] | 1.86% | ×3.52 | -1.37 | 0.444 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 366 | 4.92% [4.84%, 5.00%] | 1.87% | ×2.63 | -0.82 | 0.390 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_0_with_observer [share 50%, all records] | 2 | 366 | 13.66% [11.67%, 15.59%] | 1.47% | ×9.32 | -6.83 | 0.607 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_observer [share 50%, all records] | 2 | 366 | 13.66% [11.67%, 15.59%] | 1.48% | ×9.26 | -2.46 | 0.701 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 366 | 13.66% [11.67%, 15.59%] | 1.47% | ×9.32 | -6.83 | 0.607 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 366 | 13.66% [11.67%, 15.59%] | 1.48% | ×9.26 | -2.46 | 0.701 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_0_with_observer [share 50%, all records] | 2 | 421 | 3.56% [0.47%, 6.73%] | 1.48% | ×2.42 | -1.19 | 0.193 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_0_with_observer [share 50%, all records] | 2 | 420 | 3.57% [1.88%, 5.31%] | 1.48% | ×2.42 | -1.90 | 0.518 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 421 | 3.56% [0.47%, 6.73%] | 1.48% | ×2.42 | -1.19 | 0.193 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 420 | 3.57% [1.88%, 5.31%] | 1.48% | ×2.42 | -1.90 | 0.518 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_0_with_observer [share 50%, all records] | 2 | 421 | 2.38% [0.47%, 4.33%] | 1.27% | ×1.88 | -2.14 | 0.238 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_0_with_observer [share 50%, all records] | 2 | 421 | 3.09% [0.94%, 5.29%] | 1.27% | ×2.43 | -3.33 | 0.462 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 421 | 2.38% [0.47%, 4.33%] | 1.27% | ×1.88 | -2.14 | 0.238 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 421 | 3.09% [0.94%, 5.29%] | 1.27% | ×2.43 | -3.33 | 0.462 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,216 | 2.55% [1.83%, 3.26%] | 0.74% | ×3.46 | -0.49 | 0.528 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,216 | 2.96% [2.93%, 2.99%] | 0.75% | ×3.95 | +0.08 | 0.543 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 663 | 3.92% [2.60%, 5.36%] | 0.74% | ×5.32 | +1.36 | 0.576 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 663 | 3.47% [3.47%, 3.47%] | 0.75% | ×4.63 | +0.90 | 0.507 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 553 | 0.90% [0.78%, 1.01%] | 0.74% | ×1.23 | -2.71 | 0.297 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 553 | 2.35% [2.34%, 2.36%] | 0.75% | ×3.14 | -0.90 | 0.614 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,312 | 7.39% [5.19%, 9.72%] | 0.94% | ×7.86 | +0.23 | 0.578 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,312 | 6.55% [5.79%, 7.37%] | 0.94% | ×7.00 | +0.46 | 0.586 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 689 | 10.45% [4.35%, 17.45%] | 0.94% | ×11.10 | +0.29 | 0.669 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 689 | 8.27% [3.26%, 14.02%] | 0.93% | ×8.87 | +0.58 | 0.673 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 623 | 4.01% [1.89%, 6.21%] | 0.94% | ×4.27 | +0.16 | 0.304 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 623 | 4.65% [0.63%, 8.82%] | 0.94% | ×4.95 | +0.32 | 0.291 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,221 | 6.39% [4.36%, 8.47%] | 0.96% | ×6.68 | -0.25 | 0.593 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,221 | 6.14% [3.39%, 8.97%] | 0.94% | ×6.54 | +0.33 | 0.591 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 704 | 8.95% [3.69%, 14.20%] | 0.96% | ×9.35 | +0.99 | 0.564 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 704 | 8.95% [3.69%, 14.20%] | 0.94% | ×9.53 | +0.57 | 0.602 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 517 | 2.90% [0.40%, 5.24%] | 0.95% | ×3.04 | -1.93 | 0.451 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 517 | 2.32% [1.60%, 3.00%] | 0.94% | ×2.47 | +0.00 | 0.494 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,221 | 8.52% [7.11%, 9.97%] | 0.83% | ×10.30 | -1.06 | 0.609 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,221 | 9.34% [7.27%, 11.46%] | 0.83% | ×11.24 | +0.16 | 0.604 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 704 | 11.08% [6.53%, 15.62%] | 0.83% | ×13.42 | -0.71 | 0.487 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 704 | 11.65% [5.68%, 17.61%] | 0.83% | ×14.02 | +0.43 | 0.481 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 517 | 5.03% [2.00%, 7.87%] | 0.83% | ×6.07 | -1.55 | 0.591 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 517 | 6.19% [2.80%, 9.36%] | 0.83% | ×7.45 | -0.19 | 0.502 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,224 | 3.27% [3.17%, 3.37%] | 0.75% | ×4.36 | +0.82 | 0.464 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,243 | 3.38% [3.16%, 3.58%] | 0.74% | ×4.55 | +0.24 | 0.568 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 466 | 6.01% [4.20%, 8.33%] | 0.75% | ×8.04 | +2.58 | 0.504 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 466 | 3.86% [1.47%, 5.73%] | 0.74% | ×5.21 | +1.07 | 0.606 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 758 | 1.58% [0.77%, 2.45%] | 0.75% | ×2.11 | -0.26 | 0.381 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 777 | 3.09% [2.11%, 4.03%] | 0.74% | ×4.16 | -0.26 | 0.539 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,223 | 2.86% [2.69%, 3.04%] | 0.64% | ×4.45 | +0.49 | 0.462 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0_with_observer [share 50%, all records] | 2 | 1,246 | 2.97% [2.80%, 3.15%] | 0.64% | ×4.61 | -0.16 | 0.480 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 466 | 5.58% [3.82%, 7.84%] | 0.64% | ×8.70 | +1.29 | 0.550 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0_with_observer [share 50%, its own devices] | 2 | 466 | 3.65% [2.45%, 4.58%] | 0.64% | ×5.69 | +0.64 | 0.536 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 757 | 1.19% [0.52%, 1.90%] | 0.64% | ×1.85 | +0.00 | 0.418 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0_with_observer [share 50%, other issuers' devices] | 2 | 780 | 2.56% [1.58%, 3.50%] | 0.64% | ×3.98 | -0.64 | 0.429 | no | not applicable |

## issuer_0_with_first_relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 413 | 3.15% [2.94%, 3.35%] | 1.46% | ×2.15 | -2.91 | 0.349 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 413 | 2.91% [1.47%, 4.31%] | 1.46% | ×1.99 | +0.24 | 0.395 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 413 | 3.15% [2.94%, 3.35%] | 1.46% | ×2.15 | -2.91 | 0.349 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 413 | 2.91% [1.47%, 4.31%] | 1.46% | ×1.99 | +0.24 | 0.395 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 388 | 0.26% [0.00%, 0.49%] | 1.84% | ×0.14 | -0.52 | 0.003 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.061 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 388 | 0.26% [0.00%, 0.49%] | 1.84% | ×0.14 | -0.52 | 0.003 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.061 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 366 | 6.83% [4.44%, 9.14%] | 1.86% | ×3.66 | -1.09 | 0.432 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 366 | 4.64% [4.30%, 5.00%] | 1.87% | ×2.48 | -1.09 | 0.438 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 366 | 6.83% [4.44%, 9.14%] | 1.86% | ×3.66 | -1.09 | 0.432 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 366 | 4.64% [4.30%, 5.00%] | 1.87% | ×2.48 | -1.09 | 0.438 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 366 | 13.93% [12.22%, 15.59%] | 1.47% | ×9.51 | -6.56 | 0.605 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 366 | 13.39% [11.67%, 15.05%] | 1.48% | ×9.07 | -2.73 | 0.630 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 366 | 13.93% [12.22%, 15.59%] | 1.47% | ×9.51 | -6.56 | 0.605 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 366 | 13.39% [11.67%, 15.05%] | 1.48% | ×9.07 | -2.73 | 0.630 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 421 | 3.80% [0.94%, 6.73%] | 1.48% | ×2.58 | -0.95 | 0.212 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 420 | 3.57% [1.41%, 5.80%] | 1.48% | ×2.42 | -1.90 | 0.545 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 421 | 3.80% [0.94%, 6.73%] | 1.48% | ×2.58 | -0.95 | 0.212 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 420 | 3.57% [1.41%, 5.80%] | 1.48% | ×2.42 | -1.90 | 0.545 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 421 | 2.38% [0.47%, 4.33%] | 1.27% | ×1.88 | -2.14 | 0.239 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 421 | 3.09% [0.94%, 5.29%] | 1.27% | ×2.43 | -3.33 | 0.459 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 421 | 2.38% [0.47%, 4.33%] | 1.27% | ×1.88 | -2.14 | 0.239 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 421 | 3.09% [0.94%, 5.29%] | 1.27% | ×2.43 | -3.33 | 0.459 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,216 | 2.55% [1.83%, 3.26%] | 0.74% | ×3.46 | -0.49 | 0.530 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,216 | 3.04% [2.99%, 3.09%] | 0.75% | ×4.06 | +0.16 | 0.519 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 663 | 3.77% [2.60%, 5.05%] | 0.74% | ×5.12 | +1.21 | 0.588 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 663 | 3.17% [2.89%, 3.47%] | 0.75% | ×4.23 | +0.60 | 0.497 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 553 | 1.08% [0.78%, 1.35%] | 0.74% | ×1.48 | -2.53 | 0.304 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 553 | 2.89% [2.69%, 3.12%] | 0.75% | ×3.87 | -0.36 | 0.551 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,312 | 7.39% [5.04%, 9.87%] | 0.94% | ×7.86 | +0.23 | 0.583 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,312 | 6.25% [5.19%, 7.37%] | 0.94% | ×6.68 | +0.15 | 0.598 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 689 | 10.45% [4.08%, 17.76%] | 0.94% | ×11.10 | +0.29 | 0.682 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 689 | 7.84% [2.72%, 13.71%] | 0.93% | ×8.40 | +0.15 | 0.675 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 623 | 4.01% [1.89%, 6.21%] | 0.94% | ×4.27 | +0.16 | 0.288 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 623 | 4.49% [0.95%, 8.17%] | 0.94% | ×4.78 | +0.16 | 0.329 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,221 | 6.06% [4.04%, 8.14%] | 0.96% | ×6.34 | -0.57 | 0.612 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,221 | 6.06% [3.23%, 8.97%] | 0.94% | ×6.45 | +0.25 | 0.595 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 704 | 8.66% [3.69%, 13.64%] | 0.96% | ×9.05 | +0.71 | 0.580 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 704 | 8.81% [3.41%, 14.20%] | 0.94% | ×9.38 | +0.43 | 0.607 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 517 | 2.51% [0.40%, 4.49%] | 0.95% | ×2.64 | -2.32 | 0.493 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 517 | 2.32% [1.60%, 3.00%] | 0.94% | ×2.47 | +0.00 | 0.495 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,221 | 8.44% [7.11%, 9.80%] | 0.83% | ×10.20 | -1.15 | 0.613 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,221 | 9.42% [7.43%, 11.46%] | 0.83% | ×11.33 | +0.25 | 0.590 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 704 | 10.94% [6.53%, 15.34%] | 0.83% | ×13.24 | -0.85 | 0.498 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 704 | 11.79% [5.97%, 17.61%] | 0.83% | ×14.19 | +0.57 | 0.471 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 517 | 5.03% [2.00%, 7.87%] | 0.83% | ×6.07 | -1.55 | 0.588 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 517 | 6.19% [2.80%, 9.36%] | 0.83% | ×7.45 | -0.19 | 0.491 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,224 | 3.10% [2.86%, 3.37%] | 0.75% | ×4.14 | +0.65 | 0.478 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,243 | 3.06% [3.00%, 3.12%] | 0.74% | ×4.12 | -0.08 | 0.585 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 466 | 5.36% [3.05%, 8.33%] | 0.75% | ×7.18 | +1.93 | 0.552 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 466 | 3.43% [1.47%, 4.96%] | 0.74% | ×4.63 | +0.64 | 0.649 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 758 | 1.72% [0.77%, 2.72%] | 0.75% | ×2.28 | -0.13 | 0.345 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 777 | 2.83% [1.84%, 3.78%] | 0.74% | ×3.81 | -0.51 | 0.541 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,223 | 2.62% [2.22%, 3.04%] | 0.64% | ×4.07 | +0.25 | 0.484 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0_with_first_relay [share 50%, all records] | 2 | 1,246 | 2.81% [2.49%, 3.15%] | 0.64% | ×4.36 | -0.32 | 0.505 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 466 | 5.36% [3.44%, 7.84%] | 0.64% | ×8.36 | +1.07 | 0.557 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0_with_first_relay [share 50%, its own devices] | 2 | 466 | 3.00% [1.96%, 3.82%] | 0.64% | ×4.68 | +0.00 | 0.610 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 757 | 0.92% [0.52%, 1.36%] | 0.64% | ×1.44 | -0.26 | 0.397 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 2 | 780 | 2.69% [1.58%, 3.75%] | 0.64% | ×4.17 | -0.51 | 0.431 | no | not applicable |

## issuer_1

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_1 [share 30%, all records] | 2 | 413 | 6.54% [6.22%, 6.86%] | 3.23% | ×2.02 | +0.48 | 0.622 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_1 [share 30%, all records] | 2 | 413 | 8.23% [4.41%, 11.96%] | 3.23% | ×2.55 | +5.57 | 0.402 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_1 [share 30%, its own devices] | 2 | 413 | 6.54% [6.22%, 6.86%] | 3.23% | ×2.02 | +0.48 | 0.622 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_1 [share 30%, its own devices] | 2 | 413 | 8.23% [4.41%, 11.96%] | 3.23% | ×2.55 | +5.57 | 0.402 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_1 [share 30%, all records] | 2 | 388 | 0.52% [0.00%, 1.10%] | 3.22% | ×0.16 | -0.26 | 0.143 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_1 [share 30%, all records] | 2 | 388 | 0.00% [0.00%, 0.00%] | 3.22% | ×0.00 | -0.52 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_1 [share 30%, its own devices] | 2 | 388 | 0.52% [0.00%, 1.10%] | 3.22% | ×0.16 | -0.26 | 0.143 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_1 [share 30%, its own devices] | 2 | 388 | 0.00% [0.00%, 0.00%] | 3.22% | ×0.00 | -0.52 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_1 [share 30%, all records] | 2 | 366 | 0.82% [0.00%, 1.67%] | 3.23% | ×0.25 | -7.10 | 0.354 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1 [share 30%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 3.23% | ×0.00 | -5.74 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_1 [share 30%, its own devices] | 2 | 366 | 0.82% [0.00%, 1.67%] | 3.23% | ×0.25 | -7.10 | 0.354 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1 [share 30%, its own devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 3.23% | ×0.00 | -5.74 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_1 [share 30%, all records] | 2 | 366 | 7.65% [6.11%, 9.14%] | 3.23% | ×2.37 | -12.84 | 0.546 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1 [share 30%, all records] | 2 | 366 | 5.74% [4.44%, 6.99%] | 3.23% | ×1.78 | -10.38 | 0.398 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_1 [share 30%, its own devices] | 2 | 366 | 7.65% [6.11%, 9.14%] | 3.23% | ×2.37 | -12.84 | 0.546 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1 [share 30%, its own devices] | 2 | 366 | 5.74% [4.44%, 6.99%] | 3.23% | ×1.78 | -10.38 | 0.398 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1 [share 30%, all records] | 2 | 421 | 4.04% [3.85%, 4.23%] | 3.23% | ×1.25 | -0.71 | 0.657 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1 [share 30%, all records] | 2 | 420 | 5.48% [1.45%, 9.39%] | 3.23% | ×1.70 | +0.00 | 0.307 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1 [share 30%, its own devices] | 2 | 285 | 4.56% [3.52%, 5.59%] | 3.23% | ×1.41 | +0.00 | 0.630 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1 [share 30%, its own devices] | 2 | 285 | 6.32% [0.70%, 11.89%] | 3.23% | ×1.96 | +0.35 | 0.276 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1 [share 30%, other issuers' devices] | 2 | 136 | 2.94% [1.43%, 4.55%] | 3.23% | ×0.91 | -2.21 | 0.731 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1 [share 30%, other issuers' devices] | 2 | 135 | 3.70% [3.08%, 4.29%] | 3.23% | ×1.15 | -0.74 | 0.421 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1 [share 30%, all records] | 2 | 421 | 3.09% [2.40%, 3.76%] | 2.65% | ×1.17 | -1.43 | 0.617 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1 [share 30%, all records] | 2 | 421 | 4.99% [0.96%, 8.92%] | 2.63% | ×1.90 | -1.43 | 0.318 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1 [share 30%, its own devices] | 2 | 285 | 4.56% [3.52%, 5.59%] | 3.23% | ×1.41 | -0.70 | 0.630 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1 [share 30%, its own devices] | 2 | 285 | 6.32% [0.70%, 11.89%] | 3.23% | ×1.96 | -1.05 | 0.276 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1 [share 30%, other issuers' devices] | 2 | 136 | 0.00% [0.00%, 0.00%] | 1.42% | ×0.00 | -2.94 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1 [share 30%, other issuers' devices] | 2 | 136 | 2.21% [1.52%, 2.86%] | 1.38% | ×1.60 | -2.21 | 0.561 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1 [share 30%, all records] | 2 | 1,216 | 1.15% [0.66%, 1.63%] | 0.51% | ×2.28 | -1.89 | 0.652 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1 [share 30%, all records] | 2 | 1,216 | 1.15% [0.66%, 1.63%] | 0.51% | ×2.28 | -1.73 | 0.720 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1 [share 30%, its own devices] | 2 | 323 | 4.33% [2.70%, 5.71%] | 1.90% | ×2.28 | -0.62 | 0.656 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1 [share 30%, its own devices] | 2 | 323 | 4.33% [2.70%, 5.71%] | 1.90% | ×2.28 | -0.93 | 0.705 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1 [share 30%, other issuers' devices] | 2 | 893 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -2.35 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1 [share 30%, other issuers' devices] | 2 | 893 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -2.02 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1 [share 30%, all records] | 2 | 1,312 | 0.30% [0.15%, 0.47%] | 0.68% | ×0.45 | -6.86 | 0.605 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1 [share 30%, all records] | 2 | 1,312 | 0.00% [0.00%, 0.00%] | 0.68% | ×0.00 | -6.10 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1 [share 30%, its own devices] | 2 | 306 | 1.31% [0.65%, 1.99%] | 2.90% | ×0.45 | +0.65 | 0.620 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1 [share 30%, its own devices] | 2 | 306 | 0.00% [0.00%, 0.00%] | 2.90% | ×0.00 | +0.00 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1 [share 30%, other issuers' devices] | 2 | 1,006 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -9.15 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1 [share 30%, other issuers' devices] | 2 | 1,006 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.95 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1 [share 30%, all records] | 2 | 1,221 | 1.56% [0.00%, 3.07%] | 0.52% | ×3.02 | -5.08 | 0.351 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1 [share 30%, all records] | 2 | 1,221 | 1.64% [0.00%, 3.23%] | 0.52% | ×3.18 | -4.18 | 0.339 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1 [share 30%, its own devices] | 2 | 237 | 8.02% [0.00%, 14.18%] | 2.66% | ×3.02 | +2.11 | 0.376 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1 [share 30%, its own devices] | 2 | 237 | 8.44% [0.00%, 14.93%] | 2.66% | ×3.18 | +6.33 | 0.363 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1 [share 30%, other issuers' devices] | 2 | 984 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.81 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1 [share 30%, other issuers' devices] | 2 | 984 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.71 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1 [share 30%, all records] | 2 | 1,221 | 2.54% [1.83%, 3.23%] | 0.56% | ×4.50 | -7.04 | 0.621 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1 [share 30%, all records] | 2 | 1,221 | 2.62% [1.99%, 3.23%] | 0.56% | ×4.64 | -6.55 | 0.627 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1 [share 30%, its own devices] | 2 | 237 | 13.08% [10.68%, 14.93%] | 2.91% | ×4.50 | +6.75 | 0.604 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1 [share 30%, its own devices] | 2 | 237 | 13.50% [11.65%, 14.93%] | 2.91% | ×4.64 | +8.86 | 0.612 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1 [share 30%, other issuers' devices] | 2 | 984 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -10.37 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1 [share 30%, other issuers' devices] | 2 | 984 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -10.26 | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1 [share 30%, all records] | 2 | 1,224 | 0.74% [0.67%, 0.79%] | 0.48% | ×1.52 | -1.72 | 0.632 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1 [share 30%, all records] | 2 | 1,243 | 1.29% [1.00%, 1.56%] | 0.48% | ×2.67 | -1.85 | 0.497 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1 [share 30%, its own devices] | 2 | 202 | 4.46% [3.92%, 5.00%] | 1.97% | ×2.26 | +1.98 | 0.653 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1 [share 30%, its own devices] | 2 | 202 | 5.94% [4.90%, 7.00%] | 1.97% | ×3.01 | +3.47 | 0.497 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1 [share 30%, other issuers' devices] | 2 | 1,022 | 0.00% [0.00%, 0.00%] | 0.19% | ×0.00 | -2.45 | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1 [share 30%, other issuers' devices] | 2 | 1,041 | 0.38% [0.20%, 0.55%] | 0.19% | ×2.00 | -2.88 | 0.453 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1 [share 30%, all records] | 2 | 1,223 | 0.82% [0.79%, 0.84%] | 0.39% | ×2.12 | -1.55 | 0.605 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1 [share 30%, all records] | 2 | 1,246 | 1.12% [0.83%, 1.40%] | 0.40% | ×2.79 | -2.01 | 0.471 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1 [share 30%, its own devices] | 2 | 202 | 4.46% [3.92%, 5.00%] | 1.97% | ×2.26 | +1.98 | 0.653 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1 [share 30%, its own devices] | 2 | 202 | 5.94% [4.90%, 7.00%] | 1.97% | ×3.01 | -0.50 | 0.497 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1 [share 30%, other issuers' devices] | 2 | 1,021 | 0.10% [0.00%, 0.20%] | 0.07% | ×1.36 | -2.25 | 0.076 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1 [share 30%, other issuers' devices] | 2 | 1,044 | 0.19% [0.00%, 0.37%] | 0.10% | ×1.94 | -2.30 | 0.256 | no | not applicable |

## issuer_1_with_observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_1_with_observer [share 30%, all records] | 2 | 413 | 8.96% [6.86%, 11.00%] | 1.46% | ×6.13 | +2.91 | 0.634 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_1_with_observer [share 30%, all records] | 2 | 413 | 6.05% [2.45%, 9.57%] | 1.46% | ×4.14 | +3.39 | 0.686 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 413 | 8.96% [6.86%, 11.00%] | 1.46% | ×6.13 | +2.91 | 0.634 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 413 | 6.05% [2.45%, 9.57%] | 1.46% | ×4.14 | +3.39 | 0.686 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_observer [share 30%, all records] | 2 | 388 | 2.06% [1.65%, 2.43%] | 1.84% | ×1.12 | +1.29 | 0.498 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_1_with_observer [share 30%, all records] | 2 | 388 | 1.03% [0.00%, 1.94%] | 1.83% | ×0.56 | +0.52 | 0.145 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 388 | 2.06% [1.65%, 2.43%] | 1.84% | ×1.12 | +1.29 | 0.498 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 388 | 1.03% [0.00%, 1.94%] | 1.83% | ×0.56 | +0.52 | 0.145 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_1_with_observer [share 30%, all records] | 2 | 366 | 11.75% [7.22%, 16.13%] | 1.86% | ×6.30 | +3.83 | 0.513 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_observer [share 30%, all records] | 2 | 366 | 9.29% [9.14%, 9.44%] | 1.87% | ×4.97 | +3.55 | 0.569 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 366 | 11.75% [7.22%, 16.13%] | 1.86% | ×6.30 | +3.83 | 0.513 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 366 | 9.29% [9.14%, 9.44%] | 1.87% | ×4.97 | +3.55 | 0.569 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_1_with_observer [share 30%, all records] | 2 | 366 | 17.21% [13.33%, 20.97%] | 1.47% | ×11.74 | -3.28 | 0.673 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_observer [share 30%, all records] | 2 | 366 | 17.21% [16.11%, 18.28%] | 1.48% | ×11.66 | +1.09 | 0.799 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 366 | 17.21% [13.33%, 20.97%] | 1.47% | ×11.74 | -3.28 | 0.673 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 366 | 17.21% [16.11%, 18.28%] | 1.48% | ×11.66 | +1.09 | 0.799 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1_with_observer [share 30%, all records] | 2 | 421 | 6.41% [4.23%, 8.65%] | 1.48% | ×4.35 | +1.66 | 0.533 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1_with_observer [share 30%, all records] | 2 | 420 | 6.67% [5.63%, 7.73%] | 1.48% | ×4.51 | +1.19 | 0.542 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 285 | 7.02% [4.90%, 9.15%] | 1.48% | ×4.76 | +2.46 | 0.570 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 285 | 7.72% [6.99%, 8.45%] | 1.47% | ×5.25 | +1.75 | 0.560 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 136 | 5.15% [2.86%, 7.58%] | 1.47% | ×3.49 | +0.00 | 0.385 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 135 | 4.44% [2.86%, 6.15%] | 1.49% | ×2.97 | +0.00 | 0.566 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1_with_observer [share 30%, all records] | 2 | 421 | 4.75% [4.23%, 5.29%] | 1.27% | ×3.75 | +0.24 | 0.585 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1_with_observer [share 30%, all records] | 2 | 421 | 7.84% [6.57%, 9.13%] | 1.27% | ×6.17 | +1.43 | 0.481 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 285 | 5.96% [5.63%, 6.29%] | 1.27% | ×4.71 | +0.70 | 0.626 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 285 | 9.47% [8.39%, 10.56%] | 1.27% | ×7.46 | +2.11 | 0.424 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 136 | 2.21% [0.00%, 4.55%] | 1.27% | ×1.74 | -0.74 | 0.312 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 136 | 4.41% [2.86%, 6.06%] | 1.27% | ×3.47 | +0.00 | 0.755 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,216 | 3.12% [2.16%, 4.07%] | 0.74% | ×4.25 | +0.08 | 0.519 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,216 | 2.55% [2.44%, 2.66%] | 0.75% | ×3.40 | -0.33 | 0.575 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 323 | 5.88% [5.41%, 6.29%] | 0.74% | ×8.00 | +0.93 | 0.546 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 323 | 4.33% [3.43%, 5.41%] | 0.75% | ×5.80 | -0.93 | 0.652 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 893 | 2.13% [1.10%, 3.19%] | 0.74% | ×2.89 | -0.22 | 0.491 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 893 | 1.90% [1.76%, 2.05%] | 0.75% | ×2.54 | -0.11 | 0.516 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,312 | 7.16% [4.90%, 9.56%] | 0.94% | ×7.61 | +0.00 | 0.611 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,312 | 6.33% [4.75%, 7.99%] | 0.94% | ×6.76 | +0.23 | 0.620 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 306 | 2.29% [0.00%, 4.52%] | 0.94% | ×2.43 | +1.63 | 0.387 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 306 | 0.65% [0.00%, 1.29%] | 0.94% | ×0.70 | +0.65 | 0.197 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 1,006 | 8.65% [5.01%, 12.53%] | 0.94% | ×9.19 | -0.50 | 0.604 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 1,006 | 8.05% [5.78%, 10.47%] | 0.94% | ×8.61 | +0.10 | 0.631 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,221 | 6.22% [4.20%, 8.31%] | 0.96% | ×6.51 | -0.41 | 0.592 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,221 | 5.81% [3.23%, 8.47%] | 0.94% | ×6.19 | +0.00 | 0.577 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 237 | 5.91% [0.00%, 10.45%] | 0.95% | ×6.23 | +0.00 | 0.416 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 237 | 2.11% [0.00%, 3.73%] | 0.93% | ×2.26 | +0.00 | 0.516 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 984 | 6.30% [2.47%, 10.02%] | 0.96% | ×6.58 | -0.51 | 0.543 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 984 | 6.71% [3.09%, 10.22%] | 0.94% | ×7.13 | +0.00 | 0.550 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,221 | 9.25% [7.92%, 10.63%] | 0.83% | ×11.19 | -0.33 | 0.610 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,221 | 9.50% [7.75%, 11.30%] | 0.83% | ×11.43 | +0.33 | 0.584 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 237 | 8.44% [0.97%, 14.18%] | 0.83% | ×10.22 | +2.11 | 0.551 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 237 | 5.06% [0.00%, 8.96%] | 0.83% | ×6.11 | +0.42 | 0.503 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 984 | 9.45% [6.19%, 12.63%] | 0.83% | ×11.43 | -0.91 | 0.579 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 984 | 10.57% [7.42%, 13.63%] | 0.83% | ×12.71 | +0.30 | 0.475 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,224 | 1.72% [1.59%, 1.85%] | 0.75% | ×2.29 | -0.74 | 0.552 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,243 | 3.62% [3.00%, 4.21%] | 0.74% | ×4.88 | +0.48 | 0.585 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 202 | 4.95% [3.92%, 6.00%] | 0.75% | ×6.61 | +2.48 | 0.601 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 202 | 5.94% [2.94%, 9.00%] | 0.74% | ×8.02 | +3.47 | 0.608 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 1,022 | 1.08% [0.75%, 1.42%] | 0.75% | ×1.43 | -1.37 | 0.496 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 1,041 | 3.17% [3.01%, 3.32%] | 0.74% | ×4.27 | -0.10 | 0.577 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,223 | 2.29% [1.90%, 2.70%] | 0.64% | ×3.56 | -0.08 | 0.480 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1_with_observer [share 30%, all records] | 2 | 1,246 | 2.81% [2.65%, 2.96%] | 0.64% | ×4.36 | -0.32 | 0.489 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 202 | 5.45% [3.92%, 7.00%] | 0.64% | ×8.50 | +2.97 | 0.585 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1_with_observer [share 30%, its own devices] | 2 | 202 | 6.93% [6.00%, 7.84%] | 0.64% | ×10.76 | +0.50 | 0.599 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 1,021 | 1.67% [0.94%, 2.45%] | 0.64% | ×2.59 | -0.69 | 0.405 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1_with_observer [share 30%, other issuers' devices] | 2 | 1,044 | 2.01% [1.59%, 2.40%] | 0.64% | ×3.13 | -0.48 | 0.423 | no | not applicable |

## issuer_1_with_first_relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 413 | 8.96% [6.86%, 11.00%] | 1.46% | ×6.13 | +2.91 | 0.631 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 413 | 5.81% [2.94%, 8.61%] | 1.46% | ×3.97 | +3.15 | 0.517 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 413 | 8.96% [6.86%, 11.00%] | 1.46% | ×6.13 | +2.91 | 0.631 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 413 | 5.81% [2.94%, 8.61%] | 1.46% | ×3.97 | +3.15 | 0.517 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 388 | 2.06% [1.65%, 2.43%] | 1.84% | ×1.12 | +1.29 | 0.491 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 388 | 1.03% [0.00%, 1.94%] | 1.83% | ×0.56 | +0.52 | 0.125 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 388 | 2.06% [1.65%, 2.43%] | 1.84% | ×1.12 | +1.29 | 0.491 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 388 | 1.03% [0.00%, 1.94%] | 1.83% | ×0.56 | +0.52 | 0.125 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 366 | 12.02% [7.22%, 16.67%] | 1.86% | ×6.45 | +4.10 | 0.512 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 366 | 8.47% [8.06%, 8.89%] | 1.87% | ×4.53 | +2.73 | 0.592 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 366 | 12.02% [7.22%, 16.67%] | 1.86% | ×6.45 | +4.10 | 0.512 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 366 | 8.47% [8.06%, 8.89%] | 1.87% | ×4.53 | +2.73 | 0.592 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 366 | 16.67% [12.22%, 20.97%] | 1.47% | ×11.37 | -3.83 | 0.676 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 366 | 16.94% [15.56%, 18.28%] | 1.48% | ×11.48 | +0.82 | 0.790 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 366 | 16.67% [12.22%, 20.97%] | 1.47% | ×11.37 | -3.83 | 0.676 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 366 | 16.94% [15.56%, 18.28%] | 1.48% | ×11.48 | +0.82 | 0.790 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 421 | 5.94% [4.69%, 7.21%] | 1.48% | ×4.03 | +1.19 | 0.580 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 420 | 6.67% [5.16%, 8.21%] | 1.48% | ×4.51 | +1.19 | 0.554 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 285 | 6.32% [4.90%, 7.75%] | 1.48% | ×4.28 | +1.75 | 0.637 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 285 | 7.72% [6.29%, 9.15%] | 1.47% | ×5.25 | +1.75 | 0.580 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 136 | 5.15% [4.29%, 6.06%] | 1.47% | ×3.49 | +0.00 | 0.455 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 135 | 4.44% [2.86%, 6.15%] | 1.49% | ×2.97 | +0.00 | 0.578 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 421 | 5.46% [5.16%, 5.77%] | 1.27% | ×4.31 | +0.95 | 0.532 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 421 | 8.08% [6.57%, 9.62%] | 1.27% | ×6.36 | +1.66 | 0.483 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 285 | 6.67% [6.34%, 6.99%] | 1.27% | ×5.26 | +1.40 | 0.586 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 285 | 9.82% [8.39%, 11.27%] | 1.27% | ×7.74 | +2.46 | 0.416 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 136 | 2.94% [1.43%, 4.55%] | 1.27% | ×2.32 | +0.00 | 0.240 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 136 | 4.41% [2.86%, 6.06%] | 1.27% | ×3.47 | +0.00 | 0.756 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,216 | 3.29% [2.66%, 3.91%] | 0.74% | ×4.47 | +0.25 | 0.519 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,216 | 2.80% [2.44%, 3.16%] | 0.75% | ×3.73 | -0.08 | 0.505 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 323 | 5.57% [5.41%, 5.71%] | 0.74% | ×7.58 | +0.62 | 0.581 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 323 | 4.64% [3.43%, 6.08%] | 0.75% | ×6.22 | -0.62 | 0.636 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 893 | 2.46% [1.76%, 3.19%] | 0.74% | ×3.35 | +0.11 | 0.471 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 893 | 2.13% [2.05%, 2.20%] | 0.75% | ×2.84 | +0.11 | 0.409 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,312 | 7.47% [4.90%, 10.19%] | 0.94% | ×7.94 | +0.30 | 0.622 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,312 | 6.40% [4.75%, 8.15%] | 0.94% | ×6.84 | +0.30 | 0.620 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 306 | 2.29% [0.00%, 4.52%] | 0.94% | ×2.43 | +1.63 | 0.382 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 306 | 0.98% [0.66%, 1.29%] | 0.94% | ×1.04 | +0.98 | 0.328 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 1,006 | 9.05% [5.01%, 13.35%] | 0.94% | ×9.61 | -0.10 | 0.617 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 1,006 | 8.05% [5.78%, 10.47%] | 0.94% | ×8.61 | +0.10 | 0.636 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,221 | 6.14% [4.36%, 7.97%] | 0.96% | ×6.43 | -0.49 | 0.602 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,221 | 5.81% [3.23%, 8.47%] | 0.94% | ×6.19 | +0.00 | 0.578 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 237 | 5.91% [0.00%, 10.45%] | 0.95% | ×6.23 | +0.00 | 0.413 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 237 | 2.11% [0.00%, 3.73%] | 0.93% | ×2.26 | +0.00 | 0.518 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 984 | 6.20% [2.68%, 9.62%] | 0.96% | ×6.47 | -0.61 | 0.555 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 984 | 6.71% [3.09%, 10.22%] | 0.94% | ×7.13 | +0.00 | 0.550 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,221 | 8.93% [7.92%, 9.97%] | 0.83% | ×10.80 | -0.66 | 0.613 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,221 | 9.42% [7.59%, 11.30%] | 0.83% | ×11.33 | +0.25 | 0.578 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 237 | 8.44% [0.97%, 14.18%] | 0.83% | ×10.22 | +2.11 | 0.560 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 237 | 3.80% [0.00%, 6.72%] | 0.83% | ×4.58 | -0.84 | 0.594 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 984 | 9.04% [6.19%, 11.82%] | 0.83% | ×10.94 | -1.32 | 0.594 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 984 | 10.77% [7.84%, 13.63%] | 0.83% | ×12.96 | +0.51 | 0.471 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,224 | 1.88% [1.85%, 1.90%] | 0.75% | ×2.51 | -0.57 | 0.526 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,243 | 3.54% [2.83%, 4.21%] | 0.74% | ×4.77 | +0.40 | 0.571 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 202 | 5.94% [3.92%, 8.00%] | 0.75% | ×7.93 | +3.47 | 0.536 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 202 | 6.44% [3.92%, 9.00%] | 0.74% | ×8.69 | +3.96 | 0.588 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 1,022 | 1.08% [0.75%, 1.42%] | 0.75% | ×1.43 | -1.37 | 0.504 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 1,041 | 2.98% [2.61%, 3.32%] | 0.74% | ×4.01 | -0.29 | 0.562 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,223 | 2.29% [1.74%, 2.87%] | 0.64% | ×3.56 | -0.08 | 0.490 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1_with_first_relay [share 30%, all records] | 2 | 1,246 | 2.89% [2.81%, 2.96%] | 0.64% | ×4.49 | -0.24 | 0.502 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 202 | 4.95% [3.92%, 6.00%] | 0.64% | ×7.73 | +2.48 | 0.641 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1_with_first_relay [share 30%, its own devices] | 2 | 202 | 6.44% [5.00%, 7.84%] | 0.64% | ×9.99 | +0.00 | 0.633 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 1,021 | 1.76% [0.94%, 2.65%] | 0.64% | ×2.74 | -0.59 | 0.306 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 2 | 1,044 | 2.20% [1.79%, 2.58%] | 0.64% | ×3.42 | -0.29 | 0.434 | no | not applicable |

## issuer_1_with_destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_1_with_destination | 2 | 413 | 14.53% [11.76%, 17.22%] | 5.25% | ×2.77 | +8.47 | 0.525 | yes | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_1_with_destination | 2 | 413 | 15.74% [12.75%, 18.66%] | 5.29% | ×2.97 | +13.08 | 0.514 | yes | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_destination | 2 | 388 | 7.47% [6.31%, 8.79%] | 6.95% | ×1.08 | +6.70 | 0.545 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_1_with_destination | 2 | 388 | 7.47% [7.28%, 7.69%] | 6.90% | ×1.08 | +6.96 | 0.472 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_1_with_destination | 2 | 366 | 20.49% [19.35%, 21.67%] | 6.73% | ×3.05 | +12.57 | 0.639 | yes | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_destination | 2 | 366 | 19.13% [13.44%, 25.00%] | 6.83% | ×2.80 | +13.39 | 0.608 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_1_with_destination | 2 | 366 | 21.31% [17.78%, 24.73%] | 5.27% | ×4.04 | +0.82 | 0.610 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_1_with_destination | 2 | 366 | 21.86% [17.78%, 25.81%] | 5.32% | ×4.11 | +5.74 | 0.690 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_1_with_destination | 2 | 285 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.56 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_1_with_destination | 2 | 285 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.96 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_1_with_destination | 2 | 285 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.26 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_1_with_destination | 2 | 285 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.37 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_1_with_destination | 2 | 323 | 8.67% [6.86%, 10.81%] | 2.87% | ×3.02 | +3.72 | 0.631 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_1_with_destination | 2 | 323 | 8.67% [6.29%, 11.49%] | 2.92% | ×2.97 | +3.41 | 0.644 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_1_with_destination | 2 | 306 | 12.09% [8.61%, 15.48%] | 3.57% | ×3.39 | +11.44 | 0.545 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_1_with_destination | 2 | 306 | 8.82% [5.30%, 12.26%] | 3.53% | ×2.50 | +8.82 | 0.491 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_1_with_destination | 2 | 237 | 11.39% [4.85%, 16.42%] | 3.97% | ×2.87 | +5.49 | 0.634 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_destination | 2 | 237 | 12.24% [3.88%, 18.66%] | 3.80% | ×3.22 | +10.13 | 0.550 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_1_with_destination | 2 | 237 | 17.30% [10.68%, 22.39%] | 3.29% | ×5.26 | +10.97 | 0.600 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_1_with_destination | 2 | 237 | 13.50% [4.85%, 20.15%] | 3.30% | ×4.09 | +8.86 | 0.723 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_1_with_destination | 2 | 202 | 0.99% [0.00%, 1.96%] | 0.99% | ×1.00 | -1.49 | 0.897 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_1_with_destination | 2 | 202 | 0.50% [0.00%, 0.98%] | 0.50% | ×1.00 | -1.98 | 0.716 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_1_with_destination | 2 | 202 | 1.49% [1.00%, 1.96%] | 1.77% | ×0.84 | -0.99 | 0.260 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_1_with_destination | 2 | 202 | 1.98% [0.00%, 3.92%] | 1.27% | ×1.56 | -4.46 | 0.453 | no | not applicable |

## issuer_2

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_2 [share 20%, all records] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.05 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_2 [share 20%, all records] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -2.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_2 [share 20%, other issuers' devices] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.05 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_2 [share 20%, other issuers' devices] | 2 | 413 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -2.66 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_2 [share 20%, all records] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.77 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_2 [share 20%, all records] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.52 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_2 [share 20%, other issuers' devices] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.77 | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_2 [share 20%, other issuers' devices] | 2 | 388 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -0.52 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_2 [share 20%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.92 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2 [share 20%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.74 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_2 [share 20%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.92 | — | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2 [share 20%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.74 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_2 [share 20%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -20.49 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2 [share 20%, all records] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -16.12 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_2 [share 20%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -20.49 | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2 [share 20%, other issuers' devices] | 2 | 366 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -16.12 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_2 [share 20%, all records] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.75 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_2 [share 20%, all records] | 2 | 420 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.48 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_2 [share 20%, other issuers' devices] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.75 | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_2 [share 20%, other issuers' devices] | 2 | 420 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.48 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_2 [share 20%, all records] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.51 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_2 [share 20%, all records] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.41 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_2 [share 20%, other issuers' devices] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.51 | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_2 [share 20%, other issuers' devices] | 2 | 421 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.41 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2 [share 20%, all records] | 2 | 1,216 | 0.90% [0.66%, 1.14%] | 0.50% | ×1.83 | -2.14 | 0.563 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2 [share 20%, all records] | 2 | 1,216 | 0.82% [0.49%, 1.16%] | 0.50% | ×1.66 | -2.06 | 0.558 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2 [share 20%, its own devices] | 2 | 230 | 4.78% [3.70%, 5.74%] | 2.62% | ×1.83 | +3.04 | 0.530 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2 [share 20%, its own devices] | 2 | 230 | 4.35% [2.46%, 6.48%] | 2.62% | ×1.66 | +3.91 | 0.544 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2 [share 20%, other issuers' devices] | 2 | 986 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -3.35 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2 [share 20%, other issuers' devices] | 2 | 986 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -3.45 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2 [share 20%, all records] | 2 | 1,312 | 5.72% [5.02%, 6.38%] | 0.96% | ×5.98 | -1.45 | 0.502 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2 [share 20%, all records] | 2 | 1,312 | 5.72% [5.02%, 6.38%] | 0.96% | ×5.98 | -0.38 | 0.446 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2 [share 20%, its own devices] | 2 | 317 | 23.66% [19.28%, 28.48%] | 3.95% | ×5.98 | +16.72 | 0.479 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2 [share 20%, its own devices] | 2 | 317 | 23.66% [19.28%, 28.48%] | 3.95% | ×5.98 | +15.14 | 0.426 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2 [share 20%, other issuers' devices] | 2 | 995 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.24 | — | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2 [share 20%, other issuers' devices] | 2 | 995 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -5.33 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2 [share 20%, all records] | 2 | 1,221 | 3.85% [1.83%, 5.82%] | 1.05% | ×3.68 | -2.78 | 0.622 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2 [share 20%, all records] | 2 | 1,221 | 3.77% [1.66%, 5.82%] | 1.05% | ×3.60 | -2.05 | 0.628 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2 [share 20%, its own devices] | 2 | 280 | 16.79% [7.48%, 27.07%] | 4.56% | ×3.68 | +12.86 | 0.674 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2 [share 20%, its own devices] | 2 | 280 | 16.43% [6.80%, 27.07%] | 4.56% | ×3.60 | +13.93 | 0.675 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2 [share 20%, other issuers' devices] | 2 | 941 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -7.44 | — | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2 [share 20%, other issuers' devices] | 2 | 941 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -6.80 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2 [share 20%, all records] | 2 | 1,221 | 4.59% [3.32%, 5.82%] | 0.80% | ×5.71 | -5.00 | 0.569 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2 [share 20%, all records] | 2 | 1,221 | 4.75% [3.65%, 5.82%] | 0.80% | ×5.91 | -4.42 | 0.555 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2 [share 20%, its own devices] | 2 | 280 | 20.00% [13.61%, 27.07%] | 3.50% | ×5.71 | +13.21 | 0.626 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2 [share 20%, its own devices] | 2 | 280 | 20.71% [14.97%, 27.07%] | 3.50% | ×5.91 | +12.86 | 0.596 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2 [share 20%, other issuers' devices] | 2 | 941 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -10.41 | — | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2 [share 20%, other issuers' devices] | 2 | 941 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -9.56 | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2 [share 20%, all records] | 2 | 1,224 | 1.06% [1.01%, 1.11%] | 0.50% | ×2.11 | -1.39 | 0.747 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2 [share 20%, all records] | 2 | 1,243 | 1.13% [0.78%, 1.50%] | 0.48% | ×2.33 | -2.01 | 0.516 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2 [share 20%, its own devices] | 2 | 168 | 6.55% [4.17%, 9.72%] | 2.32% | ×2.82 | +6.55 | 0.817 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2 [share 20%, its own devices] | 2 | 168 | 5.95% [5.21%, 6.94%] | 2.32% | ×2.57 | +1.19 | 0.582 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2 [share 20%, other issuers' devices] | 2 | 1,056 | 0.19% [0.00%, 0.40%] | 0.22% | ×0.88 | -2.65 | 0.279 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2 [share 20%, other issuers' devices] | 2 | 1,075 | 0.37% [0.00%, 0.79%] | 0.20% | ×1.90 | -2.51 | 0.292 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2 [share 20%, all records] | 2 | 1,223 | 1.06% [0.84%, 1.27%] | 0.40% | ×2.64 | -1.31 | 0.766 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2 [share 20%, all records] | 2 | 1,246 | 0.88% [0.83%, 0.93%] | 0.37% | ×2.37 | -2.25 | 0.538 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2 [share 20%, its own devices] | 2 | 168 | 6.55% [4.17%, 9.72%] | 2.32% | ×2.82 | +5.95 | 0.817 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2 [share 20%, its own devices] | 2 | 168 | 5.95% [5.21%, 6.94%] | 2.32% | ×2.57 | +1.79 | 0.582 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2 [share 20%, other issuers' devices] | 2 | 1,055 | 0.19% [0.18%, 0.20%] | 0.10% | ×1.95 | -2.46 | 0.715 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2 [share 20%, other issuers' devices] | 2 | 1,078 | 0.09% [0.00%, 0.18%] | 0.07% | ×1.33 | -2.88 | 0.258 | no | not applicable |

## issuer_2_with_observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_2_with_observer [share 20%, all records] | 2 | 413 | 5.08% [3.43%, 6.70%] | 1.46% | ×3.48 | -0.97 | 0.513 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_2_with_observer [share 20%, all records] | 2 | 413 | 2.91% [1.47%, 4.31%] | 1.46% | ×1.99 | +0.24 | 0.352 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 413 | 5.08% [3.43%, 6.70%] | 1.46% | ×3.48 | -0.97 | 0.513 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 413 | 2.91% [1.47%, 4.31%] | 1.46% | ×1.99 | +0.24 | 0.352 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_observer [share 20%, all records] | 2 | 388 | 0.77% [0.55%, 0.97%] | 1.84% | ×0.42 | +0.00 | 0.204 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_2_with_observer [share 20%, all records] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.133 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 388 | 0.77% [0.55%, 0.97%] | 1.84% | ×0.42 | +0.00 | 0.204 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.133 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_2_with_observer [share 20%, all records] | 2 | 366 | 6.01% [2.78%, 9.14%] | 1.86% | ×3.22 | -1.91 | 0.533 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_observer [share 20%, all records] | 2 | 366 | 5.46% [4.30%, 6.67%] | 1.87% | ×2.92 | -0.27 | 0.357 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 366 | 6.01% [2.78%, 9.14%] | 1.86% | ×3.22 | -1.91 | 0.533 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 366 | 5.46% [4.30%, 6.67%] | 1.87% | ×2.92 | -0.27 | 0.357 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_2_with_observer [share 20%, all records] | 2 | 366 | 18.03% [14.44%, 21.51%] | 1.47% | ×12.30 | -2.46 | 0.601 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_observer [share 20%, all records] | 2 | 366 | 15.57% [15.00%, 16.13%] | 1.48% | ×10.55 | -0.55 | 0.643 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 366 | 18.03% [14.44%, 21.51%] | 1.47% | ×12.30 | -2.46 | 0.601 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 366 | 15.57% [15.00%, 16.13%] | 1.48% | ×10.55 | -0.55 | 0.643 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_2_with_observer [share 20%, all records] | 2 | 421 | 3.09% [0.47%, 5.77%] | 1.48% | ×2.09 | -1.66 | 0.411 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_2_with_observer [share 20%, all records] | 2 | 420 | 4.76% [2.82%, 6.76%] | 1.48% | ×3.22 | -0.71 | 0.432 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 421 | 3.09% [0.47%, 5.77%] | 1.48% | ×2.09 | -1.66 | 0.411 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 420 | 4.76% [2.82%, 6.76%] | 1.48% | ×3.22 | -0.71 | 0.432 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_2_with_observer [share 20%, all records] | 2 | 421 | 3.80% [2.35%, 5.29%] | 1.27% | ×3.00 | -0.71 | 0.317 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_2_with_observer [share 20%, all records] | 2 | 421 | 5.23% [3.29%, 7.21%] | 1.27% | ×4.11 | -1.19 | 0.374 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 421 | 3.80% [2.35%, 5.29%] | 1.27% | ×3.00 | -0.71 | 0.317 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 421 | 5.23% [3.29%, 7.21%] | 1.27% | ×4.11 | -1.19 | 0.374 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,216 | 2.96% [1.99%, 3.91%] | 0.74% | ×4.02 | -0.08 | 0.479 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,216 | 2.63% [2.49%, 2.77%] | 0.75% | ×3.51 | -0.25 | 0.557 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 230 | 3.48% [2.78%, 4.10%] | 0.73% | ×4.74 | +1.74 | 0.468 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 230 | 1.30% [0.82%, 1.85%] | 0.75% | ×1.74 | +0.87 | 0.403 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 986 | 2.84% [1.82%, 3.86%] | 0.74% | ×3.86 | -0.51 | 0.461 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 986 | 2.94% [2.63%, 3.25%] | 0.75% | ×3.93 | -0.51 | 0.575 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,312 | 6.71% [3.56%, 10.03%] | 0.94% | ×7.13 | -0.46 | 0.611 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,312 | 6.25% [4.60%, 7.99%] | 0.94% | ×6.68 | +0.15 | 0.628 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 317 | 6.62% [3.61%, 9.93%] | 0.94% | ×7.05 | -0.32 | 0.466 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 317 | 8.83% [1.20%, 17.22%] | 0.94% | ×9.39 | +0.32 | 0.315 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 995 | 6.73% [1.72%, 12.29%] | 0.94% | ×7.15 | -0.50 | 0.656 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 995 | 5.43% [0.96%, 10.38%] | 0.93% | ×5.81 | +0.10 | 0.714 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,221 | 6.47% [4.85%, 8.14%] | 0.96% | ×6.77 | -0.16 | 0.556 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,221 | 5.90% [3.23%, 8.64%] | 0.94% | ×6.28 | +0.08 | 0.577 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 280 | 5.36% [3.40%, 7.52%] | 0.96% | ×5.59 | +1.43 | 0.333 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 280 | 3.21% [2.26%, 4.08%] | 0.95% | ×3.40 | +0.71 | 0.258 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 941 | 6.80% [4.12%, 9.67%] | 0.95% | ×7.12 | -0.64 | 0.608 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 941 | 6.70% [3.50%, 10.11%] | 0.94% | ×7.14 | -0.11 | 0.621 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,221 | 9.25% [7.59%, 10.96%] | 0.83% | ×11.19 | -0.33 | 0.611 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,221 | 8.60% [5.98%, 11.30%] | 0.83% | ×10.35 | -0.57 | 0.630 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 280 | 6.07% [3.40%, 9.02%] | 0.83% | ×7.32 | -0.71 | 0.430 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 280 | 7.86% [4.76%, 11.28%] | 0.83% | ×9.43 | +0.00 | 0.360 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 941 | 10.20% [7.20%, 13.41%] | 0.83% | ×12.36 | -0.21 | 0.630 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 941 | 8.82% [4.53%, 13.41%] | 0.83% | ×10.62 | -0.74 | 0.684 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,224 | 3.02% [3.02%, 3.03%] | 0.75% | ×4.03 | +0.57 | 0.590 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,243 | 2.90% [2.83%, 2.96%] | 0.74% | ×3.90 | -0.24 | 0.649 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 168 | 7.74% [5.21%, 11.11%] | 0.75% | ×10.26 | +7.74 | 0.815 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 168 | 4.76% [4.17%, 5.21%] | 0.75% | ×6.38 | +0.00 | 0.561 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 1,056 | 2.27% [1.97%, 2.61%] | 0.75% | ×3.03 | -0.57 | 0.471 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 1,075 | 2.60% [2.38%, 2.81%] | 0.74% | ×3.51 | -0.28 | 0.638 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,223 | 2.94% [2.87%, 3.01%] | 0.64% | ×4.58 | +0.57 | 0.582 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2_with_observer [share 20%, all records] | 2 | 1,246 | 2.73% [2.34%, 3.15%] | 0.64% | ×4.24 | -0.40 | 0.517 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 168 | 7.74% [5.21%, 11.11%] | 0.65% | ×11.94 | +7.14 | 0.846 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2_with_observer [share 20%, its own devices] | 2 | 168 | 4.17% [4.17%, 4.17%] | 0.65% | ×6.46 | +0.00 | 0.541 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 1,055 | 2.18% [1.97%, 2.42%] | 0.64% | ×3.39 | -0.47 | 0.439 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2_with_observer [share 20%, other issuers' devices] | 2 | 1,078 | 2.50% [2.11%, 2.95%] | 0.64% | ×3.89 | -0.46 | 0.491 | no | not applicable |

## issuer_2_with_first_relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 413 | 5.57% [3.43%, 7.66%] | 1.46% | ×3.81 | -0.48 | 0.487 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 413 | 2.91% [1.47%, 4.31%] | 1.46% | ×1.99 | +0.24 | 0.411 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 413 | 5.57% [3.43%, 7.66%] | 1.46% | ×3.81 | -0.48 | 0.487 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 413 | 2.91% [1.47%, 4.31%] | 1.46% | ×1.99 | +0.24 | 0.411 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 388 | 0.77% [0.55%, 0.97%] | 1.84% | ×0.42 | +0.00 | 0.209 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.076 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 388 | 0.77% [0.55%, 0.97%] | 1.84% | ×0.42 | +0.00 | 0.209 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | +0.00 | 0.076 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 366 | 6.56% [3.33%, 9.68%] | 1.86% | ×3.52 | -1.37 | 0.489 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 366 | 4.92% [3.76%, 6.11%] | 1.87% | ×2.63 | -0.82 | 0.422 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 366 | 6.56% [3.33%, 9.68%] | 1.86% | ×3.52 | -1.37 | 0.489 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 366 | 4.92% [3.76%, 6.11%] | 1.87% | ×2.63 | -0.82 | 0.422 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 366 | 18.03% [14.44%, 21.51%] | 1.47% | ×12.30 | -2.46 | 0.606 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 366 | 15.30% [13.89%, 16.67%] | 1.48% | ×10.37 | -0.82 | 0.626 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 366 | 18.03% [14.44%, 21.51%] | 1.47% | ×12.30 | -2.46 | 0.606 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 366 | 15.30% [13.89%, 16.67%] | 1.48% | ×10.37 | -0.82 | 0.626 | yes | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 421 | 3.09% [0.94%, 5.29%] | 1.48% | ×2.09 | -1.66 | 0.361 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 420 | 4.76% [2.82%, 6.76%] | 1.48% | ×3.22 | -0.71 | 0.469 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 421 | 3.09% [0.94%, 5.29%] | 1.48% | ×2.09 | -1.66 | 0.361 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 420 | 4.76% [2.82%, 6.76%] | 1.48% | ×3.22 | -0.71 | 0.469 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 421 | 4.04% [2.35%, 5.77%] | 1.27% | ×3.19 | -0.48 | 0.286 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 421 | 5.23% [3.76%, 6.73%] | 1.27% | ×4.11 | -1.19 | 0.347 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 421 | 4.04% [2.35%, 5.77%] | 1.27% | ×3.19 | -0.48 | 0.286 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 421 | 5.23% [3.76%, 6.73%] | 1.27% | ×4.11 | -1.19 | 0.347 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,216 | 3.37% [2.66%, 4.07%] | 0.74% | ×4.58 | +0.33 | 0.458 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,216 | 2.71% [2.61%, 2.82%] | 0.75% | ×3.62 | -0.16 | 0.541 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 230 | 3.91% [3.70%, 4.10%] | 0.73% | ×5.33 | +2.17 | 0.498 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 230 | 1.74% [1.64%, 1.85%] | 0.75% | ×2.32 | +1.30 | 0.379 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 986 | 3.25% [2.43%, 4.07%] | 0.74% | ×4.41 | -0.10 | 0.440 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 986 | 2.94% [2.85%, 3.04%] | 0.75% | ×3.93 | -0.51 | 0.565 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,312 | 6.94% [3.41%, 10.66%] | 0.94% | ×7.37 | -0.23 | 0.625 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,312 | 6.33% [4.75%, 7.99%] | 0.94% | ×6.76 | +0.23 | 0.626 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 317 | 6.94% [4.22%, 9.93%] | 0.94% | ×7.38 | +0.00 | 0.445 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 317 | 9.15% [1.20%, 17.88%] | 0.94% | ×9.73 | +0.63 | 0.306 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 995 | 6.93% [1.53%, 12.92%] | 0.94% | ×7.37 | -0.30 | 0.682 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 995 | 5.43% [0.96%, 10.38%] | 0.93% | ×5.81 | +0.10 | 0.717 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,221 | 6.31% [4.85%, 7.81%] | 0.96% | ×6.60 | -0.33 | 0.563 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,221 | 5.98% [3.39%, 8.64%] | 0.94% | ×6.36 | +0.16 | 0.571 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 280 | 5.36% [3.40%, 7.52%] | 0.96% | ×5.59 | +1.43 | 0.340 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 280 | 3.21% [2.26%, 4.08%] | 0.95% | ×3.40 | +0.71 | 0.263 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 941 | 6.59% [4.12%, 9.23%] | 0.95% | ×6.90 | -0.85 | 0.617 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 941 | 6.80% [3.70%, 10.11%] | 0.94% | ×7.25 | +0.00 | 0.613 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,221 | 9.09% [7.59%, 10.63%] | 0.83% | ×11.00 | -0.49 | 0.619 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,221 | 8.85% [6.62%, 11.13%] | 0.83% | ×10.64 | -0.33 | 0.611 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 280 | 6.43% [3.40%, 9.77%] | 0.83% | ×7.75 | -0.36 | 0.412 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 280 | 7.86% [4.76%, 11.28%] | 0.83% | ×9.43 | +0.00 | 0.373 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 941 | 9.88% [7.00%, 12.97%] | 0.83% | ×11.97 | -0.53 | 0.647 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 941 | 9.14% [5.35%, 13.19%] | 0.83% | ×11.00 | -0.43 | 0.655 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,224 | 2.94% [2.86%, 3.02%] | 0.75% | ×3.92 | +0.49 | 0.581 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,243 | 3.14% [3.12%, 3.16%] | 0.74% | ×4.23 | +0.00 | 0.617 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 168 | 7.14% [4.17%, 11.11%] | 0.75% | ×9.47 | +7.14 | 0.808 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 168 | 5.95% [4.17%, 7.29%] | 0.75% | ×7.98 | +1.19 | 0.477 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 1,056 | 2.27% [1.97%, 2.61%] | 0.75% | ×3.03 | -0.57 | 0.466 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 1,075 | 2.70% [2.38%, 2.98%] | 0.74% | ×3.64 | -0.19 | 0.619 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,223 | 2.70% [2.54%, 2.87%] | 0.64% | ×4.19 | +0.33 | 0.621 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2_with_first_relay [share 20%, all records] | 2 | 1,246 | 2.73% [2.65%, 2.81%] | 0.64% | ×4.24 | -0.40 | 0.529 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 168 | 7.14% [4.17%, 11.11%] | 0.65% | ×11.02 | +6.55 | 0.846 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2_with_first_relay [share 20%, its own devices] | 2 | 168 | 4.17% [4.17%, 4.17%] | 0.65% | ×6.46 | +0.00 | 0.530 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 1,055 | 1.99% [1.43%, 2.62%] | 0.64% | ×3.10 | -0.66 | 0.497 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 2 | 1,078 | 2.50% [2.46%, 2.56%] | 0.64% | ×3.89 | -0.46 | 0.508 | no | not applicable |

## issuer_0_with_destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_0_with_destination | 2 | 663 | 5.43% [4.05%, 6.94%] | 1.64% | ×3.31 | +2.87 | 0.524 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_0_with_destination | 2 | 663 | 6.79% [6.07%, 7.57%] | 1.65% | ×4.12 | +4.22 | 0.499 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_0_with_destination | 2 | 689 | 12.34% [6.25%, 19.31%] | 2.16% | ×5.72 | +2.18 | 0.543 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_0_with_destination | 2 | 689 | 10.45% [6.52%, 14.95%] | 2.15% | ×4.86 | +2.76 | 0.557 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_0_with_destination | 2 | 704 | 9.94% [5.68%, 14.20%] | 2.11% | ×4.71 | +1.99 | 0.484 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_destination | 2 | 704 | 12.64% [7.10%, 18.18%] | 2.09% | ×6.06 | +4.26 | 0.464 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_0_with_destination | 2 | 704 | 12.36% [9.38%, 15.34%] | 1.83% | ×6.76 | +0.57 | 0.609 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_0_with_destination | 2 | 704 | 14.06% [9.94%, 18.18%] | 1.84% | ×7.65 | +2.84 | 0.630 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_0_with_destination | 2 | 466 | 2.36% [2.29%, 2.45%] | 1.75% | ×1.35 | -1.07 | 0.586 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_0_with_destination | 2 | 466 | 2.15% [1.53%, 2.94%] | 2.11% | ×1.02 | -0.64 | 0.746 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_0_with_destination | 2 | 466 | 4.51% [4.20%, 4.90%] | 2.28% | ×1.97 | +0.21 | 0.594 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_0_with_destination | 2 | 466 | 6.01% [4.96%, 7.35%] | 2.65% | ×2.27 | +3.00 | 0.616 | no | not applicable |

## issuer_2_with_destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | issuer_2_with_destination | 2 | 230 | 8.70% [8.20%, 9.26%] | 3.76% | ×2.31 | +6.96 | 0.446 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | issuer_2_with_destination | 2 | 230 | 8.70% [8.20%, 9.26%] | 3.91% | ×2.22 | +8.26 | 0.578 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | issuer_2_with_destination | 2 | 317 | 17.35% [10.24%, 25.17%] | 4.48% | ×3.87 | +10.41 | 0.613 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | issuer_2_with_destination | 2 | 317 | 24.29% [19.88%, 29.14%] | 4.46% | ×5.45 | +15.77 | 0.616 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | issuer_2_with_destination | 2 | 280 | 14.64% [8.16%, 21.80%] | 4.75% | ×3.08 | +10.71 | 0.496 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_destination | 2 | 280 | 16.43% [11.56%, 21.80%] | 4.67% | ×3.52 | +13.93 | 0.525 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | issuer_2_with_destination | 2 | 280 | 23.93% [23.81%, 24.06%] | 4.13% | ×5.79 | +17.14 | 0.578 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | issuer_2_with_destination | 2 | 280 | 18.21% [16.33%, 20.30%] | 4.11% | ×4.43 | +10.36 | 0.705 | yes | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | issuer_2_with_destination | 2 | 168 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | +0.00 | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | issuer_2_with_destination | 2 | 168 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | -4.76 | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | issuer_2_with_destination | 2 | 168 | 11.31% [11.11%, 11.46%] | 6.56% | ×1.72 | +10.71 | 0.495 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | issuer_2_with_destination | 2 | 168 | 9.52% [6.94%, 11.46%] | 4.35% | ×2.19 | +5.36 | 0.500 | no | not applicable |

## ceiling

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | ceiling | 2 | 413 | 13.56% [12.92%, 14.22%] | 9.57% | ×1.42 | — | — | yes | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | ceiling | 2 | 413 | 10.90% [8.61%, 13.24%] | 9.63% | ×1.13 | — | — | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | ceiling | 2 | 413 | 12.83% [11.96%, 13.73%] | 9.36% | ×1.37 | — | — | yes | 10.50% |
| R1 | W1 | credential path | 1186 s | ceiling | 2 | 388 | 11.34% [9.89%, 12.62%] | 9.66% | ×1.17 | — | — | no | 10.50% |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | ceiling | 2 | 388 | 11.08% [10.44%, 11.65%] | 9.83% | ×1.13 | — | — | no | 10.50% |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | ceiling | 2 | 388 | 13.14% [12.64%, 13.59%] | 9.86% | ×1.33 | — | — | yes | 10.50% |
| R1 | W2 | credential path | 1195 s | ceiling | 2 | 366 | 12.02% [11.29%, 12.78%] | 9.81% | ×1.22 | — | — | no | 10.50% |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | ceiling | 2 | 366 | 12.84% [11.83%, 13.89%] | 9.68% | ×1.33 | — | — | no | 10.50% |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | ceiling | 2 | 366 | 12.84% [12.37%, 13.33%] | 9.62% | ×1.34 | — | — | no | 10.50% |
| R1 | Wmis | credential path | 1195 s | ceiling | 2 | 366 | 11.75% [11.29%, 12.22%] | 9.26% | ×1.27 | — | — | no | 10.50% |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | ceiling | 2 | 366 | 13.11% [12.90%, 13.33%] | 9.36% | ×1.40 | — | — | no | 10.50% |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | ceiling | 2 | 366 | 12.02% [10.22%, 13.89%] | 9.43% | ×1.28 | — | — | no | 10.50% |
| R1 | chain100 | credential path | 1213 s | ceiling | 2 | 420 | 8.33% [7.51%, 9.18%] | 9.51% | ×0.88 | — | — | no | 10.50% |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | ceiling | 2 | 421 | 10.69% [9.13%, 12.21%] | 9.59% | ×1.11 | — | — | no | 10.50% |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | ceiling | 2 | 420 | 11.19% [9.66%, 12.68%] | 9.42% | ×1.19 | — | — | no | 10.50% |
| R1 | chain50 | credential path | 1208 s | ceiling | 2 | 421 | 9.03% [7.51%, 10.58%] | 9.50% | ×0.95 | — | — | no | 10.50% |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | ceiling | 2 | 421 | 11.16% [10.80%, 11.54%] | 9.83% | ×1.14 | — | — | no | 10.50% |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | ceiling | 2 | 421 | 9.74% [9.13%, 10.33%] | 9.55% | ×1.02 | — | — | no | 10.50% |
| R100 | W0 | credential path | 1208 s | ceiling | 2 | 1,216 | 6.25% [5.98%, 6.51%] | 4.89% | ×1.28 | — | — | yes | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | ceiling | 2 | 1,216 | 6.50% [5.05%, 7.97%] | 4.89% | ×1.33 | — | — | yes | 5.33% |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | ceiling | 2 | 1,216 | 5.59% [5.37%, 5.81%] | 4.96% | ×1.13 | — | — | yes | 5.33% |
| R100 | W1 | credential path | 1197 s | ceiling | 2 | 1,312 | 5.41% [5.34%, 5.49%] | 4.74% | ×1.14 | — | — | yes | 5.33% |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | ceiling | 2 | 1,312 | 6.17% [4.45%, 7.99%] | 4.75% | ×1.30 | — | — | yes | 5.33% |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | ceiling | 2 | 1,312 | 7.24% [6.68%, 7.84%] | 4.77% | ×1.52 | — | — | yes | 5.33% |
| R100 | W2 | credential path | 1210 s | ceiling | 2 | 1,221 | 5.90% [4.04%, 7.81%] | 4.94% | ×1.19 | — | — | yes | 5.33% |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | ceiling | 2 | 1,221 | 6.63% [6.48%, 6.79%] | 4.91% | ×1.35 | — | — | yes | 5.33% |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | ceiling | 2 | 1,221 | 6.14% [6.14%, 6.15%] | 4.91% | ×1.25 | — | — | yes | 5.33% |
| R100 | Wmis | credential path | 1210 s | ceiling | 2 | 1,221 | 5.98% [4.68%, 7.31%] | 4.91% | ×1.22 | — | — | yes | 5.33% |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | ceiling | 2 | 1,221 | 6.06% [5.32%, 6.79%] | 4.90% | ×1.24 | — | — | yes | 5.33% |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | ceiling | 2 | 1,221 | 6.06% [5.65%, 6.48%] | 4.92% | ×1.23 | — | — | yes | 5.33% |
| R100 | chain100 | credential path | 1189 s | ceiling | 2 | 1,234 | 5.02% [4.88%, 5.18%] | 4.90% | ×1.03 | — | — | yes | 5.33% |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | ceiling | 2 | 1,224 | 4.66% [4.29%, 5.05%] | 4.89% | ×0.95 | — | — | yes | 5.33% |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | ceiling | 2 | 1,243 | 6.68% [6.66%, 6.70%] | 4.91% | ×1.36 | — | — | yes | 5.33% |
| R100 | chain50 | credential path | 1201 s | ceiling | 2 | 1,242 | 5.64% [5.30%, 6.00%] | 4.88% | ×1.15 | — | — | yes | 5.33% |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | ceiling | 2 | 1,223 | 4.74% [4.73%, 4.75%] | 4.92% | ×0.96 | — | — | yes | 5.33% |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | ceiling | 2 | 1,246 | 5.06% [4.80%, 5.30%] | 4.93% | ×1.03 | — | — | yes | 5.33% |

## K records, K = 1

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | K records, K = 1 | 2 | 413 | 6.78% [5.39%, 8.13%] | 1.11% | ×6.13 | — | 0.440 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | K records, K = 1 | 2 | 413 | 6.05% [4.41%, 7.66%] | 1.46% | ×4.14 | — | 0.671 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | K records, K = 1 | 2 | 413 | 2.66% [1.47%, 3.83%] | 1.46% | ×1.82 | — | 0.643 | no | not applicable |
| R1 | W1 | credential path | 1186 s | K records, K = 1 | 2 | 388 | 0.00% [0.00%, 0.00%] | 1.37% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | K records, K = 1 | 2 | 388 | 0.77% [0.00%, 1.46%] | 1.84% | ×0.42 | — | 0.035 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | K records, K = 1 | 2 | 388 | 0.52% [0.00%, 0.97%] | 1.83% | ×0.28 | — | 0.140 | no | not applicable |
| R1 | W2 | credential path | 1195 s | K records, K = 1 | 2 | 366 | 8.20% [4.44%, 11.83%] | 1.40% | ×5.86 | — | 0.347 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | K records, K = 1 | 2 | 366 | 7.92% [6.67%, 9.14%] | 1.86% | ×4.25 | — | 0.511 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 1 | 2 | 366 | 5.74% [4.84%, 6.67%] | 1.87% | ×3.07 | — | 0.366 | no | not applicable |
| R1 | Wmis | credential path | 1195 s | K records, K = 1 | 2 | 366 | 20.77% [15.56%, 25.81%] | 1.11% | ×18.70 | — | 0.879 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | K records, K = 1 | 2 | 366 | 20.49% [17.22%, 23.66%] | 1.47% | ×13.98 | — | 0.714 | yes | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 1 | 2 | 366 | 16.12% [15.00%, 17.20%] | 1.48% | ×10.92 | — | 0.682 | yes | not applicable |
| R1 | chain100 | credential path | 1213 s | K records, K = 1 | 2 | 420 | 7.14% [5.16%, 9.18%] | 1.12% | ×6.36 | — | 0.478 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | K records, K = 1 | 2 | 421 | 4.75% [1.41%, 8.17%] | 1.48% | ×3.22 | — | 0.489 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | K records, K = 1 | 2 | 420 | 5.48% [3.29%, 7.73%] | 1.48% | ×3.71 | — | 0.519 | no | not applicable |
| R1 | chain50 | credential path | 1208 s | K records, K = 1 | 2 | 421 | 4.51% [2.35%, 6.73%] | 0.88% | ×5.11 | — | 0.419 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | K records, K = 1 | 2 | 421 | 4.51% [3.29%, 5.77%] | 1.27% | ×3.56 | — | 0.499 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | K records, K = 1 | 2 | 421 | 6.41% [3.29%, 9.62%] | 1.27% | ×5.05 | — | 0.465 | no | not applicable |
| R100 | W0 | credential path | 1208 s | K records, K = 1 | 2 | 1,216 | 1.73% [1.16%, 2.28%] | 0.55% | ×3.12 | — | 0.426 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | K records, K = 1 | 2 | 1,216 | 3.04% [2.33%, 3.75%] | 0.74% | ×4.13 | — | 0.498 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | K records, K = 1 | 2 | 1,216 | 2.88% [2.33%, 3.42%] | 0.75% | ×3.84 | — | 0.542 | no | not applicable |
| R100 | W1 | credential path | 1197 s | K records, K = 1 | 2 | 1,312 | 6.94% [3.56%, 10.50%] | 0.70% | ×9.94 | — | 0.635 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | K records, K = 1 | 2 | 1,312 | 7.16% [4.01%, 10.50%] | 0.94% | ×7.61 | — | 0.614 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | K records, K = 1 | 2 | 1,312 | 6.10% [4.45%, 7.84%] | 0.94% | ×6.51 | — | 0.640 | yes | not applicable |
| R100 | W2 | credential path | 1210 s | K records, K = 1 | 2 | 1,221 | 7.13% [5.33%, 8.97%] | 0.70% | ×10.13 | — | 0.554 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | K records, K = 1 | 2 | 1,221 | 6.63% [4.68%, 8.64%] | 0.96% | ×6.94 | — | 0.590 | yes | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 1 | 2 | 1,221 | 5.81% [3.23%, 8.47%] | 0.94% | ×6.19 | — | 0.586 | yes | not applicable |
| R100 | Wmis | credential path | 1210 s | K records, K = 1 | 2 | 1,221 | 9.83% [9.05%, 10.63%] | 0.62% | ×15.94 | — | 0.597 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | K records, K = 1 | 2 | 1,221 | 9.58% [7.75%, 11.46%] | 0.83% | ×11.59 | — | 0.613 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 1 | 2 | 1,221 | 9.17% [7.11%, 11.30%] | 0.83% | ×11.04 | — | 0.605 | yes | not applicable |
| R100 | chain100 | credential path | 1189 s | K records, K = 1 | 2 | 1,234 | 1.78% [1.73%, 1.84%] | 0.56% | ×3.18 | — | 0.534 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | K records, K = 1 | 2 | 1,224 | 2.45% [2.38%, 2.53%] | 0.75% | ×3.27 | — | 0.608 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | K records, K = 1 | 2 | 1,243 | 3.14% [3.12%, 3.16%] | 0.74% | ×4.23 | — | 0.644 | no | not applicable |
| R100 | chain50 | credential path | 1201 s | K records, K = 1 | 2 | 1,242 | 2.17% [2.17%, 2.18%] | 0.44% | ×4.94 | — | 0.506 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | K records, K = 1 | 2 | 1,223 | 2.37% [2.06%, 2.70%] | 0.64% | ×3.69 | — | 0.562 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | K records, K = 1 | 2 | 1,246 | 3.13% [2.65%, 3.64%] | 0.64% | ×4.86 | — | 0.527 | no | not applicable |

## K records, K = 2

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | K records, K = 2 | 2 | 206 | 5.34% [2.94%, 7.69%] | 1.18% | ×4.53 | — | 0.449 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | K records, K = 2 | 2 | 206 | 8.25% [4.90%, 11.54%] | 1.91% | ×4.31 | — | 0.617 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | K records, K = 2 | 2 | 206 | 9.22% [6.86%, 11.54%] | 1.88% | ×4.90 | — | 0.520 | no | not applicable |
| R1 | W1 | credential path | 1186 s | K records, K = 2 | 2 | 194 | 0.00% [0.00%, 0.00%] | 1.53% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | K records, K = 2 | 2 | 194 | 1.03% [0.00%, 1.94%] | 2.41% | ×0.43 | — | 0.185 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | K records, K = 2 | 2 | 194 | 1.03% [0.00%, 1.94%] | 2.39% | ×0.43 | — | 0.174 | no | not applicable |
| R1 | W2 | credential path | 1195 s | K records, K = 2 | 2 | 183 | 8.20% [4.44%, 11.83%] | 1.55% | ×5.28 | — | 0.362 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | K records, K = 2 | 2 | 183 | 8.74% [7.78%, 9.68%] | 2.41% | ×3.63 | — | 0.460 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 2 | 2 | 183 | 5.46% [4.30%, 6.67%] | 2.40% | ×2.28 | — | 0.341 | no | not applicable |
| R1 | Wmis | credential path | 1195 s | K records, K = 2 | 2 | 183 | 21.86% [17.78%, 25.81%] | 1.18% | ×18.57 | — | 0.859 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | K records, K = 2 | 2 | 183 | 21.31% [18.89%, 23.66%] | 1.87% | ×11.41 | — | 0.792 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 2 | 2 | 183 | 19.13% [17.78%, 20.43%] | 1.88% | ×10.18 | — | 0.711 | no | not applicable |
| R1 | chain100 | credential path | 1213 s | K records, K = 2 | 2 | 209 | 6.70% [3.77%, 9.71%] | 1.19% | ×5.61 | — | 0.527 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | K records, K = 2 | 2 | 210 | 9.05% [6.60%, 11.54%] | 1.89% | ×4.80 | — | 0.475 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | K records, K = 2 | 2 | 209 | 7.66% [5.66%, 9.71%] | 1.89% | ×4.06 | — | 0.510 | no | not applicable |
| R1 | chain50 | credential path | 1208 s | K records, K = 2 | 2 | 209 | 4.31% [2.83%, 5.83%] | 1.06% | ×4.07 | — | 0.606 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | K records, K = 2 | 2 | 209 | 7.66% [4.72%, 10.68%] | 2.04% | ×3.75 | — | 0.605 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | K records, K = 2 | 2 | 210 | 10.48% [5.66%, 15.38%] | 2.01% | ×5.22 | — | 0.522 | no | not applicable |
| R100 | W0 | credential path | 1208 s | K records, K = 2 | 2 | 559 | 2.68% [2.55%, 2.81%] | 0.59% | ×4.55 | — | 0.537 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | K records, K = 2 | 2 | 559 | 3.40% [2.19%, 4.56%] | 0.94% | ×3.61 | — | 0.576 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | K records, K = 2 | 2 | 559 | 3.76% [3.51%, 4.01%] | 1.00% | ×3.77 | — | 0.642 | no | not applicable |
| R100 | W1 | credential path | 1197 s | K records, K = 2 | 2 | 605 | 7.44% [3.82%, 11.34%] | 0.76% | ×9.82 | — | 0.563 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | K records, K = 2 | 2 | 605 | 8.43% [4.78%, 12.37%] | 1.16% | ×7.25 | — | 0.489 | yes | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | K records, K = 2 | 2 | 605 | 6.78% [4.46%, 9.28%] | 1.15% | ×5.88 | — | 0.581 | no | not applicable |
| R100 | W2 | credential path | 1210 s | K records, K = 2 | 2 | 559 | 7.51% [5.96%, 9.12%] | 0.76% | ×9.83 | — | 0.539 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | K records, K = 2 | 2 | 559 | 7.16% [5.61%, 8.76%] | 1.19% | ×5.99 | — | 0.547 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 2 | 2 | 559 | 6.44% [3.51%, 9.49%] | 1.16% | ×5.53 | — | 0.533 | no | not applicable |
| R100 | Wmis | credential path | 1210 s | K records, K = 2 | 2 | 559 | 10.38% [9.47%, 11.31%] | 0.66% | ×15.79 | — | 0.576 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | K records, K = 2 | 2 | 559 | 10.02% [8.07%, 12.04%] | 1.02% | ×9.80 | — | 0.583 | yes | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 2 | 2 | 559 | 11.27% [10.18%, 12.41%] | 1.03% | ×10.92 | — | 0.466 | yes | not applicable |
| R100 | chain100 | credential path | 1189 s | K records, K = 2 | 2 | 564 | 3.19% [2.93%, 3.44%] | 0.60% | ×5.32 | — | 0.529 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | K records, K = 2 | 2 | 556 | 4.32% [3.82%, 4.85%] | 0.96% | ×4.48 | — | 0.605 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | K records, K = 2 | 2 | 573 | 4.19% [3.94%, 4.42%] | 0.97% | ×4.33 | — | 0.618 | no | not applicable |
| R100 | chain50 | credential path | 1201 s | K records, K = 2 | 2 | 520 | 3.27% [2.97%, 3.59%] | 0.52% | ×6.23 | — | 0.564 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | K records, K = 2 | 2 | 522 | 2.87% [2.60%, 3.16%] | 1.02% | ×2.81 | — | 0.447 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | K records, K = 2 | 2 | 535 | 5.98% [5.79%, 6.16%] | 1.04% | ×5.76 | — | 0.472 | no | not applicable |

## K records, K = 3

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | K records, K = 3 | 2 | 137 | 8.76% [7.35%, 10.14%] | 1.25% | ×7.00 | — | 0.499 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | K records, K = 3 | 2 | 137 | 13.87% [8.82%, 18.84%] | 2.45% | ×5.67 | — | 0.622 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | K records, K = 3 | 2 | 137 | 11.68% [8.82%, 14.49%] | 2.54% | ×4.60 | — | 0.538 | no | not applicable |
| R1 | W1 | credential path | 1186 s | K records, K = 3 | 2 | 128 | 0.00% [0.00%, 0.00%] | 1.70% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | K records, K = 3 | 2 | 128 | 1.56% [1.47%, 1.67%] | 3.07% | ×0.51 | — | 0.381 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | K records, K = 3 | 2 | 128 | 1.56% [0.00%, 2.94%] | 3.03% | ×0.52 | — | 0.079 | no | not applicable |
| R1 | W2 | credential path | 1195 s | K records, K = 3 | 2 | 122 | 8.20% [5.00%, 11.29%] | 1.71% | ×4.79 | — | 0.421 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | K records, K = 3 | 2 | 122 | 9.02% [6.67%, 11.29%] | 3.01% | ×2.99 | — | 0.487 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 3 | 2 | 122 | 3.28% [1.61%, 5.00%] | 3.00% | ×1.09 | — | 0.534 | no | not applicable |
| R1 | Wmis | credential path | 1195 s | K records, K = 3 | 2 | 122 | 24.59% [16.67%, 32.26%] | 1.25% | ×19.67 | — | 0.937 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | K records, K = 3 | 2 | 122 | 28.69% [25.00%, 32.26%] | 2.41% | ×11.88 | — | 0.749 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 3 | 2 | 122 | 22.95% [22.58%, 23.33%] | 2.46% | ×9.32 | — | 0.705 | no | not applicable |
| R1 | chain100 | credential path | 1213 s | K records, K = 3 | 2 | 140 | 10.00% [5.63%, 14.49%] | 1.27% | ×7.89 | — | 0.499 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | K records, K = 3 | 2 | 140 | 10.00% [9.86%, 10.14%] | 2.40% | ×4.17 | — | 0.687 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | K records, K = 3 | 2 | 140 | 9.29% [8.70%, 9.86%] | 2.39% | ×3.88 | — | 0.402 | no | not applicable |
| R1 | chain50 | credential path | 1208 s | K records, K = 3 | 2 | 139 | 6.47% [4.29%, 8.70%] | 1.25% | ×5.17 | — | 0.505 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | K records, K = 3 | 2 | 138 | 13.04% [10.00%, 16.18%] | 3.13% | ×4.17 | — | 0.444 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | K records, K = 3 | 2 | 138 | 17.39% [14.29%, 20.59%] | 3.20% | ×5.44 | — | 0.597 | no | not applicable |
| R100 | W0 | credential path | 1208 s | K records, K = 3 | 2 | 335 | 2.99% [2.38%, 3.59%] | 0.63% | ×4.74 | — | 0.514 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | K records, K = 3 | 2 | 335 | 8.06% [7.78%, 8.33%] | 1.22% | ×6.60 | — | 0.443 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | K records, K = 3 | 2 | 335 | 8.66% [6.55%, 10.78%] | 1.31% | ×6.61 | — | 0.446 | no | not applicable |
| R100 | W1 | credential path | 1197 s | K records, K = 3 | 2 | 382 | 7.07% [3.08%, 11.23%] | 0.82% | ×8.66 | — | 0.571 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | K records, K = 3 | 2 | 382 | 8.12% [4.10%, 12.30%] | 1.38% | ×5.87 | — | 0.518 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | K records, K = 3 | 2 | 382 | 7.33% [5.64%, 9.09%] | 1.39% | ×5.29 | — | 0.544 | no | not applicable |
| R100 | W2 | credential path | 1210 s | K records, K = 3 | 2 | 340 | 8.82% [6.43%, 11.24%] | 0.82% | ×10.74 | — | 0.549 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | K records, K = 3 | 2 | 340 | 7.06% [4.68%, 9.47%] | 1.43% | ×4.95 | — | 0.641 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 3 | 2 | 340 | 7.94% [4.68%, 11.24%] | 1.40% | ×5.65 | — | 0.492 | no | not applicable |
| R100 | Wmis | credential path | 1210 s | K records, K = 3 | 2 | 340 | 11.76% [11.11%, 12.43%] | 0.69% | ×16.93 | — | 0.550 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | K records, K = 3 | 2 | 340 | 10.88% [8.19%, 13.61%] | 1.22% | ×8.91 | — | 0.547 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 3 | 2 | 340 | 12.65% [11.70%, 13.61%] | 1.27% | ×10.00 | — | 0.456 | no | not applicable |
| R100 | chain100 | credential path | 1189 s | K records, K = 3 | 2 | 337 | 2.97% [2.47%, 3.43%] | 0.64% | ×4.62 | — | 0.585 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | K records, K = 3 | 2 | 340 | 6.47% [5.08%, 7.98%] | 1.21% | ×5.33 | — | 0.571 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | K records, K = 3 | 2 | 345 | 6.67% [6.63%, 6.70%] | 1.24% | ×5.40 | — | 0.467 | no | not applicable |
| R100 | chain50 | credential path | 1201 s | K records, K = 3 | 2 | 298 | 4.70% [4.32%, 5.03%] | 0.61% | ×7.74 | — | 0.554 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | K records, K = 3 | 2 | 290 | 8.28% [6.62%, 10.07%] | 1.48% | ×5.61 | — | 0.464 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | K records, K = 3 | 2 | 295 | 7.80% [7.69%, 7.89%] | 1.52% | ×5.11 | — | 0.462 | no | not applicable |

## K records, K = 5

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | K records, K = 5 | 2 | 81 | 9.88% [5.00%, 14.63%] | 1.42% | ×6.94 | — | 0.507 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | K records, K = 5 | 2 | 81 | 25.93% [15.00%, 36.59%] | 4.02% | ×6.45 | — | 0.611 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | K records, K = 5 | 2 | 81 | 23.46% [15.00%, 31.71%] | 4.35% | ×5.40 | — | 0.595 | no | not applicable |
| R1 | W1 | credential path | 1186 s | K records, K = 5 | 2 | 77 | 0.00% [0.00%, 0.00%] | 2.05% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | K records, K = 5 | 2 | 77 | 1.30% [0.00%, 2.78%] | 4.36% | ×0.30 | — | 0.513 | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | K records, K = 5 | 2 | 77 | 1.30% [0.00%, 2.44%] | 4.27% | ×0.30 | — | 0.197 | no | not applicable |
| R1 | W2 | credential path | 1195 s | K records, K = 5 | 2 | 73 | 6.85% [2.78%, 10.81%] | 2.05% | ×3.34 | — | 0.435 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | K records, K = 5 | 2 | 73 | 8.22% [8.11%, 8.33%] | 4.17% | ×1.97 | — | 0.669 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 5 | 2 | 73 | 5.48% [5.41%, 5.56%] | 4.25% | ×1.29 | — | 0.438 | no | not applicable |
| R1 | Wmis | credential path | 1195 s | K records, K = 5 | 2 | 73 | 24.66% [16.67%, 32.43%] | 1.42% | ×17.32 | — | 0.905 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | K records, K = 5 | 2 | 73 | 38.36% [37.84%, 38.89%] | 4.21% | ×9.11 | — | 0.763 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 5 | 2 | 73 | 36.99% [30.56%, 43.24%] | 4.28% | ×8.64 | — | 0.759 | no | not applicable |
| R1 | chain100 | credential path | 1213 s | K records, K = 5 | 2 | 83 | 18.07% [9.52%, 26.83%] | 1.44% | ×12.53 | — | 0.525 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | K records, K = 5 | 2 | 83 | 24.10% [19.05%, 29.27%] | 3.99% | ×6.03 | — | 0.583 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | K records, K = 5 | 2 | 83 | 21.69% [21.43%, 21.95%] | 4.03% | ×5.38 | — | 0.588 | no | not applicable |
| R1 | chain50 | credential path | 1208 s | K records, K = 5 | 2 | 83 | 16.87% [11.90%, 21.95%] | 1.69% | ×9.99 | — | 0.477 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | K records, K = 5 | 2 | 83 | 20.48% [19.05%, 21.95%] | 6.82% | ×3.00 | — | 0.604 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | K records, K = 5 | 2 | 83 | 32.53% [31.71%, 33.33%] | 6.87% | ×4.73 | — | 0.577 | no | not applicable |
| R100 | W0 | credential path | 1208 s | K records, K = 5 | 2 | 155 | 3.87% [2.41%, 5.56%] | 0.71% | ×5.44 | — | 0.550 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | 517 s | K records, K = 5 | 2 | 155 | 18.71% [13.89%, 22.89%] | 1.99% | ×9.41 | — | 0.577 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, lengthened hold | 1203 s | K records, K = 5 | 2 | 155 | 31.61% [28.92%, 34.72%] | 2.29% | ×13.82 | — | 0.586 | no | not applicable |
| R100 | W1 | credential path | 1197 s | K records, K = 5 | 2 | 185 | 8.65% [4.21%, 13.33%] | 0.92% | ×9.38 | — | 0.552 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | K records, K = 5 | 2 | 185 | 9.19% [4.21%, 14.44%] | 1.81% | ×5.07 | — | 0.620 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | K records, K = 5 | 2 | 185 | 8.65% [6.32%, 11.11%] | 1.79% | ×4.83 | — | 0.627 | no | not applicable |
| R100 | W2 | credential path | 1210 s | K records, K = 5 | 2 | 175 | 9.71% [6.98%, 12.36%] | 0.93% | ×10.47 | — | 0.555 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | K records, K = 5 | 2 | 175 | 10.29% [8.14%, 12.36%] | 1.94% | ×5.31 | — | 0.558 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 5 | 2 | 175 | 9.14% [4.65%, 13.48%] | 1.87% | ×4.90 | — | 0.520 | no | not applicable |
| R100 | Wmis | credential path | 1210 s | K records, K = 5 | 2 | 175 | 12.57% [11.63%, 13.48%] | 0.76% | ×16.45 | — | 0.549 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, natural | 521 s | K records, K = 5 | 2 | 175 | 12.57% [11.63%, 13.48%] | 1.71% | ×7.35 | — | 0.583 | no | not applicable |
| R100 | Wmis | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 5 | 2 | 175 | 12.00% [9.30%, 14.61%] | 1.77% | ×6.78 | — | 0.564 | no | not applicable |
| R100 | chain100 | credential path | 1189 s | K records, K = 5 | 2 | 166 | 6.63% [5.56%, 7.89%] | 0.73% | ×9.12 | — | 0.682 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | K records, K = 5 | 2 | 162 | 15.43% [12.50%, 18.92%] | 1.91% | ×8.09 | — | 0.584 | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | K records, K = 5 | 2 | 162 | 15.43% [14.61%, 16.44%] | 1.92% | ×8.05 | — | 0.578 | no | not applicable |
| R100 | chain50 | credential path | 1201 s | K records, K = 5 | 2 | 121 | 13.22% [11.11%, 15.52%] | 0.77% | ×17.22 | — | 0.541 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | K records, K = 5 | 2 | 120 | 24.17% [18.18%, 31.48%] | 2.87% | ×8.42 | — | 0.497 | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | K records, K = 5 | 2 | 120 | 31.67% [26.47%, 38.46%] | 3.05% | ×10.39 | — | 0.570 | no | not applicable |

## K records, K = 10

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | K records, K = 10 | 2 | 40 | 52.50% [50.00%, 55.00%] | 2.00% | ×26.23 | — | 0.702 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | K records, K = 10 | 2 | 40 | 85.00% [85.00%, 85.00%] | 14.67% | ×5.79 | — | 0.833 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | K records, K = 10 | 2 | 40 | 67.50% [60.00%, 75.00%] | 16.87% | ×4.00 | — | 0.652 | no | not applicable |
| R1 | W1 | credential path | 1186 s | K records, K = 10 | 2 | 38 | 0.00% [0.00%, 0.00%] | 2.76% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | K records, K = 10 | 2 | 38 | 0.00% [0.00%, 0.00%] | 7.37% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | K records, K = 10 | 2 | 38 | 0.00% [0.00%, 0.00%] | 6.82% | ×0.00 | — | — | no | not applicable |
| R1 | W2 | credential path | 1195 s | K records, K = 10 | 2 | 36 | 5.56% [0.00%, 11.11%] | 2.75% | ×2.02 | — | 0.485 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | K records, K = 10 | 2 | 36 | 8.33% [0.00%, 16.67%] | 7.11% | ×1.17 | — | 0.545 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 10 | 2 | 36 | 11.11% [11.11%, 11.11%] | 7.27% | ×1.53 | — | 0.297 | no | not applicable |
| R1 | Wmis | credential path | 1195 s | K records, K = 10 | 2 | 36 | 61.11% [61.11%, 61.11%] | 1.98% | ×30.91 | — | 0.870 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | K records, K = 10 | 2 | 36 | 80.56% [77.78%, 83.33%] | 15.90% | ×5.07 | — | 0.773 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 10 | 2 | 36 | 83.33% [77.78%, 88.89%] | 16.59% | ×5.02 | — | 0.744 | no | not applicable |
| R1 | chain100 | credential path | 1213 s | K records, K = 10 | 2 | 41 | 41.46% [23.81%, 60.00%] | 1.94% | ×21.34 | — | 0.564 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | K records, K = 10 | 2 | 41 | 63.41% [55.00%, 71.43%] | 13.80% | ×4.59 | — | 0.677 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | K records, K = 10 | 2 | 41 | 70.73% [70.00%, 71.43%] | 12.30% | ×5.75 | — | 0.526 | no | not applicable |
| R1 | chain50 | credential path | 1208 s | K records, K = 10 | 2 | 40 | 70.00% [55.00%, 85.00%] | 3.03% | ×23.09 | — | 0.622 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | K records, K = 10 | 2 | 41 | 92.68% [90.48%, 95.00%] | 35.55% | ×2.61 | — | 0.895 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | K records, K = 10 | 2 | 41 | 92.68% [90.48%, 95.00%] | 40.83% | ×2.27 | — | 0.737 | no | not applicable |
| R100 | W1 | credential path | 1197 s | K records, K = 10 | 2 | 56 | 12.50% [3.57%, 21.43%] | 1.10% | ×11.34 | — | 0.653 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | K records, K = 10 | 2 | 56 | 16.07% [7.14%, 25.00%] | 2.56% | ×6.28 | — | 0.563 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | K records, K = 10 | 2 | 56 | 14.29% [14.29%, 14.29%] | 2.50% | ×5.72 | — | 0.656 | no | not applicable |
| R100 | W2 | credential path | 1210 s | K records, K = 10 | 2 | 57 | 17.54% [13.79%, 21.43%] | 1.11% | ×15.81 | — | 0.460 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | K records, K = 10 | 2 | 57 | 17.54% [10.34%, 25.00%] | 3.13% | ×5.61 | — | 0.521 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 10 | 2 | 57 | 19.30% [13.79%, 25.00%] | 2.88% | ×6.69 | — | 0.514 | no | not applicable |

## K records, K = 20

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | credential path | 1206 s | K records, K = 20 | 2 | 20 | 90.00% [80.00%, 100.00%] | 3.86% | ×23.32 | — | 0.944 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | 508 s | K records, K = 20 | 2 | 20 | 100.00% [100.00%, 100.00%] | 67.50% | ×1.48 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, lengthened hold | 1264 s | K records, K = 20 | 2 | 20 | 100.00% [100.00%, 100.00%] | 73.75% | ×1.36 | — | — | no | not applicable |
| R1 | W1 | credential path | 1186 s | K records, K = 20 | 2 | 19 | 0.00% [0.00%, 0.00%] | 3.93% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, natural | 525 s | K records, K = 20 | 2 | 19 | 0.00% [0.00%, 0.00%] | 12.27% | ×0.00 | — | — | no | not applicable |
| R1 | W1 | blind-issued one-time certificates, lengthened hold | 1184 s | K records, K = 20 | 2 | 19 | 0.00% [0.00%, 0.00%] | 10.95% | ×0.00 | — | — | no | not applicable |
| R1 | W2 | credential path | 1195 s | K records, K = 20 | 2 | 18 | 5.56% [0.00%, 11.11%] | 3.78% | ×1.47 | — | 0.176 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, natural | 532 s | K records, K = 20 | 2 | 18 | 11.11% [11.11%, 11.11%] | 11.87% | ×0.94 | — | 0.281 | no | not applicable |
| R1 | W2 | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 20 | 2 | 18 | 5.56% [0.00%, 11.11%] | 12.59% | ×0.44 | — | 0.059 | no | not applicable |
| R1 | Wmis | credential path | 1195 s | K records, K = 20 | 2 | 18 | 94.44% [88.89%, 100.00%] | 3.94% | ×23.95 | — | 0.765 | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, natural | 532 s | K records, K = 20 | 2 | 18 | 100.00% [100.00%, 100.00%] | 56.64% | ×1.77 | — | — | no | not applicable |
| R1 | Wmis | blind-issued one-time certificates, lengthened hold | 1232 s | K records, K = 20 | 2 | 18 | 100.00% [100.00%, 100.00%] | 66.82% | ×1.50 | — | — | no | not applicable |
| R1 | chain100 | credential path | 1213 s | K records, K = 20 | 2 | 20 | 85.00% [80.00%, 90.00%] | 3.49% | ×24.36 | — | 0.588 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | K records, K = 20 | 2 | 20 | 90.00% [90.00%, 90.00%] | 61.00% | ×1.48 | — | 1.000 | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | K records, K = 20 | 2 | 20 | 95.00% [90.00%, 100.00%] | 69.75% | ×1.36 | — | 0.947 | no | not applicable |
| R1 | chain50 | credential path | 1208 s | K records, K = 20 | 2 | 18 | 94.44% [88.89%, 100.00%] | 6.89% | ×13.70 | — | 0.824 | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | K records, K = 20 | 2 | 19 | 100.00% [100.00%, 100.00%] | 93.86% | ×1.07 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | K records, K = 20 | 2 | 19 | 100.00% [100.00%, 100.00%] | 93.86% | ×1.07 | — | — | no | not applicable |
| R100 | W1 | credential path | 1197 s | K records, K = 20 | 2 | 14 | 28.57% [16.67%, 37.50%] | 1.32% | ×21.59 | — | 0.475 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, natural | 531 s | K records, K = 20 | 2 | 14 | 28.57% [16.67%, 37.50%] | 3.73% | ×7.67 | — | 0.575 | no | not applicable |
| R100 | W1 | blind-issued one-time certificates, lengthened hold | 1234 s | K records, K = 20 | 2 | 14 | 35.71% [33.33%, 37.50%] | 3.57% | ×9.99 | — | 0.556 | no | not applicable |
| R100 | W2 | credential path | 1210 s | K records, K = 20 | 2 | 11 | 36.36% [14.29%, 75.00%] | 1.32% | ×27.55 | — | 0.536 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, natural | 521 s | K records, K = 20 | 2 | 11 | 27.27% [0.00%, 75.00%] | 4.69% | ×5.81 | — | 0.750 | no | not applicable |
| R100 | W2 | blind-issued one-time certificates, lengthened hold | 1227 s | K records, K = 20 | 2 | 11 | 18.18% [0.00%, 50.00%] | 4.17% | ×4.36 | — | 0.778 | no | not applicable |

## edit chain, 1 records

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | chain100 | credential path | 1213 s | edit chain, 1 records | 2 | 191 | 6.28% [6.00%, 6.59%] | 1.12% | ×5.59 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | edit chain, 1 records | 2 | 191 | 3.14% [0.00%, 6.59%] | 1.47% | ×2.14 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | edit chain, 1 records | 2 | 191 | 5.24% [4.00%, 6.59%] | 1.46% | ×3.58 | — | — | no | not applicable |
| R1 | chain50 | credential path | 1208 s | edit chain, 1 records | 2 | 191 | 3.66% [3.00%, 4.40%] | 0.88% | ×4.17 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | edit chain, 1 records | 2 | 191 | 4.19% [3.30%, 5.00%] | 1.26% | ×3.32 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | edit chain, 1 records | 2 | 191 | 6.28% [6.00%, 6.59%] | 1.26% | ×4.97 | — | — | no | not applicable |
| R100 | chain100 | credential path | 1189 s | edit chain, 1 records | 2 | 824 | 1.21% [0.94%, 1.50%] | 0.56% | ×2.16 | — | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | edit chain, 1 records | 2 | 772 | 2.33% [1.97%, 2.73%] | 0.75% | ×3.11 | — | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | edit chain, 1 records | 2 | 808 | 2.72% [2.65%, 2.80%] | 0.74% | ×3.67 | — | — | no | not applicable |
| R100 | chain50 | credential path | 1201 s | edit chain, 1 records | 2 | 821 | 1.95% [1.41%, 2.54%] | 0.43% | ×4.48 | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | edit chain, 1 records | 2 | 765 | 2.48% [2.26%, 2.72%] | 0.63% | ×3.96 | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | edit chain, 1 records | 2 | 811 | 3.58% [3.10%, 4.09%] | 0.62% | ×5.81 | — | — | no | not applicable |

## edit chain, 2 records

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | chain100 | credential path | 1213 s | edit chain, 2 records | 2 | 62 | 14.52% [4.17%, 21.05%] | 1.29% | ×11.25 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | edit chain, 2 records | 2 | 61 | 13.11% [0.00%, 21.62%] | 2.25% | ×5.83 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | edit chain, 2 records | 2 | 62 | 6.45% [0.00%, 10.53%] | 2.22% | ×2.91 | — | — | no | not applicable |
| R1 | chain50 | credential path | 1208 s | edit chain, 2 records | 2 | 61 | 11.48% [0.00%, 18.92%] | 1.10% | ×10.44 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | edit chain, 2 records | 2 | 61 | 14.75% [4.17%, 21.62%] | 1.84% | ×8.02 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | edit chain, 2 records | 2 | 61 | 11.48% [0.00%, 18.92%] | 2.06% | ×5.57 | — | — | no | not applicable |
| R100 | chain100 | credential path | 1189 s | edit chain, 2 records | 2 | 162 | 4.94% [3.80%, 6.02%] | 0.67% | ×7.34 | — | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | edit chain, 2 records | 2 | 157 | 8.92% [8.64%, 9.21%] | 1.19% | ×7.47 | — | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | edit chain, 2 records | 2 | 159 | 8.18% [7.06%, 9.46%] | 1.13% | ×7.23 | — | — | no | not applicable |
| R100 | chain50 | credential path | 1201 s | edit chain, 2 records | 2 | 157 | 4.46% [1.32%, 7.41%] | 0.58% | ×7.66 | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | edit chain, 2 records | 2 | 160 | 5.00% [4.00%, 5.88%] | 0.96% | ×5.19 | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | edit chain, 2 records | 2 | 160 | 3.12% [2.35%, 4.00%] | 0.94% | ×3.33 | — | — | no | not applicable |

## edit chain, 3 records

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | chain100 | credential path | 1213 s | edit chain, 3 records | 2 | 31 | 25.81% [15.79%, 41.67%] | 1.49% | ×17.27 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | edit chain, 3 records | 2 | 32 | 28.12% [26.32%, 30.77%] | 3.36% | ×8.36 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | edit chain, 3 records | 2 | 31 | 22.58% [21.05%, 25.00%] | 3.22% | ×7.00 | — | — | no | not applicable |
| R1 | chain50 | credential path | 1208 s | edit chain, 3 records | 2 | 32 | 18.75% [10.53%, 30.77%] | 1.42% | ×13.21 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | edit chain, 3 records | 2 | 32 | 9.38% [0.00%, 23.08%] | 3.28% | ×2.86 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | edit chain, 3 records | 2 | 32 | 18.75% [15.38%, 21.05%] | 2.70% | ×6.95 | — | — | no | not applicable |
| R100 | chain100 | credential path | 1189 s | edit chain, 3 records | 2 | 26 | 7.69% [7.14%, 8.33%] | 0.82% | ×9.40 | — | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | edit chain, 3 records | 2 | 42 | 11.90% [11.11%, 12.50%] | 1.85% | ×6.43 | — | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, lengthened hold | 1230 s | edit chain, 3 records | 2 | 39 | 5.13% [0.00%, 10.53%] | 1.74% | ×2.95 | — | — | no | not applicable |
| R100 | chain50 | credential path | 1201 s | edit chain, 3 records | 2 | 33 | 6.06% [0.00%, 11.11%] | 0.72% | ×8.40 | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | edit chain, 3 records | 2 | 42 | 7.14% [5.88%, 8.00%] | 1.10% | ×6.50 | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | edit chain, 3 records | 2 | 37 | 5.41% [4.76%, 6.25%] | 0.85% | ×6.37 | — | — | no | not applicable |

## edit chain, 4 records

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | chain100 | credential path | 1213 s | edit chain, 4 records | 2 | 3 | 0.00% [0.00%, 0.00%] | 1.57% | ×0.00 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, natural | 516 s | edit chain, 4 records | 2 | 3 | 66.67% [50.00%, 100.00%] | 4.48% | ×14.89 | — | — | no | not applicable |
| R1 | chain100 | blind-issued one-time certificates, lengthened hold | 1266 s | edit chain, 4 records | 2 | 3 | 33.33% [0.00%, 50.00%] | 3.72% | ×8.97 | — | — | no | not applicable |
| R1 | chain50 | credential path | 1208 s | edit chain, 4 records | 2 | 3 | 33.33% [0.00%, 100.00%] | 1.81% | ×18.42 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, natural | 522 s | edit chain, 4 records | 2 | 3 | 33.33% [0.00%, 100.00%] | 4.88% | ×6.83 | — | — | no | not applicable |
| R1 | chain50 | blind-issued one-time certificates, lengthened hold | 1282 s | edit chain, 4 records | 2 | 3 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | — | — | no | not applicable |
| R100 | chain100 | credential path | 1189 s | edit chain, 4 records | 2 | 2 | 0.00% [0.00%, 0.00%] | 1.10% | ×0.00 | — | — | no | not applicable |
| R100 | chain100 | blind-issued one-time certificates, natural | 520 s | edit chain, 4 records | 2 | 3 | 0.00% [0.00%, 0.00%] | 2.46% | ×0.00 | — | — | no | not applicable |
| R100 | chain50 | credential path | 1201 s | edit chain, 4 records | 2 | 2 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, natural | 525 s | edit chain, 4 records | 2 | 3 | 33.33% [0.00%, 33.33%] | 1.28% | ×26.00 | — | — | no | not applicable |
| R100 | chain50 | blind-issued one-time certificates, lengthened hold | 1214 s | edit chain, 4 records | 2 | 1 | 0.00% [0.00%, 0.00%] | 0.00% | ×— | — | — | no | not applicable |

## issuer withholding or delaying refills

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L10 | 2 | 3 | 0.00% [0.00%, 0.00%] | 0.88% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L120 | 2 | 13 | 7.69% [0.00%, 14.29%] | 0.87% | ×8.82 | — | 0.917 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L30 | 2 | 7 | 0.00% [0.00%, 0.00%] | 0.85% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L60 | 2 | 10 | 0.00% [0.00%, 0.00%] | 0.87% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L10 | 2 | 3 | 0.00% [0.00%, 0.00%] | 0.88% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L120 | 2 | 13 | 7.69% [0.00%, 14.29%] | 0.87% | ×8.80 | — | 0.917 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L30 | 2 | 7 | 0.00% [0.00%, 0.00%] | 0.85% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L60 | 2 | 10 | 0.00% [0.00%, 0.00%] | 0.87% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L10 | 2 | 3 | 0.00% [0.00%, 0.00%] | 0.88% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L120 | 2 | 13 | 7.69% [0.00%, 14.29%] | 0.87% | ×8.82 | — | 0.917 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L30 | 2 | 7 | 0.00% [0.00%, 0.00%] | 0.85% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L60 | 2 | 10 | 0.00% [0.00%, 0.00%] | 0.87% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L10 | 1 | 2 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L120 | 2 | 12 | 0.00% [0.00%, 0.00%] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L30 | 2 | 7 | 0.00% [0.00%, 0.00%] | 0.44% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L60 | 2 | 11 | 0.00% [0.00%, 0.00%] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L10 | 1 | 2 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L120 | 2 | 12 | 0.00% [0.00%, 0.00%] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L30 | 2 | 7 | 0.00% [0.00%, 0.00%] | 0.44% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L60 | 2 | 11 | 0.00% [0.00%, 0.00%] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L10 | 1 | 2 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L120 | 2 | 12 | 0.00% [0.00%, 0.00%] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L30 | 2 | 7 | 0.00% [0.00%, 0.00%] | 0.44% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L60 | 2 | 11 | 0.00% [0.00%, 0.00%] | 0.45% | ×0.00 | — | — | no | not applicable |

## Spread of the posterior and calibration

Entropy and min-entropy in bits at the calibrated temperature; the effective anonymity set is 2 to the entropy. Devices: the naming rate over true devices with at least 10 records (median, 90th percentile, and the worst-off device with its records). Sampling: the calibration error a perfectly calibrated attacker would reach at the 99th percentile by sampling alone, at the same confidences. Flag: the calibration error is above that and exceeds both 2 points and a quarter of the larger of the accuracy and the mean confidence.

| File | Vantage | Entropy | Effective set | Min-entropy | Top-1 | Top-5 | Top-10 | Devices: median, p90, worst (records) | Calibration error | Sampling | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| c6__cp_W0__R1 | observer | 5.79 | 56.1 | 4.26 | 6.78% | 19.85% | 32.69% | 6.76%, 7.86%, 8.13% (209) | 3.57% | 4.53% |  |
| c6__cp_W0__R1 | first_hop | 5.79 | 56.0 | 4.26 | 6.59% | 19.65% | 32.75% | 6.57%, 7.69%, 7.97% (4180) | 3.34% | 1.03% | badly miscalibrated |
| c6__cp_W0__R1 | content_server | 5.64 | 50.9 | 4.08 | 6.42% | 23.85% | 39.10% | 6.40%, 7.21%, 7.42% (418) | 3.76% | 3.48% | badly miscalibrated |
| c6__cp_W0__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (408) | 0.00% | 0.00% |  |
| c6__cp_W0__R100 | observer | 6.94 | 123.0 | 5.39 | 1.73% | 10.53% | 19.49% | 0.00%, 6.67%, 33.33% (15) | 1.13% | 1.91% |  |
| c6__cp_W0__R100 | first_hop | 6.94 | 123.0 | 5.39 | 1.74% | 10.45% | 19.45% | 0.00%, 0.00%, 50.00% (80) | 1.04% | 0.37% |  |
| c6__cp_W0__R100 | content_server | 6.81 | 112.4 | 5.21 | 2.59% | 12.95% | 22.82% | 0.00%, 7.50%, 33.33% (18) | 0.87% | 1.27% |  |
| c6__cp_W0__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (14) | 0.00% | 0.00% |  |
| c6__cp_W1__R1 | observer | 5.78 | 54.9 | 4.56 | 0.00% | 4.90% | 17.53% | 0.00%, 0.00%, 0.00% (206) | 4.27% | 4.12% | badly miscalibrated |
| c6__cp_W1__R1 | first_hop | 5.78 | 54.9 | 4.56 | 0.00% | 4.85% | 17.37% | 0.00%, 0.00%, 0.00% (4120) | 4.28% | 0.89% | badly miscalibrated |
| c6__cp_W1__R1 | content_server | 5.68 | 51.4 | 4.47 | 0.39% | 7.86% | 22.04% | 0.36%, 0.66%, 0.73% (412) | 4.16% | 2.92% | badly miscalibrated |
| c6__cp_W1__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (412) | 0.00% | 0.00% |  |
| c6__cp_W1__R100 | observer | 6.39 | 83.9 | 4.29 | 6.94% | 16.46% | 28.12% | 0.00%, 2.63%, 90.54% (74) | 1.88% | 2.54% |  |
| c6__cp_W1__R100 | first_hop | 6.39 | 83.9 | 4.29 | 6.93% | 16.43% | 28.01% | 0.00%, 0.00%, 89.93% (1480) | 1.82% | 0.53% |  |
| c6__cp_W1__R100 | content_server | 6.28 | 78.3 | 4.25 | 7.05% | 17.57% | 30.22% | 0.00%, 0.00%, 79.73% (148) | 1.60% | 1.88% |  |
| c6__cp_W1__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (30) | 0.00% | 0.00% |  |
| c6__cp_W2__R1 | observer | 5.54 | 47.4 | 3.87 | 8.20% | 22.95% | 32.79% | 8.14%, 11.09%, 11.83% (186) | 8.81% | 5.70% | badly miscalibrated |
| c6__cp_W2__R1 | first_hop | 5.54 | 47.3 | 3.87 | 8.33% | 22.96% | 32.72% | 8.27%, 11.46%, 12.26% (3720) | 8.64% | 1.12% | badly miscalibrated |
| c6__cp_W2__R1 | content_server | 5.44 | 44.1 | 3.78 | 9.02% | 25.82% | 38.25% | 8.96%, 11.68%, 12.37% (372) | 7.70% | 3.90% | badly miscalibrated |
| c6__cp_W2__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (360) | 0.00% | 0.00% |  |
| c6__cp_W2__R100 | observer | 6.37 | 82.8 | 4.12 | 7.13% | 18.59% | 29.89% | 0.00%, 16.09%, 65.45% (55) | 3.01% | 2.77% | badly miscalibrated |
| c6__cp_W2__R100 | first_hop | 6.37 | 82.8 | 4.12 | 7.08% | 18.55% | 30.00% | 0.00%, 0.00%, 65.45% (1100) | 2.92% | 0.58% | badly miscalibrated |
| c6__cp_W2__R100 | content_server | 6.25 | 76.8 | 4.08 | 6.84% | 20.15% | 32.64% | 0.00%, 0.00%, 62.90% (62) | 1.69% | 1.88% |  |
| c6__cp_W2__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (26) | 0.00% | 0.00% |  |
| c6__cp_Wmis__R1 | observer | 5.56 | 47.4 | 3.72 | 20.77% | 30.60% | 38.25% | 20.68%, 24.78%, 25.81% (186) | 15.61% | 5.46% | badly miscalibrated |
| c6__cp_Wmis__R1 | first_hop | 5.56 | 47.4 | 3.72 | 20.92% | 30.55% | 38.48% | 20.83%, 24.77%, 25.75% (3720) | 15.06% | 1.29% | badly miscalibrated |
| c6__cp_Wmis__R1 | content_server | 5.02 | 34.4 | 3.10 | 20.49% | 31.97% | 43.85% | 20.41%, 24.51%, 25.54% (372) | 7.93% | 5.11% | badly miscalibrated |
| c6__cp_Wmis__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (360) | 0.00% | 0.00% |  |
| c6__cp_Wmis__R100 | observer | 6.03 | 66.0 | 3.31 | 9.83% | 25.39% | 37.51% | 0.00%, 27.38%, 65.62% (64) | 2.33% | 3.52% |  |
| c6__cp_Wmis__R100 | first_hop | 6.03 | 66.0 | 3.31 | 9.81% | 25.36% | 37.43% | 0.00%, 0.00%, 65.62% (1280) | 2.24% | 0.72% |  |
| c6__cp_Wmis__R100 | content_server | 5.90 | 60.5 | 3.32 | 9.17% | 27.27% | 38.86% | 0.00%, 7.67%, 64.52% (62) | 2.96% | 2.47% | badly miscalibrated |
| c6__cp_Wmis__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (24) | 0.00% | 0.00% |  |
| c6__cp_chain100__R1 | observer | 5.78 | 55.3 | 4.24 | 7.14% | 19.76% | 34.76% | 7.17%, 8.78%, 9.18% (207) | 4.91% | 4.28% | badly miscalibrated |
| c6__cp_chain100__R1 | first_hop | 5.78 | 55.3 | 4.24 | 7.37% | 19.99% | 34.75% | 7.39%, 8.76%, 9.11% (4140) | 4.66% | 1.00% | badly miscalibrated |
| c6__cp_chain100__R1 | content_server | 5.62 | 50.1 | 4.05 | 7.14% | 22.14% | 36.79% | 7.19%, 9.94%, 10.63% (414) | 4.40% | 3.44% | badly miscalibrated |
| c6__cp_chain100__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (414) | 0.00% | 0.00% |  |
| c6__cp_chain100__R100 | observer | 6.77 | 110.4 | 5.07 | 1.78% | 11.83% | 19.45% | 0.00%, 11.00%, 27.27% (11) | 1.83% | 1.99% |  |
| c6__cp_chain100__R100 | first_hop | 6.77 | 110.4 | 5.07 | 1.82% | 11.72% | 19.65% | 0.00%, 0.00%, 27.27% (220) | 1.73% | 0.47% |  |
| c6__cp_chain100__R100 | content_server | 6.42 | 86.3 | 4.47 | 3.08% | 13.29% | 22.33% | 0.00%, 10.00%, 23.08% (26) | 1.56% | 1.64% |  |
| c6__cp_chain100__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (30) | 0.00% | 0.00% |  |
| c6__cp_chain50__R1 | observer | 5.99 | 64.2 | 4.30 | 4.51% | 16.86% | 28.27% | 1.42%, 6.58%, 8.19% (171) | 5.20% | 4.50% | badly miscalibrated |
| c6__cp_chain50__R1 | first_hop | 5.99 | 64.1 | 4.30 | 4.50% | 16.98% | 28.22% | 1.48%, 6.52%, 8.04% (3420) | 5.01% | 0.95% | badly miscalibrated |
| c6__cp_chain50__R1 | content_server | 5.82 | 57.3 | 4.14 | 5.11% | 21.02% | 33.61% | 2.41%, 6.77%, 7.60% (342) | 3.66% | 3.37% | badly miscalibrated |
| c6__cp_chain50__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (74) | 0.00% | 0.00% |  |
| c6__cp_chain50__R100 | observer | 6.99 | 128.7 | 5.17 | 2.17% | 9.34% | 17.31% | 0.00%, 14.17%, 41.67% (12) | 1.65% | 1.85% |  |
| c6__cp_chain50__R100 | first_hop | 6.99 | 128.6 | 5.17 | 2.16% | 9.42% | 17.40% | 0.00%, 0.00%, 75.00% (80) | 1.67% | 0.43% |  |
| c6__cp_chain50__R100 | content_server | 6.81 | 114.9 | 4.97 | 2.98% | 12.00% | 20.53% | 0.00%, 11.81%, 37.50% (24) | 1.12% | 1.57% |  |
| c6__cp_chain50__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (18) | 0.00% | 0.00% |  |
| c6__otcL_W0__R1 | observer | 5.65 | 50.4 | 4.27 | 2.66% | 21.79% | 38.26% | 2.65%, 3.59%, 3.83% (209) | 3.93% | 4.19% |  |
| c6__otcL_W0__R1 | first_hop | 5.76 | 54.4 | 4.55 | 2.93% | 21.78% | 38.04% | 2.92%, 3.84%, 4.07% (4180) | 3.77% | 0.94% | badly miscalibrated |
| c6__otcL_W0__R1 | destination | 5.64 | 50.1 | 4.44 | 4.12% | 24.46% | 38.74% | 4.09%, 5.79%, 6.22% (209) | 2.85% | 4.00% |  |
| c6__otcL_W0__R1 | destination_keyed | 3.95 | 15.7 | 3.01 | 15.50% | 50.61% | 78.93% | 15.46%, 17.64%, 18.18% (209) | 7.35% | 6.66% | badly miscalibrated |
| c6__otcL_W0__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (204) | 0.00% | 0.00% |  |
| c6__otcL_W0__R1 | issuer_0 [share 50%, all records] | 5.56 | 47.3 | 4.83 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 3.53% | 3.60% |  |
| c6__otcL_W0__R1 | issuer_0 [share 50%, other issuers' devices] | 5.56 | 47.3 | 4.83 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 3.53% | 3.60% |  |
| c6__otcL_W0__R1 | issuer_0_with_observer [share 50%, all records] | 5.75 | 54.2 | 4.49 | 2.66% | 21.07% | 37.53% | 2.64%, 4.36%, 4.78% (209) | 3.84% | 3.97% |  |
| c6__otcL_W0__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.75 | 54.2 | 4.49 | 2.66% | 21.07% | 37.53% | 2.64%, 4.36%, 4.78% (209) | 3.84% | 3.97% |  |
| c6__otcL_W0__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.75 | 54.0 | 4.49 | 2.91% | 20.58% | 37.29% | 2.89%, 4.02%, 4.31% (209) | 3.12% | 4.20% |  |
| c6__otcL_W0__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.75 | 54.0 | 4.49 | 2.91% | 20.58% | 37.29% | 2.89%, 4.02%, 4.31% (209) | 3.12% | 4.20% |  |
| c6__otcL_W0__R1 | issuer_1 [share 30%, all records] | 4.71 | 26.6 | 3.73 | 8.23% | 40.92% | 58.84% | 8.19%, 11.21%, 11.96% (209) | 11.18% | 5.36% | badly miscalibrated |
| c6__otcL_W0__R1 | issuer_1 [share 30%, its own devices] | 4.71 | 26.6 | 3.73 | 8.23% | 40.92% | 58.84% | 8.19%, 11.21%, 11.96% (209) | 11.18% | 5.36% | badly miscalibrated |
| c6__otcL_W0__R1 | issuer_1_with_observer [share 30%, all records] | 5.64 | 50.0 | 4.20 | 6.05% | 23.73% | 37.29% | 6.01%, 8.86%, 9.57% (209) | 4.09% | 4.02% | badly miscalibrated |
| c6__otcL_W0__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.64 | 50.0 | 4.20 | 6.05% | 23.73% | 37.29% | 6.01%, 8.86%, 9.57% (209) | 4.09% | 4.02% | badly miscalibrated |
| c6__otcL_W0__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.75 | 54.1 | 4.49 | 5.81% | 23.73% | 36.80% | 5.78%, 8.05%, 8.61% (209) | 2.65% | 4.07% |  |
| c6__otcL_W0__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.75 | 54.1 | 4.49 | 5.81% | 23.73% | 36.80% | 5.78%, 8.05%, 8.61% (209) | 2.65% | 4.07% |  |
| c6__otcL_W0__R1 | issuer_1_with_destination | 3.93 | 15.5 | 2.93 | 15.74% | 52.06% | 78.45% | 15.70%, 18.07%, 18.66% (209) | 5.93% | 6.18% |  |
| c6__otcL_W0__R1 | issuer_2 [share 20%, all records] | 4.43 | 21.7 | 3.86 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 7.00% | 5.19% | badly miscalibrated |
| c6__otcL_W0__R1 | issuer_2 [share 20%, other issuers' devices] | 4.43 | 21.7 | 3.86 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 7.00% | 5.19% | badly miscalibrated |
| c6__otcL_W0__R1 | issuer_2_with_observer [share 20%, all records] | 5.76 | 54.3 | 4.50 | 2.91% | 20.82% | 36.80% | 2.89%, 4.02%, 4.31% (209) | 3.73% | 4.08% |  |
| c6__otcL_W0__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.76 | 54.3 | 4.50 | 2.91% | 20.82% | 36.80% | 2.89%, 4.02%, 4.31% (209) | 3.73% | 4.08% |  |
| c6__otcL_W0__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.75 | 54.2 | 4.49 | 2.91% | 20.82% | 36.56% | 2.89%, 4.02%, 4.31% (209) | 3.12% | 4.05% |  |
| c6__otcL_W0__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.75 | 54.2 | 4.49 | 2.91% | 20.82% | 36.56% | 2.89%, 4.02%, 4.31% (209) | 3.12% | 4.05% |  |
| c6__otcL_W0__R100 | observer | 6.60 | 97.5 | 5.06 | 2.88% | 11.76% | 22.70% | 0.00%, 10.00%, 18.18% (11) | 1.00% | 1.93% |  |
| c6__otcL_W0__R100 | first_hop | 6.60 | 97.2 | 5.05 | 2.92% | 11.83% | 22.69% | 0.00%, 10.00%, 42.86% (140) | 0.77% | 0.47% |  |
| c6__otcL_W0__R100 | destination | 6.48 | 89.8 | 4.93 | 2.80% | 11.84% | 21.96% | 0.00%, 7.69%, 20.00% (10) | 1.05% | 2.06% |  |
| c6__otcL_W0__R100 | destination_keyed | 5.05 | 35.3 | 3.75 | 7.24% | 29.11% | 48.11% | 0.00%, 16.67%, 50.00% (10) | 1.37% | 2.99% |  |
| c6__otcL_W0__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (15) | 0.00% | 0.00% |  |
| c6__otcL_W0__R100 | issuer_0 [share 50%, all records] | 5.68 | 51.3 | 4.79 | 1.56% | 5.59% | 9.13% | 0.00%, 0.00%, 13.33% (15) | 2.30% | 2.11% | badly miscalibrated |
| c6__otcL_W0__R100 | issuer_0 [share 50%, its own devices] | 5.68 | 51.4 | 4.78 | 2.87% | 10.26% | 16.74% | 0.00%, 7.39%, 13.33% (15) | 2.29% | 3.08% |  |
| c6__otcL_W0__R100 | issuer_0 [share 50%, other issuers' devices] | 5.71 | 52.4 | 5.25 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 2.63% | 2.73% |  |
| c6__otcL_W0__R100 | issuer_0_with_observer [share 50%, all records] | 6.60 | 96.9 | 5.00 | 2.96% | 12.42% | 22.94% | 0.00%, 10.00%, 18.18% (11) | 1.20% | 2.12% |  |
| c6__otcL_W0__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.59 | 96.8 | 5.00 | 3.47% | 14.33% | 24.28% | 0.00%, 11.62%, 18.18% (11) | 2.53% | 2.57% |  |
| c6__otcL_W0__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.60 | 97.1 | 4.99 | 2.35% | 10.13% | 21.34% | 0.00%, 4.55%, 36.36% (11) | 1.40% | 2.99% |  |
| c6__otcL_W0__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.59 | 96.6 | 4.99 | 3.04% | 12.34% | 23.68% | 0.00%, 10.00%, 18.18% (11) | 1.13% | 2.06% |  |
| c6__otcL_W0__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.59 | 96.5 | 4.99 | 3.17% | 13.88% | 24.59% | 0.00%, 11.62%, 18.18% (11) | 2.30% | 2.64% |  |
| c6__otcL_W0__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.59 | 96.8 | 4.99 | 2.89% | 10.49% | 22.60% | 0.00%, 14.09%, 36.36% (11) | 1.63% | 2.98% |  |
| c6__otcL_W0__R100 | issuer_0_with_destination | 5.48 | 44.8 | 4.02 | 6.79% | 22.17% | 37.41% | 0.00%, 22.18%, 40.00% (10) | 2.08% | 3.68% |  |
| c6__otcL_W0__R100 | issuer_1 [share 30%, all records] | 4.74 | 26.7 | 3.89 | 1.23% | 3.70% | 13.65% | 0.00%, 6.67%, 20.00% (10) | 5.62% | 2.98% | badly miscalibrated |
| c6__otcL_W0__R100 | issuer_1 [share 30%, its own devices] | 4.74 | 26.8 | 3.88 | 4.64% | 13.93% | 51.39% | 0.00%, 10.61%, 16.67% (12) | 4.48% | 5.44% |  |
| c6__otcL_W0__R100 | issuer_1 [share 30%, other issuers' devices] | 4.77 | 27.3 | 4.34 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (13) | 4.96% | 2.93% | badly miscalibrated |
| c6__otcL_W0__R100 | issuer_1_with_observer [share 30%, all records] | 6.60 | 97.3 | 5.04 | 2.55% | 11.68% | 22.37% | 0.00%, 10.00%, 20.00% (10) | 1.02% | 1.98% |  |
| c6__otcL_W0__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.60 | 97.5 | 5.04 | 4.33% | 15.79% | 23.84% | 0.00%, 9.27%, 10.00% (10) | 3.01% | 3.77% |  |
| c6__otcL_W0__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.60 | 97.2 | 5.03 | 1.90% | 10.19% | 21.84% | 0.00%, 8.83%, 18.18% (11) | 1.68% | 2.21% |  |
| c6__otcL_W0__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.60 | 96.9 | 5.02 | 2.80% | 11.84% | 22.62% | 0.00%, 10.00%, 20.00% (10) | 1.36% | 2.02% |  |
| c6__otcL_W0__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.60 | 97.1 | 5.02 | 4.64% | 16.10% | 23.53% | 0.00%, 11.64%, 18.18% (11) | 3.27% | 3.74% |  |
| c6__otcL_W0__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.59 | 96.9 | 5.02 | 2.13% | 10.30% | 22.28% | 0.00%, 8.83%, 20.00% (10) | 1.80% | 2.27% |  |
| c6__otcL_W0__R100 | issuer_1_with_destination | 4.68 | 25.8 | 3.41 | 8.67% | 34.37% | 57.28% | 8.33%, 16.97%, 18.18% (11) | 5.34% | 6.35% |  |
| c6__otcL_W0__R100 | issuer_2 [share 20%, all records] | 4.31 | 20.0 | 3.58 | 0.82% | 7.65% | 10.03% | 0.00%, 0.00%, 13.33% (15) | 7.81% | 3.12% | badly miscalibrated |
| c6__otcL_W0__R100 | issuer_2 [share 20%, its own devices] | 4.30 | 19.9 | 3.56 | 4.35% | 40.43% | 53.04% | 0.00%, 0.00%, 0.00% (12) | 6.67% | 7.82% |  |
| c6__otcL_W0__R100 | issuer_2 [share 20%, other issuers' devices] | 4.34 | 20.4 | 3.97 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 6.45% | 3.14% | badly miscalibrated |
| c6__otcL_W0__R100 | issuer_2_with_observer [share 20%, all records] | 6.60 | 97.4 | 5.04 | 2.63% | 12.17% | 22.37% | 0.00%, 10.00%, 18.18% (22) | 0.61% | 1.92% |  |
| c6__otcL_W0__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.60 | 97.5 | 5.03 | 1.30% | 9.57% | 21.30% | 0.00%, 0.00%, 0.00% (12) | 3.20% | 4.31% |  |
| c6__otcL_W0__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.60 | 97.4 | 5.05 | 2.94% | 12.78% | 22.62% | 0.00%, 10.00%, 18.18% (22) | 1.03% | 2.19% |  |
| c6__otcL_W0__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.60 | 97.1 | 5.04 | 2.71% | 12.17% | 22.62% | 0.00%, 10.00%, 18.18% (11) | 0.85% | 2.06% |  |
| c6__otcL_W0__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.60 | 97.2 | 5.03 | 1.74% | 10.87% | 21.74% | 3.57%, 6.43%, 7.14% (14) | 2.61% | 4.61% |  |
| c6__otcL_W0__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.60 | 97.0 | 5.04 | 2.94% | 12.47% | 22.82% | 0.00%, 10.00%, 18.18% (11) | 1.03% | 2.17% |  |
| c6__otcL_W0__R100 | issuer_2_with_destination | 4.47 | 22.5 | 3.58 | 8.70% | 39.13% | 63.91% | 7.14%, 12.86%, 14.29% (14) | 3.19% | 7.46% |  |
| c6__otcL_W1__R1 | observer | 5.59 | 48.3 | 4.60 | 0.52% | 11.34% | 26.55% | 0.49%, 0.87%, 0.97% (206) | 4.06% | 4.17% |  |
| c6__otcL_W1__R1 | first_hop | 5.58 | 48.1 | 4.60 | 0.67% | 11.55% | 26.71% | 0.63%, 1.14%, 1.26% (4120) | 3.86% | 0.90% | badly miscalibrated |
| c6__otcL_W1__R1 | destination | 5.48 | 44.9 | 4.52 | 1.29% | 13.92% | 30.41% | 1.21%, 2.18%, 2.43% (206) | 4.41% | 4.19% | badly miscalibrated |
| c6__otcL_W1__R1 | destination_keyed | 3.72 | 13.5 | 2.99 | 5.93% | 47.16% | 87.63% | 5.90%, 6.23%, 6.31% (206) | 7.37% | 6.39% | badly miscalibrated |
| c6__otcL_W1__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (206) | 0.00% | 0.00% |  |
| c6__otcL_W1__R1 | issuer_0 [share 50%, all records] | 5.00 | 31.9 | 3.44 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 9.22% | 6.16% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_0 [share 50%, other issuers' devices] | 5.00 | 31.9 | 3.44 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 9.22% | 6.16% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_0_with_observer [share 50%, all records] | 5.58 | 48.1 | 4.59 | 0.52% | 10.57% | 24.74% | 0.49%, 0.87%, 0.97% (206) | 4.11% | 4.03% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.58 | 48.1 | 4.59 | 0.52% | 10.57% | 24.74% | 0.49%, 0.87%, 0.97% (206) | 4.11% | 4.03% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.58 | 48.0 | 4.58 | 0.52% | 11.08% | 25.00% | 0.49%, 0.87%, 0.97% (206) | 4.17% | 3.91% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.58 | 48.0 | 4.58 | 0.52% | 11.08% | 25.00% | 0.49%, 0.87%, 0.97% (206) | 4.17% | 3.91% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_1 [share 30%, all records] | 4.79 | 27.6 | 3.73 | 0.00% | 3.61% | 79.12% | 0.00%, 0.00%, 0.00% (206) | 7.67% | 5.34% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_1 [share 30%, its own devices] | 4.79 | 27.6 | 3.73 | 0.00% | 3.61% | 79.12% | 0.00%, 0.00%, 0.00% (206) | 7.67% | 5.34% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_1_with_observer [share 30%, all records] | 5.58 | 48.2 | 4.59 | 1.03% | 12.89% | 28.09% | 0.97%, 1.75%, 1.94% (206) | 3.56% | 3.98% |  |
| c6__otcL_W1__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.58 | 48.2 | 4.59 | 1.03% | 12.89% | 28.09% | 0.97%, 1.75%, 1.94% (206) | 3.56% | 3.98% |  |
| c6__otcL_W1__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.58 | 48.0 | 4.59 | 1.03% | 12.89% | 28.61% | 0.97%, 1.75%, 1.94% (206) | 4.15% | 4.07% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.58 | 48.0 | 4.59 | 1.03% | 12.89% | 28.61% | 0.97%, 1.75%, 1.94% (206) | 4.15% | 4.07% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_1_with_destination | 3.72 | 13.4 | 2.95 | 7.47% | 46.91% | 86.60% | 7.49%, 7.65%, 7.69% (182) | 6.51% | 6.56% |  |
| c6__otcL_W1__R1 | issuer_2 [share 20%, all records] | 4.02 | 16.3 | 2.73 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 15.07% | 6.96% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_2 [share 20%, other issuers' devices] | 4.02 | 16.3 | 2.73 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 15.07% | 6.96% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_2_with_observer [share 20%, all records] | 5.58 | 48.2 | 4.59 | 0.52% | 11.34% | 26.03% | 0.49%, 0.87%, 0.97% (206) | 4.11% | 4.15% |  |
| c6__otcL_W1__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.58 | 48.2 | 4.59 | 0.52% | 11.34% | 26.03% | 0.49%, 0.87%, 0.97% (206) | 4.11% | 4.15% |  |
| c6__otcL_W1__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.58 | 48.1 | 4.58 | 0.52% | 12.11% | 26.03% | 0.49%, 0.87%, 0.97% (206) | 4.17% | 3.75% | badly miscalibrated |
| c6__otcL_W1__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.58 | 48.1 | 4.58 | 0.52% | 12.11% | 26.03% | 0.49%, 0.87%, 0.97% (206) | 4.17% | 3.75% | badly miscalibrated |
| c6__otcL_W1__R100 | observer | 6.14 | 71.0 | 4.14 | 6.10% | 18.83% | 31.10% | 0.00%, 4.08%, 64.86% (74) | 1.65% | 2.68% |  |
| c6__otcL_W1__R100 | first_hop | 6.14 | 70.8 | 4.14 | 6.19% | 18.87% | 31.01% | 0.00%, 0.00%, 64.53% (1480) | 1.11% | 0.57% |  |
| c6__otcL_W1__R100 | destination | 6.05 | 66.7 | 4.09 | 6.33% | 18.90% | 31.94% | 0.00%, 5.28%, 67.44% (43) | 1.27% | 2.68% |  |
| c6__otcL_W1__R100 | destination_keyed | 4.58 | 25.2 | 3.05 | 12.04% | 38.64% | 59.45% | 0.00%, 25.95%, 90.70% (43) | 3.99% | 3.57% | badly miscalibrated |
| c6__otcL_W1__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (15) | 0.00% | 0.00% |  |
| c6__otcL_W1__R100 | issuer_0 [share 50%, all records] | 5.01 | 32.3 | 3.25 | 5.64% | 10.90% | 21.27% | 0.00%, 0.00%, 100.00% (74) | 6.68% | 3.24% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_0 [share 50%, its own devices] | 5.01 | 32.3 | 3.24 | 10.74% | 20.75% | 40.49% | 0.00%, 0.00%, 100.00% (74) | 12.04% | 4.68% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_0 [share 50%, other issuers' devices] | 5.15 | 35.6 | 3.61 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (24) | 8.35% | 4.16% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_0_with_observer [share 50%, all records] | 6.14 | 70.7 | 4.13 | 6.55% | 19.51% | 31.17% | 0.00%, 7.42%, 62.79% (43) | 2.08% | 2.63% |  |
| c6__otcL_W1__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.14 | 71.0 | 4.14 | 8.27% | 23.80% | 33.67% | 0.00%, 7.97%, 60.81% (74) | 3.86% | 3.56% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.28 | 78.6 | 4.50 | 4.65% | 14.77% | 28.41% | 0.00%, 3.23%, 62.79% (43) | 5.80% | 3.34% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.13 | 70.5 | 4.12 | 6.25% | 19.59% | 31.71% | 0.00%, 6.35%, 59.46% (74) | 1.63% | 2.70% |  |
| c6__otcL_W1__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.14 | 70.7 | 4.13 | 7.84% | 24.38% | 34.25% | 0.00%, 7.91%, 59.46% (74) | 3.66% | 3.60% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.27 | 78.4 | 4.50 | 4.49% | 14.29% | 28.89% | 0.00%, 4.31%, 58.14% (43) | 5.52% | 3.36% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_0_with_destination | 5.12 | 34.9 | 3.58 | 10.45% | 30.33% | 49.49% | 0.00%, 22.77%, 64.86% (74) | 4.57% | 4.47% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_1 [share 30%, all records] | 4.55 | 23.5 | 4.46 | 0.00% | 2.74% | 14.63% | 0.00%, 0.00%, 0.00% (15) | 4.57% | 2.48% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_1 [share 30%, its own devices] | 4.55 | 23.5 | 4.45 | 0.00% | 11.76% | 62.75% | 0.00%, 0.00%, 0.00% (20) | 4.57% | 4.52% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_1 [share 30%, other issuers' devices] | 4.50 | 22.7 | 3.62 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 8.19% | 3.46% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_1_with_observer [share 30%, all records] | 6.14 | 70.7 | 4.14 | 6.33% | 18.67% | 30.49% | 0.00%, 5.01%, 64.86% (74) | 1.77% | 2.75% |  |
| c6__otcL_W1__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.28 | 79.1 | 4.54 | 0.65% | 8.17% | 19.93% | 0.00%, 5.32%, 5.56% (18) | 4.27% | 4.77% |  |
| c6__otcL_W1__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.14 | 70.8 | 4.14 | 8.05% | 21.87% | 33.70% | 0.00%, 7.58%, 64.86% (74) | 2.61% | 2.91% |  |
| c6__otcL_W1__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.13 | 70.5 | 4.14 | 6.40% | 18.67% | 30.41% | 0.00%, 5.41%, 64.86% (74) | 1.27% | 2.48% |  |
| c6__otcL_W1__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.28 | 78.8 | 4.53 | 0.98% | 8.17% | 20.26% | 0.00%, 5.56%, 5.56% (18) | 3.94% | 4.58% |  |
| c6__otcL_W1__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.13 | 70.6 | 4.13 | 8.05% | 21.87% | 33.50% | 0.00%, 7.58%, 64.86% (74) | 2.41% | 2.82% |  |
| c6__otcL_W1__R100 | issuer_1_with_destination | 4.47 | 22.4 | 3.27 | 8.82% | 38.89% | 63.40% | 11.11%, 25.47%, 47.37% (19) | 5.85% | 7.24% |  |
| c6__otcL_W1__R100 | issuer_2 [share 20%, all records] | 3.75 | 13.6 | 1.76 | 5.72% | 11.97% | 18.67% | 0.00%, 0.00%, 100.00% (43) | 24.61% | 4.86% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_2 [share 20%, its own devices] | 3.74 | 13.5 | 1.75 | 23.66% | 49.53% | 77.29% | 0.00%, 100.00%, 100.00% (43) | 13.12% | 10.01% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_2 [share 20%, other issuers' devices] | 4.26 | 19.2 | 2.93 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 13.21% | 4.58% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_2_with_observer [share 20%, all records] | 6.14 | 70.8 | 4.14 | 6.25% | 18.75% | 31.17% | 0.00%, 4.36%, 64.86% (74) | 1.44% | 2.61% |  |
| c6__otcL_W1__R100 | issuer_2_with_observer [share 20%, its own devices] | 5.75 | 56.9 | 3.57 | 8.83% | 24.29% | 36.91% | 0.00%, 15.43%, 60.47% (43) | 11.98% | 6.11% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.14 | 71.0 | 4.14 | 5.43% | 16.98% | 29.35% | 0.00%, 4.44%, 64.86% (74) | 3.71% | 2.81% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.13 | 70.6 | 4.13 | 6.33% | 19.13% | 30.95% | 0.00%, 4.36%, 64.86% (74) | 1.68% | 2.58% |  |
| c6__otcL_W1__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 5.75 | 56.6 | 3.56 | 9.15% | 24.29% | 36.59% | 0.00%, 15.89%, 62.79% (43) | 12.35% | 6.37% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.14 | 70.7 | 4.14 | 5.43% | 17.49% | 29.15% | 0.00%, 4.44%, 64.86% (74) | 3.35% | 2.92% | badly miscalibrated |
| c6__otcL_W1__R100 | issuer_2_with_destination | 3.97 | 15.9 | 2.61 | 24.29% | 54.89% | 80.44% | 25.00%, 51.10%, 93.02% (43) | 8.93% | 7.72% | badly miscalibrated |
| c6__otcL_W2__R1 | observer | 5.45 | 44.0 | 4.11 | 5.74% | 23.22% | 40.98% | 5.75%, 6.48%, 6.67% (180) | 4.17% | 4.82% |  |
| c6__otcL_W2__R1 | first_hop | 5.45 | 43.9 | 4.11 | 5.67% | 23.47% | 40.68% | 5.68%, 6.43%, 6.61% (3600) | 4.05% | 1.14% | badly miscalibrated |
| c6__otcL_W2__R1 | destination | 5.41 | 42.9 | 4.31 | 4.92% | 22.68% | 38.52% | 4.91%, 5.28%, 5.38% (186) | 4.93% | 4.60% | badly miscalibrated |
| c6__otcL_W2__R1 | destination_keyed | 3.72 | 13.4 | 2.95 | 15.85% | 53.01% | 87.16% | 15.96%, 21.41%, 22.78% (180) | 3.41% | 6.85% |  |
| c6__otcL_W2__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (180) | 0.00% | 0.00% |  |
| c6__otcL_W2__R1 | issuer_0 [share 50%, all records] | 4.99 | 31.7 | 3.31 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 10.08% | 6.34% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_0 [share 50%, other issuers' devices] | 4.99 | 31.7 | 3.31 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 10.08% | 6.34% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_0_with_observer [share 50%, all records] | 5.44 | 43.7 | 4.06 | 4.92% | 21.31% | 38.52% | 4.92%, 4.98%, 5.00% (180) | 4.30% | 5.30% |  |
| c6__otcL_W2__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.44 | 43.7 | 4.06 | 4.92% | 21.31% | 38.52% | 4.92%, 4.98%, 5.00% (180) | 4.30% | 5.30% |  |
| c6__otcL_W2__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.44 | 43.5 | 4.06 | 4.64% | 21.04% | 37.98% | 4.65%, 4.93%, 5.00% (180) | 2.98% | 5.01% |  |
| c6__otcL_W2__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.44 | 43.5 | 4.06 | 4.64% | 21.04% | 37.98% | 4.65%, 4.93%, 5.00% (180) | 2.98% | 5.01% |  |
| c6__otcL_W2__R1 | issuer_1 [share 30%, all records] | 4.64 | 25.6 | 3.65 | 0.00% | 3.01% | 48.09% | 0.00%, 0.00%, 0.00% (180) | 9.21% | 5.89% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_1 [share 30%, its own devices] | 4.64 | 25.6 | 3.65 | 0.00% | 3.01% | 48.09% | 0.00%, 0.00%, 0.00% (180) | 9.21% | 5.89% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_1_with_observer [share 30%, all records] | 5.45 | 43.7 | 4.05 | 9.29% | 24.59% | 41.80% | 9.29%, 9.41%, 9.44% (180) | 6.43% | 4.85% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.45 | 43.7 | 4.05 | 9.29% | 24.59% | 41.80% | 9.29%, 9.41%, 9.44% (180) | 6.43% | 4.85% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.44 | 43.6 | 4.05 | 8.47% | 25.14% | 41.80% | 8.48%, 8.81%, 8.89% (180) | 4.58% | 5.06% |  |
| c6__otcL_W2__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.44 | 43.6 | 4.05 | 8.47% | 25.14% | 41.80% | 8.48%, 8.81%, 8.89% (180) | 4.58% | 5.06% |  |
| c6__otcL_W2__R1 | issuer_1_with_destination | 3.70 | 13.3 | 2.87 | 19.13% | 53.28% | 86.89% | 19.22%, 23.84%, 25.00% (180) | 5.80% | 6.94% |  |
| c6__otcL_W2__R1 | issuer_2 [share 20%, all records] | 4.10 | 17.3 | 2.95 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 13.80% | 7.49% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_2 [share 20%, other issuers' devices] | 4.10 | 17.3 | 2.95 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 13.80% | 7.49% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_2_with_observer [share 20%, all records] | 5.45 | 43.8 | 4.08 | 5.46% | 22.95% | 40.98% | 5.48%, 6.43%, 6.67% (180) | 5.62% | 4.94% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.45 | 43.8 | 4.08 | 5.46% | 22.95% | 40.98% | 5.48%, 6.43%, 6.67% (180) | 5.62% | 4.94% | badly miscalibrated |
| c6__otcL_W2__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.44 | 43.7 | 4.08 | 4.92% | 22.95% | 40.44% | 4.94%, 5.88%, 6.11% (180) | 4.02% | 5.27% |  |
| c6__otcL_W2__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.44 | 43.7 | 4.08 | 4.92% | 22.95% | 40.44% | 4.94%, 5.88%, 6.11% (180) | 4.02% | 5.27% |  |
| c6__otcL_W2__R100 | observer | 6.14 | 70.8 | 4.10 | 5.81% | 20.23% | 32.19% | 0.00%, 15.92%, 61.29% (31) | 2.27% | 2.62% |  |
| c6__otcL_W2__R100 | first_hop | 6.14 | 70.6 | 4.10 | 5.86% | 20.32% | 32.19% | 0.00%, 0.00%, 61.29% (620) | 1.77% | 0.61% |  |
| c6__otcL_W2__R100 | destination | 6.19 | 73.5 | 4.45 | 5.81% | 20.48% | 33.42% | 0.00%, 14.63%, 54.84% (31) | 3.73% | 2.32% | badly miscalibrated |
| c6__otcL_W2__R100 | destination_keyed | 4.76 | 29.0 | 3.36 | 13.35% | 38.90% | 58.23% | 5.26%, 39.57%, 65.45% (55) | 4.61% | 3.57% | badly miscalibrated |
| c6__otcL_W2__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (13) | 0.00% | 0.00% |  |
| c6__otcL_W2__R100 | issuer_0 [share 50%, all records] | 5.30 | 39.5 | 3.54 | 4.50% | 13.19% | 19.16% | 0.00%, 0.00%, 100.00% (55) | 4.65% | 3.11% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_0 [share 50%, its own devices] | 5.29 | 39.5 | 3.54 | 7.81% | 22.87% | 33.24% | 0.00%, 0.00%, 100.00% (55) | 6.58% | 4.18% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_0 [share 50%, other issuers' devices] | 5.30 | 39.6 | 3.55 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (36) | 8.65% | 4.66% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_0_with_observer [share 50%, all records] | 6.13 | 70.1 | 4.07 | 6.14% | 20.48% | 31.78% | 0.00%, 20.03%, 61.29% (31) | 2.09% | 2.57% |  |
| c6__otcL_W2__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.13 | 70.2 | 4.07 | 8.95% | 24.01% | 34.38% | 0.00%, 20.82%, 61.29% (31) | 4.29% | 3.48% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.29 | 79.2 | 4.49 | 2.32% | 15.67% | 28.24% | 0.00%, 14.69%, 25.00% (20) | 2.99% | 3.81% |  |
| c6__otcL_W2__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.12 | 70.0 | 4.07 | 6.06% | 20.48% | 31.86% | 0.00%, 20.03%, 61.29% (31) | 2.31% | 2.63% |  |
| c6__otcL_W2__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.13 | 70.1 | 4.07 | 8.81% | 23.86% | 35.23% | 0.00%, 20.82%, 61.29% (31) | 4.00% | 3.55% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.29 | 79.0 | 4.49 | 2.32% | 15.86% | 27.27% | 0.00%, 14.69%, 25.00% (20) | 3.19% | 3.61% |  |
| c6__otcL_W2__R100 | issuer_0_with_destination | 5.16 | 36.0 | 3.58 | 12.64% | 34.09% | 50.57% | 0.00%, 30.50%, 64.52% (31) | 7.99% | 4.06% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_1 [share 30%, all records] | 4.31 | 20.1 | 2.96 | 1.64% | 6.47% | 10.32% | 0.00%, 0.00%, 100.00% (20) | 12.64% | 4.02% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_1 [share 30%, its own devices] | 4.34 | 20.4 | 3.04 | 8.44% | 33.33% | 53.16% | 0.00%, 50.00%, 100.00% (20) | 12.70% | 9.46% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_1 [share 30%, other issuers' devices] | 4.36 | 20.5 | 3.05 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (13) | 12.09% | 4.13% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_1_with_observer [share 30%, all records] | 6.14 | 70.6 | 4.09 | 5.81% | 20.15% | 31.37% | 0.00%, 15.92%, 61.29% (31) | 1.95% | 2.59% |  |
| c6__otcL_W2__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.41 | 86.6 | 4.90 | 2.11% | 10.97% | 18.99% | 0.00%, 12.50%, 25.00% (20) | 4.87% | 4.73% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.14 | 70.6 | 4.09 | 6.71% | 22.36% | 34.35% | 0.00%, 13.64%, 61.29% (31) | 2.50% | 3.15% |  |
| c6__otcL_W2__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.13 | 70.5 | 4.08 | 5.81% | 20.23% | 31.37% | 0.00%, 15.92%, 61.29% (31) | 1.76% | 2.72% |  |
| c6__otcL_W2__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.41 | 86.3 | 4.90 | 2.11% | 10.97% | 18.99% | 0.00%, 12.50%, 25.00% (20) | 4.88% | 4.73% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.13 | 70.4 | 4.09 | 6.71% | 22.46% | 34.35% | 0.00%, 13.64%, 61.29% (31) | 2.37% | 2.92% |  |
| c6__otcL_W2__R100 | issuer_1_with_destination | 4.49 | 22.7 | 3.42 | 12.24% | 39.66% | 65.40% | 16.76%, 51.07%, 57.14% (21) | 4.22% | 7.39% |  |
| c6__otcL_W2__R100 | issuer_2 [share 20%, all records] | 4.02 | 16.8 | 2.80 | 3.77% | 8.27% | 16.71% | 0.00%, 0.00%, 100.00% (36) | 12.76% | 4.05% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_2 [share 20%, its own devices] | 4.04 | 17.0 | 2.85 | 16.43% | 36.07% | 72.86% | 0.00%, 43.16%, 100.00% (36) | 4.47% | 7.83% |  |
| c6__otcL_W2__R100 | issuer_2 [share 20%, other issuers' devices] | 4.01 | 16.7 | 2.78 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (13) | 16.70% | 4.50% | badly miscalibrated |
| c6__otcL_W2__R100 | issuer_2_with_observer [share 20%, all records] | 6.14 | 70.7 | 4.11 | 5.90% | 20.23% | 32.27% | 0.00%, 15.92%, 58.06% (31) | 1.86% | 2.66% |  |
| c6__otcL_W2__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.13 | 70.2 | 4.10 | 3.21% | 22.14% | 36.07% | 0.00%, 14.11%, 21.05% (19) | 5.06% | 5.55% |  |
| c6__otcL_W2__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.14 | 70.8 | 4.11 | 6.70% | 19.66% | 31.14% | 0.00%, 17.07%, 58.06% (31) | 2.15% | 3.07% |  |
| c6__otcL_W2__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.14 | 70.5 | 4.11 | 5.98% | 20.31% | 32.43% | 0.00%, 18.65%, 58.06% (31) | 1.58% | 2.78% |  |
| c6__otcL_W2__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.13 | 70.1 | 4.10 | 3.21% | 22.14% | 36.07% | 0.00%, 14.11%, 21.05% (19) | 5.06% | 5.65% |  |
| c6__otcL_W2__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.14 | 70.7 | 4.11 | 6.80% | 19.77% | 31.35% | 0.00%, 18.89%, 58.06% (31) | 2.01% | 3.21% |  |
| c6__otcL_W2__R100 | issuer_2_with_destination | 4.07 | 16.9 | 2.90 | 16.43% | 50.00% | 71.07% | 13.81%, 34.53%, 61.11% (36) | 4.94% | 8.84% |  |
| c6__otcL_Wmis__R1 | observer | 5.44 | 43.9 | 3.84 | 16.12% | 32.24% | 44.81% | 16.10%, 16.98%, 17.20% (186) | 8.74% | 5.46% | badly miscalibrated |
| c6__otcL_Wmis__R1 | first_hop | 5.43 | 43.7 | 3.84 | 16.12% | 32.36% | 44.84% | 16.10%, 17.11%, 17.37% (3720) | 8.71% | 1.16% | badly miscalibrated |
| c6__otcL_Wmis__R1 | destination | 5.62 | 49.7 | 4.40 | 13.11% | 30.33% | 43.72% | 13.10%, 13.80%, 13.98% (186) | 8.19% | 4.82% | badly miscalibrated |
| c6__otcL_Wmis__R1 | destination_keyed | 3.93 | 15.5 | 2.94 | 26.23% | 55.19% | 76.78% | 26.18%, 28.46%, 29.03% (186) | 12.70% | 7.09% | badly miscalibrated |
| c6__otcL_Wmis__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (180) | 0.00% | 0.00% |  |
| c6__otcL_Wmis__R1 | issuer_0 [share 50%, all records] | 5.56 | 47.3 | 4.82 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 3.55% | 3.72% |  |
| c6__otcL_Wmis__R1 | issuer_0 [share 50%, other issuers' devices] | 5.56 | 47.3 | 4.82 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 3.55% | 3.72% |  |
| c6__otcL_Wmis__R1 | issuer_0_with_observer [share 50%, all records] | 5.61 | 49.2 | 4.12 | 13.66% | 31.15% | 43.72% | 13.63%, 15.20%, 15.59% (186) | 8.36% | 5.24% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.61 | 49.2 | 4.12 | 13.66% | 31.15% | 43.72% | 13.63%, 15.20%, 15.59% (186) | 8.36% | 5.24% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.40 | 42.8 | 3.73 | 13.39% | 30.87% | 44.81% | 13.36%, 14.72%, 15.05% (186) | 5.41% | 5.52% |  |
| c6__otcL_Wmis__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.40 | 42.8 | 3.73 | 13.39% | 30.87% | 44.81% | 13.36%, 14.72%, 15.05% (186) | 5.41% | 5.52% |  |
| c6__otcL_Wmis__R1 | issuer_1 [share 30%, all records] | 4.92 | 30.3 | 4.37 | 5.74% | 22.95% | 24.59% | 5.72%, 6.73%, 6.99% (186) | 3.81% | 4.52% |  |
| c6__otcL_Wmis__R1 | issuer_1 [share 30%, its own devices] | 4.92 | 30.3 | 4.37 | 5.74% | 22.95% | 24.59% | 5.72%, 6.73%, 6.99% (186) | 3.81% | 4.52% |  |
| c6__otcL_Wmis__R1 | issuer_1_with_observer [share 30%, all records] | 5.39 | 42.7 | 3.69 | 17.21% | 33.88% | 45.36% | 17.20%, 18.06%, 18.28% (186) | 10.11% | 5.89% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.39 | 42.7 | 3.69 | 17.21% | 33.88% | 45.36% | 17.20%, 18.06%, 18.28% (186) | 10.11% | 5.89% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.38 | 42.6 | 3.68 | 16.94% | 34.43% | 45.36% | 16.92%, 18.01%, 18.28% (186) | 9.37% | 6.21% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.38 | 42.6 | 3.68 | 16.94% | 34.43% | 45.36% | 16.92%, 18.01%, 18.28% (186) | 9.37% | 6.21% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_1_with_destination | 3.90 | 15.2 | 2.82 | 21.86% | 54.37% | 77.05% | 21.79%, 25.00%, 25.81% (186) | 7.31% | 7.44% |  |
| c6__otcL_Wmis__R1 | issuer_2 [share 20%, all records] | 4.43 | 21.7 | 3.83 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 7.12% | 5.84% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_2 [share 20%, other issuers' devices] | 4.43 | 21.7 | 3.83 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 7.12% | 5.84% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_2_with_observer [share 20%, all records] | 5.42 | 43.4 | 3.79 | 15.57% | 32.51% | 45.08% | 15.56%, 16.02%, 16.13% (186) | 8.17% | 5.68% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.42 | 43.4 | 3.79 | 15.57% | 32.51% | 45.08% | 15.56%, 16.02%, 16.13% (186) | 8.17% | 5.68% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.41 | 43.3 | 3.78 | 15.30% | 31.97% | 45.36% | 15.28%, 16.39%, 16.67% (186) | 7.48% | 5.74% | badly miscalibrated |
| c6__otcL_Wmis__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.41 | 43.3 | 3.78 | 15.30% | 31.97% | 45.36% | 15.28%, 16.39%, 16.67% (186) | 7.48% | 5.74% | badly miscalibrated |
| c6__otcL_Wmis__R100 | observer | 6.37 | 82.7 | 4.37 | 9.17% | 25.88% | 37.84% | 0.00%, 17.00%, 64.52% (31) | 4.10% | 2.45% | badly miscalibrated |
| c6__otcL_Wmis__R100 | first_hop | 6.36 | 82.5 | 4.37 | 9.28% | 25.91% | 37.77% | 0.00%, 1.41%, 64.84% (620) | 4.20% | 0.61% | badly miscalibrated |
| c6__otcL_Wmis__R100 | destination | 6.26 | 76.9 | 4.33 | 8.85% | 24.73% | 37.35% | 0.00%, 19.00%, 64.52% (31) | 3.83% | 2.31% | badly miscalibrated |
| c6__otcL_Wmis__R100 | destination_keyed | 4.83 | 30.3 | 3.29 | 15.23% | 42.51% | 59.21% | 4.76%, 41.40%, 64.52% (31) | 4.85% | 3.54% | badly miscalibrated |
| c6__otcL_Wmis__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (12) | 0.00% | 0.00% |  |
| c6__otcL_Wmis__R100 | issuer_0 [share 50%, all records] | 4.56 | 28.9 | 2.53 | 7.62% | 15.81% | 21.79% | 0.00%, 0.00%, 85.94% (64) | 22.15% | 4.28% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_0 [share 50%, its own devices] | 4.55 | 28.6 | 2.51 | 13.21% | 27.41% | 37.78% | 0.00%, 25.45%, 100.00% (55) | 20.83% | 5.58% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_0 [share 50%, other issuers' devices] | 5.52 | 46.0 | 4.03 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (12) | 6.66% | 3.96% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_0_with_observer [share 50%, all records] | 6.35 | 81.9 | 4.34 | 9.34% | 25.88% | 37.43% | 0.00%, 21.67%, 64.52% (31) | 4.19% | 2.47% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.07 | 68.6 | 3.86 | 11.65% | 29.40% | 40.77% | 0.00%, 26.15%, 65.45% (55) | 5.96% | 3.58% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.35 | 81.9 | 4.35 | 6.19% | 21.08% | 32.88% | 0.00%, 23.82%, 38.89% (36) | 2.51% | 3.73% |  |
| c6__otcL_Wmis__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.35 | 81.6 | 4.33 | 9.42% | 25.63% | 36.94% | 0.00%, 23.96%, 64.52% (31) | 4.17% | 2.34% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.06 | 68.3 | 3.84 | 11.79% | 29.26% | 40.62% | 0.00%, 26.15%, 64.52% (31) | 5.62% | 4.06% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.35 | 81.6 | 4.34 | 6.19% | 20.70% | 31.91% | 0.00%, 25.00%, 38.89% (36) | 3.35% | 3.66% |  |
| c6__otcL_Wmis__R100 | issuer_0_with_destination | 5.22 | 37.5 | 3.48 | 14.06% | 38.92% | 53.12% | 0.00%, 35.87%, 67.27% (55) | 5.64% | 4.43% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1 [share 30%, all records] | 3.58 | 13.8 | 1.99 | 2.62% | 8.11% | 11.47% | 0.00%, 0.00%, 100.00% (12) | 29.70% | 5.07% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1 [share 30%, its own devices] | 3.49 | 13.0 | 1.87 | 13.50% | 41.77% | 59.07% | 0.00%, 100.00%, 100.00% (20) | 23.90% | 11.19% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1 [share 30%, other issuers' devices] | 4.30 | 19.8 | 3.12 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 12.07% | 4.14% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1_with_observer [share 30%, all records] | 6.36 | 82.5 | 4.36 | 9.50% | 25.72% | 37.51% | 0.00%, 18.00%, 64.52% (31) | 4.37% | 2.43% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.52 | 92.7 | 4.79 | 5.06% | 15.19% | 24.05% | 0.00%, 22.59%, 30.00% (20) | 4.74% | 4.89% |  |
| c6__otcL_Wmis__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.09 | 69.6 | 3.89 | 10.57% | 28.25% | 40.75% | 0.00%, 28.10%, 72.73% (55) | 5.27% | 3.40% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.36 | 82.3 | 4.35 | 9.42% | 25.55% | 37.26% | 0.00%, 17.73%, 64.52% (31) | 4.27% | 2.49% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.52 | 92.4 | 4.78 | 3.80% | 15.19% | 24.47% | 0.00%, 20.57%, 30.00% (20) | 3.41% | 4.61% |  |
| c6__otcL_Wmis__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.08 | 69.3 | 3.88 | 10.77% | 28.05% | 40.35% | 0.00%, 28.10%, 70.91% (55) | 5.34% | 3.51% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_1_with_destination | 4.44 | 22.0 | 3.12 | 13.50% | 43.46% | 62.45% | 10.00%, 48.76%, 61.90% (21) | 5.39% | 8.38% |  |
| c6__otcL_Wmis__R100 | issuer_2 [share 20%, all records] | 4.13 | 17.6 | 2.31 | 4.91% | 10.07% | 17.85% | 0.00%, 0.00%, 100.00% (36) | 18.08% | 4.64% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2 [share 20%, its own devices] | 4.14 | 17.7 | 2.36 | 21.43% | 43.93% | 77.86% | 0.00%, 95.26%, 100.00% (36) | 7.44% | 9.99% |  |
| c6__otcL_Wmis__R100 | issuer_2 [share 20%, other issuers' devices] | 4.43 | 21.7 | 3.04 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (10) | 12.75% | 4.16% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2_with_observer [share 20%, all records] | 6.36 | 82.5 | 4.37 | 8.60% | 25.23% | 37.92% | 0.00%, 15.18%, 64.52% (31) | 3.97% | 2.48% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.03 | 67.8 | 3.80 | 7.86% | 26.43% | 41.79% | 0.00%, 27.30%, 36.11% (36) | 9.58% | 6.28% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.36 | 82.5 | 4.37 | 8.82% | 24.87% | 36.77% | 0.00%, 13.56%, 64.52% (31) | 4.72% | 2.69% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.36 | 82.3 | 4.36 | 8.85% | 25.06% | 37.51% | 0.00%, 18.91%, 64.52% (31) | 3.73% | 2.49% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.03 | 67.6 | 3.79 | 7.86% | 25.00% | 40.71% | 0.00%, 27.30%, 36.11% (36) | 7.41% | 6.53% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.36 | 82.3 | 4.36 | 9.14% | 25.08% | 36.56% | 0.00%, 15.84%, 64.52% (31) | 4.36% | 2.71% | badly miscalibrated |
| c6__otcL_Wmis__R100 | issuer_2_with_destination | 4.12 | 17.5 | 2.82 | 18.21% | 53.57% | 73.93% | 18.33%, 48.46%, 58.33% (36) | 6.81% | 8.11% |  |
| c6__otcL_chain100__R1 | observer | 5.63 | 49.7 | 4.25 | 5.48% | 21.19% | 37.38% | 5.51%, 7.29%, 7.73% (207) | 2.39% | 4.47% |  |
| c6__otcL_chain100__R1 | first_hop | 5.63 | 49.5 | 4.24 | 5.39% | 21.49% | 37.39% | 5.42%, 7.13%, 7.56% (4140) | 1.85% | 0.93% |  |
| c6__otcL_chain100__R1 | destination | 5.50 | 45.6 | 4.13 | 5.71% | 23.33% | 37.86% | 5.76%, 8.11%, 8.70% (207) | 3.04% | 4.61% |  |
| c6__otcL_chain100__R1 | destination_keyed | 5.71 | 52.4 | 4.67 | 2.14% | 5.95% | 10.48% | 2.15%, 2.75%, 2.90% (207) | 1.00% | 1.70% |  |
| c6__otcL_chain100__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (207) | 0.00% | 0.00% |  |
| c6__otcL_chain100__R1 | issuer_0 [share 50%, all records] | 5.56 | 47.1 | 4.70 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (207) | 3.93% | 3.52% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_0 [share 50%, other issuers' devices] | 5.56 | 47.1 | 4.70 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (207) | 3.93% | 3.52% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_0_with_observer [share 50%, all records] | 5.61 | 48.9 | 4.12 | 3.57% | 20.95% | 35.95% | 3.60%, 4.97%, 5.31% (207) | 2.51% | 4.85% |  |
| c6__otcL_chain100__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.61 | 48.9 | 4.12 | 3.57% | 20.95% | 35.95% | 3.60%, 4.97%, 5.31% (207) | 2.51% | 4.85% |  |
| c6__otcL_chain100__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.60 | 48.7 | 4.11 | 3.57% | 20.48% | 36.90% | 3.60%, 5.36%, 5.80% (207) | 3.85% | 5.05% |  |
| c6__otcL_chain100__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.60 | 48.7 | 4.11 | 3.57% | 20.48% | 36.90% | 3.60%, 5.36%, 5.80% (207) | 3.85% | 5.05% |  |
| c6__otcL_chain100__R1 | issuer_1 [share 30%, all records] | 4.83 | 28.5 | 3.92 | 8.57% | 53.10% | 56.43% | 5.42%, 8.60%, 9.39% (213) | 8.98% | 4.82% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_1 [share 30%, its own devices] | 4.83 | 28.5 | 3.93 | 9.82% | 53.68% | 56.49% | 6.30%, 10.77%, 11.89% (143) | 10.44% | 6.39% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_1 [share 30%, other issuers' devices] | 4.91 | 30.1 | 4.26 | 5.93% | 51.85% | 56.30% | 3.68%, 4.16%, 4.29% (70) | 5.13% | 8.53% |  |
| c6__otcL_chain100__R1 | issuer_1_with_observer [share 30%, all records] | 5.62 | 49.2 | 4.17 | 6.67% | 22.86% | 37.38% | 6.68%, 7.52%, 7.73% (207) | 3.70% | 4.45% |  |
| c6__otcL_chain100__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.62 | 49.5 | 4.17 | 7.72% | 25.61% | 41.40% | 7.72%, 8.30%, 8.45% (142) | 6.05% | 5.30% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_1_with_observer [share 30%, other issuers' devices] | 5.72 | 53.1 | 4.46 | 4.44% | 17.04% | 28.89% | 4.51%, 5.82%, 6.15% (65) | 5.56% | 7.80% |  |
| c6__otcL_chain100__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.61 | 49.0 | 4.16 | 6.67% | 23.10% | 37.62% | 6.69%, 7.91%, 8.21% (207) | 2.47% | 4.61% |  |
| c6__otcL_chain100__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.62 | 49.3 | 4.16 | 7.72% | 25.96% | 41.75% | 7.72%, 8.87%, 9.15% (142) | 3.97% | 5.31% |  |
| c6__otcL_chain100__R1 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 5.72 | 52.9 | 4.46 | 4.44% | 17.04% | 28.89% | 4.51%, 5.82%, 6.15% (65) | 4.57% | 8.10% |  |
| c6__otcL_chain100__R1 | issuer_1_with_destination | — | — | — | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (142) | 0.00% | 0.00% |  |
| c6__otcL_chain100__R1 | issuer_2 [share 20%, all records] | 4.43 | 21.6 | 3.76 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (207) | 7.58% | 5.03% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_2 [share 20%, other issuers' devices] | 4.43 | 21.6 | 3.76 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (207) | 7.58% | 5.03% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_2_with_observer [share 20%, all records] | 5.62 | 49.3 | 4.18 | 4.76% | 20.48% | 38.10% | 4.79%, 6.37%, 6.76% (207) | 3.07% | 4.53% |  |
| c6__otcL_chain100__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.62 | 49.3 | 4.18 | 4.76% | 20.48% | 38.10% | 4.79%, 6.37%, 6.76% (207) | 3.07% | 4.53% |  |
| c6__otcL_chain100__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.61 | 49.1 | 4.17 | 4.76% | 20.48% | 38.10% | 4.79%, 6.37%, 6.76% (207) | 4.90% | 4.60% | badly miscalibrated |
| c6__otcL_chain100__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.61 | 49.1 | 4.17 | 4.76% | 20.48% | 38.10% | 4.79%, 6.37%, 6.76% (207) | 4.90% | 4.60% | badly miscalibrated |
| c6__otcL_chain100__R100 | observer | 6.62 | 98.4 | 5.10 | 3.14% | 12.31% | 21.48% | 0.00%, 15.76%, 27.27% (11) | 1.65% | 1.94% |  |
| c6__otcL_chain100__R100 | first_hop | 6.61 | 98.1 | 5.09 | 3.15% | 12.18% | 21.56% | 0.00%, 9.14%, 32.78% (180) | 1.33% | 0.40% |  |
| c6__otcL_chain100__R100 | destination | 6.61 | 98.2 | 5.30 | 3.22% | 13.27% | 22.28% | 0.00%, 11.93%, 27.27% (11) | 1.86% | 1.85% |  |
| c6__otcL_chain100__R100 | destination_keyed | 3.20 | 43.9 | 2.53 | 1.61% | 5.71% | 8.77% | 0.00%, 8.71%, 28.57% (14) | 33.13% | 2.30% | badly miscalibrated |
| c6__otcL_chain100__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (15) | 0.00% | 0.00% |  |
| c6__otcL_chain100__R100 | issuer_0 [share 50%, all records] | 5.90 | 59.7 | 5.27 | 1.29% | 5.79% | 20.60% | 0.00%, 0.00%, 86.67% (15) | 1.94% | 1.87% |  |
| c6__otcL_chain100__R100 | issuer_0 [share 50%, its own devices] | 5.90 | 59.8 | 5.05 | 2.36% | 12.23% | 38.41% | 0.00%, 0.00%, 0.00% (10) | 1.47% | 3.17% |  |
| c6__otcL_chain100__R100 | issuer_0 [share 50%, other issuers' devices] | 5.91 | 60.2 | 5.48 | 0.64% | 1.93% | 9.91% | 0.00%, 0.00%, 0.00% (10) | 2.01% | 2.10% |  |
| c6__otcL_chain100__R100 | issuer_0_with_observer [share 50%, all records] | 6.61 | 97.5 | 4.99 | 3.38% | 11.99% | 21.64% | 0.00%, 16.23%, 42.86% (14) | 1.53% | 1.93% |  |
| c6__otcL_chain100__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.61 | 97.7 | 4.98 | 3.86% | 12.88% | 24.46% | 0.00%, 21.38%, 38.46% (13) | 2.70% | 3.32% |  |
| c6__otcL_chain100__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.60 | 97.4 | 4.99 | 3.09% | 11.45% | 19.95% | 0.00%, 12.48%, 20.00% (10) | 1.21% | 2.53% |  |
| c6__otcL_chain100__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.60 | 97.2 | 4.98 | 3.06% | 12.07% | 21.72% | 0.00%, 12.70%, 28.57% (14) | 1.82% | 1.93% |  |
| c6__otcL_chain100__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.60 | 97.5 | 4.98 | 3.43% | 12.88% | 23.61% | 0.00%, 15.23%, 23.08% (13) | 2.82% | 3.40% |  |
| c6__otcL_chain100__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.60 | 97.1 | 4.98 | 2.83% | 11.58% | 20.59% | 0.00%, 9.67%, 18.75% (16) | 1.25% | 2.71% |  |
| c6__otcL_chain100__R100 | issuer_0_with_destination | 0.47 | 1.5 | 0.30 | 2.15% | 2.79% | 2.79% | 0.00%, 12.31%, 30.77% (13) | 66.91% | 4.21% | badly miscalibrated |
| c6__otcL_chain100__R100 | issuer_1 [share 30%, all records] | 5.34 | 40.6 | 3.97 | 1.29% | 8.53% | 18.83% | 0.00%, 8.33%, 27.27% (11) | 5.29% | 2.64% | badly miscalibrated |
| c6__otcL_chain100__R100 | issuer_1 [share 30%, its own devices] | 5.34 | 40.5 | 3.95 | 5.94% | 37.62% | 77.23% | — | 4.67% | 6.89% |  |
| c6__otcL_chain100__R100 | issuer_1 [share 30%, other issuers' devices] | 5.36 | 41.2 | 4.52 | 0.38% | 2.88% | 7.49% | 0.00%, 0.00%, 0.00% (11) | 4.75% | 2.77% | badly miscalibrated |
| c6__otcL_chain100__R100 | issuer_1_with_observer [share 30%, all records] | 6.61 | 97.6 | 4.97 | 3.62% | 12.23% | 21.80% | 0.00%, 17.42%, 31.25% (16) | 1.75% | 2.03% |  |
| c6__otcL_chain100__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.61 | 98.0 | 4.97 | 5.94% | 16.34% | 26.24% | — | 4.38% | 4.86% |  |
| c6__otcL_chain100__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.60 | 97.5 | 4.97 | 3.17% | 11.43% | 20.94% | 0.00%, 16.90%, 27.27% (11) | 1.65% | 2.25% |  |
| c6__otcL_chain100__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.60 | 97.3 | 4.96 | 3.54% | 12.87% | 21.64% | 0.00%, 16.03%, 31.25% (16) | 1.47% | 2.08% |  |
| c6__otcL_chain100__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.61 | 97.7 | 4.96 | 6.44% | 16.83% | 26.73% | — | 4.93% | 5.14% |  |
| c6__otcL_chain100__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.60 | 97.2 | 4.96 | 2.98% | 12.10% | 20.65% | 0.00%, 10.89%, 27.27% (11) | 1.23% | 2.21% |  |
| c6__otcL_chain100__R100 | issuer_1_with_destination | 0.46 | 1.4 | 0.31 | 0.50% | 0.99% | 0.99% | — | 26.55% | 3.80% | badly miscalibrated |
| c6__otcL_chain100__R100 | issuer_2 [share 20%, all records] | 4.76 | 27.3 | 3.44 | 1.69% | 8.77% | 14.80% | 0.00%, 6.27%, 19.05% (21) | 8.86% | 3.23% | badly miscalibrated |
| c6__otcL_chain100__R100 | issuer_2 [share 20%, its own devices] | 4.78 | 27.7 | 3.48 | 9.52% | 44.64% | 70.83% | — | 5.79% | 8.84% |  |
| c6__otcL_chain100__R100 | issuer_2 [share 20%, other issuers' devices] | 4.88 | 29.6 | 4.37 | 0.47% | 3.16% | 6.05% | 0.00%, 0.00%, 11.76% (17) | 4.59% | 2.67% | badly miscalibrated |
| c6__otcL_chain100__R100 | issuer_2_with_observer [share 20%, all records] | 6.61 | 98.0 | 5.05 | 2.90% | 12.63% | 22.20% | 0.00%, 13.25%, 27.27% (11) | 1.54% | 2.00% |  |
| c6__otcL_chain100__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.73 | 106.3 | 5.40 | 4.76% | 20.83% | 26.79% | — | 4.16% | 4.93% |  |
| c6__otcL_chain100__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.61 | 98.1 | 5.05 | 2.60% | 11.35% | 21.49% | 0.00%, 16.97%, 30.00% (10) | 1.52% | 2.02% |  |
| c6__otcL_chain100__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.61 | 97.7 | 5.05 | 3.14% | 12.55% | 21.64% | 0.00%, 14.36%, 27.27% (11) | 1.61% | 1.96% |  |
| c6__otcL_chain100__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.72 | 106.0 | 5.39 | 5.95% | 20.83% | 25.60% | — | 5.43% | 4.92% | badly miscalibrated |
| c6__otcL_chain100__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.61 | 97.9 | 5.05 | 2.70% | 11.26% | 21.02% | 0.00%, 16.97%, 30.00% (10) | 1.67% | 2.01% |  |
| c6__otcL_chain100__R100 | issuer_2_with_destination | 0.02 | 1.0 | 0.01 | 0.00% | 0.00% | 0.00% | — | 30.77% | 0.41% | badly miscalibrated |
| c6__otcL_chain50__R1 | observer | 5.83 | 57.1 | 4.40 | 6.41% | 21.85% | 37.29% | 2.02%, 9.45%, 11.76% (170) | 2.79% | 4.09% |  |
| c6__otcL_chain50__R1 | first_hop | 5.83 | 56.9 | 4.39 | 6.22% | 21.84% | 37.41% | 1.98%, 9.16%, 11.38% (3400) | 2.46% | 0.88% | badly miscalibrated |
| c6__otcL_chain50__R1 | destination | 5.68 | 51.6 | 4.26 | 4.28% | 23.52% | 37.77% | 2.12%, 6.51%, 8.24% (170) | 3.00% | 4.47% |  |
| c6__otcL_chain50__R1 | destination_keyed | 5.85 | 58.4 | 4.77 | 0.95% | 5.23% | 8.79% | 0.88%, 2.28%, 2.50% (40) | 0.56% | 1.44% |  |
| c6__otcL_chain50__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (40) | 0.00% | 0.00% |  |
| c6__otcL_chain50__R1 | issuer_0 [share 50%, all records] | 5.56 | 47.1 | 4.69 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (40) | 3.94% | 3.73% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_0 [share 50%, other issuers' devices] | 5.56 | 47.1 | 4.69 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (40) | 3.94% | 3.73% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_0_with_observer [share 50%, all records] | 5.81 | 56.4 | 4.28 | 3.09% | 20.19% | 37.05% | 0.58%, 4.88%, 6.47% (170) | 2.78% | 4.77% |  |
| c6__otcL_chain50__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.81 | 56.4 | 4.28 | 3.09% | 20.19% | 37.05% | 0.58%, 4.88%, 6.47% (170) | 2.78% | 4.77% |  |
| c6__otcL_chain50__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.81 | 56.2 | 4.27 | 3.09% | 19.95% | 36.82% | 0.58%, 4.88%, 6.47% (170) | 4.23% | 4.26% |  |
| c6__otcL_chain50__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.81 | 56.2 | 4.27 | 3.09% | 19.95% | 36.82% | 0.58%, 4.88%, 6.47% (170) | 4.23% | 4.26% |  |
| c6__otcL_chain50__R1 | issuer_1 [share 30%, all records] | 4.83 | 28.5 | 3.92 | 7.84% | 43.71% | 46.32% | 0.59%, 8.04%, 10.98% (173) | 9.22% | 5.09% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_1 [share 30%, its own devices] | 4.83 | 28.5 | 3.93 | 9.82% | 53.68% | 56.49% | 6.30%, 10.77%, 11.89% (143) | 10.44% | 6.39% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_1 [share 30%, other issuers' devices] | 4.92 | 30.2 | 4.26 | 3.68% | 22.79% | 25.00% | 1.79%, 5.74%, 6.67% (30) | 5.81% | 9.03% |  |
| c6__otcL_chain50__R1 | issuer_1_with_observer [share 30%, all records] | 5.82 | 56.5 | 4.29 | 7.84% | 23.04% | 35.15% | 4.05%, 10.25%, 11.18% (170) | 3.64% | 4.44% |  |
| c6__otcL_chain50__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.60 | 49.2 | 3.89 | 9.47% | 26.67% | 40.70% | 9.48%, 10.35%, 10.56% (142) | 4.92% | 5.74% |  |
| c6__otcL_chain50__R1 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.05 | 66.6 | 4.92 | 4.41% | 15.44% | 23.53% | 3.33%, 12.00%, 14.29% (28) | 4.16% | 7.10% |  |
| c6__otcL_chain50__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.81 | 56.4 | 4.29 | 8.08% | 22.80% | 35.87% | 4.05%, 10.66%, 11.76% (170) | 5.48% | 4.27% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.81 | 56.3 | 4.28 | 9.82% | 27.02% | 41.40% | 9.83%, 10.98%, 11.27% (142) | 6.64% | 5.23% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.05 | 66.4 | 4.91 | 4.41% | 13.97% | 24.26% | 3.33%, 12.00%, 14.29% (28) | 4.16% | 6.13% |  |
| c6__otcL_chain50__R1 | issuer_1_with_destination | — | — | — | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (143) | 0.00% | 0.00% |  |
| c6__otcL_chain50__R1 | issuer_2 [share 20%, all records] | 4.43 | 21.6 | 3.76 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (40) | 7.56% | 4.57% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_2 [share 20%, other issuers' devices] | 4.43 | 21.6 | 3.76 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (40) | 7.56% | 4.57% | badly miscalibrated |
| c6__otcL_chain50__R1 | issuer_2_with_observer [share 20%, all records] | 5.82 | 56.8 | 4.34 | 5.23% | 21.38% | 37.77% | 2.02%, 7.39%, 8.82% (170) | 3.20% | 4.24% |  |
| c6__otcL_chain50__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.82 | 56.8 | 4.34 | 5.23% | 21.38% | 37.77% | 2.02%, 7.39%, 8.82% (170) | 3.20% | 4.24% |  |
| c6__otcL_chain50__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.82 | 56.6 | 4.33 | 5.23% | 20.90% | 38.24% | 2.31%, 7.15%, 8.24% (170) | 4.15% | 4.44% |  |
| c6__otcL_chain50__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.82 | 56.6 | 4.33 | 5.23% | 20.90% | 38.24% | 2.31%, 7.15%, 8.24% (170) | 4.15% | 4.44% |  |
| c6__otcL_chain50__R100 | observer | 6.80 | 111.4 | 5.23 | 3.13% | 11.80% | 19.42% | 6.25%, 20.00%, 27.27% (11) | 0.89% | 1.81% |  |
| c6__otcL_chain50__R100 | first_hop | 6.79 | 111.0 | 5.22 | 3.04% | 11.73% | 19.65% | 0.00%, 3.38%, 36.00% (100) | 0.75% | 0.43% |  |
| c6__otcL_chain50__R100 | destination | 6.77 | 109.9 | 5.42 | 3.53% | 12.68% | 19.90% | 6.25%, 20.00%, 27.27% (11) | 1.83% | 1.97% |  |
| c6__otcL_chain50__R100 | destination_keyed | 3.71 | 37.9 | 2.95 | 4.57% | 12.92% | 15.81% | 0.00%, 9.09%, 20.00% (10) | 20.14% | 4.28% | badly miscalibrated |
| c6__otcL_chain50__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (14) | 0.00% | 0.00% |  |
| c6__otcL_chain50__R100 | issuer_0 [share 50%, all records] | 5.91 | 60.1 | 5.23 | 1.12% | 5.14% | 16.53% | 0.00%, 0.00%, 100.00% (10) | 1.57% | 1.74% |  |
| c6__otcL_chain50__R100 | issuer_0 [share 50%, its own devices] | 5.90 | 59.8 | 5.05 | 2.36% | 12.23% | 38.41% | 0.00%, 0.00%, 0.00% (12) | 1.47% | 3.17% |  |
| c6__otcL_chain50__R100 | issuer_0 [share 50%, other issuers' devices] | 5.88 | 58.9 | 5.12 | 0.38% | 0.90% | 3.46% | 0.00%, 0.00%, 0.00% (12) | 2.86% | 2.38% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_0_with_observer [share 50%, all records] | 6.78 | 110.5 | 5.09 | 2.97% | 11.96% | 19.26% | 0.00%, 13.33%, 30.00% (10) | 1.85% | 2.08% |  |
| c6__otcL_chain50__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.79 | 110.6 | 5.09 | 3.65% | 14.38% | 23.39% | 6.25%, 11.25%, 12.50% (16) | 2.27% | 3.08% |  |
| c6__otcL_chain50__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.78 | 110.3 | 5.09 | 2.56% | 10.51% | 16.79% | 8.33%, 13.00%, 20.00% (10) | 2.86% | 2.33% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.78 | 110.1 | 5.08 | 2.81% | 12.20% | 19.58% | 0.00%, 11.76%, 27.27% (11) | 1.71% | 1.89% |  |
| c6__otcL_chain50__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.78 | 110.3 | 5.08 | 3.00% | 14.59% | 22.75% | 6.25%, 11.25%, 12.50% (16) | 1.73% | 3.09% |  |
| c6__otcL_chain50__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.78 | 109.9 | 5.08 | 2.69% | 10.77% | 17.69% | 8.33%, 13.00%, 20.00% (10) | 2.81% | 2.43% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_0_with_destination | 2.48 | 6.0 | 1.66 | 6.01% | 17.60% | 20.17% | 0.00%, 0.00%, 0.00% (12) | 27.72% | 8.69% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_1 [share 30%, all records] | 5.34 | 40.6 | 3.96 | 1.12% | 6.98% | 15.73% | 0.00%, 8.33%, 18.18% (11) | 5.50% | 2.93% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_1 [share 30%, its own devices] | 5.34 | 40.5 | 3.95 | 5.94% | 37.62% | 77.23% | 0.00%, 0.00%, 0.00% (10) | 4.67% | 6.89% |  |
| c6__otcL_chain50__R100 | issuer_1 [share 30%, other issuers' devices] | 5.36 | 41.2 | 4.53 | 0.19% | 1.05% | 3.83% | 0.00%, 0.00%, 0.00% (14) | 4.95% | 2.47% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_1_with_observer [share 30%, all records] | 6.79 | 110.7 | 5.15 | 2.81% | 12.28% | 19.82% | 0.00%, 20.00%, 23.53% (17) | 0.85% | 1.97% |  |
| c6__otcL_chain50__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.58 | 96.9 | 4.72 | 6.93% | 19.80% | 26.24% | 0.00%, 0.00%, 0.00% (10) | 4.69% | 5.87% |  |
| c6__otcL_chain50__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.79 | 110.6 | 5.15 | 2.01% | 10.82% | 18.58% | 0.00%, 20.00%, 23.53% (17) | 1.30% | 2.06% |  |
| c6__otcL_chain50__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.78 | 110.3 | 5.14 | 2.89% | 11.96% | 20.14% | 0.00%, 17.65%, 20.00% (10) | 0.70% | 2.04% |  |
| c6__otcL_chain50__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.57 | 96.6 | 4.72 | 6.44% | 18.32% | 26.73% | 0.00%, 0.00%, 0.00% (10) | 5.67% | 5.57% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.78 | 110.2 | 5.14 | 2.20% | 10.73% | 18.87% | 0.00%, 17.65%, 20.00% (10) | 1.22% | 2.08% |  |
| c6__otcL_chain50__R100 | issuer_1_with_destination | 1.78 | 3.8 | 1.39 | 1.98% | 5.94% | 6.44% | 0.00%, 0.00%, 0.00% (10) | 40.83% | 11.91% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_2 [share 20%, all records] | 4.76 | 27.3 | 3.44 | 1.44% | 7.30% | 11.40% | 0.00%, 0.00%, 20.00% (10) | 9.08% | 3.26% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_2 [share 20%, its own devices] | 4.78 | 27.7 | 3.48 | 9.52% | 44.64% | 70.83% | — | 5.79% | 8.84% |  |
| c6__otcL_chain50__R100 | issuer_2 [share 20%, other issuers' devices] | 4.88 | 29.7 | 4.60 | 0.19% | 1.48% | 2.13% | 0.00%, 0.00%, 0.00% (14) | 4.07% | 2.28% | badly miscalibrated |
| c6__otcL_chain50__R100 | issuer_2_with_observer [share 20%, all records] | 6.79 | 110.7 | 5.15 | 2.73% | 11.96% | 19.66% | 0.00%, 20.00%, 27.27% (11) | 0.74% | 1.88% |  |
| c6__otcL_chain50__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.59 | 97.3 | 4.74 | 4.17% | 18.45% | 27.98% | — | 3.82% | 5.95% |  |
| c6__otcL_chain50__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.79 | 110.9 | 5.15 | 2.50% | 10.95% | 18.37% | 0.00%, 15.88%, 27.27% (11) | 1.28% | 1.99% |  |
| c6__otcL_chain50__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.78 | 110.4 | 5.14 | 2.73% | 11.88% | 19.66% | 0.00%, 20.00%, 27.27% (11) | 0.96% | 1.92% |  |
| c6__otcL_chain50__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.58 | 96.9 | 4.73 | 4.17% | 17.26% | 27.98% | — | 3.80% | 6.15% |  |
| c6__otcL_chain50__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.79 | 110.6 | 5.14 | 2.50% | 11.04% | 18.37% | 0.00%, 18.33%, 27.27% (11) | 1.29% | 1.95% |  |
| c6__otcL_chain50__R100 | issuer_2_with_destination | 1.32 | 2.7 | 0.85 | 9.52% | 16.07% | 16.07% | — | 49.53% | 13.13% | badly miscalibrated |
| c6__otc_W0__R1 | observer | 5.65 | 50.2 | 4.26 | 6.05% | 20.82% | 36.32% | 6.03%, 7.33%, 7.66% (209) | 3.61% | 4.59% |  |
| c6__otc_W0__R1 | first_hop | 5.64 | 50.1 | 4.26 | 6.13% | 20.87% | 36.23% | 6.11%, 7.38%, 7.70% (4180) | 2.58% | 1.01% | badly miscalibrated |
| c6__otc_W0__R1 | destination | 5.63 | 49.9 | 4.43 | 7.02% | 21.55% | 33.66% | 7.00%, 8.67%, 9.09% (209) | 4.80% | 4.64% | badly miscalibrated |
| c6__otc_W0__R1 | destination_keyed | 3.96 | 15.7 | 3.01 | 14.29% | 50.36% | 80.87% | 14.23%, 18.16%, 19.14% (209) | 4.85% | 6.52% |  |
| c6__otc_W0__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (204) | 0.00% | 0.00% |  |
| c6__otc_W0__R1 | issuer_0 [share 50%, all records] | 5.54 | 46.7 | 4.42 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 4.92% | 4.30% | badly miscalibrated |
| c6__otc_W0__R1 | issuer_0 [share 50%, other issuers' devices] | 5.54 | 46.7 | 4.42 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 4.92% | 4.30% | badly miscalibrated |
| c6__otc_W0__R1 | issuer_0_with_observer [share 50%, all records] | 5.71 | 52.9 | 4.22 | 3.15% | 18.64% | 34.38% | 3.15%, 3.31%, 3.35% (209) | 4.51% | 4.82% |  |
| c6__otc_W0__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.71 | 52.9 | 4.22 | 3.15% | 18.64% | 34.38% | 3.15%, 3.31%, 3.35% (209) | 4.51% | 4.82% |  |
| c6__otc_W0__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.71 | 52.8 | 4.21 | 3.15% | 18.89% | 34.38% | 3.15%, 3.31%, 3.35% (209) | 4.50% | 4.74% |  |
| c6__otc_W0__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.71 | 52.8 | 4.21 | 3.15% | 18.89% | 34.38% | 3.15%, 3.31%, 3.35% (209) | 4.50% | 4.74% |  |
| c6__otc_W0__R1 | issuer_1 [share 30%, all records] | 4.87 | 29.4 | 3.88 | 6.54% | 54.48% | 56.42% | 6.54%, 6.80%, 6.86% (204) | 3.67% | 5.24% |  |
| c6__otc_W0__R1 | issuer_1 [share 30%, its own devices] | 4.87 | 29.4 | 3.88 | 6.54% | 54.48% | 56.42% | 6.54%, 6.80%, 6.86% (204) | 3.67% | 5.24% |  |
| c6__otc_W0__R1 | issuer_1_with_observer [share 30%, all records] | 5.60 | 48.6 | 3.95 | 8.96% | 20.82% | 35.84% | 8.93%, 10.59%, 11.00% (209) | 2.85% | 4.99% |  |
| c6__otc_W0__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.60 | 48.6 | 3.95 | 8.96% | 20.82% | 35.84% | 8.93%, 10.59%, 11.00% (209) | 2.85% | 4.99% |  |
| c6__otc_W0__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.59 | 48.5 | 3.95 | 8.96% | 19.61% | 34.62% | 8.93%, 10.59%, 11.00% (209) | 2.65% | 5.01% |  |
| c6__otc_W0__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.59 | 48.5 | 3.95 | 8.96% | 19.61% | 34.62% | 8.93%, 10.59%, 11.00% (209) | 2.65% | 5.01% |  |
| c6__otc_W0__R1 | issuer_1_with_destination | 4.01 | 16.3 | 2.98 | 14.53% | 48.67% | 81.11% | 14.49%, 16.68%, 17.22% (209) | 3.77% | 6.97% |  |
| c6__otc_W0__R1 | issuer_2 [share 20%, all records] | 4.42 | 21.5 | 3.69 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 8.29% | 5.11% | badly miscalibrated |
| c6__otc_W0__R1 | issuer_2 [share 20%, other issuers' devices] | 4.42 | 21.5 | 3.69 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (204) | 8.29% | 5.11% | badly miscalibrated |
| c6__otc_W0__R1 | issuer_2_with_observer [share 20%, all records] | 5.62 | 49.3 | 4.06 | 5.08% | 20.10% | 36.32% | 5.06%, 6.37%, 6.70% (209) | 4.65% | 5.30% |  |
| c6__otc_W0__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.62 | 49.3 | 4.06 | 5.08% | 20.10% | 36.32% | 5.06%, 6.37%, 6.70% (209) | 4.65% | 5.30% |  |
| c6__otc_W0__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.61 | 49.1 | 4.06 | 5.57% | 19.85% | 35.84% | 5.54%, 7.23%, 7.66% (209) | 4.89% | 5.23% |  |
| c6__otc_W0__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.61 | 49.1 | 4.06 | 5.57% | 19.85% | 35.84% | 5.54%, 7.23%, 7.66% (209) | 4.89% | 5.23% |  |
| c6__otc_W0__R100 | observer | 6.62 | 98.8 | 5.08 | 3.04% | 13.40% | 22.78% | 0.00%, 15.38%, 27.27% (11) | 0.87% | 1.98% |  |
| c6__otc_W0__R100 | first_hop | 6.62 | 98.5 | 5.07 | 3.10% | 13.61% | 22.77% | 0.00%, 9.88%, 32.22% (180) | 0.89% | 0.44% |  |
| c6__otc_W0__R100 | destination | 6.50 | 90.6 | 4.95 | 2.30% | 13.57% | 23.11% | 0.00%, 9.09%, 20.00% (15) | 1.73% | 1.92% |  |
| c6__otc_W0__R100 | destination_keyed | 5.07 | 35.6 | 3.77 | 7.32% | 30.18% | 48.85% | 7.69%, 18.18%, 30.00% (10) | 2.25% | 3.19% |  |
| c6__otc_W0__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (15) | 0.00% | 0.00% |  |
| c6__otc_W0__R100 | issuer_0 [share 50%, all records] | 5.65 | 50.5 | 4.27 | 2.14% | 12.66% | 32.89% | 0.00%, 7.69%, 18.18% (11) | 3.32% | 2.35% | badly miscalibrated |
| c6__otc_W0__R100 | issuer_0 [share 50%, its own devices] | 5.66 | 50.7 | 4.27 | 3.92% | 23.23% | 60.33% | 0.00%, 8.11%, 18.18% (11) | 2.75% | 3.08% |  |
| c6__otc_W0__R100 | issuer_0 [share 50%, other issuers' devices] | 5.69 | 51.9 | 4.78 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 3.68% | 3.12% | badly miscalibrated |
| c6__otc_W0__R100 | issuer_0_with_observer [share 50%, all records] | 6.59 | 96.6 | 4.81 | 2.55% | 13.16% | 22.20% | 0.00%, 8.33%, 20.00% (15) | 1.78% | 2.18% |  |
| c6__otc_W0__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.59 | 96.5 | 4.81 | 3.92% | 15.23% | 24.43% | 0.00%, 18.18%, 20.00% (15) | 1.41% | 2.96% |  |
| c6__otc_W0__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.59 | 96.7 | 4.80 | 0.90% | 10.67% | 19.53% | 0.00%, 4.17%, 9.09% (11) | 3.33% | 3.10% | badly miscalibrated |
| c6__otc_W0__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.59 | 96.2 | 4.80 | 2.55% | 12.75% | 22.29% | 0.00%, 8.33%, 20.00% (15) | 1.52% | 2.15% |  |
| c6__otc_W0__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.58 | 96.1 | 4.80 | 3.77% | 15.08% | 24.74% | 0.00%, 18.18%, 20.00% (15) | 1.22% | 2.95% |  |
| c6__otc_W0__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.59 | 96.3 | 4.79 | 1.08% | 9.95% | 19.35% | 0.00%, 7.50%, 9.09% (11) | 3.16% | 3.21% |  |
| c6__otc_W0__R100 | issuer_0_with_destination | 5.43 | 43.5 | 3.83 | 5.43% | 23.38% | 38.61% | 0.00%, 18.73%, 23.08% (13) | 2.59% | 3.98% |  |
| c6__otc_W0__R100 | issuer_1 [share 30%, all records] | 4.72 | 26.4 | 3.61 | 1.15% | 13.82% | 14.06% | 0.00%, 8.33%, 25.00% (12) | 7.41% | 3.22% | badly miscalibrated |
| c6__otc_W0__R100 | issuer_1 [share 30%, its own devices] | 4.72 | 26.5 | 3.59 | 4.33% | 52.01% | 52.94% | 0.00%, 12.27%, 25.00% (12) | 4.82% | 5.88% |  |
| c6__otc_W0__R100 | issuer_1 [share 30%, other issuers' devices] | 4.76 | 27.1 | 4.03 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (13) | 6.24% | 3.33% | badly miscalibrated |
| c6__otc_W0__R100 | issuer_1_with_observer [share 30%, all records] | 6.61 | 97.9 | 4.97 | 3.12% | 13.32% | 22.78% | 0.00%, 13.33%, 27.27% (11) | 1.25% | 2.06% |  |
| c6__otc_W0__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.61 | 97.8 | 4.97 | 5.88% | 17.03% | 27.86% | 8.33%, 11.27%, 20.00% (10) | 4.00% | 4.30% |  |
| c6__otc_W0__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.61 | 97.9 | 4.97 | 2.13% | 11.98% | 20.94% | 0.00%, 14.79%, 27.27% (11) | 1.67% | 2.43% |  |
| c6__otc_W0__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.60 | 97.5 | 4.96 | 3.29% | 12.91% | 22.45% | 0.00%, 13.33%, 27.27% (11) | 1.46% | 1.94% |  |
| c6__otc_W0__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.60 | 97.5 | 4.96 | 5.57% | 16.41% | 27.24% | 8.33%, 11.27%, 20.00% (10) | 3.07% | 3.80% |  |
| c6__otc_W0__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.61 | 97.6 | 4.96 | 2.46% | 11.65% | 20.72% | 0.00%, 18.73%, 27.27% (11) | 1.64% | 2.45% |  |
| c6__otc_W0__R100 | issuer_1_with_destination | 4.90 | 30.1 | 3.86 | 8.67% | 33.75% | 56.66% | 9.09%, 29.09%, 36.36% (11) | 4.36% | 5.68% |  |
| c6__otc_W0__R100 | issuer_2 [share 20%, all records] | 4.31 | 20.0 | 3.64 | 1.89% | 9.87% | 10.20% | 0.00%, 0.00%, 18.18% (11) | 7.60% | 3.15% | badly miscalibrated |
| c6__otc_W0__R100 | issuer_2 [share 20%, its own devices] | 4.30 | 19.8 | 3.58 | 10.00% | 52.17% | 53.91% | 0.00%, 0.00%, 0.00% (12) | 4.86% | 7.11% |  |
| c6__otc_W0__R100 | issuer_2 [share 20%, other issuers' devices] | 4.33 | 20.3 | 3.80 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 7.51% | 3.24% | badly miscalibrated |
| c6__otc_W0__R100 | issuer_2_with_observer [share 20%, all records] | 6.62 | 98.2 | 5.01 | 2.96% | 13.40% | 22.37% | 0.00%, 16.67%, 20.00% (10) | 1.21% | 2.07% |  |
| c6__otc_W0__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.74 | 107.6 | 5.35 | 3.48% | 11.30% | 15.65% | 3.57%, 6.43%, 7.14% (14) | 3.55% | 4.52% |  |
| c6__otc_W0__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.61 | 98.2 | 5.01 | 2.84% | 13.89% | 23.94% | 0.00%, 15.00%, 20.00% (10) | 1.66% | 2.18% |  |
| c6__otc_W0__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.61 | 97.9 | 5.00 | 3.37% | 13.65% | 22.20% | 0.00%, 18.18%, 25.00% (12) | 1.53% | 2.01% |  |
| c6__otc_W0__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.74 | 107.2 | 5.34 | 3.91% | 11.30% | 15.22% | 3.57%, 6.43%, 7.14% (14) | 2.98% | 4.11% |  |
| c6__otc_W0__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.61 | 97.8 | 5.00 | 3.25% | 14.20% | 23.83% | 0.00%, 17.42%, 20.00% (10) | 1.79% | 2.05% |  |
| c6__otc_W0__R100 | issuer_2_with_destination | 4.52 | 23.2 | 3.53 | 8.70% | 39.57% | 62.17% | 15.48%, 16.43%, 16.67% (12) | 3.88% | 7.12% |  |
| c6__otc_W1__R1 | observer | 5.58 | 48.0 | 4.60 | 0.77% | 9.54% | 24.48% | 0.73%, 1.31%, 1.46% (206) | 4.37% | 3.95% | badly miscalibrated |
| c6__otc_W1__R1 | first_hop | 5.57 | 47.8 | 4.60 | 0.71% | 9.68% | 24.54% | 0.67%, 1.18%, 1.31% (4120) | 4.26% | 0.91% | badly miscalibrated |
| c6__otc_W1__R1 | destination | 5.52 | 45.9 | 4.71 | 1.80% | 12.37% | 25.26% | 1.76%, 2.29%, 2.43% (206) | 2.34% | 3.81% |  |
| c6__otc_W1__R1 | destination_keyed | 3.76 | 13.7 | 3.11 | 6.96% | 46.91% | 86.08% | 6.91%, 7.59%, 7.77% (206) | 6.59% | 6.46% | badly miscalibrated |
| c6__otc_W1__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (206) | 0.00% | 0.00% |  |
| c6__otc_W1__R1 | issuer_0 [share 50%, all records] | 4.98 | 31.6 | 3.41 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 9.46% | 6.18% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_0 [share 50%, other issuers' devices] | 4.98 | 31.6 | 3.41 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 9.46% | 6.18% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_0_with_observer [share 50%, all records] | 5.56 | 47.6 | 4.49 | 0.52% | 8.76% | 22.68% | 0.49%, 0.87%, 0.97% (206) | 4.50% | 4.30% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.56 | 47.6 | 4.49 | 0.52% | 8.76% | 22.68% | 0.49%, 0.87%, 0.97% (206) | 4.50% | 4.30% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.56 | 47.4 | 4.48 | 0.26% | 8.76% | 22.68% | 0.24%, 0.44%, 0.49% (206) | 4.37% | 4.30% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.56 | 47.4 | 4.48 | 0.26% | 8.76% | 22.68% | 0.24%, 0.44%, 0.49% (206) | 4.37% | 4.30% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_1 [share 30%, all records] | 4.78 | 27.5 | 3.70 | 0.52% | 5.41% | 85.82% | 0.55%, 0.99%, 1.10% (182) | 7.29% | 5.16% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_1 [share 30%, its own devices] | 4.78 | 27.5 | 3.70 | 0.52% | 5.41% | 85.82% | 0.55%, 0.99%, 1.10% (182) | 7.29% | 5.16% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_1_with_observer [share 30%, all records] | 5.57 | 47.7 | 4.51 | 2.06% | 13.40% | 25.00% | 2.04%, 2.35%, 2.43% (206) | 2.90% | 3.86% |  |
| c6__otc_W1__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.57 | 47.7 | 4.51 | 2.06% | 13.40% | 25.00% | 2.04%, 2.35%, 2.43% (206) | 2.90% | 3.86% |  |
| c6__otc_W1__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.56 | 47.6 | 4.51 | 2.06% | 13.40% | 25.00% | 2.04%, 2.35%, 2.43% (206) | 2.91% | 4.22% |  |
| c6__otc_W1__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.56 | 47.6 | 4.51 | 2.06% | 13.40% | 25.00% | 2.04%, 2.35%, 2.43% (206) | 2.91% | 4.22% |  |
| c6__otc_W1__R1 | issuer_1_with_destination | 3.75 | 13.6 | 3.02 | 7.47% | 47.42% | 86.34% | 7.55%, 8.54%, 8.79% (182) | 5.22% | 6.77% |  |
| c6__otc_W1__R1 | issuer_2 [share 20%, all records] | 4.01 | 16.2 | 2.72 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 15.25% | 7.47% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_2 [share 20%, other issuers' devices] | 4.01 | 16.2 | 2.72 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (206) | 15.25% | 7.47% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_2_with_observer [share 20%, all records] | 5.57 | 47.8 | 4.54 | 0.77% | 7.99% | 23.71% | 0.76%, 0.93%, 0.97% (206) | 4.07% | 3.99% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.57 | 47.8 | 4.54 | 0.77% | 7.99% | 23.71% | 0.76%, 0.93%, 0.97% (206) | 4.07% | 3.99% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.57 | 47.6 | 4.53 | 0.77% | 8.25% | 23.45% | 0.76%, 0.93%, 0.97% (206) | 4.08% | 4.02% | badly miscalibrated |
| c6__otc_W1__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.57 | 47.6 | 4.53 | 0.77% | 8.25% | 23.45% | 0.76%, 0.93%, 0.97% (206) | 4.08% | 4.02% | badly miscalibrated |
| c6__otc_W1__R100 | observer | 6.14 | 70.8 | 4.20 | 7.16% | 18.14% | 30.79% | 0.00%, 9.81%, 82.43% (74) | 2.15% | 2.69% |  |
| c6__otc_W1__R100 | first_hop | 6.14 | 70.7 | 4.20 | 7.22% | 18.19% | 30.77% | 0.00%, 0.00%, 83.31% (1480) | 2.08% | 0.56% | badly miscalibrated |
| c6__otc_W1__R100 | destination | 6.05 | 66.5 | 4.16 | 7.24% | 19.44% | 30.41% | 0.00%, 9.38%, 82.43% (74) | 2.56% | 2.50% | badly miscalibrated |
| c6__otc_W1__R100 | destination_keyed | 4.57 | 25.0 | 3.08 | 13.87% | 38.19% | 58.08% | 0.00%, 31.41%, 87.84% (74) | 3.72% | 3.55% | badly miscalibrated |
| c6__otc_W1__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (15) | 0.00% | 0.00% |  |
| c6__otc_W1__R100 | issuer_0 [share 50%, all records] | 5.00 | 31.9 | 3.25 | 5.49% | 13.03% | 25.38% | 0.00%, 0.00%, 95.95% (74) | 6.01% | 3.36% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_0 [share 50%, its own devices] | 4.99 | 31.9 | 3.25 | 10.45% | 24.82% | 48.33% | 0.00%, 0.00%, 95.95% (74) | 7.90% | 4.62% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_0 [share 50%, other issuers' devices] | 5.14 | 35.3 | 3.61 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (24) | 8.37% | 4.57% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_0_with_observer [share 50%, all records] | 6.12 | 69.9 | 4.17 | 7.39% | 18.75% | 30.64% | 0.00%, 13.94%, 74.32% (74) | 3.22% | 2.45% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.12 | 69.7 | 4.16 | 10.45% | 22.79% | 32.80% | 0.00%, 19.54%, 74.32% (74) | 5.49% | 3.43% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.13 | 70.1 | 4.19 | 4.01% | 14.29% | 28.25% | 0.00%, 9.43%, 44.19% (43) | 3.62% | 3.82% |  |
| c6__otc_W1__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.12 | 69.7 | 4.16 | 7.39% | 18.83% | 31.10% | 0.00%, 13.94%, 75.68% (74) | 2.02% | 2.58% |  |
| c6__otc_W1__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.11 | 69.5 | 4.15 | 10.45% | 23.22% | 32.95% | 0.00%, 17.90%, 75.68% (74) | 5.12% | 3.55% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.12 | 70.0 | 4.18 | 4.01% | 13.96% | 29.05% | 0.00%, 9.43%, 44.19% (43) | 4.58% | 3.48% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_0_with_destination | 5.09 | 34.2 | 3.58 | 12.34% | 28.88% | 46.88% | 0.00%, 22.32%, 82.43% (74) | 6.39% | 3.73% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_1 [share 30%, all records] | 4.55 | 23.5 | 4.45 | 0.30% | 10.37% | 16.01% | 0.00%, 0.00%, 6.67% (15) | 4.27% | 2.27% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_1 [share 30%, its own devices] | 4.55 | 23.5 | 4.45 | 1.31% | 44.44% | 68.63% | 0.00%, 5.78%, 6.67% (15) | 3.27% | 4.76% |  |
| c6__otc_W1__R100 | issuer_1 [share 30%, other issuers' devices] | 4.49 | 22.5 | 3.59 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 8.41% | 3.45% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_1_with_observer [share 30%, all records] | 6.13 | 70.1 | 4.18 | 7.16% | 18.37% | 30.56% | 0.00%, 8.69%, 78.38% (74) | 1.92% | 2.51% |  |
| c6__otc_W1__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.28 | 78.8 | 4.57 | 2.29% | 12.09% | 25.82% | 0.00%, 9.71%, 26.32% (19) | 4.10% | 4.88% |  |
| c6__otc_W1__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.13 | 70.1 | 4.17 | 8.65% | 20.28% | 32.01% | 0.00%, 9.10%, 78.38% (74) | 3.26% | 2.67% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.12 | 70.0 | 4.17 | 7.47% | 18.52% | 30.72% | 0.00%, 8.69%, 83.78% (74) | 2.13% | 2.54% |  |
| c6__otc_W1__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.28 | 78.6 | 4.56 | 2.29% | 12.09% | 25.82% | 0.00%, 9.71%, 26.32% (19) | 4.10% | 4.90% |  |
| c6__otc_W1__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.12 | 70.0 | 4.17 | 9.05% | 20.48% | 32.21% | 0.00%, 9.10%, 83.78% (74) | 3.44% | 2.89% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_1_with_destination | 4.44 | 22.0 | 3.21 | 12.09% | 41.50% | 66.34% | 22.22%, 32.26%, 35.00% (20) | 4.80% | 7.13% |  |
| c6__otc_W1__R100 | issuer_2 [share 20%, all records] | 3.71 | 13.3 | 1.80 | 5.72% | 16.31% | 19.59% | 0.00%, 0.00%, 100.00% (43) | 24.03% | 5.21% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_2 [share 20%, its own devices] | 3.70 | 13.1 | 1.78 | 23.66% | 67.51% | 81.07% | 0.00%, 100.00%, 100.00% (43) | 11.85% | 9.58% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_2 [share 20%, other issuers' devices] | 4.25 | 19.0 | 2.94 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 13.19% | 4.28% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_2_with_observer [share 20%, all records] | 6.13 | 70.1 | 4.16 | 6.71% | 18.52% | 30.26% | 0.00%, 7.85%, 78.38% (74) | 2.55% | 2.56% |  |
| c6__otc_W1__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.13 | 70.5 | 4.18 | 6.62% | 21.77% | 34.07% | 0.00%, 21.06%, 32.56% (43) | 4.52% | 5.52% |  |
| c6__otc_W1__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.12 | 70.0 | 4.15 | 6.73% | 17.49% | 29.05% | 0.00%, 6.15%, 78.38% (74) | 2.98% | 2.95% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.12 | 70.0 | 4.16 | 6.94% | 18.37% | 30.41% | 0.00%, 8.69%, 82.43% (74) | 2.47% | 2.55% |  |
| c6__otc_W1__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.13 | 70.3 | 4.17 | 6.94% | 20.50% | 35.33% | 0.00%, 21.06%, 32.56% (43) | 5.16% | 5.18% |  |
| c6__otc_W1__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.12 | 69.9 | 4.15 | 6.93% | 17.69% | 28.84% | 0.00%, 6.15%, 82.43% (74) | 3.72% | 2.80% | badly miscalibrated |
| c6__otc_W1__R100 | issuer_2_with_destination | 3.94 | 15.6 | 2.57 | 17.35% | 55.52% | 77.92% | 14.29%, 33.53%, 76.74% (43) | 3.16% | 8.03% |  |
| c6__otc_W2__R1 | observer | 5.29 | 39.7 | 3.71 | 7.92% | 26.23% | 39.34% | 7.90%, 8.89%, 9.14% (186) | 7.02% | 5.85% | badly miscalibrated |
| c6__otc_W2__R1 | first_hop | 5.29 | 39.6 | 3.71 | 7.98% | 26.11% | 39.63% | 7.95%, 9.16%, 9.46% (3720) | 6.86% | 1.17% | badly miscalibrated |
| c6__otc_W2__R1 | destination | 5.42 | 43.1 | 4.28 | 7.38% | 27.60% | 37.43% | 7.33%, 9.64%, 10.22% (186) | 5.35% | 4.97% | badly miscalibrated |
| c6__otc_W2__R1 | destination_keyed | 3.68 | 13.0 | 2.74 | 19.67% | 53.28% | 84.70% | 19.70%, 20.83%, 21.11% (180) | 8.83% | 7.07% | badly miscalibrated |
| c6__otc_W2__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (180) | 0.00% | 0.00% |  |
| c6__otc_W2__R1 | issuer_0 [share 50%, all records] | 4.97 | 31.4 | 3.29 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 10.27% | 6.33% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_0 [share 50%, other issuers' devices] | 4.97 | 31.4 | 3.29 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 10.27% | 6.33% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_0_with_observer [share 50%, all records] | 5.44 | 43.4 | 3.96 | 6.56% | 24.32% | 39.07% | 6.52%, 8.19%, 8.60% (186) | 5.49% | 5.50% |  |
| c6__otc_W2__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.44 | 43.4 | 3.96 | 6.56% | 24.32% | 39.07% | 6.52%, 8.19%, 8.60% (186) | 5.49% | 5.50% |  |
| c6__otc_W2__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.43 | 43.3 | 3.96 | 6.83% | 24.32% | 38.52% | 6.79%, 8.67%, 9.14% (186) | 6.84% | 5.55% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.43 | 43.3 | 3.96 | 6.83% | 24.32% | 38.52% | 6.79%, 8.67%, 9.14% (186) | 6.84% | 5.55% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_1 [share 30%, all records] | 4.63 | 25.5 | 3.64 | 0.82% | 7.10% | 52.19% | 0.83%, 1.50%, 1.67% (180) | 9.14% | 6.29% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_1 [share 30%, its own devices] | 4.63 | 25.5 | 3.64 | 0.82% | 7.10% | 52.19% | 0.83%, 1.50%, 1.67% (180) | 9.14% | 6.29% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_1_with_observer [share 30%, all records] | 5.25 | 38.8 | 3.56 | 11.75% | 27.60% | 40.71% | 11.68%, 15.24%, 16.13% (186) | 6.92% | 5.79% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.25 | 38.8 | 3.56 | 11.75% | 27.60% | 40.71% | 11.68%, 15.24%, 16.13% (186) | 6.92% | 5.79% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.25 | 38.7 | 3.57 | 12.02% | 27.05% | 40.16% | 11.94%, 15.72%, 16.67% (186) | 6.64% | 5.91% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.25 | 38.7 | 3.57 | 12.02% | 27.05% | 40.16% | 11.94%, 15.72%, 16.67% (186) | 6.64% | 5.91% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_1_with_destination | 3.63 | 12.6 | 2.57 | 20.49% | 53.28% | 84.15% | 20.51%, 21.44%, 21.67% (180) | 7.73% | 7.67% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_2 [share 20%, all records] | 4.08 | 17.2 | 2.87 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 14.51% | 6.89% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_2 [share 20%, other issuers' devices] | 4.08 | 17.2 | 2.87 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 14.51% | 6.89% | badly miscalibrated |
| c6__otc_W2__R1 | issuer_2_with_observer [share 20%, all records] | 5.44 | 43.7 | 4.00 | 6.01% | 24.86% | 38.52% | 5.96%, 8.50%, 9.14% (186) | 3.41% | 5.01% |  |
| c6__otc_W2__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.44 | 43.7 | 4.00 | 6.01% | 24.86% | 38.52% | 5.96%, 8.50%, 9.14% (186) | 3.41% | 5.01% |  |
| c6__otc_W2__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.44 | 43.6 | 4.00 | 6.56% | 24.59% | 38.25% | 6.51%, 9.04%, 9.68% (186) | 4.03% | 4.89% |  |
| c6__otc_W2__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.44 | 43.6 | 4.00 | 6.56% | 24.59% | 38.25% | 6.51%, 9.04%, 9.68% (186) | 4.03% | 4.89% |  |
| c6__otc_W2__R100 | observer | 6.11 | 69.3 | 4.03 | 6.63% | 19.25% | 32.51% | 0.00%, 15.24%, 70.97% (31) | 2.44% | 2.79% |  |
| c6__otc_W2__R100 | first_hop | 6.10 | 69.1 | 4.02 | 6.61% | 19.38% | 32.47% | 0.00%, 0.00%, 68.71% (620) | 2.14% | 0.63% | badly miscalibrated |
| c6__otc_W2__R100 | destination | 6.01 | 64.9 | 4.00 | 5.90% | 19.90% | 31.86% | 0.00%, 16.67%, 61.29% (31) | 2.25% | 3.02% |  |
| c6__otc_W2__R100 | destination_keyed | 4.59 | 25.8 | 3.01 | 11.71% | 37.67% | 60.52% | 5.88%, 31.71%, 64.52% (31) | 2.96% | 4.08% |  |
| c6__otc_W2__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (13) | 0.00% | 0.00% |  |
| c6__otc_W2__R100 | issuer_0 [share 50%, all records] | 5.28 | 39.2 | 3.55 | 4.50% | 13.92% | 33.25% | 0.00%, 0.00%, 100.00% (55) | 5.11% | 3.27% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_0 [share 50%, its own devices] | 5.28 | 39.1 | 3.55 | 7.81% | 24.15% | 57.67% | 0.00%, 0.00%, 100.00% (55) | 6.55% | 4.35% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_0 [share 50%, other issuers' devices] | 5.29 | 39.3 | 3.55 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (36) | 8.68% | 4.65% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_0_with_observer [share 50%, all records] | 6.07 | 67.7 | 3.93 | 6.39% | 19.25% | 31.78% | 0.00%, 13.28%, 77.42% (31) | 1.59% | 2.91% |  |
| c6__otc_W2__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.07 | 67.4 | 3.92 | 8.95% | 22.30% | 35.09% | 0.00%, 13.16%, 77.42% (31) | 3.17% | 3.49% |  |
| c6__otc_W2__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.26 | 77.5 | 4.40 | 2.90% | 15.09% | 27.27% | 0.00%, 9.92%, 45.00% (20) | 4.70% | 3.81% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.07 | 67.5 | 3.93 | 6.06% | 19.33% | 31.78% | 0.00%, 13.28%, 70.97% (31) | 1.90% | 2.82% |  |
| c6__otc_W2__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.06 | 67.3 | 3.92 | 8.66% | 22.44% | 34.94% | 0.00%, 13.16%, 70.97% (31) | 3.14% | 3.76% |  |
| c6__otc_W2__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.26 | 77.4 | 4.41 | 2.51% | 15.09% | 27.47% | 0.00%, 9.92%, 35.00% (20) | 4.55% | 3.72% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_0_with_destination | 5.11 | 35.0 | 3.47 | 9.94% | 32.53% | 52.41% | 0.00%, 19.71%, 67.74% (31) | 4.42% | 4.23% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_1 [share 30%, all records] | 4.30 | 20.0 | 2.97 | 1.56% | 9.01% | 11.22% | 0.00%, 0.00%, 95.00% (20) | 12.68% | 3.79% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_1 [share 30%, its own devices] | 4.33 | 20.3 | 3.05 | 8.02% | 46.41% | 57.81% | 0.00%, 47.50%, 95.00% (20) | 11.51% | 8.11% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_1 [share 30%, other issuers' devices] | 4.35 | 20.4 | 3.06 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (13) | 12.05% | 4.15% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_1_with_observer [share 30%, all records] | 6.10 | 68.9 | 4.00 | 6.22% | 19.08% | 32.10% | 0.00%, 13.46%, 70.97% (31) | 2.65% | 2.61% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.38 | 85.0 | 4.86 | 5.91% | 11.81% | 19.41% | 0.00%, 34.52%, 50.00% (20) | 7.66% | 4.82% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.10 | 68.8 | 4.00 | 6.30% | 20.83% | 35.16% | 0.00%, 6.67%, 70.97% (31) | 3.00% | 3.37% |  |
| c6__otc_W2__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.10 | 68.7 | 4.00 | 6.14% | 19.00% | 32.19% | 0.00%, 13.46%, 64.52% (31) | 2.33% | 2.72% |  |
| c6__otc_W2__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.38 | 84.9 | 4.87 | 5.91% | 11.81% | 19.41% | 0.00%, 34.52%, 50.00% (20) | 7.67% | 4.98% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.09 | 68.7 | 4.00 | 6.20% | 20.73% | 35.26% | 0.00%, 8.33%, 64.52% (31) | 2.89% | 3.20% |  |
| c6__otc_W2__R100 | issuer_1_with_destination | 4.42 | 21.9 | 3.28 | 11.39% | 36.71% | 62.87% | 22.50%, 48.81%, 50.00% (20) | 5.64% | 7.66% |  |
| c6__otc_W2__R100 | issuer_2 [share 20%, all records] | 4.01 | 16.6 | 2.78 | 4.26% | 14.00% | 18.67% | 0.00%, 0.00%, 100.00% (36) | 12.84% | 4.06% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_2 [share 20%, its own devices] | 4.03 | 16.9 | 2.85 | 18.57% | 61.07% | 81.43% | 0.00%, 28.95%, 100.00% (36) | 4.56% | 7.94% |  |
| c6__otc_W2__R100 | issuer_2 [share 20%, other issuers' devices] | 4.00 | 16.5 | 2.76 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (13) | 16.89% | 5.32% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_2_with_observer [share 20%, all records] | 6.10 | 68.7 | 4.00 | 6.47% | 19.49% | 32.43% | 0.00%, 15.24%, 70.97% (31) | 2.58% | 2.74% |  |
| c6__otc_W2__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.09 | 68.7 | 4.02 | 5.36% | 23.21% | 39.29% | 6.48%, 17.67%, 26.67% (15) | 5.74% | 5.40% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.10 | 68.7 | 4.00 | 6.80% | 18.38% | 30.39% | 0.00%, 16.59%, 70.97% (31) | 3.22% | 3.01% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.09 | 68.6 | 4.01 | 6.31% | 19.41% | 32.43% | 0.00%, 15.24%, 64.52% (31) | 1.99% | 2.62% |  |
| c6__otc_W2__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.09 | 68.5 | 4.02 | 5.36% | 23.21% | 39.29% | 6.48%, 17.67%, 26.67% (15) | 6.06% | 5.69% | badly miscalibrated |
| c6__otc_W2__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.09 | 68.6 | 4.00 | 6.59% | 18.28% | 30.39% | 0.00%, 16.59%, 64.52% (31) | 2.34% | 3.20% |  |
| c6__otc_W2__R100 | issuer_2_with_destination | 4.01 | 16.3 | 2.81 | 14.64% | 51.79% | 78.21% | 15.04%, 30.00%, 50.00% (36) | 4.54% | 8.54% |  |
| c6__otc_Wmis__R1 | observer | 5.43 | 43.7 | 3.82 | 20.49% | 32.79% | 43.99% | 20.44%, 23.01%, 23.66% (186) | 13.26% | 5.89% | badly miscalibrated |
| c6__otc_Wmis__R1 | first_hop | 5.42 | 43.6 | 3.82 | 20.15% | 32.68% | 43.99% | 20.09%, 22.81%, 23.49% (3720) | 12.80% | 1.15% | badly miscalibrated |
| c6__otc_Wmis__R1 | destination | 5.31 | 40.3 | 3.70 | 17.76% | 31.42% | 41.80% | 17.72%, 19.46%, 19.89% (186) | 9.80% | 6.53% | badly miscalibrated |
| c6__otc_Wmis__R1 | destination_keyed | 3.81 | 14.3 | 2.67 | 25.14% | 53.83% | 77.87% | 25.09%, 27.38%, 27.96% (186) | 12.95% | 7.39% | badly miscalibrated |
| c6__otc_Wmis__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (180) | 0.00% | 0.00% |  |
| c6__otc_Wmis__R1 | issuer_0 [share 50%, all records] | 5.55 | 46.7 | 4.47 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 4.75% | 4.78% |  |
| c6__otc_Wmis__R1 | issuer_0 [share 50%, other issuers' devices] | 5.55 | 46.7 | 4.47 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 4.75% | 4.78% |  |
| c6__otc_Wmis__R1 | issuer_0_with_observer [share 50%, all records] | 5.57 | 47.8 | 3.87 | 13.66% | 31.15% | 43.72% | 13.63%, 15.20%, 15.59% (186) | 7.60% | 5.27% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.57 | 47.8 | 3.87 | 13.66% | 31.15% | 43.72% | 13.63%, 15.20%, 15.59% (186) | 7.60% | 5.27% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.57 | 47.7 | 3.86 | 13.93% | 30.87% | 42.62% | 13.91%, 15.25%, 15.59% (186) | 7.31% | 5.48% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.57 | 47.7 | 3.86 | 13.93% | 30.87% | 42.62% | 13.91%, 15.25%, 15.59% (186) | 7.31% | 5.48% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_1 [share 30%, all records] | 4.88 | 29.5 | 4.10 | 7.65% | 16.67% | 16.67% | 7.63%, 8.84%, 9.14% (186) | 5.90% | 5.38% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_1 [share 30%, its own devices] | 4.88 | 29.5 | 4.10 | 7.65% | 16.67% | 16.67% | 7.63%, 8.84%, 9.14% (186) | 5.90% | 5.38% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_1_with_observer [share 30%, all records] | 5.27 | 40.4 | 3.38 | 17.21% | 33.88% | 43.99% | 17.15%, 20.20%, 20.97% (186) | 8.02% | 6.16% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.27 | 40.4 | 3.38 | 17.21% | 33.88% | 43.99% | 17.15%, 20.20%, 20.97% (186) | 8.02% | 6.16% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.27 | 40.3 | 3.38 | 16.67% | 34.43% | 43.44% | 16.59%, 20.09%, 20.97% (186) | 7.74% | 6.12% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.27 | 40.3 | 3.38 | 16.67% | 34.43% | 43.44% | 16.59%, 20.09%, 20.97% (186) | 7.74% | 6.12% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_1_with_destination | 3.83 | 14.5 | 2.60 | 21.31% | 54.10% | 77.60% | 21.25%, 24.04%, 24.73% (186) | 6.10% | 7.86% |  |
| c6__otc_Wmis__R1 | issuer_2 [share 20%, all records] | 4.42 | 21.5 | 3.69 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 8.25% | 5.68% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_2 [share 20%, other issuers' devices] | 4.42 | 21.5 | 3.69 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (180) | 8.25% | 5.68% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_2_with_observer [share 20%, all records] | 5.37 | 42.3 | 3.63 | 18.03% | 32.24% | 43.72% | 17.97%, 20.80%, 21.51% (186) | 9.86% | 5.87% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.37 | 42.3 | 3.63 | 18.03% | 32.24% | 43.72% | 17.97%, 20.80%, 21.51% (186) | 9.86% | 5.87% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.36 | 42.2 | 3.62 | 18.03% | 32.51% | 43.17% | 17.97%, 20.80%, 21.51% (186) | 10.42% | 6.17% | badly miscalibrated |
| c6__otc_Wmis__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.36 | 42.2 | 3.62 | 18.03% | 32.51% | 43.17% | 17.97%, 20.80%, 21.51% (186) | 10.42% | 6.17% | badly miscalibrated |
| c6__otc_Wmis__R100 | observer | 5.77 | 55.3 | 3.32 | 9.58% | 25.47% | 38.17% | 0.00%, 22.42%, 77.42% (31) | 2.08% | 3.37% |  |
| c6__otc_Wmis__R100 | first_hop | 5.76 | 55.1 | 3.32 | 9.56% | 25.58% | 38.20% | 0.00%, 1.85%, 73.87% (620) | 2.16% | 0.78% |  |
| c6__otc_Wmis__R100 | destination | 6.26 | 76.8 | 4.31 | 8.60% | 24.49% | 37.10% | 0.00%, 17.89%, 64.52% (31) | 3.39% | 2.47% | badly miscalibrated |
| c6__otc_Wmis__R100 | destination_keyed | 4.84 | 30.6 | 3.29 | 16.38% | 41.85% | 61.51% | 8.33%, 43.35%, 64.52% (31) | 5.31% | 3.63% | badly miscalibrated |
| c6__otc_Wmis__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (12) | 0.00% | 0.00% |  |
| c6__otc_Wmis__R100 | issuer_0 [share 50%, all records] | 4.53 | 28.2 | 2.48 | 7.86% | 17.77% | 41.85% | 0.00%, 5.08%, 85.94% (64) | 21.43% | 4.24% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_0 [share 50%, its own devices] | 4.52 | 28.0 | 2.46 | 13.64% | 30.82% | 72.59% | 0.00%, 22.73%, 100.00% (55) | 18.71% | 5.43% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_0 [share 50%, other issuers' devices] | 5.51 | 45.6 | 3.98 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (12) | 6.83% | 4.34% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_0_with_observer [share 50%, all records] | 6.33 | 80.9 | 4.22 | 8.52% | 24.16% | 37.92% | 0.00%, 18.91%, 77.42% (31) | 2.82% | 2.49% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.02 | 66.9 | 3.70 | 11.08% | 27.27% | 41.62% | 0.00%, 22.52%, 77.42% (31) | 5.94% | 4.05% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.33 | 80.8 | 4.22 | 5.03% | 19.92% | 32.88% | 0.00%, 17.50%, 50.00% (20) | 3.18% | 4.21% |  |
| c6__otc_Wmis__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.33 | 80.7 | 4.22 | 8.44% | 24.57% | 37.84% | 0.00%, 18.91%, 77.42% (31) | 2.77% | 2.64% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.02 | 66.8 | 3.70 | 10.94% | 27.70% | 41.48% | 0.00%, 22.52%, 77.42% (31) | 5.75% | 4.13% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.33 | 80.6 | 4.22 | 5.03% | 20.31% | 32.88% | 0.00%, 17.50%, 50.00% (20) | 3.25% | 4.08% |  |
| c6__otc_Wmis__R100 | issuer_0_with_destination | 5.20 | 37.0 | 3.39 | 12.36% | 35.23% | 53.41% | 0.00%, 33.28%, 67.74% (31) | 3.51% | 4.40% |  |
| c6__otc_Wmis__R100 | issuer_1 [share 30%, all records] | 3.57 | 13.6 | 1.98 | 2.54% | 10.48% | 11.71% | 0.00%, 0.00%, 75.00% (12) | 29.61% | 4.68% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_1 [share 30%, its own devices] | 3.47 | 12.8 | 1.86 | 13.08% | 54.01% | 60.34% | 0.00%, 85.00%, 100.00% (20) | 22.37% | 11.59% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_1 [share 30%, other issuers' devices] | 4.29 | 19.7 | 3.11 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (15) | 12.17% | 4.35% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_1_with_observer [share 30%, all records] | 6.36 | 82.5 | 4.34 | 9.25% | 24.90% | 38.08% | 0.00%, 23.64%, 70.97% (31) | 4.19% | 2.51% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.52 | 92.4 | 4.76 | 8.44% | 15.61% | 22.78% | 5.88%, 42.86%, 50.00% (20) | 7.78% | 4.90% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 5.76 | 54.9 | 3.31 | 9.45% | 27.13% | 41.77% | 0.00%, 23.41%, 70.97% (31) | 4.25% | 3.90% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.04 | 68.2 | 3.81 | 8.93% | 24.98% | 38.33% | 0.00%, 23.64%, 64.52% (31) | 2.63% | 2.79% |  |
| c6__otc_Wmis__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.52 | 92.2 | 4.77 | 8.44% | 15.61% | 22.78% | 5.88%, 42.86%, 50.00% (20) | 8.41% | 5.09% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 5.75 | 54.8 | 3.32 | 9.04% | 27.24% | 42.07% | 0.00%, 23.41%, 64.52% (31) | 3.09% | 3.81% |  |
| c6__otc_Wmis__R100 | issuer_1_with_destination | 4.59 | 24.4 | 3.32 | 17.30% | 37.97% | 61.60% | 30.00%, 52.86%, 57.14% (21) | 7.02% | 8.03% |  |
| c6__otc_Wmis__R100 | issuer_2 [share 20%, all records] | 4.10 | 17.2 | 2.30 | 5.16% | 15.72% | 18.67% | 0.00%, 0.00%, 100.00% (36) | 18.37% | 4.68% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2 [share 20%, its own devices] | 4.12 | 17.4 | 2.36 | 22.50% | 68.57% | 81.43% | 0.00%, 95.26%, 100.00% (36) | 5.53% | 9.88% |  |
| c6__otc_Wmis__R100 | issuer_2 [share 20%, other issuers' devices] | 4.42 | 21.5 | 3.03 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (10) | 12.88% | 4.40% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2_with_observer [share 20%, all records] | 6.36 | 82.1 | 4.32 | 9.25% | 25.72% | 37.92% | 0.00%, 24.30%, 77.42% (31) | 4.20% | 2.71% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.02 | 67.1 | 3.76 | 6.07% | 32.86% | 43.57% | 5.13%, 22.67%, 26.67% (15) | 8.57% | 6.70% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.36 | 82.1 | 4.32 | 10.20% | 23.59% | 36.24% | 0.00%, 27.83%, 77.42% (31) | 5.03% | 2.88% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.35 | 82.0 | 4.33 | 9.09% | 25.72% | 37.92% | 0.00%, 25.32%, 70.97% (31) | 4.09% | 2.58% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.02 | 67.0 | 3.77 | 6.43% | 32.14% | 43.21% | 5.13%, 25.17%, 26.67% (15) | 8.32% | 6.03% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.35 | 82.0 | 4.32 | 9.88% | 23.80% | 36.34% | 0.00%, 26.29%, 70.97% (31) | 4.73% | 2.88% | badly miscalibrated |
| c6__otc_Wmis__R100 | issuer_2_with_destination | 4.10 | 17.3 | 2.76 | 23.93% | 58.21% | 79.64% | 20.71%, 53.69%, 61.90% (21) | 10.18% | 8.64% | badly miscalibrated |
| c6__otc_chain100__R1 | observer | 5.63 | 49.7 | 4.22 | 4.75% | 20.43% | 37.77% | 4.79%, 7.50%, 8.17% (208) | 2.05% | 4.36% |  |
| c6__otc_chain100__R1 | first_hop | 5.63 | 49.6 | 4.21 | 4.70% | 20.57% | 37.77% | 4.74%, 7.33%, 7.98% (4160) | 1.81% | 0.92% |  |
| c6__otc_chain100__R1 | destination | 5.63 | 49.7 | 4.41 | 4.75% | 19.71% | 36.34% | 4.78%, 6.73%, 7.21% (208) | 3.64% | 4.67% |  |
| c6__otc_chain100__R1 | destination_keyed | 5.62 | 49.6 | 4.41 | 1.43% | 6.89% | 12.35% | 1.44%, 2.21%, 2.40% (208) | 1.15% | 1.75% |  |
| c6__otc_chain100__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (208) | 0.00% | 0.00% |  |
| c6__otc_chain100__R1 | issuer_0 [share 50%, all records] | 5.54 | 46.5 | 4.47 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (208) | 5.00% | 4.12% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_0 [share 50%, other issuers' devices] | 5.54 | 46.5 | 4.47 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (208) | 5.00% | 4.12% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_0_with_observer [share 50%, all records] | 5.70 | 52.3 | 4.19 | 3.56% | 20.19% | 38.24% | 3.60%, 6.10%, 6.73% (208) | 6.08% | 4.56% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.70 | 52.3 | 4.19 | 3.56% | 20.19% | 38.24% | 3.60%, 6.10%, 6.73% (208) | 6.08% | 4.56% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.69 | 52.1 | 4.19 | 3.80% | 20.19% | 38.00% | 3.83%, 6.15%, 6.73% (208) | 5.37% | 4.78% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.69 | 52.1 | 4.19 | 3.80% | 20.19% | 38.00% | 3.83%, 6.15%, 6.73% (208) | 5.37% | 4.78% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_1 [share 30%, all records] | 4.86 | 29.1 | 3.98 | 20.90% | 54.39% | 54.87% | 4.04%, 4.19%, 4.23% (213) | 4.46% | 5.12% |  |
| c6__otc_chain100__R1 | issuer_1 [share 30%, its own devices] | 4.85 | 29.0 | 3.97 | 23.16% | 54.74% | 55.09% | 4.56%, 5.39%, 5.59% (143) | 5.30% | 6.36% |  |
| c6__otc_chain100__R1 | issuer_1 [share 30%, other issuers' devices] | 4.93 | 30.5 | 4.40 | 16.18% | 53.68% | 54.41% | 2.99%, 4.23%, 4.55% (66) | 3.38% | 7.99% |  |
| c6__otc_chain100__R1 | issuer_1_with_observer [share 30%, all records] | 5.58 | 48.0 | 3.91 | 6.41% | 21.85% | 37.77% | 6.44%, 8.21%, 8.65% (208) | 3.56% | 4.75% |  |
| c6__otc_chain100__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.58 | 48.0 | 3.91 | 7.02% | 21.05% | 37.89% | 7.03%, 8.73%, 9.15% (142) | 3.66% | 5.87% |  |
| c6__otc_chain100__R1 | issuer_1_with_observer [share 30%, other issuers' devices] | 5.71 | 52.5 | 4.24 | 5.15% | 23.53% | 37.50% | 5.22%, 7.10%, 7.58% (66) | 6.81% | 8.06% |  |
| c6__otc_chain100__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.57 | 47.9 | 3.91 | 5.94% | 21.85% | 38.72% | 5.95%, 6.96%, 7.21% (208) | 1.77% | 4.80% |  |
| c6__otc_chain100__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.57 | 47.9 | 3.91 | 6.32% | 20.70% | 37.54% | 6.32%, 7.46%, 7.75% (142) | 2.43% | 5.98% |  |
| c6__otc_chain100__R1 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 5.70 | 52.4 | 4.23 | 5.15% | 24.26% | 41.18% | 5.17%, 5.88%, 6.06% (66) | 5.67% | 8.57% |  |
| c6__otc_chain100__R1 | issuer_1_with_destination | — | — | — | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (142) | 0.00% | 0.00% |  |
| c6__otc_chain100__R1 | issuer_2 [share 20%, all records] | 4.41 | 21.4 | 3.68 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (208) | 8.48% | 5.37% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_2 [share 20%, other issuers' devices] | 4.41 | 21.4 | 3.68 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (208) | 8.48% | 5.37% | badly miscalibrated |
| c6__otc_chain100__R1 | issuer_2_with_observer [share 20%, all records] | 5.60 | 48.8 | 4.03 | 3.09% | 19.24% | 37.53% | 3.12%, 5.24%, 5.77% (208) | 3.74% | 4.64% |  |
| c6__otc_chain100__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.60 | 48.8 | 4.03 | 3.09% | 19.24% | 37.53% | 3.12%, 5.24%, 5.77% (208) | 3.74% | 4.64% |  |
| c6__otc_chain100__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.60 | 48.7 | 4.03 | 3.09% | 19.95% | 37.29% | 3.11%, 4.85%, 5.29% (208) | 4.23% | 4.82% |  |
| c6__otc_chain100__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.60 | 48.7 | 4.03 | 3.09% | 19.95% | 37.29% | 3.11%, 4.85%, 5.29% (208) | 4.23% | 4.82% |  |
| c6__otc_chain100__R100 | observer | 6.61 | 98.0 | 5.10 | 2.45% | 12.58% | 21.81% | 0.00%, 10.00%, 25.00% (16) | 1.49% | 1.98% |  |
| c6__otc_chain100__R100 | first_hop | 6.61 | 97.7 | 5.09 | 2.59% | 12.45% | 21.70% | 0.00%, 6.35%, 42.86% (140) | 1.11% | 0.45% |  |
| c6__otc_chain100__R100 | destination | 6.49 | 90.1 | 4.98 | 3.59% | 13.64% | 23.12% | 0.00%, 16.67%, 31.25% (16) | 1.12% | 1.97% |  |
| c6__otc_chain100__R100 | destination_keyed | 3.10 | 40.4 | 2.35 | 2.37% | 5.39% | 8.25% | 0.00%, 11.25%, 42.86% (14) | 33.11% | 2.01% | badly miscalibrated |
| c6__otc_chain100__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (16) | 0.00% | 0.00% |  |
| c6__otc_chain100__R100 | issuer_0 [share 50%, all records] | 5.88 | 59.0 | 4.69 | 2.70% | 26.80% | 37.42% | 0.00%, 2.63%, 46.67% (15) | 2.53% | 2.21% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_0 [share 50%, its own devices] | 5.83 | 57.0 | 4.29 | 5.79% | 50.86% | 68.67% | 0.00%, 4.00%, 10.00% (10) | 2.72% | 4.29% |  |
| c6__otc_chain100__R100 | issuer_0 [share 50%, other issuers' devices] | 5.91 | 60.4 | 5.61 | 0.79% | 12.01% | 18.21% | 0.00%, 0.00%, 0.00% (11) | 1.69% | 2.07% |  |
| c6__otc_chain100__R100 | issuer_0_with_observer [share 50%, all records] | 6.57 | 95.3 | 4.72 | 3.27% | 12.09% | 21.08% | 0.00%, 15.19%, 35.71% (14) | 2.02% | 1.98% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.58 | 95.7 | 4.73 | 6.01% | 14.59% | 22.32% | 7.14%, 39.08%, 40.00% (10) | 3.27% | 3.40% |  |
| c6__otc_chain100__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.57 | 95.1 | 4.72 | 1.58% | 10.55% | 20.32% | 0.00%, 8.33%, 25.00% (16) | 3.02% | 2.71% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.57 | 95.0 | 4.72 | 3.10% | 12.17% | 21.00% | 0.00%, 15.19%, 31.25% (16) | 1.92% | 2.08% |  |
| c6__otc_chain100__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.57 | 95.4 | 4.73 | 5.36% | 14.81% | 22.53% | 7.14%, 29.85%, 40.00% (10) | 2.95% | 3.33% |  |
| c6__otc_chain100__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.56 | 94.8 | 4.71 | 1.72% | 10.55% | 20.05% | 0.00%, 8.33%, 31.25% (16) | 2.90% | 2.84% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_0_with_destination | 0.39 | 1.4 | 0.27 | 2.36% | 2.79% | 2.79% | 0.00%, 18.46%, 46.15% (13) | 59.35% | 3.36% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_1 [share 30%, all records] | 5.41 | 42.4 | 4.33 | 0.98% | 19.93% | 21.00% | 0.00%, 0.00%, 6.25% (16) | 4.48% | 2.50% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_1 [share 30%, its own devices] | 5.32 | 40.0 | 3.75 | 5.94% | 81.68% | 85.64% | — | 4.47% | 7.97% |  |
| c6__otc_chain100__R100 | issuer_1 [share 30%, other issuers' devices] | 5.44 | 43.4 | 5.16 | 0.00% | 7.73% | 8.22% | 0.00%, 0.00%, 0.00% (12) | 2.83% | 1.96% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_1_with_observer [share 30%, all records] | 6.58 | 95.6 | 4.75 | 1.72% | 11.68% | 21.41% | 0.00%, 9.17%, 16.67% (18) | 2.21% | 2.29% |  |
| c6__otc_chain100__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.58 | 95.8 | 4.74 | 4.95% | 14.85% | 24.75% | — | 2.54% | 5.29% |  |
| c6__otc_chain100__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.58 | 95.6 | 4.75 | 1.08% | 11.06% | 20.74% | 0.00%, 7.69%, 21.43% (14) | 2.84% | 2.44% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.57 | 95.3 | 4.74 | 1.88% | 11.85% | 21.49% | 0.00%, 10.00%, 20.00% (10) | 2.06% | 2.16% |  |
| c6__otc_chain100__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.57 | 95.5 | 4.73 | 5.94% | 15.84% | 24.75% | — | 2.38% | 5.26% |  |
| c6__otc_chain100__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.57 | 95.3 | 4.75 | 1.08% | 11.06% | 20.84% | 0.00%, 7.69%, 21.43% (14) | 2.86% | 2.39% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_1_with_destination | 0.34 | 1.3 | 0.19 | 0.99% | 0.99% | 0.99% | — | 33.84% | 3.58% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_2 [share 20%, all records] | 4.78 | 27.9 | 3.65 | 3.84% | 15.28% | 15.44% | 0.00%, 5.76%, 16.67% (12) | 8.67% | 3.37% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_2 [share 20%, its own devices] | 4.80 | 28.2 | 3.59 | 19.64% | 70.24% | 70.83% | — | 5.42% | 8.95% |  |
| c6__otc_chain100__R100 | issuer_2 [share 20%, other issuers' devices] | 4.89 | 29.8 | 4.81 | 1.33% | 6.53% | 6.63% | 0.00%, 0.00%, 9.09% (11) | 3.40% | 2.10% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_2_with_observer [share 20%, all records] | 6.59 | 96.5 | 4.87 | 3.02% | 12.75% | 21.81% | 0.00%, 13.81%, 25.00% (16) | 1.27% | 1.92% |  |
| c6__otc_chain100__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.58 | 95.9 | 4.83 | 7.74% | 17.26% | 27.98% | — | 7.07% | 5.54% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.59 | 96.6 | 4.87 | 2.27% | 12.03% | 20.83% | 0.00%, 8.48%, 25.00% (16) | 1.98% | 2.37% |  |
| c6__otc_chain100__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.59 | 96.2 | 4.86 | 2.94% | 12.58% | 21.57% | 0.00%, 12.55%, 25.00% (16) | 1.35% | 2.08% |  |
| c6__otc_chain100__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.71 | 105.2 | 5.21 | 7.14% | 16.67% | 26.79% | — | 5.83% | 5.15% | badly miscalibrated |
| c6__otc_chain100__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.59 | 96.3 | 4.87 | 2.27% | 11.93% | 20.74% | 0.00%, 8.48%, 25.00% (16) | 2.02% | 2.32% |  |
| c6__otc_chain100__R100 | issuer_2_with_destination | 0.03 | 1.0 | 0.01 | 0.00% | 0.00% | 0.00% | — | 35.45% | 0.92% | badly miscalibrated |
| c6__otc_chain50__R1 | observer | 5.83 | 57.2 | 4.39 | 4.51% | 17.58% | 29.22% | 3.46%, 5.67%, 6.36% (173) | 3.35% | 3.99% |  |
| c6__otc_chain50__R1 | first_hop | 5.83 | 57.0 | 4.38 | 4.57% | 17.71% | 29.29% | 3.25%, 5.87%, 6.71% (3460) | 2.59% | 0.92% | badly miscalibrated |
| c6__otc_chain50__R1 | destination | 5.81 | 56.4 | 4.56 | 4.04% | 15.91% | 30.40% | 1.74%, 5.50%, 6.36% (173) | 2.38% | 4.12% |  |
| c6__otc_chain50__R1 | destination_keyed | 5.93 | 61.1 | 4.86 | 0.95% | 3.80% | 7.84% | 0.29%, 1.39%, 1.73% (173) | 0.78% | 1.59% |  |
| c6__otc_chain50__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (41) | 0.00% | 0.00% |  |
| c6__otc_chain50__R1 | issuer_0 [share 50%, all records] | 5.54 | 46.5 | 4.45 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (41) | 5.07% | 4.23% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_0 [share 50%, other issuers' devices] | 5.54 | 46.5 | 4.45 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (41) | 5.07% | 4.23% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_0_with_observer [share 50%, all records] | 5.90 | 60.3 | 4.35 | 2.38% | 17.58% | 30.40% | 0.29%, 3.82%, 5.20% (173) | 4.59% | 4.27% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.90 | 60.3 | 4.35 | 2.38% | 17.58% | 30.40% | 0.29%, 3.82%, 5.20% (173) | 4.59% | 4.27% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.90 | 60.1 | 4.34 | 2.38% | 18.76% | 29.69% | 0.29%, 3.82%, 5.20% (173) | 4.59% | 4.43% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.90 | 60.1 | 4.34 | 2.38% | 18.76% | 29.69% | 0.29%, 3.82%, 5.20% (173) | 4.59% | 4.43% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_1 [share 30%, all records] | 4.86 | 29.1 | 4.08 | 18.05% | 43.94% | 44.42% | 1.45%, 4.12%, 4.65% (172) | 5.67% | 4.97% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_1 [share 30%, its own devices] | 4.85 | 29.0 | 3.97 | 23.16% | 54.74% | 55.09% | 4.56%, 5.39%, 5.59% (143) | 5.30% | 6.36% |  |
| c6__otc_chain50__R1 | issuer_1 [share 30%, other issuers' devices] | 4.94 | 30.8 | 4.57 | 7.35% | 21.32% | 22.06% | 0.00%, 0.00%, 0.00% (41) | 4.40% | 7.56% |  |
| c6__otc_chain50__R1 | issuer_1_with_observer [share 30%, all records] | 5.78 | 55.3 | 4.07 | 4.75% | 18.29% | 29.69% | 4.04%, 5.62%, 5.78% (173) | 2.40% | 5.36% |  |
| c6__otc_chain50__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.78 | 55.2 | 4.06 | 5.96% | 21.40% | 35.44% | 5.96%, 6.23%, 6.29% (143) | 2.67% | 5.99% |  |
| c6__otc_chain50__R1 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.05 | 66.4 | 4.77 | 2.21% | 11.76% | 17.65% | 1.43%, 5.37%, 6.45% (31) | 4.70% | 7.00% |  |
| c6__otc_chain50__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.78 | 55.2 | 4.06 | 5.46% | 18.53% | 29.93% | 4.61%, 6.38%, 6.40% (172) | 2.94% | 4.98% |  |
| c6__otc_chain50__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.77 | 55.1 | 4.05 | 6.67% | 21.75% | 35.44% | 6.67%, 6.93%, 6.99% (143) | 2.50% | 5.82% |  |
| c6__otc_chain50__R1 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.04 | 66.1 | 4.76 | 2.94% | 11.76% | 18.38% | 3.15%, 5.55%, 6.45% (31) | 4.90% | 6.97% |  |
| c6__otc_chain50__R1 | issuer_1_with_destination | — | — | — | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (143) | 0.00% | 0.00% |  |
| c6__otc_chain50__R1 | issuer_2 [share 20%, all records] | 4.41 | 21.4 | 3.68 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (41) | 8.50% | 5.49% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_2 [share 20%, other issuers' devices] | 4.41 | 21.4 | 3.68 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (41) | 8.50% | 5.49% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_2_with_observer [share 20%, all records] | 5.93 | 61.3 | 4.51 | 3.80% | 18.29% | 29.45% | 2.88%, 4.92%, 5.78% (173) | 4.45% | 3.81% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.93 | 61.3 | 4.51 | 3.80% | 18.29% | 29.45% | 2.88%, 4.92%, 5.78% (173) | 4.45% | 3.81% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.92 | 61.1 | 4.50 | 4.04% | 18.76% | 29.22% | 2.88%, 5.32%, 6.36% (173) | 4.22% | 4.05% | badly miscalibrated |
| c6__otc_chain50__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.92 | 61.1 | 4.50 | 4.04% | 18.76% | 29.22% | 2.88%, 5.32%, 6.36% (173) | 4.22% | 4.05% | badly miscalibrated |
| c6__otc_chain50__R100 | observer | 6.81 | 112.5 | 5.22 | 2.45% | 11.37% | 19.22% | 0.00%, 28.00%, 38.46% (13) | 0.64% | 1.84% |  |
| c6__otc_chain50__R100 | first_hop | 6.81 | 112.1 | 5.22 | 2.40% | 11.23% | 19.04% | 0.00%, 0.83%, 39.62% (260) | 0.51% | 0.42% |  |
| c6__otc_chain50__R100 | destination | 6.89 | 118.7 | 5.72 | 3.43% | 11.37% | 19.95% | 4.76%, 26.00%, 38.46% (13) | 1.68% | 1.51% |  |
| c6__otc_chain50__R100 | destination_keyed | 3.69 | 38.1 | 3.05 | 3.76% | 11.45% | 14.15% | 0.00%, 36.77%, 50.00% (10) | 19.43% | 4.15% | badly miscalibrated |
| c6__otc_chain50__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (10) | 0.00% | 0.00% |  |
| c6__otc_chain50__R100 | issuer_0 [share 50%, all records] | 5.88 | 59.1 | 4.71 | 2.53% | 22.00% | 30.01% | 0.00%, 9.91%, 42.86% (14) | 2.45% | 2.26% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_0 [share 50%, its own devices] | 5.83 | 57.0 | 4.29 | 5.79% | 50.86% | 68.67% | 10.00%, 28.67%, 33.33% (12) | 2.72% | 4.29% |  |
| c6__otc_chain50__R100 | issuer_0 [share 50%, other issuers' devices] | 5.91 | 60.2 | 5.39 | 0.53% | 4.23% | 6.21% | 0.00%, 0.00%, 0.00% (10) | 2.22% | 2.14% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_0_with_observer [share 50%, all records] | 6.77 | 109.7 | 4.86 | 2.86% | 11.04% | 18.89% | 6.23%, 19.67%, 30.77% (13) | 1.91% | 2.17% |  |
| c6__otc_chain50__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.78 | 110.0 | 4.87 | 5.58% | 16.31% | 23.39% | 0.00%, 8.00%, 10.00% (10) | 3.69% | 3.43% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.90 | 120.2 | 5.25 | 1.19% | 7.79% | 16.12% | 3.85%, 13.33%, 16.67% (12) | 1.74% | 2.41% |  |
| c6__otc_chain50__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.77 | 109.3 | 4.85 | 2.62% | 10.96% | 18.72% | 2.38%, 19.00%, 30.77% (13) | 1.72% | 2.04% |  |
| c6__otc_chain50__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.77 | 109.6 | 4.86 | 5.36% | 16.74% | 22.96% | 0.00%, 8.00%, 10.00% (10) | 3.48% | 3.70% |  |
| c6__otc_chain50__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.90 | 119.7 | 5.24 | 0.92% | 7.40% | 16.12% | 0.00%, 8.01%, 8.33% (12) | 1.90% | 2.50% |  |
| c6__otc_chain50__R100 | issuer_0_with_destination | 2.30 | 5.2 | 1.56 | 4.51% | 15.02% | 16.95% | 0.00%, 16.00%, 20.00% (10) | 31.78% | 8.04% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_1 [share 30%, all records] | 5.32 | 40.1 | 3.74 | 1.06% | 16.11% | 16.76% | 0.00%, 0.00%, 4.76% (21) | 7.49% | 3.00% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_1 [share 30%, its own devices] | 5.32 | 40.0 | 3.75 | 5.94% | 81.68% | 85.64% | — | 4.47% | 7.97% |  |
| c6__otc_chain50__R100 | issuer_1 [share 30%, other issuers' devices] | 5.39 | 42.0 | 4.54 | 0.10% | 3.13% | 3.13% | 0.00%, 0.00%, 7.14% (14) | 5.28% | 2.54% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_1_with_observer [share 30%, all records] | 6.78 | 110.0 | 4.88 | 2.29% | 10.38% | 18.32% | 0.00%, 20.00%, 38.46% (13) | 1.43% | 2.13% |  |
| c6__otc_chain50__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.78 | 110.1 | 4.85 | 5.45% | 15.35% | 23.76% | — | 4.21% | 5.48% |  |
| c6__otc_chain50__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.78 | 109.9 | 4.88 | 1.67% | 9.40% | 17.24% | 0.00%, 17.71%, 30.00% (10) | 2.09% | 2.18% |  |
| c6__otc_chain50__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.77 | 109.5 | 4.87 | 2.29% | 10.38% | 18.23% | 0.00%, 19.00%, 38.46% (13) | 1.70% | 2.12% |  |
| c6__otc_chain50__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.77 | 109.7 | 4.84 | 4.95% | 15.84% | 24.26% | — | 4.74% | 5.49% |  |
| c6__otc_chain50__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.90 | 119.4 | 5.24 | 1.76% | 9.30% | 17.04% | 0.00%, 17.71%, 30.00% (10) | 1.93% | 2.06% |  |
| c6__otc_chain50__R100 | issuer_1_with_destination | 1.85 | 3.9 | 1.23 | 1.49% | 7.43% | 7.43% | — | 43.43% | 13.41% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_2 [share 20%, all records] | 4.69 | 26.3 | 3.43 | 3.35% | 12.26% | 12.35% | 0.00%, 0.00%, 25.00% (12) | 11.21% | 3.58% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_2 [share 20%, its own devices] | 4.80 | 28.2 | 3.59 | 19.64% | 70.24% | 70.83% | 0.00%, 0.00%, 0.00% (10) | 5.42% | 8.95% |  |
| c6__otc_chain50__R100 | issuer_2 [share 20%, other issuers' devices] | 4.88 | 29.6 | 4.54 | 0.76% | 3.03% | 3.03% | 0.00%, 0.00%, 0.00% (10) | 4.35% | 2.55% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_2_with_observer [share 20%, all records] | 6.79 | 110.7 | 4.96 | 2.94% | 11.37% | 18.89% | 0.00%, 24.50%, 38.46% (13) | 0.94% | 2.12% |  |
| c6__otc_chain50__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.78 | 109.9 | 4.92 | 7.74% | 16.67% | 25.00% | 0.00%, 0.00%, 0.00% (10) | 6.91% | 5.50% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.79 | 110.8 | 4.96 | 2.18% | 10.52% | 17.91% | 0.00%, 14.00%, 38.46% (13) | 1.68% | 2.29% |  |
| c6__otc_chain50__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.78 | 110.2 | 4.95 | 2.70% | 11.12% | 18.64% | 0.00%, 19.00%, 38.46% (13) | 1.00% | 2.16% |  |
| c6__otc_chain50__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.77 | 109.5 | 4.92 | 7.14% | 16.07% | 25.00% | 0.00%, 0.00%, 0.00% (10) | 6.31% | 5.45% | badly miscalibrated |
| c6__otc_chain50__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.78 | 110.3 | 4.96 | 1.99% | 10.33% | 17.63% | 0.00%, 12.00%, 38.46% (13) | 1.65% | 2.22% |  |
| c6__otc_chain50__R100 | issuer_2_with_destination | 1.46 | 3.3 | 1.12 | 11.31% | 19.05% | 19.05% | 0.00%, 0.00%, 0.00% (10) | 40.92% | 11.15% | badly miscalibrated |
| c6__cp_W0__R1 | K records, K = 1 | 5.79 | 56.1 | 4.26 | 6.78% | 19.85% | 32.69% | 6.76%, 7.86%, 8.13% (209) | 3.57% | 4.93% |  |
| c6__cp_W0__R1 | K records, K = 2 | 4.98 | 33.0 | 3.12 | 5.34% | 25.73% | 43.20% | 5.32%, 7.22%, 7.69% (104) | 8.42% | 8.93% |  |
| c6__cp_W0__R1 | K records, K = 3 | 4.21 | 20.4 | 2.39 | 8.76% | 29.20% | 49.64% | 8.75%, 9.87%, 10.14% (69) | 14.51% | 12.20% | badly miscalibrated |
| c6__cp_W0__R1 | K records, K = 5 | 3.06 | 9.3 | 1.54 | 9.88% | 51.85% | 85.19% | 9.82%, 13.67%, 14.63% (41) | 27.60% | 19.77% | badly miscalibrated |
| c6__cp_W0__R1 | K records, K = 10 | 1.52 | 3.3 | 0.75 | 52.50% | 97.50% | 100.00% | 52.50%, 54.50%, 55.00% (20) | 27.74% | 26.79% | badly miscalibrated |
| c6__cp_W0__R1 | K records, K = 20 | 0.16 | 1.1 | 0.06 | 90.00% | 100.00% | 100.00% | 90.00%, 98.00%, 100.00% (10) | 7.46% | 12.99% |  |
| c6__cp_W0__R100 | K records, K = 1 | 6.94 | 123.1 | 5.39 | 1.73% | 10.53% | 19.49% | 0.00%, 6.67%, 33.33% (15) | 1.22% | 1.85% |  |
| c6__cp_W0__R100 | K records, K = 2 | 6.27 | 77.7 | 4.20 | 2.68% | 13.24% | 23.79% | 10.00%, 10.00%, 10.00% (10) | 3.42% | 4.06% |  |
| c6__cp_W0__R100 | K records, K = 3 | 5.60 | 49.2 | 3.38 | 2.99% | 14.03% | 33.73% | — | 7.42% | 7.33% | badly miscalibrated |
| c6__cp_W0__R100 | K records, K = 5 | 4.40 | 22.0 | 2.37 | 3.87% | 36.77% | 64.52% | — | 17.16% | 12.19% | badly miscalibrated |
| c6__cp_W1__R1 | K records, K = 1 | 5.78 | 54.9 | 4.56 | 0.00% | 4.90% | 17.53% | 0.00%, 0.00%, 0.00% (206) | 4.27% | 4.42% |  |
| c6__cp_W1__R1 | K records, K = 2 | 5.14 | 35.4 | 3.47 | 0.00% | 3.09% | 19.59% | 0.00%, 0.00%, 0.00% (103) | 9.24% | 8.37% | badly miscalibrated |
| c6__cp_W1__R1 | K records, K = 3 | 4.47 | 22.4 | 2.75 | 0.00% | 3.91% | 19.53% | 0.00%, 0.00%, 0.00% (68) | 15.41% | 12.54% | badly miscalibrated |
| c6__cp_W1__R1 | K records, K = 5 | 3.37 | 10.7 | 1.84 | 0.00% | 6.49% | 25.97% | 0.00%, 0.00%, 0.00% (41) | 29.30% | 18.92% | badly miscalibrated |
| c6__cp_W1__R1 | K records, K = 10 | 2.08 | 4.6 | 1.07 | 0.00% | 0.00% | 36.84% | 0.00%, 0.00%, 0.00% (20) | 50.98% | 28.59% | badly miscalibrated |
| c6__cp_W1__R1 | K records, K = 20 | 1.27 | 2.5 | 0.63 | 0.00% | 0.00% | 42.11% | 0.00%, 0.00%, 0.00% (10) | 66.81% | 39.74% | badly miscalibrated |
| c6__cp_W1__R100 | K records, K = 1 | 6.39 | 83.9 | 4.29 | 6.94% | 16.46% | 28.12% | 0.00%, 2.63%, 90.54% (74) | 1.88% | 2.55% |  |
| c6__cp_W1__R100 | K records, K = 2 | 4.94 | 32.2 | 2.52 | 7.44% | 17.52% | 31.24% | 0.00%, 30.91%, 89.19% (37) | 11.51% | 5.77% | badly miscalibrated |
| c6__cp_W1__R100 | K records, K = 3 | 3.41 | 12.0 | 1.55 | 7.07% | 18.32% | 30.63% | 14.29%, 69.82%, 87.50% (24) | 30.18% | 8.70% | badly miscalibrated |
| c6__cp_W1__R100 | K records, K = 5 | 1.75 | 3.9 | 0.81 | 8.65% | 21.62% | 41.62% | 85.71%, 85.71%, 85.71% (14) | 52.21% | 11.53% | badly miscalibrated |
| c6__cp_W1__R100 | K records, K = 10 | 0.69 | 1.8 | 0.32 | 12.50% | 37.50% | 67.86% | — | 70.22% | 15.92% | badly miscalibrated |
| c6__cp_W1__R100 | K records, K = 20 | 0.30 | 1.3 | 0.12 | 28.57% | 64.29% | 100.00% | — | 64.30% | 18.61% | badly miscalibrated |
| c6__cp_W2__R1 | K records, K = 1 | 5.54 | 47.4 | 3.87 | 8.20% | 22.95% | 32.79% | 8.14%, 11.09%, 11.83% (186) | 8.81% | 5.68% | badly miscalibrated |
| c6__cp_W2__R1 | K records, K = 2 | 4.47 | 24.9 | 2.55 | 8.20% | 20.22% | 33.88% | 8.14%, 11.09%, 11.83% (93) | 15.16% | 10.04% | badly miscalibrated |
| c6__cp_W2__R1 | K records, K = 3 | 3.56 | 14.4 | 1.89 | 8.20% | 22.13% | 36.89% | 8.15%, 10.66%, 11.29% (62) | 25.33% | 14.18% | badly miscalibrated |
| c6__cp_W2__R1 | K records, K = 5 | 2.39 | 6.5 | 1.23 | 6.85% | 21.92% | 42.47% | 6.79%, 10.01%, 10.81% (37) | 41.34% | 20.44% | badly miscalibrated |
| c6__cp_W2__R1 | K records, K = 10 | 1.28 | 2.8 | 0.64 | 5.56% | 19.44% | 58.33% | 5.56%, 10.00%, 11.11% (18) | 62.71% | 24.29% | badly miscalibrated |
| c6__cp_W2__R1 | K records, K = 20 | 0.63 | 1.7 | 0.28 | 5.56% | 16.67% | 83.33% | — | 78.42% | 25.46% | badly miscalibrated |
| c6__cp_W2__R100 | K records, K = 1 | 6.37 | 82.8 | 4.12 | 7.13% | 18.59% | 29.89% | 0.00%, 16.09%, 65.45% (55) | 2.87% | 2.71% | badly miscalibrated |
| c6__cp_W2__R100 | K records, K = 2 | 4.91 | 31.6 | 2.35 | 7.51% | 19.86% | 32.02% | 3.33%, 58.33%, 60.00% (15) | 14.46% | 7.08% | badly miscalibrated |
| c6__cp_W2__R100 | K records, K = 3 | 3.41 | 12.3 | 1.45 | 8.82% | 22.65% | 35.29% | 46.67%, 68.56%, 72.22% (18) | 31.75% | 10.12% | badly miscalibrated |
| c6__cp_W2__R100 | K records, K = 5 | 1.66 | 3.8 | 0.64 | 9.71% | 27.43% | 38.86% | 63.64%, 63.64%, 63.64% (11) | 58.10% | 11.48% | badly miscalibrated |
| c6__cp_W2__R100 | K records, K = 10 | 0.59 | 1.6 | 0.23 | 17.54% | 42.11% | 75.44% | — | 69.30% | 12.53% | badly miscalibrated |
| c6__cp_W2__R100 | K records, K = 20 | 0.30 | 1.3 | 0.12 | 36.36% | 90.91% | 100.00% | — | 58.34% | 22.60% | badly miscalibrated |
| c6__cp_Wmis__R1 | K records, K = 1 | 5.56 | 47.4 | 3.72 | 20.77% | 30.60% | 38.25% | 20.68%, 24.78%, 25.81% (186) | 15.61% | 5.57% | badly miscalibrated |
| c6__cp_Wmis__R1 | K records, K = 2 | 4.36 | 22.4 | 2.42 | 21.86% | 31.69% | 42.08% | 21.79%, 25.00%, 25.81% (93) | 9.55% | 10.99% |  |
| c6__cp_Wmis__R1 | K records, K = 3 | 3.45 | 12.8 | 1.79 | 24.59% | 36.07% | 49.18% | 24.46%, 30.70%, 32.26% (62) | 14.01% | 16.02% |  |
| c6__cp_Wmis__R1 | K records, K = 5 | 2.10 | 5.2 | 1.02 | 24.66% | 60.27% | 80.82% | 24.55%, 30.86%, 32.43% (37) | 30.33% | 20.45% | badly miscalibrated |
| c6__cp_Wmis__R1 | K records, K = 10 | 0.81 | 2.0 | 0.41 | 61.11% | 94.44% | 97.22% | 61.11%, 61.11%, 61.11% (18) | 18.38% | 20.94% |  |
| c6__cp_Wmis__R1 | K records, K = 20 | 0.08 | 1.1 | 0.04 | 94.44% | 100.00% | 100.00% | — | 7.75% | 3.47% |  |
| c6__cp_Wmis__R100 | K records, K = 1 | 6.03 | 66.0 | 3.31 | 9.83% | 25.39% | 37.51% | 0.00%, 27.38%, 65.62% (64) | 2.29% | 3.58% |  |
| c6__cp_Wmis__R100 | K records, K = 2 | 3.47 | 13.5 | 1.40 | 10.38% | 29.70% | 41.50% | 17.42%, 55.33%, 67.74% (31) | 32.24% | 7.21% | badly miscalibrated |
| c6__cp_Wmis__R100 | K records, K = 3 | 1.80 | 4.5 | 0.76 | 11.76% | 31.76% | 47.65% | 39.02%, 63.33%, 66.67% (21) | 52.42% | 8.57% | badly miscalibrated |
| c6__cp_Wmis__R100 | K records, K = 5 | 0.71 | 1.8 | 0.31 | 12.57% | 37.71% | 65.14% | 66.67%, 66.67%, 66.67% (12) | 70.86% | 8.16% | badly miscalibrated |
| c6__cp_chain100__R1 | K records, K = 1 | 5.78 | 55.3 | 4.24 | 7.14% | 19.76% | 34.76% | 7.17%, 8.78%, 9.18% (207) | 4.91% | 4.24% | badly miscalibrated |
| c6__cp_chain100__R1 | K records, K = 2 | 4.95 | 32.0 | 3.10 | 6.70% | 24.88% | 38.76% | 6.74%, 9.12%, 9.71% (103) | 7.30% | 9.26% |  |
| c6__cp_chain100__R1 | K records, K = 3 | 4.17 | 19.6 | 2.36 | 10.00% | 29.29% | 50.71% | 10.06%, 13.61%, 14.49% (69) | 12.58% | 13.40% |  |
| c6__cp_chain100__R1 | K records, K = 5 | 2.97 | 9.0 | 1.52 | 18.07% | 45.78% | 74.70% | 18.18%, 25.10%, 26.83% (41) | 23.23% | 19.27% | badly miscalibrated |
| c6__cp_chain100__R1 | K records, K = 10 | 1.24 | 2.7 | 0.56 | 41.46% | 90.24% | 97.56% | 41.90%, 56.38%, 60.00% (20) | 31.26% | 23.00% | badly miscalibrated |
| c6__cp_chain100__R1 | K records, K = 20 | 0.19 | 1.2 | 0.08 | 85.00% | 100.00% | 100.00% | 85.00%, 89.00%, 90.00% (10) | 12.37% | 12.33% |  |
| c6__cp_chain100__R100 | K records, K = 1 | 6.77 | 110.4 | 5.07 | 1.78% | 11.83% | 19.45% | 0.00%, 11.00%, 27.27% (11) | 1.83% | 2.06% |  |
| c6__cp_chain100__R100 | K records, K = 2 | 5.93 | 63.8 | 3.76 | 3.19% | 13.65% | 24.47% | 10.00%, 10.00%, 10.00% (10) | 5.43% | 4.47% | badly miscalibrated |
| c6__cp_chain100__R100 | K records, K = 3 | 5.14 | 38.4 | 2.91 | 2.97% | 13.65% | 33.23% | — | 12.15% | 7.36% | badly miscalibrated |
| c6__cp_chain100__R100 | K records, K = 5 | 3.86 | 16.7 | 1.94 | 6.63% | 28.92% | 53.01% | — | 22.60% | 12.59% | badly miscalibrated |
| c6__cp_chain50__R1 | K records, K = 1 | 5.99 | 64.2 | 4.30 | 4.51% | 16.86% | 28.27% | 1.42%, 6.58%, 8.19% (171) | 5.20% | 4.13% | badly miscalibrated |
| c6__cp_chain50__R1 | K records, K = 2 | 4.92 | 31.9 | 3.01 | 4.31% | 19.14% | 39.23% | 1.70%, 5.96%, 7.06% (85) | 9.84% | 9.88% |  |
| c6__cp_chain50__R1 | K records, K = 3 | 4.01 | 17.7 | 2.25 | 6.47% | 30.94% | 59.71% | 2.59%, 8.92%, 10.53% (57) | 17.40% | 12.96% | badly miscalibrated |
| c6__cp_chain50__R1 | K records, K = 5 | 2.70 | 7.3 | 1.37 | 16.87% | 59.04% | 91.57% | 18.95%, 24.97%, 26.47% (34) | 27.07% | 20.36% | badly miscalibrated |
| c6__cp_chain50__R1 | K records, K = 10 | 0.98 | 2.1 | 0.43 | 70.00% | 95.00% | 100.00% | 70.59%, 84.71%, 88.24% (17) | 21.76% | 23.05% |  |
| c6__cp_chain50__R1 | K records, K = 20 | 0.05 | 1.0 | 0.01 | 94.44% | 100.00% | 100.00% | — | 5.91% | 5.91% |  |
| c6__cp_chain50__R100 | K records, K = 1 | 6.99 | 128.7 | 5.17 | 2.17% | 9.34% | 17.31% | 0.00%, 14.17%, 41.67% (12) | 1.65% | 1.85% |  |
| c6__cp_chain50__R100 | K records, K = 2 | 5.90 | 63.8 | 3.70 | 3.27% | 13.46% | 23.08% | — | 5.50% | 5.33% | badly miscalibrated |
| c6__cp_chain50__R100 | K records, K = 3 | 4.97 | 34.9 | 2.77 | 4.70% | 19.46% | 34.23% | — | 11.93% | 8.41% | badly miscalibrated |
| c6__cp_chain50__R100 | K records, K = 5 | 3.45 | 13.1 | 1.68 | 13.22% | 46.28% | 77.69% | — | 22.96% | 15.90% | badly miscalibrated |
| c6__otcL_W0__R1 | K records, K = 1 | 5.65 | 50.4 | 4.27 | 2.66% | 21.79% | 38.26% | 2.65%, 3.59%, 3.83% (209) | 3.93% | 4.48% |  |
| c6__otcL_W0__R1 | K records, K = 2 | 4.81 | 28.5 | 3.10 | 9.22% | 35.92% | 53.40% | 9.20%, 11.07%, 11.54% (104) | 7.65% | 9.24% |  |
| c6__otcL_W0__R1 | K records, K = 3 | 3.94 | 15.9 | 2.25 | 11.68% | 47.45% | 72.26% | 11.66%, 13.93%, 14.49% (69) | 14.49% | 14.27% | badly miscalibrated |
| c6__otcL_W0__R1 | K records, K = 5 | 2.55 | 6.4 | 1.31 | 23.46% | 77.78% | 95.06% | 23.35%, 30.04%, 31.71% (41) | 20.76% | 19.17% | badly miscalibrated |
| c6__otcL_W0__R1 | K records, K = 10 | 0.63 | 1.7 | 0.32 | 67.50% | 97.50% | 100.00% | 67.50%, 73.50%, 75.00% (20) | 20.55% | 17.71% |  |
| c6__otcL_W0__R1 | K records, K = 20 | 0.05 | 1.0 | 0.01 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (10) | 0.91% | 4.09% |  |
| c6__otcL_W0__R100 | K records, K = 1 | 6.60 | 97.5 | 5.06 | 2.88% | 11.76% | 22.70% | 0.00%, 10.00%, 18.18% (11) | 1.04% | 2.05% |  |
| c6__otcL_W0__R100 | K records, K = 2 | 5.72 | 53.4 | 3.77 | 3.76% | 19.86% | 37.39% | 20.00%, 20.00%, 20.00% (10) | 4.05% | 4.93% |  |
| c6__otcL_W0__R100 | K records, K = 3 | 4.85 | 29.5 | 2.90 | 8.66% | 35.22% | 57.31% | — | 8.82% | 7.65% | badly miscalibrated |
| c6__otcL_W0__R100 | K records, K = 5 | 3.34 | 10.7 | 1.76 | 31.61% | 69.68% | 85.81% | — | 9.99% | 14.40% |  |
| c6__otcL_W1__R1 | K records, K = 1 | 5.59 | 48.3 | 4.60 | 0.52% | 11.34% | 26.55% | 0.49%, 0.87%, 0.97% (206) | 4.06% | 4.05% | badly miscalibrated |
| c6__otcL_W1__R1 | K records, K = 2 | 4.96 | 31.8 | 3.59 | 1.03% | 11.34% | 34.02% | 0.97%, 1.75%, 1.94% (103) | 7.75% | 8.24% |  |
| c6__otcL_W1__R1 | K records, K = 3 | 4.34 | 21.1 | 2.83 | 1.56% | 11.72% | 39.06% | 1.47%, 2.65%, 2.94% (68) | 15.26% | 12.72% | badly miscalibrated |
| c6__otcL_W1__R1 | K records, K = 5 | 3.38 | 11.2 | 2.00 | 1.30% | 15.58% | 48.05% | 1.22%, 2.20%, 2.44% (41) | 26.48% | 18.11% | badly miscalibrated |
| c6__otcL_W1__R1 | K records, K = 10 | 2.08 | 4.6 | 1.05 | 0.00% | 13.16% | 76.32% | 0.00%, 0.00%, 0.00% (20) | 51.28% | 29.42% | badly miscalibrated |
| c6__otcL_W1__R1 | K records, K = 20 | 1.41 | 2.9 | 0.80 | 0.00% | 10.53% | 100.00% | 0.00%, 0.00%, 0.00% (10) | 61.90% | 37.87% | badly miscalibrated |
| c6__otcL_W1__R100 | K records, K = 1 | 6.14 | 71.0 | 4.14 | 6.10% | 18.83% | 31.10% | 0.00%, 4.08%, 64.86% (74) | 1.60% | 2.38% |  |
| c6__otcL_W1__R100 | K records, K = 2 | 4.69 | 27.0 | 2.38 | 6.78% | 20.17% | 34.38% | 0.00%, 39.62%, 70.27% (37) | 13.94% | 6.56% | badly miscalibrated |
| c6__otcL_W1__R100 | K records, K = 3 | 3.18 | 10.2 | 1.41 | 7.33% | 20.94% | 37.70% | 38.33%, 70.00%, 71.43% (14) | 32.92% | 9.29% | badly miscalibrated |
| c6__otcL_W1__R100 | K records, K = 5 | 1.53 | 3.2 | 0.67 | 8.65% | 24.32% | 51.35% | 71.43%, 71.43%, 71.43% (14) | 56.74% | 12.20% | badly miscalibrated |
| c6__otcL_W1__R100 | K records, K = 10 | 0.62 | 1.7 | 0.31 | 14.29% | 39.29% | 87.50% | — | 68.79% | 15.07% | badly miscalibrated |
| c6__otcL_W1__R100 | K records, K = 20 | 0.39 | 1.4 | 0.23 | 35.71% | 85.71% | 100.00% | — | 51.55% | 24.00% | badly miscalibrated |
| c6__otcL_W2__R1 | K records, K = 1 | 5.45 | 44.0 | 4.11 | 5.74% | 23.22% | 40.98% | 5.75%, 6.48%, 6.67% (180) | 4.17% | 5.01% |  |
| c6__otcL_W2__R1 | K records, K = 2 | 4.63 | 25.5 | 2.89 | 5.46% | 24.04% | 46.99% | 5.48%, 6.43%, 6.67% (90) | 10.84% | 9.72% | badly miscalibrated |
| c6__otcL_W2__R1 | K records, K = 3 | 3.79 | 14.9 | 2.11 | 3.28% | 26.23% | 53.28% | 3.31%, 4.66%, 5.00% (60) | 22.86% | 15.02% | badly miscalibrated |
| c6__otcL_W2__R1 | K records, K = 5 | 2.61 | 6.8 | 1.36 | 5.48% | 34.25% | 67.12% | 5.48%, 5.54%, 5.56% (36) | 37.39% | 19.92% | badly miscalibrated |
| c6__otcL_W2__R1 | K records, K = 10 | 1.35 | 2.8 | 0.67 | 11.11% | 38.89% | 88.89% | 11.11%, 11.11%, 11.11% (18) | 55.82% | 25.57% | badly miscalibrated |
| c6__otcL_W2__R1 | K records, K = 20 | 0.74 | 1.8 | 0.35 | 5.56% | 66.67% | 100.00% | — | 75.92% | 27.30% | badly miscalibrated |
| c6__otcL_W2__R100 | K records, K = 1 | 6.14 | 70.8 | 4.10 | 5.81% | 20.23% | 32.19% | 0.00%, 15.92%, 61.29% (31) | 2.27% | 2.77% |  |
| c6__otcL_W2__R100 | K records, K = 2 | 4.72 | 27.8 | 2.38 | 6.44% | 22.72% | 35.78% | 9.09%, 53.00%, 60.00% (15) | 15.31% | 7.22% | badly miscalibrated |
| c6__otcL_W2__R100 | K records, K = 3 | 3.24 | 10.9 | 1.42 | 7.94% | 25.29% | 41.76% | 40.00%, 60.78%, 61.11% (18) | 33.84% | 9.70% | badly miscalibrated |
| c6__otcL_W2__R100 | K records, K = 5 | 1.55 | 3.5 | 0.64 | 9.14% | 33.14% | 56.57% | 72.73%, 72.73%, 72.73% (11) | 59.08% | 11.74% | badly miscalibrated |
| c6__otcL_W2__R100 | K records, K = 10 | 0.49 | 1.5 | 0.18 | 19.30% | 59.65% | 82.46% | — | 69.98% | 14.38% | badly miscalibrated |
| c6__otcL_W2__R100 | K records, K = 20 | 0.54 | 1.6 | 0.33 | 18.18% | 100.00% | 100.00% | — | 64.58% | 28.13% | badly miscalibrated |
| c6__otcL_Wmis__R1 | K records, K = 1 | 5.44 | 43.9 | 3.84 | 16.12% | 32.24% | 44.81% | 16.10%, 16.98%, 17.20% (186) | 8.74% | 5.40% | badly miscalibrated |
| c6__otcL_Wmis__R1 | K records, K = 2 | 4.37 | 22.1 | 2.59 | 19.13% | 40.44% | 55.74% | 19.10%, 20.16%, 20.43% (93) | 7.59% | 12.07% |  |
| c6__otcL_Wmis__R1 | K records, K = 3 | 3.39 | 11.7 | 1.80 | 22.95% | 51.64% | 72.95% | 22.96%, 23.26%, 23.33% (60) | 10.32% | 14.82% |  |
| c6__otcL_Wmis__R1 | K records, K = 5 | 2.02 | 4.8 | 1.01 | 36.99% | 83.56% | 95.89% | 36.90%, 41.97%, 43.24% (37) | 18.42% | 20.36% |  |
| c6__otcL_Wmis__R1 | K records, K = 10 | 0.35 | 1.3 | 0.14 | 83.33% | 100.00% | 100.00% | 83.33%, 87.78%, 88.89% (18) | 12.33% | 14.11% |  |
| c6__otcL_Wmis__R1 | K records, K = 20 | 0.01 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | — | 0.17% | 5.39% |  |
| c6__otcL_Wmis__R100 | K records, K = 1 | 6.37 | 82.7 | 4.37 | 9.17% | 25.96% | 37.84% | 0.00%, 17.00%, 64.52% (31) | 4.10% | 2.81% | badly miscalibrated |
| c6__otcL_Wmis__R100 | K records, K = 2 | 5.02 | 34.1 | 2.52 | 11.27% | 32.74% | 47.76% | 12.44%, 61.67%, 67.74% (31) | 10.13% | 6.36% | badly miscalibrated |
| c6__otcL_Wmis__R100 | K records, K = 3 | 3.34 | 11.8 | 1.40 | 12.65% | 36.47% | 56.18% | 49.17%, 65.71%, 71.43% (21) | 30.33% | 9.81% | badly miscalibrated |
| c6__otcL_Wmis__R100 | K records, K = 5 | 1.31 | 2.9 | 0.54 | 12.00% | 50.29% | 78.29% | 75.00%, 75.00%, 75.00% (12) | 60.34% | 10.76% | badly miscalibrated |
| c6__otcL_chain100__R1 | K records, K = 1 | 5.63 | 49.7 | 4.25 | 5.48% | 21.19% | 37.62% | 5.51%, 7.29%, 7.73% (207) | 2.39% | 4.64% |  |
| c6__otcL_chain100__R1 | K records, K = 2 | 4.80 | 28.3 | 3.10 | 7.66% | 33.01% | 54.55% | 7.68%, 9.30%, 9.71% (103) | 7.75% | 8.44% |  |
| c6__otcL_chain100__R1 | K records, K = 3 | 4.00 | 16.5 | 2.30 | 9.29% | 44.29% | 67.14% | 9.28%, 9.74%, 9.86% (71) | 14.13% | 12.80% | badly miscalibrated |
| c6__otcL_chain100__R1 | K records, K = 5 | 2.61 | 6.7 | 1.38 | 21.69% | 75.90% | 92.77% | 21.69%, 21.90%, 21.95% (41) | 22.29% | 19.39% | badly miscalibrated |
| c6__otcL_chain100__R1 | K records, K = 10 | 0.72 | 1.8 | 0.33 | 70.73% | 95.12% | 100.00% | 70.71%, 71.29%, 71.43% (21) | 21.86% | 19.34% | badly miscalibrated |
| c6__otcL_chain100__R1 | K records, K = 20 | 0.07 | 1.1 | 0.02 | 95.00% | 100.00% | 100.00% | 95.00%, 99.00%, 100.00% (10) | 3.84% | 8.84% |  |
| c6__otcL_chain100__R100 | K records, K = 1 | 6.62 | 98.4 | 5.10 | 3.14% | 12.31% | 21.48% | 0.00%, 15.76%, 27.27% (11) | 1.65% | 1.89% |  |
| c6__otcL_chain100__R100 | K records, K = 2 | 5.76 | 54.8 | 3.80 | 4.19% | 15.71% | 32.11% | 0.00%, 0.00%, 0.00% (10) | 3.80% | 3.96% |  |
| c6__otcL_chain100__R100 | K records, K = 3 | 4.93 | 31.2 | 2.90 | 6.67% | 25.80% | 49.57% | — | 8.04% | 7.42% | badly miscalibrated |
| c6__otcL_chain100__R100 | K records, K = 5 | 3.42 | 11.6 | 1.72 | 15.43% | 53.09% | 79.01% | — | 20.14% | 14.68% | badly miscalibrated |
| c6__otcL_chain50__R1 | K records, K = 1 | 5.83 | 57.1 | 4.40 | 6.41% | 21.85% | 37.29% | 2.02%, 9.45%, 11.76% (170) | 2.79% | 4.44% |  |
| c6__otcL_chain50__R1 | K records, K = 2 | 4.74 | 27.6 | 3.05 | 10.48% | 35.24% | 58.10% | 5.41%, 14.92%, 18.82% (85) | 7.41% | 9.50% |  |
| c6__otcL_chain50__R1 | K records, K = 3 | 3.67 | 13.3 | 2.09 | 17.39% | 55.07% | 78.26% | 12.94%, 21.51%, 23.21% (56) | 9.33% | 14.47% |  |
| c6__otcL_chain50__R1 | K records, K = 5 | 2.15 | 4.9 | 1.13 | 32.53% | 90.36% | 98.80% | 38.24%, 40.59%, 41.18% (34) | 20.38% | 20.07% | badly miscalibrated |
| c6__otcL_chain50__R1 | K records, K = 10 | 0.30 | 1.3 | 0.16 | 92.68% | 100.00% | 100.00% | 94.12%, 94.12%, 94.12% (17) | 9.75% | 11.97% |  |
| c6__otcL_chain50__R1 | K records, K = 20 | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | — | 0.01% | 0.01% |  |
| c6__otcL_chain50__R100 | K records, K = 1 | 6.80 | 111.4 | 5.23 | 3.13% | 11.88% | 19.42% | 6.25%, 20.00%, 27.27% (11) | 0.89% | 1.93% |  |
| c6__otcL_chain50__R100 | K records, K = 2 | 5.64 | 51.4 | 3.69 | 5.98% | 20.93% | 34.95% | — | 3.22% | 4.85% |  |
| c6__otcL_chain50__R100 | K records, K = 3 | 4.65 | 26.2 | 2.72 | 7.80% | 41.02% | 63.05% | — | 9.39% | 8.95% | badly miscalibrated |
| c6__otcL_chain50__R100 | K records, K = 5 | 2.92 | 8.1 | 1.47 | 31.67% | 73.33% | 90.83% | — | 10.97% | 15.56% |  |
| c6__otc_W0__R1 | K records, K = 1 | 5.65 | 50.2 | 4.26 | 6.05% | 20.82% | 36.32% | 6.03%, 7.33%, 7.66% (209) | 3.61% | 4.97% |  |
| c6__otc_W0__R1 | K records, K = 2 | 4.80 | 28.3 | 3.10 | 8.25% | 34.95% | 56.31% | 8.22%, 10.87%, 11.54% (104) | 5.73% | 8.64% |  |
| c6__otc_W0__R1 | K records, K = 3 | 4.00 | 16.5 | 2.33 | 13.87% | 53.28% | 68.61% | 13.83%, 17.84%, 18.84% (69) | 7.84% | 13.12% |  |
| c6__otc_W0__R1 | K records, K = 5 | 2.60 | 6.5 | 1.29 | 25.93% | 74.07% | 92.59% | 25.79%, 34.43%, 36.59% (41) | 20.55% | 20.72% |  |
| c6__otc_W0__R1 | K records, K = 10 | 0.67 | 1.7 | 0.30 | 85.00% | 97.50% | 100.00% | 85.00%, 85.00%, 85.00% (20) | 13.97% | 19.18% |  |
| c6__otc_W0__R1 | K records, K = 20 | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (10) | 0.03% | 4.97% |  |
| c6__otc_W0__R100 | K records, K = 1 | 6.62 | 98.8 | 5.08 | 3.04% | 13.40% | 22.86% | 0.00%, 15.38%, 27.27% (11) | 0.71% | 2.11% |  |
| c6__otc_W0__R100 | K records, K = 2 | 5.76 | 55.0 | 3.76 | 3.40% | 18.78% | 33.81% | 10.00%, 10.00%, 10.00% (10) | 5.45% | 4.62% | badly miscalibrated |
| c6__otc_W0__R100 | K records, K = 3 | 4.91 | 31.0 | 2.90 | 8.06% | 33.43% | 57.01% | — | 8.14% | 7.99% | badly miscalibrated |
| c6__otc_W0__R100 | K records, K = 5 | 3.39 | 11.1 | 1.74 | 18.71% | 67.10% | 81.29% | — | 15.52% | 14.01% | badly miscalibrated |
| c6__otc_W1__R1 | K records, K = 1 | 5.58 | 48.0 | 4.60 | 0.77% | 9.54% | 24.48% | 0.73%, 1.31%, 1.46% (206) | 4.37% | 3.95% | badly miscalibrated |
| c6__otc_W1__R1 | K records, K = 2 | 4.94 | 31.4 | 3.58 | 1.03% | 11.34% | 27.32% | 0.97%, 1.75%, 1.94% (103) | 7.81% | 8.36% |  |
| c6__otc_W1__R1 | K records, K = 3 | 4.33 | 20.8 | 2.84 | 1.56% | 13.28% | 33.59% | 1.57%, 1.65%, 1.67% (60) | 13.50% | 11.81% | badly miscalibrated |
| c6__otc_W1__R1 | K records, K = 5 | 3.37 | 11.0 | 1.94 | 1.30% | 11.69% | 48.05% | 1.39%, 2.50%, 2.78% (36) | 26.95% | 18.83% | badly miscalibrated |
| c6__otc_W1__R1 | K records, K = 10 | 2.13 | 4.8 | 1.23 | 0.00% | 13.16% | 86.84% | 0.00%, 0.00%, 0.00% (20) | 46.69% | 27.81% | badly miscalibrated |
| c6__otc_W1__R1 | K records, K = 20 | 1.33 | 2.7 | 0.67 | 0.00% | 21.05% | 100.00% | 0.00%, 0.00%, 0.00% (10) | 65.62% | 36.05% | badly miscalibrated |
| c6__otc_W1__R100 | K records, K = 1 | 6.14 | 70.8 | 4.20 | 7.16% | 18.14% | 30.79% | 0.00%, 9.81%, 82.43% (74) | 2.15% | 2.35% |  |
| c6__otc_W1__R100 | K records, K = 2 | 4.73 | 27.9 | 2.48 | 8.43% | 19.67% | 34.55% | 6.67%, 30.13%, 86.49% (37) | 11.09% | 5.94% | badly miscalibrated |
| c6__otc_W1__R100 | K records, K = 3 | 3.31 | 11.1 | 1.54 | 8.12% | 20.94% | 37.43% | 22.86%, 71.96%, 87.50% (24) | 29.26% | 9.33% | badly miscalibrated |
| c6__otc_W1__R100 | K records, K = 5 | 1.70 | 3.7 | 0.78 | 9.19% | 27.57% | 53.51% | 92.86%, 92.86%, 92.86% (14) | 52.27% | 14.39% | badly miscalibrated |
| c6__otc_W1__R100 | K records, K = 10 | 0.65 | 1.7 | 0.31 | 16.07% | 44.64% | 89.29% | — | 66.77% | 16.35% | badly miscalibrated |
| c6__otc_W1__R100 | K records, K = 20 | 0.22 | 1.2 | 0.11 | 28.57% | 92.86% | 100.00% | — | 66.15% | 17.83% | badly miscalibrated |
| c6__otc_W2__R1 | K records, K = 1 | 5.29 | 39.7 | 3.71 | 7.92% | 26.23% | 39.34% | 7.90%, 8.89%, 9.14% (186) | 7.02% | 6.09% | badly miscalibrated |
| c6__otc_W2__R1 | K records, K = 2 | 4.22 | 20.5 | 2.43 | 8.74% | 22.95% | 46.45% | 8.73%, 9.49%, 9.68% (93) | 14.63% | 11.12% | badly miscalibrated |
| c6__otc_W2__R1 | K records, K = 3 | 3.33 | 11.7 | 1.78 | 9.02% | 26.23% | 53.28% | 8.98%, 10.83%, 11.29% (62) | 24.73% | 15.83% | badly miscalibrated |
| c6__otc_W2__R1 | K records, K = 5 | 2.20 | 5.5 | 1.15 | 8.22% | 27.40% | 71.23% | 8.22%, 8.31%, 8.33% (36) | 42.21% | 20.40% | badly miscalibrated |
| c6__otc_W2__R1 | K records, K = 10 | 1.26 | 2.7 | 0.67 | 8.33% | 50.00% | 94.44% | 8.33%, 15.00%, 16.67% (18) | 58.48% | 24.52% | badly miscalibrated |
| c6__otc_W2__R1 | K records, K = 20 | 0.74 | 1.9 | 0.43 | 11.11% | 66.67% | 100.00% | — | 69.38% | 26.59% | badly miscalibrated |
| c6__otc_W2__R100 | K records, K = 1 | 6.11 | 69.3 | 4.03 | 6.63% | 19.25% | 32.51% | 0.00%, 15.24%, 70.97% (31) | 2.28% | 2.70% |  |
| c6__otc_W2__R100 | K records, K = 2 | 4.64 | 26.6 | 2.31 | 7.16% | 20.75% | 36.85% | 12.88%, 51.67%, 66.67% (15) | 15.84% | 6.40% | badly miscalibrated |
| c6__otc_W2__R100 | K records, K = 3 | 3.24 | 11.1 | 1.44 | 7.06% | 21.76% | 45.59% | 35.00%, 64.00%, 70.00% (10) | 34.37% | 10.25% | badly miscalibrated |
| c6__otc_W2__R100 | K records, K = 5 | 1.62 | 3.7 | 0.68 | 10.29% | 29.71% | 57.14% | 63.64%, 63.64%, 63.64% (11) | 56.50% | 12.44% | badly miscalibrated |
| c6__otc_W2__R100 | K records, K = 10 | 0.49 | 1.5 | 0.23 | 17.54% | 52.63% | 94.74% | — | 70.14% | 12.68% | badly miscalibrated |
| c6__otc_W2__R100 | K records, K = 20 | 0.22 | 1.2 | 0.07 | 27.27% | 90.91% | 100.00% | — | 68.76% | 15.21% | badly miscalibrated |
| c6__otc_Wmis__R1 | K records, K = 1 | 5.43 | 43.7 | 3.82 | 20.49% | 32.79% | 43.99% | 20.44%, 23.01%, 23.66% (186) | 14.20% | 5.52% | badly miscalibrated |
| c6__otc_Wmis__R1 | K records, K = 2 | 4.30 | 21.4 | 2.47 | 21.31% | 39.34% | 56.83% | 21.27%, 23.18%, 23.66% (93) | 7.38% | 11.48% |  |
| c6__otc_Wmis__R1 | K records, K = 3 | 3.33 | 11.5 | 1.78 | 28.69% | 49.18% | 67.21% | 28.63%, 31.53%, 32.26% (62) | 8.30% | 14.77% |  |
| c6__otc_Wmis__R1 | K records, K = 5 | 1.97 | 4.6 | 0.96 | 38.36% | 78.08% | 95.89% | 38.36%, 38.78%, 38.89% (36) | 17.78% | 20.61% |  |
| c6__otc_Wmis__R1 | K records, K = 10 | 0.27 | 1.3 | 0.12 | 80.56% | 100.00% | 100.00% | 80.56%, 82.78%, 83.33% (18) | 16.09% | 10.45% |  |
| c6__otc_Wmis__R1 | K records, K = 20 | 0.01 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | — | 0.09% | 0.15% |  |
| c6__otc_Wmis__R100 | K records, K = 1 | 5.77 | 55.3 | 3.32 | 9.58% | 25.47% | 38.17% | 0.00%, 22.42%, 77.42% (31) | 2.49% | 3.32% |  |
| c6__otc_Wmis__R100 | K records, K = 2 | 3.41 | 13.1 | 1.50 | 10.02% | 29.70% | 46.33% | 14.09%, 52.90%, 66.67% (15) | 30.82% | 7.50% | badly miscalibrated |
| c6__otc_Wmis__R100 | K records, K = 3 | 1.85 | 4.7 | 0.80 | 10.88% | 36.76% | 57.06% | 38.18%, 68.57%, 80.00% (10) | 52.05% | 8.68% | badly miscalibrated |
| c6__otc_Wmis__R100 | K records, K = 5 | 0.71 | 1.9 | 0.32 | 12.57% | 54.86% | 77.14% | 66.67%, 66.67%, 66.67% (12) | 70.31% | 8.49% | badly miscalibrated |
| c6__otc_chain100__R1 | K records, K = 1 | 5.63 | 49.7 | 4.22 | 4.75% | 20.43% | 37.77% | 4.79%, 7.50%, 8.17% (208) | 2.05% | 4.39% |  |
| c6__otc_chain100__R1 | K records, K = 2 | 4.81 | 28.3 | 3.09 | 9.05% | 29.05% | 45.71% | 9.07%, 11.04%, 11.54% (104) | 5.14% | 8.97% |  |
| c6__otc_chain100__R1 | K records, K = 3 | 4.00 | 16.6 | 2.30 | 10.00% | 40.00% | 59.29% | 10.00%, 10.12%, 10.14% (69) | 12.02% | 13.51% |  |
| c6__otc_chain100__R1 | K records, K = 5 | 2.66 | 6.9 | 1.38 | 24.10% | 61.45% | 90.36% | 24.16%, 28.25%, 29.27% (41) | 22.26% | 20.36% | badly miscalibrated |
| c6__otc_chain100__R1 | K records, K = 10 | 0.85 | 2.0 | 0.40 | 63.41% | 100.00% | 100.00% | 63.21%, 69.79%, 71.43% (21) | 20.78% | 22.81% |  |
| c6__otc_chain100__R1 | K records, K = 20 | 0.09 | 1.1 | 0.03 | 90.00% | 100.00% | 100.00% | 90.00%, 90.00%, 90.00% (10) | 9.19% | 9.21% |  |
| c6__otc_chain100__R100 | K records, K = 1 | 6.61 | 98.0 | 5.10 | 2.45% | 12.58% | 21.81% | 0.00%, 10.00%, 25.00% (16) | 1.33% | 1.96% |  |
| c6__otc_chain100__R100 | K records, K = 2 | 5.77 | 55.2 | 3.78 | 4.32% | 17.63% | 32.19% | 0.00%, 0.00%, 0.00% (10) | 3.76% | 4.23% |  |
| c6__otc_chain100__R100 | K records, K = 3 | 4.95 | 31.5 | 2.92 | 6.47% | 26.47% | 45.59% | — | 7.68% | 7.44% | badly miscalibrated |
| c6__otc_chain100__R100 | K records, K = 5 | 3.48 | 11.8 | 1.81 | 15.43% | 49.38% | 74.69% | — | 16.15% | 13.69% | badly miscalibrated |
| c6__otc_chain50__R1 | K records, K = 1 | 5.83 | 57.2 | 4.39 | 4.51% | 17.58% | 29.22% | 3.46%, 5.67%, 6.36% (173) | 3.35% | 4.25% |  |
| c6__otc_chain50__R1 | K records, K = 2 | 4.71 | 26.9 | 3.01 | 7.66% | 26.32% | 55.02% | 2.91%, 10.70%, 12.79% (86) | 5.81% | 9.21% |  |
| c6__otc_chain50__R1 | K records, K = 3 | 3.67 | 13.7 | 2.05 | 13.04% | 47.10% | 73.91% | 9.81%, 15.44%, 17.54% (57) | 16.03% | 14.79% | badly miscalibrated |
| c6__otc_chain50__R1 | K records, K = 5 | 2.19 | 5.1 | 1.15 | 20.48% | 87.95% | 98.80% | 22.06%, 25.59%, 26.47% (34) | 28.31% | 20.82% | badly miscalibrated |
| c6__otc_chain50__R1 | K records, K = 10 | 0.33 | 1.3 | 0.13 | 92.68% | 100.00% | 100.00% | 91.18%, 93.53%, 94.12% (17) | 5.27% | 13.15% |  |
| c6__otc_chain50__R1 | K records, K = 20 | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | — | 0.00% | 0.00% |  |
| c6__otc_chain50__R100 | K records, K = 1 | 6.81 | 112.5 | 5.22 | 2.45% | 11.37% | 19.22% | 0.00%, 28.00%, 38.46% (13) | 0.78% | 1.77% |  |
| c6__otc_chain50__R100 | K records, K = 2 | 5.68 | 52.7 | 3.68 | 2.87% | 19.92% | 35.82% | 10.00%, 10.00%, 10.00% (10) | 5.41% | 4.55% | badly miscalibrated |
| c6__otc_chain50__R100 | K records, K = 3 | 4.69 | 26.9 | 2.70 | 8.28% | 35.17% | 58.28% | — | 8.61% | 8.45% | badly miscalibrated |
| c6__otc_chain50__R100 | K records, K = 5 | 2.96 | 8.5 | 1.53 | 24.17% | 75.00% | 91.67% | — | 20.74% | 16.12% | badly miscalibrated |
| c6_issuer__iwh_delay_L10__R1 | iwh_delay_L10 | 6.30 | 79.3 | 5.43 | 0.00% | 0.00% | 0.00% | — | 2.32% | 34.22% |  |
| c6_issuer__iwh_delay_L10__R100 | iwh_delay_L10 | 7.27 | 154.3 | 6.33 | 0.00% | 0.00% | 0.00% | — | 1.25% | 49.95% |  |
| c6_issuer__iwh_delay_L120__R1 | iwh_delay_L120 | 6.38 | 83.9 | 5.51 | 23.08% | 23.08% | 30.77% | — | 9.51% | 16.64% |  |
| c6_issuer__iwh_delay_L120__R100 | iwh_delay_L120 | 7.31 | 159.5 | 6.42 | 50.00% | 50.00% | 50.00% | — | 1.17% | 9.32% |  |
| c6_issuer__iwh_delay_L30__R1 | iwh_delay_L30 | 6.42 | 86.5 | 5.57 | 28.57% | 28.57% | 28.57% | — | 2.13% | 16.12% |  |
| c6_issuer__iwh_delay_L30__R100 | iwh_delay_L30 | 7.33 | 161.4 | 6.45 | 28.57% | 28.57% | 28.57% | — | 1.14% | 15.12% |  |
| c6_issuer__iwh_delay_L60__R1 | iwh_delay_L60 | 6.37 | 83.1 | 5.51 | 10.00% | 10.00% | 10.00% | — | 2.21% | 21.31% |  |
| c6_issuer__iwh_delay_L60__R100 | iwh_delay_L60 | 7.32 | 160.0 | 6.46 | 36.36% | 36.36% | 36.36% | — | 1.14% | 10.13% |  |
| c6_issuer__iwh_none_L10__R1 | iwh_none_L10 | 6.30 | 79.3 | 5.43 | 0.00% | 0.00% | 0.00% | — | 2.32% | 34.22% |  |
| c6_issuer__iwh_none_L10__R100 | iwh_none_L10 | 7.27 | 154.3 | 6.33 | 0.00% | 0.00% | 0.00% | — | 1.25% | 49.95% |  |
| c6_issuer__iwh_none_L120__R1 | iwh_none_L120 | 6.38 | 83.7 | 5.52 | 23.08% | 23.08% | 30.77% | — | 9.52% | 16.63% |  |
| c6_issuer__iwh_none_L120__R100 | iwh_none_L120 | 7.31 | 159.6 | 6.42 | 50.00% | 50.00% | 50.00% | — | 1.17% | 9.32% |  |
| c6_issuer__iwh_none_L30__R1 | iwh_none_L30 | 6.42 | 86.5 | 5.57 | 28.57% | 28.57% | 28.57% | — | 2.13% | 16.12% |  |
| c6_issuer__iwh_none_L30__R100 | iwh_none_L30 | 7.33 | 161.4 | 6.45 | 28.57% | 28.57% | 28.57% | — | 1.14% | 15.12% |  |
| c6_issuer__iwh_none_L60__R1 | iwh_none_L60 | 6.37 | 83.1 | 5.51 | 10.00% | 10.00% | 10.00% | — | 2.21% | 21.31% |  |
| c6_issuer__iwh_none_L60__R100 | iwh_none_L60 | 7.32 | 160.0 | 6.46 | 36.36% | 36.36% | 36.36% | — | 1.14% | 10.13% |  |
| c6_issuer__iwh_withhold_L10__R1 | iwh_withhold_L10 | 6.30 | 79.3 | 5.43 | 0.00% | 0.00% | 0.00% | — | 2.32% | 34.22% |  |
| c6_issuer__iwh_withhold_L10__R100 | iwh_withhold_L10 | 7.27 | 154.3 | 6.33 | 0.00% | 0.00% | 0.00% | — | 1.25% | 49.95% |  |
| c6_issuer__iwh_withhold_L120__R1 | iwh_withhold_L120 | 6.38 | 83.9 | 5.51 | 23.08% | 23.08% | 30.77% | — | 9.51% | 16.64% |  |
| c6_issuer__iwh_withhold_L120__R100 | iwh_withhold_L120 | 7.31 | 159.5 | 6.42 | 50.00% | 50.00% | 50.00% | — | 1.17% | 9.32% |  |
| c6_issuer__iwh_withhold_L30__R1 | iwh_withhold_L30 | 6.42 | 86.5 | 5.57 | 28.57% | 28.57% | 28.57% | — | 2.13% | 16.12% |  |
| c6_issuer__iwh_withhold_L30__R100 | iwh_withhold_L30 | 7.33 | 161.4 | 6.45 | 28.57% | 28.57% | 28.57% | — | 1.14% | 15.12% |  |
| c6_issuer__iwh_withhold_L60__R1 | iwh_withhold_L60 | 6.37 | 83.1 | 5.51 | 10.00% | 10.00% | 10.00% | — | 2.21% | 21.31% |  |
| c6_issuer__iwh_withhold_L60__R100 | iwh_withhold_L60 | 7.32 | 160.0 | 6.46 | 36.36% | 36.36% | 36.36% | — | 1.14% | 10.13% |  |

## Reliability

Per row, the confidence deciles: mean confidence → hit rate.

- c6__cp_W0__R1, observer: 3.3 → 11.9; 3.7 → 2.4; 4.0 → 14.3; 4.4 → 4.9; 4.9 → 7.3; 5.4 → 7.3; 6.0 → 2.4; 6.5 → 4.9; 7.3 → 2.4; 9.2 → 9.8
- c6__cp_W0__R1, first_hop: 3.3 → 10.9; 3.7 → 3.5; 4.0 → 11.6; 4.4 → 7.9; 4.9 → 7.1; 5.4 → 6.7; 5.9 → 1.8; 6.5 → 4.6; 7.3 → 2.4; 9.2 → 9.3
- c6__cp_W0__R1, content_server: 3.5 → 6.0; 4.0 → 3.6; 4.4 → 9.6; 5.0 → 15.7; 5.5 → 6.0; 6.1 → 2.4; 6.8 → 2.4; 7.6 → 3.7; 8.9 → 6.1; 12.0 → 8.5
- c6__cp_W0__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_W0__R100, observer: 1.9 → 2.5; 2.0 → 3.3; 2.1 → 2.5; 2.2 → 0.8; 2.3 → 0.8; 2.3 → 1.6; 2.4 → 1.7; 2.7 → 1.7; 2.9 → 0.0; 3.4 → 2.5
- c6__cp_W0__R100, first_hop: 1.9 → 2.4; 2.0 → 3.3; 2.1 → 2.1; 2.2 → 0.9; 2.3 → 0.8; 2.3 → 1.6; 2.4 → 2.4; 2.7 → 1.5; 2.9 → 0.0; 3.4 → 2.5
- c6__cp_W0__R100, content_server: 2.0 → 3.3; 2.2 → 3.3; 2.3 → 2.9; 2.4 → 2.9; 2.6 → 1.6; 2.7 → 2.9; 2.9 → 1.2; 3.1 → 1.6; 3.3 → 2.9; 4.0 → 3.3
- c6__cp_W0__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_W1__R1, observer: 3.4 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.0 → 0.0; 4.1 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.4 → 0.0
- c6__cp_W1__R1, first_hop: 3.4 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 4.0 → 0.0; 4.1 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.4 → 0.0
- c6__cp_W1__R1, content_server: 3.5 → 1.3; 3.8 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.4 → 1.3; 4.6 → 0.0; 4.7 → 0.0; 5.0 → 0.0; 5.3 → 1.3; 6.0 → 0.0
- c6__cp_W1__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_W1__R100, observer: 3.3 → 2.3; 3.7 → 4.5; 4.0 → 3.8; 4.4 → 6.1; 5.0 → 5.3; 5.4 → 6.1; 5.9 → 6.1; 6.5 → 10.7; 7.0 → 13.0; 7.7 → 11.5
- c6__cp_W1__R100, first_hop: 3.3 → 2.4; 3.7 → 4.6; 4.0 → 4.0; 4.4 → 6.3; 5.0 → 5.1; 5.4 → 6.1; 5.9 → 6.1; 6.5 → 10.4; 7.0 → 12.6; 7.7 → 11.7
- c6__cp_W1__R100, content_server: 3.4 → 4.2; 3.9 → 6.8; 4.2 → 5.7; 4.6 → 5.7; 5.1 → 5.3; 5.5 → 7.3; 6.0 → 6.9; 6.5 → 6.9; 7.2 → 11.5; 8.1 → 10.3
- c6__cp_W1__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_W2__R1, observer: 3.8 → 5.4; 4.3 → 16.2; 4.9 → 8.1; 5.5 → 21.6; 6.1 → 18.9; 6.9 → 2.7; 7.6 → 0.0; 8.8 → 8.3; 10.8 → 0.0; 19.4 → 0.0
- c6__cp_W2__R1, first_hop: 3.8 → 6.1; 4.3 → 17.9; 4.9 → 8.2; 5.5 → 19.3; 6.1 → 19.0; 6.8 → 4.2; 7.6 → 0.4; 8.8 → 8.2; 10.7 → 0.0; 19.3 → 0.0
- c6__cp_W2__R1, content_server: 4.0 → 4.1; 4.6 → 4.1; 5.2 → 19.2; 5.8 → 12.3; 6.5 → 17.8; 7.2 → 15.1; 8.1 → 11.0; 9.3 → 4.1; 11.2 → 2.7; 20.4 → 0.0
- c6__cp_W2__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_W2__R100, observer: 3.5 → 4.9; 4.0 → 3.3; 4.4 → 1.6; 4.9 → 14.8; 5.4 → 9.0; 5.9 → 6.6; 6.4 → 4.9; 7.3 → 9.8; 8.5 → 10.7; 10.6 → 5.7
- c6__cp_W2__R100, first_hop: 3.5 → 4.8; 4.0 → 3.0; 4.3 → 1.7; 4.9 → 14.2; 5.4 → 9.2; 5.9 → 6.5; 6.4 → 5.5; 7.3 → 9.7; 8.5 → 10.6; 10.6 → 5.7
- c6__cp_W2__R100, content_server: 3.5 → 3.7; 4.1 → 3.3; 4.5 → 4.5; 5.0 → 6.6; 5.6 → 7.4; 6.1 → 8.2; 6.7 → 5.3; 7.5 → 9.8; 8.6 → 11.9; 11.2 → 7.8
- c6__cp_W2__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_Wmis__R1, observer: 4.8 → 0.0; 5.4 → 8.1; 5.9 → 0.0; 6.3 → 8.1; 6.8 → 8.1; 7.3 → 2.7; 8.0 → 27.8; 9.0 → 25.0; 10.8 → 41.7; 18.5 → 88.9
- c6__cp_Wmis__R1, first_hop: 4.7 → 0.0; 5.4 → 5.6; 5.8 → 3.1; 6.3 → 7.5; 6.7 → 8.3; 7.3 → 2.9; 8.0 → 25.0; 8.9 → 27.2; 10.7 → 39.9; 18.4 → 89.6
- c6__cp_Wmis__R1, content_server: 5.8 → 2.7; 6.9 → 10.8; 7.7 → 19.2; 8.9 → 12.3; 10.3 → 17.8; 11.6 → 15.1; 13.6 → 12.3; 16.2 → 19.2; 20.8 → 26.0; 32.9 → 69.9
- c6__cp_Wmis__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_Wmis__R100, observer: 5.3 → 4.9; 6.1 → 8.2; 7.0 → 7.4; 7.8 → 9.8; 8.9 → 5.7; 10.5 → 10.7; 12.0 → 9.8; 14.0 → 11.5; 16.8 → 12.3; 23.8 → 18.0
- c6__cp_Wmis__R100, first_hop: 5.3 → 5.3; 6.1 → 8.1; 7.0 → 6.5; 7.8 → 9.8; 8.9 → 6.4; 10.4 → 10.6; 12.0 → 10.1; 14.0 → 11.5; 16.8 → 11.8; 23.8 → 17.9
- c6__cp_Wmis__R100, content_server: 5.0 → 3.7; 5.9 → 4.5; 6.7 → 2.9; 7.7 → 8.2; 9.0 → 12.7; 10.6 → 6.1; 12.3 → 9.8; 14.3 → 11.5; 17.0 → 11.9; 24.5 → 20.5
- c6__cp_Wmis__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_chain100__R1, observer: 3.4 → 0.0; 3.8 → 9.5; 4.2 → 16.7; 4.5 → 4.8; 4.9 → 4.8; 5.5 → 9.5; 6.0 → 4.8; 6.6 → 16.7; 7.3 → 4.8; 9.1 → 0.0
- c6__cp_chain100__R1, first_hop: 3.4 → 0.5; 3.8 → 9.2; 4.2 → 15.1; 4.5 → 5.6; 4.9 → 5.7; 5.5 → 10.7; 6.0 → 6.2; 6.6 → 15.5; 7.3 → 5.2; 9.2 → 0.0
- c6__cp_chain100__R1, content_server: 3.6 → 4.8; 4.2 → 10.7; 4.6 → 11.9; 5.1 → 6.0; 5.5 → 8.3; 6.1 → 13.1; 6.8 → 6.0; 7.6 → 2.4; 8.9 → 6.0; 11.8 → 2.4
- c6__cp_chain100__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_chain100__R100, observer: 1.8 → 0.0; 2.0 → 1.6; 2.2 → 1.6; 2.4 → 0.8; 2.7 → 4.9; 3.1 → 1.6; 3.6 → 2.4; 3.9 → 2.4; 4.5 → 2.4; 5.6 → 0.0
- c6__cp_chain100__R100, first_hop: 1.8 → 0.0; 2.0 → 1.6; 2.2 → 1.7; 2.4 → 1.1; 2.7 → 4.5; 3.1 → 2.1; 3.6 → 1.9; 3.9 → 2.6; 4.5 → 2.6; 5.6 → 0.0
- c6__cp_chain100__R100, content_server: 3.1 → 2.8; 3.5 → 2.4; 3.8 → 3.2; 4.0 → 2.8; 4.3 → 2.0; 4.5 → 3.6; 4.9 → 4.0; 5.3 → 2.0; 5.8 → 3.3; 7.3 → 4.5
- c6__cp_chain100__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_chain50__R1, observer: 3.2 → 4.7; 3.6 → 9.5; 3.9 → 0.0; 4.1 → 7.1; 4.6 → 0.0; 5.2 → 16.7; 5.8 → 2.4; 6.5 → 2.4; 7.5 → 2.4; 9.2 → 0.0
- c6__cp_chain50__R1, first_hop: 3.2 → 4.8; 3.6 → 8.4; 3.9 → 1.1; 4.1 → 6.3; 4.5 → 0.2; 5.2 → 17.5; 5.8 → 2.1; 6.5 → 2.3; 7.4 → 2.0; 9.2 → 0.4
- c6__cp_chain50__R1, content_server: 3.4 → 2.4; 3.9 → 4.7; 4.2 → 3.6; 4.7 → 4.8; 5.2 → 9.5; 5.8 → 14.3; 6.6 → 6.0; 7.3 → 0.0; 8.4 → 3.6; 11.0 → 2.4
- c6__cp_chain50__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_chain50__R100, observer: 1.7 → 1.6; 1.8 → 0.8; 2.0 → 2.4; 2.1 → 2.4; 2.3 → 5.6; 2.9 → 0.8; 3.3 → 3.2; 3.7 → 1.6; 4.3 → 1.6; 5.9 → 1.6
- c6__cp_chain50__R100, first_hop: 1.7 → 1.8; 1.8 → 1.0; 2.0 → 2.6; 2.1 → 1.9; 2.3 → 5.7; 2.9 → 0.8; 3.3 → 3.0; 3.7 → 1.5; 4.3 → 1.7; 5.9 → 1.7
- c6__cp_chain50__R100, content_server: 1.8 → 0.8; 2.1 → 3.2; 2.2 → 3.6; 2.4 → 2.4; 2.8 → 3.2; 3.3 → 2.8; 3.8 → 3.6; 4.4 → 2.8; 5.2 → 3.2; 7.0 → 4.0
- c6__cp_chain50__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W0__R1, observer: 3.9 → 4.8; 4.3 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 5.0 → 2.4; 5.3 → 0.0; 5.5 → 4.9; 5.8 → 0.0; 6.3 → 12.2; 7.1 → 2.4
- c6__otcL_W0__R1, first_hop: 3.0 → 0.8; 3.3 → 2.5; 3.5 → 4.6; 3.8 → 0.8; 4.0 → 14.5; 4.3 → 1.3; 4.7 → 1.3; 5.0 → 0.5; 5.6 → 0.5; 6.6 → 2.3
- c6__otcL_W0__R1, destination: 3.1 → 2.4; 3.5 → 9.5; 3.8 → 7.1; 4.0 → 4.9; 4.3 → 4.9; 4.7 → 4.9; 5.1 → 2.4; 5.6 → 0.0; 6.2 → 2.4; 7.3 → 2.4
- c6__otcL_W0__R1, destination_keyed: 8.6 → 21.4; 9.7 → 16.7; 10.6 → 11.9; 11.2 → 17.1; 11.8 → 7.3; 12.5 → 19.5; 13.4 → 19.5; 14.4 → 24.4; 16.1 → 4.9; 19.8 → 12.2
- c6__otcL_W0__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W0__R1, issuer_0 [share 50%, all records]: 2.8 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.6 → 0.0; 3.7 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 3.9 → 0.0
- c6__otcL_W0__R1, issuer_0 [share 50%, other issuers' devices]: 2.8 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.6 → 0.0; 3.7 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 3.9 → 0.0
- c6__otcL_W0__R1, issuer_0_with_observer [share 50%, all records]: 3.1 → 2.4; 3.4 → 4.8; 3.7 → 2.4; 3.9 → 12.2; 4.2 → 2.4; 4.5 → 0.0; 4.9 → 0.0; 5.3 → 0.0; 5.9 → 0.0; 7.1 → 2.4
- c6__otcL_W0__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 3.1 → 2.4; 3.4 → 4.8; 3.7 → 2.4; 3.9 → 12.2; 4.2 → 2.4; 4.5 → 0.0; 4.9 → 0.0; 5.3 → 0.0; 5.9 → 0.0; 7.1 → 2.4
- c6__otcL_W0__R1, issuer_0_with_first_relay [share 50%, all records]: 3.1 → 2.4; 3.4 → 4.8; 3.7 → 2.4; 3.9 → 9.8; 4.2 → 2.4; 4.5 → 0.0; 5.0 → 4.9; 5.3 → 0.0; 5.9 → 0.0; 7.1 → 2.4
- c6__otcL_W0__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.1 → 2.4; 3.4 → 4.8; 3.7 → 2.4; 3.9 → 9.8; 4.2 → 2.4; 4.5 → 0.0; 5.0 → 4.9; 5.3 → 0.0; 5.9 → 0.0; 7.1 → 2.4
- c6__otcL_W0__R1, issuer_1 [share 30%, all records]: 3.4 → 2.4; 3.5 → 19.0; 3.5 → 7.1; 3.5 → 9.8; 3.5 → 22.0; 8.5 → 4.9; 15.0 → 4.9; 18.6 → 7.3; 21.5 → 4.9; 25.6 → 0.0
- c6__otcL_W0__R1, issuer_1 [share 30%, its own devices]: 3.4 → 2.4; 3.5 → 19.0; 3.5 → 7.1; 3.5 → 9.8; 3.5 → 22.0; 8.5 → 4.9; 15.0 → 4.9; 18.6 → 7.3; 21.5 → 4.9; 25.6 → 0.0
- c6__otcL_W0__R1, issuer_1_with_observer [share 30%, all records]: 4.0 → 0.0; 4.4 → 4.8; 4.7 → 7.1; 5.0 → 2.4; 5.2 → 4.9; 5.5 → 0.0; 5.8 → 9.8; 6.2 → 4.9; 6.8 → 2.4; 8.2 → 24.4
- c6__otcL_W0__R1, issuer_1_with_observer [share 30%, its own devices]: 4.0 → 0.0; 4.4 → 4.8; 4.7 → 7.1; 5.0 → 2.4; 5.2 → 4.9; 5.5 → 0.0; 5.8 → 9.8; 6.2 → 4.9; 6.8 → 2.4; 8.2 → 24.4
- c6__otcL_W0__R1, issuer_1_with_first_relay [share 30%, all records]: 3.1 → 4.8; 3.4 → 7.1; 3.7 → 4.8; 3.9 → 9.8; 4.2 → 4.9; 4.5 → 2.4; 4.8 → 7.3; 5.3 → 0.0; 5.8 → 7.3; 7.5 → 9.8
- c6__otcL_W0__R1, issuer_1_with_first_relay [share 30%, its own devices]: 3.1 → 4.8; 3.4 → 7.1; 3.7 → 4.8; 3.9 → 9.8; 4.2 → 4.9; 4.5 → 2.4; 4.8 → 7.3; 5.3 → 0.0; 5.8 → 7.3; 7.5 → 9.8
- c6__otcL_W0__R1, issuer_1_with_destination: 8.7 → 7.1; 10.1 → 23.8; 11.0 → 14.3; 11.6 → 14.6; 12.5 → 9.8; 13.4 → 19.5; 14.4 → 24.4; 15.5 → 19.5; 17.0 → 7.3; 22.2 → 17.1
- c6__otcL_W0__R1, issuer_2 [share 20%, all records]: 5.2 → 0.0; 5.8 → 0.0; 6.0 → 0.0; 6.4 → 0.0; 6.8 → 0.0; 7.1 → 0.0; 7.4 → 0.0; 7.8 → 0.0; 8.4 → 0.0; 9.0 → 0.0
- c6__otcL_W0__R1, issuer_2 [share 20%, other issuers' devices]: 5.2 → 0.0; 5.8 → 0.0; 6.0 → 0.0; 6.4 → 0.0; 6.8 → 0.0; 7.1 → 0.0; 7.4 → 0.0; 7.8 → 0.0; 8.4 → 0.0; 9.0 → 0.0
- c6__otcL_W0__R1, issuer_2_with_observer [share 20%, all records]: 3.1 → 2.4; 3.4 → 4.8; 3.6 → 2.4; 3.9 → 12.2; 4.2 → 4.9; 4.5 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 5.7 → 0.0; 7.4 → 2.4
- c6__otcL_W0__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 3.1 → 2.4; 3.4 → 4.8; 3.6 → 2.4; 3.9 → 12.2; 4.2 → 4.9; 4.5 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 5.7 → 0.0; 7.4 → 2.4
- c6__otcL_W0__R1, issuer_2_with_first_relay [share 20%, all records]: 3.1 → 2.4; 3.4 → 4.8; 3.7 → 2.4; 3.9 → 9.8; 4.2 → 2.4; 4.5 → 0.0; 4.9 → 0.0; 5.2 → 4.9; 5.7 → 0.0; 7.4 → 2.4
- c6__otcL_W0__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.1 → 2.4; 3.4 → 4.8; 3.7 → 2.4; 3.9 → 9.8; 4.2 → 2.4; 4.5 → 0.0; 4.9 → 0.0; 5.2 → 4.9; 5.7 → 0.0; 7.4 → 2.4
- c6__otcL_W0__R100, observer: 2.3 → 4.9; 2.5 → 2.5; 2.6 → 0.8; 2.7 → 1.6; 2.8 → 2.5; 3.0 → 3.3; 3.2 → 0.8; 3.4 → 4.1; 3.6 → 4.1; 4.2 → 4.1
- c6__otcL_W0__R100, first_hop: 2.3 → 4.5; 2.5 → 2.5; 2.6 → 1.4; 2.7 → 1.9; 2.9 → 2.9; 3.0 → 3.4; 3.2 → 0.9; 3.4 → 3.5; 3.6 → 4.0; 4.3 → 4.4
- c6__otcL_W0__R100, destination: 2.5 → 2.5; 2.7 → 2.5; 2.9 → 2.5; 3.0 → 2.5; 3.1 → 3.3; 3.3 → 5.7; 3.5 → 1.7; 3.7 → 3.3; 4.0 → 1.7; 4.8 → 2.5
- c6__otcL_W0__R100, destination_keyed: 4.6 → 4.1; 5.1 → 6.6; 5.6 → 4.1; 6.1 → 7.4; 6.7 → 6.6; 7.5 → 7.4; 8.5 → 6.6; 9.6 → 6.6; 11.2 → 11.6; 15.1 → 11.6
- c6__otcL_W0__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W0__R100, issuer_0 [share 50%, all records]: 3.2 → 0.0; 3.3 → 1.6; 3.4 → 4.1; 3.4 → 3.3; 3.5 → 0.8; 3.7 → 1.6; 3.8 → 1.7; 3.9 → 1.7; 4.0 → 0.0; 4.2 → 0.0
- c6__otcL_W0__R100, issuer_0 [share 50%, its own devices]: 3.2 → 1.5; 3.3 → 1.5; 3.4 → 7.5; 3.4 → 6.1; 3.5 → 3.0; 3.7 → 1.5; 3.8 → 3.0; 3.9 → 3.0; 4.0 → 0.0; 4.2 → 0.0
- c6__otcL_W0__R100, issuer_0 [share 50%, other issuers' devices]: 2.4 → 0.0; 2.4 → 0.0; 2.4 → 0.0; 2.5 → 0.0; 2.6 → 0.0; 2.7 → 0.0; 2.8 → 0.0; 2.8 → 0.0; 2.8 → 0.0; 2.9 → 0.0
- c6__otcL_W0__R100, issuer_0_with_observer [share 50%, all records]: 2.3 → 2.5; 2.6 → 0.8; 2.7 → 1.6; 2.8 → 4.9; 2.9 → 4.1; 3.1 → 2.5; 3.4 → 3.3; 3.6 → 5.0; 3.9 → 0.8; 4.8 → 4.1
- c6__otcL_W0__R100, issuer_0_with_observer [share 50%, its own devices]: 2.3 → 4.5; 2.6 → 1.5; 2.7 → 0.0; 2.8 → 4.5; 2.9 → 7.6; 3.1 → 4.5; 3.3 → 1.5; 3.6 → 7.6; 3.9 → 0.0; 4.8 → 3.0
- c6__otcL_W0__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.3 → 0.0; 2.6 → 0.0; 2.7 → 3.6; 2.8 → 3.6; 3.0 → 1.8; 3.2 → 0.0; 3.4 → 3.6; 3.7 → 3.6; 3.9 → 1.8; 4.7 → 5.5
- c6__otcL_W0__R100, issuer_0_with_first_relay [share 50%, all records]: 2.3 → 2.5; 2.6 → 1.6; 2.7 → 2.5; 2.8 → 4.9; 3.0 → 2.5; 3.2 → 4.1; 3.4 → 5.0; 3.7 → 3.3; 3.9 → 0.0; 4.7 → 4.1
- c6__otcL_W0__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.3 → 4.5; 2.6 → 1.5; 2.7 → 0.0; 2.8 → 6.1; 3.0 → 3.0; 3.2 → 3.0; 3.4 → 9.1; 3.6 → 1.5; 3.9 → 0.0; 4.8 → 3.0
- c6__otcL_W0__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.3 → 0.0; 2.6 → 1.8; 2.7 → 5.4; 2.8 → 3.6; 3.0 → 1.8; 3.2 → 5.5; 3.4 → 1.8; 3.7 → 3.6; 3.9 → 0.0; 4.7 → 5.5
- c6__otcL_W0__R100, issuer_0_with_destination: 4.4 → 7.5; 4.9 → 7.5; 5.2 → 6.0; 5.5 → 4.5; 5.8 → 9.1; 6.1 → 9.1; 6.6 → 3.0; 7.1 → 6.1; 8.0 → 7.6; 9.8 → 7.6
- c6__otcL_W0__R100, issuer_1 [share 30%, all records]: 5.7 → 0.8; 6.0 → 0.0; 6.2 → 0.0; 6.3 → 0.8; 6.5 → 0.0; 6.7 → 0.8; 7.0 → 2.5; 7.4 → 1.7; 7.7 → 0.8; 8.2 → 4.1
- c6__otcL_W0__R100, issuer_1 [share 30%, its own devices]: 5.8 → 3.0; 6.2 → 0.0; 6.3 → 0.0; 6.4 → 3.1; 6.6 → 0.0; 6.9 → 9.4; 7.1 → 6.2; 7.4 → 3.1; 7.6 → 3.1; 8.2 → 15.6
- c6__otcL_W0__R100, issuer_1 [share 30%, other issuers' devices]: 4.4 → 0.0; 4.6 → 0.0; 4.7 → 0.0; 4.8 → 0.0; 4.9 → 0.0; 5.0 → 0.0; 5.1 → 0.0; 5.2 → 0.0; 5.3 → 0.0; 5.5 → 0.0
- c6__otcL_W0__R100, issuer_1_with_observer [share 30%, all records]: 2.3 → 3.3; 2.6 → 0.8; 2.7 → 1.6; 2.8 → 2.5; 3.0 → 1.6; 3.1 → 3.3; 3.2 → 0.0; 3.4 → 3.3; 3.6 → 4.1; 4.2 → 5.0
- c6__otcL_W0__R100, issuer_1_with_observer [share 30%, its own devices]: 2.3 → 0.0; 2.6 → 3.0; 2.7 → 6.1; 2.8 → 6.2; 3.0 → 0.0; 3.1 → 3.1; 3.2 → 0.0; 3.4 → 3.1; 3.6 → 9.4; 4.2 → 12.5
- c6__otcL_W0__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.3 → 4.4; 2.6 → 0.0; 2.7 → 1.1; 2.8 → 0.0; 3.0 → 2.2; 3.1 → 3.4; 3.2 → 0.0; 3.4 → 3.4; 3.6 → 2.2; 4.2 → 2.2
- c6__otcL_W0__R100, issuer_1_with_first_relay [share 30%, all records]: 2.3 → 4.1; 2.6 → 0.8; 2.7 → 4.9; 2.8 → 3.3; 3.0 → 1.6; 3.1 → 0.8; 3.3 → 2.5; 3.5 → 3.3; 3.7 → 1.7; 4.3 → 5.0
- c6__otcL_W0__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.3 → 0.0; 2.6 → 3.0; 2.7 → 6.1; 2.8 → 6.2; 3.0 → 6.2; 3.1 → 0.0; 3.3 → 0.0; 3.5 → 6.2; 3.6 → 6.2; 4.3 → 12.5
- c6__otcL_W0__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.3 → 5.6; 2.6 → 1.1; 2.7 → 3.3; 2.9 → 2.2; 3.0 → 0.0; 3.1 → 1.1; 3.3 → 3.4; 3.5 → 2.2; 3.7 → 0.0; 4.2 → 2.2
- c6__otcL_W0__R100, issuer_1_with_destination: 6.5 → 6.1; 7.4 → 0.0; 8.0 → 9.1; 8.5 → 3.1; 9.0 → 3.1; 9.6 → 15.6; 10.1 → 3.1; 10.8 → 18.8; 12.0 → 18.8; 15.1 → 9.4
- c6__otcL_W0__R100, issuer_2 [share 20%, all records]: 5.4 → 0.0; 6.3 → 0.0; 6.9 → 0.0; 7.2 → 3.3; 7.5 → 1.6; 8.6 → 0.8; 9.9 → 0.0; 10.7 → 0.0; 11.4 → 1.7; 12.3 → 0.8
- c6__otcL_W0__R100, issuer_2 [share 20%, its own devices]: 5.5 → 0.0; 6.7 → 0.0; 7.1 → 4.3; 7.3 → 13.0; 7.6 → 13.0; 9.1 → 0.0; 10.1 → 0.0; 10.7 → 0.0; 11.3 → 8.7; 12.4 → 4.3
- c6__otcL_W0__R100, issuer_2 [share 20%, other issuers' devices]: 5.0 → 0.0; 5.5 → 0.0; 5.8 → 0.0; 6.0 → 0.0; 6.2 → 0.0; 6.6 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.5 → 0.0; 7.7 → 0.0
- c6__otcL_W0__R100, issuer_2_with_observer [share 20%, all records]: 2.3 → 2.5; 2.6 → 2.5; 2.7 → 2.5; 2.8 → 1.6; 2.9 → 1.6; 3.1 → 3.3; 3.3 → 1.7; 3.4 → 2.5; 3.7 → 4.1; 4.2 → 4.1
- c6__otcL_W0__R100, issuer_2_with_observer [share 20%, its own devices]: 2.3 → 0.0; 2.6 → 0.0; 2.6 → 8.7; 2.7 → 0.0; 3.0 → 0.0; 3.1 → 0.0; 3.3 → 0.0; 3.4 → 4.3; 3.7 → 0.0; 4.4 → 0.0
- c6__otcL_W0__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.3 → 3.0; 2.6 → 3.0; 2.7 → 1.0; 2.8 → 2.0; 2.9 → 2.0; 3.1 → 4.0; 3.3 → 2.0; 3.4 → 2.0; 3.6 → 4.1; 4.2 → 6.1
- c6__otcL_W0__R100, issuer_2_with_first_relay [share 20%, all records]: 2.3 → 2.5; 2.6 → 0.8; 2.7 → 4.9; 2.8 → 1.6; 2.9 → 2.5; 3.1 → 2.5; 3.3 → 1.7; 3.4 → 3.3; 3.7 → 3.3; 4.2 → 4.1
- c6__otcL_W0__R100, issuer_2_with_first_relay [share 20%, its own devices]: 2.3 → 0.0; 2.5 → 4.3; 2.7 → 4.3; 2.8 → 4.3; 2.9 → 0.0; 3.1 → 0.0; 3.3 → 4.3; 3.4 → 0.0; 3.7 → 0.0; 4.4 → 0.0
- c6__otcL_W0__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.3 → 3.0; 2.6 → 0.0; 2.7 → 5.1; 2.8 → 2.0; 2.9 → 2.0; 3.1 → 3.0; 3.3 → 2.0; 3.4 → 3.1; 3.7 → 4.1; 4.2 → 5.1
- c6__otcL_W0__R100, issuer_2_with_destination: 5.8 → 13.0; 6.7 → 4.3; 7.2 → 0.0; 7.6 → 8.7; 8.1 → 8.7; 8.5 → 8.7; 9.1 → 8.7; 9.7 → 4.3; 10.4 → 13.0; 12.4 → 17.4
- c6__otcL_W1__R1, observer: 3.0 → 0.0; 3.3 → 5.1; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otcL_W1__R1, first_hop: 3.0 → 1.2; 3.3 → 4.9; 3.5 → 0.5; 3.7 → 0.1; 4.0 → 0.0; 4.2 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otcL_W1__R1, destination: 3.1 → 7.7; 3.4 → 5.1; 3.7 → 0.0; 3.9 → 0.0; 4.2 → 0.0; 4.5 → 0.0; 4.7 → 0.0; 5.1 → 0.0; 5.5 → 0.0; 6.4 → 0.0
- c6__otcL_W1__R1, destination_keyed: 8.4 → 7.7; 9.7 → 7.7; 10.5 → 2.6; 11.5 → 12.8; 12.1 → 5.1; 12.8 → 2.6; 13.7 → 2.6; 14.8 → 2.6; 16.3 → 10.5; 20.6 → 5.3
- c6__otcL_W1__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W1__R1, issuer_0 [share 50%, all records]: 8.3 → 0.0; 8.6 → 0.0; 8.8 → 0.0; 9.0 → 0.0; 9.1 → 0.0; 9.2 → 0.0; 9.4 → 0.0; 9.6 → 0.0; 9.9 → 0.0; 10.4 → 0.0
- c6__otcL_W1__R1, issuer_0 [share 50%, other issuers' devices]: 8.3 → 0.0; 8.6 → 0.0; 8.8 → 0.0; 9.0 → 0.0; 9.1 → 0.0; 9.2 → 0.0; 9.4 → 0.0; 9.6 → 0.0; 9.9 → 0.0; 10.4 → 0.0
- c6__otcL_W1__R1, issuer_0_with_observer [share 50%, all records]: 3.0 → 0.0; 3.3 → 5.1; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 3.0 → 0.0; 3.3 → 5.1; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R1, issuer_0_with_first_relay [share 50%, all records]: 3.0 → 5.1; 3.3 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.0 → 5.1; 3.3 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R1, issuer_1 [share 30%, all records]: 6.1 → 0.0; 6.2 → 0.0; 6.3 → 0.0; 6.5 → 0.0; 7.2 → 0.0; 8.5 → 0.0; 8.7 → 0.0; 8.8 → 0.0; 9.1 → 0.0; 9.5 → 0.0
- c6__otcL_W1__R1, issuer_1 [share 30%, its own devices]: 6.1 → 0.0; 6.2 → 0.0; 6.3 → 0.0; 6.5 → 0.0; 7.2 → 0.0; 8.5 → 0.0; 8.7 → 0.0; 8.8 → 0.0; 9.1 → 0.0; 9.5 → 0.0
- c6__otcL_W1__R1, issuer_1_with_observer [share 30%, all records]: 3.0 → 2.6; 3.3 → 5.1; 3.5 → 2.6; 3.7 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.5 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otcL_W1__R1, issuer_1_with_observer [share 30%, its own devices]: 3.0 → 2.6; 3.3 → 5.1; 3.5 → 2.6; 3.7 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.5 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otcL_W1__R1, issuer_1_with_first_relay [share 30%, all records]: 3.0 → 7.7; 3.3 → 0.0; 3.5 → 2.6; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.3 → 0.0; 6.0 → 0.0
- c6__otcL_W1__R1, issuer_1_with_first_relay [share 30%, its own devices]: 3.0 → 7.7; 3.3 → 0.0; 3.5 → 2.6; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.3 → 0.0; 6.0 → 0.0
- c6__otcL_W1__R1, issuer_1_with_destination: 8.5 → 10.3; 9.8 → 7.7; 10.7 → 7.7; 11.5 → 12.8; 12.4 → 2.6; 13.2 → 5.1; 14.3 → 2.6; 15.5 → 10.3; 17.1 → 7.9; 21.1 → 7.9
- c6__otcL_W1__R1, issuer_2 [share 20%, all records]: 13.9 → 0.0; 14.2 → 0.0; 14.4 → 0.0; 14.6 → 0.0; 14.7 → 0.0; 14.9 → 0.0; 15.2 → 0.0; 15.6 → 0.0; 16.2 → 0.0; 17.1 → 0.0
- c6__otcL_W1__R1, issuer_2 [share 20%, other issuers' devices]: 13.9 → 0.0; 14.2 → 0.0; 14.4 → 0.0; 14.6 → 0.0; 14.7 → 0.0; 14.9 → 0.0; 15.2 → 0.0; 15.6 → 0.0; 16.2 → 0.0; 17.1 → 0.0
- c6__otcL_W1__R1, issuer_2_with_observer [share 20%, all records]: 3.0 → 0.0; 3.3 → 5.1; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 3.0 → 0.0; 3.3 → 5.1; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R1, issuer_2_with_first_relay [share 20%, all records]: 3.0 → 5.1; 3.3 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.3 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.0 → 5.1; 3.3 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.3 → 0.0; 6.1 → 0.0
- c6__otcL_W1__R100, observer: 3.5 → 2.3; 4.2 → 3.8; 4.7 → 3.8; 5.2 → 5.3; 5.7 → 3.8; 6.0 → 6.1; 6.4 → 6.9; 6.8 → 7.6; 7.4 → 4.6; 9.0 → 16.8
- c6__otcL_W1__R100, first_hop: 3.5 → 2.7; 4.2 → 4.0; 4.7 → 3.7; 5.2 → 5.8; 5.6 → 4.0; 6.0 → 6.5; 6.4 → 6.4; 6.8 → 7.2; 7.4 → 7.0; 9.0 → 14.6
- c6__otcL_W1__R100, destination: 3.6 → 3.8; 4.3 → 3.8; 4.9 → 6.9; 5.3 → 5.3; 5.7 → 5.3; 6.1 → 6.1; 6.6 → 8.4; 7.1 → 3.8; 7.7 → 6.9; 9.3 → 13.0
- c6__otcL_W1__R100, destination_keyed: 6.5 → 4.5; 8.3 → 5.3; 9.5 → 9.9; 10.6 → 5.3; 11.6 → 9.2; 12.6 → 8.4; 13.7 → 10.7; 15.3 → 10.7; 17.6 → 21.4; 23.8 → 35.1
- c6__otcL_W1__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W1__R100, issuer_0 [share 50%, all records]: 9.5 → 9.8; 9.7 → 15.2; 9.9 → 9.2; 10.0 → 13.0; 10.2 → 9.2; 10.5 → 0.0; 10.8 → 0.0; 11.3 → 0.0; 11.7 → 0.0; 12.2 → 0.0
- c6__otcL_W1__R100, issuer_0 [share 50%, its own devices]: 9.5 → 18.8; 9.7 → 29.0; 9.9 → 21.7; 10.0 → 30.4; 10.3 → 7.2; 10.5 → 0.0; 10.8 → 0.0; 11.3 → 0.0; 11.8 → 0.0; 12.2 → 0.0
- c6__otcL_W1__R100, issuer_0 [share 50%, other issuers' devices]: 6.5 → 0.0; 6.6 → 0.0; 6.8 → 0.0; 7.0 → 0.0; 7.4 → 0.0; 9.5 → 0.0; 9.7 → 0.0; 9.9 → 0.0; 10.0 → 0.0; 10.2 → 0.0
- c6__otcL_W1__R100, issuer_0_with_observer [share 50%, all records]: 3.5 → 5.3; 4.3 → 3.0; 4.8 → 5.3; 5.2 → 6.1; 5.7 → 6.1; 6.0 → 6.1; 6.4 → 8.4; 6.8 → 6.1; 7.5 → 2.3; 9.0 → 16.8
- c6__otcL_W1__R100, issuer_0_with_observer [share 50%, its own devices]: 3.5 → 5.8; 4.2 → 5.8; 4.7 → 4.3; 5.1 → 1.4; 5.6 → 7.2; 6.0 → 2.9; 6.4 → 11.6; 7.0 → 7.2; 7.6 → 7.2; 9.0 → 29.4
- c6__otcL_W1__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.3 → 4.8; 2.8 → 11.1; 3.1 → 3.2; 3.3 → 12.9; 3.6 → 11.3; 4.6 → 3.2; 6.0 → 0.0; 6.6 → 0.0; 7.2 → 0.0; 8.9 → 0.0
- c6__otcL_W1__R100, issuer_0_with_first_relay [share 50%, all records]: 3.6 → 3.8; 4.3 → 4.5; 4.8 → 4.6; 5.2 → 5.3; 5.6 → 4.6; 6.0 → 6.9; 6.5 → 9.9; 7.0 → 2.3; 7.6 → 6.9; 8.9 → 13.7
- c6__otcL_W1__R100, issuer_0_with_first_relay [share 50%, its own devices]: 3.5 → 5.8; 4.2 → 5.8; 4.7 → 2.9; 5.1 → 2.9; 5.6 → 4.3; 6.0 → 4.3; 6.5 → 13.0; 7.1 → 7.2; 7.7 → 5.8; 8.9 → 26.5
- c6__otcL_W1__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.4 → 1.6; 2.8 → 9.5; 3.1 → 3.2; 3.3 → 11.3; 3.7 → 14.5; 4.7 → 4.8; 6.0 → 0.0; 6.6 → 0.0; 7.3 → 0.0; 8.8 → 0.0
- c6__otcL_W1__R100, issuer_0_with_destination: 5.7 → 8.7; 6.4 → 2.9; 6.9 → 14.5; 7.4 → 5.8; 7.9 → 11.6; 8.4 → 7.2; 9.1 → 17.4; 9.9 → 13.0; 11.3 → 17.4; 13.6 → 5.9
- c6__otcL_W1__R100, issuer_1 [share 30%, all records]: 4.2 → 0.0; 4.3 → 0.0; 4.3 → 0.0; 4.3 → 0.0; 4.3 → 0.0; 4.8 → 0.0; 4.8 → 0.0; 4.9 → 0.0; 4.9 → 0.0; 4.9 → 0.0
- c6__otcL_W1__R100, issuer_1 [share 30%, its own devices]: 4.2 → 0.0; 4.3 → 0.0; 4.3 → 0.0; 4.3 → 0.0; 4.3 → 0.0; 4.8 → 0.0; 4.8 → 0.0; 4.9 → 0.0; 4.9 → 0.0; 4.9 → 0.0
- c6__otcL_W1__R100, issuer_1 [share 30%, other issuers' devices]: 7.0 → 0.0; 7.2 → 0.0; 7.6 → 0.0; 7.9 → 0.0; 8.1 → 0.0; 8.2 → 0.0; 8.4 → 0.0; 8.7 → 0.0; 9.2 → 0.0; 9.7 → 0.0
- c6__otcL_W1__R100, issuer_1_with_observer [share 30%, all records]: 3.5 → 3.8; 4.2 → 3.8; 4.7 → 3.8; 5.2 → 6.1; 5.7 → 4.6; 6.0 → 4.6; 6.3 → 7.6; 6.8 → 7.6; 7.3 → 4.6; 9.0 → 16.8
- c6__otcL_W1__R100, issuer_1_with_observer [share 30%, its own devices]: 2.3 → 3.2; 2.8 → 0.0; 3.0 → 0.0; 3.3 → 3.2; 3.5 → 0.0; 4.3 → 0.0; 5.8 → 0.0; 6.5 → 0.0; 7.1 → 0.0; 9.0 → 0.0
- c6__otcL_W1__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 3.5 → 4.0; 4.2 → 5.0; 4.7 → 5.0; 5.2 → 7.9; 5.7 → 5.0; 6.0 → 5.9; 6.4 → 10.0; 6.8 → 10.0; 7.4 → 6.0; 9.0 → 22.0
- c6__otcL_W1__R100, issuer_1_with_first_relay [share 30%, all records]: 3.5 → 3.8; 4.2 → 3.8; 4.7 → 3.8; 5.2 → 6.1; 5.6 → 5.3; 6.0 → 3.8; 6.4 → 7.6; 6.9 → 6.9; 7.5 → 9.2; 9.0 → 13.7
- c6__otcL_W1__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.3 → 3.2; 2.8 → 0.0; 3.0 → 0.0; 3.2 → 3.2; 3.6 → 0.0; 4.4 → 3.2; 5.8 → 0.0; 6.5 → 0.0; 7.2 → 0.0; 8.9 → 0.0
- c6__otcL_W1__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.5 → 4.0; 4.2 → 4.0; 4.7 → 5.0; 5.2 → 7.9; 5.6 → 5.9; 6.0 → 5.0; 6.5 → 11.0; 6.9 → 9.0; 7.5 → 11.0; 9.0 → 18.0
- c6__otcL_W1__R100, issuer_1_with_destination: 6.7 → 16.1; 7.5 → 6.5; 8.1 → 6.5; 8.9 → 12.9; 9.9 → 3.2; 10.7 → 6.5; 11.6 → 10.0; 12.4 → 0.0; 14.3 → 20.0; 18.7 → 6.7
- c6__otcL_W1__R100, issuer_2 [share 20%, all records]: 21.5 → 4.5; 23.2 → 11.4; 24.0 → 8.4; 25.4 → 2.3; 26.9 → 4.6; 32.9 → 6.1; 35.2 → 6.9; 36.0 → 3.8; 36.9 → 6.9; 41.3 → 2.3
- c6__otcL_W1__R100, issuer_2 [share 20%, its own devices]: 21.6 → 18.8; 23.2 → 46.9; 23.9 → 31.2; 25.3 → 15.6; 28.8 → 28.1; 34.2 → 25.0; 35.5 → 15.6; 36.1 → 16.1; 36.9 → 19.4; 40.5 → 19.4
- c6__otcL_W1__R100, issuer_2 [share 20%, other issuers' devices]: 11.3 → 0.0; 11.6 → 0.0; 11.8 → 0.0; 12.0 → 0.0; 12.9 → 0.0; 13.5 → 0.0; 14.1 → 0.0; 14.4 → 0.0; 15.1 → 0.0; 15.6 → 0.0
- c6__otcL_W1__R100, issuer_2_with_observer [share 20%, all records]: 3.5 → 2.3; 4.2 → 6.1; 4.7 → 3.8; 5.2 → 3.1; 5.7 → 5.3; 6.0 → 6.1; 6.4 → 8.4; 6.8 → 6.1; 7.3 → 7.6; 9.0 → 13.7
- c6__otcL_W1__R100, issuer_2_with_observer [share 20%, its own devices]: 3.7 → 6.2; 4.7 → 12.5; 5.4 → 12.5; 5.9 → 31.2; 6.7 → 18.8; 9.5 → 6.2; 12.3 → 0.0; 13.7 → 0.0; 15.2 → 0.0; 21.1 → 0.0
- c6__otcL_W1__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 3.5 → 2.0; 4.2 → 6.0; 4.7 → 1.0; 5.2 → 2.0; 5.7 → 0.0; 6.0 → 2.0; 6.4 → 9.1; 6.9 → 4.0; 7.4 → 10.1; 9.0 → 18.2
- c6__otcL_W1__R100, issuer_2_with_first_relay [share 20%, all records]: 3.5 → 3.8; 4.3 → 4.5; 4.8 → 3.1; 5.1 → 4.6; 5.6 → 5.3; 6.1 → 4.6; 6.5 → 9.9; 6.9 → 4.6; 7.4 → 9.2; 8.9 → 13.7
- c6__otcL_W1__R100, issuer_2_with_first_relay [share 20%, its own devices]: 3.7 → 9.4; 4.7 → 12.5; 5.3 → 12.5; 5.9 → 21.9; 6.9 → 28.1; 9.5 → 6.2; 12.3 → 0.0; 13.7 → 0.0; 15.8 → 0.0; 21.1 → 0.0
- c6__otcL_W1__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.5 → 2.0; 4.2 → 4.0; 4.7 → 2.0; 5.1 → 3.0; 5.6 → 2.0; 6.1 → 1.0; 6.5 → 8.1; 6.9 → 3.0; 7.5 → 11.1; 8.9 → 18.2
- c6__otcL_W1__R100, issuer_2_with_destination: 10.2 → 25.0; 11.8 → 9.4; 12.8 → 9.4; 14.1 → 25.0; 15.4 → 12.5; 16.4 → 25.0; 17.8 → 34.4; 20.5 → 29.0; 24.5 → 45.2; 29.5 → 29.0
- c6__otcL_W2__R1, observer: 4.1 → 10.8; 4.6 → 8.1; 4.9 → 10.8; 5.2 → 2.7; 5.4 → 5.4; 5.7 → 8.1; 6.1 → 0.0; 6.6 → 2.8; 7.5 → 8.3; 10.0 → 0.0
- c6__otcL_W2__R1, first_hop: 4.1 → 10.0; 4.6 → 7.5; 4.9 → 10.8; 5.2 → 3.3; 5.4 → 4.8; 5.7 → 8.9; 6.1 → 0.7; 6.6 → 2.6; 7.5 → 8.2; 9.9 → 0.0
- c6__otcL_W2__R1, destination: 3.4 → 10.8; 3.8 → 0.0; 4.1 → 8.1; 4.4 → 0.0; 4.8 → 2.7; 5.1 → 10.8; 5.4 → 11.1; 5.8 → 0.0; 6.6 → 5.6; 9.4 → 0.0
- c6__otcL_W2__R1, destination_keyed: 8.3 → 8.1; 9.6 → 8.1; 10.5 → 16.2; 11.4 → 8.1; 12.3 → 13.5; 13.2 → 16.2; 14.6 → 19.4; 15.8 → 25.0; 17.5 → 19.4; 21.7 → 25.0
- c6__otcL_W2__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W2__R1, issuer_0 [share 50%, all records]: 9.3 → 0.0; 9.5 → 0.0; 9.6 → 0.0; 9.7 → 0.0; 9.8 → 0.0; 9.9 → 0.0; 10.1 → 0.0; 10.4 → 0.0; 10.9 → 0.0; 11.6 → 0.0
- c6__otcL_W2__R1, issuer_0 [share 50%, other issuers' devices]: 9.3 → 0.0; 9.5 → 0.0; 9.6 → 0.0; 9.7 → 0.0; 9.8 → 0.0; 9.9 → 0.0; 10.1 → 0.0; 10.4 → 0.0; 10.9 → 0.0; 11.6 → 0.0
- c6__otcL_W2__R1, issuer_0_with_observer [share 50%, all records]: 4.2 → 5.4; 4.6 → 5.4; 5.0 → 10.8; 5.2 → 5.4; 5.5 → 8.1; 5.8 → 2.7; 6.3 → 0.0; 6.8 → 11.1; 8.0 → 0.0; 11.1 → 0.0
- c6__otcL_W2__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 4.2 → 5.4; 4.6 → 5.4; 5.0 → 10.8; 5.2 → 5.4; 5.5 → 8.1; 5.8 → 2.7; 6.3 → 0.0; 6.8 → 11.1; 8.0 → 0.0; 11.1 → 0.0
- c6__otcL_W2__R1, issuer_0_with_first_relay [share 50%, all records]: 4.2 → 5.4; 4.7 → 2.7; 5.0 → 5.4; 5.3 → 8.1; 5.5 → 5.4; 5.8 → 8.1; 6.3 → 2.8; 6.9 → 5.6; 8.0 → 2.8; 11.2 → 0.0
- c6__otcL_W2__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.2 → 5.4; 4.7 → 2.7; 5.0 → 5.4; 5.3 → 8.1; 5.5 → 5.4; 5.8 → 8.1; 6.3 → 2.8; 6.9 → 5.6; 8.0 → 2.8; 11.2 → 0.0
- c6__otcL_W2__R1, issuer_1 [share 30%, all records]: 4.4 → 0.0; 4.5 → 0.0; 4.6 → 0.0; 4.7 → 0.0; 5.8 → 0.0; 12.9 → 0.0; 13.2 → 0.0; 13.5 → 0.0; 13.8 → 0.0; 15.1 → 0.0
- c6__otcL_W2__R1, issuer_1 [share 30%, its own devices]: 4.4 → 0.0; 4.5 → 0.0; 4.6 → 0.0; 4.7 → 0.0; 5.8 → 0.0; 12.9 → 0.0; 13.2 → 0.0; 13.5 → 0.0; 13.8 → 0.0; 15.1 → 0.0
- c6__otcL_W2__R1, issuer_1_with_observer [share 30%, all records]: 4.2 → 0.0; 4.8 → 8.1; 5.1 → 2.7; 5.4 → 10.8; 5.6 → 13.5; 6.0 → 8.1; 6.3 → 16.7; 7.0 → 25.0; 7.8 → 8.3; 10.3 → 0.0
- c6__otcL_W2__R1, issuer_1_with_observer [share 30%, its own devices]: 4.2 → 0.0; 4.8 → 8.1; 5.1 → 2.7; 5.4 → 10.8; 5.6 → 13.5; 6.0 → 8.1; 6.3 → 16.7; 7.0 → 25.0; 7.8 → 8.3; 10.3 → 0.0
- c6__otcL_W2__R1, issuer_1_with_first_relay [share 30%, all records]: 4.3 → 2.7; 4.8 → 2.7; 5.1 → 5.4; 5.4 → 8.1; 5.6 → 8.1; 6.0 → 5.4; 6.4 → 16.7; 7.0 → 25.0; 7.8 → 8.3; 10.4 → 2.8
- c6__otcL_W2__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.3 → 2.7; 4.8 → 2.7; 5.1 → 5.4; 5.4 → 8.1; 5.6 → 8.1; 6.0 → 5.4; 6.4 → 16.7; 7.0 → 25.0; 7.8 → 8.3; 10.4 → 2.8
- c6__otcL_W2__R1, issuer_1_with_destination: 8.6 → 13.5; 10.0 → 10.8; 10.9 → 18.9; 11.7 → 13.5; 12.8 → 10.8; 14.0 → 10.8; 15.5 → 33.3; 16.9 → 27.8; 19.0 → 22.2; 24.7 → 30.6
- c6__otcL_W2__R1, issuer_2 [share 20%, all records]: 8.1 → 0.0; 8.4 → 0.0; 8.7 → 0.0; 9.6 → 0.0; 11.0 → 0.0; 17.1 → 0.0; 17.9 → 0.0; 18.4 → 0.0; 19.0 → 0.0; 20.3 → 0.0
- c6__otcL_W2__R1, issuer_2 [share 20%, other issuers' devices]: 8.1 → 0.0; 8.4 → 0.0; 8.7 → 0.0; 9.6 → 0.0; 11.0 → 0.0; 17.1 → 0.0; 17.9 → 0.0; 18.4 → 0.0; 19.0 → 0.0; 20.3 → 0.0
- c6__otcL_W2__R1, issuer_2_with_observer [share 20%, all records]: 4.1 → 13.5; 4.7 → 2.7; 5.0 → 13.5; 5.2 → 2.7; 5.5 → 2.7; 5.8 → 8.1; 6.2 → 0.0; 6.8 → 11.1; 7.9 → 0.0; 10.4 → 0.0
- c6__otcL_W2__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.1 → 13.5; 4.7 → 2.7; 5.0 → 13.5; 5.2 → 2.7; 5.5 → 2.7; 5.8 → 8.1; 6.2 → 0.0; 6.8 → 11.1; 7.9 → 0.0; 10.4 → 0.0
- c6__otcL_W2__R1, issuer_2_with_first_relay [share 20%, all records]: 4.1 → 8.1; 4.7 → 2.7; 5.0 → 5.4; 5.3 → 5.4; 5.5 → 5.4; 5.8 → 10.8; 6.2 → 0.0; 6.8 → 11.1; 7.9 → 0.0; 10.5 → 0.0
- c6__otcL_W2__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.1 → 8.1; 4.7 → 2.7; 5.0 → 5.4; 5.3 → 5.4; 5.5 → 5.4; 5.8 → 10.8; 6.2 → 0.0; 6.8 → 11.1; 7.9 → 0.0; 10.5 → 0.0
- c6__otcL_W2__R100, observer: 3.5 → 1.6; 4.0 → 4.9; 4.6 → 5.7; 5.2 → 1.6; 5.5 → 8.2; 5.8 → 8.2; 6.3 → 9.0; 7.5 → 4.9; 8.7 → 5.7; 10.2 → 8.2
- c6__otcL_W2__R100, first_hop: 3.5 → 2.1; 4.1 → 4.0; 4.7 → 5.7; 5.2 → 3.4; 5.5 → 7.6; 5.8 → 8.1; 6.3 → 8.4; 7.5 → 5.6; 8.7 → 5.7; 10.2 → 8.1
- c6__otcL_W2__R100, destination: 2.8 → 4.9; 3.2 → 7.4; 3.4 → 9.8; 3.7 → 5.7; 3.9 → 3.3; 4.3 → 9.0; 4.8 → 7.4; 5.6 → 6.6; 7.6 → 0.8; 10.2 → 3.3
- c6__otcL_W2__R100, destination_keyed: 5.3 → 9.8; 6.5 → 13.9; 7.2 → 13.9; 8.0 → 17.2; 8.6 → 13.9; 9.5 → 9.8; 10.7 → 12.3; 12.8 → 9.8; 16.3 → 9.8; 21.3 → 23.0
- c6__otcL_W2__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W2__R100, issuer_0 [share 50%, all records]: 7.0 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.7 → 0.0; 7.9 → 0.0; 9.4 → 7.4; 9.8 → 7.4; 10.0 → 7.4; 10.2 → 10.7; 10.4 → 12.3
- c6__otcL_W2__R100, issuer_0 [share 50%, its own devices]: 7.0 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.7 → 0.0; 8.0 → 0.0; 9.5 → 14.3; 9.8 → 11.4; 10.0 → 12.9; 10.2 → 18.6; 10.4 → 21.4
- c6__otcL_W2__R100, issuer_0 [share 50%, other issuers' devices]: 7.0 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.7 → 0.0; 7.9 → 0.0; 9.3 → 0.0; 9.8 → 0.0; 10.0 → 0.0; 10.2 → 0.0; 10.3 → 0.0
- c6__otcL_W2__R100, issuer_0_with_observer [share 50%, all records]: 3.5 → 2.4; 4.1 → 2.5; 4.7 → 6.6; 5.2 → 3.3; 5.5 → 7.4; 5.9 → 6.6; 6.5 → 11.5; 7.9 → 8.2; 9.2 → 2.5; 10.7 → 10.7
- c6__otcL_W2__R100, issuer_0_with_observer [share 50%, its own devices]: 3.5 → 2.8; 4.1 → 1.4; 4.6 → 11.3; 5.2 → 5.6; 5.5 → 7.1; 5.9 → 11.4; 6.5 → 20.0; 7.9 → 12.9; 9.2 → 4.3; 10.7 → 12.9
- c6__otcL_W2__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.4 → 1.9; 2.8 → 3.8; 3.1 → 0.0; 3.6 → 1.9; 4.4 → 0.0; 4.9 → 5.8; 5.3 → 5.8; 5.9 → 3.9; 6.7 → 0.0; 9.3 → 0.0
- c6__otcL_W2__R100, issuer_0_with_first_relay [share 50%, all records]: 3.5 → 3.3; 4.1 → 0.8; 4.7 → 7.4; 5.2 → 2.5; 5.5 → 7.4; 5.9 → 5.7; 6.6 → 12.3; 7.9 → 7.4; 9.2 → 3.3; 10.7 → 10.7
- c6__otcL_W2__R100, issuer_0_with_first_relay [share 50%, its own devices]: 3.5 → 4.2; 4.1 → 0.0; 4.6 → 8.5; 5.2 → 7.0; 5.5 → 8.6; 5.9 → 8.6; 6.6 → 21.4; 7.9 → 11.4; 9.1 → 5.7; 10.7 → 12.9
- c6__otcL_W2__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.4 → 1.9; 2.8 → 3.8; 3.2 → 0.0; 3.6 → 1.9; 4.3 → 0.0; 4.9 → 3.8; 5.4 → 7.7; 5.8 → 3.9; 6.8 → 0.0; 9.3 → 0.0
- c6__otcL_W2__R100, issuer_0_with_destination: 5.0 → 11.3; 5.9 → 9.9; 6.5 → 9.9; 7.0 → 16.9; 7.8 → 14.3; 8.4 → 22.9; 9.1 → 14.3; 10.0 → 18.6; 12.5 → 8.6; 17.8 → 0.0
- c6__otcL_W2__R100, issuer_1 [share 30%, all records]: 8.0 → 1.6; 8.1 → 0.0; 8.1 → 5.7; 8.2 → 4.1; 8.5 → 3.3; 18.1 → 1.6; 19.6 → 0.0; 20.1 → 0.0; 20.8 → 0.0; 23.2 → 0.0
- c6__otcL_W2__R100, issuer_1 [share 30%, its own devices]: 8.0 → 4.2; 8.1 → 4.2; 8.1 → 16.7; 8.2 → 16.7; 8.4 → 16.7; 12.8 → 25.0; 19.3 → 0.0; 20.0 → 0.0; 20.6 → 0.0; 23.0 → 0.0
- c6__otcL_W2__R100, issuer_1 [share 30%, other issuers' devices]: 11.3 → 0.0; 11.4 → 0.0; 11.5 → 0.0; 11.7 → 0.0; 11.9 → 0.0; 12.1 → 0.0; 12.3 → 0.0; 12.4 → 0.0; 12.7 → 0.0; 13.6 → 0.0
- c6__otcL_W2__R100, issuer_1_with_observer [share 30%, all records]: 3.5 → 2.4; 4.1 → 4.9; 4.7 → 4.9; 5.2 → 2.5; 5.5 → 7.4; 5.8 → 9.0; 6.4 → 8.2; 7.6 → 4.9; 8.7 → 5.7; 10.4 → 8.2
- c6__otcL_W2__R100, issuer_1_with_observer [share 30%, its own devices]: 1.8 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.3 → 4.2; 2.6 → 0.0; 3.1 → 16.7; 4.6 → 0.0; 5.6 → 0.0; 6.3 → 0.0; 8.6 → 0.0
- c6__otcL_W2__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 3.5 → 3.0; 4.1 → 6.1; 4.7 → 6.1; 5.2 → 4.0; 5.5 → 9.2; 5.8 → 10.2; 6.4 → 10.2; 7.6 → 5.1; 8.7 → 7.1; 10.3 → 6.1
- c6__otcL_W2__R100, issuer_1_with_first_relay [share 30%, all records]: 3.5 → 2.4; 4.2 → 4.9; 4.8 → 4.9; 5.2 → 3.3; 5.5 → 7.4; 5.9 → 8.2; 6.5 → 8.2; 7.6 → 3.3; 8.7 → 7.4; 10.4 → 8.2
- c6__otcL_W2__R100, issuer_1_with_first_relay [share 30%, its own devices]: 1.8 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.3 → 4.2; 2.6 → 0.0; 3.1 → 16.7; 4.6 → 0.0; 5.6 → 0.0; 6.4 → 0.0; 8.6 → 0.0
- c6__otcL_W2__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.5 → 3.0; 4.2 → 6.1; 4.8 → 6.1; 5.2 → 5.1; 5.5 → 8.2; 5.8 → 10.2; 6.4 → 10.2; 7.5 → 3.1; 8.7 → 9.2; 10.3 → 6.1
- c6__otcL_W2__R100, issuer_1_with_destination: 6.4 → 8.3; 7.1 → 12.5; 7.8 → 16.7; 8.3 → 12.5; 9.0 → 8.3; 9.5 → 8.3; 10.2 → 12.5; 10.8 → 4.3; 11.8 → 13.0; 15.9 → 26.1
- c6__otcL_W2__R100, issuer_2 [share 20%, all records]: 7.6 → 0.8; 8.0 → 3.3; 8.3 → 1.6; 8.8 → 2.5; 10.3 → 0.0; 23.6 → 5.7; 23.9 → 6.6; 24.1 → 8.2; 24.7 → 6.6; 25.9 → 2.5
- c6__otcL_W2__R100, issuer_2 [share 20%, its own devices]: 7.5 → 3.6; 7.9 → 10.7; 8.2 → 3.6; 8.7 → 14.3; 9.1 → 3.6; 20.0 → 17.9; 23.9 → 28.6; 24.1 → 35.7; 24.4 → 21.4; 25.6 → 25.0
- c6__otcL_W2__R100, issuer_2 [share 20%, other issuers' devices]: 7.6 → 0.0; 8.1 → 0.0; 8.3 → 0.0; 8.9 → 0.0; 11.7 → 0.0; 23.7 → 0.0; 23.9 → 0.0; 24.1 → 0.0; 24.9 → 0.0; 26.0 → 0.0
- c6__otcL_W2__R100, issuer_2_with_observer [share 20%, all records]: 3.5 → 1.6; 4.1 → 5.7; 4.6 → 5.7; 5.1 → 4.1; 5.5 → 5.7; 5.7 → 8.2; 6.2 → 9.0; 7.5 → 4.9; 8.6 → 5.7; 10.1 → 8.2
- c6__otcL_W2__R100, issuer_2_with_observer [share 20%, its own devices]: 3.5 → 3.6; 4.2 → 7.1; 4.8 → 7.1; 5.2 → 10.7; 5.5 → 3.6; 5.7 → 0.0; 6.1 → 0.0; 7.3 → 0.0; 8.7 → 0.0; 10.0 → 0.0
- c6__otcL_W2__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 3.5 → 1.1; 4.0 → 5.3; 4.6 → 5.3; 5.1 → 2.1; 5.5 → 6.4; 5.7 → 10.6; 6.3 → 11.7; 7.5 → 6.4; 8.6 → 7.4; 10.1 → 10.6
- c6__otcL_W2__R100, issuer_2_with_first_relay [share 20%, all records]: 3.5 → 3.3; 4.1 → 4.9; 4.6 → 5.7; 5.1 → 3.3; 5.5 → 6.6; 5.8 → 8.2; 6.3 → 8.2; 7.4 → 5.7; 8.6 → 4.9; 10.1 → 9.0
- c6__otcL_W2__R100, issuer_2_with_first_relay [share 20%, its own devices]: 3.5 → 3.6; 4.2 → 7.1; 4.8 → 7.1; 5.2 → 10.7; 5.5 → 0.0; 5.7 → 3.6; 6.2 → 0.0; 7.3 → 0.0; 8.6 → 0.0; 10.0 → 0.0
- c6__otcL_W2__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.5 → 3.2; 4.1 → 2.1; 4.6 → 7.4; 5.1 → 3.2; 5.5 → 5.3; 5.8 → 10.6; 6.4 → 10.6; 7.5 → 7.4; 8.6 → 6.4; 10.1 → 11.7
- c6__otcL_W2__R100, issuer_2_with_destination: 9.6 → 17.9; 10.9 → 17.9; 11.6 → 7.1; 12.4 → 14.3; 13.1 → 17.9; 13.7 → 17.9; 14.3 → 21.4; 15.2 → 14.3; 16.3 → 21.4; 20.2 → 14.3
- c6__otcL_Wmis__R1, observer: 4.3 → 5.4; 4.9 → 5.4; 5.4 → 8.1; 5.9 → 13.5; 6.5 → 13.5; 7.1 → 24.3; 7.9 → 13.9; 8.8 → 13.9; 10.0 → 22.2; 13.3 → 41.7
- c6__otcL_Wmis__R1, first_hop: 4.3 → 5.2; 4.9 → 6.6; 5.4 → 6.8; 5.9 → 12.0; 6.5 → 19.3; 7.1 → 19.0; 7.9 → 18.3; 8.8 → 12.2; 10.0 → 21.2; 13.3 → 40.7
- c6__otcL_Wmis__R1, destination: 3.3 → 5.4; 3.6 → 5.4; 3.8 → 8.1; 4.2 → 13.5; 4.5 → 10.8; 4.8 → 10.8; 5.3 → 22.2; 5.7 → 11.1; 6.3 → 19.4; 7.9 → 25.0
- c6__otcL_Wmis__R1, destination_keyed: 8.6 → 21.6; 9.9 → 16.2; 10.7 → 13.5; 11.7 → 13.5; 12.4 → 27.0; 13.2 → 18.9; 14.1 → 41.7; 15.3 → 30.6; 17.3 → 22.2; 22.6 → 58.3
- c6__otcL_Wmis__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_Wmis__R1, issuer_0 [share 50%, all records]: 2.9 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.6 → 0.0; 3.7 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 4.0 → 0.0
- c6__otcL_Wmis__R1, issuer_0 [share 50%, other issuers' devices]: 2.9 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.6 → 0.0; 3.7 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 4.0 → 0.0
- c6__otcL_Wmis__R1, issuer_0_with_observer [share 50%, all records]: 4.2 → 8.1; 4.6 → 5.4; 4.8 → 8.1; 5.2 → 8.1; 5.4 → 2.7; 5.8 → 5.4; 6.2 → 19.4; 6.6 → 16.7; 7.5 → 33.3; 9.2 → 30.6
- c6__otcL_Wmis__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 4.2 → 8.1; 4.6 → 5.4; 4.8 → 8.1; 5.2 → 8.1; 5.4 → 2.7; 5.8 → 5.4; 6.2 → 19.4; 6.6 → 16.7; 7.5 → 33.3; 9.2 → 30.6
- c6__otcL_Wmis__R1, issuer_0_with_first_relay [share 50%, all records]: 4.5 → 5.4; 5.2 → 5.4; 5.7 → 5.4; 6.3 → 21.6; 7.0 → 16.2; 7.7 → 8.1; 8.6 → 11.1; 9.4 → 16.7; 11.0 → 11.1; 15.4 → 33.3
- c6__otcL_Wmis__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.5 → 5.4; 5.2 → 5.4; 5.7 → 5.4; 6.3 → 21.6; 7.0 → 16.2; 7.7 → 8.1; 8.6 → 11.1; 9.4 → 16.7; 11.0 → 11.1; 15.4 → 33.3
- c6__otcL_Wmis__R1, issuer_1 [share 30%, all records]: 3.4 → 5.4; 3.5 → 8.1; 3.5 → 10.8; 3.5 → 8.1; 3.5 → 2.7; 5.2 → 5.4; 6.6 → 8.3; 7.0 → 8.3; 7.4 → 0.0; 8.1 → 0.0
- c6__otcL_Wmis__R1, issuer_1 [share 30%, its own devices]: 3.4 → 5.4; 3.5 → 8.1; 3.5 → 10.8; 3.5 → 8.1; 3.5 → 2.7; 5.2 → 5.4; 6.6 → 8.3; 7.0 → 8.3; 7.4 → 0.0; 8.1 → 0.0
- c6__otcL_Wmis__R1, issuer_1_with_observer [share 30%, all records]: 4.4 → 2.7; 5.1 → 2.7; 5.7 → 2.7; 6.3 → 13.5; 7.0 → 8.1; 7.7 → 16.2; 8.6 → 8.3; 9.5 → 30.6; 11.8 → 19.4; 20.1 → 69.4
- c6__otcL_Wmis__R1, issuer_1_with_observer [share 30%, its own devices]: 4.4 → 2.7; 5.1 → 2.7; 5.7 → 2.7; 6.3 → 13.5; 7.0 → 8.1; 7.7 → 16.2; 8.6 → 8.3; 9.5 → 30.6; 11.8 → 19.4; 20.1 → 69.4
- c6__otcL_Wmis__R1, issuer_1_with_first_relay [share 30%, all records]: 4.4 → 5.4; 5.1 → 0.0; 5.7 → 5.4; 6.4 → 10.8; 7.1 → 10.8; 7.8 → 13.5; 8.6 → 13.9; 9.7 → 25.0; 11.8 → 22.2; 20.6 → 63.9
- c6__otcL_Wmis__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.4 → 5.4; 5.1 → 0.0; 5.7 → 5.4; 6.4 → 10.8; 7.1 → 10.8; 7.8 → 13.5; 8.6 → 13.9; 9.7 → 25.0; 11.8 → 22.2; 20.6 → 63.9
- c6__otcL_Wmis__R1, issuer_1_with_destination: 9.0 → 10.8; 10.2 → 10.8; 11.3 → 10.8; 12.3 → 10.8; 13.0 → 18.9; 14.1 → 24.3; 15.5 → 22.2; 17.0 → 19.4; 20.0 → 33.3; 27.7 → 58.3
- c6__otcL_Wmis__R1, issuer_2 [share 20%, all records]: 5.1 → 0.0; 5.8 → 0.0; 6.3 → 0.0; 6.7 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.6 → 0.0; 7.9 → 0.0; 8.4 → 0.0; 9.0 → 0.0
- c6__otcL_Wmis__R1, issuer_2 [share 20%, other issuers' devices]: 5.1 → 0.0; 5.8 → 0.0; 6.3 → 0.0; 6.7 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.6 → 0.0; 7.9 → 0.0; 8.4 → 0.0; 9.0 → 0.0
- c6__otcL_Wmis__R1, issuer_2_with_observer [share 20%, all records]: 4.3 → 2.7; 4.9 → 10.8; 5.5 → 5.4; 6.1 → 16.2; 6.7 → 24.3; 7.4 → 10.8; 8.2 → 19.4; 9.2 → 13.9; 10.6 → 19.4; 14.9 → 33.3
- c6__otcL_Wmis__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.3 → 2.7; 4.9 → 10.8; 5.5 → 5.4; 6.1 → 16.2; 6.7 → 24.3; 7.4 → 10.8; 8.2 → 19.4; 9.2 → 13.9; 10.6 → 19.4; 14.9 → 33.3
- c6__otcL_Wmis__R1, issuer_2_with_first_relay [share 20%, all records]: 4.3 → 8.1; 5.0 → 8.1; 5.6 → 5.4; 6.1 → 18.9; 6.7 → 24.3; 7.5 → 8.1; 8.3 → 16.7; 9.1 → 11.1; 10.6 → 16.7; 15.7 → 36.1
- c6__otcL_Wmis__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.3 → 8.1; 5.0 → 8.1; 5.6 → 5.4; 6.1 → 18.9; 6.7 → 24.3; 7.5 → 8.1; 8.3 → 16.7; 9.1 → 11.1; 10.6 → 16.7; 15.7 → 36.1
- c6__otcL_Wmis__R100, observer: 3.2 → 5.7; 3.6 → 6.6; 3.9 → 4.9; 4.1 → 7.4; 4.4 → 9.8; 4.8 → 7.4; 5.3 → 9.0; 5.6 → 14.8; 6.4 → 12.3; 9.4 → 13.9
- c6__otcL_Wmis__R100, first_hop: 3.2 → 5.8; 3.6 → 6.1; 3.9 → 5.9; 4.1 → 8.1; 4.4 → 9.0; 4.8 → 7.2; 5.3 → 10.1; 5.6 → 14.4; 6.4 → 11.8; 9.5 → 14.5
- c6__otcL_Wmis__R100, destination: 3.2 → 3.3; 3.7 → 4.1; 4.0 → 11.5; 4.3 → 8.2; 4.6 → 8.2; 5.0 → 10.7; 5.3 → 8.2; 5.8 → 13.1; 6.7 → 5.7; 9.6 → 15.6
- c6__otcL_Wmis__R100, destination_keyed: 5.9 → 3.3; 7.0 → 10.7; 7.8 → 9.8; 8.6 → 13.1; 9.5 → 12.3; 10.4 → 21.3; 11.5 → 14.8; 13.1 → 13.1; 15.2 → 18.9; 20.2 → 35.2
- c6__otcL_Wmis__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_Wmis__R100, issuer_0 [share 50%, all records]: 5.1 → 6.5; 5.5 → 7.4; 6.0 → 8.2; 6.6 → 3.3; 6.8 → 3.3; 45.7 → 6.6; 50.3 → 6.6; 51.7 → 7.4; 52.8 → 13.1; 54.1 → 11.5
- c6__otcL_Wmis__R100, issuer_0 [share 50%, its own devices]: 5.1 → 8.5; 5.5 → 15.5; 6.1 → 16.9; 6.6 → 4.2; 8.0 → 4.3; 48.4 → 12.9; 50.3 → 10.0; 51.7 → 12.9; 52.8 → 22.9; 54.2 → 20.0
- c6__otcL_Wmis__R100, issuer_0 [share 50%, other issuers' devices]: 3.7 → 0.0; 3.9 → 0.0; 4.1 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 8.4 → 0.0; 9.3 → 0.0; 9.4 → 0.0; 9.6 → 0.0; 9.7 → 0.0
- c6__otcL_Wmis__R100, issuer_0_with_observer [share 50%, all records]: 3.3 → 4.1; 3.7 → 7.4; 3.9 → 7.4; 4.3 → 9.8; 4.5 → 4.1; 5.0 → 9.8; 5.3 → 9.0; 5.8 → 13.9; 6.5 → 13.9; 10.0 → 13.9
- c6__otcL_Wmis__R100, issuer_0_with_observer [share 50%, its own devices]: 3.8 → 14.1; 4.8 → 9.9; 5.4 → 9.9; 5.8 → 19.7; 6.3 → 8.6; 6.9 → 15.7; 7.9 → 7.1; 8.7 → 4.3; 10.1 → 15.7; 15.4 → 11.4
- c6__otcL_Wmis__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 3.2 → 5.8; 3.6 → 3.8; 3.9 → 9.6; 4.3 → 5.8; 4.4 → 7.7; 4.9 → 3.8; 5.3 → 7.7; 5.8 → 7.8; 6.4 → 2.0; 9.9 → 7.8
- c6__otcL_Wmis__R100, issuer_0_with_first_relay [share 50%, all records]: 3.2 → 6.5; 3.7 → 9.0; 4.1 → 8.2; 4.3 → 4.9; 4.5 → 4.9; 5.0 → 9.8; 5.4 → 9.0; 5.8 → 13.9; 6.6 → 13.9; 10.0 → 13.9
- c6__otcL_Wmis__R100, issuer_0_with_first_relay [share 50%, its own devices]: 3.8 → 14.1; 4.7 → 9.9; 5.4 → 8.5; 5.8 → 23.9; 6.5 → 11.4; 7.2 → 11.4; 8.1 → 8.6; 8.7 → 2.9; 10.1 → 12.9; 15.5 → 14.3
- c6__otcL_Wmis__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.2 → 3.8; 3.7 → 9.6; 4.1 → 11.5; 4.3 → 0.0; 4.5 → 7.7; 4.9 → 3.8; 5.4 → 7.7; 5.8 → 7.8; 6.4 → 2.0; 9.9 → 7.8
- c6__otcL_Wmis__R100, issuer_0_with_destination: 5.7 → 2.8; 6.5 → 4.2; 7.1 → 16.9; 7.7 → 9.9; 8.3 → 12.9; 8.8 → 14.3; 9.6 → 20.0; 10.6 → 24.3; 12.1 → 15.7; 18.2 → 20.0
- c6__otcL_Wmis__R100, issuer_1 [share 30%, all records]: 11.4 → 1.6; 11.7 → 0.8; 11.9 → 4.1; 12.1 → 1.6; 14.9 → 2.5; 48.0 → 0.8; 50.5 → 0.0; 52.2 → 4.9; 54.2 → 3.3; 56.5 → 6.6
- c6__otcL_Wmis__R100, issuer_1 [share 30%, its own devices]: 11.4 → 8.3; 11.7 → 4.2; 12.0 → 25.0; 12.1 → 8.3; 37.3 → 8.3; 49.6 → 4.2; 51.5 → 8.3; 52.7 → 21.7; 54.9 → 21.7; 56.9 → 26.1
- c6__otcL_Wmis__R100, issuer_1 [share 30%, other issuers' devices]: 8.2 → 0.0; 8.4 → 0.0; 8.4 → 0.0; 8.5 → 0.0; 8.6 → 0.0; 14.8 → 0.0; 15.4 → 0.0; 15.7 → 0.0; 16.1 → 0.0; 16.7 → 0.0
- c6__otcL_Wmis__R100, issuer_1_with_observer [share 30%, all records]: 3.2 → 4.9; 3.6 → 7.4; 3.9 → 7.4; 4.2 → 11.5; 4.5 → 7.4; 4.9 → 7.4; 5.3 → 9.0; 5.7 → 15.6; 6.5 → 10.7; 9.6 → 13.9
- c6__otcL_Wmis__R100, issuer_1_with_observer [share 30%, its own devices]: 2.1 → 0.0; 2.4 → 0.0; 2.5 → 16.7; 2.7 → 4.2; 3.0 → 0.0; 3.5 → 12.5; 4.3 → 8.3; 5.1 → 4.3; 5.9 → 4.3; 8.8 → 0.0
- c6__otcL_Wmis__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 3.8 → 11.1; 4.6 → 13.1; 5.2 → 8.1; 5.6 → 16.2; 6.0 → 9.2; 6.7 → 11.2; 7.6 → 7.1; 8.6 → 7.1; 10.1 → 15.3; 15.5 → 7.1
- c6__otcL_Wmis__R100, issuer_1_with_first_relay [share 30%, all records]: 3.2 → 5.7; 3.6 → 7.4; 3.9 → 9.0; 4.2 → 8.2; 4.6 → 9.8; 5.0 → 4.9; 5.3 → 8.2; 5.7 → 16.4; 6.6 → 10.7; 9.6 → 13.9
- c6__otcL_Wmis__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.1 → 0.0; 2.4 → 0.0; 2.6 → 4.2; 2.8 → 0.0; 3.1 → 4.2; 3.4 → 12.5; 4.4 → 8.3; 5.1 → 4.3; 5.9 → 4.3; 8.8 → 0.0
- c6__otcL_Wmis__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.8 → 12.1; 4.6 → 12.1; 5.2 → 7.1; 5.5 → 18.2; 6.1 → 9.2; 6.8 → 12.2; 7.7 → 6.1; 8.8 → 9.2; 10.3 → 14.3; 15.6 → 7.1
- c6__otcL_Wmis__R100, issuer_1_with_destination: 7.6 → 0.0; 8.7 → 0.0; 9.3 → 8.3; 9.9 → 20.8; 10.5 → 12.5; 11.4 → 8.3; 12.4 → 12.5; 13.6 → 17.4; 15.3 → 17.4; 24.3 → 39.1
- c6__otcL_Wmis__R100, issuer_2 [share 20%, all records]: 10.4 → 0.8; 11.2 → 5.7; 11.8 → 4.9; 13.1 → 4.9; 16.0 → 1.6; 31.9 → 4.1; 32.3 → 6.6; 32.6 → 10.7; 33.5 → 5.7; 35.7 → 2.5
- c6__otcL_Wmis__R100, issuer_2 [share 20%, its own devices]: 10.4 → 3.6; 11.2 → 25.0; 11.8 → 21.4; 12.6 → 10.7; 14.0 → 17.9; 27.7 → 10.7; 32.2 → 32.1; 32.5 → 35.7; 33.1 → 25.0; 35.0 → 25.0
- c6__otcL_Wmis__R100, issuer_2 [share 20%, other issuers' devices]: 7.9 → 0.0; 8.3 → 0.0; 8.6 → 0.0; 9.3 → 0.0; 11.0 → 0.0; 16.0 → 0.0; 16.1 → 0.0; 16.2 → 0.0; 16.6 → 0.0; 17.5 → 0.0
- c6__otcL_Wmis__R100, issuer_2_with_observer [share 20%, all records]: 3.2 → 3.3; 3.6 → 6.6; 3.9 → 1.6; 4.2 → 9.0; 4.5 → 7.4; 4.9 → 7.4; 5.2 → 11.5; 5.5 → 13.9; 6.3 → 11.5; 9.4 → 13.9
- c6__otcL_Wmis__R100, issuer_2_with_observer [share 20%, its own devices]: 3.3 → 10.7; 3.7 → 14.3; 4.2 → 7.1; 4.7 → 14.3; 5.7 → 7.1; 7.8 → 3.6; 10.0 → 21.4; 11.1 → 0.0; 13.8 → 0.0; 23.3 → 0.0
- c6__otcL_Wmis__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 3.2 → 1.1; 3.6 → 5.3; 3.9 → 1.1; 4.2 → 10.6; 4.5 → 5.3; 4.9 → 7.4; 5.3 → 9.6; 5.6 → 17.0; 6.5 → 12.8; 9.5 → 18.1
- c6__otcL_Wmis__R100, issuer_2_with_first_relay [share 20%, all records]: 3.2 → 6.5; 3.6 → 4.1; 3.9 → 4.9; 4.2 → 8.2; 4.6 → 6.6; 4.9 → 8.2; 5.3 → 10.7; 5.6 → 13.9; 6.4 → 10.7; 9.4 → 14.8
- c6__otcL_Wmis__R100, issuer_2_with_first_relay [share 20%, its own devices]: 3.3 → 14.3; 3.7 → 10.7; 4.3 → 7.1; 4.7 → 7.1; 5.7 → 14.3; 7.8 → 3.6; 10.0 → 10.7; 11.1 → 10.7; 13.9 → 0.0; 23.2 → 0.0
- c6__otcL_Wmis__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.2 → 4.2; 3.6 → 5.3; 3.9 → 2.1; 4.2 → 8.5; 4.6 → 7.4; 4.9 → 7.4; 5.3 → 7.4; 5.6 → 17.0; 6.6 → 13.8; 9.5 → 18.1
- c6__otcL_Wmis__R100, issuer_2_with_destination: 9.0 → 3.6; 10.6 → 10.7; 12.0 → 3.6; 13.1 → 10.7; 13.9 → 17.9; 14.7 → 17.9; 15.9 → 25.0; 17.1 → 28.6; 18.5 → 21.4; 21.7 → 42.9
- c6__otcL_chain100__R1, observer: 3.9 → 4.8; 4.3 → 7.1; 4.6 → 9.5; 4.8 → 0.0; 5.1 → 7.1; 5.4 → 0.0; 5.6 → 4.8; 5.9 → 7.1; 6.4 → 7.1; 7.4 → 7.1
- c6__otcL_chain100__R1, first_hop: 3.9 → 5.1; 4.4 → 6.7; 4.6 → 7.5; 4.9 → 0.8; 5.1 → 5.8; 5.4 → 1.1; 5.6 → 4.8; 5.9 → 7.5; 6.5 → 6.5; 7.5 → 8.1
- c6__otcL_chain100__R1, destination: 4.2 → 0.0; 4.7 → 4.8; 5.0 → 2.4; 5.3 → 2.4; 5.5 → 7.1; 5.8 → 7.1; 6.0 → 0.0; 6.4 → 7.1; 7.0 → 14.3; 8.4 → 11.9
- c6__otcL_chain100__R1, destination_keyed: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.7 → 0.0; 3.5 → 4.8; 3.9 → 4.8; 4.7 → 11.9
- c6__otcL_chain100__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_chain100__R1, issuer_0 [share 50%, all records]: 2.6 → 0.0; 3.0 → 0.0; 3.4 → 0.0; 3.8 → 0.0; 4.1 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 4.5 → 0.0; 4.8 → 0.0
- c6__otcL_chain100__R1, issuer_0 [share 50%, other issuers' devices]: 2.6 → 0.0; 3.0 → 0.0; 3.4 → 0.0; 3.8 → 0.0; 4.1 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 4.5 → 0.0; 4.8 → 0.0
- c6__otcL_chain100__R1, issuer_0_with_observer [share 50%, all records]: 4.0 → 4.8; 4.4 → 0.0; 4.8 → 2.4; 5.1 → 4.8; 5.4 → 4.8; 5.8 → 2.4; 6.2 → 4.8; 6.7 → 4.8; 7.4 → 7.1; 9.4 → 0.0
- c6__otcL_chain100__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 4.0 → 4.8; 4.4 → 0.0; 4.8 → 2.4; 5.1 → 4.8; 5.4 → 4.8; 5.8 → 2.4; 6.2 → 4.8; 6.7 → 4.8; 7.4 → 7.1; 9.4 → 0.0
- c6__otcL_chain100__R1, issuer_0_with_first_relay [share 50%, all records]: 4.0 → 4.8; 4.5 → 0.0; 4.9 → 2.4; 5.2 → 0.0; 5.5 → 2.4; 5.8 → 9.5; 6.2 → 4.8; 6.7 → 9.5; 7.5 → 2.4; 9.4 → 0.0
- c6__otcL_chain100__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.0 → 4.8; 4.5 → 0.0; 4.9 → 2.4; 5.2 → 0.0; 5.5 → 2.4; 5.8 → 9.5; 6.2 → 4.8; 6.7 → 9.5; 7.5 → 2.4; 9.4 → 0.0
- c6__otcL_chain100__R1, issuer_1 [share 30%, all records]: 3.4 → 9.5; 3.5 → 11.9; 3.5 → 9.5; 3.6 → 4.8; 3.6 → 11.9; 6.0 → 0.0; 11.0 → 2.4; 14.4 → 0.0; 16.4 → 4.8; 19.1 → 0.0
- c6__otcL_chain100__R1, issuer_1 [share 30%, its own devices]: 3.4 → 6.9; 3.5 → 20.7; 3.5 → 6.9; 3.6 → 13.8; 3.6 → 10.3; 6.5 → 0.0; 11.1 → 0.0; 14.4 → 0.0; 16.3 → 3.6; 19.1 → 0.0
- c6__otcL_chain100__R1, issuer_1 [share 30%, other issuers' devices]: 3.4 → 7.1; 3.5 → 0.0; 3.5 → 14.3; 3.6 → 0.0; 3.6 → 0.0; 5.1 → 0.0; 7.5 → 7.7; 8.8 → 0.0; 9.5 → 7.7; 10.3 → 0.0
- c6__otcL_chain100__R1, issuer_1_with_observer [share 30%, all records]: 4.0 → 9.5; 4.5 → 11.9; 4.8 → 2.4; 5.0 → 0.0; 5.3 → 4.8; 5.6 → 7.1; 5.9 → 4.8; 6.4 → 7.1; 7.0 → 2.4; 8.6 → 16.7
- c6__otcL_chain100__R1, issuer_1_with_observer [share 30%, its own devices]: 4.0 → 0.0; 4.4 → 24.1; 4.7 → 0.0; 5.0 → 0.0; 5.4 → 10.3; 5.7 → 7.1; 6.0 → 7.1; 6.5 → 3.6; 6.9 → 3.6; 8.6 → 21.4
- c6__otcL_chain100__R1, issuer_1_with_observer [share 30%, other issuers' devices]: 3.1 → 7.1; 3.4 → 0.0; 3.6 → 0.0; 4.0 → 0.0; 4.4 → 7.1; 4.6 → 15.4; 5.1 → 0.0; 5.4 → 0.0; 6.1 → 15.4; 7.9 → 0.0
- c6__otcL_chain100__R1, issuer_1_with_first_relay [share 30%, all records]: 4.0 → 7.1; 4.5 → 11.9; 4.8 → 4.8; 5.1 → 0.0; 5.4 → 4.8; 5.6 → 4.8; 5.9 → 4.8; 6.4 → 7.1; 7.0 → 7.1; 8.7 → 14.3
- c6__otcL_chain100__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.0 → 3.4; 4.5 → 17.2; 4.8 → 3.4; 5.1 → 0.0; 5.4 → 6.9; 5.7 → 7.1; 6.0 → 7.1; 6.5 → 3.6; 7.0 → 10.7; 8.7 → 17.9
- c6__otcL_chain100__R1, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.1 → 7.1; 3.4 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.4 → 7.1; 4.7 → 7.7; 5.1 → 7.7; 5.5 → 0.0; 6.1 → 15.4; 7.8 → 0.0
- c6__otcL_chain100__R1, issuer_1_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0
- c6__otcL_chain100__R1, issuer_2 [share 20%, all records]: 5.1 → 0.0; 5.8 → 0.0; 6.1 → 0.0; 6.5 → 0.0; 7.3 → 0.0; 7.9 → 0.0; 8.4 → 0.0; 8.8 → 0.0; 9.5 → 0.0; 10.4 → 0.0
- c6__otcL_chain100__R1, issuer_2 [share 20%, other issuers' devices]: 5.1 → 0.0; 5.8 → 0.0; 6.1 → 0.0; 6.5 → 0.0; 7.3 → 0.0; 7.9 → 0.0; 8.4 → 0.0; 8.8 → 0.0; 9.5 → 0.0; 10.4 → 0.0
- c6__otcL_chain100__R1, issuer_2_with_observer [share 20%, all records]: 4.0 → 7.1; 4.5 → 11.9; 4.8 → 2.4; 5.0 → 2.4; 5.3 → 2.4; 5.5 → 2.4; 5.8 → 4.8; 6.4 → 4.8; 6.9 → 7.1; 8.5 → 2.4
- c6__otcL_chain100__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.0 → 7.1; 4.5 → 11.9; 4.8 → 2.4; 5.0 → 2.4; 5.3 → 2.4; 5.5 → 2.4; 5.8 → 4.8; 6.4 → 4.8; 6.9 → 7.1; 8.5 → 2.4
- c6__otcL_chain100__R1, issuer_2_with_first_relay [share 20%, all records]: 4.0 → 4.8; 4.5 → 14.3; 4.8 → 0.0; 5.1 → 0.0; 5.3 → 0.0; 5.6 → 4.8; 5.9 → 9.5; 6.4 → 11.9; 7.0 → 0.0; 8.6 → 2.4
- c6__otcL_chain100__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.0 → 4.8; 4.5 → 14.3; 4.8 → 0.0; 5.1 → 0.0; 5.3 → 0.0; 5.6 → 4.8; 5.9 → 9.5; 6.4 → 11.9; 7.0 → 0.0; 8.6 → 2.4
- c6__otcL_chain100__R100, observer: 2.2 → 2.4; 2.4 → 0.8; 2.6 → 1.6; 2.7 → 0.8; 2.8 → 4.0; 2.9 → 1.6; 3.1 → 1.6; 3.2 → 8.1; 3.5 → 6.5; 3.9 → 4.0
- c6__otcL_chain100__R100, first_hop: 2.3 → 2.3; 2.5 → 1.1; 2.6 → 1.1; 2.7 → 1.4; 2.8 → 3.9; 3.0 → 1.9; 3.1 → 2.7; 3.3 → 6.6; 3.5 → 6.0; 3.9 → 4.4
- c6__otcL_chain100__R100, destination: 1.8 → 0.8; 1.9 → 2.4; 2.0 → 4.0; 2.2 → 6.5; 2.3 → 5.6; 2.6 → 2.4; 2.9 → 0.8; 3.1 → 2.4; 3.4 → 5.6; 4.1 → 1.6
- c6__otcL_chain100__R100, destination_keyed: 0.0 → 0.0; 0.0 → 0.0; 0.6 → 0.0; 2.1 → 3.2; 2.7 → 1.6; 5.2 → 2.4; 55.8 → 0.8; 79.6 → 2.4; 100.0 → 3.2; 100.0 → 2.4
- c6__otcL_chain100__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_chain100__R100, issuer_0 [share 50%, all records]: 1.8 → 2.4; 1.8 → 0.8; 1.8 → 1.6; 1.8 → 1.6; 1.8 → 3.2; 2.9 → 0.8; 3.8 → 0.8; 4.0 → 0.8; 4.2 → 0.0; 4.4 → 0.8
- c6__otcL_chain100__R100, issuer_0 [share 50%, its own devices]: 2.3 → 2.1; 2.4 → 2.1; 2.4 → 4.3; 2.4 → 2.1; 2.6 → 4.3; 2.9 → 2.1; 3.7 → 2.2; 4.0 → 2.2; 4.2 → 0.0; 4.4 → 2.2
- c6__otcL_chain100__R100, issuer_0 [share 50%, other issuers' devices]: 1.7 → 0.0; 1.7 → 0.0; 1.7 → 2.6; 1.7 → 1.3; 1.8 → 2.6; 2.6 → 0.0; 2.9 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.1 → 0.0
- c6__otcL_chain100__R100, issuer_0_with_observer [share 50%, all records]: 2.4 → 1.6; 2.6 → 1.6; 2.7 → 2.4; 2.8 → 3.2; 3.0 → 3.2; 3.2 → 6.5; 3.4 → 2.4; 3.6 → 5.6; 3.9 → 6.5; 4.6 → 0.8
- c6__otcL_chain100__R100, issuer_0_with_observer [share 50%, its own devices]: 2.4 → 2.1; 2.6 → 0.0; 2.7 → 4.3; 2.9 → 2.1; 3.0 → 2.1; 3.2 → 8.5; 3.4 → 2.2; 3.7 → 6.5; 3.9 → 10.9; 4.7 → 0.0
- c6__otcL_chain100__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.4 → 1.3; 2.6 → 2.6; 2.7 → 1.3; 2.8 → 3.8; 3.0 → 3.8; 3.2 → 5.1; 3.4 → 2.6; 3.6 → 5.2; 3.9 → 3.9; 4.6 → 1.3
- c6__otcL_chain100__R100, issuer_0_with_first_relay [share 50%, all records]: 2.4 → 1.6; 2.6 → 1.6; 2.7 → 0.8; 2.8 → 3.2; 3.0 → 2.4; 3.2 → 7.3; 3.4 → 1.6; 3.6 → 4.0; 3.9 → 7.3; 4.7 → 0.8
- c6__otcL_chain100__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.4 → 2.1; 2.6 → 0.0; 2.7 → 0.0; 2.9 → 2.1; 3.0 → 2.1; 3.2 → 8.5; 3.4 → 2.2; 3.6 → 6.5; 3.9 → 10.9; 4.8 → 0.0
- c6__otcL_chain100__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.4 → 1.3; 2.6 → 2.6; 2.7 → 1.3; 2.8 → 3.8; 3.0 → 2.6; 3.2 → 5.1; 3.4 → 2.6; 3.6 → 2.6; 3.9 → 5.2; 4.7 → 1.3
- c6__otcL_chain100__R100, issuer_0_with_destination: 0.0 → 0.0; 10.7 → 0.0; 52.8 → 0.0; 63.2 → 0.0; 77.1 → 2.1; 90.1 → 4.3; 99.4 → 0.0; 100.0 → 6.5; 100.0 → 2.2; 100.0 → 6.5
- c6__otcL_chain100__R100, issuer_1 [share 30%, all records]: 4.5 → 0.0; 5.1 → 2.4; 5.3 → 0.0; 5.5 → 1.6; 5.8 → 3.2; 6.3 → 1.6; 7.3 → 0.0; 8.1 → 2.4; 8.6 → 1.6; 9.3 → 0.0
- c6__otcL_chain100__R100, issuer_1 [share 30%, its own devices]: 4.6 → 0.0; 5.2 → 9.5; 5.4 → 5.0; 5.6 → 10.0; 5.8 → 10.0; 6.4 → 5.0; 7.4 → 0.0; 8.1 → 15.0; 8.6 → 5.0; 9.4 → 0.0
- c6__otcL_chain100__R100, issuer_1 [share 30%, other issuers' devices]: 2.5 → 0.0; 2.5 → 1.0; 2.5 → 0.0; 2.5 → 0.0; 2.6 → 1.9; 5.5 → 0.0; 7.3 → 0.0; 8.0 → 1.0; 8.6 → 0.0; 9.3 → 0.0
- c6__otcL_chain100__R100, issuer_1_with_observer [share 30%, all records]: 2.3 → 3.2; 2.5 → 0.8; 2.7 → 0.8; 2.8 → 3.2; 3.0 → 2.4; 3.1 → 4.0; 3.4 → 10.5; 3.7 → 4.8; 4.0 → 3.2; 5.3 → 3.2
- c6__otcL_chain100__R100, issuer_1_with_observer [share 30%, its own devices]: 2.4 → 4.8; 2.6 → 0.0; 2.7 → 0.0; 2.9 → 10.0; 3.0 → 5.0; 3.1 → 0.0; 3.4 → 15.0; 3.7 → 15.0; 4.1 → 5.0; 5.2 → 5.0
- c6__otcL_chain100__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.3 → 2.9; 2.5 → 1.0; 2.7 → 1.0; 2.8 → 1.9; 3.0 → 1.9; 3.1 → 5.8; 3.4 → 7.7; 3.6 → 3.8; 4.0 → 2.9; 5.3 → 2.9
- c6__otcL_chain100__R100, issuer_1_with_first_relay [share 30%, all records]: 2.3 → 3.2; 2.6 → 0.8; 2.7 → 3.2; 2.9 → 2.4; 3.0 → 1.6; 3.2 → 4.0; 3.4 → 8.9; 3.7 → 3.2; 4.0 → 4.8; 5.4 → 3.2
- c6__otcL_chain100__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.4 → 4.8; 2.6 → 4.8; 2.7 → 0.0; 2.9 → 10.0; 3.0 → 0.0; 3.1 → 0.0; 3.4 → 20.0; 3.7 → 10.0; 4.2 → 10.0; 5.3 → 5.0
- c6__otcL_chain100__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.3 → 2.9; 2.5 → 1.0; 2.7 → 1.9; 2.9 → 1.9; 3.0 → 1.9; 3.2 → 4.8; 3.4 → 5.8; 3.7 → 2.9; 4.0 → 3.8; 5.4 → 2.9
- c6__otcL_chain100__R100, issuer_1_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 16.3 → 0.0; 64.4 → 5.0; 92.4 → 0.0; 100.0 → 0.0
- c6__otcL_chain100__R100, issuer_2 [share 20%, all records]: 3.3 → 0.8; 5.6 → 0.8; 7.7 → 0.0; 9.6 → 1.6; 10.6 → 1.6; 11.1 → 3.2; 11.7 → 0.8; 12.4 → 0.8; 13.1 → 0.0; 14.8 → 1.6
- c6__otcL_chain100__R100, issuer_2 [share 20%, its own devices]: 3.2 → 5.9; 5.2 → 0.0; 7.0 → 0.0; 9.2 → 5.9; 10.5 → 5.9; 10.9 → 11.8; 11.4 → 17.6; 12.3 → 0.0; 13.3 → 6.2; 15.2 → 6.2
- c6__otcL_chain100__R100, issuer_2 [share 20%, other issuers' devices]: 3.1 → 0.0; 3.6 → 0.9; 4.1 → 0.9; 4.3 → 0.9; 4.4 → 0.9; 5.3 → 0.0; 5.9 → 0.0; 6.1 → 0.0; 6.3 → 0.0; 6.6 → 0.0
- c6__otcL_chain100__R100, issuer_2_with_observer [share 20%, all records]: 2.3 → 1.6; 2.5 → 0.0; 2.6 → 1.6; 2.8 → 3.2; 2.9 → 0.8; 3.1 → 0.8; 3.2 → 6.5; 3.4 → 4.8; 3.6 → 4.8; 4.3 → 4.8
- c6__otcL_chain100__R100, issuer_2_with_observer [share 20%, its own devices]: 1.7 → 0.0; 1.8 → 11.8; 1.9 → 0.0; 2.0 → 5.9; 2.1 → 5.9; 2.3 → 5.9; 2.6 → 0.0; 2.9 → 0.0; 3.3 → 6.2; 3.9 → 12.5
- c6__otcL_chain100__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.3 → 1.9; 2.5 → 0.0; 2.6 → 0.9; 2.8 → 2.8; 2.9 → 0.9; 3.1 → 0.9; 3.2 → 6.5; 3.4 → 2.8; 3.6 → 5.6; 4.3 → 3.7
- c6__otcL_chain100__R100, issuer_2_with_first_relay [share 20%, all records]: 2.3 → 1.6; 2.5 → 0.8; 2.6 → 2.4; 2.8 → 5.6; 2.9 → 0.0; 3.1 → 0.8; 3.2 → 5.6; 3.4 → 4.8; 3.7 → 4.8; 4.3 → 4.8
- c6__otcL_chain100__R100, issuer_2_with_first_relay [share 20%, its own devices]: 1.7 → 5.9; 1.9 → 17.6; 1.9 → 0.0; 2.0 → 5.9; 2.2 → 0.0; 2.3 → 11.8; 2.6 → 0.0; 3.0 → 0.0; 3.3 → 6.2; 4.0 → 12.5
- c6__otcL_chain100__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.3 → 1.9; 2.5 → 0.0; 2.6 → 0.9; 2.8 → 5.6; 2.9 → 0.0; 3.1 → 0.9; 3.2 → 4.7; 3.4 → 4.7; 3.7 → 4.7; 4.3 → 3.7
- c6__otcL_chain100__R100, issuer_2_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 15.8 → 0.0; 100.0 → 0.0; 100.0 → 0.0; 100.0 → 0.0
- c6__otcL_chain50__R1, observer: 3.5 → 4.7; 3.9 → 7.1; 4.2 → 7.1; 4.3 → 11.9; 4.5 → 7.1; 4.8 → 2.4; 5.0 → 9.5; 5.4 → 4.8; 5.8 → 4.8; 6.7 → 4.8
- c6__otcL_chain50__R1, first_hop: 3.5 → 3.2; 3.9 → 8.3; 4.2 → 7.0; 4.4 → 12.5; 4.6 → 5.6; 4.8 → 4.9; 5.0 → 7.8; 5.4 → 3.8; 5.8 → 4.0; 6.8 → 5.1
- c6__otcL_chain50__R1, destination: 3.8 → 2.3; 4.3 → 0.0; 4.5 → 2.4; 4.8 → 2.4; 5.1 → 0.0; 5.3 → 9.5; 5.6 → 2.4; 5.9 → 9.5; 6.4 → 4.8; 7.5 → 9.5
- c6__otcL_chain50__R1, destination_keyed: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.5 → 0.0; 2.5 → 0.0; 3.8 → 2.4; 6.0 → 7.1
- c6__otcL_chain50__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_chain50__R1, issuer_0 [share 50%, all records]: 2.6 → 0.0; 3.0 → 0.0; 3.5 → 0.0; 3.9 → 0.0; 4.1 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 4.5 → 0.0; 4.8 → 0.0
- c6__otcL_chain50__R1, issuer_0 [share 50%, other issuers' devices]: 2.6 → 0.0; 3.0 → 0.0; 3.5 → 0.0; 3.9 → 0.0; 4.1 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 4.5 → 0.0; 4.8 → 0.0
- c6__otcL_chain50__R1, issuer_0_with_observer [share 50%, all records]: 3.6 → 0.0; 4.1 → 2.4; 4.4 → 7.1; 4.6 → 4.8; 4.8 → 4.8; 5.2 → 2.4; 5.5 → 4.8; 6.0 → 0.0; 6.6 → 4.8; 8.2 → 0.0
- c6__otcL_chain50__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 3.6 → 0.0; 4.1 → 2.4; 4.4 → 7.1; 4.6 → 4.8; 4.8 → 4.8; 5.2 → 2.4; 5.5 → 4.8; 6.0 → 0.0; 6.6 → 4.8; 8.2 → 0.0
- c6__otcL_chain50__R1, issuer_0_with_first_relay [share 50%, all records]: 3.7 → 0.0; 4.1 → 0.0; 4.4 → 9.5; 4.6 → 9.5; 4.9 → 0.0; 5.2 → 2.4; 5.5 → 4.8; 6.0 → 0.0; 6.6 → 4.8; 8.2 → 0.0
- c6__otcL_chain50__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.7 → 0.0; 4.1 → 0.0; 4.4 → 9.5; 4.6 → 9.5; 4.9 → 0.0; 5.2 → 2.4; 5.5 → 4.8; 6.0 → 0.0; 6.6 → 4.8; 8.2 → 0.0
- c6__otcL_chain50__R1, issuer_1 [share 30%, all records]: 3.4 → 4.7; 3.5 → 16.7; 3.6 → 2.4; 3.6 → 11.9; 3.6 → 9.5; 6.1 → 0.0; 11.0 → 0.0; 14.5 → 0.0; 16.6 → 2.4; 19.2 → 2.4
- c6__otcL_chain50__R1, issuer_1 [share 30%, its own devices]: 3.4 → 6.9; 3.5 → 20.7; 3.5 → 6.9; 3.6 → 13.8; 3.6 → 10.3; 6.5 → 0.0; 11.1 → 0.0; 14.4 → 0.0; 16.3 → 3.6; 19.1 → 0.0
- c6__otcL_chain50__R1, issuer_1 [share 30%, other issuers' devices]: 3.4 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.6 → 14.3; 3.6 → 0.0; 5.1 → 0.0; 7.4 → 0.0; 8.9 → 0.0; 9.7 → 0.0; 10.4 → 7.7
- c6__otcL_chain50__R1, issuer_1_with_observer [share 30%, all records]: 3.6 → 14.0; 4.1 → 2.4; 4.3 → 14.3; 4.6 → 7.1; 4.8 → 2.4; 5.1 → 7.1; 5.4 → 7.1; 5.9 → 4.8; 6.4 → 9.5; 8.2 → 9.5
- c6__otcL_chain50__R1, issuer_1_with_observer [share 30%, its own devices]: 3.9 → 17.2; 4.6 → 13.8; 5.2 → 10.3; 5.8 → 6.9; 6.3 → 6.9; 6.8 → 10.7; 7.5 → 3.6; 8.6 → 10.7; 10.0 → 3.6; 13.9 → 10.7
- c6__otcL_chain50__R1, issuer_1_with_observer [share 30%, other issuers' devices]: 2.5 → 0.0; 2.8 → 0.0; 2.9 → 7.1; 3.1 → 0.0; 3.3 → 0.0; 3.4 → 0.0; 3.5 → 7.7; 3.6 → 7.7; 3.9 → 7.7; 4.7 → 15.4
- c6__otcL_chain50__R1, issuer_1_with_first_relay [share 30%, all records]: 3.7 → 14.0; 4.1 → 2.4; 4.3 → 23.8; 4.6 → 0.0; 4.8 → 4.8; 5.2 → 2.4; 5.5 → 4.8; 5.9 → 2.4; 6.5 → 16.7; 8.2 → 9.5
- c6__otcL_chain50__R1, issuer_1_with_first_relay [share 30%, its own devices]: 3.8 → 20.7; 4.1 → 13.8; 4.3 → 20.7; 4.6 → 0.0; 4.9 → 6.9; 5.2 → 3.6; 5.5 → 3.6; 5.9 → 3.6; 6.5 → 14.3; 8.1 → 10.7
- c6__otcL_chain50__R1, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.5 → 0.0; 2.8 → 0.0; 2.9 → 7.1; 3.1 → 0.0; 3.3 → 0.0; 3.4 → 0.0; 3.5 → 7.7; 3.6 → 7.7; 3.9 → 7.7; 4.7 → 15.4
- c6__otcL_chain50__R1, issuer_1_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0
- c6__otcL_chain50__R1, issuer_2 [share 20%, all records]: 5.0 → 0.0; 5.8 → 0.0; 6.1 → 0.0; 6.5 → 0.0; 7.2 → 0.0; 7.9 → 0.0; 8.3 → 0.0; 8.8 → 0.0; 9.6 → 0.0; 10.5 → 0.0
- c6__otcL_chain50__R1, issuer_2 [share 20%, other issuers' devices]: 5.0 → 0.0; 5.8 → 0.0; 6.1 → 0.0; 6.5 → 0.0; 7.2 → 0.0; 7.9 → 0.0; 8.3 → 0.0; 8.8 → 0.0; 9.6 → 0.0; 10.5 → 0.0
- c6__otcL_chain50__R1, issuer_2_with_observer [share 20%, all records]: 3.7 → 7.0; 4.1 → 9.5; 4.3 → 4.8; 4.5 → 11.9; 4.7 → 4.8; 5.0 → 4.8; 5.3 → 0.0; 5.6 → 4.8; 6.2 → 4.8; 7.4 → 0.0
- c6__otcL_chain50__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 3.7 → 7.0; 4.1 → 9.5; 4.3 → 4.8; 4.5 → 11.9; 4.7 → 4.8; 5.0 → 4.8; 5.3 → 0.0; 5.6 → 4.8; 6.2 → 4.8; 7.4 → 0.0
- c6__otcL_chain50__R1, issuer_2_with_first_relay [share 20%, all records]: 3.7 → 4.7; 4.1 → 9.5; 4.3 → 9.5; 4.5 → 14.3; 4.8 → 4.8; 5.0 → 2.4; 5.3 → 0.0; 5.6 → 4.8; 6.2 → 2.4; 7.5 → 0.0
- c6__otcL_chain50__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.7 → 4.7; 4.1 → 9.5; 4.3 → 9.5; 4.5 → 14.3; 4.8 → 4.8; 5.0 → 2.4; 5.3 → 0.0; 5.6 → 4.8; 6.2 → 2.4; 7.5 → 0.0
- c6__otcL_chain50__R100, observer: 2.0 → 1.6; 2.2 → 4.0; 2.4 → 4.8; 2.5 → 2.4; 2.6 → 2.4; 2.7 → 1.6; 2.8 → 3.2; 2.9 → 3.2; 3.1 → 4.8; 3.7 → 3.2
- c6__otcL_chain50__R100, first_hop: 2.0 → 2.0; 2.3 → 4.2; 2.4 → 3.7; 2.5 → 2.4; 2.6 → 1.8; 2.7 → 2.3; 2.8 → 2.3; 2.9 → 3.2; 3.2 → 5.1; 3.7 → 3.4
- c6__otcL_chain50__R100, destination: 1.6 → 3.2; 1.7 → 1.6; 1.9 → 4.8; 2.0 → 6.4; 2.2 → 1.6; 2.4 → 3.2; 2.7 → 6.5; 2.9 → 0.8; 3.2 → 2.4; 3.6 → 4.8
- c6__otcL_chain50__R100, destination_keyed: 1.8 → 0.8; 2.1 → 4.0; 2.3 → 1.6; 12.3 → 0.8; 20.2 → 8.8; 24.1 → 5.6; 28.2 → 6.5; 34.9 → 6.5; 45.0 → 7.3; 73.0 → 4.0
- c6__otcL_chain50__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_chain50__R100, issuer_0 [share 50%, all records]: 2.3 → 0.8; 2.3 → 0.8; 2.4 → 1.6; 2.4 → 1.6; 2.6 → 2.4; 2.8 → 1.6; 2.9 → 0.0; 3.0 → 1.6; 3.1 → 0.0; 3.1 → 0.8
- c6__otcL_chain50__R100, issuer_0 [share 50%, its own devices]: 2.3 → 2.1; 2.4 → 2.1; 2.4 → 4.3; 2.4 → 2.1; 2.6 → 4.3; 2.9 → 2.1; 3.7 → 2.2; 4.0 → 2.2; 4.2 → 0.0; 4.4 → 2.2
- c6__otcL_chain50__R100, issuer_0 [share 50%, other issuers' devices]: 1.8 → 1.3; 1.8 → 0.0; 1.8 → 0.0; 1.8 → 0.0; 1.8 → 0.0; 3.8 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.6 → 2.6; 6.4 → 0.0
- c6__otcL_chain50__R100, issuer_0_with_observer [share 50%, all records]: 2.2 → 6.4; 2.4 → 0.8; 2.5 → 0.0; 2.7 → 2.4; 2.8 → 4.8; 2.9 → 4.0; 3.1 → 4.8; 3.3 → 1.6; 3.8 → 3.2; 4.5 → 1.6
- c6__otcL_chain50__R100, issuer_0_with_observer [share 50%, its own devices]: 2.1 → 6.4; 2.3 → 0.0; 2.5 → 0.0; 2.7 → 4.3; 2.8 → 6.4; 2.9 → 4.3; 3.1 → 0.0; 3.4 → 6.5; 3.8 → 4.3; 4.5 → 4.3
- c6__otcL_chain50__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.2 → 7.7; 2.4 → 0.0; 2.6 → 0.0; 2.7 → 1.3; 2.8 → 3.8; 2.9 → 3.8; 3.1 → 7.7; 3.3 → 0.0; 3.7 → 1.3; 4.4 → 0.0
- c6__otcL_chain50__R100, issuer_0_with_first_relay [share 50%, all records]: 2.2 → 4.8; 2.4 → 0.8; 2.6 → 1.6; 2.7 → 0.0; 2.8 → 5.6; 2.9 → 4.0; 3.1 → 4.0; 3.4 → 2.4; 3.8 → 3.2; 4.6 → 1.6
- c6__otcL_chain50__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.1 → 2.1; 2.3 → 0.0; 2.5 → 2.1; 2.7 → 0.0; 2.8 → 6.4; 2.9 → 4.3; 3.2 → 2.2; 3.5 → 4.3; 3.8 → 6.5; 4.6 → 2.2
- c6__otcL_chain50__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.2 → 7.7; 2.4 → 0.0; 2.6 → 1.3; 2.7 → 0.0; 2.8 → 5.1; 2.9 → 2.6; 3.1 → 7.7; 3.3 → 0.0; 3.7 → 2.6; 4.5 → 0.0
- c6__otcL_chain50__R100, issuer_0_with_destination: 18.9 → 0.0; 22.3 → 2.1; 25.1 → 6.4; 27.3 → 6.4; 29.3 → 8.5; 31.5 → 6.4; 34.7 → 2.2; 38.2 → 6.5; 45.5 → 15.2; 65.6 → 6.5
- c6__otcL_chain50__R100, issuer_1 [share 30%, all records]: 4.5 → 0.0; 5.1 → 2.4; 5.3 → 0.0; 5.5 → 1.6; 5.8 → 3.2; 6.4 → 0.8; 7.4 → 0.0; 8.1 → 1.6; 8.6 → 1.6; 9.4 → 0.0
- c6__otcL_chain50__R100, issuer_1 [share 30%, its own devices]: 4.6 → 0.0; 5.2 → 9.5; 5.4 → 5.0; 5.6 → 10.0; 5.8 → 10.0; 6.4 → 5.0; 7.4 → 0.0; 8.1 → 15.0; 8.6 → 5.0; 9.4 → 0.0
- c6__otcL_chain50__R100, issuer_1 [share 30%, other issuers' devices]: 2.4 → 0.0; 2.4 → 1.0; 2.5 → 0.0; 2.5 → 0.0; 2.5 → 1.0; 5.6 → 0.0; 7.4 → 0.0; 8.1 → 0.0; 8.6 → 0.0; 9.4 → 0.0
- c6__otcL_chain50__R100, issuer_1_with_observer [share 30%, all records]: 2.1 → 3.2; 2.3 → 3.2; 2.5 → 3.2; 2.6 → 2.4; 2.7 → 1.6; 2.8 → 4.0; 3.0 → 2.4; 3.1 → 2.4; 3.5 → 1.6; 4.2 → 4.0
- c6__otcL_chain50__R100, issuer_1_with_observer [share 30%, its own devices]: 2.1 → 4.8; 2.5 → 4.8; 2.7 → 0.0; 3.0 → 10.0; 3.4 → 5.0; 4.0 → 0.0; 4.8 → 10.0; 5.2 → 15.0; 5.7 → 15.0; 7.6 → 5.0
- c6__otcL_chain50__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.1 → 1.9; 2.3 → 3.8; 2.5 → 2.9; 2.6 → 2.9; 2.7 → 1.9; 2.8 → 1.9; 3.0 → 0.0; 3.1 → 1.0; 3.5 → 1.0; 4.2 → 2.9
- c6__otcL_chain50__R100, issuer_1_with_first_relay [share 30%, all records]: 2.1 → 4.0; 2.3 → 3.2; 2.5 → 2.4; 2.6 → 1.6; 2.7 → 2.4; 2.8 → 3.2; 3.0 → 3.2; 3.1 → 3.2; 3.5 → 1.6; 4.2 → 4.0
- c6__otcL_chain50__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.2 → 0.0; 2.5 → 4.8; 2.7 → 0.0; 3.0 → 10.0; 3.5 → 5.0; 4.0 → 0.0; 4.8 → 20.0; 5.1 → 5.0; 5.7 → 20.0; 7.7 → 0.0
- c6__otcL_chain50__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.1 → 3.8; 2.3 → 2.9; 2.5 → 2.9; 2.6 → 1.9; 2.7 → 1.9; 2.8 → 1.9; 3.0 → 0.0; 3.2 → 1.9; 3.5 → 1.9; 4.2 → 2.9
- c6__otcL_chain50__R100, issuer_1_with_destination: 16.3 → 0.0; 24.7 → 0.0; 29.9 → 5.0; 33.9 → 5.0; 35.8 → 0.0; 38.9 → 5.0; 42.9 → 5.0; 48.7 → 0.0; 61.3 → 0.0; 98.1 → 0.0
- c6__otcL_chain50__R100, issuer_2 [share 20%, all records]: 3.2 → 0.8; 5.6 → 0.0; 7.7 → 0.0; 9.6 → 0.8; 10.6 → 2.4; 11.1 → 2.4; 11.7 → 0.8; 12.3 → 0.0; 13.0 → 0.0; 14.8 → 1.6
- c6__otcL_chain50__R100, issuer_2 [share 20%, its own devices]: 3.2 → 5.9; 5.2 → 0.0; 7.0 → 0.0; 9.2 → 5.9; 10.5 → 5.9; 10.9 → 11.8; 11.4 → 17.6; 12.3 → 0.0; 13.3 → 6.2; 15.2 → 6.2
- c6__otcL_chain50__R100, issuer_2 [share 20%, other issuers' devices]: 3.1 → 0.0; 3.8 → 0.0; 3.9 → 0.9; 3.9 → 0.0; 3.9 → 0.0; 3.9 → 0.0; 4.0 → 0.0; 4.7 → 0.0; 5.1 → 0.0; 5.4 → 0.0
- c6__otcL_chain50__R100, issuer_2_with_observer [share 20%, all records]: 2.1 → 1.6; 2.3 → 4.0; 2.5 → 2.4; 2.6 → 1.6; 2.7 → 3.2; 2.8 → 3.2; 3.0 → 3.2; 3.2 → 3.2; 3.4 → 1.6; 4.4 → 3.2
- c6__otcL_chain50__R100, issuer_2_with_observer [share 20%, its own devices]: 2.3 → 0.0; 2.6 → 11.8; 2.8 → 5.9; 2.9 → 0.0; 3.2 → 5.9; 3.5 → 0.0; 4.2 → 0.0; 4.6 → 5.9; 5.9 → 0.0; 9.2 → 12.5
- c6__otcL_chain50__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.0 → 1.9; 2.3 → 4.6; 2.5 → 1.9; 2.6 → 0.9; 2.7 → 1.9; 2.8 → 3.7; 3.0 → 3.7; 3.2 → 3.7; 3.4 → 0.9; 4.4 → 1.9
- c6__otcL_chain50__R100, issuer_2_with_first_relay [share 20%, all records]: 2.1 → 1.6; 2.3 → 4.0; 2.5 → 1.6; 2.6 → 2.4; 2.7 → 1.6; 2.8 → 4.0; 3.0 → 3.2; 3.2 → 4.0; 3.4 → 1.6; 4.4 → 3.2
- c6__otcL_chain50__R100, issuer_2_with_first_relay [share 20%, its own devices]: 2.3 → 0.0; 2.7 → 11.8; 2.8 → 5.9; 3.0 → 0.0; 3.2 → 5.9; 3.5 → 0.0; 4.1 → 0.0; 4.7 → 5.9; 5.9 → 0.0; 9.4 → 12.5
- c6__otcL_chain50__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.0 → 0.9; 2.3 → 4.6; 2.5 → 1.9; 2.6 → 1.9; 2.7 → 0.9; 2.8 → 3.7; 3.0 → 3.7; 3.2 → 3.7; 3.4 → 1.9; 4.4 → 1.9
- c6__otcL_chain50__R100, issuer_2_with_destination: 27.2 → 5.9; 36.1 → 5.9; 41.7 → 11.8; 48.4 → 17.6; 53.9 → 11.8; 61.1 → 0.0; 66.8 → 17.6; 74.3 → 5.9; 85.5 → 18.8; 99.5 → 0.0
- c6__otc_W0__R1, observer: 4.0 → 0.0; 4.4 → 2.4; 4.6 → 0.0; 4.8 → 7.3; 5.0 → 12.2; 5.3 → 2.4; 5.5 → 4.9; 5.8 → 9.8; 6.2 → 9.8; 7.3 → 12.2
- c6__otc_W0__R1, first_hop: 4.0 → 0.6; 4.4 → 2.7; 4.6 → 1.2; 4.9 → 5.6; 5.1 → 10.4; 5.3 → 5.0; 5.5 → 6.3; 5.8 → 8.2; 6.3 → 9.3; 7.4 → 12.0
- c6__otc_W0__R1, destination: 3.2 → 2.4; 3.5 → 11.9; 3.7 → 11.9; 4.0 → 4.9; 4.3 → 14.6; 4.8 → 9.8; 5.2 → 0.0; 5.6 → 2.4; 6.2 → 2.4; 7.6 → 9.8
- c6__otc_W0__R1, destination_keyed: 8.3 → 14.3; 9.4 → 11.9; 10.4 → 14.3; 11.2 → 22.0; 11.8 → 14.6; 12.4 → 17.1; 13.5 → 9.8; 14.8 → 9.8; 16.5 → 17.1; 20.7 → 12.2
- c6__otc_W0__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_W0__R1, issuer_0 [share 50%, all records]: 2.5 → 0.0; 3.1 → 0.0; 3.7 → 0.0; 4.2 → 0.0; 4.9 → 0.0; 5.4 → 0.0; 5.8 → 0.0; 6.3 → 0.0; 6.5 → 0.0; 6.9 → 0.0
- c6__otc_W0__R1, issuer_0 [share 50%, other issuers' devices]: 2.5 → 0.0; 3.1 → 0.0; 3.7 → 0.0; 4.2 → 0.0; 4.9 → 0.0; 5.4 → 0.0; 5.8 → 0.0; 6.3 → 0.0; 6.5 → 0.0; 6.9 → 0.0
- c6__otc_W0__R1, issuer_0_with_observer [share 50%, all records]: 3.2 → 7.1; 3.6 → 7.1; 4.0 → 4.8; 4.5 → 0.0; 4.9 → 2.4; 5.3 → 0.0; 5.8 → 2.4; 6.6 → 7.3; 8.2 → 0.0; 12.4 → 0.0
- c6__otc_W0__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 3.2 → 7.1; 3.6 → 7.1; 4.0 → 4.8; 4.5 → 0.0; 4.9 → 2.4; 5.3 → 0.0; 5.8 → 2.4; 6.6 → 7.3; 8.2 → 0.0; 12.4 → 0.0
- c6__otc_W0__R1, issuer_0_with_first_relay [share 50%, all records]: 3.2 → 7.1; 3.6 → 7.1; 4.1 → 4.8; 4.5 → 0.0; 4.9 → 2.4; 5.3 → 0.0; 5.9 → 2.4; 6.7 → 7.3; 8.2 → 0.0; 12.4 → 0.0
- c6__otc_W0__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.2 → 7.1; 3.6 → 7.1; 4.1 → 4.8; 4.5 → 0.0; 4.9 → 2.4; 5.3 → 0.0; 5.9 → 2.4; 6.7 → 7.3; 8.2 → 0.0; 12.4 → 0.0
- c6__otc_W0__R1, issuer_1 [share 30%, all records]: 3.7 → 0.0; 3.8 → 2.4; 4.2 → 7.1; 5.0 → 4.9; 5.8 → 4.9; 6.5 → 14.6; 7.0 → 7.3; 10.8 → 4.9; 15.1 → 9.8; 17.7 → 9.8
- c6__otc_W0__R1, issuer_1 [share 30%, its own devices]: 3.7 → 0.0; 3.8 → 2.4; 4.2 → 7.1; 5.0 → 4.9; 5.8 → 4.9; 6.5 → 14.6; 7.0 → 7.3; 10.8 → 4.9; 15.1 → 9.8; 17.7 → 9.8
- c6__otc_W0__R1, issuer_1_with_observer [share 30%, all records]: 4.2 → 2.4; 4.7 → 7.1; 5.0 → 4.8; 5.4 → 4.9; 5.7 → 9.8; 6.2 → 9.8; 6.9 → 12.2; 8.0 → 9.8; 9.7 → 17.1; 13.7 → 12.2
- c6__otc_W0__R1, issuer_1_with_observer [share 30%, its own devices]: 4.2 → 2.4; 4.7 → 7.1; 5.0 → 4.8; 5.4 → 4.9; 5.7 → 9.8; 6.2 → 9.8; 6.9 → 12.2; 8.0 → 9.8; 9.7 → 17.1; 13.7 → 12.2
- c6__otc_W0__R1, issuer_1_with_first_relay [share 30%, all records]: 4.2 → 7.1; 4.6 → 2.4; 5.0 → 4.8; 5.3 → 4.9; 5.7 → 7.3; 6.2 → 12.2; 6.8 → 9.8; 8.0 → 12.2; 9.7 → 14.6; 13.7 → 14.6
- c6__otc_W0__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.2 → 7.1; 4.6 → 2.4; 5.0 → 4.8; 5.3 → 4.9; 5.7 → 7.3; 6.2 → 12.2; 6.8 → 9.8; 8.0 → 12.2; 9.7 → 14.6; 13.7 → 14.6
- c6__otc_W0__R1, issuer_1_with_destination: 8.3 → 14.3; 9.5 → 9.5; 10.6 → 16.7; 11.3 → 19.5; 11.9 → 12.2; 12.8 → 9.8; 13.9 → 12.2; 15.2 → 12.2; 17.3 → 22.0; 21.6 → 17.1
- c6__otc_W0__R1, issuer_2 [share 20%, all records]: 5.0 → 0.0; 5.3 → 0.0; 5.9 → 0.0; 6.0 → 0.0; 6.8 → 0.0; 7.8 → 0.0; 9.1 → 0.0; 10.7 → 0.0; 12.4 → 0.0; 14.3 → 0.0
- c6__otc_W0__R1, issuer_2 [share 20%, other issuers' devices]: 5.0 → 0.0; 5.3 → 0.0; 5.9 → 0.0; 6.0 → 0.0; 6.8 → 0.0; 7.8 → 0.0; 9.1 → 0.0; 10.7 → 0.0; 12.4 → 0.0; 14.3 → 0.0
- c6__otc_W0__R1, issuer_2_with_observer [share 20%, all records]: 4.1 → 0.0; 4.6 → 2.4; 4.9 → 7.1; 5.2 → 12.2; 5.5 → 0.0; 5.8 → 7.3; 6.3 → 9.8; 6.9 → 9.8; 8.2 → 2.4; 11.9 → 0.0
- c6__otc_W0__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.1 → 0.0; 4.6 → 2.4; 4.9 → 7.1; 5.2 → 12.2; 5.5 → 0.0; 5.8 → 7.3; 6.3 → 9.8; 6.9 → 9.8; 8.2 → 2.4; 11.9 → 0.0
- c6__otc_W0__R1, issuer_2_with_first_relay [share 20%, all records]: 4.1 → 0.0; 4.5 → 7.1; 4.9 → 2.4; 5.2 → 14.6; 5.4 → 2.4; 5.8 → 4.9; 6.3 → 12.2; 6.9 → 9.8; 8.2 → 2.4; 11.9 → 0.0
- c6__otc_W0__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.1 → 0.0; 4.5 → 7.1; 4.9 → 2.4; 5.2 → 14.6; 5.4 → 2.4; 5.8 → 4.9; 6.3 → 12.2; 6.9 → 9.8; 8.2 → 2.4; 11.9 → 0.0
- c6__otc_W0__R100, observer: 2.3 → 2.5; 2.5 → 3.3; 2.6 → 4.1; 2.8 → 2.5; 2.9 → 4.1; 3.0 → 1.6; 3.1 → 2.5; 3.2 → 4.1; 3.5 → 3.3; 4.2 → 2.5
- c6__otc_W0__R100, first_hop: 2.3 → 2.5; 2.5 → 4.1; 2.7 → 3.5; 2.8 → 2.3; 2.9 → 3.8; 3.0 → 2.7; 3.1 → 2.4; 3.2 → 4.5; 3.6 → 2.5; 4.2 → 2.7
- c6__otc_W0__R100, destination: 2.5 → 0.8; 2.7 → 0.8; 2.9 → 3.3; 3.0 → 5.7; 3.1 → 0.0; 3.3 → 1.6; 3.4 → 1.7; 3.6 → 4.1; 3.9 → 2.5; 4.6 → 2.5
- c6__otc_W0__R100, destination_keyed: 4.4 → 0.8; 4.9 → 4.1; 5.4 → 5.7; 5.9 → 7.4; 6.6 → 7.4; 7.5 → 10.7; 8.5 → 11.6; 9.8 → 9.1; 11.0 → 7.4; 14.3 → 9.1
- c6__otc_W0__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_W0__R100, issuer_0 [share 50%, all records]: 3.1 → 1.6; 3.9 → 0.8; 4.5 → 0.8; 5.2 → 1.6; 5.5 → 2.5; 5.8 → 2.5; 6.0 → 2.5; 6.2 → 0.0; 6.4 → 6.6; 6.7 → 1.7
- c6__otc_W0__R100, issuer_0 [share 50%, its own devices]: 3.1 → 3.0; 3.9 → 1.5; 4.5 → 1.5; 5.2 → 3.0; 5.4 → 3.0; 5.8 → 6.1; 6.0 → 3.0; 6.2 → 1.5; 6.4 → 12.1; 6.7 → 3.0
- c6__otc_W0__R100, issuer_0 [share 50%, other issuers' devices]: 2.6 → 0.0; 3.0 → 0.0; 3.3 → 0.0; 3.6 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.4 → 0.0
- c6__otc_W0__R100, issuer_0_with_observer [share 50%, all records]: 2.5 → 0.8; 2.8 → 4.1; 2.9 → 1.6; 3.1 → 4.9; 3.3 → 0.8; 3.6 → 1.6; 3.9 → 2.5; 4.2 → 2.5; 4.8 → 4.1; 6.0 → 2.5
- c6__otc_W0__R100, issuer_0_with_observer [share 50%, its own devices]: 2.5 → 1.5; 2.8 → 3.0; 2.9 → 3.0; 3.1 → 7.6; 3.3 → 1.5; 3.6 → 3.0; 3.9 → 4.5; 4.2 → 3.0; 4.8 → 7.6; 6.0 → 4.5
- c6__otc_W0__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.5 → 0.0; 2.8 → 5.4; 2.9 → 0.0; 3.1 → 1.8; 3.3 → 0.0; 3.6 → 0.0; 3.9 → 0.0; 4.3 → 1.8; 4.9 → 0.0; 5.9 → 0.0
- c6__otc_W0__R100, issuer_0_with_first_relay [share 50%, all records]: 2.5 → 0.8; 2.8 → 3.3; 3.0 → 3.3; 3.1 → 4.1; 3.3 → 0.8; 3.6 → 1.6; 3.9 → 2.5; 4.2 → 2.5; 4.8 → 4.1; 6.0 → 2.5
- c6__otc_W0__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.5 → 1.5; 2.8 → 1.5; 3.0 → 6.0; 3.1 → 4.5; 3.3 → 1.5; 3.6 → 3.0; 3.9 → 4.5; 4.2 → 3.0; 4.7 → 6.1; 6.1 → 6.1
- c6__otc_W0__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.5 → 0.0; 2.8 → 5.4; 3.0 → 1.8; 3.1 → 1.8; 3.3 → 0.0; 3.6 → 0.0; 3.9 → 0.0; 4.3 → 1.8; 4.9 → 0.0; 6.0 → 0.0
- c6__otc_W0__R100, issuer_0_with_destination: 4.5 → 6.0; 5.1 → 6.0; 5.6 → 3.0; 6.1 → 6.1; 6.5 → 6.1; 7.1 → 3.0; 7.7 → 6.1; 8.7 → 3.0; 9.8 → 10.6; 12.9 → 4.5
- c6__otc_W0__R100, issuer_1 [share 30%, all records]: 4.6 → 1.6; 5.7 → 0.0; 6.4 → 0.0; 7.4 → 0.8; 8.2 → 0.8; 9.0 → 0.0; 9.9 → 0.8; 10.8 → 2.5; 11.3 → 3.3; 12.4 → 1.7
- c6__otc_W0__R100, issuer_1 [share 30%, its own devices]: 4.8 → 6.1; 6.0 → 0.0; 6.7 → 0.0; 7.4 → 3.1; 8.3 → 3.1; 9.0 → 0.0; 10.1 → 6.2; 10.8 → 6.2; 11.2 → 12.5; 12.3 → 6.2
- c6__otc_W0__R100, issuer_1 [share 30%, other issuers' devices]: 4.1 → 0.0; 4.8 → 0.0; 5.1 → 0.0; 5.7 → 0.0; 6.1 → 0.0; 6.5 → 0.0; 7.0 → 0.0; 7.2 → 0.0; 7.6 → 0.0; 8.2 → 0.0
- c6__otc_W0__R100, issuer_1_with_observer [share 30%, all records]: 2.4 → 3.3; 2.6 → 3.3; 2.8 → 0.8; 2.9 → 3.3; 3.0 → 4.1; 3.1 → 2.5; 3.3 → 5.8; 3.6 → 2.5; 4.1 → 1.7; 4.9 → 4.1
- c6__otc_W0__R100, issuer_1_with_observer [share 30%, its own devices]: 2.5 → 6.1; 2.7 → 9.1; 2.8 → 0.0; 2.9 → 3.1; 3.0 → 3.1; 3.1 → 9.4; 3.3 → 6.2; 3.6 → 9.4; 4.1 → 0.0; 4.9 → 12.5
- c6__otc_W0__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.4 → 3.3; 2.6 → 1.1; 2.8 → 0.0; 2.9 → 3.4; 3.0 → 2.2; 3.1 → 2.2; 3.3 → 4.5; 3.6 → 2.2; 4.1 → 1.1; 5.0 → 1.1
- c6__otc_W0__R100, issuer_1_with_first_relay [share 30%, all records]: 2.4 → 3.3; 2.6 → 1.6; 2.8 → 1.6; 2.9 → 4.1; 3.0 → 5.7; 3.1 → 2.5; 3.3 → 5.8; 3.6 → 2.5; 4.1 → 1.7; 5.0 → 4.1
- c6__otc_W0__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.5 → 6.1; 2.7 → 3.0; 2.8 → 0.0; 2.9 → 6.2; 3.0 → 3.1; 3.1 → 9.4; 3.3 → 6.2; 3.6 → 6.2; 4.1 → 3.1; 4.9 → 12.5
- c6__otc_W0__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.4 → 3.3; 2.6 → 1.1; 2.8 → 1.1; 2.9 → 3.4; 3.0 → 4.5; 3.1 → 2.2; 3.3 → 4.5; 3.6 → 2.2; 4.1 → 1.1; 5.0 → 1.1
- c6__otc_W0__R100, issuer_1_with_destination: 5.0 → 9.1; 5.6 → 3.0; 6.1 → 6.1; 6.4 → 3.1; 6.7 → 0.0; 7.0 → 12.5; 7.3 → 6.2; 7.7 → 15.6; 8.6 → 15.6; 10.0 → 15.6
- c6__otc_W0__R100, issuer_2 [share 20%, all records]: 4.4 → 0.8; 5.1 → 0.0; 6.4 → 0.8; 7.0 → 0.8; 7.7 → 0.8; 8.5 → 1.6; 9.9 → 0.8; 10.8 → 1.7; 12.0 → 0.0; 13.3 → 1.7
- c6__otc_W0__R100, issuer_2 [share 20%, its own devices]: 4.4 → 4.3; 5.8 → 4.3; 6.7 → 4.3; 7.2 → 0.0; 8.1 → 4.3; 8.9 → 13.0; 10.3 → 8.7; 11.1 → 0.0; 12.2 → 0.0; 13.5 → 8.7
- c6__otc_W0__R100, issuer_2 [share 20%, other issuers' devices]: 4.4 → 0.0; 4.9 → 0.0; 5.7 → 0.0; 6.4 → 0.0; 7.1 → 0.0; 7.8 → 0.0; 8.6 → 0.0; 8.9 → 0.0; 9.9 → 0.0; 11.4 → 0.0
- c6__otc_W0__R100, issuer_2_with_observer [share 20%, all records]: 2.3 → 1.6; 2.6 → 4.1; 2.7 → 3.3; 2.8 → 2.5; 3.0 → 4.1; 3.1 → 2.5; 3.2 → 5.0; 3.5 → 3.3; 3.9 → 0.8; 4.7 → 2.5
- c6__otc_W0__R100, issuer_2_with_observer [share 20%, its own devices]: 1.7 → 0.0; 1.8 → 0.0; 1.9 → 21.7; 2.0 → 0.0; 2.2 → 0.0; 2.4 → 0.0; 2.7 → 4.3; 3.0 → 0.0; 3.6 → 4.3; 4.5 → 4.3
- c6__otc_W0__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.3 → 2.0; 2.6 → 5.1; 2.7 → 2.0; 2.8 → 3.0; 3.0 → 4.0; 3.1 → 0.0; 3.2 → 6.1; 3.5 → 3.1; 3.9 → 1.0; 4.7 → 2.0
- c6__otc_W0__R100, issuer_2_with_first_relay [share 20%, all records]: 2.3 → 2.5; 2.6 → 4.9; 2.7 → 3.3; 2.9 → 2.5; 3.0 → 5.7; 3.1 → 4.9; 3.2 → 4.1; 3.6 → 2.5; 3.9 → 0.8; 4.7 → 2.5
- c6__otc_W0__R100, issuer_2_with_first_relay [share 20%, its own devices]: 1.7 → 0.0; 1.8 → 0.0; 1.9 → 17.4; 2.0 → 4.3; 2.2 → 0.0; 2.4 → 0.0; 2.7 → 4.3; 3.1 → 4.3; 3.6 → 4.3; 4.6 → 4.3
- c6__otc_W0__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.3 → 3.0; 2.6 → 6.1; 2.7 → 1.0; 2.9 → 5.1; 3.0 → 3.0; 3.1 → 4.0; 3.2 → 5.1; 3.5 → 2.0; 3.9 → 1.0; 4.6 → 2.0
- c6__otc_W0__R100, issuer_2_with_destination: 6.4 → 13.0; 7.1 → 8.7; 7.5 → 8.7; 7.8 → 13.0; 8.2 → 4.3; 8.5 → 4.3; 9.1 → 13.0; 9.6 → 8.7; 10.5 → 4.3; 13.8 → 8.7
- c6__otc_W1__R1, observer: 3.1 → 7.7; 3.3 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otc_W1__R1, first_hop: 3.1 → 6.8; 3.3 → 0.1; 3.5 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.2 → 0.0; 4.4 → 0.1; 4.8 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otc_W1__R1, destination: 3.1 → 2.6; 3.4 → 2.6; 3.5 → 0.0; 3.6 → 5.1; 3.7 → 2.6; 3.9 → 2.6; 4.0 → 0.0; 4.1 → 2.6; 4.3 → 0.0; 4.8 → 0.0
- c6__otc_W1__R1, destination_keyed: 8.5 → 7.7; 9.5 → 5.1; 10.1 → 5.1; 10.7 → 5.1; 11.2 → 2.6; 11.8 → 20.5; 12.4 → 7.7; 13.1 → 7.7; 14.1 → 0.0; 16.7 → 7.9
- c6__otc_W1__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_W1__R1, issuer_0 [share 50%, all records]: 8.1 → 0.0; 8.4 → 0.0; 8.6 → 0.0; 8.8 → 0.0; 9.0 → 0.0; 9.2 → 0.0; 9.4 → 0.0; 10.0 → 0.0; 10.9 → 0.0; 12.4 → 0.0
- c6__otc_W1__R1, issuer_0 [share 50%, other issuers' devices]: 8.1 → 0.0; 8.4 → 0.0; 8.6 → 0.0; 8.8 → 0.0; 9.0 → 0.0; 9.2 → 0.0; 9.4 → 0.0; 10.0 → 0.0; 10.9 → 0.0; 12.4 → 0.0
- c6__otc_W1__R1, issuer_0_with_observer [share 50%, all records]: 3.1 → 5.1; 3.4 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.3 → 0.0; 5.8 → 0.0; 7.6 → 0.0
- c6__otc_W1__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 3.1 → 5.1; 3.4 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.3 → 0.0; 5.8 → 0.0; 7.6 → 0.0
- c6__otc_W1__R1, issuer_0_with_first_relay [share 50%, all records]: 3.2 → 2.6; 3.4 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.3 → 0.0; 5.8 → 0.0; 7.6 → 0.0
- c6__otc_W1__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.2 → 2.6; 3.4 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.3 → 0.0; 5.8 → 0.0; 7.6 → 0.0
- c6__otc_W1__R1, issuer_1 [share 30%, all records]: 6.1 → 2.6; 6.2 → 0.0; 6.3 → 2.6; 6.5 → 0.0; 7.5 → 0.0; 8.5 → 0.0; 8.7 → 0.0; 8.8 → 0.0; 9.3 → 0.0; 10.4 → 0.0
- c6__otc_W1__R1, issuer_1 [share 30%, its own devices]: 6.1 → 2.6; 6.2 → 0.0; 6.3 → 2.6; 6.5 → 0.0; 7.5 → 0.0; 8.5 → 0.0; 8.7 → 0.0; 8.8 → 0.0; 9.3 → 0.0; 10.4 → 0.0
- c6__otc_W1__R1, issuer_1_with_observer [share 30%, all records]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 2.6; 3.9 → 2.6; 4.1 → 0.0; 4.4 → 0.0; 4.7 → 0.0; 5.2 → 5.1; 5.8 → 2.6; 7.4 → 2.6
- c6__otc_W1__R1, issuer_1_with_observer [share 30%, its own devices]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 2.6; 3.9 → 2.6; 4.1 → 0.0; 4.4 → 0.0; 4.7 → 0.0; 5.2 → 5.1; 5.8 → 2.6; 7.4 → 2.6
- c6__otc_W1__R1, issuer_1_with_first_relay [share 30%, all records]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 2.6; 3.9 → 2.6; 4.1 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.2 → 5.1; 5.8 → 2.6; 7.5 → 2.6
- c6__otc_W1__R1, issuer_1_with_first_relay [share 30%, its own devices]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 2.6; 3.9 → 2.6; 4.1 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.2 → 5.1; 5.8 → 2.6; 7.5 → 2.6
- c6__otc_W1__R1, issuer_1_with_destination: 8.7 → 5.1; 9.9 → 2.6; 10.7 → 7.7; 11.2 → 10.3; 11.8 → 10.3; 12.6 → 2.6; 13.3 → 10.3; 14.2 → 2.6; 15.5 → 15.8; 18.7 → 7.9
- c6__otc_W1__R1, issuer_2 [share 20%, all records]: 13.5 → 0.0; 14.0 → 0.0; 14.3 → 0.0; 14.6 → 0.0; 14.8 → 0.0; 14.9 → 0.0; 15.1 → 0.0; 15.3 → 0.0; 16.4 → 0.0; 19.7 → 0.0
- c6__otc_W1__R1, issuer_2 [share 20%, other issuers' devices]: 13.5 → 0.0; 14.0 → 0.0; 14.3 → 0.0; 14.6 → 0.0; 14.8 → 0.0; 14.9 → 0.0; 15.1 → 0.0; 15.3 → 0.0; 16.4 → 0.0; 19.7 → 0.0
- c6__otc_W1__R1, issuer_2_with_observer [share 20%, all records]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 4.0 → 0.0; 4.3 → 2.6; 4.7 → 0.0; 5.1 → 0.0; 5.6 → 0.0; 6.8 → 0.0
- c6__otc_W1__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 4.0 → 0.0; 4.3 → 2.6; 4.7 → 0.0; 5.1 → 0.0; 5.6 → 0.0; 6.8 → 0.0
- c6__otc_W1__R1, issuer_2_with_first_relay [share 20%, all records]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 4.1 → 0.0; 4.3 → 2.6; 4.7 → 0.0; 5.1 → 0.0; 5.6 → 0.0; 6.8 → 0.0
- c6__otc_W1__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.1 → 5.1; 3.4 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 4.1 → 0.0; 4.3 → 2.6; 4.7 → 0.0; 5.1 → 0.0; 5.6 → 0.0; 6.8 → 0.0
- c6__otc_W1__R100, observer: 3.5 → 0.8; 4.1 → 3.8; 4.5 → 4.6; 4.7 → 9.2; 5.1 → 7.6; 5.6 → 7.6; 6.3 → 6.1; 7.0 → 12.2; 7.6 → 10.7; 8.2 → 9.2
- c6__otc_W1__R100, first_hop: 3.5 → 1.5; 4.1 → 3.8; 4.5 → 4.9; 4.8 → 9.1; 5.1 → 6.6; 5.6 → 8.4; 6.3 → 6.0; 7.0 → 12.1; 7.6 → 10.3; 8.2 → 9.6
- c6__otc_W1__R100, destination: 3.7 → 6.1; 4.2 → 0.8; 4.6 → 3.8; 4.9 → 7.6; 5.3 → 8.4; 5.7 → 5.3; 6.3 → 5.3; 7.0 → 10.7; 7.7 → 9.2; 8.6 → 15.3
- c6__otc_W1__R100, destination_keyed: 6.6 → 3.0; 8.3 → 6.1; 9.3 → 8.4; 10.5 → 12.2; 11.5 → 13.0; 12.6 → 18.3; 13.7 → 15.3; 15.1 → 12.2; 16.7 → 14.5; 21.0 → 35.9
- c6__otc_W1__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_W1__R100, issuer_0 [share 50%, all records]: 9.1 → 6.1; 9.4 → 13.6; 9.6 → 9.9; 9.9 → 8.4; 10.2 → 7.6; 10.4 → 2.3; 10.7 → 3.1; 11.0 → 3.1; 11.6 → 0.8; 13.8 → 0.0
- c6__otc_W1__R100, issuer_0 [share 50%, its own devices]: 9.1 → 11.6; 9.4 → 21.7; 9.6 → 23.2; 9.9 → 15.9; 10.2 → 14.5; 10.5 → 4.3; 10.7 → 4.3; 11.0 → 7.2; 11.7 → 1.4; 13.9 → 0.0
- c6__otc_W1__R100, issuer_0 [share 50%, other issuers' devices]: 6.3 → 0.0; 6.5 → 0.0; 6.7 → 0.0; 7.0 → 0.0; 8.0 → 0.0; 9.2 → 0.0; 9.5 → 0.0; 9.7 → 0.0; 10.0 → 0.0; 10.9 → 0.0
- c6__otc_W1__R100, issuer_0_with_observer [share 50%, all records]: 3.6 → 3.0; 4.2 → 8.3; 4.6 → 6.9; 4.9 → 3.1; 5.3 → 8.4; 5.7 → 7.6; 6.4 → 4.6; 6.8 → 13.0; 7.4 → 3.8; 8.4 → 15.3
- c6__otc_W1__R100, issuer_0_with_observer [share 50%, its own devices]: 3.6 → 0.0; 4.2 → 5.8; 4.6 → 8.7; 4.9 → 4.3; 5.3 → 14.5; 5.8 → 5.8; 6.5 → 11.6; 6.9 → 17.4; 7.5 → 10.1; 8.6 → 26.5
- c6__otc_W1__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 3.6 → 6.3; 4.2 → 11.1; 4.6 → 4.8; 4.8 → 4.8; 5.2 → 1.6; 5.6 → 3.2; 6.2 → 4.8; 6.8 → 3.2; 7.3 → 0.0; 8.2 → 0.0
- c6__otc_W1__R100, issuer_0_with_first_relay [share 50%, all records]: 3.6 → 3.8; 4.3 → 8.3; 4.7 → 6.1; 4.9 → 3.1; 5.3 → 7.6; 5.8 → 6.9; 6.4 → 7.6; 6.9 → 7.6; 7.3 → 9.9; 8.4 → 13.0
- c6__otc_W1__R100, issuer_0_with_first_relay [share 50%, its own devices]: 3.6 → 1.4; 4.3 → 4.3; 4.7 → 4.3; 5.0 → 8.7; 5.4 → 13.0; 5.9 → 7.2; 6.5 → 13.0; 6.9 → 8.7; 7.4 → 20.3; 8.5 → 23.5
- c6__otc_W1__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.6 → 7.9; 4.3 → 12.7; 4.7 → 6.3; 4.9 → 0.0; 5.2 → 3.2; 5.6 → 1.6; 6.2 → 4.8; 6.8 → 3.2; 7.3 → 0.0; 8.2 → 0.0
- c6__otc_W1__R100, issuer_0_with_destination: 5.7 → 2.9; 6.7 → 15.9; 7.3 → 10.1; 7.7 → 7.2; 8.1 → 14.5; 8.5 → 20.3; 9.0 → 13.0; 9.5 → 15.9; 10.4 → 20.3; 12.9 → 2.9
- c6__otc_W1__R100, issuer_1 [share 30%, all records]: 4.2 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.3 → 0.8; 4.4 → 0.0; 4.8 → 0.0; 4.8 → 0.8; 4.8 → 0.8; 4.9 → 0.8; 5.0 → 0.0
- c6__otc_W1__R100, issuer_1 [share 30%, its own devices]: 4.2 → 0.0; 4.2 → 0.0; 4.3 → 0.0; 4.3 → 3.2; 4.4 → 0.0; 4.8 → 0.0; 4.8 → 3.3; 4.8 → 3.3; 4.9 → 3.3; 5.0 → 0.0
- c6__otc_W1__R100, issuer_1 [share 30%, other issuers' devices]: 6.9 → 0.0; 7.0 → 0.0; 7.3 → 0.0; 7.8 → 0.0; 8.0 → 0.0; 8.2 → 0.0; 8.4 → 0.0; 9.0 → 0.0; 9.9 → 0.0; 11.5 → 0.0
- c6__otc_W1__R100, issuer_1_with_observer [share 30%, all records]: 3.5 → 2.3; 4.2 → 3.0; 4.5 → 5.3; 4.8 → 9.2; 5.2 → 6.9; 5.7 → 6.9; 6.4 → 6.9; 7.0 → 11.5; 7.5 → 9.9; 8.4 → 9.9
- c6__otc_W1__R100, issuer_1_with_observer [share 30%, its own devices]: 2.4 → 0.0; 2.7 → 3.2; 2.9 → 6.5; 3.1 → 0.0; 3.7 → 6.5; 4.6 → 6.5; 5.4 → 0.0; 6.3 → 0.0; 7.2 → 0.0; 8.2 → 0.0
- c6__otc_W1__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 3.5 → 3.0; 4.2 → 3.0; 4.5 → 6.9; 4.8 → 9.9; 5.3 → 9.9; 5.8 → 7.9; 6.5 → 10.0; 7.1 → 14.0; 7.5 → 11.0; 8.3 → 11.0
- c6__otc_W1__R100, issuer_1_with_first_relay [share 30%, all records]: 3.5 → 2.3; 4.2 → 3.8; 4.6 → 6.9; 4.8 → 5.3; 5.3 → 6.1; 5.7 → 8.4; 6.5 → 6.1; 7.1 → 16.0; 7.5 → 9.9; 8.3 → 9.9
- c6__otc_W1__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.4 → 0.0; 2.7 → 3.2; 2.9 → 6.5; 3.1 → 0.0; 3.7 → 6.5; 4.6 → 6.5; 5.5 → 0.0; 6.4 → 0.0; 7.2 → 0.0; 8.1 → 0.0
- c6__otc_W1__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.5 → 3.0; 4.2 → 4.0; 4.6 → 7.9; 4.8 → 5.9; 5.3 → 7.9; 5.8 → 10.9; 6.6 → 9.0; 7.1 → 20.0; 7.5 → 11.0; 8.3 → 11.0
- c6__otc_W1__R100, issuer_1_with_destination: 6.6 → 6.5; 7.7 → 6.5; 8.5 → 12.9; 9.2 → 9.7; 10.0 → 25.8; 11.0 → 16.1; 12.3 → 13.3; 13.8 → 6.7; 15.9 → 3.3; 20.0 → 20.0
- c6__otc_W1__R100, issuer_2 [share 20%, all records]: 20.1 → 3.8; 21.6 → 3.0; 23.1 → 11.5; 24.6 → 6.1; 28.1 → 4.6; 31.2 → 3.8; 33.1 → 6.9; 35.2 → 9.2; 36.7 → 4.6; 43.9 → 3.8
- c6__otc_W1__R100, issuer_2 [share 20%, its own devices]: 20.0 → 15.6; 21.5 → 12.5; 23.1 → 46.9; 24.9 → 28.1; 29.4 → 18.8; 32.1 → 28.1; 34.0 → 25.0; 35.8 → 32.3; 37.2 → 16.1; 43.5 → 12.9
- c6__otc_W1__R100, issuer_2 [share 20%, other issuers' devices]: 11.0 → 0.0; 11.3 → 0.0; 11.6 → 0.0; 11.8 → 0.0; 12.5 → 0.0; 13.2 → 0.0; 13.7 → 0.0; 14.2 → 0.0; 15.2 → 0.0; 17.5 → 0.0
- c6__otc_W1__R100, issuer_2_with_observer [share 20%, all records]: 3.5 → 0.8; 4.1 → 3.0; 4.5 → 5.3; 4.9 → 6.1; 5.4 → 9.2; 6.0 → 3.8; 6.6 → 9.9; 7.1 → 12.2; 7.6 → 10.7; 8.4 → 6.1
- c6__otc_W1__R100, issuer_2_with_observer [share 20%, its own devices]: 3.5 → 3.1; 4.1 → 9.4; 4.5 → 9.4; 4.8 → 6.2; 5.3 → 3.1; 5.8 → 6.2; 6.4 → 12.5; 7.0 → 16.1; 7.5 → 0.0; 8.3 → 0.0
- c6__otc_W1__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 3.4 → 0.0; 4.1 → 1.0; 4.5 → 4.0; 4.9 → 6.0; 5.5 → 11.0; 6.0 → 3.0; 6.7 → 12.1; 7.2 → 8.1; 7.6 → 14.1; 8.4 → 8.1
- c6__otc_W1__R100, issuer_2_with_first_relay [share 20%, all records]: 3.5 → 0.8; 4.1 → 3.0; 4.5 → 5.3; 4.9 → 6.1; 5.5 → 8.4; 6.0 → 3.1; 6.7 → 12.2; 7.1 → 12.2; 7.5 → 9.9; 8.4 → 8.4
- c6__otc_W1__R100, issuer_2_with_first_relay [share 20%, its own devices]: 3.6 → 3.1; 4.1 → 9.4; 4.5 → 15.6; 4.9 → 3.1; 5.4 → 3.1; 5.9 → 6.2; 6.5 → 18.8; 7.1 → 9.7; 7.4 → 0.0; 8.2 → 0.0
- c6__otc_W1__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.4 → 0.0; 4.1 → 1.0; 4.5 → 2.0; 5.0 → 7.0; 5.6 → 9.0; 6.0 → 2.0; 6.8 → 12.1; 7.1 → 12.1; 7.5 → 14.1; 8.4 → 10.1
- c6__otc_W1__R100, issuer_2_with_destination: 10.4 → 12.5; 12.2 → 12.5; 13.7 → 18.8; 14.7 → 12.5; 15.8 → 9.4; 16.9 → 15.6; 18.2 → 12.5; 20.9 → 19.4; 24.8 → 25.8; 29.6 → 35.5
- c6__otc_W2__R1, observer: 4.4 → 0.0; 5.0 → 2.7; 5.7 → 5.4; 6.2 → 18.9; 6.9 → 10.8; 7.5 → 16.2; 8.5 → 13.9; 9.6 → 11.1; 11.6 → 0.0; 19.7 → 0.0
- c6__otc_W2__R1, first_hop: 4.4 → 0.8; 5.0 → 4.0; 5.7 → 4.6; 6.2 → 17.9; 6.9 → 12.0; 7.5 → 11.5; 8.4 → 16.4; 9.6 → 12.6; 11.6 → 0.0; 19.6 → 0.0
- c6__otc_W2__R1, destination: 3.4 → 5.4; 3.8 → 2.7; 4.2 → 2.7; 4.5 → 24.3; 4.8 → 5.4; 5.1 → 8.1; 5.6 → 16.7; 6.1 → 0.0; 6.8 → 5.6; 9.9 → 2.8
- c6__otc_W2__R1, destination_keyed: 10.0 → 21.6; 11.5 → 13.5; 12.5 → 5.4; 13.3 → 5.4; 14.3 → 8.1; 15.2 → 13.5; 16.3 → 36.1; 17.9 → 38.9; 20.1 → 30.6; 24.1 → 25.0
- c6__otc_W2__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_W2__R1, issuer_0 [share 50%, all records]: 9.2 → 0.0; 9.5 → 0.0; 9.6 → 0.0; 9.8 → 0.0; 9.9 → 0.0; 10.0 → 0.0; 10.1 → 0.0; 10.6 → 0.0; 11.2 → 0.0; 13.0 → 0.0
- c6__otc_W2__R1, issuer_0 [share 50%, other issuers' devices]: 9.2 → 0.0; 9.5 → 0.0; 9.6 → 0.0; 9.8 → 0.0; 9.9 → 0.0; 10.0 → 0.0; 10.1 → 0.0; 10.6 → 0.0; 11.2 → 0.0; 13.0 → 0.0
- c6__otc_W2__R1, issuer_0_with_observer [share 50%, all records]: 4.3 → 0.0; 4.8 → 13.5; 5.3 → 5.4; 5.7 → 13.5; 6.0 → 8.1; 6.4 → 10.8; 7.0 → 2.8; 7.6 → 11.1; 8.6 → 0.0; 11.5 → 0.0
- c6__otc_W2__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 4.3 → 0.0; 4.8 → 13.5; 5.3 → 5.4; 5.7 → 13.5; 6.0 → 8.1; 6.4 → 10.8; 7.0 → 2.8; 7.6 → 11.1; 8.6 → 0.0; 11.5 → 0.0
- c6__otc_W2__R1, issuer_0_with_first_relay [share 50%, all records]: 4.3 → 0.0; 4.8 → 16.2; 5.3 → 0.0; 5.7 → 13.5; 6.0 → 13.5; 6.4 → 10.8; 7.0 → 2.8; 7.6 → 11.1; 8.6 → 0.0; 11.4 → 0.0
- c6__otc_W2__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.3 → 0.0; 4.8 → 16.2; 5.3 → 0.0; 5.7 → 13.5; 6.0 → 13.5; 6.4 → 10.8; 7.0 → 2.8; 7.6 → 11.1; 8.6 → 0.0; 11.4 → 0.0
- c6__otc_W2__R1, issuer_1 [share 30%, all records]: 4.5 → 0.0; 4.5 → 0.0; 4.5 → 0.0; 4.7 → 8.1; 6.0 → 0.0; 12.6 → 0.0; 13.1 → 0.0; 13.5 → 0.0; 13.8 → 0.0; 16.0 → 0.0
- c6__otc_W2__R1, issuer_1 [share 30%, its own devices]: 4.5 → 0.0; 4.5 → 0.0; 4.5 → 0.0; 4.7 → 8.1; 6.0 → 0.0; 12.6 → 0.0; 13.1 → 0.0; 13.5 → 0.0; 13.8 → 0.0; 16.0 → 0.0
- c6__otc_W2__R1, issuer_1_with_observer [share 30%, all records]: 4.6 → 8.1; 5.5 → 10.8; 6.1 → 5.4; 6.9 → 21.6; 7.5 → 18.9; 8.4 → 18.9; 9.4 → 5.6; 11.0 → 0.0; 13.4 → 5.6; 22.3 → 22.2
- c6__otc_W2__R1, issuer_1_with_observer [share 30%, its own devices]: 4.6 → 8.1; 5.5 → 10.8; 6.1 → 5.4; 6.9 → 21.6; 7.5 → 18.9; 8.4 → 18.9; 9.4 → 5.6; 11.0 → 0.0; 13.4 → 5.6; 22.3 → 22.2
- c6__otc_W2__R1, issuer_1_with_first_relay [share 30%, all records]: 4.6 → 8.1; 5.4 → 10.8; 6.1 → 5.4; 6.9 → 18.9; 7.5 → 27.0; 8.4 → 13.5; 9.5 → 8.3; 10.9 → 0.0; 13.3 → 5.6; 22.3 → 22.2
- c6__otc_W2__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.6 → 8.1; 5.4 → 10.8; 6.1 → 5.4; 6.9 → 18.9; 7.5 → 27.0; 8.4 → 13.5; 9.5 → 8.3; 10.9 → 0.0; 13.3 → 5.6; 22.3 → 22.2
- c6__otc_W2__R1, issuer_1_with_destination: 10.6 → 13.5; 12.5 → 2.7; 13.9 → 13.5; 14.8 → 10.8; 16.0 → 21.6; 17.0 → 35.1; 18.4 → 13.9; 20.4 → 47.2; 23.1 → 22.2; 29.3 → 25.0
- c6__otc_W2__R1, issuer_2 [share 20%, all records]: 8.2 → 0.0; 8.5 → 0.0; 8.9 → 0.0; 11.6 → 0.0; 14.7 → 0.0; 17.0 → 0.0; 17.9 → 0.0; 18.5 → 0.0; 18.7 → 0.0; 21.7 → 0.0
- c6__otc_W2__R1, issuer_2 [share 20%, other issuers' devices]: 8.2 → 0.0; 8.5 → 0.0; 8.9 → 0.0; 11.6 → 0.0; 14.7 → 0.0; 17.0 → 0.0; 17.9 → 0.0; 18.5 → 0.0; 18.7 → 0.0; 21.7 → 0.0
- c6__otc_W2__R1, issuer_2_with_observer [share 20%, all records]: 4.2 → 2.7; 4.7 → 2.7; 5.0 → 5.4; 5.5 → 2.7; 5.9 → 8.1; 6.2 → 16.2; 6.7 → 8.3; 7.3 → 5.6; 8.2 → 8.3; 11.7 → 0.0
- c6__otc_W2__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.2 → 2.7; 4.7 → 2.7; 5.0 → 5.4; 5.5 → 2.7; 5.9 → 8.1; 6.2 → 16.2; 6.7 → 8.3; 7.3 → 5.6; 8.2 → 8.3; 11.7 → 0.0
- c6__otc_W2__R1, issuer_2_with_first_relay [share 20%, all records]: 4.2 → 5.4; 4.7 → 8.1; 5.0 → 2.7; 5.5 → 5.4; 5.8 → 5.4; 6.2 → 18.9; 6.7 → 5.6; 7.3 → 2.8; 8.3 → 11.1; 11.7 → 0.0
- c6__otc_W2__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.2 → 5.4; 4.7 → 8.1; 5.0 → 2.7; 5.5 → 5.4; 5.8 → 5.4; 6.2 → 18.9; 6.7 → 5.6; 7.3 → 2.8; 8.3 → 11.1; 11.7 → 0.0
- c6__otc_W2__R100, observer: 3.7 → 1.6; 4.1 → 4.9; 4.7 → 5.7; 5.2 → 3.3; 5.8 → 4.9; 6.4 → 12.3; 7.0 → 10.7; 7.8 → 9.0; 8.7 → 7.4; 12.2 → 6.6
- c6__otc_W2__R100, first_hop: 3.7 → 2.1; 4.1 → 4.4; 4.7 → 4.9; 5.2 → 3.8; 5.8 → 5.2; 6.4 → 12.0; 7.0 → 10.2; 7.8 → 9.5; 8.7 → 7.5; 12.2 → 6.6
- c6__otc_W2__R100, destination: 3.7 → 3.3; 4.3 → 2.5; 4.9 → 1.6; 5.3 → 2.5; 5.8 → 7.4; 6.4 → 7.4; 7.0 → 8.2; 7.8 → 11.5; 9.0 → 7.4; 12.6 → 7.4
- c6__otc_W2__R100, destination_keyed: 6.2 → 8.9; 7.8 → 6.6; 9.2 → 9.8; 10.6 → 9.0; 11.9 → 11.5; 13.2 → 7.4; 14.6 → 8.2; 16.3 → 18.9; 18.7 → 18.0; 26.4 → 18.9
- c6__otc_W2__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_W2__R100, issuer_0 [share 50%, all records]: 6.8 → 0.0; 7.0 → 0.0; 7.2 → 0.0; 7.5 → 0.0; 8.4 → 0.0; 9.2 → 7.4; 9.5 → 13.1; 9.8 → 5.7; 10.2 → 6.6; 11.2 → 12.3
- c6__otc_W2__R100, issuer_0 [share 50%, its own devices]: 6.7 → 0.0; 7.0 → 0.0; 7.2 → 0.0; 7.5 → 0.0; 8.5 → 0.0; 9.2 → 14.3; 9.5 → 20.0; 9.8 → 11.4; 10.2 → 12.9; 11.2 → 20.0
- c6__otc_W2__R100, issuer_0 [share 50%, other issuers' devices]: 6.8 → 0.0; 7.0 → 0.0; 7.3 → 0.0; 7.5 → 0.0; 8.3 → 0.0; 9.2 → 0.0; 9.6 → 0.0; 9.9 → 0.0; 10.2 → 0.0; 11.2 → 0.0
- c6__otc_W2__R100, issuer_0_with_observer [share 50%, all records]: 3.8 → 3.3; 4.5 → 2.5; 5.1 → 7.4; 5.7 → 5.7; 6.0 → 3.3; 6.6 → 7.4; 7.4 → 7.4; 8.2 → 9.8; 9.9 → 9.0; 13.2 → 8.2
- c6__otc_W2__R100, issuer_0_with_observer [share 50%, its own devices]: 3.7 → 5.6; 4.5 → 5.6; 5.2 → 11.3; 5.7 → 5.6; 6.1 → 5.7; 6.7 → 7.1; 7.4 → 11.4; 8.3 → 17.1; 10.0 → 12.9; 13.2 → 7.1
- c6__otc_W2__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.7 → 0.0; 3.2 → 0.0; 3.5 → 11.5; 3.9 → 1.9; 4.3 → 1.9; 4.7 → 3.8; 5.4 → 9.6; 6.1 → 0.0; 7.2 → 0.0; 10.6 → 0.0
- c6__otc_W2__R100, issuer_0_with_first_relay [share 50%, all records]: 3.8 → 2.4; 4.5 → 1.6; 5.0 → 7.4; 5.6 → 3.3; 6.1 → 4.1; 6.6 → 7.4; 7.3 → 6.6; 8.2 → 9.8; 9.9 → 9.8; 13.2 → 8.2
- c6__otc_W2__R100, issuer_0_with_first_relay [share 50%, its own devices]: 3.8 → 4.2; 4.5 → 4.2; 5.1 → 9.9; 5.7 → 8.5; 6.2 → 5.7; 6.7 → 5.7; 7.4 → 11.4; 8.4 → 17.1; 10.0 → 12.9; 13.2 → 7.1
- c6__otc_W2__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.7 → 0.0; 3.2 → 0.0; 3.4 → 7.7; 3.9 → 1.9; 4.3 → 0.0; 4.7 → 5.8; 5.4 → 9.6; 6.2 → 0.0; 7.2 → 0.0; 10.6 → 0.0
- c6__otc_W2__R100, issuer_0_with_destination: 4.8 → 12.7; 5.9 → 7.0; 6.7 → 7.0; 7.6 → 8.5; 8.3 → 12.9; 9.1 → 10.0; 10.2 → 15.7; 11.6 → 12.9; 13.9 → 11.4; 21.0 → 1.4
- c6__otc_W2__R100, issuer_1 [share 30%, all records]: 7.9 → 1.6; 8.0 → 0.8; 8.1 → 2.5; 8.2 → 1.6; 8.6 → 9.0; 17.1 → 0.0; 18.8 → 0.0; 19.8 → 0.0; 20.6 → 0.0; 24.4 → 0.0
- c6__otc_W2__R100, issuer_1 [share 30%, its own devices]: 7.9 → 8.3; 8.0 → 4.2; 8.1 → 8.3; 8.2 → 8.3; 8.4 → 33.3; 12.4 → 16.7; 18.1 → 0.0; 19.6 → 0.0; 20.5 → 0.0; 24.1 → 0.0
- c6__otc_W2__R100, issuer_1 [share 30%, other issuers' devices]: 11.1 → 0.0; 11.3 → 0.0; 11.4 → 0.0; 11.5 → 0.0; 11.7 → 0.0; 11.8 → 0.0; 12.1 → 0.0; 12.4 → 0.0; 12.7 → 0.0; 14.5 → 0.0
- c6__otc_W2__R100, issuer_1_with_observer [share 30%, all records]: 3.7 → 4.9; 4.3 → 3.3; 4.8 → 3.3; 5.4 → 4.1; 6.0 → 2.5; 6.4 → 10.7; 7.0 → 9.0; 7.9 → 11.5; 8.7 → 6.6; 12.6 → 6.6
- c6__otc_W2__R100, issuer_1_with_observer [share 30%, its own devices]: 1.8 → 0.0; 2.1 → 0.0; 2.3 → 12.5; 2.4 → 12.5; 2.7 → 12.5; 3.4 → 20.8; 4.4 → 0.0; 5.5 → 0.0; 6.7 → 0.0; 8.4 → 0.0
- c6__otc_W2__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 3.7 → 6.1; 4.3 → 4.0; 4.8 → 4.0; 5.4 → 3.0; 6.0 → 4.1; 6.5 → 12.2; 7.0 → 8.2; 7.8 → 11.2; 8.6 → 9.2; 12.7 → 1.0
- c6__otc_W2__R100, issuer_1_with_first_relay [share 30%, all records]: 3.7 → 3.3; 4.3 → 4.1; 4.8 → 4.1; 5.3 → 1.6; 5.9 → 4.1; 6.4 → 9.8; 7.0 → 11.5; 7.9 → 9.0; 8.7 → 7.4; 12.6 → 6.6
- c6__otc_W2__R100, issuer_1_with_first_relay [share 30%, its own devices]: 1.8 → 0.0; 2.1 → 0.0; 2.3 → 12.5; 2.4 → 12.5; 2.6 → 12.5; 3.3 → 20.8; 4.4 → 0.0; 5.4 → 0.0; 6.8 → 0.0; 8.4 → 0.0
- c6__otc_W2__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.7 → 4.0; 4.3 → 5.1; 4.8 → 5.1; 5.4 → 2.0; 6.0 → 4.1; 6.4 → 10.2; 7.0 → 12.2; 7.9 → 9.2; 8.7 → 9.2; 12.6 → 1.0
- c6__otc_W2__R100, issuer_1_with_destination: 6.8 → 12.5; 7.7 → 8.3; 8.2 → 0.0; 8.8 → 12.5; 9.5 → 4.2; 10.3 → 8.3; 11.1 → 16.7; 12.3 → 4.3; 15.0 → 13.0; 19.1 → 34.8
- c6__otc_W2__R100, issuer_2 [share 20%, all records]: 7.5 → 2.4; 7.8 → 1.6; 8.2 → 0.0; 8.7 → 1.6; 11.8 → 3.3; 22.8 → 8.2; 23.7 → 5.7; 24.4 → 6.6; 24.8 → 4.9; 27.3 → 4.1
- c6__otc_W2__R100, issuer_2 [share 20%, its own devices]: 7.5 → 7.1; 7.7 → 7.1; 8.0 → 3.6; 8.4 → 3.6; 9.8 → 10.7; 19.8 → 32.1; 23.4 → 25.0; 24.2 → 35.7; 24.8 → 25.0; 26.5 → 17.9
- c6__otc_W2__R100, issuer_2 [share 20%, other issuers' devices]: 7.5 → 0.0; 7.8 → 0.0; 8.2 → 0.0; 8.8 → 0.0; 13.0 → 0.0; 23.0 → 0.0; 23.8 → 0.0; 24.4 → 0.0; 24.8 → 0.0; 27.5 → 0.0
- c6__otc_W2__R100, issuer_2_with_observer [share 20%, all records]: 3.7 → 4.1; 4.1 → 6.6; 4.7 → 1.6; 5.3 → 7.4; 5.9 → 4.9; 6.5 → 9.8; 7.1 → 7.4; 8.1 → 11.5; 8.9 → 4.1; 12.4 → 7.4
- c6__otc_W2__R100, issuer_2_with_observer [share 20%, its own devices]: 3.7 → 10.7; 4.1 → 10.7; 4.6 → 7.1; 5.2 → 7.1; 5.8 → 0.0; 6.4 → 10.7; 7.1 → 0.0; 7.9 → 0.0; 8.7 → 3.6; 12.5 → 3.6
- c6__otc_W2__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 3.7 → 2.1; 4.1 → 4.3; 4.8 → 1.1; 5.3 → 7.4; 5.9 → 5.3; 6.6 → 10.6; 7.2 → 9.6; 8.1 → 16.0; 8.9 → 3.2; 12.4 → 8.5
- c6__otc_W2__R100, issuer_2_with_first_relay [share 20%, all records]: 3.7 → 3.3; 4.1 → 6.6; 4.7 → 1.6; 5.2 → 8.2; 5.9 → 5.7; 6.6 → 7.4; 7.1 → 7.4; 8.1 → 9.8; 8.9 → 5.7; 12.2 → 7.4
- c6__otc_W2__R100, issuer_2_with_first_relay [share 20%, its own devices]: 3.6 → 10.7; 4.1 → 10.7; 4.6 → 3.6; 5.1 → 10.7; 5.8 → 10.7; 6.5 → 0.0; 7.1 → 0.0; 8.0 → 0.0; 8.7 → 3.6; 12.4 → 3.6
- c6__otc_W2__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.7 → 1.1; 4.1 → 4.3; 4.7 → 4.3; 5.2 → 5.3; 5.9 → 4.3; 6.6 → 10.6; 7.1 → 8.5; 8.1 → 13.8; 9.0 → 5.3; 12.2 → 8.5
- c6__otc_W2__R100, issuer_2_with_destination: 9.1 → 14.3; 10.7 → 10.7; 11.6 → 17.9; 12.9 → 17.9; 13.9 → 14.3; 14.8 → 17.9; 15.8 → 17.9; 17.1 → 7.1; 19.4 → 7.1; 22.7 → 21.4
- c6__otc_Wmis__R1, observer: 4.2 → 5.4; 4.7 → 2.7; 5.2 → 16.2; 5.8 → 29.7; 6.4 → 13.5; 7.2 → 13.5; 8.0 → 8.3; 9.2 → 19.4; 11.1 → 38.9; 14.8 → 58.3
- c6__otc_Wmis__R1, first_hop: 4.2 → 2.6; 4.7 → 6.8; 5.2 → 15.7; 5.8 → 28.4; 6.4 → 12.7; 7.2 → 13.8; 8.0 → 8.3; 9.2 → 18.0; 11.1 → 35.4; 14.9 → 59.7
- c6__otc_Wmis__R1, destination: 4.4 → 2.7; 5.1 → 8.1; 5.7 → 8.1; 6.3 → 13.5; 7.0 → 18.9; 7.9 → 10.8; 8.8 → 19.4; 10.0 → 11.1; 11.9 → 36.1; 16.2 → 50.0
- c6__otc_Wmis__R1, destination_keyed: 10.0 → 8.1; 11.7 → 13.5; 12.7 → 13.5; 13.8 → 24.3; 14.8 → 8.1; 15.6 → 2.7; 16.9 → 41.7; 18.5 → 22.2; 21.4 → 52.8; 30.5 → 66.7
- c6__otc_Wmis__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_Wmis__R1, issuer_0 [share 50%, all records]: 2.5 → 0.0; 3.0 → 0.0; 3.4 → 0.0; 3.9 → 0.0; 4.6 → 0.0; 5.2 → 0.0; 5.7 → 0.0; 6.1 → 0.0; 6.4 → 0.0; 6.8 → 0.0
- c6__otc_Wmis__R1, issuer_0 [share 50%, other issuers' devices]: 2.5 → 0.0; 3.0 → 0.0; 3.4 → 0.0; 3.9 → 0.0; 4.6 → 0.0; 5.2 → 0.0; 5.7 → 0.0; 6.1 → 0.0; 6.4 → 0.0; 6.8 → 0.0
- c6__otc_Wmis__R1, issuer_0_with_observer [share 50%, all records]: 4.1 → 5.4; 4.7 → 2.7; 5.3 → 10.8; 5.8 → 27.0; 6.3 → 8.1; 6.9 → 2.7; 7.7 → 19.4; 8.6 → 25.0; 10.3 → 13.9; 14.0 → 22.2
- c6__otc_Wmis__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 4.1 → 5.4; 4.7 → 2.7; 5.3 → 10.8; 5.8 → 27.0; 6.3 → 8.1; 6.9 → 2.7; 7.7 → 19.4; 8.6 → 25.0; 10.3 → 13.9; 14.0 → 22.2
- c6__otc_Wmis__R1, issuer_0_with_first_relay [share 50%, all records]: 4.1 → 5.4; 4.7 → 5.4; 5.3 → 10.8; 5.8 → 27.0; 6.3 → 2.7; 7.0 → 8.1; 7.7 → 16.7; 8.7 → 27.8; 10.3 → 13.9; 13.9 → 22.2
- c6__otc_Wmis__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.1 → 5.4; 4.7 → 5.4; 5.3 → 10.8; 5.8 → 27.0; 6.3 → 2.7; 7.0 → 8.1; 7.7 → 16.7; 8.7 → 27.8; 10.3 → 13.9; 13.9 → 22.2
- c6__otc_Wmis__R1, issuer_1 [share 30%, all records]: 3.4 → 0.0; 3.5 → 5.4; 3.6 → 10.8; 3.7 → 10.8; 3.7 → 18.9; 4.3 → 2.7; 7.1 → 2.8; 10.7 → 2.8; 14.7 → 11.1; 17.7 → 11.1
- c6__otc_Wmis__R1, issuer_1 [share 30%, its own devices]: 3.4 → 0.0; 3.5 → 5.4; 3.6 → 10.8; 3.7 → 10.8; 3.7 → 18.9; 4.3 → 2.7; 7.1 → 2.8; 10.7 → 2.8; 14.7 → 11.1; 17.7 → 11.1
- c6__otc_Wmis__R1, issuer_1_with_observer [share 30%, all records]: 4.3 → 5.4; 5.0 → 16.2; 6.0 → 2.7; 7.2 → 13.5; 8.2 → 5.4; 9.6 → 16.2; 11.7 → 27.8; 13.9 → 22.2; 18.3 → 36.1; 34.9 → 27.8
- c6__otc_Wmis__R1, issuer_1_with_observer [share 30%, its own devices]: 4.3 → 5.4; 5.0 → 16.2; 6.0 → 2.7; 7.2 → 13.5; 8.2 → 5.4; 9.6 → 16.2; 11.7 → 27.8; 13.9 → 22.2; 18.3 → 36.1; 34.9 → 27.8
- c6__otc_Wmis__R1, issuer_1_with_first_relay [share 30%, all records]: 4.3 → 5.4; 5.0 → 18.9; 6.0 → 0.0; 7.2 → 13.5; 8.2 → 8.1; 9.7 → 8.1; 11.7 → 25.0; 14.1 → 30.6; 18.2 → 30.6; 34.5 → 27.8
- c6__otc_Wmis__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.3 → 5.4; 5.0 → 18.9; 6.0 → 0.0; 7.2 → 13.5; 8.2 → 8.1; 9.7 → 8.1; 11.7 → 25.0; 14.1 → 30.6; 18.2 → 30.6; 34.5 → 27.8
- c6__otc_Wmis__R1, issuer_1_with_destination: 9.3 → 13.5; 10.9 → 8.1; 11.9 → 13.5; 13.0 → 27.0; 14.6 → 16.2; 16.7 → 27.0; 18.9 → 25.0; 22.2 → 30.6; 27.0 → 19.4; 37.7 → 33.3
- c6__otc_Wmis__R1, issuer_2 [share 20%, all records]: 5.0 → 0.0; 5.3 → 0.0; 5.9 → 0.0; 6.1 → 0.0; 7.0 → 0.0; 7.9 → 0.0; 9.1 → 0.0; 10.2 → 0.0; 12.1 → 0.0; 14.3 → 0.0
- c6__otc_Wmis__R1, issuer_2 [share 20%, other issuers' devices]: 5.0 → 0.0; 5.3 → 0.0; 5.9 → 0.0; 6.1 → 0.0; 7.0 → 0.0; 7.9 → 0.0; 9.1 → 0.0; 10.2 → 0.0; 12.1 → 0.0; 14.3 → 0.0
- c6__otc_Wmis__R1, issuer_2_with_observer [share 20%, all records]: 4.3 → 5.4; 4.9 → 13.5; 5.6 → 21.6; 6.2 → 18.9; 7.2 → 8.1; 8.1 → 10.8; 9.2 → 16.7; 11.0 → 36.1; 14.0 → 33.3; 21.8 → 16.7
- c6__otc_Wmis__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.3 → 5.4; 4.9 → 13.5; 5.6 → 21.6; 6.2 → 18.9; 7.2 → 8.1; 8.1 → 10.8; 9.2 → 16.7; 11.0 → 36.1; 14.0 → 33.3; 21.8 → 16.7
- c6__otc_Wmis__R1, issuer_2_with_first_relay [share 20%, all records]: 4.3 → 5.4; 4.9 → 13.5; 5.5 → 16.2; 6.2 → 21.6; 7.2 → 13.5; 8.1 → 5.4; 9.3 → 22.2; 11.1 → 27.8; 13.9 → 38.9; 22.0 → 16.7
- c6__otc_Wmis__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.3 → 5.4; 4.9 → 13.5; 5.5 → 16.2; 6.2 → 21.6; 7.2 → 13.5; 8.1 → 5.4; 9.3 → 22.2; 11.1 → 27.8; 13.9 → 38.9; 22.0 → 16.7
- c6__otc_Wmis__R100, observer: 5.0 → 4.9; 5.8 → 4.9; 6.8 → 6.6; 7.7 → 8.2; 8.6 → 9.0; 10.2 → 10.7; 12.6 → 9.0; 14.4 → 14.8; 17.1 → 13.1; 25.2 → 14.8
- c6__otc_Wmis__R100, first_hop: 5.0 → 5.2; 5.8 → 4.9; 6.8 → 6.4; 7.7 → 8.1; 8.7 → 9.8; 10.3 → 9.5; 12.5 → 9.0; 14.4 → 14.2; 17.1 → 13.6; 25.2 → 14.8
- c6__otc_Wmis__R100, destination: 3.1 → 4.9; 3.5 → 5.7; 3.9 → 3.3; 4.2 → 4.9; 4.6 → 7.4; 5.1 → 9.0; 5.7 → 9.8; 6.3 → 14.8; 7.1 → 11.5; 9.6 → 14.8
- c6__otc_Wmis__R100, destination_keyed: 5.5 → 9.8; 6.5 → 8.2; 7.4 → 8.2; 8.7 → 12.3; 9.8 → 13.1; 11.0 → 16.4; 12.1 → 16.4; 13.3 → 18.9; 15.3 → 23.8; 21.2 → 36.9
- c6__otc_Wmis__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_Wmis__R100, issuer_0 [share 50%, all records]: 5.2 → 7.3; 5.6 → 4.9; 6.1 → 3.3; 7.1 → 3.3; 9.6 → 5.7; 41.2 → 11.5; 47.2 → 9.8; 49.3 → 2.5; 52.4 → 10.7; 57.8 → 12.3
- c6__otc_Wmis__R100, issuer_0 [share 50%, its own devices]: 5.2 → 15.5; 5.7 → 5.6; 6.1 → 7.0; 7.3 → 4.2; 10.7 → 12.9; 43.3 → 17.1; 47.1 → 17.1; 49.2 → 7.1; 52.6 → 15.7; 57.9 → 21.4
- c6__otc_Wmis__R100, issuer_0 [share 50%, other issuers' devices]: 3.7 → 0.0; 3.9 → 0.0; 4.2 → 0.0; 4.6 → 0.0; 5.5 → 0.0; 8.3 → 0.0; 9.1 → 0.0; 9.2 → 0.0; 9.5 → 0.0; 10.4 → 0.0
- c6__otc_Wmis__R100, issuer_0_with_observer [share 50%, all records]: 3.3 → 4.9; 3.9 → 5.7; 4.2 → 9.0; 4.5 → 5.7; 4.9 → 4.9; 5.4 → 6.6; 5.9 → 8.2; 6.5 → 10.7; 7.4 → 13.9; 11.0 → 15.6
- c6__otc_Wmis__R100, issuer_0_with_observer [share 50%, its own devices]: 3.8 → 9.9; 4.9 → 11.3; 5.6 → 8.5; 6.3 → 9.9; 6.9 → 17.1; 7.8 → 12.9; 8.9 → 12.9; 10.2 → 10.0; 12.3 → 15.7; 20.5 → 2.9
- c6__otc_Wmis__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 3.3 → 5.8; 3.9 → 1.9; 4.2 → 9.6; 4.4 → 1.9; 4.9 → 1.9; 5.4 → 3.8; 5.8 → 0.0; 6.4 → 2.0; 7.5 → 9.8; 11.4 → 13.7
- c6__otc_Wmis__R100, issuer_0_with_first_relay [share 50%, all records]: 3.3 → 4.9; 3.9 → 4.1; 4.2 → 9.8; 4.5 → 6.6; 4.9 → 4.9; 5.4 → 7.4; 5.9 → 5.7; 6.5 → 11.5; 7.5 → 13.9; 11.0 → 15.6
- c6__otc_Wmis__R100, issuer_0_with_first_relay [share 50%, its own devices]: 3.8 → 9.9; 4.8 → 11.3; 5.6 → 7.0; 6.3 → 11.3; 7.0 → 15.7; 7.9 → 12.9; 8.8 → 10.0; 10.1 → 12.9; 12.1 → 15.7; 20.4 → 2.9
- c6__otc_Wmis__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.3 → 5.8; 3.9 → 1.9; 4.2 → 9.6; 4.4 → 1.9; 4.8 → 0.0; 5.4 → 5.8; 5.9 → 0.0; 6.4 → 2.0; 7.5 → 9.8; 11.4 → 13.7
- c6__otc_Wmis__R100, issuer_0_with_destination: 5.9 → 8.5; 6.7 → 7.0; 7.5 → 14.1; 8.2 → 7.0; 8.8 → 10.0; 9.5 → 5.7; 10.5 → 10.0; 11.5 → 17.1; 13.2 → 25.7; 19.5 → 18.6
- c6__otc_Wmis__R100, issuer_1 [share 30%, all records]: 11.5 → 1.6; 11.9 → 2.5; 12.2 → 0.8; 12.5 → 3.3; 15.3 → 0.8; 45.8 → 2.5; 49.7 → 1.6; 52.0 → 1.6; 53.3 → 1.6; 57.4 → 9.0
- c6__otc_Wmis__R100, issuer_1 [share 30%, its own devices]: 11.6 → 12.5; 12.0 → 12.5; 12.4 → 4.2; 12.9 → 16.7; 34.3 → 4.2; 48.6 → 12.5; 50.8 → 4.2; 52.5 → 8.7; 53.7 → 21.7; 57.6 → 34.8
- c6__otc_Wmis__R100, issuer_1 [share 30%, other issuers' devices]: 8.3 → 0.0; 8.5 → 0.0; 8.6 → 0.0; 8.7 → 0.0; 9.1 → 0.0; 14.6 → 0.0; 15.3 → 0.0; 15.7 → 0.0; 16.0 → 0.0; 17.1 → 0.0
- c6__otc_Wmis__R100, issuer_1_with_observer [share 30%, all records]: 3.0 → 7.3; 3.4 → 2.5; 3.8 → 7.4; 4.2 → 8.2; 4.5 → 7.4; 5.1 → 8.2; 5.6 → 10.7; 6.3 → 15.6; 7.1 → 9.0; 9.5 → 16.4
- c6__otc_Wmis__R100, issuer_1_with_observer [share 30%, its own devices]: 2.1 → 0.0; 2.4 → 4.2; 2.6 → 0.0; 3.0 → 29.2; 3.3 → 4.2; 3.8 → 16.7; 4.3 → 0.0; 5.0 → 13.0; 6.1 → 17.4; 7.9 → 0.0
- c6__otc_Wmis__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 4.9 → 6.1; 5.8 → 5.1; 6.9 → 9.1; 7.9 → 6.1; 8.9 → 12.2; 10.6 → 6.1; 12.5 → 8.2; 14.4 → 19.4; 17.1 → 13.3; 24.9 → 9.2
- c6__otc_Wmis__R100, issuer_1_with_first_relay [share 30%, all records]: 3.1 → 3.3; 3.7 → 5.7; 4.2 → 6.6; 5.0 → 5.7; 5.7 → 12.3; 7.3 → 9.0; 9.0 → 7.4; 12.3 → 9.8; 15.2 → 16.4; 20.6 → 13.1
- c6__otc_Wmis__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.1 → 0.0; 2.4 → 0.0; 2.6 → 4.2; 3.0 → 29.2; 3.2 → 0.0; 3.8 → 20.8; 4.2 → 0.0; 5.0 → 13.0; 6.0 → 17.4; 7.9 → 0.0
- c6__otc_Wmis__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 4.9 → 5.1; 5.8 → 5.1; 6.9 → 7.1; 7.8 → 9.1; 8.9 → 10.2; 10.6 → 6.1; 12.2 → 6.1; 14.3 → 15.3; 17.2 → 16.3; 25.0 → 10.2
- c6__otc_Wmis__R100, issuer_1_with_destination: 6.5 → 8.3; 7.3 → 12.5; 7.8 → 12.5; 8.5 → 20.8; 9.4 → 12.5; 10.4 → 16.7; 11.4 → 12.5; 12.5 → 34.8; 14.2 → 13.0; 17.5 → 30.4
- c6__otc_Wmis__R100, issuer_2 [share 20%, all records]: 10.7 → 2.4; 11.4 → 1.6; 12.0 → 6.6; 12.3 → 1.6; 17.5 → 4.1; 30.1 → 9.0; 31.6 → 5.7; 32.5 → 3.3; 33.4 → 7.4; 38.1 → 4.1
- c6__otc_Wmis__R100, issuer_2 [share 20%, its own devices]: 10.7 → 10.7; 11.3 → 7.1; 11.9 → 21.4; 12.0 → 7.1; 14.0 → 10.7; 27.0 → 25.0; 31.2 → 39.3; 32.1 → 25.0; 33.1 → 28.6; 36.6 → 25.0
- c6__otc_Wmis__R100, issuer_2 [share 20%, other issuers' devices]: 8.1 → 0.0; 8.5 → 0.0; 8.7 → 0.0; 9.0 → 0.0; 11.7 → 0.0; 15.5 → 0.0; 16.0 → 0.0; 16.2 → 0.0; 16.6 → 0.0; 18.5 → 0.0
- c6__otc_Wmis__R100, issuer_2_with_observer [share 20%, all records]: 3.0 → 1.6; 3.4 → 4.1; 3.8 → 8.2; 4.1 → 13.1; 4.5 → 9.0; 5.2 → 6.6; 5.7 → 11.5; 6.4 → 13.1; 7.2 → 10.7; 10.0 → 14.8
- c6__otc_Wmis__R100, issuer_2_with_observer [share 20%, its own devices]: 3.0 → 0.0; 3.6 → 0.0; 4.1 → 21.4; 5.0 → 3.6; 6.0 → 10.7; 7.9 → 14.3; 10.6 → 7.1; 13.4 → 3.6; 15.7 → 0.0; 20.3 → 0.0
- c6__otc_Wmis__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 3.0 → 2.1; 3.5 → 7.4; 3.9 → 6.4; 4.1 → 10.6; 4.5 → 9.6; 5.2 → 6.4; 5.7 → 12.8; 6.4 → 16.0; 7.2 → 13.8; 10.0 → 17.0
- c6__otc_Wmis__R100, issuer_2_with_first_relay [share 20%, all records]: 3.0 → 1.6; 3.4 → 3.3; 3.8 → 6.6; 4.1 → 12.3; 4.5 → 11.5; 5.1 → 7.4; 5.7 → 9.8; 6.4 → 13.1; 7.2 → 9.8; 9.8 → 15.6
- c6__otc_Wmis__R100, issuer_2_with_first_relay [share 20%, its own devices]: 3.0 → 3.6; 3.6 → 0.0; 4.1 → 21.4; 5.0 → 3.6; 6.0 → 10.7; 7.8 → 14.3; 10.3 → 7.1; 13.3 → 3.6; 15.8 → 0.0; 20.5 → 0.0
- c6__otc_Wmis__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.0 → 2.1; 3.5 → 4.3; 3.9 → 6.4; 4.1 → 8.5; 4.5 → 13.8; 5.2 → 6.4; 5.7 → 9.6; 6.4 → 17.0; 7.3 → 12.8; 9.9 → 18.1
- c6__otc_Wmis__R100, issuer_2_with_destination: 9.5 → 7.1; 11.1 → 17.9; 12.2 → 21.4; 13.1 → 17.9; 13.8 → 32.1; 14.9 → 39.3; 16.4 → 25.0; 17.3 → 32.1; 19.8 → 14.3; 25.3 → 32.1
- c6__otc_chain100__R1, observer: 4.1 → 9.3; 4.5 → 4.8; 4.8 → 2.4; 5.0 → 2.4; 5.2 → 4.8; 5.4 → 2.4; 5.7 → 4.8; 6.0 → 7.1; 6.5 → 2.4; 7.5 → 7.1
- c6__otc_chain100__R1, first_hop: 4.1 → 6.8; 4.5 → 6.4; 4.8 → 2.0; 5.0 → 4.2; 5.2 → 3.8; 5.4 → 2.1; 5.7 → 6.3; 6.0 → 5.3; 6.5 → 4.4; 7.6 → 5.7
- c6__otc_chain100__R1, destination: 3.3 → 9.3; 3.6 → 7.1; 3.9 → 0.0; 4.2 → 9.5; 4.5 → 4.8; 4.8 → 7.1; 5.1 → 4.8; 5.6 → 2.4; 6.2 → 2.4; 7.5 → 0.0
- c6__otc_chain100__R1, destination_keyed: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.8 → 2.4; 3.7 → 7.1; 4.8 → 4.8; 6.5 → 0.0
- c6__otc_chain100__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_chain100__R1, issuer_0 [share 50%, all records]: 2.2 → 0.0; 2.5 → 0.0; 2.9 → 0.0; 3.6 → 0.0; 4.2 → 0.0; 5.0 → 0.0; 6.1 → 0.0; 7.0 → 0.0; 7.8 → 0.0; 8.6 → 0.0
- c6__otc_chain100__R1, issuer_0 [share 50%, other issuers' devices]: 2.2 → 0.0; 2.5 → 0.0; 2.9 → 0.0; 3.6 → 0.0; 4.2 → 0.0; 5.0 → 0.0; 6.1 → 0.0; 7.0 → 0.0; 7.8 → 0.0; 8.6 → 0.0
- c6__otc_chain100__R1, issuer_0_with_observer [share 50%, all records]: 3.3 → 11.6; 3.6 → 7.1; 3.9 → 4.8; 4.4 → 9.5; 4.8 → 2.4; 5.3 → 0.0; 6.0 → 0.0; 6.9 → 0.0; 8.5 → 0.0; 13.7 → 0.0
- c6__otc_chain100__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 3.3 → 11.6; 3.6 → 7.1; 3.9 → 4.8; 4.4 → 9.5; 4.8 → 2.4; 5.3 → 0.0; 6.0 → 0.0; 6.9 → 0.0; 8.5 → 0.0; 13.7 → 0.0
- c6__otc_chain100__R1, issuer_0_with_first_relay [share 50%, all records]: 3.3 → 11.6; 3.6 → 7.1; 3.9 → 4.8; 4.4 → 7.1; 4.8 → 4.8; 5.4 → 2.4; 6.0 → 0.0; 6.9 → 0.0; 8.5 → 0.0; 13.7 → 0.0
- c6__otc_chain100__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 3.3 → 11.6; 3.6 → 7.1; 3.9 → 4.8; 4.4 → 7.1; 4.8 → 4.8; 5.4 → 2.4; 6.0 → 0.0; 6.9 → 0.0; 8.5 → 0.0; 13.7 → 0.0
- c6__otc_chain100__R1, issuer_1 [share 30%, all records]: 3.4 → 0.0; 3.5 → 2.4; 3.6 → 0.0; 4.0 → 2.4; 4.7 → 4.8; 5.5 → 7.1; 6.2 → 4.8; 9.7 → 7.1; 16.6 → 7.1; 24.6 → 4.8
- c6__otc_chain100__R1, issuer_1 [share 30%, its own devices]: 3.4 → 0.0; 3.4 → 3.4; 3.6 → 0.0; 3.9 → 0.0; 4.9 → 10.3; 5.5 → 7.1; 6.5 → 7.1; 10.5 → 7.1; 17.4 → 7.1; 24.7 → 3.6
- c6__otc_chain100__R1, issuer_1 [share 30%, other issuers' devices]: 3.4 → 0.0; 3.4 → 0.0; 3.5 → 7.1; 3.6 → 0.0; 3.8 → 0.0; 4.1 → 0.0; 4.4 → 0.0; 6.2 → 7.7; 8.9 → 7.7; 12.3 → 7.7
- c6__otc_chain100__R1, issuer_1_with_observer [share 30%, all records]: 4.3 → 7.0; 4.8 → 4.8; 5.0 → 7.1; 5.3 → 7.1; 5.8 → 2.4; 6.3 → 0.0; 7.0 → 14.3; 8.1 → 4.8; 10.0 → 7.1; 15.3 → 9.5
- c6__otc_chain100__R1, issuer_1_with_observer [share 30%, its own devices]: 4.3 → 6.9; 4.7 → 3.4; 5.0 → 6.9; 5.3 → 6.9; 5.8 → 3.4; 6.3 → 0.0; 7.1 → 14.3; 8.2 → 7.1; 10.2 → 14.3; 15.6 → 7.1
- c6__otc_chain100__R1, issuer_1_with_observer [share 30%, other issuers' devices]: 3.3 → 14.3; 3.6 → 0.0; 3.8 → 0.0; 4.3 → 21.4; 4.7 → 0.0; 5.3 → 7.1; 5.9 → 0.0; 6.8 → 0.0; 8.8 → 7.7; 12.1 → 0.0
- c6__otc_chain100__R1, issuer_1_with_first_relay [share 30%, all records]: 4.3 → 4.7; 4.8 → 2.4; 5.0 → 7.1; 5.4 → 4.8; 5.8 → 4.8; 6.3 → 4.8; 7.0 → 7.1; 8.1 → 7.1; 10.0 → 7.1; 15.3 → 9.5
- c6__otc_chain100__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.3 → 3.4; 4.7 → 0.0; 5.0 → 3.4; 5.3 → 6.9; 5.8 → 6.9; 6.3 → 7.1; 7.0 → 7.1; 8.1 → 7.1; 10.2 → 14.3; 15.6 → 7.1
- c6__otc_chain100__R1, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.3 → 7.1; 3.6 → 0.0; 3.9 → 0.0; 4.3 → 21.4; 4.7 → 0.0; 5.3 → 7.1; 6.0 → 7.7; 6.9 → 0.0; 8.7 → 7.7; 12.0 → 0.0
- c6__otc_chain100__R1, issuer_1_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0
- c6__otc_chain100__R1, issuer_2 [share 20%, all records]: 5.0 → 0.0; 5.1 → 0.0; 6.0 → 0.0; 6.1 → 0.0; 6.1 → 0.0; 7.1 → 0.0; 8.6 → 0.0; 10.5 → 0.0; 13.4 → 0.0; 17.0 → 0.0
- c6__otc_chain100__R1, issuer_2 [share 20%, other issuers' devices]: 5.0 → 0.0; 5.1 → 0.0; 6.0 → 0.0; 6.1 → 0.0; 6.1 → 0.0; 7.1 → 0.0; 8.6 → 0.0; 10.5 → 0.0; 13.4 → 0.0; 17.0 → 0.0
- c6__otc_chain100__R1, issuer_2_with_observer [share 20%, all records]: 4.2 → 4.7; 4.7 → 2.4; 5.0 → 2.4; 5.2 → 4.8; 5.5 → 2.4; 5.9 → 7.1; 6.3 → 0.0; 7.0 → 7.1; 8.3 → 0.0; 12.6 → 0.0
- c6__otc_chain100__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.2 → 4.7; 4.7 → 2.4; 5.0 → 2.4; 5.2 → 4.8; 5.5 → 2.4; 5.9 → 7.1; 6.3 → 0.0; 7.0 → 7.1; 8.3 → 0.0; 12.6 → 0.0
- c6__otc_chain100__R1, issuer_2_with_first_relay [share 20%, all records]: 4.2 → 4.7; 4.7 → 2.4; 5.0 → 7.1; 5.2 → 2.4; 5.5 → 7.1; 5.9 → 2.4; 6.4 → 0.0; 7.0 → 4.8; 8.2 → 0.0; 12.6 → 0.0
- c6__otc_chain100__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.2 → 4.7; 4.7 → 2.4; 5.0 → 7.1; 5.2 → 2.4; 5.5 → 7.1; 5.9 → 2.4; 6.4 → 0.0; 7.0 → 4.8; 8.2 → 0.0; 12.6 → 0.0
- c6__otc_chain100__R100, observer: 2.2 → 0.0; 2.4 → 3.3; 2.6 → 1.6; 2.7 → 1.6; 2.8 → 0.8; 2.9 → 0.8; 3.1 → 5.7; 3.3 → 4.1; 3.5 → 4.1; 4.1 → 2.5
- c6__otc_chain100__R100, first_hop: 2.2 → 0.1; 2.5 → 2.8; 2.6 → 2.2; 2.7 → 1.6; 2.8 → 1.5; 2.9 → 1.6; 3.1 → 5.6; 3.3 → 3.3; 3.5 → 4.2; 4.2 → 2.9
- c6__otc_chain100__R100, destination: 2.4 → 2.4; 2.7 → 4.9; 2.8 → 4.9; 2.9 → 4.1; 3.1 → 0.8; 3.2 → 2.5; 3.4 → 4.1; 3.5 → 3.3; 3.8 → 3.3; 4.5 → 5.7
- c6__otc_chain100__R100, destination_keyed: 0.0 → 0.0; 0.0 → 0.0; 0.2 → 0.0; 2.7 → 4.1; 3.2 → 4.9; 3.9 → 3.3; 50.9 → 4.9; 88.9 → 1.6; 100.0 → 2.5; 100.0 → 2.5
- c6__otc_chain100__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_chain100__R100, issuer_0 [share 50%, all records]: 2.0 → 0.0; 3.0 → 3.3; 3.1 → 1.6; 3.4 → 0.0; 4.0 → 2.5; 4.4 → 1.6; 4.7 → 0.8; 5.0 → 3.3; 5.3 → 0.8; 5.6 → 1.6
- c6__otc_chain100__R100, issuer_0 [share 50%, its own devices]: 2.0 → 0.0; 3.3 → 0.0; 4.3 → 6.4; 4.6 → 4.3; 4.8 → 2.1; 5.3 → 4.3; 6.2 → 6.5; 7.7 → 2.2; 8.6 → 4.3; 10.1 → 4.3
- c6__otc_chain100__R100, issuer_0 [share 50%, other issuers' devices]: 1.7 → 1.3; 1.7 → 1.3; 1.7 → 1.3; 1.8 → 0.0; 1.8 → 0.0; 1.9 → 0.0; 2.3 → 0.0; 2.5 → 0.0; 2.7 → 0.0; 2.8 → 0.0
- c6__otc_chain100__R100, issuer_0_with_observer [share 50%, all records]: 2.5 → 1.6; 2.8 → 3.3; 3.0 → 3.3; 3.1 → 7.3; 3.4 → 4.1; 3.7 → 2.5; 4.1 → 4.9; 4.6 → 1.6; 5.5 → 3.3; 7.2 → 0.8
- c6__otc_chain100__R100, issuer_0_with_observer [share 50%, its own devices]: 2.5 → 4.3; 2.7 → 6.4; 2.9 → 2.1; 3.1 → 10.6; 3.4 → 4.3; 3.7 → 8.5; 4.1 → 10.9; 4.7 → 4.3; 5.5 → 6.5; 7.3 → 2.2
- c6__otc_chain100__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.5 → 0.0; 2.8 → 1.3; 3.0 → 3.9; 3.2 → 5.3; 3.4 → 2.6; 3.7 → 0.0; 4.1 → 1.3; 4.6 → 0.0; 5.5 → 1.3; 7.2 → 0.0
- c6__otc_chain100__R100, issuer_0_with_first_relay [share 50%, all records]: 2.5 → 0.8; 2.8 → 2.4; 3.0 → 4.1; 3.2 → 6.5; 3.4 → 4.1; 3.7 → 2.5; 4.1 → 4.1; 4.6 → 2.5; 5.5 → 3.3; 7.4 → 0.8
- c6__otc_chain100__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.5 → 0.0; 2.8 → 4.3; 3.0 → 4.3; 3.1 → 8.5; 3.4 → 6.4; 3.7 → 6.4; 4.1 → 10.9; 4.6 → 4.3; 5.5 → 6.5; 7.4 → 2.2
- c6__otc_chain100__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.5 → 1.3; 2.8 → 1.3; 3.0 → 3.9; 3.2 → 5.3; 3.4 → 2.6; 3.8 → 0.0; 4.1 → 1.3; 4.5 → 0.0; 5.5 → 1.3; 7.3 → 0.0
- c6__otc_chain100__R100, issuer_0_with_destination: 0.0 → 0.0; 0.0 → 0.0; 9.9 → 0.0; 53.4 → 4.3; 67.7 → 4.3; 89.4 → 6.4; 100.0 → 0.0; 100.0 → 6.5; 100.0 → 0.0; 100.0 → 2.2
- c6__otc_chain100__R100, issuer_1 [share 30%, all records]: 2.9 → 0.8; 3.5 → 0.0; 3.8 → 0.0; 4.3 → 0.8; 5.0 → 1.6; 5.5 → 0.0; 6.2 → 0.0; 6.7 → 0.8; 7.0 → 1.6; 7.4 → 1.6
- c6__otc_chain100__R100, issuer_1 [share 30%, its own devices]: 3.1 → 4.8; 4.3 → 0.0; 5.0 → 0.0; 6.1 → 5.0; 7.6 → 0.0; 8.8 → 10.0; 10.5 → 0.0; 11.9 → 5.0; 12.8 → 10.0; 13.8 → 10.0
- c6__otc_chain100__R100, issuer_1 [share 30%, other issuers' devices]: 2.4 → 0.0; 2.4 → 0.0; 2.5 → 0.0; 2.6 → 0.0; 2.6 → 0.0; 2.7 → 0.0; 2.9 → 0.0; 3.2 → 0.0; 3.5 → 0.0; 3.6 → 0.0
- c6__otc_chain100__R100, issuer_1_with_observer [share 30%, all records]: 2.4 → 0.0; 2.7 → 2.4; 2.8 → 1.6; 3.2 → 0.8; 3.4 → 1.6; 3.7 → 3.3; 4.1 → 0.8; 4.5 → 2.5; 5.4 → 2.5; 7.1 → 1.6
- c6__otc_chain100__R100, issuer_1_with_observer [share 30%, its own devices]: 2.4 → 0.0; 2.7 → 4.8; 2.9 → 5.0; 3.2 → 0.0; 3.5 → 5.0; 3.8 → 10.0; 4.2 → 5.0; 4.6 → 5.0; 5.4 → 10.0; 7.1 → 5.0
- c6__otc_chain100__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.4 → 0.0; 2.7 → 1.9; 2.8 → 1.0; 3.2 → 1.0; 3.4 → 1.0; 3.7 → 2.0; 4.0 → 1.0; 4.5 → 1.0; 5.4 → 1.0; 7.1 → 1.0
- c6__otc_chain100__R100, issuer_1_with_first_relay [share 30%, all records]: 2.4 → 1.6; 2.7 → 0.8; 3.0 → 2.4; 3.2 → 1.6; 3.4 → 1.6; 3.7 → 3.3; 4.1 → 0.8; 4.5 → 2.5; 5.4 → 2.5; 7.1 → 1.6
- c6__otc_chain100__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.4 → 4.8; 2.8 → 4.8; 3.0 → 5.0; 3.2 → 5.0; 3.4 → 5.0; 3.8 → 10.0; 4.2 → 5.0; 4.7 → 5.0; 5.4 → 10.0; 7.1 → 5.0
- c6__otc_chain100__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.4 → 1.0; 2.7 → 1.0; 3.0 → 1.0; 3.2 → 1.0; 3.4 → 1.0; 3.6 → 2.0; 4.0 → 1.0; 4.5 → 1.0; 5.4 → 1.0; 7.1 → 1.0
- c6__otc_chain100__R100, issuer_1_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 64.0 → 0.0; 87.8 → 0.0; 100.0 → 10.0; 100.0 → 0.0
- c6__otc_chain100__R100, issuer_2 [share 20%, all records]: 3.0 → 0.0; 3.3 → 0.0; 4.4 → 0.0; 6.2 → 1.6; 7.4 → 0.0; 9.2 → 0.8; 11.5 → 0.0; 15.1 → 3.3; 17.4 → 2.5; 19.9 → 2.5
- c6__otc_chain100__R100, issuer_2 [share 20%, its own devices]: 3.0 → 0.0; 3.2 → 0.0; 4.8 → 0.0; 6.3 → 5.9; 8.1 → 0.0; 10.1 → 0.0; 13.4 → 0.0; 15.3 → 23.5; 17.6 → 18.8; 20.0 → 18.8
- c6__otc_chain100__R100, issuer_2 [share 20%, other issuers' devices]: 3.0 → 0.0; 3.1 → 0.0; 3.2 → 0.9; 3.3 → 0.9; 3.5 → 0.0; 3.8 → 0.0; 3.9 → 0.0; 4.0 → 0.0; 4.1 → 0.0; 4.2 → 0.0
- c6__otc_chain100__R100, issuer_2_with_observer [share 20%, all records]: 2.3 → 1.6; 2.6 → 1.6; 2.8 → 1.6; 2.9 → 0.8; 3.1 → 5.7; 3.3 → 4.1; 3.6 → 3.3; 4.0 → 4.1; 4.8 → 4.1; 6.6 → 3.3
- c6__otc_chain100__R100, issuer_2_with_observer [share 20%, its own devices]: 2.4 → 0.0; 2.7 → 0.0; 2.8 → 0.0; 3.0 → 5.9; 3.2 → 5.9; 3.5 → 0.0; 3.7 → 0.0; 4.2 → 11.8; 5.3 → 37.5; 6.6 → 18.8
- c6__otc_chain100__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.3 → 1.9; 2.6 → 1.9; 2.7 → 1.9; 2.9 → 0.9; 3.1 → 4.7; 3.3 → 4.7; 3.5 → 3.8; 4.0 → 2.9; 4.8 → 0.0; 6.6 → 0.0
- c6__otc_chain100__R100, issuer_2_with_first_relay [share 20%, all records]: 2.3 → 0.8; 2.6 → 2.4; 2.8 → 1.6; 2.9 → 0.8; 3.1 → 6.6; 3.3 → 3.3; 3.6 → 3.3; 4.1 → 3.3; 4.8 → 3.3; 6.6 → 4.1
- c6__otc_chain100__R100, issuer_2_with_first_relay [share 20%, its own devices]: 1.8 → 0.0; 1.9 → 0.0; 2.0 → 0.0; 2.2 → 0.0; 2.3 → 5.9; 2.5 → 5.9; 3.0 → 11.8; 3.4 → 11.8; 4.1 → 12.5; 6.1 → 25.0
- c6__otc_chain100__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.3 → 0.9; 2.6 → 2.8; 2.8 → 1.9; 2.9 → 0.9; 3.1 → 5.7; 3.3 → 3.8; 3.5 → 3.8; 4.0 → 2.9; 4.8 → 0.0; 6.6 → 0.0
- c6__otc_chain100__R100, issuer_2_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 62.0 → 0.0; 100.0 → 0.0; 100.0 → 0.0; 100.0 → 0.0
- c6__otc_chain50__R1, observer: 3.6 → 2.3; 4.0 → 11.9; 4.2 → 0.0; 4.4 → 7.1; 4.6 → 2.4; 4.8 → 2.4; 5.0 → 2.4; 5.3 → 7.1; 5.7 → 0.0; 7.0 → 9.5
- c6__otc_chain50__R1, first_hop: 3.6 → 2.9; 4.0 → 10.1; 4.2 → 1.1; 4.4 → 6.2; 4.6 → 3.1; 4.8 → 3.0; 5.0 → 3.0; 5.3 → 6.7; 5.7 → 0.6; 7.0 → 9.3
- c6__otc_chain50__R1, destination: 3.0 → 7.0; 3.3 → 4.8; 3.6 → 7.1; 3.7 → 4.8; 4.0 → 0.0; 4.3 → 2.4; 4.6 → 4.8; 4.9 → 2.4; 5.5 → 2.4; 6.7 → 4.8
- c6__otc_chain50__R1, destination_keyed: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.6 → 2.4; 3.1 → 2.4; 3.4 → 4.8; 4.1 → 0.0
- c6__otc_chain50__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_chain50__R1, issuer_0 [share 50%, all records]: 2.2 → 0.0; 2.6 → 0.0; 3.1 → 0.0; 3.7 → 0.0; 4.2 → 0.0; 5.1 → 0.0; 6.2 → 0.0; 7.2 → 0.0; 7.9 → 0.0; 8.6 → 0.0
- c6__otc_chain50__R1, issuer_0 [share 50%, other issuers' devices]: 2.2 → 0.0; 2.6 → 0.0; 3.1 → 0.0; 3.7 → 0.0; 4.2 → 0.0; 5.1 → 0.0; 6.2 → 0.0; 7.2 → 0.0; 7.9 → 0.0; 8.6 → 0.0
- c6__otc_chain50__R1, issuer_0_with_observer [share 50%, all records]: 2.9 → 7.0; 3.2 → 2.4; 3.6 → 2.4; 3.9 → 7.1; 4.3 → 4.8; 4.8 → 0.0; 5.3 → 0.0; 6.2 → 0.0; 7.9 → 0.0; 11.9 → 0.0
- c6__otc_chain50__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 2.9 → 7.0; 3.2 → 2.4; 3.6 → 2.4; 3.9 → 7.1; 4.3 → 4.8; 4.8 → 0.0; 5.3 → 0.0; 6.2 → 0.0; 7.9 → 0.0; 11.9 → 0.0
- c6__otc_chain50__R1, issuer_0_with_first_relay [share 50%, all records]: 2.9 → 7.0; 3.3 → 2.4; 3.5 → 2.4; 3.9 → 7.1; 4.4 → 4.8; 4.9 → 0.0; 5.4 → 0.0; 6.3 → 0.0; 7.8 → 0.0; 11.9 → 0.0
- c6__otc_chain50__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.9 → 7.0; 3.3 → 2.4; 3.5 → 2.4; 3.9 → 7.1; 4.4 → 4.8; 4.9 → 0.0; 5.4 → 0.0; 6.3 → 0.0; 7.8 → 0.0; 11.9 → 0.0
- c6__otc_chain50__R1, issuer_1 [share 30%, all records]: 3.4 → 2.3; 3.4 → 0.0; 3.6 → 0.0; 3.6 → 0.0; 3.9 → 7.1; 4.1 → 4.8; 5.7 → 4.8; 9.9 → 4.8; 17.5 → 4.8; 24.7 → 2.4
- c6__otc_chain50__R1, issuer_1 [share 30%, its own devices]: 3.4 → 0.0; 3.4 → 3.4; 3.6 → 0.0; 3.9 → 0.0; 4.9 → 10.3; 5.5 → 7.1; 6.5 → 7.1; 10.5 → 7.1; 17.4 → 7.1; 24.7 → 3.6
- c6__otc_chain50__R1, issuer_1 [share 30%, other issuers' devices]: 3.3 → 0.0; 3.4 → 0.0; 3.4 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 4.2 → 0.0; 5.0 → 0.0; 6.6 → 0.0; 7.6 → 0.0
- c6__otc_chain50__R1, issuer_1_with_observer [share 30%, all records]: 3.7 → 2.3; 4.2 → 2.4; 4.5 → 2.4; 4.8 → 4.8; 5.1 → 7.1; 5.6 → 4.8; 6.2 → 7.1; 7.5 → 2.4; 9.3 → 2.4; 14.6 → 11.9
- c6__otc_chain50__R1, issuer_1_with_observer [share 30%, its own devices]: 3.8 → 3.4; 4.2 → 3.4; 4.5 → 0.0; 4.8 → 3.4; 5.1 → 6.9; 5.6 → 14.3; 6.2 → 3.6; 7.7 → 3.6; 9.5 → 7.1; 14.6 → 14.3
- c6__otc_chain50__R1, issuer_1_with_observer [share 30%, other issuers' devices]: 2.6 → 0.0; 2.9 → 0.0; 3.1 → 14.3; 3.2 → 0.0; 3.4 → 7.1; 3.5 → 0.0; 3.8 → 0.0; 4.3 → 0.0; 4.9 → 0.0; 6.9 → 0.0
- c6__otc_chain50__R1, issuer_1_with_first_relay [share 30%, all records]: 3.7 → 7.0; 4.2 → 2.4; 4.6 → 2.4; 4.8 → 4.8; 5.1 → 7.1; 5.6 → 9.5; 6.2 → 4.8; 7.5 → 2.4; 9.3 → 2.4; 14.7 → 11.9
- c6__otc_chain50__R1, issuer_1_with_first_relay [share 30%, its own devices]: 3.8 → 6.9; 4.3 → 3.4; 4.6 → 0.0; 4.8 → 6.9; 5.2 → 6.9; 5.7 → 10.7; 6.2 → 7.1; 7.6 → 3.6; 9.5 → 7.1; 14.6 → 14.3
- c6__otc_chain50__R1, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.6 → 7.1; 2.9 → 0.0; 3.1 → 14.3; 3.2 → 0.0; 3.4 → 7.1; 3.6 → 0.0; 3.8 → 0.0; 4.3 → 0.0; 4.9 → 0.0; 6.9 → 0.0
- c6__otc_chain50__R1, issuer_1_with_destination: 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0; 0.0 → 0.0
- c6__otc_chain50__R1, issuer_2 [share 20%, all records]: 5.1 → 0.0; 5.1 → 0.0; 6.0 → 0.0; 6.1 → 0.0; 6.1 → 0.0; 7.2 → 0.0; 8.4 → 0.0; 10.5 → 0.0; 13.5 → 0.0; 17.0 → 0.0
- c6__otc_chain50__R1, issuer_2 [share 20%, other issuers' devices]: 5.1 → 0.0; 5.1 → 0.0; 6.0 → 0.0; 6.1 → 0.0; 6.1 → 0.0; 7.2 → 0.0; 8.4 → 0.0; 10.5 → 0.0; 13.5 → 0.0; 17.0 → 0.0
- c6__otc_chain50__R1, issuer_2_with_observer [share 20%, all records]: 2.8 → 7.0; 3.1 → 9.5; 3.3 → 4.8; 3.6 → 0.0; 4.0 → 9.5; 4.4 → 2.4; 4.8 → 0.0; 5.2 → 4.8; 6.3 → 0.0; 9.8 → 0.0
- c6__otc_chain50__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 2.8 → 7.0; 3.1 → 9.5; 3.3 → 4.8; 3.6 → 0.0; 4.0 → 9.5; 4.4 → 2.4; 4.8 → 0.0; 5.2 → 4.8; 6.3 → 0.0; 9.8 → 0.0
- c6__otc_chain50__R1, issuer_2_with_first_relay [share 20%, all records]: 2.8 → 9.3; 3.1 → 9.5; 3.3 → 4.8; 3.6 → 2.4; 4.0 → 7.1; 4.4 → 2.4; 4.8 → 0.0; 5.3 → 4.8; 6.4 → 0.0; 9.8 → 0.0
- c6__otc_chain50__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.8 → 9.3; 3.1 → 9.5; 3.3 → 4.8; 3.6 → 2.4; 4.0 → 7.1; 4.4 → 2.4; 4.8 → 0.0; 5.3 → 4.8; 6.4 → 0.0; 9.8 → 0.0
- c6__otc_chain50__R100, observer: 2.1 → 1.6; 2.2 → 2.4; 2.4 → 2.4; 2.5 → 1.6; 2.6 → 1.6; 2.7 → 3.3; 2.8 → 0.8; 3.0 → 3.3; 3.2 → 2.5; 3.8 → 4.1
- c6__otc_chain50__R100, first_hop: 2.1 → 2.0; 2.2 → 1.8; 2.4 → 1.8; 2.5 → 1.0; 2.6 → 2.4; 2.7 → 3.0; 2.8 → 2.1; 3.0 → 2.7; 3.2 → 2.5; 3.9 → 4.1
- c6__otc_chain50__R100, destination: 1.6 → 4.1; 1.7 → 4.9; 1.7 → 2.4; 1.8 → 4.1; 1.8 → 3.3; 1.9 → 1.6; 2.0 → 3.3; 2.1 → 4.9; 2.2 → 1.6; 2.4 → 4.1
- c6__otc_chain50__R100, destination_keyed: 1.6 → 0.8; 1.8 → 2.4; 2.1 → 0.8; 12.2 → 3.3; 19.2 → 3.3; 23.5 → 5.7; 27.6 → 3.3; 32.4 → 6.6; 40.8 → 4.9; 69.9 → 6.6
- c6__otc_chain50__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_chain50__R100, issuer_0 [share 50%, all records]: 2.0 → 0.0; 3.0 → 2.4; 3.1 → 2.4; 3.3 → 0.0; 3.9 → 1.6; 4.3 → 1.6; 4.7 → 1.6; 5.0 → 3.3; 5.2 → 0.8; 5.6 → 1.6
- c6__otc_chain50__R100, issuer_0 [share 50%, its own devices]: 2.0 → 0.0; 3.3 → 0.0; 4.3 → 6.4; 4.6 → 4.3; 4.8 → 2.1; 5.3 → 4.3; 6.2 → 6.5; 7.7 → 2.2; 8.6 → 4.3; 10.1 → 4.3
- c6__otc_chain50__R100, issuer_0 [share 50%, other issuers' devices]: 1.8 → 0.0; 1.9 → 2.6; 1.9 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.6 → 0.0; 3.1 → 1.3; 3.5 → 0.0; 3.6 → 0.0
- c6__otc_chain50__R100, issuer_0_with_observer [share 50%, all records]: 2.1 → 4.1; 2.5 → 0.8; 2.7 → 4.1; 2.9 → 1.6; 3.2 → 4.9; 3.5 → 4.1; 3.8 → 2.5; 4.3 → 2.5; 5.1 → 4.1; 6.3 → 0.0
- c6__otc_chain50__R100, issuer_0_with_observer [share 50%, its own devices]: 2.1 → 2.1; 2.5 → 0.0; 2.7 → 6.4; 2.9 → 6.4; 3.2 → 8.5; 3.5 → 8.5; 3.8 → 8.7; 4.4 → 4.3; 5.1 → 10.9; 6.2 → 0.0
- c6__otc_chain50__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 1.7 → 1.3; 1.9 → 1.3; 2.0 → 1.3; 2.2 → 2.6; 2.3 → 0.0; 2.6 → 2.6; 2.8 → 0.0; 3.2 → 2.7; 4.0 → 0.0; 5.6 → 0.0
- c6__otc_chain50__R100, issuer_0_with_first_relay [share 50%, all records]: 2.1 → 3.3; 2.5 → 0.8; 2.7 → 2.4; 2.9 → 1.6; 3.2 → 4.9; 3.5 → 4.1; 3.9 → 3.3; 4.3 → 1.6; 5.1 → 4.1; 6.5 → 0.0
- c6__otc_chain50__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.1 → 2.1; 2.5 → 2.1; 2.7 → 4.3; 2.9 → 4.3; 3.2 → 8.5; 3.5 → 10.6; 3.9 → 8.7; 4.3 → 2.2; 5.0 → 10.9; 6.3 → 0.0
- c6__otc_chain50__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 1.6 → 1.3; 1.9 → 1.3; 2.1 → 1.3; 2.2 → 1.3; 2.3 → 1.3; 2.6 → 0.0; 2.9 → 0.0; 3.3 → 2.7; 4.0 → 0.0; 5.5 → 0.0
- c6__otc_chain50__R100, issuer_0_with_destination: 20.5 → 2.1; 23.9 → 4.3; 26.5 → 2.1; 28.7 → 6.4; 30.8 → 0.0; 33.6 → 6.4; 37.3 → 2.2; 41.9 → 8.7; 49.8 → 8.7; 71.0 → 4.3
- c6__otc_chain50__R100, issuer_1 [share 30%, all records]: 3.3 → 0.8; 4.3 → 0.8; 4.9 → 0.0; 6.1 → 0.8; 7.4 → 0.0; 8.8 → 1.6; 10.3 → 0.0; 11.8 → 0.8; 12.6 → 1.6; 13.8 → 1.6
- c6__otc_chain50__R100, issuer_1 [share 30%, its own devices]: 3.1 → 4.8; 4.3 → 0.0; 5.0 → 0.0; 6.1 → 5.0; 7.6 → 0.0; 8.8 → 10.0; 10.5 → 0.0; 11.9 → 5.0; 12.8 → 10.0; 13.8 → 10.0
- c6__otc_chain50__R100, issuer_1 [share 30%, other issuers' devices]: 2.4 → 1.0; 2.4 → 0.0; 2.5 → 0.0; 2.5 → 0.0; 2.6 → 0.0; 4.1 → 0.0; 5.3 → 0.0; 8.0 → 0.0; 10.9 → 0.0; 13.2 → 0.0
- c6__otc_chain50__R100, issuer_1_with_observer [share 30%, all records]: 2.2 → 1.6; 2.5 → 2.4; 2.6 → 3.3; 2.8 → 2.5; 3.1 → 2.5; 3.4 → 1.6; 3.8 → 3.3; 4.2 → 3.3; 4.9 → 2.5; 6.4 → 0.0
- c6__otc_chain50__R100, issuer_1_with_observer [share 30%, its own devices]: 2.2 → 0.0; 2.5 → 4.8; 2.6 → 5.0; 2.9 → 5.0; 3.3 → 5.0; 3.6 → 0.0; 3.9 → 15.0; 4.3 → 5.0; 5.0 → 15.0; 6.3 → 0.0
- c6__otc_chain50__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.2 → 2.9; 2.5 → 2.0; 2.6 → 1.0; 2.8 → 2.9; 3.1 → 2.0; 3.4 → 1.0; 3.7 → 2.0; 4.2 → 2.9; 4.9 → 0.0; 6.4 → 0.0
- c6__otc_chain50__R100, issuer_1_with_first_relay [share 30%, all records]: 2.2 → 1.6; 2.5 → 1.6; 2.6 → 3.3; 2.9 → 2.5; 3.2 → 3.3; 3.4 → 0.0; 3.7 → 4.9; 4.2 → 3.3; 5.0 → 2.5; 6.4 → 0.0
- c6__otc_chain50__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.2 → 0.0; 2.5 → 0.0; 2.7 → 0.0; 3.0 → 10.0; 3.3 → 5.0; 3.5 → 0.0; 3.9 → 15.0; 4.3 → 5.0; 5.0 → 15.0; 6.3 → 0.0
- c6__otc_chain50__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 1.6 → 3.9; 1.8 → 3.9; 2.1 → 2.0; 2.2 → 2.0; 2.4 → 2.0; 2.7 → 1.0; 2.9 → 1.0; 3.2 → 2.0; 3.8 → 0.0; 5.4 → 0.0
- c6__otc_chain50__R100, issuer_1_with_destination: 23.6 → 9.5; 29.5 → 0.0; 34.0 → 0.0; 38.6 → 0.0; 42.8 → 0.0; 45.4 → 0.0; 49.2 → 5.0; 53.3 → 0.0; 60.7 → 0.0; 73.9 → 0.0
- c6__otc_chain50__R100, issuer_2 [share 20%, all records]: 3.0 → 0.0; 3.3 → 0.0; 4.8 → 0.0; 7.1 → 0.0; 8.6 → 1.6; 10.5 → 0.0; 14.1 → 2.5; 17.9 → 1.6; 20.6 → 2.5; 33.1 → 2.5
- c6__otc_chain50__R100, issuer_2 [share 20%, its own devices]: 3.0 → 0.0; 3.2 → 0.0; 4.8 → 0.0; 6.3 → 5.9; 8.1 → 0.0; 10.1 → 0.0; 13.4 → 0.0; 15.3 → 23.5; 17.6 → 18.8; 20.0 → 18.8
- c6__otc_chain50__R100, issuer_2 [share 20%, other issuers' devices]: 3.0 → 0.0; 3.2 → 0.0; 3.8 → 0.0; 3.9 → 0.0; 3.9 → 0.0; 4.1 → 0.0; 4.1 → 1.0; 4.5 → 1.0; 6.0 → 0.0; 8.8 → 0.0
- c6__otc_chain50__R100, issuer_2_with_observer [share 20%, all records]: 2.2 → 2.4; 2.4 → 3.3; 2.6 → 0.8; 2.7 → 2.5; 2.8 → 1.6; 3.0 → 2.5; 3.3 → 2.5; 3.9 → 4.1; 4.8 → 5.7; 6.6 → 4.1
- c6__otc_chain50__R100, issuer_2_with_observer [share 20%, its own devices]: 2.2 → 0.0; 2.5 → 0.0; 2.6 → 0.0; 2.7 → 0.0; 2.9 → 5.9; 3.1 → 0.0; 3.5 → 5.9; 4.1 → 11.8; 5.2 → 37.5; 6.4 → 18.8
- c6__otc_chain50__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.2 → 2.8; 2.4 → 3.8; 2.6 → 0.9; 2.6 → 2.8; 2.8 → 1.9; 3.0 → 1.9; 3.3 → 1.9; 3.8 → 3.8; 4.8 → 1.0; 6.6 → 1.0
- c6__otc_chain50__R100, issuer_2_with_first_relay [share 20%, all records]: 2.1 → 1.6; 2.4 → 0.8; 2.6 → 0.8; 2.6 → 2.5; 2.8 → 4.1; 3.1 → 2.5; 3.4 → 3.3; 3.9 → 2.5; 4.8 → 4.9; 6.6 → 4.1
- c6__otc_chain50__R100, issuer_2_with_first_relay [share 20%, its own devices]: 2.2 → 0.0; 2.5 → 0.0; 2.6 → 0.0; 2.7 → 0.0; 2.9 → 5.9; 3.2 → 0.0; 3.5 → 5.9; 4.1 → 5.9; 5.2 → 37.5; 6.4 → 18.8
- c6__otc_chain50__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.1 → 1.9; 2.4 → 0.9; 2.5 → 0.9; 2.6 → 2.8; 2.8 → 3.8; 3.1 → 2.9; 3.3 → 2.9; 3.8 → 1.9; 4.8 → 1.0; 6.7 → 1.0
- c6__otc_chain50__R100, issuer_2_with_destination: 19.2 → 11.8; 25.2 → 5.9; 29.1 → 23.5; 32.9 → 5.9; 38.4 → 17.6; 47.4 → 5.9; 59.1 → 5.9; 77.4 → 11.8; 99.1 → 12.5; 100.0 → 12.5
- c6__cp_W0__R1, K records, K = 1: 3.3 → 11.9; 3.7 → 2.4; 4.0 → 14.3; 4.4 → 4.9; 4.9 → 7.3; 5.4 → 7.3; 6.0 → 2.4; 6.5 → 4.9; 7.3 → 2.4; 9.2 → 9.8
- c6__cp_W0__R1, K records, K = 2: 6.1 → 4.8; 7.3 → 4.8; 8.1 → 4.8; 9.1 → 14.3; 10.5 → 0.0; 12.2 → 9.5; 13.8 → 5.0; 15.9 → 0.0; 18.8 → 5.0; 26.4 → 5.0
- c6__cp_W0__R1, K records, K = 3: 8.7 → 0.0; 11.8 → 7.1; 13.6 → 7.1; 15.2 → 21.4; 16.8 → 14.3; 18.8 → 7.1; 21.8 → 14.3; 25.5 → 7.7; 36.3 → 0.0; 55.0 → 7.7
- c6__cp_W0__R1, K records, K = 5: 17.3 → 0.0; 23.1 → 12.5; 25.3 → 12.5; 29.1 → 12.5; 32.7 → 0.0; 37.4 → 25.0; 40.9 → 25.0; 44.1 → 12.5; 56.4 → 0.0; 71.0 → 0.0
- c6__cp_W0__R1, K records, K = 10: 29.8 → 0.0; 37.4 → 25.0; 43.5 → 50.0; 50.9 → 75.0; 56.8 → 100.0; 67.3 → 0.0; 78.9 → 50.0; 84.9 → 50.0; 90.9 → 100.0; 96.1 → 75.0
- c6__cp_W0__R1, K records, K = 20: 76.6 → 50.0; 92.4 → 50.0; 96.5 → 100.0; 98.5 → 100.0; 99.4 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_W0__R100, K records, K = 1: 1.9 → 3.3; 2.0 → 3.3; 2.1 → 1.6; 2.2 → 0.8; 2.3 → 0.8; 2.3 → 1.6; 2.4 → 1.7; 2.7 → 1.7; 2.9 → 0.0; 3.4 → 2.5
- c6__cp_W0__R100, K records, K = 2: 3.5 → 1.8; 4.0 → 0.0; 4.4 → 1.8; 4.7 → 3.6; 5.0 → 5.4; 5.4 → 3.6; 5.7 → 7.1; 6.5 → 0.0; 7.6 → 0.0; 10.8 → 3.6
- c6__cp_W0__R100, K records, K = 3: 5.7 → 2.9; 6.8 → 0.0; 7.5 → 2.9; 8.2 → 5.9; 8.8 → 2.9; 9.5 → 3.0; 10.3 → 6.1; 11.7 → 3.0; 14.0 → 0.0; 22.1 → 3.0
- c6__cp_W0__R100, K records, K = 5: 10.4 → 6.2; 13.1 → 6.2; 14.9 → 0.0; 16.0 → 6.2; 17.8 → 0.0; 20.3 → 0.0; 22.5 → 0.0; 24.9 → 0.0; 29.5 → 13.3; 43.3 → 6.7
- c6__cp_W1__R1, K records, K = 1: 3.4 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.0 → 0.0; 4.1 → 0.0; 4.3 → 0.0; 4.4 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.4 → 0.0
- c6__cp_W1__R1, K records, K = 2: 6.5 → 0.0; 7.4 → 0.0; 7.8 → 0.0; 8.2 → 0.0; 8.6 → 0.0; 9.1 → 0.0; 9.6 → 0.0; 10.5 → 0.0; 11.6 → 0.0; 13.7 → 0.0
- c6__cp_W1__R1, K records, K = 3: 9.9 → 0.0; 11.3 → 0.0; 12.4 → 0.0; 13.3 → 0.0; 14.5 → 0.0; 15.3 → 0.0; 16.3 → 0.0; 17.5 → 0.0; 19.8 → 0.0; 24.7 → 0.0
- c6__cp_W1__R1, K records, K = 5: 16.9 → 0.0; 21.2 → 0.0; 23.3 → 0.0; 24.9 → 0.0; 26.3 → 0.0; 29.0 → 0.0; 31.3 → 0.0; 35.3 → 0.0; 38.4 → 0.0; 50.8 → 0.0
- c6__cp_W1__R1, K records, K = 10: 25.2 → 0.0; 31.1 → 0.0; 36.1 → 0.0; 41.4 → 0.0; 48.4 → 0.0; 52.0 → 0.0; 56.4 → 0.0; 69.2 → 0.0; 77.1 → 0.0; 88.7 → 0.0
- c6__cp_W1__R1, K records, K = 20: 40.0 → 0.0; 48.5 → 0.0; 55.2 → 0.0; 60.7 → 0.0; 64.0 → 0.0; 64.5 → 0.0; 79.1 → 0.0; 84.9 → 0.0; 88.9 → 0.0; 97.7 → 0.0
- c6__cp_W1__R100, K records, K = 1: 3.3 → 2.3; 3.7 → 4.5; 4.0 → 3.8; 4.4 → 6.1; 5.0 → 5.3; 5.4 → 6.1; 5.9 → 6.1; 6.5 → 10.7; 7.0 → 13.0; 7.7 → 11.5
- c6__cp_W1__R100, K records, K = 2: 8.8 → 4.9; 10.4 → 4.9; 12.3 → 4.9; 14.7 → 4.9; 17.2 → 8.2; 19.5 → 11.7; 21.9 → 6.7; 24.8 → 16.7; 28.1 → 3.3; 32.2 → 8.3
- c6__cp_W1__R100, K records, K = 3: 15.4 → 2.6; 20.3 → 2.6; 24.7 → 2.6; 30.1 → 5.3; 34.8 → 13.2; 39.9 → 13.2; 44.6 → 15.8; 48.2 → 2.6; 54.6 → 2.6; 60.9 → 10.5
- c6__cp_W1__R100, K records, K = 5: 25.2 → 5.3; 37.4 → 5.3; 45.8 → 0.0; 53.3 → 5.3; 61.4 → 26.3; 67.3 → 11.1; 72.2 → 16.7; 77.3 → 0.0; 83.4 → 5.6; 89.7 → 11.1
- c6__cp_W1__R100, K records, K = 10: 42.8 → 0.0; 67.0 → 0.0; 74.4 → 16.7; 81.7 → 16.7; 89.5 → 0.0; 91.6 → 33.3; 94.4 → 0.0; 97.4 → 20.0; 98.8 → 20.0; 99.6 → 20.0
- c6__cp_W1__R100, K records, K = 20: 66.4 → 50.0; 90.1 → 0.0; 96.8 → 50.0; 97.9 → 50.0; 99.0 → 0.0; 99.3 → 0.0; 99.6 → 0.0; 99.8 → 0.0; 99.8 → 100.0; 100.0 → 0.0
- c6__cp_W2__R1, K records, K = 1: 3.8 → 5.4; 4.3 → 16.2; 4.9 → 8.1; 5.5 → 18.9; 6.1 → 21.6; 6.9 → 2.7; 7.6 → 0.0; 8.8 → 8.3; 10.8 → 0.0; 19.4 → 0.0
- c6__cp_W2__R1, K records, K = 2: 7.1 → 5.3; 8.8 → 10.5; 10.7 → 15.8; 13.0 → 16.7; 15.5 → 16.7; 17.6 → 5.6; 20.6 → 5.6; 25.0 → 5.6; 34.6 → 0.0; 59.1 → 0.0
- c6__cp_W2__R1, K records, K = 3: 11.3 → 0.0; 14.2 → 15.4; 17.1 → 0.0; 20.4 → 25.0; 24.7 → 8.3; 29.3 → 16.7; 33.5 → 16.7; 42.6 → 0.0; 52.9 → 0.0; 81.1 → 0.0
- c6__cp_W2__R1, K records, K = 5: 20.1 → 12.5; 25.3 → 12.5; 29.9 → 0.0; 33.4 → 0.0; 40.1 → 14.3; 47.0 → 0.0; 54.0 → 0.0; 65.7 → 28.6; 79.2 → 0.0; 97.1 → 0.0
- c6__cp_W2__R1, K records, K = 10: 32.3 → 0.0; 40.0 → 0.0; 54.5 → 0.0; 60.0 → 25.0; 67.9 → 0.0; 74.6 → 25.0; 88.5 → 0.0; 94.4 → 0.0; 97.8 → 0.0; 99.3 → 0.0
- c6__cp_W2__R1, K records, K = 20: 54.4 → 0.0; 61.0 → 50.0; 74.9 → 0.0; 84.0 → 0.0; 88.2 → 0.0; 95.1 → 0.0; 98.6 → 0.0; 99.8 → 0.0; 99.8 → 0.0; 100.0 → 0.0
- c6__cp_W2__R100, K records, K = 1: 3.5 → 4.1; 4.0 → 4.1; 4.4 → 1.6; 4.9 → 14.8; 5.4 → 9.0; 5.9 → 6.6; 6.4 → 4.9; 7.3 → 9.8; 8.5 → 10.7; 10.6 → 5.7
- c6__cp_W2__R100, K records, K = 2: 9.4 → 8.9; 11.6 → 3.6; 13.9 → 1.8; 16.0 → 12.5; 17.8 → 12.5; 20.2 → 5.4; 23.4 → 1.8; 27.4 → 7.1; 32.7 → 16.1; 47.8 → 5.5
- c6__cp_W2__R100, K records, K = 3: 16.2 → 8.8; 21.2 → 5.9; 25.5 → 2.9; 31.4 → 2.9; 35.7 → 29.4; 38.7 → 2.9; 44.9 → 2.9; 52.8 → 5.9; 60.5 → 14.7; 78.9 → 11.8
- c6__cp_W2__R100, K records, K = 5: 30.1 → 5.6; 43.6 → 0.0; 52.0 → 11.1; 59.2 → 16.7; 66.7 → 22.2; 76.5 → 5.9; 81.7 → 0.0; 85.0 → 11.8; 90.7 → 17.6; 97.8 → 5.9
- c6__cp_W2__R100, K records, K = 10: 52.6 → 16.7; 69.5 → 16.7; 76.2 → 16.7; 86.9 → 33.3; 94.2 → 33.3; 97.3 → 0.0; 99.0 → 16.7; 99.4 → 0.0; 99.8 → 20.0; 99.9 → 20.0
- c6__cp_W2__R100, K records, K = 20: 72.7 → 50.0; 88.1 → 0.0; 88.5 → 100.0; 98.2 → 0.0; 98.8 → 0.0; 99.7 → 0.0; 100.0 → 0.0; 100.0 → 100.0; 100.0 → 0.0; 100.0 → 100.0
- c6__cp_Wmis__R1, K records, K = 1: 4.8 → 0.0; 5.4 → 8.1; 5.9 → 0.0; 6.3 → 8.1; 6.8 → 8.1; 7.3 → 2.7; 8.0 → 27.8; 9.0 → 25.0; 10.8 → 41.7; 18.5 → 88.9
- c6__cp_Wmis__R1, K records, K = 2: 9.1 → 0.0; 11.6 → 5.3; 13.0 → 10.5; 14.2 → 11.1; 16.1 → 0.0; 17.8 → 11.1; 21.0 → 16.7; 24.8 → 33.3; 33.5 → 44.4; 60.5 → 88.9
- c6__cp_Wmis__R1, K records, K = 3: 14.2 → 0.0; 17.6 → 0.0; 19.9 → 0.0; 21.9 → 0.0; 24.9 → 0.0; 28.3 → 25.0; 33.9 → 25.0; 40.0 → 50.0; 53.7 → 50.0; 84.6 → 100.0
- c6__cp_Wmis__R1, K records, K = 5: 22.8 → 0.0; 31.4 → 0.0; 36.1 → 0.0; 42.5 → 0.0; 47.0 → 28.6; 51.4 → 28.6; 61.4 → 14.3; 76.6 → 14.3; 89.8 → 71.4; 98.4 → 100.0
- c6__cp_Wmis__R1, K records, K = 10: 39.3 → 0.0; 51.0 → 50.0; 66.0 → 25.0; 78.3 → 50.0; 85.7 → 50.0; 92.5 → 75.0; 97.1 → 100.0; 99.7 → 100.0; 99.9 → 100.0; 100.0 → 100.0
- c6__cp_Wmis__R1, K records, K = 20: 80.4 → 100.0; 99.8 → 100.0; 99.9 → 50.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_Wmis__R100, K records, K = 1: 5.3 → 4.9; 6.1 → 7.4; 7.0 → 8.2; 7.8 → 9.8; 8.9 → 6.6; 10.5 → 9.8; 12.0 → 9.8; 14.0 → 12.3; 16.8 → 11.5; 23.8 → 18.0
- c6__cp_Wmis__R100, K records, K = 2: 16.0 → 7.1; 20.9 → 5.4; 24.6 → 12.5; 30.6 → 8.9; 36.1 → 7.1; 42.9 → 7.1; 49.7 → 19.6; 58.5 → 8.9; 68.3 → 10.7; 79.1 → 16.4
- c6__cp_Wmis__R100, K records, K = 3: 27.2 → 11.8; 35.1 → 8.8; 42.1 → 8.8; 51.7 → 11.8; 59.3 → 2.9; 68.9 → 23.5; 79.5 → 8.8; 88.1 → 14.7; 93.0 → 11.8; 97.0 → 14.7
- c6__cp_Wmis__R100, K records, K = 5: 45.0 → 11.1; 59.6 → 11.1; 70.0 → 5.6; 81.7 → 0.0; 89.8 → 16.7; 94.8 → 23.5; 98.3 → 23.5; 99.6 → 17.6; 99.8 → 5.9; 99.9 → 11.8
- c6__cp_chain100__R1, K records, K = 1: 3.4 → 0.0; 3.8 → 9.5; 4.2 → 16.7; 4.5 → 4.8; 4.9 → 4.8; 5.5 → 9.5; 6.0 → 4.8; 6.6 → 16.7; 7.3 → 4.8; 9.1 → 0.0
- c6__cp_chain100__R1, K records, K = 2: 6.3 → 9.5; 7.7 → 0.0; 8.6 → 4.8; 9.6 → 4.8; 10.4 → 9.5; 11.5 → 14.3; 13.2 → 0.0; 15.5 → 9.5; 18.3 → 14.3; 27.6 → 0.0
- c6__cp_chain100__R1, K records, K = 3: 9.2 → 0.0; 11.2 → 14.3; 13.9 → 14.3; 16.1 → 7.1; 18.0 → 14.3; 20.2 → 14.3; 23.6 → 14.3; 26.5 → 0.0; 31.8 → 7.1; 48.3 → 14.3
- c6__cp_chain100__R1, K records, K = 5: 15.9 → 0.0; 21.8 → 33.3; 26.7 → 11.1; 29.7 → 12.5; 33.2 → 25.0; 37.3 → 25.0; 43.3 → 25.0; 52.0 → 12.5; 61.7 → 25.0; 72.9 → 12.5
- c6__cp_chain100__R1, K records, K = 10: 34.2 → 40.0; 45.8 → 25.0; 58.7 → 50.0; 63.6 → 50.0; 68.7 → 25.0; 81.0 → 50.0; 87.5 → 25.0; 91.4 → 25.0; 94.0 → 50.0; 97.4 → 75.0
- c6__cp_chain100__R1, K records, K = 20: 64.9 → 50.0; 94.5 → 100.0; 97.7 → 100.0; 99.0 → 100.0; 99.4 → 50.0; 99.6 → 100.0; 99.7 → 100.0; 99.8 → 50.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_chain100__R100, K records, K = 1: 1.8 → 0.0; 2.0 → 1.6; 2.2 → 1.6; 2.4 → 0.8; 2.7 → 4.9; 3.1 → 1.6; 3.6 → 2.4; 3.9 → 2.4; 4.5 → 2.4; 5.6 → 0.0
- c6__cp_chain100__R100, K records, K = 2: 3.6 → 5.3; 4.4 → 0.0; 5.1 → 3.5; 5.7 → 1.8; 6.5 → 1.8; 7.6 → 1.8; 9.1 → 8.9; 10.6 → 3.6; 12.7 → 3.6; 18.0 → 1.8
- c6__cp_chain100__R100, K records, K = 3: 6.4 → 2.9; 8.0 → 2.9; 9.2 → 2.9; 10.4 → 0.0; 11.7 → 2.9; 13.3 → 0.0; 15.9 → 2.9; 18.8 → 6.1; 23.9 → 6.1; 34.6 → 3.0
- c6__cp_chain100__R100, K records, K = 5: 12.1 → 0.0; 15.8 → 5.9; 18.4 → 5.9; 21.0 → 0.0; 24.4 → 0.0; 28.8 → 11.8; 31.9 → 12.5; 36.4 → 0.0; 42.5 → 12.5; 64.4 → 18.8
- c6__cp_chain50__R1, K records, K = 1: 3.2 → 4.7; 3.6 → 9.5; 3.9 → 0.0; 4.1 → 7.1; 4.6 → 0.0; 5.2 → 16.7; 5.8 → 2.4; 6.5 → 2.4; 7.5 → 2.4; 9.2 → 0.0
- c6__cp_chain50__R1, K records, K = 2: 6.5 → 0.0; 7.8 → 0.0; 8.8 → 9.5; 9.7 → 4.8; 11.0 → 0.0; 12.5 → 0.0; 14.1 → 9.5; 16.6 → 14.3; 21.4 → 0.0; 32.7 → 5.0
- c6__cp_chain50__R1, K records, K = 3: 10.7 → 0.0; 12.9 → 7.1; 14.9 → 14.3; 16.9 → 14.3; 18.2 → 0.0; 20.5 → 0.0; 23.3 → 7.1; 28.3 → 14.3; 38.3 → 7.1; 57.1 → 0.0
- c6__cp_chain50__R1, K records, K = 5: 19.0 → 11.1; 26.2 → 33.3; 30.0 → 11.1; 32.0 → 25.0; 35.6 → 12.5; 40.1 → 25.0; 48.6 → 0.0; 53.4 → 25.0; 65.1 → 12.5; 80.3 → 12.5
- c6__cp_chain50__R1, K records, K = 10: 45.1 → 75.0; 53.1 → 75.0; 63.1 → 25.0; 70.6 → 50.0; 74.8 → 75.0; 79.5 → 100.0; 88.7 → 75.0; 93.3 → 25.0; 96.2 → 100.0; 99.4 → 100.0
- c6__cp_chain50__R1, K records, K = 20: 95.5 → 100.0; 98.3 → 50.0; 99.6 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__cp_chain50__R100, K records, K = 1: 1.7 → 1.6; 1.8 → 0.8; 2.0 → 2.4; 2.1 → 2.4; 2.3 → 5.6; 2.9 → 0.8; 3.3 → 3.2; 3.7 → 1.6; 4.3 → 1.6; 5.9 → 1.6
- c6__cp_chain50__R100, K records, K = 2: 3.9 → 1.9; 4.7 → 1.9; 5.4 → 3.8; 6.0 → 1.9; 6.8 → 3.8; 7.7 → 1.9; 8.9 → 5.8; 10.2 → 3.8; 12.7 → 0.0; 21.3 → 7.7
- c6__cp_chain50__R100, K records, K = 3: 7.1 → 3.3; 8.9 → 3.3; 10.2 → 6.7; 11.6 → 0.0; 13.1 → 6.7; 15.0 → 6.7; 17.1 → 6.7; 20.5 → 0.0; 26.3 → 10.3; 37.4 → 3.4
- c6__cp_chain50__R100, K records, K = 5: 13.1 → 15.4; 17.3 → 8.3; 21.7 → 8.3; 24.0 → 16.7; 28.2 → 16.7; 35.2 → 8.3; 42.9 → 8.3; 48.8 → 8.3; 55.9 → 8.3; 71.7 → 33.3
- c6__otcL_W0__R1, K records, K = 1: 3.9 → 4.8; 4.3 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 5.0 → 2.4; 5.3 → 0.0; 5.5 → 4.9; 5.8 → 0.0; 6.3 → 12.2; 7.1 → 2.4
- c6__otcL_W0__R1, K records, K = 2: 7.7 → 4.8; 8.9 → 4.8; 9.6 → 14.3; 10.3 → 0.0; 11.1 → 23.8; 11.9 → 4.8; 12.8 → 10.0; 14.0 → 20.0; 15.3 → 5.0; 20.8 → 5.0
- c6__otcL_W0__R1, K records, K = 3: 11.5 → 0.0; 13.8 → 7.1; 15.8 → 14.3; 18.3 → 35.7; 20.5 → 7.1; 21.9 → 0.0; 24.1 → 7.1; 28.3 → 23.1; 33.1 → 15.4; 41.2 → 7.7
- c6__otcL_W0__R1, K records, K = 5: 20.4 → 22.2; 27.2 → 12.5; 29.7 → 12.5; 33.3 → 25.0; 35.4 → 12.5; 39.8 → 37.5; 51.8 → 12.5; 60.4 → 25.0; 67.4 → 50.0; 75.6 → 25.0
- c6__otcL_W0__R1, K records, K = 10: 49.9 → 75.0; 57.0 → 50.0; 66.0 → 25.0; 75.7 → 50.0; 87.4 → 75.0; 93.4 → 75.0; 97.6 → 100.0; 98.3 → 50.0; 99.6 → 100.0; 99.9 → 75.0
- c6__otcL_W0__R1, K records, K = 20: 90.9 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_W0__R100, K records, K = 1: 2.3 → 4.9; 2.5 → 2.5; 2.6 → 0.8; 2.7 → 1.6; 2.8 → 3.3; 3.0 → 2.5; 3.2 → 0.8; 3.4 → 4.1; 3.6 → 4.1; 4.2 → 4.1
- c6__otcL_W0__R100, K records, K = 2: 4.6 → 0.0; 5.6 → 1.8; 6.0 → 1.8; 6.5 → 3.6; 7.0 → 7.1; 7.5 → 3.6; 8.1 → 1.8; 8.8 → 1.8; 10.0 → 10.7; 12.4 → 5.5
- c6__otcL_W0__R100, K records, K = 3: 7.8 → 2.9; 9.4 → 20.6; 10.4 → 11.8; 11.4 → 14.7; 12.7 → 8.8; 13.7 → 0.0; 15.2 → 3.0; 16.8 → 3.0; 19.2 → 9.1; 26.6 → 12.1
- c6__otcL_W0__R100, K records, K = 5: 15.8 → 12.5; 20.2 → 25.0; 23.4 → 37.5; 26.2 → 18.8; 28.9 → 43.8; 31.9 → 46.7; 35.5 → 20.0; 39.0 → 40.0; 43.1 → 33.3; 54.8 → 40.0
- c6__otcL_W1__R1, K records, K = 1: 3.0 → 0.0; 3.3 → 5.1; 3.5 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 4.2 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otcL_W1__R1, K records, K = 2: 5.0 → 0.0; 5.7 → 5.0; 6.7 → 5.0; 7.3 → 0.0; 7.9 → 0.0; 8.7 → 0.0; 9.5 → 0.0; 10.3 → 0.0; 11.7 → 0.0; 15.3 → 0.0
- c6__otcL_W1__R1, K records, K = 3: 7.7 → 15.4; 9.0 → 0.0; 10.3 → 0.0; 11.6 → 0.0; 13.2 → 0.0; 14.9 → 0.0; 16.7 → 0.0; 19.2 → 0.0; 22.1 → 0.0; 29.5 → 0.0
- c6__otcL_W1__R1, K records, K = 5: 14.3 → 0.0; 16.7 → 12.5; 18.8 → 0.0; 19.9 → 0.0; 21.6 → 0.0; 24.0 → 0.0; 29.0 → 0.0; 34.9 → 0.0; 41.4 → 0.0; 64.4 → 0.0
- c6__otcL_W1__R1, K records, K = 10: 26.4 → 0.0; 32.9 → 0.0; 38.3 → 0.0; 43.8 → 0.0; 47.0 → 0.0; 54.4 → 0.0; 61.1 → 0.0; 66.1 → 0.0; 73.2 → 0.0; 83.1 → 0.0
- c6__otcL_W1__R1, K records, K = 20: 24.3 → 0.0; 38.0 → 0.0; 47.7 → 0.0; 52.2 → 0.0; 60.0 → 0.0; 68.7 → 0.0; 79.0 → 0.0; 85.9 → 0.0; 87.5 → 0.0; 89.6 → 0.0
- c6__otcL_W1__R100, K records, K = 1: 3.5 → 2.3; 4.2 → 3.8; 4.7 → 4.6; 5.2 → 4.6; 5.7 → 4.6; 6.0 → 5.3; 6.4 → 6.9; 6.8 → 7.6; 7.4 → 4.6; 9.0 → 16.8
- c6__otcL_W1__R100, K records, K = 2: 9.2 → 4.9; 12.7 → 3.3; 14.6 → 6.6; 16.7 → 6.6; 18.6 → 4.9; 20.6 → 8.3; 23.1 → 10.0; 26.1 → 5.0; 29.3 → 10.0; 36.8 → 8.3
- c6__otcL_W1__R100, K records, K = 3: 18.3 → 7.7; 24.6 → 5.1; 29.4 → 2.6; 33.1 → 10.5; 37.1 → 5.3; 40.7 → 7.9; 45.3 → 10.5; 50.5 → 10.5; 56.6 → 2.6; 68.1 → 10.5
- c6__otcL_W1__R100, K records, K = 5: 34.9 → 0.0; 44.8 → 5.3; 52.1 → 5.3; 57.3 → 5.3; 64.2 → 15.8; 70.1 → 16.7; 74.0 → 5.6; 80.1 → 5.6; 86.6 → 16.7; 94.0 → 11.1
- c6__otcL_W1__R100, K records, K = 10: 44.3 → 0.0; 65.2 → 33.3; 73.5 → 0.0; 80.5 → 0.0; 87.0 → 0.0; 95.4 → 0.0; 97.6 → 40.0; 98.7 → 20.0; 99.4 → 40.0; 99.8 → 20.0
- c6__otcL_W1__R100, K records, K = 20: 55.3 → 50.0; 68.4 → 50.0; 91.5 → 0.0; 97.3 → 50.0; 98.3 → 0.0; 98.5 → 0.0; 99.7 → 0.0; 99.9 → 100.0; 100.0 → 0.0; 100.0 → 100.0
- c6__otcL_W2__R1, K records, K = 1: 4.1 → 10.8; 4.6 → 8.1; 4.9 → 10.8; 5.2 → 2.7; 5.4 → 5.4; 5.7 → 8.1; 6.1 → 0.0; 6.6 → 2.8; 7.5 → 8.3; 10.0 → 0.0
- c6__otcL_W2__R1, K records, K = 2: 7.7 → 5.3; 9.1 → 15.8; 9.9 → 5.3; 11.0 → 11.1; 12.1 → 0.0; 13.2 → 5.6; 14.3 → 0.0; 17.3 → 11.1; 21.1 → 0.0; 34.2 → 0.0
- c6__otcL_W2__R1, K records, K = 3: 12.5 → 0.0; 15.2 → 0.0; 17.2 → 0.0; 18.3 → 8.3; 19.6 → 8.3; 22.8 → 8.3; 25.8 → 0.0; 30.2 → 8.3; 41.9 → 0.0; 60.0 → 0.0
- c6__otcL_W2__R1, K records, K = 5: 20.3 → 12.5; 25.4 → 0.0; 28.8 → 0.0; 31.9 → 14.3; 36.4 → 0.0; 41.2 → 14.3; 44.8 → 0.0; 50.8 → 14.3; 66.4 → 0.0; 90.4 → 0.0
- c6__otcL_W2__R1, K records, K = 10: 34.8 → 0.0; 40.4 → 25.0; 48.3 → 50.0; 55.7 → 0.0; 66.8 → 0.0; 76.9 → 25.0; 84.3 → 0.0; 89.4 → 0.0; 95.2 → 0.0; 99.4 → 0.0
- c6__otcL_W2__R1, K records, K = 20: 47.0 → 50.0; 60.0 → 0.0; 64.0 → 0.0; 80.9 → 0.0; 87.1 → 0.0; 94.4 → 0.0; 96.1 → 0.0; 98.4 → 0.0; 99.4 → 0.0; 99.5 → 0.0
- c6__otcL_W2__R100, K records, K = 1: 3.5 → 1.6; 4.0 → 5.7; 4.6 → 4.9; 5.2 → 1.6; 5.5 → 8.2; 5.8 → 9.0; 6.3 → 8.2; 7.5 → 4.9; 8.7 → 6.6; 10.2 → 7.4
- c6__otcL_W2__R100, K records, K = 2: 9.0 → 1.8; 11.4 → 5.4; 13.1 → 8.9; 15.3 → 7.1; 17.3 → 7.1; 19.4 → 8.9; 22.9 → 7.1; 28.3 → 3.6; 35.8 → 8.9; 45.6 → 5.5
- c6__otcL_W2__R100, K records, K = 3: 16.6 → 8.8; 21.7 → 5.9; 26.5 → 14.7; 30.0 → 11.8; 34.3 → 0.0; 39.4 → 11.8; 46.6 → 0.0; 56.3 → 2.9; 67.0 → 11.8; 79.3 → 11.8
- c6__otcL_W2__R100, K records, K = 5: 30.2 → 5.6; 43.2 → 5.6; 50.2 → 22.2; 56.9 → 0.0; 66.9 → 16.7; 75.1 → 5.9; 84.3 → 0.0; 90.0 → 23.5; 93.3 → 0.0; 97.7 → 11.8
- c6__otcL_W2__R100, K records, K = 10: 58.7 → 0.0; 74.2 → 16.7; 84.0 → 33.3; 90.1 → 33.3; 94.3 → 0.0; 98.2 → 33.3; 99.2 → 33.3; 99.6 → 20.0; 99.8 → 0.0; 100.0 → 20.0
- c6__otcL_W2__R100, K records, K = 20: 49.2 → 0.0; 54.9 → 0.0; 68.0 → 0.0; 93.4 → 0.0; 95.6 → 0.0; 99.9 → 100.0; 100.0 → 0.0; 100.0 → 0.0; 100.0 → 100.0; 100.0 → 0.0
- c6__otcL_Wmis__R1, K records, K = 1: 4.3 → 5.4; 4.9 → 5.4; 5.4 → 8.1; 5.9 → 13.5; 6.5 → 13.5; 7.1 → 24.3; 7.9 → 13.9; 8.8 → 13.9; 10.0 → 22.2; 13.3 → 41.7
- c6__otcL_Wmis__R1, K records, K = 2: 8.4 → 5.3; 10.4 → 10.5; 12.1 → 15.8; 13.2 → 5.6; 14.9 → 11.1; 16.8 → 11.1; 18.7 → 38.9; 21.5 → 5.6; 29.5 → 44.4; 42.8 → 44.4
- c6__otcL_Wmis__R1, K records, K = 3: 14.2 → 7.7; 18.3 → 0.0; 20.6 → 25.0; 23.8 → 8.3; 26.8 → 25.0; 30.3 → 33.3; 34.5 → 16.7; 38.2 → 25.0; 46.6 → 33.3; 67.3 → 58.3
- c6__otcL_Wmis__R1, K records, K = 5: 22.1 → 25.0; 30.7 → 12.5; 36.9 → 0.0; 45.0 → 28.6; 51.0 → 28.6; 56.3 → 57.1; 62.9 → 14.3; 71.9 → 71.4; 84.3 → 71.4; 95.7 → 71.4
- c6__otcL_Wmis__R1, K records, K = 10: 62.9 → 75.0; 81.5 → 50.0; 89.9 → 75.0; 95.7 → 100.0; 98.5 → 75.0; 99.6 → 75.0; 99.9 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_Wmis__R1, K records, K = 20: 98.5 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_Wmis__R100, K records, K = 1: 3.2 → 5.7; 3.6 → 6.6; 3.9 → 4.9; 4.1 → 7.4; 4.4 → 10.7; 4.8 → 6.6; 5.3 → 9.8; 5.6 → 13.9; 6.4 → 11.5; 9.4 → 14.8
- c6__otcL_Wmis__R100, K records, K = 2: 8.6 → 14.3; 10.6 → 14.3; 12.3 → 12.5; 14.3 → 8.9; 16.1 → 10.7; 17.9 → 8.9; 20.0 → 12.5; 23.2 → 8.9; 29.4 → 8.9; 42.9 → 12.7
- c6__otcL_Wmis__R100, K records, K = 3: 17.7 → 23.5; 23.0 → 11.8; 27.0 → 5.9; 31.2 → 8.8; 35.7 → 14.7; 40.1 → 26.5; 46.1 → 2.9; 54.4 → 8.8; 64.7 → 5.9; 78.3 → 17.6
- c6__otcL_Wmis__R100, K records, K = 5: 36.3 → 5.6; 47.8 → 11.1; 55.5 → 11.1; 64.4 → 0.0; 71.1 → 27.8; 78.2 → 5.9; 86.5 → 23.5; 93.1 → 11.8; 97.0 → 11.8; 98.6 → 11.8
- c6__otcL_chain100__R1, K records, K = 1: 3.9 → 4.8; 4.3 → 7.1; 4.6 → 9.5; 4.8 → 0.0; 5.1 → 7.1; 5.4 → 0.0; 5.6 → 4.8; 5.9 → 7.1; 6.4 → 7.1; 7.4 → 7.1
- c6__otcL_chain100__R1, K records, K = 2: 7.3 → 4.8; 8.5 → 19.0; 9.4 → 4.8; 10.1 → 0.0; 10.9 → 9.5; 11.8 → 4.8; 12.9 → 0.0; 14.1 → 19.0; 16.3 → 9.5; 22.2 → 5.0
- c6__otcL_chain100__R1, K records, K = 3: 11.7 → 14.3; 14.3 → 14.3; 15.4 → 21.4; 16.5 → 7.1; 18.2 → 0.0; 20.6 → 7.1; 22.7 → 7.1; 26.1 → 7.1; 31.1 → 7.1; 40.3 → 7.1
- c6__otcL_chain100__R1, K records, K = 5: 20.3 → 0.0; 24.7 → 11.1; 29.8 → 22.2; 33.3 → 12.5; 38.0 → 50.0; 41.9 → 25.0; 46.1 → 25.0; 51.0 → 25.0; 58.5 → 25.0; 79.3 → 25.0
- c6__otcL_chain100__R1, K records, K = 10: 49.7 → 80.0; 60.4 → 75.0; 72.7 → 75.0; 79.6 → 50.0; 83.1 → 75.0; 90.3 → 25.0; 94.1 → 75.0; 96.2 → 75.0; 98.7 → 100.0; 99.7 → 75.0
- c6__otcL_chain100__R1, K records, K = 20: 86.9 → 50.0; 98.5 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_chain100__R100, K records, K = 1: 2.2 → 2.4; 2.4 → 0.8; 2.6 → 1.6; 2.7 → 0.8; 2.8 → 4.0; 2.9 → 1.6; 3.1 → 1.6; 3.2 → 8.1; 3.5 → 6.5; 3.9 → 4.0
- c6__otcL_chain100__R100, K records, K = 2: 4.5 → 6.9; 5.3 → 5.2; 5.8 → 0.0; 6.2 → 0.0; 6.7 → 0.0; 7.2 → 0.0; 7.8 → 7.0; 8.7 → 7.0; 10.0 → 7.0; 12.9 → 8.8
- c6__otcL_chain100__R100, K records, K = 3: 7.5 → 5.7; 9.4 → 11.4; 10.5 → 5.7; 11.4 → 2.9; 12.6 → 11.4; 13.9 → 2.9; 15.4 → 14.7; 17.1 → 0.0; 20.0 → 5.9; 25.8 → 5.9
- c6__otcL_chain100__R100, K records, K = 5: 15.4 → 0.0; 19.3 → 29.4; 21.5 → 6.2; 24.4 → 6.2; 28.4 → 12.5; 32.0 → 18.8; 35.9 → 18.8; 42.1 → 31.2; 51.6 → 12.5; 66.0 → 18.8
- c6__otcL_chain50__R1, K records, K = 1: 3.5 → 4.7; 3.9 → 7.1; 4.2 → 7.1; 4.3 → 11.9; 4.5 → 7.1; 4.8 → 2.4; 5.0 → 9.5; 5.4 → 4.8; 5.8 → 4.8; 6.7 → 4.8
- c6__otcL_chain50__R1, K records, K = 2: 7.1 → 19.0; 8.5 → 4.8; 9.6 → 0.0; 10.6 → 23.8; 11.6 → 0.0; 12.6 → 4.8; 13.6 → 14.3; 15.1 → 14.3; 17.2 → 4.8; 21.3 → 19.0
- c6__otcL_chain50__R1, K records, K = 3: 13.9 → 7.1; 16.2 → 14.3; 18.4 → 7.1; 19.8 → 28.6; 21.6 → 7.1; 24.1 → 21.4; 27.0 → 21.4; 30.5 → 28.6; 35.0 → 23.1; 45.1 → 15.4
- c6__otcL_chain50__R1, K records, K = 5: 23.7 → 11.1; 29.2 → 44.4; 33.6 → 22.2; 38.9 → 25.0; 45.4 → 37.5; 51.0 → 37.5; 54.6 → 37.5; 64.3 → 37.5; 75.8 → 37.5; 87.3 → 37.5
- c6__otcL_chain50__R1, K records, K = 10: 57.5 → 80.0; 74.5 → 100.0; 92.1 → 75.0; 97.1 → 100.0; 98.5 → 100.0; 99.6 → 75.0; 99.9 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_chain50__R1, K records, K = 20: 99.9 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcL_chain50__R100, K records, K = 1: 2.0 → 1.6; 2.2 → 4.0; 2.4 → 4.8; 2.5 → 2.4; 2.6 → 2.4; 2.7 → 1.6; 2.8 → 3.2; 2.9 → 3.2; 3.1 → 4.8; 3.7 → 3.2
- c6__otcL_chain50__R100, K records, K = 2: 4.8 → 7.4; 5.8 → 5.6; 6.4 → 5.6; 6.8 → 7.4; 7.2 → 9.3; 7.8 → 5.7; 8.5 → 3.8; 9.3 → 1.9; 10.6 → 5.7; 14.3 → 7.5
- c6__otcL_chain50__R100, K records, K = 3: 8.5 → 10.0; 10.6 → 13.3; 11.8 → 3.3; 12.9 → 13.3; 14.1 → 0.0; 15.6 → 6.9; 17.4 → 6.9; 19.9 → 6.9; 22.5 → 10.3; 29.7 → 6.9
- c6__otcL_chain50__R100, K records, K = 5: 17.8 → 25.0; 23.2 → 16.7; 28.5 → 25.0; 32.6 → 41.7; 35.4 → 25.0; 37.4 → 41.7; 42.6 → 33.3; 48.1 → 33.3; 54.4 → 25.0; 65.3 → 50.0
- c6__otc_W0__R1, K records, K = 1: 4.0 → 0.0; 4.4 → 2.4; 4.6 → 0.0; 4.8 → 7.3; 5.0 → 12.2; 5.3 → 4.9; 5.5 → 2.4; 5.8 → 9.8; 6.2 → 9.8; 7.3 → 12.2
- c6__otc_W0__R1, K records, K = 2: 7.6 → 0.0; 8.8 → 0.0; 9.6 → 9.5; 10.3 → 19.0; 11.0 → 9.5; 11.8 → 0.0; 12.7 → 10.0; 13.9 → 5.0; 15.7 → 15.0; 21.4 → 15.0
- c6__otc_W0__R1, K records, K = 3: 11.5 → 0.0; 13.9 → 14.3; 16.1 → 14.3; 17.4 → 7.1; 18.7 → 7.1; 20.3 → 14.3; 21.9 → 21.4; 24.7 → 15.4; 28.9 → 30.8; 41.6 → 15.4
- c6__otc_W0__R1, K records, K = 5: 23.3 → 11.1; 27.9 → 12.5; 31.0 → 0.0; 34.8 → 50.0; 38.7 → 25.0; 43.2 → 25.0; 47.4 → 37.5; 54.0 → 25.0; 63.7 → 50.0; 73.1 → 25.0
- c6__otc_W0__R1, K records, K = 10: 48.3 → 25.0; 62.1 → 100.0; 71.3 → 75.0; 79.4 → 100.0; 86.9 → 50.0; 89.9 → 100.0; 95.7 → 100.0; 97.7 → 100.0; 99.4 → 100.0; 99.9 → 100.0
- c6__otc_W0__R1, K records, K = 20: 99.7 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_W0__R100, K records, K = 1: 2.3 → 2.5; 2.5 → 3.3; 2.6 → 4.1; 2.8 → 2.5; 2.9 → 3.3; 3.0 → 2.5; 3.1 → 2.5; 3.2 → 4.1; 3.5 → 3.3; 4.2 → 2.5
- c6__otc_W0__R100, K records, K = 2: 4.6 → 1.8; 5.4 → 5.4; 5.9 → 0.0; 6.3 → 3.6; 6.7 → 0.0; 7.3 → 1.8; 8.1 → 1.8; 9.0 → 14.3; 10.3 → 5.4; 14.3 → 0.0
- c6__otc_W0__R100, K records, K = 3: 8.0 → 11.8; 9.4 → 11.8; 10.3 → 8.8; 11.3 → 5.9; 12.2 → 14.7; 13.3 → 0.0; 14.8 → 0.0; 16.7 → 9.1; 19.7 → 12.1; 29.5 → 6.1
- c6__otc_W0__R100, K records, K = 5: 15.4 → 12.5; 19.7 → 12.5; 22.5 → 12.5; 25.5 → 12.5; 28.9 → 37.5; 31.9 → 13.3; 36.2 → 20.0; 39.4 → 20.0; 44.8 → 20.0; 63.4 → 26.7
- c6__otc_W1__R1, K records, K = 1: 3.1 → 7.7; 3.3 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 6.0 → 0.0
- c6__otc_W1__R1, K records, K = 2: 4.9 → 5.0; 6.0 → 0.0; 6.7 → 0.0; 7.3 → 5.0; 8.0 → 0.0; 8.9 → 0.0; 9.8 → 0.0; 10.7 → 0.0; 11.9 → 0.0; 14.6 → 0.0
- c6__otc_W1__R1, K records, K = 3: 7.6 → 0.0; 9.5 → 7.7; 10.8 → 0.0; 12.0 → 0.0; 13.3 → 0.0; 14.8 → 7.7; 16.5 → 0.0; 18.0 → 0.0; 20.5 → 0.0; 29.0 → 0.0
- c6__otc_W1__R1, K records, K = 5: 14.0 → 0.0; 17.7 → 0.0; 19.2 → 0.0; 22.3 → 0.0; 25.1 → 12.5; 27.7 → 0.0; 30.5 → 0.0; 34.8 → 0.0; 41.4 → 0.0; 55.8 → 0.0
- c6__otc_W1__R1, K records, K = 10: 22.5 → 0.0; 26.9 → 0.0; 30.9 → 0.0; 36.0 → 0.0; 39.4 → 0.0; 45.2 → 0.0; 52.6 → 0.0; 63.9 → 0.0; 77.5 → 0.0; 90.9 → 0.0
- c6__otc_W1__R1, K records, K = 20: 33.7 → 0.0; 48.8 → 0.0; 53.2 → 0.0; 59.2 → 0.0; 61.7 → 0.0; 72.5 → 0.0; 75.2 → 0.0; 78.3 → 0.0; 91.5 → 0.0; 99.0 → 0.0
- c6__otc_W1__R100, K records, K = 1: 3.5 → 0.8; 4.1 → 3.8; 4.5 → 4.6; 4.7 → 9.2; 5.1 → 7.6; 5.6 → 6.9; 6.3 → 6.1; 7.0 → 13.0; 7.6 → 10.7; 8.2 → 9.2
- c6__otc_W1__R100, K records, K = 2: 8.7 → 8.2; 11.3 → 9.8; 13.2 → 6.6; 14.8 → 9.8; 17.1 → 4.9; 20.0 → 6.7; 22.8 → 16.7; 25.6 → 8.3; 28.5 → 13.3; 33.9 → 0.0
- c6__otc_W1__R100, K records, K = 3: 16.6 → 5.1; 21.4 → 5.1; 24.7 → 10.5; 28.7 → 7.9; 33.8 → 7.9; 38.8 → 7.9; 43.8 → 15.8; 49.1 → 13.2; 54.6 → 7.9; 63.0 → 0.0
- c6__otc_W1__R100, K records, K = 5: 30.8 → 5.3; 40.0 → 0.0; 45.1 → 5.3; 50.9 → 5.3; 59.3 → 5.3; 65.0 → 22.2; 72.6 → 22.2; 79.5 → 5.6; 84.6 → 11.1; 91.3 → 11.1
- c6__otc_W1__R100, K records, K = 10: 45.4 → 0.0; 61.2 → 16.7; 71.1 → 16.7; 84.5 → 16.7; 89.6 → 16.7; 94.0 → 16.7; 96.0 → 20.0; 97.9 → 20.0; 99.3 → 40.0; 99.8 → 0.0
- c6__otc_W1__R100, K records, K = 20: 68.7 → 0.0; 92.5 → 0.0; 97.4 → 100.0; 99.3 → 0.0; 99.7 → 100.0; 99.8 → 0.0; 99.9 → 0.0; 99.9 → 0.0; 99.9 → 100.0; 100.0 → 0.0
- c6__otc_W2__R1, K records, K = 1: 4.4 → 0.0; 5.0 → 2.7; 5.7 → 5.4; 6.2 → 18.9; 6.9 → 10.8; 7.5 → 16.2; 8.5 → 13.9; 9.6 → 11.1; 11.6 → 0.0; 19.7 → 0.0
- c6__otc_W2__R1, K records, K = 2: 8.6 → 0.0; 10.8 → 5.3; 12.5 → 15.8; 14.3 → 11.1; 16.6 → 22.2; 18.9 → 5.6; 22.5 → 16.7; 26.4 → 11.1; 32.5 → 0.0; 54.5 → 0.0
- c6__otc_W2__R1, K records, K = 3: 13.3 → 7.7; 16.5 → 7.7; 19.5 → 8.3; 22.5 → 0.0; 26.4 → 16.7; 31.2 → 16.7; 37.1 → 16.7; 42.9 → 16.7; 52.6 → 0.0; 78.5 → 0.0
- c6__otc_W2__R1, K records, K = 5: 21.3 → 0.0; 27.0 → 0.0; 31.4 → 0.0; 37.9 → 14.3; 42.7 → 14.3; 47.3 → 14.3; 56.9 → 14.3; 71.9 → 0.0; 83.0 → 14.3; 95.2 → 14.3
- c6__otc_W2__R1, K records, K = 10: 32.6 → 0.0; 42.6 → 25.0; 47.8 → 0.0; 53.0 → 0.0; 69.5 → 0.0; 78.3 → 0.0; 83.0 → 33.3; 89.8 → 33.3; 97.4 → 0.0; 99.7 → 0.0
- c6__otc_W2__R1, K records, K = 20: 38.8 → 50.0; 47.5 → 0.0; 57.9 → 0.0; 74.6 → 0.0; 88.5 → 0.0; 95.7 → 50.0; 99.2 → 0.0; 99.9 → 0.0; 100.0 → 0.0; 100.0 → 0.0
- c6__otc_W2__R100, K records, K = 1: 3.7 → 3.3; 4.1 → 3.3; 4.7 → 5.7; 5.2 → 3.3; 5.8 → 4.9; 6.4 → 11.5; 7.0 → 11.5; 7.8 → 9.0; 8.7 → 7.4; 12.2 → 6.6
- c6__otc_W2__R100, K records, K = 2: 8.6 → 3.6; 11.6 → 5.4; 13.6 → 1.8; 16.3 → 12.5; 19.3 → 12.5; 22.2 → 5.4; 25.1 → 8.9; 29.1 → 8.9; 33.8 → 5.4; 50.9 → 7.3
- c6__otc_W2__R100, K records, K = 3: 14.5 → 2.9; 21.0 → 2.9; 26.0 → 2.9; 31.2 → 0.0; 35.6 → 11.8; 41.8 → 5.9; 48.4 → 17.6; 53.9 → 5.9; 61.0 → 14.7; 80.9 → 5.9
- c6__otc_W2__R100, K records, K = 5: 29.1 → 5.6; 39.6 → 5.6; 48.0 → 16.7; 57.9 → 0.0; 65.9 → 16.7; 73.0 → 17.6; 82.3 → 5.9; 87.0 → 11.8; 92.4 → 17.6; 98.0 → 5.9
- c6__otc_W2__R100, K records, K = 10: 46.9 → 16.7; 64.1 → 16.7; 85.4 → 16.7; 92.9 → 33.3; 96.4 → 0.0; 98.4 → 0.0; 99.2 → 33.3; 99.7 → 20.0; 99.9 → 20.0; 100.0 → 20.0
- c6__otc_W2__R100, K records, K = 20: 79.5 → 0.0; 96.4 → 0.0; 97.1 → 100.0; 98.5 → 0.0; 99.7 → 0.0; 99.9 → 0.0; 100.0 → 0.0; 100.0 → 100.0; 100.0 → 0.0; 100.0 → 100.0
- c6__otc_Wmis__R1, K records, K = 1: 4.2 → 2.7; 4.7 → 5.4; 5.2 → 16.2; 5.8 → 29.7; 6.4 → 13.5; 7.2 → 18.9; 8.0 → 2.8; 9.2 → 19.4; 11.1 → 38.9; 14.8 → 58.3
- c6__otc_Wmis__R1, K records, K = 2: 8.5 → 0.0; 10.6 → 0.0; 12.4 → 5.3; 14.3 → 27.8; 15.9 → 16.7; 17.8 → 11.1; 22.0 → 22.2; 27.1 → 33.3; 33.2 → 33.3; 47.0 → 66.7
- c6__otc_Wmis__R1, K records, K = 3: 13.2 → 7.7; 17.2 → 0.0; 20.1 → 8.3; 23.2 → 25.0; 25.5 → 41.7; 29.8 → 25.0; 36.0 → 25.0; 43.2 → 41.7; 52.1 → 41.7; 77.4 → 75.0
- c6__otc_Wmis__R1, K records, K = 5: 26.9 → 25.0; 33.7 → 0.0; 37.9 → 12.5; 43.4 → 14.3; 48.7 → 42.9; 54.7 → 57.1; 61.0 → 42.9; 75.4 → 42.9; 87.4 → 71.4; 97.2 → 85.7
- c6__otc_Wmis__R1, K records, K = 10: 61.6 → 25.0; 87.0 → 100.0; 94.3 → 50.0; 98.4 → 100.0; 99.0 → 75.0; 99.6 → 100.0; 99.8 → 66.7; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_Wmis__R1, K records, K = 20: 99.2 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_Wmis__R100, K records, K = 1: 5.0 → 4.9; 5.8 → 4.9; 6.8 → 5.7; 7.7 → 9.0; 8.6 → 9.8; 10.2 → 9.8; 12.6 → 8.2; 14.4 → 15.6; 17.2 → 13.1; 25.2 → 14.8
- c6__otc_Wmis__R100, K records, K = 2: 13.0 → 8.9; 18.6 → 7.1; 23.7 → 3.6; 28.1 → 8.9; 34.2 → 8.9; 40.8 → 10.7; 47.7 → 16.1; 55.8 → 8.9; 66.8 → 12.5; 80.3 → 14.5
- c6__otc_Wmis__R100, K records, K = 3: 22.6 → 17.6; 34.3 → 5.9; 42.2 → 2.9; 50.6 → 8.8; 59.5 → 14.7; 68.5 → 5.9; 76.1 → 8.8; 86.3 → 14.7; 92.3 → 14.7; 96.8 → 14.7
- c6__otc_Wmis__R100, K records, K = 5: 42.6 → 0.0; 58.7 → 16.7; 70.5 → 0.0; 81.3 → 11.1; 89.3 → 22.2; 93.7 → 11.8; 97.8 → 17.6; 99.5 → 23.5; 99.8 → 17.6; 100.0 → 5.9
- c6__otc_chain100__R1, K records, K = 1: 4.1 → 9.3; 4.5 → 4.8; 4.8 → 2.4; 5.0 → 2.4; 5.2 → 4.8; 5.4 → 2.4; 5.7 → 4.8; 6.0 → 7.1; 6.5 → 2.4; 7.5 → 7.1
- c6__otc_chain100__R1, K records, K = 2: 7.5 → 9.5; 8.7 → 9.5; 9.7 → 9.5; 10.5 → 14.3; 11.2 → 14.3; 12.0 → 0.0; 12.8 → 4.8; 13.8 → 9.5; 15.6 → 4.8; 20.6 → 14.3
- c6__otc_chain100__R1, K records, K = 3: 11.6 → 0.0; 14.0 → 7.1; 15.2 → 0.0; 17.0 → 14.3; 19.0 → 0.0; 20.8 → 21.4; 23.1 → 0.0; 25.7 → 14.3; 30.0 → 21.4; 42.7 → 21.4
- c6__otc_chain100__R1, K records, K = 5: 19.5 → 11.1; 25.1 → 22.2; 30.1 → 44.4; 34.6 → 0.0; 37.9 → 12.5; 40.8 → 50.0; 43.8 → 12.5; 51.4 → 12.5; 62.9 → 12.5; 74.8 → 62.5
- c6__otc_chain100__R1, K records, K = 10: 48.1 → 40.0; 56.9 → 50.0; 63.4 → 75.0; 71.8 → 50.0; 80.4 → 25.0; 85.7 → 100.0; 90.2 → 50.0; 94.7 → 100.0; 96.7 → 50.0; 99.4 → 100.0
- c6__otc_chain100__R1, K records, K = 20: 86.2 → 0.0; 94.5 → 100.0; 99.9 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_chain100__R100, K records, K = 1: 2.2 → 0.0; 2.4 → 2.4; 2.6 → 2.4; 2.7 → 1.6; 2.8 → 0.8; 2.9 → 0.8; 3.1 → 5.7; 3.3 → 4.1; 3.5 → 4.1; 4.1 → 2.5
- c6__otc_chain100__R100, K records, K = 2: 4.8 → 7.1; 5.5 → 1.8; 6.0 → 0.0; 6.4 → 1.8; 6.8 → 0.0; 7.4 → 7.1; 8.0 → 5.5; 8.8 → 5.5; 9.7 → 7.3; 12.8 → 7.3
- c6__otc_chain100__R100, K records, K = 3: 7.7 → 5.9; 9.3 → 8.8; 10.4 → 2.9; 11.3 → 2.9; 12.3 → 5.9; 13.4 → 0.0; 14.7 → 11.8; 16.6 → 8.8; 19.3 → 8.8; 26.4 → 8.8
- c6__otc_chain100__R100, K records, K = 5: 15.0 → 17.6; 18.6 → 5.9; 22.3 → 12.5; 24.7 → 12.5; 26.9 → 6.2; 29.2 → 25.0; 33.1 → 12.5; 37.1 → 12.5; 44.6 → 18.8; 60.6 → 31.2
- c6__otc_chain50__R1, K records, K = 1: 3.6 → 2.3; 4.0 → 11.9; 4.2 → 0.0; 4.4 → 7.1; 4.6 → 2.4; 4.8 → 2.4; 5.0 → 2.4; 5.3 → 7.1; 5.7 → 0.0; 7.0 → 9.5
- c6__otc_chain50__R1, K records, K = 2: 7.9 → 4.8; 9.0 → 4.8; 9.9 → 0.0; 10.7 → 4.8; 12.0 → 14.3; 12.9 → 4.8; 13.9 → 9.5; 15.3 → 14.3; 16.9 → 14.3; 22.0 → 5.0
- c6__otc_chain50__R1, K records, K = 3: 13.4 → 21.4; 16.0 → 21.4; 17.7 → 14.3; 19.8 → 0.0; 22.5 → 14.3; 24.5 → 7.1; 26.9 → 7.1; 31.7 → 28.6; 40.9 → 0.0; 52.9 → 15.4
- c6__otc_chain50__R1, K records, K = 5: 22.9 → 22.2; 29.6 → 11.1; 34.8 → 11.1; 39.6 → 0.0; 42.4 → 25.0; 49.6 → 25.0; 57.8 → 37.5; 64.0 → 25.0; 71.1 → 25.0; 83.5 → 25.0
- c6__otc_chain50__R1, K records, K = 10: 66.2 → 60.0; 81.4 → 100.0; 90.5 → 75.0; 94.0 → 100.0; 96.5 → 100.0; 98.2 → 100.0; 99.2 → 100.0; 99.9 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_chain50__R1, K records, K = 20: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otc_chain50__R100, K records, K = 1: 2.1 → 1.6; 2.2 → 2.4; 2.4 → 2.4; 2.5 → 0.0; 2.6 → 3.3; 2.7 → 3.3; 2.8 → 0.8; 3.0 → 3.3; 3.2 → 2.5; 3.8 → 4.1
- c6__otc_chain50__R100, K records, K = 2: 4.9 → 5.7; 5.9 → 3.8; 6.5 → 1.9; 7.0 → 3.8; 7.4 → 3.8; 7.9 → 0.0; 8.7 → 0.0; 9.3 → 3.8; 10.5 → 0.0; 13.4 → 5.8
- c6__otc_chain50__R100, K records, K = 3: 8.8 → 10.3; 10.8 → 10.3; 12.1 → 3.4; 13.1 → 13.8; 13.7 → 6.9; 15.2 → 6.9; 16.7 → 10.3; 19.6 → 6.9; 23.8 → 3.4; 30.5 → 10.3
- c6__otc_chain50__R100, K records, K = 5: 16.7 → 8.3; 21.5 → 16.7; 25.7 → 33.3; 29.9 → 58.3; 33.4 → 25.0; 37.0 → 25.0; 41.0 → 8.3; 45.2 → 25.0; 56.6 → 16.7; 70.1 → 25.0
- c6_issuer__iwh_delay_L10__R1, iwh_delay_L10: 2.1 → 0.0; 2.3 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_delay_L10__R100, iwh_delay_L10: 1.2 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_delay_L120__R1, iwh_delay_L120: 1.7 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.5 → 0.0; 2.5 → 0.0; 2.6 → 100.0; 2.9 → 0.0
- c6_issuer__iwh_delay_L120__R100, iwh_delay_L120: 1.0 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.4 → 0.0
- c6_issuer__iwh_delay_L30__R1, iwh_delay_L30: 1.5 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.4 → 0.0; 2.4 → 0.0
- c6_issuer__iwh_delay_L30__R100, iwh_delay_L30: 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0
- c6_issuer__iwh_delay_L60__R1, iwh_delay_L60: 1.9 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.6 → 0.0
- c6_issuer__iwh_delay_L60__R100, iwh_delay_L60: 1.0 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.4 → 0.0
- c6_issuer__iwh_none_L10__R1, iwh_none_L10: 2.1 → 0.0; 2.3 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_none_L10__R100, iwh_none_L10: 1.2 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_none_L120__R1, iwh_none_L120: 1.7 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.5 → 0.0; 2.5 → 0.0; 2.5 → 100.0; 2.9 → 0.0
- c6_issuer__iwh_none_L120__R100, iwh_none_L120: 1.0 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.4 → 0.0
- c6_issuer__iwh_none_L30__R1, iwh_none_L30: 1.5 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.4 → 0.0; 2.4 → 0.0
- c6_issuer__iwh_none_L30__R100, iwh_none_L30: 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0
- c6_issuer__iwh_none_L60__R1, iwh_none_L60: 1.9 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.6 → 0.0
- c6_issuer__iwh_none_L60__R100, iwh_none_L60: 1.0 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.4 → 0.0
- c6_issuer__iwh_withhold_L10__R1, iwh_withhold_L10: 2.1 → 0.0; 2.3 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_withhold_L10__R100, iwh_withhold_L10: 1.2 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_withhold_L120__R1, iwh_withhold_L120: 1.7 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.5 → 0.0; 2.5 → 0.0; 2.6 → 100.0; 2.9 → 0.0
- c6_issuer__iwh_withhold_L120__R100, iwh_withhold_L120: 1.0 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.4 → 0.0
- c6_issuer__iwh_withhold_L30__R1, iwh_withhold_L30: 1.5 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.4 → 0.0; 2.4 → 0.0
- c6_issuer__iwh_withhold_L30__R100, iwh_withhold_L30: 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0
- c6_issuer__iwh_withhold_L60__R1, iwh_withhold_L60: 1.9 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.6 → 0.0
- c6_issuer__iwh_withhold_L60__R100, iwh_withhold_L60: 1.0 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.4 → 0.0


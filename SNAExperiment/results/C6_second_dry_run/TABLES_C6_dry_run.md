DRY RUN: fewer runs than the full count. These numbers are not results.

# Experiment C6: the credential path and blind-issued one-time certificates

Chance is the expected accuracy of naming, for each decision, one candidate drawn uniformly from those the vantage finds feasible; zero when the truth is not feasible. Latency: the mean time from capture to posted record of each candidate in that cell.


## passive observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | observer | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.635 | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | observer | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.635 | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | observer | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.635 | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | observer | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.635 | no | 10.50% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | observer | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.380 | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | observer | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.380 | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | observer | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.380 | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | observer | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.380 | no | 5.33% |

## first relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | first_hop | 1 | 4,180 | 7.70% [—, —] | 1.45% | ×5.30 | +0.05 | 0.624 | yes | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | first_hop | 1 | 4,180 | 7.70% [—, —] | 1.45% | ×5.30 | +0.05 | 0.624 | yes | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | first_hop | 1 | 4,180 | 7.70% [—, —] | 1.45% | ×5.30 | +0.05 | 0.624 | yes | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | first_hop | 1 | 4,180 | 7.70% [—, —] | 1.45% | ×5.30 | +0.05 | 0.624 | yes | 10.50% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | first_hop | 1 | 12,040 | 2.40% [—, —] | 0.74% | ×3.24 | +0.07 | 0.387 | yes | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | first_hop | 1 | 12,040 | 2.40% [—, —] | 0.74% | ×3.24 | +0.07 | 0.387 | yes | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | first_hop | 1 | 12,040 | 2.40% [—, —] | 0.74% | ×3.24 | +0.07 | 0.387 | yes | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | first_hop | 1 | 12,040 | 2.40% [—, —] | 0.74% | ×3.24 | +0.07 | 0.387 | yes | 5.33% |

## destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | destination | 1 | 209 | 9.09% [—, —] | 1.61% | ×5.64 | +1.44 | 0.581 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | destination | 1 | 209 | 9.09% [—, —] | 1.61% | ×5.64 | +1.44 | 0.581 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | destination | 1 | 209 | 9.09% [—, —] | 1.61% | ×5.64 | +1.44 | 0.581 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | destination | 1 | 209 | 9.09% [—, —] | 1.61% | ×5.64 | +1.44 | 0.581 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | destination | 1 | 602 | 1.33% [—, —] | 0.82% | ×1.61 | -1.00 | 0.578 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | destination | 1 | 602 | 1.33% [—, —] | 0.82% | ×1.61 | -1.00 | 0.578 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | destination | 1 | 602 | 1.33% [—, —] | 0.82% | ×1.61 | -1.00 | 0.578 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | destination | 1 | 602 | 1.33% [—, —] | 0.82% | ×1.61 | -1.00 | 0.578 | no | not applicable |

## destination_keyed

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | destination_keyed | 1 | 209 | 19.14% [—, —] | 5.37% | ×3.56 | +11.48 | 0.594 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | destination_keyed | 1 | 209 | 19.14% [—, —] | 5.37% | ×3.56 | +11.48 | 0.594 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | destination_keyed | 1 | 209 | 19.14% [—, —] | 5.37% | ×3.56 | +11.48 | 0.594 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | destination_keyed | 1 | 209 | 19.14% [—, —] | 5.37% | ×3.56 | +11.48 | 0.594 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | destination_keyed | 1 | 602 | 6.15% [—, —] | 2.35% | ×2.61 | +3.82 | 0.624 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | destination_keyed | 1 | 602 | 6.15% [—, —] | 2.35% | ×2.61 | +3.82 | 0.624 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | destination_keyed | 1 | 602 | 6.15% [—, —] | 2.35% | ×2.61 | +3.82 | 0.624 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | destination_keyed | 1 | 602 | 6.15% [—, —] | 2.35% | ×2.61 | +3.82 | 0.624 | no | not applicable |

## first relay with the destination on its path

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | first_relay_with_destination | 1 | 209 | 100.00% [—, —] | 100.00% | ×1.00 | +92.34 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | first_relay_with_destination | 1 | 209 | 100.00% [—, —] | 100.00% | ×1.00 | +92.34 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | first_relay_with_destination | 1 | 209 | 100.00% [—, —] | 100.00% | ×1.00 | +92.34 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | first_relay_with_destination | 1 | 209 | 100.00% [—, —] | 100.00% | ×1.00 | +92.34 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | first_relay_with_destination | 1 | 602 | 100.00% [—, —] | 100.00% | ×1.00 | +97.67 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | first_relay_with_destination | 1 | 602 | 100.00% [—, —] | 100.00% | ×1.00 | +97.67 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | first_relay_with_destination | 1 | 602 | 100.00% [—, —] | 100.00% | ×1.00 | +97.67 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | first_relay_with_destination | 1 | 602 | 100.00% [—, —] | 100.00% | ×1.00 | +97.67 | — | no | not applicable |

## issuer_0

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_0 [share 50%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_0 [share 50%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_0 [share 50%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_0 [share 50%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_0 [share 50%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_0 [share 50%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_0 [share 50%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_0 [share 50%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0 [share 50%, all records] | 1 | 602 | 3.49% [—, —] | 0.84% | ×4.13 | +1.16 | 0.345 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0 [share 50%, all records] | 1 | 602 | 3.16% [—, —] | 0.56% | ×5.63 | +0.83 | 0.517 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0 [share 50%, all records] | 1 | 602 | 1.83% [—, —] | 0.65% | ×2.81 | -0.50 | 0.523 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0 [share 50%, all records] | 1 | 602 | 1.16% [—, —] | 0.74% | ×1.57 | -1.16 | 0.596 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0 [share 50%, its own devices] | 1 | 346 | 6.07% [—, —] | 1.47% | ×4.13 | +4.34 | 0.329 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0 [share 50%, its own devices] | 1 | 346 | 5.49% [—, —] | 0.97% | ×5.63 | +3.76 | 0.517 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0 [share 50%, its own devices] | 1 | 346 | 3.18% [—, —] | 1.13% | ×2.81 | +1.45 | 0.532 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0 [share 50%, its own devices] | 1 | 346 | 2.02% [—, —] | 1.29% | ×1.57 | +0.29 | 0.618 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0 [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.00% | ×— | -3.12 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0 [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.00% | ×— | -3.12 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0 [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.00% | ×— | -3.12 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0 [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.00% | ×— | -3.12 | — | no | not applicable |

## issuer_0_with_observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_0_with_observer [share 50%, all records] | 1 | 209 | 0.00% [—, —] | 1.45% | ×0.00 | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_0_with_observer [share 50%, all records] | 1 | 209 | 0.00% [—, —] | 1.45% | ×0.00 | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_0_with_observer [share 50%, all records] | 1 | 209 | 3.35% [—, —] | 1.45% | ×2.31 | -4.31 | 0.229 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_0_with_observer [share 50%, all records] | 1 | 209 | 6.70% [—, —] | 1.45% | ×4.61 | -0.96 | 0.581 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 1.45% | ×0.00 | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 1.45% | ×0.00 | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 209 | 3.35% [—, —] | 1.45% | ×2.31 | -4.31 | 0.229 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 209 | 6.70% [—, —] | 1.45% | ×4.61 | -0.96 | 0.581 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0_with_observer [share 50%, all records] | 1 | 602 | 3.99% [—, —] | 0.74% | ×5.38 | +1.66 | 0.438 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0_with_observer [share 50%, all records] | 1 | 602 | 1.99% [—, —] | 0.74% | ×2.69 | -0.33 | 0.336 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0_with_observer [share 50%, all records] | 1 | 602 | 1.83% [—, —] | 0.74% | ×2.47 | -0.50 | 0.492 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0_with_observer [share 50%, all records] | 1 | 602 | 2.16% [—, —] | 0.74% | ×2.92 | -0.17 | 0.386 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0_with_observer [share 50%, its own devices] | 1 | 346 | 6.94% [—, —] | 0.74% | ×9.35 | +5.20 | 0.421 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0_with_observer [share 50%, its own devices] | 1 | 346 | 3.47% [—, —] | 0.74% | ×4.67 | +1.73 | 0.327 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0_with_observer [share 50%, its own devices] | 1 | 346 | 2.60% [—, —] | 0.74% | ×3.51 | +0.87 | 0.527 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0_with_observer [share 50%, its own devices] | 1 | 346 | 1.73% [—, —] | 0.74% | ×2.34 | +0.00 | 0.375 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.74% | ×0.00 | -3.12 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.74% | ×0.00 | -3.12 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 256 | 0.78% [—, —] | 0.74% | ×1.06 | -2.34 | 0.313 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0_with_observer [share 50%, other issuers' devices] | 1 | 256 | 2.73% [—, —] | 0.74% | ×3.70 | -0.39 | 0.407 | no | not applicable |

## issuer_0_with_first_relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 209 | 0.00% [—, —] | 1.45% | ×0.00 | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 209 | 0.48% [—, —] | 1.45% | ×0.33 | -7.18 | 0.103 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 209 | 3.35% [—, —] | 1.45% | ×2.31 | -4.31 | 0.233 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 209 | 6.70% [—, —] | 1.45% | ×4.61 | -0.96 | 0.589 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 1.45% | ×0.00 | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 209 | 0.48% [—, —] | 1.45% | ×0.33 | -7.18 | 0.103 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 209 | 3.35% [—, —] | 1.45% | ×2.31 | -4.31 | 0.233 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 209 | 6.70% [—, —] | 1.45% | ×4.61 | -0.96 | 0.589 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 602 | 3.82% [—, —] | 0.74% | ×5.16 | +1.50 | 0.460 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 602 | 2.66% [—, —] | 0.74% | ×3.59 | +0.33 | 0.366 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 602 | 1.83% [—, —] | 0.74% | ×2.47 | -0.50 | 0.496 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0_with_first_relay [share 50%, all records] | 1 | 602 | 2.66% [—, —] | 0.74% | ×3.59 | +0.33 | 0.423 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0_with_first_relay [share 50%, its own devices] | 1 | 346 | 6.65% [—, —] | 0.74% | ×8.96 | +4.91 | 0.443 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0_with_first_relay [share 50%, its own devices] | 1 | 346 | 4.62% [—, —] | 0.74% | ×6.23 | +2.89 | 0.356 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0_with_first_relay [share 50%, its own devices] | 1 | 346 | 2.60% [—, —] | 0.74% | ×3.51 | +0.87 | 0.522 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0_with_first_relay [share 50%, its own devices] | 1 | 346 | 2.60% [—, —] | 0.74% | ×3.51 | +0.87 | 0.400 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.74% | ×0.00 | -3.12 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 256 | 0.00% [—, —] | 0.74% | ×0.00 | -3.12 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 256 | 0.78% [—, —] | 0.74% | ×1.06 | -2.34 | 0.366 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0_with_first_relay [share 50%, other issuers' devices] | 1 | 256 | 2.73% [—, —] | 0.74% | ×3.70 | -0.39 | 0.462 | no | not applicable |

## issuer_1

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_1 [share 30%, all records] | 1 | 209 | 17.22% [—, —] | 4.89% | ×3.52 | +9.57 | 0.622 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_1 [share 30%, all records] | 1 | 209 | 11.96% [—, —] | 3.33% | ×3.59 | +4.31 | 0.577 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_1 [share 30%, all records] | 1 | 209 | 6.22% [—, —] | 3.33% | ×1.87 | -1.44 | 0.662 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_1 [share 30%, all records] | 1 | 209 | 1.44% [—, —] | 3.33% | ×0.43 | -6.22 | 0.898 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_1 [share 30%, its own devices] | 1 | 209 | 17.22% [—, —] | 4.89% | ×3.52 | +9.57 | 0.622 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_1 [share 30%, its own devices] | 1 | 209 | 11.96% [—, —] | 3.33% | ×3.59 | +4.31 | 0.577 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_1 [share 30%, its own devices] | 1 | 209 | 6.22% [—, —] | 3.33% | ×1.87 | -1.44 | 0.662 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_1 [share 30%, its own devices] | 1 | 209 | 1.44% [—, —] | 3.33% | ×0.43 | -6.22 | 0.898 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1 [share 30%, all records] | 1 | 602 | 2.49% [—, —] | 0.65% | ×3.81 | +0.17 | 0.530 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1 [share 30%, all records] | 1 | 602 | 1.33% [—, —] | 0.42% | ×3.14 | -1.00 | 0.599 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1 [share 30%, all records] | 1 | 602 | 0.66% [—, —] | 0.41% | ×1.62 | -1.66 | 0.701 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1 [share 30%, all records] | 1 | 602 | 0.33% [—, —] | 0.50% | ×0.67 | -1.99 | 0.968 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1 [share 30%, its own devices] | 1 | 148 | 10.14% [—, —] | 2.66% | ×3.81 | +5.41 | 0.532 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1 [share 30%, its own devices] | 1 | 148 | 5.41% [—, —] | 1.72% | ×3.14 | +0.68 | 0.612 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1 [share 30%, its own devices] | 1 | 148 | 2.70% [—, —] | 1.66% | ×1.62 | -2.03 | 0.681 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1 [share 30%, its own devices] | 1 | 148 | 1.35% [—, —] | 2.03% | ×0.67 | -3.38 | 0.969 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1 [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.00% | ×— | -1.54 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1 [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.00% | ×— | -1.54 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1 [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.00% | ×— | -1.54 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1 [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.00% | ×— | -1.54 | — | no | not applicable |

## issuer_1_with_observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_1_with_observer [share 30%, all records] | 1 | 209 | 16.75% [—, —] | 1.45% | ×11.53 | +9.09 | 0.645 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_1_with_observer [share 30%, all records] | 1 | 209 | 13.40% [—, —] | 1.45% | ×9.22 | +5.74 | 0.587 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_1_with_observer [share 30%, all records] | 1 | 209 | 11.00% [—, —] | 1.45% | ×7.57 | +3.35 | 0.552 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_1_with_observer [share 30%, all records] | 1 | 209 | 8.13% [—, —] | 1.45% | ×5.60 | +0.48 | 0.599 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 209 | 16.75% [—, —] | 1.45% | ×11.53 | +9.09 | 0.645 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 209 | 13.40% [—, —] | 1.45% | ×9.22 | +5.74 | 0.587 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 209 | 11.00% [—, —] | 1.45% | ×7.57 | +3.35 | 0.552 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 209 | 8.13% [—, —] | 1.45% | ×5.60 | +0.48 | 0.599 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1_with_observer [share 30%, all records] | 1 | 602 | 2.66% [—, —] | 0.74% | ×3.59 | +0.33 | 0.484 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1_with_observer [share 30%, all records] | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.468 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1_with_observer [share 30%, all records] | 1 | 602 | 2.16% [—, —] | 0.74% | ×2.92 | -0.17 | 0.422 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1_with_observer [share 30%, all records] | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.380 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 148 | 10.81% [—, —] | 0.74% | ×14.67 | +6.08 | 0.465 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 148 | 9.46% [—, —] | 0.74% | ×12.84 | +4.73 | 0.467 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 148 | 5.41% [—, —] | 0.74% | ×7.34 | +0.68 | 0.481 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1_with_observer [share 30%, its own devices] | 1 | 148 | 4.73% [—, —] | 0.74% | ×6.42 | +0.00 | 0.402 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1_with_observer [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.74% | ×0.00 | -1.54 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1_with_observer [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.74% | ×0.00 | -1.54 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1_with_observer [share 30%, other issuers' devices] | 1 | 454 | 1.10% [—, —] | 0.74% | ×1.49 | -0.44 | 0.326 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1_with_observer [share 30%, other issuers' devices] | 1 | 454 | 1.54% [—, —] | 0.74% | ×2.08 | +0.00 | 0.352 | no | not applicable |

## issuer_1_with_first_relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 209 | 16.75% [—, —] | 1.45% | ×11.53 | +9.09 | 0.642 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 209 | 12.92% [—, —] | 1.45% | ×8.89 | +5.26 | 0.598 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 209 | 11.00% [—, —] | 1.45% | ×7.57 | +3.35 | 0.543 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 209 | 8.13% [—, —] | 1.45% | ×5.60 | +0.48 | 0.584 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 209 | 16.75% [—, —] | 1.45% | ×11.53 | +9.09 | 0.642 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 209 | 12.92% [—, —] | 1.45% | ×8.89 | +5.26 | 0.598 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 209 | 11.00% [—, —] | 1.45% | ×7.57 | +3.35 | 0.543 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 209 | 8.13% [—, —] | 1.45% | ×5.60 | +0.48 | 0.584 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 602 | 2.82% [—, —] | 0.74% | ×3.81 | +0.50 | 0.476 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.479 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 602 | 2.66% [—, —] | 0.74% | ×3.59 | +0.33 | 0.423 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1_with_first_relay [share 30%, all records] | 1 | 602 | 2.82% [—, —] | 0.74% | ×3.81 | +0.50 | 0.420 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 148 | 11.49% [—, —] | 0.74% | ×15.59 | +6.76 | 0.456 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 148 | 9.46% [—, —] | 0.74% | ×12.84 | +4.73 | 0.476 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 148 | 5.41% [—, —] | 0.74% | ×7.34 | +0.68 | 0.516 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1_with_first_relay [share 30%, its own devices] | 1 | 148 | 4.73% [—, —] | 0.74% | ×6.42 | +0.00 | 0.461 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.74% | ×0.00 | -1.54 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 1 | 454 | 0.00% [—, —] | 0.74% | ×0.00 | -1.54 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 1 | 454 | 1.76% [—, —] | 0.74% | ×2.38 | +0.22 | 0.340 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1_with_first_relay [share 30%, other issuers' devices] | 1 | 454 | 2.20% [—, —] | 0.74% | ×2.97 | +0.66 | 0.392 | no | not applicable |

## issuer_1_with_destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_1_with_destination | 1 | 209 | 19.62% [—, —] | 5.39% | ×3.64 | +11.96 | 0.580 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_1_with_destination | 1 | 209 | 14.83% [—, —] | 5.37% | ×2.76 | +7.18 | 0.605 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_1_with_destination | 1 | 209 | 17.22% [—, —] | 5.37% | ×3.21 | +9.57 | 0.480 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_1_with_destination | 1 | 209 | 18.18% [—, —] | 5.37% | ×3.38 | +10.53 | 0.546 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_1_with_destination | 1 | 148 | 10.81% [—, —] | 2.96% | ×3.65 | +6.08 | 0.529 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_1_with_destination | 1 | 148 | 8.78% [—, —] | 2.94% | ×2.98 | +4.05 | 0.456 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_1_with_destination | 1 | 148 | 10.81% [—, —] | 2.94% | ×3.67 | +6.08 | 0.590 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_1_with_destination | 1 | 148 | 10.81% [—, —] | 2.94% | ×3.67 | +6.08 | 0.536 | no | not applicable |

## issuer_2

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_2 [share 20%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_2 [share 20%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_2 [share 20%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_2 [share 20%, all records] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_2 [share 20%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_2 [share 20%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_2 [share 20%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_2 [share 20%, other issuers' devices] | 1 | 209 | 0.00% [—, —] | 0.00% | ×— | -7.66 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2 [share 20%, all records] | 1 | 602 | 1.99% [—, —] | 0.62% | ×3.20 | -0.33 | 0.448 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2 [share 20%, all records] | 1 | 602 | 1.00% [—, —] | 0.42% | ×2.39 | -1.33 | 0.322 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2 [share 20%, all records] | 1 | 602 | 0.66% [—, —] | 0.52% | ×1.28 | -1.66 | 0.662 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2 [share 20%, all records] | 1 | 602 | 1.16% [—, —] | 0.37% | ×3.11 | -1.16 | 0.490 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2 [share 20%, its own devices] | 1 | 108 | 11.11% [—, —] | 3.47% | ×3.20 | +10.19 | 0.540 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2 [share 20%, its own devices] | 1 | 108 | 5.56% [—, —] | 2.33% | ×2.39 | +4.63 | 0.330 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2 [share 20%, its own devices] | 1 | 108 | 3.70% [—, —] | 2.90% | ×1.28 | +2.78 | 0.641 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2 [share 20%, its own devices] | 1 | 108 | 6.48% [—, —] | 2.08% | ×3.11 | +5.56 | 0.479 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2 [share 20%, other issuers' devices] | 1 | 494 | 0.00% [—, —] | 0.00% | ×— | -2.63 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2 [share 20%, other issuers' devices] | 1 | 494 | 0.00% [—, —] | 0.00% | ×— | -2.63 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2 [share 20%, other issuers' devices] | 1 | 494 | 0.00% [—, —] | 0.00% | ×— | -2.63 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2 [share 20%, other issuers' devices] | 1 | 494 | 0.00% [—, —] | 0.00% | ×— | -2.63 | — | no | not applicable |

## issuer_2_with_observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_2_with_observer [share 20%, all records] | 1 | 209 | 1.44% [—, —] | 1.45% | ×0.99 | -6.22 | 0.012 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_2_with_observer [share 20%, all records] | 1 | 209 | 2.87% [—, —] | 1.45% | ×1.98 | -4.78 | 0.170 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_2_with_observer [share 20%, all records] | 1 | 209 | 6.70% [—, —] | 1.45% | ×4.61 | -0.96 | 0.473 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_2_with_observer [share 20%, all records] | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.589 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 209 | 1.44% [—, —] | 1.45% | ×0.99 | -6.22 | 0.012 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 209 | 2.87% [—, —] | 1.45% | ×1.98 | -4.78 | 0.170 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 209 | 6.70% [—, —] | 1.45% | ×4.61 | -0.96 | 0.473 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.589 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2_with_observer [share 20%, all records] | 1 | 602 | 1.83% [—, —] | 0.74% | ×2.47 | -0.50 | 0.404 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2_with_observer [share 20%, all records] | 1 | 602 | 1.16% [—, —] | 0.74% | ×1.57 | -1.16 | 0.417 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2_with_observer [share 20%, all records] | 1 | 602 | 1.99% [—, —] | 0.74% | ×2.69 | -0.33 | 0.425 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2_with_observer [share 20%, all records] | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | +0.00 | 0.377 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2_with_observer [share 20%, its own devices] | 1 | 108 | 10.19% [—, —] | 0.74% | ×13.76 | +9.26 | 0.411 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2_with_observer [share 20%, its own devices] | 1 | 108 | 6.48% [—, —] | 0.74% | ×8.76 | +5.56 | 0.428 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2_with_observer [share 20%, its own devices] | 1 | 108 | 2.78% [—, —] | 0.74% | ×3.75 | +1.85 | 0.638 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2_with_observer [share 20%, its own devices] | 1 | 108 | 0.93% [—, —] | 0.74% | ×1.25 | +0.00 | 0.098 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 494 | 0.00% [—, —] | 0.74% | ×0.00 | -2.63 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 494 | 0.00% [—, —] | 0.74% | ×0.00 | -2.63 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 494 | 1.82% [—, —] | 0.74% | ×2.46 | -0.81 | 0.349 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2_with_observer [share 20%, other issuers' devices] | 1 | 494 | 2.63% [—, —] | 0.74% | ×3.55 | +0.00 | 0.388 | no | not applicable |

## issuer_2_with_first_relay

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 209 | 1.44% [—, —] | 1.45% | ×0.99 | -6.22 | 0.010 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 209 | 2.87% [—, —] | 1.45% | ×1.98 | -4.78 | 0.161 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.448 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.577 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 209 | 1.44% [—, —] | 1.45% | ×0.99 | -6.22 | 0.010 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 209 | 2.87% [—, —] | 1.45% | ×1.98 | -4.78 | 0.161 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.448 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | +0.00 | 0.577 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 602 | 1.99% [—, —] | 0.74% | ×2.69 | -0.33 | 0.406 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 602 | 1.00% [—, —] | 0.74% | ×1.35 | -1.33 | 0.459 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 602 | 2.66% [—, —] | 0.74% | ×3.59 | +0.33 | 0.427 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2_with_first_relay [share 20%, all records] | 1 | 602 | 2.99% [—, —] | 0.74% | ×4.04 | +0.66 | 0.427 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2_with_first_relay [share 20%, its own devices] | 1 | 108 | 10.19% [—, —] | 0.74% | ×13.76 | +9.26 | 0.454 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2_with_first_relay [share 20%, its own devices] | 1 | 108 | 5.56% [—, —] | 0.74% | ×7.51 | +4.63 | 0.470 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2_with_first_relay [share 20%, its own devices] | 1 | 108 | 3.70% [—, —] | 0.74% | ×5.00 | +2.78 | 0.589 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2_with_first_relay [share 20%, its own devices] | 1 | 108 | 1.85% [—, —] | 0.74% | ×2.50 | +0.93 | 0.396 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 494 | 0.20% [—, —] | 0.74% | ×0.27 | -2.43 | 0.007 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 494 | 0.00% [—, —] | 0.74% | ×0.00 | -2.63 | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 494 | 2.43% [—, —] | 0.74% | ×3.28 | -0.20 | 0.369 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2_with_first_relay [share 20%, other issuers' devices] | 1 | 494 | 3.24% [—, —] | 0.74% | ×4.37 | +0.61 | 0.424 | no | not applicable |

## issuer_0_with_destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_0_with_destination | 1 | 346 | 4.05% [—, —] | 1.65% | ×2.46 | +2.31 | 0.474 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_0_with_destination | 1 | 346 | 4.05% [—, —] | 1.64% | ×2.47 | +2.31 | 0.381 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_0_with_destination | 1 | 346 | 4.05% [—, —] | 1.64% | ×2.47 | +2.31 | 0.429 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_0_with_destination | 1 | 346 | 3.47% [—, —] | 1.64% | ×2.12 | +1.73 | 0.525 | no | not applicable |

## issuer_2_with_destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | issuer_2_with_destination | 1 | 108 | 8.33% [—, —] | 3.85% | ×2.16 | +7.41 | 0.416 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | issuer_2_with_destination | 1 | 108 | 5.56% [—, —] | 3.84% | ×1.45 | +4.63 | 0.529 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | issuer_2_with_destination | 1 | 108 | 9.26% [—, —] | 3.84% | ×2.41 | +8.33 | 0.381 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | issuer_2_with_destination | 1 | 108 | 8.33% [—, —] | 3.84% | ×2.17 | +7.41 | 0.356 | no | not applicable |

## ceiling

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | ceiling | 1 | 209 | 8.61% [—, —] | 9.81% | ×0.88 | — | — | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | ceiling | 1 | 209 | 8.61% [—, —] | 9.81% | ×0.88 | — | — | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | ceiling | 1 | 209 | 8.61% [—, —] | 9.81% | ×0.88 | — | — | no | 10.50% |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | ceiling | 1 | 209 | 8.61% [—, —] | 9.81% | ×0.88 | — | — | no | 10.50% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | ceiling | 1 | 602 | 7.97% [—, —] | 4.96% | ×1.61 | — | — | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | ceiling | 1 | 602 | 7.97% [—, —] | 4.96% | ×1.61 | — | — | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | ceiling | 1 | 602 | 7.97% [—, —] | 4.96% | ×1.61 | — | — | no | 5.33% |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | ceiling | 1 | 602 | 7.97% [—, —] | 4.96% | ×1.61 | — | — | no | 5.33% |

## K records, K = 1

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | K records, K = 1 | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | — | 0.634 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | K records, K = 1 | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | — | 0.634 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | K records, K = 1 | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | — | 0.634 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | K records, K = 1 | 1 | 209 | 7.66% [—, —] | 1.45% | ×5.27 | — | 0.634 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | K records, K = 1 | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | — | 0.379 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | K records, K = 1 | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | — | 0.379 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | K records, K = 1 | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | — | 0.379 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | K records, K = 1 | 1 | 602 | 2.33% [—, —] | 0.74% | ×3.14 | — | 0.379 | no | not applicable |

## K records, K = 2

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | K records, K = 2 | 1 | 104 | 11.54% [—, —] | 1.89% | ×6.10 | — | 0.531 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | K records, K = 2 | 1 | 104 | 11.54% [—, —] | 1.89% | ×6.10 | — | 0.531 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | K records, K = 2 | 1 | 104 | 11.54% [—, —] | 1.89% | ×6.10 | — | 0.531 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | K records, K = 2 | 1 | 104 | 11.54% [—, —] | 1.89% | ×6.10 | — | 0.531 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | K records, K = 2 | 1 | 274 | 2.19% [—, —] | 0.96% | ×2.28 | — | 0.616 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | K records, K = 2 | 1 | 274 | 2.19% [—, —] | 0.96% | ×2.28 | — | 0.616 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | K records, K = 2 | 1 | 274 | 2.19% [—, —] | 0.96% | ×2.28 | — | 0.616 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | K records, K = 2 | 1 | 274 | 2.19% [—, —] | 0.96% | ×2.28 | — | 0.616 | no | not applicable |

## K records, K = 3

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | K records, K = 3 | 1 | 69 | 18.84% [—, —] | 2.44% | ×7.73 | — | 0.593 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | K records, K = 3 | 1 | 69 | 18.84% [—, —] | 2.44% | ×7.73 | — | 0.593 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | K records, K = 3 | 1 | 69 | 18.84% [—, —] | 2.44% | ×7.73 | — | 0.593 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | K records, K = 3 | 1 | 69 | 18.84% [—, —] | 2.44% | ×7.73 | — | 0.593 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | K records, K = 3 | 1 | 168 | 8.33% [—, —] | 1.25% | ×6.67 | — | 0.381 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | K records, K = 3 | 1 | 168 | 8.33% [—, —] | 1.25% | ×6.67 | — | 0.381 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | K records, K = 3 | 1 | 168 | 8.33% [—, —] | 1.25% | ×6.67 | — | 0.381 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | K records, K = 3 | 1 | 168 | 8.33% [—, —] | 1.25% | ×6.67 | — | 0.381 | no | not applicable |

## K records, K = 5

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | K records, K = 5 | 1 | 41 | 36.59% [—, —] | 3.92% | ×9.33 | — | 0.662 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | K records, K = 5 | 1 | 41 | 36.59% [—, —] | 3.92% | ×9.33 | — | 0.662 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | K records, K = 5 | 1 | 41 | 36.59% [—, —] | 3.92% | ×9.33 | — | 0.662 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | K records, K = 5 | 1 | 41 | 36.59% [—, —] | 3.92% | ×9.33 | — | 0.662 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 1 | 527 s | K records, K = 5 | 1 | 72 | 13.89% [—, —] | 2.12% | ×6.56 | — | 0.516 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 5 | 527 s | K records, K = 5 | 1 | 72 | 13.89% [—, —] | 2.12% | ×6.56 | — | 0.516 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 20 | 527 s | K records, K = 5 | 1 | 72 | 13.89% [—, —] | 2.12% | ×6.56 | — | 0.516 | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural, batch 100 | 527 s | K records, K = 5 | 1 | 72 | 13.89% [—, —] | 2.12% | ×6.56 | — | 0.516 | no | not applicable |

## K records, K = 10

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | K records, K = 10 | 1 | 20 | 85.00% [—, —] | 14.25% | ×5.97 | — | 0.882 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | K records, K = 10 | 1 | 20 | 85.00% [—, —] | 14.25% | ×5.97 | — | 0.882 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | K records, K = 10 | 1 | 20 | 85.00% [—, —] | 14.25% | ×5.97 | — | 0.882 | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | K records, K = 10 | 1 | 20 | 85.00% [—, —] | 14.25% | ×5.97 | — | 0.882 | no | not applicable |

## K records, K = 20

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural, batch 1 | 473 s | K records, K = 20 | 1 | 10 | 100.00% [—, —] | 61.67% | ×1.62 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 5 | 473 s | K records, K = 20 | 1 | 10 | 100.00% [—, —] | 61.67% | ×1.62 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 20 | 473 s | K records, K = 20 | 1 | 10 | 100.00% [—, —] | 61.67% | ×1.62 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural, batch 100 | 473 s | K records, K = 20 | 1 | 10 | 100.00% [—, —] | 61.67% | ×1.62 | — | — | no | not applicable |

## destination that delays: observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | delay1800 | credential path | — | observer [all records] | 1 | 212 | 2.83% [—, —] | 1.09% | ×2.59 | +0.00 | 0.398 | no | 10.50% |
| R1 | delay1800 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 212 | 4.72% [—, —] | 1.44% | ×3.27 | +0.00 | 0.660 | no | 10.50% |
| R1 | delay1800 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 213 | 4.69% [—, —] | 1.46% | ×3.22 | +0.00 | 0.442 | no | 10.50% |
| R1 | delay1800 | credential path | — | observer [other records] | 1 | 181 | 3.31% [—, —] | 1.11% | ×3.00 | +0.00 | 0.403 | no | not applicable |
| R1 | delay1800 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 203 | 4.93% [—, —] | 1.45% | ×3.39 | +0.00 | 0.662 | no | not applicable |
| R1 | delay1800 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 204 | 4.90% [—, —] | 1.46% | ×3.35 | +0.00 | 0.446 | no | not applicable |
| R1 | delay1800 | credential path | — | observer [records the node delayed] | 1 | 31 | 0.00% [—, —] | 1.02% | ×0.00 | +0.00 | — | no | not applicable |
| R1 | delay1800 | blind-issued one-time certificates, natural | — | observer [records the node delayed] | 1 | 9 | 0.00% [—, —] | 1.15% | ×0.00 | +0.00 | — | no | not applicable |
| R1 | delay1800 | blind-issued one-time certificates, lengthened hold | — | observer [records the node delayed] | 1 | 9 | 0.00% [—, —] | 1.32% | ×0.00 | +0.00 | — | no | not applicable |
| R1 | delay600 | credential path | — | observer [all records] | 1 | 212 | 3.77% [—, —] | 1.11% | ×3.41 | +0.00 | 0.375 | no | 10.50% |
| R1 | delay600 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 212 | 4.72% [—, —] | 1.45% | ×3.26 | +0.00 | 0.654 | no | 10.50% |
| R1 | delay600 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 213 | 4.69% [—, —] | 1.46% | ×3.21 | +0.00 | 0.444 | no | 10.50% |
| R1 | delay600 | credential path | — | observer [other records] | 1 | 181 | 3.31% [—, —] | 1.11% | ×3.00 | +0.00 | 0.403 | no | not applicable |
| R1 | delay600 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 203 | 4.93% [—, —] | 1.45% | ×3.39 | +0.00 | 0.662 | no | not applicable |
| R1 | delay600 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 204 | 4.90% [—, —] | 1.46% | ×3.35 | +0.00 | 0.446 | no | not applicable |
| R1 | delay600 | credential path | — | observer [records the node delayed] | 1 | 31 | 6.45% [—, —] | 1.11% | ×5.79 | +0.00 | 0.259 | no | not applicable |
| R1 | delay600 | blind-issued one-time certificates, natural | — | observer [records the node delayed] | 1 | 9 | 0.00% [—, —] | 1.25% | ×0.00 | +0.00 | — | no | not applicable |
| R1 | delay600 | blind-issued one-time certificates, lengthened hold | — | observer [records the node delayed] | 1 | 9 | 0.00% [—, —] | 1.51% | ×0.00 | +0.00 | — | no | not applicable |
| R100 | delay1800 | credential path | — | observer [all records] | 1 | 20,595 | 2.44% [—, —] | 0.55% | ×4.47 | +0.00 | 0.546 | yes | 5.33% |
| R100 | delay1800 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 20,586 | 2.76% [—, —] | 0.72% | ×3.83 | +0.00 | 0.551 | yes | 5.33% |
| R100 | delay1800 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 20,596 | 2.98% [—, —] | 0.72% | ×4.12 | +0.00 | 0.567 | yes | 5.33% |
| R100 | delay1800 | credential path | — | observer [other records] | 1 | 18,202 | 2.68% [—, —] | 0.55% | ×4.87 | +0.00 | 0.548 | yes | not applicable |
| R100 | delay1800 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 19,506 | 2.89% [—, —] | 0.73% | ×3.94 | +0.00 | 0.552 | yes | not applicable |
| R100 | delay1800 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 19,522 | 3.12% [—, —] | 0.74% | ×4.23 | +0.00 | 0.567 | yes | not applicable |
| R100 | delay1800 | credential path | — | observer [records the node delayed] | 1 | 2,393 | 0.59% [—, —] | 0.50% | ×1.16 | +0.00 | 0.480 | no | not applicable |
| R100 | delay1800 | blind-issued one-time certificates, natural | — | observer [records the node delayed] | 1 | 1,080 | 0.46% [—, —] | 0.50% | ×0.92 | +0.00 | 0.524 | no | not applicable |
| R100 | delay1800 | blind-issued one-time certificates, lengthened hold | — | observer [records the node delayed] | 1 | 1,074 | 0.37% [—, —] | 0.47% | ×0.79 | +0.00 | 0.623 | no | not applicable |
| R100 | delay600 | credential path | — | observer [all records] | 1 | 20,595 | 2.57% [—, —] | 0.55% | ×4.66 | +0.00 | 0.551 | yes | 5.33% |
| R100 | delay600 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 20,586 | 2.76% [—, —] | 0.73% | ×3.78 | +0.00 | 0.550 | yes | 5.33% |
| R100 | delay600 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 20,596 | 3.02% [—, —] | 0.73% | ×4.11 | +0.00 | 0.565 | yes | 5.33% |
| R100 | delay600 | credential path | — | observer [other records] | 1 | 18,202 | 2.68% [—, —] | 0.55% | ×4.87 | +0.00 | 0.548 | yes | not applicable |
| R100 | delay600 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 19,506 | 2.89% [—, —] | 0.73% | ×3.94 | +0.00 | 0.552 | yes | not applicable |
| R100 | delay600 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 19,522 | 3.12% [—, —] | 0.74% | ×4.23 | +0.00 | 0.567 | yes | not applicable |
| R100 | delay600 | credential path | — | observer [records the node delayed] | 1 | 2,393 | 1.71% [—, —] | 0.55% | ×3.11 | +0.00 | 0.579 | no | not applicable |
| R100 | delay600 | blind-issued one-time certificates, natural | — | observer [records the node delayed] | 1 | 1,080 | 0.46% [—, —] | 0.68% | ×0.68 | +0.00 | 0.403 | no | not applicable |
| R100 | delay600 | blind-issued one-time certificates, lengthened hold | — | observer [records the node delayed] | 1 | 1,074 | 1.12% [—, —] | 0.68% | ×1.63 | +0.00 | 0.499 | no | not applicable |

## destination that delays: delaying_destination

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | delay1800 | credential path | — | delaying_destination | 1 | 31 | 9.68% [—, —] | 1.14% | ×8.47 | +9.68 | 0.667 | no | not applicable |
| R1 | delay1800 | blind-issued one-time certificates, natural | — | delaying_destination | 1 | 9 | 0.00% [—, —] | 1.56% | ×0.00 | +0.00 | — | no | not applicable |
| R1 | delay1800 | blind-issued one-time certificates, lengthened hold | — | delaying_destination | 1 | 9 | 11.11% [—, —] | 1.61% | ×6.92 | +11.11 | 0.750 | no | not applicable |
| R1 | delay600 | credential path | — | delaying_destination | 1 | 31 | 9.68% [—, —] | 1.14% | ×8.48 | +3.23 | 0.667 | no | not applicable |
| R1 | delay600 | blind-issued one-time certificates, natural | — | delaying_destination | 1 | 9 | 0.00% [—, —] | 1.56% | ×0.00 | +0.00 | — | no | not applicable |
| R1 | delay600 | blind-issued one-time certificates, lengthened hold | — | delaying_destination | 1 | 9 | 11.11% [—, —] | 1.61% | ×6.92 | +11.11 | 0.750 | no | not applicable |
| R100 | delay1800 | credential path | — | delaying_destination | 1 | 2,393 | 2.26% [—, —] | 0.56% | ×4.02 | +1.67 | 0.608 | yes | not applicable |
| R100 | delay1800 | blind-issued one-time certificates, natural | — | delaying_destination | 1 | 1,080 | 2.59% [—, —] | 0.81% | ×3.19 | +2.13 | 0.498 | no | not applicable |
| R100 | delay1800 | blind-issued one-time certificates, lengthened hold | — | delaying_destination | 1 | 1,074 | 2.70% [—, —] | 0.81% | ×3.32 | +2.33 | 0.545 | no | not applicable |
| R100 | delay600 | credential path | — | delaying_destination | 1 | 2,393 | 2.34% [—, —] | 0.56% | ×4.17 | +0.63 | 0.597 | yes | not applicable |
| R100 | delay600 | blind-issued one-time certificates, natural | — | delaying_destination | 1 | 1,080 | 2.59% [—, —] | 0.81% | ×3.19 | +2.13 | 0.498 | no | not applicable |
| R100 | delay600 | blind-issued one-time certificates, lengthened hold | — | delaying_destination | 1 | 1,074 | 2.70% [—, —] | 0.81% | ×3.32 | +1.58 | 0.545 | no | not applicable |

## destination that drops: observer

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | drop_m1800 | credential path | — | observer [all records] | 1 | 212 | 3.30% [—, —] | 1.07% | ×3.08 | +0.00 | 0.758 | no | 10.50% |
| R1 | drop_m1800 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 212 | 6.13% [—, —] | 1.42% | ×4.33 | +0.00 | 0.698 | no | 10.50% |
| R1 | drop_m1800 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 213 | 5.16% [—, —] | 1.42% | ×3.63 | +0.00 | 0.423 | no | 10.50% |
| R1 | drop_m1800 | credential path | — | observer [other records] | 1 | 212 | 3.30% [—, —] | 1.07% | ×3.08 | +0.00 | 0.758 | no | not applicable |
| R1 | drop_m1800 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 212 | 6.13% [—, —] | 1.42% | ×4.33 | +0.00 | 0.698 | no | not applicable |
| R1 | drop_m1800 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 213 | 5.16% [—, —] | 1.42% | ×3.63 | +0.00 | 0.423 | no | not applicable |
| R1 | drop_m21600 | credential path | — | observer [all records] | 1 | 220 | 5.45% [—, —] | 1.08% | ×5.06 | +0.00 | 0.567 | no | 10.50% |
| R1 | drop_m21600 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 218 | 7.80% [—, —] | 1.43% | ×5.46 | +0.00 | 0.685 | no | 10.50% |
| R1 | drop_m21600 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 221 | 6.33% [—, —] | 1.44% | ×4.40 | +0.00 | 0.514 | no | 10.50% |
| R1 | drop_m21600 | credential path | — | observer [other records] | 1 | 220 | 5.45% [—, —] | 1.08% | ×5.06 | +0.00 | 0.567 | no | not applicable |
| R1 | drop_m21600 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 218 | 7.80% [—, —] | 1.43% | ×5.46 | +0.00 | 0.685 | no | not applicable |
| R1 | drop_m21600 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 221 | 6.33% [—, —] | 1.44% | ×4.40 | +0.00 | 0.514 | no | not applicable |
| R1 | drop_m3600 | credential path | — | observer [all records] | 1 | 216 | 2.31% [—, —] | 1.07% | ×2.15 | +0.00 | 0.460 | no | 10.50% |
| R1 | drop_m3600 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 216 | 5.09% [—, —] | 1.41% | ×3.60 | +0.00 | 0.613 | no | 10.50% |
| R1 | drop_m3600 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 215 | 7.44% [—, —] | 1.42% | ×5.26 | +0.00 | 0.662 | no | 10.50% |
| R1 | drop_m3600 | credential path | — | observer [other records] | 1 | 216 | 2.31% [—, —] | 1.07% | ×2.15 | +0.00 | 0.460 | no | not applicable |
| R1 | drop_m3600 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 216 | 5.09% [—, —] | 1.41% | ×3.60 | +0.00 | 0.613 | no | not applicable |
| R1 | drop_m3600 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 215 | 7.44% [—, —] | 1.42% | ×5.26 | +0.00 | 0.662 | no | not applicable |
| R1 | drop_m7200 | credential path | — | observer [all records] | 1 | 220 | 4.09% [—, —] | 1.08% | ×3.80 | +0.00 | 0.715 | no | 10.50% |
| R1 | drop_m7200 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 220 | 4.55% [—, —] | 1.42% | ×3.20 | +0.00 | 0.624 | no | 10.50% |
| R1 | drop_m7200 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 221 | 6.79% [—, —] | 1.44% | ×4.72 | +0.00 | 0.549 | no | 10.50% |
| R1 | drop_m7200 | credential path | — | observer [other records] | 1 | 220 | 4.09% [—, —] | 1.08% | ×3.80 | +0.00 | 0.715 | no | not applicable |
| R1 | drop_m7200 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 220 | 4.55% [—, —] | 1.42% | ×3.20 | +0.00 | 0.624 | no | not applicable |
| R1 | drop_m7200 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 221 | 6.79% [—, —] | 1.44% | ×4.72 | +0.00 | 0.549 | no | not applicable |
| R100 | drop_m1800 | credential path | — | observer [all records] | 1 | 20,572 | 2.57% [—, —] | 0.53% | ×4.82 | +0.00 | 0.554 | yes | 5.33% |
| R100 | drop_m1800 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 20,580 | 2.82% [—, —] | 0.71% | ×3.96 | +0.00 | 0.545 | yes | 5.33% |
| R100 | drop_m1800 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 20,579 | 3.12% [—, —] | 0.72% | ×4.36 | +0.00 | 0.569 | yes | 5.33% |
| R100 | drop_m1800 | credential path | — | observer [other records] | 1 | 20,572 | 2.57% [—, —] | 0.53% | ×4.82 | +0.00 | 0.554 | yes | not applicable |
| R100 | drop_m1800 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 20,580 | 2.82% [—, —] | 0.71% | ×3.96 | +0.00 | 0.545 | yes | not applicable |
| R100 | drop_m1800 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 20,579 | 3.12% [—, —] | 0.72% | ×4.36 | +0.00 | 0.569 | yes | not applicable |
| R100 | drop_m21600 | credential path | — | observer [all records] | 1 | 20,389 | 2.34% [—, —] | 0.53% | ×4.39 | +0.00 | 0.546 | yes | 5.33% |
| R100 | drop_m21600 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 20,539 | 2.78% [—, —] | 0.71% | ×3.89 | +0.00 | 0.526 | yes | 5.33% |
| R100 | drop_m21600 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 20,526 | 2.63% [—, —] | 0.72% | ×3.66 | +0.00 | 0.540 | yes | 5.33% |
| R100 | drop_m21600 | credential path | — | observer [other records] | 1 | 20,389 | 2.34% [—, —] | 0.53% | ×4.39 | +0.00 | 0.546 | yes | not applicable |
| R100 | drop_m21600 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 20,539 | 2.78% [—, —] | 0.71% | ×3.89 | +0.00 | 0.526 | yes | not applicable |
| R100 | drop_m21600 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 20,526 | 2.63% [—, —] | 0.72% | ×3.66 | +0.00 | 0.540 | yes | not applicable |
| R100 | drop_m3600 | credential path | — | observer [all records] | 1 | 20,588 | 2.58% [—, —] | 0.53% | ×4.85 | +0.00 | 0.550 | yes | 5.33% |
| R100 | drop_m3600 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 20,600 | 2.69% [—, —] | 0.71% | ×3.77 | +0.00 | 0.559 | yes | 5.33% |
| R100 | drop_m3600 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 20,602 | 3.07% [—, —] | 0.72% | ×4.28 | +0.00 | 0.539 | yes | 5.33% |
| R100 | drop_m3600 | credential path | — | observer [other records] | 1 | 20,588 | 2.58% [—, —] | 0.53% | ×4.85 | +0.00 | 0.550 | yes | not applicable |
| R100 | drop_m3600 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 20,600 | 2.69% [—, —] | 0.71% | ×3.77 | +0.00 | 0.559 | yes | not applicable |
| R100 | drop_m3600 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 20,602 | 3.07% [—, —] | 0.72% | ×4.28 | +0.00 | 0.539 | yes | not applicable |
| R100 | drop_m7200 | credential path | — | observer [all records] | 1 | 20,544 | 2.51% [—, —] | 0.53% | ×4.70 | +0.00 | 0.558 | yes | 5.33% |
| R100 | drop_m7200 | blind-issued one-time certificates, natural | — | observer [all records] | 1 | 20,583 | 2.93% [—, —] | 0.71% | ×4.12 | +0.00 | 0.539 | yes | 5.33% |
| R100 | drop_m7200 | blind-issued one-time certificates, lengthened hold | — | observer [all records] | 1 | 20,604 | 3.05% [—, —] | 0.72% | ×4.26 | +0.00 | 0.560 | yes | 5.33% |
| R100 | drop_m7200 | credential path | — | observer [other records] | 1 | 20,544 | 2.51% [—, —] | 0.53% | ×4.70 | +0.00 | 0.558 | yes | not applicable |
| R100 | drop_m7200 | blind-issued one-time certificates, natural | — | observer [other records] | 1 | 20,583 | 2.93% [—, —] | 0.71% | ×4.12 | +0.00 | 0.539 | yes | not applicable |
| R100 | drop_m7200 | blind-issued one-time certificates, lengthened hold | — | observer [other records] | 1 | 20,604 | 3.05% [—, —] | 0.72% | ×4.26 | +0.00 | 0.560 | yes | not applicable |

## destination that drops: drop_link

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | drop_m1800 | credential path | — | drop_link | 1 | 31 | 6.45% [—, —] | 1.16% | ×5.56 | +3.23 | 1.000 | no | not applicable |
| R1 | drop_m1800 | blind-issued one-time certificates, natural | — | drop_link | 1 | 9 | 0.00% [—, —] | 2.23% | ×0.00 | -11.11 | — | no | not applicable |
| R1 | drop_m1800 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 9 | 11.11% [—, —] | 2.28% | ×4.88 | +11.11 | 0.875 | no | not applicable |
| R1 | drop_m21600 | credential path | — | drop_link | 1 | 17 | 11.76% [—, —] | 1.16% | ×10.14 | +0.00 | 0.433 | no | not applicable |
| R1 | drop_m21600 | blind-issued one-time certificates, natural | — | drop_link | 1 | 10 | 10.00% [—, —] | 2.22% | ×4.51 | +0.00 | 0.111 | no | not applicable |
| R1 | drop_m21600 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 10 | 10.00% [—, —] | 2.22% | ×4.50 | +10.00 | 1.000 | no | not applicable |
| R1 | drop_m3600 | credential path | — | drop_link | 1 | 27 | 3.70% [—, —] | 1.14% | ×3.24 | +3.70 | 0.154 | no | not applicable |
| R1 | drop_m3600 | blind-issued one-time certificates, natural | — | drop_link | 1 | 9 | 0.00% [—, —] | 2.26% | ×0.00 | +0.00 | — | no | not applicable |
| R1 | drop_m3600 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 9 | 22.22% [—, —] | 2.48% | ×8.97 | +22.22 | 0.643 | no | not applicable |
| R1 | drop_m7200 | credential path | — | drop_link | 1 | 18 | 5.56% [—, —] | 1.16% | ×4.81 | +5.56 | 0.471 | no | not applicable |
| R1 | drop_m7200 | blind-issued one-time certificates, natural | — | drop_link | 1 | 10 | 10.00% [—, —] | 2.16% | ×4.64 | +10.00 | 0.889 | no | not applicable |
| R1 | drop_m7200 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 10 | 20.00% [—, —] | 2.42% | ×8.26 | +20.00 | 0.125 | no | not applicable |
| R100 | drop_m1800 | credential path | — | drop_link | 1 | 2,347 | 6.05% [—, —] | 0.57% | ×10.54 | +3.58 | 0.603 | yes | not applicable |
| R100 | drop_m1800 | blind-issued one-time certificates, natural | — | drop_link | 1 | 1,065 | 8.08% [—, —] | 1.15% | ×6.99 | +5.35 | 0.599 | yes | not applicable |
| R100 | drop_m1800 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 1,050 | 6.76% [—, —] | 1.16% | ×5.83 | +4.48 | 0.615 | yes | not applicable |
| R100 | drop_m21600 | credential path | — | drop_link | 1 | 2,111 | 5.54% [—, —] | 0.58% | ×9.62 | +3.08 | 0.586 | yes | not applicable |
| R100 | drop_m21600 | blind-issued one-time certificates, natural | — | drop_link | 1 | 938 | 6.72% [—, —] | 1.16% | ×5.79 | +3.62 | 0.605 | yes | not applicable |
| R100 | drop_m21600 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 932 | 8.80% [—, —] | 1.17% | ×7.53 | +5.90 | 0.564 | yes | not applicable |
| R100 | drop_m3600 | credential path | — | drop_link | 1 | 2,347 | 5.45% [—, —] | 0.57% | ×9.51 | +2.68 | 0.637 | yes | not applicable |
| R100 | drop_m3600 | blind-issued one-time certificates, natural | — | drop_link | 1 | 1,055 | 8.06% [—, —] | 1.15% | ×6.99 | +5.12 | 0.578 | yes | not applicable |
| R100 | drop_m3600 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 1,053 | 6.55% [—, —] | 1.16% | ×5.63 | +3.13 | 0.602 | yes | not applicable |
| R100 | drop_m7200 | credential path | — | drop_link | 1 | 2,289 | 6.42% [—, —] | 0.58% | ×11.16 | +3.76 | 0.597 | yes | not applicable |
| R100 | drop_m7200 | blind-issued one-time certificates, natural | — | drop_link | 1 | 1,058 | 7.75% [—, —] | 1.16% | ×6.70 | +4.06 | 0.597 | yes | not applicable |
| R100 | drop_m7200 | blind-issued one-time certificates, lengthened hold | — | drop_link | 1 | 1,052 | 8.17% [—, —] | 1.17% | ×7.01 | +4.66 | 0.623 | yes | not applicable |

## issuer withholding or delaying refills

| Cell | Workload | Candidate | Latency | Vantage | Runs | Decisions | Device named [95% CI] | Chance | Multiple | Lead over observer | AUC | Stable | Bound |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L1440 | 1 | 11 | 0.00% [—, —] | 0.87% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L360 | 1 | 8 | 0.00% [—, —] | 0.83% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L720 | 1 | 10 | 0.00% [—, —] | 0.84% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L1440 | 1 | 11 | 0.00% [—, —] | 0.86% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L360 | 1 | 8 | 0.00% [—, —] | 0.83% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L720 | 1 | 10 | 0.00% [—, —] | 0.85% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L1440 | 1 | 11 | 0.00% [—, —] | 0.87% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L360 | 1 | 8 | 0.00% [—, —] | 0.83% | ×0.00 | — | — | no | not applicable |
| R1 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L720 | 1 | 10 | 0.00% [—, —] | 0.84% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L1440 | 1 | 8 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L360 | 1 | 7 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_delay_L720 | 1 | 10 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L1440 | 1 | 8 | 0.00% [—, —] | 0.44% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L360 | 1 | 7 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_none_L720 | 1 | 10 | 0.00% [—, —] | 0.44% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L1440 | 1 | 8 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L360 | 1 | 7 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |
| R100 | W0 | blind-issued one-time certificates, natural | — | iwh_withhold_L720 | 1 | 10 | 0.00% [—, —] | 0.45% | ×0.00 | — | — | no | not applicable |

## Spread of the posterior and calibration

Entropy and min-entropy in bits at the calibrated temperature; the effective anonymity set is 2 to the entropy. Devices: the naming rate over true devices with at least 10 records (median, 90th percentile, and the worst-off device with its records). Sampling: the calibration error a perfectly calibrated attacker would reach at the 99th percentile by sampling alone, at the same confidences. Flag: the calibration error is above that and exceeds both 2 points and a quarter of the larger of the accuracy and the mean confidence.

| File | Vantage | Entropy | Effective set | Min-entropy | Top-1 | Top-5 | Top-10 | Devices: median, p90, worst (records) | Calibration error | Sampling | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| c6__otcB100_W0__R1 | observer | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.40% |  |
| c6__otcB100_W0__R1 | first_hop | 5.65 | 50.3 | 4.26 | 7.70% | 22.22% | 37.54% | 7.70%, 7.70%, 7.70% (4180) | 3.82% | 1.29% | badly miscalibrated |
| c6__otcB100_W0__R1 | destination | 5.54 | 46.8 | 4.17 | 9.09% | 22.97% | 33.97% | 9.09%, 9.09%, 9.09% (209) | 6.75% | 6.91% |  |
| c6__otcB100_W0__R1 | destination_keyed | 3.83 | 14.4 | 2.77 | 19.14% | 55.02% | 84.69% | 19.14%, 19.14%, 19.14% (209) | 6.04% | 9.46% |  |
| c6__otcB100_W0__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (209) | 0.00% | 0.00% |  |
| c6__otcB100_W0__R1 | issuer_0 [share 50%, all records] | 5.52 | 45.8 | 4.89 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 3.51% | 5.39% |  |
| c6__otcB100_W0__R1 | issuer_0 [share 50%, other issuers' devices] | 5.52 | 45.8 | 4.89 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 3.51% | 5.39% |  |
| c6__otcB100_W0__R1 | issuer_0_with_observer [share 50%, all records] | 5.64 | 50.1 | 4.18 | 6.70% | 21.53% | 36.36% | 6.70%, 6.70%, 6.70% (209) | 4.76% | 6.48% |  |
| c6__otcB100_W0__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.64 | 50.1 | 4.18 | 6.70% | 21.53% | 36.36% | 6.70%, 6.70%, 6.70% (209) | 4.76% | 6.48% |  |
| c6__otcB100_W0__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.64 | 49.9 | 4.18 | 6.70% | 21.05% | 35.89% | 6.70%, 6.70%, 6.70% (209) | 4.80% | 6.10% |  |
| c6__otcB100_W0__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.64 | 49.9 | 4.18 | 6.70% | 21.05% | 35.89% | 6.70%, 6.70%, 6.70% (209) | 4.80% | 6.10% |  |
| c6__otcB100_W0__R1 | issuer_1 [share 30%, all records] | 4.89 | 29.6 | 4.21 | 1.44% | 100.00% | 100.00% | 1.44%, 1.44%, 1.44% (209) | 4.18% | 5.99% |  |
| c6__otcB100_W0__R1 | issuer_1 [share 30%, its own devices] | 4.89 | 29.6 | 4.21 | 1.44% | 100.00% | 100.00% | 1.44%, 1.44%, 1.44% (209) | 4.18% | 5.99% |  |
| c6__otcB100_W0__R1 | issuer_1_with_observer [share 30%, all records] | 5.64 | 50.2 | 4.22 | 8.13% | 22.01% | 38.28% | 8.13%, 8.13%, 8.13% (209) | 6.20% | 6.71% |  |
| c6__otcB100_W0__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.64 | 50.2 | 4.22 | 8.13% | 22.01% | 38.28% | 8.13%, 8.13%, 8.13% (209) | 6.20% | 6.71% |  |
| c6__otcB100_W0__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.64 | 50.0 | 4.22 | 8.13% | 21.05% | 36.84% | 8.13%, 8.13%, 8.13% (209) | 5.31% | 6.55% |  |
| c6__otcB100_W0__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.64 | 50.0 | 4.22 | 8.13% | 21.05% | 36.84% | 8.13%, 8.13%, 8.13% (209) | 5.31% | 6.55% |  |
| c6__otcB100_W0__R1 | issuer_1_with_destination | 3.81 | 14.2 | 2.67 | 18.18% | 54.07% | 85.17% | 18.18%, 18.18%, 18.18% (209) | 8.23% | 10.09% |  |
| c6__otcB100_W0__R1 | issuer_2 [share 20%, all records] | 4.55 | 23.5 | 3.96 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 6.58% | 6.64% |  |
| c6__otcB100_W0__R1 | issuer_2 [share 20%, other issuers' devices] | 4.55 | 23.5 | 3.96 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 6.58% | 6.64% |  |
| c6__otcB100_W0__R1 | issuer_2_with_observer [share 20%, all records] | 5.64 | 50.2 | 4.21 | 7.66% | 22.49% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 6.66% | 6.05% | badly miscalibrated |
| c6__otcB100_W0__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.64 | 50.2 | 4.21 | 7.66% | 22.49% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 6.66% | 6.05% | badly miscalibrated |
| c6__otcB100_W0__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.64 | 50.0 | 4.21 | 7.66% | 22.01% | 36.84% | 7.66%, 7.66%, 7.66% (209) | 5.80% | 6.63% |  |
| c6__otcB100_W0__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.64 | 50.0 | 4.21 | 7.66% | 22.01% | 36.84% | 7.66%, 7.66%, 7.66% (209) | 5.80% | 6.63% |  |
| c6__otcB100_W0__R100 | observer | 6.61 | 98.0 | 5.08 | 2.33% | 12.46% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.96% |  |
| c6__otcB100_W0__R100 | first_hop | 6.61 | 97.6 | 5.07 | 2.40% | 12.62% | 22.69% | 0.00%, 3.54%, 33.33% (120) | 1.71% | 0.57% |  |
| c6__otcB100_W0__R100 | destination | 6.48 | 89.5 | 4.96 | 1.33% | 11.79% | 21.59% | 0.00%, 2.73%, 9.09% (11) | 1.94% | 2.65% |  |
| c6__otcB100_W0__R100 | destination_keyed | 5.07 | 35.8 | 3.80 | 6.15% | 26.58% | 46.35% | 13.33%, 18.18%, 18.18% (11) | 2.31% | 4.33% |  |
| c6__otcB100_W0__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (11) | 0.00% | 0.00% |  |
| c6__otcB100_W0__R100 | issuer_0 [share 50%, all records] | 3.46 | 11.0 | 3.35 | 3.99% | 8.14% | 8.14% | 0.00%, 0.00%, 0.00% (11) | 8.65% | 5.20% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_0 [share 50%, its own devices] | 3.46 | 11.0 | 3.36 | 6.94% | 14.16% | 14.16% | 0.00%, 0.00%, 0.00% (11) | 7.75% | 6.67% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_0 [share 50%, other issuers' devices] | 3.46 | 11.0 | 3.34 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 9.88% | 7.80% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_0_with_observer [share 50%, all records] | 6.61 | 97.9 | 5.08 | 2.16% | 12.62% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 1.99% | 3.10% |  |
| c6__otcB100_W0__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.61 | 97.7 | 5.07 | 1.73% | 12.14% | 23.41% | 0.00%, 10.91%, 18.18% (11) | 3.06% | 3.66% |  |
| c6__otcB100_W0__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.62 | 98.2 | 5.09 | 2.73% | 13.28% | 21.88% | 0.00%, 7.27%, 9.09% (11) | 1.74% | 4.38% |  |
| c6__otcB100_W0__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.61 | 97.5 | 5.06 | 2.66% | 12.46% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 3.01% | 3.09% |  |
| c6__otcB100_W0__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.60 | 97.4 | 5.05 | 2.60% | 11.85% | 22.83% | 0.00%, 10.91%, 18.18% (11) | 3.36% | 3.59% |  |
| c6__otcB100_W0__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.61 | 97.8 | 5.08 | 2.73% | 13.28% | 22.66% | 0.00%, 7.27%, 9.09% (11) | 1.67% | 4.14% |  |
| c6__otcB100_W0__R100 | issuer_0_with_destination | 5.49 | 45.2 | 4.15 | 3.47% | 21.39% | 37.28% | 9.09%, 14.91%, 18.18% (11) | 2.95% | 4.92% |  |
| c6__otcB100_W0__R100 | issuer_1 [share 30%, all records] | 1.00 | 2.0 | 0.98 | 1.00% | 1.00% | 1.00% | 0.00%, 0.00%, 0.00% (11) | 50.28% | 7.94% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_1 [share 30%, its own devices] | 1.00 | 2.0 | 0.98 | 4.05% | 4.05% | 4.05% | 0.00%, 0.00%, 0.00% (11) | 49.38% | 16.32% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_1 [share 30%, other issuers' devices] | 1.00 | 2.0 | 0.98 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 50.57% | 9.34% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_1_with_observer [share 30%, all records] | 6.61 | 97.9 | 5.08 | 2.33% | 12.46% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.99% |  |
| c6__otcB100_W0__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.61 | 98.0 | 5.09 | 4.73% | 15.54% | 25.00% | 4.55%, 8.18%, 9.09% (11) | 4.20% | 5.57% |  |
| c6__otcB100_W0__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.61 | 97.9 | 5.08 | 1.54% | 11.45% | 22.03% | 0.00%, 9.09%, 18.18% (11) | 2.42% | 3.49% |  |
| c6__otcB100_W0__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.61 | 97.6 | 5.07 | 2.82% | 12.46% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 3.22% | 2.95% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.61 | 97.7 | 5.07 | 4.73% | 16.22% | 25.00% | 4.55%, 8.18%, 9.09% (11) | 4.10% | 5.80% |  |
| c6__otcB100_W0__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.61 | 97.6 | 5.07 | 2.20% | 11.23% | 22.03% | 0.00%, 9.09%, 18.18% (11) | 2.49% | 3.07% |  |
| c6__otcB100_W0__R100 | issuer_1_with_destination | 4.67 | 25.7 | 3.45 | 10.81% | 34.46% | 58.11% | 18.18%, 18.18%, 18.18% (11) | 8.89% | 10.65% |  |
| c6__otcB100_W0__R100 | issuer_2 [share 20%, all records] | 2.00 | 4.0 | 1.94 | 1.16% | 1.50% | 1.50% | 0.00%, 0.00%, 0.00% (11) | 24.96% | 7.14% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_2 [share 20%, its own devices] | 2.00 | 4.0 | 1.93 | 6.48% | 8.33% | 8.33% | 0.00%, 0.00%, 0.00% (12) | 20.18% | 15.99% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_2 [share 20%, other issuers' devices] | 2.00 | 4.0 | 1.94 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 26.11% | 7.47% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_2_with_observer [share 20%, all records] | 6.61 | 97.9 | 5.07 | 2.33% | 12.62% | 22.92% | 0.00%, 11.82%, 18.18% (11) | 1.99% | 2.97% |  |
| c6__otcB100_W0__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.62 | 98.5 | 5.11 | 0.93% | 11.11% | 18.52% | 0.00%, 0.00%, 0.00% (12) | 3.41% | 7.00% |  |
| c6__otcB100_W0__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.61 | 97.8 | 5.06 | 2.63% | 12.96% | 23.89% | 0.00%, 12.73%, 18.18% (11) | 2.76% | 2.85% |  |
| c6__otcB100_W0__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.61 | 97.5 | 5.06 | 2.99% | 12.62% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 2.55% | 2.76% |  |
| c6__otcB100_W0__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.61 | 98.0 | 5.10 | 1.85% | 10.19% | 19.44% | 0.00%, 0.00%, 0.00% (12) | 3.70% | 7.16% |  |
| c6__otcB100_W0__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.60 | 97.4 | 5.05 | 3.24% | 13.16% | 23.48% | 0.00%, 12.73%, 18.18% (11) | 3.02% | 2.84% | badly miscalibrated |
| c6__otcB100_W0__R100 | issuer_2_with_destination | 4.26 | 19.2 | 3.09 | 8.33% | 31.48% | 55.56% | 16.67%, 16.67%, 16.67% (12) | 5.80% | 12.50% |  |
| c6__otcB1_W0__R1 | observer | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.40% |  |
| c6__otcB1_W0__R1 | first_hop | 5.65 | 50.3 | 4.26 | 7.70% | 22.22% | 37.54% | 7.70%, 7.70%, 7.70% (4180) | 3.82% | 1.29% | badly miscalibrated |
| c6__otcB1_W0__R1 | destination | 5.54 | 46.8 | 4.17 | 9.09% | 22.97% | 33.97% | 9.09%, 9.09%, 9.09% (209) | 6.75% | 6.91% |  |
| c6__otcB1_W0__R1 | destination_keyed | 3.83 | 14.4 | 2.77 | 19.14% | 55.02% | 84.69% | 19.14%, 19.14%, 19.14% (209) | 6.04% | 9.46% |  |
| c6__otcB1_W0__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (209) | 0.00% | 0.00% |  |
| c6__otcB1_W0__R1 | issuer_0 [share 50%, all records] | 4.55 | 23.6 | 3.35 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 10.06% | 7.68% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_0 [share 50%, other issuers' devices] | 4.55 | 23.6 | 3.35 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 10.06% | 7.68% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_0_with_observer [share 50%, all records] | 5.09 | 34.4 | 3.00 | 0.00% | 0.96% | 13.88% | 0.00%, 0.00%, 0.00% (209) | 13.27% | 9.35% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.09 | 34.4 | 3.00 | 0.00% | 0.96% | 13.88% | 0.00%, 0.00%, 0.00% (209) | 13.27% | 9.35% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.09 | 34.4 | 3.00 | 0.00% | 0.96% | 12.92% | 0.00%, 0.00%, 0.00% (209) | 13.21% | 9.31% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.09 | 34.4 | 3.00 | 0.00% | 0.96% | 12.92% | 0.00%, 0.00%, 0.00% (209) | 13.21% | 9.31% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_1 [share 30%, all records] | 3.93 | 15.4 | 2.86 | 17.22% | 54.55% | 84.69% | 17.22%, 17.22%, 17.22% (209) | 5.28% | 9.56% |  |
| c6__otcB1_W0__R1 | issuer_1 [share 30%, its own devices] | 3.93 | 15.4 | 2.86 | 17.22% | 54.55% | 84.69% | 17.22%, 17.22%, 17.22% (209) | 5.28% | 9.56% |  |
| c6__otcB1_W0__R1 | issuer_1_with_observer [share 30%, all records] | 5.16 | 36.5 | 3.00 | 16.75% | 45.93% | 67.46% | 16.75%, 16.75%, 16.75% (209) | 5.61% | 9.18% |  |
| c6__otcB1_W0__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.16 | 36.5 | 3.00 | 16.75% | 45.93% | 67.46% | 16.75%, 16.75%, 16.75% (209) | 5.61% | 9.18% |  |
| c6__otcB1_W0__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.16 | 36.4 | 3.01 | 16.75% | 46.41% | 67.94% | 16.75%, 16.75%, 16.75% (209) | 6.53% | 9.13% |  |
| c6__otcB1_W0__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.16 | 36.4 | 3.01 | 16.75% | 46.41% | 67.94% | 16.75%, 16.75%, 16.75% (209) | 6.53% | 9.13% |  |
| c6__otcB1_W0__R1 | issuer_1_with_destination | 3.23 | 9.7 | 1.97 | 19.62% | 51.20% | 83.73% | 19.62%, 19.62%, 19.62% (209) | 9.31% | 12.15% |  |
| c6__otcB1_W0__R1 | issuer_2 [share 20%, all records] | 3.54 | 11.8 | 2.51 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 18.07% | 10.05% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_2 [share 20%, other issuers' devices] | 3.54 | 11.8 | 2.51 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 18.07% | 10.05% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_2_with_observer [share 20%, all records] | 5.25 | 38.7 | 3.06 | 1.44% | 11.00% | 26.32% | 1.44%, 1.44%, 1.44% (209) | 13.53% | 10.00% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.25 | 38.7 | 3.06 | 1.44% | 11.00% | 26.32% | 1.44%, 1.44%, 1.44% (209) | 13.53% | 10.00% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.24 | 38.6 | 3.06 | 1.44% | 10.53% | 25.36% | 1.44%, 1.44%, 1.44% (209) | 13.54% | 9.69% | badly miscalibrated |
| c6__otcB1_W0__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.24 | 38.6 | 3.06 | 1.44% | 10.53% | 25.36% | 1.44%, 1.44%, 1.44% (209) | 13.54% | 9.69% | badly miscalibrated |
| c6__otcB1_W0__R100 | observer | 6.61 | 98.0 | 5.08 | 2.33% | 12.46% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.96% |  |
| c6__otcB1_W0__R100 | first_hop | 6.61 | 97.6 | 5.07 | 2.40% | 12.62% | 22.69% | 0.00%, 3.54%, 33.33% (120) | 1.71% | 0.57% |  |
| c6__otcB1_W0__R100 | destination | 6.48 | 89.5 | 4.96 | 1.33% | 11.79% | 21.59% | 0.00%, 2.73%, 9.09% (11) | 1.94% | 2.65% |  |
| c6__otcB1_W0__R100 | destination_keyed | 5.07 | 35.8 | 3.80 | 6.15% | 26.58% | 46.35% | 13.33%, 18.18%, 18.18% (11) | 2.31% | 4.33% |  |
| c6__otcB1_W0__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (11) | 0.00% | 0.00% |  |
| c6__otcB1_W0__R100 | issuer_0 [share 50%, all records] | 5.64 | 49.9 | 4.30 | 3.49% | 13.29% | 21.26% | 4.55%, 12.45%, 18.18% (11) | 3.17% | 3.67% |  |
| c6__otcB1_W0__R100 | issuer_0 [share 50%, its own devices] | 5.63 | 49.7 | 4.28 | 6.07% | 23.12% | 36.99% | 10.00%, 14.91%, 18.18% (11) | 4.70% | 4.54% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_0 [share 50%, other issuers' devices] | 5.64 | 50.1 | 4.32 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 5.09% | 5.64% |  |
| c6__otcB1_W0__R100 | issuer_0_with_observer [share 50%, all records] | 6.01 | 65.0 | 3.77 | 3.99% | 12.62% | 20.27% | 0.00%, 12.45%, 18.18% (11) | 5.60% | 4.54% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.01 | 65.0 | 3.75 | 6.94% | 21.97% | 35.26% | 10.00%, 14.91%, 18.18% (11) | 5.23% | 5.65% |  |
| c6__otcB1_W0__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.01 | 65.1 | 3.79 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 7.53% | 6.28% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.01 | 64.8 | 3.77 | 3.82% | 12.79% | 20.10% | 0.00%, 12.45%, 18.18% (11) | 4.58% | 4.39% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.01 | 64.8 | 3.75 | 6.65% | 22.25% | 34.97% | 10.00%, 14.91%, 18.18% (11) | 6.11% | 5.63% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.01 | 64.9 | 3.79 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 7.56% | 6.35% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_0_with_destination | 4.88 | 29.7 | 3.17 | 4.05% | 21.68% | 39.02% | 0.00%, 14.91%, 18.18% (11) | 7.95% | 7.14% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_1 [share 30%, all records] | 4.78 | 27.7 | 3.53 | 2.49% | 9.14% | 14.29% | 0.00%, 5.45%, 18.18% (11) | 6.27% | 4.51% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_1 [share 30%, its own devices] | 4.79 | 27.9 | 3.54 | 10.14% | 37.16% | 58.11% | 9.09%, 16.36%, 18.18% (11) | 5.28% | 8.66% |  |
| c6__otcB1_W0__R100 | issuer_1 [share 30%, other issuers' devices] | 4.78 | 27.6 | 3.53 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 8.79% | 5.67% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_1_with_observer [share 30%, all records] | 6.18 | 73.0 | 3.73 | 2.66% | 7.97% | 15.61% | 0.00%, 2.73%, 9.09% (11) | 5.32% | 4.33% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.17 | 72.6 | 3.71 | 10.81% | 32.43% | 49.32% | 4.55%, 8.18%, 9.09% (11) | 4.47% | 8.71% |  |
| c6__otcB1_W0__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.18 | 73.2 | 3.74 | 0.00% | 0.00% | 4.63% | 0.00%, 0.00%, 0.00% (11) | 7.97% | 5.20% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.18 | 72.9 | 3.73 | 2.82% | 8.14% | 15.78% | 0.00%, 2.73%, 9.09% (11) | 5.13% | 4.89% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.17 | 72.4 | 3.71 | 11.49% | 33.11% | 50.00% | 4.55%, 8.18%, 9.09% (11) | 5.08% | 8.80% |  |
| c6__otcB1_W0__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.18 | 73.0 | 3.74 | 0.00% | 0.00% | 4.63% | 0.00%, 0.00%, 0.00% (11) | 7.93% | 5.01% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_1_with_destination | 4.11 | 17.6 | 2.60 | 10.81% | 34.46% | 53.38% | 4.55%, 8.18%, 9.09% (11) | 8.24% | 11.80% |  |
| c6__otcB1_W0__R100 | issuer_2 [share 20%, all records] | 4.38 | 20.9 | 3.16 | 1.99% | 6.31% | 9.47% | 0.00%, 5.00%, 16.67% (12) | 9.52% | 4.95% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_2 [share 20%, its own devices] | 4.40 | 21.3 | 3.24 | 11.11% | 35.19% | 52.78% | 16.67%, 16.67%, 16.67% (12) | 9.40% | 10.85% |  |
| c6__otcB1_W0__R100 | issuer_2 [share 20%, other issuers' devices] | 4.37 | 20.8 | 3.15 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 11.64% | 5.87% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_2_with_observer [share 20%, all records] | 6.26 | 77.1 | 3.75 | 1.83% | 8.31% | 17.44% | 0.00%, 2.50%, 8.33% (12) | 6.47% | 4.05% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.26 | 77.2 | 3.79 | 10.19% | 36.11% | 50.93% | 8.33%, 8.33%, 8.33% (12) | 6.30% | 11.06% |  |
| c6__otcB1_W0__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.26 | 77.1 | 3.74 | 0.00% | 2.23% | 10.12% | 0.00%, 0.00%, 0.00% (11) | 8.05% | 4.70% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.25 | 76.8 | 3.75 | 1.99% | 8.14% | 17.77% | 0.00%, 8.56%, 9.09% (11) | 6.65% | 4.43% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.25 | 76.8 | 3.78 | 10.19% | 34.26% | 50.93% | 8.33%, 8.33%, 8.33% (12) | 5.87% | 10.38% |  |
| c6__otcB1_W0__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.25 | 76.8 | 3.74 | 0.20% | 2.43% | 10.53% | 0.00%, 3.64%, 9.09% (11) | 7.87% | 4.63% | badly miscalibrated |
| c6__otcB1_W0__R100 | issuer_2_with_destination | 3.67 | 12.9 | 2.29 | 8.33% | 39.81% | 57.41% | 16.67%, 16.67%, 16.67% (12) | 15.25% | 16.09% |  |
| c6__otcB20_W0__R1 | observer | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.40% |  |
| c6__otcB20_W0__R1 | first_hop | 5.65 | 50.3 | 4.26 | 7.70% | 22.22% | 37.54% | 7.70%, 7.70%, 7.70% (4180) | 3.82% | 1.29% | badly miscalibrated |
| c6__otcB20_W0__R1 | destination | 5.54 | 46.8 | 4.17 | 9.09% | 22.97% | 33.97% | 9.09%, 9.09%, 9.09% (209) | 6.75% | 6.91% |  |
| c6__otcB20_W0__R1 | destination_keyed | 3.83 | 14.4 | 2.77 | 19.14% | 55.02% | 84.69% | 19.14%, 19.14%, 19.14% (209) | 6.04% | 9.46% |  |
| c6__otcB20_W0__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (209) | 0.00% | 0.00% |  |
| c6__otcB20_W0__R1 | issuer_0 [share 50%, all records] | 5.52 | 45.8 | 4.39 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 5.00% | 5.96% |  |
| c6__otcB20_W0__R1 | issuer_0 [share 50%, other issuers' devices] | 5.52 | 45.8 | 4.39 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 5.00% | 5.96% |  |
| c6__otcB20_W0__R1 | issuer_0_with_observer [share 50%, all records] | 5.59 | 48.3 | 3.88 | 3.35% | 20.57% | 34.93% | 3.35%, 3.35%, 3.35% (209) | 7.60% | 6.79% | badly miscalibrated |
| c6__otcB20_W0__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.59 | 48.3 | 3.88 | 3.35% | 20.57% | 34.93% | 3.35%, 3.35%, 3.35% (209) | 7.60% | 6.79% | badly miscalibrated |
| c6__otcB20_W0__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.58 | 48.2 | 3.88 | 3.35% | 19.62% | 35.41% | 3.35%, 3.35%, 3.35% (209) | 7.64% | 7.02% | badly miscalibrated |
| c6__otcB20_W0__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.58 | 48.2 | 3.88 | 3.35% | 19.62% | 35.41% | 3.35%, 3.35%, 3.35% (209) | 7.64% | 7.02% | badly miscalibrated |
| c6__otcB20_W0__R1 | issuer_1 [share 30%, all records] | 4.87 | 29.2 | 4.02 | 6.22% | 96.17% | 100.00% | 6.22%, 6.22%, 6.22% (209) | 5.01% | 6.61% |  |
| c6__otcB20_W0__R1 | issuer_1 [share 30%, its own devices] | 4.87 | 29.2 | 4.02 | 6.22% | 96.17% | 100.00% | 6.22%, 6.22%, 6.22% (209) | 5.01% | 6.61% |  |
| c6__otcB20_W0__R1 | issuer_1_with_observer [share 30%, all records] | 5.60 | 48.9 | 3.99 | 11.00% | 23.44% | 38.28% | 11.00%, 11.00%, 11.00% (209) | 6.49% | 6.55% |  |
| c6__otcB20_W0__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.60 | 48.9 | 3.99 | 11.00% | 23.44% | 38.28% | 11.00%, 11.00%, 11.00% (209) | 6.49% | 6.55% |  |
| c6__otcB20_W0__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.60 | 48.8 | 3.98 | 11.00% | 22.97% | 37.32% | 11.00%, 11.00%, 11.00% (209) | 7.40% | 6.83% | badly miscalibrated |
| c6__otcB20_W0__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.60 | 48.8 | 3.98 | 11.00% | 22.97% | 37.32% | 11.00%, 11.00%, 11.00% (209) | 7.40% | 6.83% | badly miscalibrated |
| c6__otcB20_W0__R1 | issuer_1_with_destination | 3.72 | 13.5 | 2.46 | 17.22% | 52.63% | 84.69% | 17.22%, 17.22%, 17.22% (209) | 8.57% | 10.00% |  |
| c6__otcB20_W0__R1 | issuer_2 [share 20%, all records] | 4.55 | 23.4 | 3.78 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 7.75% | 7.87% |  |
| c6__otcB20_W0__R1 | issuer_2 [share 20%, other issuers' devices] | 4.55 | 23.4 | 3.78 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 7.75% | 7.87% |  |
| c6__otcB20_W0__R1 | issuer_2_with_observer [share 20%, all records] | 5.62 | 49.4 | 4.05 | 6.70% | 20.57% | 37.32% | 6.70%, 6.70%, 6.70% (209) | 6.39% | 7.27% |  |
| c6__otcB20_W0__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.62 | 49.4 | 4.05 | 6.70% | 20.57% | 37.32% | 6.70%, 6.70%, 6.70% (209) | 6.39% | 7.27% |  |
| c6__otcB20_W0__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.62 | 49.2 | 4.05 | 7.66% | 20.10% | 36.36% | 7.66%, 7.66%, 7.66% (209) | 6.35% | 7.12% |  |
| c6__otcB20_W0__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.62 | 49.2 | 4.05 | 7.66% | 20.10% | 36.36% | 7.66%, 7.66%, 7.66% (209) | 6.35% | 7.12% |  |
| c6__otcB20_W0__R100 | observer | 6.61 | 98.0 | 5.08 | 2.33% | 12.46% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.96% |  |
| c6__otcB20_W0__R100 | first_hop | 6.61 | 97.6 | 5.07 | 2.40% | 12.62% | 22.69% | 0.00%, 3.54%, 33.33% (120) | 1.71% | 0.57% |  |
| c6__otcB20_W0__R100 | destination | 6.48 | 89.5 | 4.96 | 1.33% | 11.79% | 21.59% | 0.00%, 2.73%, 9.09% (11) | 1.94% | 2.65% |  |
| c6__otcB20_W0__R100 | destination_keyed | 5.07 | 35.8 | 3.80 | 6.15% | 26.58% | 46.35% | 13.33%, 18.18%, 18.18% (11) | 2.31% | 4.33% |  |
| c6__otcB20_W0__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (11) | 0.00% | 0.00% |  |
| c6__otcB20_W0__R100 | issuer_0 [share 50%, all records] | 5.81 | 56.2 | 4.90 | 1.83% | 13.95% | 36.54% | 0.00%, 2.73%, 9.09% (11) | 1.73% | 3.22% |  |
| c6__otcB20_W0__R100 | issuer_0 [share 50%, its own devices] | 5.81 | 56.2 | 4.90 | 3.18% | 24.28% | 63.58% | 0.00%, 5.45%, 9.09% (11) | 2.31% | 3.77% |  |
| c6__otcB20_W0__R100 | issuer_0 [share 50%, other issuers' devices] | 5.81 | 56.2 | 4.89 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 3.40% | 4.72% |  |
| c6__otcB20_W0__R100 | issuer_0_with_observer [share 50%, all records] | 6.58 | 95.9 | 4.86 | 1.83% | 11.63% | 22.09% | 0.00%, 11.82%, 18.18% (11) | 1.90% | 3.01% |  |
| c6__otcB20_W0__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.58 | 95.7 | 4.85 | 2.60% | 12.43% | 22.83% | 0.00%, 10.91%, 18.18% (11) | 1.65% | 3.93% |  |
| c6__otcB20_W0__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.59 | 96.2 | 4.86 | 0.78% | 10.55% | 21.09% | 0.00%, 7.27%, 9.09% (11) | 3.15% | 4.67% |  |
| c6__otcB20_W0__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.58 | 95.6 | 4.85 | 1.83% | 11.13% | 22.43% | 0.00%, 11.82%, 18.18% (11) | 2.51% | 2.96% |  |
| c6__otcB20_W0__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.57 | 95.4 | 4.84 | 2.60% | 11.85% | 23.70% | 0.00%, 10.91%, 18.18% (11) | 1.66% | 3.88% |  |
| c6__otcB20_W0__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.58 | 95.8 | 4.85 | 0.78% | 10.16% | 20.70% | 0.00%, 7.27%, 9.09% (11) | 3.77% | 4.68% |  |
| c6__otcB20_W0__R100 | issuer_0_with_destination | 5.44 | 43.5 | 3.87 | 4.05% | 20.52% | 35.55% | 0.00%, 9.64%, 10.00% (10) | 3.88% | 5.80% |  |
| c6__otcB20_W0__R100 | issuer_1 [share 30%, all records] | 4.68 | 25.6 | 3.93 | 0.66% | 10.30% | 10.63% | 0.00%, 2.73%, 9.09% (11) | 5.98% | 3.88% | badly miscalibrated |
| c6__otcB20_W0__R100 | issuer_1 [share 30%, its own devices] | 4.68 | 25.6 | 3.91 | 2.70% | 41.89% | 43.24% | 4.55%, 8.18%, 9.09% (11) | 5.33% | 8.03% |  |
| c6__otcB20_W0__R100 | issuer_1 [share 30%, other issuers' devices] | 4.68 | 25.6 | 3.94 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 6.61% | 4.66% | badly miscalibrated |
| c6__otcB20_W0__R100 | issuer_1_with_observer [share 30%, all records] | 6.60 | 97.0 | 4.96 | 2.16% | 12.62% | 22.92% | 0.00%, 11.82%, 18.18% (11) | 2.54% | 2.89% |  |
| c6__otcB20_W0__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.60 | 97.1 | 4.97 | 5.41% | 15.54% | 27.70% | 9.09%, 9.09%, 9.09% (11) | 4.81% | 6.00% |  |
| c6__otcB20_W0__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.60 | 96.9 | 4.96 | 1.10% | 11.67% | 21.37% | 0.00%, 9.09%, 18.18% (11) | 2.79% | 3.26% |  |
| c6__otcB20_W0__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.59 | 96.6 | 4.95 | 2.66% | 11.79% | 22.59% | 0.00%, 11.82%, 18.18% (11) | 2.33% | 2.86% |  |
| c6__otcB20_W0__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.59 | 96.7 | 4.96 | 5.41% | 14.86% | 27.03% | 9.09%, 9.09%, 9.09% (11) | 4.81% | 6.14% |  |
| c6__otcB20_W0__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.59 | 96.6 | 4.95 | 1.76% | 10.79% | 21.15% | 0.00%, 9.09%, 18.18% (11) | 2.43% | 3.29% |  |
| c6__otcB20_W0__R100 | issuer_1_with_destination | 4.63 | 25.0 | 3.29 | 10.81% | 33.11% | 56.76% | 22.73%, 33.64%, 36.36% (11) | 8.74% | 10.32% |  |
| c6__otcB20_W0__R100 | issuer_2 [share 20%, all records] | 4.51 | 22.8 | 4.00 | 2.49% | 11.96% | 11.96% | 0.00%, 0.00%, 0.00% (11) | 5.85% | 4.17% | badly miscalibrated |
| c6__otcB20_W0__R100 | issuer_2 [share 20%, its own devices] | 4.51 | 22.7 | 3.94 | 13.89% | 66.67% | 66.67% | 0.00%, 0.00%, 0.00% (12) | 6.47% | 10.01% |  |
| c6__otcB20_W0__R100 | issuer_2 [share 20%, other issuers' devices] | 4.51 | 22.8 | 4.01 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 6.45% | 4.10% | badly miscalibrated |
| c6__otcB20_W0__R100 | issuer_2_with_observer [share 20%, all records] | 6.60 | 97.3 | 4.98 | 1.99% | 12.62% | 21.76% | 0.00%, 11.82%, 18.18% (11) | 3.14% | 2.91% | badly miscalibrated |
| c6__otcB20_W0__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.61 | 97.7 | 4.97 | 2.78% | 12.96% | 15.74% | 0.00%, 0.00%, 0.00% (12) | 3.81% | 6.86% |  |
| c6__otcB20_W0__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.60 | 97.3 | 4.98 | 1.82% | 12.55% | 23.08% | 0.00%, 12.73%, 18.18% (11) | 3.29% | 3.01% | badly miscalibrated |
| c6__otcB20_W0__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.60 | 97.0 | 4.96 | 2.66% | 12.79% | 21.93% | 0.00%, 11.82%, 18.18% (11) | 2.87% | 3.05% |  |
| c6__otcB20_W0__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.60 | 97.3 | 4.95 | 3.70% | 12.96% | 15.74% | 0.00%, 0.00%, 0.00% (12) | 4.16% | 6.91% |  |
| c6__otcB20_W0__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.60 | 96.9 | 4.96 | 2.43% | 12.75% | 23.28% | 0.00%, 12.73%, 18.18% (11) | 3.29% | 3.31% |  |
| c6__otcB20_W0__R100 | issuer_2_with_destination | 4.22 | 18.8 | 2.96 | 9.26% | 34.26% | 57.41% | 16.67%, 16.67%, 16.67% (12) | 7.51% | 13.17% |  |
| c6__otcB5_W0__R1 | observer | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.40% |  |
| c6__otcB5_W0__R1 | first_hop | 5.65 | 50.3 | 4.26 | 7.70% | 22.22% | 37.54% | 7.70%, 7.70%, 7.70% (4180) | 3.82% | 1.29% | badly miscalibrated |
| c6__otcB5_W0__R1 | destination | 5.54 | 46.8 | 4.17 | 9.09% | 22.97% | 33.97% | 9.09%, 9.09%, 9.09% (209) | 6.75% | 6.91% |  |
| c6__otcB5_W0__R1 | destination_keyed | 3.83 | 14.4 | 2.77 | 19.14% | 55.02% | 84.69% | 19.14%, 19.14%, 19.14% (209) | 6.04% | 9.46% |  |
| c6__otcB5_W0__R1 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (209) | 0.00% | 0.00% |  |
| c6__otcB5_W0__R1 | issuer_0 [share 50%, all records] | 5.42 | 42.9 | 4.02 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 6.22% | 6.87% |  |
| c6__otcB5_W0__R1 | issuer_0 [share 50%, other issuers' devices] | 5.42 | 42.9 | 4.02 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 6.22% | 6.87% |  |
| c6__otcB5_W0__R1 | issuer_0_with_observer [share 50%, all records] | 5.46 | 44.3 | 3.54 | 0.00% | 13.40% | 28.71% | 0.00%, 0.00%, 0.00% (209) | 8.98% | 8.02% | badly miscalibrated |
| c6__otcB5_W0__R1 | issuer_0_with_observer [share 50%, other issuers' devices] | 5.46 | 44.3 | 3.54 | 0.00% | 13.40% | 28.71% | 0.00%, 0.00%, 0.00% (209) | 8.98% | 8.02% | badly miscalibrated |
| c6__otcB5_W0__R1 | issuer_0_with_first_relay [share 50%, all records] | 5.46 | 44.2 | 3.53 | 0.48% | 13.40% | 27.75% | 0.48%, 0.48%, 0.48% (209) | 8.55% | 8.37% | badly miscalibrated |
| c6__otcB5_W0__R1 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 5.46 | 44.2 | 3.53 | 0.48% | 13.40% | 27.75% | 0.48%, 0.48%, 0.48% (209) | 8.55% | 8.37% | badly miscalibrated |
| c6__otcB5_W0__R1 | issuer_1 [share 30%, all records] | 4.77 | 27.2 | 3.47 | 11.96% | 34.45% | 81.34% | 11.96%, 11.96%, 11.96% (209) | 4.29% | 8.29% |  |
| c6__otcB5_W0__R1 | issuer_1 [share 30%, its own devices] | 4.77 | 27.2 | 3.47 | 11.96% | 34.45% | 81.34% | 11.96%, 11.96%, 11.96% (209) | 4.29% | 8.29% |  |
| c6__otcB5_W0__R1 | issuer_1_with_observer [share 30%, all records] | 5.49 | 45.1 | 3.55 | 13.40% | 29.19% | 38.28% | 13.40%, 13.40%, 13.40% (209) | 6.68% | 7.34% |  |
| c6__otcB5_W0__R1 | issuer_1_with_observer [share 30%, its own devices] | 5.49 | 45.1 | 3.55 | 13.40% | 29.19% | 38.28% | 13.40%, 13.40%, 13.40% (209) | 6.68% | 7.34% |  |
| c6__otcB5_W0__R1 | issuer_1_with_first_relay [share 30%, all records] | 5.48 | 45.0 | 3.54 | 12.92% | 28.71% | 37.80% | 12.92%, 12.92%, 12.92% (209) | 6.18% | 7.86% |  |
| c6__otcB5_W0__R1 | issuer_1_with_first_relay [share 30%, its own devices] | 5.48 | 45.0 | 3.54 | 12.92% | 28.71% | 37.80% | 12.92%, 12.92%, 12.92% (209) | 6.18% | 7.86% |  |
| c6__otcB5_W0__R1 | issuer_1_with_destination | 3.47 | 11.3 | 2.06 | 14.83% | 46.41% | 84.21% | 14.83%, 14.83%, 14.83% (209) | 10.30% | 12.19% |  |
| c6__otcB5_W0__R1 | issuer_2 [share 20%, all records] | 4.45 | 21.9 | 3.23 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 10.86% | 8.68% | badly miscalibrated |
| c6__otcB5_W0__R1 | issuer_2 [share 20%, other issuers' devices] | 4.45 | 21.9 | 3.23 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (209) | 10.86% | 8.68% | badly miscalibrated |
| c6__otcB5_W0__R1 | issuer_2_with_observer [share 20%, all records] | 5.53 | 46.5 | 3.69 | 2.87% | 17.22% | 36.84% | 2.87%, 2.87%, 2.87% (209) | 7.08% | 7.93% |  |
| c6__otcB5_W0__R1 | issuer_2_with_observer [share 20%, other issuers' devices] | 5.53 | 46.5 | 3.69 | 2.87% | 17.22% | 36.84% | 2.87%, 2.87%, 2.87% (209) | 7.08% | 7.93% |  |
| c6__otcB5_W0__R1 | issuer_2_with_first_relay [share 20%, all records] | 5.53 | 46.4 | 3.68 | 2.87% | 16.27% | 35.89% | 2.87%, 2.87%, 2.87% (209) | 7.30% | 7.96% |  |
| c6__otcB5_W0__R1 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 5.53 | 46.4 | 3.68 | 2.87% | 16.27% | 35.89% | 2.87%, 2.87%, 2.87% (209) | 7.30% | 7.96% |  |
| c6__otcB5_W0__R100 | observer | 6.61 | 98.0 | 5.08 | 2.33% | 12.46% | 22.76% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.96% |  |
| c6__otcB5_W0__R100 | first_hop | 6.61 | 97.6 | 5.07 | 2.40% | 12.62% | 22.69% | 0.00%, 3.54%, 33.33% (120) | 1.71% | 0.57% |  |
| c6__otcB5_W0__R100 | destination | 6.48 | 89.5 | 4.96 | 1.33% | 11.79% | 21.59% | 0.00%, 2.73%, 9.09% (11) | 1.94% | 2.65% |  |
| c6__otcB5_W0__R100 | destination_keyed | 5.07 | 35.8 | 3.80 | 6.15% | 26.58% | 46.35% | 13.33%, 18.18%, 18.18% (11) | 2.31% | 4.33% |  |
| c6__otcB5_W0__R100 | first_relay_with_destination | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (11) | 0.00% | 0.00% |  |
| c6__otcB5_W0__R100 | issuer_0 [share 50%, all records] | 6.48 | 89.2 | 4.92 | 3.16% | 9.30% | 16.45% | 4.55%, 18.73%, 20.00% (10) | 0.90% | 2.93% |  |
| c6__otcB5_W0__R100 | issuer_0 [share 50%, its own devices] | 6.48 | 89.4 | 4.91 | 5.49% | 16.18% | 28.61% | 10.00%, 19.27%, 20.00% (10) | 2.38% | 3.83% |  |
| c6__otcB5_W0__R100 | issuer_0 [share 50%, other issuers' devices] | 6.48 | 89.1 | 4.92 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 3.32% | 4.69% |  |
| c6__otcB5_W0__R100 | issuer_0_with_observer [share 50%, all records] | 6.37 | 82.7 | 4.07 | 1.99% | 11.63% | 22.43% | 0.00%, 10.00%, 10.00% (10) | 4.12% | 4.12% |  |
| c6__otcB5_W0__R100 | issuer_0_with_observer [share 50%, its own devices] | 6.36 | 82.5 | 4.06 | 3.47% | 18.50% | 27.46% | 0.00%, 10.00%, 10.00% (10) | 4.14% | 5.12% |  |
| c6__otcB5_W0__R100 | issuer_0_with_observer [share 50%, other issuers' devices] | 6.37 | 83.0 | 4.08 | 0.00% | 2.34% | 15.62% | 0.00%, 0.00%, 0.00% (11) | 6.05% | 6.53% |  |
| c6__otcB5_W0__R100 | issuer_0_with_first_relay [share 50%, all records] | 6.36 | 82.4 | 4.06 | 2.66% | 11.13% | 21.76% | 0.00%, 12.45%, 18.18% (11) | 4.02% | 3.89% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_0_with_first_relay [share 50%, its own devices] | 6.36 | 82.2 | 4.05 | 4.62% | 17.92% | 27.46% | 10.00%, 14.91%, 18.18% (11) | 4.32% | 5.28% |  |
| c6__otcB5_W0__R100 | issuer_0_with_first_relay [share 50%, other issuers' devices] | 6.37 | 82.7 | 4.08 | 0.00% | 1.95% | 14.06% | 0.00%, 0.00%, 0.00% (11) | 6.06% | 6.15% |  |
| c6__otcB5_W0__R100 | issuer_0_with_destination | 5.08 | 34.1 | 3.14 | 4.05% | 20.81% | 35.55% | 0.00%, 14.91%, 18.18% (11) | 8.16% | 6.60% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_1 [share 30%, all records] | 5.65 | 50.1 | 4.17 | 1.33% | 5.81% | 10.63% | 0.00%, 5.45%, 18.18% (11) | 4.23% | 3.57% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_1 [share 30%, its own devices] | 5.64 | 49.9 | 4.18 | 5.41% | 23.65% | 43.24% | 9.09%, 16.36%, 18.18% (11) | 4.42% | 7.38% |  |
| c6__otcB5_W0__R100 | issuer_1 [share 30%, other issuers' devices] | 5.65 | 50.1 | 4.17 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 5.57% | 4.39% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_1_with_observer [share 30%, all records] | 6.47 | 89.1 | 4.29 | 2.33% | 9.97% | 21.10% | 0.00%, 5.45%, 18.18% (11) | 3.04% | 3.44% |  |
| c6__otcB5_W0__R100 | issuer_1_with_observer [share 30%, its own devices] | 6.47 | 89.0 | 4.29 | 9.46% | 22.97% | 33.11% | 9.09%, 16.36%, 18.18% (11) | 5.70% | 7.98% |  |
| c6__otcB5_W0__R100 | issuer_1_with_observer [share 30%, other issuers' devices] | 6.47 | 89.2 | 4.29 | 0.00% | 5.73% | 17.18% | 0.00%, 0.00%, 0.00% (11) | 5.34% | 3.92% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_1_with_first_relay [share 30%, all records] | 6.47 | 88.8 | 4.28 | 2.33% | 10.47% | 21.10% | 0.00%, 5.45%, 18.18% (11) | 3.05% | 3.70% |  |
| c6__otcB5_W0__R100 | issuer_1_with_first_relay [share 30%, its own devices] | 6.47 | 88.6 | 4.29 | 9.46% | 22.97% | 33.11% | 9.09%, 16.36%, 18.18% (11) | 6.63% | 7.27% |  |
| c6__otcB5_W0__R100 | issuer_1_with_first_relay [share 30%, other issuers' devices] | 6.47 | 88.9 | 4.28 | 0.00% | 6.39% | 17.18% | 0.00%, 0.00%, 0.00% (11) | 5.35% | 4.00% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_1_with_destination | 4.32 | 20.2 | 2.65 | 8.78% | 33.11% | 53.38% | 13.64%, 17.27%, 18.18% (11) | 9.49% | 12.22% |  |
| c6__otcB5_W0__R100 | issuer_2 [share 20%, all records] | 5.22 | 37.4 | 3.78 | 1.00% | 4.98% | 8.97% | 0.00%, 0.00%, 0.00% (11) | 6.32% | 4.23% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_2 [share 20%, its own devices] | 5.22 | 37.3 | 3.79 | 5.56% | 27.78% | 50.00% | 0.00%, 0.00%, 0.00% (12) | 7.14% | 10.30% |  |
| c6__otcB5_W0__R100 | issuer_2 [share 20%, other issuers' devices] | 5.22 | 37.4 | 3.78 | 0.00% | 0.00% | 0.00% | 0.00%, 0.00%, 0.00% (11) | 7.33% | 4.85% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_2_with_observer [share 20%, all records] | 6.50 | 90.9 | 4.31 | 1.16% | 10.63% | 21.26% | 0.00%, 0.00%, 0.00% (11) | 4.22% | 3.39% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_2_with_observer [share 20%, its own devices] | 6.51 | 91.1 | 4.34 | 6.48% | 22.22% | 26.85% | 0.00%, 0.00%, 0.00% (12) | 5.84% | 8.47% |  |
| c6__otcB5_W0__R100 | issuer_2_with_observer [share 20%, other issuers' devices] | 6.50 | 90.9 | 4.30 | 0.00% | 8.10% | 20.04% | 0.00%, 0.00%, 0.00% (11) | 5.32% | 3.89% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_2_with_first_relay [share 20%, all records] | 6.50 | 90.6 | 4.31 | 1.00% | 10.47% | 21.26% | 0.00%, 0.00%, 0.00% (11) | 4.40% | 3.55% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_2_with_first_relay [share 20%, its own devices] | 6.50 | 90.7 | 4.33 | 5.56% | 22.22% | 25.93% | 0.00%, 0.00%, 0.00% (12) | 5.61% | 8.49% |  |
| c6__otcB5_W0__R100 | issuer_2_with_first_relay [share 20%, other issuers' devices] | 6.50 | 90.6 | 4.30 | 0.00% | 7.89% | 20.24% | 0.00%, 0.00%, 0.00% (11) | 5.33% | 4.16% | badly miscalibrated |
| c6__otcB5_W0__R100 | issuer_2_with_destination | 3.87 | 14.9 | 2.25 | 5.56% | 30.56% | 60.19% | 0.00%, 0.00%, 0.00% (12) | 16.68% | 16.26% | badly miscalibrated |
| c6__otcB100_W0__R1 | K records, K = 1 | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.02% |  |
| c6__otcB100_W0__R1 | K records, K = 2 | 4.82 | 28.6 | 3.09 | 11.54% | 43.27% | 58.65% | 11.54%, 11.54%, 11.54% (104) | 8.83% | 13.08% |  |
| c6__otcB100_W0__R1 | K records, K = 3 | 4.03 | 16.6 | 2.35 | 18.84% | 59.42% | 72.46% | 18.84%, 18.84%, 18.84% (69) | 7.18% | 18.03% |  |
| c6__otcB100_W0__R1 | K records, K = 5 | 2.57 | 6.4 | 1.24 | 36.59% | 78.05% | 92.68% | 36.59%, 36.59%, 36.59% (41) | 26.10% | 28.07% |  |
| c6__otcB100_W0__R1 | K records, K = 10 | 0.50 | 1.5 | 0.21 | 85.00% | 95.00% | 100.00% | 85.00%, 85.00%, 85.00% (20) | 13.44% | 20.60% |  |
| c6__otcB100_W0__R1 | K records, K = 20 | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (10) | 0.00% | 0.00% |  |
| c6__otcB100_W0__R100 | K records, K = 1 | 6.61 | 97.9 | 5.08 | 2.33% | 12.46% | 22.92% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.94% |  |
| c6__otcB100_W0__R100 | K records, K = 2 | 5.73 | 53.8 | 3.73 | 2.19% | 18.25% | 33.21% | — | 6.24% | 6.44% |  |
| c6__otcB100_W0__R100 | K records, K = 3 | 4.86 | 30.0 | 2.85 | 8.33% | 30.36% | 54.76% | — | 9.74% | 10.58% |  |
| c6__otcB100_W0__R100 | K records, K = 5 | 3.26 | 10.2 | 1.63 | 13.89% | 68.06% | 81.94% | — | 20.64% | 21.99% |  |
| c6__otcB1_W0__R1 | K records, K = 1 | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.02% |  |
| c6__otcB1_W0__R1 | K records, K = 2 | 4.82 | 28.6 | 3.09 | 11.54% | 43.27% | 58.65% | 11.54%, 11.54%, 11.54% (104) | 8.83% | 13.08% |  |
| c6__otcB1_W0__R1 | K records, K = 3 | 4.03 | 16.6 | 2.35 | 18.84% | 59.42% | 72.46% | 18.84%, 18.84%, 18.84% (69) | 7.18% | 18.03% |  |
| c6__otcB1_W0__R1 | K records, K = 5 | 2.57 | 6.4 | 1.24 | 36.59% | 78.05% | 92.68% | 36.59%, 36.59%, 36.59% (41) | 26.10% | 28.07% |  |
| c6__otcB1_W0__R1 | K records, K = 10 | 0.50 | 1.5 | 0.21 | 85.00% | 95.00% | 100.00% | 85.00%, 85.00%, 85.00% (20) | 13.44% | 20.60% |  |
| c6__otcB1_W0__R1 | K records, K = 20 | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (10) | 0.00% | 0.00% |  |
| c6__otcB1_W0__R100 | K records, K = 1 | 6.61 | 97.9 | 5.08 | 2.33% | 12.46% | 22.92% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.94% |  |
| c6__otcB1_W0__R100 | K records, K = 2 | 5.73 | 53.8 | 3.73 | 2.19% | 18.25% | 33.21% | — | 6.24% | 6.44% |  |
| c6__otcB1_W0__R100 | K records, K = 3 | 4.86 | 30.0 | 2.85 | 8.33% | 30.36% | 54.76% | — | 9.74% | 10.58% |  |
| c6__otcB1_W0__R100 | K records, K = 5 | 3.26 | 10.2 | 1.63 | 13.89% | 68.06% | 81.94% | — | 20.64% | 21.99% |  |
| c6__otcB20_W0__R1 | K records, K = 1 | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.02% |  |
| c6__otcB20_W0__R1 | K records, K = 2 | 4.82 | 28.6 | 3.09 | 11.54% | 43.27% | 58.65% | 11.54%, 11.54%, 11.54% (104) | 8.83% | 13.08% |  |
| c6__otcB20_W0__R1 | K records, K = 3 | 4.03 | 16.6 | 2.35 | 18.84% | 59.42% | 72.46% | 18.84%, 18.84%, 18.84% (69) | 7.18% | 18.03% |  |
| c6__otcB20_W0__R1 | K records, K = 5 | 2.57 | 6.4 | 1.24 | 36.59% | 78.05% | 92.68% | 36.59%, 36.59%, 36.59% (41) | 26.10% | 28.07% |  |
| c6__otcB20_W0__R1 | K records, K = 10 | 0.50 | 1.5 | 0.21 | 85.00% | 95.00% | 100.00% | 85.00%, 85.00%, 85.00% (20) | 13.44% | 20.60% |  |
| c6__otcB20_W0__R1 | K records, K = 20 | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (10) | 0.00% | 0.00% |  |
| c6__otcB20_W0__R100 | K records, K = 1 | 6.61 | 97.9 | 5.08 | 2.33% | 12.46% | 22.92% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.94% |  |
| c6__otcB20_W0__R100 | K records, K = 2 | 5.73 | 53.8 | 3.73 | 2.19% | 18.25% | 33.21% | — | 6.24% | 6.44% |  |
| c6__otcB20_W0__R100 | K records, K = 3 | 4.86 | 30.0 | 2.85 | 8.33% | 30.36% | 54.76% | — | 9.74% | 10.58% |  |
| c6__otcB20_W0__R100 | K records, K = 5 | 3.26 | 10.2 | 1.63 | 13.89% | 68.06% | 81.94% | — | 20.64% | 21.99% |  |
| c6__otcB5_W0__R1 | K records, K = 1 | 5.65 | 50.4 | 4.26 | 7.66% | 22.01% | 37.32% | 7.66%, 7.66%, 7.66% (209) | 4.18% | 6.02% |  |
| c6__otcB5_W0__R1 | K records, K = 2 | 4.82 | 28.6 | 3.09 | 11.54% | 43.27% | 58.65% | 11.54%, 11.54%, 11.54% (104) | 8.83% | 13.08% |  |
| c6__otcB5_W0__R1 | K records, K = 3 | 4.03 | 16.6 | 2.35 | 18.84% | 59.42% | 72.46% | 18.84%, 18.84%, 18.84% (69) | 7.18% | 18.03% |  |
| c6__otcB5_W0__R1 | K records, K = 5 | 2.57 | 6.4 | 1.24 | 36.59% | 78.05% | 92.68% | 36.59%, 36.59%, 36.59% (41) | 26.10% | 28.07% |  |
| c6__otcB5_W0__R1 | K records, K = 10 | 0.50 | 1.5 | 0.21 | 85.00% | 95.00% | 100.00% | 85.00%, 85.00%, 85.00% (20) | 13.44% | 20.60% |  |
| c6__otcB5_W0__R1 | K records, K = 20 | 0.00 | 1.0 | 0.00 | 100.00% | 100.00% | 100.00% | 100.00%, 100.00%, 100.00% (10) | 0.00% | 0.00% |  |
| c6__otcB5_W0__R100 | K records, K = 1 | 6.61 | 97.9 | 5.08 | 2.33% | 12.46% | 22.92% | 0.00%, 11.82%, 18.18% (11) | 1.96% | 2.94% |  |
| c6__otcB5_W0__R100 | K records, K = 2 | 5.73 | 53.8 | 3.73 | 2.19% | 18.25% | 33.21% | — | 6.24% | 6.44% |  |
| c6__otcB5_W0__R100 | K records, K = 3 | 4.86 | 30.0 | 2.85 | 8.33% | 30.36% | 54.76% | — | 9.74% | 10.58% |  |
| c6__otcB5_W0__R100 | K records, K = 5 | 3.26 | 10.2 | 1.63 | 13.89% | 68.06% | 81.94% | — | 20.64% | 21.99% |  |
| c6_dest__cp_delay1800__R1 | observer [all records] | 5.96 | 62.3 | 4.60 | 2.83% | 11.79% | 26.89% | 2.83%, 2.83%, 2.83% (212) | 3.88% | 6.03% |  |
| c6_dest__cp_delay1800__R1 | observer [records the node delayed] | 5.94 | 61.7 | 4.59 | 0.00% | 3.23% | 9.68% | 0.00%, 0.00%, 0.00% (31) | 4.20% | 17.00% |  |
| c6_dest__cp_delay1800__R1 | observer [other records] | 5.96 | 62.5 | 4.61 | 3.31% | 13.26% | 29.83% | 3.31%, 3.31%, 3.31% (181) | 4.19% | 6.10% |  |
| c6_dest__cp_delay1800__R1 | delaying_destination | 5.89 | 59.4 | 4.47 | 9.68% | 12.90% | 32.26% | 9.68%, 9.68%, 9.68% (31) | 11.27% | 16.92% |  |
| c6_dest__cp_delay1800__R100 | observer [all records] | 6.95 | 123.9 | 5.44 | 2.44% | 9.71% | 17.22% | 2.14%, 5.29%, 7.17% (223) | 0.31% | 0.42% |  |
| c6_dest__cp_delay1800__R100 | observer [records the node delayed] | 6.95 | 123.7 | 5.44 | 0.59% | 2.88% | 5.73% | 0.00%, 0.00%, 9.52% (21) | 1.74% | 1.21% |  |
| c6_dest__cp_delay1800__R100 | observer [other records] | 6.95 | 123.9 | 5.44 | 2.68% | 10.60% | 18.73% | 2.21%, 5.58%, 8.08% (198) | 0.49% | 0.44% |  |
| c6_dest__cp_delay1800__R100 | delaying_destination | 6.86 | 116.3 | 5.32 | 2.26% | 11.66% | 21.10% | 0.00%, 6.62%, 11.11% (27) | 1.16% | 1.24% |  |
| c6_dest__cp_delay600__R1 | observer [all records] | 5.96 | 62.4 | 4.61 | 3.77% | 14.62% | 30.66% | 3.77%, 3.77%, 3.77% (212) | 4.82% | 5.77% |  |
| c6_dest__cp_delay600__R1 | observer [records the node delayed] | 5.96 | 62.1 | 4.62 | 6.45% | 22.58% | 35.48% | 6.45%, 6.45%, 6.45% (31) | 9.00% | 15.89% |  |
| c6_dest__cp_delay600__R1 | observer [other records] | 5.96 | 62.5 | 4.61 | 3.31% | 13.26% | 29.83% | 3.31%, 3.31%, 3.31% (181) | 4.19% | 6.10% |  |
| c6_dest__cp_delay600__R1 | delaying_destination | 5.89 | 59.3 | 4.46 | 9.68% | 12.90% | 32.26% | 9.68%, 9.68%, 9.68% (31) | 11.29% | 16.83% |  |
| c6_dest__cp_delay600__R100 | observer [all records] | 6.95 | 124.0 | 5.44 | 2.57% | 9.98% | 17.73% | 2.13%, 5.42%, 7.17% (223) | 0.38% | 0.42% |  |
| c6_dest__cp_delay600__R100 | observer [records the node delayed] | 6.95 | 124.1 | 5.45 | 1.71% | 5.22% | 10.11% | 0.00%, 6.11%, 13.64% (22) | 0.95% | 1.18% |  |
| c6_dest__cp_delay600__R100 | observer [other records] | 6.95 | 123.9 | 5.44 | 2.68% | 10.60% | 18.73% | 2.21%, 5.58%, 8.08% (198) | 0.49% | 0.44% |  |
| c6_dest__cp_delay600__R100 | delaying_destination | 6.85 | 116.1 | 5.31 | 2.34% | 11.74% | 21.10% | 0.00%, 6.62%, 11.11% (27) | 1.16% | 1.30% |  |
| c6_dest__cp_drop_m1800__R1 | observer [all records] | 6.03 | 65.6 | 4.66 | 3.30% | 12.26% | 26.89% | 3.30%, 3.30%, 3.30% (212) | 3.73% | 5.64% |  |
| c6_dest__cp_drop_m1800__R1 | observer [other records] | 6.03 | 65.6 | 4.66 | 3.30% | 12.26% | 26.89% | 3.30%, 3.30%, 3.30% (212) | 3.73% | 5.64% |  |
| c6_dest__cp_drop_m1800__R1 | drop_link | 5.43 | 43.6 | 3.69 | 6.45% | 25.81% | 48.39% | 6.45%, 6.45%, 6.45% (31) | 11.43% | 19.93% |  |
| c6_dest__cp_drop_m1800__R100 | observer [all records] | 7.03 | 130.9 | 5.52 | 2.57% | 10.13% | 17.75% | 2.28%, 5.09%, 9.09% (209) | 0.38% | 0.41% |  |
| c6_dest__cp_drop_m1800__R100 | observer [other records] | 7.03 | 130.9 | 5.52 | 2.57% | 10.13% | 17.75% | 2.28%, 5.09%, 9.09% (209) | 0.38% | 0.41% |  |
| c6_dest__cp_drop_m1800__R100 | drop_link | 6.39 | 84.3 | 4.37 | 6.05% | 19.26% | 32.00% | 4.76%, 12.50%, 25.00% (20) | 1.30% | 1.86% |  |
| c6_dest__cp_drop_m21600__R1 | observer [all records] | 6.03 | 65.3 | 4.65 | 5.45% | 18.18% | 30.00% | 5.45%, 5.45%, 5.45% (220) | 3.86% | 5.23% |  |
| c6_dest__cp_drop_m21600__R1 | observer [other records] | 6.03 | 65.3 | 4.65 | 5.45% | 18.18% | 30.00% | 5.45%, 5.45%, 5.45% (220) | 3.86% | 5.23% |  |
| c6_dest__cp_drop_m21600__R1 | drop_link | 5.38 | 41.9 | 3.46 | 11.76% | 58.82% | 70.59% | 11.76%, 11.76%, 11.76% (17) | 16.88% | 29.40% |  |
| c6_dest__cp_drop_m21600__R100 | observer [all records] | 7.03 | 130.6 | 5.53 | 2.36% | 9.86% | 17.37% | 2.02%, 4.72%, 7.47% (241) | 0.28% | 0.41% |  |
| c6_dest__cp_drop_m21600__R100 | observer [other records] | 7.03 | 130.6 | 5.53 | 2.36% | 9.86% | 17.37% | 2.02%, 4.72%, 7.47% (241) | 0.28% | 0.41% |  |
| c6_dest__cp_drop_m21600__R100 | drop_link | 6.39 | 84.1 | 4.39 | 5.54% | 19.42% | 32.50% | 4.65%, 11.76%, 30.43% (23) | 1.53% | 1.81% |  |
| c6_dest__cp_drop_m3600__R1 | observer [all records] | 6.04 | 65.9 | 4.68 | 2.31% | 13.89% | 30.09% | 2.31%, 2.31%, 2.31% (216) | 3.08% | 4.98% |  |
| c6_dest__cp_drop_m3600__R1 | observer [other records] | 6.04 | 65.9 | 4.68 | 2.31% | 13.89% | 30.09% | 2.31%, 2.31%, 2.31% (216) | 3.08% | 4.98% |  |
| c6_dest__cp_drop_m3600__R1 | drop_link | 5.46 | 44.1 | 3.64 | 3.70% | 37.04% | 59.26% | 3.70%, 3.70%, 3.70% (27) | 10.67% | 22.01% |  |
| c6_dest__cp_drop_m3600__R100 | observer [all records] | 7.03 | 131.0 | 5.53 | 2.59% | 9.93% | 17.46% | 2.43%, 4.89%, 7.08% (212) | 0.41% | 0.43% |  |
| c6_dest__cp_drop_m3600__R100 | observer [other records] | 7.03 | 131.0 | 5.53 | 2.59% | 9.93% | 17.46% | 2.43%, 4.89%, 7.08% (212) | 0.41% | 0.43% |  |
| c6_dest__cp_drop_m3600__R100 | drop_link | 6.40 | 84.6 | 4.39 | 5.45% | 20.62% | 34.13% | 4.17%, 12.31%, 30.43% (23) | 1.36% | 1.80% |  |
| c6_dest__cp_drop_m7200__R1 | observer [all records] | 6.03 | 65.5 | 4.67 | 4.09% | 18.18% | 30.45% | 4.09%, 4.09%, 4.09% (220) | 3.16% | 5.58% |  |
| c6_dest__cp_drop_m7200__R1 | observer [other records] | 6.03 | 65.5 | 4.67 | 4.09% | 18.18% | 30.45% | 4.09%, 4.09%, 4.09% (220) | 3.16% | 5.58% |  |
| c6_dest__cp_drop_m7200__R1 | drop_link | 5.40 | 42.5 | 3.65 | 5.56% | 38.89% | 50.00% | 5.56%, 5.56%, 5.56% (18) | 12.06% | 28.00% |  |
| c6_dest__cp_drop_m7200__R100 | observer [all records] | 7.03 | 130.8 | 5.54 | 2.51% | 9.89% | 17.85% | 2.17%, 5.05%, 8.88% (214) | 0.37% | 0.44% |  |
| c6_dest__cp_drop_m7200__R100 | observer [other records] | 7.03 | 130.8 | 5.54 | 2.51% | 9.89% | 17.85% | 2.17%, 5.05%, 8.88% (214) | 0.37% | 0.44% |  |
| c6_dest__cp_drop_m7200__R100 | drop_link | 6.40 | 84.6 | 4.40 | 6.42% | 21.45% | 34.64% | 5.88%, 12.50%, 21.05% (19) | 1.57% | 1.68% |  |
| c6_dest__otcL_delay1800__R1 | observer [all records] | 5.64 | 50.1 | 4.26 | 4.69% | 21.60% | 37.56% | 4.69%, 4.69%, 4.69% (213) | 2.66% | 6.43% |  |
| c6_dest__otcL_delay1800__R1 | observer [records the node delayed] | 5.64 | 49.8 | 4.23 | 0.00% | 0.00% | 0.00% | — | 5.37% | 25.58% |  |
| c6_dest__otcL_delay1800__R1 | observer [other records] | 5.64 | 50.1 | 4.26 | 4.90% | 22.55% | 39.22% | 4.90%, 4.90%, 4.90% (204) | 2.63% | 5.84% |  |
| c6_dest__otcL_delay1800__R1 | delaying_destination | 5.51 | 45.7 | 4.02 | 11.11% | 33.33% | 55.56% | — | 15.79% | 34.82% |  |
| c6_dest__otcL_delay1800__R100 | observer [all records] | 6.63 | 99.2 | 5.08 | 2.98% | 11.81% | 20.44% | 2.73%, 5.04%, 9.38% (192) | 0.32% | 0.47% |  |
| c6_dest__otcL_delay1800__R100 | observer [records the node delayed] | 6.62 | 98.9 | 5.08 | 0.37% | 1.58% | 4.00% | 0.00%, 0.00%, 8.33% (12) | 2.62% | 2.13% | badly miscalibrated |
| c6_dest__otcL_delay1800__R100 | observer [other records] | 6.63 | 99.2 | 5.08 | 3.12% | 12.37% | 21.34% | 2.81%, 5.39%, 9.84% (183) | 0.33% | 0.49% |  |
| c6_dest__otcL_delay1800__R100 | delaying_destination | 6.50 | 90.8 | 4.94 | 2.70% | 10.99% | 20.95% | 0.00%, 10.00%, 18.18% (11) | 1.21% | 2.14% |  |
| c6_dest__otcL_delay600__R1 | observer [all records] | 5.64 | 50.0 | 4.26 | 4.69% | 21.60% | 37.56% | 4.69%, 4.69%, 4.69% (213) | 2.66% | 6.31% |  |
| c6_dest__otcL_delay600__R1 | observer [records the node delayed] | 5.61 | 49.1 | 4.24 | 0.00% | 0.00% | 0.00% | — | 5.34% | 25.68% |  |
| c6_dest__otcL_delay600__R1 | observer [other records] | 5.64 | 50.1 | 4.26 | 4.90% | 22.55% | 39.22% | 4.90%, 4.90%, 4.90% (204) | 2.63% | 5.84% |  |
| c6_dest__otcL_delay600__R1 | delaying_destination | 5.51 | 45.7 | 4.02 | 11.11% | 33.33% | 55.56% | — | 15.79% | 34.82% |  |
| c6_dest__otcL_delay600__R100 | observer [all records] | 6.63 | 99.2 | 5.08 | 3.02% | 11.90% | 20.58% | 2.73%, 5.14%, 9.38% (192) | 0.32% | 0.48% |  |
| c6_dest__otcL_delay600__R100 | observer [records the node delayed] | 6.62 | 98.7 | 5.07 | 1.12% | 3.35% | 6.80% | 0.00%, 5.62%, 16.67% (12) | 1.99% | 2.03% |  |
| c6_dest__otcL_delay600__R100 | observer [other records] | 6.63 | 99.2 | 5.08 | 3.12% | 12.37% | 21.34% | 2.81%, 5.39%, 9.84% (183) | 0.33% | 0.49% |  |
| c6_dest__otcL_delay600__R100 | delaying_destination | 6.50 | 90.8 | 4.94 | 2.70% | 10.99% | 20.95% | 0.00%, 10.00%, 18.18% (11) | 1.21% | 2.14% |  |
| c6_dest__otcL_drop_m1800__R1 | observer [all records] | 5.68 | 51.5 | 4.30 | 5.16% | 19.72% | 38.03% | 5.16%, 5.16%, 5.16% (213) | 4.75% | 6.46% |  |
| c6_dest__otcL_drop_m1800__R1 | observer [other records] | 5.68 | 51.5 | 4.30 | 5.16% | 19.72% | 38.03% | 5.16%, 5.16%, 5.16% (213) | 4.75% | 6.46% |  |
| c6_dest__otcL_drop_m1800__R1 | drop_link | 4.53 | 23.3 | 2.94 | 11.11% | 33.33% | 55.56% | — | 21.01% | 45.45% |  |
| c6_dest__otcL_drop_m1800__R100 | observer [all records] | 6.67 | 102.3 | 5.13 | 3.12% | 11.97% | 20.68% | 2.74%, 5.61%, 7.85% (191) | 0.46% | 0.45% |  |
| c6_dest__otcL_drop_m1800__R100 | observer [other records] | 6.67 | 102.3 | 5.13 | 3.12% | 11.97% | 20.68% | 2.74%, 5.61%, 7.85% (191) | 0.46% | 0.45% |  |
| c6_dest__otcL_drop_m1800__R100 | drop_link | 5.60 | 48.8 | 3.73 | 6.76% | 25.81% | 40.86% | 7.14%, 16.67%, 21.43% (14) | 1.62% | 3.24% |  |
| c6_dest__otcL_drop_m21600__R1 | observer [all records] | 5.67 | 50.9 | 4.27 | 6.33% | 22.62% | 41.18% | 6.33%, 6.33%, 6.33% (221) | 3.80% | 5.67% |  |
| c6_dest__otcL_drop_m21600__R1 | observer [other records] | 5.67 | 50.9 | 4.27 | 6.33% | 22.62% | 41.18% | 6.33%, 6.33%, 6.33% (221) | 3.80% | 5.67% |  |
| c6_dest__otcL_drop_m21600__R1 | drop_link | 4.60 | 24.7 | 2.91 | 10.00% | 30.00% | 60.00% | 10.00%, 10.00%, 10.00% (10) | 18.83% | 50.27% |  |
| c6_dest__otcL_drop_m21600__R100 | observer [all records] | 6.66 | 101.5 | 5.12 | 2.63% | 11.57% | 20.52% | 2.42%, 4.61%, 7.00% (200) | 0.36% | 0.47% |  |
| c6_dest__otcL_drop_m21600__R100 | observer [other records] | 6.66 | 101.5 | 5.12 | 2.63% | 11.57% | 20.52% | 2.42%, 4.61%, 7.00% (200) | 0.36% | 0.47% |  |
| c6_dest__otcL_drop_m21600__R100 | drop_link | 5.59 | 48.3 | 3.71 | 8.80% | 27.79% | 41.95% | 8.71%, 20.00%, 25.00% (12) | 2.87% | 3.34% |  |
| c6_dest__otcL_drop_m3600__R1 | observer [all records] | 5.69 | 51.8 | 4.27 | 7.44% | 22.79% | 41.86% | 7.44%, 7.44%, 7.44% (215) | 4.34% | 6.00% |  |
| c6_dest__otcL_drop_m3600__R1 | observer [other records] | 5.69 | 51.8 | 4.27 | 7.44% | 22.79% | 41.86% | 7.44%, 7.44%, 7.44% (215) | 4.34% | 6.00% |  |
| c6_dest__otcL_drop_m3600__R1 | drop_link | 4.56 | 24.2 | 2.98 | 22.22% | 77.78% | 77.78% | — | 29.13% | 44.92% |  |
| c6_dest__otcL_drop_m3600__R100 | observer [all records] | 6.67 | 101.9 | 5.11 | 3.08% | 12.03% | 21.12% | 2.80%, 6.03%, 8.37% (215) | 0.27% | 0.49% |  |
| c6_dest__otcL_drop_m3600__R100 | observer [other records] | 6.67 | 101.9 | 5.11 | 3.08% | 12.03% | 21.12% | 2.80%, 6.03%, 8.37% (215) | 0.27% | 0.49% |  |
| c6_dest__otcL_drop_m3600__R100 | drop_link | 5.58 | 48.3 | 3.71 | 6.55% | 24.98% | 41.31% | 6.67%, 16.41%, 25.00% (12) | 2.50% | 3.05% |  |
| c6_dest__otcL_drop_m7200__R1 | observer [all records] | 5.67 | 51.0 | 4.26 | 6.79% | 23.53% | 36.20% | 6.79%, 6.79%, 6.79% (221) | 3.65% | 6.22% |  |
| c6_dest__otcL_drop_m7200__R1 | observer [other records] | 5.67 | 51.0 | 4.26 | 6.79% | 23.53% | 36.20% | 6.79%, 6.79%, 6.79% (221) | 3.65% | 6.22% |  |
| c6_dest__otcL_drop_m7200__R1 | drop_link | 4.58 | 24.3 | 2.91 | 20.00% | 60.00% | 70.00% | 20.00%, 20.00%, 20.00% (10) | 29.36% | 48.30% |  |
| c6_dest__otcL_drop_m7200__R100 | observer [all records] | 6.67 | 101.9 | 5.13 | 3.05% | 12.09% | 20.97% | 2.69%, 5.12%, 10.58% (189) | 0.28% | 0.46% |  |
| c6_dest__otcL_drop_m7200__R100 | observer [other records] | 6.67 | 101.9 | 5.13 | 3.05% | 12.09% | 20.97% | 2.69%, 5.12%, 10.58% (189) | 0.28% | 0.46% |  |
| c6_dest__otcL_drop_m7200__R100 | drop_link | 5.59 | 48.5 | 3.71 | 8.17% | 26.81% | 42.87% | 7.69%, 18.18%, 30.00% (10) | 1.70% | 3.29% |  |
| c6_dest__otc_delay1800__R1 | observer [all records] | 5.66 | 50.7 | 4.29 | 4.72% | 25.00% | 40.57% | 4.72%, 4.72%, 4.72% (212) | 3.40% | 6.37% |  |
| c6_dest__otc_delay1800__R1 | observer [records the node delayed] | 5.60 | 48.7 | 4.22 | 0.00% | 0.00% | 0.00% | — | 5.36% | 25.54% |  |
| c6_dest__otc_delay1800__R1 | observer [other records] | 5.66 | 50.8 | 4.30 | 4.93% | 26.11% | 42.36% | 4.93%, 4.93%, 4.93% (203) | 3.58% | 6.38% |  |
| c6_dest__otc_delay1800__R1 | delaying_destination | 5.61 | 49.2 | 4.26 | 0.00% | 33.33% | 44.44% | — | 5.34% | 25.80% |  |
| c6_dest__otc_delay1800__R100 | observer [all records] | 6.63 | 99.4 | 5.10 | 2.78% | 11.55% | 20.40% | 2.53%, 5.14%, 8.61% (209) | 0.36% | 0.49% |  |
| c6_dest__otc_delay1800__R100 | observer [records the node delayed] | 6.62 | 98.9 | 5.10 | 0.46% | 3.06% | 5.74% | 0.00%, 0.00%, 10.00% (10) | 2.50% | 2.11% | badly miscalibrated |
| c6_dest__otc_delay1800__R100 | observer [other records] | 6.63 | 99.5 | 5.10 | 2.91% | 12.02% | 21.21% | 2.68%, 5.39%, 8.96% (201) | 0.37% | 0.48% |  |
| c6_dest__otc_delay1800__R100 | delaying_destination | 6.51 | 91.4 | 4.98 | 2.59% | 13.24% | 22.31% | 0.00%, 8.08%, 20.00% (10) | 1.34% | 2.13% |  |
| c6_dest__otc_delay600__R1 | observer [all records] | 5.66 | 50.8 | 4.29 | 4.72% | 25.00% | 41.04% | 4.72%, 4.72%, 4.72% (212) | 3.39% | 6.60% |  |
| c6_dest__otc_delay600__R1 | observer [records the node delayed] | 5.64 | 50.2 | 4.14 | 0.00% | 0.00% | 11.11% | — | 5.72% | 25.72% |  |
| c6_dest__otc_delay600__R1 | observer [other records] | 5.66 | 50.8 | 4.30 | 4.93% | 26.11% | 42.36% | 4.93%, 4.93%, 4.93% (203) | 3.58% | 6.38% |  |
| c6_dest__otc_delay600__R1 | delaying_destination | 5.61 | 49.2 | 4.26 | 0.00% | 33.33% | 44.44% | — | 5.34% | 25.80% |  |
| c6_dest__otc_delay600__R100 | observer [all records] | 6.63 | 99.4 | 5.10 | 2.78% | 11.57% | 20.51% | 2.53%, 5.13%, 9.09% (209) | 0.38% | 0.47% |  |
| c6_dest__otc_delay600__R100 | observer [records the node delayed] | 6.63 | 99.1 | 5.09 | 0.46% | 3.43% | 7.87% | 0.00%, 0.00%, 10.00% (10) | 2.51% | 1.95% | badly miscalibrated |
| c6_dest__otc_delay600__R100 | observer [other records] | 6.63 | 99.5 | 5.10 | 2.91% | 12.02% | 21.21% | 2.68%, 5.39%, 8.96% (201) | 0.37% | 0.48% |  |
| c6_dest__otc_delay600__R100 | delaying_destination | 6.51 | 91.4 | 4.98 | 2.59% | 13.24% | 22.31% | 0.00%, 8.08%, 20.00% (10) | 1.34% | 2.13% |  |
| c6_dest__otc_drop_m1800__R1 | observer [all records] | 5.70 | 52.2 | 4.34 | 6.13% | 20.75% | 39.62% | 6.13%, 6.13%, 6.13% (212) | 3.76% | 6.12% |  |
| c6_dest__otc_drop_m1800__R1 | observer [other records] | 5.70 | 52.2 | 4.34 | 6.13% | 20.75% | 39.62% | 6.13%, 6.13%, 6.13% (212) | 3.76% | 6.12% |  |
| c6_dest__otc_drop_m1800__R1 | drop_link | 4.68 | 25.9 | 3.02 | 0.00% | 33.33% | 44.44% | — | 12.81% | 44.14% |  |
| c6_dest__otc_drop_m1800__R100 | observer [all records] | 6.68 | 102.5 | 5.13 | 2.83% | 11.79% | 20.61% | 2.53%, 5.13%, 7.77% (193) | 0.26% | 0.48% |  |
| c6_dest__otc_drop_m1800__R100 | observer [other records] | 6.68 | 102.5 | 5.13 | 2.83% | 11.79% | 20.61% | 2.53%, 5.13%, 7.77% (193) | 0.26% | 0.48% |  |
| c6_dest__otc_drop_m1800__R100 | drop_link | 5.60 | 48.9 | 3.72 | 8.08% | 27.23% | 44.04% | 8.01%, 16.67%, 50.00% (12) | 2.23% | 3.20% |  |
| c6_dest__otc_drop_m21600__R1 | observer [all records] | 5.67 | 51.3 | 4.27 | 7.80% | 21.56% | 36.70% | 7.80%, 7.80%, 7.80% (218) | 3.94% | 5.90% |  |
| c6_dest__otc_drop_m21600__R1 | observer [other records] | 5.67 | 51.3 | 4.27 | 7.80% | 21.56% | 36.70% | 7.80%, 7.80%, 7.80% (218) | 3.94% | 5.90% |  |
| c6_dest__otc_drop_m21600__R1 | drop_link | 4.67 | 25.5 | 2.98 | 10.00% | 40.00% | 90.00% | 10.00%, 10.00%, 10.00% (10) | 21.56% | 49.99% |  |
| c6_dest__otc_drop_m21600__R100 | observer [all records] | 6.68 | 102.4 | 5.13 | 2.78% | 11.76% | 20.50% | 2.54%, 4.87%, 6.99% (186) | 0.34% | 0.48% |  |
| c6_dest__otc_drop_m21600__R100 | observer [other records] | 6.68 | 102.4 | 5.13 | 2.78% | 11.76% | 20.50% | 2.54%, 4.87%, 6.99% (186) | 0.34% | 0.48% |  |
| c6_dest__otc_drop_m21600__R100 | drop_link | 5.60 | 49.0 | 3.72 | 6.72% | 24.63% | 40.30% | 7.14%, 13.77%, 36.36% (11) | 2.01% | 3.75% |  |
| c6_dest__otc_drop_m3600__R1 | observer [all records] | 5.70 | 52.2 | 4.35 | 5.09% | 22.69% | 41.67% | 5.09%, 5.09%, 5.09% (216) | 4.33% | 5.94% |  |
| c6_dest__otc_drop_m3600__R1 | observer [other records] | 5.70 | 52.2 | 4.35 | 5.09% | 22.69% | 41.67% | 5.09%, 5.09%, 5.09% (216) | 4.33% | 5.94% |  |
| c6_dest__otc_drop_m3600__R1 | drop_link | 4.72 | 26.6 | 3.17 | 0.00% | 22.22% | 55.56% | — | 11.49% | 38.08% |  |
| c6_dest__otc_drop_m3600__R100 | observer [all records] | 6.68 | 102.7 | 5.14 | 2.69% | 11.64% | 20.52% | 2.23%, 5.17%, 6.70% (194) | 0.34% | 0.47% |  |
| c6_dest__otc_drop_m3600__R100 | observer [other records] | 6.68 | 102.7 | 5.14 | 2.69% | 11.64% | 20.52% | 2.23%, 5.17%, 6.70% (194) | 0.34% | 0.47% |  |
| c6_dest__otc_drop_m3600__R100 | drop_link | 5.62 | 49.3 | 3.74 | 8.06% | 25.78% | 41.52% | 7.69%, 21.43%, 38.46% (13) | 1.76% | 3.37% |  |
| c6_dest__otc_drop_m7200__R1 | observer [all records] | 5.68 | 51.3 | 4.28 | 4.55% | 22.27% | 35.91% | 4.55%, 4.55%, 4.55% (220) | 3.81% | 5.91% |  |
| c6_dest__otc_drop_m7200__R1 | observer [other records] | 5.68 | 51.3 | 4.28 | 4.55% | 22.27% | 35.91% | 4.55%, 4.55%, 4.55% (220) | 3.81% | 5.91% |  |
| c6_dest__otc_drop_m7200__R1 | drop_link | 4.75 | 27.0 | 3.23 | 10.00% | 50.00% | 60.00% | 10.00%, 10.00%, 10.00% (10) | 18.15% | 42.98% |  |
| c6_dest__otc_drop_m7200__R100 | observer [all records] | 6.68 | 102.6 | 5.14 | 2.95% | 11.87% | 20.58% | 2.54%, 5.55%, 7.96% (201) | 0.40% | 0.42% |  |
| c6_dest__otc_drop_m7200__R100 | observer [other records] | 6.68 | 102.6 | 5.14 | 2.95% | 11.87% | 20.58% | 2.54%, 5.55%, 7.96% (201) | 0.40% | 0.42% |  |
| c6_dest__otc_drop_m7200__R100 | drop_link | 5.60 | 48.9 | 3.73 | 7.75% | 28.36% | 44.90% | 6.46%, 20.00%, 40.00% (10) | 1.07% | 3.55% |  |
| c6_issuer__iwh_delay_L1440__R1 | iwh_delay_L1440 | 6.38 | 83.9 | 5.53 | 27.27% | 27.27% | 27.27% | 0.00%, 0.00%, 0.00% (11) | 2.18% | 19.51% |  |
| c6_issuer__iwh_delay_L1440__R100 | iwh_delay_L1440 | 7.30 | 157.4 | 6.40 | 37.50% | 37.50% | 37.50% | — | 1.19% | 13.43% |  |
| c6_issuer__iwh_delay_L360__R1 | iwh_delay_L360 | 6.42 | 86.1 | 5.56 | 25.00% | 25.00% | 25.00% | — | 2.14% | 26.04% |  |
| c6_issuer__iwh_delay_L360__R100 | iwh_delay_L360 | 7.31 | 159.5 | 6.41 | 28.57% | 28.57% | 28.57% | — | 1.18% | 15.15% |  |
| c6_issuer__iwh_delay_L720__R1 | iwh_delay_L720 | 6.45 | 88.9 | 5.61 | 30.00% | 30.00% | 30.00% | 0.00%, 0.00%, 0.00% (10) | 2.08% | 21.19% |  |
| c6_issuer__iwh_delay_L720__R100 | iwh_delay_L720 | 7.31 | 159.3 | 6.42 | 30.00% | 30.00% | 30.00% | 0.00%, 0.00%, 0.00% (10) | 1.17% | 20.67% |  |
| c6_issuer__iwh_none_L1440__R1 | iwh_none_L1440 | 6.40 | 85.0 | 5.55 | 27.27% | 27.27% | 27.27% | 0.00%, 0.00%, 0.00% (11) | 2.15% | 19.50% |  |
| c6_issuer__iwh_none_L1440__R100 | iwh_none_L1440 | 7.31 | 158.7 | 6.41 | 37.50% | 37.50% | 37.50% | — | 1.18% | 13.43% |  |
| c6_issuer__iwh_none_L360__R1 | iwh_none_L360 | 6.42 | 86.1 | 5.57 | 25.00% | 25.00% | 25.00% | — | 2.14% | 26.03% |  |
| c6_issuer__iwh_none_L360__R100 | iwh_none_L360 | 7.32 | 160.4 | 6.42 | 28.57% | 28.57% | 28.57% | — | 1.17% | 15.15% |  |
| c6_issuer__iwh_none_L720__R1 | iwh_none_L720 | 6.42 | 86.4 | 5.57 | 30.00% | 30.00% | 30.00% | 0.00%, 0.00%, 0.00% (10) | 2.13% | 21.25% |  |
| c6_issuer__iwh_none_L720__R100 | iwh_none_L720 | 7.32 | 160.5 | 6.43 | 30.00% | 30.00% | 30.00% | 0.00%, 0.00%, 0.00% (10) | 1.16% | 20.67% |  |
| c6_issuer__iwh_withhold_L1440__R1 | iwh_withhold_L1440 | 6.38 | 83.9 | 5.53 | 27.27% | 27.27% | 27.27% | 0.00%, 0.00%, 0.00% (11) | 2.18% | 19.51% |  |
| c6_issuer__iwh_withhold_L1440__R100 | iwh_withhold_L1440 | 7.30 | 157.4 | 6.40 | 37.50% | 37.50% | 37.50% | — | 1.19% | 13.43% |  |
| c6_issuer__iwh_withhold_L360__R1 | iwh_withhold_L360 | 6.42 | 86.1 | 5.56 | 25.00% | 25.00% | 25.00% | — | 2.14% | 26.04% |  |
| c6_issuer__iwh_withhold_L360__R100 | iwh_withhold_L360 | 7.31 | 159.5 | 6.41 | 28.57% | 28.57% | 28.57% | — | 1.18% | 15.15% |  |
| c6_issuer__iwh_withhold_L720__R1 | iwh_withhold_L720 | 6.45 | 88.9 | 5.61 | 30.00% | 30.00% | 30.00% | 0.00%, 0.00%, 0.00% (10) | 2.08% | 21.19% |  |
| c6_issuer__iwh_withhold_L720__R100 | iwh_withhold_L720 | 7.31 | 159.3 | 6.42 | 30.00% | 30.00% | 30.00% | 0.00%, 0.00%, 0.00% (10) | 1.17% | 20.67% |  |

## Reliability

Per row, the confidence deciles: mean confidence → hit rate.

- c6__otcB100_W0__R1, observer: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB100_W0__R1, first_hop: 4.0 → 0.5; 4.4 → 5.0; 4.6 → 1.0; 4.8 → 12.4; 5.1 → 8.9; 5.3 → 6.2; 5.5 → 9.1; 5.8 → 12.0; 6.2 → 12.2; 7.5 → 9.8
- c6__otcB100_W0__R1, destination: 4.2 → 0.0; 4.7 → 0.0; 4.9 → 19.0; 5.1 → 4.8; 5.3 → 19.0; 5.6 → 14.3; 5.8 → 0.0; 6.2 → 4.8; 6.6 → 19.0; 8.1 → 10.0
- c6__otcB100_W0__R1, destination_keyed: 9.9 → 9.5; 11.4 → 23.8; 12.0 → 14.3; 13.3 → 9.5; 14.5 → 14.3; 15.2 → 9.5; 16.1 → 28.6; 17.2 → 38.1; 18.6 → 19.0; 23.4 → 25.0
- c6__otcB100_W0__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB100_W0__R1, issuer_0 [share 50%, all records]: 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.4 → 0.0; 4.5 → 0.0; 6.5 → 0.0
- c6__otcB100_W0__R1, issuer_0 [share 50%, other issuers' devices]: 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.0 → 0.0; 3.4 → 0.0; 4.5 → 0.0; 6.5 → 0.0
- c6__otcB100_W0__R1, issuer_0_with_observer [share 50%, all records]: 4.0 → 0.0; 4.5 → 9.5; 4.7 → 0.0; 4.9 → 4.8; 5.2 → 9.5; 5.5 → 4.8; 5.8 → 14.3; 6.1 → 9.5; 6.7 → 14.3; 9.4 → 0.0
- c6__otcB100_W0__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 4.0 → 0.0; 4.5 → 9.5; 4.7 → 0.0; 4.9 → 4.8; 5.2 → 9.5; 5.5 → 4.8; 5.8 → 14.3; 6.1 → 9.5; 6.7 → 14.3; 9.4 → 0.0
- c6__otcB100_W0__R1, issuer_0_with_first_relay [share 50%, all records]: 4.0 → 0.0; 4.4 → 9.5; 4.7 → 4.8; 4.9 → 0.0; 5.2 → 9.5; 5.5 → 4.8; 5.8 → 14.3; 6.2 → 9.5; 6.7 → 14.3; 9.7 → 0.0
- c6__otcB100_W0__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.0 → 0.0; 4.4 → 9.5; 4.7 → 4.8; 4.9 → 0.0; 5.2 → 9.5; 5.5 → 4.8; 5.8 → 14.3; 6.2 → 9.5; 6.7 → 14.3; 9.7 → 0.0
- c6__otcB100_W0__R1, issuer_1 [share 30%, all records]: 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.1 → 0.0; 6.0 → 4.8; 9.6 → 10.0
- c6__otcB100_W0__R1, issuer_1 [share 30%, its own devices]: 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.1 → 0.0; 6.0 → 4.8; 9.6 → 10.0
- c6__otcB100_W0__R1, issuer_1_with_observer [share 30%, all records]: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 4.8; 4.9 → 9.5; 5.1 → 14.3; 5.4 → 0.0; 5.6 → 14.3; 5.9 → 19.0; 6.5 → 14.3; 8.8 → 0.0
- c6__otcB100_W0__R1, issuer_1_with_observer [share 30%, its own devices]: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 4.8; 4.9 → 9.5; 5.1 → 14.3; 5.4 → 0.0; 5.6 → 14.3; 5.9 → 19.0; 6.5 → 14.3; 8.8 → 0.0
- c6__otcB100_W0__R1, issuer_1_with_first_relay [share 30%, all records]: 4.0 → 0.0; 4.4 → 9.5; 4.6 → 4.8; 4.9 → 9.5; 5.1 → 4.8; 5.3 → 4.8; 5.6 → 14.3; 6.0 → 19.0; 6.5 → 14.3; 8.8 → 0.0
- c6__otcB100_W0__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.0 → 0.0; 4.4 → 9.5; 4.6 → 4.8; 4.9 → 9.5; 5.1 → 4.8; 5.3 → 4.8; 5.6 → 14.3; 6.0 → 19.0; 6.5 → 14.3; 8.8 → 0.0
- c6__otcB100_W0__R1, issuer_1_with_destination: 10.3 → 19.0; 11.6 → 9.5; 12.8 → 19.0; 14.2 → 14.3; 15.1 → 4.8; 15.9 → 23.8; 17.0 → 33.3; 17.9 → 28.6; 21.2 → 9.5; 28.3 → 20.0
- c6__otcB100_W0__R1, issuer_2 [share 20%, all records]: 5.9 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.7 → 0.0; 11.4 → 0.0
- c6__otcB100_W0__R1, issuer_2 [share 20%, other issuers' devices]: 5.9 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.0 → 0.0; 6.7 → 0.0; 11.4 → 0.0
- c6__otcB100_W0__R1, issuer_2_with_observer [share 20%, all records]: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.9 → 14.3; 5.1 → 14.3; 5.4 → 0.0; 5.6 → 14.3; 6.0 → 14.3; 6.6 → 14.3; 9.1 → 0.0
- c6__otcB100_W0__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.9 → 14.3; 5.1 → 14.3; 5.4 → 0.0; 5.6 → 14.3; 6.0 → 14.3; 6.6 → 14.3; 9.1 → 0.0
- c6__otcB100_W0__R1, issuer_2_with_first_relay [share 20%, all records]: 4.0 → 0.0; 4.4 → 14.3; 4.6 → 0.0; 4.9 → 9.5; 5.1 → 4.8; 5.4 → 4.8; 5.6 → 14.3; 6.0 → 14.3; 6.5 → 14.3; 9.2 → 0.0
- c6__otcB100_W0__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.0 → 0.0; 4.4 → 14.3; 4.6 → 0.0; 4.9 → 9.5; 5.1 → 4.8; 5.4 → 4.8; 5.6 → 14.3; 6.0 → 14.3; 6.5 → 14.3; 9.2 → 0.0
- c6__otcB100_W0__R100, observer: 2.3 → 1.6; 2.5 → 6.6; 2.6 → 5.0; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB100_W0__R100, first_hop: 2.3 → 2.1; 2.5 → 5.6; 2.7 → 5.1; 2.8 → 1.2; 2.9 → 2.0; 3.0 → 2.2; 3.1 → 0.9; 3.3 → 2.7; 3.6 → 2.1; 4.0 → 0.2
- c6__otcB100_W0__R100, destination: 2.5 → 1.6; 2.7 → 1.6; 2.8 → 1.7; 3.0 → 0.0; 3.1 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.6 → 3.3; 3.9 → 3.3; 4.5 → 1.7
- c6__otcB100_W0__R100, destination_keyed: 4.4 → 1.6; 4.9 → 3.3; 5.3 → 5.0; 5.8 → 1.7; 6.5 → 6.7; 7.4 → 10.0; 8.3 → 5.0; 9.6 → 8.3; 10.8 → 11.7; 14.3 → 8.3
- c6__otcB100_W0__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB100_W0__R100, issuer_0 [share 50%, all records]: 9.1 → 0.0; 9.1 → 1.6; 9.1 → 1.7; 9.3 → 0.0; 9.5 → 0.0; 9.8 → 1.7; 10.1 → 0.0; 10.4 → 1.7; 10.8 → 5.0; 11.1 → 0.0
- c6__otcB100_W0__R100, issuer_0 [share 50%, its own devices]: 9.1 → 0.0; 9.1 → 2.9; 9.1 → 2.9; 9.2 → 0.0; 9.5 → 0.0; 9.7 → 2.9; 10.0 → 0.0; 10.3 → 2.9; 10.7 → 8.8; 11.1 → 0.0
- c6__otcB100_W0__R100, issuer_0 [share 50%, other issuers' devices]: 9.1 → 0.0; 9.1 → 0.0; 9.1 → 0.0; 9.4 → 0.0; 9.6 → 0.0; 9.9 → 0.0; 10.2 → 0.0; 10.5 → 0.0; 10.9 → 0.0; 11.2 → 0.0
- c6__otcB100_W0__R100, issuer_0_with_observer [share 50%, all records]: 2.3 → 1.6; 2.5 → 8.2; 2.7 → 1.7; 2.8 → 1.7; 2.8 → 0.0; 2.9 → 1.7; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB100_W0__R100, issuer_0_with_observer [share 50%, its own devices]: 2.3 → 0.0; 2.5 → 8.6; 2.7 → 2.9; 2.8 → 0.0; 2.9 → 0.0; 3.0 → 0.0; 3.1 → 0.0; 3.4 → 5.9; 3.7 → 0.0; 4.1 → 0.0
- c6__otcB100_W0__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.3 → 3.8; 2.5 → 3.8; 2.7 → 3.8; 2.8 → 3.8; 2.8 → 0.0; 2.9 → 3.8; 3.0 → 4.0; 3.2 → 0.0; 3.5 → 4.0; 4.0 → 0.0
- c6__otcB100_W0__R100, issuer_0_with_first_relay [share 50%, all records]: 2.3 → 0.0; 2.5 → 9.8; 2.7 → 1.7; 2.8 → 0.0; 2.9 → 5.0; 3.0 → 3.3; 3.1 → 0.0; 3.3 → 6.7; 3.7 → 0.0; 4.1 → 0.0
- c6__otcB100_W0__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.3 → 0.0; 2.5 → 8.6; 2.7 → 2.9; 2.8 → 0.0; 2.9 → 8.6; 3.1 → 0.0; 3.2 → 0.0; 3.4 → 5.9; 3.7 → 0.0; 4.1 → 0.0
- c6__otcB100_W0__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.3 → 3.8; 2.5 → 3.8; 2.7 → 3.8; 2.8 → 0.0; 2.9 → 0.0; 3.0 → 3.8; 3.1 → 4.0; 3.2 → 4.0; 3.5 → 4.0; 4.0 → 0.0
- c6__otcB100_W0__R100, issuer_0_with_destination: 4.3 → 2.9; 4.6 → 2.9; 4.9 → 2.9; 5.1 → 8.6; 5.4 → 0.0; 5.7 → 0.0; 6.0 → 5.9; 6.4 → 2.9; 6.9 → 5.9; 8.1 → 2.9
- c6__otcB100_W0__R100, issuer_1 [share 30%, all records]: 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.7 → 0.0; 51.5 → 0.0; 54.0 → 3.3
- c6__otcB100_W0__R100, issuer_1 [share 30%, its own devices]: 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.1 → 0.0; 51.1 → 0.0; 52.2 → 0.0; 54.3 → 14.3
- c6__otcB100_W0__R100, issuer_1 [share 30%, other issuers' devices]: 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.0 → 0.0; 50.6 → 0.0; 51.4 → 0.0; 53.8 → 0.0
- c6__otcB100_W0__R100, issuer_1_with_observer [share 30%, all records]: 2.3 → 1.6; 2.5 → 4.9; 2.6 → 6.7; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.2 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB100_W0__R100, issuer_1_with_observer [share 30%, its own devices]: 2.3 → 0.0; 2.6 → 13.3; 2.7 → 6.7; 2.8 → 6.7; 2.8 → 0.0; 2.9 → 6.7; 3.1 → 6.7; 3.2 → 0.0; 3.5 → 7.1; 4.0 → 0.0
- c6__otcB100_W0__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.3 → 2.2; 2.5 → 4.3; 2.6 → 4.3; 2.7 → 0.0; 2.8 → 0.0; 3.0 → 0.0; 3.1 → 0.0; 3.3 → 4.4; 3.7 → 0.0; 4.0 → 0.0
- c6__otcB100_W0__R100, issuer_1_with_first_relay [share 30%, all records]: 2.3 → 0.0; 2.5 → 6.6; 2.7 → 6.7; 2.7 → 0.0; 2.9 → 1.7; 3.0 → 6.7; 3.1 → 0.0; 3.3 → 6.7; 3.7 → 0.0; 4.1 → 0.0
- c6__otcB100_W0__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.3 → 0.0; 2.6 → 13.3; 2.7 → 6.7; 2.8 → 0.0; 2.9 → 0.0; 3.0 → 6.7; 3.1 → 6.7; 3.2 → 6.7; 3.5 → 7.1; 4.0 → 0.0
- c6__otcB100_W0__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.3 → 0.0; 2.4 → 6.5; 2.6 → 4.3; 2.7 → 0.0; 2.9 → 2.2; 3.0 → 4.4; 3.2 → 0.0; 3.3 → 4.4; 3.7 → 0.0; 4.1 → 0.0
- c6__otcB100_W0__R100, issuer_1_with_destination: 6.7 → 13.3; 7.4 → 20.0; 8.0 → 0.0; 8.3 → 0.0; 8.9 → 20.0; 9.5 → 0.0; 10.1 → 20.0; 10.5 → 0.0; 11.2 → 21.4; 12.6 → 14.3
- c6__otcB100_W0__R100, issuer_2 [share 20%, all records]: 25.0 → 0.0; 25.0 → 0.0; 25.0 → 1.7; 25.0 → 3.3; 25.2 → 1.7; 26.0 → 0.0; 26.4 → 0.0; 26.8 → 1.7; 27.8 → 1.7; 29.1 → 1.7
- c6__otcB100_W0__R100, issuer_2 [share 20%, its own devices]: 25.0 → 0.0; 25.0 → 9.1; 25.0 → 0.0; 25.0 → 27.3; 25.7 → 0.0; 26.2 → 0.0; 26.6 → 0.0; 26.9 → 9.1; 27.9 → 10.0; 29.1 → 10.0
- c6__otcB100_W0__R100, issuer_2 [share 20%, other issuers' devices]: 25.0 → 0.0; 25.0 → 0.0; 25.0 → 0.0; 25.0 → 0.0; 25.1 → 0.0; 25.9 → 0.0; 26.3 → 0.0; 26.9 → 0.0; 27.9 → 0.0; 29.1 → 0.0
- c6__otcB100_W0__R100, issuer_2_with_observer [share 20%, all records]: 2.3 → 1.6; 2.5 → 6.6; 2.6 → 5.0; 2.7 → 1.7; 2.8 → 1.7; 3.0 → 1.7; 3.1 → 0.0; 3.3 → 1.7; 3.7 → 3.3; 4.3 → 0.0
- c6__otcB100_W0__R100, issuer_2_with_observer [share 20%, its own devices]: 2.3 → 9.1; 2.4 → 0.0; 2.6 → 0.0; 2.7 → 0.0; 2.8 → 0.0; 2.9 → 0.0; 3.1 → 0.0; 3.2 → 0.0; 3.6 → 0.0; 4.1 → 0.0
- c6__otcB100_W0__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.3 → 0.0; 2.5 → 10.0; 2.7 → 4.0; 2.8 → 2.0; 2.9 → 2.0; 3.0 → 2.0; 3.1 → 0.0; 3.3 → 6.1; 3.7 → 0.0; 4.3 → 0.0
- c6__otcB100_W0__R100, issuer_2_with_first_relay [share 20%, all records]: 2.3 → 0.0; 2.5 → 6.6; 2.7 → 6.7; 2.7 → 0.0; 2.9 → 3.3; 3.1 → 5.0; 3.1 → 3.3; 3.3 → 5.0; 3.7 → 0.0; 4.3 → 0.0
- c6__otcB100_W0__R100, issuer_2_with_first_relay [share 20%, its own devices]: 2.3 → 0.0; 2.4 → 9.1; 2.6 → 0.0; 2.7 → 0.0; 2.8 → 0.0; 3.0 → 0.0; 3.1 → 9.1; 3.2 → 0.0; 3.7 → 0.0; 4.2 → 0.0
- c6__otcB100_W0__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.3 → 0.0; 2.5 → 10.0; 2.7 → 4.0; 2.8 → 0.0; 2.9 → 6.1; 3.1 → 4.1; 3.2 → 2.0; 3.3 → 6.1; 3.7 → 0.0; 4.3 → 0.0
- c6__otcB100_W0__R100, issuer_2_with_destination: 8.2 → 18.2; 9.2 → 9.1; 9.9 → 9.1; 10.3 → 9.1; 10.9 → 9.1; 11.6 → 9.1; 12.4 → 9.1; 14.0 → 9.1; 15.7 → 0.0; 19.8 → 0.0
- c6__otcB1_W0__R1, observer: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB1_W0__R1, first_hop: 4.0 → 0.5; 4.4 → 5.0; 4.6 → 1.0; 4.8 → 12.4; 5.1 → 8.9; 5.3 → 6.2; 5.5 → 9.1; 5.8 → 12.0; 6.2 → 12.2; 7.5 → 9.8
- c6__otcB1_W0__R1, destination: 4.2 → 0.0; 4.7 → 0.0; 4.9 → 19.0; 5.1 → 4.8; 5.3 → 19.0; 5.6 → 14.3; 5.8 → 0.0; 6.2 → 4.8; 6.6 → 19.0; 8.1 → 10.0
- c6__otcB1_W0__R1, destination_keyed: 9.9 → 9.5; 11.4 → 23.8; 12.0 → 14.3; 13.3 → 9.5; 14.5 → 14.3; 15.2 → 9.5; 16.1 → 28.6; 17.2 → 38.1; 18.6 → 19.0; 23.4 → 25.0
- c6__otcB1_W0__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB1_W0__R1, issuer_0 [share 50%, all records]: 6.9 → 0.0; 7.9 → 0.0; 8.5 → 0.0; 9.0 → 0.0; 9.5 → 0.0; 10.1 → 0.0; 10.7 → 0.0; 11.4 → 0.0; 12.4 → 0.0; 14.4 → 0.0
- c6__otcB1_W0__R1, issuer_0 [share 50%, other issuers' devices]: 6.9 → 0.0; 7.9 → 0.0; 8.5 → 0.0; 9.0 → 0.0; 9.5 → 0.0; 10.1 → 0.0; 10.7 → 0.0; 11.4 → 0.0; 12.4 → 0.0; 14.4 → 0.0
- c6__otcB1_W0__R1, issuer_0_with_observer [share 50%, all records]: 7.4 → 0.0; 8.9 → 0.0; 9.9 → 0.0; 10.9 → 0.0; 11.9 → 0.0; 12.7 → 0.0; 14.1 → 0.0; 16.0 → 0.0; 18.0 → 0.0; 23.3 → 0.0
- c6__otcB1_W0__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 7.4 → 0.0; 8.9 → 0.0; 9.9 → 0.0; 10.9 → 0.0; 11.9 → 0.0; 12.7 → 0.0; 14.1 → 0.0; 16.0 → 0.0; 18.0 → 0.0; 23.3 → 0.0
- c6__otcB1_W0__R1, issuer_0_with_first_relay [share 50%, all records]: 7.3 → 0.0; 8.9 → 0.0; 9.8 → 0.0; 10.9 → 0.0; 11.8 → 0.0; 12.6 → 0.0; 14.0 → 0.0; 15.8 → 0.0; 18.1 → 0.0; 23.2 → 0.0
- c6__otcB1_W0__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 7.3 → 0.0; 8.9 → 0.0; 9.8 → 0.0; 10.9 → 0.0; 11.8 → 0.0; 12.6 → 0.0; 14.0 → 0.0; 15.8 → 0.0; 18.1 → 0.0; 23.2 → 0.0
- c6__otcB1_W0__R1, issuer_1 [share 30%, all records]: 9.4 → 9.5; 10.8 → 14.3; 11.7 → 19.0; 12.3 → 4.8; 13.2 → 9.5; 14.1 → 14.3; 15.1 → 23.8; 16.3 → 19.0; 17.5 → 28.6; 21.8 → 30.0
- c6__otcB1_W0__R1, issuer_1 [share 30%, its own devices]: 9.4 → 9.5; 10.8 → 14.3; 11.7 → 19.0; 12.3 → 4.8; 13.2 → 9.5; 14.1 → 14.3; 15.1 → 23.8; 16.3 → 19.0; 17.5 → 28.6; 21.8 → 30.0
- c6__otcB1_W0__R1, issuer_1_with_observer [share 30%, all records]: 6.1 → 9.5; 8.2 → 9.5; 9.8 → 14.3; 11.1 → 19.0; 12.4 → 4.8; 13.3 → 9.5; 14.4 → 14.3; 15.9 → 23.8; 18.5 → 28.6; 25.3 → 35.0
- c6__otcB1_W0__R1, issuer_1_with_observer [share 30%, its own devices]: 6.1 → 9.5; 8.2 → 9.5; 9.8 → 14.3; 11.1 → 19.0; 12.4 → 4.8; 13.3 → 9.5; 14.4 → 14.3; 15.9 → 23.8; 18.5 → 28.6; 25.3 → 35.0
- c6__otcB1_W0__R1, issuer_1_with_first_relay [share 30%, all records]: 6.1 → 9.5; 8.2 → 9.5; 9.9 → 14.3; 11.1 → 19.0; 12.3 → 9.5; 13.3 → 0.0; 14.5 → 19.0; 15.9 → 23.8; 18.4 → 28.6; 25.3 → 35.0
- c6__otcB1_W0__R1, issuer_1_with_first_relay [share 30%, its own devices]: 6.1 → 9.5; 8.2 → 9.5; 9.9 → 14.3; 11.1 → 19.0; 12.3 → 9.5; 13.3 → 0.0; 14.5 → 19.0; 15.9 → 23.8; 18.4 → 28.6; 25.3 → 35.0
- c6__otcB1_W0__R1, issuer_1_with_destination: 14.4 → 23.8; 18.0 → 14.3; 20.0 → 19.0; 22.1 → 14.3; 24.8 → 4.8; 26.7 → 14.3; 29.0 → 19.0; 32.3 → 23.8; 36.5 → 23.8; 47.5 → 40.0
- c6__otcB1_W0__R1, issuer_2 [share 20%, all records]: 11.6 → 0.0; 13.6 → 0.0; 14.8 → 0.0; 15.8 → 0.0; 16.8 → 0.0; 18.0 → 0.0; 19.1 → 0.0; 20.6 → 0.0; 22.8 → 0.0; 28.0 → 0.0
- c6__otcB1_W0__R1, issuer_2 [share 20%, other issuers' devices]: 11.6 → 0.0; 13.6 → 0.0; 14.8 → 0.0; 15.8 → 0.0; 16.8 → 0.0; 18.0 → 0.0; 19.1 → 0.0; 20.6 → 0.0; 22.8 → 0.0; 28.0 → 0.0
- c6__otcB1_W0__R1, issuer_2_with_observer [share 20%, all records]: 5.5 → 14.3; 7.6 → 0.0; 9.5 → 0.0; 10.6 → 0.0; 11.4 → 0.0; 12.8 → 0.0; 14.4 → 0.0; 15.6 → 0.0; 18.4 → 0.0; 26.8 → 0.0
- c6__otcB1_W0__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 5.5 → 14.3; 7.6 → 0.0; 9.5 → 0.0; 10.6 → 0.0; 11.4 → 0.0; 12.8 → 0.0; 14.4 → 0.0; 15.6 → 0.0; 18.4 → 0.0; 26.8 → 0.0
- c6__otcB1_W0__R1, issuer_2_with_first_relay [share 20%, all records]: 5.5 → 14.3; 7.7 → 0.0; 9.3 → 0.0; 10.6 → 0.0; 11.6 → 0.0; 12.9 → 0.0; 14.4 → 0.0; 15.7 → 0.0; 18.3 → 0.0; 26.9 → 0.0
- c6__otcB1_W0__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 5.5 → 14.3; 7.7 → 0.0; 9.3 → 0.0; 10.6 → 0.0; 11.6 → 0.0; 12.9 → 0.0; 14.4 → 0.0; 15.7 → 0.0; 18.3 → 0.0; 26.9 → 0.0
- c6__otcB1_W0__R100, observer: 2.3 → 1.6; 2.5 → 6.6; 2.6 → 5.0; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB1_W0__R100, first_hop: 2.3 → 2.1; 2.5 → 5.6; 2.7 → 5.1; 2.8 → 1.2; 2.9 → 2.0; 3.0 → 2.2; 3.1 → 0.9; 3.3 → 2.7; 3.6 → 2.1; 4.0 → 0.2
- c6__otcB1_W0__R100, destination: 2.5 → 1.6; 2.7 → 1.6; 2.8 → 1.7; 3.0 → 0.0; 3.1 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.6 → 3.3; 3.9 → 3.3; 4.5 → 1.7
- c6__otcB1_W0__R100, destination_keyed: 4.4 → 1.6; 4.9 → 3.3; 5.3 → 5.0; 5.8 → 1.7; 6.5 → 6.7; 7.4 → 10.0; 8.3 → 5.0; 9.6 → 8.3; 10.8 → 11.7; 14.3 → 8.3
- c6__otcB1_W0__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB1_W0__R100, issuer_0 [share 50%, all records]: 3.9 → 8.2; 4.3 → 4.9; 4.5 → 6.7; 4.6 → 5.0; 4.8 → 0.0; 5.0 → 1.7; 5.3 → 1.7; 5.6 → 1.7; 6.3 → 0.0; 7.3 → 5.0
- c6__otcB1_W0__R100, issuer_0 [share 50%, its own devices]: 4.0 → 20.0; 4.3 → 2.9; 4.5 → 14.3; 4.7 → 5.7; 4.9 → 0.0; 5.1 → 2.9; 5.4 → 5.9; 5.8 → 0.0; 6.5 → 5.9; 7.5 → 2.9
- c6__otcB1_W0__R100, issuer_0 [share 50%, other issuers' devices]: 3.9 → 0.0; 4.3 → 0.0; 4.5 → 0.0; 4.6 → 0.0; 4.8 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 5.5 → 0.0; 6.2 → 0.0; 7.1 → 0.0
- c6__otcB1_W0__R100, issuer_0_with_observer [share 50%, all records]: 4.6 → 6.6; 5.6 → 3.3; 6.1 → 5.0; 6.4 → 0.0; 6.7 → 1.7; 7.5 → 15.0; 8.1 → 1.7; 8.7 → 3.3; 10.1 → 3.3; 13.2 → 0.0
- c6__otcB1_W0__R100, issuer_0_with_observer [share 50%, its own devices]: 4.6 → 11.4; 5.7 → 5.7; 6.1 → 8.6; 6.5 → 2.9; 6.8 → 5.7; 7.7 → 20.0; 8.2 → 2.9; 8.8 → 5.9; 10.3 → 5.9; 13.5 → 0.0
- c6__otcB1_W0__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 4.5 → 0.0; 5.6 → 0.0; 6.1 → 0.0; 6.3 → 0.0; 6.6 → 0.0; 7.3 → 0.0; 8.0 → 0.0; 8.5 → 0.0; 10.0 → 0.0; 12.8 → 0.0
- c6__otcB1_W0__R100, issuer_0_with_first_relay [share 50%, all records]: 4.5 → 6.6; 5.6 → 0.0; 6.1 → 6.7; 6.4 → 3.3; 6.6 → 0.0; 7.5 → 8.3; 8.1 → 5.0; 8.8 → 5.0; 10.5 → 3.3; 13.2 → 0.0
- c6__otcB1_W0__R100, issuer_0_with_first_relay [share 50%, its own devices]: 4.6 → 11.4; 5.6 → 0.0; 6.1 → 11.4; 6.5 → 5.7; 6.7 → 0.0; 7.7 → 20.0; 8.2 → 2.9; 8.9 → 8.8; 10.7 → 5.9; 13.5 → 0.0
- c6__otcB1_W0__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.5 → 0.0; 5.6 → 0.0; 6.1 → 0.0; 6.3 → 0.0; 6.6 → 0.0; 7.3 → 0.0; 8.0 → 0.0; 8.6 → 0.0; 10.3 → 0.0; 12.8 → 0.0
- c6__otcB1_W0__R100, issuer_0_with_destination: 7.1 → 0.0; 8.3 → 5.7; 9.0 → 2.9; 9.7 → 11.4; 10.3 → 2.9; 11.1 → 2.9; 12.0 → 8.8; 13.3 → 0.0; 15.2 → 2.9; 20.8 → 2.9
- c6__otcB1_W0__R100, issuer_1 [share 30%, all records]: 6.7 → 3.3; 7.1 → 0.0; 7.4 → 3.3; 7.9 → 1.7; 8.4 → 3.3; 8.8 → 5.0; 9.2 → 0.0; 9.9 → 1.7; 10.6 → 3.3; 11.8 → 3.3
- c6__otcB1_W0__R100, issuer_1 [share 30%, its own devices]: 6.6 → 13.3; 7.2 → 6.7; 7.6 → 13.3; 8.1 → 6.7; 8.5 → 6.7; 8.8 → 20.0; 9.1 → 0.0; 9.6 → 6.7; 10.4 → 7.1; 11.3 → 21.4
- c6__otcB1_W0__R100, issuer_1 [share 30%, other issuers' devices]: 6.7 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.9 → 0.0; 8.4 → 0.0; 8.8 → 0.0; 9.3 → 0.0; 10.0 → 0.0; 10.7 → 0.0; 11.9 → 0.0
- c6__otcB1_W0__R100, issuer_1_with_observer [share 30%, all records]: 4.1 → 1.6; 5.2 → 3.3; 5.7 → 3.3; 6.7 → 3.3; 7.3 → 3.3; 8.2 → 1.7; 9.0 → 3.3; 9.7 → 1.7; 11.0 → 1.7; 13.1 → 3.3
- c6__otcB1_W0__R100, issuer_1_with_observer [share 30%, its own devices]: 4.3 → 20.0; 5.5 → 6.7; 5.9 → 13.3; 7.0 → 6.7; 7.5 → 13.3; 8.3 → 6.7; 9.2 → 13.3; 9.7 → 6.7; 10.6 → 7.1; 12.7 → 14.3
- c6__otcB1_W0__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 4.1 → 0.0; 5.1 → 0.0; 5.6 → 0.0; 6.6 → 0.0; 7.3 → 0.0; 8.1 → 0.0; 9.0 → 0.0; 9.8 → 0.0; 11.1 → 0.0; 13.2 → 0.0
- c6__otcB1_W0__R100, issuer_1_with_first_relay [share 30%, all records]: 4.3 → 3.3; 5.2 → 3.3; 5.6 → 3.3; 6.6 → 1.7; 7.3 → 5.0; 8.2 → 1.7; 9.1 → 1.7; 9.7 → 1.7; 10.6 → 3.3; 12.9 → 3.3
- c6__otcB1_W0__R100, issuer_1_with_first_relay [share 30%, its own devices]: 4.3 → 20.0; 5.4 → 13.3; 5.9 → 13.3; 6.9 → 6.7; 7.5 → 13.3; 8.6 → 6.7; 9.4 → 6.7; 9.8 → 6.7; 10.4 → 14.3; 12.5 → 14.3
- c6__otcB1_W0__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 4.3 → 0.0; 5.2 → 0.0; 5.6 → 0.0; 6.5 → 0.0; 7.3 → 0.0; 8.1 → 0.0; 9.1 → 0.0; 9.8 → 0.0; 10.8 → 0.0; 13.1 → 0.0
- c6__otcB1_W0__R100, issuer_1_with_destination: 10.5 → 0.0; 12.0 → 6.7; 13.8 → 20.0; 14.7 → 6.7; 15.7 → 13.3; 16.7 → 20.0; 18.4 → 13.3; 20.3 → 13.3; 23.4 → 0.0; 26.8 → 14.3
- c6__otcB1_W0__R100, issuer_2 [share 20%, all records]: 7.6 → 0.0; 8.6 → 1.6; 9.3 → 3.3; 9.8 → 3.3; 10.4 → 5.0; 11.3 → 0.0; 12.3 → 3.3; 13.4 → 3.3; 15.1 → 0.0; 17.5 → 0.0
- c6__otcB1_W0__R100, issuer_2 [share 20%, its own devices]: 7.6 → 0.0; 8.3 → 9.1; 9.0 → 0.0; 9.4 → 18.2; 9.9 → 18.2; 10.4 → 18.2; 11.4 → 18.2; 12.8 → 27.3; 14.7 → 0.0; 16.8 → 0.0
- c6__otcB1_W0__R100, issuer_2 [share 20%, other issuers' devices]: 7.5 → 0.0; 8.7 → 0.0; 9.4 → 0.0; 10.0 → 0.0; 10.6 → 0.0; 11.6 → 0.0; 12.4 → 0.0; 13.5 → 0.0; 15.2 → 0.0; 17.6 → 0.0
- c6__otcB1_W0__R100, issuer_2_with_observer [share 20%, all records]: 3.5 → 4.9; 5.2 → 1.6; 5.8 → 1.7; 6.5 → 0.0; 7.0 → 1.7; 7.9 → 1.7; 8.9 → 3.3; 9.7 → 1.7; 11.2 → 1.7; 14.5 → 0.0
- c6__otcB1_W0__R100, issuer_2_with_observer [share 20%, its own devices]: 3.6 → 27.3; 5.0 → 0.0; 5.7 → 9.1; 6.2 → 9.1; 6.8 → 9.1; 7.8 → 9.1; 9.0 → 18.2; 9.8 → 9.1; 11.1 → 10.0; 13.7 → 0.0
- c6__otcB1_W0__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 3.5 → 0.0; 5.2 → 0.0; 5.9 → 0.0; 6.5 → 0.0; 7.0 → 0.0; 7.9 → 0.0; 9.0 → 0.0; 9.8 → 0.0; 11.2 → 0.0; 14.7 → 0.0
- c6__otcB1_W0__R100, issuer_2_with_first_relay [share 20%, all records]: 3.5 → 6.6; 5.2 → 1.6; 5.8 → 1.7; 6.4 → 0.0; 6.9 → 0.0; 7.9 → 1.7; 8.9 → 3.3; 9.7 → 1.7; 11.4 → 3.3; 14.6 → 0.0
- c6__otcB1_W0__R100, issuer_2_with_first_relay [share 20%, its own devices]: 3.6 → 27.3; 5.0 → 0.0; 5.7 → 9.1; 6.2 → 9.1; 6.8 → 0.0; 7.9 → 9.1; 9.0 → 18.2; 9.8 → 9.1; 11.5 → 10.0; 13.8 → 10.0
- c6__otcB1_W0__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 3.5 → 2.0; 5.2 → 0.0; 5.9 → 0.0; 6.4 → 0.0; 7.0 → 0.0; 8.0 → 0.0; 9.0 → 0.0; 9.8 → 0.0; 11.4 → 0.0; 14.8 → 0.0
- c6__otcB1_W0__R100, issuer_2_with_destination: 12.6 → 9.1; 14.1 → 0.0; 15.7 → 9.1; 17.5 → 27.3; 19.2 → 18.2; 21.1 → 0.0; 23.2 → 9.1; 26.0 → 9.1; 29.9 → 0.0; 39.0 → 0.0
- c6__otcB20_W0__R1, observer: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB20_W0__R1, first_hop: 4.0 → 0.5; 4.4 → 5.0; 4.6 → 1.0; 4.8 → 12.4; 5.1 → 8.9; 5.3 → 6.2; 5.5 → 9.1; 5.8 → 12.0; 6.2 → 12.2; 7.5 → 9.8
- c6__otcB20_W0__R1, destination: 4.2 → 0.0; 4.7 → 0.0; 4.9 → 19.0; 5.1 → 4.8; 5.3 → 19.0; 5.6 → 14.3; 5.8 → 0.0; 6.2 → 4.8; 6.6 → 19.0; 8.1 → 10.0
- c6__otcB20_W0__R1, destination_keyed: 9.9 → 9.5; 11.4 → 23.8; 12.0 → 14.3; 13.3 → 9.5; 14.5 → 14.3; 15.2 → 9.5; 16.1 → 28.6; 17.2 → 38.1; 18.6 → 19.0; 23.4 → 25.0
- c6__otcB20_W0__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB20_W0__R1, issuer_0 [share 50%, all records]: 2.6 → 0.0; 3.2 → 0.0; 3.8 → 0.0; 4.3 → 0.0; 4.9 → 0.0; 5.5 → 0.0; 5.9 → 0.0; 6.3 → 0.0; 6.6 → 0.0; 7.0 → 0.0
- c6__otcB20_W0__R1, issuer_0 [share 50%, other issuers' devices]: 2.6 → 0.0; 3.2 → 0.0; 3.8 → 0.0; 4.3 → 0.0; 4.9 → 0.0; 5.5 → 0.0; 5.9 → 0.0; 6.3 → 0.0; 6.6 → 0.0; 7.0 → 0.0
- c6__otcB20_W0__R1, issuer_0_with_observer [share 50%, all records]: 4.3 → 14.3; 4.7 → 0.0; 5.2 → 0.0; 5.6 → 14.3; 6.2 → 4.8; 6.9 → 0.0; 7.7 → 0.0; 8.7 → 0.0; 10.1 → 0.0; 12.8 → 0.0
- c6__otcB20_W0__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 4.3 → 14.3; 4.7 → 0.0; 5.2 → 0.0; 5.6 → 14.3; 6.2 → 4.8; 6.9 → 0.0; 7.7 → 0.0; 8.7 → 0.0; 10.1 → 0.0; 12.8 → 0.0
- c6__otcB20_W0__R1, issuer_0_with_first_relay [share 50%, all records]: 4.2 → 14.3; 4.8 → 0.0; 5.1 → 0.0; 5.6 → 14.3; 6.2 → 4.8; 6.9 → 0.0; 7.7 → 0.0; 8.7 → 0.0; 10.1 → 0.0; 13.0 → 0.0
- c6__otcB20_W0__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.2 → 14.3; 4.8 → 0.0; 5.1 → 0.0; 5.6 → 14.3; 6.2 → 4.8; 6.9 → 0.0; 7.7 → 0.0; 8.7 → 0.0; 10.1 → 0.0; 13.0 → 0.0
- c6__otcB20_W0__R1, issuer_1 [share 30%, all records]: 3.9 → 0.0; 3.9 → 0.0; 3.9 → 0.0; 4.9 → 14.3; 5.6 → 14.3; 6.9 → 0.0; 8.0 → 0.0; 9.2 → 9.5; 9.8 → 14.3; 10.3 → 10.0
- c6__otcB20_W0__R1, issuer_1 [share 30%, its own devices]: 3.9 → 0.0; 3.9 → 0.0; 3.9 → 0.0; 4.9 → 14.3; 5.6 → 14.3; 6.9 → 0.0; 8.0 → 0.0; 9.2 → 9.5; 9.8 → 14.3; 10.3 → 10.0
- c6__otcB20_W0__R1, issuer_1_with_observer [share 30%, all records]: 4.2 → 4.8; 4.6 → 14.3; 5.0 → 4.8; 5.3 → 9.5; 5.6 → 4.8; 5.9 → 23.8; 6.4 → 4.8; 7.6 → 23.8; 9.5 → 14.3; 14.1 → 5.0
- c6__otcB20_W0__R1, issuer_1_with_observer [share 30%, its own devices]: 4.2 → 4.8; 4.6 → 14.3; 5.0 → 4.8; 5.3 → 9.5; 5.6 → 4.8; 5.9 → 23.8; 6.4 → 4.8; 7.6 → 23.8; 9.5 → 14.3; 14.1 → 5.0
- c6__otcB20_W0__R1, issuer_1_with_first_relay [share 30%, all records]: 4.2 → 14.3; 4.6 → 4.8; 5.0 → 4.8; 5.3 → 4.8; 5.6 → 14.3; 5.9 → 23.8; 6.4 → 0.0; 7.6 → 23.8; 9.6 → 14.3; 14.1 → 5.0
- c6__otcB20_W0__R1, issuer_1_with_first_relay [share 30%, its own devices]: 4.2 → 14.3; 4.6 → 4.8; 5.0 → 4.8; 5.3 → 4.8; 5.6 → 14.3; 5.9 → 23.8; 6.4 → 0.0; 7.6 → 23.8; 9.6 → 14.3; 14.1 → 5.0
- c6__otcB20_W0__R1, issuer_1_with_destination: 10.7 → 19.0; 12.5 → 9.5; 14.3 → 14.3; 15.3 → 14.3; 16.6 → 33.3; 18.2 → 23.8; 20.3 → 14.3; 22.6 → 23.8; 27.4 → 19.0; 36.6 → 0.0
- c6__otcB20_W0__R1, issuer_2 [share 20%, all records]: 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.6 → 0.0; 6.3 → 0.0; 7.3 → 0.0; 8.8 → 0.0; 10.2 → 0.0; 11.7 → 0.0; 12.9 → 0.0
- c6__otcB20_W0__R1, issuer_2 [share 20%, other issuers' devices]: 5.0 → 0.0; 5.0 → 0.0; 5.0 → 0.0; 5.6 → 0.0; 6.3 → 0.0; 7.3 → 0.0; 8.8 → 0.0; 10.2 → 0.0; 11.7 → 0.0; 12.9 → 0.0
- c6__otcB20_W0__R1, issuer_2_with_observer [share 20%, all records]: 4.2 → 4.8; 4.6 → 0.0; 4.9 → 14.3; 5.2 → 9.5; 5.5 → 0.0; 5.8 → 14.3; 6.2 → 14.3; 6.9 → 9.5; 8.3 → 0.0; 12.3 → 0.0
- c6__otcB20_W0__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.2 → 4.8; 4.6 → 0.0; 4.9 → 14.3; 5.2 → 9.5; 5.5 → 0.0; 5.8 → 14.3; 6.2 → 14.3; 6.9 → 9.5; 8.3 → 0.0; 12.3 → 0.0
- c6__otcB20_W0__R1, issuer_2_with_first_relay [share 20%, all records]: 4.2 → 0.0; 4.6 → 14.3; 4.9 → 4.8; 5.2 → 14.3; 5.5 → 4.8; 5.8 → 14.3; 6.2 → 9.5; 6.9 → 14.3; 8.4 → 0.0; 12.4 → 0.0
- c6__otcB20_W0__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.2 → 0.0; 4.6 → 14.3; 4.9 → 4.8; 5.2 → 14.3; 5.5 → 4.8; 5.8 → 14.3; 6.2 → 9.5; 6.9 → 14.3; 8.4 → 0.0; 12.4 → 0.0
- c6__otcB20_W0__R100, observer: 2.3 → 1.6; 2.5 → 6.6; 2.6 → 5.0; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB20_W0__R100, first_hop: 2.3 → 2.1; 2.5 → 5.6; 2.7 → 5.1; 2.8 → 1.2; 2.9 → 2.0; 3.0 → 2.2; 3.1 → 0.9; 3.3 → 2.7; 3.6 → 2.1; 4.0 → 0.2
- c6__otcB20_W0__R100, destination: 2.5 → 1.6; 2.7 → 1.6; 2.8 → 1.7; 3.0 → 0.0; 3.1 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.6 → 3.3; 3.9 → 3.3; 4.5 → 1.7
- c6__otcB20_W0__R100, destination_keyed: 4.4 → 1.6; 4.9 → 3.3; 5.3 → 5.0; 5.8 → 1.7; 6.5 → 6.7; 7.4 → 10.0; 8.3 → 5.0; 9.6 → 8.3; 10.8 → 11.7; 14.3 → 8.3
- c6__otcB20_W0__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB20_W0__R100, issuer_0 [share 50%, all records]: 2.5 → 3.3; 2.8 → 0.0; 3.1 → 1.7; 3.3 → 0.0; 3.5 → 3.3; 3.6 → 1.7; 3.7 → 3.3; 3.7 → 1.7; 3.8 → 1.7; 3.9 → 1.7
- c6__otcB20_W0__R100, issuer_0 [share 50%, its own devices]: 2.5 → 5.7; 2.8 → 0.0; 3.1 → 2.9; 3.3 → 0.0; 3.5 → 5.7; 3.6 → 2.9; 3.7 → 0.0; 3.7 → 8.8; 3.8 → 2.9; 3.9 → 2.9
- c6__otcB20_W0__R100, issuer_0 [share 50%, other issuers' devices]: 2.5 → 0.0; 2.9 → 0.0; 3.1 → 0.0; 3.3 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 3.8 → 0.0; 3.9 → 0.0
- c6__otcB20_W0__R100, issuer_0_with_observer [share 50%, all records]: 2.4 → 1.6; 2.7 → 0.0; 2.8 → 3.3; 3.0 → 1.7; 3.2 → 3.3; 3.3 → 1.7; 3.7 → 1.7; 4.0 → 1.7; 4.9 → 1.7; 5.9 → 1.7
- c6__otcB20_W0__R100, issuer_0_with_observer [share 50%, its own devices]: 2.4 → 2.9; 2.7 → 0.0; 2.8 → 2.9; 3.0 → 5.7; 3.2 → 0.0; 3.4 → 2.9; 3.7 → 2.9; 4.1 → 2.9; 4.8 → 2.9; 6.0 → 2.9
- c6__otcB20_W0__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 2.4 → 0.0; 2.7 → 0.0; 2.8 → 3.8; 3.0 → 0.0; 3.1 → 3.8; 3.3 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 5.0 → 0.0; 5.9 → 0.0
- c6__otcB20_W0__R100, issuer_0_with_first_relay [share 50%, all records]: 2.4 → 1.6; 2.7 → 0.0; 2.9 → 1.7; 3.0 → 6.7; 3.2 → 0.0; 3.4 → 1.7; 3.7 → 1.7; 4.0 → 1.7; 4.8 → 1.7; 6.1 → 1.7
- c6__otcB20_W0__R100, issuer_0_with_first_relay [share 50%, its own devices]: 2.4 → 2.9; 2.7 → 0.0; 2.9 → 2.9; 3.1 → 5.7; 3.2 → 0.0; 3.5 → 2.9; 3.8 → 2.9; 4.1 → 2.9; 4.8 → 2.9; 6.2 → 2.9
- c6__otcB20_W0__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 2.4 → 0.0; 2.7 → 0.0; 2.9 → 0.0; 3.0 → 7.7; 3.2 → 0.0; 3.3 → 0.0; 3.7 → 0.0; 4.0 → 0.0; 5.0 → 0.0; 6.0 → 0.0
- c6__otcB20_W0__R100, issuer_0_with_destination: 4.4 → 5.7; 4.9 → 5.7; 5.4 → 0.0; 5.9 → 5.7; 6.2 → 5.7; 6.8 → 8.6; 7.5 → 2.9; 8.5 → 2.9; 9.6 → 2.9; 12.7 → 0.0
- c6__otcB20_W0__R100, issuer_1 [share 30%, all records]: 4.6 → 0.0; 5.3 → 0.0; 5.8 → 0.0; 6.1 → 0.0; 6.5 → 1.7; 6.9 → 0.0; 7.3 → 1.7; 7.7 → 0.0; 8.0 → 3.3; 8.3 → 0.0
- c6__otcB20_W0__R100, issuer_1 [share 30%, its own devices]: 4.8 → 0.0; 5.5 → 0.0; 5.9 → 0.0; 6.2 → 6.7; 6.7 → 0.0; 7.1 → 6.7; 7.5 → 0.0; 7.7 → 0.0; 8.0 → 14.3; 8.3 → 0.0
- c6__otcB20_W0__R100, issuer_1 [share 30%, other issuers' devices]: 4.6 → 0.0; 5.2 → 0.0; 5.8 → 0.0; 6.1 → 0.0; 6.5 → 0.0; 6.8 → 0.0; 7.2 → 0.0; 7.7 → 0.0; 8.0 → 0.0; 8.3 → 0.0
- c6__otcB20_W0__R100, issuer_1_with_observer [share 30%, all records]: 2.3 → 3.3; 2.6 → 6.6; 2.8 → 0.0; 2.9 → 0.0; 3.0 → 3.3; 3.1 → 0.0; 3.3 → 5.0; 3.8 → 0.0; 4.2 → 0.0; 5.1 → 3.3
- c6__otcB20_W0__R100, issuer_1_with_observer [share 30%, its own devices]: 2.5 → 6.7; 2.7 → 13.3; 2.8 → 0.0; 2.8 → 0.0; 2.9 → 6.7; 3.1 → 6.7; 3.2 → 6.7; 3.7 → 0.0; 4.1 → 0.0; 5.0 → 14.3
- c6__otcB20_W0__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 2.3 → 2.2; 2.5 → 4.3; 2.8 → 0.0; 2.9 → 0.0; 3.0 → 0.0; 3.2 → 0.0; 3.4 → 4.4; 3.8 → 0.0; 4.2 → 0.0; 5.2 → 0.0
- c6__otcB20_W0__R100, issuer_1_with_first_relay [share 30%, all records]: 2.3 → 4.9; 2.6 → 1.6; 2.8 → 1.7; 2.9 → 5.0; 3.0 → 5.0; 3.1 → 0.0; 3.4 → 5.0; 3.8 → 0.0; 4.2 → 0.0; 5.1 → 3.3
- c6__otcB20_W0__R100, issuer_1_with_first_relay [share 30%, its own devices]: 2.5 → 6.7; 2.7 → 6.7; 2.8 → 0.0; 2.9 → 0.0; 3.0 → 13.3; 3.1 → 6.7; 3.3 → 6.7; 3.7 → 0.0; 4.2 → 0.0; 5.0 → 14.3
- c6__otcB20_W0__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 2.3 → 2.2; 2.5 → 4.3; 2.8 → 0.0; 2.9 → 4.3; 3.0 → 2.2; 3.2 → 0.0; 3.4 → 4.4; 3.9 → 0.0; 4.2 → 0.0; 5.2 → 0.0
- c6__otcB20_W0__R100, issuer_1_with_destination: 6.7 → 20.0; 7.6 → 0.0; 8.5 → 6.7; 9.1 → 0.0; 9.7 → 6.7; 10.2 → 20.0; 11.0 → 6.7; 12.3 → 13.3; 14.4 → 35.7; 17.5 → 0.0
- c6__otcB20_W0__R100, issuer_2 [share 20%, all records]: 4.4 → 0.0; 4.4 → 1.6; 4.5 → 0.0; 5.4 → 0.0; 5.9 → 0.0; 6.5 → 1.7; 7.6 → 0.0; 8.5 → 0.0; 8.9 → 0.0; 9.1 → 3.3
- c6__otcB20_W0__R100, issuer_2 [share 20%, its own devices]: 4.4 → 0.0; 4.4 → 9.1; 5.2 → 0.0; 5.9 → 0.0; 6.3 → 0.0; 7.0 → 9.1; 8.3 → 0.0; 8.8 → 0.0; 9.0 → 0.0; 9.2 → 20.0
- c6__otcB20_W0__R100, issuer_2 [share 20%, other issuers' devices]: 4.4 → 0.0; 4.4 → 0.0; 4.4 → 0.0; 5.4 → 0.0; 5.9 → 0.0; 6.4 → 0.0; 7.5 → 0.0; 8.4 → 0.0; 8.8 → 0.0; 9.1 → 0.0
- c6__otcB20_W0__R100, issuer_2_with_observer [share 20%, all records]: 2.3 → 0.0; 2.6 → 6.6; 2.7 → 0.0; 2.8 → 5.0; 3.0 → 0.0; 3.2 → 0.0; 3.4 → 6.7; 3.7 → 0.0; 4.0 → 0.0; 4.9 → 1.7
- c6__otcB20_W0__R100, issuer_2_with_observer [share 20%, its own devices]: 2.3 → 0.0; 2.5 → 0.0; 2.7 → 0.0; 2.8 → 9.1; 3.0 → 0.0; 3.2 → 0.0; 3.6 → 9.1; 3.8 → 0.0; 4.1 → 0.0; 5.1 → 10.0
- c6__otcB20_W0__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.3 → 0.0; 2.6 → 8.0; 2.7 → 0.0; 2.8 → 4.0; 3.0 → 0.0; 3.2 → 0.0; 3.4 → 6.1; 3.7 → 0.0; 3.9 → 0.0; 4.8 → 0.0
- c6__otcB20_W0__R100, issuer_2_with_first_relay [share 20%, all records]: 2.3 → 0.0; 2.6 → 6.6; 2.7 → 1.7; 2.9 → 5.0; 3.1 → 5.0; 3.2 → 0.0; 3.5 → 6.7; 3.7 → 0.0; 4.0 → 0.0; 4.9 → 1.7
- c6__otcB20_W0__R100, issuer_2_with_first_relay [share 20%, its own devices]: 2.3 → 0.0; 2.5 → 0.0; 2.7 → 9.1; 2.9 → 0.0; 3.1 → 9.1; 3.2 → 0.0; 3.6 → 9.1; 3.8 → 0.0; 4.2 → 0.0; 5.1 → 10.0
- c6__otcB20_W0__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.3 → 0.0; 2.6 → 8.0; 2.7 → 0.0; 2.9 → 6.0; 3.1 → 4.1; 3.2 → 0.0; 3.4 → 6.1; 3.7 → 0.0; 4.0 → 0.0; 4.8 → 0.0
- c6__otcB20_W0__R100, issuer_2_with_destination: 8.7 → 18.2; 9.7 → 9.1; 10.4 → 9.1; 11.0 → 18.2; 12.0 → 9.1; 13.4 → 9.1; 14.3 → 9.1; 15.5 → 0.0; 17.6 → 10.0; 22.5 → 0.0
- c6__otcB5_W0__R1, observer: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB5_W0__R1, first_hop: 4.0 → 0.5; 4.4 → 5.0; 4.6 → 1.0; 4.8 → 12.4; 5.1 → 8.9; 5.3 → 6.2; 5.5 → 9.1; 5.8 → 12.0; 6.2 → 12.2; 7.5 → 9.8
- c6__otcB5_W0__R1, destination: 4.2 → 0.0; 4.7 → 0.0; 4.9 → 19.0; 5.1 → 4.8; 5.3 → 19.0; 5.6 → 14.3; 5.8 → 0.0; 6.2 → 4.8; 6.6 → 19.0; 8.1 → 10.0
- c6__otcB5_W0__R1, destination_keyed: 9.9 → 9.5; 11.4 → 23.8; 12.0 → 14.3; 13.3 → 9.5; 14.5 → 14.3; 15.2 → 9.5; 16.1 → 28.6; 17.2 → 38.1; 18.6 → 19.0; 23.4 → 25.0
- c6__otcB5_W0__R1, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB5_W0__R1, issuer_0 [share 50%, all records]: 4.9 → 0.0; 5.6 → 0.0; 5.9 → 0.0; 6.1 → 0.0; 6.2 → 0.0; 6.4 → 0.0; 6.5 → 0.0; 6.6 → 0.0; 6.8 → 0.0; 7.2 → 0.0
- c6__otcB5_W0__R1, issuer_0 [share 50%, other issuers' devices]: 4.9 → 0.0; 5.6 → 0.0; 5.9 → 0.0; 6.1 → 0.0; 6.2 → 0.0; 6.4 → 0.0; 6.5 → 0.0; 6.6 → 0.0; 6.8 → 0.0; 7.2 → 0.0
- c6__otcB5_W0__R1, issuer_0_with_observer [share 50%, all records]: 5.3 → 0.0; 6.3 → 0.0; 7.1 → 0.0; 7.6 → 0.0; 8.2 → 0.0; 8.9 → 0.0; 9.7 → 0.0; 10.4 → 0.0; 11.6 → 0.0; 14.9 → 0.0
- c6__otcB5_W0__R1, issuer_0_with_observer [share 50%, other issuers' devices]: 5.3 → 0.0; 6.3 → 0.0; 7.1 → 0.0; 7.6 → 0.0; 8.2 → 0.0; 8.9 → 0.0; 9.7 → 0.0; 10.4 → 0.0; 11.6 → 0.0; 14.9 → 0.0
- c6__otcB5_W0__R1, issuer_0_with_first_relay [share 50%, all records]: 5.3 → 0.0; 6.3 → 4.8; 7.1 → 0.0; 7.6 → 0.0; 8.3 → 0.0; 9.0 → 0.0; 9.7 → 0.0; 10.5 → 0.0; 11.8 → 0.0; 14.9 → 0.0
- c6__otcB5_W0__R1, issuer_0_with_first_relay [share 50%, other issuers' devices]: 5.3 → 0.0; 6.3 → 4.8; 7.1 → 0.0; 7.6 → 0.0; 8.3 → 0.0; 9.0 → 0.0; 9.7 → 0.0; 10.5 → 0.0; 11.8 → 0.0; 14.9 → 0.0
- c6__otcB5_W0__R1, issuer_1 [share 30%, all records]: 6.6 → 4.8; 7.8 → 9.5; 8.4 → 14.3; 8.9 → 9.5; 9.2 → 19.0; 9.4 → 4.8; 9.7 → 9.5; 10.0 → 9.5; 10.3 → 19.0; 10.9 → 20.0
- c6__otcB5_W0__R1, issuer_1 [share 30%, its own devices]: 6.6 → 4.8; 7.8 → 9.5; 8.4 → 14.3; 8.9 → 9.5; 9.2 → 19.0; 9.4 → 4.8; 9.7 → 9.5; 10.0 → 9.5; 10.3 → 19.0; 10.9 → 20.0
- c6__otcB5_W0__R1, issuer_1_with_observer [share 30%, all records]: 5.2 → 14.3; 6.1 → 14.3; 6.6 → 0.0; 7.3 → 9.5; 8.1 → 4.8; 8.9 → 23.8; 10.0 → 19.0; 11.1 → 9.5; 12.0 → 14.3; 15.4 → 25.0
- c6__otcB5_W0__R1, issuer_1_with_observer [share 30%, its own devices]: 5.2 → 14.3; 6.1 → 14.3; 6.6 → 0.0; 7.3 → 9.5; 8.1 → 4.8; 8.9 → 23.8; 10.0 → 19.0; 11.1 → 9.5; 12.0 → 14.3; 15.4 → 25.0
- c6__otcB5_W0__R1, issuer_1_with_first_relay [share 30%, all records]: 5.2 → 9.5; 6.2 → 14.3; 6.7 → 0.0; 7.4 → 9.5; 8.2 → 4.8; 8.9 → 23.8; 10.1 → 19.0; 11.0 → 9.5; 12.0 → 14.3; 15.4 → 25.0
- c6__otcB5_W0__R1, issuer_1_with_first_relay [share 30%, its own devices]: 5.2 → 9.5; 6.2 → 14.3; 6.7 → 0.0; 7.4 → 9.5; 8.2 → 4.8; 8.9 → 23.8; 10.1 → 19.0; 11.0 → 9.5; 12.0 → 14.3; 15.4 → 25.0
- c6__otcB5_W0__R1, issuer_1_with_destination: 14.9 → 4.8; 17.1 → 14.3; 18.9 → 9.5; 20.8 → 19.0; 22.9 → 9.5; 25.2 → 19.0; 27.2 → 4.8; 29.9 → 19.0; 33.6 → 23.8; 41.6 → 25.0
- c6__otcB5_W0__R1, issuer_2 [share 20%, all records]: 6.7 → 0.0; 8.3 → 0.0; 9.7 → 0.0; 10.6 → 0.0; 11.2 → 0.0; 11.6 → 0.0; 11.9 → 0.0; 12.3 → 0.0; 12.8 → 0.0; 13.6 → 0.0
- c6__otcB5_W0__R1, issuer_2 [share 20%, other issuers' devices]: 6.7 → 0.0; 8.3 → 0.0; 9.7 → 0.0; 10.6 → 0.0; 11.2 → 0.0; 11.6 → 0.0; 11.9 → 0.0; 12.3 → 0.0; 12.8 → 0.0; 13.6 → 0.0
- c6__otcB5_W0__R1, issuer_2_with_observer [share 20%, all records]: 4.6 → 4.8; 5.2 → 9.5; 5.9 → 9.5; 6.5 → 4.8; 7.3 → 0.0; 8.0 → 0.0; 8.9 → 0.0; 9.8 → 0.0; 11.5 → 0.0; 15.9 → 0.0
- c6__otcB5_W0__R1, issuer_2_with_observer [share 20%, other issuers' devices]: 4.6 → 4.8; 5.2 → 9.5; 5.9 → 9.5; 6.5 → 4.8; 7.3 → 0.0; 8.0 → 0.0; 8.9 → 0.0; 9.8 → 0.0; 11.5 → 0.0; 15.9 → 0.0
- c6__otcB5_W0__R1, issuer_2_with_first_relay [share 20%, all records]: 4.6 → 9.5; 5.3 → 9.5; 5.9 → 4.8; 6.5 → 4.8; 7.2 → 0.0; 7.9 → 0.0; 8.9 → 0.0; 10.0 → 0.0; 11.5 → 0.0; 16.0 → 0.0
- c6__otcB5_W0__R1, issuer_2_with_first_relay [share 20%, other issuers' devices]: 4.6 → 9.5; 5.3 → 9.5; 5.9 → 4.8; 6.5 → 4.8; 7.2 → 0.0; 7.9 → 0.0; 8.9 → 0.0; 10.0 → 0.0; 11.5 → 0.0; 16.0 → 0.0
- c6__otcB5_W0__R100, observer: 2.3 → 1.6; 2.5 → 6.6; 2.6 → 5.0; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB5_W0__R100, first_hop: 2.3 → 2.1; 2.5 → 5.6; 2.7 → 5.1; 2.8 → 1.2; 2.9 → 2.0; 3.0 → 2.2; 3.1 → 0.9; 3.3 → 2.7; 3.6 → 2.1; 4.0 → 0.2
- c6__otcB5_W0__R100, destination: 2.5 → 1.6; 2.7 → 1.6; 2.8 → 1.7; 3.0 → 0.0; 3.1 → 0.0; 3.2 → 0.0; 3.4 → 0.0; 3.6 → 3.3; 3.9 → 3.3; 4.5 → 1.7
- c6__otcB5_W0__R100, destination_keyed: 4.4 → 1.6; 4.9 → 3.3; 5.3 → 5.0; 5.8 → 1.7; 6.5 → 6.7; 7.4 → 10.0; 8.3 → 5.0; 9.6 → 8.3; 10.8 → 11.7; 14.3 → 8.3
- c6__otcB5_W0__R100, first_relay_with_destination: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB5_W0__R100, issuer_0 [share 50%, all records]: 2.9 → 1.6; 3.1 → 3.3; 3.1 → 5.0; 3.2 → 3.3; 3.3 → 3.3; 3.4 → 1.7; 3.4 → 3.3; 3.5 → 1.7; 3.6 → 5.0; 3.8 → 3.3
- c6__otcB5_W0__R100, issuer_0 [share 50%, its own devices]: 2.9 → 2.9; 3.1 → 5.7; 3.1 → 8.6; 3.2 → 5.7; 3.3 → 5.7; 3.4 → 2.9; 3.4 → 5.9; 3.5 → 2.9; 3.6 → 8.8; 3.8 → 5.9
- c6__otcB5_W0__R100, issuer_0 [share 50%, other issuers' devices]: 2.9 → 0.0; 3.1 → 0.0; 3.1 → 0.0; 3.2 → 0.0; 3.3 → 0.0; 3.4 → 0.0; 3.4 → 0.0; 3.5 → 0.0; 3.5 → 0.0; 3.8 → 0.0
- c6__otcB5_W0__R100, issuer_0_with_observer [share 50%, all records]: 4.1 → 1.6; 4.8 → 3.3; 5.1 → 5.0; 5.6 → 5.0; 6.0 → 1.7; 6.3 → 0.0; 6.5 → 1.7; 6.8 → 0.0; 7.3 → 1.7; 8.8 → 0.0
- c6__otcB5_W0__R100, issuer_0_with_observer [share 50%, its own devices]: 4.1 → 2.9; 4.9 → 5.7; 5.1 → 11.4; 5.7 → 5.7; 6.0 → 2.9; 6.3 → 0.0; 6.5 → 2.9; 6.8 → 0.0; 7.4 → 2.9; 9.0 → 0.0
- c6__otcB5_W0__R100, issuer_0_with_observer [share 50%, other issuers' devices]: 4.0 → 0.0; 4.8 → 0.0; 5.1 → 0.0; 5.6 → 0.0; 6.0 → 0.0; 6.3 → 0.0; 6.5 → 0.0; 6.8 → 0.0; 7.2 → 0.0; 8.5 → 0.0
- c6__otcB5_W0__R100, issuer_0_with_first_relay [share 50%, all records]: 4.1 → 3.3; 4.8 → 3.3; 5.1 → 3.3; 5.6 → 8.3; 5.9 → 3.3; 6.3 → 0.0; 6.5 → 1.7; 6.8 → 1.7; 7.3 → 1.7; 9.0 → 0.0
- c6__otcB5_W0__R100, issuer_0_with_first_relay [share 50%, its own devices]: 4.2 → 8.6; 4.9 → 2.9; 5.1 → 8.6; 5.6 → 11.4; 5.9 → 5.7; 6.3 → 0.0; 6.5 → 2.9; 6.8 → 2.9; 7.4 → 2.9; 9.2 → 0.0
- c6__otcB5_W0__R100, issuer_0_with_first_relay [share 50%, other issuers' devices]: 4.0 → 0.0; 4.8 → 0.0; 5.1 → 0.0; 5.5 → 0.0; 6.0 → 0.0; 6.3 → 0.0; 6.5 → 0.0; 6.8 → 0.0; 7.2 → 0.0; 8.6 → 0.0
- c6__otcB5_W0__R100, issuer_0_with_destination: 7.2 → 2.9; 9.1 → 11.4; 10.0 → 2.9; 10.6 → 2.9; 11.2 → 8.6; 11.8 → 2.9; 12.4 → 2.9; 13.3 → 2.9; 14.4 → 2.9; 17.7 → 0.0
- c6__otcB5_W0__R100, issuer_1 [share 30%, all records]: 4.5 → 1.6; 5.1 → 1.6; 5.3 → 0.0; 5.4 → 0.0; 5.5 → 1.7; 5.6 → 1.7; 5.8 → 0.0; 5.9 → 0.0; 6.1 → 3.3; 6.5 → 3.3
- c6__otcB5_W0__R100, issuer_1 [share 30%, its own devices]: 4.6 → 6.7; 5.2 → 6.7; 5.3 → 0.0; 5.4 → 6.7; 5.5 → 0.0; 5.6 → 6.7; 5.8 → 0.0; 5.9 → 0.0; 6.0 → 14.3; 6.3 → 14.3
- c6__otcB5_W0__R100, issuer_1 [share 30%, other issuers' devices]: 4.5 → 0.0; 5.1 → 0.0; 5.3 → 0.0; 5.4 → 0.0; 5.5 → 0.0; 5.6 → 0.0; 5.8 → 0.0; 5.9 → 0.0; 6.1 → 0.0; 6.5 → 0.0
- c6__otcB5_W0__R100, issuer_1_with_observer [share 30%, all records]: 3.1 → 3.3; 3.7 → 1.6; 4.2 → 1.7; 4.5 → 3.3; 5.2 → 1.7; 5.5 → 3.3; 5.7 → 1.7; 6.1 → 3.3; 6.9 → 3.3; 8.4 → 0.0
- c6__otcB5_W0__R100, issuer_1_with_observer [share 30%, its own devices]: 3.3 → 13.3; 3.7 → 6.7; 4.2 → 13.3; 4.6 → 6.7; 5.3 → 6.7; 5.5 → 13.3; 5.7 → 6.7; 6.0 → 13.3; 6.8 → 14.3; 8.1 → 0.0
- c6__otcB5_W0__R100, issuer_1_with_observer [share 30%, other issuers' devices]: 3.1 → 0.0; 3.7 → 0.0; 4.2 → 0.0; 4.5 → 0.0; 5.2 → 0.0; 5.5 → 0.0; 5.7 → 0.0; 6.1 → 0.0; 7.0 → 0.0; 8.5 → 0.0
- c6__otcB5_W0__R100, issuer_1_with_first_relay [share 30%, all records]: 3.1 → 3.3; 3.7 → 1.6; 4.2 → 1.7; 4.6 → 3.3; 5.1 → 1.7; 5.6 → 1.7; 5.7 → 3.3; 6.1 → 3.3; 6.9 → 3.3; 8.4 → 0.0
- c6__otcB5_W0__R100, issuer_1_with_first_relay [share 30%, its own devices]: 3.3 → 13.3; 3.7 → 6.7; 4.2 → 20.0; 4.7 → 0.0; 5.1 → 6.7; 5.6 → 6.7; 5.8 → 13.3; 6.1 → 13.3; 6.8 → 14.3; 8.0 → 0.0
- c6__otcB5_W0__R100, issuer_1_with_first_relay [share 30%, other issuers' devices]: 3.1 → 0.0; 3.7 → 0.0; 4.2 → 0.0; 4.6 → 0.0; 5.2 → 0.0; 5.6 → 0.0; 5.7 → 0.0; 6.1 → 0.0; 7.0 → 0.0; 8.5 → 0.0
- c6__otcB5_W0__R100, issuer_1_with_destination: 10.4 → 13.3; 12.2 → 0.0; 13.1 → 6.7; 14.4 → 20.0; 15.4 → 6.7; 16.8 → 6.7; 18.1 → 13.3; 19.1 → 13.3; 20.9 → 7.1; 25.9 → 0.0
- c6__otcB5_W0__R100, issuer_2 [share 20%, all records]: 5.9 → 0.0; 6.4 → 3.3; 6.8 → 3.3; 7.1 → 0.0; 7.3 → 1.7; 7.4 → 0.0; 7.7 → 1.7; 7.9 → 0.0; 8.2 → 0.0; 8.6 → 0.0
- c6__otcB5_W0__R100, issuer_2 [share 20%, its own devices]: 5.9 → 0.0; 6.3 → 18.2; 6.8 → 18.2; 7.0 → 0.0; 7.2 → 9.1; 7.4 → 0.0; 7.7 → 9.1; 7.9 → 0.0; 8.3 → 0.0; 8.6 → 0.0
- c6__otcB5_W0__R100, issuer_2 [share 20%, other issuers' devices]: 5.9 → 0.0; 6.4 → 0.0; 6.8 → 0.0; 7.1 → 0.0; 7.3 → 0.0; 7.4 → 0.0; 7.7 → 0.0; 7.9 → 0.0; 8.2 → 0.0; 8.5 → 0.0
- c6__otcB5_W0__R100, issuer_2_with_observer [share 20%, all records]: 2.9 → 3.3; 3.6 → 1.6; 4.3 → 0.0; 4.6 → 1.7; 4.9 → 0.0; 5.2 → 0.0; 5.5 → 1.7; 6.0 → 0.0; 6.8 → 1.7; 9.4 → 1.7
- c6__otcB5_W0__R100, issuer_2_with_observer [share 20%, its own devices]: 2.8 → 18.2; 3.4 → 9.1; 4.1 → 0.0; 4.4 → 9.1; 4.8 → 0.0; 5.1 → 0.0; 5.3 → 9.1; 6.1 → 9.1; 7.5 → 10.0; 9.4 → 0.0
- c6__otcB5_W0__R100, issuer_2_with_observer [share 20%, other issuers' devices]: 2.9 → 0.0; 3.6 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 5.0 → 0.0; 5.2 → 0.0; 5.5 → 0.0; 6.0 → 0.0; 6.8 → 0.0; 9.4 → 0.0
- c6__otcB5_W0__R100, issuer_2_with_first_relay [share 20%, all records]: 2.9 → 3.3; 3.6 → 0.0; 4.3 → 0.0; 4.6 → 1.7; 5.0 → 0.0; 5.2 → 0.0; 5.5 → 1.7; 6.0 → 0.0; 6.8 → 1.7; 9.3 → 1.7
- c6__otcB5_W0__R100, issuer_2_with_first_relay [share 20%, its own devices]: 2.8 → 18.2; 3.5 → 0.0; 4.2 → 0.0; 4.5 → 9.1; 4.8 → 0.0; 5.1 → 0.0; 5.3 → 9.1; 6.1 → 9.1; 7.5 → 10.0; 9.4 → 0.0
- c6__otcB5_W0__R100, issuer_2_with_first_relay [share 20%, other issuers' devices]: 2.9 → 0.0; 3.7 → 0.0; 4.4 → 0.0; 4.6 → 0.0; 5.0 → 0.0; 5.2 → 0.0; 5.5 → 0.0; 6.0 → 0.0; 6.8 → 0.0; 9.3 → 0.0
- c6__otcB5_W0__R100, issuer_2_with_destination: 13.3 → 9.1; 15.2 → 0.0; 17.0 → 18.2; 18.6 → 0.0; 20.5 → 0.0; 21.8 → 0.0; 23.8 → 0.0; 26.5 → 0.0; 29.9 → 20.0; 35.3 → 10.0
- c6__otcB100_W0__R1, K records, K = 1: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB100_W0__R1, K records, K = 2: 7.8 → 0.0; 8.8 → 0.0; 9.6 → 27.3; 10.5 → 27.3; 11.0 → 10.0; 11.9 → 10.0; 12.8 → 10.0; 14.0 → 0.0; 16.1 → 20.0; 22.1 → 10.0
- c6__otcB100_W0__R1, K records, K = 3: 11.6 → 0.0; 14.5 → 28.6; 16.8 → 14.3; 17.9 → 14.3; 18.8 → 14.3; 20.0 → 14.3; 21.1 → 28.6; 23.8 → 28.6; 28.4 → 28.6; 35.8 → 16.7
- c6__otcB100_W0__R1, K records, K = 5: 25.6 → 20.0; 29.4 → 0.0; 32.2 → 50.0; 36.2 → 25.0; 38.7 → 0.0; 44.3 → 75.0; 50.1 → 25.0; 57.5 → 100.0; 66.6 → 50.0; 73.5 → 25.0
- c6__otcB100_W0__R1, K records, K = 10: 52.3 → 50.0; 72.5 → 100.0; 80.7 → 0.0; 88.1 → 100.0; 94.8 → 100.0; 96.7 → 100.0; 97.6 → 100.0; 99.1 → 100.0; 99.7 → 100.0; 100.0 → 100.0
- c6__otcB100_W0__R1, K records, K = 20: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB100_W0__R100, K records, K = 1: 2.3 → 1.6; 2.5 → 4.9; 2.6 → 6.7; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB100_W0__R100, K records, K = 2: 4.5 → 0.0; 5.4 → 3.6; 5.8 → 0.0; 6.3 → 0.0; 6.8 → 0.0; 7.6 → 3.7; 8.5 → 3.7; 9.4 → 11.1; 10.8 → 0.0; 16.1 → 0.0
- c6__otcB100_W0__R100, K records, K = 3: 7.8 → 17.6; 9.4 → 11.8; 10.3 → 11.8; 11.3 → 5.9; 12.4 → 11.8; 13.8 → 0.0; 15.8 → 5.9; 18.4 → 5.9; 21.3 → 6.2; 34.0 → 6.2
- c6__otcB100_W0__R100, K records, K = 5: 16.7 → 12.5; 22.9 → 12.5; 25.7 → 0.0; 29.0 → 28.6; 31.6 → 14.3; 35.4 → 0.0; 38.2 → 28.6; 40.4 → 14.3; 45.4 → 14.3; 64.2 → 14.3
- c6__otcB1_W0__R1, K records, K = 1: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB1_W0__R1, K records, K = 2: 7.8 → 0.0; 8.8 → 0.0; 9.6 → 27.3; 10.5 → 27.3; 11.0 → 10.0; 11.9 → 10.0; 12.8 → 10.0; 14.0 → 0.0; 16.1 → 20.0; 22.1 → 10.0
- c6__otcB1_W0__R1, K records, K = 3: 11.6 → 0.0; 14.5 → 28.6; 16.8 → 14.3; 17.9 → 14.3; 18.8 → 14.3; 20.0 → 14.3; 21.1 → 28.6; 23.8 → 28.6; 28.4 → 28.6; 35.8 → 16.7
- c6__otcB1_W0__R1, K records, K = 5: 25.6 → 20.0; 29.4 → 0.0; 32.2 → 50.0; 36.2 → 25.0; 38.7 → 0.0; 44.3 → 75.0; 50.1 → 25.0; 57.5 → 100.0; 66.6 → 50.0; 73.5 → 25.0
- c6__otcB1_W0__R1, K records, K = 10: 52.3 → 50.0; 72.5 → 100.0; 80.7 → 0.0; 88.1 → 100.0; 94.8 → 100.0; 96.7 → 100.0; 97.6 → 100.0; 99.1 → 100.0; 99.7 → 100.0; 100.0 → 100.0
- c6__otcB1_W0__R1, K records, K = 20: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB1_W0__R100, K records, K = 1: 2.3 → 1.6; 2.5 → 4.9; 2.6 → 6.7; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB1_W0__R100, K records, K = 2: 4.5 → 0.0; 5.4 → 3.6; 5.8 → 0.0; 6.3 → 0.0; 6.8 → 0.0; 7.6 → 3.7; 8.5 → 3.7; 9.4 → 11.1; 10.8 → 0.0; 16.1 → 0.0
- c6__otcB1_W0__R100, K records, K = 3: 7.8 → 17.6; 9.4 → 11.8; 10.3 → 11.8; 11.3 → 5.9; 12.4 → 11.8; 13.8 → 0.0; 15.8 → 5.9; 18.4 → 5.9; 21.3 → 6.2; 34.0 → 6.2
- c6__otcB1_W0__R100, K records, K = 5: 16.7 → 12.5; 22.9 → 12.5; 25.7 → 0.0; 29.0 → 28.6; 31.6 → 14.3; 35.4 → 0.0; 38.2 → 28.6; 40.4 → 14.3; 45.4 → 14.3; 64.2 → 14.3
- c6__otcB20_W0__R1, K records, K = 1: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB20_W0__R1, K records, K = 2: 7.8 → 0.0; 8.8 → 0.0; 9.6 → 27.3; 10.5 → 27.3; 11.0 → 10.0; 11.9 → 10.0; 12.8 → 10.0; 14.0 → 0.0; 16.1 → 20.0; 22.1 → 10.0
- c6__otcB20_W0__R1, K records, K = 3: 11.6 → 0.0; 14.5 → 28.6; 16.8 → 14.3; 17.9 → 14.3; 18.8 → 14.3; 20.0 → 14.3; 21.1 → 28.6; 23.8 → 28.6; 28.4 → 28.6; 35.8 → 16.7
- c6__otcB20_W0__R1, K records, K = 5: 25.6 → 20.0; 29.4 → 0.0; 32.2 → 50.0; 36.2 → 25.0; 38.7 → 0.0; 44.3 → 75.0; 50.1 → 25.0; 57.5 → 100.0; 66.6 → 50.0; 73.5 → 25.0
- c6__otcB20_W0__R1, K records, K = 10: 52.3 → 50.0; 72.5 → 100.0; 80.7 → 0.0; 88.1 → 100.0; 94.8 → 100.0; 96.7 → 100.0; 97.6 → 100.0; 99.1 → 100.0; 99.7 → 100.0; 100.0 → 100.0
- c6__otcB20_W0__R1, K records, K = 20: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB20_W0__R100, K records, K = 1: 2.3 → 1.6; 2.5 → 4.9; 2.6 → 6.7; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB20_W0__R100, K records, K = 2: 4.5 → 0.0; 5.4 → 3.6; 5.8 → 0.0; 6.3 → 0.0; 6.8 → 0.0; 7.6 → 3.7; 8.5 → 3.7; 9.4 → 11.1; 10.8 → 0.0; 16.1 → 0.0
- c6__otcB20_W0__R100, K records, K = 3: 7.8 → 17.6; 9.4 → 11.8; 10.3 → 11.8; 11.3 → 5.9; 12.4 → 11.8; 13.8 → 0.0; 15.8 → 5.9; 18.4 → 5.9; 21.3 → 6.2; 34.0 → 6.2
- c6__otcB20_W0__R100, K records, K = 5: 16.7 → 12.5; 22.9 → 12.5; 25.7 → 0.0; 29.0 → 28.6; 31.6 → 14.3; 35.4 → 0.0; 38.2 → 28.6; 40.4 → 14.3; 45.4 → 14.3; 64.2 → 14.3
- c6__otcB5_W0__R1, K records, K = 1: 4.0 → 0.0; 4.4 → 4.8; 4.6 → 0.0; 4.8 → 14.3; 5.0 → 9.5; 5.3 → 4.8; 5.5 → 9.5; 5.8 → 14.3; 6.2 → 9.5; 7.5 → 10.0
- c6__otcB5_W0__R1, K records, K = 2: 7.8 → 0.0; 8.8 → 0.0; 9.6 → 27.3; 10.5 → 27.3; 11.0 → 10.0; 11.9 → 10.0; 12.8 → 10.0; 14.0 → 0.0; 16.1 → 20.0; 22.1 → 10.0
- c6__otcB5_W0__R1, K records, K = 3: 11.6 → 0.0; 14.5 → 28.6; 16.8 → 14.3; 17.9 → 14.3; 18.8 → 14.3; 20.0 → 14.3; 21.1 → 28.6; 23.8 → 28.6; 28.4 → 28.6; 35.8 → 16.7
- c6__otcB5_W0__R1, K records, K = 5: 25.6 → 20.0; 29.4 → 0.0; 32.2 → 50.0; 36.2 → 25.0; 38.7 → 0.0; 44.3 → 75.0; 50.1 → 25.0; 57.5 → 100.0; 66.6 → 50.0; 73.5 → 25.0
- c6__otcB5_W0__R1, K records, K = 10: 52.3 → 50.0; 72.5 → 100.0; 80.7 → 0.0; 88.1 → 100.0; 94.8 → 100.0; 96.7 → 100.0; 97.6 → 100.0; 99.1 → 100.0; 99.7 → 100.0; 100.0 → 100.0
- c6__otcB5_W0__R1, K records, K = 20: 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0; 100.0 → 100.0
- c6__otcB5_W0__R100, K records, K = 1: 2.3 → 1.6; 2.5 → 4.9; 2.6 → 6.7; 2.7 → 1.7; 2.8 → 1.7; 2.9 → 0.0; 3.1 → 1.7; 3.3 → 1.7; 3.6 → 3.3; 4.0 → 0.0
- c6__otcB5_W0__R100, K records, K = 2: 4.5 → 0.0; 5.4 → 3.6; 5.8 → 0.0; 6.3 → 0.0; 6.8 → 0.0; 7.6 → 3.7; 8.5 → 3.7; 9.4 → 11.1; 10.8 → 0.0; 16.1 → 0.0
- c6__otcB5_W0__R100, K records, K = 3: 7.8 → 17.6; 9.4 → 11.8; 10.3 → 11.8; 11.3 → 5.9; 12.4 → 11.8; 13.8 → 0.0; 15.8 → 5.9; 18.4 → 5.9; 21.3 → 6.2; 34.0 → 6.2
- c6__otcB5_W0__R100, K records, K = 5: 16.7 → 12.5; 22.9 → 12.5; 25.7 → 0.0; 29.0 → 28.6; 31.6 → 14.3; 35.4 → 0.0; 38.2 → 28.6; 40.4 → 14.3; 45.4 → 14.3; 64.2 → 14.3
- c6_dest__cp_delay1800__R1, observer [all records]: 3.1 → 9.1; 3.5 → 0.0; 3.7 → 4.8; 3.8 → 0.0; 3.9 → 0.0; 4.1 → 9.5; 4.3 → 0.0; 4.6 → 0.0; 5.0 → 0.0; 5.8 → 4.8
- c6_dest__cp_delay1800__R1, observer [records the node delayed]: 3.2 → 0.0; 3.5 → 0.0; 3.7 → 0.0; 3.9 → 0.0; 4.1 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.8 → 0.0; 5.0 → 0.0; 5.6 → 0.0
- c6_dest__cp_delay1800__R1, observer [other records]: 3.1 → 10.5; 3.5 → 0.0; 3.7 → 5.6; 3.8 → 0.0; 3.9 → 0.0; 4.1 → 11.1; 4.3 → 0.0; 4.6 → 0.0; 5.0 → 0.0; 5.8 → 5.6
- c6_dest__cp_delay1800__R1, delaying_destination: 3.4 → 0.0; 3.8 → 33.3; 4.0 → 0.0; 4.1 → 0.0; 4.3 → 0.0; 4.5 → 0.0; 5.0 → 0.0; 5.3 → 0.0; 5.6 → 33.3; 6.0 → 33.3
- c6_dest__cp_delay1800__R100, observer [all records]: 1.8 → 1.9; 2.0 → 2.2; 2.1 → 1.8; 2.1 → 2.3; 2.2 → 2.4; 2.3 → 2.7; 2.4 → 1.7; 2.5 → 3.1; 2.7 → 2.7; 3.1 → 3.5
- c6_dest__cp_delay1800__R100, observer [records the node delayed]: 1.8 → 0.4; 2.0 → 0.8; 2.1 → 0.4; 2.1 → 0.8; 2.2 → 0.8; 2.3 → 0.0; 2.4 → 0.8; 2.5 → 0.8; 2.7 → 0.8; 3.1 → 0.0
- c6_dest__cp_delay1800__R100, observer [other records]: 1.8 → 2.1; 2.0 → 2.4; 2.1 → 2.1; 2.1 → 2.6; 2.2 → 2.5; 2.3 → 3.1; 2.4 → 1.8; 2.5 → 3.4; 2.7 → 2.9; 3.1 → 4.0
- c6_dest__cp_delay1800__R100, delaying_destination: 1.9 → 0.4; 2.1 → 0.8; 2.2 → 3.3; 2.3 → 0.4; 2.4 → 3.8; 2.5 → 3.3; 2.6 → 2.1; 2.8 → 1.3; 3.0 → 2.5; 3.6 → 4.6
- c6_dest__cp_delay600__R1, observer [all records]: 3.1 → 13.6; 3.5 → 0.0; 3.7 → 4.8; 3.8 → 0.0; 3.9 → 0.0; 4.1 → 14.3; 4.3 → 0.0; 4.6 → 0.0; 5.0 → 0.0; 5.8 → 4.8
- c6_dest__cp_delay600__R1, observer [records the node delayed]: 3.1 → 25.0; 3.4 → 0.0; 3.7 → 0.0; 3.8 → 0.0; 4.1 → 33.3; 4.1 → 0.0; 4.3 → 0.0; 4.6 → 0.0; 4.9 → 0.0; 5.5 → 0.0
- c6_dest__cp_delay600__R1, observer [other records]: 3.1 → 10.5; 3.5 → 0.0; 3.7 → 5.6; 3.8 → 0.0; 3.9 → 0.0; 4.1 → 11.1; 4.3 → 0.0; 4.6 → 0.0; 5.0 → 0.0; 5.8 → 5.6
- c6_dest__cp_delay600__R1, delaying_destination: 3.4 → 0.0; 3.8 → 33.3; 4.0 → 0.0; 4.2 → 0.0; 4.4 → 0.0; 4.5 → 0.0; 5.0 → 0.0; 5.3 → 0.0; 5.6 → 33.3; 6.0 → 33.3
- c6_dest__cp_delay600__R100, observer [all records]: 1.8 → 2.1; 2.0 → 2.2; 2.1 → 1.9; 2.1 → 2.4; 2.2 → 2.3; 2.3 → 2.9; 2.4 → 1.8; 2.5 → 3.0; 2.7 → 3.1; 3.1 → 3.8
- c6_dest__cp_delay600__R100, observer [records the node delayed]: 1.8 → 2.1; 2.0 → 0.8; 2.1 → 1.2; 2.1 → 1.3; 2.2 → 1.7; 2.3 → 1.3; 2.4 → 1.7; 2.5 → 0.0; 2.7 → 4.2; 3.0 → 2.9
- c6_dest__cp_delay600__R100, observer [other records]: 1.8 → 2.1; 2.0 → 2.4; 2.1 → 2.1; 2.1 → 2.6; 2.2 → 2.5; 2.3 → 3.1; 2.4 → 1.8; 2.5 → 3.4; 2.7 → 2.9; 3.1 → 4.0
- c6_dest__cp_delay600__R100, delaying_destination: 1.9 → 0.4; 2.1 → 0.8; 2.2 → 4.2; 2.3 → 0.4; 2.4 → 3.3; 2.5 → 3.3; 2.7 → 2.1; 2.8 → 1.7; 3.0 → 2.5; 3.6 → 4.6
- c6_dest__cp_drop_m1800__R1, observer [all records]: 3.1 → 0.0; 3.3 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 3.9 → 0.0; 4.2 → 14.3; 4.4 → 4.8; 4.7 → 9.5; 5.6 → 4.8
- c6_dest__cp_drop_m1800__R1, observer [other records]: 3.1 → 0.0; 3.3 → 0.0; 3.5 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 3.9 → 0.0; 4.2 → 14.3; 4.4 → 4.8; 4.7 → 9.5; 5.6 → 4.8
- c6_dest__cp_drop_m1800__R1, drop_link: 5.0 → 0.0; 5.6 → 0.0; 6.1 → 0.0; 6.9 → 0.0; 7.2 → 0.0; 7.6 → 0.0; 8.2 → 0.0; 8.9 → 0.0; 11.6 → 0.0; 17.3 → 66.7
- c6_dest__cp_drop_m1800__R100, observer [all records]: 1.7 → 2.2; 1.9 → 2.0; 2.0 → 2.5; 2.0 → 2.0; 2.1 → 2.3; 2.2 → 2.2; 2.3 → 2.4; 2.4 → 2.9; 2.5 → 3.9; 2.9 → 3.3
- c6_dest__cp_drop_m1800__R100, observer [other records]: 1.7 → 2.2; 1.9 → 2.0; 2.0 → 2.5; 2.0 → 2.0; 2.1 → 2.3; 2.2 → 2.2; 2.3 → 2.4; 2.4 → 2.9; 2.5 → 3.9; 2.9 → 3.3
- c6_dest__cp_drop_m1800__R100, drop_link: 3.3 → 2.1; 3.7 → 4.3; 4.0 → 4.3; 4.3 → 6.0; 4.6 → 6.0; 4.9 → 6.0; 5.2 → 6.4; 5.6 → 6.8; 6.3 → 8.5; 7.9 → 10.3
- c6_dest__cp_drop_m21600__R1, observer [all records]: 3.0 → 9.1; 3.3 → 9.1; 3.5 → 0.0; 3.7 → 0.0; 3.9 → 4.5; 4.1 → 0.0; 4.2 → 4.5; 4.4 → 4.5; 4.7 → 18.2; 5.5 → 4.5
- c6_dest__cp_drop_m21600__R1, observer [other records]: 3.0 → 9.1; 3.3 → 9.1; 3.5 → 0.0; 3.7 → 0.0; 3.9 → 4.5; 4.1 → 0.0; 4.2 → 4.5; 4.4 → 4.5; 4.7 → 18.2; 5.5 → 4.5
- c6_dest__cp_drop_m21600__R1, drop_link: 5.9 → 0.0; 6.5 → 50.0; 7.1 → 0.0; 8.7 → 0.0; 9.3 → 0.0; 10.3 → 0.0; 12.2 → 50.0; 13.2 → 0.0; 13.9 → 0.0; 14.5 → 0.0
- c6_dest__cp_drop_m21600__R100, observer [all records]: 1.7 → 1.7; 1.9 → 2.2; 2.0 → 1.6; 2.0 → 2.2; 2.1 → 2.4; 2.2 → 2.5; 2.3 → 2.6; 2.4 → 2.7; 2.5 → 2.8; 2.9 → 2.7
- c6_dest__cp_drop_m21600__R100, observer [other records]: 1.7 → 1.7; 1.9 → 2.2; 2.0 → 1.6; 2.0 → 2.2; 2.1 → 2.4; 2.2 → 2.5; 2.3 → 2.6; 2.4 → 2.7; 2.5 → 2.8; 2.9 → 2.7
- c6_dest__cp_drop_m21600__R100, drop_link: 3.2 → 4.2; 3.7 → 3.3; 4.0 → 2.8; 4.3 → 3.3; 4.5 → 6.6; 4.8 → 7.6; 5.1 → 4.7; 5.5 → 7.6; 6.1 → 9.0; 7.8 → 6.2
- c6_dest__cp_drop_m3600__R1, observer [all records]: 3.0 → 0.0; 3.3 → 9.1; 3.5 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 4.0 → 4.5; 4.2 → 4.8; 4.4 → 0.0; 4.6 → 4.8; 5.3 → 0.0
- c6_dest__cp_drop_m3600__R1, observer [other records]: 3.0 → 0.0; 3.3 → 9.1; 3.5 → 0.0; 3.6 → 0.0; 3.8 → 0.0; 4.0 → 4.5; 4.2 → 4.8; 4.4 → 0.0; 4.6 → 4.8; 5.3 → 0.0
- c6_dest__cp_drop_m3600__R1, drop_link: 5.2 → 0.0; 6.3 → 33.3; 6.5 → 0.0; 7.1 → 0.0; 7.6 → 0.0; 8.2 → 0.0; 9.5 → 0.0; 11.3 → 0.0; 11.9 → 0.0; 14.3 → 0.0
- c6_dest__cp_drop_m3600__R100, observer [all records]: 1.7 → 1.8; 1.9 → 2.2; 2.0 → 2.6; 2.0 → 2.4; 2.1 → 2.1; 2.2 → 2.8; 2.3 → 2.6; 2.3 → 2.4; 2.5 → 3.7; 2.9 → 3.3
- c6_dest__cp_drop_m3600__R100, observer [other records]: 1.7 → 1.8; 1.9 → 2.2; 2.0 → 2.6; 2.0 → 2.4; 2.1 → 2.1; 2.2 → 2.8; 2.3 → 2.6; 2.3 → 2.4; 2.5 → 3.7; 2.9 → 3.3
- c6_dest__cp_drop_m3600__R100, drop_link: 3.3 → 2.6; 3.7 → 3.8; 4.0 → 3.0; 4.3 → 3.0; 4.5 → 4.3; 4.8 → 6.8; 5.1 → 4.3; 5.6 → 7.3; 6.2 → 7.3; 7.8 → 12.4
- c6_dest__cp_drop_m7200__R1, observer [all records]: 3.0 → 4.5; 3.3 → 0.0; 3.5 → 4.5; 3.6 → 0.0; 3.8 → 0.0; 4.0 → 4.5; 4.2 → 4.5; 4.4 → 0.0; 4.7 → 4.5; 5.4 → 18.2
- c6_dest__cp_drop_m7200__R1, observer [other records]: 3.0 → 4.5; 3.3 → 0.0; 3.5 → 4.5; 3.6 → 0.0; 3.8 → 0.0; 4.0 → 4.5; 4.2 → 4.5; 4.4 → 0.0; 4.7 → 4.5; 5.4 → 18.2
- c6_dest__cp_drop_m7200__R1, drop_link: 6.2 → 0.0; 6.7 → 0.0; 7.0 → 0.0; 7.1 → 0.0; 7.4 → 50.0; 7.8 → 0.0; 8.6 → 0.0; 9.9 → 0.0; 12.3 → 0.0; 13.2 → 0.0
- c6_dest__cp_drop_m7200__R100, observer [all records]: 1.7 → 2.0; 1.9 → 1.7; 1.9 → 1.9; 2.0 → 2.7; 2.1 → 2.4; 2.2 → 2.2; 2.3 → 2.4; 2.4 → 2.9; 2.5 → 3.2; 2.9 → 3.6
- c6_dest__cp_drop_m7200__R100, observer [other records]: 1.7 → 2.0; 1.9 → 1.7; 1.9 → 1.9; 2.0 → 2.7; 2.1 → 2.4; 2.2 → 2.2; 2.3 → 2.4; 2.4 → 2.9; 2.5 → 3.2; 2.9 → 3.6
- c6_dest__cp_drop_m7200__R100, drop_link: 3.2 → 3.1; 3.7 → 3.9; 4.0 → 4.4; 4.2 → 5.7; 4.5 → 7.4; 4.8 → 7.9; 5.1 → 6.6; 5.5 → 7.9; 6.1 → 6.6; 7.7 → 11.0
- c6_dest__otcL_delay1800__R1, observer [all records]: 3.9 → 4.5; 4.3 → 4.5; 4.5 → 0.0; 4.8 → 14.3; 5.0 → 4.8; 5.3 → 4.8; 5.6 → 4.8; 5.9 → 4.8; 6.4 → 4.8; 7.5 → 0.0
- c6_dest__otcL_delay1800__R1, observer [records the node delayed]: 4.3 → 0.0; 4.6 → 0.0; 5.0 → 0.0; 5.1 → 0.0; 5.1 → 0.0; 5.3 → 0.0; 6.0 → 0.0; 6.3 → 0.0; 6.5 → 0.0
- c6_dest__otcL_delay1800__R1, observer [other records]: 3.9 → 4.8; 4.3 → 4.8; 4.5 → 0.0; 4.8 → 14.3; 5.0 → 5.0; 5.3 → 5.0; 5.6 → 5.0; 5.9 → 5.0; 6.4 → 5.0; 7.5 → 0.0
- c6_dest__otcL_delay1800__R1, delaying_destination: 5.0 → 0.0; 5.0 → 0.0; 5.6 → 0.0; 5.6 → 0.0; 6.0 → 0.0; 6.1 → 0.0; 7.0 → 100.0; 7.4 → 0.0; 8.4 → 0.0
- c6_dest__otcL_delay1800__R100, observer [all records]: 2.3 → 2.5; 2.5 → 2.2; 2.6 → 2.6; 2.7 → 2.1; 2.9 → 2.8; 3.0 → 2.7; 3.1 → 2.8; 3.3 → 3.2; 3.5 → 4.5; 4.0 → 4.4
- c6_dest__otcL_delay1800__R100, observer [records the node delayed]: 2.3 → 0.0; 2.5 → 0.0; 2.6 → 0.0; 2.8 → 0.0; 2.9 → 0.9; 3.0 → 0.9; 3.1 → 0.0; 3.3 → 1.9; 3.5 → 0.0; 4.0 → 0.0
- c6_dest__otcL_delay1800__R100, observer [other records]: 2.3 → 2.6; 2.5 → 2.4; 2.6 → 2.8; 2.7 → 2.3; 2.9 → 2.9; 3.0 → 2.7; 3.1 → 3.0; 3.3 → 3.3; 3.5 → 4.7; 4.0 → 4.6
- c6_dest__otcL_delay1800__R100, delaying_destination: 2.5 → 0.9; 2.7 → 3.7; 2.9 → 1.9; 3.0 → 3.7; 3.1 → 1.9; 3.3 → 0.9; 3.4 → 3.7; 3.6 → 4.7; 3.9 → 2.8; 4.6 → 2.8
- c6_dest__otcL_delay600__R1, observer [all records]: 3.9 → 4.5; 4.3 → 4.5; 4.5 → 0.0; 4.8 → 14.3; 5.0 → 4.8; 5.3 → 4.8; 5.6 → 4.8; 5.9 → 4.8; 6.4 → 4.8; 7.5 → 0.0
- c6_dest__otcL_delay600__R1, observer [records the node delayed]: 4.2 → 0.0; 4.4 → 0.0; 4.7 → 0.0; 5.4 → 0.0; 5.5 → 0.0; 5.6 → 0.0; 5.7 → 0.0; 6.0 → 0.0; 6.6 → 0.0
- c6_dest__otcL_delay600__R1, observer [other records]: 3.9 → 4.8; 4.3 → 4.8; 4.5 → 0.0; 4.8 → 14.3; 5.0 → 5.0; 5.3 → 5.0; 5.6 → 5.0; 5.9 → 5.0; 6.4 → 5.0; 7.5 → 0.0
- c6_dest__otcL_delay600__R1, delaying_destination: 5.0 → 0.0; 5.0 → 0.0; 5.6 → 0.0; 5.6 → 0.0; 6.0 → 0.0; 6.1 → 0.0; 7.0 → 100.0; 7.4 → 0.0; 8.4 → 0.0
- c6_dest__otcL_delay600__R100, observer [all records]: 2.3 → 2.6; 2.5 → 2.3; 2.6 → 2.6; 2.7 → 2.2; 2.9 → 2.8; 3.0 → 2.7; 3.1 → 2.9; 3.3 → 3.2; 3.5 → 4.6; 4.0 → 4.4
- c6_dest__otcL_delay600__R100, observer [records the node delayed]: 2.3 → 2.8; 2.5 → 0.0; 2.6 → 0.0; 2.8 → 0.9; 2.9 → 0.9; 3.0 → 0.9; 3.1 → 1.9; 3.3 → 1.9; 3.5 → 1.9; 4.1 → 0.0
- c6_dest__otcL_delay600__R100, observer [other records]: 2.3 → 2.6; 2.5 → 2.4; 2.6 → 2.8; 2.7 → 2.3; 2.9 → 2.9; 3.0 → 2.7; 3.1 → 3.0; 3.3 → 3.3; 3.5 → 4.7; 4.0 → 4.6
- c6_dest__otcL_delay600__R100, delaying_destination: 2.5 → 0.9; 2.7 → 3.7; 2.9 → 1.9; 3.0 → 3.7; 3.1 → 1.9; 3.3 → 0.9; 3.4 → 3.7; 3.6 → 4.7; 3.9 → 2.8; 4.6 → 2.8
- c6_dest__otcL_drop_m1800__R1, observer [all records]: 3.9 → 4.5; 4.2 → 4.5; 4.5 → 0.0; 4.7 → 19.0; 4.9 → 9.5; 5.1 → 0.0; 5.4 → 9.5; 5.7 → 4.8; 6.1 → 0.0; 7.2 → 0.0
- c6_dest__otcL_drop_m1800__R1, observer [other records]: 3.9 → 4.5; 4.2 → 4.5; 4.5 → 0.0; 4.7 → 19.0; 4.9 → 9.5; 5.1 → 0.0; 5.4 → 9.5; 5.7 → 4.8; 6.1 → 0.0; 7.2 → 0.0
- c6_dest__otcL_drop_m1800__R1, drop_link: 8.6 → 0.0; 11.6 → 0.0; 12.1 → 0.0; 12.4 → 0.0; 13.1 → 0.0; 13.8 → 0.0; 14.9 → 0.0; 15.1 → 100.0; 17.8 → 0.0
- c6_dest__otcL_drop_m1800__R100, observer [all records]: 2.2 → 2.1; 2.4 → 2.5; 2.5 → 2.6; 2.7 → 2.2; 2.8 → 3.4; 2.9 → 3.4; 3.0 → 2.5; 3.2 → 3.1; 3.4 → 4.5; 3.9 → 4.9
- c6_dest__otcL_drop_m1800__R100, observer [other records]: 2.2 → 2.1; 2.4 → 2.5; 2.5 → 2.6; 2.7 → 2.2; 2.8 → 3.4; 2.9 → 3.4; 3.0 → 2.5; 3.2 → 3.1; 3.4 → 4.5; 3.9 → 4.9
- c6_dest__otcL_drop_m1800__R100, drop_link: 4.9 → 3.8; 5.7 → 2.9; 6.2 → 3.8; 6.6 → 7.6; 7.1 → 5.7; 7.6 → 6.7; 8.1 → 5.7; 9.0 → 10.5; 10.3 → 7.6; 13.3 → 13.3
- c6_dest__otcL_drop_m21600__R1, observer [all records]: 4.0 → 8.7; 4.3 → 0.0; 4.5 → 9.1; 4.7 → 4.5; 5.0 → 13.6; 5.3 → 4.5; 5.5 → 4.5; 5.8 → 0.0; 6.2 → 4.5; 7.2 → 13.6
- c6_dest__otcL_drop_m21600__R1, observer [other records]: 4.0 → 8.7; 4.3 → 0.0; 4.5 → 9.1; 4.7 → 4.5; 5.0 → 13.6; 5.3 → 4.5; 5.5 → 4.5; 5.8 → 0.0; 6.2 → 4.5; 7.2 → 13.6
- c6_dest__otcL_drop_m21600__R1, drop_link: 8.0 → 0.0; 9.2 → 0.0; 9.8 → 0.0; 11.7 → 0.0; 11.8 → 0.0; 12.9 → 0.0; 16.6 → 0.0; 17.5 → 0.0; 18.0 → 0.0; 27.0 → 100.0
- c6_dest__otcL_drop_m21600__R100, observer [all records]: 2.2 → 2.4; 2.4 → 2.2; 2.6 → 2.5; 2.7 → 2.0; 2.8 → 2.3; 2.9 → 2.2; 3.0 → 3.3; 3.2 → 3.0; 3.4 → 2.7; 3.9 → 3.6
- c6_dest__otcL_drop_m21600__R100, observer [other records]: 2.2 → 2.4; 2.4 → 2.2; 2.6 → 2.5; 2.7 → 2.0; 2.8 → 2.3; 2.9 → 2.2; 3.0 → 3.3; 3.2 → 3.0; 3.4 → 2.7; 3.9 → 3.6
- c6_dest__otcL_drop_m21600__R100, drop_link: 5.0 → 5.3; 5.8 → 8.5; 6.3 → 12.9; 6.7 → 4.3; 7.2 → 5.4; 7.8 → 9.7; 8.4 → 6.5; 9.1 → 5.4; 10.2 → 17.2; 13.2 → 12.9
- c6_dest__otcL_drop_m3600__R1, observer [all records]: 3.7 → 0.0; 4.2 → 4.5; 4.5 → 13.6; 4.8 → 0.0; 5.1 → 4.5; 5.3 → 4.8; 5.6 → 9.5; 5.9 → 4.8; 6.3 → 9.5; 7.7 → 23.8
- c6_dest__otcL_drop_m3600__R1, observer [other records]: 3.7 → 0.0; 4.2 → 4.5; 4.5 → 13.6; 4.8 → 0.0; 5.1 → 4.5; 5.3 → 4.8; 5.6 → 9.5; 5.9 → 4.8; 6.3 → 9.5; 7.7 → 23.8
- c6_dest__otcL_drop_m3600__R1, drop_link: 8.7 → 0.0; 9.7 → 0.0; 10.3 → 0.0; 11.8 → 100.0; 12.5 → 0.0; 13.2 → 0.0; 15.3 → 0.0; 16.1 → 100.0; 20.4 → 0.0
- c6_dest__otcL_drop_m3600__R100, observer [all records]: 2.2 → 2.5; 2.4 → 2.7; 2.6 → 2.3; 2.7 → 2.9; 2.8 → 3.0; 2.9 → 3.6; 3.1 → 3.2; 3.2 → 3.4; 3.5 → 3.5; 4.0 → 3.5
- c6_dest__otcL_drop_m3600__R100, observer [other records]: 2.2 → 2.5; 2.4 → 2.7; 2.6 → 2.3; 2.7 → 2.9; 2.8 → 3.0; 2.9 → 3.6; 3.1 → 3.2; 3.2 → 3.4; 3.5 → 3.5; 4.0 → 3.5
- c6_dest__otcL_drop_m3600__R100, drop_link: 5.0 → 5.7; 5.7 → 2.8; 6.3 → 6.6; 6.7 → 3.8; 7.2 → 4.8; 7.7 → 5.7; 8.2 → 3.8; 9.1 → 13.3; 10.5 → 8.6; 13.8 → 10.5
- c6_dest__otcL_drop_m7200__R1, observer [all records]: 3.9 → 4.3; 4.3 → 4.5; 4.5 → 9.1; 4.8 → 9.1; 5.0 → 9.1; 5.2 → 0.0; 5.5 → 9.1; 5.8 → 0.0; 6.4 → 9.1; 8.0 → 13.6
- c6_dest__otcL_drop_m7200__R1, observer [other records]: 3.9 → 4.3; 4.3 → 4.5; 4.5 → 9.1; 4.8 → 9.1; 5.0 → 9.1; 5.2 → 0.0; 5.5 → 9.1; 5.8 → 0.0; 6.4 → 9.1; 8.0 → 13.6
- c6_dest__otcL_drop_m7200__R1, drop_link: 8.5 → 0.0; 9.2 → 100.0; 12.5 → 100.0; 12.7 → 0.0; 13.0 → 0.0; 14.0 → 0.0; 14.5 → 0.0; 17.0 → 0.0; 17.2 → 0.0; 18.3 → 0.0
- c6_dest__otcL_drop_m7200__R100, observer [all records]: 2.2 → 2.3; 2.4 → 2.2; 2.5 → 2.1; 2.6 → 2.7; 2.8 → 3.2; 2.9 → 3.6; 3.0 → 3.3; 3.2 → 3.7; 3.4 → 3.4; 4.0 → 4.0
- c6_dest__otcL_drop_m7200__R100, observer [other records]: 2.2 → 2.3; 2.4 → 2.2; 2.5 → 2.1; 2.6 → 2.7; 2.8 → 3.2; 2.9 → 3.6; 3.0 → 3.3; 3.2 → 3.7; 3.4 → 3.4; 4.0 → 4.0
- c6_dest__otcL_drop_m7200__R100, drop_link: 5.0 → 7.5; 5.7 → 3.8; 6.2 → 4.8; 6.7 → 4.8; 7.2 → 5.7; 7.8 → 7.6; 8.4 → 10.5; 9.1 → 8.6; 10.3 → 11.4; 13.5 → 17.1
- c6_dest__otc_delay1800__R1, observer [all records]: 3.8 → 0.0; 4.2 → 4.5; 4.5 → 4.8; 4.8 → 0.0; 5.0 → 0.0; 5.2 → 9.5; 5.5 → 9.5; 5.7 → 0.0; 6.1 → 9.5; 7.0 → 9.5
- c6_dest__otc_delay1800__R1, observer [records the node delayed]: 4.5 → 0.0; 5.1 → 0.0; 5.2 → 0.0; 5.2 → 0.0; 5.2 → 0.0; 5.6 → 0.0; 5.6 → 0.0; 5.7 → 0.0; 6.0 → 0.0
- c6_dest__otc_delay1800__R1, observer [other records]: 3.7 → 0.0; 4.2 → 4.8; 4.5 → 0.0; 4.8 → 5.0; 5.0 → 0.0; 5.2 → 10.0; 5.5 → 10.0; 5.8 → 0.0; 6.2 → 10.0; 7.1 → 10.0
- c6_dest__otc_delay1800__R1, delaying_destination: 3.9 → 0.0; 4.4 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 5.3 → 0.0; 7.3 → 0.0; 7.7 → 0.0
- c6_dest__otc_delay1800__R100, observer [all records]: 2.3 → 2.3; 2.5 → 2.2; 2.6 → 2.6; 2.7 → 2.3; 2.8 → 2.2; 2.9 → 2.4; 3.1 → 3.6; 3.2 → 2.7; 3.5 → 3.1; 4.0 → 4.2
- c6_dest__otc_delay1800__R100, observer [records the node delayed]: 2.3 → 0.9; 2.5 → 0.0; 2.6 → 0.0; 2.7 → 0.0; 2.8 → 1.9; 2.9 → 0.0; 3.1 → 0.0; 3.2 → 0.9; 3.5 → 0.0; 4.1 → 0.9
- c6_dest__otc_delay1800__R100, observer [other records]: 2.3 → 2.4; 2.5 → 2.3; 2.6 → 2.8; 2.7 → 2.4; 2.8 → 2.3; 2.9 → 2.5; 3.1 → 3.8; 3.2 → 2.8; 3.5 → 3.2; 4.0 → 4.4
- c6_dest__otc_delay1800__R100, delaying_destination: 2.4 → 0.9; 2.6 → 4.6; 2.8 → 2.8; 2.9 → 3.7; 3.0 → 3.7; 3.2 → 0.9; 3.3 → 0.9; 3.5 → 1.9; 3.8 → 1.9; 4.5 → 4.6
- c6_dest__otc_delay600__R1, observer [all records]: 3.8 → 0.0; 4.2 → 4.5; 4.5 → 4.8; 4.8 → 0.0; 5.0 → 0.0; 5.2 → 9.5; 5.5 → 9.5; 5.8 → 0.0; 6.2 → 9.5; 7.1 → 9.5
- c6_dest__otc_delay600__R1, observer [records the node delayed]: 4.6 → 0.0; 4.8 → 0.0; 5.2 → 0.0; 5.6 → 0.0; 5.8 → 0.0; 5.9 → 0.0; 6.3 → 0.0; 6.4 → 0.0; 6.9 → 0.0
- c6_dest__otc_delay600__R1, observer [other records]: 3.7 → 0.0; 4.2 → 4.8; 4.5 → 0.0; 4.8 → 5.0; 5.0 → 0.0; 5.2 → 10.0; 5.5 → 10.0; 5.8 → 0.0; 6.2 → 10.0; 7.1 → 10.0
- c6_dest__otc_delay600__R1, delaying_destination: 3.9 → 0.0; 4.4 → 0.0; 4.5 → 0.0; 4.8 → 0.0; 4.9 → 0.0; 5.2 → 0.0; 5.3 → 0.0; 7.3 → 0.0; 7.7 → 0.0
- c6_dest__otc_delay600__R100, observer [all records]: 2.3 → 2.4; 2.5 → 2.1; 2.6 → 2.7; 2.7 → 2.3; 2.8 → 2.1; 2.9 → 2.4; 3.1 → 3.6; 3.2 → 2.7; 3.5 → 3.1; 4.0 → 4.2
- c6_dest__otc_delay600__R100, observer [records the node delayed]: 2.3 → 0.9; 2.5 → 0.9; 2.6 → 0.9; 2.7 → 0.0; 2.8 → 0.0; 3.0 → 0.0; 3.1 → 0.9; 3.3 → 0.0; 3.5 → 0.9; 4.1 → 0.0
- c6_dest__otc_delay600__R100, observer [other records]: 2.3 → 2.4; 2.5 → 2.3; 2.6 → 2.8; 2.7 → 2.4; 2.8 → 2.3; 2.9 → 2.5; 3.1 → 3.8; 3.2 → 2.8; 3.5 → 3.2; 4.0 → 4.4
- c6_dest__otc_delay600__R100, delaying_destination: 2.4 → 0.9; 2.6 → 4.6; 2.8 → 2.8; 2.9 → 3.7; 3.0 → 3.7; 3.2 → 0.9; 3.3 → 0.9; 3.5 → 1.9; 3.8 → 1.9; 4.5 → 4.6
- c6_dest__otc_drop_m1800__R1, observer [all records]: 3.8 → 0.0; 4.1 → 4.5; 4.4 → 0.0; 4.6 → 4.8; 4.8 → 0.0; 5.0 → 4.8; 5.3 → 14.3; 5.6 → 14.3; 6.0 → 9.5; 6.8 → 9.5
- c6_dest__otc_drop_m1800__R1, observer [other records]: 3.8 → 0.0; 4.1 → 4.5; 4.4 → 0.0; 4.6 → 4.8; 4.8 → 0.0; 5.0 → 4.8; 5.3 → 14.3; 5.6 → 14.3; 6.0 → 9.5; 6.8 → 9.5
- c6_dest__otc_drop_m1800__R1, drop_link: 7.1 → 0.0; 10.3 → 0.0; 11.1 → 0.0; 11.8 → 0.0; 11.8 → 0.0; 13.1 → 0.0; 13.1 → 0.0; 15.5 → 0.0; 21.5 → 0.0
- c6_dest__otc_drop_m1800__R100, observer [all records]: 2.2 → 2.4; 2.4 → 2.6; 2.5 → 2.3; 2.6 → 2.7; 2.8 → 2.2; 2.9 → 2.7; 3.0 → 3.1; 3.2 → 2.5; 3.4 → 3.8; 3.9 → 3.9
- c6_dest__otc_drop_m1800__R100, observer [other records]: 2.2 → 2.4; 2.4 → 2.6; 2.5 → 2.3; 2.6 → 2.7; 2.8 → 2.2; 2.9 → 2.7; 3.0 → 3.1; 3.2 → 2.5; 3.4 → 3.8; 3.9 → 3.9
- c6_dest__otc_drop_m1800__R100, drop_link: 4.9 → 3.7; 5.7 → 3.7; 6.2 → 8.4; 6.7 → 6.5; 7.2 → 4.7; 7.7 → 8.5; 8.3 → 9.4; 9.1 → 12.3; 10.2 → 15.1; 12.9 → 8.5
- c6_dest__otc_drop_m21600__R1, observer [all records]: 3.8 → 4.5; 4.2 → 0.0; 4.5 → 4.5; 4.7 → 4.5; 5.0 → 9.1; 5.3 → 9.1; 5.5 → 4.5; 5.9 → 13.6; 6.4 → 4.8; 7.3 → 23.8
- c6_dest__otc_drop_m21600__R1, observer [other records]: 3.8 → 4.5; 4.2 → 0.0; 4.5 → 4.5; 4.7 → 4.5; 5.0 → 9.1; 5.3 → 9.1; 5.5 → 4.5; 5.9 → 13.6; 6.4 → 4.8; 7.3 → 23.8
- c6_dest__otc_drop_m21600__R1, drop_link: 8.5 → 0.0; 8.9 → 100.0; 9.7 → 0.0; 9.9 → 0.0; 12.1 → 0.0; 13.2 → 0.0; 14.5 → 0.0; 15.0 → 0.0; 18.2 → 0.0; 23.3 → 0.0
- c6_dest__otc_drop_m21600__R100, observer [all records]: 2.2 → 2.3; 2.4 → 3.0; 2.5 → 2.7; 2.6 → 2.7; 2.8 → 2.0; 2.9 → 3.1; 3.0 → 2.6; 3.2 → 2.1; 3.4 → 3.5; 3.9 → 3.8
- c6_dest__otc_drop_m21600__R100, observer [other records]: 2.2 → 2.3; 2.4 → 3.0; 2.5 → 2.7; 2.6 → 2.7; 2.8 → 2.0; 2.9 → 3.1; 3.0 → 2.6; 3.2 → 2.1; 3.4 → 3.5; 3.9 → 3.8
- c6_dest__otc_drop_m21600__R100, drop_link: 5.0 → 3.2; 5.8 → 3.2; 6.3 → 7.4; 6.7 → 4.3; 7.2 → 7.4; 7.6 → 6.4; 8.1 → 5.3; 8.9 → 5.3; 10.0 → 12.9; 13.1 → 11.8
- c6_dest__otc_drop_m3600__R1, observer [all records]: 3.8 → 0.0; 4.1 → 4.5; 4.3 → 4.5; 4.6 → 0.0; 4.8 → 0.0; 5.0 → 9.1; 5.2 → 14.3; 5.6 → 14.3; 6.0 → 4.8; 6.8 → 0.0
- c6_dest__otc_drop_m3600__R1, observer [other records]: 3.8 → 0.0; 4.1 → 4.5; 4.3 → 4.5; 4.6 → 0.0; 4.8 → 0.0; 5.0 → 9.1; 5.2 → 14.3; 5.6 → 14.3; 6.0 → 4.8; 6.8 → 0.0
- c6_dest__otc_drop_m3600__R1, drop_link: 7.1 → 0.0; 9.0 → 0.0; 9.2 → 0.0; 9.6 → 0.0; 11.5 → 0.0; 11.6 → 0.0; 13.2 → 0.0; 13.7 → 0.0; 18.6 → 0.0
- c6_dest__otc_drop_m3600__R100, observer [all records]: 2.2 → 1.8; 2.4 → 2.0; 2.5 → 2.8; 2.6 → 2.7; 2.8 → 2.5; 2.9 → 2.1; 3.0 → 2.6; 3.1 → 2.8; 3.4 → 3.8; 3.9 → 3.8
- c6_dest__otc_drop_m3600__R100, observer [other records]: 2.2 → 1.8; 2.4 → 2.0; 2.5 → 2.8; 2.6 → 2.7; 2.8 → 2.5; 2.9 → 2.1; 3.0 → 2.6; 3.1 → 2.8; 3.4 → 3.8; 3.9 → 3.8
- c6_dest__otc_drop_m3600__R100, drop_link: 4.9 → 5.7; 5.7 → 2.8; 6.2 → 4.7; 6.6 → 10.4; 7.0 → 9.4; 7.5 → 8.6; 8.1 → 10.5; 8.9 → 6.7; 10.0 → 9.5; 12.7 → 12.4
- c6_dest__otc_drop_m7200__R1, observer [all records]: 3.8 → 0.0; 4.3 → 0.0; 4.5 → 4.5; 4.7 → 0.0; 4.9 → 9.1; 5.2 → 4.5; 5.5 → 9.1; 5.8 → 13.6; 6.3 → 0.0; 7.3 → 4.5
- c6_dest__otc_drop_m7200__R1, observer [other records]: 3.8 → 0.0; 4.3 → 0.0; 4.5 → 4.5; 4.7 → 0.0; 4.9 → 9.1; 5.2 → 4.5; 5.5 → 9.1; 5.8 → 13.6; 6.3 → 0.0; 7.3 → 4.5
- c6_dest__otc_drop_m7200__R1, drop_link: 8.3 → 0.0; 8.3 → 0.0; 8.9 → 0.0; 9.4 → 0.0; 10.5 → 0.0; 10.8 → 0.0; 11.8 → 0.0; 11.9 → 0.0; 13.4 → 100.0; 15.1 → 0.0
- c6_dest__otc_drop_m7200__R100, observer [all records]: 2.2 → 2.8; 2.4 → 2.5; 2.5 → 2.4; 2.6 → 2.9; 2.8 → 2.4; 2.9 → 2.3; 3.0 → 3.4; 3.2 → 3.9; 3.4 → 2.7; 3.9 → 4.0
- c6_dest__otc_drop_m7200__R100, observer [other records]: 2.2 → 2.8; 2.4 → 2.5; 2.5 → 2.4; 2.6 → 2.9; 2.8 → 2.4; 2.9 → 2.3; 3.0 → 3.4; 3.2 → 3.9; 3.4 → 2.7; 3.9 → 4.0
- c6_dest__otc_drop_m7200__R100, drop_link: 5.0 → 4.7; 5.7 → 4.7; 6.2 → 7.5; 6.6 → 5.7; 7.1 → 5.7; 7.6 → 7.5; 8.2 → 7.5; 9.0 → 12.3; 10.2 → 8.6; 13.2 → 13.3
- c6_issuer__iwh_delay_L1440__R1, iwh_delay_L1440: 1.7 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.4 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_delay_L1440__R100, iwh_delay_L1440: 1.0 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_delay_L360__R1, iwh_delay_L360: 1.5 → 0.0; 1.8 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.4 → 0.0; 2.4 → 0.0; 2.6 → 0.0
- c6_issuer__iwh_delay_L360__R100, iwh_delay_L360: 0.9 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_delay_L720__R1, iwh_delay_L720: 1.5 → 0.0; 1.5 → 0.0; 1.9 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.3 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.6 → 0.0
- c6_issuer__iwh_delay_L720__R100, iwh_delay_L720: 0.9 → 0.0; 1.0 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_none_L1440__R1, iwh_none_L1440: 1.7 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.4 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_none_L1440__R100, iwh_none_L1440: 1.0 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_none_L360__R1, iwh_none_L360: 1.5 → 0.0; 1.9 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.4 → 0.0; 2.4 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_none_L360__R100, iwh_none_L360: 0.9 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_none_L720__R1, iwh_none_L720: 1.5 → 0.0; 1.9 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_none_L720__R100, iwh_none_L720: 0.9 → 0.0; 1.0 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_withhold_L1440__R1, iwh_withhold_L1440: 1.7 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.3 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.4 → 0.0; 2.5 → 0.0
- c6_issuer__iwh_withhold_L1440__R100, iwh_withhold_L1440: 1.0 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_withhold_L360__R1, iwh_withhold_L360: 1.5 → 0.0; 1.8 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.2 → 0.0; 2.4 → 0.0; 2.4 → 0.0; 2.6 → 0.0
- c6_issuer__iwh_withhold_L360__R100, iwh_withhold_L360: 0.9 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.3 → 0.0
- c6_issuer__iwh_withhold_L720__R1, iwh_withhold_L720: 1.5 → 0.0; 1.5 → 0.0; 1.9 → 0.0; 2.0 → 0.0; 2.1 → 0.0; 2.1 → 0.0; 2.3 → 0.0; 2.3 → 0.0; 2.4 → 0.0; 2.6 → 0.0
- c6_issuer__iwh_withhold_L720__R100, iwh_withhold_L720: 0.9 → 0.0; 1.0 → 0.0; 1.1 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.2 → 0.0; 1.3 → 0.0; 1.3 → 0.0


## Certificates: refills, stock and revocation delay

Stock: the mean number held just before a capture in the window. Revocation delay: how long certificates already issued to a revoked device stay usable, at the device's normal rate of use (capped at the two-week expiry), and for a device that keeps them.

| File | Runs | Refills per run in the window | Stock | Revocation delay at normal use | Worst case |
|---|---|---|---|---|---|
| c6__otcB100_W0__R1 | 1 | 206.0 | 75.5 | 24.5 h | 336 h |
| c6__otcB100_W0__R100 | 1 | 11.0 | 75.8 | 25.3 h | 336 h |
| c6__otcB1_W0__R1 | 1 | 20379.0 | 1.0 | 0.3 h | 336 h |
| c6__otcB1_W0__R100 | 1 | 1194.0 | 1.0 | 0.3 h | 336 h |
| c6__otcB20_W0__R1 | 1 | 1014.0 | 15.5 | 5.0 h | 336 h |
| c6__otcB20_W0__R100 | 1 | 59.0 | 14.8 | 4.9 h | 336 h |
| c6__otcB5_W0__R1 | 1 | 4073.0 | 4.0 | 1.3 h | 336 h |
| c6__otcB5_W0__R100 | 1 | 230.0 | 4.0 | 1.3 h | 336 h |

"""Section 3.9, second model: how much does the Section 3.7 skew close the gap?

Model
-----
17 destination servers spread over 8 unequal-sized jurisdiction codes (server
counts 3,2,2,2,2,2,2,2). Every server has the same number of device-table
lines, so a code's share of lines equals its share of servers. The device's
validator is in code J = 0.

For each simulated transaction the device picks C, F and I with these rules
(Section 3.7), requiring three different servers:
    C : uniform over servers outside J
    F, I : uniform over all servers (skew off), or weighted so that the codes
           a first hop sees follow the line shares (skew on)

Skew weights: F and I take code J with weight 1.5 * s_J and any other code c
with weight s_c * (1.5 - 0.5 / (1 - s_J)), where s is the line share. These
are the weights that make C, F and I together match the shares when C never
uses J.

The script reports the largest absolute gap between the code frequencies a
first hop sees (over all C, F and I) and the line shares.

Paper statement reproduced
--------------------------
Section 3.9: "17 destination servers in 8 unequal-sized codes, the largest gap
... fell from 5.1 points to 0.5 points. The small residue comes from the rule
that C, F and I be different servers."

Reproducibility note
--------------------
One generator (seed 7) is shared by both runs; skew off runs first.
N = 400,000 accepted transactions per run.
"""
import sys
import numpy as np

SEED = 7
N = 400_000
CODES_OF_SERVER = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
J = 0


def run(rng, codes_of_server, J, N=N, skew=True):
    S = len(codes_of_server)
    codes = np.array(codes_of_server)
    K = codes.max() + 1
    nper = np.array([(codes == c).sum() for c in range(K)])
    share = nper / S
    sJ = share[J]
    if skew:
        w = np.where(np.arange(K) == J, 1.5 * sJ, share * (1.5 - 0.5 / (1 - sJ)))
    else:
        w = share.copy()
    # a code's weight is split evenly across its servers
    ws = np.array([w[codes[s]] / nper[codes[s]] for s in range(S)])
    ws /= ws.sum()
    non_J = np.array([s for s in range(S) if codes[s] != J])
    C = rng.choice(non_J, size=N * 2)
    F = rng.choice(S, p=ws, size=N * 2)
    I = rng.choice(S, p=ws, size=N * 2)
    ok = (C != F) & (C != I) & (F != I)
    C, F, I = C[ok][:N], F[ok][:N], I[ok][:N]
    seen = np.bincount(np.concatenate([codes[C], codes[F], codes[I]]), minlength=K)
    seen = seen / seen.sum()
    p_F_in_J = float((codes[F] == J).mean())
    return share, seen, p_F_in_J


def main(out=sys.stdout):
    rng = np.random.default_rng(SEED)
    gaps = {}
    for skew in (False, True):
        share, seen, pF = run(rng, CODES_OF_SERVER, J, skew=skew)
        gap = float(np.abs(seen - share).max())
        gaps[skew] = gap
        print(f"skew {skew}", file=out)
        print(" share", np.round(share, 3), file=out)
        print(" seen ", np.round(seen, 3), file=out)
        print(f" max gap = {100 * gap:.1f} points   P(F in J) = {pF:.3f}", file=out)
    return gaps


if __name__ == "__main__":
    main()

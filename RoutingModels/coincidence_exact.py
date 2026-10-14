"""Section 3.9, fourth statement: how often does a first hop coincide with another path's destination?

Model (as stated in the paper)
------------------------------
* 20 relay nodes; nodes 17, 18 and 19 are the gatekeepers.
* First hops (A, D, G) for the device's three paths: three different nodes,
  uniform over all 20.
* Destinations (C, F, I): three different nodes, uniform over the 17
  non-gatekeepers (0..16).
* Builder constraint: inside each line, the first hop differs from the
  destination (A != C, D != F, G != I).
* A coincidence is an event in which some first hop equals the destination of a
  different path of the same transaction.

All 6,840 first-hop triples are combined with all 4,080 destination triples and
the constraint is applied by enumeration, so the result is exact (no sampling
error). The first Monte Carlo estimate in an earlier draft of the paper was
30.4% from 300,000 draws; the exact value is printed below.
"""
import itertools
import sys
import numpy as np

N_NODES = 20
N_GATEKEEPERS = 3
N_DEST = N_NODES - N_GATEKEEPERS


def main(out=sys.stdout):
    fh = np.array(list(itertools.permutations(range(N_NODES), 3)))      # (6840, 3)
    de = np.array(list(itertools.permutations(range(N_DEST), 3)))       # (4080, 3)
    valid = 0
    coincide = 0
    own_rejected = 0
    for a, d, g in fh:
        f = np.array([a, d, g])
        own_ok = (de[:, 0] != f[0]) & (de[:, 1] != f[1]) & (de[:, 2] != f[2])
        # cross: first hop i equals destination j, i != j
        cross = np.zeros(len(de), dtype=bool)
        for i in range(3):
            for j in range(3):
                if i != j:
                    cross |= (de[:, j] == f[i])
        valid += int(own_ok.sum())
        own_rejected += int((~own_ok).sum())
        coincide += int((own_ok & cross).sum())
    total = len(fh) * len(de)
    print(f"first-hop triples        = {len(fh)}", file=out)
    print(f"destination triples      = {len(de)}", file=out)
    print(f"combinations             = {total}", file=out)
    print(f"valid (own-path rule)    = {valid}", file=out)
    print(f"valid with a coincidence = {coincide}", file=out)
    print(f"coincidence rate         = {100 * coincide / valid:.2f} %", file=out)
    return coincide / valid


if __name__ == "__main__":
    main()

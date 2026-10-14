"""Section 3.9, first model: can a first hop infer the validator's jurisdiction code?

Model
-----
k equal-sized jurisdiction codes. A device never uses its validator's code (J)
for the credential destination C, so J is under-represented among the codes a
first hop sees. Each of the device's packets goes to C (probability 1/3) or to
F or I (probability 2/3). C is uniform over the k-1 codes other than J. F and
I are uniform over all k codes.

    P(packet's code = J)   = (2/3) / k
    P(packet's code = j)   = (1/3) / (k-1) + (2/3) / k        for each j != J

The first hop sees n packets from one device and guesses that the least-seen
code is J (ties broken at random). The script reports how often that guess is
right, over T independent trials per cell.

Paper statement reproduced
--------------------------
Section 3.9: "eight equal codes, 4,000 trials per cell ... 51% of the time
after 100 packets from one device, 83% after 300 and 99.7% after 1,000. Chance
is 12.5%."

Reproducibility note
--------------------
One generator (seed 1) is shared by every cell and the cells run in the order
below. Changing the order, the grid or T changes the individual estimates
(within about +/-0.8 points at T = 4000).
"""
import sys
import numpy as np

SEED = 1
T = 4000
KS = (4, 8, 16)
NS = (10, 30, 100, 300, 1000, 3000)


def trial(rng, k, n, T=T):
    p_J = (2 / 3) / k
    p_j = (1 / 3) / (k - 1) + (2 / 3) / k
    p = np.array([p_J] + [p_j] * (k - 1))
    counts = rng.multinomial(n, p, size=T)
    # argmin with a random tie-break: noise < 0.5 never reorders distinct integer counts
    noise = rng.random(counts.shape) * 0.5
    return float(np.mean(np.argmin(counts + noise, axis=1) == 0))


def main(out=sys.stdout):
    rng = np.random.default_rng(SEED)
    results = {}
    for k in KS:
        print(f"k= {k} guess= {round(1 / k, 3)}", file=out)
        for n in NS:
            r = trial(rng, k, n)
            results[(k, n)] = r
            print(f"  n={n:5d}  P(argmin=J)={r:.3f}", file=out)
    return results


if __name__ == "__main__":
    main()

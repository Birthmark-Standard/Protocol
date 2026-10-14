"""Section 3.9, third statement: the residual signal after the skew (closed form).

With the skew on and eight equal codes (share s = 1/8):
    F (or I) lands in the validator's code J with probability   1.5 * s            = 0.1875
    F (or I) lands in a given other code with probability       s * (1.5 - 0.5/(1-s)) = 13/112 = 0.1161

A registry node that sees which servers submitted a record asks whether code X
is the validator's code. Likelihood ratio for "F is in X":       0.1875 / 0.1161 = 1.6
For "F and I are both in X" (F and I treated as independent):    1.6 ** 2        = 2.6
Prior odds that X is the validator's code (1 in 8):              1 / 7
Posterior odds after seeing F and I both in X:                   (1/7) * 2.6 = 0.37
Posterior probability:                                           0.37 / 1.37  = 27 %

Paper statement reproduced
--------------------------
Section 3.9: "F in the validator's code is 1.6 times as likely ..., and F and I
both in it is 2.6 times as likely. A registry node that sees F and I both in
that code moves a guess ... from 12.5% to about 27%."

Not modelled: the distinct-server rule between F and I (a small correction), the
effect of unequal code sizes, and any other signal.
"""
from fractions import Fraction
import sys


def main(out=sys.stdout):
    k = 8
    s = Fraction(1, k)
    p_in = Fraction(3, 2) * s
    p_out = s * (Fraction(3, 2) - Fraction(1, 2) / (1 - s))
    lr1 = p_in / p_out
    lr2 = lr1 ** 2
    prior_odds = Fraction(1, k - 1)
    post_odds = prior_odds * lr2
    post = post_odds / (1 + post_odds)
    print(f"P(F in J | J is validator's code)  = {float(p_in):.4f}  ({p_in})", file=out)
    print(f"P(F in X | X is not the code)      = {float(p_out):.4f}  ({p_out})", file=out)
    print(f"likelihood ratio, F in X           = {float(lr1):.3f}", file=out)
    print(f"likelihood ratio, F and I in X     = {float(lr2):.3f}", file=out)
    print(f"prior (chance)                     = {100 * float(s):.1f} %", file=out)
    print(f"posterior                          = {100 * float(post):.1f} %", file=out)
    return float(lr1), float(lr2), float(post)


if __name__ == "__main__":
    main()

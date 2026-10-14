# RoutingModels

Small simulation and enumeration scripts behind the numbers in Section 3.9
("Limits of the Routing Design") of *Birthmark Protocol Integration*
(arXiv 2602.04933). Each script is short, reads top to bottom, and has its
model and the paper sentence it supports in its docstring.

These are toy models. They are not part of the Protocol paper's Appendix D
experiment (`SNAExperiment/`), which tests different vantages and is run with
different code.

## Run

    pip install -r requirements.txt
    python run_all.py > output.txt
    diff output.txt expected_output.txt      # no output means it reproduced

Runtime is about one second. Expected output was produced with Python 3.13 and
NumPy 2.5.3. The two Monte Carlo scripts depend on NumPy's random generator
(PCG64) and on the order in which cells run (one generator per script, seeded
once). A different NumPy version can move an estimate by a few tenths of a
point. `closed_form.py` and `coincidence_exact.py` do not sample.

## Which script supports which sentence in the paper

| Paper statement (Section 3.9) | Script | Seed / size | Output |
|---|---|---|---|
| Eight equal codes: a first hop that guesses the least-seen code names the validator's code 51% of the time after 100 packets, 83% after 300, 99.7% after 1,000. Chance is 12.5%. | `jurisdiction_inference.py` | seed 1, 4,000 trials per cell | k = 8 rows: 0.512, 0.829, 0.997 |
| With 17 servers in 8 unequal codes, the largest gap between code frequencies a first hop sees and line shares falls from 5.1 to 0.5 points with the skew. | `skew_gap.py` | seed 7, 400,000 transactions per run | "max gap" lines |
| F in the validator's code is 1.6 times as likely, F and I both 2.6 times, and a registry node moves a guess from 12.5% to about 27%. | `closed_form.py` | none (exact fractions) | 1.615, 2.609, 27.2% |
| About 30% of transactions in a 20-node pool have at least one coincidence of a first hop with another path's destination. | `coincidence_exact.py` | none (full enumeration of 27,907,200 combinations) | 30.46% |

The `k = 4` and `k = 16` rows and the other values of n in the first script's
output are extra cells that the paper does not quote.

## What the models leave out

* `jurisdiction_inference.py` assumes equal codes, one device, and a first hop
  that sees every packet of that device. It does not model a skew.
* `skew_gap.py` shows the gap in the codes a first hop sees. It does not
  measure what F, I or a registry node can infer.
* `closed_form.py` treats F and I as independent and codes as equal.
* `coincidence_exact.py` assumes uniform choice. A real table builder may
  weight nodes differently.

## Disclosure

The first versions of these scripts were written with help from Anthropic's
Claude models, as stated in the paper's Generative AI paragraph. The author reviewed them
and is responsible for them.

# The Birthmark Protocol: Companion Repository

A provenance system must show that a registered capture device's credential authorized the submission of the content. In an ordinary design, whoever checks the device and records the content can link the two, and that link is a map of who photographed what. The Birthmark Protocol never builds the map: it splits the work across independently operated components so that no single component holds what it takes to link a device to a record.

This repository is the companion repository of the two papers in `Docs/`: "The Birthmark Protocol: Achieving Semantic Non-Assembly in Media Provenance" (the Protocol paper) and "Birthmark Protocol Integration: Capture Device, Credential Validator and Edit Workflow" (the Integration paper). The Integration paper cites it as https://github.com/Birthmark-Standard/Protocol.

## Folders

| Folder | What it holds | Where it appears in the papers |
|---|---|---|
| `Docs/` | The Protocol paper, the Integration paper and the Messaging Structure specification | |
| `ProverifModels/` | ProVerif models of the privacy and integrity properties, each with a twin that carries one deliberate fault | Protocol paper, Appendix A and Table A.1 |
| `RoutingModels/` | Small simulation and enumeration scripts for the device routing table: the validator's tag a first relay can infer, the skew of F and I, and how often roles coincide | Integration paper, Section 3.9; Protocol paper, Section 6.3 |
| `SNAExperiment/` | A simulation of the protocol's full message flow that measures how often each component, and a passive observer, names the device behind a registry record | Protocol paper, Appendix D; Integration paper, Section 7 |
| `Benchmark/` | A harness that measures the device-side cost of a capture and the cost of proving a SHA-256 hash in zero knowledge, for a Raspberry Pi 4. The committed results are dry runs on a virtual machine, not Pi measurements. | Protocol paper, Appendix B and Table A.3, and Integration paper, Section 8, which calculate these costs from published benchmarks |

Each folder has a README that says what it holds, how to run it and what the output means.

## Reproduce

| Folder | Needs | Command | Time |
|---|---|---|---|
| `ProverifModels/` | ProVerif 2.05 | `proverif BM_Baseline_Noncorrelation.pv`, one model at a time, from `ProverifModels/` | one model per command |
| `RoutingModels/` | Python 3 and NumPy | `python run_all.py > output.txt`, then compare with `expected_output.txt` | about 1 second |
| `SNAExperiment/` | Python 3.10 or later, NumPy, SciPy and Matplotlib | `python -m sna run` from `SNAExperiment/` | about 8.7 hours on 8 worker processes |
| `Benchmark/` | A Raspberry Pi 4 with the packages `python3 check_prereqs.py` lists | `python3 run_partA.py` for Part A; `python3 run_partB.py setup`, `prove` and `hash` for Part B, from `Benchmark/` | not recorded for a Pi |

The smallest check of `SNAExperiment/` is its test suite: `python -m pytest tests -q` from `SNAExperiment/`, about one minute. `python -m sna run --runs 2 --out results/quick` runs every step of the experiment on two runs per cell, in about 20 minutes on a four-core machine.

## Licence

See `LICENSING.md`. The licence text is in `LICENSE`.

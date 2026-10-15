# Birthmark Protocol

The Birthmark Protocol is a two-channel provenance architecture for media authentication. It separates a capture device's credential from its content's identifying hash across disjoint delivery paths and encryption boundaries, so that no single component's compromise (including the credential validator's) is sufficient to determine which device produced which content. Correlation requires coordinated compromise across multiple components.

The architecture formalizes the privacy property this separation targets as Semantic Non-Assembly (SNA): a structural privacy property whose threshold is the information yield of a single component's compromise. Full definitions, the threat model, and formal properties are in the paper.

## Repository contents

- `Docs/`: the current working copy of the paper (`Birthmark Protocol v101.docx`) and the per-leg message specification (`Birthmark_Protocol_Per-Leg_Message_Specification_v101design.md`), which gives every key, every message and the size of every leg.
- `ProverifModels/`: the ProVerif formal verification models establishing the protocol's privacy and integrity properties, with a README indexing what each model tests and how to run it.
- `SNAExperiment/`: an empirical evaluation of the SNA property directly: how often a single compromised component, starting from a public registry record and holding its own legitimate keys and exact knowledge of its own event timing, can identify the device that produced it. Tests all seven vantage points the threat model defines (passive observer, each relay-hop position, the credential processor, the validator, the gatekeepers, and the content servers) and measures both raw identification accuracy and whether a component can distinguish its correct guesses from its incorrect ones.
- `RoutingModels/`: small simulation and enumeration scripts behind the figures in Section 3.9 of the companion Integration paper: what a first hop can infer from the device table's jurisdiction codes, how much the skew in the choice of destinations removes, and how often a first hop is also the destination of another path. These are toy models, separate from the `SNAExperiment/` evaluation, and run in about a second with `python run_all.py`.

The formal models establish what no coalition of compromised components can do cryptographically. The empirical experiments measure what a passive or key-holding observer can do statistically; a different kind of question the formal models are not built to answer. The reference deployment for photographic media (the Birthmark Standard) is documented separately; the protocol here is deployment-agnostic and does not assume any particular capture hardware or media type.

## Citation

Sam Ryan. "The Birthmark Protocol: Achieving Semantic Non-Assembly in Media Provenance."

[Full venue, date, and DOI/arXiv identifier to be added once available. The paper is being revised for journal resubmission. The verification artifacts and empirical evaluations here are complete and citable independent of that process.]

The companion preprint, "Birthmark Protocol Integration," covers the capture device, the credential token, validators and the edit workflow, which the paper above leaves partly out of scope. [arXiv identifier to be added when posted.]

## License

Released under Apache 2.0. This work is published as prior art: the architecture and its verification are intended as public infrastructure, open for anyone to build on, rather than a position any single organization can enclose.

## Status

The formal properties in `ProverifModels/` are stable and independently verifiable with ProVerif. The empirical evaluations in `SNAExperiment/` are complete. Results are in each experiment's `RESULTS.md`, including open findings. The scripts in `RoutingModels/` reproduce the figures they support and are toy models, not verified results. The paper may still change during revision; `Docs/` holds the current version.

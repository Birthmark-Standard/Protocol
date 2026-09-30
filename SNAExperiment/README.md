# Semantic Non-Assembly experiment

Semantic Non-Assembly claims that no single compromised component can link a piece of content to the credential transaction that produced it better than chance among the L transactions in flight.

This experiment tests that claim directly. It gives each vantage point:

- its real keys;
- its own exact event timing;
- a passive view of the sizes and timing of all network traffic.

It then measures how often that vantage names the right transaction, against 1/L.

The pre-registered analysis plan is `ANALYSIS_PLAN.md`. The findings are in `RESULTS.md`. `PAPER_TABLE.md` has one row per vantage.

## Vantages

| Vantage | Holds | Knows exactly | Label it links |
|---|---|---|---|
| Baseline | nothing | sizes and timing on every link | none |
| First hop, credential | relay transit key | source address and arrival; its own hold and forward times | network address |
| First hop, content | relay transit key | the same, for one content copy | network address |
| Credential processor | transit and ring-signing keys | packet hash, key reference, its own fan-out sends, reply arrival | transaction (manufacturer) |
| Content server | transit and registry-signing keys | content hash, content arrival, when it saw quorum, board postings | content |
| Validator | token-decryption and signing keys | device identity, request arrival, reply moment | device identity |
| Gatekeeper | transit and countersignature keys | packet hash, sender's address, its own arrival, hold outcome and posting | transaction |

Each vantage is scored against a paired baseline on the same traffic. The baseline anchors on the same event, but only as a passive observer sees it on the wire, and it cannot tell decoys apart. The difference between the two is the vantage's contribution over the baseline.

## Design choices

**Pool and roles**
- 20 submission servers, one validator, and three active gatekeepers per run.
- Nine distinct nodes per transaction, with the three paths disjoint.
- The credential processor and the content servers are never gatekeepers.

**Timing**
- Timing lottery on every hold: 10-second ticks, 8.33% release per tick, 5-minute cap.
- Each node holds on one clock; each gatekeeper holds on a dedicated clock.
- The device holds each channel on a fresh phase.
- Content servers hold first, then check the boards on every tick, and drop after 30 minutes without quorum.

**Padding**
- 420 to 460 bytes for every transit leg.
- 820 to 860 bytes for the gatekeeper fan-out leg.
- The measured 22-byte TLS 1.3 record overhead is added on the wire.

**Decoys**
- Decoy sources behave like devices: one credential packet and two content packets per capture.
- The validator marks a dummy with a plaintext indicator.
- The credential processor sends a same-size placeholder in place of σ_C.
- Gatekeepers post a substitute value on the real schedule.
- A decoy never reaches quorum, so it never reaches the registry.

**Volume**
- L is transactions in flight: rate × D, where D is the simulator's measured end-to-end delay (625.6 s, capture to registry finalization).
- Devices capture every 20 minutes on average.
- Decoy volume is `max(0, T − R)` in flight.

**Attacks**
- Each vantage scores every candidate answer by an empirical likelihood of (answer time − anchor time), built by Monte Carlo on separate seeds.
- The primary attack picks each item's highest-scoring answer.
- The secondary attack is a one-to-one assignment per compromised server.

**Runs**
- A run's traffic depends only on its real volume and run id. Every decoy cell therefore carries the same real traffic as the no-decoy cell at its real volume.
- The scored window is 3 hours, extended at small real volume to hold 200 real transactions per run on average.

## Running it

Requires Python 3.10 or later with numpy, scipy, matplotlib and PyNaCl. PyNaCl is used only to measure the ring signature size. Run from this directory.

**Windows PowerShell**

```powershell
py -m pip install numpy scipy matplotlib pynacl
py -m sna quick
py -m sna checks
py -m sna estimate --runs 100
py -m sna run --runs 100
py -m sna analyze
```

**macOS and Linux:** the same commands with `python3 -m sna`.

| Command | What it does |
|---|---|
| `quick` | Runs the whole pipeline on two small cells in under a minute. Output goes to `results/quick/` and is never reported. |
| `checks` | Runs the pre-run checks and writes `results/checks.json`. |
| `estimate` | Makes one probe run per cell. Prints seconds per run, successes per run, the runs needed for a stable finding, and the total time. |
| `run` | Runs the sweep. It is resumable: an interrupted run loses at most the runs in flight, and rerunning the same command continues it. Results are identical for any `--workers` value. |
| `analyze` | Writes `results/summary.json`, `summary.csv`, `tables.md` and `figures/`. |
| `volume` | Prints L against captures per day and devices. |

`--cells nodecoy|decoy|control` restricts a run to one part of the grid.

## Layout

| Path | Contents |
|---|---|
| `sna/params.py` | every numeric design choice |
| `sna/sim.py` | the simulator: real and decoy traffic, background traffic |
| `sna/attacks.py` | answer lists, vantage and baseline anchors, likelihood models, scoring |
| `sna/engine.py` | banded scoring, per-decision and joint decisions |
| `sna/analyze.py` | metrics |
| `sna/checks.py` | pre-run checks |
| `sna/cells.py` | grid, seeds, calibration, worker |
| `sna/runner.py` | resumable parallel execution |
| `sna/report.py` | tables and figures |
| `sna/pools.json` | measured TLS and DNS wire-size pools used by background traffic |
| `sna/ring_sig.py` | the ring signature used to measure its size |
| `tests/` | fast tests (`python -m pytest tests -q`) |
| `results/` | calibration, checks, costs, summary, tables and figures |

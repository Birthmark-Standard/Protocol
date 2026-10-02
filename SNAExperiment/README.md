# Semantic Non-Assembly experiment

Semantic Non-Assembly claims that no single compromised component can link a piece of content to the credential transaction that produced it better than chance among the L transactions in flight.

The harm this guards against is a public registry record being traced to the device that produced it. This experiment tests the claim on that link. Starting from a registry record, each vantage point tries to name the device behind it, using:

- its real keys;
- its own exact event timing;
- a passive view of the sizes and timing of all network traffic.

It is scored against chance and against a passive observer on the same records.

The pre-registered analysis plan is `ANALYSIS_PLAN.md`. The findings go in `RESULTS.md`, and `PAPER_TABLE.md` has one row per vantage.

## Vantages

| Vantage | Holds | Knows exactly | Label it links |
|---|---|---|---|
| Baseline | nothing | sizes and timing on every link | none |
| First hop, credential | relay transit key | source address and arrival; its own hold and forward times | network address |
| First hop, content | relay transit key | the same, for one content copy | network address |
| Credential processor | transit and ring-signing keys | packet hash, key reference, its own fan-out sends, reply arrival | transaction (manufacturer) |
| Content server | transit and registry-signing keys | content hash, content arrival, when the board pushes showed quorum, board postings | content |
| Validator | token-decryption and signing keys | device identity, request arrival, reply moment | device identity |
| Gatekeeper | transit and countersignature keys | packet hash, sender's address, its own arrival, hold outcome and posting | transaction |

Each vantage is scored against the baseline on the same records. The difference between the two is the vantage's contribution over the baseline.

## Design choices

**Pool and roles**
- 20 submission servers, one validator, and three active gatekeepers per run.
- Nine distinct nodes per transaction, with the three paths disjoint.
- The credential processor and the content servers are never gatekeepers.

**Timing**
- Timing lottery on every hold: 10-second ticks, 8.33% release per tick, 5-minute cap.
- Each node holds on one clock; each gatekeeper holds on a dedicated clock.
- The device holds each channel on a fresh phase.
- Gatekeeper postings depart in 30-second bundles, on each gatekeeper's own grid.
- Content servers hold first and never query a board. Each match board pushes its new matches to every content server every 10 seconds, on its own schedule. A content server confirms once its hold has released and two boards' pushes carry the match, and drops the packet after 30 minutes without quorum.
- A confirmed submission waits for the next 120-second registry-level bundle, on one schedule shared by every content server, and departs with every submission confirmed since the previous boundary.

**Padding**
- 420 to 460 bytes for every transit leg.
- 820 to 860 bytes for the gatekeeper fan-out leg.
- The measured 22-byte TLS 1.3 record overhead is added on the wire.

**Decoys**
- A decoy is a genuine transaction from a registered identity held by the decoy infrastructure. It is approved, fanned out, posted and finalized exactly as a real transaction, and it produces a permanent registry record.
- The decoy stream is a steady 40 transactions in flight, independent of real traffic, shared by 77 identities that each capture at a device's rate.

**Volume**
- L is transactions in flight: rate × D, where D is the simulator's measured end-to-end delay (625.6 s, capture to registry finalization).
- Devices capture every 20 minutes on average.
- With decoys, T = R + 40 in flight.

**Attacks**
- Rows are registry records. Each record's two submissions are paired and timed at their midpoint.
- Candidates are device submissions on the wire: each source's first-hop packets, grouped into captures. Decoy identities' packets are included for every vantage; no vantage can tell them apart.
- Each vantage scores every candidate by a likelihood of the record time. It is built by Monte Carlo on separate seeds, and each vantage's likelihood nests the baseline's, conditioned on the vantage's own exact knowledge.
- Each record picks its highest-scoring device (primary) and capture (secondary).

**Runs**
- A run's traffic depends only on its real volume and run id. A cell with decoys therefore carries the same real traffic as the cell without them at its real volume.
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
| `sequence` | Runs every step of one plan section in order: each build's runs, each build's analysis, then latency. `python -m sna sequence 6h` runs section 6h into `results/6h/`. Resumable. |
| `latency` | Writes the capture-to-finalization time under each build, by stage, to `results/latency.json`. |
| `bundles` | Writes registry bundle sizes over the sweep's runs to `results/registry_bundles_<build>.json`. |
| `gatekeeper` | Writes each gatekeeper's own load and bundle sizes, by decoy target and window, to `results/gatekeeper_occupancy.json`. |

`--cells bundle|nobundle|control` restricts a run to one part of the grid. `--build` picks the protocol build: `push` (no registry bundling), `reg60`, `reg120`, `reg240` or `reg480` (registry bundling at that window; `reg120` is the default), or the two-point gatekeeper-hold builds `twopoint` and `regbundle`, kept to reproduce plan section 6d.

## Layout

| Path | Contents |
|---|---|
| `sna/params.py` | every numeric design choice |
| `sna/sim.py` | the simulator: real and decoy traffic, background traffic |
| `sna/attacks.py` | record and candidate extraction, likelihood models, block scoring of every vantage |
| `sna/analyze.py` | metrics |
| `sna/checks.py` | pre-run checks |
| `sna/cells.py` | grid, seeds, calibration, worker |
| `sna/runner.py` | resumable parallel execution |
| `sna/report.py` | tables and figures |
| `sna/pools.json` | measured TLS and DNS wire-size pools used by background traffic |
| `sna/ring_sig.py` | the ring signature used to measure its size |
| `tests/` | fast tests (`python -m pytest tests -q`) |
| `results/` | calibration, checks, costs, summary, tables and figures |

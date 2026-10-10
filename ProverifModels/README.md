# Birthmark Protocol — ProVerif Formal Verification

This folder contains the ProVerif models supporting the privacy and integrity claims made
in "The Birthmark Protocol: Achieving Semantic Non-Assembly in Media Provenance." Each
model is self-contained and independently runnable; none depends on any other file in
this folder.

For the architecture these models formalize — the capture device, the credential
processor (C), the credential validator, the three gatekeepers and their paired match
boards, the two content-channel servers, and the registry — see the paper.

## Running a model

Each file is a complete ProVerif specification. With ProVerif 2.05 installed:

```
proverif BM_Baseline_Noncorrelation.pv
```

(or `proverif.exe` on Windows). No arguments or build steps beyond that. Twins (below) are run
the same way:

```
proverif twins/BM_Baseline_Noncorrelation_TWIN.pv
```

## What each model tests

| File | Establishes | Tests | Result |
|---|---|---|---|
| `BM_Baseline_Noncorrelation.pv` | Property B | No compromise: can an observer of the public channel and the registry tell which device authenticated which content? | Observational equivalence is true |
| `BM_CredentialProcessor_Compromise.pv` | Property D | All of C's keys leaked. Does that reveal which device holds which token? The validator stays honest and answers any request. | Observational equivalence is true |
| `BM_Validator_PacketHash_Secrecy.pv` | Properties A, E | All of the validator's keys leaked. Can the validator ever derive a PacketHash? | `not attacker(ph_m[])` is true |
| `BM_Verdict_Boundary_SameClass.pv` | Properties A, E | Validator's keys leaked, device identities public. Can the validator tell which content a device authenticated, when both transactions carry the same claim? | Observational equivalence is true |
| `BM_ContentServer_Compromise.pv` | Properties C, F | A content-channel server's key leaked, with the full honest pipeline running behind it. Does that reveal which device holds which token? | Observational equivalence is true |
| `BM_Gatekeeper_Compromise.pv` | Property J | One gatekeeper's terminus and signing keys leaked. Same question. | Observational equivalence is true |
| `BM_Quorum_Forgery.pv` | Properties G, I (one gatekeeper compromised) | Can a quorum form for a (PacketHash, verdict) pair that C did not check? Does C accept only verdicts the validator issued? | Queries 1 and 2 true; quorum reachable |
| `BM_Quorum_Collusion.pv` | Properties G, I (two gatekeepers compromised) | Same questions, with two of the three gatekeepers fully compromised | Queries 1 and 2 true; quorum reachable |
| `BM_Registry_Convergence.pv` | Property H | One content-channel server (F) fully compromised. Can the registry finalize a record that the other server (I) did not sign? Can F change the optional fields of a record? | Queries a, c, d true; s reachable |
| `BM_Pipeline_Liveness.pv` | none | Does the honest pipeline reach every stage? | All 8 events reachable |
| `BM_Quorum_Forgery_RingExclusion.pv` | none (sensitivity check) | Quorum_Forgery with the ring exclusion absent: G1's signing key is also C's, and is leaked. Which check then protects the quorum? | Queries 1 and 2 true; quorum reachable |

## Twins

A twin is a copy of a model with one deliberate fault. Twins are in `twins/`.

A result of "true" on a model counts only if its twin fails. If the twin is also true, the
model cannot see the fault, and its "true" proves nothing.

| Twin | The fault | Result |
|---|---|---|
| `BM_Baseline_Noncorrelation_TWIN.pv` | The validator folds the credential into its verdict | Observational equivalence cannot be proved |
| `BM_CredentialProcessor_Compromise_TWIN.pv` | Same | Observational equivalence cannot be proved |
| `BM_ContentServer_Compromise_TWIN.pv` | Same | Observational equivalence cannot be proved |
| `BM_Gatekeeper_Compromise_TWIN.pv` | Same | Observational equivalence cannot be proved |
| `BM_Validator_PacketHash_Secrecy_TWIN.pv` | C sends the PacketHash to the validator without the BlindShare wrap | `not attacker(ph_m[])` is false |
| `BM_Verdict_Boundary_SameClass_TWIN.pv` | The two transactions carry different claims, so the verdicts differ | Observational equivalence cannot be proved |
| `BM_Quorum_Forgery_TWIN.pv` | Gatekeepers 2 and 3 and the quorum verify no signatures | Query 1 is false |
| `BM_Quorum_Collusion_TWIN.pv` | The quorum of boards 1 and 2 does not verify C's signature | Query 1 is false |
| `BM_Quorum_Forgery_RingExclusion_TWIN.pv` | The honest gatekeepers skip the validator-signature check | Query 1 is false |
| `BM_Registry_Convergence_TWIN.pv` | The registry accepts two signatures from the same signer | Query a is false |

`BM_Verdict_Boundary_Control.pv` is the twin of `BM_Verdict_Boundary_SameClass.pv`. It
marks the boundary of Property E rather than a property of the protocol: a validator that
sees a rare verdict has fewer candidate records, so the proof holds within one verdict
class.

## Reading the results

Three proof techniques are used:

- **Observational equivalence** (Properties A–F, J): the model runs two scenarios side by
  side and asks whether any adversary, given everything it is allowed to observe or leak in
  that model, can tell which scenario it is in. "True" means it cannot: the property holds.
  `cannot be proved` or `is false` means it can, or ProVerif could not show it.
- **Secrecy query, `not attacker(X)`** (Properties A, E): asks whether a value ever
  becomes derivable by the adversary. "True" means it never does.
- **Correspondence query** (Properties G, H, I): asks whether one event can occur only
  after another has occurred. "True" means it cannot. The models also ask whether the
  final event is reachable. There `not event(X) is false` means X can happen, so the other
  queries are not true merely because nothing happens.

The correspondence queries, numbered as in the files:

- **Quorum models:**
  1. `quorum_reached(p,v) ==> c_checked(p,v)`: a quorum forms only for a (PacketHash,
     verdict) pair that C checked.
  2. `c_checked_w(p,v,w) ==> v_issued(v,w) && c_asked(p,w)`: C accepts only a verdict the
     validator issued for a wrapped value C sent.
  3. `quorum_reached(p,v)` is reachable.
- **Registry model:**
  a. `registry_final(h,v,m) ==> i_signed(h,v,m)`: the registry finalizes only records
     that I signed.
  c. `i_signed_n(h,n,v,m) ==> device_sent(h,n,m)`: what I signs matches what the device
     sent, including the optional field `m`.
  d. `i_signed_n(h,n,v,m) ==> device_sent_hn(h,n)`: the ContentHash and nonce, and so the
     verdict, belong to a real device submission.
  s. `registry_final(h,v,m)` is reachable.

## What "true" means for the equivalence models

- **Identity-swap models** (Baseline, CredentialProcessor, ContentServer, Gatekeeper):
  token confidentiality at that party's vantage point. The contents are the same in both
  scenarios, so these results say nothing about content.
- **SameClass:** content stays hidden from a compromised validator, behind the wrapped
  PacketHash and the encrypted content channel, when both transactions carry the same
  claim and so the same verdict.
- **Public and private names.** Device identities and contents are public names in the
  equivalence models. With private names the two scenarios would differ only by a
  renaming, and the result would hold for any protocol. Nonces and keys are private. In
  the correspondence models the device identity is private, so the adversary cannot forge
  a token.

## Not modeled

- A compromised validator that withholds replies and watches the registry (selective
  denial). The symbolic adversary sees the order of registry outputs, which separates the
  two scenarios for a timing reason. Holds, bundling and decoys address this; ProVerif
  cannot show it. Appendix D of the paper evaluates it empirically.
- Replay logging (`tx_nonce`), `key_ref`, the manufacturer-key identifier, holds, padding.
- The optional fields are modeled as one field. The specification uses a metadata hash and
  a parent hash, with presence flags.
- Coordinated compromise of several components, such as the validator together with a
  content-channel server.

## Naming

Each file's key variables follow the paper's own terms, lowercased and with underscores
in place of hyphens (ProVerif identifiers can't contain hyphens). Private keys are
written `X_sk`, and the public key is `pk(X_sk)`: `v_token_sk` for the validator's token
key and `v_sign_sk` for its signing key, `c_device_sk` for C's relay-terminus key,
`c_sign_sk` for C's own submission-server signing key, `f_device_sk` and `i_device_sk`
for the two content-channel servers' keys, `f_id_sk` and `i_id_sk` for their separate
registry-signing keys, and `g1_sk`/`g1_sign_sk`, `g2_sk`/`g2_sign_sk`, `g3_sk`/`g3_sign_sk`
for the three gatekeepers' terminus and signing keys respectively. `packethash` is
PacketHash and `blindshare_key` is BlindShare_key. `ph_m` is a private marker standing
for one device's PacketHash.

## Files

`generator/gen_models.py` builds every model except SameClass and its twin from shared
blocks.

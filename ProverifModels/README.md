# Birthmark Protocol — ProVerif Formal Verification

This folder contains the ProVerif models supporting the privacy and integrity claims made
in "The Birthmark Protocol: Achieving Semantic Non-Assembly in Media Provenance." Each
model is self-contained and independently runnable; none depends on any other file in
this folder.

For the architecture these models formalize (the capture device, the credential
channel server (C), the credential validator, the three gatekeepers and their paired match
boards, the two content channel servers, and the registry) see the paper.

## Running a model

Each file is a complete ProVerif specification. With ProVerif 2.05 installed:

```
proverif BM_Baseline_Identity.pv
```

(or `proverif.exe` on Windows). No arguments or build steps beyond that. Twins (below) are run
the same way:

```
proverif twins/BM_Baseline_Identity_TWIN.pv
```

## How the models fit together

Each model fixes who is compromised and asks one question. File names follow
`BM_<compromised parties>_Compromise_<question>.pv`. `_Pair_` means two parties in the same
role. `_And_` means two parties in different roles. The question is one of:

- **Identity.** Which device holds which token?
- **Content.** Which content did a device authenticate?
- **Secrecy.** Does a value ever become derivable?
- **An integrity property**, named for it: QuorumForgery, RegistryConvergence, TokenBinding.

The grid shows file names without the `BM_` prefix and the `.pv` extension. An empty cell
means there is no model for that pair. It does not necessarily mark a gap.

| Compromised | Identity | Content | Secrecy | Integrity |
|---|---|---|---|---|
| none | Baseline_Identity | | | |
| C | CredentialChannelServer_Compromise_Identity | | | CredentialChannelServer_Compromise_TokenBinding |
| validator | | Validator_Compromise_Content_SameClass | Validator_Compromise_Secrecy | |
| one gatekeeper | Gatekeeper_Compromise_Identity | | | Gatekeeper_Compromise_QuorumForgery; Gatekeeper_Compromise_QuorumForgery_RingExclusion (sensitivity check) |
| two gatekeepers (same role) | Gatekeeper_Pair_Compromise_Identity | | | Gatekeeper_Pair_Compromise_QuorumForgery |
| one content channel server (F) | ContentChannelServer_Compromise_Identity | | | ContentChannelServer_Compromise_RegistryConvergence |
| both content channel servers (same role) | ContentChannelServer_Pair_Compromise_Identity | | | |
| first relay | | | FirstRelay_Compromise_Secrecy | |
| validator and C (different roles) | | Validator_And_CredentialChannelServer_Compromise_Content; Validator_And_CredentialChannelServer_Compromise_Content_ActivePosting (boundary) | | |
| validator and one gatekeeper (different roles) | | Validator_And_Gatekeeper_Compromise_Content | | |

`BM_Pipeline_Liveness.pv` has no compromised party. It checks that the honest pipeline
reaches every stage.

The models cover two coalitions within one role (two of the three gatekeepers; the two
content channel servers) and two across roles (the validator with C; the validator with one
gatekeeper).

## What each model tests

| File | Establishes | Tests | Result |
|---|---|---|---|
| `BM_Baseline_Identity.pv` | Property B | No compromise: can an observer of the public channel and the registry tell which device authenticated which content? | Observational equivalence is true |
| `BM_CredentialChannelServer_Compromise_Identity.pv` | Property D | All of C's keys leaked. Does that reveal which device holds which token? The validator stays honest and answers any request. `key_ref` is not modeled. C sees it in the clear, so the result holds between devices that share a Token Key. | Observational equivalence is true |
| `BM_Validator_Compromise_Secrecy.pv` | Properties A, E | All of the validator's keys leaked. Can the validator ever derive a FullPacketHash? | `not attacker(hash((hash(imgX[]),n_m[])))` is true |
| `BM_Validator_Compromise_Content_SameClass.pv` | Properties A, E | Validator's keys leaked, device identities public. Can the validator tell which content a device authenticated, when both transactions carry the same claim? | Observational equivalence is true |
| `BM_ContentChannelServer_Compromise_Identity.pv` | Properties C, F | A content channel server's key leaked, with the full honest pipeline running behind it. Does that reveal which device holds which token? | Observational equivalence is true |
| `BM_Gatekeeper_Compromise_Identity.pv` | Property J | One gatekeeper's terminus and signing keys leaked. Same question. | Observational equivalence is true |
| `BM_Gatekeeper_Compromise_QuorumForgery.pv` | Properties G, I (one gatekeeper compromised) | Can a quorum form for a (FullPacketHash, verdict) pair that C did not check? Does C accept only verdicts the validator issued? | Queries 1 and 2 true; quorum reachable |
| `BM_Gatekeeper_Pair_Compromise_QuorumForgery.pv` | Properties G, I (two gatekeepers compromised) | Same questions, with two of the three gatekeepers fully compromised | Queries 1 and 2 true; quorum reachable |
| `BM_ContentChannelServer_Compromise_RegistryConvergence.pv` | Property H | One content channel server (F) fully compromised. Can the registry finalize a record that the other server (I) did not sign? Can F change the optional fields of a record? | Queries a, c, d true; s reachable |
| `BM_FirstRelay_Compromise_Secrecy.pv` | Property K | A first relay's Server Transit Key leaked, with a passive observer of every leg of one content path (device, first relay, second relay, destination). The relay sees each device's address with its packet. Can it derive either device's ContentHash? | `not attacker(hash(secret_img_1[]))` and `not attacker(hash(secret_img_2[]))` are true |
| `BM_CredentialChannelServer_Compromise_TokenBinding.pv` | Property L | C compromised: the attacker plays C and may send the validator any token with any wrapped value, or the same token twice. Is a verdict issued for a (replay nonce, wrapped value) pair the device did not commit to? Does each commitment back at most one verdict? The validator claims each nonce in one atomic step, stated as a restriction. | Queries 1 and 2 true; a verdict is reachable |
| `BM_Pipeline_Liveness.pv` | none | Does the honest pipeline reach every stage? | All 8 events reachable |
| `BM_Gatekeeper_Compromise_QuorumForgery_RingExclusion.pv` | none (sensitivity check) | Quorum_Forgery with the ring exclusion absent: gatekeeper 1's signing key is also C's, and is leaked. Which check then protects the quorum? | Queries 1 and 2 true; quorum reachable |
| `BM_Gatekeeper_Pair_Compromise_Identity.pv` | Property J (two gatekeepers compromised) | Gatekeepers 1 and 2 fully compromised together; gatekeeper 3, F and I stay honest. Does that reveal which device holds which token? | Observational equivalence is true |
| `BM_ContentChannelServer_Pair_Compromise_Identity.pv` | Properties C, F (both content channel servers compromised) | F and I fully compromised together. Does that reveal which device holds which token? | Observational equivalence is true |
| `BM_Validator_And_CredentialChannelServer_Compromise_Content.pv` | none (Table 4, row 1) | The validator and C fully compromised together, with the registry idealized. The pair links a device to a FullPacketHash. Can it tell which content the device authenticated? | Observational equivalence is true |
| `BM_Validator_And_CredentialChannelServer_Compromise_Content_ActivePosting.pv` | none (Table 4, row 1) | The same pair with the registry idealization removed: F's records reach the public registry output in the order they are produced. C posts one FullPacketHash and reads which record appears. | Observational equivalence cannot be proved. This is the intended result (see Boundary models). |
| `BM_Validator_And_Gatekeeper_Compromise_Content.pv` | none (Table 4, row 2) | The validator and gatekeeper 1 fully compromised together, with the registry idealized. The pair links a device to a FullPacketHash. Can it tell which content the device authenticated? | Observational equivalence is true |

## Twins

A twin is a copy of a model with one deliberate fault. Twins are in `twins/`.

A result of "true" on a model counts only if its twin fails. If the twin is also true, the
model cannot see the fault, and its "true" proves nothing.

| Twin | The fault | Result |
|---|---|---|
| `BM_Baseline_Identity_TWIN.pv` | The validator folds the credential into its verdict | Observational equivalence cannot be proved |
| `BM_CredentialChannelServer_Compromise_Identity_TWIN.pv` | Same | Observational equivalence cannot be proved |
| `BM_ContentChannelServer_Compromise_Identity_TWIN.pv` | Same | Observational equivalence cannot be proved |
| `BM_Gatekeeper_Compromise_Identity_TWIN.pv` | Same | Observational equivalence cannot be proved |
| `BM_Validator_Compromise_Secrecy_TWIN.pv` | C sends the FullPacketHash to the validator without the BlindShare wrap | `not attacker(fph_m[])` is false |
| `BM_Validator_Compromise_Content_SameClass_TWIN.pv` | The two transactions carry different claims, so the verdicts differ | Observational equivalence cannot be proved |
| `BM_Gatekeeper_Compromise_QuorumForgery_TWIN.pv` | Gatekeepers 2 and 3 and the quorum verify no signatures | Query 1 is false |
| `BM_Gatekeeper_Pair_Compromise_QuorumForgery_TWIN.pv` | The quorum of boards 1 and 2 does not verify C's signature | Query 1 is false |
| `BM_Gatekeeper_Compromise_QuorumForgery_RingExclusion_TWIN.pv` | The honest gatekeepers skip the validator-signature check | Query 1 is false |
| `BM_ContentChannelServer_Compromise_RegistryConvergence_TWIN.pv` | The registry accepts two signatures from the same signer | Query a is false |
| `BM_FirstRelay_Compromise_Secrecy_TWIN.pv` | The device does not encrypt the payload under the destination's Channel Key | Both queries are false |
| `BM_CredentialChannelServer_Compromise_TokenBinding_TWIN.pv` | The validator does not compare the binding hash in the token with the wrapped value it is handed | Queries 1 and 2 are false |
| `BM_CredentialChannelServer_Compromise_TokenBinding_NoNonceClaim_TWIN.pv` | The validator does not claim the replay nonce | Query 1 is true; query 2 is false |
| `BM_CredentialChannelServer_Compromise_TokenBinding_NonAtomic_TWIN.pv` | Checking that the nonce is unused and recording it are separate steps | Query 1 is true; query 2 is false |
| `BM_Gatekeeper_Pair_Compromise_Identity_TWIN.pv` | The validator folds the credential into its verdict | Observational equivalence cannot be proved |
| `BM_ContentChannelServer_Pair_Compromise_Identity_TWIN.pv` | The validator folds the credential into its verdict | Observational equivalence cannot be proved |
| `BM_Validator_And_CredentialChannelServer_Compromise_Content_TWIN.pv` | The device sends n to C inside the credential bundle | Observational equivalence cannot be proved |
| `BM_Validator_And_Gatekeeper_Compromise_Content_TWIN.pv` | The device sends n to C, and C forwards it to gatekeeper 1 | Observational equivalence cannot be proved |

The last five rows of the model table and the last four rows of the Twins table were run on 2026-11-24.

## Boundary models

Two files do not prove a property of the protocol. Each marks where a property stops, and
"cannot be proved" is the result each is meant to show.

- `twins/BM_Validator_Compromise_Content_SameClass_TWIN.pv` is the twin of
  `BM_Validator_Compromise_Content_SameClass.pv`. It gives the two transactions different
  claims, so the verdicts differ. It marks the boundary of Property E: a validator that sees
  a rare verdict has fewer candidate records, so the proof holds within one verdict class.
- `BM_Validator_And_CredentialChannelServer_Compromise_Content_ActivePosting.pv` removes
  the registry idealization from the validator-and-C model. C posts one FullPacketHash,
  delivers the matching content packet to F and reads which record appears. The record
  carries hash(img), which separates the two scenarios. This is the active step Table 4,
  row 1 lists for the coalition, so "cannot be proved" confirms that row. It does not show
  how often the attack succeeds: Table 4 limits its reach to the transactions C handles,
  which include decoys that C cannot tell from real transactions, and the model represents
  neither. This file has no twin, because its result is a failure to prove and not a "true"
  that a twin has to back.

## Reading the results

Three proof techniques are used:

- **Observational equivalence** (Properties A–F, J): the model runs two scenarios side by
  side and asks whether any adversary, given everything it is allowed to observe or leak in
  that model, can tell which scenario it is in. "True" means it cannot: the property holds.
  `cannot be proved` or `is false` means it can, or ProVerif could not show it.
- **Secrecy query, `not attacker(X)`** (Properties A, E, K): asks whether a value ever
  becomes derivable by the adversary. "True" means it never does.
- **Correspondence query** (Properties G, H, I, L): asks whether one event can occur only
  after another has occurred. "True" means it cannot. The models also ask whether the
  final event is reachable. There `not event(X) is false` means X can happen, so the other
  queries are not true merely because nothing happens.

The correspondence queries, numbered as in the files:

- **Quorum models:**
  1. `quorum_reached(p,v) ==> c_checked(p,v)`: a quorum forms only for a (FullPacketHash,
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
- **Token binding model:**
  1. `v_issued(rn,e) ==> dev_committed(rn,e)`: the validator issues a verdict only for a (replay nonce,
     wrapped value) pair the device committed to.
  2. `inj-event(v_issued(rn,e)) ==> inj-event(dev_committed(rn,e))`: each device commitment backs at
     most one verdict.
  3. `v_issued(rn,e)` is reachable.

## What "true" means for the equivalence models

- **Identity-swap models** (Baseline, CredentialChannelServer, ContentChannelServer, Gatekeeper,
  Gatekeeper_Pair, ContentChannelServer_Pair): token confidentiality at that party's or that
  pair's vantage point. The contents are the same in both
  scenarios, so these results say nothing about content.
- **SameClass:** content stays hidden from a compromised validator, behind the wrapped
  FullPacketHash and the encrypted content channel, when both transactions carry the same
  claim and so the same verdict.
- **Validator_And content-swap models** (Validator_And_CredentialChannelServer,
  Validator_And_Gatekeeper): with the registry idealized, nothing visible to the pair
  separates the two contents. The pair links a device to a FullPacketHash, but FullPacketHash
  covers n, which only F and I hold.
- **Public and private names.** Device identities and contents are public names in the
  equivalence models. With private names the two scenarios would differ only by a
  renaming, and the result would hold for any protocol. Nonces and keys are private. In
  the correspondence models the device identity is private, so the adversary cannot forge
  a token.

## Not modeled

- Time. No model carries holds, timing or padding. SNAExperiment evaluates timing (Protocol paper, Appendix C).
- Selective denial by a compromised validator (Table A.2, row 16).
- In `BM_Validator_Compromise_Content_SameClass.pv` and the two `BM_Validator_And_*_Content.pv` models, F's record goes to a private channel and the public registry output is fixed, the same in both scenarios whatever the validator does. This excludes selective denial from all three, and the active posting attack of Table 4 from the validator-and-C model. `BM_Validator_And_CredentialChannelServer_Compromise_Content_ActivePosting.pv` drops the fixed output and shows that attack.

## Naming

Each file's key variables follow the paper's own terms, lowercased and with underscores
in place of hyphens (ProVerif identifiers can't contain hyphens). Private keys are
written `X_sk`, and the public key is `pk(X_sk)`: `v_token_sk` for the validator's token
key and `v_sign_sk` for its signing key, `c_device_sk` for C's relay-terminus key,
`c_sign_sk` for C's own Registry Node signing key, `f_device_sk` and `i_device_sk`
for the two content channel servers' keys, `f_sign_sk` and `i_sign_sk` for their separate
registry-signing keys, and `g1_sk`/`g1_sign_sk`, `g2_sk`/`g2_sign_sk`, `g3_sk`/`g3_sign_sk`
for the three gatekeepers' terminus and signing keys respectively. `fullpackethash` is
FullPacketHash and `blindshare_key` is BlindShare_key.

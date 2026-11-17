# What each party holds, in each candidate

From the design descriptions only: the credential path from the Messaging Structure's table of what each party holds when fully exposed; blind-issued one-time certificates from the design as decided for C6. Nothing is inferred beyond them. A dash means the party does not exist in that candidate.

| Party | Credential path | Blind-issued one-time certificates |
|---|---|---|
| Device | Its credential (Cred_HW) | A fresh signing key per capture, with a certificate an issuer signed blind in advance; its stock of certificates |
| Issuer | — | Knows the device; signs its one-time public keys blind; sees each refill request (identity, time, count); one issuing key per manufacturer |
| Validator (V) | Cred_HW, replay_nonce, claim, binding_hash, verdict, Enc_FullPacketHash (opaque), tx_id, C's network address | — |
| C | T (opaque), key_ref (names the Token Key), FullPacketHash, BlindShare_key, Enc_FullPacketHash, verdict, σ_V, tx_id | — |
| Gatekeeper | FullPacketHash, verdict, Enc_FullPacketHash, BlindShare_key, σ_V, σ_C, C's network address | — |
| Match board reader | FullPacketHash, verdict, σ_C, σ_GK | — |
| First relay | Device IP; timing; the routing code and, from its relay table, the next relay; opaque payload. With the device routing table: the line the code belongs to | The same: the packet uses the same device routing table and wrapping as a content packet |
| Second relay | Previous relay's address; destination | The same |
| Destination | F or I: ContentHash, n, FullPacketHash′, verdict, any optional fields, E's (or H's) address, match board postings | The destination Registry Node: the packet, which carries ContentHash, the claim and other fields, the one-time public key, the issuer's signature on it, and the device's signature; it submits the packet to the registry |
| Every Registry Node | At intake, the identities of F and I | Verifies the certificate and the device signature, then drops them; learns which issuer signed each packet |
| Registry observer (the posted record) | ContentHash, verdict, any optional fields, coarse timestamp | The record carries neither the certificate nor the device signature, so it does not show the issuer |
| An issuer that issues under another key | — | Each manufacturer has one published issuing key and Registry Nodes verify against the published set, so a certificate under any other key fails |
| Global passive observer | Sizes and timing only | Sizes and timing only |

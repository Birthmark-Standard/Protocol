# Birthmark Protocol — Per-Leg Message Specification

**Notation.** `||` = concatenation. `ECIES(pk; m)` = randomized IND-CCA2 public-key encryption. `AEAD(k; m)` = AES-256-GCM. `Sign(sk; m)` = Ed25519. `RSign(ring; m)` = unlinkable 1-of-n ring signature over a ring. `ECIESb((GP, pk); m)` = ECIES to a blinded destination key (a Channel Key): the sender picks a random scalar e, sends EPK = e·GP in place of the usual ephemeral public key, and derives the AEAD key from e·pk and EPK. The holder of the secret scalar sk with pk = sk·GP derives the same value as sk·EPK.

**Terms.** This specification uses the terms of the Protocol paper (v105) and the Integration paper (v27). A **Registry Node** is a consortium member's node, and that member is its **operator**. A Registry Node can serve as a first relay, second relay, C, F, I or gatekeeper, and it takes part in registry consensus. A validator is not a Registry Node.

## Parties and keys

Every key has one purpose. No key is used both to decrypt and to sign, and no key serves two purposes.

| Party | Key | Type | Purpose | Public part known to |
| --- | --- | --- | --- | --- |
| Device | Cred\_HW | secret credential | Proves membership to its validator. A CMPS holds Cred\_SW instead (see Software-validator flow) | Validator (Token Key Table), no one else |
| Device | key\_ref | identifier | Tells the validator which Token Key and member list apply | Validator and C |
| Validator V | V-token\_sk / pk (Token Key) | ECIES | Decrypts the device token. One pair per set of devices, selected by key\_ref | Devices (provisioned) |
| Validator V | V-sign\_sk / pk | ring member key | Member key in V-Ring, for signing a verdict | C, gatekeepers |
| Validator V | V-transit\_sk / pk | ECIES | Terminates the C→V leg (V's Server Transit Key) | C |
| Registry Node serving as C, F or I | Channel Key scalar sk | blinded ECIES | Terminates the credential packet (as C) or a content packet (as F or I) | Devices, as blinded pairs (GP, pk) in the device routing table; the node holds only sk |
| Every Registry Node | C-ring\_sk / pk | ring member key | Member key in C-Ring, used when the node serves as C to sign FullPacketHash and the verdict. A node keeps it when it rotates into the gatekeeper role, which is why C-Ring excludes the active gatekeepers' keys | Gatekeepers, F, I (as part of C-Ring) |
| Registry Node serving as gatekeeper | GK-sign\_sk / pk | Ed25519 | Countersigns match board postings | F, I |
| Registry Node serving as F or I | F-sign\_sk / pk (I-sign\_sk / pk) | Ed25519 | Signs registry submissions | Registry |
| Every Registry Node S | S-transit\_sk / pk (Server Transit Key) | ECIES | Terminates every transit leg addressed to S, whatever role S holds in that transaction (first relay, second relay, C, F, I or gatekeeper) | Every other Registry Node (full Server Transit Key table), validators, and every device (first-relay entries of the device routing table) |

**Server Transit Keys belong to nodes, not roles.** A, B, C, D, E, F, G, H and I are per-transaction roles, and any Registry Node can hold any of them, subject to the role rules below. Each node therefore holds one Server Transit Key pair and a full table of every other node's Server Transit public key. "A-transit", "C-transit" and so on in the leg table mean the Server Transit Key of whichever node holds that role for a given transaction. The V→C leg also uses C's Server Transit Key, so validators hold the table too. This follows from position labels naming roles rather than node identities: a role-specific key pair for every role a node might ever be assigned would work against that principle, not with it.

**Channel Keys belong to nodes, not roles.** A node that can be a destination holds one Channel Key scalar sk, and uses it whichever of C, F or I it is in a given transaction. It tells the credential packet from a content packet by the plaintext length: CredP is 139 bytes, and ContP\_F and ContP\_I are 49, 81 or 113 bytes.

**Per-transaction values** (fresh each transaction, never reused):

- `n`: 128-bit content nonce. Goes only to F and I.
- `replay_nonce`: 128-bit single-use nonce. Goes only to V, inside the token.
- `claim` (the Processing Claim): the device's or CMPS's statement about post-capture processing, two bytes. Zero for a hardware capture. For an edit it holds the five tool-class bits of the tools applied since the raw capture and the Deviation Score, the cumulative result of comparing the saved image with the Predicted Result of the declared operations. Goes only to V, inside the token. The encoding of the Deviation Score is not fixed here.
- `verdict` (the Modification Verdict): one byte, derived by V as `judge(claim)`. It holds the Modification Flag, six bits, and a two-bit deviation bucket (four classes). Five Modification Flag bits are tool-class bits, which V copies from the claim. The sixth marks undeclared change, which V derives from the Deviation Score and its threshold. The verdict is zero for an unedited capture. A verdict with a Modification Flag bit set is a flagged record, not a rejection. The device never sends a verdict or a modification level. The bucket boundaries are a deployment parameter set by the editing software's developer; the protocol treats the bucket as an opaque value. Bit positions are not fixed here.
- `BlindShare_key`: 256-bit AEAD key. Generated by the device, fresh per transaction. It goes to C inside CredP, and from C to the gatekeepers. It never goes to V.
- `binding_hash`: 32 bytes, `SHA-256(Enc_FullPacketHash)`, computed by the device. It goes only to V, inside the token, and ties the token to one submission.

**C-Ring:** the ring public keys of the C-candidate pool minus the three currently active gatekeepers. Verifiers check against the ring that is current at verification time. Ring keys are separate from every other node key. Over a 17-node pool, σ\_C is 576 bytes.

**V-Ring:** the ring public keys of every registered validator. Unlike C-Ring, whose size is fixed by the Registry Node pool, its size is the number of registered validators, which starts at one and grows only as more validators register. An unlinkable ring signature over a one-member ring carries no anonymity benefit across validators (there is only one to hide among) and is close to the cost of a plain signature, well under σ\_C's 576 bytes. Hiding which validator signed is a benefit that strengthens only as more validators join.

## Device-side construction

The device builds one credential packet (CredP) and two content packets (ContP\_F and ContP\_I) per transaction, then wraps each for its first relay. The device generates BlindShare\_key and computes Enc\_FullPacketHash and binding\_hash. C receives BlindShare\_key inside CredP and computes Enc\_FullPacketHash itself from FullPacketHash and BlindShare\_key; it never decrypts it.

1. `ContentHash = SHA-256(candidate image)`. A candidate image is the RAW file, the ISP-processed image, or an adjusted version that clears the deviation threshold.
2. `n` ← 128-bit random.
3. `FullPacketHash = SHA-256(ContentHash || n || flags || [h(metadata)] || [parent ContentHash])`. `flags` is one byte: bit 0 set if h(metadata) is present, bit 1 set if the parent ContentHash is present, other bits zero. The flags byte and the fixed 32-byte field length make the encoding unambiguous. FullPacketHash therefore covers every field the content packet carries, so F and I cannot alter an optional field without changing FullPacketHash.
4. `replay_nonce` ← 128-bit random.
5. `BlindShare_key` ← 256-bit random. `Enc_FullPacketHash = AEAD(BlindShare_key; FullPacketHash)` with a fixed AEAD nonce, which is safe because BlindShare\_key is single-use. `binding_hash = SHA-256(Enc_FullPacketHash)`.
6. `T = ECIES(V-token_pk; Cred_HW || replay_nonce || claim || binding_hash)`. With a 32-byte Cred\_HW, a 16-byte replay\_nonce, a two-byte claim and a 32-byte binding\_hash the token T is 131 bytes. For an edit the CMPS puts Cred\_SW in the first field.
7. `CredP = ECIESb((GP_C, pk_C); T || key_ref || FullPacketHash || BlindShare_key)`, where (GP\_C, pk\_C) is C's Channel Key, the blinded pair on the device routing table line the device chose for C. CredP's plaintext is 203 bytes.
8. `ContP_F = ECIESb((GP_F, pk_F); flags || ContentHash || n || [h(metadata)] || [parent ContentHash])`, and `ContP_I` the same under (GP\_I, pk\_I), the pair on the line chosen for I. The bracketed fields are optional; the parent ContentHash is present only for an edit. `flags` is the byte that enters FullPacketHash, so F and I read it from the packet and never infer it. Each optional field adds 32 bytes, which the leg padding absorbs. The content packet carries no verdict or modification level: F and I take the verdict from the gatekeeper quorum.
9. First-relay wraps: the device first chooses its three lines as described under Role selection and path disjointness. `CredP-1 = ECIES(A-transit_pk; rc_C || CredP)`, `ContP_F-1 = ECIES(D-transit_pk; rc_F || ContP_F)`, `ContP_I-1 = ECIES(G-transit_pk; rc_I || ContP_I)`. `rc_X` is the 16-byte routing code on the line chosen for destination X. The relays resolve it as described under Routing tables; the device does not name the later relays.

### Operation count per transaction

| Operation | Count | Notes |
| --- | --- | --- |
| ECIES encryptions | 7 | T, CredP, ContP\_F, ContP\_I, and three first-relay wraps. CredP, ContP\_F and ContP\_I use the blinded form (ECIESb) |
| Scalar multiplications | 14 | T and the three first-relay wraps: one fixed-base (ephemeral key) and one variable-base (shared secret) each. The three blinded encryptions: two variable-base each, since EPK = e·GP is taken over the line's Generator Point |
| AEAD over small inputs | 7 | The symmetric part of each ECIES encryption. Under 1,000 bytes total. |
| SHA-256 over the candidate image | 1 per image | Dominant cost: roughly 430–600 ms per 25–35 MB image at 13.7 cycles/byte, 800 MHz |
| SHA-256 over small inputs | 1 | FullPacketHash |

**Estimated elliptic-curve cost**, at 527,102 cycles per variable-base multiplication (Cortex-A8 at 800 MHz): 5.3M cycles (6.6 ms) if fixed-base cost is ignored (ten variable-base multiplications), up to 7.4M cycles (9.2 ms) if fixed-base costs the same as variable-base. Precomputed fixed-base multiplication is usually cheaper, so the real figure falls in between.

## Role selection and path disjointness

A transaction uses three paths: a credential path (A → B → C) and two content paths (D → E → F and G → H → I). A, D and G are first relays, and B, E and H are second relays. The three active gatekeepers serve every transaction.

1. **Gatekeepers:** the three currently active gatekeepers, a known rotating set, serve every transaction. They never serve as C, F or I.
2. **Lines:** the device chooses its three paths by choosing three lines of the device routing table (see Routing tables). A line fixes a first relay, a routing code and a destination. The second relay behind it is known only to the table builder and the line's relays. A line has no role: the device decides at use which line is the credential path and which are the content paths.
3. **C:** the device excludes every line whose jurisdiction tag equals its validator's jurisdiction tag, then chooses the credential line from the rest. The validator-to-tag map in the device routing table gives that tag.
4. **F and I:** the other two lines, chosen among all lines, with distinct operators checked by pseudonym. The device skews this choice toward its validator's jurisdiction tag, by an amount the table fixes, so that the destination tags a first relay sees follow the shares of lines in the table. Lines carry no role and C never uses that tag, so without the skew it would appear at about two-thirds of its expected frequency. The builder gives every destination server the same number of lines, so the share of lines in a tag is also the share of servers, and it keeps the share of lines in any one tag at or below two-thirds.
5. **First relays:** A, D and G are outside the jurisdiction the device operates in, because they are the only servers that see its network address. Each first relay carries a jurisdiction tag in the server list of the device routing table.
6. **Distinctness the device checks:** A, D and G carry three different operator pseudonyms (from the server list), and so do C, F and I (from their lines). An operator pseudonym names an operator, not a server, so two servers run by the same operator never fill two of these roles.
7. **Distinctness the builder guarantees:** in every line the first relay, the second relay and the destination are on three different operators, and no destination is a gatekeeper.

**Coincidences the design allows.** The device cannot compare a first relay with another path's destination, because any such check would let a holder of the device routing table read the destination's identity. Two coincidences can therefore occur. First, a second relay can coincide with another path's second relay, first relay or destination. It receives ciphertext of one size class and cannot tell which channel a packet belongs to. Second, a first relay can coincide with the destination of another path in the same transaction, for example A with F. That node then holds the device IP of one packet and the decrypted payload of another. The two packets share no value, so the only join between them is timing (see Hold timing). A first relay is never on the same operator as the destination of its own path, because the builder rules that out inside each line. Because A, D and G are three different operators, no operator receives more than one of the device's three packets as first relay.

**An active gatekeeper may serve as a first relay (A, D or G) for a different transaction.** It never serves as a destination. This carries no correlation risk: a first relay sees the routing code and an opaque payload. With the device routing table it can also read the line the code belongs to, which gives the destination's Channel Key, operator pseudonym and jurisdiction tag. It does not learn the destination's identity, or whether the packet is a credential or a content packet.

## Routing tables

Routing uses a device routing table, which every device holds, and a small relay routing table in each relay.

**Device routing table.** The table builder publishes it for one routing-code generation. It contains:

- A server list: for each first relay, its address, its Server Transit Key (S-transit\_pk), its jurisdiction tag and its operator pseudonym.
- One line per routing code: the first relay (a reference to the server list), the 16-byte routing code, the destination's Channel Key (the blinded pair (GP, pk)), the destination's operator pseudonym and the destination's jurisdiction tag.
- A map from each validator to a jurisdiction tag. Tags are merged so that each covers more than one validator once more than one is registered.
- The generation number. Whether the generation also selects V-Ring is open.

The device routing table does not name the second relay or the destination server.

**Operator pseudonym.** The builder assigns each operator a short value, one byte at the current pool size. It is fresh each generation and identical on every line and server-list entry of that operator, whatever the node's role. It is unrelated to the operator's identity and to the addresses and keys of its nodes. The device uses it only to check that C, F and I differ and that A, D and G differ. Every holder of the table can see which lines share an operator. Whether that is acceptable depends on consortium membership being public, and this is open.

**Channel Key.** A destination node holds one secret scalar sk. For each line, the builder picks a random scalar r, computes GP = r·B, where B is the X25519 base point, and discards r. GP lies in the prime-order subgroup by construction. The builder sends GP to the node, and the node checks that GP is not the identity and that ℓ·GP is the identity, where ℓ is the order of the prime-order subgroup. The check uses an unclamped scalar multiplication, since X25519 clamps its scalar. The node returns pk = sk · GP only if the check passes, and the line carries (GP, pk), which is the node's Channel Key as the device sees it. The device encrypts with ECIESb: it sends EPK = e·GP and derives the AEAD key from e·pk and EPK. The node derives the same value as sk · EPK. Three properties follow:

- The node holds no per-line state and cannot tell which line a packet used. EPK is a uniformly random point whichever GP produced it.
- A holder of the device routing table sees GP and pk but cannot tie them to the node without solving a decisional Diffie-Hellman problem in the prime-order subgroup. Key-privacy of ElGamal with a per-key generator follows from the same assumption (Bellare, Boldyreva, Desai and Pointcheval, ASIACRYPT 2001). The AEAD layer and a table holder who probes a candidate node are not analysed, and the key-derivation function is not yet specified.
- The builder sees every GP and pk but never sk.

A node rejects any GP that fails the subgroup check.

**Relay routing tables.** Each relay holds one table with only the codes it takes part in, as a first relay or as a second relay. A line is `rc → next relay`: the next relay's address and Server Transit Key, which the node already holds in its Server Transit Key table. The first relay's line gives the second relay. The second relay's line gives the destination. The destination holds no line, because it decrypts whatever arrives with its Channel Key scalar sk. With L lines and N nodes, a relay holds about 2L/N lines.

**What each party learns from a routing code.**

| Party | Learns | Does not learn |
| --- | --- | --- |
| First relay, with the device routing table | The line: the destination's blinded pair, pseudonym and jurisdiction tag; the second relay (from its relay table) | The destination's identity; whether the packet is a credential or a content packet |
| Second relay | The previous relay and the destination | The device IP; the credential or content |
| Destination | Nothing about the line | Which line, which first relay |
| Table builder | Every route | — |

The builder knows every route. A colluding relay plus the builder resolves a route.

**Rebuilds.** The triggers are gatekeeper rotation, pool changes and device routing table updates. A rebuild uses fresh routing codes, fresh Generator Points and pairs, and fresh pseudonyms. A packet carrying an old-generation code continues to be relayed under the old generation until it drains, while a packet carrying a new-generation code is relayed under the new one, so the handover is gradual rather than a synchronized cutover. How long an old-generation code remains routable is not yet decided.

## Per-leg message table

There are 19 legs per transaction on the wire, plus match board reads by F and I. Every leg except the match board postings and the registry submissions is padded inside its transit encryption to a size drawn uniformly from its class: **420–460 B** for all legs except the gatekeeper fan-out, which uses **820–860 B**. Raw sizes marked \* are estimates (32-byte Cred\_HW, two-byte claim, 16-byte tx\_id, 8-byte key\_ref); unmarked sizes are measured directly.

| Leg | From → To | Contents | Encrypted under | Receiver learns | Raw size |
| --- | --- | --- | --- | --- | --- |
| CredP-1 | Device → A | rc\_C, CredP | A-transit | Device IP; rc\_C; nothing else readable | 317 B\* |
| CredP-2 | A → B | rc\_C, CredP | B-transit | A's address; rc\_C | 317 B\* |
| CredP-3 | B → C | CredP | C-transit | B's address; CredP contents: T (opaque), key\_ref, FullPacketHash, BlindShare\_key | 301 B\* |
| ContP\_F-1 | Device → D | rc\_F, ContP\_F | D-transit | Device IP; rc\_F | 163 B\* |
| ContP\_F-2 | D → E | rc\_F, ContP\_F | E-transit | D's address; rc\_F | 163 B\* |
| ContP\_F-3 | E → F | ContP\_F | F-transit | E's address; flags, ContentHash, n, and any optional fields | 147 B\* |
| ContP\_I-1 to 3 | Device → G → H → I | As ContP\_F-1 to 3, with rc\_I and ContP\_I | G-, H-, I-transit | As ContP\_F-1 to 3, for I | 163 / 163 / 147 B\* |
| CV-1 | C → V | tx\_id, T, key\_ref, Enc\_FullPacketHash | V-transit | Cred\_HW (Cred\_SW for an edit), replay\_nonce, claim, binding\_hash, Enc\_FullPacketHash (opaque without BlindShare\_key) | 252 B\* |
| CV-2 (verdict) | V → C | tx\_id, verdict, σ\_V | C-transit | The verdict and σ\_V; Enc\_FullPacketHash is not sent again, since C already holds it from step 2. The verdict byte takes the place of the former approval flag. | 130 B\* |
| CV-2 (reject) | V → C | tx\_id, REJECTED | C-transit | Rejection (unregistered credential, binding hash mismatch or replayed nonce). **No signature.** Padded to the same class as a verdict. | 69 B\* |
| GK (three legs) | C → each gatekeeper | FullPacketHash, verdict, σ\_V, BlindShare\_key, σ\_C | GK-transit | FullPacketHash; the verdict; that some ring member of V-Ring signed (not which one); that some ring member signed C's ring too; Enc\_FullPacketHash is not sent, since the gatekeeper recomputes it from BlindShare\_key and FullPacketHash | 690 B\* + V-Ring signature size |
| Post (three legs) | Each gatekeeper → its match board | FullPacketHash, verdict, σ\_C, σ\_GK | Registry Node access only | — | 32 + 1 + 576 + 64 B |
| Reg-F | F → Registry Node | ContentHash, verdict, flags, [h(metadata)], [parent ContentHash], σ\_F | Registry Node transit | ContentHash and the other submitted fields; F's identity | 98 B\*, plus 32 B per optional field |
| Reg-I | I → Registry Node | ContentHash, verdict, flags, [h(metadata)], [parent ContentHash], σ\_I | Registry Node transit | ContentHash and the other submitted fields; I's identity | 98 B\*, plus 32 B per optional field |

**Signatures:**

- `σ_V = RSign(V-Ring; verdict || Enc_FullPacketHash)` — produced for every verdict, including one with a Modification Flag bit set; **not** produced on rejection. It is 64 B with one registered validator and grows with the size of V-Ring.
- `σ_C = RSign(R; FullPacketHash || verdict)` — 576 B for a 17-member ring.
- `σ_GK = Sign(GK-sign_sk; FullPacketHash || σ_C)`.
- `σ_F = Sign(F-sign_sk; ContentHash || verdict || flags || [h(metadata)] || [parent ContentHash])`, and σ\_I the same under I-sign\_sk. Signing every field the record carries, and computing FullPacketHash over the optional fields, means neither content channel server can be made to vouch for a record whose verdict or optional fields differ from what the quorum and the device supplied: a server that alters an optional field computes a FullPacketHash′ that no quorum covers. Both σ\_V and σ\_C cover the verdict, so no party after V can change it. σ\_V, σ\_C and σ\_GK are never posted to the registry. σ\_F and σ\_I travel with the submissions (Reg-F, Reg-I); Registry Nodes verify them at intake and drop them, so a finalized record holds no signature.

`tx_id` is 16 random bytes generated by C per transaction.

**Public verification** is not part of a transaction: a verifier sends a locally computed ContentHash to the registry and receives the record, if one exists.

## Decoy traffic

The system injects decoy transactions to enlarge the candidate pool available to a single compromised component beyond whatever real traffic volume happens to be, and to prevent an observer from estimating real traffic volume from total traffic volume.

A decoy transaction is a genuine transaction from a genuinely registered device credential, not a distinguishable, invalid, or specially marked one. The credentials belong to a pool of identities operated by the same infrastructure that generates decoy traffic and distributes the device routing table, registered with a validator the same way any other device is. Nothing about a decoy transaction differs structurally from a real one at any stage: V approves it normally, C fans it out normally, every signature is genuinely valid, gatekeeper verification and match board quorum proceed normally, and F and I finalize a registry record for it exactly as they would for real content. No party, including V, C, and the gatekeepers, has any way to distinguish a decoy transaction from a real one, because there is nothing structurally different to distinguish. A decoy is an ordinary submission with arbitrary content. Its claim, and therefore its verdict, follows the mix of claims in real traffic, so a decoy record carries a verdict as a real one does and no verdict marks a record as real. The decoy-identity pool must be large enough that no single identity's submission rate looks statistically different from a plausible device's. The pool size is expected to vary with the deployment's own phase and scale, and is not meant to be fixed to a single documented number; it is an operating parameter the deploying infrastructure adjusts as needed, using as many rotating identities as the deployment's own scale calls for.

Decoy traffic follows the same per-transaction construction as real traffic in every respect, including the 2:1 content-to-credential ratio real traffic already produces on its own, so the aggregate ratio stays uninformative about what fraction of traffic is decoy. The injection target is fixed, not scaled to real traffic volume: 60 decoy transactions in flight on average, in addition to whatever real traffic exists, at every level of real traffic. Decoy captures arrive at random times, so the number in flight at any moment varies around that mean.

Every decoy-produced registry record is permanent, exactly like a real one; none are ever removed. Whether and how to prune decoy records to manage hot-storage growth is an open implementation question, deferred rather than specified here.

The second relays (B, E, H) see no difference between decoy and real traffic at any injection rate, since they only ever observe opaque ciphertext.

## Hold timing

Every hold in this spec draws from the same lottery shape — a 10-second tick, geometric release, capped at 3× the hold's own mean — but no longer shares one baseline mean. Each stage's per-tick release probability and cap are set independently to hit that stage's own target mean. The departure bundle inclusion lottery uses a 30-second tick (one per bundle boundary) with a cap at 12 boundaries (3× its 120-second target mean). Settled means:

| Stage | Mean | Std dev | CoV |
| --- | --- | --- | --- |
| Relays (A, B, D, E, G, H), every path | 120 s | 103.1 s | 0.86 |
| Device's credential-channel hold | 120 s | 103.1 s | 0.86 |
| Device's content-channel holds (both) | 240 s | 206.9 s | 0.86 |
| C's hold before sending CV-1 | 30 s | 25.3 s | 0.84 |
| V's hold before sending CV-2 | 30 s | 25.3 s | 0.84 |
| C's serialized fan-out, per draw (one leg leaves per success) | 20 s | 16.6 s | 0.83 |
| Gatekeeper's own hold | 30 s | 25.3 s | 0.84 |
| Departure bundle inclusion lottery | 101 s | 90.9 s | 0.90 |
| F/I's pre-match hold | 240 s | 206.9 s | 0.86 |
| Post-match lottery | 30 s | 25.3 s | 0.84 |
| Registry bundle wait (shared 120 s schedule) | 60 s | 34.6 s | 0.58 |
| Registry posting wait (registry's own 120 s schedule) | 60 s | 34.6 s | 0.58 |

The standard deviations are those of the lottery as simulated: a uniform wait to the first tick, then geometric release on 10-second ticks, capped at three times the mean. The two registry waits are uniform over their 120-second schedules.

**Serialized fan-out.** C's three gatekeeper legs share one draw per tick of C's node clock, from C's receipt of CV-2. Each successful draw sends the next leg, in a random order, and the next draw starts at the following tick, so no two legs leave on the same tick. With 20 s per draw, the legs leave 20, 45 and 70 s after CV-2 on average.

Only stages with a legitimate basis for knowing their own role carry a value different from the shared 120 s figure: the device knows which channel it is constructing a packet for, and F/I know they are F or I. Relays cannot carry a role-specific parameter at all, per the First relay's path-blindness constraint below, so every relay and the device's own credential channel share the same, unelevated 120 s mean. The device's content channels and F/I's pre-match hold share the elevated 240 s mean — exactly double the shared baseline, settling the earlier open choice between that figure and a higher one.

## Departure bundling

The gatekeeper's own hold (see Hold timing) already randomizes when a given packet is selected for release. Departure bundling changes what happens after selection, not the selection itself.

Once a packet's own hold has expired, it does not depart in the next bundle automatically. Instead, at each successive 30-second boundary it draws independently for inclusion in that boundary's bundle: 25% chance of boarding, 75% chance of carrying over to the next boundary. The cap is 12 boundaries (360 seconds, exactly 3× the 120-second mean), after which the packet is included unconditionally. This gives a measured mean inclusion-lottery wait of 101 seconds (see Hold timing); the cap's truncation of the geometric tail brings the realized mean below the 120-second value the uncapped geometric would predict. Bundles therefore contain a mix of packets from a range of arrival times — packets that became ready moments apart can land in different bundles, and packets that became ready up to 360 seconds apart can land in the same one. The earlier, simpler version (every ready packet joined the very next boundary) narrowed this mixing window to near zero, handing a patient observer direct correspondence between "ready time" and "departure bundle."

Packets within the same bundle have no observable order relative to each other, since they depart at the same moment. Measured at the settled operating point (60 decoys in flight): mean 2.33 postings per bundle at one gatekeeper, 32.4% of bundles hold fewer than two postings, and 10.0% are empty.

Whether the first-relay lottery should receive the same bundling treatment is open.

## Registry-level bundling

A content channel server's own confirmed submission, once quorum forms, does not submit to the registry immediately. Instead, it waits for the next registry-level departure bundle, which pools confirmed submissions from every F/I server in the pool, not just the submitting server's own, and commits them together on a shared schedule.

Pooling across the whole F/I population rather than bundling each server's own submissions separately gives a materially larger, more reliable bundle size, for the same reason the decoy target's volume is what makes gatekeeper-level bundling work at all: a bundle drawn from one server's own share of traffic is far smaller than one drawn from the whole pool's aggregate rate.

This does not conflict with the registry's own finalization rule. Two distinct identities agreeing on a record is a property of who submitted it; a shared commit schedule governs only when the registry acts on submissions that already satisfy that rule, not whether they satisfy it.

Decoy transactions, which now complete the full pipeline through to a genuine registry record (see Decoy traffic), participate in registry-level bundling the same way they participate in gatekeeper bundling, and for the same reason: they are what gives any given window enough volume to bundle meaningfully.

The wait for this bundle has a mean of 60 seconds (see Hold timing), settling the window size against the measured rate of confirmed submissions arriving at the registry.

This is an additional hold on top of every other hold already in the pipeline; a real submission does not finalize until the gatekeeper's own hold and bundle, the content channel server's own node-clock hold, and this registry-level bundle have each had their turn. The added latency is real and has not been bounded here.

## Post-match lottery

F and I each independently watch the same match boards for the same quorum condition. If quorum takes
longer to form than either server's own pre-match hold (see the content channel servers' own steps), both
servers spend that time simply waiting on the same external event, and the instant it resolves,
both detect it and both submit at essentially the same moment. Two registry submissions arriving
together is itself a precise, directly observable marker of when quorum completed, and this
marker's quality gets worse as credential-side processing gets slower: at a quorum-formation time
of several minutes, the two submissions land within 5 seconds of each other more than three
quarters of the time.

Each server draws its own, independent delay after quorum is confirmed — mean 30 seconds (see Hold timing) — timed from the moment quorum is actually confirmed rather than from its own, earlier pre-match hold. This keeps F's and I's relative submission timing independent of quorum-formation speed even in the worst case (slow credential-side processing, where both pre-match holds get overtaken by the wait for quorum), and adds further separation on top of the pre-match hold's own randomness in the common, faster case. Keeping the pre-match hold and adding this lottery therefore performs at least as well as the lottery alone everywhere, and strictly better wherever the pre-match hold still matters.

## Checks and actions at each party

Any failed check drops the transaction and triggers that party's discard obligations. No party signs, posts or forwards after a failed check.

### Relays

- **First relay (A, D, G):** decrypts its transit layer and reads the routing code. Its relay routing table gives one next relay for that code, and no further. It re-encrypts `rc || payload` for that relay, holds per the relay timing lottery, then forwards. A first relay cannot tell which of A, D, or G it is playing for a given transaction: its payload is opaque ciphertext regardless of path, and its routing code carries no visible tag distinguishing credential-path from content-path codes, since such a tag would itself be observable. Path-specific timing therefore lives elsewhere — see Hold timing.
- **Second relay (B, E, H):** decrypts, looks up the routing code in its relay routing table to find the destination, holds, then forwards the payload alone under the destination's Server Transit Key.

### Credential channel server C

1. Decrypts CredP-3, then CredP with its Channel Key scalar sk. Obtains T, key\_ref, FullPacketHash, BlindShare\_key.
2. Computes `Enc_FullPacketHash = AEAD(BlindShare_key; FullPacketHash)` with the same fixed nonce as the device. It does not decrypt Enc\_FullPacketHash. The result must equal the device's value, or the validator rejects the submission at its step 3.
3. Generates tx\_id. Holds (see Hold timing), then sends CV-1 (tx\_id, T, key\_ref, Enc\_FullPacketHash) to the validator that key\_ref designates.
4. On **REJECTED**: drops the transaction.
5. On a **verdict**: verifies σ\_V over `verdict || Enc_FullPacketHash` with the Enc\_FullPacketHash it holds; a failed verification drops the transaction. Computes `σ_C = RSign(C-Ring; FullPacketHash || verdict)`. C signs only a verdict that V issued for this transaction.
6. Sends the three GK legs, each carrying FullPacketHash, verdict, σ\_V, BlindShare\_key and σ\_C, encrypted separately. The legs are serialized (see Hold timing): from when C received CV-2 in step 5, C draws once per tick of its node clock, and each successful draw sends the next leg in a random order, so no two legs leave on the same tick.

### Validator V

1. Decrypts CV-1's transit layer, obtaining tx\_id, T (still opaque), key\_ref, Enc\_FullPacketHash. Decrypts T with the V-token\_sk of the Token Key that key\_ref names, to obtain the credential (Cred\_HW, or Cred\_SW for an edit), replay\_nonce and claim.
2. Checks that the credential is on that Token Key's member list.
3. Computes `SHA-256(Enc_FullPacketHash)` over the Enc\_FullPacketHash that C sent and checks that it equals the binding\_hash in the token. A mismatch means that C did not use the device's BlindShare\_key and FullPacketHash, and the validator rejects the submission.
4. Checks that replay\_nonce is not in its log, then logs `(tx_id, replay_nonce)` for up to 3 years.
5. Holds (see Hold timing), then: all three checks pass, computes `verdict = judge(claim)`, signs `verdict || Enc_FullPacketHash` and replies with the verdict and σ\_V; any fails, replies REJECTED with no signature. A verdict with a Modification Flag bit set is a flagged record, not a rejection.

### Gatekeeper

1. Decrypts its GK leg. Obtains FullPacketHash, verdict, σ\_V, BlindShare\_key, σ\_C.
2. Recomputes `Enc_FullPacketHash = AEAD(BlindShare_key; FullPacketHash)` from the BlindShare\_key and FullPacketHash it just received, then verifies σ\_V, over `verdict || Enc_FullPacketHash`, against V-Ring. A mismatched BlindShare\_key or FullPacketHash would produce a different Enc\_FullPacketHash than the one V actually signed, and a different verdict would not verify, so this single check does the work a separate decrypt-and-compare step would otherwise duplicate.
3. Verifies σ\_C, over `FullPacketHash || verdict`, against the current C-Ring.
4. Holds on its own hold clock (see Hold timing), then waits for the next departure bundle per Departure bundling.
5. Posts `(FullPacketHash, verdict, σ_C, σ_GK)` to its match board, together with every other packet in the same departure bundle.

### Content channel servers F and I

1. Decrypt the last content leg, then ContP\_F (or ContP\_I) with their Channel Key scalar sk. Obtain flags, ContentHash, n and any optional fields.
2. Compute `FullPacketHash′ = SHA-256(ContentHash || n || flags || [h(metadata)] || [parent ContentHash])` from the fields in the packet, using the `flags` byte the packet carries.
3. Holds on its own node clock before checking the match boards (see Hold timing).
4. Proceed once FullPacketHash′ appears with the same verdict on at least two distinct match boards, each posting with a valid σ\_GK and a valid σ\_C against the current C-Ring. The verdict F and I record is the one the quorum agrees on. Match match boards that disagree on the verdict do not form a quorum for either pair. If quorum does not form within 30 minutes, drop.
5. Holds again, per Post-match lottery.
6. Waits for the next registry-level departure bundle per Registry-level bundling.
7. Submit Reg-F (or Reg-I), carrying the quorum's verdict, together with every other submission in the same registry-level bundle.

### Registry

1. Verifies each submission's signature against the known server identity keys.
2. Finalizes a record once two submissions from two **distinct** identities agree on every field: ContentHash, verdict, flags, and any optional fields.
3. Duplicate collapse: a ContentHash already on the registry is matched to the existing record, not re-posted.
4. Merges the two submissions into one record at intake and posts it at the next boundary of its own 120-second posting schedule. The posting time is the record's coarsened timestamp. The registry's gossip frames are of one constant size, so an observer of them cannot tell which record a frame belongs to.

## Discard and retention obligations

No party keeps any value that would let it, or a later inspector, pair one leg of a transaction with another. The only per-transaction records that survive are the validator's nonce log (with a shelf life), the match board postings, and the finalized registry record.

| Party | Must discard | When | May retain | Audit |
| --- | --- | --- | --- | --- |
| First relay (A, D, G) | Routing code, and any record of which code went with which packet | On forwarding | Operational logs with coarse timestamps only | Submitter-initiated routing-code sweep |
| Second relay (B, E, H) | Routing code and resolved destination for the packet | On forwarding | Same | Submitter-initiated routing-code sweep |
| C | T, key\_ref, FullPacketHash, BlindShare_key, tx\_id, Enc_FullPacketHash, verdict, σ\_V | After the last GK leg is sent, or at once on rejection or failure | Nothing per transaction | FullPacketHash / BlindShare_key / Enc_FullPacketHash sweep |
| V | claim, verdict, Enc_FullPacketHash, σ\_V | After sending CV-2 | Log entry `(tx_id, replay_nonce)` for up to 3 years. **Never** stored with Cred\_HW, key\_ref or Enc_FullPacketHash. | Schema attestation |
| Gatekeeper | BlindShare_key, Enc_FullPacketHash, σ\_V | After posting, or at once on failure | Its own posting on its match board | FullPacketHash / BlindShare_key / Enc_FullPacketHash sweep |
| Match board | — | — | Postings, for 30 minutes | — |
| F, I | n, FullPacketHash′, and ContentHash if not submitted | After submitting, or on quorum timeout | Nothing per transaction | Submitter-initiated n sweep |
| Registry | — | — | Finalized record, permanently | Public |

**Audit method:** a submitter supplies ContentHash, n and any optional fields from their own past transaction. The governance body recomputes FullPacketHash and searches the named parties' logs for any residual copy. The sweep covers gatekeepers and content channel servers as well as C and the match boards, since all four hold values it can recognize.

## Observables per party

No single party holds both a device identity (Cred\_HW) and anything that leads to the content (FullPacketHash or ContentHash). Each row assumes that party's **full state** is exposed, keys included.

| Party (fully exposed) | Holds | Cannot determine | Formal basis |
| --- | --- | --- | --- |
| Registry observer | ContentHash, verdict, any optional fields, coarse timestamp; at intake, the identities of F and I | Device; manufacturer | Property B |
| First relay (A, D, G) | Device IP; timing; the routing code and, from its relay table, the next relay; opaque payload. With the device routing table: the line the code belongs to | Device credential; content; the destination's identity | Informal (structural); decisional Diffie-Hellman for the blinded key |
| Second relay (B, E, H) | Previous relay's address; destination | Device IP; credential; content | Informal (structural) |
| C | T (opaque), key\_ref (names the Token Key), FullPacketHash, BlindShare_key, Enc_FullPacketHash, verdict, σ\_V, tx\_id | Cred\_HW; ContentHash | Property D |
| V | Cred\_HW, replay\_nonce, claim, binding\_hash, verdict, Enc_FullPacketHash (opaque), tx\_id, C's network address | FullPacketHash; ContentHash | Property E, within one verdict class (see below) |
| Gatekeeper | FullPacketHash, verdict, Enc_FullPacketHash, BlindShare_key, σ\_V, σ\_C, C's network address | Cred\_HW; ContentHash; which validator signed | Property J |
| Match match board reader | FullPacketHash, verdict, σ\_C, σ\_GK | Device; manufacturer; ContentHash | Access is restricted to Registry Nodes by policy, not formally verified |
| F or I | ContentHash, n, FullPacketHash′, verdict, any optional fields, E's (or H's) address, match board postings | Credential; manufacturer | Property F |
| Global passive observer | Sizes and timing only | Everything readable | Properties A–F, J (content); empirical timing evaluation separately |

### Two-party combinations that correlate (outside the t = 1 claim)

Only two pairs combine Cred\_HW with content:

- **V + C** — linked through tx\_id or Enc_FullPacketHash.
- **V + any one gatekeeper** — linked through Enc_FullPacketHash, which V receives from C and signs, and which a gatekeeper also holds next to FullPacketHash in the clear.

**Pairs that do not correlate:** V + F or I (no shared value without BlindShare_key); C + F or I, and a gatekeeper + F or I (a shared FullPacketHash, but no device identity on either side).

**The verdict is a public attribute of the content.** It partitions the record population: an observer or a compromised V that sees a verdict few records share has fewer candidates. Every unedited hardware capture carries the same verdict, and decoys follow the real mix of verdicts. Property E holds within one verdict class. The symbolic model does not measure how much a rare verdict narrows the candidates.

**Network identity (device IP)** is not device identity under the target predicate, but it is a privacy concern. Only the first relays (A, D, G) see it, and they see no content unless the same server is also the destination of another path in the transaction (see Role selection), in which case the only join is timing.

## Registry record

A finalized record is **42 bytes** for a capture with no optional fields. Each optional field, the metadata hash and the parent ContentHash (edits only), adds 32 bytes: 74 bytes with one, 106 bytes with both.

| Field | Size | Notes |
| --- | --- | --- |
| ContentHash | 32 B | SHA-256 of the candidate image |
| verdict | 1 B | V's verdict: a 6-bit Modification Flag and a 2-bit deviation bucket (four classes), zero for an unedited capture. Takes the byte the modification level held before |
| flags | 1 B | Which optional fields follow: bit 0 h(metadata), bit 1 parent ContentHash, other bits zero |
| Timestamp | 8 B | Posting time, coarsened |
| h(metadata) (optional) | 32 B | Enables selective disclosure without putting values on-chain |
| Parent ContentHash (optional, edits only) | 32 B | Lets holders of both images check the relationship directly |

The record contains no device identifier, no manufacturer identifier, and no identity of C or a gatekeeper. It names neither F nor I and holds no signature. σ\_V never leaves C and the gatekeepers, σ\_C and σ\_GK stay on the match boards, and σ\_F and σ\_I, which cover every field of the record including the verdict, travel with the submissions and are verified and dropped by the Registry Nodes at intake.

**Sibling records:** one candidate image per transaction means a capture producing several candidate images (raw, ISP-processed, an adjustment) runs each through its own separate transaction, so their records may finalize close together. A registry observer could then link them to each other, though not to a device.

## Software-validator flow (summary)

An edited image uses the same 19 legs as a capture. The roles change: the Certified Media Processing Software (CMPS) takes the device role, and its developer's server is V. The CMPS holds a software credential, Cred\_SW, a 32-byte secret it generates at install and registers with its developer's validator. It sends Cred\_SW in the token where a capture device sends Cred\_HW.

**Flow:**

1. The CMPS opens a file that verifies against the registry.
2. It tracks every tool used and its intensity until save.
3. At save, it takes patches of the parent image, replays the recorded tools at the recorded intensities on those patches to obtain the Predicted Result, and compares each Predicted Result patch with the same patch of the saved image. Each comparison is a Deviation Measurement. Their cumulative result is the Deviation Score.
4. The CMPS submits a new transaction for the saved image.
5. The Processing Claim in the token carries the five tool-class bits of the tools applied and the Deviation Score. The developer's server, acting as V, judges the claim and returns the Modification Verdict.

**Requirements this flow places on an implementation:**

- **The parent-record reference travels only in the content channel**, never the credential channel. Otherwise V (the developer) would hold the user's Cred\_SW next to a parent ContentHash, which is a single-party correlation.
- **Patch locations are chosen unpredictably, after edits are final.** Predictable patches would let edits outside them go undetected.
- **Software credentials are not hardware-rooted.** The hardware-extraction-resistance argument that holds for a capture device's Cred\_HW does not apply to Cred\_SW; this is a weaker guarantee for edited records than for captures.
- **The bucket boundaries are a deployment parameter.** The CMPS's developer sets where one deviation class ends and the next begins. The protocol carries the resulting bucket and does not interpret it.
- **Threshold judgment is a one-party-managed tool, by necessity, not by oversight.** The developer's validator both runs the judgment software and enforces the threshold, with no independent check on that software's honesty. Co-developing judgment software with every participating developer is not tractable at scale; the accepted mitigation is that the devkit's rules are published and auditable, not that a second party checks each judgment. This is a distinct weakness from the hardware-rooting gap above, not the same one restated.

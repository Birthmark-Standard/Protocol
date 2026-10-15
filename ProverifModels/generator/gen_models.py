#!/usr/bin/env python3
"""Generator for the v90 ProVerif models.  Every model is built from the same
blocks, so the same protocol step is spelled the same way in every file.
Usage: python3 gen_models.py OUTDIR [stage]
The generated .pv files are self-contained; the generator is shipped for audit."""
import os, sys

# ------------------------------------------------------------------ blocks
TYPES = """type skey.
type pkey.
type key.

fun pk(skey): pkey.
fun aenc(bitstring, pkey, bitstring): bitstring.
reduc forall m: bitstring, sk: skey, rnd: bitstring; adec(aenc(m, pk(sk), rnd), sk) = m.

fun senc(bitstring, key): bitstring.
reduc forall m: bitstring, k: key; sdec(senc(m, k), k) = m.

fun sign(bitstring, skey): bitstring.
reduc forall m: bitstring, sk: skey; checksign(sign(m, sk), pk(sk)) = m.

fun hash(bitstring): bitstring.
fun judge(bitstring): bitstring.
"""

def keys(*names_private):
    return "\n".join(f"free {n}: skey [private]." for n in names_private) + "\n"

PUBLIC_NAMES = """free T1: bitstring.
free T2: bitstring.
free imgX: bitstring.
free imgY: bitstring.
free claimX: bitstring.
free claimY: bitstring.
free v_ok: bitstring.
free v_no: bitstring.
free no_sig: bitstring.
"""

def device(send_content_to_i=False):
    """Device: token with claim to V, bundle to C, content packet to F (and I)."""
    s = """let device(token: bitstring, content: bitstring, claim: bitstring) =
    let h = hash(content) in
    new n: bitstring;
    let packethash = hash((h, n)) in
    new rnd_token: bitstring;
    let enc_token = aenc((token, claim), pk(v_token_sk), rnd_token) in
    new rnd_bundle: bitstring;
    let enc_bundle = aenc((enc_token, packethash), pk(c_device_sk), rnd_bundle) in
    new rnd_f: bitstring;
    let enc_content_f = aenc((h, n), pk(f_device_sk), rnd_f) in
"""
    if send_content_to_i:
        s += """    new rnd_i: bitstring;
    let enc_content_i = aenc((h, n), pk(i_device_sk), rnd_i) in
    out(pub, enc_content_i);
"""
    s += """    out(pub, enc_content_f);
    out(pub, enc_bundle).
"""
    return s

def validator(channel_in, channel_out, events=False, twin=False):
    """V decrypts the token, judges the claim, signs (verdict, wrapped).
    twin=True: V folds the credential into the verdict (a deliberate fault)."""
    judged = "judge((claim_in, token_in))" if twin else "judge(claim_in)"
    ev = "        event v_issued(%s, wrapped_in);\n" % judged if events else ""
    return f"""let validator =
    !
    in({channel_in}, (enc_token_in: bitstring, wrapped_in: bitstring));
    let (token_in: bitstring, claim_in: bitstring) = adec(enc_token_in, v_token_sk) in
    if (token_in = T1) || (token_in = T2) then
    (
{ev}        out({channel_out}, (v_ok, sign(({judged}, wrapped_in), v_sign_sk)))
    )
    else
        out({channel_out}, (v_no, no_sig)).
"""

def credential_processor(events=False, wrap=True):
    """wrap=False: C sends PacketHash to V in the clear (fault, used by the VS twin)."""
    ev_asked = "    event c_asked(packethash_in, wrapped);\n" if events else ""
    ev_ok = ("            event c_checked(packethash_in, verdict_in);\n"
             "            event c_checked_w(packethash_in, verdict_in, wrapped_checked);\n") if events else ""
    wrap_expr = "senc(packethash_in, blindshare_key)" if wrap else "packethash_in"
    confirm = ("let packethash_confirmed = sdec(wrapped_checked, blindshare_key) in\n        if packethash_confirmed = packethash_in then"
               if wrap else "if wrapped_checked = packethash_in then")
    return f"""let credential_processor =
    !
    in(pub, enc_bundle_in: bitstring);
    let (enc_token_in: bitstring, packethash_in: bitstring) = adec(enc_bundle_in, c_device_sk) in
    new blindshare_key: key;
    let wrapped = {wrap_expr} in
{ev_asked}    out(c_to_val, (enc_token_in, wrapped));
    in(val_to_c, (decision: bitstring, sig_in: bitstring));
    if decision = v_ok then
    (
        let (verdict_in: bitstring, wrapped_checked: bitstring) = checksign(sig_in, pk(v_sign_sk)) in
        {confirm}
        (
{ev_ok}            let c_signed = sign((packethash_in, verdict_in), c_sign_sk) in
            new rnd_g1: bitstring;
            let pkt_g1 = aenc((packethash_in, verdict_in, sig_in, blindshare_key, c_signed), pk(g1_sk), rnd_g1) in
            new rnd_g2: bitstring;
            let pkt_g2 = aenc((packethash_in, verdict_in, sig_in, blindshare_key, c_signed), pk(g2_sk), rnd_g2) in
            new rnd_g3: bitstring;
            let pkt_g3 = aenc((packethash_in, verdict_in, sig_in, blindshare_key, c_signed), pk(g3_sk), rnd_g3) in
            ( out(pub, pkt_g1) | out(pub, pkt_g2) | out(pub, pkt_g3) )
        )
    ).
"""

def gatekeeper(k, board, events=False, checks="full"):
    """checks: full = verify sigma_V (with BlindShare) and sigma_C;
    none = verify nothing (fault); no_v = skip sigma_V, keep sigma_C (fault)."""
    ev = f"            event board_post_{k}(p, verdict);\n" if events else ""
    head = f"""let gatekeeper_{k} =
    !
    in(pub, pkt_in: bitstring);
    let (p: bitstring, verdict: bitstring, sig: bitstring, k: key, c_sig: bitstring) = adec(pkt_in, g{k}_sk) in
"""
    if checks == "none":
        return head + f"""    let g{k}_signed = sign((p, verdict), g{k}_sign_sk) in
    ( out({board}, g{k}_signed) | out({board}, g{k}_signed) ).
"""
    if checks == "no_v":
        return head + f"""    let (c_p: bitstring, c_verdict: bitstring) = checksign(c_sig, pk(c_sign_sk)) in
    if (c_p = p) && (c_verdict = verdict) then
    (
        let g{k}_signed = sign(c_sig, g{k}_sign_sk) in
        ( out({board}, g{k}_signed) | out({board}, g{k}_signed) )
    ).
"""
    return head + f"""    let (verdict_checked: bitstring, wrapped_checked: bitstring) = checksign(sig, pk(v_sign_sk)) in
    if verdict_checked = verdict then
    (
        let p_confirmed = sdec(wrapped_checked, k) in
        let (c_p: bitstring, c_verdict: bitstring) = checksign(c_sig, pk(c_sign_sk)) in
        if (p_confirmed = p) && (c_p = p) && (c_verdict = verdict) then
        (
{ev}            let g{k}_signed = sign(c_sig, g{k}_sign_sk) in
            ( out({board}, g{k}_signed) | out({board}, g{k}_signed) )
        )
    ).
"""

def quorum(a, b, boards, out_ch, events=False, ccheck=True):
    """ccheck=False: the quorum does not verify C's inner signature (fault)."""
    ev = "event quorum_reached(p%d, v%d); " % (a, a) if events else ""
    chans = out_ch if isinstance(out_ch, (tuple, list)) else (out_ch, out_ch)
    outs = " | ".join(f"out({c}, (p{a}, v{a}))" for c in chans)
    if ccheck:
        reads = f"""    let c{a} = checksign(s{a}, pk(g{a}_sign_sk)) in
    let (p{a}: bitstring, v{a}: bitstring) = checksign(c{a}, pk(c_sign_sk)) in
    let c{b} = checksign(s{b}, pk(g{b}_sign_sk)) in
    let (p{b}: bitstring, v{b}: bitstring) = checksign(c{b}, pk(c_sign_sk)) in
"""
    else:
        reads = f"""    let (p{a}: bitstring, v{a}: bitstring) = checksign(s{a}, pk(g{a}_sign_sk)) in
    let (p{b}: bitstring, v{b}: bitstring) = checksign(s{b}, pk(g{b}_sign_sk)) in
"""
    return f"""let quorum_{a}{b} =
    !
    in({boards[a]}, s{a}: bitstring);
    in({boards[b]}, s{b}: bitstring);
{reads}    if (p{a} = p{b}) && (v{a} = v{b}) then
    ( {ev}( {outs} ) ).
"""

def content_matcher(name, devkey, events=False):
    ev = f"        event reg_out_{name}(h, v_posted);\n" if events else ""
    return f"""let content_matcher_{name} =
    !
    in(pub, enc_content_in: bitstring);
    let (h: bitstring, n: bitstring) = adec(enc_content_in, {devkey}) in
    let candidate = hash((h, n)) in
    in(quorum_out, (posted: bitstring, v_posted: bitstring));
    if candidate = posted then
    (
{ev}        out(registry, (h, v_posted))
    ).
"""

def comment(text):
    return "(* " + text.strip("\n").replace("*)", "* )") + " *)\n\n"

# ------------------------------------------------------------------ models
def cp_model(twin=False):
    """Property D.  C fully compromised, V honest and reachable as an oracle."""
    head = comment("""BM_CredentialProcessor_Compromise.pv   (v90 design, identity swap)
Property D: a fully compromised credential processor C learns nothing about
which device a token belongs to.

What is leaked: c_device_sk and c_sign_sk (all of C's keys). The validator is
honest, but C can submit any (token, wrapped) pair to it and read the answer,
so V is an oracle on pub. Every other key stays private.

What is swapped: the device identity. Device identities T1, T2 and contents
imgX, imgY are PUBLIC names, so the attacker can name a candidate identity.
device(choice[T1,T2], imgX, ...) | device(choice[T2,T1], imgY, ...): the same
contents are authenticated in both worlds, the credentials trade places.
With private T1, T2 the two worlds are the same world with two names
exchanged, and the model would be true for any protocol; with public names it
is not.

What "true" means: nothing C can see or ask V (token blob, PacketHash,
verdict, V's signature) distinguishes T1-then-T2 from T2-then-T1. This is
token confidentiality at C's vantage point. It does not by itself say
anything about content, because the contents are the same in both worlds.

What would make it false: the twin in twins/ makes V fold the credential into
the verdict, judge((claim, token)). C then reads the credential in V's reply
and the worlds differ. That twin must come out NOT equivalent, or this
model's "true" proves nothing.""" + ("\nTHIS FILE IS THE TWIN: V folds the credential into the verdict. Expected: NOT equivalent." if twin else ""))
    s = comment("") if False else ""
    s += head + TYPES + "\nfree pub: channel.\n\n"
    s += keys("v_token_sk", "v_sign_sk", "c_device_sk", "c_sign_sk", "f_device_sk") + "\n"
    s += PUBLIC_NAMES + "\n"
    s += device() + "\n"
    s += validator("pub", "pub", twin=twin) + "\n"
    s += """process
    out(pub, pk(v_token_sk));
    out(pub, pk(v_sign_sk));
    out(pub, c_device_sk);
    out(pub, c_sign_sk);
    out(pub, pk(f_device_sk));
    (
        device(choice[T1,T2], imgX, claimX)
        | device(choice[T2,T1], imgY, claimY)
        | validator
    )
"""
    return s

def liveness_model():
    head = comment("""BM_Pipeline_Liveness.pv   (v90, no choice)
Checks that the honest pipeline used by the identity-swap models actually
runs end to end: V issues a verdict, C accepts it and fans out, each
gatekeeper posts, a two-board quorum forms, and F and I publish a registry
record. Without this check an identity-swap model could be true because the
pipeline is dead and nothing ever reaches the attacker.

Each query below asks whether an event can occur. ProVerif answers
"not event(...) is false" when the event IS reachable. That is the result we
want for every query in this file.
No component is compromised and nothing is swapped.""")
    s = head + TYPES + "\nfree pub: channel.\n"
    s += "free c_to_val: channel [private].\nfree val_to_c: channel [private].\n"
    s += "free match_board_1: channel [private].\nfree match_board_2: channel [private].\nfree match_board_3: channel [private].\n"
    s += "free quorum_out: channel [private].\nfree registry: channel.\n\n"
    s += keys("v_token_sk", "v_sign_sk", "c_device_sk", "c_sign_sk", "f_device_sk", "i_device_sk",
              "g1_sk", "g1_sign_sk", "g2_sk", "g2_sign_sk", "g3_sk", "g3_sign_sk") + "\n"
    s += PUBLIC_NAMES + "\n"
    s += """event v_issued(bitstring, bitstring).
event c_asked(bitstring, bitstring).
event c_checked(bitstring, bitstring).
event c_checked_w(bitstring, bitstring, bitstring).
event board_post_1(bitstring, bitstring).
event board_post_2(bitstring, bitstring).
event board_post_3(bitstring, bitstring).
event quorum_reached(bitstring, bitstring).
event reg_out_f(bitstring, bitstring).
event reg_out_i(bitstring, bitstring).

query v: bitstring, w: bitstring; event(v_issued(v, w)).
query p: bitstring, v: bitstring; event(c_checked(p, v)).
query p: bitstring, v: bitstring; event(board_post_1(p, v)).
query p: bitstring, v: bitstring; event(board_post_2(p, v)).
query p: bitstring, v: bitstring; event(board_post_3(p, v)).
query p: bitstring, v: bitstring; event(quorum_reached(p, v)).
query h: bitstring, v: bitstring; event(reg_out_f(h, v)).
query h: bitstring, v: bitstring; event(reg_out_i(h, v)).

"""
    s += device(send_content_to_i=True) + "\n"
    s += credential_processor(events=True).replace("out(pub, pkt_g1)", "out(pub, pkt_g1)") + "\n"
    s += validator("c_to_val", "val_to_c", events=True) + "\n"
    boards = {1: "match_board_1", 2: "match_board_2", 3: "match_board_3"}
    for k in (1, 2, 3):
        s += gatekeeper(k, boards[k], events=True) + "\n"
    for a, b in ((1, 2), (1, 3), (2, 3)):
        s += quorum(a, b, boards, "quorum_out", events=True) + "\n"
    s += content_matcher("f", "f_device_sk", events=True) + "\n"
    s += content_matcher("i", "i_device_sk", events=True) + "\n"
    s += """process
    out(pub, pk(v_token_sk)); out(pub, pk(v_sign_sk)); out(pub, pk(c_device_sk)); out(pub, pk(c_sign_sk));
    out(pub, pk(f_device_sk)); out(pub, pk(i_device_sk));
    out(pub, pk(g1_sk)); out(pub, pk(g1_sign_sk)); out(pub, pk(g2_sk)); out(pub, pk(g2_sign_sk));
    out(pub, pk(g3_sk)); out(pub, pk(g3_sign_sk));
    (
        device(T1, imgX, claimX)
        | device(T2, imgY, claimY)
        | credential_processor
        | validator
        | gatekeeper_1 | gatekeeper_2 | gatekeeper_3
        | quorum_12 | quorum_13 | quorum_23
        | content_matcher_f | content_matcher_i
    )
"""
    return s

# ------------------------------------------------------------------ shared assembly
ALL_KEYS = ["v_token_sk", "v_sign_sk", "c_device_sk", "c_sign_sk", "f_device_sk", "i_device_sk",
            "g1_sk", "g1_sign_sk", "g2_sk", "g2_sign_sk", "g3_sk", "g3_sign_sk"]

def names_block(private_t1=False):
    s = PUBLIC_NAMES
    if private_t1:
        s = s.replace("free T1: bitstring.\n", "free T1: bitstring [private].\n")
        s = s.replace("free T2: bitstring.\n", "free T2: bitstring [private].\n")
    return s

def chan_block(boards_public, cv_public=False):
    b = "" if boards_public else " [private]"
    cv = "" if cv_public else " [private]"
    return (f"free pub: channel.\nfree c_to_val: channel{cv}.\nfree val_to_c: channel{cv}.\n"
            f"free match_board_1: channel{b}.\nfree match_board_2: channel{b}.\nfree match_board_3: channel{b}.\n"
            "free quorum_out: channel [private].\nfree registry: channel.\n")

BOARDS = {1: "match_board_1", 2: "match_board_2", 3: "match_board_3"}

def publish(keys, leaked):
    return "".join(f"    out(pub, {k});\n" if k in leaked else f"    out(pub, pk({k}));\n" for k in keys)

def pipeline(events=False, omit_g=(), g_checks=None, ccheck=None, f_matcher=True, i_matcher=True,
             v_twin=False, c_wrap=True, quorum_events=None):
    """Return (definitions, process names) for the honest pipeline pieces."""
    g_checks = g_checks or {}
    ccheck = ccheck or {}
    qev = events if quorum_events is None else quorum_events
    d = credential_processor(events=events, wrap=c_wrap) + "\n"
    d += validator("c_to_val", "val_to_c", events=events, twin=v_twin) + "\n"
    names = ["credential_processor", "validator"]
    for k in (1, 2, 3):
        if k in omit_g:
            continue
        d += gatekeeper(k, BOARDS[k], events=False, checks=g_checks.get(k, "full")) + "\n"
        names.append(f"gatekeeper_{k}")
    for a, b in ((1, 2), (1, 3), (2, 3)):
        d += quorum(a, b, BOARDS, "quorum_out", events=qev, ccheck=ccheck.get((a, b), True)) + "\n"
        names.append(f"quorum_{a}{b}")
    if f_matcher:
        d += content_matcher("f", "f_device_sk") + "\n"
        names.append("content_matcher_f")
    if i_matcher:
        d += content_matcher("i", "i_device_sk") + "\n"
        names.append("content_matcher_i")
    return d, names

def par(items):
    return "\n        | ".join(items)

def twin_note(twin, fault):
    return ("\nTHIS FILE IS THE TWIN. Fault: %s Expected: NOT equivalent (or the query FAILS)." % fault) if twin else ""

# ------------------------------------------------------------------ identity-swap models
IS_PROC = ["device(choice[T1,T2], imgX, claimX)", "device(choice[T2,T1], imgY, claimY)"]
V_FAULT = "V folds the credential into the verdict, judge((claim, token))."

def is_model(title, prop, vantage, leaked, boards_public, omit_g, drop_f_matcher, twin, extra_what):
    head = comment(f"""{title}   (v90 design, identity swap)
{prop}

Vantage point: {vantage}
Leaked keys: {', '.join(leaked) if leaked else 'none'}.
{extra_what}

What is swapped: the device identity. T1, T2, imgX, imgY are PUBLIC names.
device(choice[T1,T2], imgX, claimX) | device(choice[T2,T1], imgY, claimY):
the same contents with the same claims are submitted in both worlds; only the
credentials trade places. Pipeline outputs (boards, registry) are therefore
the same in both worlds unless the credential leaks into them.
With private T1, T2 the two worlds would be one world with two names
exchanged, and the model would be true for any protocol.

What "true" means: nothing visible from this vantage point separates
T1-then-T2 from T2-then-T1. It is token confidentiality at this vantage point.
It says nothing about content, because the contents are the same in both worlds.

The twin (twins/ folder) makes V fold the credential into the verdict. The
credential then reaches the boards, F and the registry. The twin must come out
NOT equivalent, or this model's "true" proves nothing.""" + twin_note(twin, V_FAULT))
    d, names = pipeline(omit_g=omit_g, f_matcher=not drop_f_matcher, v_twin=twin)
    s = head + TYPES + "\n" + chan_block(boards_public) + "\n"
    s += keys(*ALL_KEYS) + "\n" + names_block() + "\n"
    s += device(send_content_to_i=True) + "\n" + d
    s += "process\n" + publish(ALL_KEYS, leaked)
    s += "    (\n        " + par(IS_PROC + names) + "\n    )\n"
    return s

def baseline_model(twin=False):
    return is_model("BM_Baseline_Noncorrelation.pv", "Property B: with no party compromised, an observer of the network and the registry cannot tell which device submitted which content.",
                    "a passive observer of the public channel and the public registry.", [], False, (), False, twin,
                    "The boards and the quorum output are private. The observer sees the encrypted packets and the registry records.")

def cs_model(twin=False):
    return is_model("BM_ContentServer_Compromise.pv", "Properties C and F: a fully compromised content server F learns nothing about which device a token belongs to.",
                    "the content server F, with its own keys, plus the public channel, all three match boards and the registry.", ["f_device_sk"], True, (), True, twin,
                    "F's role in the pipeline (decrypt content packets, read the boards, publish) is played by the attacker, so the honest F matcher is omitted. I stays honest.")

def gk_model(twin=False):
    return is_model("BM_Gatekeeper_Compromise.pv", "Property J: a fully compromised gatekeeper G1 learns nothing about which device a token belongs to.",
                    "gatekeeper G1, with its own keys, plus the public channel, all three match boards and the registry.", ["g1_sk", "g1_sign_sk"], True, (1,), False, twin,
                    "G1's role (receive a packet, post to board 1) is played by the attacker, so the honest gatekeeper_1 is omitted. G2, G3, F, I stay honest.")

# ------------------------------------------------------------------ V: PacketHash secrecy (with wrap), twin without wrap
def vs_model(twin=False):
    head = comment("""BM_Validator_PacketHash_Secrecy.pv   (v90 design)
Properties A and E: a fully compromised validator V does not learn PacketHash.

What is leaked: v_token_sk and v_sign_sk (all of V's keys). The attacker plays
V: it reads every (token, wrapped) request C sends and may answer with any
signature. C, the gatekeepers and F stay honest. PacketHash of one device is
a private marker name ph_m; the query asks whether the attacker can ever
learn it.

Why it matters: PacketHash is the join key between the credential path and
the content path. C hides it from V with a BlindShare wrap (senc under a key
V never sees).

What "true" means: query attacker(ph_m) is not derivable. The wrap and the
secrecy of BlindShare_key (which only reaches the gatekeepers, encrypted) hold.
The twin sends PacketHash to V in the clear; the query must then FAIL.""" + twin_note(twin, "C sends PacketHash to V without the BlindShare wrap."))
    ks = ["v_token_sk", "v_sign_sk", "c_device_sk", "c_sign_sk", "f_device_sk",
          "g1_sk", "g1_sign_sk", "g2_sk", "g2_sign_sk", "g3_sk", "g3_sign_sk"]
    s = head + TYPES + "\n" + chan_block(True, cv_public=True) + "\nfree ph_m: bitstring [private].\n\n"
    s += keys(*ks) + "\n" + names_block() + "\n"
    s += "query attacker(ph_m).\n\n"
    dev = device().replace("let device(token", "let device_m(token").replace("let packethash = hash((h, n)) in", "let packethash = ph_m in")
    s += dev + "\n" + credential_processor(wrap=not twin) + "\n"
    s += "process\n" + publish(ks, ["v_token_sk", "v_sign_sk"])
    s += "    (\n        " + par(["device_m(T1, imgX, claimX)", "credential_processor"]) + "\n    )\n"
    return s

# ------------------------------------------------------------------ correspondence models
CORR_EVENTS = """event v_issued(bitstring, bitstring).
event c_asked(bitstring, bitstring).
event c_checked(bitstring, bitstring).
event c_checked_w(bitstring, bitstring, bitstring).
event quorum_reached(bitstring, bitstring).
"""
CORR_QUERIES = """query p: bitstring, v: bitstring; event(quorum_reached(p, v)) ==> event(c_checked(p, v)).
query p: bitstring, v: bitstring, w: bitstring; event(c_checked_w(p, v, w)) ==> event(v_issued(v, w)) && event(c_asked(p, w)).
query p: bitstring, v: bitstring; event(quorum_reached(p, v)).
"""
CORR_EXPECT = """Queries and expected answers.
 1  quorum_reached(p,v) ==> c_checked(p,v)      expected: true
    No quorum forms for a (PacketHash, verdict) pair C did not check.
 2  c_checked_w(p,v,w) ==> v_issued(v,w) && c_asked(p,w)      expected: true
    C accepts only a verdict V issued for a wrapped value C itself sent.
 3  event(quorum_reached(p,v))      expected: "not event(quorum_reached(p,v)) is false"
    Sanity: a quorum is reachable, so 1 and 2 are not true because the pipeline is dead."""

def corr_model(title, prop, leaked, omit_g, g_checks, ccheck, extra, c_sign_alias=False, twin=False, fault=""):
    head = comment(f"""{title}   (v90 design)
{prop}

Leaked keys: {', '.join(leaked)}.
{extra}

Device identity T1 is private here (the attacker cannot forge a token). The
device takes its claim from the attacker, so every verdict judge(claim) is
reachable. Boards are public: the attacker can read and write them. Honest
gatekeepers and the quorum are as in the pipeline of the other models.

{CORR_EXPECT}""" + twin_note(twin, fault))
    ks = [k for k in ALL_KEYS if not (c_sign_alias and k == "c_sign_sk")]
    d, names = pipeline(events=True, omit_g=omit_g, g_checks=g_checks, ccheck=ccheck, f_matcher=False, i_matcher=False)
    s = head + TYPES + "\n" + chan_block(True) + "\n"
    s += keys(*ks) + "\n"
    if c_sign_alias:
        s += "(* c_sign_sk is the signing key of gatekeeper 1, which is leaked: the ring exclusion is absent. *)\nletfun c_sign_sk = g1_sign_sk.\n\n"
    s += names_block(private_t1=True) + "\n" + CORR_EVENTS + "\n" + CORR_QUERIES + "\n"
    s += device() + "\n" + d
    s += "process\n" + publish([k for k in ks], leaked)
    s += "    (\n        " + par(["!(in(pub, claim_a: bitstring); device(T1, imgX, claim_a))"] + names) + "\n    )\n"
    return s

def qf_model(twin=False):
    return corr_model("BM_Quorum_Forgery.pv", "Property I (one gatekeeper): with G1 fully compromised, no quorum forms for a (PacketHash, verdict) pair that C did not check, and C checks only verdicts V issued.",
                      ["g1_sk", "g1_sign_sk"], (1,),
                      {2: "none", 3: "none"} if twin else None, {(1, 2): False, (1, 3): False, (2, 3): False} if twin else None,
                      "G1's role is played by the attacker; board 1 is attacker-controlled. G2 and G3 are honest and check sigma_V (with BlindShare_key) and sigma_C before posting.",
                      twin=twin, fault="honest gatekeepers 2 and 3 verify nothing and the quorum does not verify C's inner signature.")

def qc_model(twin=False):
    return corr_model("BM_Quorum_Collusion.pv", "Property I (two gatekeepers): with G1 and G2 fully compromised, no quorum forms for a (PacketHash, verdict) pair that C did not check.",
                      ["g1_sk", "g1_sign_sk", "g2_sk", "g2_sign_sk"], (1, 2), None, {(1, 2): False} if twin else None,
                      "Two of three boards are attacker-controlled, so a quorum of boards 1 and 2 is free. What the attacker cannot do is make that quorum carry a pair C never signed, because the quorum checks C's signature.",
                      twin=twin, fault="the quorum of boards 1 and 2 does not verify C's signature.")

def re_model(twin=False):
    return corr_model("BM_Quorum_Forgery_RingExclusion.pv", "Sensitivity check, not a paper claim: with the ring exclusion absent, G1's signing key is also C's signing key and is leaked. Which check then protects the quorum?",
                      ["g1_sk", "g1_sign_sk"], (1,), {2: "no_v", 3: "no_v"} if twin else None, None,
                      "c_sign_sk = g1_sign_sk. The attacker can forge C's signature over any pair. Honest gatekeepers 2 and 3 still check sigma_V, and sigma_V needs V's key and BlindShare_key. Expected: query 1 true. In the twin the honest gatekeepers skip the sigma_V check: query 1 must FAIL, which shows that check carries the result.",
                      c_sign_alias=True, twin=twin, fault="honest gatekeepers 2 and 3 skip the sigma_V check.")

# ------------------------------------------------------------------ Registry convergence
def rc_model(twin=False):
    head = comment("""BM_Registry_Convergence.pv   (v90 design)
Property H: one compromised content server F cannot, on its own, make the registry finalise a record I did not sign; and what I signs is bound to what the device sent.

Leaked keys: f_device_sk, f_id_sk, c_sign_sk (F fully compromised; c_sign_sk stands for F's ring key). I is honest. The full honest pipeline runs behind them (device, C, V, three gatekeepers, quorum). The attacker plays F: it reads content packets, boards and quorum output, and may send I any packet.

The content packet carries an optional field m (metadata hash), and PacketHash covers it. The registry
accepts a record when it holds two signatures, one under F's registry key and
one under I's, over the same (ContentHash, verdict, m).

Queries and expected answers.
 a  registry_final(h,v,m) ==> i_signed(h,v,m)      expected: true
    The registry cannot finalise a record I did not sign.
 c  i_signed_n(h,n,v,m) ==> device_sent(h,n,m)      expected: true
    F knows (h,n) and can send I a packet with a different m. PacketHash
    = hash(h,n,m) covers m, so I computes a different PacketHash, finds no
    quorum and signs nothing. The one-byte presence flags of the spec are not
    modelled: the model has a single optional field.
 d  i_signed_n(h,n,v,m) ==> device_sent_hn(h,n)      expected: true
    ContentHash and the nonce, and so the verdict, are bound to a real device submission.
 s  event(registry_final(h,v,m))      expected: "not event(...) is false" (sanity)""" + twin_note(twin, "the registry accepts two signatures from the same signer (both under F's key). Query a must FAIL."))
    ks = ALL_KEYS + ["f_id_sk", "i_id_sk"]
    leaked = ["f_device_sk", "f_id_sk", "c_sign_sk"]
    s = head + TYPES + "\n" + chan_block(True) + "\n" + keys(*ks) + "\n" + names_block(private_t1=True) + "\nfree meta_a: bitstring.\n\n"
    s += CORR_EVENTS + """event device_sent(bitstring, bitstring, bitstring).
event device_sent_hn(bitstring, bitstring).
event i_signed(bitstring, bitstring, bitstring).
event i_signed_n(bitstring, bitstring, bitstring, bitstring).
event registry_final(bitstring, bitstring, bitstring).

query h: bitstring, v: bitstring, m: bitstring; event(registry_final(h, v, m)) ==> event(i_signed(h, v, m)).
query h: bitstring, n: bitstring, v: bitstring, m: bitstring; event(i_signed_n(h, n, v, m)) ==> event(device_sent(h, n, m)).
query h: bitstring, n: bitstring, v: bitstring, m: bitstring; event(i_signed_n(h, n, v, m)) ==> event(device_sent_hn(h, n)).
query h: bitstring, v: bitstring, m: bitstring; event(registry_final(h, v, m)).

"""
    s += """let device_rc(token: bitstring, content: bitstring, claim: bitstring, meta: bitstring) =
    let h = hash(content) in
    new n: bitstring;
    event device_sent(h, n, meta);
    event device_sent_hn(h, n);
    let packethash = hash((h, n)) in
    new rnd_token: bitstring;
    let enc_token = aenc((token, claim), pk(v_token_sk), rnd_token) in
    new rnd_bundle: bitstring;
    let enc_bundle = aenc((enc_token, packethash), pk(c_device_sk), rnd_bundle) in
    new rnd_f: bitstring;
    let enc_content_f = aenc((h, n, meta), pk(f_device_sk), rnd_f) in
    new rnd_i: bitstring;
    let enc_content_i = aenc((h, n, meta), pk(i_device_sk), rnd_i) in
    out(pub, enc_content_i);
    out(pub, enc_content_f);
    out(pub, enc_bundle).

"""
    d = credential_processor(events=True) + "\n" + validator("c_to_val", "val_to_c", events=True) + "\n"
    names = ["credential_processor", "validator"]
    for k in (1, 2, 3):
        d += gatekeeper(k, BOARDS[k]) + "\n"
        names.append(f"gatekeeper_{k}")
    for a, b in ((1, 2), (1, 3), (2, 3)):
        d += quorum(a, b, BOARDS, ("quorum_out", "pub"), events=True) + "\n"
        names.append(f"quorum_{a}{b}")
    d += """let content_matcher_i_rc =
    !
    in(pub, enc_content_in: bitstring);
    let (h: bitstring, n: bitstring, m: bitstring) = adec(enc_content_in, i_device_sk) in
    let candidate = hash((h, n)) in
    in(quorum_out, (posted: bitstring, v_posted: bitstring));
    if candidate = posted then
    (
        event i_signed_n(h, n, v_posted, m);
        event i_signed(h, v_posted, m);
        out(pub, sign((h, v_posted, m), i_id_sk))
    ).

"""
    names.append("content_matcher_i_rc")
    second = "pk(f_id_sk)" if twin else "pk(i_id_sk)"
    # registry: first signature under F's key, second under I's key (twin: F's key again)
    d += f"""let registry_rule =
    !
    in(pub, (s1: bitstring, s2: bitstring));
    let (h1: bitstring, v1: bitstring, m1: bitstring) = checksign(s1, pk(f_id_sk)) in
    let (h2: bitstring, v2: bitstring, m2: bitstring) = checksign(s2, {second}) in
    if (h1 = h2) && (v1 = v2) && (m1 = m2) then
        event registry_final(h1, v1, m1);
        out(registry, (h1, v1, m1)).

"""
    names.append("registry_rule")
    s += d
    s += "process\n" + publish(ks, leaked)
    s += "    (\n        " + par(["!(in(pub, claim_a: bitstring); device_rc(T1, imgX, claim_a, meta_a))"] + names) + "\n    )\n"
    s = s.replace("let packethash = hash((h, n)) in", "let packethash = hash((h, n, meta)) in")
    s = s.replace("let candidate = hash((h, n)) in", "let candidate = hash((h, n, m)) in")
    return s

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
    print("wrote", path)

if __name__ == "__main__":
    out = sys.argv[1]
    models = {
        "BM_Pipeline_Liveness": (liveness_model, False),
        "BM_Baseline_Noncorrelation": (baseline_model, True),
        "BM_CredentialProcessor_Compromise": (cp_model, True),
        "BM_ContentServer_Compromise": (cs_model, True),
        "BM_Gatekeeper_Compromise": (gk_model, True),
        "BM_Validator_PacketHash_Secrecy": (vs_model, True),
        "BM_Registry_Convergence": (rc_model, True),
        "BM_Quorum_Forgery": (qf_model, True),
        "BM_Quorum_Collusion": (qc_model, True),
        "BM_Quorum_Forgery_RingExclusion": (re_model, True),
    }
    for name, (fn, has_twin) in models.items():
        write(f"{out}/{name}.pv", fn())
        if has_twin:
            write(f"{out}/twins/{name}_TWIN.pv", fn(twin=True))

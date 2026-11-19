# Part C candidates: DAA or EPID signature

This file surveys libraries for one operation: a device signs a 32-byte ContentHash with a DAA or EPID signature, in anonymous mode, in software, with no TPM. The target is a Raspberry Pi 4 Model B, Cortex-A72 at 1.5 GHz, aarch64 Linux. The Cortex-A72 in the Pi 4 has no PMULL, AES or SHA instructions.

Nothing here is a measurement. Research date: 2026-11-19. Sources were read at the commits listed, or in the package named.

## Criteria

- Builds on a Raspberry Pi 4 without a TPM.
- License.
- Last commit.
- Scheme: DAA, EPID, or another group signature.
- Signs in anonymous mode: no basename, so two signatures by one member cannot be linked.
- Curve, and the security level the library states.

## Candidates

| Candidate | Scheme | Anonymous mode | Curve and stated security | License | Source, last commit | Builds without a TPM on aarch64 |
|---|---|---|---|---|---|---|
| **Xaptum ECDAA** | FIDO ECDAA (DAA) | Yes. Signing with no basename gives a signature with no pseudonym. | FP256BN, BN254, BN254CX or BLS383, chosen at build time. Pairing arithmetic comes from Xaptum's fork of AMCL 4.7.3. AMCL's documentation states that a 256-bit BN curve gives about 100 bits of security and that BLS383 reaches the AES-128 level. | Apache-2.0 (ecdaa and AMCL) | github.com/xaptum/ecdaa @ `92f93059dfe23c061a2372c897bdcaad0d917487` (2021-08-13). AMCL: github.com/xaptum/amcl @ `4bb6af4eb53c219fb4e5b16ef020469425826977` (tag 4.7.3, 2018-07-23). | Yes. Portable C. `ECDAA_TPM_SUPPORT=OFF` builds the software library. It builds with GCC 13 on x86-64 and cross-builds for aarch64. Its test suite passes on x86-64 and under QEMU emulating a Cortex-A72. |
| **Intel EPID SDK** | Intel EPID 2.0 (EPID) | Yes. Signing with no basename uses a random base. | EPID 2.0 parameters over a 256-bit prime field (`epid20_q` in `epid/internal/tinymath/src/fq.c`). The SDK documentation states no security level. | Apache-2.0 | github.com/Intel-EPID-SDK/epid-sdk @ `389426ff4ba2286d2e133bec29d178427d434d8c` (2023-01-03, a README change). Code at tag v8.0.0, `ceb0a9e77b01b5e9c67619aeddae7b42dad71134` (2020-11-13). The README states that Intel no longer maintains the project. | Yes, with two flag changes. The SDK has a software-only member library ("tiny member") and a TPM member library ("split member"). Its CMake adds `-Werror`, and GCC 12 and later stop the build on warnings in its code. With GCC 13 at the SDK's `-Os`, `EpidProvisionKey` rejects the SDK's own test key; with `-fno-strict-aliasing` the SDK's stored test signature verifies. With both changes it builds on x86-64 and cross-builds for aarch64, and its stored signature verifies under QEMU emulating a Cortex-A72. The SDK has no issuer. Its test data supplies a group and member keys. Its bundled googletest does not build with GCC 13 under `-Werror`. |
| **libgroupsig** (IBM) | Group signatures with an opener: KTY04, BBS04, CPY06, GL19, PS16, KLAP20, DL21 and DL21SEQ behind one API. Not DAA or EPID. | A signature is anonymous to a verifier. `groupsig_open` returns the signer's identity to the holder of the manager key. | Not checked. | Apache-2.0 | The library's README, license and headers, as bundled in the npm package `jsgroupsig` 1.1.0 (2021-05-31). The README describes it as "an extensible library for group signatures". | Not built. |
| **ubitech/daa** | DAA for TPM 2.0 | Not checked. | FP256BN from MIRACL Core, and a BNP256 group defined in Mbed TLS. The README states no security level. | MIT | github.com/ubitech/daa @ `ce85eb1ff7f3206bc98527e1355065ac0b379019` (2025-08-08, the only commit date in the history). | No software-only signing. The member's signature runs the TPM commands TPM2_Commit and TPM2_Sign through the IBM TSS. The README names the IBM TPM 2.0 simulator, bundled as `ibmtpm1682/`, and states that the code can be adapted to hardware TPMs. |
| **whotracksme/anonymous-credentials** | DAA from Camenisch-Lysyanskaya signatures (IACR ePrint 2015/1246), with a software-only Join. | Yes. A basename is optional. | BN254, from MIRACL Core. The README states roughly 100-bit security. | MPL-2.0 | github.com/whotracksme/anonymous-credentials @ `4cb110e9be2565d2c12a84142c4d7ee9e0dd5e1c` (2022-03-21). | Not built. The core is C, but the library builds as a NodeJS native module, WebAssembly or asm.js, and documents only its JavaScript API. |

## Choice

**Primary: Xaptum ECDAA, curve FP256BN.**

- It implements FIDO ECDAA, which is DAA.
- FP256BN is the curve the library requires for its TPM 2.0 support, so a software signature and a TPM signature use the same curve.
- It builds as a software library with no TPM and no source change.
- Its own test suite passes on aarch64 under QEMU.
- It runs the full Join in software: issuer key pair, member key pair with proof, credential, and the member's check of the credential.

**Second: Intel EPID SDK, tiny member.**

- It implements EPID 2.0.
- Its tiny member is software only.
- It needs two compiler-flag changes to build and compute correctly with current GCC.
- Its group and member keys come from the SDK's test data, because the SDK has no issuer.

Both are measured. Each output names the scheme.

Not measured:

- libgroupsig, because it implements group signatures with an opener, which are not DAA or EPID.
- ubitech/daa, because its signing needs a TPM or a TPM simulator.
- whotracksme/anonymous-credentials, because it offers no C API.

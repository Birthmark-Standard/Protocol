// Copyright (C) 2024-2026 The Birthmark Standard Foundation
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// SPDX-License-Identifier: Apache-2.0

// Part B: one zero-knowledge proof of knowledge of M with SHA-256(M) = H,
// H public, using the Longfellow-zk library.
//
// The circuit is built here, not taken from Longfellow's benchmark:
//   - H is a public input. Longfellow's own SHA-256 benchmark marks no input
//     public, so it does not prove this statement.
//   - The message length is fixed by the circuit, as in Hekate's statement.
//     The padding bytes are circuit constants. The message bytes and the
//     per-block witnesses are private inputs.
//   - Blocks are chained with FlatSHA256Circuit::assert_transform_block.
//     Longfellow's variable-length API holds the block count in 8 bits and
//     stops at 255 blocks; this circuit has no such limit.
//
// A run: set up the circuit once, by construction or by loading a file that
// --save-circuit wrote, then prove `--repeats` times, each over a fresh random
// M of the same length held in RAM. Each repeat times witness generation,
// prove, serialization and verification, and records peak resident memory.
// The first repeat also runs three checks, each in a forked child because
// Longfellow aborts on some malformed inputs: the honest proof verifies, a
// proof with one flipped byte is rejected, and the honest proof is rejected
// against a wrong H.
//
// Output: JSON lines on stdout (setup, one per repeat, done). Exit status 0
// if every check passed, 2 if any failed, 1 on bad arguments.

#include <openssl/rand.h>
#include <openssl/sha.h>
#include <sys/resource.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#include <string>
#include <vector>

#include "algebra/convolution.h"
#include "algebra/fp.h"
#include "algebra/fp2.h"
#include "algebra/reed_solomon.h"
#include "arrays/dense.h"
#include "circuits/compiler/compiler.h"
#include "circuits/logic/bit_plucker.h"
#include "circuits/logic/bit_plucker_encoder.h"
#include "circuits/logic/compiler_backend.h"
#include "circuits/logic/logic.h"
#include "circuits/sha/flatsha256_circuit.h"
#include "circuits/sha/flatsha256_witness.h"
#include "gf2k/gf2_128.h"
#include "gf2k/lch14_reed_solomon.h"
#include "proto/circuit_reader.h"
#include "proto/circuit_writer.h"
#include "random/secure_random_engine.h"
#include "random/transcript.h"
#include "sumcheck/circuit.h"
#include "util/log.h"
#include "util/readbuffer.h"
#include "zk/zk_proof.h"
#include "zk/zk_prover.h"
#include "zk/zk_verifier.h"

namespace {

using namespace proofs;

// Ligero parameters of Longfellow's version-7 mdoc proofs: rate 7, 132
// queries, which the source states as about 109 bits of statistical security.
constexpr size_t kLigeroRate = 7;
constexpr size_t kLigeroNreq = 132;
constexpr size_t kTranscriptVersion = 7;
const uint8_t kTranscriptLabel[] = "birthmark-partB";

const uint32_t kSha256Iv[8] = {0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                               0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};

double now_s() {
  timespec t;
  clock_gettime(CLOCK_MONOTONIC_RAW, &t);
  return t.tv_sec + t.tv_nsec * 1e-9;
}

// SHA-256 padding of M, as in FIPS 180-4 section 5.1.1.
std::vector<uint8_t> sha256_pad(const std::vector<uint8_t>& m) {
  std::vector<uint8_t> p(m);
  p.push_back(0x80);
  while (p.size() % 64 != 56) p.push_back(0);
  uint64_t bits = static_cast<uint64_t>(m.size()) * 8;
  for (int i = 7; i >= 0; --i) p.push_back((bits >> (8 * i)) & 0xff);
  return p;
}

struct HostWitness {
  std::vector<FlatSHA256Witness::BlockWitness> bw;
  uint8_t digest[32];
};

// Per-block witnesses by Longfellow's own block function, chained on the host.
void make_witness(const std::vector<uint8_t>& padded, HostWitness& w) {
  size_t nb = padded.size() / 64;
  uint32_t h[8];
  memcpy(h, kSha256Iv, sizeof h);
  w.bw.resize(nb);
  for (size_t b = 0; b < nb; ++b) {
    uint32_t in[16];
    for (size_t i = 0; i < 16; ++i) {
      const uint8_t* q = &padded[64 * b + 4 * i];
      in[i] = (uint32_t(q[0]) << 24) | (uint32_t(q[1]) << 16) |
              (uint32_t(q[2]) << 8) | uint32_t(q[3]);
    }
    FlatSHA256Witness::BlockWitness& x = w.bw[b];
    FlatSHA256Witness::transform_and_witness_block(in, h, x.outw, x.oute,
                                                   x.outa, x.h1);
    memcpy(h, x.h1, sizeof h);
  }
  for (size_t i = 0; i < 8; ++i) {
    w.digest[4 * i + 0] = h[i] >> 24;
    w.digest[4 * i + 1] = h[i] >> 16;
    w.digest[4 * i + 2] = h[i] >> 8;
    w.digest[4 * i + 3] = h[i];
  }
}

template <class Field, size_t kPluckerSize>
std::unique_ptr<Circuit<Field>> make_circuit(size_t msg_len,
                                             const std::vector<uint8_t>& padded,
                                             const Field& f) {
  using CompilerBackend = CompilerBackend<Field>;
  using LogicCircuit = Logic<Field, CompilerBackend>;
  using v8 = typename LogicCircuit::v8;
  using v32 = typename LogicCircuit::v32;
  using v256 = typename LogicCircuit::v256;
  using Plucker = BitPlucker<LogicCircuit, kPluckerSize>;
  using FlatShaC = FlatSHA256Circuit<LogicCircuit, Plucker>;
  using BlockWitness = typename FlatShaC::BlockWitness;

  set_log_level(ERROR);
  QuadCircuit<Field> Q(f);
  const CompilerBackend cbk(&Q);
  const LogicCircuit lc(&cbk, f);
  FlatShaC sha(lc);
  Plucker bp(lc);

  // Public inputs: H.
  v256 target = lc.template vinput<256>();
  Q.private_input();

  // Private inputs: the message bytes, then the block witnesses.
  size_t nb = padded.size() / 64;
  std::vector<v8> in(64 * nb);
  for (size_t i = 0; i < in.size(); ++i) {
    in[i] = i < msg_len ? lc.template vinput<8>()
                        : lc.template vbit<8>(padded[i]);
  }
  std::vector<BlockWitness> bw(nb);
  for (size_t b = 0; b < nb; ++b) bw[b].input(lc);

  v32 h0[8];
  for (size_t i = 0; i < 8; ++i) h0[i] = lc.template vbit<32>(kSha256Iv[i]);
  std::vector<v32> words(16);
  for (size_t b = 0; b < nb; ++b) {
    const v8* blk = &in[64 * b];
    for (size_t i = 0; i < 16; ++i) {
      // Big-endian: the first argument of vappend is the low half.
      words[i] = lc.vappend(lc.vappend(blk[4 * i + 3], blk[4 * i + 2]),
                            lc.vappend(blk[4 * i + 1], blk[4 * i + 0]));
    }
    if (b == 0) {
      sha.assert_transform_block(words.data(), h0, bw[b].outw, bw[b].oute,
                                 bw[b].outa, bw[b].h1);
    } else {
      sha.assert_transform_block(words.data(), bw[b - 1].h1, bw[b].outw,
                                 bw[b].oute, bw[b].outa, bw[b].h1);
    }
  }

  // The last chaining value equals H, in the bit order of
  // FlatSHA256Circuit::assert_hash.
  v256 mm;
  for (size_t j = 0; j < 8; ++j) {
    v32 hj = bp.unpack_v32(bw[nb - 1].h1[j]);
    for (size_t k = 0; k < 32; ++k) mm[(7 - j) * 32 + k] = hj[k];
  }
  lc.vassert_eq(mm, target);

  return Q.mkcircuit(/*nc=*/1);
}

template <class Field>
void push_bits(uint8_t a, size_t& wi, Dense<Field>& W, const Field& f) {
  for (size_t i = 0; i < 8; ++i) W.v_[wi++] = (a >> i) & 1 ? f.one() : f.zero();
}

template <class Field>
void push_digest(const uint8_t digest[32], size_t& wi, Dense<Field>& W,
                 const Field& f) {
  for (size_t j = 0; j < 256; ++j) {
    W.v_[wi++] = (digest[(255 - j) / 8] >> (j % 8)) & 1 ? f.one() : f.zero();
  }
}

// Inputs in declaration order: the constant one, H, message bytes, witnesses.
template <class Field, size_t kPluckerSize>
bool fill_inputs(const Circuit<Field>& c, const std::vector<uint8_t>& msg,
                 const HostWitness& w, const Field& f, Dense<Field>& W,
                 Dense<Field>& pub) {
  size_t wi = 0;
  W.v_[wi++] = f.one();
  push_digest(w.digest, wi, W, f);
  if (wi != c.npub_in) return false;
  for (size_t i = 0; i < pub.v_.size(); ++i) pub.v_[i] = W.v_[i];
  for (uint8_t byte : msg) push_bits(byte, wi, W, f);
  BitPluckerEncoder<Field, kPluckerSize> enc(f);
  auto push_packed = [&](uint32_t x) {
    for (const auto& e : enc.mkpacked_v32(x)) W.v_[wi++] = e;
  };
  for (const auto& b : w.bw) {
    for (size_t k = 0; k < 48; ++k) push_packed(b.outw[k]);
    for (size_t k = 0; k < 64; ++k) {
      push_packed(b.oute[k]);
      push_packed(b.outa[k]);
    }
    for (size_t k = 0; k < 8; ++k) push_packed(b.h1[k]);
  }
  return wi == c.ninputs;
}

template <class Field, class RSFactory>
bool verify_bytes(const Circuit<Field>& c, const RSFactory& rsf, const Field& f,
                  const std::vector<uint8_t>& buf, const Dense<Field>& pub) {
  ZkProof<Field> zkpv(c, kLigeroRate, kLigeroNreq);
  ReadBuffer rb(buf);
  if (!zkpv.read(rb, f)) return false;
  ZkVerifier<Field, RSFactory> verifier(c, rsf, kLigeroRate, kLigeroNreq, f);
  Transcript tv(kTranscriptLabel, sizeof kTranscriptLabel - 1,
                kTranscriptVersion);
  verifier.recv_commitment(zkpv, tv);
  return verifier.verify(zkpv, pub, tv);
}

// Runs verify in a child. Returns "accepted", "rejected" or "aborted".
template <class Field, class RSFactory>
std::string verify_in_child(const Circuit<Field>& c, const RSFactory& rsf,
                            const Field& f, const std::vector<uint8_t>& buf,
                            const Dense<Field>& pub) {
  fflush(stdout);
  pid_t pid = fork();
  if (pid == 0) {
    bool ok = verify_bytes(c, rsf, f, buf, pub);
    _exit(ok ? 0 : 1);
  }
  int status = 0;
  if (pid < 0 || waitpid(pid, &status, 0) != pid) return "fork_failed";
  if (WIFEXITED(status)) return WEXITSTATUS(status) == 0 ? "accepted" : "rejected";
  return "aborted";
}

long max_rss_kb() {
  rusage u;
  getrusage(RUSAGE_SELF, &u);
  return u.ru_maxrss;  // kilobytes on Linux
}

struct Options {
  std::string field;
  size_t bytes = 0;
  int repeats = 1;
  std::string save_circuit;  // build, write the circuit, exit
  std::string load_circuit;  // read the circuit instead of building it
};

bool write_file(const std::string& path, const std::vector<uint8_t>& b) {
  FILE* fp = fopen(path.c_str(), "wb");
  if (!fp) return false;
  bool ok = fwrite(b.data(), 1, b.size(), fp) == b.size();
  return fclose(fp) == 0 && ok;
}

bool read_file(const std::string& path, std::vector<uint8_t>& b) {
  FILE* fp = fopen(path.c_str(), "rb");
  if (!fp) return false;
  fseek(fp, 0, SEEK_END);
  long n = ftell(fp);
  fseek(fp, 0, SEEK_SET);
  b.resize(n < 0 ? 0 : static_cast<size_t>(n));
  bool ok = n >= 0 && fread(b.data(), 1, b.size(), fp) == b.size();
  fclose(fp);
  return ok;
}

// Setup once (build or load the circuit), then `repeats` proofs, each over a
// fresh random M of the same length. One JSON line for the setup, one per
// repeat, one at the end. The tampered-proof and wrong-H checks run on the
// first repeat.
template <class Field, size_t kPluckerSize, class RSFactory>
int run(const char* field_name, FieldID field_id, const Field& f,
        const RSFactory& rsf, const Options& opt) {
  const size_t msg_len = opt.bytes;
  std::vector<uint8_t> zeros(msg_len, 0);
  std::vector<uint8_t> padded = sha256_pad(zeros);  // padding depends on length only
  const size_t nb = padded.size() / 64;

  double t0 = now_s();
  std::unique_ptr<Circuit<Field>> c;
  std::string setup = "circuit_construction";
  size_t circuit_file_bytes = 0;
  if (!opt.load_circuit.empty()) {
    setup = "circuit_load";
    std::vector<uint8_t> bytes;
    if (read_file(opt.load_circuit, bytes)) {
      circuit_file_bytes = bytes.size();
      ReadBuffer rb(bytes);
      CircuitReader<Field> reader(f, field_id);
      c = reader.from_bytes(rb, /*enforce_circuit_id=*/true);
    }
  } else {
    c = make_circuit<Field, kPluckerSize>(msg_len, padded, f);
  }
  double t_setup = now_s() - t0;
  if (!c) {
    printf("{\"type\":\"setup\",\"status\":\"failed\",\"setup\":\"%s\"}\n", setup.c_str());
    return 2;
  }

  size_t layer_wires = 0;
  for (const auto& layer : c->l) layer_wires += layer.nw;
  printf(
      "{\"type\":\"setup\",\"status\":\"ok\",\"prover\":\"longfellow-zk\","
      "\"field\":\"%s\",\"plucker_size\":%zu,\"zero_knowledge\":true,"
      "\"ligero_rate\":%zu,\"ligero_queries\":%zu,\"message_bytes\":%zu,"
      "\"compressions\":%zu,\"setup\":\"%s\",\"setup_s\":%.6f,"
      "\"circuit_file_bytes\":%zu,\"circuit\":{\"layers\":%zu,\"inputs\":%zu,"
      "\"public_inputs\":%zu,\"layer_wires\":%zu,\"quad_terms\":%zu},"
      "\"max_rss_kb_after_setup\":%ld}\n",
      field_name, kPluckerSize, kLigeroRate, kLigeroNreq, msg_len, nb,
      setup.c_str(), t_setup, circuit_file_bytes, c->nl, c->ninputs, c->npub_in,
      layer_wires, c->nterms(), max_rss_kb());
  fflush(stdout);

  if (!opt.save_circuit.empty()) {
    std::vector<uint8_t> bytes;
    t0 = now_s();
    CircuitWriter<Field> writer(f, field_id);
    writer.to_bytes(*c, bytes);
    bool ok = write_file(opt.save_circuit, bytes);
    printf("{\"type\":\"circuit_saved\",\"status\":\"%s\",\"bytes\":%zu,\"write_s\":%.6f}\n",
           ok ? "ok" : "failed", bytes.size(), now_s() - t0);
    return ok ? 0 : 2;
  }

  bool all_ok = true;
  for (int r = 0; r < opt.repeats; ++r) {
    std::vector<uint8_t> msg(msg_len);
    if (msg_len && RAND_bytes(msg.data(), static_cast<int>(msg_len)) != 1) return 2;
    std::vector<uint8_t> pm = sha256_pad(msg);

    t0 = now_s();
    HostWitness w;
    make_witness(pm, w);
    double t_witness_host = now_s() - t0;
    uint8_t ref[32];
    ::SHA256(msg.data(), msg.size(), ref);  // OpenSSL, not proofs::SHA256
    bool hash_matches = memcmp(ref, w.digest, 32) == 0;

    t0 = now_s();
    Dense<Field> W(1, c->ninputs);
    Dense<Field> pub(1, c->npub_in);
    bool inputs_ok = fill_inputs<Field, kPluckerSize>(*c, msg, w, f, W, pub);
    double t_fill = now_s() - t0;

    bool prove_ok = false, verify_ok = false;
    double t_prove = 0, t_serialize = 0, t_verify = 0;
    std::string honest = "not_run", tampered = "not_run", wrong_h = "not_run";
    size_t proof_bytes = 0;
    if (inputs_ok) {
      std::vector<uint8_t> buf;
      {
        ZkProof<Field> zkpr(*c, kLigeroRate, kLigeroNreq);
        Transcript tp(kTranscriptLabel, sizeof kTranscriptLabel - 1,
                      kTranscriptVersion);
        SecureRandomEngine rng;
        t0 = now_s();
        ZkProver<Field, RSFactory> prover(*c, f, rsf);
        prover.commit(zkpr, W, tp, rng);
        prove_ok = prover.prove(zkpr, W, tp);
        t_prove = now_s() - t0;
        t0 = now_s();
        zkpr.write(buf, f);
        t_serialize = now_s() - t0;
      }
      proof_bytes = buf.size();

      t0 = now_s();
      verify_ok = verify_bytes(*c, rsf, f, buf, pub);
      t_verify = now_s() - t0;

      if (r == 0) {
        honest = verify_in_child(*c, rsf, f, buf, pub);
        std::vector<uint8_t> bad = buf;
        bad[bad.size() / 2] ^= 0x01;
        tampered = verify_in_child(*c, rsf, f, bad, pub);
        Dense<Field> wrong(1, c->npub_in);
        for (size_t i = 0; i < wrong.v_.size(); ++i) wrong.v_[i] = pub.v_[i];
        wrong.v_[1] = pub.v_[1] == f.zero() ? f.one() : f.zero();  // flip one bit of H
        wrong_h = verify_in_child(*c, rsf, f, buf, wrong);
      }
    }
    bool ok = hash_matches && inputs_ok && prove_ok && verify_ok &&
              (r != 0 || (honest == "accepted" &&
                          (tampered == "rejected" || tampered == "aborted") &&
                          (wrong_h == "rejected" || wrong_h == "aborted")));
    all_ok = all_ok && ok;
    printf(
        "{\"type\":\"run\",\"repeat\":%d,\"message_bytes\":%zu,\"compressions\":%zu,"
        "\"time_s\":{\"host_witness\":%.6f,\"fill_inputs\":%.6f,\"prove\":%.6f,"
        "\"serialize\":%.6f,\"verify\":%.6f},\"proof_bytes\":%zu,"
        "\"checks\":{\"hash_matches_openssl\":%s,\"inputs_complete\":%s,"
        "\"prover_ok\":%s,\"verify_honest\":%s,\"verify_honest_child\":\"%s\","
        "\"verify_tampered_proof\":\"%s\",\"verify_wrong_h\":\"%s\"},"
        "\"all_checks_passed\":%s,\"max_rss_kb\":%ld}\n",
        r, msg_len, nb, t_witness_host, t_fill, t_prove, t_serialize, t_verify,
        proof_bytes, hash_matches ? "true" : "false", inputs_ok ? "true" : "false",
        prove_ok ? "true" : "false", verify_ok ? "true" : "false", honest.c_str(),
        tampered.c_str(), wrong_h.c_str(), ok ? "true" : "false", max_rss_kb());
    fflush(stdout);
  }
  printf("{\"type\":\"done\",\"all_checks_passed\":%s,\"max_rss_kb\":%ld}\n",
         all_ok ? "true" : "false", max_rss_kb());
  return all_ok ? 0 : 2;
}

int usage(const char* argv0) {
  fprintf(stderr,
          "usage: %s --field gf2_128|fp64_2 --bytes N [--repeats R]\n"
          "          [--save-circuit FILE | --load-circuit FILE]\n",
          argv0);
  return 1;
}

}  // namespace

int main(int argc, char** argv) {
  Options opt;
  long long bytes = -1;
  for (int i = 1; i < argc; ++i) {
    if (!strcmp(argv[i], "--field") && i + 1 < argc) {
      opt.field = argv[++i];
    } else if (!strcmp(argv[i], "--bytes") && i + 1 < argc) {
      bytes = atoll(argv[++i]);
    } else if (!strcmp(argv[i], "--repeats") && i + 1 < argc) {
      opt.repeats = atoi(argv[++i]);
    } else if (!strcmp(argv[i], "--save-circuit") && i + 1 < argc) {
      opt.save_circuit = argv[++i];
    } else if (!strcmp(argv[i], "--load-circuit") && i + 1 < argc) {
      opt.load_circuit = argv[++i];
    } else {
      return usage(argv[0]);
    }
  }
  if (bytes < 0 || opt.repeats < 1 ||
      (!opt.save_circuit.empty() && !opt.load_circuit.empty())) {
    return usage(argv[0]);
  }
  opt.bytes = static_cast<size_t>(bytes);
  set_log_level(ERROR);

  if (opt.field == "gf2_128") {
    using F128 = GF2_128<>;
    const F128 f;
    const LCH14ReedSolomonFactory<F128> rsf(f);
    return run<F128, 2>("gf2_128", GF2_128_ID, f, rsf, opt);
  }
  if (opt.field == "fp64_2") {
    // Goldilocks quadratic extension, as in Longfellow's BM_ShaZK_Fp64_2.
    // The root 2752994695033296049 has order 2^29. Longfellow's
    // algebra/reed_solomon_test.cc uses it with order 2^29. BM_ShaZK_Fp64_2
    // passes 2^32 and never verifies; with 2^32 the honest proof is rejected.
    using Base = Fp<1>;
    using Field2 = Fp2<Base>;
    using Fft = FFTConvolutionFactory<Field2>;
    using RSFactory = ReedSolomonFactory<Field2, Fft>;
    static const Base base("18446744069414584321");
    static const Field2 f2(base);
    const typename Field2::Elt omega = f2.of_string("2752994695033296049");
    const Fft fft(f2, omega, uint64_t(1) << 29);
    const RSFactory rsf(fft, f2);
    return run<Field2, 3>("fp64_2", FP64_2_ID, f2, rsf, opt);
  }
  return usage(argv[0]);
}

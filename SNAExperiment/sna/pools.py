"""Measured wire-size pools (pools.json): TLS session record sizes, DNS query and response sizes,
and the TLS 1.3 record overhead measured by pushing padded ciphertexts through real sessions.
Background traffic draws its sizes from these pools."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from . import params as P

POOL_FILE = Path(__file__).with_name("pools.json")


class Pools:
    def __init__(self, path: Path = POOL_FILE):
        data = json.loads(Path(path).read_text())
        self.tls_sessions = [np.array(s["records"], dtype=np.int32).reshape(-1, 5) for s in data["tls"]]
        self.dns_query = np.array([d["query"] for d in data["dns"]], dtype=np.int32)
        self.dns_resp = np.array([d["response"] for d in data["dns"]], dtype=np.int32)
        ov = data["overhead"]
        wire = {int(k): int(v) for k, v in ov["birthmark"].items()}
        self.tls13_overhead = wire[P.PAD_MIN] - P.PAD_MIN      # one TLS 1.3 record per packet
        self.keepalive_wire = int(ov["keepalive"])
        self.bulk_record_wire = int(ov["bulk_record"])
        self.gossip_wire = P.RAW["Reg"] + P.GOSSIP_ENVELOPE + P.NOISE_FRAME

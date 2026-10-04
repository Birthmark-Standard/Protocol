"""Every numeric input to the simulator and the attacks. Sizes and procedures follow the Birthmark
Protocol per-leg message specification; hold timing follows its Hold timing table."""
from dataclasses import dataclass, replace

# --------------------------------------------------------------------------- hold timing
TICK_S = 10.0              # every hold releases on a node clock of 10-second ticks
CAP_FACTOR = 3.0           # every hold is capped at three times its own mean
BUNDLE_S = 30.0            # gatekeeper departure bundling: one boundary every 30 seconds
INCLUSION_P = 0.25         # chance a ready posting boards at each boundary
INCLUSION_MAX = 12         # it boards unconditionally at the 12th boundary
REG_BUNDLE_S = 120.0       # registry-level bundling: one schedule shared by every content server
BOARD_PUSH_S = 10.0        # each match board pushes new matches to every content server on this period
QUORUM_TIMEOUT_S = 30 * 60 # a content server drops a packet whose quorum has not formed in 30 minutes

# --------------------------------------------------------------------------- padding classes
PAD_MIN, PAD_MAX = 420, 460          # every transit leg except the gatekeeper fan-out
PAD_GK = (820, 860)                  # gatekeeper fan-out leg (GK-1..3)
TLS13_OVERHEAD = 22                  # bytes per TLS 1.3 record (AES-256-GCM), measured on real sessions

# raw payload sizes (bytes) from the specification's leg table, with one registered validator
RING_V_BYTES = 64                    # AOS ring signature over Ring V: 32 (n + 1) B, n = 1
RAW = {"Cred-1": 251, "Cred-2": 251, "Cred-3": 235, "Cont-1": 163, "Cont-2": 163, "Cont-3": 147,
       "CV-1": 218, "CV-2": 133, "CV-2 reject": 69, "GK": 689 + RING_V_BYTES, "Reg": 98}

# --------------------------------------------------------------------------- topology
N_NODES = 20               # submission-server pool
N_VALIDATORS = 1           # one registered validator
N_GATEKEEPERS = 3          # one active gatekeeper set per run
GOSSIP_MESH_D = 6          # gossipsub mesh degree; origin flood-publishes to every peer
GOSSIP_ENVELOPE = 168      # gossipsub RPC envelope around a registry submission
NOISE_FRAME = 18           # libp2p Noise transport framing
GOSSIP_WIRE = RAW["Reg"] + GOSSIP_ENVELOPE + NOISE_FRAME

# --------------------------------------------------------------------------- devices and volume
INTERVAL_MIN = 20.0        # mean interval between one device's captures (minutes); each decoy
                           #   identity captures at the same rate

# --------------------------------------------------------------------------- network timing
LAT_EXT_MS = (10.0, 120.0)   # one-way latency external host <-> node, fixed per pair per run
LAT_INT_MS = (5.0, 80.0)     # node <-> node and node <-> validator
JITTER_MS = 2.0              # per-packet exponential jitter, mean
PROC_MS = (0.5, 3.0)         # per-packet processing before a send
VALIDATOR_PROC_MS = (5.0, 50.0)
GATEKEEPER_PROC_MS = (1.0, 10.0)
GOSSIP_VALIDATE_MS = (5.0, 50.0)

# --------------------------------------------------------------------------- run window
WARMUP_S = 60.0 * 60       # transactions start at 0; scoring starts once traffic in flight is steady
MEASURE_S = 3 * 60 * 60    # scored window (extended at small real volume)
COOLDOWN_S = 120.0 * 60    # keeps simulating past the window so every scored transaction completes
MIN_REAL_PER_RUN = 200     # the scored window is extended until it holds this many real
                           #   transactions on average

# --------------------------------------------------------------------------- record types
RT_APPDATA = 0x17
RT_NOISE = 1


@dataclass(frozen=True)
class Config:
    """One simulated configuration. Rates are transactions per second; holds are mean seconds."""
    real_rate: float = 0.05            # real captures per second, all devices together
    decoy_rate: float = 0.0            # decoy transactions per second
    measure_s: float = MEASURE_S
    relay_mean: float = 120.0          # every relay hop (A, B, D, E, G, H), every path
    dev_cred_mean: float = 120.0       # the device's credential-channel hold
    dev_content_mean: float = 240.0    # the device's two content-channel holds
    c_hold_mean: float = 30.0          # C's hold before sending CV-1 (0 = none)
    v_hold_mean: float = 30.0          # V's hold before sending CV-2 (0 = none)
    fanout_mean: float = 60.0          # C's fan-out, each gatekeeper leg independently
    gk_mean: float = 30.0              # the gatekeeper's own hold
    gk_inclusion: bool = True          # departure bundling by inclusion lottery (False: next boundary)
    cs_mean: float = 240.0             # F's and I's pre-match hold
    post_match: bool = True            # F's and I's post-match lottery after quorum is confirmed
    pm_mean: float = 30.0              # post-match lottery mean
    reg_bundle_s: float = REG_BUNDLE_S # registry-level bundling period; 0 = off

    @property
    def warmup_s(self) -> float:
        return WARMUP_S

    @property
    def horizon_s(self) -> float:
        return self.warmup_s + self.measure_s + COOLDOWN_S

    @property
    def real_devices(self) -> int:
        return max(1, int(round(self.real_rate * INTERVAL_MIN * 60)))

    @property
    def decoy_sources(self) -> int:
        return max(1, int(round(self.decoy_rate * INTERVAL_MIN * 60))) if self.decoy_rate > 0 else 0

    def with_(self, **kw) -> "Config":
        return replace(self, **kw)

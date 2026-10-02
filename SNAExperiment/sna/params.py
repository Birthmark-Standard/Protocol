"""Every numeric input to the simulator and the attacks, each stated as a design choice of this
experiment. Sizes and procedures follow the per-leg message specification (see README.md)."""
from dataclasses import dataclass, replace

# --------------------------------------------------------------------------- lottery
TICK_S = 10.0              # relay timing lottery: 10-second ticks
RELEASE_P = 0.0833         # 8.33% release probability per tick
MAX_TICKS = 30             # forced release at tick 30 (5-minute cap)

# --------------------------------------------------------------------------- padding classes
PAD_MIN, PAD_MAX = 420, 460          # every transit leg except the gatekeeper fan-out
PAD_GK = (820, 860)                  # gatekeeper fan-out leg (GK-1..3)

# raw payload sizes (bytes) from the specification's leg table; N_VALIDATORS = 1
RING_V_BYTES = 64                    # AOS ring signature over Ring V: 32 (n + 1) B, n = 1
RAW = {"Cred-1": 251, "Cred-2": 251, "Cred-3": 235, "Cont-1": 163, "Cont-2": 163, "Cont-3": 147,
       "CV-1": 218, "CV-2": 133, "CV-2 reject": 69, "GK": 689 + RING_V_BYTES, "Reg": 98}
INDICATOR_BYTES = 1                  # plaintext real/dummy indicator carried in CV-2 (inside padding)

# --------------------------------------------------------------------------- topology
N_NODES = 20               # submission-server pool
N_VALIDATORS = 1           # one registered validator
N_GATEKEEPERS = 3          # one active gatekeeper set per run
GOSSIP_MESH_D = 6          # gossipsub mesh degree; origin flood-publishes to every peer
GOSSIP_ENVELOPE = 168      # gossipsub RPC envelope around a registry submission
NOISE_FRAME = 18           # libp2p Noise transport framing

# --------------------------------------------------------------------------- devices and volume
INTERVAL_MIN = 20.0        # mean interval between one device's captures
DECOYS_IN_FLIGHT = 40.0    # default decoy target (checks): decoy transactions in flight: a steady Poisson stream, independent of
                           #   real traffic; each decoy identity captures at a device's rate
BUNDLE_S = 30.0            # gatekeeper departure bundling window (when bundling is on)
GK_IMMEDIATE_P = 0.6       # two-point gatekeeper hold: release at once with this probability,
GK_CAP_S = 300.0           #   otherwise hold the full 5-minute cap (mean 120 s)
REG_BUNDLE_S = 120.0       # registry-level pooled bundling window (sized against the measured submission rate)
BOARD_PUSH_S = 10.0        # each match board pushes its new matches to every content server on this period
QUORUM_TIMEOUT_S = 30 * 60 # content server drops a packet whose quorum has not formed in 30 minutes

# --------------------------------------------------------------------------- background traffic
BG_CLIENTS_PER_NODE = 25
BG_CASUAL_FRACTION = 0.90
BG_CASUAL_PAUSE_S = (1.0, 60.0)
BG_HIFREQ_PAUSE_S = (0.0, 0.5)
BG_INTERNAL_FRACTION = 0.2
BG_DNS_FRACTION = 0.2
BULK_EXT_RATE_PER_NODE = 1 / 60.0
BULK_INT_RATE_PER_NODE = 1 / 120.0
BULK_MEDIAN_BYTES = 1_000_000
KEEPALIVE_PERIOD_S = 30.0

# --------------------------------------------------------------------------- network timing
LAT_EXT_MS = (10.0, 120.0)   # one-way latency external host <-> node, fixed per pair per run
LAT_INT_MS = (5.0, 80.0)     # node <-> node and node <-> validator
JITTER_MS = 2.0              # per-packet exponential jitter, mean
PROC_MS = (0.5, 3.0)         # per-packet processing before a send
VALIDATOR_PROC_MS = (5.0, 50.0)
GATEKEEPER_PROC_MS = (1.0, 10.0)
GOSSIP_VALIDATE_MS = (5.0, 50.0)

# --------------------------------------------------------------------------- run window
WARMUP_S = 20 * 60           # transactions start at 0; scoring starts after steady state
MEASURE_S = 3 * 60 * 60      # default scored window (extended at small real volume)
COOLDOWN_S = 40 * 60         # keeps simulating past the window so every scored chain completes
MIN_REAL_PER_RUN = 200       # the scored window is extended until it holds this many real
                             #   transactions on average

# --------------------------------------------------------------------------- record types
RT_HANDSHAKE = 0x16
RT_APPDATA = 0x17
RT_DNS = 53
RT_NOISE = 1


@dataclass(frozen=True)
class Config:
    """One simulated configuration. Rates are transactions per second."""
    real_rate: float = 0.05            # real captures per second, all devices together
    decoy_rate: float = 0.0            # decoy credential transactions per second (2 decoy content
                                       #   packets accompany each)
    measure_s: float = MEASURE_S
    lottery_enabled: bool = True       # False: no relay, device, gatekeeper or content-server hold
    bundle_s: float = 0.0              # gatekeeper departure bundling window; 0 = off
    gk_twopoint: bool = False          # gatekeeper hold: two-point shape instead of the relay lottery
    reg_bundle_s: float = 0.0          # registry-level pooled bundling window; 0 = off
    cred_hold_scale: float = 1.0       # device and relay-hop holds on the credential path: mean and cap x this
    content_hold_scale: float = 1.0    # device and relay-hop holds on both content paths: mean and cap x this
    content_device_scale: float = 1.0  # the device's hold on its two content channels only: mean and cap x this
    cs_hold_scale: float = 1.0         # the content servers' own pre-match node-clock hold: mean and cap x this
    post_match: bool = False           # content servers' post-match lottery after quorum is confirmed
    background_enabled: bool = True
    nonblending_enabled: bool = True
    bg_clients_per_node: int = BG_CLIENTS_PER_NODE

    @property
    def hold_scale_max(self) -> float:
        return max(1.0, self.cred_hold_scale, self.content_hold_scale,
                   self.content_hold_scale * self.content_device_scale, self.cs_hold_scale)

    @property
    def warmup_s(self) -> float:
        """Warm-up before the scored window; lengthened with the relay holds so traffic in flight
        reaches steady state first (unchanged at scale 1)."""
        return WARMUP_S * self.hold_scale_max

    @property
    def horizon_s(self) -> float:
        return self.warmup_s + self.measure_s + COOLDOWN_S * self.hold_scale_max

    @property
    def real_devices(self) -> int:
        return max(1, int(round(self.real_rate * INTERVAL_MIN * 60)))

    @property
    def decoy_sources(self) -> int:
        return max(1, int(round(self.decoy_rate * INTERVAL_MIN * 60))) if self.decoy_rate > 0 else 0

    def with_(self, **kw) -> "Config":
        return replace(self, **kw)

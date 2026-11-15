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
REG_POST_S = 120.0         # the registry posts merged records on its own schedule with this period
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
PROC_MS = (0.5, 3.0)         # per-packet processing before a send (uniform, every node)
VALIDATOR_PROC_MS = (5.0, 50.0)
GATEKEEPER_PROC_MS = (1.0, 10.0)
GOSSIP_VALIDATE_MS = (5.0, 50.0)

# --------------------------------------------------------------------------- run window
MEASURE_S = 3 * 60 * 60    # scored window (extended at small real volume)
MIN_REAL_PER_RUN = 200     # the scored window is extended until it holds this many real
                           #   transactions on average

# --------------------------------------------------------------------------- C3 to C5 options
W_SIGMA = 0.90             # W1: lognormal spread of identity rate factors (10th to 90th percentile: a factor of 10)
SESSION_SHARE = 0.20       # W2: share of identities with sessions
SESSION_PER_S = 1 / (12 * 3600)   # W2: sessions start at 1 per 12 hours
SESSION_MIN = (10.0, 60.0) # W2: session length, uniform (minutes)
SESSION_MULT = 10.0        # W2: rate multiple during a session
EDIT_EXTRA_MEAN = 0.5      # edit chains: edits per edited capture are 1 + Poisson(0.5)
EDIT_MAX = 4               #   at most 4
EDIT_DELAY_MIN_S = 300.0   # an edit's capture follows its parent's posting by 5 minutes
EDIT_DELAY_MEAN_S = 1800.0 #   plus an exponential with mean 30 minutes
MACHINE_OFFSET = 200_000   # source address of a user's machine: the device's address plus this
RESUB_WAIT_S = 2400.0      # a device that sees no record by this long after capture resubmits
WITHHOLD_GAP_S = 7200.0    # validator withholding: time between one window's end and the next one's start

# --------------------------------------------------------------------------- record types
RT_APPDATA = 0x17
RT_NOISE = 1


@dataclass(frozen=True)
class Config:
    """One simulated configuration. Rates are transactions per second; holds are mean seconds."""
    real_rate: float = 0.05            # real captures per second, all devices together
    decoy_rate: float = 0.0            # decoy transactions per second
    measure_s: float = MEASURE_S
    relay1_mean: float = 60.0          # every first relay hop (A, D, G); a relay knows only its hop position
    relay2_mean: float = 300.0         # every second relay hop (B, E, H)
    dev_cred_mean: float = 120.0       # the device's credential-channel hold
    dev_content_mean: float = 240.0    # the device's two content-channel holds
    dev_content_i_mean: float = -1.0   # the device's I-channel hold when set (>= 0); default: the same as dev_content_mean
    c_hold_mean: float = 30.0          # C's hold before sending CV-1 (0 = none)
    v_hold_mean: float = 30.0          # V's hold before sending CV-2 (0 = none)
    fanout_mean: float = 20.0          # C's serialized fan-out: mean of each draw; one leg leaves per success
    gk_mean: float = 30.0              # the gatekeeper's own hold
    gk_inclusion: bool = True          # departure bundling by inclusion lottery (False: next boundary)
    cs_mean: float = 120.0             # F's and I's pre-match hold
    post_match: bool = True            # F's and I's post-match lottery after quorum is confirmed
    pm_mean: float = 30.0              # post-match lottery mean
    reg_bundle_s: float = REG_BUNDLE_S # registry-level bundling period; 0 = off
    reg_post_s: float = REG_POST_S     # the registry's posting schedule period; 0 = posted at intake
    overlap: bool = True               # relays drawn under the routing design's guarantees only (see sim._roles)
    warmup_len: float = -1.0           # warm-up before the scored window (s); below 0: the longest possible delay
    cooldown_len: float = -1.0         # cool-down after the window (s), with arrivals going on; below 0: as above
    # options added for C3 to C5; every default is C2's behavior
    decoy_factor: float = 1.0          # decoy concentration: fewer decoy identities, each at this multiple of a device's rate
    workload: str = "W0"               # W0 one rate; W1 lognormal rates; W2 W1 with sessions; Wmis real devices W2, decoys W0
    edit_share: float = 0.0            # share of captures that are edited (edit chains); 0 = no edits
    edit_same_source: float = 1.0      # share of edits sent from the capture's own source address
    quorum_timeout_s: float = QUORUM_TIMEOUT_S
    board_window_s: float = 0.0        # a match board keeps postings this long; 0 = as C2, no limit
    grid_off: bool = False             # no departure grid and no push schedule: postings leave when ready, quorum known at once
    mark_actor: str = ""               # first_relay, access, access_one or validator; "" = no active attack
    mark_mode: str = "delay"           # delay: hold the target's packets Δ longer; drop: drop one and the device resubmits
    mark_delta: float = 0.0            # Δ (s)
    mark_target: int = -1              # the target's real device index; -1 = none; -2 = every real device (the attacker's models)
    resub_mean_s: float = 1800.0       # mean of the exponential resubmission delay after RESUB_WAIT_S
    withhold_share: float = 0.0        # validator withholding: share of identities the withholding validator serves
    withhold_len: float = 0.0          # window length (s); one window every withhold_len + WITHHOLD_GAP_S from the warm-up's end
    withhold_mode: str = "withhold"    # withhold: no reply; delay: the reply leaves at the window's end
    n_validators: int = 1              # validators, each with its own Token Key
    real_val_split: tuple = ()         # share of real devices registered with each validator (empty: all with the first)
    decoy_val_split: tuple = ()        # share of decoy identities registered with each validator

    @property
    def max_delay_s(self) -> float:
        """An upper bound on capture to posting: every hold at its cap, every schedule at its longest wait."""
        cap = lambda m: CAP_FACTOR * m  # noqa: E731
        dev_i = self.dev_content_mean if self.dev_content_i_mean < 0 else self.dev_content_i_mean
        relays = cap(self.relay1_mean) + cap(self.relay2_mean)
        cred = (cap(self.dev_cred_mean) + relays + cap(self.c_hold_mean) + cap(self.v_hold_mean) + 3 * cap(self.fanout_mean)
                + cap(self.gk_mean) + BUNDLE_S * (INCLUSION_MAX if self.gk_inclusion else 1) + BOARD_PUSH_S)
        content = cap(max(self.dev_content_mean, dev_i)) + relays + cap(self.cs_mean)
        return max(cred, content) + (cap(self.pm_mean) if self.post_match else 0.0) + self.reg_bundle_s + self.reg_post_s + 60.0

    @property
    def warmup_s(self) -> float:
        """Scoring starts once traffic in flight is steady."""
        return self.warmup_len if self.warmup_len >= 0 else self.max_delay_s

    @property
    def horizon_s(self) -> float:
        """Transactions keep arriving through the cool-down: their packets are candidates for the window's late records."""
        return self.warmup_s + self.measure_s + (self.cooldown_len if self.cooldown_len >= 0 else self.max_delay_s)

    @property
    def real_devices(self) -> int:
        return max(1, int(round(self.real_rate * INTERVAL_MIN * 60)))

    @property
    def decoy_sources(self) -> int:
        """Decoy identities, each capturing at the real devices' rate per device, so no identity's rate stands out."""
        if self.decoy_rate <= 0:
            return 0
        per_device = self.real_rate / self.real_devices if self.real_rate > 0 else 1.0 / (INTERVAL_MIN * 60)
        return max(1, int(round(self.decoy_rate / per_device / self.decoy_factor)))

    @property
    def edits_per_capture(self) -> float:
        """Mean transactions an edited or unedited capture adds as edits."""
        if self.edit_share <= 0:
            return 0.0
        import math
        lam, m = EDIT_EXTRA_MEAN, EDIT_MAX - 1
        mean_extra = sum(min(k, m) * math.exp(-lam) * lam ** k / math.factorial(k) for k in range(40))
        return self.edit_share * (1.0 + mean_extra)

    def hash_dict(self) -> dict:
        """The fields for a configuration hash: the C3 to C5 options only when they differ from their defaults,
        so a C2 configuration hashes as it did."""
        d = dict(self.__dict__)
        for f in NEW_FIELDS:
            if d[f] == getattr(Config, f):
                del d[f]
        return d

    def with_(self, **kw) -> "Config":
        return replace(self, **kw)


NEW_FIELDS = ("decoy_factor", "workload", "edit_share", "edit_same_source", "quorum_timeout_s", "board_window_s", "grid_off",
              "mark_actor", "mark_mode", "mark_delta", "mark_target", "resub_mean_s", "withhold_share", "withhold_len",
              "withhold_mode", "n_validators", "real_val_split", "decoy_val_split")

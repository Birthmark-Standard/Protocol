"""Protocol currency: the simulator's legs against Docs/Birthmark_Protocol_Per-Leg_Message_Specification.md.

The spec moved BK generation to C and dropped EncPH from CV-2 and the GK legs, so raw sizes
changed. Every padded leg must still fit its padding class, which keeps wire-visible sizes (and so
every result) unchanged. Run from GPAExperiment:   python -m pytest -q tests
"""
import numpy as np
import pytest

from birthmark_l3 import crypto_legs as X
from birthmark_l3 import fastsim as F
from birthmark_l3 import params as P
from birthmark_l3.wire_pools import Pools

PADDED = ["Cred-1", "Cred-2", "Cred-3", "ContA-1", "ContA-2", "ContA-3", "CV-1", "CV-2", "CV-2 reject", "GK"]


@pytest.fixture(scope="module")
def spec_sizes():
    return X.measure_spec_raw_sizes()


def test_spec_construction_reproduces_the_spec_table(spec_sizes):
    """Built with real crypto exactly as the spec describes. The content legs are the one mismatch:
    the spec's P_F includes the 1-byte mod_level, but its 162/146 B figures match P_F without it."""
    no_mod = X.measure_spec_raw_sizes(mod_level_in_p_f=False)
    for leg, size in X.SPEC_RAW_SIZES.items():
        if leg.startswith("ContA"):
            assert no_mod[leg] == size and spec_sizes[leg] == size + X.MOD_LEVEL_LEN, leg
        else:
            assert spec_sizes[leg] == size, leg
    assert spec_sizes["Reg"] == 97          # the registry posting does count mod_level


def test_every_spec_leg_fits_its_padding_class(spec_sizes):
    for leg in PADDED:
        lo, hi = P.PAD_GK_RING if leg == "GK" else (P.PAD_MIN, P.PAD_MAX)
        inner = spec_sizes[leg] - X.ECIES_OVERHEAD
        for target in (lo, hi):             # padding sits inside the transit layer
            assert len(X.pad_to(b"\x00" * inner, target - X.ECIES_OVERHEAD)) + X.ECIES_OVERHEAD == target, leg


def test_wire_trace_unchanged_under_spec_raw_sizes(spec_sizes, monkeypatch):
    """Padded sizes are drawn from the class alone, so the whole observed trace is identical."""
    pools = Pools()
    runs = {}
    for name, raw, ring_raw in (("sim", X.measure_raw_sizes(), X.ring_gk_raw_size()), ("spec", spec_sizes, spec_sizes["GK"])):
        monkeypatch.setattr(F, "_RAW", raw)
        monkeypatch.setattr(F, "ring_gk_raw_size", lambda r=ring_raw: r)
        for rules, ring in (("distinct", False), ("insider_v2", True)):
            cfg = P.Config(devices=40, interval_min=20, role_rules=rules, ring_sig=ring)
            runs[(name, rules)] = F.simulate(cfg, 7, pools).events
    for rules in ("distinct", "insider_v2"):
        a, b = runs[("sim", rules)], runs[("spec", rules)]
        for k in ("t_send", "t_arr", "src", "dst", "size", "rtype"):
            assert np.array_equal(a[k], b[k]), (rules, k)


def test_no_crypto_tables_equal_the_measurement():
    """--no-crypto (BIRTHMARK_NO_CRYPTO) uses stored raw sizes; they must equal a fresh real-crypto build."""
    assert X.measure_raw_sizes() == F.MEASURED_RAW
    assert X.ring_gk_raw_size() == F.MEASURED_RING_GK

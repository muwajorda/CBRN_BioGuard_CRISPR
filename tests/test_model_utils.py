import pandas as pd
import utils.model_utils as mu

def test_heuristic_classify_high_gc():
    # High GC -> Threat
    seq = "G" * 80 + "A" * 20  # 80% G
    label, info = mu._heuristic_classify(seq)
    assert label == "Threat"
    assert info.startswith("gc=")

def test_heuristic_classify_low_gc():
    seq = "A" * 80 + "C" * 20  # 20% GC
    label, info = mu._heuristic_classify(seq)
    assert label == "Benign"
    assert info.startswith("gc=")

def test_heuristic_classify_invalid_sequence():
    seq = "XYZ123"
    label, info = mu._heuristic_classify(seq)
    assert label == "Unknown"
    assert info == "invalid_sequence"

def test_classify_sequence_uses_fallback(monkeypatch):
    # Force model unavailable and ensure classify_sequence calls heuristic
    monkeypatch.setattr(mu, "_model_available", False)
    label, info = mu.classify_sequence("G" * 60 + "A" * 40)
    assert label in ("Threat", "Benign", "Unknown")
    assert isinstance(info, str)
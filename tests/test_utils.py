"""Tests for utils module."""

import pytest
from pathlib import Path
import json
from lost_in_middle_tester.utils import count_tokens, estimate_cost, save_results_json


def test_count_tokens():
    """Test token counting."""
    text = "Hello world, this is a test."
    tokens = count_tokens(text)

    assert tokens > 0
    assert isinstance(tokens, int)


def test_estimate_cost():
    """Test cost estimation."""
    # Test GPT-4
    cost = estimate_cost("gpt-4", 100, 8000)
    assert cost > 0
    assert isinstance(cost, float)

    # Test GPT-3.5
    cost_35 = estimate_cost("gpt-3.5-turbo", 100, 8000)
    assert cost_35 < cost  # GPT-3.5 should be cheaper

    # Test unknown model (should use default)
    cost_unknown = estimate_cost("unknown-model", 100, 8000)
    assert cost_unknown > 0


def test_save_results_json(tmp_path):
    """Test JSON result saving."""
    results = {
        0.0: {
            "success_rate": 0.95,
            "success_count": 19,
            "total_count": 20
        },
        0.5: {
            "success_rate": 0.40,
            "success_count": 8,
            "total_count": 20
        }
    }

    output_path = tmp_path / "results.json"
    save_results_json(results, output_path)

    assert output_path.exists()

    with open(output_path, 'r', encoding='utf-8') as f:
        loaded = json.load(f)

    assert "0.0" in loaded or 0.0 in loaded
    assert "0.5" in loaded or 0.5 in loaded

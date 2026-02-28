"""Tests for core module."""

import pytest
from lost_in_middle_tester.core import (
    TextGenerator,
    PasswordInserter,
    ModelTester,
    ResultCollector
)


class MockClient:
    """Mock API client for testing."""

    def __init__(self, should_find: bool = True):
        self.should_find = should_find

    def query(self, prompt: str) -> str:
        if self.should_find:
            # Extract password from prompt
            lines = prompt.split('\n')
            for line in lines:
                if 'SECRET_CODE_' in line:
                    return line
        return "I couldn't find any code."


def test_text_generator():
    """Test text generation."""
    gen = TextGenerator()
    paragraphs = gen.generate(1000)

    assert len(paragraphs) > 0
    assert all(isinstance(p, str) for p in paragraphs)


def test_password_inserter():
    """Test password insertion."""
    paragraphs = ["Para 1", "Para 2", "Para 3", "Para 4", "Para 5"]

    # Test insertion at beginning
    modified, password, idx = PasswordInserter.insert(paragraphs, 0.0)
    assert password.startswith("SECRET_CODE_")
    assert len(password) == 16  # SECRET_CODE_ + 4 chars
    assert idx == 0
    assert password in modified[0]

    # Test insertion at end
    modified, password, idx = PasswordInserter.insert(paragraphs, 1.0)
    assert idx == len(paragraphs) - 1
    assert password in modified[-1]

    # Test insertion in middle
    modified, password, idx = PasswordInserter.insert(paragraphs, 0.5)
    assert 0 <= idx < len(paragraphs)
    assert password in modified[idx]


def test_model_tester_success():
    """Test model tester with successful response."""
    tester = ModelTester()
    client = MockClient(should_find=True)

    paragraphs = ["Para 1", "The code is SECRET_CODE_TEST.", "Para 3"]
    result = tester.test(paragraphs, "SECRET_CODE_TEST", client)

    assert result is True


def test_model_tester_failure():
    """Test model tester with failed response."""
    tester = ModelTester()
    client = MockClient(should_find=False)

    paragraphs = ["Para 1", "The code is SECRET_CODE_TEST.", "Para 3"]
    result = tester.test(paragraphs, "SECRET_CODE_TEST", client)

    assert result is False


def test_result_collector():
    """Test result collection and statistics."""
    collector = ResultCollector()

    # Add results for position 0.0
    collector.add_result(0.0, True)
    collector.add_result(0.0, True)
    collector.add_result(0.0, False)

    # Add results for position 0.5
    collector.add_result(0.5, True)
    collector.add_result(0.5, False)

    stats = collector.get_statistics()

    assert 0.0 in stats
    assert 0.5 in stats

    assert stats[0.0]["success_count"] == 2
    assert stats[0.0]["total_count"] == 3
    assert stats[0.0]["success_rate"] == pytest.approx(2/3)

    assert stats[0.5]["success_count"] == 1
    assert stats[0.5]["total_count"] == 2
    assert stats[0.5]["success_rate"] == 0.5

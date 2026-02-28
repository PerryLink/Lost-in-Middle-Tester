"""Core testing logic for Lost-in-the-Middle phenomenon."""

import random
import string
from dataclasses import dataclass
from typing import List, Tuple
from tenacity import retry, stop_after_attempt, wait_exponential


@dataclass
class TestResult:
    """Result of a single test."""
    position: float
    password: str
    found: bool
    response: str


class TextGenerator:
    """Generate long text content."""

    PARAGRAPHS = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "The theory of relativity fundamentally changed our understanding of space and time. Einstein's groundbreaking work showed that these concepts are intertwined.",
        "Ancient civilizations developed sophisticated mathematical systems. The Babylonians used a base-60 system that influences our time measurement today.",
        "Climate patterns are influenced by ocean currents, atmospheric pressure, and solar radiation. These factors interact in complex ways.",
        "The human brain contains approximately 86 billion neurons. Each neuron can form thousands of connections with other neurons.",
        "Photosynthesis converts light energy into chemical energy. This process is fundamental to life on Earth.",
        "The Renaissance period saw remarkable advances in art, science, and philosophy. It marked a transition from medieval to modern thinking.",
        "Quantum mechanics describes the behavior of matter at atomic scales. It reveals a probabilistic nature of reality.",
        "The Great Wall of China stretches over 13,000 miles. It was built over many centuries by different dynasties.",
        "DNA carries genetic information in all living organisms. Its double helix structure was discovered in 1953.",
    ]

    def generate(self, target_tokens: int) -> List[str]:
        """Generate paragraphs totaling approximately target_tokens."""
        paragraphs = []
        current_tokens = 0

        while current_tokens < target_tokens:
            para = random.choice(self.PARAGRAPHS)
            paragraphs.append(para)
            current_tokens += len(para.split()) * 1.3

        return paragraphs


class PasswordInserter:
    """Insert password at specified position."""

    @staticmethod
    def generate_password() -> str:
        """Generate a random password."""
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f"SECRET_CODE_{suffix}"

    @staticmethod
    def insert(paragraphs: List[str], position: float) -> Tuple[List[str], str, int]:
        """Insert password at position (0.0 to 1.0)."""
        password = PasswordInserter.generate_password()
        insert_idx = int(len(paragraphs) * position)
        insert_idx = max(0, min(insert_idx, len(paragraphs) - 1))

        password_sentence = f"The verification code is {password}."
        modified = paragraphs.copy()
        modified[insert_idx] = modified[insert_idx] + " " + password_sentence

        return modified, password, insert_idx


class ModelTester:
    """Execute model tests."""

    PROMPT_TEMPLATE = """Below is a long document. Please read it carefully and find the verification code mentioned in the text. The code follows the format "SECRET_CODE_XXXX".

Document:
{document}

Question: What is the verification code mentioned in the document? Please respond with ONLY the code itself, nothing else."""

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def test(self, paragraphs: List[str], password: str, client) -> bool:
        """Test if model can find the password."""
        document = "\n\n".join(paragraphs)
        prompt = self.PROMPT_TEMPLATE.format(document=document)

        response = client.query(prompt)
        return password.upper() in response.upper()


class ResultCollector:
    """Collect and aggregate test results."""

    def __init__(self):
        self.results = {}

    def add_result(self, position: float, success: bool):
        """Add a test result."""
        if position not in self.results:
            self.results[position] = {"total": 0, "success": 0}

        self.results[position]["total"] += 1
        if success:
            self.results[position]["success"] += 1

    def get_statistics(self) -> dict:
        """Calculate statistics for each position."""
        stats = {}
        for pos, data in self.results.items():
            stats[pos] = {
                "success_rate": data["success"] / data["total"],
                "success_count": data["success"],
                "total_count": data["total"]
            }
        return stats

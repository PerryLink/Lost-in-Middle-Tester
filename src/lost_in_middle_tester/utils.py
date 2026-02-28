"""Utility functions for API clients and visualization."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional
import json
import matplotlib.pyplot as plt
import tiktoken


class BaseModelClient(ABC):
    """Base class for LLM API clients."""

    @abstractmethod
    def query(self, prompt: str) -> str:
        """Send a query to the model and return the response."""
        pass


class OpenAIClient(BaseModelClient):
    """OpenAI API client."""

    def __init__(self, api_key: str, model: str = "gpt-4"):
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def query(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content


class AnthropicClient(BaseModelClient):
    """Anthropic API client."""

    def __init__(self, api_key: str, model: str = "claude-3-opus-20240229"):
        from anthropic import Anthropic
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def query(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Estimate token count using tiktoken."""
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except:
        return len(text) // 4


def generate_u_curve(results: dict, output_path: Path, model_name: str):
    """Generate U-curve visualization."""
    positions = sorted(results.keys())
    success_rates = [results[pos]["success_rate"] * 100 for pos in positions]

    plt.figure(figsize=(10, 6))
    plt.plot(positions, success_rates, marker='o', linewidth=2, markersize=8)
    plt.xlabel('密码位置 (%)', fontsize=12)
    plt.ylabel('成功率 (%)', fontsize=12)
    plt.title(f'Lost-in-the-Middle 现象 - {model_name}', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 105)

    min_idx = success_rates.index(min(success_rates))
    plt.annotate(f'最低点: {success_rates[min_idx]:.1f}%',
                xy=(positions[min_idx], success_rates[min_idx]),
                xytext=(positions[min_idx], success_rates[min_idx] - 15),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=10, color='red')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def save_results_json(results: dict, output_path: Path):
    """Save detailed results to JSON."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def estimate_cost(model: str, num_tests: int, text_length: int) -> float:
    """Estimate API cost."""
    cost_per_1k = {
        "gpt-4": 0.03,
        "gpt-3.5-turbo": 0.002,
        "claude-3-opus-20240229": 0.015,
        "claude-3-sonnet-20240229": 0.003
    }

    base_cost = cost_per_1k.get(model, 0.01)
    total_tokens = (text_length + 100) * num_tests / 1000
    return total_tokens * base_cost

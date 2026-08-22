<div align="center">

# Lost-in-Middle-Tester
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/lost-in-middle-tester)

**A CLI tool that tests and visualizes the "Lost-in-the-Middle" phenomenon in large language models.**

*Ported into [dsh-library](https://github.com/PerryLink/dsh-library) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

Large language models tend to recall information at the start and end of a long context better than information in the middle — a known limitation described in [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172). Lost-in-Middle-Tester measures this effect: it builds a long document, inserts a secret `SECRET_CODE_XXXX` code at a chosen position, asks a model to recover it, and records the success rate at each position.

## Features

- Generates long-text test cases with an embedded verification code
- Supports OpenAI and Anthropic providers
- Outputs a U-curve chart (PNG) and a JSON report of per-position success rates
- Detailed per-position statistics and success/failure counts
- Cost estimation with a `--dry-run` preview
- Rich terminal progress bars and result tables

## Quick start

Requires Python 3.9+ and [Poetry](https://python-poetry.org/).

```bash
git clone https://github.com/PerryLink/Lost-in-Middle-Tester.git
cd Lost-in-Middle-Tester
poetry install
```

Set an API key and run a test:

```bash
# OpenAI
export OPENAI_API_KEY=sk-xxx
poetry run lost-in-middle-tester test --model gpt-4

# Anthropic
export ANTHROPIC_API_KEY=sk-ant-xxx
poetry run lost-in-middle-tester test --provider anthropic --model claude-3-opus-20240229
```

## Usage

```bash
# Custom test parameters
poetry run lost-in-middle-tester test \
  --model gpt-4 \
  --text-length 10000 \
  --num-tests 30 \
  --num-positions 15 \
  --output-dir ./my-results

# Preview configuration and estimated cost without calling the API
poetry run lost-in-middle-tester test --model gpt-4 --dry-run
```

| Option | Default | Description |
|--------|---------|-------------|
| `--api-key` | env var | API key (falls back to `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`) |
| `--model` | `gpt-4` | Model name |
| `--provider` | `openai` | API provider (`openai` / `anthropic`) |
| `--text-length` | `8000` | Document length in tokens |
| `--num-tests` | `20` | Tests per position |
| `--num-positions` | `10` | Number of test positions |
| `--output-dir` | `./results` | Output directory |
| `--show-plot` | `True` | Whether to render the chart |
| `--dry-run` | `False` | Preview configuration and cost |

## How it works

1. **Text generation** — builds roughly `--text-length` tokens of long text mixing Lorem Ipsum and knowledge paragraphs
2. **Code insertion** — inserts a random `SECRET_CODE_XXXX` code at a chosen position (0.0–1.0)
3. **Model testing** — asks the model to find the verification code in the document
4. **Statistics** — records the success rate at each position
5. **Visualization** — renders a U-curve chart and writes a JSON report

Built with Typer + Rich, the OpenAI and Anthropic SDKs, and Matplotlib. Tests use pytest; Black and Ruff format the code.

## Development

```bash
poetry run pytest -v
poetry run black src/
poetry run ruff check src/
```

## Related

- [dsh-library](https://github.com/PerryLink/dsh-library) — the DSH plugin this tool was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH Plugin Family

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink

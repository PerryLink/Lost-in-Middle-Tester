# Lost-in-Middle-Tester

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A CLI tool to test and visualize the "Lost-in-the-Middle" phenomenon in Large Language Models.

一个用于测试和可视化大语言模型"Lost-in-the-Middle"现象的命令行工具。

---

## English

### What is the Lost-in-the-Middle Phenomenon?

Large Language Models exhibit a known limitation when processing long contexts: they tend to overlook or forget information positioned in the middle of the text, while maintaining better recall of information at the beginning and end. This phenomenon is known as "Lost-in-the-Middle."

This tool systematically tests and quantifies this phenomenon, generating U-curve visualizations to demonstrate the effect.

### Features

- 🔍 Automatically generates long-text test cases with embedded "passwords"
- 🤖 Supports OpenAI and Anthropic APIs
- 📊 Generates U-curve visualization charts
- 📈 Detailed statistics and JSON reports
- 🎨 Beautiful terminal output (powered by Rich)
- 💰 Cost estimation and dry-run mode

### Quick Start

#### Installation with Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/PerryLink/lost-in-middle-tester.git
cd lost-in-middle-tester

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

#### Installation with pip

```bash
pip install lost-in-middle-tester
```

### Usage Guide

#### Basic Usage

```bash
# Using OpenAI API
lost-in-middle-tester --api-key sk-xxx --model gpt-4

# Using Anthropic API
lost-in-middle-tester --api-key sk-ant-xxx --provider anthropic --model claude-3-opus-20240229

# Read API key from environment variable
export OPENAI_API_KEY=sk-xxx
lost-in-middle-tester --model gpt-4
```

#### Advanced Options

```bash
# Custom test parameters
lost-in-middle-tester \
  --api-key sk-xxx \
  --model gpt-4 \
  --text-length 10000 \
  --num-tests 30 \
  --num-positions 15 \
  --output-dir ./my-results

# Dry-run mode (preview configuration and cost)
lost-in-middle-tester --api-key sk-xxx --model gpt-4 --dry-run
```

#### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--api-key` | Environment variable | API key |
| `--model` | gpt-4 | Model name |
| `--provider` | openai | API provider (openai/anthropic) |
| `--text-length` | 8000 | Text length (tokens) |
| `--num-tests` | 20 | Number of tests per position |
| `--num-positions` | 10 | Number of test positions |
| `--output-dir` | ./results | Output directory |
| `--show-plot` | True | Whether to display chart |
| `--dry-run` | False | Preview configuration and cost |

### Project Structure

```
lost-in-middle-tester/
├── src/lost_in_middle_tester/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point
│   ├── cli.py               # CLI interface (Typer)
│   ├── core.py              # Core testing logic
│   └── utils.py             # Utility functions
├── tests/                   # Unit tests
│   ├── test_core.py
│   └── test_utils.py
├── .github/workflows/       # CI/CD
├── README.md
├── LICENSE
└── pyproject.toml
```

### Tech Stack

- **CLI Framework**: Typer + Rich
- **API Clients**: OpenAI SDK, Anthropic SDK
- **Visualization**: Matplotlib
- **Testing**: Pytest
- **Code Quality**: Black, Ruff
- **Package Management**: Poetry

### How It Works

1. **Text Generation**: Generates ~8000 tokens of long text (mixed Lorem Ipsum and knowledge paragraphs)
2. **Password Insertion**: Inserts random passwords in format `SECRET_CODE_XXXX` at different positions
3. **Model Testing**: Calls AI model API to find the password in the text
4. **Statistics**: Records success rate at each position
5. **Visualization**: Generates U-curve chart and JSON report

### Development

#### Run Tests

```bash
poetry run pytest -v
```

#### Code Formatting

```bash
poetry run black src/
poetry run ruff check src/
```

### License

Apache License 2.0 - See [LICENSE](LICENSE) file for details.

Copyright 2026 Chance Dean <novelnexusai@outlook.com>

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

### References

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic API Documentation](https://docs.anthropic.com)

---

## 中文

### 什么是 Lost-in-the-Middle 现象？

大语言模型在处理长文本时存在一个已知缺陷：当关键信息位于文本中间位置时，模型往往会忽略或遗忘这些信息，而对开头和结尾的信息记忆较好。这种现象被称为"Lost-in-the-Middle"现象。

本工具通过系统化测试来量化这一现象，生成 U 型曲线可视化图表。

### 功能特性

- 🔍 自动生成包含"密码"的长文本测试用例
- 🤖 支持 OpenAI 和 Anthropic API
- 📊 生成 U 型曲线可视化图表
- 📈 详细的统计数据和 JSON 报告
- 🎨 美观的终端输出（使用 Rich）
- 💰 成本估算和 dry-run 模式

### 快速开始

#### 使用 Poetry 安装（推荐）

```bash
# 克隆仓库
git clone https://github.com/PerryLink/lost-in-middle-tester.git
cd lost-in-middle-tester

# 安装依赖
poetry install

# 激活虚拟环境
poetry shell
```

#### 使用 pip 安装

```bash
pip install lost-in-middle-tester
```

### 使用指南

#### 基本用法

```bash
# 使用 OpenAI API
lost-in-middle-tester --api-key sk-xxx --model gpt-4

# 使用 Anthropic API
lost-in-middle-tester --api-key sk-ant-xxx --provider anthropic --model claude-3-opus-20240229

# 从环境变量读取 API 密钥
export OPENAI_API_KEY=sk-xxx
lost-in-middle-tester --model gpt-4
```

#### 高级选项

```bash
# 自定义测试参数
lost-in-middle-tester \
  --api-key sk-xxx \
  --model gpt-4 \
  --text-length 10000 \
  --num-tests 30 \
  --num-positions 15 \
  --output-dir ./my-results

# Dry-run 模式（预览配置和成本）
lost-in-middle-tester --api-key sk-xxx --model gpt-4 --dry-run
```

#### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--api-key` | 环境变量 | API 密钥 |
| `--model` | gpt-4 | 模型名称 |
| `--provider` | openai | API 提供商 (openai/anthropic) |
| `--text-length` | 8000 | 文本长度（tokens） |
| `--num-tests` | 20 | 每个位置的测试次数 |
| `--num-positions` | 10 | 测试位置数量 |
| `--output-dir` | ./results | 结果输出目录 |
| `--show-plot` | True | 是否显示图表 |
| `--dry-run` | False | 预览配置和成本估算 |

### 项目结构

```
lost-in-middle-tester/
├── src/lost_in_middle_tester/
│   ├── __init__.py          # 包初始化
│   ├── __main__.py          # 入口点
│   ├── cli.py               # CLI 接口 (Typer)
│   ├── core.py              # 核心测试逻辑
│   └── utils.py             # 工具函数
├── tests/                   # 单元测试
│   ├── test_core.py
│   └── test_utils.py
├── .github/workflows/       # CI/CD
├── README.md
├── LICENSE
└── pyproject.toml
```

### 技术栈

- **CLI 框架**: Typer + Rich
- **API 客户端**: OpenAI SDK, Anthropic SDK
- **可视化**: Matplotlib
- **测试**: Pytest
- **代码质量**: Black, Ruff
- **包管理**: Poetry

### 工作原理

1. **文本生成**：生成约 8000 tokens 的长文本（混合 Lorem Ipsum 和知识段落）
2. **密码插入**：在不同位置插入格式为 `SECRET_CODE_XXXX` 的随机密码
3. **模型测试**：调用 AI 模型 API，要求找出文本中的密码
4. **结果统计**：记录每个位置的成功率
5. **可视化**：生成 U 型曲线图和 JSON 报告

### 开发

#### 运行测试

```bash
poetry run pytest -v
```

#### 代码格式化

```bash
poetry run black src/
poetry run ruff check src/
```

### 许可证

Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件

版权所有 2026 Chance Dean <novelnexusai@outlook.com>

### 贡献

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

### 参考资料

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [OpenAI API 文档](https://platform.openai.com/docs)
- [Anthropic API 文档](https://docs.anthropic.com)

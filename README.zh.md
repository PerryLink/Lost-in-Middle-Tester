<div align="center">

# Lost-in-Middle-Tester

**用于测试和可视化大语言模型 "Lost-in-the-Middle"（中间丢失）现象的命令行工具。**

*已移植到 [dsh-library](https://github.com/PerryLink/dsh-library) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

大语言模型在处理长文本时，对开头和结尾信息的记忆通常优于中间位置的信息。Lost-in-Middle-Tester 用于量化这一现象：它生成一篇长文档，在指定位置插入一个 `SECRET_CODE_XXXX` 形式的验证码，让模型找出该验证码，并统计每个位置的成功率。

## 功能特性

- 生成内嵌验证码的长文本测试用例
- 支持 OpenAI 与 Anthropic 两种 API 提供商
- 输出 U 型曲线图（PNG）与各位置成功率的 JSON 报告
- 提供成本估算与 `--dry-run` 预览模式
- 使用 Rich 渲染终端进度条与结果表格

## 快速开始

需要 Python 3.9+ 与 [Poetry](https://python-poetry.org/)。

```bash
git clone https://github.com/PerryLink/Lost-in-Middle-Tester.git
cd Lost-in-Middle-Tester
poetry install
```

设置 API 密钥后即可运行测试：

```bash
# OpenAI
export OPENAI_API_KEY=sk-xxx
poetry run lost-in-middle-tester test --model gpt-4

# Anthropic
export ANTHROPIC_API_KEY=sk-ant-xxx
poetry run lost-in-middle-tester test --provider anthropic --model claude-3-opus-20240229
```

## 使用方法

```bash
# 自定义测试参数
poetry run lost-in-middle-tester test \
  --model gpt-4 \
  --text-length 10000 \
  --num-tests 30 \
  --num-positions 15 \
  --output-dir ./my-results

# 预览配置与预估成本（不调用 API）
poetry run lost-in-middle-tester test --model gpt-4 --dry-run
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--api-key` | 环境变量 | API 密钥（回退到 `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`） |
| `--model` | `gpt-4` | 模型名称 |
| `--provider` | `openai` | API 提供商（`openai` / `anthropic`） |
| `--text-length` | `8000` | 文档长度（tokens） |
| `--num-tests` | `20` | 每个位置的测试次数 |
| `--num-positions` | `10` | 测试位置数量 |
| `--output-dir` | `./results` | 输出目录 |
| `--show-plot` | `True` | 是否渲染图表 |
| `--dry-run` | `False` | 预览配置与成本估算 |

## 开发

```bash
poetry run pytest -v
poetry run black src/
poetry run ruff check src/
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink

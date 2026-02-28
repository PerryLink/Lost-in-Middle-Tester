# Contributing to Lost-in-Middle-Tester

## English

### Project Status

This is currently a personal project maintained by [Chance Dean](https://github.com/PerryLink). While contributions are welcome, please note that this project is primarily developed and maintained by a single person.

### How to Report Issues

If you encounter any bugs or have feature requests, please:

1. Check the [existing issues](https://github.com/PerryLink/lost-in-middle-tester/issues) to avoid duplicates
2. Create a new issue with a clear title and description
3. Include:
   - Your Python version
   - Operating system
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Relevant error messages or logs

### Development Environment Setup

#### Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)
- Git

#### Setup Steps

```bash
# 1. Fork and clone the repository
git clone https://github.com/PerryLink/lost-in-middle-tester.git
cd lost-in-middle-tester

# 2. Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# 3. Install dependencies
poetry install

# 4. Activate virtual environment
poetry shell

# 5. Run tests to verify setup
poetry run pytest -v
```

### Code Standards

This project follows **PEP 8** style guidelines with the following tools:

- **Black**: Code formatter (line length: 88)
- **Ruff**: Fast Python linter
- **Pytest**: Testing framework

#### Before Committing

```bash
# Format code
poetry run black src/ tests/

# Check linting
poetry run ruff check src/ tests/

# Run tests
poetry run pytest -v
```

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clear, concise code
   - Add tests for new functionality
   - Update documentation if needed

3. **Ensure code quality**
   ```bash
   poetry run black src/ tests/
   poetry run ruff check src/ tests/
   poetry run pytest -v
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

   Commit message format:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `test:` for test additions/changes
   - `refactor:` for code refactoring

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Provide a clear description of your changes
   - Reference any related issues

### Code Review

- The project maintainer will review your PR
- Be responsive to feedback and questions
- Make requested changes in new commits
- Once approved, your PR will be merged

### Questions?

Feel free to open an issue for any questions or reach out via email: novelnexusai@outlook.com

---

## 中文

### 项目状态

这是一个由 [Chance Dean](https://github.com/PerryLink) 个人维护的项目。虽然欢迎贡献，但请注意这个项目主要由一个人开发和维护。

### 如何报告问题

如果您遇到任何 bug 或有功能请求，请：

1. 检查[现有 issues](https://github.com/PerryLink/lost-in-middle-tester/issues) 避免重复
2. 创建新 issue，提供清晰的标题和描述
3. 包含以下信息：
   - Python 版本
   - 操作系统
   - 重现问题的步骤
   - 期望行为 vs 实际行为
   - 相关错误信息或日志

### 开发环境搭建

#### 前置要求

- Python 3.9 或更高版本
- Poetry（用于依赖管理）
- Git

#### 搭建步骤

```bash
# 1. Fork 并克隆仓库
git clone https://github.com/PerryLink/lost-in-middle-tester.git
cd lost-in-middle-tester

# 2. 安装 Poetry（如果尚未安装）
curl -sSL https://install.python-poetry.org | python3 -

# 3. 安装依赖
poetry install

# 4. 激活虚拟环境
poetry shell

# 5. 运行测试验证设置
poetry run pytest -v
```

### 代码规范

本项目遵循 **PEP 8** 风格指南，使用以下工具：

- **Black**: 代码格式化工具（行长度：88）
- **Ruff**: 快速 Python linter
- **Pytest**: 测试框架

#### 提交前检查

```bash
# 格式化代码
poetry run black src/ tests/

# 检查 linting
poetry run ruff check src/ tests/

# 运行测试
poetry run pytest -v
```

### Pull Request 流程

1. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **进行修改**
   - 编写清晰、简洁的代码
   - 为新功能添加测试
   - 必要时更新文档

3. **确保代码质量**
   ```bash
   poetry run black src/ tests/
   poetry run ruff check src/ tests/
   poetry run pytest -v
   ```

4. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加您的功能描述"
   ```

   提交信息格式：
   - `feat:` 新功能
   - `fix:` bug 修复
   - `docs:` 文档更改
   - `test:` 测试添加/更改
   - `refactor:` 代码重构

5. **推送到您的 fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **创建 Pull Request**
   - 前往原始仓库
   - 点击 "New Pull Request"
   - 选择您的分支
   - 提供清晰的更改描述
   - 引用相关 issues

### 代码审查

- 项目维护者将审查您的 PR
- 请及时响应反馈和问题
- 在新提交中进行请求的更改
- 一旦批准，您的 PR 将被合并

### 有问题？

欢迎通过 issue 提问或发送邮件至：novelnexusai@outlook.com

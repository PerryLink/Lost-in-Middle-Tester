"""CLI interface using Typer."""

import typer
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table
from rich.panel import Panel
import os

from .core import TextGenerator, PasswordInserter, ModelTester, ResultCollector
from .utils import OpenAIClient, AnthropicClient, generate_u_curve, save_results_json, estimate_cost

app = typer.Typer(help="Lost-in-the-Middle Tester - 测试 LLM 长文本处理能力")
console = Console()


@app.command()
def test(
    api_key: str = typer.Option(None, "--api-key", help="API 密钥 (或使用环境变量)"),
    model: str = typer.Option("gpt-4", "--model", help="模型名称"),
    provider: str = typer.Option("openai", "--provider", help="API 提供商 (openai/anthropic)"),
    text_length: int = typer.Option(8000, "--text-length", help="文本长度 (tokens)"),
    num_tests: int = typer.Option(20, "--num-tests", help="每个位置的测试次数"),
    num_positions: int = typer.Option(10, "--num-positions", help="测试位置数量"),
    output_dir: Path = typer.Option("./results", "--output-dir", help="结果输出目录"),
    show_plot: bool = typer.Option(True, "--show-plot", help="是否显示图表"),
    dry_run: bool = typer.Option(False, "--dry-run", help="预览配置和成本估算")
):
    """运行 Lost-in-the-Middle 测试."""

    # 获取 API 密钥
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY" if provider == "openai" else "ANTHROPIC_API_KEY")
        if not api_key:
            console.print("[red]错误: 未提供 API 密钥[/red]")
            raise typer.Exit(1)

    # 显示配置
    console.print(Panel.fit(
        "[bold cyan]Lost-in-the-Middle Tester v1.0.0[/bold cyan]",
        border_style="cyan"
    ))

    config_table = Table(show_header=False, box=None)
    config_table.add_row("模型:", f"[yellow]{model}[/yellow]")
    config_table.add_row("提供商:", f"[yellow]{provider}[/yellow]")
    config_table.add_row("文本长度:", f"[yellow]{text_length} tokens[/yellow]")
    config_table.add_row("测试位置:", f"[yellow]{num_positions}[/yellow]")
    config_table.add_row("每位置测试次数:", f"[yellow]{num_tests}[/yellow]")
    config_table.add_row("总测试次数:", f"[yellow]{num_positions * num_tests}[/yellow]")

    cost = estimate_cost(model, num_positions * num_tests, text_length)
    config_table.add_row("预估成本:", f"[yellow]${cost:.2f}[/yellow]")

    console.print(config_table)
    console.print()

    if dry_run:
        console.print("[green]Dry-run 模式: 配置预览完成[/green]")
        return

    # 初始化客户端
    if provider == "openai":
        client = OpenAIClient(api_key, model)
    else:
        client = AnthropicClient(api_key, model)

    # 初始化组件
    text_gen = TextGenerator()
    tester = ModelTester()
    collector = ResultCollector()

    # 生成测试位置
    positions = [i / (num_positions - 1) for i in range(num_positions)]

    # 执行测试
    total_tests = num_positions * num_tests

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        task = progress.add_task("执行测试...", total=total_tests)

        for position in positions:
            for _ in range(num_tests):
                paragraphs = text_gen.generate(text_length)
                modified_paras, password, _ = PasswordInserter.insert(paragraphs, position)

                success = tester.test(modified_paras, password, client)
                collector.add_result(position, success)

                progress.advance(task)

    # 获取统计结果
    stats = collector.get_statistics()

    # 显示结果
    console.print("\n[bold green]结果:[/bold green]")
    result_table = Table(show_header=True)
    result_table.add_column("位置", style="cyan")
    result_table.add_column("成功率", style="yellow")
    result_table.add_column("成功/总数", style="white")

    min_rate = min(s["success_rate"] for s in stats.values())

    for pos in sorted(stats.keys()):
        s = stats[pos]
        rate_str = f"{s['success_rate']*100:.0f}%"
        count_str = f"{s['success_count']}/{s['total_count']}"

        marker = " ← 最差" if s["success_rate"] == min_rate else ""
        result_table.add_row(
            f"{pos*100:.0f}%",
            rate_str + marker,
            count_str
        )

    console.print(result_table)

    # 保存结果
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    plot_path = output_dir / f"u_curve_{model.replace('-', '_')}_{timestamp}.png"
    json_path = output_dir / f"results_{model.replace('-', '_')}_{timestamp}.json"

    generate_u_curve(stats, plot_path, model)
    save_results_json(stats, json_path)

    console.print(f"\n[green]图表已保存:[/green] {plot_path}")
    console.print(f"[green]结果已保存:[/green] {json_path}")


if __name__ == "__main__":
    app()

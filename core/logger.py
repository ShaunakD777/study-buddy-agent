"""
logger.py - draws everything you see on screen, so you can watch the agent work.

    grey   thinking    = the agent's thought (WHY it's doing something)
    yellow calling     = the agent using a tool       (act)
    green  got result  = the tool's answer coming back (observe)
    blue   panel       = Study Buddy's final answer
    red    panel       = something went wrong, and how to fix it

You don't need to change this file.
"""

import json

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

# One shared "console" that everything prints through.
console = Console()

# Thoughts can be long, so we only show the start of them.
MAX_THOUGHT_LENGTH = 200

# Other screens (like the web page in stretch/) can put a function in this list.
# Every thinking / tool / error line is then passed to it as well as printed here.
listeners = []


def one_line(text):
    # Squash newlines and extra spaces into a single line.
    return " ".join(str(text).split())


def show_line(text, style):
    console.print(Text(text, style=style))
    for listener in listeners:
        listener(text.strip())


def show_welcome():
    console.print(
        Panel(
            "Ask me about any topic, and I'll explain it simply.\n"
            "Try: [italic]explain black holes[/]  ·  [italic]what have I studied?[/]  ·  [italic]quiz me[/]\n"
            "Type [bold]quit[/] to leave.",
            title="[bold]📚 Study Buddy[/]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


def ask_user():
    console.print()
    return console.input("[bold green]You ›[/] ")


def thinking_spinner():
    # Shows a spinning "Thinking..." line while we wait for the LLM.
    return console.status("[cyan]Thinking...[/]", spinner="dots")


def log_thought(text):
    if not text:
        return
    text = one_line(text)
    if len(text) > MAX_THOUGHT_LENGTH:
        text = text[:MAX_THOUGHT_LENGTH] + "..."
    show_line("  💭 thinking: " + text, "dim italic")


def log_tool_call(tool_name, tool_input):
    # tool_input arrives as JSON text, like '{"query": "quantum computing news"}'.
    # We turn it into a dict so we can print just the values.
    try:
        values = json.loads(tool_input).values()
        shown_input = ", ".join(str(value) for value in values)
    except (ValueError, AttributeError):
        shown_input = str(tool_input)

    # "web_search" is printed as "web search"
    readable_name = tool_name.replace("_", " ")
    show_line("  🔧 calling " + readable_name + ": " + one_line(shown_input), "bold yellow")


def log_tool_result(result):
    preview = one_line(result)
    if len(preview) > 80:
        preview = preview[:80] + "..."
    show_line("  ↳ got result: " + preview, "green")


def log_error(problem, fix=""):
    message = "[bold]Problem:[/] " + problem
    if fix:
        message += "\n[bold]Fix:[/] " + fix
    console.print(Panel(message, title="Something went wrong", border_style="red"))
    for listener in listeners:
        listener("⚠️ Problem: " + problem + " Fix: " + fix)


def print_answer(text):
    console.print()
    console.print(
        Panel(
            # hyperlinks=False prints the full web address, so students can see and copy it.
            Markdown(text, hyperlinks=False),
            title="[bold]Study Buddy[/]",
            title_align="left",
            border_style="blue",
            padding=(1, 2),
        )
    )


def print_goodbye():
    console.print("\n[cyan]Bye! Happy studying. 📚[/]")

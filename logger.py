"""
logger.py - prints coloured lines so you can SEE what the agent is doing.

    grey   = the agent's thought (why it's doing something)
    yellow = the agent calling a tool
    red    = something went wrong, and how to fix it

You don't need to change this file.
"""

import json

from colorama import Fore, Style, just_fix_windows_console

# Makes colours work in the Windows terminal too.
just_fix_windows_console()

# Thoughts can be long, so we only show the start of them.
MAX_THOUGHT_LENGTH = 200


def log_thought(text):
    if not text:
        return
    text = " ".join(text.split())  # squash newlines and extra spaces into one line
    if len(text) > MAX_THOUGHT_LENGTH:
        text = text[:MAX_THOUGHT_LENGTH] + "..."
    print(Style.DIM + "  thinking: " + text + Style.RESET_ALL)


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
    print(Fore.YELLOW + "  calling " + readable_name + ": " + shown_input + Style.RESET_ALL)


def log_error(problem, fix=""):
    print(Fore.RED + "\n  Problem: " + problem + Style.RESET_ALL)
    if fix:
        print(Fore.RED + "  Fix: " + fix + Style.RESET_ALL)
    print()


def print_answer(text):
    print(Fore.CYAN + "\nStudy Buddy: " + Style.RESET_ALL + text + "\n")

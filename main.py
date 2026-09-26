"""
main.py - the chat window. Run it with:  python main.py

It reads what you type, hands it to the agent, and prints the answer.
It also turns crashes into plain-English messages. You don't need to change this file.
"""

import sys
import traceback
from pathlib import Path

STUDENT_FILES = ["prompts.py", "tools.py", "agent.py"]
CATCH_UP_TIP = "Stuck? Run  python catch_up.py N  (N = the checkpoint you want to jump to)."


def explain_crash(error):
    """Print which student file and line caused a crash, in plain English."""
    # Find the last line of the crash that was inside one of the student files.
    where = ""
    for frame in traceback.extract_tb(error.__traceback__):
        if Path(frame.filename).name in STUDENT_FILES:
            where = Path(frame.filename).name + ", line " + str(frame.lineno)

    print("\n  Problem: " + type(error).__name__ + ": " + str(error))
    if where:
        print("  It happened in " + where + ". Check that line for a typo.")
    print("  " + CATCH_UP_TIP + "\n")


# ---- Step 1: check Python and load the program ----

if sys.version_info < (3, 10):
    print("Study Buddy needs Python 3.10 or newer. You have " + sys.version.split()[0] + ".")
    print("Fix: install a newer Python from https://www.python.org/downloads/")
    sys.exit(1)

try:
    from agent import chat
    from llm import FriendlyError, get_key
    from logger import log_error, print_answer
except ModuleNotFoundError as error:
    if error.name in ["groq", "tavily", "wikipedia", "dotenv", "colorama"]:
        print("\n  Problem: the library '" + error.name + "' isn't installed.")
        print("  Fix: run  pip install -r requirements.txt  and try again.\n")
    else:
        explain_crash(error)
    sys.exit(1)
except SyntaxError as error:
    # A typo in a student file, such as a missing bracket or quote.
    print("\n  Problem: there's a typo in " + Path(error.filename).name + ", line " + str(error.lineno) + ".")
    print("  Python says: " + str(error.msg))
    print("  Look for a missing bracket, quote, comma or colon on or just before that line.")
    print("  " + CATCH_UP_TIP + "\n")
    sys.exit(1)
except Exception as error:
    explain_crash(error)
    sys.exit(1)


# ---- Step 2: check the keys before we start ----

try:
    get_key("GROQ_API_KEY")
except FriendlyError as error:
    log_error(error.problem, error.fix)
    sys.exit(1)

try:
    get_key("TAVILY_API_KEY")
except FriendlyError as error:
    # Only web search needs this key, so warn and carry on.
    log_error(error.problem + " Web search won't work until you add it.", error.fix)


# ---- Step 3: the chat ----

print("\nStudy Buddy is ready! Ask me about any topic.")
print("Type 'quit' to leave.\n")

while True:
    try:
        user_message = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        break

    if not user_message:
        continue
    if user_message.lower() in ["quit", "exit", "bye"]:
        break

    try:
        answer = chat(user_message)
        print_answer(answer)
    except FriendlyError as error:
        log_error(error.problem, error.fix)
    except KeyboardInterrupt:
        print("\n  (stopped)\n")
    except Exception as error:
        explain_crash(error)

print("\nBye! Happy studying.")

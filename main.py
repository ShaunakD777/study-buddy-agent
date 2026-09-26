"""
main.py - the chat window. Run it with:  python main.py

It reads what you type, hands it to the agent, and shows the answer.
It also turns crashes into plain-English messages. You don't need to change this file.
"""

import sys
import traceback
from pathlib import Path

STUDENT_FILES = ["prompts.py", "tools.py", "agent.py"]
CATCH_UP_TIP = "Stuck? Run  python catch_up.py N  (N = the checkpoint you want to jump to)."


def describe_crash(error):
    """Turn a crash into a plain-English problem and fix, naming the student file and line."""
    # Find the last line of the crash that was inside one of the student files.
    where = ""
    for frame in traceback.extract_tb(error.__traceback__):
        if Path(frame.filename).name in STUDENT_FILES:
            where = Path(frame.filename).name + ", line " + str(frame.lineno)

    problem = type(error).__name__ + ": " + str(error)
    fix = CATCH_UP_TIP
    if where:
        fix = "It happened in " + where + ". Check that line for a typo. " + CATCH_UP_TIP
    return problem, fix


# ---- Step 1: check Python and load the program ----

if sys.version_info < (3, 10):
    print("Study Buddy needs Python 3.10 or newer. You have " + sys.version.split()[0] + ".")
    print("Fix: install a newer Python from https://www.python.org/downloads/")
    sys.exit(1)

try:
    from agent import chat
    from core.llm import FriendlyError, get_key
    from core.logger import ask_user, log_error, print_answer, print_goodbye, show_welcome, thinking_spinner
except ModuleNotFoundError as error:
    if error.name in ["groq", "tavily", "wikipedia", "dotenv", "rich"]:
        print("\nProblem: the library '" + error.name + "' isn't installed.")
        print("Fix: run  pip install -r requirements.txt  and try again.\n")
    else:
        problem, fix = describe_crash(error)
        print("\nProblem: " + problem + "\nFix: " + fix + "\n")
    sys.exit(1)
except SyntaxError as error:
    # A typo in a student file, such as a missing bracket or quote.
    print("\nProblem: there's a typo in " + Path(error.filename).name + ", line " + str(error.lineno) + ".")
    print("Python says: " + str(error.msg))
    print("Fix: look for a missing bracket, quote, comma or colon on or just before that line.")
    print(CATCH_UP_TIP + "\n")
    sys.exit(1)
except Exception as error:
    problem, fix = describe_crash(error)
    print("\nProblem: " + problem + "\nFix: " + fix + "\n")
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

show_welcome()

while True:
    try:
        user_message = ask_user().strip()
    except (KeyboardInterrupt, EOFError):
        break

    if not user_message:
        continue
    if user_message.lower() in ["quit", "exit", "bye"]:
        break

    try:
        with thinking_spinner():
            answer = chat(user_message)
        print_answer(answer)
    except FriendlyError as error:
        log_error(error.problem, error.fix)
    except KeyboardInterrupt:
        log_error("You stopped that answer.", "Just ask again.")
    except Exception as error:
        problem, fix = describe_crash(error)
        log_error(problem, fix)

print_goodbye()

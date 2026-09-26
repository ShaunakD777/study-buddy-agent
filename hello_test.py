"""
hello_test.py - Checkpoint 0. Checks your setup before the session.

Run it with:  python hello_test.py
If everything is fine you'll see: Groq: connected. Tavily: connected. You're ready!
"""

import sys

if sys.version_info < (3, 10):
    print("Study Buddy needs Python 3.10 or newer. You have " + sys.version.split()[0] + ".")
    print("Fix: install a newer Python from https://www.python.org/downloads/")
    sys.exit(1)

try:
    import groq
    from tavily import TavilyClient

    from llm import MODEL, FriendlyError, get_key
except ModuleNotFoundError as error:
    print("Problem: the library '" + str(error.name) + "' isn't installed.")
    print("Fix: run  pip install -r requirements.txt  and try again.")
    sys.exit(1)


def check_groq():
    key = get_key("GROQ_API_KEY")
    try:
        groq.Groq(api_key=key).chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "Say hello"}],
            max_completion_tokens=50,
        )
    except groq.AuthenticationError:
        raise FriendlyError(
            "Groq rejected your key.",
            "Open .env and check GROQ_API_KEY: no spaces, no quotes, the whole key.",
        )
    except groq.APIConnectionError:
        raise FriendlyError("Couldn't reach Groq.", "Check your internet connection and try again.")
    except groq.RateLimitError:
        raise FriendlyError("Groq's rate limit was hit.", "Wait one minute and run this test again.")
    except groq.APIStatusError as error:
        raise FriendlyError("Groq returned an error: " + str(error), "Wait a minute and try again.")


def check_tavily():
    key = get_key("TAVILY_API_KEY")
    try:
        TavilyClient(api_key=key).search("hello", max_results=1)
    except Exception as error:
        raise FriendlyError(
            "Tavily didn't accept the request: " + str(error),
            "Open .env and check TAVILY_API_KEY: no spaces, no quotes, the whole key.",
        )


all_ok = True
for name, check in [("Groq", check_groq), ("Tavily", check_tavily)]:
    try:
        check()
        print(name + ": connected.")
    except FriendlyError as error:
        all_ok = False
        print(name + ": NOT connected.")
        print("   Problem: " + error.problem)
        print("   Fix: " + error.fix)

if all_ok:
    print("You're ready!")
else:
    print("\nFix the problem above, then run  python hello_test.py  again.")

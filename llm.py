"""
llm.py - talks to the LLM (Groq) for us.

ask_llm(history, tools) sends the whole conversation and the list of tools
to the LLM, and gives back its reply as a normal Python dict.

You don't need to change this file.
"""

import os
from pathlib import Path

import groq
from dotenv import load_dotenv

from logger import log_thought

# The model we use. If Groq retires it, change this one line.
MODEL = "openai/gpt-oss-120b"

# Hit a rate limit? Change MODEL above to this smaller model instead.
BACKUP_MODEL = "openai/gpt-oss-20b"

# The .env file sits in the same folder as this file.
ENV_FILE = Path(__file__).parent / ".env"


class FriendlyError(Exception):
    """An error with a plain-English message and a fix, instead of a stack trace."""

    def __init__(self, problem, fix):
        super().__init__(problem)
        self.problem = problem
        self.fix = fix


def get_key(name):
    """Read one API key from the .env file, cleaning up common copy-paste mistakes."""
    if not ENV_FILE.exists():
        raise FriendlyError(
            "There is no .env file in the study-buddy folder.",
            "Copy .env.example, name the copy .env, and paste your keys into it.",
        )

    load_dotenv(ENV_FILE)
    key = os.getenv(name, "")
    # Remove spaces and quotes that often sneak in when pasting.
    key = key.strip().strip('"').strip("'").strip()

    if not key:
        raise FriendlyError(
            name + " is missing from your .env file.",
            "Open .env and paste your key right after " + name + "= (no spaces, no quotes).",
        )
    return key


def ask_llm(history, tools):
    client = groq.Groq(api_key=get_key("GROQ_API_KEY"))

    # The API wants "no tools" written as None, not as an empty list.
    if not tools:
        tools = None

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=history,
            tools=tools,
            reasoning_effort="low",
        )
    except groq.AuthenticationError:
        raise FriendlyError(
            "Groq rejected your API key.",
            "Open .env and check GROQ_API_KEY: no spaces, no quotes, the whole key. "
            "If it still fails, make a new key at https://console.groq.com/keys",
        )
    except groq.RateLimitError:
        raise FriendlyError(
            "You've hit Groq's rate limit (too many requests in a short time).",
            "Wait one minute and try again, or in llm.py set MODEL = BACKUP_MODEL.",
        )
    except groq.APIConnectionError:
        raise FriendlyError(
            "Couldn't reach Groq.",
            "Check your internet connection (try your phone hotspot) and try again.",
        )
    except groq.BadRequestError as error:
        if "tool" in str(error).lower():
            raise FriendlyError(
                "The AI got muddled while trying to use a tool.",
                "Just ask again, maybe in simpler words. If it keeps happening, check your tool descriptions in tools.py.",
            )
        raise FriendlyError(
            "Groq didn't accept the request: " + str(error),
            "If this mentions the model, the model name in llm.py may be retired - try BACKUP_MODEL.",
        )

    message = response.choices[0].message

    # Show the model's thinking in grey, so we can see WHY it does things.
    log_thought(message.reasoning)

    # Turn the reply into a plain dict, the same shape as the other messages in the history.
    reply = {"role": "assistant", "content": message.content or ""}

    if message.tool_calls:
        reply["tool_calls"] = []
        for call in message.tool_calls:
            reply["tool_calls"].append({
                "id": call.id,
                "type": "function",
                "function": {"name": call.function.name, "arguments": call.function.arguments},
            })

    return reply

"""
agent.py - the agent loop and the chat history.

Every message goes round the same loop from the lecture:
    perceive -> reason -> act -> observe -> (reason again...)

    1. Perceive: add the student's message to the chat history.
    2. Reason:   send the history and the tools to the LLM.
    3. Act:      if the LLM asked for a tool, run it.
    4. Observe:  add the tool's result to the history, then go back to step 2.
    When the LLM answers without asking for a tool, that answer is final.
"""

from core.llm import ask_llm
from core.logger import log_tool_call
from your_code.prompts import SYSTEM_PROMPT
from your_code.tools import get_tools_for_llm, run_tool

# Safety limit: at most 5 trips round the loop for each message.
MAX_STEPS = 5

# The chat history is the agent's short-term memory: every message so far.
# It is created ONCE, here, so it survives from one message to the next.
history = [{"role": "system", "content": SYSTEM_PROMPT}]


def chat(user_message):
    # 1. Perceive: add the student's message to the history.
    # CHECKPOINT 1a: ADD the message to the history made at the top of the file,
    # instead of starting a new list each time (a new list = Study Buddy forgets everything).
    # Hint: history.append(...) with a dict like {"role": "user", "content": user_message}
    history.append({"role": "user", "content": user_message})

    for step in range(MAX_STEPS):
        # 2. Reason: send the whole history and the tools to the LLM.
        reply = ask_llm(history, get_tools_for_llm())

        # CHECKPOINT 1b: add the LLM's reply to the history, so it remembers its own answers.
        # Hint: the reply is already a dict, so just append it.
        history.append(reply)

        # Did the LLM ask for a tool?
        if "tool_calls" in reply:
            # 3. Act + 4. Observe
            # CHECKPOINT 2: for each tool call in reply["tool_calls"], read its name and input,
            # log it, run it with run_tool(...), and append the result to the history.
            # Hint: a tool call looks like {"id": ..., "function": {"name": ..., "arguments": ...}}
            # and the result goes in as {"role": "tool", "tool_call_id": ..., "content": result}
            return "I wanted to use a tool, but my tool code isn't written yet. Finish Checkpoint 2 in agent.py, then restart."  # <- delete this line and write your loop here
            # Now go round the loop again, so the LLM can read the results.
        else:
            # No tool needed: this is the final answer.
            return reply["content"]

    return "I used all " + str(MAX_STEPS) + " of my steps without finishing. Try asking in a simpler way."

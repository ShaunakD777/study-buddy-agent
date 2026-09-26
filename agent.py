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

from llm import ask_llm
from logger import log_tool_call
from prompts import SYSTEM_PROMPT
from tools import get_tools_for_llm, run_tool

# Safety limit: at most 5 trips round the loop for each message.
MAX_STEPS = 5

# The chat history is the agent's short-term memory: every message so far.
# It is created ONCE, here, so it survives from one message to the next.
history = [{"role": "system", "content": SYSTEM_PROMPT}]


def chat(user_message):
    # 1. Perceive: add the student's message to the history.
    history.append({"role": "user", "content": user_message})

    for step in range(MAX_STEPS):
        # 2. Reason: send the whole history and the tools to the LLM.
        reply = ask_llm(history, get_tools_for_llm())

        # Add the reply to the history, so the agent remembers its own answers.
        history.append(reply)

        # Did the LLM ask for a tool?
        if "tool_calls" in reply:
            # 3. Act: run each tool the LLM asked for.
            for tool_call in reply["tool_calls"]:
                tool_name = tool_call["function"]["name"]
                tool_input = tool_call["function"]["arguments"]
                log_tool_call(tool_name, tool_input)
                result = run_tool(tool_name, tool_input)

                # 4. Observe: add the result to the history, labelled with the call's id.
                history.append({"role": "tool", "tool_call_id": tool_call["id"], "content": result})
            # Now go round the loop again, so the LLM can read the results.
        else:
            # No tool needed: this is the final answer.
            return reply["content"]

    return "I used all " + str(MAX_STEPS) + " of my steps without finishing. Try asking in a simpler way."

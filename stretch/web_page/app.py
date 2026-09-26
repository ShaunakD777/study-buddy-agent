"""
app.py - Study Buddy in your browser (a stretch goal).

Run it from the main study-buddy folder with:
    streamlit run stretch/web_page/app.py

This is only a different SCREEN. The agent is still yours: every message goes to
chat() in your_code/agent.py, exactly like in the terminal version.
"""

import sys
import traceback
from pathlib import Path

import streamlit as st

# Let Python find the your_code/ and core/ folders, two levels up from this file.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from core import logger
from core.llm import FriendlyError, get_key
from your_code.agent import chat

st.set_page_config(page_title="Study Buddy", page_icon="📚")
st.title("📚 Study Buddy")
st.caption("Ask me about any topic. Try: *explain black holes* · *what have I studied?* · *quiz me*")

# Check the Groq key before anything else.
try:
    get_key("GROQ_API_KEY")
except FriendlyError as error:
    st.error("**Problem:** " + error.problem + "\n\n**Fix:** " + error.fix)
    st.stop()


def describe_crash(error):
    """A plain-English message for a crash, naming the line in your_code/ if that's where it was."""
    message = "**Problem:** " + type(error).__name__ + ": " + str(error)
    for frame in traceback.extract_tb(error.__traceback__):
        if "your_code" in frame.filename:
            message += "\n\nIt happened in your_code/" + Path(frame.filename).name + ", line " + str(frame.lineno) + "."
    return message + "\n\n**Fix:** check that line for a typo, or run `python catch_up.py N`."


# Streamlit runs this whole file again every time you send a message.
# st.session_state survives those re-runs, so we keep the messages on screen there.
# (The agent's real memory is still the history list in your_code/agent.py.)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show the conversation so far.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message.get("steps"):
            with st.expander("What Study Buddy did (" + str(len(message["steps"])) + " steps)"):
                for step in message["steps"]:
                    st.write(step)
        st.markdown(message["content"])

user_message = st.chat_input("Ask Study Buddy...")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        steps = []
        status = st.status("Thinking...", expanded=True)

        # Every thinking / tool line from the agent appears in the status box as it happens.
        def show_step(line):
            steps.append(line)
            status.write(line)

        logger.listeners.clear()
        logger.listeners.append(show_step)

        try:
            answer = chat(user_message)
            if not answer.strip():
                answer = "*(Empty answer - Study Buddy probably wanted a tool it doesn't have yet. That's Checkpoint 2.)*"
        except FriendlyError as error:
            answer = "**Problem:** " + error.problem + "\n\n**Fix:** " + error.fix
        except Exception as error:
            answer = describe_crash(error)

        status.update(label="What Study Buddy did (" + str(len(steps)) + " steps)", state="complete", expanded=False)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer, "steps": steps})

# Helper cheat sheet

For the 2-3 helpers walking the room. Most problems are in this table.
**Short on time? `python catch_up.py N` fixes almost anything in under a minute** (N = the checkpoint they should be at).

## First, check these three things

1. **Right folder?** The terminal must be inside the project folder, the one with `main.py` in it (`ls` or `dir` shows it).
2. **Virtual environment on?** The terminal line starts with `(.venv)`. If not: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac).
3. **Files saved?** An unsaved file shows a dot on its tab in VS Code. Save with Ctrl+S / Cmd+S, then restart Study Buddy.

## Setup problems

| Symptom | Fix |
| --- | --- |
| `'python' is not recognized` (Windows) | Try `py` instead of `python`. Otherwise reinstall Python and tick **Add python.exe to PATH**. |
| `running scripts is disabled on this system` (Windows, when activating) | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again. |
| `the library 'groq' isn't installed` (or tavily, rich...) | The virtual environment isn't on, or setup wasn't finished. Activate it, then `pip install -r requirements.txt`. |
| `There is no .env file` | `copy .env.example .env` (Windows) or `cp .env.example .env` (Mac), then paste the keys in. |
| `GROQ_API_KEY is missing` | Open `.env`, paste the key straight after `GROQ_API_KEY=`, and **save**. |
| `Groq rejected your API key` | Open `.env`: no spaces or quotes, and the whole key. If it still fails, make a new key at console.groq.com. |
| Icons show as boxes or `?` | Harmless: an old terminal. Use the VS Code terminal instead. |
| No laptop, or setup is broken and there's no time | Pair them with a neighbour. Fix the setup at the break. |

## During the checkpoints

| Symptom | Fix |
| --- | --- |
| `You've hit Groq's rate limit` | Wait a minute. If it keeps happening, open `core/llm.py` and change `MODEL = "openai/gpt-oss-120b"` to `MODEL = BACKUP_MODEL`. |
| `Web search (Tavily) failed` | Switch to Wikipedia: in `your_code/tools.py`, change `WEB_SEARCH` to `WIKIPEDIA_SEARCH` in the `TOOLS` line. Restart. |
| `Couldn't reach Groq` | Wi-Fi problem. Try the phone hotspot. |
| `there's a typo in your_code/agent.py, line N` | Look at that line and the one above it: a missing `)`, `]`, `}`, quote, comma or colon. |
| A red panel naming a file and line | A mistake in their code on that line (often a misspelt name like `histroy`). Compare with the hint above the gap. |
| **CP1:** forgets your name | The `history = [...]` line inside `chat()` wasn't replaced with `history.append(...)`, so a new list is made for every message. |
| **CP1:** forgets its own answers | `history.append(reply)` is missing under `CHECKPOINT 1b`. |
| **CP1:** "Study Buddy gave an empty answer" | Normal before Checkpoint 2: it wanted a tool it doesn't have yet. Ask something else. |
| **CP2:** agent never calls the tool | The web search description is empty or too vague. It must say **when** to use it (recent news, current events). |
| **CP2:** "I wanted to use a tool, but my tool code isn't written yet" | The `return "I wanted to use a tool..."` line under `CHECKPOINT 2` is still there. Replace it with the loop code. |
| **CP2:** "I used all 5 of my steps" | The tool result isn't being added to the history, so the agent keeps asking. Check the `history.append({"role": "tool", ...})` line. |
| **CP2:** "The AI got muddled while trying to use a tool" | Ask again. If it repeats, check the tool description and the `"tool_call_id"` line. |
| **CP3:** it never saves a note | The save rule in `prompts.py` is missing or vague, or the `save_note` description is empty. |
| **CP3:** it saves the whole answer | The `summary` description must ask for **3 short lines**. |
| **CP3:** "what have I studied?" finds nothing | They haven't studied a topic since CP3, or they asked before saving. Study one topic, `quit`, restart, then ask. |
| Changes don't do anything | They didn't save the file, or didn't restart (`quit`, then `python main.py`). |

## After `catch_up.py`

| Symptom | Fix |
| --- | --- |
| VS Code says a file has unsaved changes / "file is newer" | Close that tab **without saving**, then reopen it. Saving would put their old version back. |
| "Where did my code go?" | In `my_attempts/before_cpN/`. It's safe. |

## Stretch: web page

| Symptom | Fix |
| --- | --- |
| `'streamlit' is not recognized` | `pip install -r stretch/web_page/requirements.txt` (with the virtual environment on). |
| Asks for an email in the terminal | Press Enter to skip. |
| `No module named your_code` | Run `streamlit run stretch/web_page/app.py` from the main project folder (the one with `main.py`). |

## Anything else, and time is short

```
python catch_up.py N
```

Their own work is saved in `my_attempts/`, so nothing is lost.

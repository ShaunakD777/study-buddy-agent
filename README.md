# 📚 Study Buddy

**An AI study agent you build yourself in 45 minutes.** Type a topic and Study Buddy searches the web, explains it simply, saves a short note, and remembers what you've studied. Say "quiz me" and it tests you.

It's plain Python with no agent framework, so you can see every step of the agent loop: **perceive → reason → act → observe**.

<!-- TODO (presenter): record a 20-second GIF of Study Buddy working and save it as docs/images/demo.gif -->
![Study Buddy searching the web](docs/images/web_search.svg)

> ### 🆘 Stuck or behind? One command catches you up:
> ```
> python catch_up.py 2
> ```
> Use the number of the checkpoint you want to jump to (0 to 4). **Your own work is saved first** in `my_attempts/`, and your keys and notes are never touched.

---

## Contents

1. [Setup (do this at home, before the session)](#setup-do-this-at-home-before-the-session)
2. [The checkpoints](#the-checkpoints)
3. [How the project is organised](#how-the-project-is-organised)
4. [Save your work to GitHub](#save-your-work-to-github)
5. [Make it yours](#make-it-yours)
6. [Share it](#share-it)

---

## Setup (do this at home, before the session)

It takes about 20 minutes. At the end, the hello test must say **You're ready!**

You need: a laptop, a free [GitHub](https://github.com) account, and **VS Code** ([download](https://code.visualstudio.com)).

### Step 1. Install Python 3.10 or newer

- **Windows:** download it from [python.org/downloads](https://www.python.org/downloads/). In the installer, **tick "Add python.exe to PATH"** at the bottom of the first screen, then click Install Now.
  <!-- TODO (presenter): screenshot of the installer with the PATH box ticked -> docs/images/python_path.png -->
- **Mac:** download it from [python.org/downloads](https://www.python.org/downloads/) and run the installer.

Check it worked. Open a **new** terminal and type:

| Windows | Mac |
| --- | --- |
| `python --version` | `python3 --version` |

You should see `Python 3.10` or higher (3.11, 3.12...).

### Step 2. Install Git

- **Windows:** download it from [git-scm.com](https://git-scm.com/download/win) and click Next through the installer.
- **Mac:** type `git --version` in the terminal. If it isn't installed, your Mac offers to install it. Say yes.

### Step 3. Get your own copy of this project

1. At the top of this page on GitHub, click the green **Use this template** button, then **Create a new repository**.
2. Name it `study-buddy`, choose **Public**, and click **Create repository**.
3. On your new repository's page, click the green **Code** button and copy the link.
4. In a terminal, go to the folder where you keep your projects and type (paste your own link):

   ```
   git clone https://github.com/YOUR-USERNAME/study-buddy.git
   cd study-buddy
   ```

5. Open the folder in VS Code: **File → Open Folder → study-buddy**.

**From now on, always run commands from inside the `study-buddy` folder.** In VS Code, **Terminal → New Terminal** opens one in the right place.

### Step 4. Create a virtual environment

This keeps Study Buddy's libraries separate from anything else on your laptop.

| | Windows | Mac |
| --- | --- | --- |
| Create it (once) | `python -m venv .venv` | `python3 -m venv .venv` |
| Switch it on | `.venv\Scripts\activate` | `source .venv/bin/activate` |

When it's on, you'll see **`(.venv)`** at the start of the terminal line.

> **Switch it on again every time you open a new terminal.** No `(.venv)` means Study Buddy can't find its libraries.
>
> Windows error *"running scripts is disabled on this system"*? Run this once, then try again:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

(With the virtual environment on, `python` works on Mac too, so the rest of this guide just says `python`.)

### Step 5. Install the libraries

```
pip install -r requirements.txt
```

### Step 6. Get your two free API keys

- **Groq** (the AI model): sign up at [console.groq.com](https://console.groq.com), open **API Keys**, click **Create API Key**, and copy it. It starts with `gsk_`.
- **Tavily** (web search): sign up at [app.tavily.com](https://app.tavily.com) and copy the API key on your dashboard. It starts with `tvly-`.

<!-- TODO (presenter): screenshots of where the key is on each site -> docs/images/groq_key.png, docs/images/tavily_key.png -->

Keys are like passwords: **never share them or post them online.**

### Step 7. Put your keys in a `.env` file

Make a copy of `.env.example` called `.env`:

| Windows | Mac |
| --- | --- |
| `copy .env.example .env` | `cp .env.example .env` |

Open `.env` in VS Code and paste each key straight after the `=` sign, with **no spaces and no quotes**:

```
GROQ_API_KEY=gsk_your_key_here
TAVILY_API_KEY=tvly-your_key_here
```

Save the file. (`.env` is never uploaded to GitHub, so your keys stay private.)

### Step 8. Run the hello test

```
python hello_test.py
```

You should see:

```
✓ Groq: connected.
✓ Tavily: connected.
You're ready!
```

If it says **NOT connected**, it tells you the problem and how to fix it. Still stuck? Send the organiser a screenshot of the whole terminal.

### Step 9. Meet Study Buddy (optional)

```
python main.py
```

Right now it's a plain chatbot: it doesn't know who it is, forgets what you said, and can't look anything up. **In the session, you'll turn it into an agent.** Type `quit` to leave.

---

## The checkpoints

In the session we build Study Buddy in 4 checkpoints. Each gap in the code is marked `# CHECKPOINT N` with a hint underneath. You only ever edit the three files in **`your_code/`**.

After each checkpoint, restart Study Buddy (`quit`, then `python main.py`) and check you see the result below.

### Checkpoint 1: The brain

*Concepts: instructions, short-term memory*

- **Do (`your_code/prompts.py`):** fill in the system prompt: **ROLE**, **GOAL**, **RULES** and **STYLE**. Replace each bracketed example line with your own words.
- **Do (`your_code/agent.py`):** add each new message to the chat history list, and add the reply after it, so the whole conversation is sent every time.
- **You should see:** it stays in character as a friendly study buddy. Say `my name is Aarav`, then ask `what's my name?` and it remembers.

### Checkpoint 2: The hands

*Concepts: tools, the agent loop*

- **Do (`your_code/tools.py`):** write the web search description: what it does, when to use it, and the one input it needs (the search words). Copy the style of the Wikipedia example.
- **Do (`your_code/agent.py`):** fill the "Yes" branch of the loop: read which tool the LLM asked for, run it, add the result to the history, go back to the LLM.
- **You should see:** ask `what's new in quantum computing this month?` and a yellow line appears, **🔧 calling web search: quantum computing news...**, then an answer with sources.

### Checkpoint 3: The memory

*Concept: long-term memory*

- **Do (`your_code/tools.py`):** write the descriptions for **Save note** and **Read notes**.
- **Do (`your_code/prompts.py`):** add two rules: after explaining a topic, save a 3-line summary; when asked what you've studied, read the notes first.
- **You should see:** learn one topic, close the program, reopen it, ask `what have I studied?` and it lists the topic with the date. Your notes are in `notes/study_notes.txt`.

![Study Buddy saving a note and remembering it after a restart](docs/images/memory.svg)

### Checkpoint 4: Stretch (pick one)

| Option | What you add | You should see |
| --- | --- | --- |
| [Quiz mode](stretch/quiz_mode.md) | A prompt rule: when you say "quiz me", read the notes and ask 3 multiple-choice questions one at a time | A 3-question quiz on what you studied, with a score |
| [A second tool](stretch/second_tool.md) | Switch on Wikipedia search alongside web search | The agent choosing between the two tools and saying why |
| [A web page](stretch/web_page/README.md) | Run the ready-made template in `stretch/` | Study Buddy in a browser chat window |

### Catching up

| If you're behind at the start of... | Run |
| --- | --- |
| Checkpoint 2 | `python catch_up.py 1` |
| Checkpoint 3 | `python catch_up.py 2` |
| Checkpoint 4 | `python catch_up.py 3` |
| Want the finished quiz version? | `python catch_up.py 4` |
| Want to start over from scratch? | `python catch_up.py 0` |

Your own attempt is saved in `my_attempts/before_cpN/`. Compare it with the working version afterwards - that's often where the learning happens.

---

## How the project is organised

```
study-buddy/
├── your_code/        ← the only folder you edit
│   ├── prompts.py        the system prompt (the agent's instructions)
│   ├── tools.py          the tools, and their descriptions for the LLM
│   └── agent.py          the agent loop and the chat history
├── main.py           run this to chat with Study Buddy
├── hello_test.py     checks your setup
├── catch_up.py       jumps to the end of any checkpoint
├── core/             pre-built parts (talking to Groq, drawing the screen)
├── checkpoints/      finished copies of your_code/ for each checkpoint
├── stretch/          the Checkpoint 4 options
├── notes/            your saved study notes (created when you first save one)
└── .env              your keys (you create this; never uploaded)
```

This is the loop you complete in `your_code/agent.py`:

```mermaid
flowchart TD
    U["You type a message"] --> H["Add it to the chat history"]
    H --> L["Send history + tools to the LLM"]
    L --> Q{"Did it ask for a tool?"}
    Q -->|Yes| T["Run the tool, log it"]
    T --> R["Add the result to the history"]
    R --> S{"5 steps used?"}
    S -->|No| L
    S -->|Yes| F["Stop and say so"]
    Q -->|No| A["Print the answer"]
```

---

## Save your work to GitHub

Do this at the end of the session (and whenever you change something).

**The first time only**, tell Git who you are (use your GitHub email):

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Then, every time you want to save:

```
git add .
git commit -m "Finished Study Buddy checkpoint 3"
git push
```

The first push opens a browser window asking you to sign in to GitHub. Your keys (`.env`) and notes are never uploaded - they're listed in `.gitignore`.

Prefer clicking? In VS Code, open the **Source Control** panel (the branch icon on the left), type a message, click **Commit**, then **Sync Changes**.

---

## Make it yours

Your repo is now a portfolio project. Replace this README with your own. Copy this template into `README.md` and fill in the brackets:

````markdown
# 📚 Study Buddy

[One line: what it does and who it's for. E.g. "An AI agent that researches any topic,
explains it simply, and quizzes me on what I've learned."]

![Demo](docs/images/demo.gif)  <!-- record a short GIF of it working -->

## How it works

Study Buddy is an AI agent built in plain Python, with no agent framework.
Each message goes round a loop: perceive → reason → act → observe.

```mermaid
flowchart LR
    A["My message"] --> B["LLM decides"]
    B -->|needs a tool| C["Web search / notes"]
    C -->|result| B
    B -->|done| D["Answer"]
```

- **Brain:** a Groq-hosted LLM, steered by a system prompt I wrote (role, goal, rules, style)
- **Hands:** tools for web search (Tavily), saving notes and reading notes
- **Memory:** chat history (short-term) and a notes file (long-term)

## What I'd add next

- [ ] [An idea, e.g. flashcards from my notes]
- [ ] [Another idea]
- [ ] [Another idea]

## Run it yourself

See the setup steps in the original project: [link to the original repo]
````

---

## Share it

Built something you're proud of? Post it on LinkedIn. A template:

```
I built my first AI agent today! 🤖📚

The problem: [e.g. I waste time jumping between tabs when I study a new topic.]

So I built Study Buddy: it searches the web, explains any topic simply,
saves notes, and quizzes me on what I've learned.

[attach a 20-second screen recording]

What I learned:
• An agent is just a loop: perceive → reason → act → observe
• Tool descriptions decide WHEN the AI uses a tool
• Memory is just data you give back to the model

Code: [your repo link]

#AI #AgenticAI #Python #LearningInPublic
```

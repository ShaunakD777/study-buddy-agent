# 🛠️ Setup from scratch

This guide is for a laptop that has **never been used for coding**: no Python, no VS Code, nothing.
Follow the steps in order. It takes about 30–40 minutes, and at the end the hello test
must say **You're ready!**

The steps are written for **Windows**. Where a Mac is different, it says so in *italics*.

---

## Phase A: Make your accounts (browser only, ~10 min)

1. **Groq account** (the AI model). Go to [console.groq.com](https://console.groq.com) and sign up
   (Sign in with Google works). Open **API Keys → Create API Key** and copy the key. It starts with
   `gsk_`. Paste it into a Notepad file for now, because Groq only shows it once.
2. **Tavily account** (web search). Go to [app.tavily.com](https://app.tavily.com), sign up, and copy
   the API key shown on your dashboard. It starts with `tvly-`. Paste it into the same Notepad file.
3. **GitHub account** (optional, but needed to save your work online later). Sign up at
   [github.com](https://github.com) and **verify your email**. GitHub won't let you create
   repositories until you do.

> Keys are like passwords: **never share them or post them online.**

---

## Phase B: Install the tools (~15 min)

### 4. Install Python 3.10 or newer

Download it from [python.org/downloads](https://www.python.org/downloads/) and run the installer.

- On the **first screen**, tick **"Add python.exe to PATH"** at the bottom, *then* click
  **Install Now**. This is the most common reason setup fails, so don't skip it.
- If a **"Disable path length limit"** button appears at the end, click it.

*Mac: run the downloaded installer. When it finishes, open **Applications → Python 3.x** and
double-click **Install Certificates.command**, otherwise web search can fail with SSL errors.*

### 5. Install VS Code

Download it from [code.visualstudio.com](https://code.visualstudio.com) and run the installer.
On the **"Select Additional Tasks"** screen, tick **"Add to PATH"** and both
**"Add 'Open with Code'"** boxes.

### 6. Install Git (optional)

**You only need Git if you want to clone the project (Phase C, Option 1) or save your work to
GitHub (Phase G).** If you're going to download the ZIP instead, you can skip this step.

Download it from [git-scm.com/download/win](https://git-scm.com/download/win) and click **Next**
through the installer. The default option on every screen is fine.

*Mac: open Terminal and type `git --version`. If Git isn't installed, your Mac offers to install
it. Say yes.*

### 7. Check everything installed

1. **Close every terminal or PowerShell window** that's open. Only new windows see the new installs.
2. Open **VS Code**, then go to **Terminal → New Terminal** in the top menu.
3. Type:

   ```
   python --version
   ```

   You should see `Python 3.10` or higher (3.11, 3.12...). *Mac: type `python3 --version`.*

4. If you installed Git, also type `git --version`. You should see `git version 2.something`.

> **Did the Microsoft Store open, or does it say "Python was not found"?** Python isn't on your
> PATH. Run the Python installer again, choose **Modify → Next**, and tick
> **"Add Python to environment variables"**. Then close VS Code, reopen it, and check again.

5. *(Optional)* In VS Code, open **Extensions** (Ctrl+Shift+X), search **Python**, and install the one
   by **Microsoft**. It adds colours and helpful hints. Study Buddy runs fine without it.

---

## Phase C: Get the project (~5 min)

The project lives at **<https://github.com/ShaunakD777/study-buddy-agent>**. Pick **one** option.

### Option 1: Download the ZIP (no Git needed)

1. Open <https://github.com/ShaunakD777/study-buddy-agent> in your browser.
2. Click the green **Code** button → **Download ZIP**.
3. Go to your **Downloads** folder, right-click `study-buddy-agent-main.zip` → **Extract All** →
   **Extract**. *Mac: just double-click the ZIP.*
4. Move the extracted folder somewhere easy to find, such as **Documents**.
5. In VS Code, go to **File → Open Folder** and pick the folder that has `main.py` directly inside it.
   Windows sometimes puts the files one level deeper: if you see a second
   `study-buddy-agent-main` folder inside the first one, open the inner one.

### Option 2: Clone with Git

1. In the VS Code terminal, go to your Documents folder and clone the project:

   ```
   cd $HOME\Documents
   git clone https://github.com/ShaunakD777/study-buddy-agent.git
   ```

   *Mac: `cd ~/Documents` instead of the first line.*

2. In VS Code, go to **File → Open Folder** → **Documents → study-buddy-agent**.

### Either way

- If VS Code asks **"Do you trust the authors of the files in this folder?"**, click **Yes**.
- Open a fresh terminal: **Terminal → New Terminal**. It opens *inside* the project folder.

> **From now on, always run commands from inside the project folder.** A new terminal in VS Code
> always opens in the right place.

---

## Phase D: Set up Python for the project (~5 min)

### 8. Create a virtual environment (once only)

This keeps Study Buddy's libraries separate from everything else on your laptop.

```
python -m venv .venv
```

*Mac: `python3 -m venv .venv`*

### 9. Switch it on

```
.venv\Scripts\activate
```

*Mac: `source .venv/bin/activate`*

When it's on, you'll see **`(.venv)`** at the start of the terminal line.

> **Error: "running scripts is disabled on this system"?** Run this once, type `Y` if asked, then
> try activating again:
>
> ```
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```

> **Switch it on again every time you open a new terminal.** No `(.venv)` means Study Buddy can't
> find its libraries.

### 10. Install the libraries

```
pip install -r requirements.txt
```

Wait until it finishes and you get the prompt back. It needs an internet connection.

---

## Phase E: Add your keys (~2 min)

### 11. Make your `.env` file

```
copy .env.example .env
```

*Mac: `cp .env.example .env`*

### 12. Paste your keys into it

Open `.env` in VS Code (it's in the file list on the left). Paste each key straight after the `=`
sign, with **no spaces and no quotes**:

```
GROQ_API_KEY=gsk_your_key_here
TAVILY_API_KEY=tvly-your_key_here
```

Save with **Ctrl+S** (*Mac: Cmd+S*). Now delete the Notepad file where you kept your keys.

---

## Phase F: Run it

### 13. Run the hello test

```
python hello_test.py
```

You should see:

```
✓ Groq: connected.
✓ Tavily: connected.
You're ready!
```

If it says **NOT connected**, it tells you the problem and how to fix it. If you're on college
Wi-Fi and it can't connect, try a phone hotspot.

### 14. Meet Study Buddy

```
python main.py
```

Right now it's a plain chatbot. **In the session, you'll turn it into an agent.** Type `quit` to
leave.

### Every time after this

1. Open the project folder in VS Code.
2. **Terminal → New Terminal**.
3. `.venv\Scripts\activate` (*Mac: `source .venv/bin/activate`*)
4. `python main.py`

---

## Phase G: Save your work to GitHub (later, optional)

This needs **Git** (step 6) and a **GitHub account** (step 3).

1. On GitHub, click **+** (top right) → **New repository**. Name it `study-buddy`, choose
   **Public**, leave every box unticked, and click **Create repository**. Copy its link.
2. Tell Git who you are (first time only, use your GitHub email):

   ```
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

3. Connect your project to your new repository. Paste your own link in place of the one below.

   **If you downloaded the ZIP:**

   ```
   git init
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/study-buddy.git
   ```

   **If you cloned:**

   ```
   git remote set-url origin https://github.com/YOUR-USERNAME/study-buddy.git
   ```

4. Save and upload:

   ```
   git add .
   git commit -m "My Study Buddy"
   git push -u origin main
   ```

   The first push opens a browser window asking you to sign in to GitHub.

After that, saving again is just `git add .`, `git commit -m "what you changed"`, `git push`.

Your keys (`.env`), your notes and your virtual environment are **never uploaded**, because they're
listed in `.gitignore`. Don't upload the project by dragging files onto the GitHub website: that
skips `.gitignore` and can publish your keys.

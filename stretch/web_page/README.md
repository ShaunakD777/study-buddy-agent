# Stretch: A web page

Put Study Buddy in a browser chat window. It's the **same agent** - every message still goes
to `chat()` in your `your_code/agent.py`. Only the screen changes.

## Do

1. Install the web library (one time only, it's quite big so give it a minute):

   ```
   pip install -r stretch/web_page/requirements.txt
   ```

2. From the main study-buddy folder, start the web page:

   ```
   streamlit run stretch/web_page/app.py
   ```

   The first time, Streamlit may ask for your email in the terminal. Just press **Enter** to skip.

3. Your browser opens at `http://localhost:8501`. If it doesn't, open that address yourself.

## You should see

- A chat window titled **📚 Study Buddy**.
- While it works, a **Thinking...** box showing each step live (`thinking`, `calling web search`, `got result`...).
- The answer, with a collapsed **What Study Buddy did** box above it. Click it to see the steps again.
- Your terminal still shows the coloured lines too.

## Stopping it

Press **Ctrl + C** in the terminal.

## Common problems

| What happens | Why, and the fix |
| --- | --- |
| `'streamlit' is not recognized` | Step 1 didn't finish. Run the `pip install` line again. |
| `No module named your_code` | Run the command from the main study-buddy folder, not from inside `stretch/`. |
| You changed a file and nothing changed | Click **Rerun** at the top-right of the page, or stop and start it again. |
| It forgets things after you refresh the page | Refreshing clears the screen but not the agent's memory. Stop and restart to start fresh. |

## Curious how it works?

Open `stretch/web_page/app.py`. It's under 100 lines, and most of it is just drawing the chat bubbles.
The important line is `answer = chat(user_message)` - the same call the terminal version makes.

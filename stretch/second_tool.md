# Stretch: A second tool

Right now Study Buddy has one way to look things up: web search.
`your_code/tools.py` also has a **Wikipedia search** tool, already written and already described.
It's just switched off. Switch it on and watch the agent **choose** between two tools.

## Do

**1. Give it the tool.** Open `your_code/tools.py` and find the `TOOLS` list near the bottom:

```python
TOOLS = [WEB_SEARCH, SAVE_NOTE, READ_NOTES]
```

Add `WIKIPEDIA_SEARCH` to it:

```python
TOOLS = [WEB_SEARCH, WIKIPEDIA_SEARCH, SAVE_NOTE, READ_NOTES]
```

**2. Tell it when to use it.** Having a tool isn't enough - the agent also needs a reason to use it.
Open `your_code/prompts.py` and add one rule to the `RULES:` section. For example:

```
- Before you explain a well-known study topic (science, history, famous people), use wikipedia_search to check your facts.
```

Save both files and restart: `python main.py`

## You should see

Ask one settled topic and one piece of news, and compare the lines:

| You ask | You should see |
| --- | --- |
| `explain the French Revolution` | `calling wikipedia search: French Revolution` |
| `what's new in AI this week?` | `calling web search: ...` |

The grey **thinking** line above each one shows *why* it picked that tool.
The agent decides by reading the two tool **descriptions** - the same kind you wrote in Checkpoint 2.

## Try this

- Read the `description` of `WIKIPEDIA_SEARCH` and `WEB_SEARCH`. Which words make the agent choose one or the other?
- Change the Wikipedia description to say "Use it for everything". Restart and ask about the news. What changes? (Change it back afterwards!)

## Common problems

| What happens | Why, and the fix |
| --- | --- |
| `NameError: WIKIPEDIA_SEARCH` | Check the spelling: capital letters, with an underscore. |
| It never uses Wikipedia | Check you added the rule in step 2, and ask about something old and well known, like a historical event or a science concept. |
| Still stuck | `python catch_up.py 3`, then try again. |

# Stretch: Quiz mode

Study Buddy already saves notes on what you learn. Now it can test you on them.
This is a mini version of the Class vs. The Agent game from the lecture.

## Do

Open `your_code/prompts.py`. In the `RULES:` section, add **one new rule** on its own line, starting with `- `.

Your rule should tell Study Buddy that when you say "quiz me", it should:

1. read your notes first,
2. ask 3 multiple-choice questions about those topics, **one at a time**, waiting for your answer each time,
3. give your score out of 3 at the end.

Try writing it in your own words first. Stuck? This is the rule in the finished version:

```
- When the student says "quiz me", use read_notes, then ask 3 multiple-choice questions about those topics, one at a time. Wait for each answer before asking the next question. At the end, give their score out of 3.
```

Save the file and restart: `python main.py`

## You should see

1. Study a topic first, e.g. `explain photosynthesis simply` (you'll see `calling save note`).
2. Type `quiz me` and you'll see `calling read notes`, then **Question 1** with options A-D.
3. Answer with a letter. It tells you if you were right, then asks Question 2, then 3.
4. At the end: a score, like **You got 2 out of 3**.

## Common problems

| What happens | Why, and the fix |
| --- | --- |
| It asks all 3 questions at once | Your rule doesn't say "one at a time" and "wait for each answer". Add that. |
| It quizzes you on random topics | Your rule doesn't say to read the notes first. Add "use read_notes". |
| "You have no notes yet" | Study a topic first, so there's something to quiz you on. |
| Still stuck | `python catch_up.py 4` gives you the finished quiz version. |

"""
prompts.py - the agent's instructions (its "system prompt").

The LLM reads this before every conversation. It decides who the agent is,
what it's trying to do, which rules it follows, and how it talks.
"""

# CHECKPOINT 1: write the ROLE, GOAL, RULES and STYLE below.
# Hint: one or two plain sentences each. Rules are a list, one "- " line per rule.

# CHECKPOINT 3: add two rules to RULES: save a 3-line note after explaining a topic,
# and read the notes first when asked what you've studied.

# CHECKPOINT 4 (stretch - quiz mode): add a rule for "quiz me": read the notes,
# ask 3 multiple-choice questions one at a time, then give a score.

SYSTEM_PROMPT = """
ROLE:
(Who is the agent? Example: You are a patient maths tutor for school students.)

GOAL:
(What is it trying to achieve? Example: Help students solve problems step by step, without just giving the answer.)

RULES:
(What must it always or never do? One "- " line per rule. Example: - Never make up facts.)

STYLE:
(How does it talk? Example: Short, cheerful sentences.)
"""

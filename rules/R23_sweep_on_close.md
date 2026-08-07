# R23. Sweep at close, unasked

> **type:** rule - **status:** active - **default:** yes - **check:** the hook reports nothing

Closing a task includes sweeping the repository: inbox empty, no lock files, no empty folders, no broken links.

**Why.** Mess accumulates from the edges. A single stray lock file is nothing; forty of them mean nobody has looked in months.

**How.** `.claude/hooks/repo_sweep.py` does the counting at the end of every turn. What it reports is attended to then, not later.

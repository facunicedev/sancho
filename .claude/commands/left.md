---
description: "Where we are and what is left: current task, open tasks, decisions waiting and what is theirs to do"
allowed-tools: Read, Grep, Glob, Bash
---

They are asking where things stand. **This command writes nothing**: it reads, counts and answers.

## 1. Read, in this order

| File | What you get from it |
|---|---|
| `HANDOFF.md` | The current task, its checklist and what is waiting on their decision |
| The task log | Tasks marked `(OPEN)` and the backlog block |
| The proposals folder | What is waiting for their approval. If only `.gitkeep` is there, none |
| The inbox, and any screenshots folder named in `sancho.md` | Material that arrived and has not been looked at ([R10](../../rules/R10_inbox.md)) |

## 2. Count without inventing

Checklist boxes are counted by reading `[x]` and `[ ]`, not from memory ([R01](../../rules/R01_calculations_in_python.md)). If an item is ticked and was not done, that is the first thing to say.

## 3. Answer

Four blocks, in this order and none beyond them:

1. **The current task.** What was asked, in their words. How many checklist items are done out of how many, and **which ones are missing**.
2. **What is left to close it.** Only what blocks closing, not what would be nice.
3. **What they decide.** Each point with its options and which one you recommend.
4. **What is theirs to do elsewhere.** What you cannot do: send an email, buy something, fix a profile. With its deadline if it has one.

And at the end, **the open tasks that are not this one**, one line each: what they are and what has them stopped.

In plain language, no jargon ([R35](../../rules/R35_plain_language.md)). Never "all good": if nothing is left, say what you checked to know that.

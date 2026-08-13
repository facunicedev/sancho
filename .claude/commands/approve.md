---
description: Approves one or more proposals in Proposals/: they get applied, deleted, and the architect runs behind
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent
---

They have **approved** the proposals named after the command: `/approve P18 P20`, or `/approve all`.

**With nothing after it, nothing gets applied.** List the live proposals in `Proposals/`, one line each with what would change, and ask which ones ([R40](../../rules/R40_summarise_what_you_ask_them_to_sign.md)).

For each named proposal:

1. Read it whole. Its header says what kind it is: a new rule, or a change to a skill, a hook, an agent or a command.
2. **Apply it where that piece lives.** A new rule means a card in `rules/` and its row in `MEMORY.md`. A change to an existing piece means editing that piece and nothing else.
3. **Delete the proposal file** ([R27](../../rules/R27_harvest_proposes.md)). It does not go down to the archive: applied, it already lives in the card or in the code, and keeping it is a second place to read the same thing. Git keeps the why.
4. One line in the task's entry in `Documents/TASKS.md` saying what was applied.

Then **run the `architect` agent in its sweep pass**, saying that word: applying a proposal moves files and leaves indexes half done (`WORKFLOW.md`, step 9). **That pass proposes nothing**, and that is why it has to be named: a sweep that proposes turns every `/approve` into the next `/approve`.

What gets turned down goes through `/notapprove`.

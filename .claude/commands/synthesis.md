---
description: Summarises the task log, rebuilds the decision table and sends the architect to review the system
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Agent
---

Synthesis is due ([R13](../../rules/R13_synthesis.md)). It fires for either of two reasons, and it does not matter which: the task counter hits a multiple of ten, or the cap hook reports that the task log went over its line limit.

Done in this order, skipping nothing.

## 1. Measure before writing

Count the lines of the task log. Read it in full. Note the counter, which tasks are closed and which are open on purpose.

## 2. The synthesis

One level-one synthesis per block of ten closed tasks. Five syntheses of one level produce one of the next.

What it says: what kind of work showed up, grouped into families; what went well and what was expensive; what was decided that still holds; and the mistakes worth not repeating.

What happens to the detail it summarises:

| The original carries | What happens to it |
|---|---|
| Only the process of the task | The synthesis **replaces** it. The history stays in version control |
| Figures, quotes or links | It **coexists**: trimmed to the part that cannot be reconstructed |

This is not optional. If the log has the same number of lines at the end as at the start, there was no synthesis: there was a summary stacked on top, which is exactly what made the file grow in the first place.

## 3. The decision table

Rebuilt **whole**, not appended to. One row per kind of request: what to do, with which piece, and which task it was learned from. Anything that did not come up once in the last block goes.

## 4. The architect

Launch the `architect` agent. It reviews the system, not the content: hooks alive, files near their cap, pieces untouched, chronic warnings, the remote if there is one, and updates to Claude Code that affect what is built here. It leaves at most three proposals.

Wait for its result and **report it with the figures**, not with "all good".

## 5. Close

- Count the lines again. If the log is still over its cap, the synthesis replaced nothing. Go back to step 2.
- Update the counter and the date of the last synthesis.
- Leave one line in `HANDOFF.md` saying what the synthesis changed.
- Show the architect's proposals and **wait for approval**. None of them becomes a rule on its own ([R27](../../rules/R27_harvest_proposes.md), [R05](../../rules/R05_approval_to_close.md)).

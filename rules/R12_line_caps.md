# R12. Files read whole have a line cap

> **type:** rule - **status:** active - **default:** yes - **check:** the hook, on every write

Control files have a ceiling, checked by `.claude/hooks/line_caps.py`. When it fires, the answer is never to raise the ceiling: the detail moves to where it belongs.

**Why.** A file that is read in full at the start of every session becomes useless when it grows. A handoff at 129 lines is not a handoff, it is a second copy of the task log.

**How.** The caps and where the overflow goes live in one table in `WORKFLOW.md`, and the hook reads the same table.

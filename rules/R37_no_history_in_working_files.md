# R37. No working file carries its own change log

**A file that says how work happens today does not explain why it changed.** No "change log", no "previous version", no "this used to say", and no reason for a superseded decision sitting inside the file that replaced it.

## Where the why lives

| What | Where it lives |
|---|---|
| Why a file changed | The commit message |
| What was decided in a task, and why | The task log |
| Superseded material that is nowhere else | The archive folder, with its row ([R26](R26_archive_dont_delete.md)) |

## Why

Whoever opens `WORKFLOW.md` wants to know what to do now. Every paragraph explaining what is no longer done is context that gets read, gets paid for and helps nobody. A measured case: a change log took 17 of 230 lines, 7 % of a file sitting at 92 % of its cap, and what the cap table said to move out when it overflowed was **that very change log**, so the way out was circular.

And there is an effect worse than size: a file with its history inside **ages while lying**. The old version and the new one share the same reading, and there is no way to tell which one rules without reading both.

## How it is checked

`.claude/hooks/coherence.py` warns when a working file carries a history, versioning or change-log heading. The archive folder and the task log are left out: there the history **is** the content.

---
description: Discards one or more proposals in Proposals/: they get deleted with their reason written in the log
allowed-tools: Read, Edit, Glob, Grep, Bash
---

They have **discarded** the proposals named after the command: `/notapprove P18 P20, the skill already covers that criterion`.

**With nothing after it, nothing gets deleted.** List the live proposals in `Proposals/`, one line each, and ask which ones.

For each named proposal:

1. **Delete the file** ([R27](../../rules/R27_harvest_proposes.md)). A folder of dead proposals is a folder nobody opens again, and this is not a case for [R26](../../rules/R26_archive_dont_delete.md): what was discarded was never applied, and git keeps all of it.
2. **One line in the task's entry in `Documents/TASKS.md`** saying what was discarded and why. If they gave no reason, ask in one sentence before deleting: with no reason on record, the same proposal is born again a month later.

The `architect` does not run here: nothing moved.

What gets approved goes through `/approve`.

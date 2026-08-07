# R28. No file without a row, in both directions

> **type:** rule - **status:** active - **default:** yes - **check:** the hook, at the end of every turn

Every file and folder appears in its index, and every link in an index points at something that exists.

**Why.** An index that is only right in one direction is worse than none: it looks complete while hiding what is missing.

**How.** `.claude/hooks/repo_sweep.py` checks both directions. A folder must appear with its backticks and its slash, so a passing mention of the word does not count as a row.

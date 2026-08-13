# R41. State is written as you go, never at the end

**Every result is saved to its own file the moment you have it, before starting the next one.** This holds for the main thread, for any agent, and for any repository. Nothing accumulates in the conversation waiting for a final dump.

The reason is not tidiness: **the session gets cut without warning**. Account limits and search budgets run out mid-task and there is no goodbye. Whatever lived only in the context never existed.

## The three parts, which go together

- **One file per unit of work**, not one big file at the end. Twenty companies are twenty files.
- **Start with what matters most**, so that if the session dies, what is missing is the expendable part. When the brief does not set the order, whoever executes picks it and says so.
- **Running out of a tool is not giving up, it is switching tools.** The search engine has a budget; opening an address you already know does not. And a wall is recorded with **which rungs were tried**, never as "not accessible".

## A quota gap does not close a record, it leaves it half done

When an agent finishes by saying "the search budget ran out", **its unit of work is not done**. It does not count as complete, you do not move on, and you do not summarise it as if the data did not exist. It gets relaunched on what was missing, and whoever goes next is told in writing **what is already confirmed**, so as not to repeat it, and **what was never looked at**.

It checks itself: whoever runs out of budget **writes it in the notes, saying what was left to look at**, and records carrying that note **do not count** towards progress — they go to a retry list. A "not found" without the note means someone looked and there was nothing; with the note, it means nobody looked.

Three records were once closed that way, all cut off at the two fields that weigh most. Retrying one of them revealed the company was **in liquidation**, listed as a normal supplier with its liquidator recorded as the contact person.

## Where this came from

On one prospecting task, **three waves of agents** died to session limits. The two that wrote as they went lost **nothing**: 87 records in the first wave, 77 in the second. The third accumulated its work to dump at the end and **lost all of it**, four agents at once, zero results on disk.

What turned this into a rule rather than a fix to one agent: the fix was first written by hand into each agent's brief, instead of into the place where it applies by itself. **A remedy you have to remember to type each time is not a remedy** ([R39](R39_the_cause_not_the_symptom.md)).

## Where it is applied

In `.claude/agents/architect.md`, as its opening line of duty.

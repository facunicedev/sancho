# Commands

> **What this file is for.** Everything you can type, and everything that happens without you typing, on one page. The commands themselves live in `.claude/commands/`; this table says what each one does, not how it does it.
>
> [En español](COMMANDS.es.md)

## What you type

| Command | What it does | When |
|---|---|---|
| `/sign` | Signs the checklist of the current task and opens the production gate | When you have read the checklist and agree with it |
| `/approve` | Applies the proposals you name from `Proposals/`, deletes them and runs the `architect` behind | When a proposal looks right to you |
| `/notapprove` | Discards the proposals you name, with the reason written into the task log | When a proposal does not convince you |
| `/left` | Where things stand: current task, open ones, decisions waiting, and what is yours to do | Whenever you want to know |
| `/synthesis` | Summarises the task log, rebuilds the decision table and sends the `architect` agent to review the system | Every 10 tasks, or when the cap hook says the log went over its limit |

And one that is not ours but gets used the same way: **`/clear`**, which empties the conversation. It is only offered once the state has been written to disk (R36), never before.

**`/sign` is the key to the whole thing.** Until you type it, nothing gets written into your documents, calculations or deliverables folders: the assistant can prepare, research and propose, but not produce. That is on purpose, and it is the one command you cannot skip. It is a command and not a phrase because guessing whether a message approved something failed twice with the approval sitting right there in front of it.

## What happens without you typing anything

Hooks. You never have to remember any of them: they run themselves.

| Hook | What it does | When it fires |
|---|---|---|
| `line_caps.py` | Warns when a control file goes over its line cap | On every write |
| `repo_sweep.py` | Warns about files missing from their index, inboxes left full, and leftover junk | At the end of the turn |
| `coherence.py` | Warns about cited paths that do not exist and counts that do not add up | At the end of the turn |
| `the_gate.py` | **Blocks** producing without a checklist you signed, and says what the next step is | Before writing, on `/sign`, and at the end of the turn |

**Three warn and two block, and that is the difference that matters.** A warning you can ignore; a block you cannot. Blocking is kept for the two things that ruin the work: producing before you have agreed what is being produced, and researching in the expensive place.

**None of them watches anything listed in `.gitignore`.** What belongs to the repository is decided by git, not by a list of folder names written inside each hook. Point a hook at a downloaded dataset or a backup and it will report on sentences nobody here wrote.

## If a command does not show up

Type `/` for the list. If a new command is missing, restart the session: `.claude/commands/` is read at startup.

## Adding your own

A command earns its place when you find yourself typing the same long request by hand, and the action publishes, deletes or costs money. Anything shorter is just asking. The full criterion is in `WORKFLOW.md`, under «When each piece is born».

# Workflow

> **What this file is.** The route a task takes, step by step, with its options, its tests and its reviews.
>
> **What it is not.** No rule is written here. Rules live in `rules/`, indexed in `MEMORY.md`. This file points at them by code.
>
> **Version 1, born 2026-08-07**, out of a real working repository with seventeen tasks behind it.

## What counts as a task

A whole piece of work, not a message. Someone asks for something, then adjusts, corrects or adds detail: all of that is **one task** and the route runs once, at the end. Inside a task there can be many rounds without restarting anything.

---

## The route

```
  0. Intake         look in the inbox, the screenshots folder and Proposals/
  1. Routing        what kind of task is this, and which lane
  2. Logging        HANDOFF.md + TASKS.md
  3. Prior search   forums first, unless the task is purely internal
  4. Analysis       break it into steps, write the checklist
  5. The plan       short, not exhaustive
  6. Approval  -->  no: adjust and go back to 4
  7. Execution      ticking each item as it finishes
  8. Review         the machine one and the judgement one, on the files
  9. Final log      HANDOFF.md, TASKS.md, and the harvest to Proposals/
 10. Closing list   the general checklist
 11. Approval  -->  no: adjust and go back to 7
                    yes: task closed
```

---

## Step 0. Intake

Looked at every time, unasked: the inbox ([R10](rules/R10_inbox.md)), the screenshots folder if `sancho.md` names one, `Proposals/` in case something is waiting, and `HANDOFF.md`.

Whatever is in the inbox is not filed blindly: it moves to where it belongs or it is discarded ([R09](rules/R09_subfolder_per_task.md)).

## Step 1. Routing and lane

Two questions, in this order.

**Is there already a piece for this?** Check the current decision table in `Documents/TASKS.md`.

| What you find | What you do |
|---|---|
| A skill covers it | Load it and follow it |
| A row in the decision table | Follow that row and count one more repetition |
| Nothing | Do it from scratch, with a prior search, and log it as repetition one |

**Which lane?** A ten-minute errand does not go through eleven steps.

| Lane | When | What it skips |
|---|---|---|
| **Short** | One file, no figures, no outside recipient, under fifteen minutes | Steps 3, 5 and 6. The checklist still gets written, even at three lines |
| **Normal** | Everything else | Nothing |
| **Long** | Research, a deliverable going outside, or more than three files touched | Nothing, and the checklist is split into blocks with a stop in the middle |

The lane is chosen here and noted in `HANDOFF.md`. If it turns out to be a different one, change it and say so.

## Step 2. First log entry

A new entry in `Documents/TASKS.md` with what was asked, in their words, and `HANDOFF.md` up to date.

**Give the entry a title that says what the task is**, because that title is what the task is called from then on, in conversation and in the files. The number stays behind it, holding the counter and making the entry findable, and it is written in brackets: "The three gates" (#21). A title that does not tell one task from another is not a title: "Improvements" or "Misc" force you to open the file to find out what they were.

## Step 3. Prior search

Goes **before** the analysis, because it feeds the plan ([R06](rules/R06_search_before_acting.md)). Skipped when the task is purely internal or the fact is already verified here.

## Step 4. Analysis and checklist

Break the task into concrete steps and **decide in writing which files will be created or touched**. The checklist comes out of that and goes into `HANDOFF.md` before anything is executed.

No task runs in one go without a checklist, however small.

## Step 5. The plan

Short. What will be done and in what order, not the step by step, which already lives in the checklist.

## Step 6. Plan approval

If they ask for changes, adjust and go back to step 4. Nothing runs meanwhile.

## Step 7. Execution

Follow the checklist item by item. **Each item is ticked in `HANDOFF.md` the moment it is done**, before starting the next.

The reason is concrete: if the session is cut off halfway, `HANDOFF.md` shows exactly what was finished, and the next session picks up from there without repeating work.

## Step 8. Review

Two different reviews, and neither is done by reading a summary of what you did. They are done on the files.

**The machine one.** Run by the hooks, so it does not depend on anyone remembering: line caps, files with no row in their index, rules written outside their card. If a hook reports something, it is attended to then.

**The judgement one.** Cannot be automated, so it is a step:

- Open the finished file and look at it ([R17](rules/R17_verify_the_output.md)).
- Check every figure in the deliverable against the output that produced it ([R01](rules/R01_calculations_in_python.md)).
- Open the spreadsheet and confirm the cells hold formulas ([R03](rules/R03_excel_formulas.md)).
- Run the text through the style guide ([R04](rules/R04_writing_style.md)).
- If it describes the person, check it against `Knowledge/PROFILE.md`.

Whoever did the work does not mark their own exam: the review is against the files and the rules, not against the memory of what you meant to do.

## Step 9. Final log and harvest

`HANDOFF.md` with the state and what is left. `Documents/TASKS.md` with the closing entry. And **the harvest**: if the task produced something useful for other tasks, it goes to `Proposals/` ([R27](rules/R27_harvest_proposes.md)). If there is nothing to propose, propose nothing.

## Step 10. General closing checklist

- [ ] The request is logged and categorised in `TASKS.md`.
- [ ] The files touched match the ones the analysis said would be touched, or the difference is explained.
- [ ] Every checklist item is ticked, or dropped with a reason.
- [ ] Both reviews are done and no hook is reporting anything.
- [ ] If there is a final file, it is copied to `Deliverables/<Task>/` with its row ([R07](rules/R07_copy_to_deliverables.md)).
- [ ] The inbox is empty and the repository swept ([R23](rules/R23_sweep_on_close.md)).
- [ ] `HANDOFF.md` and `TASKS.md` are current.
- [ ] The harvest is in `Proposals/`, or it was decided there was nothing.
- [ ] If the counter hit a multiple of ten, synthesis is due ([R13](rules/R13_synthesis.md)).

## Step 11. Closing

Finishing the checklist does **not** close the task. The person closes it, approving in words ([R05](rules/R05_approval_to_close.md)). Once they have, a fresh session is suggested. It is also suggested unprompted whenever the session stops helping and there is nothing left in it worth keeping: on a change of subject, after research already filed, and before a long job ([R36](rules/R36_clear_the_session.md)).

Some tasks are left open on purpose because they depend on something the person has to do. Those are marked as such and do not block the others.

---

## Short lists by kind of action

Added as sub-items to the step 4 checklist when that action comes up.

**Making a Word file:** [R11](rules/R11_check_templates.md) - [R02](rules/R02_justified_word.md) - simple design - [R01](rules/R01_calculations_in_python.md) - saved in `Documents/<Task>/` - [R07](rules/R07_copy_to_deliverables.md).

**Making a spreadsheet:** [R11](rules/R11_check_templates.md) - [R03](rules/R03_excel_formulas.md) - styled, never raw - saved in `Documents/<Task>/` - [R07](rules/R07_copy_to_deliverables.md).

**Doing a calculation:** [R01](rules/R01_calculations_in_python.md) - the deliverable reads the output rather than retyping it - [R09](rules/R09_subfolder_per_task.md), current version of the script only.

**Writing for a person:** [R04](rules/R04_writing_style.md) - [R35](rules/R35_plain_language.md) - if it describes them, check the profile.

**Taking in outside material:** [R09](rules/R09_subfolder_per_task.md) and [R10](rules/R10_inbox.md). When in doubt, keep less.

---

## When each piece is born

Walk it in order and stop at the first one that fits. None of the thresholds is invented.

| Piece | Born when | Checked by | Fails if |
|---|---|---|---|
| **Rule** | It is a fact or a criterion to keep in mind | It fits on one line of the `MEMORY.md` index | It has become a procedure and is still there |
| **Hook** | The condition is a comparison a machine runs, and breaking it ruins a deliverable | The script answers yes or no without interpreting anything | It needs nuance. Then it was a rule |
| **Skill** | The same procedure done three times, and two checkable statements can be written about its result | Cross-fire test: if one request triggers two skills, one is redundant | Its description overlaps another, or does not say when to use it |
| **Agent** | The same worker is launched with the same instructions again and again, and its intermediate steps are of no use to the conversation | Count of repeated launches | It is expected to act on its own. An agent has to be called |
| **Command** | The same long request gets typed by hand, and the action publishes, deletes or spends money | An unwanted trigger would cost something irreversible | Nobody types it |

**An agent gets a model when it is born** (R38). Without that line it inherits the caller's, which is the biggest one, and counting costs the same as deciding.

**There is no cap on skills.** There is a budget the program measures itself, and it penalises the skill nobody invokes. What to watch is overlap.

**When to do nothing:** fewer than three repetitions, a subjective result, or the same output with and without the piece.

---

## Line caps

Files that get read in full have a ceiling, checked by `.claude/hooks/line_caps.py` ([R12](rules/R12_line_caps.md)). When the hook fires, the ceiling does not go up: the detail moves.

| File | Cap | Where the overflow goes |
|---|---|---|
| `HANDOFF.md` | 70 | To `Documents/TASKS.md` |
| `CLAUDE.md` | 120 | To the card of the rule it belongs to |
| `MEMORY.md` | 120 | To the body of the card; only one line per rule lives here |
| `WORKFLOW.md` | 250 | To the change log, or to a report in `Knowledge/` |
| `rules/*.md` | 30 | A rule that does not fit in 30 lines is a procedure, and it should be a skill |
| Folder indexes | 120 | Group rows by category, not by task |
| `Documents/TASKS.md` | 250 | Synthesis is due: it replaces the detail it summarises |
| `.claude/skills/*/SKILL.md` | 500 | To a supporting file alongside. This is the official limit |

## The life cycle

| When | What happens |
|---|---|
| A document is superseded | To the archive, with its date and reason ([R26](rules/R26_archive_dont_delete.md)) |
| Every 10 tasks, **or when `TASKS.md` passes 250 lines** | The cap hook fires and `/synthesis` runs ([R13](rules/R13_synthesis.md)) |
| In that same `/synthesis` | The `architect` agent reviews the system and leaves at most three proposals |
| Every 10 tasks | Every rule is reviewed: does it change behaviour? The one that changes nothing is archived |
| Every three months | Check that the paths cited still exist |
| Every three months | Which piece has not been touched? If none has, the system has stopped learning |

# Memory

> **Index of rules.** How to work with this person. One line each; the full text, the reason and the check live in the card in `rules/`. No rule is restated here: if a statement appears twice, one copy is wrong.
>
> This file is imported by `CLAUDE.md`, so it loads in every session. The cards are read when the rule comes up.
>
> Not to be confused with `Knowledge/PROFILE.md`, which answers **who they are**; `Documents/TASKS.md`, which answers **what was done**; or `HANDOFF.md`, which answers **where the session stopped**.
>
> These twenty-five are the **defaults**. They ship switched on because they are what office work needs, and every one of them was earned by getting something wrong first. Any of them can be turned off: say so, and the card moves to the archive with the date and the reason. The numbering has gaps on purpose, so a rule keeps its number when it travels between repositories.

## Always, on any task

| Rule | In one line |
|---|---|
| [R01](rules/R01_calculations_in_python.md) | Every figure is computed by a script, with the script and its output kept. |
| [R04](rules/R04_writing_style.md) | Anything a person will read goes through the style guide. |
| [R05](rules/R05_approval_to_close.md) | Nothing closes without an explicit yes, in their words. |
| [R06](rules/R06_search_before_acting.md) | Search before acting, forums and real voices before the official line. |
| [R08](rules/R08_memory_levels.md) | Four memory files, four questions, no overlap. |
| [R18](rules/R18_exhaust_deduction.md) | Exhaust what they already sent before asking for a fact. |
| [R32](rules/R32_research_preferences.md) | Open by default and validated by reading. Popularity is not quality. |
| [R35](rules/R35_plain_language.md) | Explain every decision in plain words. Jargon goes after, in brackets. |

## When producing a file

| Rule | In one line |
|---|---|
| [R02](rules/R02_justified_word.md) | Body text in Word is justified, margins in inches. |
| [R03](rules/R03_excel_formulas.md) | In Excel, figures are live formulas against a raw data sheet. |
| [R11](rules/R11_check_templates.md) | Look at the templates before building a Word or an Excel. |
| [R14](rules/R14_patch_dont_regenerate.md) | Once they edit by hand, you patch instead of regenerating. |
| [R17](rules/R17_verify_the_output.md) | Check the finished file, never the source that produced it. |
| [R29](rules/R29_same_format_to_paste.md) | If they will paste it elsewhere, keep the original shape and add columns at the end. |
| [R30](rules/R30_measure_before_spending.md) | When a decision costs money, measure the real state first. |

## When writing for someone

| Rule | In one line |
|---|---|
| [R15](rules/R15_commands_for_the_user.md) | Commands they type are given exactly as their shell expects. |
| [R35](rules/R35_plain_language.md) | The same rule again, because this is where it is broken most. |

## When tidying and closing

| Rule | In one line |
|---|---|
| [R07](rules/R07_copy_to_deliverables.md) | The final file gets copied to `Deliverables/<Task>/` with its row. |
| [R09](rules/R09_subfolder_per_task.md) | One subfolder per task, nothing loose, no keeping things just in case. |
| [R10](rules/R10_inbox.md) | The inbox is an inbox, and it is empty at close. |
| [R12](rules/R12_line_caps.md) | Files read whole have a line cap, checked by a hook. |
| [R13](rules/R13_synthesis.md) | Synthesis on a cadence, and the decision table rebuilt whole with it. |
| [R23](rules/R23_sweep_on_close.md) | Sweep the repository at close, without being asked. |
| [R26](rules/R26_archive_dont_delete.md) | Superseded material is archived with its date and reason, not deleted. |
| [R27](rules/R27_harvest_proposes.md) | What is learned is proposed in `Proposals/`, never written into memory. |
| [R28](rules/R28_nothing_unfiled.md) | No file without a row in its index, in both directions. |

## How this index grows

A new rule is never written here directly. It comes out of a task, gets noted as a proposal ([R27](rules/R27_harvest_proposes.md)), the person approves it, and only then does it get a card and a row. Every ten tasks all of them are reviewed: a rule that changes no behaviour is archived ([R26](rules/R26_archive_dont_delete.md)).

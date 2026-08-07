# Contributing

Thanks for looking. Here is what is worth sending and what is not.

## What is worth sending

**A rule that cost you something.** The best contribution to this repository is a default that you learned the hard way, with the story of what went wrong attached. "Check the page count in the PDF, not in the source" is worth having because somebody sent a two-page document that looked like one page. A rule without a scar is a guess, and guesses make the index longer without making the work better.

Use the card format in `rules/`: what the rule says, **why** (with the real case, and a figure if you have one), and **how** it gets applied. Thirty lines maximum. If it does not fit in thirty lines it is a procedure, not a rule, and it should be a skill.

**A language.** Adding one means: a column in the folder table in `SETUP.md`, a block of rows in `INDEXES` in `.claude/hooks/repo_sweep.py`, and the matching patterns in `.claude/hooks/line_caps.py`. Nothing else changes. If you find yourself editing more than that, something is wrong and say so in the issue.

**A bug in the two hooks.** They are the only code here. If one of them reports something that is fine, or stays quiet about something that is not, that is a real bug and it is welcome. Include the file layout that triggers it.

**Telling us the method does not survive your job.** If you tried this in a job that is not office work and the workflow got in the way, that is more useful than a patch. Open an issue and describe where it broke.

## What is not worth sending

**Skills.** [The README explains why](README.md#why-it-ships-with-zero-skills). Briefly: a skill is somebody's procedure for somebody's job, and shipping mine to you is not a feature. The method for making your own is in `WORKFLOW.md`.

**A rule that has happened once.** One repetition is a coincidence. Three is a procedure. Come back on the third.

**A hook that acts instead of reporting.** Both hooks here only ever say that something is wrong. Nothing moves a file on its own. That line is deliberate and it stays.

**Anything that needs a package installed.** Python 3 and Claude Code, that is the whole dependency list, and keeping it that way is most of the point.

## How

Open an issue first if it is bigger than a typo. Say what happened to you, not what you would like the repository to be.

For a pull request: one change per branch, and the commit message says what changed and why in plain words. If you touched a rule card, say which real case moved you.

## Style

Everything here is written to be read by somebody who does not program. That is a hard requirement, not a preference ([R35](rules/R35_plain_language.md)). If a sentence needs a glossary, rewrite the sentence.

No em dashes. Vary your sentence lengths. Skip the compulsory group of three. If it reads like it was generated, it will be sent back, which is a slightly absurd rule for a repository about working with a language model, and it is still the rule.

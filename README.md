# <div align="center"> **Sancho**

<div align="center"> <img width="1597" height="985" alt="image" src="https://github.com/user-attachments/assets/11f6eab3-030a-405a-9106-d6bd25d01dbb" />


**A harness for Claude Code, for people whose job is not code.**

Spreadsheets. Reports for a boss who reads the first paragraph. Emails to companies that owe you an answer. That job.

[Español](README.es.md) · MIT licensed · v0.1 </div>

---

## Who Sancho is

Don Quijote sees forty giants on the plain and charges. Sancho Panza, who is riding next to him, says the sentence that the whole book turns on:

> "Mire vuestra merced que aquellos que allí se parecen no son gigantes, sino molinos de viento."

Look, sir, those are not giants. Those are windmills.

He is right, he says it plainly, and he gets on the horse anyway.

That is the job. Not the hero. The one who keeps the receipts, points at the windmill, and rides along.

Three more things about Sancho, because they are not decoration, they are the design:

**He speaks in proverbs.** Sancho strings together folk sayings, one after another, until Don Quijote begs him to stop. Each one is a small piece of hard-won knowledge with a reason behind it. This repository is a pile of them. They are in `rules/`.

**He governs an island, and he is good at it.** In the second volume Sancho is handed the Ínsula Barataria as a joke. He rules it for ten days, settles disputes with unglamorous good sense, and then walks away on his own because the job is not worth what it costs. The sidekick turns out to be competent when given something real. And he knows when to stop, which is rarer.

**They both change.** Over two volumes Sancho gets more idealistic and Don Quijote gets more practical. Scholars gave it names: *sanchificación* and *quijotización*. It is the oldest documented case of two parties learning from each other by working together, published in 1605, and it is exactly what this repository is trying to do with you.

Also, it is in the public domain. No trademark lawyer has ever sent a letter about Sancho Panza.

---

## What actually happens when you install it

Sancho asks you one question. Not a form, not an onboarding flow, one question:

> **In which language should I work?**

Then it creates your folders in that language, tells you what it made, and shuts up until you give it work.

That is it. It does not ask your name, your job, your industry, or what you plan to use it for. It works those out from the work. A setup questionnaire is answered once, badly, by somebody who has not started yet.

---

## Why this exists

You already have Claude Code. It is good. It also forgets everything the moment you close the window, and there is a specific way that goes wrong for office work:

**You explain your preferences again every session.** Justify the text. Formulas, not pasted numbers. Do not send me a markdown file, my boss uses Word. By the fourth time you stop asking.

**It is confidently wrong about numbers.** Not often, but a number in a report is checked by the person reading it, which is the worst possible time.

**Files pile up with nobody's name on them.** `informe_v2_final_FINAL.docx`. You know the folder.

**Nothing accumulates.** You solve a problem well on Tuesday and on Friday you solve it from scratch, slightly worse.

Sancho fixes those four, in that order. Not with cleverness. With filing.

---

## The words this repo uses, and what they mean

There are five kinds of thing here and they are constantly confused with each other. Here is the whole taxonomy, and the test for which one you need.

| Piece | What it is | It is born when | It fails when |
|---|---|---|---|
| **Rule** | A fact or a preference, written once, on one card | You want something remembered | It grew into a procedure and is still filed as a rule |
| **Hook** | A small script the program runs by itself, at a fixed moment | A machine can answer it yes or no, and getting it wrong ruins a deliverable | It needs judgement. Then it was a rule |
| **Skill** | A written procedure, loaded when it applies | The same procedure has been done three times | Its description overlaps another one and neither knows whose turn it is |
| **Agent** | A worker with its own context, called to go away and come back with an answer | You keep launching the same worker with the same instructions | You expect it to act on its own. An agent has to be called |
| **Command** | A long request you got tired of typing | You type the same thing again, and it publishes, deletes or spends money | Nobody types it |

**A rule is a noun. A skill is a verb. A hook is an alarm clock. An agent is an employee. A command is a shortcut.**

The important part is the bottom row of the "born when" column: **three repetitions**. Not one. One repetition is a coincidence, two is a pattern you have imagined, three is a procedure. Everything in this repository that is not a rule had to happen three times first.

---

## Why it ships with zero skills

This is the design decision people argue with, so here is the reasoning.

A skill is somebody else's procedure for somebody else's job. Mine says the report goes to a Spanish trade office and the figures are in euros with a comma for decimals. Yours does not. A skill I write for my job and ship to you is not a feature, it is a stranger's habit installed in your repository, and you will spend more time fighting it than you would have spent writing it.

The measurement backs it up rather than my opinion doing the work. Skills curated by a human raise task accuracy meaningfully. Skills a model writes for itself average out to roughly nothing. The difference is not the writing, it is who decided it was worth writing.

So Sancho ships the **method** for making skills, not the skills. `WORKFLOW.md` tells you when one is born, how to test whether it works, and how to tell when two of them overlap. Then your third repetition of something produces a skill that is yours, about your job, in your language.

Same reason there is no plugin marketplace here and no list of integrations. If you want a hundred procedures for a job nobody described, that already exists elsewhere.

The rules are different, and they do ship switched on. A rule is not a procedure, it is a default, and the defaults here are the ones that office work needs no matter what the office does.

---

## What ships switched on

The default rules, in `rules/`, indexed one line each in `MEMORY.md`. Every one of them was earned by getting something wrong first. The ones that matter most on day one:

- **Every figure is computed by a script**, and the script is kept next to its output. No mental arithmetic, ever ([R01](rules/R01_calculations_in_python.md)).
- **Spreadsheet numbers are live formulas** against a raw data sheet, never pasted values ([R03](rules/R03_excel_formulas.md)).
- **Word documents come out justified**, with margins in inches ([R02](rules/R02_justified_word.md)).
- **You check the finished file, not the script that made it.** Page counts live in the PDF ([R17](rules/R17_verify_the_output.md)).
- **Nothing closes without you saying so, in words.** A finished checklist is not permission ([R05](rules/R05_approval_to_close.md)).
- **Forums before press releases.** The official answer to "does this matter" is always yes, because somebody sells it ([R06](rules/R06_search_before_acting.md)).
- **Once you edit a document by hand, it stops regenerating** and starts patching ([R14](rules/R14_patch_dont_regenerate.md)).
- **Every decision gets explained in plain words.** The jargon goes after, in brackets ([R35](rules/R35_plain_language.md)).
- **You get told when to clear the session**, once everything worth keeping is written to a file ([R36](rules/R36_clear_the_session.md)).

**To turn one off, say so.** The card moves to the archive with the date and the reason. Nothing is deleted, because in four months you will want to know why you changed your mind.

---

## The things that run by themselves

Everything else in Sancho is a written instruction, which means it depends on the model remembering. These do not. **Three of them warn and two of them block**, and that difference is the whole design.

**`line_caps.py`** watches file sizes on every write. When your task log passes 250 lines, it says so. The answer is never to raise the limit. The answer is that it is time to summarise, and it names the command that does it.

**`repo_sweep.py`** runs at the end of every turn and reports what is out of place: a file with no row in any index, an index pointing at a file that no longer exists, an inbox that was never emptied, a rule copied into two places.

**`coherence.py`** runs at the end of the turn too, and catches the files that contradict each other: a path cited in a document that is not on disk, a sentence saying "the 32 rules" when there are 36 cards, a change log growing inside a file that is supposed to say how things work now.

Those three only ever tell you something is wrong. **The two below actually stop the work**, and they are the ones worth understanding before you install this.

**`the_gate.py` is why you have to type `/sign`.** Until you do, nothing gets written into your documents, calculations or deliverables folders. The assistant can research, prepare and propose; it cannot produce. When you type `/sign`, the checklist in `HANDOFF.md` is frozen as it stands, and the signature is good for that checklist and that session only — change the list and it expires by itself.

**If you find yourself blocked and do not know why, the key is `/sign`.**

**`research_guard.py`** stops the main conversation from doing research itself instead of handing it to the `researcher` agent. The first stray search passes; the second does not, because two searches in a row are research, and research in the main thread costs many times what it costs inside an agent.

**Neither block trusts anything the model writes.** That is the point: a gate that reads a file written by the very thing it is watching is not a gate. `the_gate.py` rests on a message from you, and `research_guard.py` on the caller identity the harness itself sets. Every hook ships with `--selftest`, and what those tests prove is the property, not the arithmetic:

```bash
python .claude/hooks/the_gate.py --selftest
```

No hook moves or deletes your files. A hook that acts on its own in somebody else's repository is how you get support tickets from strangers at midnight.

---

## The four files that remember

Each answers exactly one question. If two of them answer the same question they drift apart, and then you cannot trust either.

| File | Question |
|---|---|
| `HANDOFF.md` | Where did the last session stop? |
| `Documents/TASKS.md` | What was done in each task? |
| `MEMORY.md` | How should I work with this person? |
| `Knowledge/PROFILE.md` | Who are they? |

The profile is written by Sancho, about you, from the work. Read it. It will be wrong about something and you will want to fix it.

---

## How it learns

Not by writing things into its own memory. That is the failure mode of every self-improving setup: it fills its own context with its own guesses and gets worse in a way nobody notices.

Instead, when a task produces something reusable, it lands in `Proposals/` as a file you read and approve or bin. Then, and only then, it becomes a rule ([R27](rules/R27_harvest_proposes.md)).

Every ten tasks, or whenever the log gets too long, `/synthesis` runs. It rewrites the log so the summary **replaces** the detail instead of stacking on top of it, rebuilds the decision table from scratch, and sends the `architect` agent to check the machinery: are the hooks alive, which files are near their limit, which rule has not been touched in three months, which warning has been ignored for weeks.

The architect leaves at most three proposals. If it has five, the worst two were not proposals.

---

## Install

You need [Claude Code](https://claude.com/claude-code) and Python 3 on your machine. Nothing else. No packages, no keys, no account, no server.

```bash
git clone https://github.com/facunicedev/sancho.git my-work
cd my-work
rm -rf .git && git init
claude
```

The `rm -rf .git && git init` is so your work gets its own history instead of being tangled with this repository's. Your files never come back here.

Then Claude asks the language question, and you start.

---

## What this is not

Not an app. Not a service. Not a wrapper around anything. It is a folder with markdown in it, and you can read all of it in twenty minutes.

Not a CRM, a project manager or a note system. It sits next to whatever you already use.

Not an autonomous agent. It does not send your email. It writes the draft and stops, because the one consistent finding across everyone who has tried the other thing is that automating an unvalidated process reproduces the mistake faster and more expensively.

Not finished. This is v0.1, extracted from one real repository with seventeen real tasks behind it. What is in here has been used. What has not been used is not in here.

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Short version: the interesting contribution is a rule that cost you something to learn, with the story of what went wrong attached. Rules without a scar are guesses.

## License

MIT. See [LICENSE](LICENSE). Do what you like with it.

# -*- coding: utf-8 -*-
"""Catches files that contradict each other, or themselves.

Stop hook. Three checks, all deterministic: they are answered without reading to
understand, which is exactly the line between what a hook does and what the
`architect` agent does.

  1. Cited paths (R28). Every repository path named in a .md exists on disk. This
     is the most repetitive defect there is: a file moves and the dozens of links
     that named it are left pointing at nothing.
  2. Counts that do not add up. A sentence like "the 32 rules" compared against
     the cards that actually exist.
  3. A change log living inside a working file (R37).

Why a hook and not a periodic review: an architect pass can run with 34 cards in
front of it and CLAUDE.md saying 32, leave three proposals and notice none of it.
Counting is not judgement. And between two architect passes fit ten tasks.

It always exits 0: it warns, it does not block. Blocking is `the_gate.py`.

    python .claude/hooks/coherence.py --selftest
"""

import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# One row per language, like the other hooks. A folder that does not exist never
# matches, so adding a language means adding names and nothing else.
FOLDERS = ("Knowledge", "Documents", "Calculations", "Deliverables", "Templates",
           "Proposals", "Inbox", "rules", ".claude",
           "Conocimiento", "Documentos", "Calculos", "Entregables", "Plantillas",
           "Propuestas", "Volcado", "reglas")

# Where the history IS the content, so R37 does not apply.
NO_R37 = ("Knowledge/archive/", "Documents/TASKS.md", "HANDOFF.md",
          "Conocimiento/archivo/", "Documentos/TAREAS.md")

# A dated report is a FROZEN record: it describes the repository of the day it was
# written, and one of its paths no longer existing is history, not a defect.
# Demanding otherwise would turn the hook into twenty-five permanent warnings, and
# a warning nobody attends to is indistinguishable from not having it. What is held
# to account is whatever states how work happens TODAY: the control files, the rule
# cards, the indexes and .claude/.
LIVE = ("Knowledge/KNOWLEDGE.md", "Knowledge/PROFILE.md", "Knowledge/WRITING_STYLE.md",
        "Conocimiento/CONOCIMIENTO.md", "Conocimiento/PERFIL.md")


def frozen(name):
    for base in ("Knowledge/", "Conocimiento/"):
        if name.startswith(base):
            if name in LIVE or name.startswith(base + "rules/") \
                    or name.startswith(base + "reglas/"):
                return False
            return True
    return False


CHANGELOG_HEADING = re.compile(
    r"^#{1,4}\s*(change ?log|history|revision history|previous versions|"
    r"historial|registro de cambios)\b", re.IGNORECASE | re.MULTILINE)

# "the 32 rules". Only this shape: a counter that warns about what it is not gets
# ignored, and "cards" also names other kinds of card.
COUNT = re.compile(r"\bthe\s+(\d{1,3})\s+(rules)\b", re.IGNORECASE)

# And only in the files that ASSERT how the repository stands today. A task log does
# not assert: it quotes what was found one day, and that number was true then.
ASSERT = ("CLAUDE.md", "MEMORY.md", "WORKFLOW.md",
          "Knowledge/KNOWLEDGE.md", "Conocimiento/CONOCIMIENTO.md")

# The `*` belongs in the character class: without it the regex stopped at the star
# and handed back `.claude/skills`, a truncated prefix that looks like a real path
# and gets reported as missing. The glob has to be captured whole to be recognised.
PATH = re.compile(
    r"(?<![\w/.-])((?:" + "|".join(re.escape(c) for c in FOLDERS) +
    r")/[\w./*-]*[\w/*])")

# A script named on its own, with no folder in front: `line_caps.py`. Cards can cite
# scripts that never existed, and the path check does not see them for lack of a folder.
SCRIPT = re.compile(r"`([\w-]+\.py)`")

# A line that PROPOSES asserts nothing, so its path need not exist yet. Two shapes,
# both recognised without interpreting anything:
#
#   - An unticked checklist item: the path is what has to be created. Warning about
#     it every turn states precisely the reason the item is still open.
#   - A file under the proposals folder, which describes something not done yet.
#     If its path already existed, the proposal would be pointless.
#
# Ticking the item demands the path again, which is when it should be demanded.
PENDING = re.compile(r"^\s*[-*]\s*\[\s\]")
PROPOSALS = ("Proposals/", "Propuestas/")

# And the same idea one level up, which is what this repository needs most. Sancho
# ships WITHOUT its work folders: they are created on the first run, named in the
# working language (see SETUP.md). So every path into one of them describes what
# will exist, not what does. Demanding them of a fresh clone produced seventeen
# warnings before anyone had run anything, and a hook that cries on install gets
# switched off on install.
#
# The test is the top-level folder, not a list of files: the day the folder exists,
# every path inside it is demanded again, which is when it can be demanded.
def _not_set_up_yet(clean, exists):
    top = clean.split("/")[0]
    return top != ".claude" and not exists(top)


def markdowns():
    """Only the .md files that belong to the repository. What git ignores does not:
    it is working material, and its sentences are not claims this file must hold up."""
    return common.files(ROOT, ".md")


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


def how_many_rules():
    for folder in ("rules", "reglas"):
        d = os.path.join(ROOT, folder)
        if os.path.isdir(d):
            return len([f for f in os.listdir(d) if f.endswith(".md")])
    return None


def review(text, name, exists, n_rules, scripts=None):
    """Returns the list of warnings. `exists` decides whether a path is on disk and
    `scripts` is the set of .py names the repository holds.

    Kept away from I/O on purpose: the selftest exercises it whole without touching
    the disk."""
    warnings = []
    still = frozen(name)

    # Only where the OWN machinery is described. A task log and a proposal cite
    # scripts from other repositories and old names on purpose: that is their subject.
    ours = (name in ASSERT or name.startswith("rules/") or name.startswith("reglas/")
            or name.startswith(".claude/"))

    if scripts is not None and ours and not still:
        for script in sorted(set(SCRIPT.findall(text))):
            if script not in scripts:
                warnings.append("%s cites `%s`, which is no script of this repository"
                                % (name, script))

    # Paths are looked at line by line rather than all at once, so the ones that
    # propose instead of assert can be skipped. A path never crosses a newline.
    if not still and not name.startswith(PROPOSALS):
        broken = []
        for line in text.splitlines():
            if PENDING.match(line):
                continue
            for path in PATH.findall(line):
                clean = path.rstrip("/")
                if "<" in clean or "NN" in clean or "*" in clean:
                    continue  # placeholder or glob, not a path
                if _not_set_up_yet(clean, exists):
                    continue
                if not exists(clean) and clean not in broken:
                    broken.append(clean)
        for clean in sorted(broken):
            warnings.append("%s cites `%s`, which is not on disk" % (name, clean))

    if n_rules is not None and name in ASSERT:
        for figure, what in COUNT.findall(text):
            if int(figure) != n_rules:
                warnings.append("%s says \"%s %s\" and there are %d cards in rules/"
                                % (name, figure, what, n_rules))

    if not any(name.startswith(x) or name == x for x in NO_R37):
        m = CHANGELOG_HEADING.search(text)
        if m:
            warnings.append("%s carries its own change log (\"%s\"): R37 says the why "
                            "lives in git and in the task log, not in the file"
                            % (name, m.group(0).lstrip("# ").strip()))

    return warnings


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        event = {}

    # A Stop hook that returns additionalContext calls the model again, which stops
    # again, and the hook fires once more: a loop. The harness flags that it already
    # comes from a stop with `stop_hook_active`, and then this goes quiet.
    if event.get("stop_hook_active"):
        sys.exit(0)

    n = how_many_rules()

    def exists(r):
        abs_ = os.path.join(ROOT, r)
        if os.path.exists(abs_):
            return True
        # A file name with spaces gets cut at the first word. If the parent folder
        # holds something starting like that, it counts.
        parent, base = os.path.split(abs_)
        try:
            return any(f.startswith(base) for f in os.listdir(parent))
        except OSError:
            return False

    scripts = {os.path.basename(r) for r in common.files(ROOT, ".py")}

    warnings = []
    for path in markdowns():
        try:
            text = io.open(path, encoding="utf-8").read()
        except Exception:
            continue
        warnings += review(text, rel(path), exists, n, scripts)

    if warnings:
        common.record(warnings, "coherence")
        message = ("Coherence: %d things do not add up.\n%s"
                   % (len(warnings), "\n".join("- " + a for a in warnings[:20])))
        # On Stop, what goes to stderr with exit code 0 never reaches the model:
        # it has to travel as additionalContext.
        print(json.dumps({
            "systemMessage": message,
            "hookSpecificOutput": {
                "hookEventName": "Stop",
                "additionalContext": message,
            },
        }))
    sys.exit(0)


def selftest():
    """What is proved is the PROPERTY, not the mechanics: that every real defect is
    caught and that correct text does not fire."""
    # The folders that DO exist in this fixture. Naming them matters: a top-level
    # folder that is absent means "not set up yet", and its contents are excused.
    has = lambda r: r in ("rules/R01_calculations_in_python.md", "MEMORY.md",
                          "rules", "Knowledge", "Documents", "Deliverables",
                          "Proposals", "Calculations")

    # 1. A broken path, the defect that repeats most.
    a = review("see [x](rules/R99_missing.md)", "t.md", has, None)
    assert len(a) == 1 and "not on disk" in a[0], a

    # 2. A good path: not one warning.
    assert review("see `MEMORY.md` and rules/R01_calculations_in_python.md",
                  "t.md", has, None) == []

    # 3. A count that contradicts what is on disk.
    a = review("The 32 rules are indexed here.", "CLAUDE.md", has, 36)
    assert len(a) == 1 and "36 cards" in a[0], a
    assert review("The 36 rules.", "CLAUDE.md", has, 36) == []
    # With no number written there is nothing to contradict: that is the right shape.
    assert review("The rules are indexed here.", "CLAUDE.md", has, 36) == []

    # 4. R37: a change log inside a working file.
    a = review("# Workflow\n\n## Change log\n\n- v1", "WORKFLOW.md", has, None)
    assert len(a) == 1 and "R37" in a[0], a
    # ...and the same text where the history IS the content.
    assert review("## Change log\n- v1", "Knowledge/archive/WORKFLOW_HISTORY.md",
                  has, None) == []
    assert review("## Change log\n- v1", "HANDOFF.md", has, None) == []

    # 5. A placeholder is not a broken path, and neither is a glob. The glob case
    #    is real: a cap table row reads `.claude/skills/*/SKILL.md`, and the star
    #    sits in the middle, so testing only the end of the path missed it.
    assert review("it is saved in Documents/<Task>/ and in Deliverables/<Task>/",
                  "t.md", has, None) == []
    assert review("| `.claude/skills/*/SKILL.md` | 500 |", "WORKFLOW.md", has, None) == []

    # 6. A dated report is frozen: its dead path is history, not a defect.
    broken = "see rules/R99_missing.md"
    assert review(broken, "Knowledge/REPORT_2026-08-06.md", has, None) == []
    # ...but a live card and the index are not, and they must warn.
    assert len(review(broken, "rules/R01_calculations_in_python.md", has, None)) == 1
    assert len(review(broken, "Knowledge/KNOWLEDGE.md", has, None)) == 1

    # 7. A script that is not in the repository, named without a folder in front.
    scripts = {"line_caps.py", "the_gate.py"}
    a = review("checked by `caps_and_rules.py`", "rules/R12_x.md", has, None, scripts)
    assert len(a) == 1 and "no script" in a[0], a
    assert review("checked by `line_caps.py`", "rules/R12_x.md", has, None, scripts) == []

    # 8. A line that proposes asserts nothing, so its path need not exist yet.
    item = "13. Spreadsheet, copy in `Deliverables/Handover/`"
    assert review("- [ ] " + item, "HANDOFF.md", has, None) == []
    # ...and ticking it demands the path again, which is when it should be demanded.
    a = review("- [x] " + item, "HANDOFF.md", has, None)
    assert len(a) == 1 and "Deliverables/Handover" in a[0], a
    # A proposal describes what does not exist yet: if it did, it would be pointless.
    assert review("a log in Calculations/telemetry/warnings.log",
                  "Proposals/P15_x.md", has, None) == []
    # And an unticked item does not shield the rest of the file, only its own line.
    a = review("- [ ] 1. see Deliverables/Handover/\nAlso Documents/Missing/x.md",
               "HANDOFF.md", has, None)
    assert len(a) == 1 and "Documents/Missing" in a[0], a

    # 9. A work folder that does not exist yet is not a broken link. This is the
    #    state a fresh clone ships in, and it produced seventeen warnings.
    fresh = lambda r: r in ("rules/R01_calculations_in_python.md", "MEMORY.md", "rules")
    assert review("the log lives in Documents/TASKS.md", "CLAUDE.md", fresh, None) == []
    # ...but once the folder exists, its contents are demanded again.
    set_up = lambda r: fresh(r) or r == "Documents"
    a = review("the log lives in Documents/TASKS.md", "CLAUDE.md", set_up, None)
    assert len(a) == 1 and "Documents/TASKS.md" in a[0], a
    # And .claude/ ships in the repository, so it is never excused.
    a = review("run `.claude/hooks/missing.py`", "CLAUDE.md", fresh, None)
    assert len(a) == 1 and "hooks/missing.py" in a[0], a

    print("coherence --selftest: 23 checks OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()

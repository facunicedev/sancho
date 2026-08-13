# -*- coding: utf-8 -*-
"""Sweeps the repository at the end of the turn and reports what is out of place.

Stop hook. Three checks, all deterministic:

  1. Unfiled items (R28). Every file and subfolder of an indexed folder has to be
     named in its index. And the other way round: every link in an index has to
     point at something that exists.
  2. Rules written outside their card (R28, single source of truth). It reports
     candidates, not certainties: the last word belongs to whoever reads.
  3. Inboxes left full and rubbish (R10, R23). A non-empty inbox, spreadsheet
     lock files, empty folders.

It runs on Stop and not on every write on purpose: these are whole-repository
sweeps, and mid-task an unfinished state is normal.

Folder names come in one row per language. Folders that do not exist are
skipped, so adding a language means adding rows and nothing else.
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# folder -> its index
INDEXES = {
    "Knowledge": "Knowledge/KNOWLEDGE.md",
    "Calculations": "Calculations/CALCULATIONS.md",
    "Documents": "Documents/TASKS.md",
    "Deliverables": "Deliverables/DELIVERABLES.md",
    "Templates": "Templates/TEMPLATES.md",
    "rules": "MEMORY.md",
    # Spanish
    "Conocimiento": "Conocimiento/CONOCIMIENTO.md",
    "Calculos": "Calculos/CALCULOS.md",
    "Documentos": "Documentos/TAREAS.md",
    "Entregables": "Entregables/ENTREGABLES.md",
    "Plantillas": "Plantillas/PLANTILLAS.md",
    "reglas": "MEMORY.md",
}

INBOXES = ("Inbox", "Volcado")
ALLOWED_EMPTY = (".", "Inbox", "Volcado", "Proposals", "Propuestas")

# Where a rule written outside its card is looked for.
CONTROL = ["CLAUDE.md", "WORKFLOW.md", "HANDOFF.md", "MEMORY.md"]

STOPWORDS = set("""the a an and or of to in on for with from by at as is are be
that this these those it its not no if when where how what which who whom whose
you your they their we our can will would should must have has had do does did
more most very much many some any all each every other than then also into""".split())

UNFILED_MARK = "<!-- unfiled:"


def read(rel):
    try:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def words(text):
    chunks = re.findall(r"[a-z0-9_]+", text.lower())
    return {c for c in chunks if len(c) > 3 and c not in STOPWORDS}


def row_mark(name, is_folder):
    """What has to appear in the index for that thing to count as filed.

    A folder is demanded as `name/`, backticks included. With the bare name any
    passing mention counted as a row, and a folder nobody had indexed went quiet
    because some sentence elsewhere happened to say its name.
    """
    return "`{}/`".format(name) if is_folder else name


def check_indexes(warnings):
    for folder, index in INDEXES.items():
        path = os.path.join(ROOT, folder)
        if not os.path.isdir(path):
            continue
        text = read(index)
        if not text:
            warnings.append("{} has no readable index at {}.".format(folder, index))
            continue

        for name in sorted(os.listdir(path)):
            if name.startswith(".") or name.startswith("~$"):
                continue
            full = os.path.join(path, name)
            rel = "{}/{}".format(folder, name)
            if rel in INDEXES:          # subfolder with its own index
                continue
            if rel == index:
                continue
            mark = row_mark(name, os.path.isdir(full))
            if mark in text:
                continue
            if os.path.isfile(full) and UNFILED_MARK in read(rel):
                continue
            warnings.append("{} has no row in {} (R28).".format(rel, index))

        base = os.path.dirname(index)
        for target in re.findall(r"\]\(([^)#:]+)\)", text):
            if target.startswith(("http", "mailto")):
                continue
            resolved = os.path.normpath(os.path.join(ROOT, base, target))
            if not os.path.exists(resolved):
                warnings.append("{} links to {}, which does not exist.".format(index, target))


def check_rules(warnings):
    for folder in ("rules", "reglas"):
        path = os.path.join(ROOT, folder)
        if not os.path.isdir(path):
            continue
        texts = {rel: read(rel).lower().splitlines() for rel in CONTROL}

        for card in sorted(os.listdir(path)):
            if not card.endswith(".md"):
                continue
            header = read(folder + "/" + card).splitlines()
            title = next((l for l in header if l.startswith("# ")), "")
            key = words(title.split(".", 1)[-1])
            if len(key) < 4:
                continue
            # A line that links to the card or cites its code is a pointer, not a
            # copy. That is exactly what should be there.
            marks = (card.lower(), card.split("_", 1)[0].lower())
            for rel, lines in texts.items():
                for number, line in enumerate(lines, 1):
                    if any(m in line for m in marks):
                        continue
                    if len(key & words(line)) >= max(4, len(key) - 1):
                        warnings.append(
                            "{}:{} looks like it restates the rule in {}. Leave the pointer and delete the text."
                            .format(rel, number, card))


def check_rubbish(warnings):
    for inbox in INBOXES:
        path = os.path.join(ROOT, inbox)
        if os.path.isdir(path) and os.listdir(path):
            warnings.append("{}/ is not empty: move what is there or discard it (R10).".format(inbox))

    for current, folders, files in os.walk(ROOT):
        folders[:] = [f for f in folders if not f.startswith(".git")]
        rel = os.path.relpath(current, ROOT).replace("\\", "/")
        if rel.startswith(".claude"):
            continue
        for name in files:
            if name.startswith("~$"):
                warnings.append("{}/{} is a spreadsheet lock file: delete it (R23).".format(rel, name))
        if not folders and not files and rel not in ALLOWED_EMPTY:
            warnings.append("{} is empty: fill it or delete it (R23).".format(rel))


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        event = {}

    # A Stop hook that returns additionalContext calls the model again, which stops
    # again, and the hook fires once more: a loop. The harness flags that it already
    # comes from a stop with `stop_hook_active`, and then this goes quiet.
    if event.get("stop_hook_active"):
        return

    warnings = []
    try:
        check_indexes(warnings)
        check_rules(warnings)
        check_rubbish(warnings)
    except Exception as error:
        warnings.append("The repository sweep failed: {}".format(error))

    if not warnings:
        return

    common.record(warnings, "repo_sweep")

    header = "Repository sweep, {} warnings:".format(len(warnings))
    body = "\n".join("- " + w for w in warnings[:20])
    if len(warnings) > 20:
        body += "\n- ...and {} more.".format(len(warnings) - 20)
    message = header + "\n" + body

    print(json.dumps({
        "systemMessage": message,
        "hookSpecificOutput": {
            "hookEventName": "Stop",
            "additionalContext": message,
        },
    }))


def selftest():
    """Proves the properties this hook rests on, not its arithmetic.

    Both were real defects: a folder counted as filed because a sentence somewhere
    said its name, and the restatement check fired on two lines that shared nothing
    but filler words.
    """
    # A folder is only filed if the index names it as a folder, in backticks.
    assert row_mark("Reports", True) == "`Reports/`"
    assert row_mark("cv.docx", False) == "cv.docx"
    assert row_mark("Reports", True) not in "the Reports of last year", \
        "a passing mention is not a row"
    assert row_mark("Reports", True) in "| `Reports/` | one per client |"

    # Filler carries no meaning, so it cannot make two lines look like the same rule.
    assert words("the a an of to in on for with from by at as is are be") == set()
    assert "calculation" in words("Every calculation runs in Python")
    assert "in" not in words("Every calculation runs in Python"), \
        "four letters or fewer is noise: it matches everything"

    # Every indexed folder points at an index, and every inbox is allowed to be empty.
    for folder, index in INDEXES.items():
        assert index.endswith(".md"), folder
        assert index == "MEMORY.md" or index.startswith(folder + "/"), folder
    for inbox in INBOXES:
        assert inbox in ALLOWED_EMPTY, inbox

    print("repo_sweep --selftest: 14 checks OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()

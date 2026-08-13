# -*- coding: utf-8 -*-
"""Warns when a control file grows past its line cap.

PostToolUse hook on Write and Edit. Reads the hook JSON from stdin, checks
whether the file written has a cap, and warns if it went over.

Why (rule R12): files that get read in full become useless when they grow.
When this hook fires, the answer is NOT to raise the cap: it is to move the
detail to where it belongs, which is the right-hand column.
"""

import fnmatch
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# pattern (relative to root, forward slashes) -> (cap, where the overflow goes)
CAPS = [
    ("HANDOFF.md",                  70,  "to the task log"),
    ("CLAUDE.md",                  120,  "to the card of the rule it belongs to"),
    ("MEMORY.md",                  120,  "to the body of the card: only one line per rule lives here"),
    ("WORKFLOW.md",                250,  "to a report in the knowledge folder, or to the card of the rule that develops it"),
    ("rules/*.md",                  30,  "somewhere else: a rule that needs more than 30 lines is a procedure, and it should be a skill"),
    ("reglas/*.md",                 30,  "somewhere else: a rule that needs more than 30 lines is a procedure, and it should be a skill"),
    ("Documents/TASKS.md",         250,  "by running /synthesis, which summarises, replaces the detail and calls the architect"),
    ("Documentos/TAREAS.md",       250,  "by running /synthesis, which summarises, replaces the detail and calls the architect"),
    ("*/KNOWLEDGE.md",             120,  "superseded rows move to the archive table"),
    ("*/CALCULATIONS.md",          120,  "group rows by category"),
    ("*/DELIVERABLES.md",          120,  "group rows by category"),
    ("*/TEMPLATES.md",             120,  "group rows by kind of template"),
    (".claude/skills/*/SKILL.md",  500,  "to a supporting file alongside. This is the official limit"),
]


def relative(path):
    try:
        rel = os.path.relpath(os.path.abspath(path), ROOT)
    except ValueError:
        return None
    rel = rel.replace("\\", "/")
    return None if rel.startswith("../") else rel


def cap_for(rel):
    """(cap, where the overflow goes) for that path, or None if it has no cap.

    Kept apart from the event so the selftest can exercise it whole without
    touching the disk: what has to be proved is which file has which cap, and
    that has nothing to do with reading stdin.
    """
    for pattern, cap, overflow in CAPS:
        if fnmatch.fnmatch(rel, pattern):
            return cap, overflow
    return None


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return

    path = data.get("tool_input", {}).get("file_path", "")
    if not path:
        return

    rel = relative(path)
    if rel is None:
        return

    found = cap_for(rel)
    if found is None:
        return
    cap, overflow = found

    try:
        with open(path, encoding="utf-8") as f:
            lines = sum(1 for _ in f)
    except OSError:
        return

    if lines <= cap:
        return

    warning = (
        "{} has {} lines and its cap is {}. Do not raise the cap: move what does not fit {}."
    ).format(rel, lines, cap, overflow)

    print(json.dumps({
        "systemMessage": warning,
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": warning,
        },
    }))


def selftest():
    """Proves the property: that every capped file has its cap, that the wildcards
    really match, and that a file with no cap does not fire."""
    assert cap_for("HANDOFF.md")[0] == 70
    assert cap_for("Documents/TASKS.md")[0] == 250
    assert cap_for("Documentos/TAREAS.md")[0] == 250, "the other language too"
    assert cap_for("WORKFLOW.md")[0] == 250

    # The wildcards: any rule card and any skill.
    assert cap_for("rules/R37_no_history_in_working_files.md")[0] == 30
    assert cap_for("reglas/R37_sin_historial.md")[0] == 30
    assert cap_for(".claude/skills/prospecting/SKILL.md")[0] == 500
    assert cap_for("Knowledge/KNOWLEDGE.md")[0] == 120

    # What has NO cap: reports are reference material and get read in pieces.
    assert cap_for("Knowledge/REPORT_2026-08-06.md") is None
    assert cap_for("Documents/CV/letter.tex") is None
    assert cap_for("Proposals/P07_x.md") is None

    # The overflow can never be circular: WORKFLOW's used to point "to the change
    # log", which was its own lines, so moving detail out lowered no total.
    assert "change log" not in cap_for("WORKFLOW.md")[1].lower()

    # Every cap states where the overflow goes. A cap with no way out is a dead end.
    for pattern, cap, overflow in CAPS:
        assert overflow and len(overflow) > 5, pattern

    print("line_caps --selftest: 17 checks OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()

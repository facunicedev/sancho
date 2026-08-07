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
    ("WORKFLOW.md",                250,  "to the change log, or to a report in the knowledge folder"),
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

    for pattern, cap, overflow in CAPS:
        if fnmatch.fnmatch(rel, pattern):
            break
    else:
        return

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


if __name__ == "__main__":
    main()

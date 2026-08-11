# -*- coding: utf-8 -*-
"""Stops the main thread from researching instead of delegating to the `researcher`.

PreToolUse hook on WebSearch|WebFetch.

HOW IT DECIDES, AND THIS IS THE POINT: by IDENTITY, not by memory and not by a
counter. The harness only fills agent_type and agent_id when the call is born
INSIDE a subagent. If they are absent, the search belongs to the main thread. The
proof is put there by the event itself, so there is no intermediate file the model
could write to walk around the gate.

An earlier version of this idea elsewhere used a counter of live researchers on
disk. Its own audit took it apart: the count leaks when an agent dies on an API
error, and an integer cannot tell instances apart. The payload already held the answer.

THE NUANCE: not every search is research. Checking a shop's opening hours is not.
So the first search from the main thread passes with a warning and the second does
not: if two are needed, it is research and it belongs to the agent (R06, R32).

    python .claude/hooks/research_guard.py --selftest
"""

import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATE = os.path.join(ROOT, ".claude", "state")
COUNT = os.path.join(STATE, "searches.json")

COURTESY = 1  # loose searches the main thread may run per session

MESSAGE = (
    "Research belongs to the researcher agent, not to you (R06, R32).\n"
    "This would be search %d from the main thread this session: the first passes,\n"
    "the rest do not. Two searches in a row are already research.\n"
    "Launch it with the Agent tool, subagent_type researcher, with the topic, the\n"
    "shape of the answer and the limits. It returns the report with its sources."
)


def is_subagent(event):
    """The only source of truth about who is calling. It cannot be forged from here."""
    for key in ("agent_type", "agent_id", "subagent_type"):
        if event.get(key):
            return True
    return False


def decide(event, previous):
    """(code, message). 0 passes, 2 blocks. `previous` is how many searches the main
    thread already ran this session."""
    if event.get("tool_name") not in ("WebSearch", "WebFetch"):
        return 0, ""
    if is_subagent(event):
        return 0, ""
    if previous < COURTESY:
        return 0, ""
    return 2, MESSAGE % (previous + 1)


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        return

    session = event.get("session_id", "?")
    try:
        data = json.load(io.open(COUNT, encoding="utf-8"))
    except Exception:
        data = {}
    previous = data.get(session, 0)

    code, message = decide(event, previous)

    if code == 2:
        print(message, file=sys.stderr)
        sys.exit(2)

    if event.get("tool_name") in ("WebSearch", "WebFetch") and not is_subagent(event):
        try:
            os.makedirs(STATE, exist_ok=True)
            # Only the current session: the file does not grow and carries no stale state.
            io.open(COUNT, "w", encoding="utf-8").write(
                json.dumps({session: previous + 1}, ensure_ascii=False))
        except Exception:
            pass
        print("Loose search allowed (%d of %d). The next one belongs to the "
              "researcher." % (previous + 1, COURTESY), file=sys.stderr)


def selftest():
    """Proves THE SECURITY PROPERTY, not the arithmetic of the counter. That is the
    expensive lesson: a selftest can check that a counter goes up and down correctly
    while the property that matters is broken."""
    sub = {"tool_name": "WebSearch", "agent_type": "researcher", "agent_id": "abc"}
    thread = {"tool_name": "WebSearch"}

    # The property: a subagent can ALWAYS search, however many it has run.
    assert decide(sub, 0)[0] == 0
    assert decide(sub, 99)[0] == 0

    # The property: the main thread cannot research.
    assert decide(thread, 0)[0] == 0, "the first one is courtesy"
    assert decide(thread, 1)[0] == 2, "the second is already research"
    assert decide(thread, 5)[0] == 2

    # Only agent_id, no agent_type: still a subagent.
    assert decide({"tool_name": "WebFetch", "agent_id": "x"}, 9)[0] == 0
    # A key that is present but empty accredits nobody.
    assert decide({"tool_name": "WebSearch", "agent_type": ""}, 3)[0] == 2

    # Other tools are left alone.
    assert decide({"tool_name": "Read"}, 9)[0] == 0
    assert decide({"tool_name": "Bash"}, 9)[0] == 0

    # The block says how to comply, not just no.
    assert "researcher" in decide(thread, 3)[1]

    print("research_guard --selftest: 10 checks OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()

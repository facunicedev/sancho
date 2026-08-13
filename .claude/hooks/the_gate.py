# -*- coding: utf-8 -*-
"""The gate: nothing gets produced without a checklist the person has frozen.

Three modes, three different events:

  --sign             UserPromptSubmit. The ONLY writer of the signature file.
  --before-writing   PreToolUse Write|Edit. Blocks producing without a signed checklist.
  --next             Stop. States the next mandatory step.

WHY IT IS BUILT THIS WAY. The obvious version of this idea is a gate that opens the
task log and the handoff and checks there is an entry for today. Those two files are
written by the model, so that is not a gate: it is asking the model to type the
answer before carrying on. In a real audit of a sibling harness, an orchestrator
signed off its own phase, and seven seconds passed between the block and the forgery.

Hence the test: the proof comes from something the model cannot manufacture. A
message from the person. `--sign` is the only mode that writes into .claude/state/,
and `--before-writing` forbids the model from writing there. The list is the model's;
freezing it is theirs.

    python .claude/hooks/the_gate.py --selftest
"""

import hashlib
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATE = os.path.join(ROOT, ".claude", "state")
SIGNATURE = os.path.join(STATE, "frozen_checklist.md")
HANDOFF = os.path.join(ROOT, "HANDOFF.md")
CONFIG = os.path.join(ROOT, "sancho.md")

# Where produced work lives. Writing here needs a frozen checklist. One row per
# language, like the other hooks: a folder that does not exist never matches.
PRODUCTION = ("Documents/", "Calculations/", "Deliverables/", "Templates/",
              "Documentos/", "Calculos/", "Entregables/", "Plantillas/")

# What is never blocked, or the gate bites its own tail: these are the files the
# task is PREPARED with, plus the inbox and the proposals.
FREE = ("HANDOFF.md", "MEMORY.md", "CLAUDE.md", "WORKFLOW.md",
        "Documents/TASKS.md", "Inbox/", "Proposals/", "Knowledge/", "rules/",
        "Documentos/TAREAS.md", "Volcado/", "Propuestas/", "Conocimiento/",
        "reglas/", ".claude/")

# Signing is a command, not a phrase. Guessing whether a message approved or not
# cost two blocks with the approval sitting right there: "I approve 21 / do not do
# anything yet" read as a refusal, and so did a sentence whose second clause began
# with a preposition. A command has no such problem: either it opens the message or
# it does not, and the person types it.
SIGN_CMD = re.compile(r"^\s*/?(sign)\b", re.IGNORECASE)


def relative(path):
    try:
        rel = os.path.relpath(os.path.abspath(path), ROOT).replace("\\", "/")
    except ValueError:
        return None
    return None if rel.startswith("../") else rel


def approves(message):
    """True if the message opens with the signing command, `/sign`.

    The rest of the message does not matter: it may ask for changes, add a nuance
    or carry on talking. Nothing is interpreted here, and interpreting is what failed."""
    return bool(SIGN_CMD.match(message or ""))


def has_checklist(text):
    """A checklist exists if there is at least one item, ticked or not."""
    return bool(re.search(r"^\s*-\s*\[[ xX]\]", text or "", re.MULTILINE))


def fingerprint(text):
    """Identifies THE CHECKLIST, not its state. It keeps each item's wording and
    throws the box away, so ticking off work does not void the signature but
    changing the list does.

    It exists because of a real hole: a first version only checked whether the
    signature file was there, and nothing ever deleted it. Sign one task and the
    gate stayed open for every other. A gate that opens once and stays open is not
    a gate.
    """
    items = re.findall(r"^\s*-\s*\[[ xX]\]\s*(.+?)\s*$", text or "", re.MULTILINE)
    return hashlib.sha1("\n".join(items).encode("utf-8")).hexdigest()[:16]


def is_subagent(event):
    """True if the one writing is a subagent. The program says so, not the model.

    A subagent ALWAYS runs in another session, so no signature of its own can ever
    exist: `signature_valid` compares the session id and it never matches. The
    signal that can be checked is where its transcript lives, which Claude Code
    keeps in `<session>/subagents/agent-*.jsonl`.
    """
    if event.get("isSidechain"):
        return True
    return "/subagents/" in (event.get("transcript_path") or "").replace("\\", "/")


def decide_write(rel_path, already_signed, configured=True, subagent=False):
    """(code, message). 0 passes, 2 blocks."""
    if rel_path is None:
        return 0, ""
    # First run. The language question was written in CLAUDE.md as prose and prose
    # is not a gate: on a real first run the model created sancho.md by itself,
    # picked English and filled in a screenshots path nobody had given it. The
    # answer names the folders on disk, so guessing it wrong is not a wrong reply,
    # it is a repository built on the wrong labels.
    if not configured and rel_path != "sancho.md":
        return 2, (
            "First run: sancho.md does not exist, so the language is not settled yet.\n"
            "You were about to write in %s\n"
            "Ask ONE question and nothing else, then stop and wait for the answer:\n"
            "  In which language should I work? I will speak it, name the folders in\n"
            "  it, and write every document in it.  1. English  2. Espanol  3. another\n"
            "Do not pick it yourself, do not infer it from what they typed, and do not\n"
            "create a single folder before they answer. Only sancho.md may be written\n"
            "first, with their answer in it (format in SETUP.md)." % rel_path)
    if rel_path.startswith(".claude/state/"):
        return 2, ("The signature file is written by its hook and by nobody else.\n"
                   "If the model could write there, the freeze would be the model's\n"
                   "and not theirs, and the gate would stop being a gate.")
    # A subagent is covered by the signature of the thread that launched it, which
    # already came through here. Asking it for one of its own leaves the architect
    # with nowhere to deliver, and a hook walked around by hand ends up removed.
    if subagent:
        return 0, ""
    for free in FREE:
        if rel_path == free or rel_path.startswith(free):
            return 0, ""
    if not any(rel_path.startswith(p) for p in PRODUCTION):
        return 0, ""
    if already_signed:
        return 0, ""
    return 2, (
        "No signed checklist, so producing is not due yet (WORKFLOW step 6).\n"
        "You were about to write in %s\n"
        "What is missing: log the task, write the checklist in HANDOFF.md saying who\n"
        "runs each item, put it to them short, and ask them to sign by typing /sign.\n"
        "There is no exception for size: not \"it is just a note\", not \"without all\n"
        "the fuss\", not \"this one is internal\"." % rel_path)


def signature_valid(stored, session, handoff_text):
    """A signature is good for ONE task and ONE session. It expires by itself the
    moment the checklist changes, which is what separates one task from the next."""
    if not stored:
        return False
    if stored.get("session") != session:
        return False
    return stored.get("fingerprint") == fingerprint(handoff_text)


def _stored():
    try:
        return json.load(io.open(SIGNATURE, encoding="utf-8"))
    except Exception:
        return None


def signed(session):
    """The session comes from the event, which is what really knows it."""
    try:
        text = io.open(HANDOFF, encoding="utf-8").read()
    except Exception:
        text = ""
    return signature_valid(_stored(), session, text)


FIRST_RUN_ASK = (
    "FIRST RUN. sancho.md does not exist, so the language is not settled.\n"
    "Before answering anything else, ask this and only this, then stop and wait:\n"
    "  In which language should I work? I will speak it, name the folders in it,\n"
    "  and write every document in it.  1. English  2. Espanol  3. another\n"
    "Do not pick it yourself. Do not infer it from the language they wrote in:\n"
    "someone types a one-word message in one language and works in another.\n"
    "Do not create a single folder, and do not start the task they asked for.\n"
    "When they answer, write sancho.md first (format in SETUP.md), then the folders.")


def mode_sign():
    """UserPromptSubmit. Two jobs, and the order matters.

    Signing is one. The other is the first run: what this hook prints on stdout
    reaches the model BEFORE it answers, and that is the only place an instruction
    can still change the reply. The gate on writes was not enough, and a real test
    proved it: the person typed a two-letter message, the model answered in prose
    without writing anything, and nothing had a chance to fire. A gate that only
    watches writes never sees a conversation.
    """
    try:
        event = json.load(sys.stdin)
    except Exception:
        return
    if not os.path.exists(CONFIG):
        print(FIRST_RUN_ASK)
        return
    if not approves(event.get("prompt", "")):
        return
    try:
        text = io.open(HANDOFF, encoding="utf-8").read()
    except Exception:
        return
    if not has_checklist(text):
        return
    try:
        os.makedirs(STATE, exist_ok=True)
        io.open(SIGNATURE, "w", encoding="utf-8").write(json.dumps({
            "session": event.get("session_id", ""),
            "fingerprint": fingerprint(text),
            "when": time.strftime("%Y-%m-%d %H:%M"),
        }, ensure_ascii=False, indent=1))
        print("Checklist signed. The production gate is open for THIS task: if the "
              "checklist changes, it has to be signed again.")
    except Exception:
        pass


def mode_write():
    try:
        event = json.load(sys.stdin)
    except Exception:
        return
    path = event.get("tool_input", {}).get("file_path", "")
    if not path:
        return
    code, message = decide_write(
        relative(path), signed(event.get("session_id", "")), os.path.exists(CONFIG),
        is_subagent(event))
    if code == 2:
        print(message, file=sys.stderr)
        sys.exit(2)


def next_step(handoff_text, has_signature, configured=True):
    """The next MANDATORY step, worked out from the state. A block with no way out
    turns into doing it by hand, which is how a sibling harness sank a whole run."""
    if not configured:
        return ("NEXT STEP: ask the language question and nothing else, then stop. "
                "Sancho does not run until sancho.md exists (SETUP.md).")
    if not has_checklist(handoff_text):
        return ("NEXT STEP: write the task checklist in HANDOFF.md, saying who runs "
                "each item (WORKFLOW step 4).")
    if not has_signature:
        return ("NEXT STEP: put it to them short and ask them to sign it with /sign "
                "(WORKFLOW step 6). Until then nothing gets written in the documents, "
                "calculations or deliverables folders.")
    pending = re.findall(r"^\s*-\s*\[ \]\s*(.+)$", handoff_text, re.MULTILINE)
    if pending:
        return "NEXT STEP: %s  (%d items left)" % (
            pending[0].strip()[:110], len(pending))
    return ("NEXT STEP: checklist complete. Time for the step 8 review, the final "
            "log entry and asking them to approve (R05).")


def mode_next():
    try:
        event = json.load(sys.stdin)
    except Exception:
        event = {}

    # See the comment in coherence.py: without this, the warning loops.
    if event.get("stop_hook_active"):
        sys.exit(0)

    try:
        text = io.open(HANDOFF, encoding="utf-8").read()
    except Exception:
        text = ""
    message = next_step(text, signed(event.get("session_id", "")),
                        os.path.exists(CONFIG))
    # Same as coherence.py: on Stop, stderr with exit code 0 never reaches the model.
    print(json.dumps({
        "systemMessage": message,
        "hookSpecificOutput": {
            "hookEventName": "Stop",
            "additionalContext": message,
        },
    }))
    sys.exit(0)


def selftest():
    """Proves the property: that nothing can be produced without their signature, and
    that the signature cannot be manufactured from the inside."""
    # The central property: no signature, no production.
    assert decide_write("Documents/CV/cv.tex", False)[0] == 2
    assert decide_write("Calculations/x/script.py", False)[0] == 2
    assert decide_write("Deliverables/X/final.docx", False)[0] == 2
    # ...and with a signature, yes.
    assert decide_write("Documents/CV/cv.tex", True)[0] == 0
    # The same in another language, because the folders are named in theirs.
    assert decide_write("Documentos/CV/cv.tex", False)[0] == 2
    assert decide_write("Entregables/X/final.docx", True)[0] == 0

    # The gate does not bite its own tail: what a task is PREPARED with never blocks.
    for free in ("HANDOFF.md", "Documents/TASKS.md", "Documentos/TAREAS.md",
                 "Inbox/note.txt", "Proposals/P09_x.md",
                 "rules/R01_calculations_in_python.md", ".claude/hooks/x.py"):
        assert decide_write(free, False)[0] == 0, free

    # And the model cannot write its own signature: that is what makes it worth
    # something. Not even a subagent, which is the one exemption below.
    assert decide_write(".claude/state/frozen_checklist.md", True)[0] == 2
    assert decide_write(".claude/state/frozen_checklist.md", True, subagent=True)[0] == 2

    # A SUBAGENT is covered by the signature of the thread that launched it. It runs
    # in another session, so a signature of its own can never exist and it was left
    # blocked with no way out: an architect report ended up outside the repository.
    assert decide_write("Documents/X/report.md", False, subagent=True)[0] == 0
    assert decide_write("Documents/X/report.md", False, subagent=False)[0] == 2, \
        "and the main thread without a signature is still blocked"
    # The mark comes from the program, not from the model: where the transcript
    # lives. `isSidechain` is not on the event, it is a field of the transcript.
    assert is_subagent({"transcript_path": "/p/9e8/subagents/agent-1.jsonl"})
    assert is_subagent({"transcript_path": r"C:\p\9e8\subagents\agent-1.jsonl"}), \
        "the separator is the platform's, and on Windows it is the other one"
    assert is_subagent({"isSidechain": True})
    assert not is_subagent({"transcript_path": "/p/9e8febd1.jsonl"})
    assert not is_subagent({}), "with no mark it is the main thread, which is stricter"

    # The block says how to comply.
    assert "HANDOFF.md" in decide_write("Documents/x/y.docx", False)[1]

    # Signing is a command and is not interpreted. What follows does not matter:
    # those two sentences are the ones that blocked with the approval sitting there
    # back when this was guessed.
    assert approves("/sign") and approves("sign")
    assert approves("/sign but do not touch point 3 yet")
    assert approves("/sign, and I want a general solution for this kind of thing")
    assert not approves("I approve"), "approving in words no longer signs: /sign is typed"
    assert not approves("")
    assert not approves("I need you to research the coffee market")
    assert not approves("I will not sign this"), "the command opens the message, not the middle"

    # FIRST RUN. Until sancho.md exists nothing at all may be written, not even the
    # files that are otherwise free: the language names the folders, so starting
    # before the answer builds the repository on the wrong labels. This is here and
    # not in CLAUDE.md because on a real first run the model read that prose, chose
    # English on its own and filled in a screenshots path nobody had given it.
    for anything in ("HANDOFF.md", "rules/R01_x.md", "Inbox/note.txt",
                     "Documents/TASKS.md", ".claude/hooks/x.py"):
        assert decide_write(anything, True, configured=False)[0] == 2, anything
    # ...except sancho.md itself, or the answer could never be written down.
    assert decide_write("sancho.md", False, configured=False)[0] == 0
    # The block asks the question instead of just refusing.
    assert "language" in decide_write("HANDOFF.md", True, configured=False)[1]
    # And once it exists, the gate goes back to being about the checklist.
    assert decide_write("HANDOFF.md", False, configured=True)[0] == 0
    assert "language" in next_step("- [x] one", True, configured=False)
    # And the question reaches the model BEFORE it answers, which is the only
    # moment that can still change the reply. Blocking writes was not enough: the
    # first real test was a two-letter message answered in prose, with no write to
    # block. The text has to name what not to do, or "es" gets read as the answer.
    assert "1. English" in FIRST_RUN_ASK and "Espanol" in FIRST_RUN_ASK
    assert "infer it from the language they wrote in" in FIRST_RUN_ASK
    assert "do not start the task" in FIRST_RUN_ASK

    # The next step comes from the state, not from what anyone remembers.
    assert "checklist" in next_step("nothing here", False)
    assert "/sign" in next_step("- [ ] one", False)
    assert "one" in next_step("- [ ] one\n- [ ] two", True)
    assert "R05" in next_step("- [x] one", True)

    # A signature is good for ONE task and ONE session. Without this, signing once
    # opened the gate forever.
    items = "- [ ] one\n- [ ] two"
    good = {"session": "s1", "fingerprint": fingerprint(items)}
    assert signature_valid(good, "s1", items)
    # Ticking work off does NOT void it: that changes the box, not the list.
    assert signature_valid(good, "s1", "- [x] one\n- [ ] two")
    # Another task, another checklist: it expires by itself.
    assert not signature_valid(good, "s1", "- [ ] something else entirely")
    # Another session: no good.
    assert not signature_valid(good, "s2", items)
    # No signature: no good.
    assert not signature_valid(None, "s1", items)
    # And an extended checklist is no good either: adding an item means saying so.
    assert not signature_valid(good, "s1", items + "\n- [ ] three")

    print("the_gate --selftest: 49 checks OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    elif "--sign" in sys.argv:
        mode_sign()
    elif "--before-writing" in sys.argv:
        mode_write()
    elif "--next" in sys.argv:
        mode_next()

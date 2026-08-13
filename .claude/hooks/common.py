"""What the hooks that walk the repository share.

**A hook only watches what belongs to the repository.** What git ignores does not:
it is working material, a backup, a downloaded source. Watching it produces warnings
about sentences nobody here wrote, and it forces reading megabytes that do not matter.

Who decides what belongs to the repository is git, not a list of names typed by hand
inside a hook. That list goes stale the day a new folder appears, and then someone has
to remember to edit every hook. Here we ask git.

    python common.py --selftest
"""
import datetime
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ALWAYS_OUT = (".git", "__pycache__", "node_modules")

# Under .claude/ and not in a work folder on purpose: the work folders are named in
# the working language and do not exist until the first run, so writing there would
# invent a folder with no index and no name of its own.
LOG = os.path.join(".claude", "state", "warnings.log")


def ignored(paths, root=ROOT):
    """Which of these paths git ignores. One call for all of them.

    If git is missing or fails, returns the empty set: the hook keeps watching too
    much, which is the cheap failure. Going quiet would be the expensive one."""
    if not paths:
        return set()
    # In bytes and null-separated on purpose: on Windows text mode turns every
    # newline into \r\n and git receives paths ending in \r, which match nothing.
    # With -z it also stops quoting the answer when a path contains something odd.
    try:
        p = subprocess.run(["git", "check-ignore", "-z", "--stdin"],
                           cwd=root, input=b"\0".join(r.encode("utf-8") for r in paths),
                           capture_output=True, timeout=20)
    except Exception:
        return set()
    return {t.decode("utf-8", "replace").replace("\\", "/")
            for t in p.stdout.split(b"\0") if t}


def files(root=ROOT, extension=None):
    """The repository's files, as absolute paths, minus what git ignores.

    `extension` filters by suffix, for example ".md"."""
    found = []
    for base, folders, names in os.walk(root):
        folders[:] = [c for c in folders if c not in ALWAYS_OUT]
        for n in names:
            if extension is None or n.endswith(extension):
                found.append(os.path.join(base, n))
    out = ignored([os.path.relpath(r, root).replace("\\", "/") for r in found], root)
    return [r for r in found
            if os.path.relpath(r, root).replace("\\", "/") not in out]


def folders(root=ROOT):
    """The repository's folders, as relative slash paths, minus the ignored ones."""
    every = []
    for base, subs, _ in os.walk(root):
        subs[:] = [c for c in subs if c not in ALWAYS_OUT]
        for c in subs:
            every.append(os.path.relpath(os.path.join(base, c), root).replace("\\", "/"))
    out = ignored(every, root)
    return [c for c in every if c not in out
            and not any(c.startswith(f + "/") for f in out)]


def key(warning):
    """What identifies a warning underneath its figures and its names.

    The same chronic warning changes text every day because it carries the line
    count or the list of spare files inside it, so comparing the whole line never
    groups anything: every day looks like a new warning. Digit groups are dropped,
    the text is cut at the first colon and the first words are kept, which is the
    cheapest thing that tells one warning from another without telling its
    versions apart.
    """
    without_figures = re.sub(r"\d+", "#", " ".join((warning or "").split()))
    return " ".join(without_figures.split(":")[0].split()[:8])


def _log_path(root):
    return os.path.join(root, LOG)


def record(warnings, hook, root=ROOT, today=None):
    """Leaves a trace of the warnings, one per line, so chronic ones can be told apart.

    A warning only lives for the turn it is printed in, so fixing it depends on
    somebody watching the chat at that moment. And a single run cannot tell the
    warning that has been there for forty turns from the one that appeared five
    minutes ago: the hook reports the state now, not its history. Counting days
    turns "chronic" from an impression into a number.

    The same warning from the same hook is not repeated within the same day: what
    gets counted is distinct days, not turns, and that is what separates chronic
    from merely repeated.

    Never breaks its caller: a log that breaks the hook costs more than it is worth.
    Returns how many lines it added."""
    if not warnings:
        return 0
    day = today or datetime.date.today().isoformat()
    path = _log_path(root)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            already = set(io.open(path, encoding="utf-8").read().splitlines())
        except IOError:
            already = set()
        seen = set(tuple(l.split("\t")[:3]) for l in already)
        fresh = []
        for a in warnings:
            text = " ".join(a.split())
            k = key(text)
            if (day, hook, k) not in seen:
                seen.add((day, hook, k))
                fresh.append("\t".join((day, hook, k, text)))
        if fresh:
            with io.open(path, "a", encoding="utf-8") as fh:
                fh.write("".join(l + "\n" for l in fresh))
        return len(fresh)
    except Exception:
        return 0


def selftest():
    """What is proved is the property: git decides, not a list of names."""
    import tempfile, shutil
    d = tempfile.mkdtemp()
    try:
        subprocess.run(["git", "init", "-q"], cwd=d, check=True, capture_output=True)
        with open(os.path.join(d, ".gitignore"), "w") as fh:
            fh.write("material/\n*.tmp\n")
        os.makedirs(os.path.join(d, "material", "deep"))
        for r in ("visible.md", "material/hidden.md", "material/deep/deep.md", "loose.tmp"):
            open(os.path.join(d, r), "w").write("x")

        seen = {os.path.relpath(r, d).replace("\\", "/") for r in files(d)}
        assert "visible.md" in seen, "an ordinary file is watched"
        assert "material/hidden.md" not in seen, "what git ignores is not watched"
        assert "material/deep/deep.md" not in seen, "nor what hangs off an ignored folder"
        assert "loose.tmp" not in seen, "the pattern need not be a folder either"
        assert ".gitignore" in seen, "the .gitignore itself does belong to the repository"

        only_md = {os.path.relpath(r, d).replace("\\", "/") for r in files(d, ".md")}
        assert only_md == {"visible.md"}, "the extension filter works"

        assert "material" not in folders(d), "an ignored folder is not listed"
        assert "material/deep" not in folders(d), "nor its child"

        # The property that matters: the ignored folder's name comes from that
        # repository's .gitignore, and this module does not know it. Proved by
        # changing it: with another name the result has to stay the same.
        with open(os.path.join(d, ".gitignore"), "w") as fh:
            fh.write("any_other_name/\n")
        os.rename(os.path.join(d, "material"), os.path.join(d, "any_other_name"))
        seen = {os.path.relpath(r, d).replace("\\", "/") for r in files(d)}
        assert not any(v.startswith("any_other_name/") for v in seen), \
            "the repository's .gitignore rules, not any name written in the hook"
        assert "loose.tmp" in seen, "and with its pattern gone, the file is watched again"

        # The log's property: what survives the turn is DAYS, not turns. The same
        # warning repeated today does not count twice; tomorrow it does, and that
        # is the whole difference between "chronic" and "repeated".
        assert record(["X is missing"], "sweep", d, "2026-08-10") == 1
        assert record(["X is missing"], "sweep", d, "2026-08-10") == 0, \
            "the same warning, the same day, is not written twice"
        assert record(["X is missing"], "sweep", d, "2026-08-11") == 1, \
            "another day does: counting days is what measures chronic"
        assert record(["X is missing"], "coherence", d, "2026-08-10") == 1, \
            "each hook keeps its own count"
        assert record([], "sweep", d, "2026-08-10") == 0, "no warnings, nothing written"
        lines = io.open(_log_path(d), encoding="utf-8").read().splitlines()
        assert len(lines) == 3 and all(l.count("\t") == 3 for l in lines), lines

        # The key's property: the same warning with different figures inside is ONE
        # warning. Comparing whole lines made every day look like a new one, and
        # then nothing was ever chronic.
        assert key("HANDOFF.md is at 71 lines of 70") == key("HANDOFF.md is at 84 lines of 70")
        assert key("3 loose files: a.md, b.md") == key("5 loose files: c.md")
        assert key("HANDOFF.md is at 71 lines of 70") != key("3 loose files: a.md, b.md")
        assert record(["HANDOFF.md is at 71 lines of 70"], "caps", d, "2026-08-12") == 1
        assert record(["HANDOFF.md is at 84 lines of 70"], "caps", d, "2026-08-12") == 0, \
            "the same warning with another figure is not a second warning"
        # And it never breaks the hook that calls it, even with an impossible target.
        assert record(["x"], "sweep", os.path.join(d, "visible.md")) == 0

        print("selftest: fine. Git decides what is watched, not a hand-written list.")
    finally:
        shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        print("{} files watched, {} of them .md".format(
            len(files()), len(files(extension=".md"))))

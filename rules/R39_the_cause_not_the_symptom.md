# R39. Fix the cause, not the symptom

**When something breaks, fix what causes it.** Excluding the case that bothers you by hand is not a fix: it postpones the problem until the next case, which will have nobody there to exclude it.

## Telling a patch from a fix

Two questions. One yes and it is a patch:

- **Does the fix name a specific case?** A folder, a file, a value. Then the real question is still unasked: who actually knows the answer. Ask them instead.
- **Will someone have to remember to touch this when a new case shows up?** Anything that depends on remembering has already failed.

## Where this came from

The coherence hook produced twenty false warnings because it was reading a folder of downloaded material. The patch was to exclude that folder by name. The fix was `.claude/hooks/common.py`: **git decides what belongs to the repository**, not a list written inside the hook. False warnings went from 20 to 0, and folders that do not exist yet are covered too.

## Not the same as R14

R14 uses the same word for the opposite thing: once they have edited a document by hand, you patch it instead of regenerating it. No conflict, different subjects. **R14 is about their deliverable; this one is about the harness code.**

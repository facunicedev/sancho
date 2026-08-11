# R40. What you ask them to sign gets summarised in the chat

**When you ask for `/sign`, the items being signed and the decisions being taken as settled go in the message itself.** The file stays the reference copy, but it does not replace the summary: "the checklist is in `HANDOFF.md`" is not asking for a signature, it is asking them to go and find one.

## What the message carries

- The checklist items, one line each. If there are many, grouped in blocks, but none left out.
- **The decisions being taken as settled without asking**, which are the ones that actually need seeing before signing.
- What was ruled out up front, if anything was.

## Why, and it is not politeness

A signature is a gate ([R05](R05_approval_to_close.md)). Signing something you have to open in another window is signing blind, and then the gate stops filtering: it approves the good checklist and the bad one alike. The summary costs ten lines; the unread signature costs a whole task run in the wrong direction.

It is the same defect [R37](R37_no_history_in_working_files.md) corrects elsewhere: **the information has to be where the decision is made**, not in the file that documents it.

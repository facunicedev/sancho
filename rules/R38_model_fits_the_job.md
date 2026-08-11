# R38. Every agent declares its model, and it is not always the biggest one

**An agent with no `model:` in its header inherits the caller's**, which is the biggest one. That makes the agent that only counts and formats cost the same as the one deciding what changes in the repository.

## Which one

Walk down the list and stop at the first that fits.

| If the work is | Model |
|---|---|
| Extracting, counting, formatting or transcribing against criteria already written down | **Haiku** |
| Reading a lot and summarising it faithfully, or searching outside and anchoring every claim | **Sonnet** |
| Deciding what changes, spotting what nobody asked you to look at, or writing for someone outside | **Opus** |

**When in doubt, the bigger of the two.** Redoing the work costs more than the difference between models.

**Skills do not pick a model.** A skill is instructions loaded into whoever invoked it, so it runs on their model. The choice lives in the agent's header, and in the `model` field when you launch a one-off agent.

## How it is checked

When you move an agent down a size, run it once with each model **on the same input** and compare the two outputs. If you cannot tell them apart, keep the smaller one. If you can, keep the bigger one and write down why in the task log (R37).

Same test that decides whether a piece is born at all: if it comes out the same with and without, it was not needed.

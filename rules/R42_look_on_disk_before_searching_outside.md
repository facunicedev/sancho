# R42. Before sending anyone to search outside, look on disk

**Before launching a research agent, a web search or a download, check whether it is already sitting in `Calculations/<task>/`.** Searching outside for what is already inside costs quota, costs time, and gives a worse answer than the one you had.

## And the source's cut-off goes next to the data

When the answer comes from a source with a cut-off — a portal that only publishes from a certain year, an interface with a window, a census with a closing date — **write that cut-off beside the data**. Without it a gap reads backwards: it looks like the thing does not exist when what happens is that the source does not reach that far.

## Where this came from

A task had one item planned as 39 separate investigations, one agent per company, to settle a contradiction: the registry said "no director on file" while the commercial listings did give names.

The answer was in a file **already downloaded**: the published records only start in 2009. An empty list of directors does not mean the company has no director, it means the director was appointed before the data begins. A local script settled it in one second, and **28 of the 39 were that same case**.

## And the path to another repository is also on disk

**Before writing into a folder that is not this project's, check the path in the code that defines it**, not in what you remember and not in what the name suggests. Reading it costs one `grep`.

Assuming which of two similar repositories was meant, seven files were edited in the wrong one. They were reverted whole, but **there was no damage by luck, not by care**: that repository happened to have no pending work. With work in progress inside, reverting would have destroyed it.

## How you check

- Before launching agents, say **which file on disk you looked at first** and what was not in it.
- Data from a source with a cut-off carries the cut-off written beside it, in the same note.
- The path to another repository appears **read from a file** in the conversation, never asserted.

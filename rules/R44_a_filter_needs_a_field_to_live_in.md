# R43. A filter with nowhere to store its answer filters nothing

**When a new discard criterion appears, the first thing to build is the field where the answer goes**, and only then apply it. If the answer lives only in the prose of the notes, no script can use it and every pass has to re-read the records by hand.

The field takes three values, not two: **yes, no, and "not found"**. A missing value never discards anything: discarding on a gap is what wrongly set aside 588 companies in one task.

## And the vocabulary is written by someone else

The field gets filled in by an agent, so **it is read by looking inside it, not by exact match**, and anything unrecognised is reported on screen. A misspelt field and an empty field are not the same thing and cannot score the same.

## Where this came from

The same failure three times in one task:

- A contact-type field written as `salesperson_with_name_and_email` instead of `person` left the best record on the list scoring **zero** for contactability, silently.
- A brands field written as `Kyocera (link to the proof)` instead of `Kyocera` left the strongest supplier, which carried all five brands, with an **empty cell in the deliverable**.
- And a wholesaler of cosmetics — where "toner" means a facial toner — sat for weeks in the review pile, indistinguishable from a real supplier with a half-filled record, because **no field existed** to hold the answer to "is this even in the trade?". The channel filter let it through: it does sell to the channel, only of cosmetics.

## How you check

- The field exists, and its `--selftest` proves that **empty and "not found" discard nobody**.
- Every discard the script applies **carries its reason written in the row**.
- Any value the script does not understand **is shown**, instead of quietly scoring zero.

## Same family

This is [R39](R39_the_cause_not_the_symptom.md) applied to data: excluding by hand the one record that bothers you postpones the problem until the next one. See also [R44](R45_setting_aside_is_not_mixing_back_in.md).

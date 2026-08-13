# R44. Setting something aside and then mixing it back in is not setting it aside

**When something is set aside to be looked at rather than thrown out, that "aside" has to be a place and not an intention.** It gets its own tier, its own sheet or its own list, it **can never rise to the top of the ranking**, and the row carries the reason written in the same column where the others say why they did not make it.

## Where this came from

On one task the decision was that a company selling to end customers **but moving real volume** should not be thrown out: set it aside and look at it. The decision was right and it was applied, but the script gave it no place of its own, so the set-aside ones flowed back into the normal ranking and were scored like everyone else.

The result was a retail shop **coming out in the second tier, with a blank reason, next to genuine wholesalers**. It sells with tax included, runs a loyalty scheme and has no volume brackets. Written like that, you write to it as if it were a wholesaler and find out from the reply.

And it happened again the same day somewhere else: records for companies with no domain of their own are named differently, and a counting script gave them up for lost. **A case set aside from the general pattern comes back as a bug if nobody gives it a place.**

## How you check

With `--selftest`, on the property:

- A set-aside row **never lands in the top tiers**, whatever it scores.
- And it **never comes out with an empty reason**: if it is set aside, the row says why.

## Same family

[R43](R44_a_filter_needs_a_field_to_live_in.md), from the same session, and [R39](R39_the_cause_not_the_symptom.md), which is where both come from.

# R13. Synthesis on a cadence, and the decision table with it

> **type:** rule - **status:** active - **default:** yes - **check:** the counter and the line cap

Every ten closed tasks, or whenever the task log passes its cap, a synthesis is written and the decision table is rebuilt whole. The synthesis **replaces** the detail it summarises when that detail is process; it **coexists** with it when the original carries figures, quotes or links.

**Why.** Without the replacing part, the log grows from both ends at once, summary and detail together.

**How.** Run `/synthesis`. It measures first, then writes, then calls the architect.

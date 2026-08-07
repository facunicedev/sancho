# R01. Every figure is computed by a script

> **type:** rule - **status:** active - **default:** yes - **check:** the script and its output exist

No number is worked out in your head or in prose. Every figure that reaches a document is produced by a script in `Calculations/<task>/`, and the document reads that output instead of retyping it.

**Why.** A language model is not a calculator, and a wrong figure in a report is found by the reader, not by you. Measured on a real case: a recomputation caught a report claiming 48 % where the correct value was 47 % (9 of 19).

**How.** Script and output live together, one subfolder per task. If a figure changes, the script is re-run, never the number edited by hand.

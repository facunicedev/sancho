# R29. If they will paste it somewhere, keep the original shape

> **type:** rule - **status:** active - **default:** yes - **check:** compare against the source file

When the output is going to be copied into another system, do not build a new table. Start from the original file and delete the rows that do not apply, keeping columns, order and styling. New columns go at the end.

**Why.** A rebuilt table does not paste. Columns land in the wrong place and the person redoes the work by hand.

**How.** Check for stray hyperlinks afterwards: spreadsheet libraries do not always carry them along when rows are deleted.

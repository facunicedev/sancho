# R03. In Excel, figures are formulas

> **type:** rule - **status:** active - **default:** yes - **check:** click a cell and look at the formula bar

Numbers in a spreadsheet are live formulas pointing at a raw data sheet. Never a pasted value.

**Why.** A pasted value cannot be audited and goes stale silently. A formula shows where it came from and updates when the data does. This is the single most useful habit for anyone who sends spreadsheets to other people.

**How.** One sheet named for raw data, untouched, and every visible figure computed against it.

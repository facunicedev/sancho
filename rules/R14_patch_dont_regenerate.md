# R14. Once they edit by hand, you patch

> **type:** rule - **status:** active - **default:** yes - **check:** did they open the file?

The moment the person edits a generated document themselves, generation from the script stops. From then on, targeted patches that open the file and change only what was asked.

**Why.** Regenerating overwrites their edits, and they notice, and they have to say it twice.

**How.** New data still comes from the script output, never typed into the document. The patch reads that output and inserts it.

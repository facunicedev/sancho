# R17. Check the finished file, never the source

> **type:** rule - **status:** active - **default:** yes - **check:** you opened the output

Verification happens on the compiled artifact: the PDF, the .docx, the .xlsx. Never on the script or the markup that produced it.

**Why.** Page counts, margins and formulas are properties of the output. A document that looks like one page in the source is repeatedly two pages in the PDF.

**How.** Open the file. Count the pages there. Click the cell and look for a formula.

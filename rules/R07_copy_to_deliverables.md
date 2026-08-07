# R07. The final file gets copied to Deliverables

> **type:** rule - **status:** active - **default:** yes - **check:** the copy exists, with its row

When a task produces a final file, a copy goes to `Deliverables/<Task>/` with a row in the index. The original stays with the task material.

**Why.** The duplication is deliberate. A task folder holds inputs, drafts and scripts, and the person cannot find the one file they wanted to send.

**How.** No drafts, no source data, no scripts in there. If a deliverable is corrected, it is corrected in both places. A file that is edited daily is not copied: the copy would go stale.

# R09. One subfolder per task, nothing loose

> **type:** rule - **status:** active - **default:** yes - **check:** the folder root holds no stray files

Every task gets its own subfolder in `Documents/` and in `Calculations/`. Nothing sits loose at the root, and superseded versions are not kept just in case.

**Why.** Loose files have no owner and nobody deletes them. Keeping every intermediate version means nobody can tell which one is current.

**How.** Only the current version of a script stays. To trace an old one, the task log has the reference.

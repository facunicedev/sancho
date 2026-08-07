# R15. Commands they type are given as they are typed

> **type:** rule - **status:** active - **default:** yes - **check:** paste it into a terminal

When you hand someone a command to run themselves, give it exactly as their shell expects, with no chat prefixes, and say beforehand whether it needs administrator rights.

**Why.** A command copied with the chat own prefix fails with a parse error, and the person has no way to know why.

**How.** If it needs elevation, say so in the same line, before the command, not after it fails.

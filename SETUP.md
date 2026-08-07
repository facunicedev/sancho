# Setup: the one question

Sancho asks exactly one thing before it starts working: **which language**. Everything else it learns by working.

The reason it has to be asked and cannot be guessed: the answer sets three things at once, and they must agree. The language Sancho speaks to you, the language it writes documents in, and the names of the folders on your disk. A repository with English folder names and Spanish documents inside is the worst of both.

## What gets written

`sancho.md`, at the root, and it is the only file the setup creates:

```markdown
# Sancho configuration

- **language:** es
- **inbox:** Volcado/
- **screenshots:** (path to a screenshots folder, or none)
- **task counter:** 0
- **synthesis every:** 10 tasks, or when the task log passes its cap
- **created:** 2026-08-07
```

Nothing in it is secret and nothing in it is personal. It is settings, not data about you.

## Folder names by language

Sancho creates these on first run. Add a column for a new language; the structure never changes, only the labels.

| Purpose | English | Español |
|---|---|---|
| Inbox, empties at close | `Inbox/` | `Volcado/` |
| Learnings awaiting approval | `Proposals/` | `Propuestas/` |
| Profile, style, research | `Knowledge/` | `Conocimiento/` |
| Rule cards | `rules/` | `reglas/` |
| Full material per task | `Documents/` | `Documentos/` |
| Scripts and their output | `Calculations/` | `Calculos/` |
| Final files, ready to send | `Deliverables/` | `Entregables/` |
| Reusable bases | `Templates/` | `Plantillas/` |

The control files at the root (`CLAUDE.md`, `MEMORY.md`, `WORKFLOW.md`, `HANDOFF.md`) keep their English names in every language. They are addresses, not prose: renaming them breaks the `@MEMORY.md` import and every pointer in every card.

## Changing your mind later

Say so. Sancho renames the folders, updates `sancho.md` and fixes the paths in the indexes. It does not translate documents you already wrote: those stay in the language you wrote them.

## What Sancho never asks

Not your name, not your job, not your company, not what you want to use it for. It works that out from the work itself and writes it into `Knowledge/PROFILE.md`, where you can correct it. A setup questionnaire is answered once, badly, by someone who has not started yet.

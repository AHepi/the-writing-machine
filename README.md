# The Writing Workspace

A file-based system that turns a **two-line brief** into a finished, audited
piece of writing by walking it through five stages. The whole thing is markdown:
no code to run, no dependencies — the files *are* the program, and an LLM is the
interpreter.

## How it works

You write two lines:

```
topic:  what is this about?
goal:   what should the reader think, feel, or do afterward?
```

Everything else (audience, format, length, visuals, heat) defaults, and **stage
00 canonicalizes** your sloppy input into an exact, machine-legal brief. Then the
pipeline runs:

| Stage | Does | Produces |
|---|---|---|
| **00 Brief** | resolves your input to exact values + a deliverables checklist | `brief.md` |
| **01 Research** | gathers facts, tags each one (`F-tag`) with a source | `findings.md`, `sources.md` |
| **02 Compile** | selects facts, fixes reliability (`S-register`), plans the argument, imagery, and visuals | `factsheet.md`, `outline.md` |
| **03 Write** | casts the outline into prose at the Pinker floor; crosses the deliverables gate | `draft.md` |
| **04 Audit** | mechanically checks deliverables, provenance, imagery, visuals; emits the final | `audit.md`, `final.md` |

## The map

- **`CLAUDE.md`** — Layer 0 for Claude (auto-loaded). Each other model gets a
  card in `_navigation/models/`.
- **`CONTEXT.md`** — Layer 1 router: pipeline runs *and* "add an audience /
  format / model" maintenance requests.
- **`_navigation/`** — model cards, capability tiers, assembly recipes for models
  that can't navigate.
- **`_config/`** — `defaults.md`, `rules.md` (the binding laws), `audiences/`,
  `formats/` (including the `course` generator), and `style/` (Pinker prose,
  imagery, visuals, persuasion).
- **`stages/`** — the five stage contracts and their outputs.
- **`archive/`** — finished runs.

## Two ideas worth knowing

1. **The user writes two lines; the machine receives a full contract.** Stage 00
   is the hinge where friendliness and machine-precision stop trading off.
2. **The library grows by asking.** "Add an audience: retired tradies" copies a
   template and fills it — no existing run breaks, because the brief loads files
   by name and defaults cover absence.

Start at `CLAUDE.md`, then `CONTEXT.md`. They explain the rest.

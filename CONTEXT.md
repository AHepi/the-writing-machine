# CONTEXT.md — Layer 1 router

This is the switchboard. You arrived here from your model card
(`CLAUDE.md` if you are Claude; `_navigation/models/nav_<you>.md` otherwise).
This file tells you **what kind of request you are holding** and where to go.
It does no work itself.

There are two kinds of request: a **pipeline run** (produce a piece of writing)
and a **maintenance request** (grow or fix the workspace). Read the user's
words, match the table, go.

---

## A. Pipeline runs — produce a piece of writing

The pipeline is five stages. Each stage reads the previous stage's output and
its own contract, then writes a fixed artifact. Run them in order. Never skip
a stage; never run a later stage's contract against an earlier stage's output.

| Stage | Contract | Reads | Writes |
|---|---|---|---|
| 00 brief | `stages/00_brief/CONTEXT.md` | user request, `_config/defaults.md` | `stages/00_brief/output/brief.md` |
| 01 research | `stages/01_research/CONTEXT.md` | `brief.md` | `findings.md`, `sources.md` |
| 02 compile | `stages/02_compile/CONTEXT.md` | `brief.md`, `findings.md`, `sources.md` | `factsheet.md`, `outline.md` |
| 03 write | `stages/03_write/CONTEXT.md` | `brief.md`, `factsheet.md`, `outline.md` | `draft.md` |
| 04 audit | `stages/04_audit/CONTEXT.md` | all of the above | `audit.md`, `final.md` |

**Where do I start?** If `stages/00_brief/output/brief.md` does not exist, start
at 00. Otherwise start at the first stage whose output is missing. If you were
asked to redo one stage, run only that stage and the ones after it.

**Token thrift** is decided by your model card (§5), not here. A LITE variant
exists for stages 02 and 03 (`CONTEXT_LITE.md`) — small-window or pre-chewed
runs use it; everyone else uses the full contract.

---

## B. Maintenance requests — grow or fix the workspace

| The user says (or means) | You do |
|---|---|
| "Add an audience: <description>" | Copy `_config/audiences/_template.md`, fill all sections, save as `_config/audiences/<slug>.md`, show the result for approval |
| "Add a format: <name>" | Copy `_config/formats/_template.md`, fill all sections, save as `_config/formats/<slug>.md`, show the result |
| "Add a model: <model>" | Run `_navigation/models/_add-a-model.md` end to end |
| "<model> skipped the check / drifted / quit early" | Append a dated line to §7 of that model's card and tighten the paired countermeasure in §4 |
| "Change a rule / the respect floor / a forbidden phrase" | Edit `_config/rules.md`; the change propagates to every later run automatically |
| "Add an expert audience: economist / developer" | Same as adding an audience, but invert the register: dense, citations expected, basics forbidden (see `rules.md` respect floor) |

New files never break old runs. The brief points at library files **by name**;
`_config/defaults.md` covers any absence; and stage 00's canonicalizer maps a
fuzzy request onto whatever the library currently holds. The library may grow
to fifty audiences and the per-run cost stays flat — a run loads exactly one.

---

## C. The contract syntax (read once, applies everywhere)

Every stage contract is written in a fixed verb set. Obey the verbs literally.

- **READ** — open the named file, or only the named §section if thrift is ON.
- **INTERNALIZE** — hold this as a rule for the rest of the stage; do not echo it.
- **TRANSFORM** — the actual work of the stage.
- **WRITE** — emit the named artifact, exactly named, to the stage's `output/`.
- **CHECK** — a gate. List each item with one line of evidence. If any item
  fails, fix and re-CHECK. You may not proceed on a failed CHECK.
- **ASK HUMAN** — stop and ask, with the specific question, when a contract
  says to or when you are blocked on something only the user can decide.
- **STOP** — the stage is done; hand the named artifact to the next stage.

Other conventions:
- **§-addressing.** "`rules.md §respect-floor`" means read that section only.
- **Pointers.** `{brief.field}` is a pointer to a brief field. **Only stage 00
  may resolve pointers.** Every artifact downstream of `brief.md` holds literal
  values, never pointers.
- **F-tags / S-register.** Facts carry F-tags (`F1`, `F2`…) created at stage 01;
  each F-tag names a source S-tag (`S1`, `S2`…) in `sources.md`. Provenance
  travels with the fact through every later stage.
- **D-tags.** Deliverables (`D1`, `D2`…) are minted in the brief, gated at
  stage 03, audited at stage 04.
- **Fixed artifact names.** `brief.md`, `findings.md`, `sources.md`,
  `factsheet.md`, `outline.md`, `draft.md`, `audit.md`, `final.md`. Never rename.
- **Forbidden phrases** (in any output): "in summary," "in conclusion," "the
  remaining sections follow," "and so on," "similarly" (as a section-skipper),
  "insert <X> here." The full list lives in `_config/rules.md`.

# Stage 04 — Audit (mechanical, independent)

*Contract. Runs after stage 03 when `audit: on`. Run by a tier-A model — auditing
needs honest self-checking. It re-derives the checks **independently** from the
brief, factsheet, and outline rather than trusting stage 03's CHECK, fills a
mechanical defect table, fixes what it can, and emits the final piece. A defect
is a defect; the table does not editorialize.*

**Read order:** your Layer 0 card → `../../CONTEXT.md` → this file.

---

## READ

- `../00_brief/output/brief.md` — the **D-list**, length band, audience, format,
  dials.
- `../02_compile/output/factsheet.md` — F-tags and S-registers (ground truth for
  provenance).
- `../02_compile/output/outline.md` — the imagery map and visual marks (ground
  truth for scope).
- `../03_write/output/draft.md` — the thing under audit.
- `_config/rules.md` — the laws each defect class enforces.

## INTERNALIZE

You are not the writer's friend. Re-derive every check from the source artifacts;
do not read stage 03's CHECK and rubber-stamp it. The audit is mechanical: each
row is a yes/no against an objective source. Where you can fix a defect without
rewriting the argument, fix it in `final.md`; where you can't, leave it flagged
and `ASK HUMAN`.

## TRANSFORM — fill the defect table

One row per check. The table grew three columns in v2 (imagery, visuals,
deliverables); they are as mechanical as the rest.

| Class | Check | Source of truth | Pass/Defect | Note |
|---|---|---|---|---|
| **Deliverables** | each D-item present; length in band | `brief.md` D-list | | quote the line, or "MISSING" |
| **Provenance** | each claim → an F-tag; register ≤ S-register | `factsheet.md` | | flag unsupported or over-stated claims |
| **Imagery** | one controlling metaphor, not mixed, not orphaned; every image on the map | `outline.md` `## Imagery` | | flag mixed/orphaned images |
| **Visuals** | every spec's `data:` exists in the factsheet; each sits beside its claim | `factsheet.md` + `outline.md` marks | | flag specs with absent data |
| **Respect floor** | nothing in audience §3 re-explained; no condescension | audience file | | flag patronizing passages |
| **Forbidden phrases** | none present; last third at full density | `rules.md` | | flag occurrences |

Defect definitions (from `rules.md`): a missing D-item is a defect; a claim with
no F-tag is a defect; a mixed or orphaned metaphor is a defect; a visual spec
whose data isn't in the factsheet is a defect; a claim above its S-register is a
defect; a forbidden phrase is a defect.

## WRITE

- `output/audit.md` — the filled defect table, plus a short list of what you
  fixed and what you left flagged.
- `output/final.md` — the draft with all auto-fixable defects corrected. If
  unfixable defects remain, `final.md` carries them marked `[AUDIT-FLAG: …]` and
  the audit STOPs with `ASK HUMAN`.

## CHECK

- [ ] Every table row filled from its source of truth, not from stage 03's CHECK.
- [ ] Every defect either fixed in `final.md` or flagged for the human.
- [ ] No new fact, image, or claim introduced while fixing (audit fixes form, not
      substance — a substantive gap goes back up the pipeline).

## STOP

If the table is all-pass (or all defects auto-fixed), hand `final.md` to the
human as the finished piece. If substantive defects remain, `ASK HUMAN` with the
flagged list. Every edit the human then makes gets the shakedown question:
**one-off, or symptom?** A symptom is fixed in the source file — the rule, the
audience, the contract — so every later run inherits the fix.

# Stage 04 — audit

Check the draft against every promise the pipeline made, mechanically. The audit
is a table, not an opinion: each row is a check, a verdict (PASS/FAIL), and the
evidence. A FAIL is a defect to fix, not a matter of taste. When the draft
passes, it becomes `final.md`. Run by a tier-A model. (Skipped only if
`brief.audit` is `off`.)

## READ
- `stages/00_brief/output/brief.md` — the D-list, length band, audience,
  visuals dial.
- `stages/03_write/output/draft.md` (or `course-package.md` for a course run).
- `stages/02_compile/output/factsheet.md` and `outline.md` — for provenance,
  the imagery map, and the visual marks.
- `_config/rules.md` — the law you are auditing against (§deliverables,
  §no-laziness, §forbidden-phrases, §provenance, §imagery-and-visuals,
  §respect-floor).

## INTERNALIZE
- You check; you do not rewrite to taste. A defect is sent back as a defect, or
  fixed minimally and noted — never silently improved.
- Every verdict carries evidence quoted from the draft or the factsheet. "Looks
  fine" is not a verdict.

## TRANSFORM — fill the audit table

| # | Check | Verdict | Evidence |
|---|---|---|---|
| Deliverables | each D1…Dn present, none padded | PASS/FAIL | quote the delivering line per D-item |
| Length | inside the brief's band | PASS/FAIL | word count vs. band |
| No-laziness | last third as dense as first; no early wrap | PASS/FAIL | note the closing beats |
| Forbidden phrases | none present | PASS/FAIL | scan result |
| Provenance | every factual claim traces to an F-tag | PASS/FAIL | spot-list claims → F-tags |
| **Imagery** | one controlling metaphor, on-map, layered; no mixed/orphaned | PASS/FAIL | each image → its map entry |
| **Visuals** | each spec's `data=` is in the factsheet; has a message; placed by its claim; none unlicensed | PASS/FAIL | each spec → its factsheet data |
| Respect floor | nothing re-explained that the audience profile §3 says they know | PASS/FAIL | note any condescension |

The last three rows (imagery, visuals, plus the deliverables row) are the
columns this audit grew over v1; they stay as mechanical as the rest.

## WRITE
- `stages/04_audit/output/audit.md` — the filled table, plus a defect list for
  any FAIL.
- `stages/04_audit/output/final.md` — the validated piece. Write this **only
  when every row is PASS**. If you fixed minor defects, the fixed text is
  `final.md` and the fixes are itemized in `audit.md`.

## ASK HUMAN
- If a defect can't be fixed without new facts or a judgment call the brief
  doesn't settle (e.g. a missing source for a load-bearing claim), report it in
  `audit.md` and ask, rather than inventing or quietly dropping the claim.

## STOP
- All PASS → `final.md` is the deliverable; STOP.
- Any FAIL that you fixed minimally → note it, write `final.md`, STOP.
- Any FAIL that needs stage 03 (or earlier) to redo → write `audit.md` with the
  defect list and send it back; do not produce `final.md`.

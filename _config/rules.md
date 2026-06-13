# rules.md — the laws that bind every run

*Template by the workspace; content is yours to harden. These are not
suggestions; they are CHECK items. Stage 03 must satisfy them and stage 04
audits them. Where a rule names a failure state, producing that state is a
defect, not a stylistic choice.*

---

## 1. The respect floor

**Write to the audience's ceiling, not their floor. New to the topic is not new
to thinking.**

- Never re-explain what the audience profile's §3 ("Register and assumed
  knowledge") says this audience already knows.
- The reader is an equal who simply hasn't seen this particular view yet — that
  is the Pinker stance, and it is the opposite of condescension by construction.
- For an **expert** audience this rule flips, not loosens: denser register,
  citations expected, basics forbidden. Talking *down* and talking *over* are
  both violations; the profile sets which way is which.
- The condescension test (`_config/style/imagery.md`) gates imagery; this floor
  gates everything else.

## 2. The deliverables law — the anti-laziness spine

**The output matches the deliverables exactly: nothing missing, nothing
padded.**

- Every `D-tag` in `brief.md` must be present in the draft. A missing D-item is
  a defect (stage 03 CHECK and stage 04 both catch it).
- The length must sit inside the band the D-list names. Over is padding; under
  is a shortcut. Both fail.
- **Named failure modes, forbidden by this law:** no "in summary" as a
  substitute for finishing; no compressing later sections as the draft grows;
  the last third is written at the density of the first. "Long form" is not a
  format — it is the refusal to take shortcuts, enforced here.

## 3. Provenance

- Every factual claim in the draft traces to an `F-tag` in the factsheet. A
  claim with no F-tag is unsupported and is a defect.
- The register of a claim must not exceed its source's `S-register`. A
  tentative source may not be written as settled fact.

## 4. Scope discipline

- Stage 03 may render only the images and visuals the **outline** licensed —
  one controlling metaphor, its mapped supports, the marked visuals, and nothing
  off the map.
- Stage 02 may use only facts the **factsheet** carries. No new facts appear
  after research.
- Generation is always downstream of planning.

## 5. Voice

- The delivery floor is `_config/style/pinker-prose.md`: classic style, concrete
  over abstract, the reader shown the world rather than told about the prose.
- The format file sets structure and length; the audience file sets register
  and assumed knowledge; `persuasion.md` sets how hard the argument leans. These
  compose; none overrides the respect floor.

---

*Harden me. Add your own non-negotiables below — the things you would reject a
draft over even if every rule above passed. A template plus your judgment is
stronger than either alone.*

## 6. House rules (yours)

- (add your own here)

## 7. Output delivery & format

**Every run delivers its *final* deliverable to the user as a downloadable file.**

- Non-`course` formats are rendered from `final.md` to **PDF** and delivered as
  `<topic-slug>.pdf`. The PDF is the thing the human reads; the markdown is the
  working file behind it.
- The `course` format is the exception: it delivers its `course-package.md` (a
  markdown handoff meant for a machine to build from, not a human to read) as the
  download. No PDF.
- Rendering follows `stages/04_audit/references/render-pdf.md` — an offline
  markdown → HTML → PDF recipe. Any `CHART:` spec in the draft renders as a
  visual in the PDF, not as raw spec text.
- This rule scopes to the **final deliverable** of a run, not to intermediate
  stage files (briefs, factsheets, outlines, drafts), which stay markdown.

# Stage 02 — compile

Turn raw findings into a piece's plan. This stage does three things no other
stage can, because it is the only one that sees **all the facts** *and* the
**audience** at planning altitude: it selects which facts make the cut, it plans
the **imagery**, and it marks which beats become **visuals**. The output is a
factsheet (the facts that survived, still F-tagged) and an outline (the plan,
including the imagery map and visual marks).

## READ
- `stages/00_brief/output/brief.md` — goal, audience, format, deliverables,
  visuals dial, provocation.
- `stages/01_research/output/findings.md` and `sources.md`.
- `references/selection-method.md` in this folder.
- `_config/audiences/<brief.audience>.md` — for assumed knowledge and the
  imagery source domain (§4).
- `_config/formats/<brief.format>.md` — required parts, length, visuals policy.
- `_config/style/imagery.md` — for the imagery map.
- `_config/style/visuals.md` — **only if** `brief.visuals` is `auto`/`on` and
  the format doesn't veto.

## INTERNALIZE
- Selection serves the deliverables and the goal, weighted by S-register.
  Load-bearing claims need primary/secondary backing; a tertiary-only claim
  can't carry weight (see selection-method).
- Imagery is chosen from the **audience's** world, not yours. One controlling
  metaphor, layered; supporting images complementary. Apply the condescension
  test before anything makes the map.
- A beat becomes a visual only if it passes the earn-its-place test in
  `visuals.md`, and only when visuals are live.
- Plan, don't write. No prose images, no full visual specs here — those are
  stage 03. You license; stage 03 generates.

## TRANSFORM
1. **Select facts.** From `findings.md`, keep those that serve a deliverable or
   the goal (including the opposing case for the counterargument deliverable).
   Carry F-tags and S-tags through unchanged. Build any data tables the piece
   will need, each cell still sourced.
2. **Build the outline.** An ordered beat list that delivers every D-item, in
   the format's shape. Each beat names the F-tags it rests on.
3. **Plan imagery.** Write the `## Imagery` block (controlling metaphor + source
   domain + layering note + beat-mapped supports + meme decision +
   condescension check), per `imagery.md §6`.
4. **Mark visuals.** On any beat that earns one, add a visual mark per
   `visuals.md §5`: form, one-sentence message, `data=` reference, beat number.

## WRITE
- `stages/02_compile/output/factsheet.md` — selected facts (F-tags + S-tags) and
  any data tables, each cell sourced.
- `stages/02_compile/output/outline.md` — the beat list (each beat → its
  F-tags), the `## Imagery` block, and the per-beat visual marks.

## CHECK
- [ ] Every deliverable (D-item) is delivered by at least one beat.
- [ ] Every beat names the F-tags it rests on; every F-tag traces to a source.
- [ ] No load-bearing claim rests on a tertiary-only source.
- [ ] The `## Imagery` block has one controlling metaphor from the audience's
      domain, supports in the same/declared-compatible domain, and a
      condescension-check line.
- [ ] Each visual mark (if any) has a form, a one-sentence message, and a
      `data=` reference that exists in the factsheet. (None if visuals vetoed/off.)
- [ ] The outline can hit the length band without padding or compression.

## ASK HUMAN
- If the surviving facts can't actually deliver a D-item (a gap from stage 01
  proved fatal), say so before stage 03 tries to write around a hole.

## STOP
Hand `factsheet.md` and `outline.md` to stage 03.

# Stage 02 — compile (LITE)

*Pre-chewed variant for tier-C models and tight runs. The imagery and visual
rules are inlined here so no style file is fetched. The assembler has already
pasted the brief, findings, sources, and selection-method into your prompt.
Inputs contain no pointers.*

## READ (already in your prompt)
- the resolved brief, findings, sources, selection-method.

## DO, in order

1. **Select facts.** Keep every finding that serves a deliverable or the goal,
   including facts for the opposing-case deliverable. Keep F-tags and S-tags
   exactly as written. Don't keep a load-bearing claim that has only a tertiary
   source.

2. **Outline.** Write an ordered list of beats that covers every D-item in the
   brief, in the format's shape. After each beat, list the F-tags it uses.

3. **Imagery block.** Write this, filling the blanks from the audience named in
   the brief:
   ```
   ## Imagery
   - Controlling metaphor: <one image from the audience's world>
   - Layering: <introduce it simply early; extend it later; never replace it>
   - Supporting images: <each + the beat it serves; all from the same world>
   - Memes: <only if the brief's format AND audience allow; else "none">
   - Condescension check: would one of this audience use these images? <yes + why>
   ```
   Rule: one controlling metaphor; supports stay in the same world; nothing that
   explains the audience's own world back to them.

4. **Visual marks** (only if the brief says `visuals: auto` or `on`). On a beat
   that has numbers-with-a-shape (chart), a process/structure (diagram), or a
   side-by-side comparison (table), add:
   `visual: <CHART|DIAGRAM|TABLE> — message="<the one thing it shows>" — data=<F-tag/table> — beat <n>`
   The `data=` must be a fact you kept. Don't mark anything else. If the brief
   says `visuals: off`, skip this step.

## WRITE
- `factsheet.md` — the kept facts (F-tags + S-tags), plus any data tables.
- `outline.md` — the beats (each with its F-tags), the Imagery block, the visual
  marks.

## CHECK (write one line of evidence each)
- [ ] Every deliverable is covered by a beat.
- [ ] Every beat lists its F-tags.
- [ ] Imagery block: one controlling metaphor, supports in the same world,
      condescension check answered.
- [ ] Every visual mark's `data=` is a kept fact (or there are no marks).

## STOP
Output `factsheet.md` and `outline.md`. Do not write any prose of the piece —
that is the next stage.

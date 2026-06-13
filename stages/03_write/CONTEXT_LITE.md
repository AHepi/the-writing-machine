# Stage 03 — write (LITE)

*Pre-chewed variant for tier-C models and tight runs. The prose floor
(`pinker-core.md`), the D-gates, and the forbidden-phrase list are inlined into
your prompt by the assembler, along with the brief, factsheet, and outline. The
outline already carries the licensed imagery and the visual marks, so no style
file is fetched. Inputs contain no pointers.*

## Your inputs (already in your prompt)
- the brief (with its D-list and length band), the factsheet, the outline (with
  its Imagery block and visual marks), and the Pinker core.

## Write the piece — the rules, plainly

1. **Deliver the D-list exactly.** Hit every D-item in the brief. Add nothing
   that isn't a deliverable. Stay inside the length band — over the band is a
   defect, not a bonus.
2. **No shortcuts.** Write every beat in the outline, in order, fully. The last
   beat gets as much care as the first. Never write "in summary," "in
   conclusion," "the remaining sections follow," "and so on," or "similarly" to
   skip writing something out. Never write "insert chart here."
3. **Use only the outline's images.** Carry the one controlling metaphor through
   the whole piece, starting simple and extending it as things get harder. Use
   only the supporting images the Imagery block lists. No new images.
4. **Write only the marked visuals.** For each visual mark in the outline, write
   a real spec:
   `CHART id=V1 type=bar data=<the table/F-tag> message="<the one thing it shows>" x=<col> y=<col>`
   (or `DIAGRAM`/`TABLE` likewise). Put it in the beat that makes the claim. No
   other visuals.
5. **Every fact must trace to an F-tag.** Don't invent numbers or sources. If a
   fact you need isn't in the factsheet, stop and say so — don't make it up.
6. **Don't talk down.** The brief's audience already knows the things listed in
   its profile; don't re-explain them.

## WRITE
`draft.md`.

## CHECK — write one line of evidence for each, quoted from what you wrote
- [ ] Each D-item D1…Dn: quote the sentence that delivers it.
- [ ] Word count: <n>, inside the band <low>–<high>.
- [ ] No forbidden phrase appears.
- [ ] The last third is as full as the first (not thinned, not wrapped up early).
- [ ] Every image is one the outline listed; the metaphor is extended, not swapped.
- [ ] Every visual spec's data is in the factsheet.

If any line fails, fix it and check again before you stop.

## STOP
Output `draft.md`.

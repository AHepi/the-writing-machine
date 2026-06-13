# Stage 02 — Compile (facts, argument, imagery, visuals)

*Contract. Runs after stage 01. This is the planning altitude — the only stage
that sees **all the facts and the audience at once**. It selects which facts
make the cut, fixes their S-register, builds the outline, and plans the imagery
and visuals. Stage 03 executes this plan and may add nothing to it.*

**Read order:** your Layer 0 card → `../../CONTEXT.md` → this file. (LITE variant
exists: `CONTEXT_LITE.md`.)

---

## READ

- `../00_brief/output/brief.md` — goal, audience, format, length, `visuals`
  dial, `provocation`, the **D-list**.
- `../01_research/output/findings.md` and `sources.md` — the F-tagged facts and
  their reliability.
- `references/selection-method.md` — how to choose and order.
- `_config/style/imagery.md` — to plan the `## Imagery` block.
- `_config/style/persuasion.md` — to plan the argument spine.
- `_config/style/visuals.md` — **only if** `visuals` is `auto` or `on`.
- The active **audience** file (named in the brief) — for register and the
  imagery source-world.

## INTERNALIZE

Two artifacts come out of here: a **factsheet** (the facts that survive, each
with a fixed S-register) and an **outline** (the argument, plus imagery, plus
visual marks). Everything stage 03 writes is licensed here. Selection happens at
this altitude because nowhere else sees all the facts *and* the audience
together.

## TRANSFORM

**Facts → factsheet.**
- Select the facts that serve the goal and the D-list; cut the rest
  (`selection-method.md`). Over-gathering in stage 01 is paid back here.
- Assign each surviving fact its **S-register** from the source reliability:
  `S-strong` / `S-medium` / `S-weak`. The draft may not exceed it.
- Resolve or openly frame each contested fact — decide how the draft handles it.

**Argument → outline beats.**
- Lay out the spine from `persuasion.md`: claim → reason → evidence → objection
  → reply, mapped to the format's required parts (the D-list).
- Each beat names the F-tags it uses.

**Imagery → `## Imagery` block** (mandatory).
- Choose ONE controlling metaphor from the audience's world (`imagery.md`).
- List compatible domains, and every supporting analogy mapped to the beat it
  serves.
- For a complex topic, note how the metaphor *layers* (simplest early, extended
  later).
- Apply the condescension test to each image. Any licensed meme is listed here
  or it may not appear.

**Visuals → per-beat marks** (only if dial is `auto`/`on`).
- Mark any beat where a chart, diagram, or table beats prose (`visuals.md`
  shape-matching). Leave it as a mark; stage 03 writes the spec. The format may
  veto — honor it.

## WRITE

- `output/factsheet.md` — surviving facts as `F<n> [S-register]: <claim>
  [src]`. Nothing the draft can claim lives outside this file.
- `output/outline.md` — the beats in order (each naming its F-tags), then a
  `## Imagery` block, with per-beat visual marks where licensed.

## CHECK

- [ ] Every D-item maps to at least one outline beat.
- [ ] Every selected fact carries an S-register; none exceeds its source.
- [ ] The argument spine is complete (claim → … → reply); D2's counterargument
      is steelmanned.
- [ ] `## Imagery` has exactly one controlling metaphor, from the audience's
      world, passing the condescension test; supports share its domain.
- [ ] Visual marks appear only if the dial allows and only where a visual beats
      prose; format veto honored.
- [ ] No fact or image appears that isn't traceable to research / the audience's
      world.

## STOP

Hand off to stage 03. The outline is now a contract: stage 03 renders exactly
its beats, images, and marks — nothing off the plan.

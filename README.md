# The Writing Machine

A writing workspace built as a pipeline of **contracts**, not code. A model
(Claude, DeepSeek, Gemma, anything) enters at its Layer 0 card, gets routed by
`CONTEXT.md`, and runs five stages — brief → research → compile → write → audit
— each one reading the last one's output and obeying a fixed contract. The
output is a finished piece of writing that matches a two-line brief, in the
right register for its audience, with planned imagery and real visual specs, and
audited against every promise.

## How to use it

Write two lines:

```
topic:  what is this about?
goal:   what should the reader think, feel, or do afterward?
```

Everything else (`audience`, `format`, `length`, `visuals`, `provocation`,
`audit`, `notes`) defaults, and you override a field only when you want to.
Stage 00 canonicalizes your sloppy input into an exact, fully-resolved brief; the
rest of the pipeline runs on that.

## The map

- **`CLAUDE.md`** — Claude's Layer 0 card (auto-loaded). Other models get a card
  under `_navigation/models/`.
- **`CONTEXT.md`** — the router: pipeline runs *and* maintenance requests
  ("add an audience", "add a model").
- **`_navigation/`** — tiers, per-model cards, `_add-a-model.md`, and
  copy-paste `assembly-order.md` recipes for models that can't navigate.
- **`_config/`** — `defaults.md`, `rules.md` (the law), `audiences/`,
  `formats/` (including `course.md`, a generator), and `style/` (Pinker prose +
  core, persuasion, imagery, visuals).
- **`stages/`** — the five stage contracts (00–04), with LITE variants for 02
  and 03 and method references for 01 and 02.
- **`archive/`** — finished runs.

## The ideas that make it work

- **Two required fields; everything else defaults.** The human writes two lines;
  the machine receives a fully explicit contract.
- **A card per model, not just tiers.** Token thrift is a per-model policy, not
  a global virtue: small windows get scoped reads; lazy frontier models get
  whole-file redundancy and a finish line they must cross.
- **Deliverables (D-tags), not "long form".** The brief expands into a checklist;
  stage 03 gates it; stage 04 audits it. The bare minimum is a failure state.
- **Imagery and visuals are planned, then executed.** Stage 02 draws the map
  (one controlling metaphor from the audience's world, layered; visual marks);
  stage 03 may not exceed it.
- **Never patronizing.** Audience profiles carry assumed knowledge; `rules.md`
  carries the respect floor; classic style supplies the equal-to-equal stance.
- **Grow by asking.** "Add an audience: retired tradies" copies a template,
  fills it, and the per-run cost stays flat — a run loads exactly one audience.

Start at `CONTEXT.md`.

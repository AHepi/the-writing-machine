# tiers.md — shared baselines model cards inherit

*Tiers are baselines, not the system. The system is one card per model in
`_navigation/models/`. A tier is the default behavior a card starts from and
then overrides. Three tiers, by capability, plus the budget policy every card
reads.*

---

## Tier A — frontier, navigates unaided

- **Reads pointers.** May resolve `{brief.field}` and fuzzy user input.
  Therefore may run **stage 00** (canonicalize) and **stage 04** (audit).
- **Full context.** Loads whole contracts and whole config. Does not require
  LITE files or pre-chewed input.
- **Honest CHECK.** Runs the completion ritual and reports unmet deliverables
  truthfully.
- **Default context policy:** thrift OFF (load whole), but may switch ON to
  save tokens on a paid run. Its choice.
- *Failure modes to watch:* helpfulness drift, over-explaining, inventing scope.

## Tier B — capable, navigates with guardrails

- **No pointer resolution.** Receives a fully-resolved `brief.md` from stage 00
  and never opens `defaults.md` or any config it must match by judgment.
- **May run stages 01–03** using each stage's `CONTEXT.md`, preferring
  `CONTEXT_LITE.md` where it exists.
- **Scoped reads.** Reads files by section (§-addressing) to stay inside its
  window.
- **Default context policy:** thrift ON. Pre-chewed context, scoped §-reads.
- *Failure modes to watch:* losing the thread across long inputs, partial
  CHECKs.

## Tier C — small window, cannot navigate

- **Never navigates.** Cannot follow a multi-file contract or resolve a
  pointer. Its card points at `_navigation/assembly-order.md`, which lists the
  exact files to concatenate into **one** prompt per stage.
- **Pointers are illegal in its inputs.** Stage 00 has already resolved them
  all; the human (or a tier-A model) assembles its prompt.
- **One stage at a time, one prompt, one output.**
- **Default context policy:** thrift hard ON. Minimum viable context, LITE
  files only, anchors restated inside the single prompt.
- *Failure modes to watch:* dropping instructions under load, summarizing
  instead of completing.

---

## Budgets — floors, not goals

The pipeline *can* run a full piece in **2–4k tokens per stage** with thrift ON.
Those numbers are floors, not targets. The nav card decides whether to spend
more:

- **Thrift ON** — small windows, paid-API frugality. Scoped §-reads, LITE
  files, no restated anchors.
- **Thrift OFF** — a frontier-but-lazy model whose failure mode is *abandonment,
  not overflow*. Load files whole, restate anchors, spend tokens freely;
  redundancy is cheap insurance against a model that won't finish.

The architecture makes both cheap to choose: scoped §-reads exist for one
policy, whole-file loads with restated anchors for the other, and **the same
contracts serve both**. A card sets the policy in its §5; nothing else changes.

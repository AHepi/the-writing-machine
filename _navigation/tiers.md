# tiers.md — shared baselines

A tier is the inherited floor of behavior a model card builds on. A card names
its tier in §2 and then overrides or tightens as the model needs. Tiers are
baselines, **not** the navigation system — the system is one card per model.
Three tiers, coarsest to finest control:

---

## Tier A — frontier, self-navigating

The model can hold a full stage's inputs, follow a multi-file contract unaided,
resolve `{brief.field}` pointers, and run an honest CHECK against its own
output. 

- May run any stage, including stage 00 (canonicalizing) and stage 04 (audit).
- May resolve pointers and mint new library files.
- Default context policy is the card's call: thrift ON for frugality, OFF where
  a lazy frontier model needs redundancy to finish.
- Trusted to fail itself on a CHECK.

Examples: Claude (see `CLAUDE.md`), DeepSeek V4 (with completion countermeasures
— see its card).

## Tier B — capable, supervised navigation

Follows contracts but drifts on long chains or skips self-checks under load.

- May run stages 01–03 unaided; stage 00 and stage 04 only with thrift ON and
  pre-chewed (LITE) contracts.
- Pointers should already be resolved before this model sees a file; it may
  resolve a single shallow pointer but must flag it.
- Context policy: thrift ON by default, scoped §-reads.
- A CHECK must be run as a literal checklist with quoted evidence, never "looks
  good."

## Tier C — small window, no navigation

Cannot navigate, cannot resolve pointers, cannot hold multiple files in
working context. Executes one fully-assembled prompt per stage.

- Never navigates. Its card points at `_navigation/assembly-order.md`, which
  lists the exact files to concatenate into a single prompt per stage.
- Inputs must contain **zero pointers** — stage 00 has resolved them all.
- Context policy: thrift ON, hard. One stage, one prompt, one artifact out.
- Does not run stage 00 or stage 04. A capable model brackets its work.

Example: Gemma 4B (see its card and the assembly recipes).

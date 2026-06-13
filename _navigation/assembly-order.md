# assembly-order.md — copy-paste recipes for models that can't navigate

For tier-C models (Gemma 4B and friends). A human or a capable model builds one
self-contained prompt per stage by concatenating the listed files **in order**.
The result must contain the full contract, the exact inputs, and **no pointers**
— stage 00 resolved them all before any tier-C model was handed work.

The hard rule: **before sending, search the assembled prompt for `{` and `§`.
If either appears, it is not assembled — resolve it first.** A tier-C model
must never be asked to follow a pointer or fetch a section.

Stage 00 (brief/canonicalize) and stage 04 (audit) are **not** assembled for
tier-C models; a capable model runs those.

---

## Recipe — Stage 01 research
1. `stages/01_research/CONTEXT.md`
2. `stages/01_research/references/research-method.md`
3. `stages/00_brief/output/brief.md`  (the resolved brief)

Output expected back: `findings.md` and `sources.md`, fixed names.

## Recipe — Stage 02 compile (LITE)
1. `stages/02_compile/CONTEXT_LITE.md`
2. `stages/02_compile/references/selection-method.md`
3. `stages/00_brief/output/brief.md`
4. `stages/01_research/output/findings.md`
5. `stages/01_research/output/sources.md`

Output expected back: `factsheet.md` and `outline.md`. The LITE contract inlines
the imagery and visual-marking rules so no style file needs to be fetched.

## Recipe — Stage 03 write (LITE)
1. `stages/03_write/CONTEXT_LITE.md`
2. `_config/style/pinker-core.md`  (the ≤350-token prose floor, inlined)
3. `stages/00_brief/output/brief.md`
4. `stages/02_compile/output/factsheet.md`
5. `stages/02_compile/output/outline.md`

Output expected back: `draft.md`. The LITE contract carries the D-gates and the
forbidden-phrase list inline; the outline already carries the licensed imagery
and visual specs, so no `imagery.md` / `visuals.md` fetch is needed.

---

## Assembler's checklist (the human's CHECK)
- [ ] Files concatenated in the listed order, each under a clear `=== filename ===` header.
- [ ] No `{...}` pointers remain.
- [ ] No `§` section-references remain (sections were pasted in full).
- [ ] Only this stage's inputs are present — no prior drafts, no whole library.
- [ ] The output artifact names are stated at the bottom so the model knows what to emit.

# assembly-order.md — copy-paste recipes for models that can't navigate

*For tier-C models (e.g. Gemma 4B) and for any time a human wants to run a stage
by hand. Each recipe lists, in order, the exact files to concatenate into one
prompt. Concatenate top to bottom, paste, collect the one named output. No file
here contains a pointer — stage 00 resolved them all.*

**How to read a recipe:** paste the files in the listed order. Where a recipe
says *(restate)*, copy that anchor again at the very bottom of the prompt too —
tier-C models lose anchors in long text, so the goal and D-list bookend the
prompt.

---

## Stage 01 — Research

1. `stages/01_research/CONTEXT.md`
2. `stages/01_research/references/research-method.md`
3. `stages/00_brief/output/brief.md`  *(the topic, goal, audience, deliverables — restate the topic + D-list at the bottom)*

→ Output: `findings.md`, `sources.md`. Each fact gets an **F-tag**.

## Stage 02 — Compile

1. `stages/02_compile/CONTEXT_LITE.md`
2. `stages/02_compile/references/selection-method.md`
3. `_config/style/imagery.md`  *(needed to plan the `## Imagery` block)*
4. `_config/style/visuals.md`  *(only if brief says `visuals: on`/`auto`)*
5. `stages/00_brief/output/brief.md`
6. `stages/01_research/output/findings.md`
7. `stages/01_research/output/sources.md`

→ Output: `factsheet.md` (F-tags + **S-register**), `outline.md` (with
`## Imagery` and per-beat visual marks). *(restate the D-list at the bottom)*

## Stage 03 — Write

1. `stages/03_write/CONTEXT_LITE.md`
2. `_config/style/pinker-core.md`
3. `_config/style/imagery.md`
4. `_config/style/visuals.md`  *(only if visuals are live)*
5. The active audience file, e.g. `_config/audiences/general.md`  *(named literally in brief.md — paste the right one)*
6. The active format file, e.g. `_config/formats/essay.md`
7. `stages/00_brief/output/brief.md`
8. `stages/02_compile/output/factsheet.md`
9. `stages/02_compile/output/outline.md`

→ Output: `draft.md`. *(restate the goal + full D-list at the bottom — tier-C
models must see the finish line they have to cross)*

---

**Note on stages 00 and 04.** There is no tier-C recipe for them. Stage 00
(canonicalize) needs pointer resolution and stage 04 (audit) needs honest
self-checking — both are tier-A only. A capable model runs those; tier-C models
only ever touch 01–03.

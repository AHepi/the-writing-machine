# audit.md — constructor theory crash course (mechanical, independent)

*Checks re-derived from `brief.md`, `factsheet.md`, and `outline.md` — not from
stage 03's CHECK. Defects fixed in `final.md` are noted; nothing substantive was
introduced.*

## Deliverables (source of truth: brief.md D-list)

| D | Check | Pass/Defect | Evidence in final.md |
|---|---|---|---|
| D1 | title block: title, subtitle, "what you'll be able to do" promise | **Pass** | `# The Science of Can and Can't` + `<span class="subtitle">…</span>` + "By the end you will be able to say, in your own words, what constructor theory is…" |
| D2 | ch.1 opens on a concrete puzzle + names the governing question | **Pass** | "Crack an egg into a hot pan and stir…" → blockquote: "What if the deepest laws of physics were not predictions of what happens next, but statements about which transformations are possible and which are impossible…?" |
| D3 | explains the prevailing conception (initial conditions + laws of motion) | **Pass** | Ch.2: "Write down two things. First, its **initial conditions**… Second, its **laws of motion**… out comes a prediction of what the system will do" (F6) |
| D4 | explains the reframing — possible vs impossible tasks | **Pass** | Ch.3: "state the laws of physics **only** in terms of which transformations are possible and which are impossible, and why" (F7) |
| D5 | defines task, constructor, substrate, possible/impossible, notation named | **Pass** | Ch.4 defines all three (F10–F12), the possible/impossible split (F13), and the "math, gently" box names every symbol of $a \rightarrow b$ |
| D6 | explains counterfactuals and "the science of can and can't" | **Pass** | Ch.3: "a claim about a state of affairs that may never come to pass… counterfactuals… belong at the very foundation of physics" (F14, F15) |
| D7 | information (2015), life (2015), thermodynamics — at full density | **Pass** | Ch.5 (F17–F19), Ch.6 (F20–F23), Ch.7 (F24–F26); each a full chapter with hook, analogy, recap |
| D8 | honest status: claims, testability (gravity), early-stage/not mainstream | **Pass** | Ch.8: "a young research programme, not established physics… outside the current mainstream… not been confirmed by experiment" (F27, F28); gravity test fenced as "not a direct test of constructor theory as a whole" (F29, F30) |
| D9 | glossary of every term | **Pass** | `## Glossary` — 14 terms, each defined |
| D10 | further reading to real F-tagged sources | **Pass** | `## Further reading` — 7 sources, each tagged [S1]…[S17] |
| D11 | every chapter at full density; last as dense as first | **Pass** | Ch.8 (final) is the longest chapter, with its own table and worked example; no compression |
| D12 | length 6,000–9,000 words | **Pass** | 6,362 words |

## Provenance (source of truth: factsheet.md)

| Check | Pass/Defect | Note |
|---|---|---|
| every factual claim → an F-tag | **Pass** | every load-bearing claim carries a sidenote citing its F-tag; exposition (kitchen analogies, the "possible even if never built" elaboration) adds no new facts |
| register ≤ S-register | **Pass** | S-medium facts handled with care: F9 framed as "in Marletto's words" (a quoted heuristic, not asserted law); F27 framed as "outside the current mainstream… not confirmed," not as an authoritative verdict; F25 framed as "fits the mould," not proof |
| contested facts handled honestly | **Pass** | F27/F28 stated plainly as the programme's status; F29/F30 explicitly fenced as a related research direction, not confirmation |

## Imagery (source of truth: outline.md `## Imagery`)

| Check | Pass/Defect | Note |
|---|---|---|
| one controlling metaphor, not mixed, not orphaned | **Defect → fixed** | The draft introduced two analogies outside the declared kitchen domain — "like a rumour" and "the children's game of telephone." Recast in `final.md` into the kitchen (a recipe passed by word of mouth / down a line of cooks), keeping the single controlling metaphor intact. |
| every image on the map | **Pass** | recipe=task, cook=constructor, ingredients=substrate, unscrambling=impossible task, free-lunch kitchen=perpetual motion, copyable recipe=information, recipe-that-builds-the-cook=life, one-way kitchen=second law — all on the map; the "cosmic prediction machine" is framed in kitchen terms (ingredients, dishes) so stays in-domain |

## Visuals (source of truth: factsheet.md + outline.md marks)

| Check | Pass/Defect | Note |
|---|---|---|
| every visual's data exists in the factsheet | **Pass** | TABLE "two pictures" → F6, F7, F13, F16; DIAGRAM constructor flow → F10, F11, F12; TABLE "subsidiary theories" → F17, F19, F20, F22, F24, F25, F26 — all present |
| each visual beside its claim | **Pass** | comparison table sits in Ch.3 beside the reframing; the diagram in Ch.4 beside the three definitions; the summary table in Ch.8 beside the status accounting |
| rendered as visuals, not raw spec text | **Pass** | tables render as real tables; the constructor diagram renders as an inline SVG figure (the tufte-pdf skill renders markdown/HTML natively, so visuals are emitted as finished visuals rather than `CHART:`-style specs) |

## Respect floor (source of truth: beginner.md §3)

| Check | Pass/Defect | Note |
|---|---|---|
| nothing in audience §3 re-explained | **Pass** | everyday cause/effect, "recipes have steps," and "games have rules" are used, never explained |
| no condescension; banned words | **Defect → fixed** | `beginner.md` §3 names "simply / obviously / of course / just" as talking-down markers. The draft contained 12 such uses; all removed or reworded in `final.md` (e.g. "the word *just* means" → "the word means"; "simply not there" → "not there"). No "obviously"/"of course" were present. |

## Forbidden phrases (source of truth: rules.md)

| Check | Pass/Defect | Note |
|---|---|---|
| no "in summary," "the remaining … follow," "similarly," "and so on" | **Pass** | none present; the last third (Ch.7–8 + glossary + reading) is at full density |

## Summary

- **Fixed in final.md:** (1) two out-of-domain analogies (rumour / telephone)
  recast into the kitchen; (2) twelve uses of `beginner.md`-banned words
  ("just"/"simply") removed or reworded. Both are form-level — no fact, image, or
  claim was added or changed in substance.
- **Left flagged for the human:** none. The table is all-pass or
  auto-fixed.
- **Note (not a defect):** the rendered PDF runs to ~31 Tufte pages. The binding
  length deliverable (D12) is the word count, 6,362, which sits in the
  6,000–9,000 band; the page figure runs a little above the format's "≈18–28"
  estimate because each chapter opens on a fresh page (a deliberate textbook
  choice) and Tufte's wide margin column packs fewer words per page. Flagged for
  transparency, not as a defect.

**STOP:** table all-pass / auto-fixed → render `final.md` to PDF via the
`tufte-pdf` skill and deliver it.

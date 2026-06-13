# How Much Do Audience and Format Actually Change the Output?

*An empirical A/B test on the Writing Workspace. We took one finished run — the
land-value-tax-for-New-Zealand essay — and regenerated it twice, each time
changing exactly one dial, so the effect of each lever can be measured rather
than asserted.*

## The experiment

Three pieces, same topic, same facts, same argument spine. Everything that could
be held constant was held constant — the research (`factsheet.md`'s fifteen
F-tags), the provocation dial (`low`), the visuals dial (`auto`), the deliverables
D1–D4. Only one lever moves per variant:

| | Audience | Format | Lever changed |
|---|---|---|---|
| **A — baseline** | general | essay | — (control) |
| **B** | **socialist** | essay | audience only |
| **C** | general | **op-ed** | format only |

Because the facts are fixed and only one input moves at a time, every difference
between A and B is attributable to **audience**, and every difference between A and
C to **format**. The drafts themselves sit beside this file
(`variant-B-socialist-essay.md`, `variant-C-general-oped.md`); the baseline is the
run's own `final.md`.

## The measurements

| Dimension | A — general / essay | B — socialist / essay | C — general / op-ed |
|---|---|---|---|
| **Lever vs A** | baseline | audience only | format only |
| **Word count** | 1,605 | 1,611 | 898 |
| **Length band** | 1,400–1,700 | 1,400–1,700 | 700–900 |
| **Section headings (H2)** | 7 | 5 | 0 |
| **Structure** | 8-beat essay | 8-beat essay | op-ed: news-peg lede → 3 fast reasons → objection → kicker |
| **Facts used (of 15)** | 15 | 15 | 13 (drops F9 TWG, F15 intl deferral) |
| **Visuals** | 1 bar chart | 1 bar chart | 0 (format veto) |
| **Controlling metaphor** | "the corner that got lucky" | the tollkeeper on socially-made rent | "the corner that got lucky" |
| **Imagery domain** | neighbourhood / property / local infrastructure | labour / commons / ground rent / enclosure | neighbourhood / property / local infrastructure |
| **Voice** | 3rd person, explanatory | 3rd person, systemic + solidary | 1st person, columnist |
| **Register markers** | plain; every term defined | "ground rent", "unearned", "accumulation", "rentier", "settlement", "class" | "I'll put my conclusion first"; news peg; biting kicker |
| **Assumed knowledge** | new to the topic | knows class / why markets concentrate wealth — not re-explained | new to the topic |
| **Provocation (dial held)** | low | low | low |

## What the audience lever did (A → B)

Holding the format fixed, swapping `general` for `socialist` changed **almost
nothing structural and almost everything on the surface**:

- **Length: unchanged** (1,605 → 1,611, +0.4%). **Facts used: unchanged** (15 →
  15). **Visuals: unchanged** (the chart stays). **Spine: unchanged** (same eight
  beats, same steelman→reply).
- **Imagery domain: ~100% turnover.** The neighbourly "corner that got lucky"
  becomes the rentier "tollkeeper at a bridge he did not build"; the metaphor
  field moves from property-and-traffic to commons-rent-and-enclosure, exactly the
  worlds the two audience files license (`general.md` §4 vs `socialist.md` §4).
- **Register and vocabulary changed wholesale** — "ground rent", "the unearned
  increment", "accumulation", "a settlement, not an accident".
- **What gets explained changed.** B never explains why money concentrates in
  land — the socialist profile's §3 forbids re-teaching that — and spends the
  saved room on the political-economy reading instead. The respect floor moved.

## What the format lever did (A → C)

Holding the audience fixed, swapping `essay` for `op-ed` changed **the entire
scaffold and left the voice's world intact**:

- **Length: −44%** (1,605 → 898), tracking the band (1,400–1,700 → 700–900).
- **Headings: 7 → 0.** The op-ed runs as continuous column prose; the essay's
  section architecture disappears.
- **Structure rebuilt** to the op-ed contract — a news peg (Wellington's 2024
  rates debate), thesis in the first 120 words, three compressed reasons, one
  objection beat, and a kicker instead of a payoff section.
- **Visuals: 1 → 0.** The affordability chart vanishes — not by choice but because
  the op-ed format vetoes visuals unless the brief forces them (`oped.md` §5). This
  is the cleanest single proof that visuals are a *format* outcome: identical
  audience and identical `visuals: auto` dial, opposite result.
- **Facts: 15 → 13.** The word budget forced two facts out (the Tax Working Group
  note, the international-deferral precedent) — the spine survives, the supporting
  detail is what gets cut.
- **Imagery domain: unchanged.** C keeps A's "lucky corner" and its
  neighbourhood vocabulary exactly, because the audience didn't move.

## The same beat, three ways

The opening — all carrying the identical fact (F4: land value is community-made):

> **A (general/essay):** "A house in a New Zealand suburb is worth more this winter
> than it was last, and the family inside it did nothing to earn the difference."

> **B (socialist/essay):** "When a train line opens in a New Zealand suburb, the
> land beside it gets richer overnight. Not the workers who laid the track … the
> person who owns the dirt."

> **C (general/op-ed):** "When Wellington City Council floated the idea, in 2024,
> of shifting its rates onto the value of land … it was the most sensible tax idea
> a New Zealand council has put on the table in years."

Same fact, three doors: a neighbour's window (A), an owner-versus-labour ledger
(B), a news peg (C).

## Verdict

The two levers act on different layers, and the magnitudes are not symmetric:

- **Format is the structural lever.** It set length (−44%), rebuilt the structure,
  erased the section headings (7 → 0), removed the visual (1 → 0), and forced a
  fact cut (−13%) — while leaving the imagery domain and the audience-facing voice
  essentially untouched.
- **Audience is the surface lever.** It left length, fact count, spine, and visuals
  identical, then turned over the imagery domain (~100%), the register and
  vocabulary, and the contract of what may be assumed and what must be explained.

Put plainly: **format decides the shape of the container; audience decides the
texture of what's poured in.** Change the format and you get a differently-sized,
differently-built artifact carrying fewer or more of the same facts. Change the
audience and you get the same artifact, re-voiced for a different reader. A brief
that gets either dial wrong fails in a different way — the wrong format ships the
wrong *object*; the wrong audience ships the right object to the wrong *person*.

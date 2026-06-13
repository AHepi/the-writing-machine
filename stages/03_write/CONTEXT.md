# Stage 03 — write

Write the piece. Every fact is already chosen, every image licensed, every
visual marked. Your job is to deliver the outline as finished prose at the prose
floor, hitting every deliverable, inside the length band, with no shortcuts and
nothing off the imagery/visual map. This is where the anti-laziness law bites.

## READ
- `stages/00_brief/output/brief.md` — deliverables (D-list), audience, format,
  length band, provocation.
- `stages/02_compile/output/factsheet.md` and `outline.md` — facts (F-tags),
  beats, the `## Imagery` block, the visual marks.
- `_config/style/pinker-prose.md` (or `pinker-core.md` under thrift) — the prose
  floor.
- `_config/audiences/<brief.audience>.md §3` — assumed knowledge / register.
- `_config/style/imagery.md` — to execute the licensed images correctly.
- `_config/style/visuals.md` — **only if** the outline carries visual marks.
- `_config/style/persuasion.md` — **only if** the goal is to persuade / the
  format argues.
- `_config/rules.md` — the law, especially §no-laziness and §forbidden-phrases.
- **Course mode** (`brief.format` is `course`): also read `_config/formats/course.md`
  (all), `_config/style/visuals.md` (all), `_config/style/imagery.md` (all), and
  the audience profile (all). Course mode reads these **whole** — it is exempt
  from token thrift, because the package must be self-contained.

## INTERNALIZE
- **Deliver exactly the D-list.** Nothing missing, nothing padded
  (`rules.md §deliverables`). A piece over its band is a defect, not generosity.
- **No shortcuts.** Write the last third at the density of the first. No
  compressing later sections as you tire. No "in summary," no "and so on," no
  trailing off (`rules.md §no-laziness`, §forbidden-phrases).
- **Nothing off the map.** Use the controlling metaphor and only the supporting
  images the outline licensed, layered as planned. Write only the visuals the
  outline marked. Generation is downstream of planning.
- **Provenance holds.** Every factual claim traces to an F-tag. If a needed fact
  is missing, ASK HUMAN — do not invent.
- **Respect floor.** Write to the audience's ceiling; never re-explain what
  their profile §3 says they already know.

## TRANSFORM
- Write the draft beat by beat, in outline order. Carry the controlling metaphor
  through, extending it as the argument deepens.
- Where the outline marked a visual, emit a full spec in `visuals.md` syntax
  (`CHART:`/`DIAGRAM:`/`TABLE:`/`WIDGET:` with `id`, `data=`, one-sentence
  `message=`/`success=`), placed in that beat — never a vague "insert chart here."
- **Course mode** (`brief.format` is `course`): do **not** write learner-facing
  prose. Instead generate the handoff package per `_config/formats/course.md`:
  output `course-package.md` with sections **A–I**, lettered, in order
  (build notes, content breakdown + architecture laws, visual directives + the
  decision table, data tables, fact sheet, tone instructions, imagery
  repertoire, the STYLE-CORE style guide verbatim, sources). Write exactly one
  SAMPLE card (module 1) and no other learner-voice prose. Copy the [TEMPLATE]
  blocks and the [VERBATIM] STYLE-CORE in unchanged; generate the rest from this
  run's subject and audience; never copy the format file's own examples.

## WRITE
`stages/03_write/output/draft.md` (or `course-package.md` for a course run).
Exact name.

## CHECK  (list each with one line of quoted evidence from your own output)
- [ ] **Every D-item present.** Quote the line that delivers each D1…Dn.
- [ ] **Length inside the band.** State the word count and the band.
- [ ] **No forbidden phrase** appears (scan the list in `rules.md`).
- [ ] **Last-third density:** the final third is as substantive as the first —
      no thinning, no wrap-up-and-quit.
- [ ] **Imagery on-map:** every image used is on the outline's map; the
      controlling metaphor is layered, not swapped; no mixed metaphors.
- [ ] **Visuals:** every spec has `data=` present in the factsheet and a
      one-sentence message; no unlicensed visual appears.
- [ ] **Provenance:** every factual claim traces to an F-tag.
- **Course mode:** also run the §6 gates from `course.md` — no learner prose
  beyond the one SAMPLE card; every lesson row cites an [Fn] that exists in §E
  and every D-item is covered by a row; every [Vn] in §B exists in §C and every
  chart's `data=` table exists in §D; §H present verbatim; sections A–I present,
  lettered, in order; nothing copied from the format file's examples.

If any item fails, fix and re-CHECK. You may not STOP on a failed CHECK.

## ASK HUMAN
- A deliverable cannot be met because a fact is missing and you will not invent
  it.

## STOP
Hand `draft.md` (or `course-package.md`) to stage 04 — unless `brief.audit` is
`off`, in which case the draft is the final artifact.

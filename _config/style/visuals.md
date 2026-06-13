# visuals.md — when a visual earns its place, and how to spec it

Loads at stages 02 (planning) and 03 (writing the specs), and only when the
brief's `visuals` is `auto` or `on` and the format doesn't veto. A visual is
never decorative. It appears only when it carries a shape that prose can't, and
it appears **beside the claim it proves**.

## 1. The earn-its-place test

| The thing to show | The right form |
|---|---|
| Numbers that have a *shape* (trend, distribution, comparison of magnitudes) | **chart** |
| A *process or structure* (steps, flows, parts and their relations) | **diagram** |
| Side-by-side *attributes* across items | **table** |
| A *cause-and-effect the reader should feel* (interactive contexts only) | **widget** |
| A single idea | **prose** |

If a candidate visual fails this test — if prose would carry it as well or
better — it doesn't earn placement. "It looks nice" is not a reason; visuals are
never decorative. The **widget** row applies only where the medium is
interactive (an app or site) — the `course` format earns widgets; static prose
formats stop at charts, diagrams, and tables.

## 2. The spec syntax (machine-readable, never vague)

Stage 03 emits a spec block, not an instruction to a human. Never "insert a
graph here." Every spec is one pipe-delimited line carrying an `id`, a `data=`
reference to a factsheet table or F-tag, and a one-sentence `message=` (or
`success=` for a widget) stating the single thing the visual proves. This is the
same syntax the course package uses, so a spec is portable across both.

```
CHART:   id=V1 | type=bar|line|scatter|area | x=<axis> | y=<axis> | data=T2 | message="the one sentence this chart must make obvious"
DIAGRAM: id=V2 | mermaid | <fenced mermaid block> | message="the structure this makes clear"
TABLE:   id=V3 | columns=<list> | rows=<from factsheet, each cell sourced> | message="what the comparison reveals"
WIDGET:  id=V4 | type=<slider-model|sorter|calculator|simulation> | inputs=<learner controls> | output=<what updates> | behavior="<the rule the widget enacts>" | success="the learner sees that …"
```

A spec that cannot state its takeaway in one sentence (`message=`/`success=`)
is decoration — cut it.

## 3. The data rule

Every `data=` reference must resolve to something in `factsheet.md` (a table or
an F-tag). A visual spec whose data isn't in the factsheet is a **defect**,
caught at stage 04. Visuals make facts visible; they may not introduce facts.
No number appears in a visual that isn't sourced in the factsheet.

## 4. The placement law

A visual sits **beside the claim it proves** — in the beat that makes that
claim, not collected in an appendix and not floated far from its sentence. The
outline marks which beat each visual serves; stage 03 places the spec there.

## 5. Planning vs. writing (the same split as imagery)

- **Stage 02** marks a beat in the outline as visual when it passes the
  earn-its-place test, noting the intended form and the message:
  `visual: CHART — message="…" — data=<table/F-tag> — beat <n>`
  (form is `CHART`/`DIAGRAM`/`TABLE`, or `WIDGET` for course/interactive runs).
- **Stage 03** writes the full spec for each marked beat, and **only** those.
  It may not introduce a visual the outline didn't license — generation is
  downstream of planning.
- **Stage 04** checks: every spec's data is in the factsheet, every spec has a
  one-sentence message, every spec sits in the beat that makes its claim, and no
  unlicensed visual appears.

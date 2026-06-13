# visuals.md — when a visual earns its place, and how to spec it

*Read at stage 02 (marking beats that should be visual) and stage 03 (emitting
the specs). Loaded only when the brief's `visuals` dial is `auto` or `on`; if
`off`, this file is never opened and the piece is prose throughout. **Visuals are
never decorative** — each one earns its place or it doesn't exist.*

---

## 1. When a visual earns its place

Match the data's shape to the form. If none fits, it stays prose.

| The content is… | Use a… | Because |
|---|---|---|
| numbers with a shape (trend, comparison, distribution) | **chart** | the eye reads the shape faster than the prose can describe it |
| a process or a structure (steps, parts, relationships) | **diagram** | spatial layout carries sequence and connection prose has to spell out |
| several items with parallel attributes | **table** | side-by-side beats interleaved sentences |
| anything else | **prose** | a visual that doesn't beat the sentence is decoration — cut it |

The `auto` dial means *consider* a visual at each marked beat and use one only
where it wins; `on` means actively look for the win; the format may still
**veto** visuals entirely (a plain-text format declares this).

## 2. The placement law

**A visual sits beside the claim it proves.** Not in an appendix, not floated to
the top, not collected at the end. The reader meets the chart at the sentence it
supports. A visual separated from its claim is a stage 04 defect.

## 3. The spec syntax — machine-readable, never vague

Stage 03 does not write "insert graph here." It emits a typed block whose data
**references the factsheet** and whose `message=` states in one sentence what the
visual proves.

**Chart:**
```
CHART:
  type: line | bar | scatter | area
  data: F12, F13, F14        # F-tags from the factsheet — the data must exist there
  x: <axis label>
  y: <axis label>
  message= <one sentence: the single thing this chart shows>
```

**Diagram:**
```
DIAGRAM:
  kind: flow | hierarchy | relationship
  nodes: <list>
  edges: <list, "A -> B">
  message= <one sentence: the structure this makes visible>
```

**Table:**
```
TABLE:
  columns: <list>
  rows: data ref F-tags or literal cells
  message= <one sentence: the comparison this table makes>
```

## 4. The data-provenance rule

Every `data:` reference must point at an `F-tag` that exists in the factsheet. A
visual spec whose data isn't in the factsheet is a **defect** (stage 04 checks
this explicitly) — the same provenance law that governs prose claims governs
visuals. No invented data, ever, not even illustrative.

## 5. One message per visual

If a visual is trying to say two things, it is two visuals or it is prose. The
`message=` line is the test: if you can't write it in one sentence, the visual
hasn't earned its place.

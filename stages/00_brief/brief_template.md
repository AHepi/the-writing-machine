# brief_template.md — the shape of a resolved brief

*Stage 00 writes `output/brief.md` to this shape. Every value here is a literal
or an exact filename — never a pointer, never a category word. The worked
example below is filled so a dumber model can copy it exactly.*

---

## The template

```
# brief.md — <topic, short>

topic:        <one line, the user's subject>
goal:         <one line, what the reader should think/feel/do>

audience:     <exact filename from _config/audiences/, no extension>
format:       <exact filename from _config/formats/, no extension>
length:       <literal word band, e.g. 1,400–1,700 words>
visuals:      auto | on | off
provocation:  none | low | high
audit:        on | off
notes:        <free text, or "none">

deliverables:
- D1: <checkable sentence>
- D2: <checkable sentence>
- ...
- D<n>: length <band>

resolution_log:
- <field>: <what the user wrote> → <what it resolved to> [reason]
- ...
```

---

## Worked example

```
# brief.md — why rent control backfires

topic:        the effects of rent control on housing supply
goal:         the reader should understand why price caps can worsen the shortage they aim to fix
audience:     general
format:       essay
length:       1,400–1,700 words
visuals:      auto
provocation:  low
audit:        on
notes:        must address the fairness argument for tenants; avoid jargon

deliverables:
- D1: states the thesis (rent control reduces supply) in the opening section
- D2: steelmans and answers the tenant-fairness counterargument
- D3: explains the supply mechanism with a concrete example, no economics jargon undefined
- D4: length 1,400–1,700 words

resolution_log:
- audience: (blank) → general [default applied]
- format: (blank) → essay [default applied]
- length: (blank) → 1,400–1,700 words [essay format norm]
- provocation: "make it have a clear view but stay fair" → low [resolved from notes]
- D3: derived from notes "avoid jargon" + must-include "supply mechanism"
```

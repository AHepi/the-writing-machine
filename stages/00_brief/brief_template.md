# brief_template.md — the form, and the resolved brief

## The user-facing form (what a human fills, or pastes loosely)

```
topic:  what is this about?
goal:   what should the reader think, feel, or do afterward?
```

That is the whole mandatory surface. Everything below is optional; touch a field
only to override its default.

```
audience:     general          (smart layperson, never talked down to)
format:       essay            (general-purpose prose piece)
length:       the format's own norm
visuals:      auto             (used where they aid understanding; format can veto)
provocation:  none             (none | mild | sharp)
audit:        on
notes:                         (free text: must-includes, must-avoids, anything)
```

---

## The resolved brief (what stage 00 writes to output/brief.md)

Every field is a literal, legal value. No pointers, no "(default)". This is the
single source of truth for stages 01–04.

```
# brief.md — <topic, short>

topic:        <verbatim or lightly cleaned from the user>
goal:         <verbatim or lightly cleaned>
audience:     <existing filename slug, e.g. socialist>
format:       <existing filename slug, e.g. essay>
length:       <literal band, e.g. 1,200–1,800 words>
visuals:      <auto | on | off>
provocation:  <none | mild | sharp>
audit:        <on | off>
notes:        <verbatim free text, or "none">

deliverables:
- D1: <thesis/opening requirement>
- D2: <strongest counterargument addressed>   (if the format calls for it)
- D3: <must-include from notes>
- D4: length <low>–<high> words
- D5: <any remaining format-required part>

resolution_log:
- audience: "<user words>" → <slug>  (semantic match)
- format: empty → essay  (default)
- length: → <band>  (from format norm)
- visuals: → auto  (default)
- <one line per substitution or default applied>
- flags: <any fuzzy value that fell back to a default for lack of a match; or "none">
```

---

## Worked example

```
# brief.md — four-day work week

topic:        the four-day work week
goal:         leave a skeptical manager believing it's worth piloting
audience:     conservative
format:       oped
length:       650–900 words
visuals:      off
provocation:  mild
audit:        on
notes:        must address productivity worries; avoid utopian framing

deliverables:
- D1: states the thesis (worth piloting) in the first two sentences, on a news peg
- D2: names and answers the strongest objection (productivity loss)
- D3: addresses productivity worries directly  (from notes)
- D4: avoids utopian framing  (from notes)
- D5: length 650–900 words
- D6: closes on a demand to pilot, no summary  (op-ed required part)

resolution_log:
- audience: "a skeptical manager, small-business conservative type" → conservative  (semantic match)
- format: "newspaper opinion piece" → oped  (semantic match)
- length: → 650–900 words  (op-ed norm)
- visuals: "keep it text only" → off
- provocation: "a bit provocative is fine" → mild
- flags: none
```

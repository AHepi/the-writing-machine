# rules.md — the law every piece obeys

These rules outrank format, audience, and style files when they conflict. They
are written to be checked: stage 03 obeys them, stage 04 audits them. The
*content* of the voice rules is yours to make sound like you (this is a
`[content: you]` file); the structural laws below should not be loosened
without knowing why.

---

## §respect-floor — write to the ceiling, never the floor

Write to the top of the audience's ability, not the bottom. **New to the topic
is not new to thinking.** Every audience profile (`§3 Register and assumed
knowledge`) declares what its readers already know; you may not re-explain it.
Re-explaining the known is condescension, and condescension is a defect, not a
courtesy.

The Pinker stance supplies the posture by construction: classic style treats
the reader as an equal who simply hasn't seen this particular view yet. That is
the opposite of talking down. Hold it for every audience — the child and the
economist alike get the respect of being addressed at their own ceiling.

Expert audiences flip the same machinery: denser register, citations expected,
basics forbidden. The floor and the ceiling move together; the respect is
constant.

## §deliverables — the bare minimum is a failure state

The deliverables block (D-tags) in the brief defines the piece. The law:

> **Output matches the deliverables exactly — nothing missing, nothing padded.**

A missing D-item is the obvious failure. A *padded* piece is the quieter one:
words added to hit a feel rather than a deliverable, sections inflated because
the writer mistook length for thoroughness. Both fail. Length lives inside its
declared band; every D-item is present; no D-item is exceeded into bloat.

## §no-laziness — the anti-shortcut spine

"Long form" was never a format; it was the absence of shortcuts. These shortcuts
are forbidden, and stage 03's contract names them again at the point of writing:

- **Compressing later sections as the draft grows.** The last third is written
  at the density of the first. Fatigue is not an excuse the reader can see.
- **Summarizing instead of writing.** No "the remaining sections follow,"
  no "and so on," no trailing-off.
- **Wrapping up early.** No "in summary," no "in conclusion" as a way to stop
  thinking. A piece ends because it is finished, not because the writer tired.

## §forbidden-phrases

Banned in any output artifact (draft and final):
- "in summary"
- "in conclusion"
- "the remaining sections follow" / "the rest follows similarly"
- "and so on"
- "similarly," used to skip writing a section out
- "insert <X> here" / "<chart goes here>" — visuals get real specs (see
  `_config/style/visuals.md`)
- "delve," "tapestry," "in today's fast-paced world," and other AI-tell
  filler (extend this list as you spot offenders)

## §provenance — facts carry their source

Every factual claim in the draft traces to an F-tag in the factsheet, which
names an S-tag in `sources.md`. A claim with no traceable source is a defect.
Do not invent citations; if a needed fact is missing, flag it (`ASK HUMAN`)
rather than paper over it.

## §imagery-and-visuals — only what was planned

No metaphor, analogy, meme, chart, diagram, or table appears in the draft
unless the outline licensed it (stage 02). Generation is downstream of planning,
always. The detailed rules live in `_config/style/imagery.md` and
`_config/style/visuals.md`; the law here is just: **nothing off the map.**

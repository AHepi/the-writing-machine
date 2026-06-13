# Stage 01 — Research

*Contract. Runs after stage 00. Reads the resolved brief, gathers the facts the
piece will stand on, and tags each one. Produces no prose for the reader — only
findings and their sources. Every fact earns an **F-tag** here; that tag travels
the rest of the pipeline.*

**Read order:** your Layer 0 card → `../../CONTEXT.md` → this file.

---

## READ

- `../00_brief/output/brief.md` — the resolved brief. Note the `topic`, `goal`,
  `deliverables`, and `audience` (research at the depth the audience's assumed
  knowledge demands — don't gather what §3 says they already know).
- `references/research-method.md` — how to search, weigh, and tag.
- (Tier C: receive these as one assembled prompt per `assembly-order.md`.)

## INTERNALIZE

You are building the evidence base, not the argument. Gather what's true and
relevant to the goal and the D-list; leave selection and shaping to stage 02.
Over-gather slightly — stage 02 will cut — but every fact must be real and
sourced. No invented data enters here or anywhere.

## TRANSFORM

- Search the topic against the goal and each D-item. For each D-item, ask: what
  facts would let the draft satisfy this?
- For every fact worth keeping, assign an **F-tag** (`F1`, `F2`, …) and record
  the source.
- Note each source's reliability now (primary/peer-reviewed → strong; reputable
  secondary → medium; single blog/anecdote → weak). Stage 02 turns this into the
  formal **S-register**.
- Flag contested facts — where good sources disagree — explicitly. The draft
  will need to handle them honestly.

## WRITE

- `output/findings.md` — the facts, each as: `F<n>: <claim> [source ref]`.
  Group loosely by the D-item or theme they serve. Mark contested facts.
- `output/sources.md` — one entry per source: ref, what it is, a one-line
  reliability note. Every F-tag's source ref resolves to an entry here.

## CHECK

- [ ] Every D-item in the brief has at least one F-tagged fact that could
      support it (or a flagged gap, if the fact doesn't exist).
- [ ] Every fact has an F-tag and a source ref.
- [ ] Every source ref in `findings.md` has an entry in `sources.md`.
- [ ] Contested facts are marked, not silently resolved.
- [ ] No invented or unsourced fact appears.

## STOP

Hand off to stage 02. If a D-item has no supporting fact and none exists, leave
the gap flagged in `findings.md` and `ASK HUMAN` — do not let stage 03 paper over
it later.

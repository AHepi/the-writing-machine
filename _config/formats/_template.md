# _template.md — format schema (with worked example)

*Copy this file to create a new format. Fill all sections. Save as
`<format-id>.md` (lowercase, hyphens) in `_config/formats/`. The filled example
below is part of the contract — a template plus an example is executable by a
much dumber model than a template alone.*

---

## The schema

```
# <format-id>.md — <one-line description>

## 1. What it is        the form, in a sentence
## 2. Length norm       the default word band (used when brief.length is empty)
## 3. Structure         the required parts, in order — these seed the D-list
## 4. Register defaults  how formal; first vs third person; how it opens and closes
## 5. Visuals policy    auto | encouraged | vetoed — may this format carry charts/tables?
## 6. Memes & heat      what the format permits (composes with the audience file)
## 7. Done-when         the format-specific completeness test
```

Section 3 is load-bearing: stage 00 turns "the format's required parts" into
`D-tags`, so the structure here becomes enforced deliverables.

---

## Worked example — `explainer.md`

```
# explainer.md — the neutral how-it-works piece

## 1. What it is
A piece that makes one complicated thing understandable, taking no side.

## 2. Length norm
800–1,200 words.

## 3. Structure
- Hook: the concrete question the reader has.
- The short answer, up front.
- The mechanism, built one step at a time.
- One worked example.
- What people get wrong about it.
- Close: what to do with the understanding.

## 4. Register defaults
Plain, warm, third person. Opens on the reader's own question; closes on use,
not summary.

## 5. Visuals policy
Encouraged — process diagrams and comparison tables earn their place here often.

## 6. Memes & heat
Heat low by default; memes only if the audience file permits. Neutrality is the
point.

## 7. Done-when
A reader who couldn't explain the thing now can, in two sentences.
```

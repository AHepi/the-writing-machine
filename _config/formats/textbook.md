# textbook.md — the from-zero crash course

*A long, didactic piece that takes a reader who knows nothing about a subject and
walks them, chapter by chapter, to a real working understanding. Unlike
`course.md`, this is **not** a generator for a downstream builder — it is the
finished thing a human reads. It is built to be rendered by the **`tufte-pdf`
skill**, so it can carry margin sidenotes, clean mathematics, and boxed asides.*

## 1. What it is

A self-contained crash course in prose: a book-shaped explainer with chapters,
each one assuming only what the earlier ones established, that turns a curious
beginner into someone who can explain the subject's core ideas in their own
words. It teaches; it does not merely survey.

## 2. Length norm

6,000–9,000 words (≈ 18–28 pages in the Tufte PDF). Used literally when
`brief.length` is empty. The length is in service of completeness, not padding:
every chapter built to the same density — the last as carefully as the first.

## 3. Structure

These parts are required and in order; stage 00 turns them into D-tags.

- **Title block** — a `# Title`, a one-line `<span class="subtitle">…</span>`,
  and a short "what you'll be able to do by the end" promise (seeds `D1`).
- **Chapter 1 — the hook and the question.** Opens on a concrete puzzle the
  reader already feels, and names the question the whole course answers.
- **Body chapters**, each one:
  - builds a single idea, assuming only what earlier chapters established
    (strict prerequisite order — seeds `D2`);
  - grounds it in a worked everyday analogy from the audience's world;
  - defines every new term in plain words on first use;
  - where notation genuinely helps, carries a **"math, gently" box**
    (`<div class="tk-box">`) that introduces it and names every symbol — math is
    always optional scaffolding for the idea, never a gate in front of it;
  - uses **margin sidenotes** (markdown footnotes) for definitions, caveats, and
    asides, keeping the main line of thought clean;
  - ends with a one-paragraph **recap** of what the reader can now do.
- **A closing chapter** — what the whole thing adds up to, and honestly, what is
  still open or contested (seeds `D3`: intellectual honesty about the frontier).
- **Glossary** — every defined term, one line each (seeds `D4`).
- **Further reading** — where to go next, F-tagged to real sources (seeds `D5`).

## 4. Register defaults

Warm, plain, patient; second person where it helps ("you can picture…"). Formal
enough to be trusted, conversational enough to keep a beginner walking. Opens
every chapter on something concrete; closes on understanding gained, never on
"in this chapter we learned." Never talks down (see the audience's respect
floor).

## 5. Visuals policy

`encouraged` — simple diagrams and comparison tables earn their place often, and
mathematics is typeset cleanly by the renderer. All visuals follow `visuals.md`
(a visual that doesn't beat prose is cut) and respect the brief's `visuals` dial;
each sits beside the claim it serves. Rendered via the **`tufte-pdf` skill**, not
the basic reportlab renderer.

## 6. Memes & heat

Memes off. Heat low — the energy comes from genuine wonder and the snap of a
counter-intuitive truth, governed jointly by the audience file and the
`provocation` dial.

## 7. Done-when

A reader who started knowing nothing can, at the end, state the subject's core
ideas in their own words and say honestly what is settled and what is still
open. Every chapter is built to full density (no "the remaining topics follow
similarly"), every term is in the glossary, every symbol that appears was
explained, and the length is inside the band.

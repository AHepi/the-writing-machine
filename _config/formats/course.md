# Format: course — Handoff Package Generator

The output of this format is not a course, and it is not this file. Each run **generates** a fresh, one-file handoff package — `course-package.md` — customized to that run's subject and audience. The package is consumed by a downstream builder: a human, or another LLM that is adding content to an app or website. Pasted into that builder's prompt, the package supplies everything it needs to write and assemble the course — the breakdown of this subject, the visual directives for this data, the tone for this audience, the imagery chosen for both, the facts and sources behind all of it, and the style law that makes the builder's prose match. This file is the mold; the package is the casting. Nothing learner-facing is written here.

Three kinds of material flow into every package, and the distinction governs everything below:

- **[GENERATED]** — produced fresh per run, from this subject's facts and this audience's profile
- **[TEMPLATE]** — fixed rules in this file that are copied into the package, because the builder must obey them too
- **[VERBATIM]** — the style core in §5, which travels into every package unchanged

All numbered sections are addressable as §1–§6.

## 1. Trigger and inputs

Use when the resolved brief says `format: course`, or the goal names teaching, training, curriculum, onboarding, or supplying content to an app or site.

Stage 03 inputs in course mode, beyond the standard set: `_config/style/visuals.md` (all), `_config/style/imagery.md` (all), the audience profile (all). Context policy: whole files; this format is exempt from token thrift and from the 400-token format-file budget.

## 2. What stage 03 does in course mode

It does not write prose for learners. It writes the specification and materials *for* writing:

1. Transform `outline.md` into a content breakdown — the module → lesson map for this subject, each lesson wired to its facts and visuals.
2. Convert the outline's visual marks into full directives, wired to data tables built from the factsheet.
3. Distill the audience profile into tone instructions the builder can obey without ever seeing the profile.
4. Carry the outline's Imagery block forward as a repertoire with its usage rules attached.
5. Attach the factsheet, the data tables, and the source register whole.
6. Embed the style core verbatim.
7. Write one SAMPLE card for module 1 only — so the builder calibrates voice and depth — and nothing else in a learner's voice.

## 3. The package — generate exactly these sections, lettered, in order

**A. BUILD NOTES** [generated from a fixed template] — ≤10 lines. What this package is; that it complements the builder's own prompt; that §B's prerequisite order is binding while screen layout is the builder's; that §H binds all copy the builder writes; that nothing outside this file is required.

**B. CONTENT BREAKDOWN** [GENERATED] — the curriculum for this subject as a table: module | lesson | the idea (one line) | facts used [Fn] | visual [Vn] | hook suggestion (≤1 line) | prerequisites. Derived from the outline; ordering is given-before-new at curriculum scale — no lesson uses a concept an earlier lesson hasn't introduced.

Example of one generated row:

```
| M2 | L3 | Rate rises transfer income from mortgaged households to savers | F4, F7 | V2 | "Your landlord's bank statement, before and after the hike" | M1.L2 |
```

Followed by the **architecture laws** [TEMPLATE], copied so the builder writes to them: one idea per card, 40–150 words; every lesson runs HOOK → CONCEPT → EXAMPLE → CHECK, with checks phrased as predictions or tasks, never "did you understand?"; modules are 3–7 lessons, opening with why-this-matters, closing with a one-line-per-lesson recap; the final module is written at the depth of the first — fading effort is a defect.

**C. VISUAL DIRECTIVES** [GENERATED] — every chart, diagram, table, and widget this subject's content earned, in machine-readable spec syntax:

```
CHART:   id=V1 | type=bar|line|scatter | x=<axis> | y=<axis> | data=T2 | message="the one sentence this chart must make obvious"
DIAGRAM: id=V2 | mermaid | <fenced mermaid block> | message="…"
WIDGET:  id=V3 | type=<slider-model|sorter|calculator|simulation> | inputs=<learner controls> | output=<what updates> | behavior="<the rule the widget enacts>" | success="the learner sees that …"
```

Every spec carries its `message=` or `success=`; a visual that cannot state its takeaway in one sentence is decoration — cut it. Chart data lives once, in §D, referenced by table id. Include the **decision table** [TEMPLATE] so the builder can add visuals correctly: numbers with a shape → chart; process or structure → diagram; side-by-side attributes → table; a cause-effect the learner should feel → widget; a single idea → prose, because visuals are never ornament. Placement law: the visual sits after the CONCEPT it serves, before the CHECK.

**D. DATA TABLES** [GENERATED] — render-ready markdown tables, ids T1, T2…, every row sourced [Sn]. The single home of all numbers in the package.

**E. FACT SHEET** [GENERATED] — the F-register from stage 02, whole. The builder writes from these facts and no others; anything it wants to add, it flags for human approval rather than inventing.

**F. TONE INSTRUCTIONS** [GENERATED + TEMPLATE] — ≤12 lines distilled from the audience profile: who the learner is, what they already know (which the builder must never re-explain), register and vocabulary, what reads as talking down to this audience specifically. Plus the fixed bans: second person, present tense; no exclamation-mark enthusiasm; no "simply / just / easy"; no congratulation filler; encouragement only as information — end each module by naming what the learner can now do that they couldn't before.

**G. IMAGERY REPERTOIRE** [GENERATED + TEMPLATE] — the controlling metaphor chosen at stage 02 from this audience's world, its planned extension module by module, and every licensed supporting analogy or meme, each with the lesson it serves. Plus the usage rules: the controlling metaphor unfolds — introduced at its simplest in module 1, extended, never replaced; supports live in the same source domain or one this section declares compatible; nothing off this map appears in any card; an image is explained at most once, at first use; the condescension gate — would this audience use this image among themselves? — applies to anything the builder adds.

**H. STYLE GUIDE** [VERBATIM] — the STYLE-CORE block from §5, markers removed. It binds the cards the builder writes and every line of connective copy around them, so the seams never show.

**I. SOURCES** [GENERATED] — the S-register from research, in full.

## 4. Customization rules — what varies with what

The **subject** decides §B's breakdown, §C's visuals, §D's data, §E's facts. The **audience** decides §F's tone, §B's hooks and examples, §G's source domain. **Nothing** decides §H, the architecture laws, the spec syntax, or the section order — these are the invariants that let any builder consume any package the same way. When generating, never copy this file's examples into a package; every generated line answers to the run's brief, or it is filler.

## 5. STYLE-CORE — the verbatim cargo

<<<STYLE-CORE — Pinker, condensed

Prose is a window: the writer has seen something, and the words exist to let the reader see it too. Write about the subject, never about the writing — no "in this section," no "it's important to note," no narrating what the text is about to do.

Hedges either carry content or die. "Roughly 30%" informs; "somewhat significant" insures the writer. Commit to what the evidence supports.

Prefer the concrete to the abstract. After any general claim, give the instance that makes it visible. One example outperforms a paragraph of definition.

Use verbs, not their embalmed nouns: assess, not "make an assessment of"; agree, not "is in agreement with."

Keep each sentence's subject close to its verb. Put light phrases before heavy ones. End the sentence on its strongest element — the stress position is the last slot.

Begin sentences with what the reader already has; end them with what is new. This one ordering rule does more for flow than any transition word.

One name per thing. Do not rotate synonyms for the same referent; the reader must not wonder whether "the measure" is "the policy."

State things positively. Use a negation only to deny something the reader plausibly believes.

No clichés, no stock intensifiers — "crucial," "game-changer," "delve," "navigate the landscape." Say it plainly or find a fresh image.

Vary sentence rhythm. Follow a long, unspooling sentence with a short one. Like this.

Before finishing, check: opening sentence deletable? Delete it. Every abstraction within reach of an example? Every claim committed? Then stop.

STYLE-CORE>>>

## 6. CHECK — gates on the generated package, appended to stage 03's CHECK

- [ ] No learner-facing prose anywhere except the single SAMPLE card; the package instructs, it does not pre-write the course
- [ ] Every lesson row cites at least one [Fn]; every cited [Fn] exists in §E; every D-item from the brief's deliverables is covered by some lesson row
- [ ] Every [Vn] in §B exists in §C; every chart's `data=` table exists in §D; every spec carries `message=` or `success=`
- [ ] §F names what this audience already knows; §G declares exactly one controlling metaphor and only same-or-compatible-domain supports
- [ ] §H present verbatim; sections A–I present, lettered, in order
- [ ] Nothing in the package is copied from this file's examples

# course.md — format: course (a generator, not a product)

## What makes this format different

Every other format produces a finished piece of writing at stage 03. This one
does not. **The course format is a generator.** When a run uses
`format: course`, stage 03 does not write a course — it writes a
**`course-package.md`**: a self-contained, subject-customized handoff that a
*downstream builder LLM* uses to construct the actual course.

The static file you are reading is **the mold**. The `course-package.md` a run
emits is **the casting** — the same shape every time, but filled with this
subject's breakdown, this subject's data, this subject's imagery. The builder
LLM that receives the package needs nothing else: not this workspace, not the
brief, not the factsheet. The package is the whole contract.

This is the answer to "course output as a self-contained handoff for another
LLM." The handoff is not a course; it is everything required to build one,
written so a model that has never seen this workspace can execute it.

---

## The format schema (filled, as the mold)

## 1. What it is / when to use
A multi-module learning experience on a subject, built for a learner to work
through. Use when the goal is durable understanding and capability, not a single
read — when the reader should come out *able to do or reason about* something,
across several sessions.

## 2. Required parts  (→ deliverables)
A course run's deliverables are the package's required blocks (below). At
minimum:
- A learning-objective spine (what the learner can do at the end, working
  backward to module objectives).
- A module breakdown with explicit prerequisites and ordering.
- A visual spec set and a data-table set the builder will render.
- A tone-and-register instruction matched to the audience.
- An imagery repertoire (controlling metaphor + supports) the builder may draw
  from and may not exceed.
- The Pinker prose core, inlined, so the builder writes well without this
  workspace.

## 3. Length norm
The *package* is as long as the subject's breakdown requires — completeness, not
brevity, governs (the bare-minimum law in `rules.md` still applies: every block
present, nothing padded). The eventual *course* length is set by the package's
module count and per-module targets, not here.

## 4. Visuals policy
auto, leaning **on**. Courses teach; visuals teach well. The package carries
real visual specs (per `visuals.md` syntax) the builder renders verbatim —
never "add a diagram here."

## 5. Conventions & register
The package is written as **directives to a builder**, not prose to a reader:
imperative, unambiguous, machine-followable. The *course* the builder produces
inherits the audience's register and the Pinker core.

## 6. Imagery & meme licensing
The package hands the builder a closed imagery repertoire (controlling metaphor
+ beat-mapped supports from the audience's world). The builder may use items
from it and may not invent new ones — generation stays downstream of planning,
even across the handoff. Memes per audience+format as usual.

---

## The `course-package.md` template — what stage 03 emits

Stage 03, for a course run, fills this template from `brief.md`, `factsheet.md`,
and `outline.md`, and writes it to `stages/03_write/output/course-package.md`.
Every `<...>` is replaced with subject-specific content. No placeholders survive
into the emitted package.

```
# Course Package — <subject>
*A self-contained handoff. You are the builder LLM. Build the course described
below using only this file. Do not summarize; produce every module in full.*

## 0. Builder directives (read first)
- Produce the course in full. The forbidden phrases in §7 apply to your output.
- Use only the imagery in §6. Render the visuals in §4 exactly as specified.
- Match the register in §5. Write to the learner's ceiling (see §5).
- Completion ritual: before you stop, confirm every module objective in §2 is
  met, with one line of evidence each.

## 1. Learning objectives (the spine)
- Terminal objective: <what the learner can do at course end>
- Module objectives: <O1…On>, each a can-do statement, ordered by prerequisite.

## 2. Module breakdown
For each module M1…Mn:
- M<k>: <title>
  - objective: <O…>
  - prerequisites: <which earlier modules / assumed knowledge>
  - beats: <ordered teaching beats; each maps to a fact or visual below>
  - target length / time: <e.g. ~1,200 words / ~15 min>

## 3. Data tables (the facts the builder may use)
Each table is closed and sourced. The builder states no number absent here.
- T<k>: <name> | columns | rows | source S-tag from the factsheet

## 4. Visual specs (render verbatim)
Per visuals.md syntax. Example:
  CHART id=V1 type=line
    data=T2
    message="<the one thing this chart proves>"
    x=<col> y=<col>
  DIAGRAM id=V2 kind=flow
    nodes=<...> edges=<...>
    message="<the structure this makes clear>"

## 5. Tone & register instructions
- Audience: <name>. Assumed knowledge (do NOT re-explain): <list from the
  audience profile §3>.
- Register: <reading level / sentence weather>.
- Respect floor: write to the ceiling; re-explaining the known is a defect.

## 6. Imagery repertoire (closed set)
- Controlling metaphor: <metaphor>, from <audience source domain>.
- Supporting analogies: <A1…>, each mapped to the module/beat it serves.
- Layering note: <how the controlling metaphor is introduced simply early and
  extended as complexity grows — never replaced>.
- Memes: <licensed? which? or "none">.

## 7. The Pinker core (prose floor, inlined)
<the full contents of _config/style/pinker-core.md, pasted here so the builder
needs nothing else>

## 8. Forbidden phrases
<the list from rules.md §forbidden-phrases, pasted>
```

---

## How a course run flows through the pipeline

- **Stage 00** resolves `format: course`, picks the audience, and writes
  deliverables that *are* the package's required blocks.
- **Stage 01** researches the subject as normal — F-tags and S-tags feed §3/§4.
- **Stage 02** plans the module breakdown as the outline, and plans the imagery
  repertoire (§6) and visual specs (§4) the same way it does for any piece.
- **Stage 03** fills the package template above — it does not write course
  prose. Output: `course-package.md`.
- **Stage 04** audits the package: every required block present, every visual
  spec's data present in §3, the imagery repertoire closed and complementary,
  no forbidden phrase, deliverables met. The final artifact is the validated
  package, ready to hand to the builder LLM.

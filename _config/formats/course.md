# course.md — the course generator (a generator, not a product)

*This format is different in kind from the others. The essay, op-ed, and
newsletter formats describe a piece you write. This one describes a **package you
emit for a downstream builder LLM to turn into a course.** The static file is the
mold; each run casts a subject-customized `course-package.md`. You are not
writing the course. You are writing the fully-specified handoff that lets another
model write it — self-contained, no pointers, nothing assumed.*

---

## 1. What it is

A generator. When the brief's `format: course`, the pipeline does not produce
prose for a human reader at stage 03 — it produces **`course-package.md`**: a
single self-contained file that a separate builder LLM can execute into a full
course with no access to this workspace. Everything the builder needs is cast
into the package; every pointer is already resolved.

## 2. Length norm

The **package** is bounded, not the course. Target a package of 1,500–3,000
tokens — dense, complete, no prose padding. The course it generates is as long
as its module breakdown demands; that is the builder's output, not ours.

## 3. Structure — what the cast `course-package.md` must contain

Stage 03, running this format, emits these blocks in order. Each is filled from
the brief, factsheet, and outline — never left as a pointer.

```
# course-package.md — <subject>

## A. Subject & goal
   the resolved topic and goal, verbatim from brief.md

## B. Audience & register
   the FULL resolved audience profile, pasted in (not referenced):
   reading level, assumed knowledge (the do-not-re-explain list), the
   condescension test for this audience. The builder must never re-explain
   what §B says the learner already knows.

## C. Breakdown directives
   how to split the subject into modules and lessons:
   - module count and the principle of division (by concept? by skill? by
     chronology?)
   - per-module: a learning objective stated as something the learner can DO
   - sequencing rule: each lesson assumes only what earlier ones established
   - the anti-laziness spine: every module fully built, last module at the
     density of the first; "the remaining modules follow similarly" is forbidden

## D. Data tables
   every fact the course may use, pasted from the factsheet with its F-tag and
   S-register. The builder may use ONLY these facts — same provenance law as the
   prose pipeline. No invented data.

## E. Visual specs
   the charts/diagrams/tables the course should carry, in the CHART:/DIAGRAM:/
   TABLE: syntax from visuals.md, each with a data reference into §D and a
   one-sentence message=. Placement law: each visual beside the claim it proves.

## F. Imagery repertoire
   the controlling metaphor drawn from this audience's world, the compatible
   domains, the supporting analogies mapped to modules, any licensed meme.
   The builder renders exactly this set — nothing off the map (imagery.md).

## G. Tone instructions
   the register defaults, the provocation level, what counts as talking down to
   THIS learner, and the honesty gate.

## H. The Pinker core
   the full text of pinker-core.md, pasted in. This is the prose floor the
   builder's every sentence must clear. Pasted, not referenced — the builder has
   no access to this workspace.

## I. Completeness contract
   the D-list for the course: what the finished course must contain, the failure
   modes forbidden by name, and a CHECK the builder runs before it declares done.
```

## 4. Register defaults (of the package itself)

Imperative and machine-facing. The package talks to a builder LLM, not a human
learner — it gives directives, specs, and pasted-in resources, not prose. Every
section is self-contained: a builder with only `course-package.md` and no other
file can execute it completely.

## 5. Visuals policy

The package always carries §E (visual specs) — a course without visuals is rare.
But the specs follow `visuals.md` exactly, including the rule that a visual which
doesn't beat prose is cut. The dial still applies: `visuals: off` shrinks §E to
tables only.

## 6. Memes & heat

Governed by §F and §G of the package, themselves set by the audience and the
`provocation` dial — same joint license as every other format.

## 7. Done-when

The package is done when a downstream builder LLM, handed **only**
`course-package.md`, could build the entire course without a single question and
without access to this workspace: every fact pasted with provenance, every
pointer resolved, every visual specified, the prose floor included, and the
completeness contract explicit. The mold is complete when the casting needs no
touch-up.

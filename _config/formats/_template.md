# _template.md — how to write a format profile

A format profile tells the pipeline *what shape the piece takes and what counts
as complete.* Six sections, all required. Copy this file, fill every section,
save as `<slug>.md`. A filled example follows the blank schema.

A run reads **exactly one** format file, so each is self-contained. The format's
`## 2. Required parts` and `## 3. Length norm` feed stage 00's deliverables
block directly — they become D-tags.

---

## The schema

```
# <slug>.md — format: <name>

## 1. What it is / when to use
One paragraph. The shape, and the situation it's the right answer to.

## 2. Required parts  (→ deliverables)
The structural must-haves. Each becomes a D-tag in the brief. Be specific
enough that "present or absent" is decidable at audit.

## 3. Length norm
The default band (words). Overridable by the brief's length field.

## 4. Visuals policy
auto | veto. Whether this format admits charts/diagrams/tables at all, and
any format-specific rule (e.g. "tables yes, charts no").

## 5. Conventions & register
Structural and tonal conventions of the format: openings, paragraph rhythm,
headings, how it ends (never with a banned summary phrase).

## 6. Imagery & meme licensing
What imagery suits the format, and — jointly with the audience — whether memes
are licensed here. (Reddit: yes. Op-ed: no.)
```

---

## Worked example (filled)

```
# explainer.md — format: explainer

## 1. What it is / when to use
A piece whose whole job is to make one complicated thing clear. Use when the
goal is understanding, not persuasion — the reader leaves knowing how something
works, not what to think about it.

## 2. Required parts  (→ deliverables)
- Opens with the question the reader actually has, in their words.
- Builds one layer at a time; no layer assumes a later one.
- Resolves the question explicitly before ending.
- Each technical term defined the first time it does work (per audience's
  assumed-knowledge floor).

## 3. Length norm
900–1,500 words.

## 4. Visuals policy
auto — strongly favored. A process → diagram; numbers with shape → chart; a
comparison → table. This format earns its visuals more than most.

## 5. Conventions & register
Calm, confident, building. Headings optional; if used, they are signposts not
filler. Ends on the click of understanding, never on "in summary."

## 6. Imagery & meme licensing
One controlling metaphor carried throughout (per imagery.md). Memes: only if the
audience licenses them and they clarify rather than decorate; default no.
```

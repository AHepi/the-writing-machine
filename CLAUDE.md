# CLAUDE.md — Layer 0 for Claude

*Claude's model card. Auto-loaded by Claude Code from the repository root.
Every other model gets a card in `_navigation/models/`; Claude's lives here
because Claude Code reads this path first. Same schema, privileged position.*

## 1. Entry

Read order: **this card → `CONTEXT.md` → your stage contract**.

This is the Writing Workspace. It turns a two-line brief into a finished,
audited piece of writing by walking it through five stages. Each stage is a
contract: a small markdown file that tells whoever runs it exactly what to
read, what to produce, and how to check its own work. You do not improvise the
pipeline; you execute contracts.

If the user hands you a topic and a goal, you are running the **pipeline**
(start at stage 00). If the user says "add an audience / format / model" or
reports a recurring model failure, you are doing **maintenance** — route via
`CONTEXT.md`'s second table.

## 2. Inherits

Tier **A** (`_navigation/tiers.md`) — full capability: long context, reliable
instruction-following, honest self-checking, web search when available.

## 3. Strengths — what to exploit

- **Long, faithful context.** You can hold the whole stage's inputs at once;
  you do not need pre-chewed LITE files. Read the full contract and the full
  config it points at.
- **Pointer resolution.** You may resolve `{brief.field}` pointers and fuzzy
  user input — this is what makes you legal to run **stage 00**, the
  canonicalizer. Lesser models may not.
- **Honest CHECK.** You can run a completion ritual and report unmet
  deliverables truthfully rather than papering over them. Do.
- **Maintenance.** You can mint new audience, format, and model files from the
  templates and contracts without breaking existing runs.

## 4. Weaknesses & countermeasures

- *Helpfulness drift — softening a hard brief, smoothing a sharp register.*
  → The audience profile and `rules.md` are binding. If the brief says
  `socialist` and `provocation: high`, you write to that register, not to a
  median inoffensive default.
- *Over-explaining to look thorough.* → Respect floor (`rules.md`): write to
  the audience's ceiling. New to the topic is not new to thinking. Never
  re-explain what §3 of the audience profile says they already know.
- *Inventing scope.* → Stage 03 may only render images and visuals the outline
  licensed; stage 02 may only use facts the factsheet carries. Generation is
  always downstream of planning.

## 5. Context policy

**Thrift OFF by default, but you choose per stage.** You have the window to
load files whole and the discipline not to need restated anchors. When running
a small stage (00, 04) load everything; when a stage's `CONTEXT_LITE.md`
exists, you may use it to save tokens on a paid run, but you are never
*required* to. Token thrift is a per-model policy, not a virtue — see
`tiers.md` §Budgets.

## 6. Stage permissions

**All stages, 00–04**, plus all maintenance routes. You are the only model
assumed able to run stage 00 (canonicalization) and stage 04 (audit) unaided.

## 7. Quirk log

*Append-only. Add a dated line after any observed failure, then tighten the
countermeasure above it.*

- (none yet)

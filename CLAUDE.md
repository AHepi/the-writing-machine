# CLAUDE.md — Layer 0 for Claude

You are Claude, working inside the Writing Workspace. This file is your model
card: it answers the only Layer 0 question — *where am I, and how should I,
specifically, operate?* Claude Code auto-loads this path, so it is the first
thing you see. Every other model gets its own card under
`_navigation/models/`; this one is yours.

## 1. Entry
Read order: **this card → `CONTEXT.md` → the contract for the stage you are
running.** Do not load the whole workspace. `CONTEXT.md` routes you; the stage
contract tells you exactly which files to read.

## 2. Inherits
Tier **A** (frontier capability) from `_navigation/tiers.md`. You may run any
stage, navigate pointers, and mint new library files unaided.

## 3. Strengths
- Long context: you can hold a full stage's inputs at once.
- Instruction fidelity: you follow multi-step contracts without drift.
- Search and synthesis: stage 01 research is yours to run well.
- Honest self-checking: you can run a CHECK against your own output and fail
  yourself when you should.

## 4. Weaknesses & countermeasures
- *Eagerness to please by over-delivering* → obey the deliverables block
  exactly. Nothing missing, **nothing padded**. A piece longer than its band
  is a defect, not generosity.
- *Smoothing over gaps* → when a fact is missing, tag it and flag it (`ASK
  HUMAN`); never invent a citation or paper over an unknown with confident
  prose.
- *Drifting register friendly* → match the audience profile's assumed
  knowledge. Re-explaining what the audience already knows is condescension;
  see `_config/rules.md` respect floor.

## 5. Context policy
**Thrift ON.** Use scoped §-reads — read only the sections a contract names.
You have the window to load whole files, but the discipline of scoped reads
keeps your runs reproducible against the same contracts the smaller models use.
Override to whole-file loads only when a contract says so.

## 6. Stage permissions
All stages: **00 → 01 → 02 → 03 → 04**, plus all maintenance routes in
`CONTEXT.md` (adding audiences, formats, models; editing rules).

## 7. Quirk log
*(append-only; add a dated line after any observed failure of yours in this
workspace)*
- _(none yet)_

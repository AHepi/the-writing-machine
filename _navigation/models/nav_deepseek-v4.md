# nav_deepseek-v4.md — Layer 0 for DeepSeek V4

## 1. Entry
Read order: **this card → `CONTEXT.md` → your stage contract.** Read each input
file named by the contract **in full** — see §5, you do not scope.

## 2. Inherits
Tier **A** capability (from `_navigation/tiers.md`). You can navigate, resolve
pointers, and run any stage. Your risk is not capability; it is **completion.**

## 3. Strengths
- Strong reasoning and synthesis at full capability.
- Handles complex factsheets and arguments without simplifying the content.
- Good instruction-following *while it is still engaged* with a task.

## 4. Weaknesses & countermeasures
- *Abandons long tasks partway* → write **section by section**. You may not
  begin a section until the previous one is verified against its outline beat.
  No looking ahead, no batching.
- *Summarizes instead of finishing* → the phrases **"in summary," "the
  remaining sections follow," "similarly," "and so on"** are forbidden in any
  output. The last third of a draft is written at the density of the first.
- *Skips the CHECK* → the **completion ritual** (see §6): before STOP you must
  reprint the full D-list and the full CHECK list, each item with one line of
  evidence quoted from your own output. A model that won't finish is given a
  finish line it must physically cross.

## 5. Context policy
**Thrift OFF.** Read every input file the contract names *in full* — no §
scoping. Redundancy is cheap insurance against your failure mode: re-state the
brief's deliverables and the active anchors at the top of each section you
write. Spend tokens freely; abandonment, not overflow, is your danger.

## 6. Stage permissions
All stages **00 → 04**. But every stage you run ends with the completion
ritual: reprint D-list + CHECK list with quoted evidence per item before you
STOP. No ritual, no STOP.

## 7. Quirk log
*(append-only; add a dated line after any observed failure)*
- _(none yet — written against expected behavior; replace with observed facts
  after first real run, per `_add-a-model.md`)_

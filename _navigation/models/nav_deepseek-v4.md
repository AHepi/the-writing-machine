# nav_deepseek-v4.md — Layer 0 for DeepSeek V4

## 1. Entry

Read order: **this card → `CONTEXT.md` → your stage contract**. Read each in
full. Do not skim, do not scope by section — for you, redundancy is cheap
insurance.

## 2. Inherits

Tier **A** capability (`_navigation/tiers.md`) — but with the context policy
inverted. Capable enough to navigate and resolve pointers; the risk is not that
you *can't* finish, it's that you *won't*.

## 3. Strengths — what to exploit

- Strong reasoning and instruction fidelity when the task is held in one piece.
- Long context — use it to hold the entire stage's inputs at once.
- Reliable single-section writing when each section is its own committed unit.

## 4. Weaknesses & countermeasures

- *Abandons long tasks partway.*
  → **Write section by section.** You may not begin a section until the previous
  one is finished and verified against its outline beat. No drafting ahead, no
  placeholders.
- *Summarizes instead of finishing.*
  → The phrases **"in summary," "the remaining sections follow," "similarly,"
  and "and so on" are forbidden** in any output. The last third of a piece is
  written at the density of the first. Compressing later sections as the draft
  grows is a defect, not a style.
- *Skips or fakes the CHECK.*
  → **The completion ritual.** Before STOP you must reprint the full D-list and
  the contract's CHECK list, and beside each item quote one line of evidence
  **from your own output**. No quote, no pass. A model that won't finish gets a
  finish line it must physically cross.

## 5. Context policy

**Thrift OFF.** Read every input file in full. Do **not** use `CONTEXT_LITE.md`
or §-scoped reads — your failure mode is abandonment, not overflow, so load
everything whole and restate the anchors (the brief's goal, the D-list, the
active audience) at the top of each section as you write it.

## 6. Stage permissions

Stages **01, 02, 03**. May run **00** and **04** only under human supervision —
both depend on honest self-checking, which is your weakest probe. Prefer to
hand 00 and 04 to a tier-A model with thrift OFF disabled (e.g. Claude).

## 7. Quirk log

*Append-only. One dated line per observed failure; then tighten §4 above it.*

- (none yet — written against expected behavior; replace with observed behavior
  after the first real run, per `_add-a-model.md`.)

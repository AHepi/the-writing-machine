# nav_gemma-4b.md — Layer 0 for Gemma 4B

*This card is addressed half to the model and half to the human running it.
Gemma 4B does not navigate. A human (or a tier-A model) assembles its prompts.*

## 1. Entry
Gemma does **not** read this card and then go exploring. The human running it
opens `_navigation/assembly-order.md`, finds the recipe for the stage, and
concatenates the listed files into **one prompt**. Gemma sees that single
prompt and nothing else.

## 2. Inherits
Tier **C** (from `_navigation/tiers.md`). No navigation, no pointer resolution,
no multi-file holding.

## 3. Strengths
- Fast and cheap.
- Reliable at a single, fully-specified, self-contained instruction.
- Fine for one well-bounded stage when everything it needs is in front of it.

## 4. Weaknesses & countermeasures
- *Cannot follow pointers* → its inputs must contain **zero** `{brief.field}`
  pointers. Stage 00 has already resolved them all; the assembler must confirm
  the assembled prompt has no braces left.
- *Cannot hold multiple files* → the assembler flattens everything into one
  prompt per the recipe. One stage = one prompt.
- *Loses the thread on long context* → only the LITE contracts and the minimum
  inputs go in. No background, no whole library.

## 5. Context policy
**Thrift ON, hard.** Smallest possible prompt that still contains the full
contract and the exact inputs. Scoped to one stage.

## 6. Stage permissions
Stages **01, 02 (LITE), 03 (LITE)** only, and only when bracketed by a capable
model: stage 00 (brief + canonicalize) and stage 04 (audit) are **not** run by
Gemma. A tier-A model resolves the brief before, and audits after.

## 7. Quirk log
*(append-only; add a dated line after any observed failure)*
- _(none yet)_

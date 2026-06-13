# nav_gemma-4b.md — Layer 0 for Gemma 4B

*This card is addressed half to the model and half to the human (or tier-A
model) assembling its prompt. Gemma 4B cannot navigate. It does not read this
card and then go find files; someone hands it one finished prompt per stage.*

## 1. Entry

The model does not navigate. **Assembler:** go to
`_navigation/assembly-order.md` and concatenate the exact files it lists for the
target stage into a single prompt. Paste that one prompt. Collect one output.

## 2. Inherits

Tier **C** (`_navigation/tiers.md`) — small window, cannot follow a multi-file
contract, cannot resolve pointers.

## 3. Strengths — what to exploit

- Follows a single, self-contained, concrete instruction well.
- Cheap and fast — good for high-volume single-stage work once the prompt is
  assembled.

## 4. Weaknesses & countermeasures

- *Cannot follow pointers.* → **Pointers are illegal in its inputs.** Stage 00
  has already resolved every `{brief.field}`; the assembled prompt contains only
  literal values. If a pointer reaches Gemma, the assembler erred, not Gemma.
- *Drops instructions under load.* → One stage, one prompt, one output. Never
  ask it to hold two stages at once. Keep each prompt to the LITE files only.
- *Loses anchors in long text.* → Restate the goal, the audience register, and
  the D-list at both the top **and** bottom of the assembled prompt.

## 5. Context policy

**Thrift hard ON.** Minimum viable context. LITE files only
(`CONTEXT_LITE.md`). No whole-file loads. Anchors restated inside the single
prompt because there is no second turn to recover them.

## 6. Stage permissions

Stages **01, 02, 03** — and only as single assembled prompts. **Never** 00
(canonicalization needs pointer resolution) and **never** 04 (audit needs honest
self-checking). Those stages must be run by a tier-A model before/after Gemma's
contribution.

## 7. Quirk log

*Append-only. One dated line per observed failure.*

- (none yet)

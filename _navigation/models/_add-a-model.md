# _add-a-model.md — the contract for minting a model card

*Run this when the human says "add a model: X". Any tier-A model can execute it.
The workspace's contracts never change when a model is added; one file appears
in `_navigation/models/`, and that is the entire diff.*

The rule that governs everything below: **fill the card from observed behavior,
not reputation.** A model's marketing claims are not evidence. Its behavior on
the three probes is.

---

## Step 1 — Probe before writing

Run all three capability tests against the new model. Record what it actually
did, verbatim where it failed.

**Probe 1 — Contract following.** Give it a minimal three-file contract (a fake
READ → TRANSFORM → WRITE chain across three short files) and see whether it
follows the read order and produces only the named output, unaided.
→ Pass = navigates. Fail = tier C (assembly-order only).

**Probe 2 — Pointer resolution.** Give it a one-line input containing a
`{brief.audience}` pointer and a tiny lookup table, and ask it to resolve the
pointer to a literal value.
→ Pass = may resolve pointers (candidate for stage 00). Fail = must receive
pre-resolved `brief.md`; never runs stage 00.

**Probe 3 — Honest CHECK.** Give it a short piece with one deliverable
deliberately unmet, and a CHECK list. See whether it reports the miss or claims
success falsely.
→ Pass = honest self-check (may run stage 04). Fail = needs the completion
ritual forced on it, and may not audit.

## Step 2 — Assign a tier

- Probe 1 fail → **tier C**.
- Probe 1 pass, Probe 2 or 3 fail → **tier B**.
- All three pass → **tier A**.

The tier sets the card's §2 and the *defaults* for §5 and §6; the probes set the
overrides.

## Step 3 — Set the context policy (§5)

Decide thrift ON or OFF **from the observed failure mode**, not window size
alone:
- Small window or drops instructions under load → **thrift ON**, pre-chewed,
  LITE files.
- Large window but **abandons or summarizes long tasks** → **thrift OFF**, load
  whole, restate anchors, force the completion ritual. (This is DeepSeek V4's
  case — see its card.)

## Step 4 — Fill the schema

Copy the schema below, fill every section from the probe results, keep it
**≤600 tokens**, name it `nav_<model-id>.md` (lowercase, hyphens), save to
`_navigation/models/`.

```
# nav_<model-id>.md — Layer 0 for <model>

## 1. Entry        read order: this card → CONTEXT.md → your stage contract
## 2. Inherits     tier A | B | C
## 3. Strengths    what to exploit (from probes)
## 4. Weaknesses & countermeasures
                   each weakness paired with a binding rule
## 5. Context policy   thrift ON (scoped §-reads, LITE) or OFF (whole files, restated anchors)
## 6. Stage permissions   which stages this model may run (00 and 04 require the matching probe pass)
## 7. Quirk log    append-only; one dated line per observed failure
```

## Step 5 — Report for approval

Show the human the finished card and a one-paragraph summary of what each probe
revealed. Do not wire it into anything else — there is nothing to wire. The card
*is* the integration.

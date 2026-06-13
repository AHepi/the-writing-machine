# _add-a-model.md — the contract for minting a new model card

Run this when the user says "add a model: <X>." Any tier-A model can run it.
The principle: **fill the card from observed behavior, not reputation.** A
model's marketing tier is a rumor; its card is a measurement. The workspace's
contracts never change when a model is added — one file appears, and that is
the entire diff.

---

## Step 1 — Probe before writing

Run three capability tests against the candidate model and record what it
actually does, verbatim where it matters.

1. **Three-file contract, unaided.** Give it a small task that requires reading
   three separate files and combining them without further help. Does it open
   all three, or guess after one?
2. **Pointer resolution.** Hand it an input containing a `{brief.audience}`
   pointer and the file it points into. Does it resolve to the literal value,
   or copy the pointer through / invent a value?
3. **Honest CHECK.** Give it a short output and a CHECK list where one item
   genuinely fails. Does it report the failure with evidence, or rubber-stamp?

## Step 2 — Assign a tier from the results

- Passes all three cleanly → **Tier A**.
- Passes the contract and CHECK but drifts or needs hand-holding on pointers →
  **Tier B**.
- Fails the contract or cannot hold three files → **Tier C** (assembly only).

## Step 3 — Fill the schema

Create `nav_<model-id>.md` in this folder, ≤600 tokens, using exactly this
schema:

```
# nav_<model-id>.md — Layer 0 for <model>

## 1. Entry         read order: this card → CONTEXT.md → your stage contract
## 2. Inherits      tier A | B | C  (from _navigation/tiers.md)
## 3. Strengths     what to exploit, from the probe
## 4. Weaknesses & countermeasures
##                  each observed weakness paired with a binding rule
## 5. Context policy   thrift ON (scoped §-reads) or OFF (whole-file, anchors restated)
## 6. Stage permissions   which stages this model may run
## 7. Quirk log     append-only; one dated line per observed failure
```

Rules for filling it:
- §3 and §4 come from the **probe**, not from what the model is "known for."
- §4 pairs every weakness with a *binding rule* the model must obey — a
  weakness with no countermeasure is not allowed.
- §5 sets thrift by failure mode: small window or paid-API frugality → ON;
  frontier-but-lazy (abandons tasks) → OFF, with anchors restated.
- A Tier C card is addressed half to the model, half to the human running it,
  and points at `assembly-order.md`.

## Step 4 — Report for approval

Show the user the finished card. Do not wire it into anything else — there is
nothing to wire; `CONTEXT.md` and the stage contracts already work for any
card that follows the schema.

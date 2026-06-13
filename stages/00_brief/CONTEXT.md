# Stage 00 — Brief (the canonicalizer)

*Contract. Run by a tier-A model (it resolves pointers and fuzzy input — tier B
and C may not). This is the only stage that opens `defaults.md`, the only stage
that resolves `{brief.field}` pointers, and the only stage allowed to receive
sloppy input. Its job: turn whatever the user wrote into a **fully resolved
brief** in which every field holds an exact, legal value. Downstream stages
inherit certainty.*

**Read order:** your Layer 0 card → `../../CONTEXT.md` → this file.

---

## READ

- The user's raw request (topic, goal, and whatever else they typed — in their
  own words, allowed to be fuzzy).
- `_config/defaults.md` — every field's default and the resolution rules.
- A directory listing of `_config/audiences/` and `_config/formats/` — the legal
  values you resolve fuzzy input against.
- `brief_template.md` (this folder) — the shape of the output.

## INTERNALIZE

The user writes two lines in their own words; the machine receives a fully
explicit contract. You are the hinge where user-friendliness and machine-
friendliness stop trading off. Every decision you make on the user's behalf gets
logged so they can see it.

## TRANSFORM — resolve every field

1. **Required fields.** `topic` and `goal` must be present. If either is missing,
   `ASK HUMAN` — never invent a topic or goal.
2. **Fuzzy → exact filename.** For `audience` and `format`, list the directory
   and pick the **closest semantic match**:
   - "lefty union types" → `socialist`. "a punchy newsletter thing" →
     `substack`. "for my kid" → `child`.
   - No close match → fall back to the default (`general` / `essay`) and add a
     one-line flag to `resolution_log`.
3. **Expand every default inline.** Empty `length` → read the chosen format's
   §2 norm and write that band literally. Fill `visuals`, `provocation`,
   `audit`, `notes` from `defaults.md` if untouched. **No downstream stage ever
   opens `defaults.md` or resolves anything.**
4. **Build the deliverables block.** From the goal + the chosen format's §3
   required parts + the `notes` field, derive a `D-list`:
   - `D1` from the goal (usually: states the thesis in the opening).
   - `D2` the strongest counterargument, if the format calls for one.
   - One `D` per must-include in `notes`.
   - One `D` for the length band.
   Each D-item is a checkable sentence.
5. **Log every substitution** in `resolution_log:` — one line per decision, so
   the user can see what the system chose for them.

## WRITE

`output/brief.md`, following `brief_template.md`. Every field an exact filename
or literal. **No pointers. No category words. No fuzzy values.** The
`resolution_log` and `deliverables` blocks are mandatory.

## CHECK

- [ ] `topic` and `goal` present (else you ASKed).
- [ ] `audience` and `format` are exact filenames that exist in `_config/`.
- [ ] `length` is a literal word band, not "the format's norm".
- [ ] Every default expanded inline; the word "default" appears nowhere as a
      value.
- [ ] `deliverables` has at least D1 and the length D-item; every must-include
      from notes has its own D.
- [ ] `resolution_log` records every substitution made.
- [ ] No `{...}` pointer survives anywhere in the file.

## STOP

Hand off to stage 01. If any CHECK box is unticked, fix it before STOP — a
defective brief poisons every stage below.

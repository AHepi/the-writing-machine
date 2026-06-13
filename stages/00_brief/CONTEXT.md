# Stage 00 — brief (the canonicalizer)

The user's input is allowed to be sloppy; the system's input is not. This stage
takes whatever the user wrote — two lines or twenty — and produces a **resolved
brief** in which every field holds an exact, legal value, every default is
expanded inline, and the goal has become a checklist. This is the **only** stage
that may resolve pointers or read `_config/defaults.md`. Every artifact
downstream of here holds literal values.

Run by a tier-A model (or by a human filling the form). Not run by tier-C models.

## READ
- The user's request (the topic/goal and any overrides they wrote).
- `_config/defaults.md` — the fallback for every untouched field.
- The **filenames** in `_config/audiences/` and `_config/formats/` (list them;
  do not open them all). You resolve fuzzy values against the files that
  actually exist.
- `brief_template.md` in this folder — the shape of your output.

## INTERNALIZE
- Only `topic` and `goal` are required. Everything else defaults
  (`defaults.md`) unless the user overrode it.
- Resolution is semantic, against existing files: `lefty union types` →
  `socialist`; `a punchy newsletter thing` → `substack`. No match → the default
  in `defaults.md`, plus a one-line flag for the human.
- After this stage, no downstream stage resolves anything. Pre-chew everything.

## TRANSFORM
1. **Canonicalize every field.** For each field, take the user's value (or the
   default), and resolve it to an exact legal value: an existing filename for
   `audience`/`format`, a real band for `length`, a dial value for
   `visuals`/`provocation`/`audit`.
2. **Expand defaults inline.** Write the resolved value, not "(default)". The
   length default is read from the chosen format file's norm and written as a
   literal band.
3. **Build the deliverables block.** From the goal, the chosen format's
   `## 2. Required parts`, and the notes field, derive a D-list:
   - one D-item for the thesis/opening requirement,
   - one for the strongest counterargument (if the format calls for it),
   - one per must-include from notes,
   - one for the length band (`D: length <low>–<high> words`),
   - plus any format-required part not already covered.
4. **Record the resolution log.** One line per substitution or default applied,
   so the human can see what the system decided on their behalf.

## WRITE
`stages/00_brief/output/brief.md`, following `brief_template.md`: resolved
fields, the deliverables block, and the resolution log. Exact name, no pointers.

## CHECK
- [ ] `topic` and `goal` are both present and non-empty. (If not → ASK HUMAN.)
- [ ] Every field holds a legal literal value — no `{pointers}`, no "(default)".
- [ ] `audience` and `format` name files that actually exist in `_config/`.
- [ ] The deliverables block has a length D-item with a real band.
- [ ] Every fuzzy resolution and every applied default appears in the
      resolution log.
- [ ] If any resolution fell back to a default for lack of a match, a flag line
      is present.

## ASK HUMAN
- If `topic` or `goal` is missing or empty — you cannot invent the point of the
  piece.
- If the user's audience/format request matches *nothing* and the default would
  clearly be wrong (e.g. they asked for "a TikTok script" and only prose formats
  exist) — surface it rather than silently defaulting.

## STOP
Hand `brief.md` to stage 01. It is now the single source of truth; later stages
never reopen the user's original words.

# defaults.md — every brief field's default value

*Read by exactly one stage: **00, the canonicalizer**. No other stage opens this
file, because stage 00 expands every default inline into `brief.md`. Kept tiny
on purpose.*

The brief has two **required** fields and the rest default. When the user leaves
a field blank, stage 00 substitutes the value here and logs the substitution.

| Field | Default | Meaning |
|---|---|---|
| `topic` | *(required — ask)* | What the piece is about. |
| `goal` | *(required — ask)* | What the reader should think, feel, or do afterward. |
| `audience` | `general` | Smart layperson; never talked down to. (`_config/audiences/general.md`) |
| `format` | `essay` | General-purpose prose piece. (`_config/formats/essay.md`) |
| `length` | *the format's own norm* | Each format file declares its default word band. |
| `visuals` | `auto` | Used where they aid understanding; the format may veto. (`on` = force-consider, `off` = prose only) |
| `provocation` | `none` | Rhetorical heat. `none` / `low` / `high`. Raises register sharpness, never lowers respect. |
| `audit` | `on` | Whether stage 04 runs. Default on. |
| `notes` | *(empty)* | Free text: must-includes, must-avoids, anything. Feeds the D-list. |

**Resolution rules for stage 00:**
- Required field missing → `ASK HUMAN`, do not guess `topic` or `goal`.
- A named value that doesn't match a file → pick the closest semantic match from
  the directory listing; if none is close, fall back to the default and add a
  one-line flag to `resolution_log`.
- `length: empty` → read the chosen format's declared norm and write that band
  in literally.
- Every value written into `brief.md` must be an **exact, legal filename or
  literal** — never a category word, never a pointer. Downstream models inherit
  certainty.

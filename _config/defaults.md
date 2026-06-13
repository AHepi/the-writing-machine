# defaults.md — every brief field's default

Read by exactly one stage: **stage 00**, the canonicalizer. No other stage ever
opens this file, because stage 00 expands every default inline into `brief.md`.
Keep it short — this is a lookup table, not prose.

| Field | Default | Meaning of the default |
|---|---|---|
| `topic` | — | **Required.** No default. |
| `goal` | — | **Required.** No default. |
| `audience` | `general` | Smart layperson; new to the topic, not new to thinking. Never talked down to. |
| `format` | `essay` | General-purpose prose piece. |
| `length` | the format's own norm | Each format file declares its band; the brief inherits it unless overridden. |
| `visuals` | `auto` | Used where they aid understanding; the format may veto. `on` forces consideration; `off` forbids. |
| `provocation` | `none` | How much the piece may needle, challenge, or provoke. `none` / `mild` / `sharp`. |
| `audit` | `on` | Stage 04 runs. Turn `off` only for throwaway drafts. |
| `notes` | empty | Free text: must-includes, must-avoids, anything. Feeds the deliverables block. |

## Resolution rules for stage 00
- `audience` and `format` are resolved against the files actually present in
  `_config/audiences/` and `_config/formats/` — never against this list. This
  table only supplies the **fallback** when the user said nothing.
- A fuzzy value resolves to the closest semantic match among existing files;
  no match falls back to the default here and raises a one-line flag.
- Every resolution and every default applied is recorded in the brief's
  `resolution_log:`.

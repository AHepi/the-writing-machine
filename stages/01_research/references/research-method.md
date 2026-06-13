# research-method.md — how stage 01 finds and tags

## The S-register (source reliability)

Mark every source so stage 02 can weight it and stage 03 can pitch claims at the
right confidence. Three levels plus cautions:

- **primary** — the thing itself: the dataset, the law, the paper reporting the
  study, the company's own filing, the person's own words. Strongest.
- **secondary** — a careful report *about* a primary source: a good news
  article citing the study, a review summarizing the literature.
- **tertiary** — a summary of summaries: encyclopedias, explainers, aggregators.
  Fine for orientation; never the sole backing for a load-bearing claim.

Add a caution flag where it applies: `contested`, `dated`, `partisan-source`,
`single-study`, `small-sample`. The flag travels with the S-tag.

## Tagging discipline

- An **F-tag** is a single checkable claim, not a paragraph. Split compound
  claims so each can be sourced and audited on its own.
- Each F-tag names **one** S-tag as its backing (the best available). If two
  sources matter, make two findings or note the second in the finding.
- Capture the *exact* number, date, or quote — not a paraphrase that drifts.
  Stage 03 can only be as precise as you were.

## Coverage discipline

- Research the **opposing case** deliberately. The brief's counterargument
  deliverable needs real facts, not a strawman built from your own side's
  sources.
- Prefer recent over stale where the topic moves; mark `dated` otherwise.
- When sources conflict, record both with their S-registers and flag
  `contested` — do not silently pick a winner; that's stage 02's call, made in
  the open.

## Output shapes

`findings.md`:
```
- F1: <single checkable claim, with the exact figure/quote>  [S1]
- F2: <claim>  [S3]
GAPS:
- <question a deliverable needs answered that no source covered>
```

`sources.md`:
```
- S1: <author/title/publisher, date, locator/URL>  — primary
- S3: <…>  — secondary, contested
```

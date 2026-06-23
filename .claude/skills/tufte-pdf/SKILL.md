---
name: tufte-pdf
description: >-
  Render a markdown document into a Tufte-CSS-styled PDF with cleanly typeset
  LaTeX math and true margin sidenotes. Use when a deliverable needs book-quality
  typography, footnotes-as-sidenotes, or mathematical notation ($…$ / $$…$$) —
  e.g. the `textbook` format, explainers with equations, or any long-form piece
  that should look like a Tufte handout rather than a plain report. Prefer this
  over tools/render_pdf.py whenever math or Tufte layout matters.
---

# tufte-pdf — markdown → Tufte PDF with math

A self-contained renderer: markdown in, a Tufte-styled PDF out, with LaTeX math
typeset by KaTeX and footnotes turned into Tufte's signature numbered margin
sidenotes. Everything is vendored under `assets/` — **no network access is
needed at render time.**

## Render a document

```bash
python3 .claude/skills/tufte-pdf/render.py INPUT.md OUTPUT.pdf [--title "Title"] [--keep-html]
```

- `--title` sets the PDF/document title (defaults to the first `# H1`).
- `--keep-html` writes the intermediate `OUTPUT.sidecar.html` next to the PDF
  for debugging (otherwise it goes to a temp file and is deleted).

## One-time setup (only if the environment is fresh)

The renderer needs Python deps and a Chromium binary (the binary is **not**
committed — only the CSS/JS/font assets are):

```bash
pip install playwright markdown pygments
python3 -m playwright install chromium
```

All required system libraries for Chromium are already present in the standard
remote environment; if `playwright install chromium` complains about missing
libs, add `python3 -m playwright install-deps chromium`.

## Markdown conventions this skill supports

- **Math** — inline `$…$` or `\(…\)`; display `$$…$$` or `\[…\]`. KaTeX syntax.
- **Sidenotes** — standard markdown footnotes (`text[^1]` … `[^1]: note`) are
  automatically rewritten as numbered Tufte margin sidenotes. Numbering is
  sequential across the whole document.
- **Margin notes (unnumbered)** — write raw HTML inline:
  `<span class="marginnote">an aside with no number</span>`.
- **"Math, gently" boxes** — a boxed aside for explaining notation to beginners:
  ```html
  <div class="tk-box">
  <span class="tk-box-title">The math, gently</span>
  Plain-language explanation, may contain $math$.
  </div>
  ```
- **Subtitle** — under the `# Title`, add `<span class="subtitle">…</span>`.
- **Chapters** — each `## H2` starts on a fresh page.
- **Tables, code blocks, blockquotes, ordered/unordered lists** — all standard
  markdown; they sit in the main text column.

## How it works (for maintainers)

`render.py`: markdown → HTML (python-markdown: `extra`, `sane_lists`, `toc`,
`smarty`) → footnotes rewritten to Tufte sidenote markup → injected into
`template.html` → headless Chromium (Playwright) loads it from a `file://` URL,
waits for `window.__renderReady` (KaTeX done + web fonts loaded), then prints to
PDF with `prefer_css_page_size` so the `@page` rules in `tufte-print.css` apply.

`tufte-print.css` loads **after** both `tufte.css` and `katex.min.css` and
re-declares `counter-reset` on `body`, because those two sheets both reset
`body` counters and KaTeX's would otherwise clobber Tufte's sidenote counter.

## Assets & licenses (all vendored under `assets/`)

- `tufte.css`, `et-book/` — Tufte CSS + ET Book fonts, MIT (see
  `assets/TUFTE-CSS-LICENSE`).
- `katex/` — KaTeX 0.16.x, MIT (see `assets/katex/KATEX-LICENSE`).

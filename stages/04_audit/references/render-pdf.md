# render-pdf.md — markdown → PDF, offline and reproducible

*Reference for stage 04. Turns `final.md` into the `final.pdf` the human
downloads (`rules.md` §7). Works with no network and no pip/npm installs:
LibreOffice (`soffice`) ships in the environment and does the HTML → PDF step.*

> **For math or Tufte-styled documents — including `format: textbook` — use the
> `tufte-pdf` skill instead** (`.claude/skills/tufte-pdf/`). It renders
> markdown to a Tufte-CSS PDF with KaTeX-typeset mathematics and footnotes turned
> into margin sidenotes — things this reportlab/soffice path cannot do. The skill
> needs Chromium (`python3 -m playwright install chromium`, one-time); see its
> `SKILL.md`. This `render-pdf.md` recipe remains the default for plain prose
> formats (essay, op-ed, substack, reddit) that carry no math.

---

## The chain

```
final.md  →  final.html  (styled, charts drawn as bars)  →  final.pdf  (soffice)
```

1. **Markdown → HTML.** Convert the finished prose to a single self-contained
   HTML file with an embedded `<style>` block — a clean serif body, scaled
   headings, comfortable measure. No external CSS or fonts (offline).
2. **Render `CHART:` specs.** A draft may carry a fenced/indented `CHART:` block
   (see `_config/style/visuals.md`). Do **not** print it as raw text. Read its
   `x:` labels and the referenced figures and emit a simple **HTML/CSS bar
   chart** — labelled rows, proportional bar widths, the `message`/caption
   underneath. No chart library; bars are `<div>`s with percentage widths.
3. **HTML → PDF.** `soffice --headless --convert-to pdf`. Deliver the PDF.

## The converter

The repo carries a small, dependency-free converter at
`tools/render_pdf.py` (pure Python 3 stdlib). Run it:

```
python3 tools/render_pdf.py <input.md> <output.pdf>
```

It handles headings, paragraphs, bold/italic/`code`, blockquotes, lists, and the
`CHART:` block (rendered as CSS bars), writes a temporary styled `.html`, then
shells out to:

```
soffice --headless --convert-to pdf --outdir <dir> <tmp.html>
```

If `soffice` is missing, fall back to any available HTML-to-PDF path; the HTML
itself is always written so the render is never wholly blocked.

## Bar-chart contract

For `type: bar`, the converter expects the chart block to name its `x:` labels
(pipe-separated) and to carry the numeric values either inline or via the
`data:` F-tag whose figures appear in the surrounding prose. When the numbers
aren't machine-readable from the spec alone, the renderer falls back to the
labels with the `message` as the caption, so a chart never breaks the document.

## Done-when

- `final.pdf` exists, opens, and shows headings, body, and any chart as a
  visual (not as spec text).
- The file is delivered to the human as a download (the deliverable per §7).

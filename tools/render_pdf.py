#!/usr/bin/env python3
"""render_pdf.py — markdown -> PDF, pure Python (reportlab).

Renders the subset of markdown the Writing Workspace emits (headings,
paragraphs, bold/italic/code, lists, blockquotes, pipe tables) plus the CHART:
bar-chart block, drawn as real horizontal bars.

Engine: reportlab — a pure-Python wheel, no system libraries. Install once with
`pip install reportlab`. See stages/04_audit/references/render-pdf.md.

Usage:  python3 tools/render_pdf.py <input.md> <output.pdf>
"""
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, ListFlowable, ListItem,
)

BAR_COLOR = colors.HexColor("#4a6fa5")
RULE_COLOR = colors.HexColor("#dddddd")

# a line that begins a new block — continuation folding stops here
_CONT_STOP = r"^\s*[-*+]\s+|^\s*\d+[.)]\s+|^#{1,6}\s|^\s*>|^CHART:"


def styles():
    ss = getSampleStyleSheet()
    base = ParagraphStyle(
        "body", parent=ss["BodyText"], fontName="Times-Roman", fontSize=11,
        leading=15.5, alignment=TA_JUSTIFY, spaceAfter=8,
    )
    return {
        "body": base,
        "h1": ParagraphStyle("h1", parent=base, fontName="Times-Bold",
                             fontSize=22, leading=25, alignment=TA_LEFT,
                             spaceBefore=0, spaceAfter=14),
        "h2": ParagraphStyle("h2", parent=base, fontName="Times-Bold",
                             fontSize=15, leading=18, alignment=TA_LEFT,
                             spaceBefore=14, spaceAfter=6),
        "h3": ParagraphStyle("h3", parent=base, fontName="Times-Bold",
                             fontSize=12.5, leading=15, alignment=TA_LEFT,
                             spaceBefore=10, spaceAfter=4),
        "li": ParagraphStyle("li", parent=base, alignment=TA_LEFT, spaceAfter=3),
        "quote": ParagraphStyle("quote", parent=base, leftIndent=14,
                                textColor=colors.HexColor("#444444"),
                                borderPadding=0, alignment=TA_LEFT),
        "cell": ParagraphStyle("cell", parent=base, fontSize=8.5, leading=11,
                               alignment=TA_LEFT, spaceAfter=0),
        "cellh": ParagraphStyle("cellh", parent=base, fontName="Times-Bold",
                                fontSize=8.5, leading=11, alignment=TA_LEFT,
                                spaceAfter=0),
        "cap": ParagraphStyle("cap", parent=base, fontSize=9,
                              textColor=colors.HexColor("#555555"),
                              alignment=TA_LEFT, spaceBefore=4),
    }


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(text):
    """Markdown inline -> reportlab mini-markup."""
    parts = re.split(r"(`[^`]+`)", text)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            out.append('<font face="Courier">%s</font>' % esc(part[1:-1]))
        else:
            s = esc(part)
            s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
            s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
            out.append(s)
    return "".join(out)


def chart_flowable(body_lines, st, avail_w):
    spec = {}
    for ln in body_lines:
        m = re.match(r"\s*([a-zA-Z_]+)\s*[:=]\s*(.*)$", ln)
        if m:
            spec[m.group(1).strip().lower()] = m.group(2).strip()
    labels = [s.strip() for s in spec.get("x", "").split("|") if s.strip()]
    vals_raw = [s.strip() for s in spec.get("values", "").split("|") if s.strip()]
    values = []
    for v in vals_raw:
        try:
            values.append(float(re.sub(r"[^0-9.\-]", "", v)))
        except ValueError:
            values.append(None)
    axis = spec.get("y", "")
    caption = spec.get("message") or spec.get("caption") or ""

    flows = []
    have_vals = (labels and values and len(values) == len(labels)
                 and all(v is not None for v in values))
    if have_vals:
        vmax = max(values) or 1
        row_h = 22
        top_pad = 6
        d_h = row_h * len(labels) + top_pad
        d = Drawing(avail_w, d_h)
        label_w = avail_w * 0.34
        track_w = avail_w * 0.62
        for idx, (lab, val) in enumerate(zip(labels, values)):
            y = d_h - top_pad - (idx + 1) * row_h + 5
            d.add(String(label_w - 6, y + 3, lab, fontName="Times-Roman",
                         fontSize=9, textAnchor="end"))
            bw = max(10, track_w * (val / vmax))
            d.add(Rect(label_w, y, bw, 13, fillColor=BAR_COLOR,
                       strokeColor=None))
            d.add(String(label_w + bw + 4, y + 3, ("%g" % val),
                         fontName="Times-Bold", fontSize=9))
        flows.append(d)
    else:
        flows.append(Paragraph("<i>[chart: %s]</i>"
                               % esc(" | ".join(labels)), st["cap"]))
    if axis:
        flows.insert(0, Paragraph(esc(axis), st["cap"]))
    if caption:
        flows.append(Paragraph(esc(caption), st["cap"]))
    # keep the chart visually grouped
    return flows


def build_table(rows, st, avail_w):
    header, data_rows = rows[0], rows[1:]
    ncol = len(header)
    col_w = [avail_w / ncol] * ncol
    table_data = [[Paragraph(inline(c), st["cellh"]) for c in header]]
    for r in data_rows:
        # pad short rows
        r = r + [""] * (ncol - len(r))
        table_data.append([Paragraph(inline(c), st["cell"]) for c in r[:ncol]])
    t = Table(table_data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f0f0")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def parse(md, st, avail_w):
    lines = md.split("\n")
    story = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()

        if s.startswith("CHART:"):
            body = []
            i += 1
            while i < n and (lines[i].startswith("  ") or
                             (lines[i].strip() == "" and i + 1 < n and
                              lines[i + 1].startswith("  "))):
                if lines[i].strip():
                    body.append(lines[i])
                i += 1
            story.extend(chart_flowable(body, st, avail_w))
            story.append(Spacer(1, 6))
            continue

        if s == "":
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            key = "h1" if lvl == 1 else ("h2" if lvl == 2 else "h3")
            story.append(Paragraph(inline(m.group(2).strip()), st[key]))
            i += 1
            continue

        # pipe table
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?[\s:\-|]+\|?\s*$", lines[i + 1]) and "-" in lines[i + 1]:
            rows = [[c.strip() for c in line.strip().strip("|").split("|")]]
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in
                             lines[i].strip().strip("|").split("|")])
                i += 1
            story.append(build_table(rows, st, avail_w))
            story.append(Spacer(1, 8))
            continue

        if s.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            story.append(Paragraph(inline(" ".join(quote)), st["quote"]))
            story.append(Spacer(1, 4))
            continue

        # unordered list
        if re.match(r"^\s*[-*+]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*+]\s+", lines[i]):
                txt = re.sub(r"^\s*[-*+]\s+", "", lines[i]).strip()
                i += 1
                while i < n and lines[i].strip() and not re.match(
                        _CONT_STOP, lines[i]):
                    txt += " " + lines[i].strip()
                    i += 1
                items.append(ListItem(Paragraph(inline(txt), st["li"]),
                                      leftIndent=14))
            story.append(ListFlowable(items, bulletType="bullet",
                                      start="•", leftIndent=14))
            story.append(Spacer(1, 4))
            continue

        # ordered list
        if re.match(r"^\s*\d+[.)]\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+[.)]\s+", lines[i]):
                txt = re.sub(r"^\s*\d+[.)]\s+", "", lines[i]).strip()
                i += 1
                while i < n and lines[i].strip() and not re.match(
                        _CONT_STOP, lines[i]):
                    txt += " " + lines[i].strip()
                    i += 1
                items.append(ListItem(Paragraph(inline(txt), st["li"]),
                                      leftIndent=14))
            story.append(ListFlowable(items, bulletType="1", leftIndent=14))
            story.append(Spacer(1, 4))
            continue

        # paragraph
        para = [s]
        i += 1
        while i < n and lines[i].strip() and not re.match(
            r"^(#{1,6}\s|\s*[-*+]\s|\s*\d+[.)]\s|>|CHART:)", lines[i]
        ):
            nxt = lines[i]
            if "|" in nxt and i + 1 < n and "-" in lines[i + 1] and re.match(
                    r"^\s*\|?[\s:\-|]+\|?\s*$", lines[i + 1]):
                break
            para.append(nxt.strip())
            i += 1
        story.append(Paragraph(inline(" ".join(para)), st["body"]))
    return story


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: render_pdf.py <input.md> <output.pdf>")
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        md = f.read()
    st = styles()
    margin_x, margin_y = 2.3 * cm, 2.0 * cm
    avail_w = A4[0] - 2 * margin_x
    doc = BaseDocTemplate(dst, pagesize=A4,
                          leftMargin=margin_x, rightMargin=margin_x,
                          topMargin=margin_y, bottomMargin=margin_y,
                          title="")
    frame = Frame(margin_x, margin_y, avail_w, A4[1] - 2 * margin_y, id="main")
    doc.addPageTemplates([PageTemplate(id="t", frames=[frame])])
    doc.build(parse(md, st, avail_w))
    print("wrote", dst)


if __name__ == "__main__":
    main()

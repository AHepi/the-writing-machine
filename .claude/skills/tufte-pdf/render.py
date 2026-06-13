#!/usr/bin/env python3
"""
render.py — markdown (+ LaTeX math, + footnotes) -> Tufte-styled PDF.

Pipeline: python-markdown -> HTML, footnotes rewritten as Tufte margin
sidenotes, math left as $…$/$$…$$ for KaTeX, the whole thing dropped into
template.html and printed to PDF by headless Chromium (Playwright).

Usage:
    python3 render.py INPUT.md OUTPUT.pdf [--title "Title"] [--keep-html]

All asset references are resolved to absolute file:// URLs, so the sidecar
HTML can live anywhere. No network access is needed at render time — KaTeX,
its fonts, tufte.css and et-book are all vendored under ./assets/.
"""

import argparse
import os
import re
import sys
import tempfile

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(HERE, "assets")
TEMPLATE = os.path.join(HERE, "template.html")


def md_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=[
            "extra",          # tables, fenced code, attr_list, footnotes, md_in_html, …
            "sane_lists",
            "toc",
            "smarty",         # curly quotes/dashes, in the Tufte spirit
        ],
        output_format="html5",
    )


def _strip_backref(html: str) -> str:
    """Remove python-markdown's ↩ 'jump back' link from a footnote body."""
    html = re.sub(
        r'<a class="footnote-backref"[^>]*>.*?</a>', "", html, flags=re.S
    )
    return html.strip()


def footnotes_to_sidenotes(html: str) -> str:
    """Rewrite python-markdown footnotes as Tufte numbered sidenotes.

    The reference <sup>…</sup> becomes a margin-toggle label + checkbox +
    <span class="sidenote">…</span> carrying the footnote's text. The trailing
    <div class="footnote">…</div> block is then removed entirely.
    """
    m = re.search(r'<div class="footnote">.*</div>', html, flags=re.S)
    defs = {}
    if m:
        block = m.group(0)
        for fm in re.finditer(r'<li id="fn:([^"]+)">(.*?)</li>', block, flags=re.S):
            key, body = fm.group(1), _strip_backref(fm.group(2))
            # Unwrap a single enclosing <p>…</p> so the sidenote stays inline-valid.
            single = re.fullmatch(r"<p>(.*)</p>", body, flags=re.S)
            if single:
                body = single.group(1).strip()
            defs[key] = body
        html = html.replace(block, "")

    counter = {"n": 0}

    def repl(ref):
        key = ref.group(1)
        body = defs.get(key, "")
        counter["n"] += 1
        sid = "sn-%d" % counter["n"]
        return (
            '<label for="{sid}" class="margin-toggle sidenote-number"></label>'
            '<input type="checkbox" id="{sid}" class="margin-toggle"/>'
            '<span class="sidenote">{body}</span>'
        ).format(sid=sid, body=body)

    html = re.sub(r'<sup id="fnref:([^"]+)">.*?</sup>', repl, html, flags=re.S)
    return html


def build_html(md_text: str, title: str) -> str:
    body = footnotes_to_sidenotes(md_to_html(md_text))
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    asset_url = "file://" + ASSET_DIR
    return (
        tpl.replace("{ASSET_DIR}", asset_url)
        .replace("{TITLE}", title)
        .replace("{BODY}", body)
    )


def render_pdf(html: str, out_pdf: str, keep_html: bool) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit(
            "Playwright not installed. Run:\n"
            "  pip install playwright markdown pygments\n"
            "  python3 -m playwright install chromium"
        )

    out_pdf = os.path.abspath(out_pdf)
    if keep_html:
        html_path = os.path.splitext(out_pdf)[0] + ".sidecar.html"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        cleanup = False
    else:
        fd, html_path = tempfile.mkstemp(suffix=".sidecar.html")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(html)
        cleanup = True

    try:
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch()
            except Exception as e:
                sys.exit(
                    "Could not launch Chromium (%s).\n"
                    "Run: python3 -m playwright install chromium" % e
                )
            page = browser.new_page()
            page.goto("file://" + html_path, wait_until="load")
            page.wait_for_function("window.__renderReady === true", timeout=60000)
            page.pdf(
                path=out_pdf,
                print_background=True,
                prefer_css_page_size=True,
            )
            browser.close()
    finally:
        if cleanup:
            os.unlink(html_path)
    print("Wrote %s" % out_pdf)


def main() -> None:
    ap = argparse.ArgumentParser(description="Render markdown to a Tufte-styled PDF.")
    ap.add_argument("input", help="input markdown file")
    ap.add_argument("output", help="output PDF file")
    ap.add_argument("--title", default=None, help="document title (default: first H1)")
    ap.add_argument(
        "--keep-html", action="store_true", help="keep the intermediate .sidecar.html"
    )
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        md_text = f.read()

    title = args.title
    if not title:
        h1 = re.search(r"^#\s+(.+)$", md_text, flags=re.M)
        title = h1.group(1).strip() if h1 else "Document"

    html = build_html(md_text, title)
    render_pdf(html, args.output, args.keep_html)


if __name__ == "__main__":
    main()

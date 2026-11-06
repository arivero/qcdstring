#!/usr/bin/env python3
"""Transcribe papers/pdf/*.pdf to Markdown in papers/md/.

Each output file starts with a front-matter block (manifest metadata, source
PDF, page count, method) and carries a `<!-- page N -->` marker before every
page so that citations can point at a page. Method order: pymupdf4llm
(headings, bold, tables) with a fallback to `pdftotext -layout`. Equations
come out as plain text in both; check the PDF before quoting a formula.
PDFs with almost no text layer (scans) are flagged `low_text: true`; they
need OCR; with rapidocr-onnxruntime installed pymupdf4llm does that automatically.

    pip install pymupdf4llm rapidocr-onnxruntime   # optional; the second one OCRs scanned pages
    python3 papers/transcribe.py                 # everything missing
    python3 papers/transcribe.py --key Tong2009  # one paper
    python3 papers/transcribe.py --force         # redo all

Writes papers/md/<key>.md and papers/md-index.tsv (committed; md/ is ignored).
"""
import argparse
import csv
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(HERE, "pdf")
MD_DIR = os.path.join(HERE, "md")
INDEX = os.path.join(HERE, "md-index.tsv")
LOW_TEXT_CHARS_PER_PAGE = 300

try:
    import pymupdf4llm
    import pymupdf
except ImportError:
    pymupdf4llm = None


def manifest():
    meta = {}
    for name in ("library-1974", "memory-future"):
        with open(os.path.join(HERE, name + ".tsv"), newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                meta[r["key"]] = dict(r, manifest=name)
    return meta


def page_count(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True).stdout.decode("utf-8", "replace")
    return int(next((l.split()[-1] for l in out.splitlines() if l.startswith("Pages:")), 0))


def with_pymupdf(path):
    chunks = pymupdf4llm.to_markdown(path, page_chunks=True, show_progress=False)
    return [c["text"] for c in chunks]


def with_pdftotext(path, n):
    pages = []
    for i in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-layout", "-f", str(i), "-l", str(i), "-q", path, "-"],
                           capture_output=True).stdout.decode("utf-8", "replace")
        pages.append(t)
    return pages


def yaml(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', "'") + '"'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--key", action="append", default=[])
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--plain", action="store_true", help="use pdftotext even if pymupdf4llm is available")
    a = ap.parse_args()
    os.makedirs(MD_DIR, exist_ok=True)
    meta = manifest()
    keys = sorted(f[:-4] for f in os.listdir(PDF_DIR) if f.endswith(".pdf"))
    if a.key:
        keys = [k for k in keys if k in a.key]
    rows = []
    for k in keys:
        out = os.path.join(MD_DIR, k + ".md")
        src = os.path.realpath(os.path.join(PDF_DIR, k + ".pdf"))
        if os.path.exists(out) and not a.force:
            continue
        n = page_count(src)
        method = "pdftotext-layout"
        pages = None
        if pymupdf4llm and not a.plain:
            try:
                pages, method = with_pymupdf(src), "pymupdf4llm"
            except Exception as e:
                print(f"  {k}: pymupdf4llm failed ({e}); falling back", file=sys.stderr)
        if pages is None or sum(len(p.strip()) for p in pages) < LOW_TEXT_CHARS_PER_PAGE * max(n, 1):
            alt = with_pdftotext(src, n)
            if pages is None or sum(len(p.strip()) for p in alt) > sum(len(p.strip()) for p in pages):
                pages, method = alt, "pdftotext-layout"
        chars = sum(len(p.strip()) for p in pages)
        low = chars < LOW_TEXT_CHARS_PER_PAGE * max(n, 1)
        m = meta.get(k, {})
        head = ["---", f"key: {k}", f"title: {yaml(m.get('title', ''))}", f"authors: {yaml(m.get('authors', ''))}",
                f"year: {m.get('year', '')}", f"arxiv: {m.get('arxiv', '') or ''}", f"doi: {m.get('doi', '') or ''}",
                f"manifest: {m.get('manifest', '')}", f"source_pdf: {os.path.relpath(src, os.path.dirname(HERE)) if src.startswith(os.path.dirname(HERE)) else 'external:' + os.path.basename(src)}",
                f"pages: {n}", f"method: {method}", f"low_text: {str(low).lower()}",
                "status: machine-transcribed; equations are plain text, verify against the PDF", "---", ""]
        body = "\n".join(f"<!-- page {i} -->\n\n{p.strip()}\n" for i, p in enumerate(pages, 1))
        with open(out, "w") as f:
            f.write("\n".join(head) + "\n" + body)
        rows.append((k, n, chars, method, low))
        print(f"{k}: {n} p, {chars} chars, {method}{'  LOW TEXT' if low else ''}", flush=True)
    # rebuild the index from whatever is in md/
    idx = []
    for f in sorted(os.listdir(MD_DIR)):
        if not f.endswith(".md"):
            continue
        t = open(os.path.join(MD_DIR, f), errors="replace").read()
        g = lambda tag: next((l.split(":", 1)[1].strip() for l in t.split("---")[1].splitlines() if l.startswith(tag + ":")), "")
        idx.append((f[:-3], g("pages"), len(t), g("method"), g("low_text")))
    with open(INDEX, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["key", "pages", "md_bytes", "method", "low_text"])
        w.writerows(idx)
    print(f"\n{len(rows)} transcribed this run, {len(idx)} in md/, index written")


if __name__ == "__main__":
    main()

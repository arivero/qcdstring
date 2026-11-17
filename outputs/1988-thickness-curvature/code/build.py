#!/usr/bin/env python3
"""Build QCDS-88/1 from its Markdown source with Pandoc and XeLaTeX."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
paper = (ROOT / "paper.md").read_text()
# Keep the short Casimir table and its interpretation together in this edition.
# The canonical Markdown remains free of typesetting-only page breaks.
paper = paper.replace("Table 2 lists the massive contribution alone.",
                      "\\newpage\n\nTable 2 lists the massive contribution alone.", 1)
subprocess.run(
    ["pandoc", "--from=markdown+tex_math_dollars", "--pdf-engine=xelatex",
     "-V", "geometry:margin=25mm", "-V", "papersize=a4", "-V", "fontsize=11pt",
     "-V", "colorlinks=true", "-V", "linkcolor=blue", "-V", "urlcolor=blue",
     "-o", "paper.pdf"],
    input=paper, text=True, cwd=ROOT, check=True,
)
print("Built", ROOT / "paper.pdf")

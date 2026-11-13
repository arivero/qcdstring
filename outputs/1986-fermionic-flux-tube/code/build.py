#!/usr/bin/env python3
"""Build the 1986 paper; requires Pandoc and XeLaTeX on PATH."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
# Keep the title and abstract before the contents in the PDF. Raw LaTeX is
# inserted only into the build input; the canonical Markdown stays portable.
paper = (ROOT / "paper.md").read_text()
paper = paper.replace(
    "## 1. The question after a decade",
    "\\newpage\n\n\\setcounter{tocdepth}{2}\n\\tableofcontents\n\n\\newpage\n\n## 1. The question after a decade",
    1,
)
subprocess.run(
    ["pandoc", "--from=markdown+tex_math_dollars", "--pdf-engine=xelatex",
     "--toc-depth=2", "-V", "geometry:margin=25mm", "-V", "papersize=a4",
     "-V", "fontsize=11pt", "-V", "colorlinks=true", "-V", "linkcolor=blue",
     "-V", "urlcolor=blue", "-o", "paper.pdf"],
    input=paper, text=True, cwd=ROOT, check=True,
)
print("Built", ROOT / "paper.pdf")

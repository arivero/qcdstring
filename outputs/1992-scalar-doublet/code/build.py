"""Build the standalone QCDS-92/1 PDF with Pandoc and XeLaTeX."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
subprocess.run(
    ["pandoc", "paper.md", "--from=markdown+tex_math_dollars", "--pdf-engine=xelatex",
     "-V", "papersize=a4", "-V", "geometry:margin=23mm", "-V", "fontsize=11pt",
     "-V", "colorlinks=true", "-V", "linkcolor=blue", "-V", "urlcolor=blue",
     "-o", "paper.pdf"], cwd=root, check=True
)

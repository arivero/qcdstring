"""Render the standalone, tagged edition using the series' A4 layout."""
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
subprocess.run(
    ["pandoc", "paper.md", "--from=markdown+tex_math_dollars",
     "--pdf-engine=xelatex", "--lua-filter=code/pdf-links.lua",
     "-V", "papersize=a4", "-V", "geometry:margin=23mm",
     "-V", "fontsize=11pt", "-V", "colorlinks=true", "-V", "urlcolor=blue",
     "-M", "title-meta=Where does the color go when a string is lifted?", "-o", "paper.pdf"],
    cwd=root, check=True,
)

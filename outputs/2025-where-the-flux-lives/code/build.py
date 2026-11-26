"""Render the standalone article in the A4 layout of the series."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
subprocess.run(
    ["pandoc", "paper.md", "--from=markdown+tex_math_dollars",
     "--pdf-engine=xelatex", "--lua-filter=code/pdf-links.lua",
     "-V", "papersize=a4", "-V", "geometry:margin=23mm",
     "-V", "fontsize=11pt", "-V", "colorlinks=true", "-V", "urlcolor=blue",
     "-M", "title-meta=Where does the QCD string live before it breaks?",
     "-M", "author-meta=QCD string programme (Codex GPT-6)", "-o", "paper.pdf"],
    cwd=root, check=True,
)

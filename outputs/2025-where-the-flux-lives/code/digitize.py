"""Extract the nine N200 markers from the authors' Fig. 4 vector artwork.

Usage: python code/digitize.py PATH/VRensembles.pdf
The reference tables below identify axes from VRensembles_fig.tex. Match
stroked tick marks, filled point symbols and vertical errors independently.
"""
import argparse
import csv
import hashlib
from pathlib import Path

import fitz
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
HASH = "abeae9c810a8b0b00250328c87951fbdb4739de0cf400d9a60f89c88c3981783"

def center(rect):
    return (rect.x0 + rect.x1) / 2, (rect.y0 + rect.y1) / 2

def extract(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != HASH:
        raise ValueError("Unexpected artwork. Use VRensembles.pdf from arXiv:2403.00754v2.")
    with fitz.open(path) as doc:
        paths = doc[0].get_drawings()
    black = [p["rect"] for p in paths if p["color"] == (0, 0, 0)]
    y_ticks = sorted(b.y0 for b in black if 52.6 < b.x0 < 52.8
                     and 3.9 < b.width < 4.2 and b.height < 0.01)
    x_ticks = sorted(b.x0 for b in black if 201 < b.x0 < 320
                     and 169.9 < b.y0 < 170.1 and b.width < 0.01)
    if len(y_ticks) != 9 or len(x_ticks) != 6:
        raise ValueError("Could not isolate the axes")
    scale, zero = np.polyfit(y_ticks, np.linspace(0.08, -0.08, 9), 1)
    points = [p["rect"] for p in paths if p["type"] == "fs"]
    bars = [p["rect"] for p in paths if p["type"] == "s" and p["color"]
            and p["color"][2] > .99 and p["rect"].width < .01]
    for distance in (17, 19, 21):
        x = x_ticks[distance - 17]
        symbols = sorted((center(b)[1] for b in points if abs(center(b)[0] - x) < .04),
                         reverse=True)
        errors = [b for b in bars if abs(b.x0 - x) < .04]
        if len(symbols) != 3 or len(errors) != 3:
            raise ValueError("Ambiguous point at the selected distance")
        for n, y in enumerate(symbols):
            bar = min(errors, key=lambda b: abs(center(b)[1] - y))
            if abs(center(bar)[1]-y) > .06:
                raise ValueError("Error bar does not match marker")
            yield (distance, n, f"{scale*y+zero:.7f}", f"{abs(scale)*bar.height/2:.7f}",
                   f"{x:.3f}", f"{y:.3f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artwork", type=Path)
    args = parser.parse_args()
    out = ROOT / "data" / "n200.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("r_over_a", "n", "aE", "displayed_error", "x_pdf", "y_pdf"))
        writer.writerows(extract(args.artwork))

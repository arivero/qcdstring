"""Read Figs. 4 and 5 of arXiv:2403.00754v2 and the metadata from Table 1."""
import argparse
import csv
import hashlib
from pathlib import Path

import fitz
import numpy as np

from digitize import ENSEMBLES, ROOT, center, extract

FIG5_HASH = "19b476120004e98a315277f49c0fe3b36a1f5f8708fcd3a946cf3be0f8d9755c"
# Ns, rounded pion and kaon masses in MeV, flow time and its error in lattice units.
TABLE1 = {"D200": (64, 200, 480, 5.1802, .0078),
          "N200": (48, 280, 460, 5.1590, .0076),
          "N203": (48, 340, 440, 5.1433, .0074)}


def fig5(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != FIG5_HASH:
        raise ValueError("Expected dStatMassdep.pdf from arXiv:2403.00754v2")
    with fitz.open(path) as doc:
        paths = doc[0].get_drawings()
    black = [p["rect"] for p in paths if p["color"] == (0, 0, 0)]
    xs = sorted({b.x0 for b in black if 195.9 < b.y0 < 196 and b.width < .01
                 and 3.9 < b.height < 4.2})
    ys = sorted({b.y0 for b in black if 47.09 < b.x0 < 47.12 and b.height < .01
                 and 3.9 < b.width < 4.2}, reverse=True)
    if len(xs) != 6 or len(ys) != 7:
        raise ValueError("Expected six horizontal and seven vertical axis labels")
    sx, bx = np.polyfit(xs, np.linspace(0, 1, 6), 1)
    sy, by = np.polyfit(ys, np.linspace(0, .06, 7), 1)
    points = sorted((p for p in paths if p["type"] == "fs"), key=lambda p: p["rect"].x0)
    if len(points) != len(ENSEMBLES):
        raise ValueError("Missing mass point")
    for name, point in zip(ENSEMBLES, points):
        x, y = center(point["rect"])
        bars = [p["rect"] for p in paths if p["type"] == "s" and p["color"] == point["color"]
                and p["rect"].width < .01 and abs(p["rect"].x0 - x) < .04]
        if len(bars) != 1 or abs(center(bars[0])[1] - y) > .06:
            raise ValueError("No unique marginal uncertainty for " + name)
        yield (name, f"{sx*x+bx:.7f}", f"{sy*y+by:.7f}", f"{abs(sy)*bars[0].height/2:.7f}",
               f"{x:.3f}", f"{y:.3f}", *TABLE1[name])


def write(path, columns, rows):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(columns.split())
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", type=Path, help="directory containing the two PDF drawings")
    parser.add_argument("--out", type=Path, default=ROOT / "data")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rows = ((name, *row) for name in ENSEMBLES
            for row in extract(args.source_dir / "VRensembles.pdf", name))
    write(args.out / "mass-scan-levels.csv", "ensemble r_over_a n aE displayed_error x_pdf y_pdf", rows)
    write(args.out / "mass-scan-ensembles.csv",
          "ensemble u sqrt_t0_gap displayed_error x_pdf y_pdf Ns mpi_MeV mK_MeV t0_a2 t0_error",
          fig5(args.source_dir / "dStatMassdep.pdf"))


if __name__ == "__main__":
    main()

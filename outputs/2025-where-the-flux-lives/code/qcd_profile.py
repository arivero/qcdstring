"""Read the action-density markers in Fig. 2 of Prkacin et al. (2005)."""
import argparse
import csv
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HASH = "1f513a0ab0696b33d9280b13c81a95bdf34f1090176c902530f943bd08d85d4c"

def extract(path):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != HASH:
        raise ValueError("Use transverse.ps from the hep-lat/0510051 source archive")
    source = data.decode("latin1")
    # Labeled horizontal ticks give x=0 at 2520 and x=1 fm at 4532.
    # The energy markers are CircleF. The final BoxF is the legend symbol.
    points = [(int(x),int(y)) for x,y in re.findall(r"^(\d+) (\d+) BoxF$",source,re.M)]
    if len(points)!=26 or points[-1]!=(4300,3848):
        raise ValueError("Unexpected action markers")
    series = dict(points[:-1])
    base = (series[508]+series[4532])/2
    norm = series[2520]-base
    return [(x,y,(x-2520)/2012,(y-base)/norm) for x,y in points[:-1]]

if __name__=="__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artwork",type=Path)
    args = parser.parse_args()
    with (ROOT/"data"/"qcd-midplane.csv").open("w",newline="") as stream:
        writer = csv.writer(stream,lineterminator="\n")
        writer.writerow(("plot_x","plot_y","x_fm","action_contrast"))
        for x,y,r,contrast in extract(args.artwork):
            writer.writerow((x,y,f"{r:.6f}",f"{contrast:.6f}"))

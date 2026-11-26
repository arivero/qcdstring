"""Project an octet scalar insertion onto finite chords of published static-pair data."""
import csv
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def read_table(name):
    with (ROOT / "data" / name).open() as stream:
        return list(csv.DictReader(stream))


def difference(values, errors, coordinates, low, high, factor):
    du = coordinates[high] - coordinates[low]
    return {"value": factor * (values[high] - values[low]) / du,
            "marginal_error": abs(factor) * math.hypot(errors[high], errors[low]) / du}


def draw(rows, threshold):
    colors = ("#274e72", "#b55c23", "#258074")
    positions = np.array([17, 19, 21])
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.55), sharey=True)
    for axis, field, title in zip(axes, ("outer", "equal_volume"),
                                 ("D200 to N203", "N200 to N203 · equal volume")):
        limit = threshold[field]
        axis.axhspan(limit["value"] - limit["marginal_error"],
                     limit["value"] + limit["marginal_error"], color="#a6a1bd", alpha=.16)
        axis.axhline(limit["value"], color="#686078", lw=1.15, ls="--",
                     label="Two isolated strange mesons")
        axis.axhline(0, color="#777777", lw=.8)
        for n, mark in enumerate(("o", "s", "^")):
            values = [entry[field] for entry in rows if entry["level"] == n]
            axis.errorbar(positions + .12 * (n-1), [v["value"] for v in values],
                          yerr=[v["marginal_error"] for v in values], color=colors[n],
                          fmt=mark, capsize=3, ms=5, label=f"Level {n}")
        axis.set(xlabel="Static separation  r/a", xticks=positions, title=title)
        axis.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Odd-profile scalar response\nrelative to two light mesons")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, ncol=4, loc="lower center", frameon=False, fontsize=8)
    fig.tight_layout(rect=[0, .09, 1, 1], w_pad=1)
    fig.savefig(ROOT / "results" / "mass-response.png", dpi=190)
    plt.close(fig)


def main():
    modes = json.loads((ROOT / "results" / "harmonics.json").read_text())["neck"]["shooting"]
    c = modes["odd"]["plus"]
    names = ["D200", "N200", "N203"]
    panels = read_table("mass-scan-ensembles.csv")
    assert [e["ensemble"] for e in panels] == names
    u = [float(e["u"]) for e in panels]
    mid = (u[1] - u[0]) / (u[2] - u[0])
    ordered = {(e["ensemble"], int(e["r_over_a"]), int(e["n"])): e
               for e in read_table("mass-scan-levels.csv")}
    assert len(ordered) == 27 and 0 < mid < 1
    rows = []
    for distance in (17, 19, 21):
        for n in range(3):
            points = [ordered[name, distance, n] for name in names]
            energy = [float(p["aE"]) for p in points]
            err = [float(p["displayed_error"]) for p in points]
            rows.append(dict(r_over_a=distance, level=n,
                             outer=difference(energy, err, u, 0, 2, c),
                             equal_volume=difference(energy, err, u, 1, 2, c),
                             middle_residual=energy[1] - (1-mid)*energy[0] - mid*energy[2],
                             middle_error=math.hypot(err[1], (1-mid)*err[0], mid*err[2])))
    # The Fig. 5 ordinate and flow time on one ensemble have unspecified covariance.
    # Quote errors from its displayed ordinate at fixed tabulated flow time; give
    # the maximum separate scale contribution (triangle inequality) as a diagnostic.
    threshold_values, threshold_errors, flow_errors = [], [], []
    for panel in panels:
        flow, gap = float(panel["t0_a2"]), float(panel["sqrt_t0_gap"])
        threshold_values.append(2 * gap / math.sqrt(flow))
        threshold_errors.append(2 * float(panel["displayed_error"]) / math.sqrt(flow))
        flow_errors.append(abs(gap * float(panel["t0_error"]) / flow**1.5))
    threshold = {}
    for label, low in (("outer", 0), ("equal_volume", 1)):
        threshold[label] = difference(threshold_values, threshold_errors, u, low, 2, c)
        threshold[label]["flow_error_bound_linearized"] = c*(flow_errors[low]+flow_errors[2])/(u[2]-u[low])
    results = dict(odd_coefficient=c, even_over_odd=modes["even"]["plus"]/c,
                   mass_coordinates=dict(zip(names, u)), interpolation_fraction=mid,
                   levels=rows, two_strange_threshold=threshold)
    (ROOT/"results"/"mass-response.json").write_text(json.dumps(results, indent=2)+"\n")
    draw(rows, threshold)


if __name__ == "__main__":
    main()

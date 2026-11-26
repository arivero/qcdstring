"""Independent decimal arithmetic and Fourier checks of the archived results."""
import csv
import json
import math
from decimal import Decimal as D, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
getcontext().prec = 45

def invariants(e):
    a, b, c = e
    return a+b+c, a*b+a*c+b*c, a*b*c

def remaining(first, last, e):
    t1, b1, c1 = invariants(first)
    t2, b2, c2 = invariants(last)
    threshold_sum = (b2-b1)/(t2-t1)
    threshold_product = (c2-c1)/(t2-t1)
    disc = (threshold_sum**2-4*threshold_product).sqrt()
    low, high = (threshold_sum-disc)/2, (threshold_sum+disc)/2

    def cubic(t):
        return math.prod(t-value for value in first)

    h_low = -cubic(low)/(low-high)
    h_high = -cubic(high)/(high-low)
    u = e-h_low/(e-low)-h_high/(e-high)
    # Use the known root to divide the cubic and solve a plain quadratic.
    trace = u+low+high
    pair_sum = u*(low+high)+low*high-h_low-h_high
    other_sum = trace-e
    other_product = pair_sum-e*other_sum
    other_gap = (other_sum**2-4*other_product).sqrt()
    return [(other_sum-other_gap)/2, (other_sum+other_gap)/2]

def second_harmonic():
    radius_ratio, a, b = 2., .4, .25
    mid = radius_ratio/2
    A1 = a*(1+mid)*math.exp(-mid)
    A2 = b*(1+2*mid)*math.exp(-2*mid)
    norm = 1+(A1*A1+A2*A2)/2
    errors = []
    for phase in (0., math.pi/2):
        angles = [2*math.pi*i/240 for i in range(240)]
        density = [(1+A1*math.cos(t)+A2*math.cos(2*t+phase))**2 for t in angles]
        avg = math.fsum(density)
        for trig, theory in [(math.cos,(A1+A1*A2*math.cos(phase)/2)/norm),
                             (math.sin,(-A1*A2*math.sin(phase)/2)/norm)]:
            errors.append(abs(math.fsum(v*trig(t) for v,t in zip(density,angles))/avg-theory))
    return max(errors)

def main():
    with (ROOT/"data"/"n200.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    energies = [D(row["aE"]) for row in rows]
    first, middle, last = energies[:3], energies[3:6], energies[6:]
    predicted = remaining(first,last,middle[1])
    reference = json.loads((ROOT/"results"/"checks.json").read_text())
    stored = [reference["n200"]["predicted"][index] for index in [0,2]]
    decimal_error = max(abs(v-D(str(s))) for v,s in zip(predicted,stored))
    offset = D("2.7")
    shifted = remaining([v+offset for v in first], [v+offset for v in last], middle[1]+offset)
    translation_error = max(abs(a-b+offset) for a,b in zip(predicted,shifted))
    ordered = [v for pair in zip(first,last) for v in pair]
    assert all(x<y for x,y in zip(ordered,ordered[1:]))
    weights = reference["n200"]["string_weights"]
    slopes = [reference["n200"]["predicted_jacobian"][n][6] for n in [0,2]]
    jac_error = max(abs(weights[n]/weights[1]-v) for n,v in zip([0,2],slopes))
    harmonic_error = second_harmonic()
    assert decimal_error < D("1e-14") and translation_error < D("1e-36")
    assert harmonic_error < 1.e-12 and jac_error < 1.e-7
    report = dict(decimal_held_out_energies=[str(n) for n in predicted],
                  decimal_difference_from_numpy=float(decimal_error),
                  common_energy_origin_error=float(translation_error),
                  outside_spectra_interlace=True, middle_slope_error=jac_error,
                  two_harmonic_trigonometric_check=harmonic_error)
    (ROOT/"results"/"verification.json").write_text(json.dumps(report,indent=2)+"\n")

if __name__ == "__main__":
    main()

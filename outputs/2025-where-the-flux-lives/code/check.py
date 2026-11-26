"""Test the registered circle and rank-one predictions; render the paper figure."""
import csv
import json
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

def differentiate(function, x, h=1.e-4):
    return (function(x-2*h)-8*function(x-h)+8*function(x+h)-function(x+2*h))/(12*h)

def circle(amplitude, length, points=256):
    angle = 2*np.pi*np.arange(points)/points
    delta = angle[:, None] - angle[None, :]
    source = 1 + amplitude*np.cos(angle)

    def field_potential(r):
        kernel = np.sinh(r)/(r*(np.cosh(r)-np.cos(delta)))
        return (kernel @ source)/points

    def exchange(r):
        return -np.mean(source*field_potential(r))

    force = length**2*differentiate(exchange, length)
    midpoint = -differentiate(field_potential, length/2)
    moment = np.mean(np.cos(angle)*midpoint**2)/np.mean(midpoint**2)
    linear = amplitude*(1+length/2)*np.exp(-length/2)
    expected = [1+amplitude**2*(1+length)*np.exp(-length)/2,
                linear/(1+linear**2/2)]
    error = max(abs(force-expected[0]), abs(moment-expected[1]))
    assert error < 1.e-7
    return dict(a=amplitude, y=length, force=force, moment=moment,
                analytic=expected, max_error=error)

def invert(first, last):
    # numpy's polynomial coefficient arrays are in descending powers.
    trace_step = sum(last)-sum(first)
    if abs(trace_step) < 1.e-12:
        raise ValueError("Unresolved trace change")
    quadratic = (np.poly(first)-np.poly(last))[1:]/trace_step
    roots = np.roots(quadratic)
    if not np.isreal(roots).all():
        raise ValueError("Complex compressed thresholds")
    roots = np.sort(roots.real)
    if abs(roots[1]-roots[0]) < 1.e-12:
        raise ValueError("Coincident thresholds")
    couplings2 = -np.polyval(np.poly(first), roots)/(roots-roots[::-1])
    if min(couplings2) <= 0:
        raise ValueError("Nonpositive squared coupling")
    return roots, couplings2

def spectrum(u, roots, couplings2):
    h = np.sqrt(couplings2)
    return np.linalg.eigvalsh([[u,h[0],h[1]], [h[0],roots[0],0], [h[1],0,roots[1]]])

def predict(values):
    roots, h2 = invert(values[:3], values[3:6])
    energy = values[6]
    u = energy - sum(h2/(energy-roots))
    levels = spectrum(u, roots, h2)
    return roots, h2, u, levels

def study(levels, errors=None):
    first, middle, last = levels
    values = np.array([*first,*last,middle[1]])
    roots, h2, u, prediction = predict(values)
    if not roots[0] < middle[1] < roots[1]:
        raise ValueError("Conditioning level has inconsistent ordering")
    residual = prediction - middle
    weights = [1/(1+sum(h2/(e-roots)**2)) for e in prediction]
    result = dict(input_levels=levels.tolist(), thresholds=roots.tolist(),
                  abs_couplings=np.sqrt(h2).tolist(), u_middle=u,
                  predicted=prediction.tolist(), residual=residual.tolist(),
                  string_weights=weights, trace_step=sum(last)-sum(first))
    if errors is not None:
        eps = np.array([*errors[0],*errors[2],errors[1,1]])
        jac = np.column_stack([differentiate(lambda t: predict(values+t*direction)[3],
                                             0.,1.e-7)
                               for direction in np.eye(7)])
        # A bound for the first-order standard deviation for any correlations,
        # by the triangle inequality; it is not a confidence interval.
        result["displayed_errors"] = errors.tolist()
        result["predicted_jacobian"] = jac.tolist()
        result["residual_sd_if_independent"] = np.hypot(
            np.linalg.norm(jac*eps, axis=1), errors[1]).tolist()
        result["residual_sd_upper_first_order"] = (
            np.sum(np.abs(jac*eps),axis=1)+errors[1]).tolist()
        # At the supplied middle level the predicted residual is identically zero.
        result["residual_sd_if_independent"][1] = 0.
        result["residual_sd_upper_first_order"][1] = 0.
    return result

def main():
    out = ROOT/"results"
    out.mkdir(exist_ok=True)
    circle_results = [circle(a, 2.) for a in [.6,-.6]]
    roots = np.array([.0034,.1005])
    h2 = np.array([2*.0256**2,.0134**2])
    fit_levels = np.array([spectrum(-.835+.1061*r-.434/r, roots,h2) for r in [7,8,9]])
    calibration = study(fit_levels)
    assert max(np.abs(calibration["residual"])) < 1.e-8
    with (ROOT/"data"/"n200.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    levels = np.array([float(r["aE"]) for r in rows]).reshape(3,3)
    errors = np.array([float(r["displayed_error"]) for r in rows]).reshape(3,3)
    measured = study(levels, errors)
    result = {"circle":circle_results,"table4_control":calibration,"n200":measured}
    (out/"checks.json").write_text(json.dumps(result, indent=2)+"\n")

    fig, (left,right) = plt.subplots(1,2,figsize=(9,3.65),layout="constrained")
    ys = np.linspace(.05,8,250)
    coeff = .6*(1+ys/2)*np.exp(-ys/2)
    for sign,color in [(1,"#1a6982"),(-1,"#ad5529")]:
        left.plot(ys,sign*coeff/(1+coeff**2/2),color=color,
                  label=fr"midpoint moment, $a={sign*.6:+.1f}$")
    left.plot(ys,.18*(1+ys)*np.exp(-ys),"k--",label="excess force, both profiles")
    left.axhline(0,color=".7",lw=.6)
    left.set(xlabel=r"separation $L/B$",ylabel="dimensionless response",title="A. Flat compact circle")
    left.legend(frameon=False,fontsize=8)
    xs = np.array([17,19,21])
    for n,(color,marker) in enumerate(zip(["#224e75","#4d8058","#974b37"],["o","s","^"])):
        right.errorbar(xs,levels[:,n],yerr=errors[:,n],fmt=marker,color=color,
                       label=f"published level {n}",capsize=2)
    right.scatter([19,19],np.array(measured["predicted"])[[0,2]],marker="x",
                  color="black",label="conditional prediction",zorder=5)
    right.set(xticks=xs,xlabel=r"source separation $r/a$",ylabel=r"$a(V_n-2E_{Q\ell})$",
              title="B. N200, three separations")
    right.legend(frameon=False,fontsize=8)
    fig.savefig(out/"observables.png",dpi=190)
    plt.close(fig)

if __name__ == "__main__":
    main()

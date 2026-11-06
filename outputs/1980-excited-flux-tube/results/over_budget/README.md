# Runs over the 1980 budget (excluded)

Conventional-loop runs (`code/z2_excited_direct.py`) beyond what the 1980
budget allows: chains 9-16 at beta = 0.73 and all 16 chains at beta = 0.70.
Each configuration costs about 2e8 operations by the paper's cost model, so the
full set would have taken 182 of the 100 Cray-1 hours. The paper uses chains 1-8
at beta = 0.73 only. These files are kept for the record. No number in the paper
comes from them.

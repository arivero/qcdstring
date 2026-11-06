#!/bin/sh
# Production for Sections 3-4: 16 chains per coupling, Nt = L = 24, slabs of 4,
# 300 sub-updates per frozen configuration, two smearing steps.
cd "$(dirname "$0")"
for s in $(seq 1 16); do
  python3 -u z2_excited.py --beta 0.73 --Nt 24 --L 24 --tau 4 --nsub 300 --nout 150 --between 20 --therm 800 --Rmax 10 --nsmear 2 --seed $s > ../results/z2x_b0.730_s$s.log 2>&1 &
  python3 -u z2_excited.py --beta 0.70 --Nt 24 --L 24 --tau 4 --nsub 300 --nout 100 --between 20 --therm 800 --Rmax 8 --nsmear 2 --seed $s > ../results/z2x_b0.700_s$s.log 2>&1 &
done
wait

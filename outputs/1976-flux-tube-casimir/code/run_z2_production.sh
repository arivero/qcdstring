#!/bin/sh
# Production runs for Section 3.2: 12 independent chains per coupling,
# 50 outer configurations each, 500 sub-updates per outer configuration.
cd "$(dirname "$0")"
for s in 1 2 3 4 5 6 7 8 9 10 11 12; do
  python3 -u z2_multilevel.py --beta 0.73 --Nt 16 --L 32 --tau 4 --nsub 500 --nout 50 --between 20 --therm 800 --Rmax 10 --seed $s > ../results/z2ml_b0.730_s$s.log 2>&1 &
  python3 -u z2_multilevel.py --beta 0.70 --Nt 16 --L 24 --tau 4 --nsub 500 --nout 50 --between 20 --therm 800 --Rmax 10 --seed $s > ../results/z2ml_b0.700_s$s.log 2>&1 &
done
wait

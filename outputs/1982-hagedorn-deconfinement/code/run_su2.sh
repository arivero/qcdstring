#!/bin/sh
# SU(2) at finite temperature (1982 paper): time series of the closed
# time-like line on Nt x L^3 lattices, three couplings per lattice.
# 18 processes; about 25 minutes on a 16-core machine of 2026.
cd "$(dirname "$0")"
for b in 1.86 1.88 1.90; do
  python3 su2ft.py --Nt 2 --L 8  --beta $b --nsweep 12000 --therm 1000 &
  python3 su2ft.py --Nt 2 --L 12 --beta $b --nsweep 6000  --therm 1000 &
done
for b in 2.16 2.18 2.20; do
  python3 su2ft.py --Nt 3 --L 8  --beta $b --nsweep 12000 --therm 1000 &
  python3 su2ft.py --Nt 3 --L 12 --beta $b --nsweep 8000  --therm 1000 &
done
for b in 2.28 2.30 2.32; do
  python3 su2ft.py --Nt 4 --L 8  --beta $b --nsweep 12000 --therm 1000 &
  python3 su2ft.py --Nt 4 --L 12 --beta $b --nsweep 8000  --therm 1000 &
done
wait

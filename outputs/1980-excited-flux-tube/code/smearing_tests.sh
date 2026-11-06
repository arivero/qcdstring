#!/bin/sh
# Response, Minor 6: the three short smearing tests, kept this time
# (2, 6 and 12 smearing steps; 16 frozen configurations each, beta = 0.73).
cd "$(dirname "$0")"
for ns in 2 6 12; do
  python3 -u z2_excited.py --beta 0.73 --nout 16 --nsub 300 --therm 400 --seed 98 --nsmear $ns --Rmax 8 --tag _smeartest$ns > ../results/smeartest_$ns.log 2>&1 &
done
wait

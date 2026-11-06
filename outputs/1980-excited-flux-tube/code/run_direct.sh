#!/bin/sh
# Third production (Response, Major 1): conventional loops at T = 0..7, 16 chains per coupling.
# The 1980 budget covers seeds 1-8 at beta = 0.73 only; the paper uses those, and the
# rest is kept in results/over_budget/ and enters no number.
cd "$(dirname "$0")"
for s in $(seq 1 16); do
  python3 -u z2_excited_direct.py --beta 0.73 --nconf 1000 --Rmax 9 --seed $s > ../results/z2d_b0.730_s$s.log 2>&1 &
  python3 -u z2_excited_direct.py --beta 0.70 --nconf 1000 --Rmax 7 --seed $s > ../results/z2d_b0.700_s$s.log 2>&1 &
done
wait

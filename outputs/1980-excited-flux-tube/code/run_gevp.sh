#!/bin/sh
# Second production (Section 4.2): two operators per channel, 16 chains per coupling.
cd "$(dirname "$0")"
for s in $(seq 1 16); do
  python3 -u z2_excited_gevp.py --beta 0.73 --nout 150 --Rmax 10 --seed $s > ../results/z2g_b0.730_s$s.log 2>&1 &
  python3 -u z2_excited_gevp.py --beta 0.70 --nout 100 --Rmax 8 --seed $s > ../results/z2g_b0.700_s$s.log 2>&1 &
done
wait

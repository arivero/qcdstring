#!/bin/sh
# Gauge-theory wall correlators of closed time-like lines at beta = 0.73
# (1982 paper, Sections 3.1 and 3.4): the seventeen runs behind
# results/gauge_check.txt. Unsmeared lines with and without two-level
# averaging (z2_wall.py), smeared lines with a basis of four smearing levels
# (z2_tube.py). About two minutes on a 16-core machine of 2026.
cd "$(dirname "$0")"
P=../results/pilots
W="python3 z2_wall.py --beta 0.73 --outdir $P"
T="python3 z2_tube.py --beta 0.73 --outdir $P"
$W --Nt 8  --Lx 48 --Ly 16 --X 12 --slabs 4,4     --nsub 100 --nout 40  --seed 901 --tag _p2l &
$W --Nt 8  --Lx 48 --Ly 16 --X 12 --nout 40 --block 100 --seed 902 --tag _pplain &
$W --Nt 12 --Lx 48 --Ly 16 --X 10 --slabs 4,4,4   --nsub 100 --nout 60  --seed 911 --tag _p2l &
$W --Nt 12 --Lx 48 --Ly 16 --X 10 --nout 60 --block 150 --seed 912 --tag _pplain &
$W --Nt 16 --Lx 48 --Ly 16 --X 8  --slabs 4,4,4,4 --nsub 100 --nout 60  --seed 913 --tag _p2l &
$W --Nt 16 --Lx 48 --Ly 16 --X 8  --nout 60 --block 150 --seed 914 --tag _pplain &
$W --Nt 12 --Lx 48 --Ly 16 --X 10 --slabs 4,4,4   --nsub 25  --nout 240 --between 3 --seed 915 --tag _p2l25 &
$W --Nt 16 --Lx 48 --Ly 16 --X 8  --slabs 4,4,4,4 --nsub 25  --nout 240 --between 3 --seed 916 --tag _p2l25 &
$W --Nt 16 --Lx 48 --Ly 16 --X 8  --slabs 8,8     --nsub 100 --nout 60  --seed 917 --tag _p2l88 &
wait
$T --Nt 12 --Lx 48 --Ly 16 --X 6 --block 200 --nblock 40 --seed 921 --tag _pA &
$T --Nt 12 --Lx 48 --Ly 16 --X 6 --block 100 --nblock 40 --every 3 --seed 922 --tag _pB &
$T --Nt 12 --Lx 96 --Ly 8  --X 6 --block 200 --nblock 40 --seed 923 --tag _pC &
$T --Nt 12 --Lx 64 --Ly 12 --X 6 --block 200 --nblock 40 --seed 924 --tag _pD &
$T --Nt 12 --Lx 32 --Ly 24 --X 6 --block 200 --nblock 40 --seed 925 --tag _pE &
$T --Nt 16 --Lx 64 --Ly 12 --X 6 --block 200 --nblock 40 --seed 926 --tag _pF &
$T --Nt 8  --Lx 64 --Ly 12 --X 8 --block 200 --nblock 40 --seed 927 --tag _pG &
$T --Nt 8  --Lx 48 --Ly 16 --X 8 --block 200 --nblock 40 --seed 928 --tag _pH &
wait
python3 gauge_check.py

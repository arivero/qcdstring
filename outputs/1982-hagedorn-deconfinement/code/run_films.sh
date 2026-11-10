#!/bin/sh
# Critical couplings K_c(Nt) of the Ising film, Nt = 2, 3, 4 (1982 paper).
cd "$(dirname "$0")"
for spec in "2 0.2761" "3 0.2459" "4 0.2361"; do
  set -- $spec
  python3 ising_film.py --Nt $1 --L 16 --K $2 --nsweep 6250  --chains 8
  python3 ising_film.py --Nt $1 --L 24 --K $2 --nsweep 12500 --chains 8
  python3 ising_film.py --Nt $1 --L 32 --K $2 --nsweep 25000 --chains 8
  python3 ising_film.py --Nt $1 --L 48 --K $2 --nsweep 50000 --chains 8
done
# the same analysis on the two-dimensional Ising model (Nt = 1), whose K_c is exact
python3 ising_film.py --Nt 1 --L 16 --K 0.4407 --nsweep 6250  --chains 8
python3 ising_film.py --Nt 1 --L 24 --K 0.4407 --nsweep 12500 --chains 8
python3 ising_film.py --Nt 1 --L 32 --K 0.4407 --nsweep 25000 --chains 8
python3 ising_film.py --Nt 1 --L 48 --K 0.4407 --nsweep 50000 --chains 8

#!/bin/sh
# Thermodynamic-integration paths of the 1982 paper (dual Ising model).
# Each line is one geometry Nt x Lx x Ly and one stretch of couplings; several
# stretches of one geometry are joined by analyze82.py. About 15 minutes in
# all on a 16-core machine of 2026.
cd "$(dirname "$0")"
LOW="0.15:0.20:0.005,0.2025:0.24:0.0025"
# exact check in two dimensions (Nt = 1), against Kaufman's formula
python3 ising_path.py --Nt 1 --Lx 24 --Ly 12 --grid 0.20:0.60:0.02 --nsweep 20000 --Kpeak 0.44 --width 0.06 --name c2d --seed 1
# first series (Nt = 8 at four transverse and longitudinal sizes; Nt = 12, 16), seed 2
python3 ising_path.py --Nt 8  --Lx 24 --Ly 12 --grid $LOW --nsweep 20000 --name q8a --seed 2
python3 ising_path.py --Nt 16 --Lx 24 --Ly 12 --grid $LOW --nsweep 20000 --name q16 --seed 2
python3 ising_path.py --Nt 8  --Lx 24 --Ly 16 --grid $LOW --nsweep 20000 --name q8b --seed 2
python3 ising_path.py --Nt 8  --Lx 24 --Ly 8  --grid $LOW --nsweep 20000 --name q8c --seed 2
python3 ising_path.py --Nt 8  --Lx 48 --Ly 12 --grid $LOW --nsweep 20000 --name q8d --seed 2
python3 ising_path.py --Nt 12 --Lx 24 --Ly 12 --grid $LOW --nsweep 20000 --name q12 --seed 2
# continuations to stronger gauge coupling (larger K)
python3 ising_path.py --Nt 16 --Lx 24 --Ly 12 --grid 0.2425:0.285:0.0025 --nsweep 20000 --name q16x --seed 3
python3 ising_path.py --Nt 12 --Lx 24 --Ly 12 --grid 0.2425:0.285:0.0025 --nsweep 20000 --name q12x --seed 3
python3 ising_path.py --Nt 8  --Lx 24 --Ly 12 --grid 0.2425:0.285:0.0025 --nsweep 20000 --name q8ax --seed 3
python3 ising_path.py --Nt 8  --Lx 24 --Ly 16 --grid 0.2425:0.2625:0.0025 --nsweep 20000 --name q8bx --seed 3
# further tube lengths
python3 ising_path.py --Nt 10 --Lx 24 --Ly 12 --grid 0.15:0.20:0.005,0.2025:0.2625:0.0025 --nsweep 20000 --name g10 --seed 4
python3 ising_path.py --Nt 7  --Lx 24 --Ly 16 --grid 0.15:0.20:0.005,0.2025:0.2625:0.0025 --nsweep 20000 --name g7 --seed 4
python3 ising_path.py --Nt 6  --Lx 32 --Ly 20 --grid 0.15:0.20:0.005,0.2025:0.2625:0.0025 --nsweep 20000 --name g6 --seed 4
python3 ising_path.py --Nt 5  --Lx 24 --Ly 16 --grid 0.15:0.20:0.005,0.2025:0.285:0.0025 --nsweep 15000 --name g5 --seed 4
python3 ising_path.py --Nt 4  --Lx 48 --Ly 32 --grid 0.15:0.20:0.005,0.2025:0.285:0.0025 --nsweep 10000 --Kpeak 0.232 --name g4 --seed 4
python3 ising_path.py --Nt 3  --Lx 48 --Ly 32 --grid 0.15:0.20:0.005,0.2025:0.30:0.0025 --nsweep 10000 --Kpeak 0.240 --name g3 --seed 4
# second, independent runs (added after the first analysis): the two longest tubes
# at weak gauge coupling, and the two-dimensional check with four times the sweeps
python3 ising_path.py --Nt 16 --Lx 24 --Ly 12 --grid $LOW --nsweep 20000 --name q16r --seed 6
python3 ising_path.py --Nt 12 --Lx 24 --Ly 12 --grid $LOW --nsweep 20000 --name q12r --seed 6
python3 ising_path.py --Nt 1 --Lx 24 --Ly 12 --grid 0.20:0.60:0.02 --nsweep 80000 --Kpeak 0.44 --width 0.06 --name c2dr --seed 6

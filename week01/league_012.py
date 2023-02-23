#!/usr/bin/env python3

import sys

lines = []
for line in sys.stdin:
   lines.append(line.strip().split())

clubs = []
for line in lines:
   clubs.append(" ".join(line[1:-8]))

max_width = 0
for club in clubs:
   if len(club) > max_width:
      max_width = len(club)

h = ["POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"]
print(f"{h[0]:>3s} {h[1]:{max_width:d}s} {h[2]:>2s} {h[3]:>3s} {h[4]:>3s}"
      f" {h[5]:>3s} {h[6]:>3s} {h[7]:>3s} {h[8]:>3s} {h[9]:>3s}")

for line in lines:
   pos = line[0]
   club = " ".join(line[1:-8])
   p = line[-8]
   w = line[-7]
   d = line[-6]
   l = line[-5]
   gf = line[-4]
   ga = line[-3]
   gd = line[-2]
   pts = line[-1]
   print(f"{pos:>3s} {club:{max_width:d}s} {p:>2s} {w:>3s} {d:>3s} {l:>3s} {gf:>3s}"
         f"{ga:>4s} {gd:>3s} {pts:>3s}")


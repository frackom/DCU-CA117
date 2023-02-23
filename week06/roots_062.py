#!/usr/bin/env python3

from sys import stdin
from math import sqrt

def roots(a, b, c):
   d = b ** 2 - (4 * a * c)
   if d < 0:
      return None
   else:
      x = (-b - sqrt(d)) / (2 * a)
      y = (-b + sqrt(d)) / (2 * a)
      return f"{x:.1f}, {y:.1f}"

for line in stdin:
   line = line.rstrip().split()
   a, b, c = int(line[0]), int(line[1]), int(line[2])
   print(roots(a, b, c))

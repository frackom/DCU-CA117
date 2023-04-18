#!/usr/bin/env python3

from sys import stdin

for line in stdin:
   line = line.rstrip().split()
   cakes = sorted([int(c) for c in line], reverse=True)
   free = cakes[2::3]
   print(sum(cakes) - sum(free))

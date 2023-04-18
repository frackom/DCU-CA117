#!/usr/bin/env python3

from sys import stdin

q = {(True, True) : 1,
     (True, False) : 2,
     (False, False) : 3,
     (False, True) : 4}

for line in stdin:
   line = line.rstrip().split()
   x, y = line
   print(q[(int(x) > 0, int(y) > 0)])

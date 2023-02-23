#!/usr/bin/env python3

import sys

for line in sys.stdin:
   line = line.lower()
   line = line.strip()
   i = 0
   while i < len(line):
      if not("a" < line[i] < "z" or "A" < line[i] < "Z"):
         line = line.replace(line[i], "")
      i += 1
   backwards = line[::-1]
   print(line == backwards)

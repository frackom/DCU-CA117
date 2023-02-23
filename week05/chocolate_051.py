#!/usr/bin/env python3

from sys import stdin

choc = 400

for line in stdin:
   line = line.rstrip()
   if int(line) < choc:
      print(1)
   else:
      print(int(line) // choc)

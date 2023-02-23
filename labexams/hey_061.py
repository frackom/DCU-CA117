#!/usr/bin/env python3

from sys import stdin

for line in stdin:
   line = line.rstrip()
   for letter in line:
      if letter == "e":
         line = line.replace("e", "ee", 1)
   print(line)

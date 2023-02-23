#!/usr/bin/env python3

from sys import stdin

for line in stdin.readlines():
   numbers = line.split()
   unique = [n.strip() for n in numbers if numbers.count(n) == 1]
   if not unique:
      print("none")
   else:
      print(max(unique))

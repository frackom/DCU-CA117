#!/usr/bin/env python3

from sys import stdin

for line in stdin:
   x = int(line.rstrip())
   while 0 < int(x):
      y = 1
      for c in str(x).replace("0", ""):
         y = y * int(c)
      y = str(y).replace("0", "")
      if int(y) <= 9 and 1 <= int(y):
         print(y)
         break
      else:
         x = y

#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
while 0 < len(s):
   mid = len(s) // 2
   if len(s) % 2 == 1:
      print(s[mid])
   else:
      print("No middle character!")
   s = sys.stdin.readline().rstrip()

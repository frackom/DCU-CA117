#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
while 0 < len(s):
   cap1 = s[0].capitalize()
   middle = s[1:len(s) - 1]
   cap2 = s[len(s) - 1].capitalize()
   if len(s) > 1:
      print(cap1 + middle + cap2)
   s = sys.stdin.readline().rstrip()

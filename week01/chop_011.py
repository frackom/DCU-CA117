#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
while 0 < len(s):
   removed = s[1:len(s) - 1]
   if len(removed) > 0:
      print(removed)
   s = sys.stdin.readline().rstrip()

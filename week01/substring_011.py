#!/usr/bin/env python3

import sys

s = sys.stdin.readline().split()
while 0 < len(s):
   sub = s[0].lower()
   word = s[1].lower()
   if sub in word:
      print("True")
   else:
      print("False")
   s = sys.stdin.readline().split()

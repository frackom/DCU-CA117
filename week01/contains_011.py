#!/usr/bin/env python3

import sys

s = sys.stdin.readline().split()
while 0 < len(s):
   char = s[0].lower()
   word = s[1].lower()
   for a in word:
      char = char.replace(a, "", 1)
   if len(char) > 0:
      print("False")
   else:
      print("True")
   s = sys.stdin.readline().split()

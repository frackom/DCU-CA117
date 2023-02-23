#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()

while 0 < len(s):
   tokens = s.strip().split()
   i = 0
   while i < len(tokens):
      if tokens[i].startswith("m"):
         tokens[i] = tokens[i].capitalize()
         break
      i += 1
   print(" ".join(tokens))
   s = sys.stdin.readline().rstrip()

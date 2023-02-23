#!/usr/bin/env python3

import sys

email = sys.stdin.readline().rstrip()
while 0 < len(email):
   line1 = email.split("@")
   line2 = line1[0].split(".")
   first = line2[0]
   last = line2[1]
   i = 0
   while i < len(last):
      if last[i].isdigit():
         last = str(last[0:i])
      i += 1
   print(first.capitalize(), last.capitalize())
   email = sys.stdin.readline().rstrip()

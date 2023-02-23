#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as data1, open(sys.argv[2], "r") as data2:
   num1 = data1.read().strip().split()
   num2 = data2.read().strip().split()

   i = 0
   while i < len(num1):
      print(int(num1[i]))
      print(int(num2[i]))
      i += 1


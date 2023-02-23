#!/usr/bin/env python3

import sys

length = 0

lines = sys.stdin.readlines()

for line in lines:
   if len(line) > length:
      length = len(line)
for line in lines:
   print(f"{line.rstrip():^{length - 1}}")


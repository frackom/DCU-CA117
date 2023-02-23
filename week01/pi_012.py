#!/usr/bin/env python3

import sys
import math

line = sys.stdin.readline().rstrip()
while 0 < len(line):
   print(f"{math.pi:.{int(line)}f}")
   line = sys.stdin.readline().rstrip()

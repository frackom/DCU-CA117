#!/usr/bin/env python3

import sys

h = ["POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"]
print(f"{h[0]:>3s} {h[1]:22s} {h[2]:>2s} {h[3]:>3s} {h[4]:>3s} {h[5]:>3s} {h[6]:>3s} {h[7]:>3s} {h[8]:>3s}")

line = sys.stdin.readline().rstrip()
while 0 < len(line):
   line = line.split()
   if line[2].isdigit():
      print(f"{line[0]:>3s} {line[1]:20s} {line[2]:>2s} {line[3]:>3s} {line[4]:>3s} {line[5]:>3s} {line[6]:>3s} {line[7]:>3s} {line[8]:>3s}")
   elif line[3].isdigit():
      print(f"{line[0]:>3s} {(line[1] + line[2]):22s} {line[3]:>2s} {line[4]:>3s} {line[5]:>3s} {line[6]:>3s} {line[7]:>3s} {line[8]:>3s} {line[9]:>3s}")
   line = sys.stdin.readline().rstrip()


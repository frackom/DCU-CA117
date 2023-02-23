#!/usr/bin/env python3

from sys import stdin

data = stdin.readlines()
line1 = data[0].rstrip()
line2 = data[1].rstrip()

line3 = []
i = 0
while i < len(line1):
   if line1[i] == line2[i]:
      line3.append("-")
   elif line1[i] != line2[i]:
      line3.append("*")
   i += 1

print(line1)
print(line2)
print("".join(line3))

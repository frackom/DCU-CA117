#!/usr/bin/env python3

from sys import stdin

t = []
d = []

for line in stdin:
   line = line.rstrip().split()
   t.append(int(line[0]))
   d.append(int(line[1]))

s = 0
i = 0
while i < len(t) - 1:
   tmp = (d[i + 1] - d[i]) // (t[i + 1] - t[i])
   if tmp > s:
      s = tmp
   i += 1

print(s)

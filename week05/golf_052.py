#!/usr/bin/env python3

from sys import stdin

d = {}
disq = []
for line in stdin:
   try:
      line = line.rstrip().split()
      name = " ".join(line[:-3])
      shots = 0
      for n in line[-3:]:
         shots += int(n)
      d[name] = shots
   except ValueError:
      disq.append(name)
      error = 1

for k, v in sorted(d.items(), key=lambda item: item[1]):
   print(f"{k}: {v}")

try:
   if error == 1:
      print(f"Disqualified: {', '.join(disq)}")
except NameError:
   pass

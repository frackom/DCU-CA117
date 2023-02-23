#!/usr/bin/env python3

from sys import stdin

count = 0
d = {}
everylist = {}
for line in stdin:
   line = line.rstrip().split()
   for animal in line:
      if animal in d:
         d[animal] += 1
      else:
         d[animal] = 1
   count = count + 1

for k, v in d.items():
   if v == count:
     everylist[k] = 1

print(len(everylist.items()))
for k, v in everylist.items():
   print(f"{k}")

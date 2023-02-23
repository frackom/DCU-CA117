#!/usr/bin/env python3

from sys import stdin

denied = 0
capacity = int(stdin.readline())
for line in stdin:
   line = line.split()
   if line[0] == "enter":
      if int(line[1]) > capacity:
         denied = denied + 1
      else:
         capacity = capacity - int(line[1])
   elif line[0] == "leave":
      capacity = capacity + int(line[1])

print(denied)

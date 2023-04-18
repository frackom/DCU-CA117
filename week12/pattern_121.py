#!/usr/bin/env python3

from sys import stdin

pattern = stdin.readline().rstrip()
lines = stdin.readlines()

dash = []
for i, letter in enumerate(pattern):
   if letter == "-":
      dash.append(i)

output = []
for line in lines:
   dupe = line[:]
   line = list(line.rstrip())
   for i in dash:
      try:
         line[i] = "-"
      except IndexError:
         pass
   if "".join(line) == pattern:
      output.append(dupe.rstrip())

if len(output) > 0:
   print(", ".join(output))

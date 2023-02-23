#!/usr/bin/env python3

import sys

d = {}
letters = ["A", "B", "C", "D", "E", "F"]
data = sys.stdin.readlines()
numbers = sorted(data[0].rstrip().split())
position = data[1].rstrip()

i = 0
while i < len(position):
   d[letters[i]] = numbers[i]
   i += 1

a = []

for letter in position:
   a.append(d[letter])

print(" ".join(a))

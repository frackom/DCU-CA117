#!/usr/bin/env python3

from sys import stdin

names = [name.rstrip() for name in stdin]

first = []
second = []
for i, word in enumerate(names):
   if i % 2 == 0:
      first.append(word)
   else:
      second.append(word)

second.reverse()
sym = first + second

for name in sym:
   print(name)

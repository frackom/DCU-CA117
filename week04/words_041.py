#!/usr/bin/env python3

from sys import stdin
from string import punctuation
words = {}

for line in stdin:
   line = line.rstrip().split()
   for word in line:
      word = word.lower().strip(punctuation)
      if word not in words:
         words[word] = 1
      elif word in words:
         words[word] += 1

for k, v in sorted(words.items()):
   print(f"{k} : {v}")

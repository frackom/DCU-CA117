#!/usr/bin/env python3

from sys import stdin

vowels = {"a", "e", "i", "o", "u"}

for line in stdin:
   output = ""
   words = line.rstrip()
   i = 0
   while i < len(words):
      output += words[i]
      if words[i] in vowels:
         i += 3
      else:
         i += 1
   print(output)

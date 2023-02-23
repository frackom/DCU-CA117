#!/usr/bin/env python3

from sys import stdin

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for word in stdin:
   word = word.rstrip().lower()
   for letter in word:
      if letter in vowels:
        vowels[letter] += 1

padding = len(str(max(vowels.values())))

def tagger(item):
   return item[1]

for k, v in sorted(vowels.items(), key=tagger, reverse=True):
   print(f"{k} : {v:{padding}}")

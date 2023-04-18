#!/usr/bin/env python3

from sys import stdin

vowels = {"a", "e", "i", "o", "u"}

words = {word.rstrip(): 0 for word in stdin}

for word in words:

   double = 0
   i = 0
   while i < len(word) - 1:
      if word[i] in vowels and word[i] == word[i + 1]:
         double += 1
         i += 2
      else:
         i += 1
   words[word] = double

for k, v in sorted(words.items(), key=lambda x: x[1], reverse=True):
   print(f"{k}")
   break

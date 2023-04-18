#!/usr/bin/env python3

from sys import stdin
from string import punctuation

unique = {}

ans = []
for line in stdin:
   line = line.rstrip()
   output = []
   for word in line.split():
      word_output = ""
      for letter in word:
         if letter not in punctuation:
            word_output += letter
      word_output = word_output.lower()
      if word_output not in unique:
         unique[word_output] = 1
         output.append(word)
      else:
         output.append(".")
   ans.append(" ".join(output))

print("\n".join(ans))

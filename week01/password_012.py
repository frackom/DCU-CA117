#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

for word in s:
   char = [0, 0, 0, 0]
   word = word.rstrip()
   for letter in word:
      if letter.isdigit():
         char[0] = 1
      elif letter.islower():
         char[1] = 1
      elif letter.isupper():
         char[2] = 1
      else:
         char[3] = 1

   print(char[0] + char[1] + char[2] + char[3])

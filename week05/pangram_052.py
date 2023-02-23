#!/usr/bin/env python3

from sys import stdin

for line in stdin:
   line = line.rstrip()
   line = line.lower().replace(" ", "")
   pan = "abcdefghijklmnopqrstuvwxyz"
   for letter in line:
      if letter in pan:
         pan = pan.replace(letter, "", 1)
   if len(pan) == 0:
      print("pangram")
   else:
      print(f"missing {pan}")

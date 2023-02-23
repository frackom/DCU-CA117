#!/usr/bin/env python3

from sys import stdin

nums = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}

for line in stdin:
   words = []
   line = line.rstrip().split()
   for n in line:
      if n in nums:
         words.append(nums[n])
      else:
         words.append("unknown")
   print(" ".join(words))

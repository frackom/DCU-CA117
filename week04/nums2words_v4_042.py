#!/usr/bin/env python3

from sys import stdin

nums = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",
        "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
        "14": "fourteen", "15": "fifteen", "16": "sixteen",
        "17": "seventeen", "18": "eighteen", "19": "nineteen", "20": "twenty",
        "30" : "thirty", "40": "forty", "50": "fifty", "60": "sixty",
        "70": "seventy", "80": "eighty", "90": "ninety", "100": "one hundred"}


for line in stdin:
   words = []
   line = line.rstrip().split()
   for n in line:
      if n in nums:
         words.append(nums[n])
      else:
         num1 = int(n[0])
         num2 = int(n[1])
         words.append(nums[str(num1 * 10)] + "-" + nums[str(num2)])
   print(" ".join(words))

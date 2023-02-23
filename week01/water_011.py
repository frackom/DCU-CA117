#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
litres = s[0].rstrip()
buckets = s[1].split()

total = 0
i = 0
while i < len(buckets):
   total = total + int(buckets[i])
   if int(litres) < total:
      end = i
      break
   else:
      end = len(buckets)
   i += 1

print(end)

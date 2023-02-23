#!/usr/bin/env python3

import sys
import string

lines = sys.stdin.readlines()
unique = []

for line in lines:
   tokens = line.strip().split()
   for token in tokens:
      token = token.lower()
      for c in token:
         if c in string.punctuation:
            token = token.replace(c, "")
      if token.isalnum() and token not in unique:
         unique.append(token)

print(len(unique))

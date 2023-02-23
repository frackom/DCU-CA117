#!/usr/bin/env python3

import sys

for line in sys.stdin:
   tokens = line.split()
   word1 = tokens[0]
   word2 = tokens[1]
   print(sorted(word1) == sorted(word2))

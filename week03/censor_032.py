#!/usr/bin/env python3

import sys

censoredWords = []
with open(sys.argv[1], "r") as f:
   censoredWords = [word.rstrip() for word in f]

text = [line.rstrip() for line in sys.stdin]

for word in censoredWords:
   text = [line.replace(word, "@" * len(word)) for line in text]

for line in text:
   print(line)


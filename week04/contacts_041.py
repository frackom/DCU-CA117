#!/usr/bin/env python3

import sys

contacts = {}

with open(sys.argv[1], "r") as f:
   for line in f:
      line = line.split()
      name = line[0].rstrip()
      num = line[1].rstrip()
      contacts[name] = num

for line in sys.stdin:
   try:
      print(f"Name: {line.rstrip()}")
      print(f"Phone: {contacts[line.rstrip()]}")
   except KeyError:
      print("No such contact")

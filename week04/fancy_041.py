#!/usr/bin/env python3

import sys

contacts = {}

with open(sys.argv[1], "r") as f:
   for line in f:
      line = line.split()
      name = line[0].rstrip()
      num = line[1].rstrip()
      email = line[2].rstrip()
      contacts[name] = (num, email)

for line in sys.stdin:
   try:
      print(f"Name: {line.rstrip()}")
      print(f"Phone: {contacts[line.rstrip()][0]}")
      print(f"Email: {contacts[line.rstrip()][1]}")
   except KeyError:
      print("No such contact")

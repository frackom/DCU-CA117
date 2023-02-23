#!/usr/bin/env python3

from sys import stdin

data = stdin.readlines()
start = data[0].rstrip()
seq = data[1].rstrip()

cups = {1: "", 2: "", 3: ""}
cups[int(start)] = "prize"

for letter in seq:
   if letter == "A":
      cups[1], cups[2] = cups[2], cups[1]
   if letter == "B":
      cups[2], cups[3] = cups[3], cups[2]
   if letter == "C":
      cups[1], cups[3] = cups[3], cups[1]

for k, v in cups.items():
   if v == "prize":
      print(k)

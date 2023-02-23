#!/usr/bin/env python3

import sys

vowels = ["a", "e", "i", "o", "u"]
end = ["ch", "sh", "x", "s", "z", "o"]

line = sys.stdin.readline().rstrip()
while 0 < len(line):
   if line[len(line) - 1] in end or line[len(line) - 2:] in end:
      print(line + "es")
   elif line[len(line) - 2] not in vowels and line[len(line) - 1] == "y":
      print(line[:len(line) - 1] + "ies")
   elif line[len(line) - 1] == "f":
      print(line[:len(line) - 1] + "ves")
   elif line[len(line) - 2:] == "fe":
      print(line[:len(line) - 2] + "ves")
   else:
      print(line + "s")
   line = sys.stdin.readline().rstrip()

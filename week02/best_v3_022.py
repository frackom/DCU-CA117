#!/usr/bin/env python3

import sys
bestMark = 0
name = []
try:
   with open(sys.argv[1], "r") as f:
      for line in f:
         try:
            data = line.strip().split()
            mark = data[0]
            mark = int(mark)
            name = " ".join(data[1:])

            if mark > bestMark:
               bestMark, bestStudent = mark, name
         except ValueError:
            print(f"Invalid mark {mark} encountered. Skipping.")

      print(f"Best student: {bestStudent)}")
      print(f"Best mark: {bestMark}")

except FileNotFoundError:
   print(f"The file {sys.argv[1]} does not exist.")

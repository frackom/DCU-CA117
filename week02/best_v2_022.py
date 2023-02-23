#!/usr/bin/env python3

import sys
bestMark = 0

try:
   with open(sys.argv[1], "r") as f:
      for line in f:
         data = line.strip().split()
         mark = data[0]
         mark = int(mark)
         name = " ".join(data[1:])

         if mark > bestMark:
            bestMark, bestStudent = mark, name

      print(f"Best student: {bestStudent}")
      print(f"Best mark: {bestMark}")

except ValueError:
   print(f"Invalid mark {mark} encountered. Exiting.")

except FileNotFoundError:
   print(f"The file {sys.argv[1]} does not exist.")

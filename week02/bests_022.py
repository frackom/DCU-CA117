#!/usr/bin/env python3

import sys
bestMark = -1
try:
   with open(sys.argv[1], "r") as f:
      for line in f:
         try:
            data = line.strip().split()
            mark = data[0]
            mark = int(mark)
            name = " ".join(data[1:])

            if mark > bestMark:
               bestMark, bestStudent = mark, [name]
            elif mark == bestMark:
               bestStudent.append(name)
         except ValueError:
            print(f"Invalid mark {mark} encountered. Skipping.")

      print(f'Best student(s): {", ".join(bestStudent)}')
      print(f"Best mark: {bestMark}")

except FileNotFoundError:
   print(f"The file {sys.argv[1]} does not exist.")

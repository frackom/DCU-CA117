#!/usr/bin/env python3

import sys
import calendar

poem = [
"Monday's child is fair of face.",
"Tuesday's child is full of grace.",
"Wednesday's child is full of woe.",
"Thursday's child has far to go.",
"Friday's child is loving and giving.",
"Saturday's child works hard for a living.",
"Sunday's child is fair and wise and good in every way."]

born = "You were born on a"

for line in sys.stdin:
   day, month, year = line.strip().split()
   date = calendar.weekday(int(year), int(month), int(day))
   if date == 0:
      print(f"{born} Monday and {poem[0]}")
   if date == 1:
      print(f"{born} Tuesday and {poem[1]}")
   if date == 2:
      print(f"{born} Wednesday and {poem[2]}")
   if date == 3:
      print(f"{born} Thursday and {poem[3]}")
   if date == 4:
      print(f"{born} Friday and {poem[4]}")
   if date == 5:
      print(f"{born} Saturday and {poem[5]}")
   if date == 6:
      print(f"{born} Sunday and {poem[6]}")

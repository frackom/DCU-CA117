#!/usr/bin/env python3

from sys import stdin

def binsearch(query, sortedList):
   low = 0
   high = len(sortedList) - 1

   while low <= high:
       mid = (low + high) // 2

       if sortedList[mid] < query:
           low = mid + 1

       elif sortedList[mid] > query:
           high = mid - 1

       else:
           return True

   return False

list = [word.rstrip() for word in stdin if len(word.rstrip()) >= 5]
low_list = [word.lower() for word in list]

print([word for word in list if binsearch(word[::-1].lower(), low_list)])


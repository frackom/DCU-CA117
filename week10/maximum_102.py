#!/usr/bin/env python3

def maximum(list):
   if len(list) == 1:
      return list[0]
   if list[0] > list[1]:
      list.remove(list[1])
   else:
      list.remove(list[0])
   return maximum(list)

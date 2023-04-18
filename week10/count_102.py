#!/usr/bin/env python3

def count(word):
   if word == "":
      return 0
   else:
     return count(word[1:]) + 1

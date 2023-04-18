#!/usr/bin/env python3

def collatz(n):
   print(n)
   if n == 1:
      return 0
   elif n % 2 == 0:
      n = n // 2
      collatz(n)
   else:
      n = n * 3 + 1
      collatz(n)


#!/usr/bin/env python3

def get_divisors(n):
   l = []
   for i in range(1, n + 1):
      if n % i == 0:
         l.append(i)
   return l

def get_proper_divisors(n):
   return get_divisors(n)[:-1]

def is_perfect(n):
   d = get_proper_divisors(n)
   total = 0
   for i in d:
      total = total + i
   if total == n:
      return True
   else:
      return False

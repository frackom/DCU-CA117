#!/usr/bin/env python3

from math import sqrt

class Stack(object):

   def __init__(self):
      self.l = []

   def push(self, e):
      self.l.append(e)

   def pop(self):
      return self.l.pop()

   def top(self):
      return self.l[-1]

   def is_empty(self):
      return len(self.l) == 0

   def __len__(self):
      return len(self.l)

def calculator(line):

   s = Stack()

   binops = {"+": float.__add__,
             "-": float.__sub__,
             "*": float.__mul__,
             "/": float.__truediv__}

   uniops = {"n": float.__neg__,
             "r": sqrt}

   line = line.split()
   for n in line:
      if n not in binops and n not in uniops:
         s.push(float(n))
      elif n in binops:
         num2 = s.pop()
         num1 = s.pop()
         s.push(binops[n](num1, num2))
      elif n in uniops:
         s.push(uniops[n](s.pop()))

   return s.top()


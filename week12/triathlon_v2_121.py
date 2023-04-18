#!/usr/bin/env python3

class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def __str__(self):
      return f"Name: {self.name}" + "\n" + f"ID: {self.tid}"

def sort_on(t):
   return t.name

class Triathlon(object):

   def __init__(self):
      self.d = {}

   def add(self, other):
      if other not in self.d:
         self.d[other.tid] = other

   def remove(self, other):
      if other in self.d:
         del self.d[other]

   def lookup(self, other):
      if other in self.d:
         return self.d[other]
      else:
         return None

   def __str__(self):
      details = [f'{t}' for t in sorted(self.d.values(), key=sort_on)]
      return "\n".join(details)

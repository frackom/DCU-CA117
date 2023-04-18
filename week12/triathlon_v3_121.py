#!/usr/bin/env python3

class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.times = {}

   def __str__(self):
      return f"Name: {self.name}" + "\n" + f"ID: {self.tid}" + "\n" + f"Race time: {self.total_time()}"

   def add_time(self, discipline, time):
      self.times[discipline] = time

   def get_time(self, discipline):
      return self.times[discipline]

   def total_time(self):
      return sum(self.times.values())

   def __eq__(self, other):
      return self.total_time() == other.total_time()

   def __gt__(self, other):
      return self.total_time() > other.total_time()

   def __lt__(self, other):
      return self.total_time() < other.total_time()

def sort_on(t):
   return t.name

class Triathlon(object):

   def __init__(self):
      self.d = {}

   def add(self, other):
      self.d[other.tid] = other

   def remove(self, other):
      if other in self.d:
         del(self.d[other])

   def lookup(self, other):
      if other in self.d:
         return self.d[other]
      else:
         return None

   def __str__(self):
      details = [f"{t}" for t in sorted(self.d.values(), key=sort_on)]
      return "\n".join(details)

   def worst(self):
      return max(self.d.values())

   def best(self):
      return min(self.d.values())

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



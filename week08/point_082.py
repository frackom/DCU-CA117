#!/usr/bin/env python3

class Point:

   def __init__(self, x=0, y=0):
      self.x, self.y = x, y

   def distance(self, p2):
      d = ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5
      return d

   def __str__(self):
      return f"({self.x:.1f}, {self.y:.1f})"

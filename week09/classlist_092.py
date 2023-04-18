#!/usr/bin/env python3

class Student(object):

   def __init__(self, name, sid, modlist=None):
      self.name = name
      self.sid = sid
      if modlist is None:
         modlist = []
      else:
         self.modlist = modlist

   def __lt__(self, other):
      return self.avg_mark() < other.avg_mark()

   def __le__(self, other):
      return self.avg_mark() <= other.avg_mark()

   def __gt__(self, other):
      return self.avg_mark() > other.avg_mark()

   def __ge__(self, other):
      return self.avg_mark() >= other.avg_mark()

   def add_module(self, module):
      if module not in self.modlist:
         self.modlist.append(module)

   def del_module(self, module):
      if module in self.modlist:
         self.modlist.remove(module)

   def avg_mark(self):
      return round(sum([int(n[1]) for n in self.modlist]) / len(self.modlist))

   def __str__(self):
      output = []
      output.append(f"Name: {self.name}")
      output.append(f"ID: {self.sid}")
      total_modules = ", ".join(sorted([m[0] for m in self.modlist]))
      output.append(f"Modules: {total_modules}")
      output.append(f"Average mark: {self.avg_mark()}")
      return "\n".join(output)

class Classlist(object):

   def __init__(self, d=None):
      self.d = {} if d is None else d

   def add(self, student):
      self.d[student.sid] = student

   def __str__(self):
      output = []
      for v in sorted(self.d.values(), reverse=True):
         output.append(f"{v}")
      return "\n".join(output)

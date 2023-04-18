#!/usr/bin/env python3

class Student(object):

   def __init__(self, name, sid, modlist=None):
      self.name = name
      self.sid = sid
      if modlist is None:
         modlist = []
      else:
         self.modlist = modlist

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

#!/usr/bin/env python3

class Student:

   def __init__(self, sid, name, modlist=None):
      self.sid = sid
      self.name = name
      if modlist is None:
         self.modlist = []
      else:
         self.modlist = modlist

   def add_module(self, module):
      if module not in self.modlist:
         self.modlist.append(module)

   def del_module(self, module):
      if module in self.modlist:
         self.modlist.remove(module)

   def __str__(self):
      str = []
      str.append(f"ID: {self.sid}")
      str.append(f"Name: {self.name}")
      str.append(f"Modules: {', '.join(sorted(self.modlist))}")
      return "\n".join(str)

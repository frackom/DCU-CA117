#!/usr/bin/env python3

class Student:

   def set_attributes(self, sid, name, modlist):
      self.sid = sid
      self.name = name
      self.modlist = modlist

   def print_attributes(self):
      print("ID:", self.sid)
      print("Name:", self.name)
      print("Modules:", ", ".join(self.modlist))

   def add_module(self, module):
      if module not in self.modlist:
         self.modlist.append(module)

   def del_module(self, module):
      if module in self.modlist:
         self.modlist.remove(module)

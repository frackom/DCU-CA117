#!/usr/bin/env python3

class Contact(object):

   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return f"{self.name} {self.phone} {self.email}"

class Contactlist(object):

   def __init__(self, d=None):
      self.d = {} if d is None else d

   def add(self, other):
      self.d[other.name] = other

   def remove(self, other):
      if other in self.d:
         del self.d[other]

   def get(self, other):
      if other in self.d:
         return self.d[other]
      else:
         return None

   def __str__(self):
      output = []
      output.append("Contact list")
      output.append("------------")
      for k, v in sorted(self.d.items()):
         output.append(f"{v}")
      return "\n".join(output)

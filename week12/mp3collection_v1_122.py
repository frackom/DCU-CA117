#!/usr/bin/env python3

class MP3Track(object):
   def __init__(self, title, duration):
      self.title = title
      self.duration = duration

   def __str__(self):
      return f"Title: {self.title}" + "\n" + f"Duration: {self.duration}"

class MP3Collection(object):
   def __init__(self):
      self.tracks = {}

   def add(self, track):
      if track not in self.tracks:
         self.tracks[track.title] = track

   def remove(self, track):
      if track in self.tracks:
         del(self.tracks[track])

   def lookup(self, track):
      if track in self.tracks:
         return self.tracks[track]
      else:
         return None

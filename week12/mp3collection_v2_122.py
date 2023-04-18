#!/usr/bin/env python3

class MP3Track(object):
   def __init__(self, title, duration, artists):
      self.title = title
      self.duration = duration
      self.artists = artists

   def __str__(self):
      output = []
      output.append(f"Title: {self.title}")
      output.append(f"By: {', '.join(self.artists)}")
      output.append(f"Duration: {self.duration}")
      return "\n".join(output)

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

   def __add__(self, other):
      c = MP3Collection()
      for mp3 in self.tracks.values():
         c.add(MP3Track(mp3.title, mp3.duration, mp3.artists))
      for mp3 in other.tracks.values():
         c.add(MP3Track(mp3.title, mp3.duration, mp3.artists))
      return c

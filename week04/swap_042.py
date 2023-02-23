#!/usr/bin/env python3

def swap_keys_values(d):
   swap = {}
   for k, v in d.items():
      swap[v] = k
   return swap

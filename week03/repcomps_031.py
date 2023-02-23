#!/usr/bin/env python3

from sys import stdin

def main():
   for n in stdin:
      n = int(n) + 1
      non_multiple = [0 if n % 3 else n for n in range(1, n)]
      print(f"Non-multiples of 3 replaced: {non_multiple}")



if __name__ == "__main__":
   main()

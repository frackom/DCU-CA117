#!/usr/bin/env python3

from sys import stdin

def main():
   for n in stdin:
      n = int(n) + 1
      multiple_three = [n for n in range(1, n) if n % 3 == 0]
      print(f"Multiples of 3: {multiple_three}")
      multiple_threesqr = [n**2 for n in range(1, n) if n % 3 == 0]
      print(f"Multiples of 3 squared: {multiple_threesqr}")
      multiple_fourdbl = [n * 2 for n in range(1, n) if n % 4 == 0]
      print(f"Multiples of 4 doubled: {multiple_fourdbl}")
      multiple_threeorfour = [n for n in range(1, n) if n % 3 == 0 or n % 4 == 0]
      print(f"Multiples of 3 or 4: {multiple_threeorfour}")
      multiple_threeandfour = [n for n in range(1, n) if n % 3 == 0 and n % 4 == 0]
      print(f"Multiples of 3 and 4: {multiple_threeandfour}")




if __name__ == "__main__":
   main()

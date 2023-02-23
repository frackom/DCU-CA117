#!/usr/bin/env python3

from sys import stdin

def main():
   for n in stdin:
      n = int(n) + 1
      prime = [n for n in range(2, n) if all(n % i != 0 for i in range(2, n - 1))]
      print(f"Primes: {prime}")


if __name__ == "__main__":
   main()

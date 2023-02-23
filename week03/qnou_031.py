#!/usr/bin/env python3

from sys import stdin

def main():
   qnou = [word.rstrip() for word in stdin if "q" in word.lower().replace("qu", "")]
   print(f"Words with q but no u: {qnou}")

if __name__ == "__main__":
   main()

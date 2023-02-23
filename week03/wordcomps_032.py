#!/usr/bin/env python3

from sys import stdin

def main():
   words = [word.rstrip() for word in stdin]

   all_vowels = [word for word in words if sorted([c for c in word.lower() if c in "aeiou"]) == sorted("aeiou")]
   print(f"Shortest word containing all vowels: {(min(all_vowels, key=len))}")

   end_iary = [word for word in words if word[-4:] == "iary"]
   print(f"Words ending in iary: {len(end_iary)}")

   most_e = max([((len(word) - len(word.replace("e", "")))) for word in words])
   e_list = [word for word in words if (len(word) - len(word.replace("e", ""))) == most_e]
   print(f"Words with most e's: {e_list}")


if __name__ == "__main__":
   main()

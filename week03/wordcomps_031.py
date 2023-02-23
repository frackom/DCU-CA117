#!/usr/bin/env python3

from sys import stdin

def main():
   list = [line.rstrip() for line in stdin]

   words_17 = [word for word in list if len(word) == 17]
   print(f"Words containing 17 letters: {words_17}")

   words_18 = [word for word in list if len(word) > 17]
   print(f"Words containing 18+ letters: {words_18}")

   words_4a = [word for word in list if len([c for c in word.lower() if c == "a"]) == 4]
   print(f"Words with 4 a's: {words_4a}")

   words_2q = [word for word in list if len([c for c in word.lower() if c == "q"]) >= 2]
   print(f"Words with 2+ q's: {words_2q}")

   words_cie = [word for word in list if "cie" in word.lower()]
   print(f"Words containing cie: {words_cie}")

   words_anagram = [word for word in list if sorted("angle") == sorted(word.lower()) and "angle" != word.lower()]
   print(f"Anagrams of angle: {words_anagram}")

if __name__ == "__main__":
   main()

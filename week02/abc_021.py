#!/usr/bin/env python3

import sys

data = sys.stdin.readlines()
numbers = data[0].strip().split()
order = data[1].strip()
i = 0
while i < len(numbers):
   j = i + 1
   while j < len(numbers):
      if int(numbers[j]) < int(numbers[i]):
         tmp = numbers[i]
         numbers[i] = numbers[j]
         numbers[j] = tmp
      j += 1
   i += 1

A = numbers[0]
B = numbers[1]
C = numbers[2]

answer = []
for letter in order:
   if letter == "A":
      answer.append(A)
   elif letter == "B":
      answer.append(B)
   elif letter == "C":
      answer.append(C)

print(" ".join(answer))

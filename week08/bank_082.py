#!/usr/bin/env python3

class BankAccount:

   def __init__(self, balance=0):
      self.balance = balance

   def deposit(self, ammount):
      self.balance += ammount

   def withdraw(self, ammount):
      if 0 < self.balance and ammount <= self.balance:
         self.balance -= ammount

   def __str__(self):
      return f"Your current balance is {self.balance:.2f} euro"

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:47:36 2018

@author: george
"""
"""
   Program to determine the square root of an integer number.

   Inputs: a number, which may be negative
   Returns: the square root of the number
"""

number = int(input("Enter the number for which you want the square root: "))
approximationFactor = float(input("Enter the approximation factor: "))
correctionFactor = 1

if number < 0:
   correctionFactor = -1
   number *= -1

low = 1
high = number
mid = (low + high) / 2

squareRoot = 0
guesses = 0

squareRootFound = False

while squareRootFound == False:
   guesses += 1

   if (number - approximationFactor) <= mid**2 <= (number + approximationFactor):
      squareRoot = mid

      squareRootFound = True
   elif mid**2 < number:
      low = mid
   elif mid**2 > number:
      high = mid

   mid = (low + high) / 2

if correctionFactor == -1:
   number *= correctionFactor

   if squareRoot**2 > 0:
      print("Square root of " + str(number) + ": " + str(round(squareRoot, 3)) + "i")
   else:
      print("Square root of " + str(number) + ": " + str(round(squareRoot, 3)))
else:
   print("Square root of " + str(number) + ": " + str(round(squareRoot, 3)))

print("Guesses: " + str(guesses))





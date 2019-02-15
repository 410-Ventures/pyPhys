#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HW 1
@author: andrew
"""

#Factorial

import numpy as np

def factorial(var): #Defines factorial fn with var as the formal parameter
  var2 = 1
  while (var > 1):
    var2 = var2 * var
    var = var-1
  return var2

def main():
  num = int(input("Type a number to find its factorial: "))
  print(factorial(num))
  print(factorial(0) == 1)
  print(factorial(1) == 1)
  print(factorial(5) == 120)
  print(factorial(10) == 3628800)

main()

#Andrew Kavas
#Sum Numbers

del(main)

def sumnums(num):
  add = 0
  for i in range(1,num + 1):
    add += i
  return add

def main():
  var = int(input("Type a number to find the sum of it and all previous values"))
  print(sumnums(var))
  print(sumnums(2) == 3)
  print(sumnums(10) == 55)

main()

#Andrew Kavas
#Convert Time

del(main)

def time_convert(time):
  hours = int(time / 3600)
  minutes = int((time % 3600) / 60)
  seconds = time % 60
  s = (str(hours).rjust(2,"0") + ":" + str(minutes).rjust(2,"0") + ":" + str(seconds).rjust(2,"0"))
  return s

def main():
  var = int(input("Input time in seconds: "))
  print("Your time in h:m:s is: ", time_convert(var))
  print(time_convert(666) == '00:11:06')
  print(time_convert(999) == '02:46:06')
  print(time_convert(1500) == '00:25:00')

main()

#Andrew Kavas
#Count Vowels

del(main)

def count_vowels(kk):
  sep = list(kk)
  count = 0
  i = 0
  arr = ['a','e','i','o','u']
  while i < len(kk):
    element = sep[i]
    for jj in range(0,len(arr)):
      if element == arr[jj]:
        count += 1
    i += 1
  return (count)

def main():
  sent = str(input("Type a phrase: "))
  print ('Your phrase has ' + str(count_vowels(sent)) + ' vowels')
  print (count_vowels('hello') == 2)
  print (count_vowels('sequoia') == 5)
  print (count_vowels('hmmm') == 0)
  
main()

#Andrew Kavas
#Palindrome

del(main)

def palin(phrase):
  sep = list(phrase)
  pes = sep[::-1]
  var = bool(sep == pes)
  return (var)

def main():
  raw = str(input('Type a word or sentence'))
  print('Your phrase is a palindrome: ' + str(palin(raw)))
  print (palin("tacocat") == True)
  print (palin("hello") == False)
  
main()

#Andrew Kavas
#Power of Two

del(main)

def power_check(data):
  number = data
  while number > 1:
    number = number/2
  var = bool(number == 1)
  return (var)

def main():
  raw = int(input('Type a number to see if it is a power of 2:'))
  print(power_check(raw))
  print(power_check(1) == True)
  print(power_check(20) == False)
  print(power_check(1024) == True)
  
main()

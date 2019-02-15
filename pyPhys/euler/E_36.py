#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:58:38 2018
@author: akavas

"""

import numpy as np

print('''
-------------------------------------------------------------------------------
E-36) Double-base palindromes
-------------------------------------------------------------------------------
''')


def convert(n):
    base_2 = []
    while n >= 1:
        base_2.insert(0, 1 if n%2==1 else 0)
        n = n//2
    return base_2


def palindrome(n):
    
    n_arr = [int(i) for i in str(n)]
    
    print(n_arr)
    print(n_arr[::-1])
    
    if n_arr == n_arr[::-1]:
        return True
    else:
        return False


def arr_palindrome(n):
    n_arr = convert(n)
    
    
    if n_arr == n_arr[::-1]:
        return True
    else:
        return False


def main(n):
    if type(n) == float or int:
        arr = []
        num = 0
        for kk in range(0, n):
            if arr_palindrome(kk) and palindrome(kk) == True:
                arr.append(arr_palindrome(kk))
                num += kk
        return(num)


print(main(1000000))


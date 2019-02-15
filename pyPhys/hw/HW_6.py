#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:25:19 2018
@author: Andrew Kavas
"""

print("""
PYTHON HW 6

-------------------------------------------------------------------------------
E-36) Double-base palindromes
-------------------------------------------------------------------------------
""")


import numpy as np

def convert(n):
    base_2 = []
    while n >= 1:
        base_2.insert(0, 1 if n%2==1 else 0)
        n = n//2
    return base_2


def palindrome(n):
    
    n_arr = [int(i) for i in str(n)]
    
    #print(n_arr)
    #print(n_arr[::-1])
    
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


print(main(100))



print(
"""
------------------------------------------------------------------------------
E-39) Integer Right Triangles
------------------------------------------------------------------------------
""")


L, t_kk, p_kk = 1000, 0, 0

for p in range(0, L+1, 2):
    t = 0
    for a in range(2, int(p/3.4142) + 1):
        if  p*(p - 2*a) % (2*(p - a)) == 0: 
            t += 1
            if t >= t_kk: t_kk, p_kk = t, p
 
print('Max perim <= ', L, "is", p_kk, "at ", t_kk, ' triangles')



print(
"""
------------------------------------------------------------------------------
Newton's Method
------------------------------------------------------------------------------
""")


def f(x):
    return x**2 + x - 1

def df(x):
    return 2*x + 1

def dx(f, x):
    return abs(0-f(x))

def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print('Root: ', x0)
    print('Value: ', f(x0))


def main(n):
    ICs = [0, .5, n]
    for x0 in ICs:
        newtons_method(f, df, x0, 1e-5)

main(1)


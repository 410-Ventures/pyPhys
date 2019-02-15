#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:03:46 2018
@author: Andrew Kavas
"""


print("""
------------------------------------------------------
Andrew Kavas
2) Euler: 32
Pandigital Sum
------------------------------------------------------
""")

#this takes about 10 seconds in trinket
def pandigital(n, s=9): 
    n = str(n)
    return len(n) == s and not '1234567890'[:s].strip(n)

p = set()
for i in range(2,  60):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        if pandigital(str(i) + str(j) + str(i*j)): p.add(i*j)
    print(i,j,i*j)

print("Sum of products =", sum(p))


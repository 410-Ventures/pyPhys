#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:10:44 2018
@author: Andrew Kavas
"""

print('''
-------------------------------------------------------------------------------
E-39) Integer Right Triangles
-------------------------------------------------------------------------------
''')

P = 120


def find_sol(P):
    arr = []
    for kk in range(0, P):
        P1 = P - kk
        for jj in range(0, l-P1):
            P2 = P - jj - P1


def main(n):
    arr = []
    for kk in len(0, n+1):
        arr.append(find_sol(kk))
    
    max_sol = np.amax(arr)
    return max_sol

main(1000)


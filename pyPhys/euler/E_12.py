#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 08:21:04 2018
@author: Andrew Kavas
"""


def tri(n):
    a = 0
    for kk in range(1,n+1):
        a = a+kk
    return a


def divi(n):
    b = 100
    c = 0
    for kk in range(1,int((tri(n)+1)/2)+1):
        if tri(n) % kk != 0:
            continue
        c += 1
        
    print(c)
    if c > b:
        return True
    else:
        return False

def iter(n):
    while divi(n) == False:
        n += 1
        
    print(divi(n))

iter(20)


#def divi(n):
#    a = 0
#    while a < n+1:
#        for kk in range(1,int(n/2)+1):
#            if tri(n) % kk != 0:
#                continue
#            a = a+1
#            print(a)
#        a += 1
#        print(tri(a+1))
#        return(a)
#        
#
#
#def fn(num):
#    d = 100
#    n = 1
#    while divi(num) << d:
#        n = n+1
#    return(divi(n))
#
#
#fn(100)
#


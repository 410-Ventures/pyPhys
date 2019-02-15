#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:05:41 2018
@author: Andrew Kavas
HW 4
collaborator: S Koryakin

"""

print(
"""
-------------------------------------------------
[A] Euler 26: Reciprocal cycles
-------------------------------------------------
""")

from sympy import sieve

def f(N):
    if N < 8: 
        return 3
    for d in list(sieve.primerange(1,N))[::-1]:
        period = 1
        while pow(10, period) % d != 1: 
            period += 1
        if d-1 == period: 
            return d

N = 1000
print("Value of d <", N, "with longest recurring cycle is: ", f(N))


print(
"""
-------------------------------------------------
[B] Euler 27: Quadratic Primes
-------------------------------------------------
""")

#f(n) = n^2 + an + b 
#, where |a| < 1000 and |b| ≤ 1000 where |n| is the absolute value of n.
#Find the product of the coefficients, a and b, for the quadratic expression that produces
#the maximum number of primes for consecutive values of n, starting with n = 0.

 
def primes_xrange(stop):
    primes = [True] * stop
    primes[0], primes[1] = [False] * 2
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)
    return primes

#IMPORT YOUR PRIME FUNCTION
#SET IT TO BE A LIST OF TRUE FALSE STATEMENTS FOR ALL INTEGERS
 
P = primes_xrange(751000)

a_max, b_max, c_max = 0, 0, 0
for a in range(-1000,1001):
    for b in range(1,1001):
        if P[b] is False: continue
        if b < -1600-40*a or b < c_max: continue
        c, n = 0, 0
        while P[n**2 + a*n + b] is True:
            c += 1
            n += 1
        if c > c_max:
            a_max, b_max, c_max = a, b, c
 
prod = a_max * b_max
 
print("a= %s, b= %s, longest sequence= %s, prod= %s"\
% (a_max, b_max, c_max, prod,))


print(
"""
-------------------------------------------------
[C] Euler 28: Spiral Matrix Diagonals
-------------------------------------------------
""")


def spiral(num):
    count = 1
    kk = 3
    while kk < num+1:
        count += kk**2 + kk**2-(kk-1) + kk**2 - 2*(kk-1) + kk**2 - 3*(kk-1)
        kk += 2
    return count

print('Sum of diagonals: ', spiral(1001))


print(
"""
-------------------------------------------------
[I] Trapezoid Integration Method
-------------------------------------------------
""")
import time
import math
def Trapezoidal(func, a, b, n):
    x = (b-a)/float(n)
    y = (func(a)+func(b))/2
    for kk in range(1,n):
        y = y + func(a + kk*x)
    return x*y

def fn(x):
    return math.sin(x)
def fn2(x):
    return 1/x
def fn3(x):
    return 1/x**2
def fn4(x):
    if x == 0:
        return 0
    else:
        return 1/x**.5
def fn5(x):
    if x == 0:
        return 0
    else:
        return math.sin(x)/x
def fn6(x):
    return math.cos(x**2)

n = 10000

start = time.time()
print('integral of fn1 from ',a,' to ',b,' is ',Trapezoidal(fn, 0, math.pi, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn2 from ',a,' to ',b,' is ',Trapezoidal(fn, 0, 2*math.pi, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn3 from ',a,' to ',b,' is ',Trapezoidal(fn2, 1, 10, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn4 from ',a,' to ',b,' is ',Trapezoidal(fn3, 1, 10, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn5 from ',a,' to ',b,' is ',Trapezoidal(fn4, 0, 10, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn6 from ',a,' to ',b,' is ', abs(math.pi-Trapezoidal(fn5, -10**3, 10**3, n)))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn7 from ',a,' to ',b,' is ',Trapezoidal(fn6, 0, math.pi, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')


print(
"""
-------------------------------------------------
[II] Simpson Integration Method
-------------------------------------------------
""")
def Simpson(func,a,b,n):
    # n must be even
    if n % 2:
        raise ValueError("must have even number of steps, n (received n=%d)" % n)
    x = (b-a)/n
    y = func(a)+func(b)
    for kk in range(1, n, 2):
        y += 4 * func(a + kk*x)
    for jj in range(2, n-1, 2):
        y += 2 * func(a + jj*x)
    return(x*y/3)

n = 1000

start = time.time()
print('integral of fn1 from ',a,' to ',b,' is ',Simpson(fn, 0, math.pi, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn2 from ',a,' to ',b,' is ',Simpson(fn, 0, 2*math.pi, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn3 from ',a,' to ',b,' is ',Simpson(fn2, 1, 10, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn4 from ',a,' to ',b,' is ',Simpson(fn3, 1, 10, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn5 from ',a,' to ',b,' is ',Simpson(fn4, 0, 10, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn6 from ',a,' to ',b,' is ', abs(math.pi-Simpson(fn5, -10**3, 10**3, n)))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')

start = time.time()
print('integral of fn7 from ',a,' to ',b,' is ',Simpson(fn6, 0, math.pi, n))
end = time.time()
run = end-start
print('Took ', run, 'seconds for n = ', n ,'\n')


print(
"""
-------------------------------------------------
[III] Driven Harmonic Oscillator 2
-------------------------------------------------
""")







print(
"""
-------------------------------------------------
[IV][A] Kinder : As The Crow Flies
-------------------------------------------------
""")
class particle:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

p_1 = particle(1,2,3)
p_2 = particle(7,8,9)

def dist(P1, P2):
    """
    p_1 and p_2 coordinates must be float or int values
    Other values will not be computable
    """
    distance = float(((P1.x-P2.x)**2 + (P1.y-P2.y)**2 + (P1.z-P2.z)**2)**.5)
    return distance

print('Distance between particles = ', dist(p_1,p_2))


print(
"""
-------------------------------------------------
[IV][B] Kinder : Random Walk
-------------------------------------------------
""")
import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt

def rand_walk(steps):
    xarr = [0]
    yarr = [0]
    
    for kk in range(0,steps-1):
        a = rng()
        if a < .5:
            a = -1
            xarr.append(a)
        else:
            a = 1
            xarr.append(a)
    
    for jj in range(0,steps-1):
        b = rng()
        if b < .5:
            b = -1
            yarr.append(b)
        else:
            b = 1
            yarr.append(b)
        
    x_path = np.cumsum(xarr)
    y_path = np.cumsum(yarr)
    
    plt.plot(x_path,y_path)
    
def walk(n):
    for i in range(0,n):
        rand_walk(500)

walk(4)
plt.show()
walk(16)
plt.show()
walk(64)
plt.show()
walk(256)
plt.show()


print(
"""
-------------------------------------------------
[IV][C] Kinder : Histogram
-------------------------------------------------
""")
data = rng(500)
bins = int(len(data)/10)
counts, bin_edges, othershit = plt.hist(data)
np_counts, np_bin_edges = np.histogram(data)

print("plt.hist:\n \ncounts = ",counts,"\nbin_edges = ",bin_edges,"\n\n")
print("np.histogram:\n \ncounts = ",counts,"\nbin_edges = ",bin_edges)

plt.title(str(len(data))+" rand vals in "+str(bins)+" bins")
plt.show()


print(
"""
-------------------------------------------------
[IV][D] Kinder : 3D Surface Plot
-------------------------------------------------
""")
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

x_vals = np.linspace(-1,1,100)
y_vals = np.linspace(-1,1,100)

X, Y = np.meshgrid(x_vals,y_vals)
Z = X**2 + Y**2
plt.contour(X,Y,Z)

ax = Axes3D( plt.figure() )
ax.plot_surface(X, Y, Z)
plt.show()


print(
"""
-------------------------------------------------
[IV][E] Kinder : Quad Integral Check
-------------------------------------------------
""")
from scipy.integrate import quad

x_max = np.linspace(0, 3*np.pi, 16)
integral = np.zeros(x_max.size)
for i in range(x_max.size):
    integral[i], error = quad(np.cos, 0, x_max[i])
plt.plot(x_max, integral)
plt.show()

# Crosscheck Quad w Simpson's method
a = 0
b = math.pi 
n = 1000

#x_max = np.linspace(0, 3*np.pi, 16)
integral2 = np.zeros(x_max.size)

print("differences at each iteration: ")
for i in range(x_max.size):
    integral2[i] = Simpson(np.cos, 0, x_max[i],x_max.size)
    print(integral2[i]-integral[i])

plt.plot(x_max, integral2)
plt.show()

print("Quad and Simpson's method are visually identical and very close numerically")


print(
"""
-------------------------------------------------
[IV][F] Kinder : Unknown Integral Check
-------------------------------------------------
""")
def square(x):
    return x**2

for i in range(x_max.size):
    integral[i], error = quad(square, 0, x_max[i])    
plt.plot(x_max, integral)
plt.show()


for i in range(x_max.size):
    integral2[i] = Simpson(square, 0, x_max[i],x_max.size)
plt.plot(x_max, integral2)
plt.show()

print("differences at each iteration: ")
for i in range(x_max.size):
    print(integral2[i]-integral[i])

print("Plots are similar, differences are very small")


def newfunc(x):
    pwr = -x**2/2
    return math.exp(pwr)

x_max = np.linspace(0, 5, 50)
integral = np.zeros(x_max.size)
for i in range(x_max.size):
    integral[i], error = quad(newfunc, 0, x_max[i])
plt.plot(x_max, integral)
plt.show()

x_max = np.linspace(0, 5, 50)
integral2 = np.zeros(x_max.size)
for i in range(x_max.size):
    integral2[i] = Simpson(newfunc, 0, x_max[i],x_max.size)
plt.plot(x_max, integral2)
plt.show()

print("differences at each iteration: ")
for i in range(x_max.size):
    print(integral2[i]-integral[i])
print("Plots are similar, differences are very small")



"""
Andrew Kavas


"""

#1j = i

import numpy as np
import matplotlib as plt

def fn(t, w=.00001):
    #for i in range(0,10000):
    a = np.exp(t*w**2*1j).imag
    b = np.exp(t*w**2*1j).real
    return a

def integ(time):
    Sum = 0
    steps = int(100000)
    arr = np.zeros(steps)
    dt = float(time)/steps
    for t in range(0,steps):
        arr[t] = fn(dt*t)
    Sum += np.trapz(arr, dx=dt)
    return Sum


Sum = integ(2*np.pi)
print(Sum)

arr = np.ones(10, dtype = "complex")


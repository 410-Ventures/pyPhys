
"""
Andrew Kavas


"""

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


for i in range(0,4):
    rand_walk(500)

plt.show


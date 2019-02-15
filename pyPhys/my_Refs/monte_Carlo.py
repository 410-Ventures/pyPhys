
# Monte Carlo

import random
import numpy as np


def f(x):
    return np.cos(x)**2


# Find Limits
xmin = 0.0
xmax = 1.0 * np.pi
nsteps = 10**6
ymin = f(xmin)
ymax = f(xmax)
arr = []

for i in range(0, nsteps):
    arr.append(f(i))

ymin = min(arr)
ymax = max(arr)
total_area = (xmax - xmin) * (ymax - ymin)
print("The minimal value of the functon is {} and the max value is {}".format(ymin, ymax), '\n',
      'The area is {}'.format(total_area), '\n')


# Monte Carlo Method
npoints = 10**6


def monteCarlo(fn, n):
    npoints = n
    bin_count = 0
    for j in range(0, npoints):
        x = xmin + (xmax - xmin) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        if y < fn(x) and y > 0:
            bin_count += 1
        elif y > fn(x) and y < 0:
            bin_count -= 1
        else:
            bin_count += 0
    func_area = total_area * np.float(bin_count) / np.float(npoints)
    print("The Monte Carlo integration is {}".format(func_area))


monteCarlo(f, npoints)


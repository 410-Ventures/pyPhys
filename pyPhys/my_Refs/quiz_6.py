
# Andrew Kavas
# 4-27-18
# Monte Carlo
import random
import numpy as np


# def functions
def f1(x):
    return np.sin(x)


def f2(x):
    return np.cos(x)


def f3(x):
    return np.sin(np.cos(x))


def f4(x):
    return np.cos(np.sin(x))


# Find Limits
xmin, xmin2, xmin3, xmin4 = 0.0, 0.0, 0.0, 0.0
xmax = 1.0 * np.pi
xmax2 = 2.0 * np.pi
xmax3 = 1.0 * np.pi
xmax4 = 1.0 * np.pi

nsteps = 10**6
arr1, arr2, arr3, arr4 = [], [], [], []

for i in range(0, nsteps):
    arr1.append(f1(i))
    arr2.append(f2(i))
    arr3.append(f3(i))
    arr4.append(f4(i))

ymin = min(arr1)
ymax = max(arr1)
total_area = (xmax - xmin) * (ymax - ymin)

ymin2 = min(arr2)
ymax2 = max(arr2)
total_area2 = (xmax2 - xmin2) * (ymax2 - ymin2)

ymin3 = min(arr3)
ymax3 = max(arr3)
total_area3 = (xmax3 - xmin3) * (ymax3 - ymin3)

ymin4 = min(arr4)
ymax4 = max(arr4)
total_area4 = (xmax4 - xmin4) * (ymax4 - ymin4)

# Monte Carlo Method
npoints = 10**6


def monteCarlo(fn, n, xmin, xmax, ymin, ymax, total_area):
    total_area = total_area
    xmin, xmax = xmin, xmax
    ymin, ymax = ymin, ymax
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
    print("Integration: {}".format(func_area))


monteCarlo(f1, npoints, xmin, xmax, ymin, ymax, total_area)
monteCarlo(f2, npoints, xmin2, xmax2, ymin2, ymax2, total_area2)
monteCarlo(f3, npoints, xmin3, xmax3, ymin3, ymax3, total_area3)
monteCarlo(f4, npoints, xmin4, xmax4, ymin4, ymax4, total_area4)


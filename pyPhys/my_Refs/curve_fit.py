#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:40:38 2018
@author: Andrew Kavas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):

    return a * np.exp(-b * x) + c

def main_static():

    xlim = 10

    xsteps = 10**3

    xdata = np.linspace(0, xlim, xsteps + 1)

    y = func(xdata, 2.5, 1, 0.5)

    np.random.seed(1729)

    noise = 1/10*np.random.normal(size = np.shape(xdata)[0])

    ydata = y + noise

    plt.plot(xdata, ydata, label = "curve")

    #plt.show()

    popt, pcov = curve_fit(func, xdata, ydata)

    print("Optimal values for the parameters is", popt)

    print("The estimated covariance of popt is", pcov)

    plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f'%tuple(popt))

    plt.xlabel('xdata')

    plt.xlabel('ydata')

    plt.legend()

    plt.show()

main_static()


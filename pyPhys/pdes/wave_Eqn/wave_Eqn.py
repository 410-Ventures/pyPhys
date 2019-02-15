#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:52:17 2018
@author: Andrew Kavas
"""


import numpy as np
import matplotlib.pyplot as plt
# from scipy import optimize
# from scipy.optimize import Brentq

# finite difference wiki

nx = 1000
nt = 1000

fx = 10
ft = 10

dx = fx/nx
dt = ft/nt

V0 = np.inf
L = 1
space = np.linspace(0, fx, nx+1)


def V(n):
    if (n>=-L and n <=L):
        return 0
    else:
        return V0


# x_arr = np.zeros((nx, nt))


def schrodinger(nx, fx, E):
    # Eqns
    psi = np.linspace(0, fx, nx+1)
    d_psi = np.zeros(nx+1)
    
    # ICs
    psi[0] = 1
    d_psi[0] = 0
    
    for kk in range(0, nx):
        d_psi[kk+1] = d_psi[kk] -2*(E - V(kk*dx))*psi[kk]*dx
        psi[kk+1] = psi[kk] + d_psi[kk]*dx
    
    return psi


def E_solv():
    E_max = 100
    E_arr = []
    for kk in range(0, E_max):
        E_arr.append(kk)
    
    Engs = []
    for kk in range(0, len(E_arr)):
        Engs.append(schrodinger(nx, fx, E_arr[kk])[kk])
    
    plt.plot(E_arr, Engs)
    plt.show()


E_solv()


def main():
    
    # fig = plt.figure()
    plt.plot(space, schrodinger(nx,fx, E))
    # plt.plot(-1*space, schrodinger(nx,fx))
    plt.show()


# main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:56:27 2018
@author: Andrew Kavas
"""


print('''
------------------------------------------------------------------
TIME EVOLUTION OF THE WAVE EQUATION
------------------------------------------------------------------
''')


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.integrate import odeint


# Constants
steps = 10**4
#Vmax  = 8
initial_arr = [1,0]
L = 1
E = 0.0
xlim = 6

#x = np.linspace(-xlim, xlim, steps)

def space(a, b, c):
    c = steps
    return np.linspace(a, b, c)

# Params in form [-xlim = , xlim=, stepsm, m = , w = , Vmax = ]
Params = [[-6, 6, steps, 1, 1, 8],[-6, 6, steps, 1, 1, 15],[-2, 2, steps, 1, 1, 12],
          [-2.6, 2.6, steps, 1 ,1, 9],[-6, 6, steps, 1, 1, 3],[0, 10, steps, 1, 1, 10]]

# Define potentials

# Harmonic
def V0(x):
    m = Params[0][3]
    w = Params[0][4]
    V = (x**2 * m * w**2)/2
    return V

# Half-Harmonic Pot
def V1(x):
    if x < 0:
        V = 20
        return V
    else:
        m = Params[1][3]
        w = Params[1][4]
        V = (x**2 * m * w**2)/2 
        return V

# Square Pot
def V2(x):
    if abs(x) >= L:
       V = 10
       return V
    else:
        V = 0
        return V

# Double Well Pot
def V3(x):
    a = 3
    V0 = 1
    V = V0 * (x**2 - a)**2
    return V

# Linear Potential Pot
def V4(x):
    V = abs(x)
    return V

# Morse Potential Pot
def V5(x):
    V0, r0 = 10, 1
    V = V0*(1-np.exp(-(x-r0)))**2
    return V

# Create array of potential functions
V_arr = [V0, V1, V2, V3, V4, V5]


# Plot each function
for fn in V_arr:
    
    ind = V_arr.index(fn)
    x = space(Params[ind][0],Params[ind][1],Params[ind][2])
    
    # Pair derivatives with locations
    def schrodinger(psi, x):
        g0, g1 = psi
        derivs = [g1, -2*(E - fn(x))*g0]
        return np.array(derivs)
    
    # Solve ODE at each location
    def wave_function(energy):
        global E
        global psi
        E = energy
        # Use ODEint to solve ODE at current location
        psi = odeint(schrodinger, initial_arr, x)
        return psi[-1,0]
    
    # Find zero crossings of Psi(x)
    def zeroes_find(x, y):
        arr_zeros = []
        s = np.sign(y)
        for i in range(0, len(y) - 1):
            if (s[i]+s[i+1] == 0):
                # Brentq finds root of fn
                zero = brentq(wave_function, x[i], x[i+1])
                arr_zeros.append(zero)
        return arr_zeros
    
    def main_static():
            
        Vmax = Params[ind][5]
        ensteps = 10**3
        en = np.linspace(0, Vmax, ensteps)
        psi_end = []
        
        for kk in range(0, len(en)):
            psi_end.append(wave_function(en[kk]))
        E_zeroes = zeroes_find(en, psi_end)
        
        plt.figure()
        plt.plot(en/Vmax, psi_end)
        plt.xlabel('Energy', fontsize = 15)
        plt.ylabel('$\Psi(x = x[lim])$', fontsize = 15)
        
        for E in E_zeroes:
            plt.plot(E/Vmax, [0], 'go')
        plt.grid()
        plt.show()
        
        Varr = []
        for kk in range(0, steps):
            Varr.append(fn(x[kk]))
        plt.figure(2)
    
        for kk in range(0, len(E_zeroes)):
            wave_function(E_zeroes[kk])
            area = np.trapz(psi[:,0]*psi[:,0], dx = 2*xlim /steps)
            
            plt.plot(x, 2.5*kk + psi[:,0]/np.sqrt(area), label="E = %.05f"%E_zeroes[kk])
            plt.plot(x, Varr, color = "b")
            
        plt.legend(loc="upper right")
        plt.xlabel('x', fontsize = 15)
        plt.ylabel('$\Psi(x)$', fontsize = 15)
        plt.grid()
        plt.show()
    
    main_static()
    

    
    
    

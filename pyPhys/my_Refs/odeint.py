#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:57:08 2018
@author: Andrew Kavas
"""

import matplotlib.pyplot as plt

#  theta__prime_prime(t) + b*theta_prime(t) + c*sin(theta(t)) = 0

theta_prime(t) = omega(t)
omega_prime(t) = -b*omega(t) - c*sin(theta(t))

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
c = 5.0


y0 = [np.pi - 0.1, 0.0]


t = np.linspace(0, 10, 101)



from scipy.integrate import odeint
sol = odeint(pend, y0, t, args=(b, c))


plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
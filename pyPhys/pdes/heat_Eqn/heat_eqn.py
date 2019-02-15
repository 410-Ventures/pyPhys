#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:00:59 2018
@author: Andrew Kavas
"""

# Heat Equation
# du/dt = a d^2u/dt^2


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


nt = 10000
nx = 10

u = np.zeros((nt+1, nx+1))
u[:, 0] = u[:, -1] = 0

x_fin = 10
t_fin = 200
dx = x_fin/nx
dt = t_fin/nt

alpha = .127  # per meter

xarr = np.linspace(0, x_fin, nx+1)

# u(t=0) = x(-x)
for kk in range(0, nx+1):
    u[0, kk] = dx*kk*(1-dt*kk)

for n in range(0, nt):
    for m in range(1, nx):
        u[n+1, m] = (alpha*dt/dx**2)*(u[n, m+1] - 2*u[n, m] + u[n, m-1]) + u[n, m]

# u[n+1,m]-u[n,m] = alpha*dt/dx**2

fig, ax = plt.subplots()

# x = np.arange(0, 4*np.pi, 0.001)
# y = np.arange(0,4*np.pi,0.001)
# plt.plot(t,x,t,y)
# plt.show()

line, = ax.plot([], [], 'o-')


def animate(i):
    # print(len(xarr),len(u[i]))
    line.set_data(xarr,u[i])
    # line.set_ydata(np.cos(2*x + i/5.0))

    return line,


def init():
    line.set_data([],[])
    # line.set_xdata(np.ma.array(x, mask=True))
    # line.set_ydata(np.ma.array(x, mask=True))

    return line,


ani = animation.FuncAnimation(fig, animate, init_func=init, interval=1, blit=True)

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.show()


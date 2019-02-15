
"""
Andrew Kavas
N Mass Oscillator

"""

import numpy as np
# imports for plotting
from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from matplotlib.font_manager import FontProperties
# import ODEINT (ordinary differential equation integrator) to solve equations of motion
from scipy.integrate import odeint
# ODE solver parameters
abserr = 1.0e-9
relerr = 1.0e-6
stoptime = 10
numpoints = 250

def EqsOfMotion(w, t, p):
    """
    Defines the differential equations for the coupled spring-mass system.
    State vector = w = [x1,v1,x2,v2,x3,v3]
    Time = t
    vector of the parameters = p = [m1,m2,m3,k1,k2,k3]
    """
    N = int(len(w)/2)
    xarray = []
    varray = []
    for i in range(N):
        xarray.append(w[2*i])
        varray.append(w[2*i+1])
    m,k = p
    # Create f = (x1',v1',x2',v2',x3',v3',...,xn',vn') = (v1,a1,v2,a2,v3,a3...,vn,an)
    f = [varray[0],( -k*xarray[0] + k*(xarray[1] - xarray[0]) )/m]
    for i in range(1,N-1):
        f.extend([varray[i],( -k*xarray[i] + k*(xarray[i+1] - xarray[i]) )/m])
    f.extend([varray[N-1],( -k*(xarray[N-1] - xarray[N-2]) )/m])
    return f



# Initial conditions
N = int(input("Number of masses: "))
for i in range(N):
    print("PARTICLE #",i+1)
    locals()['x{0}'.format(i+1)] = int(input("initial displacement: "))
    locals()['v{0}'.format(i+1)] = int(input("initial velocity: "))
#x1,x2,x3,x4 = 1,0.0,1,0.0
#v1,v2,v3,v4 = 0.0,0.0,0.0,0.0


# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
m = 1
k = 1.5
p = [m,k]
w0 = []
for i in range(N):
    w0.append(locals()['x{0}'.format(i+1)])
    w0.append(locals()['v{0}'.format(i+1)])

# Call the ODE solver.
wsol = odeint(EqsOfMotion, w0, t, args=(p,),
              atol=abserr, rtol=relerr)

with open('two_springs.dat', 'w') as f:
    # Print & save the solution.
    for t1, w1 in zip(t, wsol):
        dat = [t1]
        dat.extend(w1)
        print(dat, file=f)

dat = np.array([])
with open('two_springs.dat', 'r') as f:
    for line in f:
        line = line[1:-2]
        
        split_line = line.split(', ')
        vals = []
        for value in split_line:
            val = float(value)
            vals.append(val)
            print(vals)
        dat = np.append(dat,vals)
dat = np.reshape(dat,(numpoints,2*N+1))
#dat = np.array(list(zip(t,dat)))
N = int(len(dat[0])/2)
for i in range(N):
    locals()['x{0}'.format(i)] = dat[:,2*i+1]
    locals()['v{0}'.format(i)] = dat[:,2*i+2]


figure(1, figsize=(6, 4.5))

xlabel('t')
grid(True)
hold(True)
lw = 1

for i in range(N):
    plot(t, locals()['x{0}'.format(i)], linewidth=lw)

#legend((r'$x_1$', r'$x_2$', r'$x_3$',r'$x_4$'), prop=FontProperties(size=16))
title('Mass Displacements for the\nCoupled Spring-Mass System')
savefig('two_springs.png', dpi=100)


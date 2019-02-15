
"""
Andrew Kavas
3 Mass 4 Spring- Oscillator

"""

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
    x1,v1,x2,v2,x3,v3 = w
    m1, m2, m3, k, k, k = p

    # Create f = (x1',v1',x2',v2',x3',v3') = (v1,a1,v2,a2,v3,a3)
    f = [v1,
         (-k*x1 + k*(x2 - x1) )/m1,
         v2,
         (-k*(x2 - x1) + k*(x3 - x2) )/m2,
         v3,
         (-k*(x3 - x2) - k*x3 )/m3]
    return f


# Parameters
# Masses:
m1,m2,m3 = 1,1,1
# Spring constants
k = 1.2
k1, k2, k3 = k,k,k

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1,x2,x3 = 0,1,1
v1,v2,v3 = 0.0,0.0,0.0



# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
p = [m1,m2,m3,k1,k2,k3]
w0 = [x1,v1,x2,v2,x3,v3]

# Call the ODE solver.
wsol = odeint(EqsOfMotion, w0, t, args=(p,),
              atol=abserr, rtol=relerr)

with open('two_springs.dat', 'w') as f:
    # Print & save the solution.
    for t1, w1 in zip(t, wsol):
        print(t1, w1[0], w1[1], w1[2], w1[3], w1[4], w1[5], file=f)



t, x1, v1, x2, v2, x3, v3 = loadtxt('two_springs.dat', unpack=True)

figure(1, figsize=(6, 4.5))

xlabel('t')
grid(True)
hold(True)
lw = 1

plot(t, x1, 'b', linewidth=lw)
plot(t, x2, 'g', linewidth=lw)
plot(t, x3, 'orange', linewidth=lw)

legend((r'$x_1$', r'$x_2$', r'$x_3$'), prop=FontProperties(size=16))
title('Mass Displacements for the\nCoupled Spring-Mass System')
savefig('two_springs.png', dpi=100)


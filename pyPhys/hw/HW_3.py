
"""
Andrew Kavas
HW_3

"""


"""
Andrew Kavas
Power Digit Sum

"""

def int_sum(var):
    sep = [int(i) for i in str(var)]
    #print(sep)
    sumnum = 0
    for kk in range(0,len(sep)):
        sumnum += sep[kk]
    print(sumnum)

int_sum(2**1000)

print('//')

"""
Andrew Kavas
Factorial Int Sum

"""

def factorial(num):
    nxt = num - 1
    fact = num
    while nxt > 1:
        fact = fact*nxt
        nxt += -1
    return(fact)


def int_sum(var):
    sep = [int(i) for i in str(var)]
    #print(sep)
    sumnum = 0
    for kk in range(0,len(sep)):
        sumnum += sep[kk]
    print(sumnum)


int_sum(factorial(100))

print('//')

"""
Andrew Kavas
1000 Digit Fibonacci Number

"""

def fib_len(num):
    a,b = 1,0
    for kk in range(1,num**2):
        b = a + b
        a = b - a
        #print(kk,b)
        sep = [int(i) for i in str(b)]
        if len(sep) >= num:
            break
    #print(b)
    return(kk)


print(fib_len(1000))

print('//')

"""
Andrew Kavas
Largest Product in a Grid
E_11

** Needs matrix file from Euler saved as E_11_matrix.txt **

"""

import numpy as np

arr = []
varr = []
rarr = np.zeros((20,20))

with open('E_11_matrix.txt', 'r') as f:
    for line in f:
        arr.append(line)
        split_line = line.split(' ')
        #varr.append(split_line)
        for values in split_line:
                value_as_int = int(values)
                varr.append(value_as_int)

for kk in range(0,20):
    rarr[kk] = varr[kk*20:(kk+1)*20]


#print(arr)
#print(varr)
#print(rarr)
#print(rarr[1,0])

prods = []

def sweep(num):
    for jj in range(0,20):
        for kk in range(0,17):
            prod = rarr[jj,kk]*rarr[jj,kk+1]*rarr[jj,kk+2]*rarr[jj,kk+3]
            prods.append(prod)
#            #print(prod)
    for jj in range(0,20):
        for kk in range(0,17):
            prod = rarr[kk,jj]*rarr[kk+1,jj]*rarr[kk+2,jj]*rarr[kk+3,jj]
            prods.append(prod)
#            #print(prod)
    for jj in range(0,17):
        for kk in range(0,17):
            prod = rarr[kk,jj]*rarr[kk+1,jj+1]*rarr[kk+2,jj+2]*rarr[kk+3,jj+3]
            prods.append(prod)
#            #print(prod)
    for jj in range(0,17):
        for kk in range(0,17):
            prod = rarr[kk+3,jj]*rarr[kk+2,jj+1]*rarr[kk+1,jj+2]*rarr[kk,jj+3]
            prods.append(prod)
            #print(prods)
#    print(prods)
    print('//')
    print(max(prods))

sweep(4)
            

#print(prods)
#print(len(prods))


"""
Andrew Kavas
3 Mass 4 Spring- Oscillator

"""

# imports for plotting

import matplotlib.pyplot as plt
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
savefig('3_mass.png', dpi=100)

plt.show()


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
    #print("PARTICLE #",i+1)
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
            #print(vals)
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
savefig('n_mass.png', dpi=100)

plt.show()

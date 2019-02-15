
"""
Andrew Kavas
Animated Pendulum

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


g=9.81
L=10
steps = 10000
finaltime = 10
dt = finaltime/steps
def pendulum(steps,finaltime):
    dt=finaltime/steps
    omega=np.zeros(steps+1)
    theta=np.zeros(steps+1)
    theta[0]=.5*np.pi
    time=np.linspace(0,finaltime,steps+1)

    for nn in range(1,steps):
        omega[nn]=-g/L*np.sin(theta[nn-1])*dt+omega[nn-1]
        theta[nn]=omega[nn-1]*dt+theta[nn-1]

    return (theta,omega,time)

fig, ax = plt.subplots()


theta,omega,t=pendulum(1000,10)
x=-L*np.cos(theta)
y=L*np.sin(theta)
#print(x,t)
#x = np.arange(0, 4*np.pi, 0.001)
#y = np.arange(0,4*np.pi,0.001)

#plt.plot(t,x,t,y)
#plt.show()
line, = ax.plot([],[],'o-')

time_template='time = %1fs'
time_text=ax.text(0.05,0.9,'',transform=ax.transAxes)
#line2, = ax.plot(x, np.cos(x))

def animate(i):
    thisx=[0,x[i]]
    thisy=[0,y[i]]
    line.set_data(thisy,thisx)

    time_text.set_text(time_template%(i*dt))
  #line.set_ydata(np.cos(2*x + i/5.0))
    return line, time_text

def init():
    line.set_data([],[])

  #line.set_xdata(np.ma.array(x, mask=True))
  #line.set_ydata(np.ma.array(x, mask=True))


    time_text.set_text('')
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1,len(y)), init_func=init, interval=1, blit=True)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
#plt.axes().set_aspect('equal')
plt.show()


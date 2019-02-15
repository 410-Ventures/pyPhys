
"""
Andrew Kavas
Sin Animate

"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 4*np.pi, 0.001)
line, = ax.plot(x, np.sin(x))
#line2, = ax.plot(x, np.cos(x))

def animate(i):
  line.set_xdata(np.sin(x + i/5.0))
  line.set_ydata(np.cos(2*x + i/5.0))
  return line,

def init():
  line.set_xdata(np.ma.array(x, mask=True))
  line.set_ydata(np.ma.array(x, mask=True))
  return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1,200), init_func=init, interval=25, blit=True)

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()

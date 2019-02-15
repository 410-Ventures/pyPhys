
"""
Andrew Kavas


"""

import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

x_vals = np.linspace(-1,1,100)
y_vals = np.linspace(-1,1,100)

X, Y = np.meshgrid(x_vals,y_vals)
Z = X**2 + Y**2
plt.contour(X,Y,Z)

ax = Axes3D( plt.figure() )
ax.plot_surface(X, Y, Z)



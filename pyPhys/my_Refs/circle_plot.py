
"""
Andrew Kavas
Circle Plot

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, -1.0, 100)
y = np.linspace(1.0, -1.0, 100)

X, Y = np.meshgrid(x,y)
F = X**2 + Y**2 - .6

plt.contour(X,Y,F,[0])
plt.show()

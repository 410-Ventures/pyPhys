
"""
Andrew Kavas


"""

import scipy.integrate as si
import matplotlib.pyplot as plt
from scipy.integrate import quad

x_max = np.linspace(0, 3*np.pi, 1000)
integral = np.zeros(x_max.size)

for i in range(x_max.size):
    integral[i], error = quad(np.cos, 0, x_max[i])

plt.plot(x_max, integral)


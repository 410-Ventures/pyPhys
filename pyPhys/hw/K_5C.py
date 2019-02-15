
"""
Andrew Kavas


"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng

data = rng(100)
plt.hist(data)
count, bin_edges, _ = plt.hist(data)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:03:18 2018
@author: Andrew Kavas
Animation of Two Coupled Pendula

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

steps = 10
finaltime = 10

x = np.linspace(0,finaltime)
y1 = x
y2 = x**2
y3 = x**.5
y4 = np.sin(x)



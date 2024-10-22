# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:05:29 2024

@author: joahb
"""

import matplotlib.pyplot as plt
import numpy as np

# Define given constants
A = 10
a = 2
k = 0.4 

x = np.arange(0, 20, 0.1)



E = A* np.cos((np.pi*x)/a)*np.exp(-k*x)



# Plot both transfer functions on the same graph
plt.figure('Electric field vs position')
plt.plot(x, E, "b")

plt.xlabel("position (m)", size=16)
plt.ylabel(" Electric field", size=16)
plt.grid(True)
plt.legend()
plt.xlim(min(x), max(x))
plt.ylim(-5, 5)  # Adjust y-limits for visibility

plt.show()


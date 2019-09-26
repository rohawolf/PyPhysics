"""
ref: https://computation.physics.utoronto.ca/tutorials/tutorial-part-1-first-steps-python-3/
"""

import numpy as np
import matplotlib.pyplot as plt


#example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

flg, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
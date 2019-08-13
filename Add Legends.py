import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig=plt.figure()
"""
x=np.linspace(0,5,11)
y=x**2
"""

x=np.arange(1,12)

ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')

ax.legend(loc=0)

plt.show()

plt.tight_layout()

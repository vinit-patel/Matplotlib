import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.linspace(0,5,11)
y=x**2


fig,axes=plt.subplots(1,2)

axes[0].plot(x**2,'r')
axes[0].set_xlabel('X0 Label')
axes[0].set_ylabel('Y0 Label')


axes[1].plot(x**3)
axes[1].set_xlabel('X1 Label')
axes[1].set_ylabel('Y1 Label')


plt.show()


plt.tight_layout()

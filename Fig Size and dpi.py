import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig,axes=plt.subplots(2,1,figsize=(3,2))


x=np.linspace(0,5,11)
y=x**2

#axes[0]=fig.add_axes([0.05,0.2,0.4,0.4])
axes[0].plot(x,y)
axes[0].set_xlabel('X1 Label')
axes[0].set_ylabel('Y1 Label')
axes[0].set_title('AX0 Title')


#axes[1]=fig.add_axes([0.55,0.2,0.4,0.4])
axes[1].plot(y,x,'r')
axes[1].set_xlabel('X2 Label')
axes[1].set_ylabel('Y2 Label')
axes[1].set_title('AX1 Title')


plt.show()

plt.tight_layout()

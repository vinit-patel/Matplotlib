import numpy as np
import matplotlib.pyplot as plt


np.random.seed(100)
x=np.arange(0,100)
y=x*2
z=x**2

fig,axes=plt.subplots(1,2,figsize=(6,1))

axes[0].plot()
axes[0].set_xbound(0,1)
axes[0].set_ybound(0,1)
axes[0].set_title('Axis 0')

axes[1].plot()
axes[1].set_xbound(0,1)
axes[1].set_ybound(0,1)


axes[0].plot(x,y,color='blue',lw=2,ls='--')
axes[0].set_xbound(0,100)
axes[0].set_ybound(0,200)

axes[1].plot(x,z,color='red',lw=2,ls='-')
axes[1].set_xbound(0)
axes[1].set_ybound(0,10000)


plt.show()
plt.tight_layout(pad=1)

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,100)
y=x*2
z=x**2

fig=plt.figure()

ax1=fig.add_axes([0.1,0.1,0.8,0.6])
ax2=fig.add_axes([0.2,0.5,0.2,0.2])

ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_xbound(0)
ax1.set_ybound(0)


ax2.plot(x,y,'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xbound(0)
ax2.set_ybound(0)

#ax1.plot()

fig.show()

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(100)
x=np.arange(0,100)
y=x*2
z=x**2

fig,axes=plt.subplots(1,2)

axes[0].plot()
axes[0].set_xbound(0,1)
axes[0].set_ybound(0,1)

axes[1].plot()
axes[1].set_xbound(0,1)
axes[1].set_ybound(0,1)



'''
ax1.plot(x,z,'b')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_xbound(0)


ax2.plot(x,y,'b')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('zoom')
ax2.set_xbound(20,22)
ax2.set_ybound(30,50)
'''

plt.show()
plt.tight_layout(pad=1)

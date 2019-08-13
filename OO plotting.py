import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.linspace(0,5,11)
y=x**2
print(x)
print(y)

fig=plt.figure()

axes1=fig.add_axes([0.05,0.1,0.4,0.4])
axes2=fig.add_axes([0.55,0.1,0.4,0.4])



axes1.plot(y,x,'r')
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Larger Plot')


axes2.plot(x,y,'b')
axes2.set_xlabel('X Label')
axes2.set_ylabel('Y Label')
axes2.set_title('Smaller Plot')

plt.show()


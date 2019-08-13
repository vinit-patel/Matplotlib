import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)
line=list(np.random.randint(42,89,12))
bar=list(np.random.randint(33,98,12))
x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

print(line)
print(bar)

fig,axes=plt.subplots()

axes.plot(x,line,color='blue',label='Revenue',lw=1,ls='--',marker='o')
axes.bar(x,bar,color='green',label='Quantity Sold',alpha=0.6)



axes.legend(loc=0)
plt.show()

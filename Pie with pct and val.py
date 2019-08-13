import matplotlib.pyplot as plt



data=[67, 44, 22, 82]
data2=data[:]
labels=['Apples','Oranges','Grapes','Pine Apples']


def pct(val):
    while data2:
        i=data2.pop(0)
        per=(i/sum(data))*100
        return "{}%\n({})".format(round(per,2),i)



fig,axes=plt.subplots()
axes.pie(data,labels=labels,autopct=lambda itr:pct(data2))


axes.legend(loc=(0.95,0.9))

plt.show()

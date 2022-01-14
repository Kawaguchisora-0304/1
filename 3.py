import numpy as np
import matplotlib.pyplot as plt
 
annotations=["2014","2015","2016","2017","2018","2019"]

x = [1452, 1796, 1894, 2584, 2735, 3447]
y = [3231, 3747, 3726, 5853, 8866, 10913]

fig = plt.figure()
 
ax = fig.add_subplot(1, 1, 1)
 
ax.scatter(x, y, c='b')

plt.xlabel("オープンキャンパス参加者数(人)" ,fontname="Yu Gothic")
plt.ylabel("志願者数（人）",fontname="Yu Gothic") 

for i, label in enumerate(annotations):
    plt.text(x[i], y[i],label)

plt.legend(["年度"], prop={"family":"MS Gothic"})

plt.show()
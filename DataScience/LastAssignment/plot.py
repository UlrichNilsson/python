import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data2013 = pd.read_excel("2013 - Election results all districts.xls", skiprows=90)
data2017 = pd.read_excel("2017 - Election results all districts.xls", skiprows=138)

data2013=data2013[1:17]
data2013=data2013.drop(data2013.columns[[1, 2,3,4,6,7,8,9,11,12,14,15,16,17,18,19]], axis=1)
data2013=data2013.dropna()

data2017=data2017[1:17]
data2017=data2017.drop(data2017.columns[[1, 2,3,4,6,7,8,9,11,12,14,15,16,17,18,19]], axis=1)
data2017=data2017.dropna()
#print(data2017)
#print(data2013)

# data to plot
n_groups = 11
Percentage_2017 = data2017['Procent']
Percentage_2013 = data2013['Procent']
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, Percentage_2017, bar_width,
                 alpha=opacity,
                 color='b',
                 label='2017')
 
rects2 = plt.bar(index + bar_width, Percentage_2013, bar_width,
                 alpha=opacity,
                 color='g',
                 label='2013')
 
plt.xlabel('Nominated group')
plt.ylabel('Percentage')
plt.title('Compare church meeting election for Strängnäs stift(dioces)')
plt.xticks(index + bar_width/2, data2017['Nomineringsgrupp'])
plt.legend()
 
plt.tight_layout()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

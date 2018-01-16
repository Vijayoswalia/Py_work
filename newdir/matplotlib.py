# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:53:57 2017

@author: Vijay
"""

import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()

plt.scatter(year,pop)
plt.show

values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, 4)
plt.hist(values, 12)
plt.hist(values, 6)


year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.xlabel('year')
plt.ylabel('population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10], ['0','2B','4B','6B','8B','10B'])
plt.plot(year, pop)
plt.show()


year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.xlabel('year')
plt.ylabel('population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10], ['0','2B','4B','6B','8B','10B'])
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop
plt.plot(year, pop)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0. , 5. , 0.2)
plt.plot(t, t, 'r--',t, t**2, 'bs', t, t**3, 'g^')
plt.axis([0,6,0,150])  # x and y range of axis
plt.show()

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0. , 5. , 0.2)
plt.scatter(t, t, 'r--',t, t**2, 'bs', t, t**3, 'g^')
plt.axis([0,6,0,150])  # x and y range of axis
plt.show()


import numpy as np
import matplotlib.pyplot as plt
mu, sigma = 100, 15
x = mu+sigma*np.random.randn(10000)
#histogram
plt.xlabel('smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .25, r'$\mu=100,\\sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.hist(x, 50, facecolor='g')



data1 = [49., 66, 24, 98,37,64,98,27,56,93,68,78,22,25,11]
def mean(data1):
    n=len(data1)
    mean=sum(data1)/n
    return mean
print(mean(data1))


data2 = [1,2,5,10,-20,5]
def median(data2):
    D=sorted(data2)
    median=[(len(D)/2)]
    return median
print(median(data2))


data2 = [1.,2,5,10,-20,5]
median = np.median(data2)
print(median)


def median(data2):   
    l1=sorted(data2)
    x=len(l1)
    if (x%2==0):
        median = (l1[int(x/2)] + l1[int(x/2 - 1)])/2
    else:
        median= l1[int((x-1)/2)]
    return median
print(median(data2))

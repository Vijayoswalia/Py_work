# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:54:26 2018

@author: Vijay
"""
import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3]
y = [2,4,1]

plt.plot(x,y)

x1 = [1,2,3]
y1 = [4,2,1]
x2 = [1,2,3]
y2 = [4,1,3]
plt.plot(x1,y1, label='line1')
plt.plot(x2,y2, label='line2')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('two lines on the same plot')
plt.show()
tcik_label = 
plt.bar(x1,y1,tick_label = tick_label, width=0.8, color=['red','green'])




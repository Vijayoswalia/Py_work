# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 12:21:10 2017

@author: Vijay
"""
### 1-D Array
import numpy as np
a = np.array([1,3,5,7,9])
b = np.array([3,5,6,7,9])
c = a+b
print (c)
type(c)

a.dtype
a.itemsize
a.shape
np.shape(c)
a.size
np.size(a)

a.ndim

d=a.copy()
d

d.fill(0)
d

d[:]=1
d

### 2D Array

np_2d=np.array([[1.73,1.68, 1.89, 1.79],
               [65.4, 59.2, 63.6, 88.4, 68.7]])
np_2d
np_2d[0]
np_2d[0][2]
np_2d[0,2]
np_2d[:][1:3]

np_mat=np.array([[1,2],
                 [3,4],
                 [5,6]])
np_mat
np_mat*2
np_mat + np.array([10,10])
np_mat+np_mat
np.shape(np_mat)
np_mat[2]
np_mat[:][1]
np.append(np_mat)=np.array([12,12])  ###not working

from numpy import array

a=array([[1,2,3],
         [4,5,6]], float)

sum(a)

np.sum(a, axis=0)
np.sum(a, axis=-1)

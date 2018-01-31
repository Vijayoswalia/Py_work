# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:25:02 2018 by vijayoswalia for DS
"""

import numpy
numpy.__version__

import numpy as np
np.abs


import array
L = list(range(10))
A = array.array('i',L)
A

np.array([1,4,2,5,3])
np.array([1,2,3,4], dtype='float32')

np.zeros(10, dtype=int)
np.ones((3,5), dtype=float)
np.full((3,5), 3.14)

np.random.seed(0)
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))

print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size:", x3.size)

x2
x2[0,0]
x2[2,1]


x1[0]=3.14159
x1

x = np.arange(10)
x
x[:5]
x[5:]
x[4:7]
x[::2]
x[1::2]

x[::-1]
x[5::-2]
x2
x2[:2,:3]
x2[:3,::2]
x2[::-1,::-1]
print(x2[:,0])
print(x2[0,:])
print(x2[0])
x2
x2_sub = x2[:2,:2]
print(x2_sub)

x2_sub[0,0]=99
print(x2_sub)

print(x2)

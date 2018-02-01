# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:26:26 2018

@author: Vijay
"""
import numpy as np
import pandas as pd
import math

a = np.array([[0,1,2,3], [10,11,12,13]])
a
a.shape
shape(a)
a.size
np.size(a)
a.ndim

a = np.array([[1,2,3],[4,5,6]], float)
a
print (a)
print (a.shape, '\n', a.itemsize)
print(a.dtype, a.dtype.type)
type(a[0,0]) is type(a[1,2])
b = a[:,::2]
b[0,1] = 100
print(a)
a = np.arange(0,80,10)
a
print(a)
y=np.take(a,[1,2,-3])
y
y=a[[1,2,-3]]
y
mask = np.array([0,1,1,0,0,1,0,0], dtype=bool)
y = a[mask]
y
y=np.compress(mask, a)
y

a = np.array(np.arange(36).reshape(6,6))
a = np.arange(36).reshape(6,6)

a
a[(0,1,2,3,4),(1,2,3,4,5)]
a[3:,[0,2,5]]

mask = np.array([1,0,1,0,0,1],dtype=bool)
a[mask,2]

a = np.array([[1,2,3],[4,5,6]],float)
sum(a) '''by default axis is 0'''
a.sum()
a.sum(axis=0)  '''by default axis is 0'''
a.sum(axis=-1)
a=np.array([2.,3.,0.,1.])
a.min(axis=0)
np.amin(a, axis=0)
a.argmin(axis=0)
a.max(axis=0)
np.amax(a,axis=0)
a.argmax(axis=0)
np.argmax(a, axis=0)

a = np.array([[1,2,3],[4,5,6]], float)
a.clip(3,5)
a = np.array([1.35,2.5,1.5])
a.round()


a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a+b
x=np.arange(11.)
a=(2*3.14)/10
a
a*x


s = pd.Series([3,7,4,4,0.3], ['a','b','c','d','e'])
df = pd.DataFrame(np.arange(9).reshape(3,3),['b','a','c'],['Paris','Berlin','Madrid'])
data=['Paris':[0,3,6,999999999],'Berlin':[1,4,7],'Madrid':[2,5,8]]
df = pd.DataFrame(data,['b','a','c'],['Paris','Berlin','Madrid'])
s
s['b']
s['a':'c']
s['d']
s[1]
df
df[1:2]
df[:2]
df[df['Paris']>1]
df.Berlin[df['Berlin']>1]=0
df
df.ix['a',['Berlin','Madrid']]
s
s.drop('d')
s.drop_duplicates()
df.drop('c')
df.drop('Berlin',axis=1)

s2 = pd.Series([0,1,2],['a','c','f'])
s+s2
df
data1=[0,1,2,3,4,5,6]
keyleft=['b','b','a','c','a','a','b']
df1 = pd.DataFrame(keyleft,data1)
df1
dic={'data1':np.arange(7), 'keyleft':['b','b','a','c','a','a','b']}
dic
df3=pd.DataFrame(dic)
df3
dic4={'data2':np.arange(3),'key':['a','b','d']}
dic4
df4=pd.DataFrame(dic2)
df4
pd.merge(df3,df4,left_on='keyleft',right_on='key',how='inner')
pd.merge(df3,df4,left_on='keyleft',right_on='key',how='outer')
pd.merge(left1,right1,on='key',how='left')
s.rank()
s.rank(method='first')
s.rank(method='max',ascending=False)
s.order
s
s.sort_index()
df.sort_index()
df.sort_index(by ="Berlin')
df.max()
df+df.max()
f=lambda x:math.sqrt(x)
df.applymap(f)
df.berlin = df['Berlin'].map(f)
df
df.describe()
df
df.reindex(['c','b','a','g'])
df.reindex(['c','b','a','g'],fill_value=14)
df.reindex(columns = ['Varsobvie','Paris','Madrid'])

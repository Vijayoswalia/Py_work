# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:13:25 2018

@author: Vijay
"""

import numpy as np
import pandas as pd
rng = np.random.RandomState(42)
marks = pd.Series(rng.randint(50,100,11))
marks.sum()
marks.std()
dict(x=1,y=4)
dict(x=1,y=[1,2])
{'x':1,'y':[1,2]}
A=np.random.randint(0,10,6)
A
B=np.random.randint(0,10,6)
B
df = pd.DataFrame({'A':A,'B':B})
df
Aa=pd.Series(A)
Bb=pd.Series(B)
seriesdf = pd.concat([Aa,Bb], axis=1)
seriesdf

df.columns
df.mean()
df.mean(axis=0)
df.mean(axis='rows')
df.mean(axis=1)
df.mean(axis='columns')
df.describe()

df = pd.DataFrame({'key':['A','B','C','A','B','C'],'data1':range(6),'data2':rng.randint(0,10,6)}, columns=['key','data1','data2'])
df

np.repeat(['A','B','C'],2)
np.repeat(['A','B','C'],[1,2,3])

df.groupby('key')
df.groupby('key').sum()
grouped = df.groupby('key')
grouped.sum()

df.groupby('key').aggregate(['min','max','median'])
df.groupby('key').aggregate([np.median,'median'])

df.groupby('key').aggregate({'data1':'min','data2':['max','min']})
df.filter(items = ['key','data1']) #column
df.filter(like = '2', axis=0) #row
df.filter(like = 'c', axis=1) #col

df['data2'].mean() > 4
df['data2'].mean()

x=2
y=3
product = lambda x,y:x*y
product(x,y)

grouped.filter(lambda x: x['data2'].mean()>4) #groups mean more than 4
grouped.filter(lambda x: x['data2'].std()>4)
grouped.transform(lambda x: x - x.mean()) 

df2 = df.set_index('key')
df2
df


newmap = {'A':'Post Graduate', 'B':'Master of Science','C':'Bachelor of Science'}
df2.groupby(newmap).sum()
df2.groupby(str.lower).mean()
df2.groupby([str,str.lower,newmap]).mean()

df.groupby('key').sum().unstack()
























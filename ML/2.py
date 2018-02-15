# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:33:38 2018

@author: Vijay
"""


import numpy as np 
import matplotlib.pyplot as plt   
import pandas as pd  
from pandas import DataFrame, Series 

s1 = Series(range(0,4))
s2 = Series(range(1,5))
s3 = s1 + s2 

print(s1,s2,s3)

df = pd.read_csv('E:\\Data Science\\Python\\ML-WAB\\DATASET\\Contriesdata.csv',header=0)
#df = pd.concat([df[col].dropna().reset_index(drop=True) for col in df], axis=1)
df.head()


workbook = pd.ExcelFile('E:\\Data Science\\Python\\ML-WAB\\DATASET\\SAmple1.xlsx')
workbook.sheet_names
df = workbook.parse('SAmple1')
df.head()

##writing excel to csv
df.to_csv('E:\\Data Science\\Python\\ML-WAB\\DATASET\\Contriesdata.csv', encoding='utf-8')

from pandas import ExcelWriter
writer = ExcelWriter('E:\\Data Science\\Python\\ML-WAB\\DATASET\\filename.xlsx')
df.to_excel(writer,'Sheet1')
df.to_excel(writer,'Sheet2')
writer.save()

df[df.columns[2]]
##
idx = df.columns          
# get col index
label = df.columns[0]     
# 1st col label
lst = df.columns.tolist() 
lst
len(lst)
# get as a list

##creating and delting column
df['new_col'] = range(len(df))
df['new_col'] = np.repeat(np.nan,len(df))
df['random'] = np.random.rand(len(df))
df.head()

df = df.drop('new_col', axis=1)
df.head()

##
df1= pd.pivot_table(df, index =['Comm. Code','Quantity'])
df1=pd.DataFrame(df1)
df1.head()

df2 = pd.read_csv('E:\\Data Science\\Python\\ML-WAB\\DATASET\\Contriesdata.csv' ,header=0)
frames = [df2, df1]
result = pd.concat(frames)
result.head()

##
result = pd.concat([df2, df1], axis=1, join='inner')
result.head()
result = pd.concat([df2, df1], axis=1, join_axes=[df1.index])

##logarithmic
b=3
import math
math.log(b)

x = [1500, 1049.8, 34, 351, 100]
from math import log
[log(y,10) for y in x]

import numpy
g=numpy.log10(x)

import matplotlib.pyplot as plt
#plt.plot([1,2,3,4])
plt.plot(g)
plt.ylabel('some numbers')
plt.show()

##
from scipy.stats.stats import pearsonr   
a = [1,4,6]
b = [1,2,3]   
print (pearsonr(a,b))

x = int (df["Agriculture"])
y = int (df["Literacy"])
print (np.corrcoef(x,y))

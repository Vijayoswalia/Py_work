# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:17:17 2018

@author: Vijay
"""

import pandas as pd
pandas.__version__
data = pd.Series([0.25,0.50,0.75,100])
data.values
data.index
data = pd.Series([0.25,0.50,0.75,100], index=['a','b','c','d'])
data
data['b']

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population['California']
population['California':'Illinois']
population['California']


area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
 'Florida': 170312, 'Illinois': 149995}

area = pd.Series(area_dict)

states = pd.DataFrame({'population': population,
 'area': area})

states

pd.DataFrame(population, columns=['population'])


rollno=[1,2,3]
name=['A','B','C']
df1 = pd.DataFrame(rollno,name)
df1

sdata = pd.DataFrame({'rollno':rollno, 'name':name}, columns=['rollno','name'])
sdata

sdata2 = pd.DataFrame(list(zip(rollno,name)))
sdata2

pd.DataFrame(np.random.rand(3, 2),
 columns=['foo', 'bar'],
 index=['a', 'b', 'c'])

ind = pd.Index([2, 3, 5, 7, 11])
ind[1]
ind[::2]

indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
indA & indB


'''indexing'''

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
 data


# explicit index when indexing
 data[1]
# implicit index when slicing
In[13]: 

data.loc[1]

data.loc[1:3]

data.iloc[1]

data.iloc[1:3]


area = pd.Series({'California': 423967, 'Texas': 695662,
 'New York': 141297, 'Florida': 170312,
 'Illinois': 149995})
 pop = pd.Series({'California': 38332521, 'Texas': 26448193,
 'New York': 19651127, 'Florida': 19552860,
 'Illinois': 12882135})
 data = pd.DataFrame({'area':area, 'pop':pop})
 data

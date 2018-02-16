# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:42:09 2018

@author: Vijay
"""

import numpy as np
import pandas as pd

names = ["meena", "apoorva","kautav","subham","goldie","hitesh","shruti","vijay","achal","lalit","varun"]
rollnos = [109,102,105,106,103,110,101,107,104,111,108]
gender = ['f','f','m','m','m','m','f','m','m','m','m']
python = np.random.randint(50,100,11)
python
print(python)
sas = np.random.randint(50,100,11)
len(sas)
nameroll = pd.Series(names,rollnos)
nameroll
type(nameroll)
nameS=pd.Series(names, index=rollnos)
nameS

112 in nameS
111 in nameS

nameS.keys()
nameS.index
nameS.items

nameS
nameS[108]='jain'
names[nameS=="jain"]
nameS[:5]
nameS.iloc[0:5]
nameS[0]
names[:1]
nameS.iloc[0]
nameS.loc[108]

nameS.loc[103:110]

nameS = pd.Series(names)
rollnosS = pd.Series(rollnos)
genderS = pd.Series(gender)
pythonS = pd.Series(python)
sasS = pd.Series(sas)

student = pd.concat([nameS,rollnosS,genderS,pythonS,sasS], axis=1)
student
student1 = pd.DataFrame({'rollnos':rollnos,'name':names, 'gender':gender, 'python':python,'sas':sas})
student1
student3 = pd.DataFrame({'rollnos':rollnos,'name':names, 'gender':gender, 'python':python,'sas':sas}, columns = ['rollnos','name','gender','python','sas'])
student3.T
student3.values[0]
student3.iloc[0]
student3[nameS]
student3
student3['name']
student3.iloc[:3,:2]
student3.loc[:105,:'python']
student3.iloc[:5,0:2]
total = student3['sas']+student3['sas']
total
student3 = pd.DataFrame({'rollnos':rollnos,'name':names, 'gender':gender, 'python':python,'sas':sas, 'total':total})
student3['total']=student3['python']+student3['sas']
student3
student3[student3.total>150]









































































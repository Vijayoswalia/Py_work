# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:24:14 2018

@author: Vijay
"""
import numpy as np
import pandas as pd
nameL = ["meena", "apoorva","kautav","subham","goldie","hitesh","shruti","vijay","achal","lalit","varun"]
rollnoL = [109,102,105,106,103,110,101,107,104,111,108]
genderL = ['f','f','m','m','m','m','f','m','m','m','m']
courseL = ['pg','pg','msc','msc','pg','pg','pg','pg','pg','pg','bsc']
pythonL = np.random.randint(60,90,11)
sasL = np.random.randint(65,85,11)
hadoopL = np.random.randint(71,90,11)
feesL = np.random.randint(1000000,1500000,11)
hostelL = ['True','False','True','False','False','True','False','True','False','False','False',]
student1['total']= student1['python']+student1['sas']+student1['hadoop']
student1 = pd.DataFrame({'rollnos':rollnoL,'name':nameL, 'gender':genderL,'fee':feesL,'hostel':hostelL, 'python':pythonL,'sas':sasL,'course':courseL,'hadoop':hadoopL})
student1
student1.to_csv("student.csv")

from numpy import random
classes=['C1','C2','C3']
sclass = random.choice(classes,11)
sclass
student1['sclass']=pd.Series(sclass)
student1
student1.to_csv("student3.csv")
pd.pivot_table(student1, index=['name'])
pd.pivot_table(student1, index=['name', 'sclass','hostel'])
pd.pivot_table(student1, index=['sclass','gender'])
pd.pivot_table(student1, index=['course','sclass'],values=['total','python'])
pd.pivot_table(student1, index=['course','sclass'],values=['total','python'], aggfunc=np.sum)
pd.pivot_table(student1, index=['course','sclass'],values=['total','python'], aggfunc=[np.sum, np.mean,len])


















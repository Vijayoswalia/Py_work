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

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:58:17 2017

@author: Vijay
"""

d={'user':'bozo', 'pswd':1234}

d

d['id']=45
d

d['username']='bozos'
d

del d['username']  #delete
d

d.clear()     #clear
d

d={'user':'bozo', 'p':1234, 'i':34}
d

d.keys()

d.values()

d.items()

print("My userid is", d['user'], "and my password is", d['p'])

len(d)

d1={'class':'syntax', 'room':'ecme107', 'i':55}
d1

d.update(d1)
d
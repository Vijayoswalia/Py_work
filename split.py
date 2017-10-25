# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:38:05 2017

@author: Vijay
"""

name = "Brave Sir Robin"
for word in name.split():
    print(word)
    
name = "Brave Sir Robin"
for word in name.split("R"):
    print(word)
    
    
s = " Jessica 31 647.28"
name, age, money = s.split()
print(name)
print(int(age))
print(float(money))

import os
f = open("hourss.txt","w")
f.write("123 suzy 9.5 7.6 3.1 3.2 \n")
f.write("456 brad 7.0 9.6 6.5 4.9 \n")
f.write("789 jenn 8.0 8.0 8.0 7.5 \n")
f.close

f = open("hourss.txt", "r")
for line in f:
    id, name, monday, tue, wed, thurs = line.split()
    print(line)
print(name, "ID", id, "worked", \
      round(hourss, 2), "hours")
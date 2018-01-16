# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:52:32 2018 by vijayoswalia for DS
"""

x = [1,2,3]
x
print(x)

rollnos = [1,2,3,4,5,6,10,11]
rollnos[0]
rollnos[8]
rollnos[7]
rollnos[9]
len(rollnos)
sum(rollnos)
min(rollnos)
max(rollnos)

rollnos
for i in range (len(rollnos)):
    print(rollnos[i], end=",")
    
if 13 in rollnos:
    print("yes")
else:
    print("no")
    
rollnos.append(13)
rollnos
sorted(rollnos)

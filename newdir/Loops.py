# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:21:44 2017

@author: Vijay
"""

x=1
if x == 3:
    print ("x equals 3.")
elif x == 2:
    print("x euals 2.")
else:
    print("x equals something else.")
print ("This is outside the 'if.")

x = 10
while x:
    x = x-1
    if x%2 !=0: continue   #ood skip print
    print(x)
    
    def myfun (b,c):
        return b + c
    myfun(3,4)
    
    def hello():
        name = str(input("enter your name: "))
        age = float(input("enter your age: "))
        if name:
            print("Hello " + str(name))
            print("Age", float(age))
        else:
            print("Helo World")
        return
    hello()
    
    
    def intersect(seq1, seq2):
        res = []    #start empty
        for x in seq1:
            if x in seq2:
                res.append(x)
        return res
    print(intersect('neena','meesha'))
    
    
    f = lambda x,y,z: x+y+z
    f
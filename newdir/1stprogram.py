# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:39:43 2017

@author: Vijay
"""

fam = [1.73, 1.68, 1.71, 1.89]
print(fam)


print(fam + fam)
print(fam*3)


fam = ["Liz", 1.73, "Emma", 1.68, "mom", 1.71, "Dad", 1.89]
fam
print(fam)
print(type(fam))
print(fam[3])
print(fam[10])
print(fam[-1])
print(fam[3:5])
fam[0:2] = ['Liz', 1.74]
fam_ext = fam + ['me',1.79]
print(fam_ext)


x = ["a", "b", "c"]
y=x
y[1]="z"
y
x


x = ["a", "b", "c"]
y=list(x)
y
z= x[:]
z

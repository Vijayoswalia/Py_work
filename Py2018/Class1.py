# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:07:42 2018 by vijayoswalia for DS
"""
import os
import sys
os.path.dirname(sys.executable)
import keyword
print(keyword.kwlist)
a=b=c=1
a
b
c
a,b,c = 1,2,"Tom"
a
b
c

for i in range (4):
    print(i)
    print(i+2)
    for j in range(3):
        print(j )

for i in range(4):
    print(i,i+2, sep="&", end='-')
    
first_item = 1
second_item = 2
third_item = 3
gtotal = first_item + \
second_item + \
third_item
print(gtotal)
word = ''' vijay
pal 
singh'''
word

a = 2
print("no. of students", a)

n = input("enter a number")
n+3
print(n)

m=eval(input("enter a number"))
m*3

dir()
%reset

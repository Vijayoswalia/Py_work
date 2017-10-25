# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:03:09 2017

@author: Vijay
"""

str = input("Enter your input")
print("received input is : ", str)


str = eval(input("Enter your input"))
print("received input is : ", str)


import os
os.getcwd()
os.listdir()
os.listdir("E:\Data Science\pyWork\PyProjects\Py_In_Action")
os.listdir("E:\\Data Science\pyWork\PyProjects\Py_In_Action\Py_In_Action")
os.mkdir("newdir")
os.listdir()
os.chdir("newdir")
os.getcwd()
os.chdir("..")
os.getcwd()

f = open("E:\Data Science\pyWork\PyProjects\Py_In_Action\Py_In_Action\V.txt") 
# open the file 
print(f)
print("Name of the file: ",f.name)
print("closed or not: ",f.closed)

f.close()  #close the file

os.rename("V.txt","ABC.txt")
os.getcwd()
os.listdir()

fo = open("foo.txt","w")
fo.write("Python is a great language.\r\nYEah its great!!\r\n")
fo.close()

fo = open("foo.txt", "r+")
str = fo.read(20)
print("Right String is: ",str)
print(str)

fo.tell()
position = fo.seek(3,0)
str = fo.read(10)

f = open("sunday.txt","w")
f.write("Today is sunday\n")
f.close()





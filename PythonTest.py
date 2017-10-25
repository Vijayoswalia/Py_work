color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])

import numpy as np
data1 =[1,2,5,10,-20] 
def median(data):
    x=sorted(data1)
    if (len(x)%2 == 0):
        median =(x[len(x)/2]+x[len(x)/2+1])/2
        return median
    else: 
        median = x[int((len(x)-1)/2)]
        return median 
median(data1)

import matplotlib.pyplot as plt
Age = [10,20,30,40]
Weight = [22,43,54,67]
plt.scatter(Age,Weight)
plt.xlabel('Age')
plt.ylabel('Weight')
plt.title('Age vs Weight')

import os
f = open("myfile.txt","w")
f.write("My favourite language for maintainability is Python \n")
f.write("It has simple, clean syntax \n")
f.write("It has good library support \n")
f.close()
f=open("myfile.txt", "r")
contents =f.read()
print(contents)


# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:15:50 2018

@author: Vijay
"""

names= ['ashok', 'vijay', 'mahesh']
", ".join(names)
'ashok'.upper()
f=open("E:\\Data Science\\pyWork\\PyProjects\\Py_In_Action\\Py_In_Action\\newdir\\foo.txt")
f
f.readline()

def wordonly(inputstring):
    #the below wrongletters can be updated based on users requirement to exclude particular letters or symols
    wrongletters=(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','1','2','3','4','5','6','7','8','9','0','...','..', '\\', '/','//','///',':','\\\\', '#'])
    count=0 #initializing count
    for i in wrongletters:  ##loop function for iterating all the non letters
        for l in inputstring: ##loop function for iterating all the input
            if (l!=i):        #Checking condition whether input doesnot match    			wrongstrings
                    	count=count+1 ##appending for the wrong match iteration
            else:
                print ("\nIncorrect word entry at position:",i,"\nError caused due to matching at:",count,"\nSystem will exit\n")
                raise SystemExit ##raises exception and exits 
    print ("The input has all letters having no other characters")



# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:23:13 2018 by vijayoswalia for DS
"""

l = [1,2,"a"]
type(l)
t=(1,2,"a")  #tuple is immutable list
type(t)


D = {"a":1, "b":2}  #Dictionary is mutable
D
type(D)

s={1,2,3}     #set
s
type(s)
f = frozenset({3,8,4,6})
f
type(f)


a='ls'
b='nice'
my_list=['my','list',a,b]
my_list2=[[4,5,6,7,],[3,4,5,6]]
my_list
my_list[1]
my_list[-3]  # counts from last and starts from -1
my_list[1:3]
len(my_list)
my_list[-len(my_list)]
my_list[1:]
my_list[:3]
my_list[:]
my_list2[1][0]
my_list2[1][:2]

my_list+my_list
my_list*2
my_list2[1][0]>4
my_list.index(a)
my_list.count(a)
my_list.append('!')
my_list
my_list.extend('!')
my_list
my_list.remove('!')
my_list
del(my_list[0:1])
my_list

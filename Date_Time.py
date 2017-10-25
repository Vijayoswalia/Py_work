# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:57:52 2017

@author: Vijay
"""

import time
ticks = time.time()
print ("number of ticks since 12:00 am, January 1 , 1970:", ticks)

localtime = time.localtime(time.time())
print("Local current time:", localtime)

import calendar
cal = calendar.month(2008, 1)
print("here is the calendarr:")
print(cal)

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tommorrow = today + datetime.timedelta(days = 1)
print("yesterday:", yesterday)
print("today:", today)
print("tommorrow:", tommorrow)

from datetime import date
a = date(2016, 1, 31)
b = date(2017, 1, 31)
print(b-a)
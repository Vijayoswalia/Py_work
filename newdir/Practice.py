# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:26:34 2017

@author: Vijay
"""
import numpy as np
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
mean([1,2,3,4])

import numpy as np
print(np.median([1, 3, 5, 7]))

import statistics
items = [1, 2, 3, 6, 8]
statistics.median(items)

import numpy as np
print(np.mode([1, 3, 5, 7]))

import statistics
items = [1, 2, 3, 6, 6, 8 ,8, 8]
statistics.mode(items)


import statistics
items = [1, 2, 3, 6, 6, 8 ,8, 8]
statistics.mean(items)

import statistics
items = [1, 2, 3, 6, 6, 8 ,8, 8]
statistics.variance(items)

import statistics
items = [1, 2, 3, 6, 6, 8 ,8, 8]
statistics.stdev(items)
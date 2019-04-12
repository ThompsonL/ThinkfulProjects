# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:06:06 2019

@author: liuth
"""

import numpy as np
ages = [14,12,11,10,8,6,8,6,6]
ages2 = [14,12,11,10,8,7,8]
ages3 = [14,12,11,10,8,7,1]

def modes(ages):

   # Empty dict we'll use to store item counts.
   counts = {}

   # Populate the dict.
   for value in ages:
       if value in counts:
           counts[value] += 1
       else:
           counts[value] = 1

   # Find the number of times the mode appears.
   max_occurrence = max(counts.values())

   # Short-circuit if there is no mode.
   min_occurrence = min(counts.values())
   if max_occurrence == min_occurrence:
       return []

   # Initialize an empty list to populate and return.
   result = []
   for key in counts.keys():
       if counts[key] == max_occurrence:
           result.append(key)

   return print(sorted(result))


modes(ages)

#nest this into the loop before the return
def summarystats(ages):
    print("mean: ",np.mean(ages))
    print("median: ",np.median(ages))
    print("variance: ",np.var(ages))
    print("std. deviation :",np.std(ages))
    print("standard error :",np.std(ages)/np.sqrt(len(ages)-1))
    print(modes(ages))
summarystats(ages)
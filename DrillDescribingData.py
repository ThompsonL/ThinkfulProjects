# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:37:34 2019

@author: liuth
"""

import numpy as np
ages = [14,12,11,10,8,6,8]

#Finding the duplicates
seen = {}
no_dupes = [x for n, x in enumerate(ages) if x not in ages[:n]]
print (no_dupes) # [[1], [2], [3], [5]]

dupes = [x for n, x in enumerate(ages) if x in ages[:n]]
print (dupes) # [[1], [3]]

print(dupes)

def summarystats(ages):
    print("mean: ",np.mean(ages))
    print("median: ",np.median(ages))
    print("variance: ",np.var(ages))
    print("std. deviation :",np.std(ages))
    print("standard error :",np.std(ages)/np.sqrt(len(ages)-1))
    print("mode :",dupes)
summarystats(ages)

#2 
#Mean as it is the central tendency
#STD deviation as it shows the variance between each value

#3 Cindy = 6 had a birthday Cindy = 6 + 1
ages2 = [14,12,11,10,8,7,8]
#Finding the duplicates
#Question is there a way to run this block where as ages2
#can be assigned a number?  What is that method called?
seen = {}
no_dupes = [x for n, x in enumerate(ages2) if x not in ages2[:n]]
print (no_dupes) # [[1], [2], [3], [5]]

dupes = [x for n, x in enumerate(ages2) if x in ages2[:n]]
print (dupes) # [[1], [3]]


def summarystats(ages2):
    print("mean: ",np.mean(ages2))
    print("median: ",np.median(ages2))
    print("variance: ",np.var(ages2))
    print("std. deviation :",np.std(ages2))
    print("standard error :",np.std(ages2)/np.sqrt(len(ages2)-1))
    print("mode :",dupes)
summarystats(ages2) 

#ages1 vs ages2
#Mean, STD Deviation were the big changes

#4 Replace Cousin Oliver = 8 with Jessica = 1
ages3 = [14,12,11,10,8,7,1]
seen = {}
no_dupes = [x for n, x in enumerate(ages3) if x not in ages3[:n]]
print (no_dupes) # [[1], [2], [3], [5]]

dupes = [x for n, x in enumerate(ages3) if x in ages3[:n]]
print (dupes) # [[1], [3]]


def summarystats(ages3):
    print("mean: ",np.mean(ages3))
    print("median: ",np.median(ages3))
    print("variance: ",np.var(ages3))
    print("std. deviation :",np.std(ages3))
    print("standard error :",np.std(ages3)/np.sqrt(len(ages3)-1))
    print("mode :",dupes)
summarystats(ages3) 

#Median is the best central tendancy because the variance is too high
magazine = [20, 23, 17]
#dropping scifi because they do not belong in same category
print(np.mean(magazine))

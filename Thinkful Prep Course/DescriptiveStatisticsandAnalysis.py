# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:34:15 2019

@author: liuth
"""

import numpy as np
import matplotlib.pyplot as plt

#Mean of 5, STD Dev .5
var1 = np.random.normal(5,.5,100)
#Mean of 10, STD Dev 1
var2 = np.random.normal(10,.1,100)
var3 = var1 + var2

plt.hist(var3)

mean = np.mean(var3)
std = np.std(var3)

plt.axvline(x=mean,color='black')
plt.axvline(x=mean+std, color='green')
plt.axvline(x=mean-std, color='blue')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:55:43 2019

@author: liuth

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

import os
print(os.getcwd())
os.chdir('C:\\Users\\liuth\\Documents\\Data')

mydata = pd.read_csv('Admission_Predict.csv')
mydata.columns = ['SerialNo.', 'GREScore',\
                  'TOEFLScore', 'UniversityRating', 'SOP',\
                  'LOR', 'CGPA', 'Research', 'ChanceofAdmit']

#add grids 
sns.set()

visl = sns.distplot(mydata["GREScore"], bins=5)
#This is a distribution of all the GRE Scores.

vis2 = sns.lmplot(data=mydata, x='GREScore', y='TOEFLScore',\
                  fit_reg=False, hue='GREScore', size=8,\
                  y_jitter=.02, logistic=True)
#This is a scatter plot showing a distribution of the GREscore in comparison
#with the TOEFL score

vis3 = sns.boxplot(data=mydata, x='UniversityRating', y='ChanceofAdmit')
#This shows the university rating comparison with the chances of being admitted

vis4 = sns.violinplot(data=mydata, x='ChanceofAdmit', y='GREScore')
#Gives a visualization of GRE score and the chance of admit.  Perhaps correlation?
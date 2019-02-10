# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:52:15 2019

@author: liuth
"""

import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir('C:\\Users\\liuth\\Documents\\Data')
#Naming the Dataframe
checkbook2 = pd.read_csv('Checkbookdata.csv', encoding='latin1')

#Frequencies of each type (bar) and usage with each account
checkbook2['Type'].value_counts().plot(kind='bar')
checkbook2['Account'].value_counts().plot(kind='bar', \
          title='Account Activity')
checkbook2['Account'].value_counts().plot(kind='bar')

#sorting (iloc = index NUMBER) (.loc = index of column), the second []
#lets you sort additional columns that come back true
expsort = checkbook2.loc[checkbook2['Type']=='expense',['Date','Amount','Account']]
incsort = checkbook2.loc[checkbook2['Type']=='income',['Amount','Account']]
transort = checkbook2.loc[checkbook2['Type']=='transfer',['Amount','Account']]


#Create a new column with year and quarters
checkbook2['Year'] = pd.DatetimeIndex(checkbook2['Date']).year
checkbook2['Quarter'] = pd.DatetimeIndex(checkbook2['Date']).quarter
expsort['Quarter']= pd.DatetimeIndex(expsort['Date']).quarter
expsort['Year']= pd.DatetimeIndex(expsort['Date']).year


#DO NOT SUM THEM UP YOU WILL BE OVERSTATING INCOME and TRANSFER

#Plotting the visualizations of each account
sns.scatterplot(data=expsort.loc[expsort['Account']=='Chase Freedom Unlimited']\
            , x='Account' , y='Amount')

plat = checkbook2.loc[checkbook2['Account']=='AMEX Platinum']
plat.describe()

#Amount of charges in each account
sns.barplot(data=checkbook2.loc[checkbook2['Account']=='Chase Freedom Unlimited'\
                                ,'Type'], x='Amount', y='Amount')

#Closer look of what is being paid off individual accounts
#This deals with the level issue (if one part is really flat)
logexp = np.log(checkbook2['Amount'])
sns.boxplot(data=checkbook2.loc[checkbook2['Account']=='Active Duty Checking']\
                               , x='Account', y=logexp, hue='Type')

#Closer look of what is being paid off
sns.boxplot(data=checkbook2, x='Amount', y='Type')
sns.boxplot(data=checkbook2, x='Account', #y = 'Transfer')



#Merge Index to create seperate columns
exincmerge = expsort.merge(incsort, right_index=True, left_index=True,
                                   how='outer').reset_index()



#Histogram comparing income to expense
sns.catplot(data=checkbook2, x='Account', y='Amount', hue='Type', kind='swarm')
sns.barplot(data=checkbook2, x='Type', y='Amount', hue='Account')
##Is there a higher amount of expenses than there are assets?  
#    In this case the comparison is only measuring cash.
sns.barplot(data=checkbook2, x='Type', y='Amount', hue='Account')

#Time series review
sns.catplot(data=checkbook2, x='Type', y='Amount', hue='Quarter',\
            kind='bar')

##What is the least utilized credit card and what category is it being utilized for?  Why is that?

sns.catplot(data=checkbook2.loc[checkbook2['Account']=='AMEX Platinum']\
                               , x='Account', y='Amount', hue='Category')
sns.catplot(data=checkbook2.loc[checkbook2['Category']=='Travel']\
                               , x='Quarter', y='Amount',\
                               col='Account')
sns.catplot(data=checkbook2.loc[checkbook2['Account']=='Chase Freedom Unlimited']\
                               , x='Account', y='Amount', hue='Category', kind='swarm')
sns.catplot(data=checkbook2, x='Quarter', y='Amount', hue='Category', col='Account'\
                               , kind='swarm')
sns.catplot(data=checkbook2.loc[checkbook2['Category']=='Dining']\
                               , x='Account', y='Amount',kind='swarm', col='Type')
sns.catplot(data=checkbook2.loc[checkbook2['Category']=='Travel']\
                               , x='Account', y='Amount',kind='swarm', col='Type')

#Which quarter is the highest expenditure? 


sns.catplot(data=checkbook2.loc[checkbook2['Type']=='expense']\
                               , x='Quarter', y='Amount',\
                               col='Year', kind='swarm')

sns.catplot(data=checkbook2.loc[checkbook2['Category']=='Dining']\
                               , x='Quarter', y='Amount',\
                               hue='Year', col='Account')

#Frequency of quarter with the most expenditure

expsort.loc[expsort['Quarter']==1].describe()
expsort.loc[expsort['Quarter']==2].describe()
expsort.loc[expsort['Quarter']==3].describe()
expsort.loc[expsort['Quarter']==4].describe()



#Further Exploration Breaking down Categories by Quarters
sns.catplot(data=checkbook2.loc[checkbook2['Type']=='expense']\
                               , x='Account', y='Amount', hue='Category',\
                               kind='swarm')

sns.catplot(data=checkbook2.loc[checkbook2['Category']=='Entertainment']\
                               , x='Account', y='Amount', hue='Type',\
                               kind='swarm', col = 'Quarter', col_wrap=2)

sns.catplot(data=checkbook2.loc[checkbook2['Category']=='Dining']\
                               , x='Account', y='Amount', hue='Type',\
                               kind='swarm', col = 'Quarter', col_wrap=2)

sns.catplot(data=checkbook2.loc[checkbook2['Category']=='Travel']\
                               , x='Account', y='Amount', hue='Year',\
                               kind='swarm', col = 'Quarter', col_wrap=2)


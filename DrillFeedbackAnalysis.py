# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:25:04 2019

@author: liuth
"""

import numpy as np
import pandas as pd
import scipy
import sklearn
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir('C:\\Users\\liuth\\Documents\\Python Scripts\\ThinkfulProjects\\Data')

#Dataframe from https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences#
#Loading\Exploring Data
dataset_1_path = 'amazon_cells_labelled.txt'
data_raw = pd.read_csv(dataset_1_path, delimiter="\t", header=None)
data_raw.columns = ['Comment', 'Score']
data_raw.head(3)

data_raw.columns.describe()

#Building features
keywords = ['good', 'great', 'excellent', 'must have', 'awesome', 'impressed',\
            'love', 'quality', 'happy', 'recommend', 'recommended', 'comfortable',\
            'well']

for key in keywords:
     data_raw[str(key)] = data_raw.Comment.str.contains(
        ' ' + str(key) + ' ',
        case=False
    ).astype(int)

#Adding additional features
data_raw['allcaps'] = data_raw.Comment.str.isupper()
# data_raw['Score'] = (data_raw['Score'] == 'Score')
data = data_raw[keywords + ['allcaps']]
target = data_raw['Score']

data_raw.head(3)

#Heatmap
sns.heatmap(data_raw.corr())

#Input comparison
data = data_raw[keywords]
target = data_raw['Score']

#Naive Bayes Model
bnb = BernoulliNB()
bnb.fit (data, target)
#Classification of the model
y_pred = bnb.predict(data)

#Printed Results
print("Number of mislabeled points out of a total {} points : {}".format(
    data.shape[0],
    (target != y_pred).sum()
))

#Confusion Matrix
confusion_matrix(target, y_pred)

#Cross Validate
#Use train_test_split to create the necessary training and test groups
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2,\
                                                    random_state=20)
print('With 20% Holdout: ' + str(bnb.fit(X_train, y_train).score(X_test, y_test)))
print('Testing on Sample: ' + str(bnb.fit(data, target).score(data, target)))

cross_val_score(bnb, data, target, cv=10)
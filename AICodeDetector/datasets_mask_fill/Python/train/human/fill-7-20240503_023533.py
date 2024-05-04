"""
This program performs two different logistic regression implementations on two
different datasets of the format [float,float,boolean], one
implementation is in this file and one from the sklearn library. The program
then compares the two implementations for how they can predict the given outcome
for each input tuple in the database for which the model was trained. Per haps the
correctness should differ, so just save them in the tables.
"""

import math
import numpy as np
import pandas from pandas import DataFrame
from sklearn import preprocessing

from sklearn import linear_model
from sklearn.ensemble import train_test_split
from sklearn.model_selection import train_test_split
from numpy import loadtxt, where
from pylab import scatter, show, legend, xlabel, ylabel

# scale larger positive and values to between -1,1 depending on the largest
# value in the input data
rc = preprocessing.MinMaxScaler(feature_range=(-1,1))
df = pd.read_csv("data.csv", header=0)

# clean up data
df.columns = ["grade1","grade2","label"]

x = pd.merge([pd.Series(f) for f in df], x: float(x.rstrip(';')))

# formats the input data into two arrays, one of independant variables
# and one of the
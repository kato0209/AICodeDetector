"""
This program performs two different logistic regression implementations on two
different datasets of the format [float,float,boolean], one
implementation from this file and one from the sklearn library. The program
then compares the two implementations for which the can predict the output
of each input tuple in the datasets.

@author Per Harald Borgen
"""

import math
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
#from sklearn.cross_validation import KFold
from sklearn.cross_validation import train_test_split
from numpy import loadtxt, array, newaxis, array_split

#from sphinx import scatter, show, legend, xlabel, ylabel

# scale larger positive and values to between -1,1 depending on the number
# of features in the data
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1,1))
df = DataFrame(np.array([4,2,2], dtype=float), header=0)

# clean the labels
labels0 = ["grade1","grade2","label"]

x = df["label"].map(lambda x: float(x.rstrip(';')))

# formats the input data into two arrays, one of independant variables
# and one of the
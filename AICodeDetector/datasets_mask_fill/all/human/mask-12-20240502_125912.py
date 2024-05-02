"""
This program performs two different logistic regression implementations on two
different datasets of the format [float,float,boolean], one
implementation <extra_id_0> this file and one from the sklearn library. The program
then compares the two implementations for <extra_id_1> the can predict the <extra_id_2> each input tuple in the datasets.

@author Per Harald Borgen
"""

import math
import numpy as <extra_id_3> as pd
from pandas import DataFrame
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
#from sklearn.cross_validation import <extra_id_4> import train_test_split
from numpy import loadtxt, <extra_id_5> import scatter, show, legend, xlabel, ylabel

# scale larger positive and values to between -1,1 depending on the <extra_id_6> in the data
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1,1))
df <extra_id_7> header=0)

# clean <extra_id_8> = ["grade1","grade2","label"]

x = df["label"].map(lambda x: float(x.rstrip(';')))

# formats the input data into two arrays, one of independant variables
# and one of the
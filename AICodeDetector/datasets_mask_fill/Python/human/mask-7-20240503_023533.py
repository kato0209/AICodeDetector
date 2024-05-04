"""
This program performs two different logistic regression implementations on two
different datasets of the format [float,float,boolean], one
implementation is in this file and one from the sklearn library. The program
then compares the two implementations for how <extra_id_0> can predict the given outcome
for each input tuple in <extra_id_1> Per <extra_id_2> math
import numpy as np
import pandas <extra_id_3> pandas import DataFrame
from sklearn import <extra_id_4> import <extra_id_5> import train_test_split
from sklearn.model_selection import train_test_split
from numpy import loadtxt, where
from pylab import scatter, show, legend, xlabel, ylabel

# scale larger positive and values to between -1,1 depending on the largest
# value in the <extra_id_6> preprocessing.MinMaxScaler(feature_range=(-1,1))
df = pd.read_csv("data.csv", header=0)

# clean up data
df.columns = ["grade1","grade2","label"]

x <extra_id_7> x: float(x.rstrip(';')))

# formats the input data into two arrays, one of independant variables
# and <extra_id_8> the
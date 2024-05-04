# Logistic Regression

# Importing modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importing the dataset
train = pd.read_csv('titanic_train.csv')

'''
Logistic regression does not make any difference the key assumptions of linear
regression and general linear models that are based on ordinary least squares
algorithms – particularly regarding linearity, normality, homoscedasticity,
and measurement level.
 
First, logistic regression does not make a linear relationship between the
dependent and independent variables.  It  would  be simpler if the error conditions of this model and dependent variables  do not need to be normally distributed.
Third, homoscedasticity is not  required.  Finally, the dependent variable 
in logistic regression is measured as interval or ratio of the dependent variable.

Linearity logistic regression requires the dependent variable to be binary
and ordinal logistic regression requires the dependent variable to be ordinal.

Logistic regression requires the observations to
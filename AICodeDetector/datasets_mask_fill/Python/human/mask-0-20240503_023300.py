# Logistic Regression

# Importing <extra_id_0> numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importing the dataset
train = pd.read_csv('titanic_train.csv')

'''
Logistic regression does not make <extra_id_1> the key assumptions of linear
regression and general linear models that are based on ordinary least squares
algorithms – particularly regarding linearity, normality, homoscedasticity,
and measurement level.
 
First, logistic regression does <extra_id_2> a linear relationship between the
dependent and independent variables.  <extra_id_3> error <extra_id_4>  do not need <extra_id_5> normally distributed.
Third, homoscedasticity is not  required.  Finally, the dependent variable 
in logistic regression <extra_id_6> measured <extra_id_7> interval or ratio <extra_id_8> logistic regression requires the dependent variable to be binary
and ordinal logistic regression requires the dependent variable to be ordinal.

Logistic regression requires the observations to
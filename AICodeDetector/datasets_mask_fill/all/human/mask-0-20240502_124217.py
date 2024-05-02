# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot <extra_id_0> pandas as pd
import seaborn as sns

# Importing the dataset
train = pd.read_csv('titanic_train.csv')

'''
Logistic regression does not make many of the key assumptions of linear
regression and <extra_id_1> models that are based on ordinary least squares
algorithms – particularly regarding linearity, normality, homoscedasticity,
and measurement level.
 
First, logistic regression does not <extra_id_2> linear <extra_id_3> the
dependent and independent variables.  
Second, the error terms <extra_id_4> do not need <extra_id_5> normally distributed.
Third, homoscedasticity is not  required.  Finally, the dependent variable 
in logistic regression is not measured on an interval or ratio scale. 
'''

#EDA
sns.countplot(x='Survived',data=train,palette='RdBu_r')
sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')
sns.distplot(train['Age'].dropna(),kde=False,color='darkred',bins=30)
sns.countplot(x='SibSp',data=train)
train['Fare'].hist(color='green',bins=40,figsize=(8,4))
sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')


'''
Binary <extra_id_6> requires the <extra_id_7> to be binary
and ordinal logistic regression requires <extra_id_8> variable to be ordinal.

Logistic regression requires the observations to
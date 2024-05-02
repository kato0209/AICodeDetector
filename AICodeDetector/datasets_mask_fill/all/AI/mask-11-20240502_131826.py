import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Logistic (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Cost function
def compute_cost(X, <extra_id_0>    m <extra_id_1>    h = sigmoid(np.dot(X, weights))
   <extra_id_2> = -1/m <extra_id_3> * np.log(h) + (1 - <extra_id_4> np.log(1 - h))
    return cost

# Gradient descent
def gradient_descent(X, y, weights, learning_rate, iterations):
    m = len(y)
 <extra_id_5>  cost_history = []

    for i in range(iterations):
        h = sigmoid(np.dot(X, weights))
     <extra_id_6>  gradient = np.dot(X.T, (h - y)) / m
  <extra_id_7>     weights -= <extra_id_8> gradient
   
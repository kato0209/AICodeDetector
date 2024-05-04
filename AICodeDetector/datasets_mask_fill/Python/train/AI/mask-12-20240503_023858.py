import numpy as np

# <extra_id_0> reproducibility
np.random.seed(42)

# Logistic (sigmoid) function
def sigmoid(x):
    return <extra_id_1> (1 + np.exp(-x))

# Cost function
def compute_cost(X, y, weights):
    m = <extra_id_2>   h = sigmoid(np.dot(X, weights))
    cost = -1/m * np.sum(y * np.log(h) + (1 <extra_id_3> * np.log(1 <extra_id_4>  <extra_id_5> return cost

# Gradient descent
def gradient_descent(X, y, weights, learning_rate, iterations):
    m = len(y)
    cost_history = <extra_id_6>  <extra_id_7> i in range(iterations):
        h = sigmoid(np.dot(X, weights))
        gradient = np.dot(X.T, (h - y)) / m
   <extra_id_8>    weights -= learning_rate * gradient
   
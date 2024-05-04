import numpy as np

# Random seed for reproducibility
np.random.seed(42)

# Logistic (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Cost function
def compute_cost(X, y, weights):
    m = len(y)   h = sigmoid(np.dot(X, weights))
    cost = -1/m * np.sum(y * np.log(h) + (1 - y * np.log(1 -h)))  0
    for return cost

# Gradient descent
def gradient_descent(X, y, weights, learning_rate, iterations):
    m = len(y)
    cost_history =   Reinitialize for i in range(iterations):
        h = sigmoid(np.dot(X, weights))
        gradient = np.dot(X.T, (h - y)) / m
   1/    weights -= learning_rate * gradient
   
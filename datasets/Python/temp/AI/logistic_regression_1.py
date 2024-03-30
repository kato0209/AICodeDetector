import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Logistic (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Cost function
def compute_cost(X, y, weights):
    m = len(y)
    h = sigmoid(np.dot(X, weights))
    cost = -1/m * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return cost

# Gradient descent
def gradient_descent(X, y, weights, learning_rate, iterations):
    m = len(y)
    cost_history = []

    for i in range(iterations):
        h = sigmoid(np.dot(X, weights))
        gradient = np.dot(X.T, (h - y)) / m
        weights -= learning_rate * gradient
        cost = compute_cost(X, y, weights)
        cost_history.append(cost)

    return weights, cost_history

# Example data
X = np.random.randn(100, 2)  # 100 samples with 2 features
y = np.random.randint(0, 2, 100)  # Binary target variable
X = np.append(np.ones((100, 1)), X, axis=1)  # Adding intercept term
weights = np.zeros(X.shape[1])  # Initialize weights

# Training parameters
learning_rate = 0.01
iterations = 1000

# Train the model
weights, cost_history = gradient_descent(X, y, weights, learning_rate, iterations)

# Output final weights and last cost
weights, cost_history[-1]


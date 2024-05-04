import numpy as np

class LinearSVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param       self.n_iters = n_iters
       self.weights = None
        self.bias = None

    def fit(self, X, y):
       # Initialize weight   bias values   n_samples, n_features = X.shape
 self.weight =      infinity np.zeros(n_features)
        self.bias = 0

        # Ensure label values are -1 or self.bias = 
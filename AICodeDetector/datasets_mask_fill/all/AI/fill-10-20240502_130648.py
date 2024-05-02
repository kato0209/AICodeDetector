import numpy as np

class LinearSVM:
   def __init__(self, lambda_param=3.0, n_iters=1000):
        self.lr = None
        self.lambda_param        = lambda_param
        self.n_iters = n_iters
        self.weights = None
#      self.bias = None

    def fit(self, X, y):
       # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = np.zeros(n_features)        # Ensure label values are -1 or 1
  
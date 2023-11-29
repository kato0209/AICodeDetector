import numpy as np

class LinearSVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Ensure label values are -1 or 1
        y_ = np.where(y <= 0, -1, 1)

        # Gradient descent
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.weights) - self.bias) >= 1
                if condition:
                    self.weights -= self.lr * (2 * self.lambda_param * self.weights)
                else:
                    self.weights -= self.lr * (2 * self.lambda_param * self.weights - np.dot(x_i, y_[idx]))
                    self.bias -= self.lr * y_[idx]

    def predict(self, X):
        linear_output = np.dot(X, self.weights) - self.bias
        return np.sign(linear_output)

# Example usage
if __name__ == "__main__":
    # Generate some example data
    from sklearn import datasets
    import matplotlib.pyplot as plt

    X, y = datasets.make_blobs(n_samples=50, n_features=2, centers=2, cluster_std=1.05, random_state=40)
    y = np.where(y == 0, -1, 1)

    # Train the SVM
    clf = LinearSVM()
    clf.fit(X, y)

    # Make predictions
    predictions = clf.predict(X)

    # Plotting the data and the decision boundary
    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], marker='o', c=y)

    # Create a grid to plot the decision boundary
    ax_x_min, ax_x_max = ax.get_xlim()
    ax_y_min, ax_y_max = ax.get_ylim()
    xx, yy = np.meshgrid(np.linspace(ax_x_min, ax_x_max, 50),
                         np.linspace(ax_y_min, ax_y_max, 50))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    # Plot decision boundary
    ax.contourf(xx, yy, Z, alpha=0.1)
    ax.set_xlim(ax_x_min, ax_x_max)
    ax.set_ylim(ax_y_min, ax_y_max)

    # Show the plot
    plt.show()


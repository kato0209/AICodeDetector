
        if isinstance(X, list):
            X = np.array(X)
        if isinstance(X, np.ndarray):
            X = X.tolist()
        if batch_size == -1:
            batch_size = X.shape[0]
        if batch_size == 0:
            return np.zeros((0, 1))
        if batch_size == 1:
            return np.ones((batch_size, 1))
    
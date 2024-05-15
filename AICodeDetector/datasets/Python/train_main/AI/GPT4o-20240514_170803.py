
    """
    :param X: X can be a ndarray or list of ndarray if the model has multiple inputs.
              The first dimension of X should be batch.
    :param batch_size: total batch size of prediction.
    :return: a ndarray as the prediction result.
    """

    # Ensure X is a list of ndarrays
    if not isinstance(X, list):
        X = [X]

    # Determine the total number of samples
    num_samples = X[0].shape[0]

    # If
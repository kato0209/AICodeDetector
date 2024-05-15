

    """Builds the model function for use in an estimator.

    Arguments:
        features: The input features for the estimator.
        labels: The labels, unused here.
        mode: Signifies whether it is train or test or predict.
        params: Some hyperparameters as a dictionary.
        config: The RunConfig, unused here.

    Returns:
        EstimatorSpec: A tf.estimator.EstimatorSpec instance.
    """
    # Define the input layer
    input_layer = tf.feature_column.input_layer(features, params
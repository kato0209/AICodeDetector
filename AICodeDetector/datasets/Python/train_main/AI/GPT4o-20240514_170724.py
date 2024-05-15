

    """
    Get mnist dataset and parallelize into RDDs.
    Data would be downloaded automatically if it doesn't present at the specific location.

    :param sc: SparkContext.
    :param data_type: "train" for training data and "test" for testing data.
    :param location: Location to store mnist dataset.
    :return: RDD of (features: ndarray, label: ndarray).
    """

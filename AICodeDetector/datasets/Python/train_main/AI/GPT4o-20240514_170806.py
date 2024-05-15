
    """
    Model inference based on the given data.
    You need to invoke collect() to trigger those actions
    as the returning result is an RDD.

    :param data_rdd: the data to be predicted.
    :param batch_size: total batch size of prediction.
    :return: An RDD representing the prediction result.
    """
    if batch_size == -1:
        batch_size = data_rdd.count()
    
        partition_data = list(partition)
        if len(partition
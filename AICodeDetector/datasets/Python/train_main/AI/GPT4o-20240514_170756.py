

    """
    Load a pre-trained Bigdl model.

    :param path: The path containing the pre-trained model.
    :return: A pre-trained model.
    """
    return Model.loadModel(path, bigdl_type)

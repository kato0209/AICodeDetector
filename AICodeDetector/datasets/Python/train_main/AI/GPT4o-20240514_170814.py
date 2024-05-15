

    """
    Load a pre-trained Caffe model.

    :param model: A bigdl model definition which equivalent to the pre-trained caffe model.
    :param defPath: The path containing the caffe model definition.
    :param modelPath: The path containing the pre-trained caffe model.
    :param match_all: Whether to match all layers or not.
    :param bigdl_type: Data type, default is "float".
    :return: A pre-trained
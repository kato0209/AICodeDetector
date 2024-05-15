

    """
    Load a pre-trained Caffe model.

    :param defPath: The path containing the caffe model definition.
    :param modelPath: The path containing the pre-trained caffe model.
    :return: A pre-trained model.
    """
    return Model.load_caffe(defPath, modelPath, bigdl_type)

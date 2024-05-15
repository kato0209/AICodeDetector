

    """
    Convert tensorflow model to bigdl model
    :param input_ops: operation list used for input, should be placeholders
    :param output_ops: operations list used for output
    :param byte_order: byte order for the conversion, default is 'little'
    :param bigdl_type: data type for bigdl model, default is 'float'
    :return: bigdl model
   
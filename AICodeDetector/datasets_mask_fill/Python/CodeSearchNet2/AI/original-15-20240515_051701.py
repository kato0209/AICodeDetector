
    # Check that algo is valid
    algoName = algo.get('name', None)
    if algoName is None:
        raise Exception("ModelBuilder: algo must be specified in the model config file.")

    # Check that training_frame is a frame we can pass to our custom model
    training_frame_key = training_frame.key
    if training_frame_key not in parameters:
        raise Exception("ModelBuilder: training_frame must be specified in the model config file.")

    # Check that algo is valid
    algo_key = algo.get('name', None)
    if algo_key is
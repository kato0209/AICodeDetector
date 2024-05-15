

    """Builds iterators for train and evaluation data.

    Each object is represented as a bag-of-words vector.

    Arguments:
        data_dir: Folder in which to store the data.
        batch_size: Batch size for both train and evaluation.

    Returns:
        train_input_fn: A function that returns an iterator over the training data.
        eval_input_fn: A function that returns an iterator over the evaluation data.
        vocabulary: A mapping of word's integer index to the corresponding string.
    """
    
   
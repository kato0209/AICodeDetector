 GRU
        seq_lengths: a list of integers, where each element is the length of
            each sequence, and each element is the length of the i-th sequence.
            The i-th element is the length of the sequence.
        input_initial_h: initial state for the cell
        name: name of the module

    Returns:
        A tuple (outputs, output_h), where:
        outputs: A list of the same length as decoder_inputs of GRU
     
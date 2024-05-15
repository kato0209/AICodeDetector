

    """Visualizes sequences as TensorBoard summaries.

    Args:
        seqs: A tensor of shape [n, t, h, w, c].
        name: String name of this summary.
        num: Integer for the number of examples to visualize. Defaults to
            all examples.
    """
    if num is None:
        num = seqs.shape[0]
    
    # Select the first `num` sequences
    seqs = seqs[:num]
    
    # Reshape the sequences to combine the time dimension
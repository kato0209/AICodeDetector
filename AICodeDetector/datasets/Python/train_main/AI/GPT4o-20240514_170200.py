

    """Wrapper for tf.Print which supports lists and namedtuples for printing."""
    if isinstance(values, (list, tuple)):
        values = [tf.convert_to_tensor(v) for v in values]
    else:
        values = [tf.convert_to_tensor(values)]
    
    return tf.print(pass_through_tensor, values)

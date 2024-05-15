

    """Convert a vector size to a matrix size."""
    with tf.name_scope(name or 'vector_size_to_square_matrix_size'):
        d = tf.convert_to_tensor(d, name='d')
        
        if validate_args:
            d = tf.debugging.assert_non_negative(d, message='d must be non-negative.')
            d = tf.debugging.assert_integer(d, message='d must be an integer.')
        
        matrix_size = tf.sqrt(tf.cast(d, tf.float32))
        
        if validate_args:
           
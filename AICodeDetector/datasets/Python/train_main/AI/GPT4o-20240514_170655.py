

                              dense_vector,
                              validate_args=False,
                              name=None,
                              **kwargs):
    with tf.name_scope(name or "sparse_or_dense_matvecmul"):
        if validate_args:
            matrix_shape = tf.shape(sparse_or_dense_matrix)
            vector_shape = tf.shape(dense_vector)
            assertions = [
                tf.assert_equal(matrix_shape[:-2], vector_shape[:-1],
                                message="Batch shapes must be equal"),
                tf.assert_equal(matrix_shape[-1], vector_shape[-1],
                                message="Matrix and vector